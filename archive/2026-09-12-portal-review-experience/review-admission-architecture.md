Review result: **0 Blocking, 1 Important, 0 Advisory**.

## Important — Completed deletions remain globally “unfinished” until their exact slug is accessed

Commit `2d589990` recognizes that a completed deletion supersedes an older paused or failed creation, but reconciliation is attached only to an exact-slug request:

- [`retireAbsentCreation`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:168) looks up only `s.creations[slug]`.
- Its callers are the same-slug acceptance path in [`acceptCreation`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:95) and same-slug status lookup in [`currentCreation`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:203).
- Global capacity reclamation in [`retireReadyCreations`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:99) considers only `ready` and `conflict`; paused and failed receipts remain counted as unfinished even when [`FindCompletedRemoval`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/session/removal.go:34) would prove them terminal.
- Startup loading likewise performs no completed-deletion reconciliation; it only invokes `retireReadyCreations(0)` at [`creation_store.go:279`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:279).

Concrete failure scenario:

1. A creation reaches the destination but remains `paused` or `failed`.
2. The destination is subsequently deleted, producing valid completed-removal evidence.
3. The user does not revisit or retry that exact slug.
4. Repeating this over the service lifetime leaves 512 logically terminal receipts in the cache.
5. A creation for an unrelated new slug calls exact-slug cleanup only for that new slug. Capacity enforcement finds no `ready` or `conflict` entries to retire and returns `too many unfinished session creations`.

This recreates a lifetime-wide admission failure at the bounded-receipt layer. Recovery currently depends on knowing and individually accessing deleted slugs, even though deletion recovery is already the persistent authority for their terminal status.

The creation store should own global reconciliation of deletion-terminal receipts. A suitable repair would sweep non-running receipts under their per-slug runtime locks, using the existing destination, authority, journal, timestamp, and exact-receipt checks, before startup/capacity enforcement. Alternatively, deletion completion can retire the portal state directly, but startup reconciliation is still needed for CLI deletion, interruption, and portal downtime.

Add a capacity-boundary test containing paused/failed receipts with valid completed-removal markers. It should prove that an unrelated creation is admitted while receipts without conclusive deletion evidence continue to block retirement.

## Architecture assessment

The admission changes in `83770217` have appropriate ownership:

- The provider applies the four-slot limit to all connected observer RPCs, starts timeouts after admission, and binds queued work to the live connection generation.
- The fixed restore workers use that same admission path rather than establishing a second reconnect budget.
- Disconnect and `Close` cancel queued work.
- The portal’s gate at [`activity.go:70`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:70) is not redundant provider policy: it governs a higher-level activity read that may issue multiple RPCs and applies the necessary per-thread ordering before consuming a global unit-of-work slot.

I found no conflicting scheduler, hidden bypass, or duplication-drift finding in that path.

The completed-deletion predicate is necessarily enforced on both sides of the process boundary: the portal retires receipts, while [`reject_deleted_portal_creation!`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2871) prevents already queued CLI work from recreating a deleted identity. Their timestamp, workspace, slug, marker-state, preserved-tracking, and exact-retired-ID rules agree in the reviewed delta.

The downstream organization and workspace changes are mechanical pins. I found no additional API, schema, deployment, or ownership divergence in their direct consumer chain.

The recorded trusted-local-operator boundary was respected. I did not treat filesystem manipulation by that operator as an adversarial condition; remote request validation and persistent-state consistency remained in scope.

I inspected the committed ranges named in the [review packet](/home/aither/workspace/ai/vpsfree.cz/work/2026-09-12-portal-review-experience/review-admission-deletion-packet.md), their commit series, direct consumers, plans, initiative state, and prior review context. Per instruction, I made no edits or Git mutations and ran no tests. Long package, VM, browser, live upgrade, and rollback acceptance therefore remain residual validation work.