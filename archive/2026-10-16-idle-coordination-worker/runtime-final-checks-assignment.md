Fresh verification utility: gpt-6-luna / low under explicit workspace watcher policy. Read /home/aither/.codex/skills/dev-session-monitor/SKILL.md, root docs/agent-instructions/verification.md and runtime AGENTS.md before execution. No edits, diagnosis, retry, approval, deployment or nested agents. Review findings are fixed and focused checks passed. Original package build passed at ced31b5f; final source only corrects an asynchronous fixture observation race, documented in review-remediation.md.

CWD: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/dev-workspace
Committed final revision: ced8e76ec73fbc4809ac30af60903874590b82f6
Logs and .status files: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/

Execute one batch sequentially; stop and report on first failure, preserve exact status and full logs, no retries:
1. nix develop --command ruby test/background_integration_systemd_test.rb -n /systemd/ ; logs systemd-final.log and .status
2. nix build --no-link --print-out-paths --print-build-logs .#checks.x86_64-linux.package .#checks.x86_64-linux.host-package-contract ; logs runtime-final-package.log and .status
3. Obtain exact built package path with nix eval --raw .#checks.x86_64-linux.package.outPath, retain path in runtime-final-package.path, then run nix develop --command go -C portal run -mod=readonly /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/native-notification-check.go EXACT_PACKAGE_PATH ; logs native-notification.log and .status. This runs only isolated local Codex, disposable private HOME/state/thread manifests, synthetic local HTTP provider, no real credentials/model calls/live sessions. Script owns and stops its private app-server process group and removes its temp directory. On failure collect bounded evidence, report any leftovers; do not rerun or modify.
4. nix develop --command go -C portal test -mod=readonly ./cmd/workspace-portal -run '^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$' -count=1 ; logs notification-protocol.log and .status

Escalate and cancel only an unexpected Linux kernel compilation in this owned build. No timeout merely for silence. Report exact revision, command/status, elapsed time, logs, bounded failure evidence and any still-running owned operation or unit. Parent resumes automatically.
