# Synthetic data in the disposable API spec database only.
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
count = 1000
user_attrs = SpecSeed.user.attributes.except('id')
User.insert_all!((1..count).map { |n| user_attrs.merge('id' => 100_000 + n, 'login' => "audit_bench_#{n}") })
env = SpecSeed.environment
resources = ClusterResource.where(name: CheckIpAccounting::RESOURCE_NAMES).order(:id).to_a
ipv6 = resources.find { |r| r.name == 'ipv6' }
package = ClusterResourcePackage.create!(label: 'Benchmark IPv6')
ClusterResourcePackageItem.create!(cluster_resource_package: package, cluster_resource: ipv6, value: 1)
UserClusterResourcePackage.insert_all!((1..count).map do |n|
  { user_id: 100_000 + n, environment_id: env.id, cluster_resource_package_id: package.id }
end)
UserClusterResource.insert_all!((1..count).flat_map do |n|
  [env, SpecSeed.other_environment].flat_map do |environment|
    resources.map do |r|
      { user_id: 100_000 + n, environment_id: environment.id, cluster_resource_id: r.id,
        value: environment.id == env.id && r.id == ipv6.id ? 1 : 0 }
    end
  end
end)
ClusterResourceUse.insert_all!(UserClusterResource.where('user_id > 100000').where(
  environment_id: env.id, cluster_resource_id: ipv6.id
).map do |r|
  { user_cluster_resource_id: r.id, value: 1, enabled: true, confirmed: 1,
    class_name: 'EnvironmentUserConfig', table_name: 'environment_user_configs', row_id: r.user_id }
end)
IpAddress.insert_all!((1..count).map do |n|
  { user_id: 100_000 + n, charged_environment_id: env.id, network_id: SpecSeed.network_v6.id,
    ip_addr: "2001:db8::#{n.to_s(16)}", prefix: 128, size: 1 }
end)
queries = 0
started = Process.clock_gettime(Process::CLOCK_MONOTONIC)
subscriber = ->(_name, _start, _finish, _id, payload) { queries += 1 unless payload[:name] == 'SCHEMA' }
report = ActiveSupport::Notifications.subscribed(subscriber, 'sql.active_record') { CheckIpAccounting.snapshot }
elapsed = Process.clock_gettime(Process::CLOCK_MONOTONIC) - started
raise 'unexpected discrepancies' unless report[:users].empty?
puts JSON.pretty_generate(synthetic_users: count, resources_per_user: 6, ips_per_user: 1,
                          package_assignments_per_user: 1, queries: queries,
                          elapsed_seconds: elapsed.round(3), summary: report[:summary])
