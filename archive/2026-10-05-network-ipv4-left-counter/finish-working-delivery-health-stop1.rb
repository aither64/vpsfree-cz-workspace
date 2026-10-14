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
  descriptor = state.read(state.path('connection.json'))
  source = JSON.parse(File.read(selection.fetch('metadata')))
  raise 'source or owned run changed' unless descriptor.dig('provenance', 'source') == source &&
    descriptor['instance_id'] == '271d430a-f951-4979-b115-fe66c7516e11' &&
    descriptor['run_id'] == '5b83fc44-1224-44c5-bd23-49f10a42f7b2' &&
    descriptor['artifact_id'] == 'a3406dd9-97b0-4914-98a7-86541b5062b2'
  launch = state.read(state.path("launch-#{descriptor.fetch('run_id')}.json"))
  raise 'runner identity not current' unless KbRuntime::ProcessIdentity.runner_matches?(launch.fetch('runner'), launch)
  call.call('stop', 'same-slug', '--timeout', '900', stage: 'owned-health-public-stop')
  proof = exit_proof.call(descriptor)
  raise 'failed Campaign changed' unless Digest::SHA256.file(original_failure).hexdigest == failure_hash
  result = { 'schema' => 1, 'generator' => source.fetch('revision'), 'instance_id' => descriptor.fetch('instance_id'),
    'artifact_id' => descriptor.fetch('artifact_id'), 'operation' => 'separate-ordinary-public-stop',
    'exit_proof' => proof, 'failed_campaign_unchanged' => true, 'failed_campaign_receipt_sha256' => failure_hash,
    'reset_performed' => false, 'resume_performed' => false, 'disk_deletion_performed' => false }
  private_write.call('proof.json', result)
  puts JSON.generate(result)
rescue StandardError => error
  warn "Separate ordinary public stop refused: #{error.message}"
  exit 1
end
