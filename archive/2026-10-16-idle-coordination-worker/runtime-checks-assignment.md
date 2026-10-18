You are a fresh verification utility watcher under explicit site policy: gpt-6-luna / low. Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md and /home/aither/workspace/ai/vpsfree.cz/docs/agent-instructions/verification.md and the runtime worktree AGENTS.md. Do not edit source, diagnose, retry, approve, deploy or spawn agents. Parent completed mandatory review and focused remediation.

Working directory: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/dev-workspace
Tested committed revision: ced31b5 (read full SHA before launch).
Logs/results directory: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/

Execute this related verification batch, each status separately, no retries:
1. nix build --no-link --print-out-paths --print-build-logs .#checks.x86_64-linux.package .#checks.x86_64-linux.host-package-contract
2. nix develop --command ruby test/background_integration_systemd_test.rb -n /systemd/
3. nix develop --command go -C portal test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1

Keep complete per-command logs runtime-package.log, systemd-check.log, notification-protocol.log, with per-command .status files. Preserve exact statuses. For first command also retain build output paths as useful. If a check fails report and stop the batch. Stop/escalate unexpected local Linux kernel compilation in this owned build only; cancellation is authorized for that case. Do not cancel merely for silence and use no generic time limit. Fixture owns only disposable units and repositories; report leftovers on failure. Do not operate live sessions, reservations or deployments. Return passed/failed/incomplete, exact revision/commands, elapsed time, log paths, bounded failure evidence and any running process/unit. Parent will continue useful work and owns diagnosis.
