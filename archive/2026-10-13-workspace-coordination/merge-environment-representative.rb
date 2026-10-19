require 'json'
require 'fileutils'
require 'rbconfig'
root = '/home/aither/workspace/ai/vpsfree.cz'
tracking = File.join(root, 'work/2026-10-13-workspace-coordination')
package = File.read(File.join(tracking, 'merge-environment-candidate.path')).strip
require File.join(package, 'libexec/workspace-coordination-execution')
state = '/home/aither/.local/state/dev-workspaces/verification/coordination-merge-environment-final'
FileUtils.mkdir_p(state, mode: 0o700)
profile = File.join(state, 'candidate-profile')
File.symlink(package, profile) unless File.symlink?(profile)
raise 'private candidate changed' unless File.realpath(profile) == package
engine = WorkspaceCoordination::Engine.new(state: state, package: package, profile: profile,
  workspace: root, entry: {'name' => 'vpsfree-cz'})
revision = 'de6aefab722414e6d206a10e3924cf5815b23519'
path = File.join(root, 'repos/vpsfree-cz-configuration.git')
artifact = nil
source = engine.retain_commit(path, revision) do |retained|
  artifact = engine.prepare_merge_hooks(retained, 'vpsfree-cz-configuration', revision)
end
engine.with_merge_hooks('hookArtifact' => artifact['id']) do
  engine.capture('ssh', '-V')
  engine.capture('bundle', 'check', cwd: source)
  engine.capture('git', '-C', source, 'checkout', '--detach', revision)
end
raise 'private verification admitted a job' unless engine.store.read['jobs'].empty?
raise 'retained source changed' unless engine.capture('git', '-C', source, 'status', '--porcelain').empty?
puts JSON.generate('schema' => 1, 'outcome' => 'passed', 'package' => package,
  'configurationHead' => revision, 'source' => source, 'hookArtifact' => artifact['id'],
  'checks' => {'freshSourceInitialized' => true, 'actualOvercommitHook' => true,
    'actualBundlerDependencies' => true, 'sshTransport' => true, 'noJob' => true,
    'noActivation' => true}, 'environmentKeys' => artifact['environment'].keys.sort)
