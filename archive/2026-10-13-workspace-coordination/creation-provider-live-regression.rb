# Reuse the isolated public-creation regression with the selected installed helper.
require_relative '../../worktrees/2026-10-13-workspace-coordination/dev-workspace/test/dev_session_test'
path = File.join(File.realpath('/home/aither/.local/state/dev-workspaces/profile'), 'libexec', 'workspace-portal', '.dev-session-wrapped')
raise 'selected helper lacks reviewed command-runner correction' unless File.read(path).include?('output, = @command_runner.capture(')
# Preserve the installed module's lexical constant scope as well as its body.
load path
