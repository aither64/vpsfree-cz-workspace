# Risk and compatibility review

Reviewed the high-risk committed series from the packet:

- `codex-web` `de83e9c7..152e3530`
- `dev-workspace` `dc8d6cf7..16c3d78f`
- `vpsfree-dev-workspace` `b37edd0f..286a1f1b`
- workspace `94ca59f3..f5aa81ce`
- `vpsfree-cz-configuration` `b4e12029..ecf8a52d`

The review treats the development-host operator as trusted, as required by the
repository boundary. The findings below concern remote request ordering,
ordinary persistence failures, and supported lifecycle races; they do not rely
on hostile local filesystem replacement.

## Blocking

### An accepted initial prompt can lose its file before attachment retention becomes durable

Commit: `dev-workspace` `16c3d78f`.

`portal/internal/web/server.go:934-947` prepares the initial attachment
association, then calls `acceptCreation`, which durably saves the creation
receipt and starts the creation worker, and only afterwards calls
`RetainCreations`. The preparation is deliberately stored as `prepared`
(`portal/internal/uploads/store.go:719-724`). Draft deletion ignores both
`prepared` submissions when it gathers references and when it decides whether
deletion is blocked (`portal/internal/uploads/store.go:592-596` and
`portal/internal/uploads/store.go:621-628`). The creation mutex does not close
this gap because draft DELETE requests do not acquire it; both requests merely
hold shared workspace-transition locks.

Consequently a concurrent DELETE can tombstone and unlink the file after
`Prepare` returns but before `RetainCreations` commits. The creation receipt is
already accepted and its worker can already be sending the frozen path to
Codex. `RetainCreations` then changes the submission to `pending` without
checking that every referenced file is still ready
(`portal/internal/uploads/store.go:928-946`). A catalog-write failure after
creation acceptance creates the same exposed interval on retry. The durable
session request can therefore refer to bytes that the portal has already
deleted, violating the accepted creation and recovery contract.

The transition from editable draft to accepted creation needs one recoverable
ordering boundary: deletion must either observe the accepted reservation and
refuse, or acceptance must not become durable/start its worker until attachment
retention is durable. Add a race/partial-failure test that interleaves draft
deletion between preparation, creation acceptance, and retention.

## Important

### Queue deletion cannot recover when attachment cancellation persistence fails

Commit: `codex-web` `152e3530` together with `dev-workspace` `16c3d78f`.

The HTTP handler first completes the App Server queue deletion and only then
marks the attachment submission cancelled
(`codex-web/conversation/handler.go:617-625`). The Codex client durably clears
its queue deletion and submission-attempt records once the queue is absent
(`codex-web/codex/client.go:3511-3535`, `codex-web/codex/client.go:3574-3576`,
and `codex-web/codex/client.go:2209-2242`). If the subsequent upload-catalog
transaction fails, `QueueDeleted` leaves the attachment submission `queued`
(`dev-workspace/portal/internal/uploads/store.go:794-804`).

After that partial completion, retrying the same HTTP deletion finds neither a
queue entry nor a retained Codex deletion attempt and returns "queued message
was not found" before calling `QueueDeleted`. Queue observation also cannot
repair it because the deleted entry is absent. The stale `queued` record then
blocks file deletion indefinitely at
`dev-workspace/portal/internal/uploads/store.go:626-628`, despite the real queue
being empty. Make queue cancellation reconciliation idempotent across the two
persistent stores and test a catalog failure after the App Server deletion has
succeeded.

### Terminal creation conflicts permanently pin their accepted draft files

Commit: `dev-workspace` `16c3d78f`.

Initial files are changed from `prepared` to `pending` immediately after the
portal accepts the request (`portal/internal/web/server.go:940-949` and
`portal/internal/uploads/store.go:928-946`). The existing creation workflow can
later prove that another writer created the destination and make that receipt a
terminal `conflict` (`portal/internal/web/creation.go:224-258`). No upload
transition accompanies this outcome. `retainCreationUploads` also collects
goals from every cached receipt without filtering terminal conflicts
(`portal/internal/web/uploads.go:188-197`).

The abandoned request's submission therefore remains `pending`: collection
pins it forever (`portal/internal/uploads/store.go:811-827`), DELETE refuses it
as unresolved (`portal/internal/uploads/store.go:621-628`), and the draft cannot
be used under the replacement name because its scope is bound to the conflicted
slug (`portal/internal/web/uploads.go:108-124`). This leaks session and workspace
quota and leaves the user's uploaded input trapped behind a request the UI says
cannot be retried. Reconcile `conflict` into an explicit releasable/cancelled
attachment state, preserving retry retention only for creation states that can
still complete, and cover the existing external-writer conflict scenario with
files attached.

### Draft expiry never reclaims scope or submission capacity

Commit: `dev-workspace` `16c3d78f`.

Every `POST /api/upload-drafts` permanently adds a scope record
(`portal/internal/web/server.go:392-398`,
`portal/internal/web/uploads.go:99-105`, and
`portal/internal/uploads/store.go:211-225`). Collection marks old unpinned file
records deleted and unlinks their directories, but it never removes draft
scopes, expired file records, or obsolete `prepared`/`cancelled` submissions
(`portal/internal/uploads/store.go:808-854`). New drafts and submissions use the
raw map lengths as hard admission limits
(`portal/internal/uploads/store.go:214-215` and
`portal/internal/uploads/store.go:684-685`).

Thus 10,000 empty draft requests, requiring no uploaded bytes, permanently
disable draft creation for the workspace. Normal repeated rejected drafts and
expired uploads eventually have the same effect, and deleting files does not
restore capacity. This turns the metadata bound into a persistent authenticated
availability failure and makes seven-day draft expiry incomplete. Reclaim
records that have no live ownership or display/recovery obligation, while
retaining tombstones that are still needed to render shared historical
references, and test that expiry/session deletion restores admission capacity.

## Advisory

No additional advisory findings.

## Compatibility and residual validation

The committed pins consistently select `codex-web` `152e3530` and runtime
`16c3d78f` through the organization, workspace, and host-configuration
consumers. The separate schema-1 upload catalog is ignored safely by older
packages; prompt paths remain ordinary text; completed deletion history gives
newer collectors evidence to reclaim files after a deletion performed by an
older package. Chunk write, completion, tombstone-before-unlink, explicit
session deletion, fork reference, and slug-reuse ordering otherwise have sound
recovery structure in the reviewed code.

The planned real-browser 1 GiB transfer, live App Server acceptance, rollback,
and deployment checks remain necessary after the Blocking and Important
findings are resolved or explicitly decided. The documented native-terminal
idle requirement remains an accepted residual boundary because there is no
cross-client lease in the unchanged App Server protocol.
