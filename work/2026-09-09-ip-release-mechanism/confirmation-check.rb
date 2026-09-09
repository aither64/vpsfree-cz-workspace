# Cross-component check: run from api/ with API gems plus libosctl available.
require 'spec_helper'
require 'libosctl'

root = ENV.fetch('VPSADMIN_CHECK_ROOT')
$LOAD_PATH.unshift(File.join(root, 'libnodectld/lib'))
require 'nodectld/confirmations'
require 'nodectld/command'
require 'nodectld/db'
OsCtl::Lib::Logger.setup(:none)

RSpec.describe IpReleaseCampaign do
  around { |example| with_current_context { example.run } }
  before { unlock_transaction_signer! }

  def finish_chain(chain, direction:, success:)
    Transaction.where(transaction_chain: chain).update_all(status: success ? 1 : 0)
    raw = ActiveRecord::Base.connection.raw_connection
    previous_options = raw.query_options.dup
    raw.query_options[:as] = :hash
    db = NodeCtld::DbTransaction.new(raw)
    NodeCtld::Confirmations.new(chain.id).run(db, direction)
    command = NodeCtld::Command.allocate
    command.instance_variable_set(:@chain, { id: chain.id, state: direction == :rollback ? 3 : 1 })
    command.instance_variable_set(:@status, success ? :ok : :failed)
    command.instance_variable_set(:@trans, { 'id' => 0 })
    command.send(:close_chain, db)
  ensure
    raw.query_options.replace(previous_options) if raw && previous_options
  end

  [[:execute, true], [:execute, false], [:rollback, true]].each do |direction, success|
    it "preserves ownership safely through #{direction}, success=#{success}" do
      ensure_available_node_status!(SpecSeed.node)
      ip = create_ip_address!(user: SpecSeed.user)
      reverse_zone = create_reverse_dns_zone!
      ip.update!(charged_environment: SpecSeed.environment, reverse_dns_zone: reverse_zone)
      host = ip.host_ip_addresses.first
      host.update!(user_created: true)
      server = create_dns_server!(node: SpecSeed.node)
      zone = create_dns_zone!(user: SpecSeed.user, source: :internal_source)
      [zone, reverse_zone].each do |z|
        create_dns_server_zone!(dns_zone: z, dns_server: server, zone_type: :primary_type)
      end
      ptr = create_dns_record!(dns_zone: reverse_zone, name: '25', record_type: 'PTR', content: 'kept.example.test.')
      host.update!(reverse_dns_record: ptr)
      transfer = create_dns_zone_transfer!(dns_zone: zone, host_ip_address: host, peer_type: :secondary_type)
      config = SpecSeed.user.environment_user_configs.find_by!(environment: SpecSeed.environment)
      usage = config.ipv4
      campaign = described_class.create_selected!(ids: [ip.id], actor: SpecSeed.admin,
                                                  label: 'Confirmation check', deadline: Time.now + 604_800)
      campaign.release!(actor: SpecSeed.admin)
      item = campaign.ip_release_request_addresses.first
      expect(item.last_result).to eq('releasing'), item.last_error
      expect(ip.reload.user_id).to eq(SpecSeed.user.id)
      expect(config.reload.ipv4).to eq(usage)
      expect(item.released_at).to be_nil
      expect(ip).to be_locked

      finish_chain(item.release_chain, direction:, success:)
      completed = direction == :execute && success
      expect(ip.reload.user_id).to eq(completed ? nil : SpecSeed.user.id)
      expect(config.reload.ipv4).to eq(usage - (completed ? ip.size : 0))
      expect(item.reload.released_at.present?).to eq(completed)
      expect(item.active_ip_address_id).to eq(completed ? nil : ip.id)
      expect(ip).not_to be_locked
      expect(DnsZoneTransfer.exists?(transfer.id)).to eq(!completed)
      expect(DnsRecord.exists?(ptr.id)).to eq(!completed)
      expect(HostIpAddress.exists?(host.id)).to eq(!completed)

      unless completed
        expect(host.reload.reverse_dns_record_id).to eq(ptr.id)
        expect(item.last_result).to eq('failed')
        campaign.release!(actor: SpecSeed.admin)
        expect(item.reload.last_result).to eq('releasing'), item.last_error
        finish_chain(item.release_chain, direction: :execute, success: true)
      end

      expect(ip.reload.user_id).to be_nil
      expect(config.reload.ipv4).to eq(usage - ip.size)
      expect(item.reload.released_by_id).to eq(SpecSeed.admin.id)
      expect(item.ip_release_request.user_id).to eq(SpecSeed.user.id)
      expect(item.release_chain.user_id).to eq(SpecSeed.admin.id)
      expect(item.released_at).not_to be_nil
      campaign.release!(actor: SpecSeed.admin)
      expect(config.reload.ipv4).to eq(usage - ip.size)
    end
  end
end
