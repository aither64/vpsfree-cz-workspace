# General change review

Reviewed the complete committed ranges from the packet:

- `codex-web`: `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117..152e353057c6da97c7bbb9ae4393075a2f8cc423`
- `dev-workspace`: `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd..16c3d78faf6351c6a0a79c479fae2ca36cc3de78`
- `vpsfree-dev-workspace`: `b37edd0f63fb7a984ba634c2d52d08e9344304b4..286a1f1b9c54d5b625712174df47975727d62193`
- workspace: `94ca59f3f9d17306c2cc5e61099d83313309f4df..f5aa81ce3baf7f4b03d4109d0c5c7df4a0d2db76`
- `vpsfree-cz-configuration`: `b4e120294696578c3871124259f266205bad4393..ecf8a52d640407b2e640cf11a70c7f8e6669b528`

I read each repository's `AGENTS.md`, the plan, state and review packet, every
commit and changed path, the shared Go/browser attachment contract, runtime
catalog and lifecycle integration, focused tests, documentation, and all
consumer pin changes. The pin commits and generated configuration commit are
focused and follow their repository rules.

## Blocking

### 1. Draft expiry never reclaims catalog records, making the record bounds a permanent upload failure threshold

Commit `16c3d78faf6351c6a0a79c479fae2ca36cc3de78` creates and persists a new
scope on every `NewDraft` call, and refuses all further drafts once the map has
10,000 entries (`portal/internal/uploads/store.go:166-167,211-225`). The index
automatically calls this endpoint whenever the browser has no reusable draft,
including after a successful creation adopts the prior draft
(`portal/internal/web/static/app.js:961-987`). However, `Collect` only marks
file records deleted and unlinks their directories; it never removes expired
draft scopes, deleted unsubmitted file records, or their prepared submissions
(`portal/internal/uploads/store.go:808-855`). There is no deletion from any of
the three catalog maps anywhere in this package.

This turns the documented 10,000-record bound into a lifetime quota rather than
a bound on live/recoverable state. Ordinary session creation and cleared or
private browser storage steadily consume it, and an untrusted same-origin
browser can exhaust the entire workspace with 10,000 empty
`POST /api/upload-drafts` requests. At that point every legitimate draft fails
with 507 permanently; deleted/expired file records can similarly make
`Backend.Create` fail its `len(data.Files) >= maxRecords` check
(`portal/internal/uploads/store.go:427-428`). Waiting seven days does not
recover capacity despite the accepted draft-expiry behavior.

Reclaim empty and expired draft scopes and unsubmitted file/submission records
once no accepted creation or prompt can refer to them. Preserve only the
tombstones and associations needed to render durable sent history. Add a
restart-aware regression that creates and expires draft-only metadata, proves
the records are removed, and proves new uploads can use the recovered capacity.

### 2. The runtime feature commit bundles independently reviewable storage, browser, and destructive lifecycle changes

Commit `16c3d78faf6351c6a0a79c479fae2ca36cc3de78` combines a new 971-line
persistent store (`portal/internal/uploads/store.go`), the upload HTTP and
conversation adapter (`portal/internal/web/uploads.go`), initial-creation and
browser submission behavior (`portal/internal/web/creation.go` and
`portal/internal/web/static/app.js`), and fork/session-deletion behavior in the
Go CLI and Ruby lifecycle journal (`portal/cmd/workspace-portal/main.go` and
`libexec/dev-session`). The packet calls these one feature but gives no
concrete reason why those parts are inseparable. Each part has a distinct
failure and rollback boundary and already has focused tests that can review it
independently: store/transport, prompt and browser integration, and lifecycle
retention/fork/deletion.

The mandatory general-review policy requires independently reviewable changes
to be split and classifies unexplained bundling as Blocking. Rewrite this
unmerged commit into functional commits that introduce and test those final
behaviors directly. Keep the existing provider-pin commit separate and update
the downstream pins after the final runtime head is rewritten.

## Important

### 3. A catalog failure after queue deletion leaves an association that can never be reconciled

The shared handler first durably deletes the App Server queue entry and only
then calls the attachment provider (`codex-web` commit `152e353`,
`conversation/handler.go:605-627`). If `QueueDeleted` fails while updating or
syncing the upload catalog, the response is an error although the queue entry
is already gone. On retry, `codex.Client.DeleteQueueEntry` has already cleared
its deletion/queue attempt and returns "queued message was not found" before
the provider is called (`codex/client.go:3511-3536`). The runtime provider does
not reconcile absent queue entries during `ObserveQueue`; only the post-delete
callback can change the submission from `queued` to `cancelled`
(`portal/internal/uploads/store.go:768-805`).

The stale `queued` state then pins the file indefinitely and every file-delete
attempt fails as queued or unresolved (`portal/internal/uploads/store.go:621-628`),
even though neither the queue nor transcript can ever observe that submission.
Make the cross-component deletion retryable as one operation, for example by
retaining sufficient deletion identity until the provider acknowledgement is
durable or by giving the provider an idempotent absent-queue reconciliation
path. Add a failure-injection test covering successful App Server deletion,
failed catalog persistence, and a successful retry after restart.

### 4. Explicit session deletion accepts a missing thread identity and can finalize while retaining owned files

During deletion, `remove_session_uploads!` treats the preserved `portal.yml` as
optional and converts a missing manifest or missing `codex.thread_id` to an
empty string (`libexec/dev-session:4836-4852`). The new `uploads
remove-session` command says a retired thread identity is required, but its
validation checks only the slug and positional arguments
(`portal/cmd/workspace-portal/main.go:468-489`). `Store.RemoveSession` then
matches an ordinary session scope only when its nonempty recorded thread equals
the supplied thread (`portal/internal/uploads/store.go:857-875`). With an empty
thread it changes nothing, returns success, and allows the Ruby deletion
journal to finalize.

The resulting completed deletion contradicts the documented promise that an
explicit session deletion removes owned files, including fork references, and
there is no remaining active journal retry to reclaim them. When an upload
catalog exists, require and validate the preserved exact thread identity before
finalizing, or resolve the exact slug/epoch owner from catalog evidence without
weakening slug-reuse isolation. Extend the deletion-journal regression with a
real catalog and a missing/empty preserved thread identity; it must stop before
`finalize_removal!` and retain a retryable journal.

## Advisory

None.

## Residual validation gaps

- The planned real-browser desktop/narrow interaction checks and 1 GiB bounded-memory transfer have not run. Existing Node coverage exercises transfer and durable-attempt helpers but does not execute the mounted DOM composer end to end.
- Live App Server attachment-only Send, steering, Queue, response-loss recovery, fork inheritance, archive/revive, and explicit deletion have not run. The queue persistence failure above needs deterministic fault injection in addition to those live checks.
- Package builds, aitherdev deployment, rollback to an upload-unaware generation, and restoration of the upload-aware generation remain untested, as expected before review findings are resolved.
