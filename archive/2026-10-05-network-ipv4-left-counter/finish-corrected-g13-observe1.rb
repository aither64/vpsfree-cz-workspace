require 'json'
require 'digest'
require_relative './cluster/lib/kb_state'
require_relative './cluster/lib/kb_process'
root, mode, evidence, cgroup = ARGV
state = KbRuntime::State.new(root, 'same-slug')
result = state.transaction(wait: false) do
  identity = state.identity
  phase = state.read(state.path('phase.json'))
  instance = 'b93cead9-2548-4754-9a37-349a5c4ddffb'
  run = 'af01bfda-d56c-4960-bfbf-39a6ed0d834c'
  raise 'instance/run differs' unless identity['instance_id'] == instance && phase['run_id'] == run
  lp = state.path("launch-#{run}.json")
  launch = state.read(lp)
  raise 'launch differs' unless launch['instance_id'] == instance && launch['run_id'] == run && launch['state_root'] == root && launch['owner_uid'] == Process.uid && launch.dig('source', 'revision') == '9c551c6ad68650d12f3d8e91f8bf33a76e2ffe0e' && launch['artifact_id'] == 'e3a0ed6d-f60a-4c30-a21e-f0dc8b6eddbd'
  pp = state.path("processes-#{run}.json")
  processes = state.read(pp)
  raise 'process record differs' unless %w[instance_id run_id artifact_id artifact_sha256].all? { |key| processes[key] == launch[key] }
  tuples = [processes.fetch('runner'), *processes.fetch('children')]
  live = tuples.map { |tuple| KbRuntime::ProcessIdentity.matches?(tuple) }
  gone = tuples.map { |tuple| KbRuntime::ProcessIdentity.gone?(tuple) }
  groups = tuples.each_with_index.filter_map { |tuple, i| live[i] ? File.read("/proc/#{tuple.fetch('pid')}/cgroup").strip : nil }.uniq
  runner_live = KbRuntime::ProcessIdentity.runner_matches?(processes.fetch('runner'), launch)
  if mode == 'before'
    raise 'retained ready live owner not proved' unless phase['phase'] == 'ready' && runner_live && processes['complete'] == false
    raise 'recorded named tuple changed or foreign' unless tuples.each_index.all? { |i| live[i] || gone[i] }
    raise 'retained containing cgroup differs' unless groups == [cgroup]
  elsif mode == 'after'
    raise 'shutdown not complete/stopped' unless phase['phase'] == 'stopped' && processes['complete'] == true && gone.all?
    raise 'ready marker remains' if File.exist?(state.path("ready-#{run}.json"))
    raise 'socket namespace remains' if File.exist?(launch['socket_dir'])
  else
    raise 'unknown observation mode'
  end
  safe_launch = launch.slice('schema', 'instance_id', 'run_id', 'artifact_id', 'artifact_sha256', 'state_root', 'slug', 'owner_uid', 'socket_dir', 'source', 'runner_identity', 'boot_id')
  saved = { 'identity' => identity, 'phase' => phase, 'launch' => safe_launch, 'processes' => processes, 'launch_sha256' => Digest::SHA256.hexdigest(state.file(lp)), 'process_sha256' => Digest::SHA256.hexdigest(state.file(pp)) }
  File.open(evidence, File::WRONLY | File::CREAT | File::EXCL | File::NOFOLLOW, 0o600) { |file| file.write(JSON.pretty_generate(saved) + "\n") }
  { 'instance_id' => instance, 'run_id' => run, 'artifact_id' => launch['artifact_id'], 'retained_source_revision' => launch.dig('source','revision'), 'phase' => phase['phase'], 'complete' => processes['complete'], 'recorded_child_count' => processes['children'].size, 'runner_matches_launch' => runner_live, 'all_named_tuples_matching_or_gone' => tuples.each_index.all? { |i| live[i] || gone[i] }, 'all_named_tuples_gone' => gone.all?, 'live_cgroups' => groups, 'private_evidence' => evidence, 'evidence_sha256' => Digest::SHA256.file(evidence).hexdigest }
end
puts JSON.generate(result)
