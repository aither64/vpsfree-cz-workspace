# frozen_string_literal: true
# Finite coordination only: public commands on one retained, source-matched instance.
require 'json'
require 'digest'
require 'securerandom'
require 'time'
packet = JSON.parse(File.binread(ARGV.fetch(0)))
require File.join(packet.fetch('harness_source'), 'cluster/lib/kb_runtime')
require File.join(packet.fetch('harness_source'), 'tools/runtime-verify')
selection = JSON.parse(File.binread(packet.fetch('selection')))
root = packet.fetch('evidence_root')
state_root = packet.fetch('state_root')
reader = KbRuntime::State.new(root, 'evidence')
raise 'private evidence root absent' unless reader.private_directory(root)
commands = KbVerify::Commands.new(selection, root)
subject = JSON.parse(File.binread(selection.fetch('metadata')))
raise 'subject selection differs' unless subject.fetch('revision') == '725c325e8b4971931e5d16df86bafa8584358ecb' && subject.fetch('source') == selection.fetch('source')
failed_attempt = packet.fetch('failed_attempt')
failed_hash = packet.fetch('failed_attempt_sha256')
configuration = packet.fetch('config')
expected = packet.fetch('retained')
GIB = 1024**3
stage = 'admission'
write = lambda do |name, value|
  reader.write(File.join(root, name), value)
end
check = lambda { |condition, message| raise KbVerify::Error, message unless condition }
unchanged_failure = lambda do
  check.call(Digest::SHA256.hexdigest(reader.file(failed_attempt)) == failed_hash, 'original failed attempt changed')
  check.call(!File.exist?(File.join(File.dirname(failed_attempt), 'runtime-smoke.json')), 'original completion appeared')
end
call = lambda do |argv, input: '', accepted: [0]|
  commands.call(argv, cwd: packet.fetch('cwd'), input:, accepted:, stage:)
end
engine = lambda do |command, *arguments, input: ''|
  call.call([File.join(selection.fetch('runtime'), 'bin/vpsfree-kb-devcluster'), '--state-root', state_root, command, 'same-slug', *arguments], input:)
end
checkpoint = lambda do |next_stage|
  stage = next_stage
  unchanged_failure.call
  write.call('progress.json', { 'kind' => 'retained-g725-public-smoke-v1', 'stage' => stage, 'complete' => false, 'at' => Time.now.utc.iso8601 })
end
capture_descriptor = lambda do |name|
  bytes = engine.call('connection').first
  value = JSON.parse(bytes)
  check.call(value.dig('provenance', 'source') == subject, 'exact G725 source')
  check.call(value.fetch('machines').keys.sort == %w[node1 services], 'only original machines')
  %w[instance_id artifact_id artifact_sha256].each { |key| check.call(value.fetch(key) == expected.fetch(key), 'retained artifact/instance changed') }
  value.fetch('provenance').fetch('machine_toplevels').each do |machine, closure|
    identity = JSON.parse(engine.call('ssh', machine, '--', 'cat', '/etc/vpsfree-kb-capture.json').first)
    check.call(identity == value.fetch('provenance').fetch('guest_identity'), 'guest identity differs')
    check.call(engine.call('ssh', machine, '--', 'readlink', '-f', '/run/current-system').first.strip == closure, 'guest closure differs')
  end
  status = JSON.parse(engine.call('status').first)
  check.call(status['found'] == true && status['state'] == 'ready' && status['ready'] == true && status['run_id'] == value.fetch('run_id'), 'fresh public ready status')
  write.call('status-' + name, status)
  write.call(name, value)
  value
end
resources = lambda do |value|
  observed = %w[services node1].to_h do |machine|
    script = File.binread(packet.fetch('resource_scripts').fetch(machine))
    output = engine.call('ssh', machine, '--', 'sh', '-s', input: script).first
    pairs = output.lines.filter_map { |line| match = /\A([a-z_]+)=([0-9]+)\n?\z/.match(line); [match[1], Integer(match[2])] if match }
    numeric = pairs.to_h
    required = machine == 'services' ? %w[available_memory_bytes available_bytes available_inodes] : %w[available_memory_bytes tank_available_bytes]
    check.call(pairs.size == required.size && numeric.keys.sort == required.sort, 'required native resource observations')
    [machine, numeric.merge('pressure' => output.lines.reject { |line| /\A[a-z_]+=[0-9]+\n?\z/.match?(line) }.join)]
  end
  check.call(observed.fetch('services').fetch('available_bytes') >= GIB, 'services 1 GiB writable headroom')
  write.call("resources-#{value.fetch('run_id')}.json", { 'run_id' => value.fetch('run_id'), 'observations' => observed, 'script_origin' => packet.fetch('resource_script_origin') })
  observed
end
read_smoke = lambda do |name|
  output = call.call(['node', '-e', File.binread(packet.fetch('read_smoke_script')), File.join(root, name), selection.fetch('metadata'), selection.fetch('source')]).first
  value = JSON.parse(output)
  check.call(value['api_tls_verified'] == true && value['php_member_read'] == true && value.dig('member', 'login') == 'test-user1', 'TLS/API/member PHP read')
  write.call("read-#{name}", value)
end
identities = lambda do
  directory = File.join(state_root, 'clusters/same-slug')
  credentials = KbVerify::CREDENTIALS.to_h { |name| [name, Digest::SHA256.hexdigest(reader.file(File.join(directory, 'credentials', name)))] }
  disks = %w[services-root.img node1-tank.img].to_h do |name|
    st = File.lstat(File.join(directory, 'disks', name))
    check.call(st.file? && !st.symlink? && st.uid == Process.uid && st.size == 8 * GIB, 'owned same-size disk')
    [name, { 'device' => st.dev, 'inode' => st.ino, 'size' => st.size }]
  end
  artifacts = Dir.glob(File.join(directory, 'artifact-*.json')).to_h { |path| [File.basename(path), Digest::SHA256.hexdigest(reader.file(path))] }
  check.call(artifacts.size == 1, 'one accepted artifact')
  images = Dir.glob(File.join(directory, 'result-config-*')).map do |path|
    resolved = File.realpath(path)
    check.call(resolved.start_with?('/nix/store/') && File.file?(resolved), 'immutable result config')
    image = JSON.parse(File.binread(resolved)).fetch('machines').fetch('services').fetch('diskImage')
    check.call(image.start_with?('/nix/store/') && image == File.expand_path(image), 'immutable source image')
    st = File.stat(image)
    check.call(st.file? && st.size == 8 * GIB, 'same fixed source image extent')
    { 'path' => image, 'device' => st.dev, 'inode' => st.ino, 'size' => st.size }
  end.uniq { |entry| [entry.fetch('device'), entry.fetch('inode')] }
  check.call(images.size == 1, 'one original source image')
  { 'credentials' => credentials, 'accounts_sha256' => Digest::SHA256.hexdigest(reader.file(File.join(directory, 'accounts.json'))), 'artifacts' => artifacts, 'disks' => disks, 'images' => images,
    'accepted_artifact_sha256' => Digest::SHA256.hexdigest(reader.file(File.join(directory, 'accepted-artifact.json'))),
    'prepared_artifact_sha256' => Digest::SHA256.hexdigest(reader.file(File.join(directory, "prepared-#{expected.fetch('artifact_id')}.json"))),
    'configuration_sha256' => Digest::SHA256.hexdigest(reader.file(configuration)) }
end
sentinels = lambda do
  { 'services' => '/root/kb-root-sentinel', 'node1' => '/tank/kb-data-sentinel' }.to_h do |machine, path|
    [machine, engine.call('ssh', machine, '--', 'sha256sum', path).first.split.first]
  end
end
stopped_proof = lambda do |descriptor|
  state = KbRuntime::State.new(state_root, 'same-slug')
  owner = KbRuntime::Engine.new(state:, software: nil, controller: nil)
  state.transaction(create: false, wait: false) do
    launch = owner.launch
    %w[instance_id run_id artifact_id artifact_sha256].each { |key| check.call(launch.fetch(key) == descriptor.fetch(key), 'stopped launch changed') }
    process = owner.process_record(launch)
    check.call(owner.phase.fetch('phase') == 'stopped' && process.fetch('complete') == true && owner.gone?(launch) && !owner.ready?(launch), 'complete stopped proof')
    claim = File.join(owner.resources.root, "#{launch.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
    socket = owner.resources.socket_dir(launch.fetch('instance_id'), launch.fetch('run_id'))
    check.call(socket == launch.fetch('socket_dir'), 'derived stopped socket identity')
    [claim, socket].each do |path|
      begin
        File.lstat(path)
        raise KbVerify::Error, 'owned claim/namespace remains'
      rescue Errno::ENOENT
        nil
      end
    end
    { 'instance_id' => launch.fetch('instance_id'), 'run_id' => launch.fetch('run_id'), 'artifact_id' => launch.fetch('artifact_id'), 'complete' => true,
      'recorded_children' => process.fetch('children').size, 'all_gone' => true, 'own_claim_absent' => true, 'own_namespace_absent' => true }
  end
end
begin
  unchanged_failure.call
  check.call(Digest::SHA256.hexdigest(reader.file(configuration)) == packet.fetch('configuration_sha256'), 'original configuration changed')
  stopped_proof.call(expected)
  check.call(!File.exist?(File.join(root, 'completed.json')) && !File.exist?(File.join(root, 'progress.json')), 'evidence unit cannot replay')
  checkpoint.call('public-resume-retained-G725')
  engine.call('resume', '--timeout', '900')
  first = capture_descriptor.call('first-connection.json')
  check.call(first.fetch('run_id') != expected.fetch('run_id'), 'fresh initial resumed run')
  checkpoint.call('corrected-native-resources')
  resources.call(first)
  checkpoint.call('TLS-API-member-PHP')
  read_smoke.call('first-connection.json')
  checkpoint.call('public-live-lease-proof')
  call.call(['node', packet.fetch('lease_helper'), File.join(root, 'first-connection.json'), selection.fetch('metadata'), selection.fetch('runtime'), state_root, configuration])
  checkpoint.call('continuity-baseline')
  { 'services' => '/root/kb-root-sentinel', 'node1' => '/tank/kb-data-sentinel' }.each do |machine, path|
    engine.call('ssh', machine, '--', 'sh', '-c', 'set -e; test ! -e "$1"; printf "%s" "$2" > "$1"', 'sh', path, packet.fetch('evidence_id'))
  end
  identity, sentinel = identities.call, sentinels.call
  write.call('continuity-baseline.json', { 'identities' => identity, 'sentinels' => sentinel })
  checkpoint.call('ordinary-public-stop')
  engine.call('stop', '--timeout', '900')
  status = JSON.parse(engine.call('status').first)
  check.call(status['found'] == true && status['state'] == 'stopped' && status['ready'] == false, 'public stopped status')
  write.call('status-stopped.json', status)
  write.call('stopped-proof.json', stopped_proof.call(first))
  checkpoint.call('same-artifact-public-resume')
  engine.call('resume', '--timeout', '900')
  resumed = capture_descriptor.call('resumed-connection.json')
  check.call(resumed.fetch('run_id') != first.fetch('run_id'), 'fresh second run')
  check.call(resumed.fetch('provenance').fetch('machine_toplevels') == first.fetch('provenance').fetch('machine_toplevels'), 'same actual closures')
  check.call(identities.call == identity && sentinels.call == sentinel, 'six credential/account/artifact/config/disk and root/data continuity')
  resources.call(resumed)
  read_smoke.call('resumed-connection.json')
  unchanged_failure.call
  write.call('completed.json', { 'kind' => 'retained-g725-public-smoke-v1', 'complete' => true, 'generator' => subject.fetch('revision'), 'instance_id' => resumed.fetch('instance_id'),
    'first_run' => first.fetch('run_id'), 'resumed_run' => resumed.fetch('run_id'), 'artifact_id' => resumed.fetch('artifact_id'), 'artifact_sha256' => resumed.fetch('artifact_sha256'),
    'public_resume_smoke_lease_stop_resume_continuity' => true, 'original_failed_attempt_unchanged' => true, 'original_campaign_completed' => false, 'finished_at' => Time.now.utc.iso8601 })
rescue Exception => failure
  write.call('failed.json', { 'kind' => 'retained-g725-public-smoke-v1', 'complete' => false, 'stage' => stage, 'failure_class' => failure.class.name, 'failure_message' => failure.message,
    'original_campaign_completed' => false, 'at' => Time.now.utc.iso8601 })
  raise
end
