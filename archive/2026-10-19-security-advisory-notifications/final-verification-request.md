# Final verification command batch

Both intended deliverables are committed, quick checked and independently
reviewed. Important bootstrap finding and YAML quoting advisory remediated under
reviewer-approved step9 narrow-fix policy; lead directly inspected diff/tests.
Config pin mechanically refreshed and clean rebased with exact '=' range-diff.
No deployment or service restart. User authorized merges only after verification.

Fresh Luna/low utility uses pinned utility model/effort/native identity and
full-access execution per dev-session-monitor. Read that skill and the existing
verification-brief.md. Own execution/tool handles/logs for this one related batch.
Do not edit source/tracking, diagnose, retry, approve, deploy or spawn agents.

Exact tested revisions:
- bot worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-irc-bot
  HEAD 49a8ff8086b7b325f9f1a8f4825619f8e03245ce
- config worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-19-security-advisory-notifications/vpsfree-cz-configuration
  HEAD e30cd3399c5f57fd792afa4147d293307227d9b4

Run sequentially, stop after first failure and report evidence without retry:
1. Config final scoped evaluation:
   nix develop -c nix eval --impure --json --file /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications/config-eval.nix
   Store final-config-eval.stdout/log/exit. Shell emits a banner; keep raw output.
   Report success milestone promptly so lead can inspect actual output.
2. Bot targeted integration:
   ./test-runner.sh test vpsadmin-events
   Store final-bot-integration.log/exit, preserve runner output/state paths.
3. Config exact affected container build without activation:
   nix develop -c confctl build 'cz.vpsfree/containers/int.vpsfbot'
   Store final-config-build.log/exit and produced derivation/output identity.
4. Observe already-created exact-head bot CI, no manual dispatch:
   RSpec 39317498639, Integration Tests 39317498503 in vpsfreecz/vpsfree-irc-bot,
   both head 49a8ff8086b7b325f9f1a8f4825619f8e03245ce. Use repository Nix gh.
   Keep exact gh view/status/log outputs under this session; if failures,
   retrieve available failed logs/artifacts without rerun; report promptly.

All evidence lives beneath /home/aither/workspace/ai/vpsfree.cz/work/2026-10-19-security-advisory-notifications/.
No invented timeout for quiet builds. Authorized cancellation applies ONLY to
owned local verification process tree if unexpected local Linux kernel build
begins; report exact drv/cache evidence so owner can investigate. No kernel work
is intended. Never cancel unrelated work or current CI just for queue delay.
If CI remains queued with no actionable evidence, report incomplete and keep
ownership/observing; parent decides next action. Keep progress reports bounded,
material milestones or escalation only; parent does not duplicate your polling.
