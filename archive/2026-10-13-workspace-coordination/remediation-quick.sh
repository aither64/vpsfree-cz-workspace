#!/usr/bin/env bash
set -euo pipefail
ruby test/workspace_coordination_test.rb
ruby test/workspace_host_test.rb
ruby test/dev_session_test.rb -n '/coordination_failure_retains|coordination_capacity_refusal/'
WORKSPACE_COORDINATION_COMMAND="$PWD/libexec/workspace-coordination-command.rb" ruby ../vpsfree-dev-workspace/test/workspace_confctl_adapter_test.rb
ruby -c libexec/workspace-host
ruby -c libexec/dev-session
ruby -c libexec/workspace-coordination.rb
ruby -c libexec/workspace-coordination-execution.rb
ruby -c libexec/workspace-coordination-host.rb
(cd portal; go test -mod=readonly ./internal/workspacecodex ./internal/teamruntime -run 'TestLeadPolicy|TestMemberPolicy|TestRetainedMember')
