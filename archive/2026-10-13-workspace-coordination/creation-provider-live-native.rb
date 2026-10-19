# Read-only call through the installed helper and the actual configured provider.
require 'json'
require 'stringio'
package = File.realpath('/home/aither/.local/state/dev-workspaces/profile')
load File.join(package, 'libexec/workspace-portal/.dev-session-wrapped')
runner = DevSession::Runner.new(workspace: '/home/aither/workspace/ai/vpsfree.cz',
  host_profile: package, out: StringIO.new, err: StringIO.new,
  env: ENV.to_h.merge('DEV_WORKSPACE_NAME' => 'vpsfree-cz',
                     'DEV_SESSION_SLUG' => '2026-10-13-workspace-coordination',
                     'DEV_SESSION_WORKSPACE' => '/home/aither/workspace/ai/vpsfree.cz'))
args = runner.send(:native_provider_arguments)
raise 'configured provider arguments missing' if args.empty?
raise 'invalid provider arguments' unless args.each_slice(2).all? { |flag, value| flag == '-c' && value.is_a?(String) }
puts JSON.generate('schema' => 1, 'outcome' => 'passed', 'selectedPackage' => package,
  'checks' => {'installedHelper' => true, 'actualConfiguredProvider' => true, 'nativeArgumentPairs' => args.length / 2})
