# frozen_string_literal: true

# Disposable native Nix profile exercise; no live workspace state is used.
require 'tmpdir'
require 'fileutils'
require 'open3'
require_relative '../../worktrees/2026-10-19-coordination-storage-cleanup/dev-workspace/libexec/workspace-coordination-execution'

def run(*args)
  out, err, status = Open3.capture3(*args)
  raise "#{args.first} failed: #{err}" unless status.success?
  out
end

package = File.realpath('/home/aither/.local/state/dev-workspaces/profile')
inputs = %w[bash git ruby].map do |name|
  command = run('sh', '-c', "command -v #{name}").strip
  real = File.realpath(command)
  real[%r{\A/nix/store/[^/]+}] || raise("not a Nix package: #{name}")
end
Dir.mktmpdir('native-profile-retention-', '/run/user/1000') do |root|
  profile = File.join(root, 'profile')
  (inputs + [package]).each { |input| run('nix-env', '--profile', profile, '--set', input) }
  before = File.readlink(profile)
  count = Dir["#{profile}-*-link"].length
  raise 'native fixture did not create four generations' unless count == 4
  engine = WorkspaceCoordination::Engine.new(state: File.join(root, 'state'),
    package: package, profile: profile, workspace: root, entry: {}, fixtures: true)
  preview = WorkspaceCoordination::Collector.new(engine).call
  generations = preview.fetch('actions').select { |item| item['kind'] == 'profile_generation' }.map { |item| item['generation'] }
  raise "unexpected native generation plan #{generations}" unless generations == [1, 2]
  result = WorkspaceCoordination::Collector.new(engine).call(apply: true)
  raise 'profile selection changed' unless File.readlink(profile) == before
  raise 'current package changed' unless File.realpath(profile) == package
  raise 'predecessor/current not retained' unless Dir["#{profile}-*-link"].sort == ["#{profile}-3-link", "#{profile}-4-link"]
  raise 'non-idempotent collection' unless WorkspaceCoordination::Collector.new(engine).call(apply: true)['removed'].empty?
  puts "Native profile check passed: #{result['removed'].length} generations removed; current and predecessor retained"
end
