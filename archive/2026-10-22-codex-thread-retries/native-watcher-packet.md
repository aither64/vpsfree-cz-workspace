# Native verification utility: one operation

You are the fresh verification utility, not a roster member. Exact installed/retained utility policy: catalog840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa; model gpt-6-luna/low; utility dw_b9dd4137280d3e047a81fbdfe0ea73c900c9fd89f8861d12. Native behavior config /nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml: only assigned verification, no source edits/diagnosis/retry/approval/deploy. Execution full access danger-full-access/approval never under inherited executor policy, no sandbox root additions. Verify actual inherited policy before ready; report inability immediately. No nested agents. Read ~/.codex/skills/dev-session-monitor/SKILL.md watcher instructions.

Trusted session2026-10-22-codex-thread-retries, workspace /home/aither/workspace/ai/vpsfree.cz. Before session reads run dev-session current from work/2026-10-22-codex-thread-retries and verify both environment markers absent or exact pair. Read workspace AGENTS.md and applicable verification/lifecycle (tests only disposable) procedures plus A/B AGENTS.md, native-verification.md and this brief. Final independent review passed; last2 fixture-only fixes directly inspected per narrow rule; final composed graphs independently verified, no missing gate.

Exact final heads A d2d74f931cc50e39345c6c15931748062ee51951; B e0fb1238bd17cc3b29cc7d59ddaa9784c89ef939; W e6c2008a8f1215265fb8ceef3081a202570c30c6; C49397f0d8ec0c2c33a4e8a0285843445068fe0ca. Check A/B HEAD/clean before invocation; report mismatch, do not repair. Native binary /nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex wrapper SHA256 dd356114c45b6b78617be9da9c21ab6d284a8d3c7de1e5a39abf45be2cabed8b, underlying libexec/codex/bin/codex SHA2565e538cfe7c25daf382afe195c08b2ffd24415b0cdd7f5456ec0cf1d277c3d1a5. Record actual version/hash. No live workspace socket/state/credentials/model policy service; fixtures are private noauth synthetic loopback, test owns private native cleanup.

RUN=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-22-codex-thread-retries/native-verification/run-1-e0fb1238
Create RUN0700, logs0600 (umask077); own this related two-command batch. Preserve exact stdout/stderr/exit+elapsed separately. No new overall timeout beyond native go-test5m per command; Nix shell preparation no invented quiet timeout. Run BOTH independent commands once sequentially (test failure not safety escalation may proceed to second); no reruns/retries/command edits. Working dirs exact below, B shell supplies Go. Set TMPDIR=/tmp for known socket-length limit, capture env fact. No repository writes.

A=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/codex-web
B=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-codex-thread-retries/dev-workspace
NATIVE=/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex

cwd A:
TMPDIR=/tmp nix develop "$B" -c env CODEX_WEB_TEST_BINARY="$NATIVE" go test -mod=readonly ./codex -run '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract)$' -count=1 -json -timeout=5m
stdout library.jsonl, stderr library.stderr, exit library.exit, elapsed library.elapsed under RUN.

cwd B/portal:
TMPDIR=/tmp nix develop "$B" -c env LIVE_SWITCH_CODEX="$NATIVE" go test -mod=readonly -tags=live_switch_integration ./cmd/workspace-portal -run '^TestNative(LiveSwitchReconnect|TurnRetryController)$' -count=1 -json -timeout=5m
stdout runtime.jsonl, stderr runtime.stderr, exit runtime.exit, elapsed runtime.elapsed under RUN.

Expected exact A top2: TestPinnedCodexRecoveryRemainsColdUntilActivation; TestPinnedCodexFailedTurnRetryContract. Latter subcases ALL required: nonempty_continuation_default, nonempty_continuation_plan, exact_cyber_terminal, automatic_queue_uses_execution_context, lost_accepted_reply_recreated_client, native_direct_busy_race_compatibility. B top2: TestNativeLiveSwitchReconnect, TestNativeTurnRetryController (latter no named subcases). Parse gojson complete selected pass/skip/fail inventory, assert expected names/subcases present and pass/no skip/zero-match. Preserve failure evidence rather than fixing. Native direct race accepting/replacing busy task must be reported failed compatibility gate, no diagnosis/waiver.

Escalate unexpected local kernel build, production egress/foreign socket/credential access: authorized cancel ONLY your owned fixture command/process on such safety escalation, retain logs/process identity. Never stop session/registered services/foreign process; quiet output no cancellation. No source edits, diagnosis, retries, CI/deploy/claims/merge/cleanup beyond test-owned private fixture cleanup. No initiative state edits; allowed logs/result manifest only under RUN. Report launch policy/ready, then concise completion passed/failed/incomplete, exact exits/cases/head/version/hash/elapsed, complete log paths+bounded failures and any still-running owned process. Remain accountable for your tool handles; return automatically to lead on completion.
