#!/usr/bin/env ruby
# Separate public-operation evidence; never resumes the failed Campaign.
require 'json'
require 'digest'
require 'securerandom'
selection = JSON.parse(File.read(ARGV.fetch(0)))
require File.join(selection.fetch('source'), 'tools/runtime-verify.rb')
require File.join(selection.fetch('source'), 'cluster/lib/kb_process.rb')
require File.join(selection.fetch('source'), 'cluster/lib/kb_resources.rb')
root = ARGV.fetch(1)
context = ARGV.fetch(2)
original_failure = File.join(root, 'receipts/runtime-smoke-attempt.json')
failure_hash = Digest::SHA256.file(original_failure).hexdigest
state = KbRuntime::State.new(File.join(root, 'state'), 'same-slug')
commands = KbVerify::Commands.new(selection, context)
runtime = File.join(selection.fetch('runtime'), 'bin/vpsfree-kb-devcluster')
call = ->(*args, input: '', stage:) { commands.call([runtime, '--state-root', File.join(root, 'state'), *args], cwd: context, input:, stage:).first }
private_write = ->(name, value) { File.open(File.join(context, name), File::WRONLY | File::CREAT | File::EXCL, 0o600) { |f| f.write(JSON.generate(value) + "\n") } }
snapshot = lambda do
  credentials = KbVerify::CREDENTIALS.to_h { |name| [name, Digest::SHA256.hexdigest(state.file(File.join(state.path('credentials'), name)))] }
  disks = %w[services-root.img node1-tank.img].to_h do |name|
    file = File.join(state.path('disks'), name); stat = File.lstat(file)
    raise 'unsafe owned disk' unless stat.file? && !stat.symlink? && stat.uid == Process.uid && stat.size == 8 * KbVerify::GIB
    [name, { 'device' => stat.dev, 'inode' => stat.ino, 'size' => stat.size }]
  end
  images = Dir.glob(File.join(state.directory, 'result-config-*')).map do |reference|
    resolved = File.realpath(reference)
    raise 'configuration is not immutable' unless resolved.start_with?('/nix/store/')
    image = JSON.parse(File.read(resolved)).fetch('machines').fetch('services').fetch('diskImage')
    stat = File.stat(image)
    raise 'unexpected immutable image' unless image.start_with?('/nix/store/') && stat.file? && stat.size == 8 * KbVerify::GIB
    { 'path' => image, 'device' => stat.dev, 'inode' => stat.ino, 'size' => stat.size }
  end.uniq
  raise 'not one image' unless images.size == 1
  { 'credentials' => credentials, 'disks' => disks, 'images' => images,
    'accounts_sha256' => Digest::SHA256.hexdigest(state.file(state.path('accounts.json'))),
    'accepted_artifact_sha256' => Digest::SHA256.hexdigest(state.file(state.path('accepted-artifact.json'))) }
end
exit_proof = lambda do |descriptor|
  status = JSON.parse(call.call('status', 'same-slug', stage: 'stopped-status'))
  raise 'not positively stopped' unless status['found'] && status['state'] == 'stopped' && status['ready'] == false
  proof = state.read(state.path("processes-#{descriptor.fetch('run_id')}.json"))
  raise 'incomplete or foreign exit receipt' unless proof['schema'] == 1 && proof['complete'] == true &&
    %w[instance_id run_id artifact_id artifact_sha256].all? { |key| proof[key] == descriptor.fetch(key) }
  tuples = [proof.fetch('runner'), *proof.fetch('children')]
  raise 'recorded process not proved gone' unless tuples.all? { |tuple| KbRuntime::ProcessIdentity.gone?(tuple) }
  launch = state.read(state.path("launch-#{descriptor.fetch('run_id')}.json"))
  raise 'socket namespace remains' if File.exist?(launch.fetch('socket_dir')) || File.symlink?(launch.fetch('socket_dir'))
  claim = File.join(KbRuntime::Resources.new(state).root, "#{descriptor.fetch('instance_id')}-#{descriptor.fetch('run_id')}.json")
  raise 'owned claim remains' if File.exist?(claim) || File.symlink?(claim)
  { 'run_id' => descriptor.fetch('run_id'), 'complete' => true, 'all_recorded_gone' => true,
    'recorded_children' => proof.fetch('children').size, 'socket_namespace_absent' => true, 'owned_claim_absent' => true,
    'native_process_receipt_sha256' => Digest::SHA256.hexdigest(state.file(state.path("processes-#{descriptor.fetch('run_id')}.json"))) }
end
begin
  first = JSON.parse(call.call('connection', 'same-slug', stage: 'before-connection'))
  source = JSON.parse(File.read(selection.fetch('metadata')))
  raise 'genuine source changed' unless first.dig('provenance', 'source') == source
  connection_file = File.join(context, 'connection-before.json')
  private_write.call('connection-before.json', first)
  commands.call(['node', File.join(selection.fetch('source'), 'tools/verify-live-lease.cjs'), connection_file,
    selection.fetch('metadata'), selection.fetch('runtime'), File.join(root, 'state'), File.join(root, 'config.json')], cwd: context, stage: 'separate-public-lease-proof')
  marker = SecureRandom.uuid
  sentinel_paths = { 'services' => '/root/kb-root-sentinel', 'node1' => '/tank/kb-data-sentinel' }
  sentinel_paths.each do |machine, file|
    call.call('ssh', 'same-slug', machine, '--', 'sh', '-c', 'set -e; test ! -e "$1"; printf "%s" "$2" > "$1"', 'sh', file, marker, stage: 'owned-sentinel')
  end
  hashes = -> { sentinel_paths.to_h { |machine, file| [machine, call.call('ssh', 'same-slug', machine, '--', 'sha256sum', file, stage: 'sentinel-observation').split.first] } }
  baseline = snapshot.call
  sentinels = hashes.call
  private_write.call('continuity-before.json', { 'identity' => baseline, 'sentinels' => sentinels })
  call.call('stop', 'same-slug', '--timeout', '900', stage: 'ordinary-public-stop')
  first_exit = exit_proof.call(first)
  call.call('resume', 'same-slug', '--timeout', '900', stage: 'same-artifact-public-resume')
  resumed = JSON.parse(call.call('connection', 'same-slug', stage: 'resumed-connection'))
  raise 'source/instance/artifact continuity differs' unless resumed.dig('provenance', 'source') == source &&
    %w[instance_id artifact_id artifact_sha256].all? { |key| resumed.fetch(key) == first.fetch(key) } && resumed.fetch('run_id') != first.fetch('run_id') &&
    resumed.dig('provenance', 'machine_toplevels') == first.dig('provenance', 'machine_toplevels')
  resumed.fetch('provenance').fetch('machine_toplevels').each do |machine, closure|
    actual = call.call('ssh', 'same-slug', machine, '--', 'readlink', '-f', '/run/current-system', stage: 'resumed-closure').strip
    identity = JSON.parse(call.call('ssh', 'same-slug', machine, '--', 'cat', '/etc/vpsfree-kb-capture.json', stage: 'resumed-guest-identity'))
    raise 'resumed guest identity/closure changed' unless actual == closure && identity == resumed.dig('provenance', 'guest_identity')
  end
  raise 'credentials/accounts/disks/artifact/sentinels changed' unless snapshot.call == baseline && hashes.call == sentinels
  private_write.call('connection-resumed.json', resumed)
  call.call('stop', 'same-slug', '--timeout', '900', stage: 'final-public-stop')
  final_exit = exit_proof.call(resumed)
  raise 'failed Campaign receipt changed' unless Digest::SHA256.file(original_failure).hexdigest == failure_hash
  report = { 'schema' => 1, 'generator' => source.fetch('revision'), 'kind' => 'separate-owned-public-lifecycle-proof',
    'instance_id' => first.fetch('instance_id'), 'artifact_id' => first.fetch('artifact_id'),
    'original_run_id' => first.fetch('run_id'), 'resumed_run_id' => resumed.fetch('run_id'),
    'lease_proof' => true, 'same_artifact_resume' => true, 'six_credentials_accounts_disks_sentinels_unchanged' => true,
    'first_exit' => first_exit, 'final_exit' => final_exit, 'failed_campaign_receipt_sha256' => failure_hash,
    'failed_campaign_unchanged' => true, 'campaign_replayed' => false, 'reset_performed' => false }
  private_write.call('proof.json', report)
  puts JSON.generate(report)
rescue StandardError => error
  warn "Separate public lifecycle operation refused: #{error.message}"
  exit 1
end
