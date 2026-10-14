# frozen_string_literal: true
require 'json'
require 'digest'
require 'time'
tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'
prior = JSON.parse(File.binread(File.join(tracking, 'finish-g14-resume-refusal-stop1-proof.json'))).fetch('snapshot')
accepted = JSON.parse(File.binread(File.join(tracking, 'finish-virtiofs-package-realize1-acceptance.json')))
raise 'old generator differs' unless accepted.fetch('generator') == '725c325e8b4971931e5d16df86bafa8584358ecb'
require File.join(accepted.fetch('source'), 'cluster/lib/kb_runtime')
campaign = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14/campaign'
reader = KbRuntime::State.new(campaign, 'campaign')
failed = Digest::SHA256.hexdigest(reader.file(File.join(campaign, 'receipts/runtime-smoke-attempt.json')))
raise 'failed attempt changed' unless failed == 'f5a7f1c287912b1beb6d1608d4e66c670599265e571dd9786317126ad5954125'
raise 'completed runtime receipt appeared' if File.exist?(File.join(campaign, 'receipts/runtime-smoke.json'))
state = KbRuntime::State.new(File.join(campaign, 'state'), 'same-slug')
engine = KbRuntime::Engine.new(state: state, software: nil, controller: nil)
absent = lambda do |path|
  File.lstat(path)
  false
rescue Errno::ENOENT
  true
end
snapshot = state.transaction(create: false, wait: false) do
  identity = state.identity
  launch = engine.launch
  %w[instance_id run_id artifact_id artifact_sha256].each do |k|
    raise 'retained identity changed' unless launch.fetch(k) == prior.fetch(k)
  end
  raise 'instance differs' unless identity.fetch('instance_id') == launch.fetch('instance_id')
  record = engine.process_record(launch)
  children = record.fetch('children')
  raise 'not fully stopped' unless engine.phase.fetch('phase') == 'stopped' && record.fetch('complete') == true && engine.gone?(launch)
  raise 'runner still present' unless KbRuntime::ProcessIdentity.gone?(record.fetch('runner'))
  raise 'child still present' unless children.all? { |c| KbRuntime::ProcessIdentity.gone?(c) }
  raise 'child history regressed' unless children.size >= prior.fetch('recorded_children')
  raise 'ready despite stop' if engine.ready?(launch)
  claim = File.join(engine.resources.root, "#{identity.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  socket = engine.resources.socket_dir(identity.fetch('instance_id'), launch.fetch('run_id'))
  raise 'socket differs' unless socket == launch.fetch('socket_dir')
  raise 'claim or socket remains' unless absent.call(claim) && absent.call(socket)
  disks = prior.fetch('disks_retained').to_h do |name, previous|
    s = File.lstat(File.join(state.directory, 'disks', name))
    raise 'retained disk changed' unless s.file? && !s.symlink? && s.uid == Process.uid && [s.dev,s.ino,s.size] == previous.values_at('device','inode','bytes')
    [name, {'device'=>s.dev,'inode'=>s.ino,'bytes'=>s.size,'allocated_bytes'=>s.blocks*512}]
  end
  trust = Digest::SHA256.hexdigest(state.file(File.join(state.directory, 'credentials', 'known_hosts')))
  raise 'retained trust changed' unless trust == prior.fetch('known_hosts_sha256')
  {'phase'=>'stopped','ready'=>false,'instance_id'=>launch.fetch('instance_id'),'run_id'=>launch.fetch('run_id'),'artifact_id'=>launch.fetch('artifact_id'),'artifact_sha256'=>launch.fetch('artifact_sha256'),'processes_complete'=>true,'recorded_children'=>children.size,'runner_positively_gone'=>true,'all_recorded_children_positively_gone'=>true,'own_claim_absent'=>true,'owned_socket_namespace_absent'=>true,'disks_retained'=>disks,'known_hosts_sha256'=>trust,'known_hosts_unchanged'=>true}
end
proof = {'schema'=>1,'at'=>Time.now.utc.iso8601,'generator'=>accepted.fetch('generator'),'scope'=>'Read-only stopped G14 identity/process/namespace/disk/trust proof; no reset, guest, reuse, new artifact or qualification operation','snapshot'=>snapshot,'original_failed_attempt_sha256'=>failed,'original_failed_attempt_unchanged'=>true,'completed_runtime_receipt_absent'=>true,'operation_admission'=>false}
output = File.join(tracking, 'finish-working-delivery-g14-retention2.json')
File.open(output, File::WRONLY|File::CREAT|File::EXCL, 0644) { |f| f.write(JSON.pretty_generate(proof)+"\n") }
puts JSON.generate({'proof'=>output,'stopped'=>true,'recorded_children'=>snapshot.fetch('recorded_children'),'mutation'=>false})
