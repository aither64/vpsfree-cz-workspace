# Disposable vpsAdmin test database only. API spec helper owns setup/cleanup.
require ENV.fetch('VPSADMIN_API_SPEC_HELPER')
require ENV.fetch('IP_ACCOUNTING_SCRIPT')
SpecSeed.seed_language_if_needed!
SpecDbSetup.seed_minimal_sysconfig!
SpecDbSetup.seed_minimal_cluster_resources!
SpecSeed.bootstrap!
ClusterResourceUse.delete_all
UserClusterResourcePackage.delete_all
IpAddress.delete_all
UserClusterResource.update_all(value: 0)

Dir.mktmpdir do |dir|
  clean = File.join(dir, 'clean.json')
  raise 'clean status' unless CheckIpAccounting.main(['--output', clean]) == 0
  raise 'clean output' unless JSON.parse(File.read(clean)).fetch('users').empty?
  raise 'overwrite status' unless CheckIpAccounting.main(['--output', clean]) == 1
  raise 'arguments' unless CheckIpAccounting.main([]) == 1
  raise 'extra arguments' unless CheckIpAccounting.main(['--output', 'unused', 'extra']) == 1
  ucr = SpecSeed.user.user_cluster_resources.joins(:cluster_resource)
                .find_by!(cluster_resources: { name: 'ipv4' })
  ucr.update!(value: 1)
  affected = File.join(dir, 'affected.json')
  raise 'affected status' unless CheckIpAccounting.main(['--output', affected]) == 2
  data = JSON.parse(File.read(affected))
  raise 'affected output' unless data.fetch('summary').fetch('affected_users') == 1
end

original = CheckIpAccounting::Report.instance_method(:build)
CheckIpAccounting::Report.define_method(:build) do
  # MariaDB must reject writes even when the predicate cannot match a row.
  User.where(id: -1).update_all(login: 'audit-read-only-probe')
  original.bind_call(self)
end
begin
  CheckIpAccounting.snapshot
  raise 'database allowed a write'
rescue ActiveRecord::StatementInvalid => e
  raise unless e.message.include?('READ ONLY')
  puts 'Read-only enforcement: MariaDB rejected the injected write.'
ensure
  CheckIpAccounting::Report.define_method(:build, original)
end
raise 'transaction leaked' if ActiveRecord::Base.connection.transaction_open?
puts 'Runtime checks: clean/findings/error exit codes, JSON, and rollback passed.'
