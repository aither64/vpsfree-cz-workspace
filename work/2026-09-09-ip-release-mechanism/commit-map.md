# Published commit series

Branch: `2026-09-09-ip-release-mechanism`.
The vpsAdmin series is based on upstream `15ae9175c`; the original unsplit heads
remain in local `-before-split` refs. Nothing has been merged into master.

| Commit | Responsibility |
| --- | --- |
| [be803e87b](https://github.com/vpsfreecz/vpsadmin/commit/be803e87b) | Shared relative `adjust_resource!`; preserve the absolute setter and cover non-IP consumers |
| [027a1033b](https://github.com/vpsfreecz/vpsadmin/commit/027a1033b) | Record and validate the environment charged for owned IPs |
| [382498ff6](https://github.com/vpsfreecz/vpsadmin/commit/382498ff6) | Serialize registration with network resource-identity changes |
| [d04af1047](https://github.com/vpsfreecz/vpsadmin/commit/d04af1047) | Shared IP/host reservation helpers and current ownership/assignment checks |
| [c2a2a1468](https://github.com/vpsfreecz/vpsadmin/commit/c2a2a1468) | Adopt relative IP accounting and combine deltas before deferred confirmation |
| [70b672da4](https://github.com/vpsfreecz/vpsadmin/commit/70b672da4) | Keep ownership until cleanup succeeds; preserve PTR/grant rollback and existing WebUI completion handling |
| [dc483b57a](https://github.com/vpsfreecz/vpsadmin/commit/dc483b57a) | Campaign API, schema, notices/reminders, current allocation counts, admin-only history, release safety, atomic bulk exemptions and operational documentation |
| [a8fa57999](https://github.com/vpsfreecz/vpsadmin/commit/a8fa57999) | Administrator/member WebUI, relevant sidebar actions, header selection, admin counts, attribution, translations and browser coverage |
| [58a9b71ea](https://github.com/vpsfreecz/vpsadmin/commit/58a9b71ea) | Separate test-only repair: skip occupied default IP fixture addresses after rolled-back examples advance auto-increment IDs |

The eight feature commits above retain their split; the ninth commit repairs an
unrelated CI fixture failure without changing production locking. The September 16
rebase preserves all six prerequisite patches and the fixture correction exactly;
only campaign API, WebUI and mail behavior changed in this follow-up.

The notification overlay is consolidated in
[f275bf35a](https://github.com/vpsfreecz/vpsfree-notification-templates/commit/f275bf35abc0dc501881b5af78b1e19fb98aec68).
The documentation contract pins the exact vpsAdmin head in
[2e5cb3b0](https://github.com/vpsfreecz/vpsfree-kb-contracts/commit/2e5cb3b078ff99805fbc42075ed45a05b576a8f2).

## Locking boundaries

Both mechanisms already exist in vpsAdmin. SQL row locks provide current state
and serialize preparation until the database transaction commits. Persistent
vpsAdmin resource reservations protect an IP, its hosts and deferred quota while
node work or rollback runs. No SQL transaction stays open while a node executes
cleanup, and campaigns hold no IP lock during the notice period.

The helpers live on IP/host models; generic Lockable and TransactionChain locking
interfaces are unchanged. The generic accounting addition shares validation with
the absolute setter. Its regression checks include absolute-value behavior,
CPU/memory/swap, dataset quota/refquota and automatic disk expansion.

See [locking-refactor-audit.md](locking-refactor-audit.md) and
[review-split-results.md](review-split-results.md). Current operator contracts are
in vpsAdmin `docs/ip-locking.md` and `docs/ip-release.md`, including writer rollout,
legacy charge reconciliation, deferred cleanup and manual contention retries.
