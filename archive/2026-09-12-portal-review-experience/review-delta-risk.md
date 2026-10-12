Review result: **0 Blocking, 1 Important, 1 Advisory.**

## Findings

### Important — An archived canonical session can remain hidden behind a paused creation receipt

Commit `1de0a78d` introduced a reconciliation dead end across lifecycle and package-generation boundaries:

- [`proveCreation()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:323) rejects every archived destination, even when its receipt evidence and identity otherwise match.
- [`canonicalCreationConflict()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:149) does not check `summary.Archived`. For an exact matching new/plan journal, or an exact fork with completion evidence, it returns false and preserves the paused/failed receipt as “recoverable.”
- That receipt intercepts the canonical page before `session.Find()` through [`creationPage()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/server.go:746).
- Recovery is impossible: new/plan retry rejects an existing archived destination in [`prepare_creation_journal()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2476), while fork retry similarly refuses archived destination reuse at [`dev-session:1096`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:1096).
- The receipt cannot retire naturally because [`retireAbsentCreation()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_store.go:167) only considers ready/conflict receipts and treats the archive as existing state.

A concrete sequence is: head persists a validated receipt/binding, rollback completes the matching session under the old package, the session is archived, then head is restored. The receipt remains paused, the archived session page is hidden, and retry repeatedly fails. A similar window exists when receipt-bound completion evidence is written but the terminal receipt update is interrupted before archival.

This violates the stated guarantee that additive receipt state cannot shadow a canonical session across rollback. Reconciliation should classify archived/terminal canonical destinations before the “matching active request may be recoverable” branch, producing a non-blocking conflict or another terminal state. Add head→base completion-and-archive→head regressions for new, plan, and fork requests, including both present and absent completion evidence.

### Advisory — Deleted threads leave permanent per-turn activity files

Commit `4dde3c6a` bounds hot checkpoints and writes compact data, but lifetime storage remains unbounded:

- Every finalized turn receives a separate persistent file in [`writeCheckpoint()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity_store.go:275).
- [`retire()`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/codex-web/codex/activity_store.go:424) only closes and evicts the in-memory thread state; it never removes persistent files.
- The runtime monitor stores these under a socket-keyed operation directory at [`activity.go:42`](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/activity.go:42), with no lifecycle cleanup for fully deleted sessions.

Archived histories intentionally need retention, but deleted sessions and superseded socket authorities accumulate unreachable thread directories and one inode per recorded turn. Repeated creation/deletion can therefore grow the portal’s private operation store indefinitely. Define an explicit retention policy or exact-identity deletion cleanup, with a regression proving deletion/name reuse cannot expose old activity.

## Residual risks and test gaps

- The packaged VM, live profile upgrade/rollback, and actual browser/App Server creation tests remain pending. They should follow reconciliation of the Important finding.
- Passive observation has only synthetic/schema coverage so far. The real pinned App Server still needs validation with simultaneous interactive and observer clients, including server-originated requests, reconnects, and shutdown.
- This review was read-only and ran no tests, as requested.
