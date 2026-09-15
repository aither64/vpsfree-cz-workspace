# Run once after the final devcluster seed and creation of the two review VPSes.
# This script contains no credentials. Mail and release smoke tests use other IPs.
require 'json'

label = 'Unassigned IP review'
raise 'Review campaign already exists; inspect it instead of reseeding' if IpReleaseCampaign.exists?(label:)

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

primary_v4 = ipv4.add_ips(6, user: primary, environment:)
primary_v6 = ipv6.add_ips(2, user: primary, environment:)
secondary_control = ipv4.add_ips(1, user: secondary, environment:)
smoke_v4 = ipv4.add_ips(2, user: secondary, environment:)
smoke_v6 = ipv6.add_ips(1, user: secondary, environment:)

campaign = IpReleaseCampaign.create_selected!(
  ids: (primary_v4.first(3) + primary_v6.first(1) + secondary_control).map(&:id), actor: admin,
  label:, deadline: Time.now + 7.days, allow_keep: true
)

raise 'Prepared campaign must remain unsent' if campaign.ip_release_requests.any? { |r| r.ip_release_request_notices.exists? }
raise 'Primary fixture count differs' unless primary_v4.length == 6 && primary_v6.length == 2
raise 'Prepared IPs must be unassigned' unless (primary_v4 + primary_v6).all?(&:free?)
raise 'Prepared ownership differs' unless (primary_v4 + primary_v6).all? { |ip| ip.user_id == primary.id && ip.charged_environment_id == environment.id }

def describe_ips(ips)
  ips.map { |ip| { id: ip.id, address: ip.to_s, owner_id: ip.user_id, charge_environment_id: ip.charged_environment_id } }
end

puts JSON.pretty_generate(
  campaign_id: campaign.id, request_ids: campaign.ip_release_requests.pluck(:id),
  deadline: campaign.deadline.iso8601, primary_user_id: primary.id, secondary_user_id: secondary.id,
  primary_ipv4: describe_ips(primary_v4), primary_ipv6: describe_ips(primary_v6),
  secondary_control: describe_ips(secondary_control), smoke_ipv4: describe_ips(smoke_v4), smoke_ipv6: describe_ips(smoke_v6),
  ptr_host_id: primary_v4.first.host_ip_addresses.first!.id,
  smoke_ptr_host_id: smoke_v4.first.host_ip_addresses.first!.id,
  vpses: [primary, secondary].flat_map { |u| u.vpses.map { |vps| { id: vps.id, user_id: u.id, hostname: vps.hostname } } }
)
