# frozen_string_literal: true
# Finite public capture on the same already-qualified retained G725 instance.
require 'json'
require 'digest'
require 'time'
packet = JSON.parse(File.binread(ARGV.fetch(0)))
require File.join(packet.fetch('harness_source'), 'cluster/lib/kb_runtime')
require File.join(packet.fetch('harness_source'), 'tools/runtime-verify')
selection = JSON.parse(File.binread(packet.fetch('selection')))
subject = JSON.parse(File.binread(selection.fetch('metadata')))
root = packet.fetch('evidence_root')
state = KbRuntime::State.new(root, 'capture-evidence')
raise 'private evidence root absent' unless state.private_directory(root)
commands = KbVerify::Commands.new(selection, root)
completed = JSON.parse(state.file(packet.fetch('public_smoke_completed')))
baseline = JSON.parse(state.file(packet.fetch('continuity_baseline')))
raise 'public smoke is not complete' unless completed['complete'] == true && completed['generator'] == subject.fetch('revision') && subject.fetch('revision') == '725c325e8b4971931e5d16df86bafa8584358ecb'
raise 'capture evidence cannot replay' if File.exist?(File.join(root, 'progress.json')) || File.exist?(File.join(root, 'completed.json'))
stage = 'same-instance-capture-admission'
write = ->(name, value) { state.write(File.join(root, name), value) }
check = ->(condition, message) { raise KbVerify::Error, message unless condition }
call = lambda do |argv, cwd: packet.fetch('cwd'), input: ''|
  commands.call(argv, cwd:, input:, stage:)
end
engine = lambda do |command, *arguments, input: ''|
  call.call([File.join(selection.fetch('runtime'), 'bin/vpsfree-kb-devcluster'), '--state-root', packet.fetch('state_root'), command, 'same-slug', *arguments], input:)
end
unchanged_failure = lambda do
  check.call(Digest::SHA256.hexdigest(state.file(packet.fetch('failed_attempt'))) == packet.fetch('failed_attempt_sha256'), 'original failed attempt changed')
  check.call(!File.exist?(File.join(File.dirname(packet.fetch('failed_attempt')), 'runtime-smoke.json')), 'original campaign completion appeared')
end
checkpoint = lambda do |value|
  stage = value
  unchanged_failure.call
  write.call('progress.json', { 'kind' => 'retained-g725-bilingual-capture-v1', 'complete' => false, 'stage' => stage, 'at' => Time.now.utc.iso8601 })
end
connection = lambda do
  value = JSON.parse(engine.call('connection').first)
  check.call(value.dig('provenance', 'source') == subject, 'actual G725 generator')
  %w[instance_id artifact_id artifact_sha256].each { |key| check.call(value.fetch(key) == completed.fetch(key), 'same smoke instance/artifact') }
  check.call(value.fetch('run_id') == completed.fetch('resumed_run'), 'same resumed live run')
  value
end
continuity = lambda do
  directory = File.join(packet.fetch('state_root'), 'clusters/same-slug')
  previous = baseline.fetch('identities')
  previous.fetch('credentials').each { |name, sha| check.call(Digest::SHA256.hexdigest(state.file(File.join(directory, 'credentials', name))) == sha, 'credential continuity') }
  %w[accounts accepted_artifact prepared_artifact configuration].each do |name|
    filename = { 'accounts' => File.join(directory, 'accounts.json'), 'accepted_artifact' => File.join(directory, 'accepted-artifact.json'),
      'prepared_artifact' => File.join(directory, "prepared-#{completed.fetch('artifact_id')}.json"), 'configuration' => packet.fetch('config') }.fetch(name)
    check.call(Digest::SHA256.hexdigest(state.file(filename)) == previous.fetch(name + '_sha256'), name + ' continuity')
  end
  previous.fetch('artifacts').each { |name, sha| check.call(Digest::SHA256.hexdigest(state.file(File.join(directory, name))) == sha, 'immutable artifact continuity') }
  previous.fetch('disks').each do |name, expected|
    st = File.lstat(File.join(directory, 'disks', name))
    check.call(st.file? && !st.symlink? && st.uid == Process.uid && { 'device' => st.dev, 'inode' => st.ino, 'size' => st.size } == expected, 'same owned disks')
  end
  previous.fetch('images').each do |expected|
    st = File.stat(expected.fetch('path'))
    check.call(st.file? && st.dev == expected.fetch('device') && st.ino == expected.fetch('inode') && st.size == expected.fetch('size'), 'same immutable image')
  end
  { 'services' => '/root/kb-root-sentinel', 'node1' => '/tank/kb-data-sentinel' }.each do |machine, path|
    check.call(engine.call('ssh', machine, '--', 'sha256sum', path).first.split.first == baseline.fetch('sentinels').fetch(machine), 'root/data sentinel continuity')
  end
end
source_hashes = lambda do
  JSON.parse(File.binread(packet.fetch('generator_binding'))).fetch('files').to_h do |entry|
    path = File.join(subject.fetch('source'), entry.fetch('path'))
    [entry.fetch('path'), Digest::SHA256.file(path).hexdigest]
  end
end
begin
  unchanged_failure.call
  current = connection.call
  continuity.call
  before = source_hashes.call
  checkpoint.call('fresh-guest-resource-proof')
  observations = %w[services node1].to_h do |machine|
    output = engine.call('ssh', machine, '--', 'sh', '-s', input: File.binread(packet.fetch('resource_scripts').fetch(machine))).first
    pairs = output.lines.filter_map { |line| match = /\A([a-z_]+)=([0-9]+)\n?\z/.match(line); [match[1], Integer(match[2])] if match }
    required = machine == 'services' ? %w[available_memory_bytes available_bytes available_inodes] : %w[available_memory_bytes tank_available_bytes]
    check.call(pairs.size == required.size && pairs.to_h.keys.sort == required.sort, 'required native resource measurements')
    [machine, pairs.to_h.merge('pressure' => output.lines.reject { |line| /\A[a-z_]+=[0-9]+\n?\z/.match?(line) }.join)]
  end
  limits = packet.fetch('guest_capture_assessment')
  services, node = observations.fetch('services'), observations.fetch('node1')
  check.call(services.fetch('available_bytes') >= 1024**3 && services.fetch('available_inodes') >= limits.fetch('minimum_free_inodes'), 'services filesystem headroom')
  check.call(services.fetch('available_memory_bytes') >= limits.fetch('services_memory_bytes') && node.fetch('available_memory_bytes') >= limits.fetch('node_memory_bytes'), 'live guest memory headroom')
  check.call(node.fetch('tank_available_bytes') >= 4 * 1024**3 + limits.fetch('template_metadata_bytes'), 'real 4 GiB quota and template/metadata headroom')
  write.call('resources.json', { 'observations' => observations, 'assessment' => limits, 'script_origin' => packet.fetch('resource_script_origin') })
  output = packet.fetch('output_root')
  check.call(state.private_directory(output), 'private output root')
  capture = File.join(selection.fetch('capture'), 'bin/vpsfree-kb-capture')
  checkpoint.call('CS-cluster-selector')
  call.call([capture, '--cluster', 'same-slug', '--state-root', packet.fetch('state_root'), '--language', 'cs', '--checkpoint', 'networking/ip-address-list', '--output-root', output])
  write.call('capture-connection.json', connection.call)
  checkpoint.call('EN-connection-selector')
  call.call([capture, '--connection', File.join(root, 'capture-connection.json'), '--language', 'en', '--checkpoint', 'networking/ip-address-list', '--output-root', output])
  checkpoint.call('EN-default-CWD')
  call.call([capture, '--connection', File.join(root, 'capture-connection.json'), '--language', 'en', '--checkpoint', 'networking/ip-address-list'], cwd: output)
  checkpoint.call('strict-installed-validation-and-export')
  validator = File.join(selection.fetch('capture'), 'bin/vpsfree-kb-validate')
  call.call([validator, '--update', '--output-root', output])
  call.call([validator, '--output-root', output])
  rows = JSON.parse(File.binread(File.join(output, 'tmp/capture-results.json')))
  check.call(rows.map { |row| [row.fetch('language'), row.fetch('id')] }.sort == [['cs', 'networking/ip-address-list'], ['en', 'networking/ip-address-list']], 'exact bilingual rows')
  check.call(rows.all? { |row| row.dig('provenance', 'source') == subject }, 'genuine G725 bitmap provenance')
  check.call(source_hashes.call == before, 'immutable generator files unchanged')
  check.call(connection.call.fetch('run_id') == current.fetch('run_id'), 'same live capture run')
  continuity.call
  exported = KbCaptureArtifacts.export(output, packet.fetch('export_root'))
  write.call('export.json', exported)
  unchanged_failure.call
  write.call('completed.json', { 'kind' => 'retained-g725-bilingual-capture-v1', 'complete' => true, 'generator' => subject.fetch('revision'),
    'instance_id' => current.fetch('instance_id'), 'run_id' => current.fetch('run_id'), 'artifact_id' => current.fetch('artifact_id'),
    'artifact_sha256' => current.fetch('artifact_sha256'), 'strict_full_inventory' => true, 'five_file_export' => exported,
    'original_failed_attempt_unchanged' => true, 'original_campaign_completed' => false, 'finished_at' => Time.now.utc.iso8601 })
rescue Exception => failure
  write.call('failed.json', { 'kind' => 'retained-g725-bilingual-capture-v1', 'complete' => false, 'stage' => stage,
    'failure_class' => failure.class.name, 'failure_message' => failure.message, 'original_campaign_completed' => false, 'at' => Time.now.utc.iso8601 })
  raise
end
