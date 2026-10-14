# frozen_string_literal: true

# Read-only evidence projection. Private campaign inputs never leave their root.
require 'json'
require 'digest'
require 'time'

tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'
private_root = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14'
accepted = JSON.parse(File.binread(File.join(tracking, 'finish-virtiofs-package-realize1-acceptance.json')))
generator = '725c325e8b4971931e5d16df86bafa8584358ecb'
raise 'package selection differs' unless accepted['accepted'] == true && accepted['generator'] == generator
require File.join(accepted.fetch('source'), 'cluster/lib/kb_runtime')

campaign = File.join(private_root, 'campaign')
reader = KbRuntime::State.new(campaign, 'campaign')
attempt_path = File.join(campaign, 'receipts/runtime-smoke-attempt.json')
attempt_bytes = reader.file(attempt_path)
attempt = JSON.parse(attempt_bytes)
result_path = File.join(private_root, 'runtime-smoke-context/result.json')
result_bytes = reader.file(result_path)
result = JSON.parse(result_bytes)
raise 'unexpected native result' unless result['complete'] == true && result['exit_code'] == 1 && result['cancel_reason'].nil?
raise 'unexpected phase result' unless attempt['kind'] == 'single-runtime-v1' && attempt['phase'] == 'runtime-smoke' && attempt['complete'] == false &&
  attempt['stage'] == 'failed' && attempt['failed_stage'] == 'starting-final-runtime' && attempt['error_class'] == 'KbVerify::Error'
raise 'completed failure receipt appeared' if File.exist?(File.join(campaign, 'receipts/runtime-smoke.json'))
inputs = attempt.fetch('inputs')
raise 'source identity differs' unless inputs.fetch('source') == JSON.parse(File.binread(accepted.fetch('metadata_path')))
raise 'configuration bytes differ' unless inputs.fetch('configuration_sha256') == Digest::SHA256.hexdigest(reader.file(File.join(private_root, 'config.json')))
raise 'selection differs' unless inputs.fetch('selection') == accepted.fetch('selection')
raise 'root differs' unless inputs.fetch('root') == campaign

context = File.join(private_root, 'runtime-smoke-context')
native_evidence = result.fetch('evidence_sha256').to_h do |name, hash|
  raise 'unsafe native evidence name' unless /\A[a-z0-9_.-]+\z/.match?(name)
  path = File.join(context, name)
  raise 'native evidence hash differs' unless Digest::SHA256.file(path).hexdigest == hash
  [name, { 'sha256' => hash, 'bytes' => File.size(path) }]
end
expected_error = "Verification refused: assertion failed: services real resource observations\n"
raise 'native refusal differs' unless reader.file(File.join(context, 'native.stderr')) == expected_error

commands = Dir.glob(File.join(campaign, 'diagnostics/*/command.json')).sort.map do |path|
  bytes = reader.file(path)
  record = JSON.parse(bytes)
  argv = record.fetch('argv')
  action = argv[3] if File.basename(argv.first) == 'vpsfree-kb-devcluster'
  action = nil unless %w[start connection ssh].include?(action)
  machine = argv[5] if action == 'ssh' && %w[services node1].include?(argv[5])
  { 'record' => path, 'sha256' => Digest::SHA256.hexdigest(bytes), 'action' => action, 'machine' => machine,
    'stage' => record['stage'], 'started_at' => record['started_at'], 'finished_at' => record['finished_at'],
    'complete' => record['complete'], 'exit_code' => record['exit_code'], 'signal' => record['signal'], 'accepted' => record['accepted'] }
end
raise 'native command was incomplete or failed' unless commands.all? { |record| record['complete'] == true && record['exit_code'] == 0 && record['signal'].nil? && record['accepted'] == true }
start = commands.select { |record| record['action'] == 'start' }
raise 'not exactly one public start' unless start.size == 1

resource_path = File.join(campaign, 'diagnostics/3fba837a05bd107e3392968e/stdout')
resource_bytes = reader.file(resource_path)
raise 'resource native output differs' unless Digest::SHA256.hexdigest(resource_bytes) == '24be7ccc05dd98f193afde63d2c323b6ccc6750450d5313754ec08b748ccbaa8'
observations = {}
pressure = []
resource_bytes.lines.each do |line|
  if (match = /\A(available_memory_bytes|available_bytes)=([0-9]+)\n\z/.match(line))
    observations[match[1]] = Integer(match[2])
  elsif /\A(?:some|full) avg10=[0-9.]+ avg60=[0-9.]+ avg300=[0-9.]+ total=[0-9]+\n\z/.match?(line)
    pressure << line.chomp
  elsif line == "available_inodes=\n"
    observations['available_inodes_present_but_empty'] = true
  else
    raise 'unexpected resource field'
  end
end
observations['pressure'] = pressure

samples = File.foreach(File.join(context, 'measurements.jsonl')).map { |line| JSON.parse(line) }
monitor = { 'samples' => samples.size }
%w[free_bytes ram_bytes shm_bytes].each do |field|
  values = samples.filter_map { |sample| sample[field] if sample[field].is_a?(Integer) }
  monitor["minimum_#{field}"] = values.min
end

state = KbRuntime::State.new(File.join(campaign, 'state'), 'same-slug')
engine = KbRuntime::Engine.new(state: state, software: nil, controller: nil)
snapshot = state.transaction(create: false, wait: false) do
  identity = state.identity
  phase = engine.phase
  launch = engine.launch
  processes = engine.process_record(launch)
  ready = engine.ready?(launch)
  claim_path = File.join(engine.resources.root, "#{identity.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  expected = launch.slice('instance_id', 'run_id', 'artifact_id', 'artifact_sha256', 'boot_id', 'owner_uid', 'state_root', 'slug', 'resource_claims')
  claim_present = File.exist?(claim_path)
  raise 'own registry claim differs' if claim_present && state.read(claim_path) != expected
  raise 'socket derivation differs' unless launch.fetch('socket_dir') == engine.resources.socket_dir(identity.fetch('instance_id'), launch.fetch('run_id'))
  state.private_directory(launch.fetch('socket_dir')) || raise('socket namespace absent')
  entries = Dir.children(launch.fetch('socket_dir')).sort
  raise 'too many socket entries' if entries.size > 32
  disk_facts = %w[services-root.img node1-tank.img].to_h do |name|
    stat = File.lstat(File.join(state.directory, 'disks', name))
    raise 'unsafe retained disk' unless stat.file? && !stat.symlink? && stat.uid == Process.uid
    [name, { 'device' => stat.dev, 'inode' => stat.ino, 'bytes' => stat.size, 'allocated_bytes' => stat.blocks * 512 }]
  end
  { 'observed_at' => Time.now.utc.iso8601, 'phase' => phase.fetch('phase'), 'ready' => ready,
    'instance_id' => identity.fetch('instance_id'), 'run_id' => launch.fetch('run_id'),
    'artifact_id' => launch.fetch('artifact_id'), 'artifact_sha256' => launch.fetch('artifact_sha256'),
    'matching_live_runner' => KbRuntime::ProcessIdentity.runner_matches?(processes.fetch('runner'), launch),
    'processes_complete' => processes.fetch('complete'), 'recorded_children' => processes.fetch('children').size,
    'matching_live_recorded_children' => processes.fetch('children').count { |record| KbRuntime::ProcessIdentity.matches?(record) },
    'positively_gone_recorded_children' => processes.fetch('children').count { |record| KbRuntime::ProcessIdentity.gone?(record) },
    'own_claim_present' => claim_present, 'own_claim_path' => claim_path,
    'socket_directory' => launch.fetch('socket_dir'),
    'socket_entries' => entries.map { |name| { 'name' => name, 'type' => File.lstat(File.join(launch.fetch('socket_dir'), name)).ftype } },
    'disks' => disk_facts, 'cleanup_certified' => false, 'stopped_certified' => false }
end

proof = { 'schema' => 1, 'generator' => generator, 'extension' => '02ed6dae758cc99b8ba58a18edb07021762c0555',
  'phase' => 'runtime-smoke', 'accepted' => false, 'complete' => false, 'native_exit_code' => 1,
  'wrapper_complete' => true, 'cancel_reason' => nil, 'native_result_sha256' => Digest::SHA256.hexdigest(result_bytes),
  'attempt_sha256' => Digest::SHA256.hexdigest(attempt_bytes), 'private_attempt' => attempt_path,
  'started_at' => result.fetch('started_at'), 'finished_at' => result.fetch('finished_at'),
  'failed_stage' => attempt.fetch('failed_stage'), 'error_class' => attempt.fetch('error_class'),
  'source_defined_error' => expected_error.chomp, 'assertions' => attempt.fetch('assertions'),
  'configuration_sha256' => inputs.fetch('configuration_sha256'), 'public_command_records' => commands,
  'native_evidence' => native_evidence, 'host_monitor' => monitor, 'services_resource_observation' => observations,
  'retained_snapshot' => snapshot,
  'limits' => 'One public start succeeded with attested identity/closures. No completed runtime qualification, member PHP/API/live lease, stop/resume, continuity or media proof. Failure ends the finite attempt; no replay/upscale/cleanup. No private inputs, account values or credentials are exported.' }
output = File.join(tracking, 'finish-virtiofs-runtime-failure-proof1.json')
File.open(output, File::WRONLY | File::CREAT | File::EXCL, 0o644) { |stream| stream.write(JSON.pretty_generate(proof) + "\n") }
puts JSON.generate(proof.slice('generator', 'accepted', 'complete', 'native_exit_code', 'failed_stage', 'source_defined_error').merge('proof' => output))
