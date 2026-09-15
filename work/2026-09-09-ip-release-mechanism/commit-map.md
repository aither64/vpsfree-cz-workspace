# Published commit series

Branch: `2026-09-09-ip-release-mechanism`.
The vpsAdmin series is based on upstream `564cc80ea`; the original unsplit heads
remain in local `-before-split` refs. Nothing has been merged into master.

| Commit | Responsibility |
| --- | --- |
| [31279b202](https://github.com/vpsfreecz/vpsadmin/commit/31279b202) | Shared relative `adjust_resource!`; preserve the absolute setter and cover non-IP consumers |
| [84e77e2bf](https://github.com/vpsfreecz/vpsadmin/commit/84e77e2bf) | Record and validate the environment charged for owned IPs |
| [660f74271](https://github.com/vpsfreecz/vpsadmin/commit/660f74271) | Serialize registration with network resource-identity changes |
| [99bc2123c](https://github.com/vpsfreecz/vpsadmin/commit/99bc2123c) | Shared IP/host reservation helpers and current ownership/assignment checks |
| [0417b8cbf](https://github.com/vpsfreecz/vpsadmin/commit/0417b8cbf) | Adopt relative IP accounting and combine deltas before deferred confirmation |
| [a8b8f9233](https://github.com/vpsfreecz/vpsadmin/commit/a8b8f9233) | Keep ownership until cleanup succeeds; preserve PTR/grant rollback and existing WebUI completion handling |
| [72aebfd83](https://github.com/vpsfreecz/vpsadmin/commit/72aebfd83) | Campaign API, schema, notices/reminders, release safety, atomic bulk exemptions and operational documentation |
| [a75bb80d5](https://github.com/vpsfreecz/vpsadmin/commit/a75bb80d5) | Administrator/member WebUI, sidebar actions, one campaign-wide address table, attribution, translations and browser coverage |

The notification overlay is consolidated in
[715c063396](https://github.com/vpsfreecz/vpsfree-notification-templates/commit/715c063396fa49277852b98d36347c8bec5160d3).
The documentation contract pins the exact vpsAdmin head in
[7222baa58](https://github.com/vpsfreecz/vpsfree-kb-contracts/commit/7222baa580476ce7f9c5c02deabece2744d92f9b).

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
