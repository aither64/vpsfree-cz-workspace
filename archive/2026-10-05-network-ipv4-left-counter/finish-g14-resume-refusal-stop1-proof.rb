# frozen_string_literal: true

require 'json'
require 'digest'
require 'time'
require '/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source/cluster/lib/kb_runtime'

tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'
private_root = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14'
context = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14-public-continuation1/resume-refusal-stop-context'
state = KbRuntime::State.new(File.join(private_root, 'campaign/state'), 'same-slug')
engine = KbRuntime::Engine.new(state: state, software: nil, controller: nil)
before = JSON.parse(File.binread(File.join(tracking, 'finish-g14-resume-key-observation1.json')))
disks_before = JSON.parse(File.binread(File.join(tracking, 'finish-continuation-g14-retention2.json'))).fetch('snapshot').fetch('disks_retained')
native_bytes = state.file(File.join(context, 'result.json'))
native = JSON.parse(native_bytes)
raise 'public stop not successful' unless native['complete'] == true && native['exit_code'] == 0 && native['cancel_reason'].nil? && native['wrapper_failure'].nil?
raise 'wrong native phase' unless native['phase'] == 'separate-public-stop-after-resume-trust-refusal' && native['generator'] == before.fetch('generator')
evidence = native.fetch('evidence_sha256').to_h do |name, expected|
  raise 'unsafe native evidence name' unless /\A[a-z0-9_.-]+\z/.match?(name)
  bytes = state.file(File.join(context, name), limit: 16 * 1024 * 1024)
  raise 'native evidence changed' unless Digest::SHA256.hexdigest(bytes) == expected
  [name, { 'sha256' => expected, 'bytes' => bytes.bytesize }]
end
absent = lambda do |path|
  File.lstat(path)
  false
rescue Errno::ENOENT
  true
end
snapshot = state.transaction(create: false, wait: false) do
  identity = state.identity
  launch = engine.launch
  old = before.fetch('snapshot')
  %w[instance_id run_id artifact_id artifact_sha256].each do |key|
    raise 'current identity changed' unless launch.fetch(key) == old.fetch(key)
  end
  record = engine.process_record(launch)
  raise 'stop lacks complete exit proof' unless engine.phase.fetch('phase') == 'stopped' && record.fetch('complete') == true && engine.gone?(launch)
  raise 'stopped run remains ready' if engine.ready?(launch)
  children = record.fetch('children')
  old.fetch('children').each do |child|
    raise 'retained child disappeared from receipt' unless children.any? { |now| now.values_at('pid', 'start_ticks') == child.values_at('pid', 'start_ticks') }
  end
  raise 'runner not positively gone' unless KbRuntime::ProcessIdentity.gone?(record.fetch('runner'))
  raise 'recorded child not positively gone' unless children.all? { |child| KbRuntime::ProcessIdentity.gone?(child) }
  claim_path = File.join(engine.resources.root, "#{identity.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  socket_path = engine.resources.socket_dir(identity.fetch('instance_id'), launch.fetch('run_id'))
  raise 'socket derivation changed' unless socket_path == launch.fetch('socket_dir')
  raise 'own claim remains' unless absent.call(claim_path)
  raise 'socket namespace remains' unless absent.call(socket_path)
  disks = disks_before.to_h do |name, previous|
    stat = File.lstat(File.join(state.directory, 'disks', name))
    raise 'unsafe or changed retained disk' unless stat.file? && !stat.symlink? && stat.uid == Process.uid &&
      [stat.dev, stat.ino, stat.size] == previous.values_at('device', 'inode', 'bytes')
    [name, { 'device' => stat.dev, 'inode' => stat.ino, 'bytes' => stat.size, 'allocated_bytes' => stat.blocks * 512 }]
  end
  known_sha = Digest::SHA256.hexdigest(state.file(state.path('credentials') + '/known_hosts'))
  raise 'retained trust changed' unless known_sha == old.fetch('known_hosts_sha256')
  { 'at' => Time.now.utc.iso8601, 'phase' => 'stopped', 'ready' => false,
    'instance_id' => launch.fetch('instance_id'), 'run_id' => launch.fetch('run_id'),
    'artifact_id' => launch.fetch('artifact_id'), 'artifact_sha256' => launch.fetch('artifact_sha256'),
    'processes_complete' => true, 'recorded_children' => children.size, 'runner_positively_gone' => true,
    'all_recorded_children_positively_gone' => true, 'own_claim_absent' => true, 'owned_socket_namespace_absent' => true,
    'disks_retained' => disks, 'known_hosts_sha256' => known_sha, 'known_hosts_unchanged' => true }
end
attempt_path = File.join(private_root, 'campaign/receipts/runtime-smoke-attempt.json')
attempt_hash = Digest::SHA256.hexdigest(state.file(attempt_path))
raise 'original failed attempt changed' unless attempt_hash == before.fetch('original_failed_attempt_sha256')
raise 'original campaign completion appeared' unless absent.call(File.join(private_root, 'campaign/receipts/runtime-smoke.json'))
proof = { 'schema' => 1, 'generator' => before.fetch('generator'), 'phase' => native.fetch('phase'),
  'native_exit_code' => 0, 'wrapper_complete' => true, 'cancel_reason' => nil,
  'started_at' => native.fetch('started_at'), 'finished_at' => native.fetch('finished_at'),
  'native_result_sha256' => Digest::SHA256.hexdigest(native_bytes), 'native_evidence' => evidence,
  'original_failed_attempt_sha256' => attempt_hash, 'original_failed_attempt_unchanged' => true,
  'original_completed_receipt_absent' => true, 'snapshot' => snapshot,
  'limits' => 'Bounded proof of this separately selected exact public stop and complete recorded exit/own claim/socket retirement. Disks, trust and failures retained. No reset/disk deletion/unit retirement, readiness repair, retry, completed qualification, capture or older-state cleanup.' }
output = File.join(tracking, 'finish-g14-resume-refusal-stop1-proof.json')
File.open(output, File::WRONLY | File::CREAT | File::EXCL, 0o644) { |stream| stream.write(JSON.pretty_generate(proof) + "\n") }
puts JSON.generate('proof' => output, 'public_stop_exit' => 0, 'stopped' => true, 'complete_exit' => true,
  'recorded_children_gone' => snapshot.fetch('recorded_children'), 'own_claim_absent' => true,
  'socket_namespace_absent' => true, 'disks_and_trust_retained' => true)
