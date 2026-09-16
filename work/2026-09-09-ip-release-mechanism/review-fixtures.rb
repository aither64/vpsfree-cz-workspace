# Run once after the final devcluster seed and creation of the two review VPSes.
# This script contains no credentials. Leave the resulting campaign untouched.
require 'json'

raise 'Review campaign already exists; inspect it instead of reseeding' if IpReleaseCampaign.exists?

admin = User.find_by!(login: 'test-admin')
primary = User.find_by!(login: 'test-user1')
secondary = User.find_by!(login: 'test-user2')
node = Node.where(role: :node).first!
location = node.location
environment = location.environment
raise 'Enable user IP ownership before creating the review VPSes' unless environment.user_ip_ownership
raise 'Create the member review VPSes first' unless [primary, secondary].all? { |u| u.vpses.exists? }

User.current = admin
UserSession.current = UserSession.create!(user: admin, auth_type: 'basic', api_ip_addr: '127.0.0.1',
                                          client_version: 'ip-release-review-fixtures')

VpsAdmin::API::TransactionSigner.unlock(ENV.fetch('REVIEW_SIGNING_PASSPHRASE'))

primary.update!(language: Language.find_by!(code: 'cs'), mailer_enabled: true)
secondary.update!(language: Language.find_by!(code: 'en'), mailer_enabled: true)
SysConfig.find_by!(category: 'webui', name: 'base_url').update!(value: 'https://webui.aitherdev.int.vpsfree.cz')

ipv6_resource = ClusterResource.find_or_create_by!(name: 'ipv6') do |resource|
  resource.assign_attributes(label: 'IPv6 address', min: 0, max: (2**128) - 1,
                             stepsize: 1, resource_type: :object, free_chain: 'Ip::Free')
end
DefaultObjectClusterResource.find_or_create_by!(environment:, class_name: 'Vps', cluster_resource: ipv6_resource) do |record|
  record.value = 0
end

ipv4 = Network.find_by!(address: '198.51.100.0', prefix: 24)
network_chain, ipv6 = Network.register!(
  { label: 'Review public IPv6', address: '2001:db8:106::', prefix: 48,
    ip_version: 6, role: :public_access, managed: true, split_access: :no_access,
    split_prefix: 64, purpose: :any, primary_location: location },
  { add_ips: false }
)
network_deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + 180
loop do
  network_chain.reload
  break if network_chain.state == 'done'
  raise "IPv6 network registration failed: #{network_chain.state}" unless %w[staged queued].include?(network_chain.state)
  raise 'IPv6 network registration timed out' if Process.clock_gettime(Process::CLOCK_MONOTONIC) >= network_deadline
  sleep 2
end
LocationNetwork.create!(network: ipv6, location:, primary: true, priority: 20, autopick: true, userpick: true)
location.update!(has_ipv6: true)
[primary, secondary].each do |user|
  allowance = UserClusterResource.find_or_initialize_by(user:, environment:,
                                                        cluster_resource: ipv6_resource)
  allowance.value = 16 * (2**(128 - ipv6.split_prefix))
  allowance.save!
end

private_network = Network.find_by!(address: '10.106.0.0', prefix: 24)

def wait_review_chain(chain)
  return unless chain

  deadline = Process.clock_gettime(Process::CLOCK_MONOTONIC) + 240
  loop do
    chain.reload
    return if chain.state == 'done'
    raise "Chain #{chain.id} failed: #{chain.state}" unless %w[staged queued].include?(chain.state)
    raise "Chain #{chain.id} timed out" if Process.clock_gettime(Process::CLOCK_MONOTONIC) >= deadline

    sleep 2
  end
end

private_resource = ClusterResource.find_by!(name: 'ipv4_private')
[primary, secondary].each do |user|
  user.user_cluster_resources.find_by!(environment:, cluster_resource: private_resource).update!(value: 16)
end

primary_v4 = ipv4.add_ips(2, user: primary, environment:)
primary_v6 = ipv6.add_ips(1, user: primary, environment:)
primary_private = [IpAddress.register(IPAddress.parse('10.106.0.20/32'),
                                    network: private_network, user: primary, environment:, prefix: 32, size: 1)]
secondary_v4 = ipv4.add_ips(1, user: secondary, environment:)
selected = primary_v4 + primary_v6 + primary_private + secondary_v4

# Produce real assignment history through the same chains as the public API.
history_ip = primary_v4.first
netif = primary.vpses.order(:id).first!.network_interfaces.first!
assignment, = TransactionChains::NetworkInterface::AddRoute.fire(
  netif, [history_ip], actor: primary, host_addrs: history_ip.host_ip_addresses.to_a
)
wait_review_chain(assignment)
raise 'Fixture was not assigned' unless history_ip.reload.network_interface_id == netif.id
unassignment, = TransactionChains::NetworkInterface::DelRoute.fire(netif, [history_ip], actor: primary)
wait_review_chain(unassignment)
history = history_ip.ip_address_assignments.order(:id).last!
raise 'Missing completed assignment history' unless history.from_date && history.to_date &&
                                                  history.assigned_by_chain_id == assignment.id &&
                                                  history.unassigned_by_chain_id == unassignment.id

ptr_host = primary_v4.last.host_ip_addresses.first!
raise 'Public IPv4 network needs a reverse zone' unless ptr_host.ip_address.reverse_dns_zone
ptr_chain, = TransactionChains::DnsZone::SetReverseRecord.fire(ptr_host, 'review-ip.example.test.', actor: admin)
wait_review_chain(ptr_chain)
raise 'Review PTR missing' unless ptr_host.reload.reverse_dns_record&.content == 'review-ip.example.test.'

campaign = IpReleaseCampaign.create_selected!(
  ids: selected.map(&:id), actor: admin, deadline: Time.now + 7.days, allow_keep: true
)
raise 'Expected fresh campaign #1' unless campaign.id == 1
raise 'Prepared campaign must remain unsent' if campaign.ip_release_requests.any? { |r| r.ip_release_request_notices.exists? }
raise 'Prepared campaign has an attempt' if campaign.ip_release_attempts.exists?
raise 'Prepared IPs must be eligible' unless campaign.ip_release_request_addresses.all? { |item| item.protection == 'eligible' }
raise 'Prepared fixture count differs' unless selected.length == 5
raise 'Prepared IPs must be unassigned' unless selected.all? { |ip| ip.reload.free? }
[primary, secondary].each do |user|
  config = user.environment_user_configs.find_by!(environment:)
  %i[ipv4 ipv4_private ipv6].each do |resource|
    owned = IpAddress.where(user: user, charged_environment: environment).select { |ip| ip.cluster_resource == resource }
    raise "User #{user.id} #{resource} quota differs from ownership" unless config.public_send(resource) == owned.sum { |ip| ip.size.to_i }
  end
end

def describe_ips(ips)
  ips.map do |ip|
    { id: ip.id, address: ip.to_s, owner_id: ip.user_id,
      charge_environment_id: ip.charged_environment_id, resource: ip.cluster_resource }
  end
end

puts 'REVIEW_INVENTORY=' + JSON.generate(
  campaign_id: campaign.id, request_ids: campaign.ip_release_requests.order(:user_id).pluck(:id),
  deadline: campaign.deadline.iso8601, primary_user_id: primary.id, secondary_user_id: secondary.id,
  primary_ipv4: describe_ips(primary_v4), primary_ipv6: describe_ips(primary_v6),
  primary_private_ipv4: describe_ips(primary_private), secondary_ipv4: describe_ips(secondary_v4),
  ptr_host_id: ptr_host.id, ptr_address: primary_v4.last.to_s,
  history_address: history_ip.to_s, history_assignment_id: history.id,
  assignment_chain_id: assignment.id, unassignment_chain_id: unassignment.id,
  vpses: [primary, secondary].flat_map { |u| u.vpses.map { |vps| { id: vps.id, user_id: u.id, hostname: vps.hostname } } }
)
