You are a fresh gpt-6-luna/low verification utility, not a team member. Read
/home/aither/.codex/skills/dev-session-monitor/SKILL.md and follow its watcher
instructions. Installed catalog digest
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa defines this utility
and full_access. Native config is
/home/aither/.local/state/dev-workspaces/profile/share/dev-workspace/agent-teams/utilities/verification_watcher-low.toml.
Your actual launch uses full-access tools; do not change access. Do not edit source,
diagnose, retry, approve, deploy or spawn agents. Keep waits <=60 seconds. Run
these independent checks, in parallel when practical, and own their handles.
Capture full logs and exact exit statuses separately under
/tmp/message-delivery-reliability-2026-10-25/ using names below. Return promptly
with raw results, exact tested heads, elapsed time, log/status paths, and bounded
failure excerpts. No generic quiet timeout or unrelated cancellation is authorized.
Stop an owned local Nix build if it unexpectedly starts compiling Linux itself
(kernel sources/config are unchanged), retaining its evidence and escalating.
No live service mutation is authorized. All Go native tests own disposable state.

1. In /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace:
nix build --no-link --print-build-logs .#packages.x86_64-linux.default.goModules
Log/status: post-review-vendor.log/.exit. lib.fakeHash is intentional; expected
exit 1 with exact actual hash. Do not fix the hash or retry.

2. In /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace:
nix develop --command env TMPDIR=/tmp/md26 DEV_WORKSPACES_CODEX_PROVIDERS=/tmp/message-delivery-reliability-2026-10-25/absent-provider-catalog.json go -C portal test -mod=readonly ./... -count=1 -timeout=180s
Log/status: post-review-portal.log/.exit. Source has all three CI fixture fixes
and selects final codex-web 0d17f1e347c4592f5a4159ef384106ad287275a2.

3. In /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/codex-web at exact head 0d17f1e347c4592f5a4159ef384106ad287275a2:
nix develop --command env TMPDIR=/tmp/md26 CODEX_WEB_TEST_BINARY=/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex go test -mod=readonly ./codex -run '^TestPinnedCodex(RecoveryRemainsColdUntilActivation|FailedTurnRetryContract|HeadlessTeamContract|EphemeralProviderSelection)$' -count=1 -timeout=300s
Log/status: post-review-native.log/.exit. Do not point at a live socket. The tests
start their own native App Servers and synthetic Responses provider.
