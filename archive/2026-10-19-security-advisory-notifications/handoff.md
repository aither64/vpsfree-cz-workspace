# Hourly advisory notifications: integration handoff

Bot94ac4eb5a7caf0456fff7df86a44cae198463276 is integrated into remote master;
configuration7ffa98a5761e001ed22b70fa24eecc21ff8c58ca is also integrated into
remote master. Both coordinated jobs succeeded, applied/verified, dependency enforced. No deployment or restart.

Modes individual/summary/off are implemented with backward-compatible default.
Site selects summary/3600 and pins the exact bot source/hash. Distinct new and
updated advisory IDs accumulate for an hour; new wins over updates. Empty
windows are silent, arrivals do not move the deadline, startup waits a full hour.
Pending counts are memory-only and lost on restart; old bot rollback restores
individual notice volume. These boundaries are documented in bot README/sample.

Independent final review and scoped fixes completed;150 specs, lint/hooks/static
checks, all8 clean VM examples and exact RSpec CI passed. Final refreshed config
evaluation and affected-container build passed without activation. See
final-acceptance.md, final-review.md and container-build-result.md.

Broader integration CI39325998761 is queued with no steps started; it is not a
failed test. Lead accepted the plan's exact local integration/build evidence for
user-authorized merges. CI observer remains owned by native utility thread
01a15612-1909-7391-a8df-8d86249b5a85, CLI handle11313. Its reports inferred
running from gh watch incorrectly; authoritative ci-final-queue-correction.json
and this handoff supersede those claims. Keep session active for eventual CI
feedback. No workflow rerun/cancellation, session closure or cleanup requested.

Bot job906818db-2123-48a0-86ab-9c9cfb736b0e succeeded. Config dependent job
55534397-1a91-40a0-a5d6-7e89628443f3 also succeeded; authoritative status in merge-status.json.
Preserve feature refs/worktrees, failed evidence and prepared receipts.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-19-security-advisory-notifications/)
