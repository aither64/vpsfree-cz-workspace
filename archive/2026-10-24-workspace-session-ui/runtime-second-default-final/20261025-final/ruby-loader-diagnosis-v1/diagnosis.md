# Ruby fragment loader diagnosis

The actual failure is fixture bootstrap: six archive-reader methods ran with zero assertions and six errors because the standalone fragment does not load sibling fixtures. Production behavior was not exercised by those errors.

NullTmux and ManagedTmux are defined by lifecycle_commands_test.rb; with_archive_cleanup_fixture belongs to archive_cleanup_test.rb. Workspace-host recovery also relies on TransitionHost from suspension_test.rb through with_transition_host. Every selected fragment requires only its common support, while the declared aggregate loaders install the needed sibling definitions before Minitest autorun.

Use existing aggregate entrypoints with exact anchored full Minitest identities. Load the complete fixture bootstrap, execute only the same selected methods. Do not pass a bounded filter to run_ruby_suite.rb: it appends its own complete-shard filter, so that would broaden execution or invalidate its reporter. No source, framework or fixture change is needed. Exact method sets and proposed argv are in diagnosis.json; no command was run.

| Stage | Cases | Existing aggregate |
| --- | ---: | --- |
| ruby-archive-check | 6 | test/dev_session_test.rb |
| ruby-archive-retirement | 4 | test/dev_session_test.rb |
| ruby-archive-recovery | 17 | test/workspace_host_test.rb |
| ruby-archive-exact-receipt | 1 | test/dev_session_test.rb |
| ruby-creation-locks | 7 | test/dev_session_test.rb |
| ruby-plan-journal | 2 | test/dev_session_test.rb |
| ruby-fork-lock | 1 | test/dev_session_test.rb |
| ruby-ordinary-readiness | 4 | test/dev_session_test.rb |

The42 selected methods preserve all original selection scopes; nested source loops remain source-controlled coverage, not invented separately recorded cases. Require verbose identity coverage, exact runs, positive assertions and zero failures/errors/skips. Resume only these Ruby and previously unrun diagnostic/syntax/finalguard stages after architect/lead disposition. Do not repeat passed Go/Node stages.

The parent independently proved all1807 bindings unchanged after the failed batch. Original logs, watcher prose and attempt receipts remain intact. Final source608 and accepted xcl/alhm remain unchanged; the separate vendor watcher owns its operation and is not observed here. No production/source fix, retry, test, runner edit or Nix/Git operation was performed.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/
