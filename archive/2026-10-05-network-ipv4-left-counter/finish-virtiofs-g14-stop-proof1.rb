# frozen_string_literal: true

require 'json'
require 'digest'
require 'time'

tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'
private_root = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14'
accepted = JSON.parse(File.binread(File.join(tracking, 'finish-virtiofs-package-realize1-acceptance.json')))
before = JSON.parse(File.binread(File.join(tracking, 'finish-virtiofs-runtime-failure-proof1.json')))
generator = '725c325e8b4971931e5d16df86bafa8584358ecb'
raise 'source differs' unless accepted['accepted'] && accepted['generator'] == generator && before['generator'] == generator
require File.join(accepted.fetch('source'), 'cluster/lib/kb_runtime')

campaign = File.join(private_root, 'campaign')
reader = KbRuntime::State.new(campaign, 'campaign')
result_path = File.join(private_root, 'final-stop-context/result.json')
result_bytes = reader.file(result_path)
raise 'native result changed' unless Digest::SHA256.hexdigest(result_bytes) == '91647a24b1a1d2c94b6494e637237a6cc9c4917a3957702341d4a408b3b76ed1'
result = JSON.parse(result_bytes)
raise 'native stop was not successful' unless result['complete'] == true && result['exit_code'] == 0 && result['cancel_reason'].nil?
native_evidence = result.fetch('evidence_sha256').to_h do |name, hash|
  raise 'unsafe evidence name' unless /\A[a-z0-9_.-]+\z/.match?(name)
  path = File.join(private_root, 'final-stop-context', name)
  raise 'native evidence changed' unless Digest::SHA256.file(path).hexdigest == hash
  [name, { 'sha256' => hash, 'bytes' => File.size(path) }]
end
attempt_path = File.join(campaign, 'receipts/runtime-smoke-attempt.json')
attempt_hash = Digest::SHA256.hexdigest(reader.file(attempt_path))
raise 'failed attempt changed' unless attempt_hash == before.fetch('attempt_sha256')
raise 'completed qualification appeared' if File.exist?(File.join(campaign, 'receipts/runtime-smoke.json'))

absent = lambda do |path|
  File.lstat(path)
  false
rescue Errno::ENOENT
  true
end
state = KbRuntime::State.new(File.join(campaign, 'state'), 'same-slug')
engine = KbRuntime::Engine.new(state: state, software: nil, controller: nil)
snapshot = state.transaction(create: false, wait: false) do
  identity = state.identity
  launch = engine.launch
  previous = before.fetch('retained_snapshot')
  %w[instance_id run_id artifact_id artifact_sha256].each do |key|
    raise 'retained identity changed' unless launch.fetch(key) == previous.fetch(key)
  end
  raise 'instance changed' unless identity.fetch('instance_id') == launch.fetch('instance_id')
  phase = engine.phase.fetch('phase')
  processes = engine.process_record(launch)
  children = processes.fetch('children')
  raise 'stop phase not complete' unless phase == 'stopped' && processes.fetch('complete') == true && engine.gone?(launch)
  raise 'recorded descendant count regressed' unless children.size >= previous.fetch('recorded_children')
  raise 'runner not positively gone' unless KbRuntime::ProcessIdentity.gone?(processes.fetch('runner'))
  raise 'recorded child not positively gone' unless children.all? { |record| KbRuntime::ProcessIdentity.gone?(record) }
  claim_path = File.join(engine.resources.root, "#{identity.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  socket_path = engine.resources.socket_dir(identity.fetch('instance_id'), launch.fetch('run_id'))
  raise 'socket derivation changed' unless socket_path == launch.fetch('socket_dir')
  raise 'claim remains' unless absent.call(claim_path)
  raise 'owned namespace remains' unless absent.call(socket_path)
  raise 'stopped run still ready' if engine.ready?(launch)
  disks = previous.fetch('disks').to_h do |name, facts|
    stat = File.lstat(File.join(state.directory, 'disks', name))
    raise 'unsafe or changed retained disk' unless stat.file? && !stat.symlink? && stat.uid == Process.uid &&
      [stat.dev, stat.ino, stat.size] == facts.values_at('device', 'inode', 'bytes')
    [name, { 'device' => stat.dev, 'inode' => stat.ino, 'bytes' => stat.size, 'allocated_bytes' => stat.blocks * 512 }]
  end
  { 'observed_at' => Time.now.utc.iso8601, 'phase' => phase, 'ready' => false,
    'instance_id' => launch.fetch('instance_id'), 'run_id' => launch.fetch('run_id'),
    'artifact_id' => launch.fetch('artifact_id'), 'artifact_sha256' => launch.fetch('artifact_sha256'),
    'processes_complete' => true, 'recorded_children' => children.size,
    'runner_positively_gone' => true, 'all_recorded_children_positively_gone' => true,
    'own_claim_absent' => true, 'own_claim_path' => claim_path,
    'owned_socket_namespace_absent' => true, 'socket_directory' => socket_path,
    'disks_retained' => disks, 'stopped_certified' => true, 'owned_socket_cleanup_certified' => true }
end
proof = { 'schema' => 1, 'generator' => generator, 'phase' => 'separate-final-public-stop',
  'native_exit_code' => 0, 'wrapper_complete' => true, 'accepted' => true,
  'native_result_sha256' => Digest::SHA256.hexdigest(result_bytes), 'native_evidence' => native_evidence,
  'started_at' => result.fetch('started_at'), 'finished_at' => result.fetch('finished_at'),
  'failed_runtime_attempt_unchanged' => true, 'failed_attempt_sha256' => attempt_hash,
  'completed_runtime_receipt_absent' => true, 'snapshot' => snapshot,
  'limits' => 'Separate public shutdown of the newly owned G14 run. No reset, disk deletion, unit retirement, qualification replay, resume, full runtime acceptance or media proof. Older retained campaigns are untouched.' }
output = File.join(tracking, 'finish-virtiofs-g14-stop-proof1.json')
File.open(output, File::WRONLY | File::CREAT | File::EXCL, 0o644) { |stream| stream.write(JSON.pretty_generate(proof) + "\n") }
puts JSON.generate(proof.slice('generator', 'phase', 'native_exit_code', 'accepted').merge('proof' => output, 'stopped' => true, 'recorded_children' => snapshot.fetch('recorded_children')))
