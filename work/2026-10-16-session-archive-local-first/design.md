# Archive reliability design and verification brief

Lead owns this design and application edits; the threadless initiative has no
retained roster. The accepted user choices are local closure before Git commit
success and coalescing pending bookkeeping to the latest state.

## Recovery and cleanup

Keep existing full-copy recovery readable. New captures use a versioned Git
representation only when the checkout is clean and has no untracked or ignored
entries; retain exact HEAD, administration/index, content digest and permissions.
Restore tracked files from retained Git objects and restore recorded permissions.
Other checkouts keep full copies. Pin additional staged objects in a batch,
excluding objects already retained by HEAD. Preserve staged/conflicted indexes.

Split cheap ownership/ref/tracking checks from expensive checkout-content checks.
Capture verifies its output. Immediately before each removal, verify only that
checkout and recovery. Retries verify retained recovery once, reconcile proved
path/registration absence, and never recapture or rewrite completed restoration.
Tracking digests may be reused only within the invocation after comparing a fresh
metadata inventory (paths, types, modes, sizes, inode, mtime and ctime); changes
force a fresh digest. Stream large files, preserving existing digest bytes.

## Local completion and tracking synchronization

New archive/revive journal versions replace the commit prerequisite with a durable
tracking-saved milestone. Existing journals retain their old phase and commit
policy. Persist a private workspace-scoped per-session tracking-sync receipt
before retirement. It records the exact local transition and pending/synced/error
status. Local proof, not Git ancestry, permits completing new operations. Keep
archived receipts after sync to distinguish locally closed archives from legacy
Git-proven archives. Sensitive sessions remain excluded from Git bookkeeping.

A workspace user service retries pending receipts with backoff. Acquire existing
creation/session locks and the shared tracking-commit lock in normal order. Read
the latest coalesced destination; use ordinary owned-path Git commit/hooks with
bounded fetches. Preserve unrelated staged/working files. Errors update sync
status without reopening or failing the archive. Revival replaces the pending
archive transition under the same session lock and can proceed offline.

## Supervision and presentation

Portal archive execution runs in a per-attempt systemd user job. Its unit name
binds the portal receipt and attempt; systemd retains execution/result and journal
logs. This uses existing manager supervision rather than a second private job
queue. Portal restart/disconnect does not cancel the worker. Reconcile exact
unit status and admit its CLI authorization only against the saved portal receipt.
CLI stays synchronous without a total wall-clock
deadline. External calls retain bounded timeouts. Expose current capture/verify/
removal progress and separate tracking-sync state. Preserve terminal cause in
errors, and separate operation finish time from journal progress time.

## Compatibility and deployment

Retain legacy archive/revive journals and snapshots. Add runtime capabilities for
Git recovery and deferred tracking; both selected-host and candidate checks must
refuse unsupported persisted state. The selected host enables deferred tracking
together with its retry timer. Source executors without that installed worker
retain synchronous bookkeeping unless explicitly configured. Portal receipt
schema 2 separates finish time from progress; its reader retains schema 1.
Old and new commands retain generation and
ownership locks. Existing cluster/coordinator/manifest contracts stay authoritative.
No database, service protocol or vpsAdminOS fleet upgrade is involved. API status
additions are additive; old journal phase readers remain. Recover the original
operation with the selected CLI before profile changes.

Deploy exact published runtime through the workspace's nested input and
configuration's dev-workspace/devWorkspace channel. Build and review before
coordinated system activation, then application profile activation, under the
aitherdev reservation. Configuration/default-branch integration is not approved.
Keep rollback evidence and recover forward with a compatible generation.

## Acceptance

Quick focused Ruby/Go/browser checks precede committed independent review.
Long package and scale/restart tests follow it. Cover clean large checkouts,
dirty/untracked/ignored/binary/conflicted-index restoration, corruption, ownership,
interruption after removal, network/hooks/remote-master failures, pending-sync
revival, portal restart and incompatible package refusal. Measure Git invocation
counts, copied bytes and full-content verification passes, not only elapsed time.
Keep deployment tests and original-session recovery evidence revision-bound.
