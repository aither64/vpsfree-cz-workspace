require 'json'
require 'digest'
require 'time'
require '/nix/store/j665iwsbv4zgaf1iaxag7h7881rrlh2q-source/cluster/lib/kb_runtime'
root = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-working1/campaign2'
s = KbRuntime::State.new(File.join(root, 'state'), 'same-slug')
e = KbRuntime::Engine.new(state: s, software: nil, controller: nil)
expected = JSON.parse(File.read(File.join(__dir__, 'finish-working-delivery-services-qemu-disposition1.json')))
failure = File.join(root, 'receipts/runtime-smoke-attempt.json')
failure_hash = Digest::SHA256.file(failure).hexdigest
raise 'failed attempt changed' unless failure_hash == '7e917035b7ae109b8b53bf1edfbc785469a62943e14da1f1c63891b3c13f8501'
raise 'completed receipt appeared' if File.exist?(File.join(root, 'receipts/runtime-smoke.json'))
absent = ->(path) { !(File.exist?(path) || File.symlink?(path)) }
snapshot = s.transaction(create: false, wait: false) do
  launch = e.launch
  %w[instance_id run_id artifact_id].each { |k| raise 'foreign run' unless launch.fetch(k) == expected.fetch(k) }
  proof = e.process_record(launch)
  raise 'not stopped' unless e.phase.fetch('phase') == 'stopped' && proof.fetch('complete') == true && e.gone?(launch)
  raise 'unexpected readiness' if e.ready?(launch)
  claim = File.join(e.resources.root, "#{launch.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  raise 'claim/socket remains' unless absent.call(claim) && absent.call(launch.fetch('socket_dir'))
  disks = %w[services-root.img node1-tank.img].to_h do |name|
    st = File.lstat(File.join(s.path('disks'), name))
    raise 'unsafe disk' unless st.file? && !st.symlink? && st.uid == Process.uid && st.size == 8 * 1024**3
    [name, { 'device' => st.dev, 'inode' => st.ino, 'bytes' => st.size, 'allocated_bytes' => st.blocks * 512 }]
  end
  { 'phase' => 'stopped', 'ready' => false, **launch.slice('instance_id', 'run_id', 'artifact_id', 'artifact_sha256'),
    'processes_complete' => true, 'runner_positively_gone' => true, 'all_recorded_children_positively_gone' => true,
    'recorded_children' => proof.fetch('children').size, 'own_claim_absent' => true, 'owned_socket_namespace_absent' => true,
    'disks_retained' => disks, 'known_hosts_sha256' => Digest::SHA256.hexdigest(s.file(File.join(s.path('credentials'), 'known_hosts'))),
    'native_process_receipt_sha256' => Digest::SHA256.hexdigest(s.file(s.path("processes-#{launch.fetch('run_id')}.json"))) }
end
puts JSON.generate({ 'schema' => 1, 'at' => Time.now.utc.iso8601, 'generator' => expected.fetch('source'),
  'snapshot' => snapshot, 'original_failed_attempt_sha256' => failure_hash,
  'original_failed_attempt_unchanged' => true, 'completed_runtime_receipt_absent' => true })
