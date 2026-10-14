# frozen_string_literal: true

# Read-only, named retained G14 receipts and stored public SSH key fingerprints.
require 'json'
require 'digest'
require 'base64'
require 'time'
require '/nix/store/rm2h27hrml95lbwri4vcmg6f7jlkrbqp-source/cluster/lib/kb_runtime'

tracking = '/home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter'
private_root = '/home/aither/.local/state/vpsfree-kb-verification/2026-10-05-network-ipv4-left-counter-g14'
state = KbRuntime::State.new(File.join(private_root, 'campaign/state'), 'same-slug')
engine = KbRuntime::Engine.new(state: state, software: nil, controller: nil)
before = JSON.parse(File.binread(File.join(tracking, 'finish-continuation-g14-retention2.json'))).fetch('snapshot')
failure = JSON.parse(File.binread(File.join(tracking, 'finish-continuation-public-smoke1-failure-proof.json')))

fingerprint = lambda do |line|
  fields = line.split
  raise 'invalid retained public-key line' unless fields.size == 3
  bytes = Base64.strict_decode64(fields.last)
  { 'endpoint' => fields.first, 'algorithm' => fields[1],
    'fingerprint' => "SHA256:#{Base64.strict_encode64(Digest::SHA256.digest(bytes)).delete('=')}" }
end
absent = lambda do |path|
  File.lstat(path)
  false
rescue Errno::ENOENT
  true
end
tuple_fact = lambda do |record|
  current = KbRuntime::ProcessIdentity.read(record.fetch('pid'))
  fact = record.slice('pid', 'start_ticks', 'boot_id', 'owner_uid', 'executable').merge(
    'recorded_argv_sha256' => Digest::SHA256.hexdigest(JSON.generate(record.fetch('argv'))),
    'matches_recorded_identity' => current == record,
    'positively_gone' => KbRuntime::ProcessIdentity.gone?(record))
  if current == record
    fact['process_group'] = Process.getpgid(record.fetch('pid'))
    fact['session_id'] = Process.getsid(record.fetch('pid'))
    fact['cgroup'] = File.read("/proc/#{record.fetch('pid')}/cgroup").strip
    raise 'identity changed during tuple observation' unless KbRuntime::ProcessIdentity.matches?(record)
  end
  fact
end

snapshot = state.transaction(create: false, wait: false) do
  identity = state.identity
  launch = engine.launch
  %w[instance_id artifact_id artifact_sha256].each do |key|
    raise 'retained artifact/instance changed' unless launch.fetch(key) == before.fetch(key)
  end
  raise 'resume did not create its own new run' if launch.fetch('run_id') == before.fetch('run_id')
  raise 'foreign instance' unless identity.fetch('instance_id') == launch.fetch('instance_id')
  phase = engine.phase
  record = engine.process_record(launch)
  raise 'invalid process schema or completion value' unless record['schema'] == 1 && [true, false].include?(record['complete'])
  child_keys = record.fetch('children').map { |child| child.values_at('pid', 'start_ticks') }
  raise 'duplicate child identity' unless child_keys == child_keys.uniq
  runner = tuple_fact.call(record.fetch('runner'))
  children = record.fetch('children').map { |child| tuple_fact.call(child) }
  claim_path = File.join(engine.resources.root, "#{identity.fetch('instance_id')}-#{launch.fetch('run_id')}.json")
  socket_path = engine.resources.socket_dir(identity.fetch('instance_id'), launch.fetch('run_id'))
  raise 'socket derivation differs' unless socket_path == launch.fetch('socket_dir')
  claim_present = !absent.call(claim_path)
  claim_bytes = claim_present ? state.file(claim_path) : nil
  if claim_bytes
    claim = JSON.parse(claim_bytes)
    %w[instance_id run_id owner_uid].each { |key| raise 'foreign current claim' unless claim.fetch(key) == launch.fetch(key) }
  end
  socket_inventory = []
  unless absent.call(socket_path)
    state.private_directory(socket_path) || raise('socket directory vanished')
    names = Dir.children(socket_path).sort
    raise 'unexpected large socket inventory' if names.size > 32
    socket_inventory = names.map do |name|
      stat = File.lstat(File.join(socket_path, name))
      { 'name' => name, 'type' => stat.ftype, 'owner_uid' => stat.uid, 'mode' => (stat.mode & 0o777),
        'device' => stat.dev, 'inode' => stat.ino }
    end
  end
  known_path = state.path('credentials') + '/known_hosts'
  known_bytes = state.file(known_path)
  retained = known_bytes.lines.reject { |line| line.strip.empty? || line.start_with?('#') }.map { |line| fingerprint.call(line) }
  wanted_diagnostic = failure.fetch('private_diagnostic')
  raise 'failure diagnostic does not bind current run' unless File.dirname(wanted_diagnostic) == state.directory &&
    /\Assh-#{Regexp.escape(launch.fetch('run_id'))}-[a-f0-9]{12}-node1-[1-9][0-9]*\.json\z/.match?(File.basename(wanted_diagnostic))
  names = Dir.children(state.directory).grep(/\Assh-#{Regexp.escape(launch.fetch('run_id'))}-[a-f0-9]{12}-(?:services|node1)-[1-9][0-9]*\.json\z/).sort
  diagnostics = names.map do |name|
    path = state.path(name)
    bytes = state.file(path)
    value = JSON.parse(bytes)
    endpoint = launch.fetch('endpoints').fetch(value.fetch('machine'))
    raise 'foreign keyscan diagnostic' unless value['schema'] == 1 && value.fetch('run_id') == launch.fetch('run_id') && value.fetch('endpoint') == endpoint
    output = Base64.strict_decode64(value.fetch('stdout_base64'))
    scanned_keys = engine.send(:ssh_host_keys, output, endpoint).map { |line| fingerprint.call(line) }
    scanned_keys.each do |key|
      key['exact_retained_key'] = retained.include?(key)
      key['same_algorithm_retained_fingerprints'] = retained.select { |old| old['endpoint'] == key['endpoint'] && old['algorithm'] == key['algorithm'] }.map { |old| old['fingerprint'] }
    end
    { 'name' => name, 'sha256' => Digest::SHA256.hexdigest(bytes), 'machine' => value.fetch('machine'),
      'attempt' => value.fetch('attempt'), 'exitstatus' => value['exitstatus'], 'termsig' => value['termsig'],
      'deadline' => value['deadline'], 'truncated' => value['truncated'], 'invocation_error' => value['invocation_error'],
      'stdout_bytes' => output.bytesize, 'stored_public_keys' => scanned_keys }
  end
  raise 'expected failed scan absent' unless diagnostics.any? { |item| item['name'] == File.basename(wanted_diagnostic) }
  raise 'known_hosts changed during read' unless state.file(known_path) == known_bytes
  raise 'phase/launch changed during read' unless engine.phase == phase && engine.launch == launch
  current_record = engine.process_record(launch)
  raise 'runner/previous child publication regressed' unless current_record.fetch('runner') == record.fetch('runner') &&
    child_keys.all? { |key| current_record.fetch('children').any? { |child| child.values_at('pid', 'start_ticks') == key } }
  { 'observed_at' => Time.now.utc.iso8601, 'phase' => phase.fetch('phase'), 'ready' => engine.ready?(launch),
    'instance_id' => launch.fetch('instance_id'), 'run_id' => launch.fetch('run_id'),
    'artifact_id' => launch.fetch('artifact_id'), 'artifact_sha256' => launch.fetch('artifact_sha256'),
    'processes_complete' => record.fetch('complete'), 'recorded_children' => children.size,
    'runner_matches_launch' => KbRuntime::ProcessIdentity.runner_matches?(record.fetch('runner'), launch),
    'runner' => runner, 'children' => children, 'complete_exit_proved' => engine.gone?(launch),
    'own_claim_present' => claim_present, 'own_claim_sha256' => claim_bytes && Digest::SHA256.hexdigest(claim_bytes),
    'owned_socket_namespace_present' => !absent.call(socket_path), 'socket_inventory' => socket_inventory,
    'known_hosts_sha256' => Digest::SHA256.hexdigest(known_bytes), 'known_hosts_bytes' => known_bytes.bytesize,
    'retained_public_key_fingerprints' => retained, 'stored_keyscan_diagnostics' => diagnostics }
end
reader = KbRuntime::State.new(File.join(private_root, 'campaign'), 'campaign')
attempt_hash = Digest::SHA256.hexdigest(reader.file(File.join(private_root, 'campaign/receipts/runtime-smoke-attempt.json')))
raise 'original failed attempt changed' unless attempt_hash == failure.fetch('original_failed_attempt_sha256')
proof = { 'schema' => 1, 'generator' => failure.fetch('generator'), 'harness_revision' => failure.fetch('harness_revision'),
  'selected_unit_exit' => 1, 'snapshot' => snapshot, 'original_failed_attempt_sha256' => attempt_hash,
  'original_completed_receipt_absent' => absent.call(File.join(private_root, 'campaign/receipts/runtime-smoke.json')),
  'limits' => 'Read-only named current G14 receipts, native recorded tuples and stored public-key fingerprints. No live scan/SSH, trust write, stop/reset/signal/retry, cleanup, new pair or media. Receipt observations are not complete process-tree certification.' }
output = File.join(tracking, 'finish-g14-resume-key-observation1.json')
File.open(output, File::WRONLY | File::CREAT | File::EXCL, 0o644) { |stream| stream.write(JSON.pretty_generate(proof) + "\n") }
puts JSON.generate('proof' => output, 'run_id' => snapshot.fetch('run_id'), 'phase' => snapshot.fetch('phase'),
  'ready' => snapshot.fetch('ready'), 'complete' => snapshot.fetch('processes_complete'),
  'runner_matches_launch' => snapshot.fetch('runner_matches_launch'), 'recorded_children' => snapshot.fetch('recorded_children'),
  'matching_children' => snapshot.fetch('children').count { |child| child['matches_recorded_identity'] },
  'gone_children' => snapshot.fetch('children').count { |child| child['positively_gone'] },
  'claim_present' => snapshot.fetch('own_claim_present'), 'socket_present' => snapshot.fetch('owned_socket_namespace_present'),
  'keyscans' => snapshot.fetch('stored_keyscan_diagnostics'))
