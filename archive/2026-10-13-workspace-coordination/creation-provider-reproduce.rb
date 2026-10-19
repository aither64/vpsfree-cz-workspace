# Reuse the new isolated regression with the exact deployed helper implementation.
require_relative '../../worktrees/2026-10-13-workspace-coordination/dev-workspace/test/dev_session_test'
source = File.read(File.join(__dir__, 'creation-provider-deployed-helper.rb'))
method_source = source[/^    def native_provider_arguments\n.*?(?=^    def update_native_client_version!)/m]
raise 'deployed method not found' unless method_source
DevSession::Runner.class_eval(method_source, 'deployed-provider-helper', 1)
