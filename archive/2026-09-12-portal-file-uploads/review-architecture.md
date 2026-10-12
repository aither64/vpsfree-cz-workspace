# Architecture and repetition review

Reviewed the committed ranges recorded in `review-packet.md`:

- `codex-web` `de83e9c72dec6cb5ff8ec13d5b0b21ed60148117..152e353057c6da97c7bbb9ae4393075a2f8cc423`
- `dev-workspace` `dc8d6cf7628a6a8db240f2e11ad61e8bc31ddacd..16c3d78faf6351c6a0a79c479fae2ca36cc3de78`
- `vpsfree-dev-workspace` `b37edd0f63fb7a984ba634c2d52d08e9344304b4..286a1f1b9c54d5b625712174df47975727d62193`
- `workspace` `94ca59f3f9d17306c2cc5e61099d83313309f4df..f5aa81ce3baf7f4b03d4109d0c5c7df4a0d2db76`
- `vpsfree-cz-configuration` `b4e120294696578c3871124259f266205bad4393..ecf8a52d640407b2e640cf11a70c7f8e6669b528`

I also inspected the applicable workspace and repository `AGENTS.md` files, the provider interfaces and queue orchestration in `codex-web`, the complete runtime catalog implementation and lifecycle call sites in `dev-workspace`, and the actual pinned consumers. The pin graph is internally consistent: `dev-workspace` imports and Nix-pins `codex-web` at `152e353057c6da97c7bbb9ae4393075a2f8cc423`; `vpsfree-dev-workspace` pins that runtime at `16c3d78faf6351c6a0a79c479fae2ca36cc3de78`; `workspace` pins the organization layer; and `vpsfree-cz-configuration` pins the same runtime through `devWorkspace`. The generic `codex-web` example remains the only other source consumer found and its text-only fallback is compatible.

## Blocking

### 1. The bounded catalog is append-only, so normal use eventually disables uploads permanently

`dev-workspace/portal/internal/uploads/store.go:163-184` enforces 10,000 entries in each map and a 16 MiB serialized catalog, but none of the lifecycle operations removes map entries. Every call to `NewDraft` appends a scope (`store.go:211-225`), every upload appends a file record, and every attached prompt appends a submission containing the original text and expanded wire text (`store.go:664-730`). `Collect` only changes file state and unlinks file directories (`store.go:808-854`), while `RemoveSession` only tombstones scopes and files (`store.go:857-880`). There is no reclamation of expired empty drafts, deleted file records, old submissions, or deleted scopes.

This makes the advertised bound a finite service lifetime rather than bounded reusable storage. A page load can create an empty draft through `dev-workspace/portal/internal/web/uploads.go:99-106`; 10,000 such drafts permanently make both new drafts and new session scopes fail. Ordinary attached prompts can hit 16 MiB much sooner because each submission retains both `Text` and `Wire`. Deleting files or sessions does not make room, despite the 507 response instructing the user to remove unused files. A remote authenticated client can accelerate this into a persistent workspace-wide denial of upload service without consuming blob quota. Near the byte cap, even tombstone or cancellation transitions can fail if their replacement JSON is larger.

Add a catalog-owned compaction policy that safely removes expired empty drafts and obsolete submissions/scopes/file tombstones after their reference and retry obligations end. Exercise recovery at both record and byte limits, including restart, session deletion, fork references, accepted-creation receipts, and retry identities. This must be resolved before long integration because the persisted format otherwise has no supported way to recover capacity.

## Important

### 2. Queue deletion commits the App Server side before the attachment provider, but the combined operation cannot be retried

`codex-web/conversation/handler.go:605-627` deletes the App Server queue entry first and only then calls `AttachmentProvider.QueueDeleted`. A successful `Client.DeleteQueueEntry` clears its durable deletion attempt (`codex-web/codex/client.go:3511-3576`). If the provider transaction then fails because of an I/O error, lock timeout, cancellation, or the catalog-capacity problem above, the HTTP request fails after the queue entry is already gone. Retrying the same request cannot reach the provider callback: with no queue entry and no retained attempt, `DeleteQueueEntry` returns `queued message was not found` at `client.go:3531-3535`.

The runtime submission consequently stays `queued` instead of becoming `cancelled` (`dev-workspace/portal/internal/uploads/store.go:768-805`). Its files remain pinned by `Collect` (`store.go:810-819`) and user deletion rejects them as queued or unresolved (`store.go:621-628`) until the entire owning session is explicitly deleted. A transient catalog failure can therefore consume quota indefinitely and the browser's natural retry cannot repair it.

Give the cross-component deletion one recoverable completion protocol. For example, retain the queue deletion receipt until provider cancellation commits, or add a durable provider reconciliation step keyed by the queue and client message identities. Test failure after confirmed App Server deletion, followed by HTTP retry and process restart.

### 3. An expired initial submission can be replayed without revalidating its deleted files

`Backend.Prepare` validates file state and on-disk presence only for a new submission. If the attempt key already exists, it returns the stored wire text after comparing text and IDs, without checking the files (`dev-workspace/portal/internal/uploads/store.go:671-678`). Unaccepted initial submissions are deliberately stored as `prepared` (`store.go:719-723`), so `Collect` does not pin their files and tombstones them after seven days (`store.go:813-825`). The scope remains available.

After a creation request was prepared but rejected, for example because the requested slug already existed in `dev-workspace/portal/internal/web/creation.go:107-161`, a client can wait for expiry and replay the same draft, text, and IDs under a different unused slug. `prepareCreationAttachments` accepts an unbound scope and derives the attempt only from text and IDs (`dev-workspace/portal/internal/web/uploads.go:108-124`), so it receives the stale wire text. The subsequent creation can be accepted at `dev-workspace/portal/internal/web/server.go:928-951` even though every path in that prompt has been removed. `RetainCreations` then records ownership after the data loss has already occurred.

Distinguish accepted idempotent replay from an unaccepted `prepared` retry. Revalidate ready records and regular files before returning an unbound prepared submission, or preserve/pin the bytes for the full lifetime in which such a retry is accepted. Add a test that prepares an initial submission, rejects creation before a receipt is stored, expires/collects it, and replays the exact request with another slug.

### 4. The workspace state identity is copied across Go and Ruby at a destructive lifecycle boundary

The portal workspace ID and state-root layout are independently reconstructed in `dev-workspace/portal/internal/web/operation_store.go:35-65`, `portal/internal/uploads/store.go:964-970`, and `portal/internal/session/removal.go:68-90`. Ruby reconstructs the same identity in `dev-workspace/libexec/dev-session:4408-4410` and again in the new upload cleanup at `libexec/dev-session:4836-4839`. The new Ruby test also recreates the formula to seed a catalog (`dev-workspace/test/dev_session_test.rb:5501-5502`) while mocking the portal command, so it proves that two Ruby copies agree rather than that the Go provider and CLI resolve the same catalog.

The formulas agree in this revision, but a future workspace path normalization, state namespace, or hash change can split them. The dangerous failure is silent: `remove_session_uploads!` returns when its locally computed catalog path is absent, after which session deletion can finalize while the Go-owned catalog and blobs remain orphaned. This is exactly the kind of storage-ownership rule that should not be duplicated across component and language boundaries.

Centralize the workspace ID and portal state layout for Go callers. At the Ruby boundary, prefer invoking the owning `workspace-portal uploads remove-session` operation unconditionally and letting that command report a safe no-op for a missing catalog, or expose one stable resolver rather than reproducing its private path. Cover the real CLI-to-Go boundary with a test that creates state through the Go store and removes it through `dev-session`.

## Advisory

No additional advisory findings.

## Architecture assessment

The public/private ownership split is otherwise coherent. `codex-web` owns optional transport and browser composition contracts, while `dev-workspace` owns workspace authorization, quotas, local paths, persisted attachment state, creation/fork adoption, and lifecycle cleanup. The optional provider preserves existing text-only consumers, and the checked downstream pins select one compatible provider/consumer series. The four findings above concern durability at the seams: catalog reclamation, two-phase queue deletion, prepared-creation retry, and cross-language state discovery.
