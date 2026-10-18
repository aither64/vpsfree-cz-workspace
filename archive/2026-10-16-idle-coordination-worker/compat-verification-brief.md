# Final verification batch

Fresh utility policy: installed catalog 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd, utilities.verification_watcher, gpt-6-luna/low/workspace_write; behavior share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml. Read dev-session-monitor skill and applicable root/repository verification guidance before running. No source/tracking edits, diagnosis, retries, approvals, deployment or nested agents. Logs and result artifacts below are allowed. Review completion is a prerequisite; lead launches only after findings reconciled.

Final revisions in compat-final-heads.json. Require exact clean HEAD before each operation. All paths absolute beneath /home/aither/workspace/ai/vpsfree.cz. Worktrees under worktrees/2026-10-16-idle-coordination-worker/. Evidence under work/2026-10-16-idle-coordination-worker/, using compat- prefix; preserve old evidence. New local executions are owned by this watcher. Never activate or resume integration drivers.

Related checks, run independently where practical and report ordinary failure promptly, preserving status/logs without retry:

1. Runtime: nix build --print-build-logs --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/compat-runtime-result .#checks.x86_64-linux.package .#checks.x86_64-linux.host-package-contract
2. Workspace: nix build --print-build-logs --out-link /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/compat-workspace-result .#packages.x86_64-linux.default .#checks.x86_64-linux.deployment-contract .#checks.x86_64-linux.agent-instructions
3. Configuration: nix develop --command confctl build --yes cz.vpsfree/machines/aitherdev
4. Runtime systemd fixture: nix develop --command ruby test/background_integration_systemd_test.rb -n /systemd/
5. After runtime package succeeds, obtain package path via nix eval --raw .#checks.x86_64-linux.package.outPath. Run isolated native fixture: nix develop --command go -C portal run -mod=readonly /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/native-notification-check.go EXACT_PACKAGE_PATH. This program uses disposable isolated local Codex state/threads, synthetic localhost provider, no real credentials/model calls/live sessions, and owns/removes its local process group/temp directory.
6. Runtime notification protocol: nix develop --command go -C portal test -mod=readonly ./cmd/workspace-portal -run ^TestCoordinationNotificationRetainsSettingsAndDeduplicatesNativeDelivery$ -count=1
7. CI: exact aither64/dev-workspace run 39014845298 at 543136a0e3be561e010d8b2ccd309f2ad37311a0. Use pinned nix shell --inputs-from . nixpkgs#gh -c gh run watch 39014845298 --repo aither64/dev-workspace --exit-status. On failure collect exact logs/artifact metadata without retry. Do not cancel other runs.

No silence timeout. Escalate and stop only an unexpected local Linux kernel compilation in this owned build (cancellation expressly authorized for that process only); no kernel change intended. Maintain ≤60-second bounded waits. Preserve full stdout/stderr and exact statuses, report elapsed time/revision/command identity, failure excerpt, any still-running operation. Return raw evidence; lead decides acceptance and diagnoses.
