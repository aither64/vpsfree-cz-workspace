# Packaged verification operation

Read ~/.codex/skills/dev-session-monitor/SKILL.md and follow its watcher role.
Scope is this one verification batch, not source edits or deployment.
Workspace guidance: AGENTS.md and docs/agent-instructions/verification.md.
Read each repository's AGENTS.md. Only the three owned worktrees below apply.

After the parent explicitly authorizes launch following independent review, run:

1. dev-workspace: `nix flake check --print-build-logs --keep-going`
2. workspace: `nix flake check --print-build-logs --keep-going`
3. vpsfree-cz-configuration: `nix develop --command confctl build cz.vpsfree/machines/aitherdev`

All worktrees are under
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-17-team-delegation/.
Capture complete separate logs and exact exit statuses in
/home/aither/workspace/ai/vpsfree.cz/work/2026-10-17-team-delegation/.
Record each exact tested git head and elapsed time. These are independent checks;
run concurrently where safe, inspect every result, and do not retry failures.
Preserve all owned process/session handles until completion or parent takeover.
Do not impose a time limit for quiet builds. If an unexpected local Linux kernel
build begins, cancel only the exact owned operation and report its identity and
bounded evidence. Do not change source, diagnose failures, approve, deploy,
create nested agents or mutate tracking/portal metadata.

Return pass/fail/incomplete for each command, exit statuses, exact heads, elapsed
time, log paths and a bounded failure excerpt. Report any still-running operation.

Launch is now authorized: review is complete, all findings are fixed and
verified under the narrow-fix rule, and all final sources are committed. Exact
heads are in final-heads.json; verify them before execution. Also inspect only
GitHub Check runs for aither64/dev-workspace at that exact final runtime head,
record the run ID and conclusion after the local batch, and retain failure
evidence without retrying. Superseded run cancellation is unavailable (token 403).
The installed utility policy comes from package
/nix/store/xg4abbjjr98f0b26m634b2r51qrr6hr3-dev-workspace-0.2.0, catalog
437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd, native utility
share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
Use exactly GPT-6 Luna/low and a fresh context.
