# Portal performance design and verification brief

Design owner: architect0. Status: implementation brief, 2026-09-29.
Scope and acceptance target come from [plan.md](plan.md). The lead owns
implementation assignments, verification evidence, pin updates and rollout.
This brief does not authorize any lifecycle operation or deployment.

## Evidence and decisions requiring lead attention

Session identity was verified with `dev-session current` from this tracking
directory. It printed `2026-09-29-portal-performance`; both environment identity
variables were absent and the trusted thread binding matched the workspace.

Inspected repository instructions and source through `origin/master`, never bare
`HEAD`. The workspace lock currently selects these same revisions:

| Repository | Inspected revision |
| --- | --- |
| codex-web | `e92dd887c888d5a9f50c70febc714f875cb44378` |
| dev-workspace | `3b570f0a8b75d809a2753177590158e9dc4639f1` |
| vpsfree-dev-workspace | `bd961682cecb0b3b2bf729a53d2e08bda3d48eb2` |

The lead must record the actual selected profile revision before rollout;
the workspace lock is not evidence of a running package. No remote fetch,
application edit, commit, live thread mutation or lifecycle action was performed
while preparing this brief.

Three corrections have been reported to the lead:

1. Existing `/thread` is the legacy **recent 20 full turns** response. Keep its
   behavior and shape; do not describe it as an existing complete-history API.
   The new page path must make all older history accessible.
2. Codex 0.155.0 `thread/read` declares `includeTurns`, not `excludeTurns`.
   Metadata reads on the new path use `includeTurns: false`. Existing code's
   undeclared field happens to rely on permissive decoding. Do not generalize
   this correction to `thread/resume`, which has a different contract.
3. `dev-workspace` deliberately refuses `workspace-host rollback` because team
   registration is forward-only. This is confirmed in `libexec/workspace-host`
   and `docs/workspace-portal.md`. Recovery must select a newer package restoring
   the prior application behavior while retaining current state readers. The
   plan's promise of selecting an earlier profile needs correction. Re-enabling
   package rollback is outside this initiative.

Generated experimental JSON schemas with the exact stored Codex 0.155.0 binary
at `/nix/store/5ic3470w8g40xyzqypbdzsvz9y3251ky-codex-0.155.0/bin/codex`.
Ambient `codex` is 0.155.1 and must not stand in for protocol verification.
Schema generation is evidence of request shapes, not proof of live pagination
semantics; the latter remains a post-review check.

The lead subsequently measured three authenticated Chromium loads of the target:
first message render took **12.36–12.54 seconds**, with **1,023 message DOM nodes**.
This is a diagnostic baseline, not the 30-load acceptance sample. Source confirms
`readLimit = 64 * 1024 * 1024` and that `ReadThread` invokes
`readRolloutMetadata` for every transcript read. The lead has not yet isolated how
much of the measured latency belongs to the suffix scan versus RPCs, transfer,
normalization and DOM work; do not attribute all 12 seconds to one cause.

## Scope, ownership and file boundaries

| Owner | Interfaces and likely files |
| --- | --- |
| codex-web | Add bounded transcript paging beside `Client.ReadThread` in `codex/`; reuse entry normalization and `timestamps.go`. Add an optional page-reader interface and HTTP operation in `conversation/handler.go`, plus shared browser page/merge helpers in `conversation/assets/conversation.js`. Preserve `assets/sync.js` recovery guarantees. Extend Go, browser and `test/codex_protocol_contract.py` contracts. Document the cross-project page contract in `docs/reference.md`. |
| dev-workspace portal | Consume the page API in `portal/internal/web/static/app.js`, templates and the generic mounted/member conversation surfaces. Update activity scheduling, diagnostics and browser tests. Explicitly forward the optional paging interface through `member_conversation.go`; embedding the old `conversation.Client` interface does not expose new optional methods. Preserve roster policy and model/effort presentation. |
| dev-workspace lifecycle | Change passive observation locking in `libexec/workspace-auto-archive.rb` and lock helpers in `libexec/dev-session`. Add combined observation to `portal/internal/workspacecodex/client.go` and `portal/cmd/workspace-portal/main.go`. Extend `test/auto_archive_test.rb`, `test/dev_session/automatic_archive_test.rb`, lock/concurrency and CLI tests. |
| Package owners | Align dev-workspace `portal/go.mod`, `portal/go.sum`, `flake.nix` and `flake.lock` with the exact codex-web revision; then update vpsfree-dev-workspace and the coordination workspace feature worktree pin chain. |

Keep durable feature semantics in codex-web's reference and dev-workspace's
portal/session guides. Keep individual benchmark results and rollout evidence
under this initiative. The architect edits only this design document. There
are no host configuration, NixOS module, namespace migration, cluster-provider,
model-policy, lifecycle-tier or persistent schema changes in scope.

## Invariants

- Every HTTP request independently resolves its opaque conversation ID to the
  trusted client, thread, canonical cwd, capability set and runtime generation.
  Preserve exact-origin enforcement, read authorization, request deadlines and
  session ownership checks. A page cursor never selects a socket, thread or cwd.
- Preserve legacy `/thread`, mutation routes and the mandatory methods on
  `conversation.Client`. Paging is an optional interface, so existing embedding
  applications and test clients still compile.
- No page requests full turn bodies, walks the full item history, or parses the
  full rollout. A large individual item can still be large: the count bound is
  not a promise of a small byte response. Preserve the existing transport byte
  bound and report oversize failures instead of silently truncating content.
- All older items, itemless turn failures and partial-turn boundaries remain
  reachable. A refresh never treats absence from the newest page as deletion.
- Keep raw message text, client IDs and digests, attachment observation and
  authorization, Markdown sanitization, timestamp provenance, turn status,
  latest-turn identity and retry receipts. Failure to see a message in a partial
  page is not evidence that a send failed or may be repeated.
- Archive observation is provisional. Only exclusive lifecycle revalidation can
  authorize the existing archive state machine. Unknown identity, activity,
  pending requests, queue state or ledger state never establishes idleness.
- No manifest, runtime authority, activity recorder, submission ledger,
  auto-archive sidecar, team roster, cluster state or journal migration is added.

## Page API and bounded history traversal

Add `GET <base>/conversations/<opaque-id>/thread/page?cursor=<opaque-token>`.
An omitted cursor requests the newest page. The server fixes page capacity at
100; it does not accept arbitrary limits, sort direction or a browser turn ID.
Reject duplicate cursor parameters, malformed tokens and excess query values
before doing history work. Keep responses private with `Cache-Control: no-store`.

Proposed Go additions, with names adjustable during implementation but semantics
fixed across producer and consumers:

```go
type TranscriptPageReader interface {
    ReadThreadPage(context.Context, string, string) (codex.TranscriptPage, error)
}

type TranscriptPage struct {
    Transcript                    // existing transcript fields, including entries
    OlderCursor *string `json:"olderCursor"`
    HasOlder    bool    `json:"hasOlder"`
    MetadataPending bool `json:"metadataPending"`
}
```

`entries` are in chronological order. `latestTurnId`, status and settings describe
the current thread, including when serving an older page; they must never turn
an old plan into an actionable proposal. `hasOlder` is exactly whether another
continuation exists, not whether this page contains 100 visible rows. Empty
pages with a progressing cursor are permitted for non-rendered/empty history.
The browser offers another older-page read rather than declaring history ended.

Page capacity counts consumed source items and synthetic turn-error entries.
This bounds both work and display rows to 100. An omitted empty reasoning item
still consumes its source-item slot; a page can therefore render fewer than 100
rows. A failed turn adds one stable synthetic row and consumes one slot. Document
this as a maximum of 100 entries, not a guarantee of exactly 100 rendered rows.

The HTTP handler performs its existing resolver/`VerifyThread` checks, asserts
the optional interface, then calls it with only the trusted thread. It applies
`TransformTranscript` and `Attachments.ObserveTranscript` to the page exactly as
for `/thread`, preserving raw text and digest. Unsupported optional interfaces
return a distinct `501` paging-unavailable response after authorization. Invalid
tokens return `400`; expired or invalidated traversal state returns `409` with a
machine-readable `transcript_cursor_expired`/`transcript_reset_required` code.
Identity denial remains unavailable/denied, never a capability fallback.

### Codex 0.155.0 data flow

The generated schemas establish these requests:

```json
{"method":"thread/read","params":{"threadId":"TRUSTED","includeTurns":false}}
{"method":"thread/turns/list","params":{"threadId":"TRUSTED","limit":100,"sortDirection":"desc","itemsView":"notLoaded"}}
{"method":"thread/items/list","params":{"threadId":"TRUSTED","turnId":"SERVER-TURN","limit":100,"sortDirection":"desc"}}
```

Both lists have `data`, optional `nextCursor`, and optional `backwardsCursor`.
Item entries contain only `turnId` and `item`. Turn rows carry status, error,
start/completion times and duration even with `itemsView: notLoaded`.
The schemas do **not** promise per-item turn metadata or a direct turn lookup.
Do not infer metadata from item IDs, UUID ordering or the newest 20 turns.

Use a turn-aware traversal as the correctness baseline:

1. Read metadata, validate returned identity, and establish the current newest
   turn through the metadata-only turn list. Preserve the narrowly recognized
   fresh, unmaterialized-thread case; no broad error-to-empty conversion.
2. Walk turn metadata newest first. For each turn, emit its failure row first in
   reverse chronology if one is required and has not already been emitted.
   Request that turn's items newest first with a limit equal to remaining page
   capacity. Validate that each returned entry belongs to that exact turn and
   has a nonempty unique item ID. Never ask for full turn items.
3. If the item page has a next cursor, retain the current turn and that cursor.
   Otherwise advance to the next older metadata turn. Visit at most 100 turn
   metadata rows during one HTTP call, including empty turns. Reaching that
   budget yields a continuation even if no displayable entries were found.
4. Reverse the normalized output for display. Use the same normalization code
   for items as legacy `/thread`, without injecting a turn failure once per item.
   The failure row has key `(threadId, turnId, "turn-error")`; an item has key
   `(threadId, turnId, itemId)`. Preserve server turn order rather than sorting
   timestamps, which may be missing or approximate.
5. Apply turn-time approximations, then existing live item timing and cached
   persisted timing from the metadata service described below. Do not invoke
   the existing 64 MiB rollout-tail scan synchronously for each new page.
   Older/forked items may legitimately retain approximate turn times.

This needs two metadata reads plus one item RPC for the common long-latest-turn
case (plus the handler's existing identity check). Many short turns can require
up to 100 small item RPCs. That is a known latency risk, not a tested result.
Do not replace this with an unsafe global-item-page/recent-turn join to meet the
benchmark. If the real benchmark requires batching, the implementer must refer
the revised metadata/item merge algorithm through the lead: its continuation
must retain unconsumed data, itemless turns and partial-turn error placement.

Continuation state is ephemeral and owned by the client/handler instance. Use
unpredictable opaque tokens bound to that client connection generation, thread,
canonical target identity and rollout lineage. Retain only bounded turn metadata,
the current per-turn item cursor and whether its failure row was emitted; do not
cache transcript bodies. Use copy-on-read continuation state so retrying a token
cannot skip history. Bound the cache by entry count and bytes (initial ceilings:
256 continuations, 8 MiB, 30 minutes idle); evictions return the explicit expired
code. Close/reconnect, changed target identity or invalid upstream lineage
invalidates affected continuations. These are tunable implementation limits,
not persistent formats or authorization evidence.

Reject absent list data, oversized result counts, unexpected turn IDs, duplicate
items, missing turn identities, repeated/non-progressing cursors and malformed
status/error objects. Never turn an upstream cursor failure into end-of-history.
Do not log token values or include socket/rollout paths in public errors.
Validate cursor behavior against the selected binary before relying on it.
In particular, `backwardsCursor` documents inclusive turn-anchor replay but does
not make the same explicit statement for item anchors; do not assume parity.

### Rollout timestamps and collaboration mode

The existing 64 MiB bound prevents an unbounded file read but is far too large
to repeat on stream refreshes. It entails file I/O, JSON decoding and allocation
even when only 100 items are returned, and repeated pages can parse identical
bytes. Item-count pagination alone therefore does not establish the latency
target. Measure rollout bytes scanned and decode time separately from RPC and
browser time.

For the page path, share an in-memory metadata reader per trusted thread/rollout
within the client. Cache parsed timestamp records and the latest applicable
collaboration-mode record, not raw transcript text. A cold read performs the
existing bounded suffix hydration in a coalesced background job with a deadline,
cancellation on client close and a small global concurrency limit (initially one).
The first page returns available live item times or marked approximate turn
times immediately. A completed enrichment invalidates/broadcasts a snapshot hint
so the next bounded refresh can improve timestamps. A `metadataPending` response
also schedules a coalesced browser retry with backoff, so enrichment is recovered
even without a usable SSE notification or on a read-only page.

Within the cache freshness interval below, warm reads reuse the parsed result
if file identity/size/high-resolution mtime are unchanged. For apparent
append-only growth, parse only new complete records, retaining an incomplete
trailing record for the next read. Verify regular-file identity and detect
replacement, observed shrinkage, same-size changes and changed bytes in the
previous tail. These checks are heuristics; they do not detect every non-append
modification. Detected changes invalidate the result and require fresh suffix
hydration. Bind results to connection/lineage/settings revisions so
a late background job cannot overwrite a newer settings notification or a new
thread. Do not hold an authority-wide lock during I/O/decoding. Bound cache bytes
and idle retention; evict display metadata rather than making the transcript
wait or introducing a durable index. On eviction, timestamps can return to their
honestly marked approximation until enrichment completes. Bytes outside the
same 64 MiB suffix remain outside timestamp coverage, as before.

Timestamp precedence stays unchanged: persisted item start, item completion or
record time, then available live observations, then approximate turn time. A
missing timestamp is not replaced with the browser's current time. Distinguish
the temporary cold-cache approximation from a permanently exact value; later
timestamp changes must not reorder history or lose the scroll anchor.

Collaboration mode is consequential for plan controls. `ReadThreadSettings` at
the inspected revision returns model/effort, not authoritative mode; calling it
is not a replacement for rollout mode extraction. Prefer a validated settings
notification/cache for the current connection and revision, otherwise the
validated rollout mode cache. If neither is known on the first page, omit
`collaborationMode` and set `metadataPending`; **do not invent `default`**.
The new browser must show mode as pending and withhold mode-dependent plan
actions until a known mode arrives, while ordinary message/pending/interrupt
controls remain usable under their existing server authority. Unknown mode
must clear stale mode state on a fresh generation rather than retain it through
`payload.collaborationMode || currentMode`. A settings operation still uses its
existing authoritative validation; this display cache cannot authorize it.

Keep legacy `/thread` behavior unchanged during this initiative. Sharing the
new cache with legacy reads is optional only if a separate compatibility test
proves the old contract. Do not globally reduce `readLimit`: it also protects
other protocol/rollout readers, and a smaller tail can silently lose the last
mode record behind a long tool output. Cache and asynchronous enrichment are
the chosen performance boundary; arbitrary metadata truncation is not.

#### Append detection decision (architect follow-up)

The lead accepted this boundary in the follow-up assignment: a 60-second
maximum cache age, an explicit normal-writer append assumption, a best-effort
tail probe, and periodic scan cost included in the benchmark.

**Acceptance decision:** retain the inode/size/high-resolution mtime and prior
4 KiB tail check as an optimization for display metadata, not as proof that the
previous prefix is unchanged. Acceptance requires the non-renewable 60-second
freshness limit and forced background rebuild below. The implementation as
inspected in `codex/page_metadata.go` lacks that limit and therefore does not yet
meet this revised requirement. The earlier general promise to detect all
non-append modifications is withdrawn.

A write to an earlier record followed by an append can preserve the old inode
and tail while changing both size and mtime exactly as an ordinary append does.
Any deterministic probe that omits some previously relevant bytes admits this
counterexample. Adding ctime, a larger fixed tail, sampled hashes or a stored
checksum without rereading its complete covered region does not prove prefix
immutability. An exhaustive bounded suffix reread can renew the metadata view;
the present reader has no writer-shared transaction or writer-provided mutation
epoch that would turn the small probe into an atomic proof.

Source evidence is limited. The installed 0.155.0 derivation selects
`openai/codex` tag `refs/tags/rust-v0.155.0`, with recursive source hash
`sha256-O+onwNd5YdE/KUJNBeQxBfK5JohzXenE4eOwejxFptc=`. Its recorded source output
`/nix/store/z9n086iaxqm6731352hgrx7zz06vddj3-source` is absent; no other local
rollout writer source was found, this member cannot access the Nix daemon, and
the exact upstream recorder-file fetch returned 404. Generated App Server
schemas establish API shapes, not rollout file immutability. Do not claim that
rollback, compaction, repair or any other writer path has been source-audited.
The lead may obtain that pinned source later; another version's append code
would not establish this package's complete writer contract.

The fast path's **explicit producer assumption** is that ordinary writes by the
selected App Server append complete JSONL records without changing earlier
records during the interval between rebuilds. This assumption is not currently
verified for every writer path. It is acceptable here only because the cache
supplies display enrichment, the operator is trusted, and bounded staleness is
an accepted limitation. It is not an assumption that arbitrary prior bytes are
immutable, nor a basis for authorization, receipt reconciliation, thread
identity, archive eligibility or mutation validation. Live in-place editing of
rollouts is outside supported normal operation; such maintenance should
explicitly invalidate/recreate the reader cache before trusting its display.

Required implementation behavior:

1. Record a monotonic `fullReadStartedAt` for each successful fresh suffix scan
   begun from empty mode/timestamp state. Its maximum usable age is 60 seconds.
   Incremental scans, appends, cache hits, retries and pending jobs preserve
   that original time; none renews it. Measuring from scan start prevents a slow
   read from extending the stale-data allowance.
2. On the first read at or after expiry, stop serving rollout-derived mode and
   exact item times from that cache. Return `metadataPending`, use independently
   available live times or marked approximate turn times, and schedule one
   coalesced full suffix rebuild, even if stat values are unchanged. A validated
   settings notification for the current connection remains an independent
   source of mode. The browser clears expired rollout-only mode and withholds
   mode-dependent plan actions while mode is unknown.
3. A fresh rebuild uses the existing at-most-64-MiB suffix and **no carried mode,
   timestamps or partial-record state**. Read only complete records. Preserve
   regular-file checks, generation/lineage binding, worker limits, cancellation,
   deadlines and superseded-result rejection. Publish the fresh map even if the
   cheap probe considered the file unchanged. Discard a scan whose own freshness
   deadline passed before publication; do not label stale output fresh.
4. Detectable replacement, shrinkage, same-size modification or old-tail mismatch
   invalidates immediately without waiting for expiry. Check the opened file
   and source identity again at completion; observed shrink/replacement requires
   retry. Growth during the read may leave a later append for the next job;
   retain the captured complete-record boundary rather than claiming to have
   consumed later data. Wrong-generation/lineage results cannot be published.
5. Rebuild failure leaves mode unknown and exact rollout timing unavailable after
   expiry. Backoff can delay enrichment, but cannot extend use of old values.
   Notify subscribers after success; `metadataPending` polling repairs views
   without SSE. No persistent cache or rollout rewrite is introduced.

Residual risk: an earlier in-place edit plus append can remain undetected by the
fast path and leave displayed mode/timestamps stale until the cache expires.
Served rollout-derived data may be at most 60 seconds old, measured from the
fresh scan's start. This does **not** guarantee repair finishes in 60 seconds:
worker backlog or failures produce pending/approximate values instead.
Concurrent arbitrary rewrites have no snapshot isolation; a fresh scan is a
best-effort view of complete records, not a proof against an adversarial writer.
Mode-dependent server operations retain their existing fresh authoritative
checks even when the browser's cached mode appears valid.

Periodic rebuilding costs up to 64 MiB of background reading/decoding per used
cache per minute. It must stay outside the page-response critical path and use
the existing worker limit. Record rebuild count/bytes/time and benchmark while a
rebuild is due. If that cost fails acceptance, refer a new design through the
lead: obtain a producer mutation-epoch contract or change the source of mode
rather than silently extending stale mode indefinitely.

Tests must edit an earlier mode/timestamp record beyond the old 4 KiB tail and
then append. Demonstrate the cheap probe's limitation, then prove fake-clock
expiry forces an empty-state rebuild and corrects the result. Continuous appends
and cache hits must not renew age. Also cover expired unchanged files, newer
independent settings notifications, delayed/failed rebuilds, stale job results,
mode absence after rebuild, immediate detectable invalidation and browser removal
of mode-dependent actions at expiry. Ordinary filesystem modifications are in
scope; hostile operator manipulation is not this feature's trust boundary.

## Browser synchronization and rendering

Add `client.threadPage({cursor, signal})` while retaining `client.thread()`.
Use a shared paging/merge helper in both generic `mountConversation` and the
portal; cover ready team-member and archived/read-only surfaces too.

Fetch the newest page immediately. Render it and enable controls as soon as its
own identity and status checks succeed. Pending prompts, queue recovery and
activity timing each settle independently. Their delay or failure must not
withhold the recent transcript. Preserve their own loading/stale/error states;
an unavailable pending endpoint must not look like a proved empty prompt list.

Maintain an ordered retained-history model and keyed DOM nodes. Replace or patch
only changed items, insert new entries and date separators, and leave unchanged
Markdown/disclosures untouched. Keep filters, copy actions, draft state,
attachment rendering, plan actions and scroll-follow behavior. Prepending older
entries preserves the visible entry and pixel offset after rendering. Updates
while scrolled away from the bottom use the existing new-output affordance.
Explicit filter changes can rebuild the filtered view; ordinary stream refreshes
must not replace the whole transcript or stringify all loaded history to decide
whether it changed.

The older-history button reads one page at a time, preserves all loaded entries,
deduplicates by stable keys and updates the oldest continuation. Never overwrite
that cursor with the latest page's cursor after older history has been loaded.
Cancel reads on conversation/member changes and page suspension, with generation
checks before every application of data. A changed thread identity clears the
previous model and cursor state before accepting data for the new thread.

SSE remains a hint stream. Preserve the sync module's reconnect/open refresh,
heartbeat watchdog, periodic snapshot repair, visibility/focus/online recovery,
deadlines, cancellation and backoff. Healthy heartbeats do not prove no messages
were missed. A newest-page refresh after reconnect/periodic repair compares
stable anchors with the retained frontier. If there is no overlap, display the
newest page immediately and fill the gap by following older pages until a known
anchor is found. Each request remains bounded; schedule gap reads separately
from visible refreshes. Do not silently stop after a fixed number of pages or
join noncontiguous ranges as if complete. A paused/failed gap remains visibly
incomplete with retry available.

Refresh retained entries from any turn that was nonterminal while displayed,
including items which have since moved outside the newest 100. On that turn's
completion or a reconnect, repair its loaded range through bounded pages before
considering it immutable. Repeated latest snapshots alone cannot repair an older
running tool after hundreds of new items. Coalesce rapid events and use at most
one newest-page request and one historical/gap request per conversation. Old
responses cannot overwrite a newer mutation result or a newer refresh generation.

Receipt reconciliation uses only positive matches of client ID and canonical
digest in observed entries. Continue durable-send retries with their original
identity; never clear a receipt because it fell out of the visible window.
Run receipt acknowledgements and their errors outside the first-render critical
path. An uncertain older receipt can remain pending until older history is read
or the existing send-recovery authority proves its outcome. Upload observation
must similarly treat a partial transcript as partial evidence, not proof of
attachment absence or permission to delete it.

### Queue, pending requests and compatibility

The queue lane retains `POST /queue/reconcile` followed by `GET /queue`, with the
ordinary mutation authority and lock. Give it independent cancellation, timeout,
coalescing and retry/backoff. Run it at initialization, reconnection, relevant
queue/deletion changes and periodic repair; do not launch a reconciliation POST
for every streamed text fragment. If reconciliation fails, keep the previous
queue marked stale and expose retry. It cannot abort a transcript or pending
read, and GET queue must remain free of cancellation-recovery mutations.

Pending requests retain a separate refresh lane and request-bound response
tokens. Controls must not infer that stale/disappeared prompts were answered.
Question drafts, snooze state and recovery checks remain tied to exact thread,
turn, item, question content and token, irrespective of transcript pagination.

| Browser/server combination | Behavior |
| --- | --- |
| Existing browser, new server | Existing `/thread` and mutation contracts. |
| New browser, new server | Bounded page path and older-history controls. |
| New browser, older server or old embedding client | One capability fallback to `/thread` for this mounted client after an explicit paging-unavailable response, or a legacy route `404` followed by a successful authorized `/thread` read. Advertise that older-history paging is unavailable; do not pretend the recent legacy transcript is complete. |
| New browser with stale cursor after server/profile change | Preserve displayed entries as stale, discard traversal tokens, recover from a new newest page and repair gaps. Never reuse tokens across conversations. |

Do not downgrade on authentication/authorization failures, timeouts, malformed
responses, cursor errors or generic server faults. Cached browser modules can
outlive a profile change; optional helper exports and DOM controls must be
feature-detected. Use existing asset versioning/cache controls so mismatched
app.js/conversation.js generations stay usable and do not create a reload loop.
No pagination state is stored in durable browser send receipts.

## Activity refresh budget

The portal's background activity observer already selects 5 seconds active and
30 seconds idle, but event wakeups can read more often and the browser polls
every 5 seconds plus every transcript apply. Remove transcript-apply coupling.

- Initial/focus/resume/reconnect reads may be immediate and coalesced. While
  visible, schedule activity reads at 5 seconds for active/waiting/unknown state,
  and 30 seconds only after a successful idle snapshot. Use one in-flight read.
- Suspend browser reads while hidden or lifecycle-paused; elapsed display ticks
  can remain local. Read-only archived views need one successful snapshot.
- Apply the same sustained rate budget to background event wakes. A meaningful
  idle-to-active transition may wake immediately; streaming item deltas must not
  turn the 5-second schedule into continuous history aggregation.
- Share/coalesce background and browser activity computation per trusted thread,
  retaining the existing per-thread gate and four-reader authority limit. A
  small in-memory last-success snapshot can serve concurrent readers within the
  appropriate interval. Fresh authority checks still occur per request. Failure
  marks cached timing stale; it does not update freshness timestamps.
- Preserve recorded activity completeness, fork lineage and count semantics.
  Do not replace the aggregate with the visible page's counts. Activity failure
  affects timing presentation, never basic conversation access.

## Archive observation, combined check and fail-closed behavior

Today passive scanning holds the per-session exclusive lock while invoking two
separate CLI processes: `thread activity` and `thread require-idle`. Replace only
the passive path with the same lock file in shared mode. Portal interaction
already uses shared lifecycle/session access; observation must coexist with it.

Lock order remains transition lock, session lock, then short auto-archive state
transactions. Passive observation uses transition shared + session shared;
actual archival retains transition exclusive + session exclusive. Release the
passive locks before attempting exclusive acquisition; never upgrade a live
shared lock. Do not hold the sidecar state lock around RPCs, Git fetches or file
hashing. Re-read policy/hold state when committing an observation.

Make lock mode explicit and keep exclusive as the default for all existing
mutations. If generalizing `with_slug_lock`, include its mode in held-lock state
and require exclusive ownership before delegating a lifecycle FD to cluster
reset. Merely seeing `@held_slug_lock` must not treat a shared observation lock
as mutation authority. Prefer a distinct observation helper if that avoids
changing the held mutation-lock invariant.

Add `workspace-portal thread observe --thread-id ... --cwd ... --socket ...`
as a single private CLI connection with output:

```json
{"threadId":"TRUSTED","cwd":"CANONICAL","updatedAt":1790000000,"idle":true,"blockers":[]}
```

Use the same result shape with `idle:false` and blockers for known active,
pending, queued or unresolved-attempt conditions. Identity/RPC/parse failures
exit nonzero; Ruby marks the observation deferred and resets aging. Require all
fields, verify exact ID/cwd, positive plausible timestamp, boolean idle and
bounded blocker strings; missing `idle` is never true. Keep `thread activity`
and `thread require-idle` for existing callers.

Factor the common client checks so this one connection reads trusted thread
metadata once for cwd/source identity and `updatedAt`, then checks latest-turn
terminal status, pending requests, queue entries and durable submission/deletion
attempts. Reuse the existing methods' validation; do not replace pending-request
checks with browser state or mutate queue/ledger state during observation. The
existing client must continue preserving persisted role instructions on reads.
If a cache or metadata-sharing shortcut cannot prove the same identity, perform
the extra read rather than weakening the check.

The combined result is a bounded-time observation, not a transaction with
concurrent Codex activity. Shared portal sends may race it. The exclusive final
path re-reads policy epoch, hold, lifecycle, manifest and authority identities,
creation readiness, current root and member idleness, queue/pending/attempt
state, worktree inventory/cleanliness and registered branch heads/merge proofs.
It recomputes fingerprint/eligibility before any lifecycle journal or destructive
step, using the existing `automatic` archive guard. Activity, a new hold, branch
movement, changed tracking or a new queued message between observation and
exclusive acquisition must defer/reset eligibility. Existing journal resume and
per-phase proof obligations remain intact.

Preserve existing 1/7/14-day tiers, hold/re-enable/revive epochs, backwards-clock
handling and source validation. Busy locks, missing source data, future/invalid
timestamps, malformed responses, unavailable App Server, unknown turn status,
unresolved attempts, journals and unprovable merge state fail closed. No error
path ages a candidate using a stale success. Merely reading a browser page is
not new user work and must not reset archive inactivity by itself.

## Diagnostics and accepted benchmark

Add bounded, content-free timing diagnostics around page resolution/verification,
RPC phases, normalization/timestamp decoration, queue reconciliation, activity
reads and passive archive observation. Record elapsed time, item/turn counts,
response bytes, cache/gap outcome and operation status. Browser marks separate
navigation, recent-render and controls-ready time. Archive diagnostics distinguish
transition wait, session wait, combined Codex check, worktree/Git proof and total
scan time. Log slow/error operations with sampling/rate limits, not one record
per streamed token. Never log prompt text, output, credentials, cursor tokens,
request bodies or unrestricted URLs; do not persist conversation screenshots.

Accepted live target from the plan: on aitherdev,
`2026-09-27-newadmin-integration` must show the recent transcript and usable
controls within **2 seconds at p95 across 30 browser loads**, including while
an archive scan is observing sessions. Older history is excluded from the timed
initial window but must work on demand.

Measure navigation start to the first painted newest-page view with its current
status and appropriate composer/read-only controls usable. Count failures and
timeouts as failures, never remove them from the sample. For 30 measurements use
nearest-rank p95, the 29th sorted value. Record browser/version, viewport, route,
package revisions, host load and cache policy; separate cold package/startup
measurements from ordinary repeated navigations. Run 30 loads without a scan and
30 with overlapping observation, with both p95 values at or below 2 seconds.
This gives the stated during-scan requirement its own measurable sample.

Capture before/after response bytes, recent-render/controls latency, portal and
App Server CPU, RPC counts, activity reads per minute, scan duration and session
lock failures. Acceptance additionally requires no page-load failure caused by
passive observation, visible gap recovery, working older history and no lost
receipts/prompts/uploads. A fast shell curl is diagnostic evidence, not the
browser usability benchmark.

The architect does not access or mutate the benchmark conversation. The lead
must arrange authorized read-only measurements. Use the already running worker
or an authorized observation-only/dry-run scan for contention measurements;
this design does not authorize starting an archival transition for any session.

## Verification plan

Quick checks precede commits and mandatory independent review. Use repository
Nix tooling; do not substitute ambient Codex 0.155.1. Exact commands are selected
from each final worktree's flake and AGENTS.md. Known focused commands include
targeted `go test` packages, relevant Ruby tests, Node syntax/browser contracts
and protocol request-corpus validation. Delegate any long/uncertain test or build
through the dev-session-monitor skill; the architect does not run the suites.

Required focused cases:

- Empty/unmaterialized, 1/99/100/101/250-item histories, one huge turn, many short
  turns, over 100 empty/error-only turns, failed/interrupted turns spanning page
  boundaries, hidden reasoning and duplicate/malformed upstream data.
- Exact 100-slot bounds and no full turn/full rollout read. Walk all pages to
  reconstruct the normalized reference history once, without duplicates or
  missing errors. Retry the same cursor; expire/evict it; append new items; change
  status; reconnect or replace lineage. Test cursor nonprogress explicitly.
- A large 64 MiB suffix: first-page work does not await its decode; unchanged
  refreshes read no repeated suffix; append growth reads only new bytes. Test
  partial/oversized records, rotation, truncation, same-size edits, cache eviction,
  background cancellation, stale job results and concurrent page reads. Preserve
  exact/approximate timestamp flags and recover mode after cold start without
  exposing plan actions under a guessed default. Include mode changes during
  enrichment, a last mode record far behind tool output, and read-only refresh.
- Foreign conversation/member/cwd/socket, denied read capability, expired roster
  membership, mutated token and origin violations. Old `conversation.Client`
  implementations remain source-compatible; member wrappers keep saved policy.
- Positive send ID/digest acknowledgements outside the first page, lost response,
  receipt reload, pending questions, stale prompt token, upload attachment
  decoration, queue deletion recovery and failure. A failing/hanging reconcile
  cannot delay rendering or erase queue/receipt state.
- Keyed DOM identity for unchanged rows, partial item updates, older prepend
  scroll anchoring, disclosure/filter/copy/plan behavior and reverse-response
  races. Exercise root, member, generic mount and archived surfaces.
- More than 100 missed items with healthy heartbeats, disconnected SSE, hidden
  tab, focus/online/BFCache recovery, stale cursors and loaded active items outside
  the recent window. Verify explicit incomplete gaps until repair completes.
- Fake-clock activity tests for 5-second active/30-second idle budgets, initial
  and meaningful transition refresh, concurrent readers, hidden tabs, failure
  staleness and shared background/browser reads. Preserve aggregate counts.
- Real subprocess flock tests: a shared observer and portal access coexist;
  an exclusive mutation conflicts; ordinary mutations remain exclusive; no
  shared-to-exclusive upgrade or shared lifecycle FD delegation occurs.
- Combined observation returns one validated result using one CLI connection.
  Failures, active turns, prompts, queue entries and unresolved durable attempts
  stay ineligible. Inject activity/hold/worktree/head changes between the shared
  observation and exclusive guard; prove no archival starts from stale evidence.
  Retain package-generation rejection and interrupted-journal tests.
- Old browser/new server, new browser/old server, expired cursors and independently
  cached old/new module combinations. Downgrade only for unsupported paging.

After quick checks and committed changes, the lead supplies the independent
reviewer the complete base-to-head series, final diffs, this brief and an explicit
no-migrations conclusion. Review pagination completeness, wrapper interfaces,
queue/receipt semantics, lifecycle locking and the entire pin chain. Consolidate
obsolete unmerged approaches before final whole-branch review.

After review: run codex-web checks, the relevant dev-workspace packaged suite,
vpsfree extension/package contracts and the complete workspace package build.
Run generated request **and response** schema contracts against 0.155.0, including
declared-property checks so permissive schemas cannot hide a misspelled field.
Use a disposable local App Server fixture to establish turn-filtered item cursor
semantics, terminal metadata/error coverage, reconnect behavior and fresh-thread
errors without writing to a real conversation. Run the browser benchmark and
authorized rollout smoke checks after these pass. Host migration/VM tests are
needed only if final changes unexpectedly affect that contract; refer any such
scope expansion to the lead first.

## Compatibility, package delivery and recovery

The one-way pin chain is:

```text
codex-web exact commit
  -> dev-workspace Go module + flake input
  -> vpsfree-dev-workspace dev-workspace input
  -> workspace feature flake vpsfree-dev-workspace input
  -> complete user-profile package on aitherdev
```

Keep Codex 0.155.0, llm-agents, nixpkgs, team catalogs and provider inputs unchanged
unless a separate demonstrated requirement is routed through the lead. The
dev-workspace derivation checks that the Go pseudo-version suffix matches the
codex-web flake revision; update and validate both. Preserve generic/site source
boundaries. Fetch current upstream before final pinning/rebase, inspect the
resulting lock diffs and avoid incidental input churn. This workspace's package
input edits belong in its dedicated feature worktree, not shared master.

There is no database, API-client generation, Terraform, service-daemon protocol,
NixOS/vpsAdminOS module, host/node coordinated upgrade or on-disk conversion.
New and old HTTP/browser clients remain compatible as described above. Activity
and archive sidecars remain readable by the existing generation. New cache
tokens are disposable on process replacement; durable send receipts are not.

Before switching, record the running profile/store path, all source heads and
the matching recovery source/package. Verify existing lifecycle, team, authority
and cluster-state transition preflights. Deploy the complete consuming package
with the stable `workspace-host switch --source <workspace-feature-worktree>`.
Do not install only the generic package and lose site extensions. Do not run
`confctl`, change a host system pin, rebuild NixOS or alter nginx/credentials.
Deployment authorization and repository default-branch integration approval are
separate; this brief supplies neither additional integration nor lifecycle scope.

Preserve previous source revisions as recovery evidence. If latency or semantic
acceptance fails, prepare/select a **newer recovery package** reverting these
application changes while retaining the current forward-compatible host/team
readers and the same site composition. Use the stable switch path and repeat
the smoke checks. Repeating an interrupted switch is the first supported repair.
The candidate `--from-candidate` entry is for a proven installed-parser failure,
not a normal shortcut. Never manually retarget profile symlinks, truncate ledgers,
edit generation markers or bypass transition refusals. Earlier-profile rollback
remains unsupported even though these particular feature changes introduce no
new persisted schema.

## Open risks and handoff gates

- Live cursor/empty-turn semantics need the exact 0.155.0 fixture check. Generated
  schemas alone do not establish ordering under concurrent appends.
- The turn-aware reference traversal is bounded but may need batching to meet
  p95 on many short turns. Measure before claiming readiness; retain error-only
  turns and partial-turn continuation in any approved optimization.
- One large item and cold activity-history backfill can dominate CPU/bytes.
  Pagination does not solve these by truncation; independent scheduling and the
  end-to-end benchmark determine whether follow-up work is necessary.
- The existing two metadata APIs cannot provide an atomic transcript snapshot.
  Stable identities, bounded cursors, overlapping repair and explicit resets
  must handle active updates without granting controls from stale history.
- The lead must reconcile plan.md's rollback and legacy-full-history wording,
  register this artifact in portal.yml, and capture final tests and rollout
  results in state.md. This assignment changes design.md only.

No application implementation, independent review, benchmark acceptance or live
rollout is claimed by this document.

## Recovery amendment: archived member omitted from discovery

Status: implementation decision finalized after the lead's completed App Server
probes. The first packaged recovery attempt refused a retained ready creation
record before mutation; the September 30 correction below is required before
retrying. Use exact
`thread/read` plus archived path/header identity proof and the narrow packaged
recovery adapter below. This amendment expands application scope
only to recovery of already-started archive journals and their general member
archive-proof defect. It does not authorize this architect to operate another
session or authorize any new archival, deletion, interruption or restart.

### Failure and evidence boundary

The lead reports archive journals for
`2026-09-26-codex-queue-ledger-capacity` and
`2026-09-27-architect-lead-policy` paused at `tracking_committed`. Their member
threads were archived successfully and have local archived rollouts, but the
member roster update did not finish. Repeating `thread/archive` reports that
the thread is archived. These are supplied operational facts; this architect
has not accessed or changed either session's private state.

At the inspected revision, `teamruntime.archivedMemberThread` proves archive
state solely by walking `thread/list {cwd, archived:true}`. It is called before
retirement, after archive attempts, during idle checks and before clearing old
attempts. An omitted thread therefore looks unarchived in every retry path.
`archiveAllLocked` may then take the materialization/replacement path or retry
an archive which already succeeded. The journal correctly refuses to advance
without proof. The defect is discovery being treated as an exhaustive archive
oracle, not failure of journal durability.

The lead completed the pinned 0.155.0 read-only probes. For both affected cwd
values, `sourceKinds:["appServer"]` and `["subAgent"]` return no archived
threads. For the September 26 session, `["vscode"]` and omitted source kinds
return only the root, omitting all three members. For the September 27 session,
they return the root and architect but omit implementer and reviewer. Returned
records have source `vscode` and paths beneath `archived_sessions`. Exact
`thread/read` succeeds for omitted members with matching cwd, and their exact
archived rollout files exist. The source-filter-only fix is disproven; there is
no remaining probe gate on the implementation choice. The internal cause of the
listing omission is not established and need not be guessed to fix archive
reconciliation. The completed candidate build does not itself include or verify
this recovery amendment.

There is a separate deployment bootstrap constraint. Both ordinary switch and
`switch --from-candidate` reject unfinished lifecycle journals. The latter also
deliberately invokes the selected package's `dev-session` for preselection
quiesce/recovery. Merely building the fixed package does not put its helper on
the old journal's execution path. Changing the selected profile first, passing
a fabricated generation, or invoking a candidate lifecycle script without the
old locks would break the transition contract.

### Choice of archival proof

| Approach | Acceptance and limitation |
| --- | --- |
| Correct member-list `sourceKinds` | Rejected by the completed probes: `appServer` and `subAgent` are empty; `vscode` and default listings still omit members. Do not implement a source-filter correction or a listing fallback as the archive oracle. Preserve unrelated discovery and its cursor checks. |
| Exact `thread/read` plus archived path/header proof | Selected implementation. Uses the exact retained thread and existing metadata API, independent of discovery completeness. Require all API, authority, path and bounded header checks below on every proof; an existing file or missing listing alone is insufficient. |
| Typed already-archived error | Useful only if the exact pinned response has an unambiguous, tested code/message or structured marker bound to the requested ID, and expected cwd/project were independently verified. Do not swallow all `-32600`, all not-found errors, or a message containing “archived”. An error cannot supply missing ownership proof. Do not globally make `codex.Client.ArchiveThread` return success on ambiguous errors. Not the primary fix. |
| Existing `--from-candidate` switch | Correct for a compatible candidate parsing state the installed host cannot read. It deliberately preserves lifecycle preflight and selected-package quiesce, so it does not resolve these journals. Retain that behavior. |
| Journal-scoped recovery adapter | Selected bootstrap mechanism to apply exact archive proof before normal selection. Add the explicit, tested entry below; retain the selected generation's lifecycle executor. It is not an earlier-generation rollback or a general command override. |

Implement exact-read/path/header proof and the recovery adapter. Do not retain
list filtering or typed-error success as speculative alternatives. The completed
probes establish the implementation choice, not a waiver of per-thread proof:
any missing or conflicting evidence at runtime leaves that journal blocked.
Do not weaken checks to make the package switch proceed.

### Exact-read proof contract

Keep expected identities in the durable roster/journal and selected runtime,
never in browser parameters. Pass the retained `Member` or its thread/project
identity to archive checks, not just an address or display name. The expected
cwd remains the original canonical `workspace/work/<slug>` even after tracking
moves to `archive/<slug>`; do not rebind the thread to the archive directory.

An exact archived proof requires all of the following:

1. Successful metadata-only `ReadThreadMetadata` for the exact retained thread
   on the already-selected App Server socket. The existing method checks returned
   ID; check exact cwd too. For a recorded `ProjectID`, require a non-null exact
   project match. Do not infer or create a project to repair missing evidence.
   Legacy members without a recorded project retain the existing exact-ID/cwd
   contract; do not silently expand that exception to current project members.
2. A nonempty absolute, clean server-returned path in that authority's canonical
   `archived_sessions` root. Bind the archive root to the actual App Server's
   configured Codex home, including a nondefault home, rather than guessing from
   the current shell. Compare path components/relative containment; substring
   matches such as `archived_sessions_backup` are invalid. Do not scan all homes
   or choose the first filename with a matching suffix.
3. The exact path is a regular non-symlink rollout, with the expected UUID in its
   supported rollout filename. Read only its bounded first JSONL metadata record
   (initial bound 1 MiB, fail closed if exceeded); require `session_meta` and the
   exact thread ID, and match cwd when present in that format. The API supplies
   project identity; do not invent a project field in the file format.
4. Recheck source/file identity after the read and keep the session/team operation
   locks through the resulting roster/ledger work. Any path/identity disagreement,
   disappearance, malformed header or unavailable metadata is an error. An active
   API path plus a separate archived copy is ambiguous, not proof of archival.

The trusted boundary is the local operator and configured App Server. These
checks prevent ordinary wrong-thread/path selection, stale state and concurrent
operations; they do not attempt to defeat a malicious local administrator.
No rollout body, SQLite repair, filesystem move or Codex mutation is part of the
proof. A missing thread is not an archived thread. Generic transport failure
does not activate a filesystem-only fallback. The disposable integration test
must verify that exact reads preserve archived state and issue no unarchive,
resume, materialization or other mutation.

After positive proof, use the existing attempt-resolution and cleanup ordering:
ordinary archival still requires `RequireSubmissionAttemptsResolved`, then
normal `ClearRetiredThreadAttempts`, then the normal atomic `Store.Update` to
`archived`. Preserve IDs, roles, policies, project, timestamps and all other
roster fields. Lost acknowledgement or a failed roster write retries the same
proof and update; it must not rearchive, unarchive, resume, replace or bootstrap
the member. A preexisting `removed` record still requires its separate supported
deleted-thread proof; this fix must not turn every absent member into archived.

### Ownership, interfaces and files

The root fix and recovery interface belong in **dev-workspace**. The implementer
brief is:

| Files | Change and focused tests |
| --- | --- |
| `portal/internal/workspacecodex/archive_proof.go` and `archive_proof_test.go` (new) | Put the shared exact metadata/path/header proof here for root and member use. Input is a trusted metadata reader, authority-bound Codex home and retained expected ID/cwd/optional project; return positive archive evidence only after every check. Bound header I/O to 1 MiB and retain useful identity/error diagnostics without transcript contents. Cover active, absent, invalid, foreign, unavailable and racing evidence. |
| `portal/internal/teamruntime/runtime.go`, `runtime_test.go` | Replace `archivedMemberThread` discovery with the shared proof, passing retained member/project identity. Apply the same contract to idle, archive-success reconciliation, ordinary removal and terminal-attempt cleanup. Keep fresh-member and removed-thread handling explicit; unknown evidence must not reach replacement/materialization during recovery. Test listing omission, already-archived retry, lost acknowledgement, legacy identity, unresolved receipts and atomic roster failures. |
| `portal/cmd/workspace-portal/main.go`, `main_test.go`; `portal/internal/workspacecodex/client.go`, `client_test.go` | Wire the trusted authority/home into proof callers and add read-only root/team `require-archived` helper entry points for adapter preflight. Reuse existing identity/state/socket arguments and durable stores; never accept these from browser input. Require every retained outstanding member and the retained root, with no archive/resume/start calls. Preserve ordinary root source rules and the private CLI already consumed by the old executor. |
| `libexec/workspace-host`; `test/workspace_host/archive_recovery_test.rb`, `profile_transition_test.rb`, `commands_and_locks_test.rb` | Implement the public journal-scoped recovery entry below and its internal helper substitution. Validate exact candidate/source, predecessor compatibility, generation/token, workspace, journal and late phase. Permit valid retained ready creation records under the September 30 contract below. Assert that only `--portal-command` changes in the selected predecessor invocation and no profile/service/Codex change occurs. |
| `test/dev_session/archive_test.rb`, `lifecycle_archive_test.rb`, `lifecycle_commands_test.rb` | Exercise the existing executor at `tracking_committed`, interrupted per-member completion and retry, normal merge/tracking proofs, runtime retirement and journal completion. No general lifecycle bypass or journal-format change is required in `libexec/dev-session`. |
| `docs/workspace-portal.md`, `docs/dev-sessions.md` | Document supported recovery invocation, trust and compatibility limits, forward recovery, and exact archive idempotence. Keep individual production approvals and replay results in the lead's rollout record. |

Use an internal proof result that distinguishes proven archived, positively
identified nonarchived/fresh state, and unavailable or conflicting evidence.
The recovery preflight accepts only proven archived. Ordinary lifecycle paths
must retain their existing explicit fresh-member/deleted-member contracts;
typed not-found is never converted to archived, and an error must not be flattened
to a false result that triggers member replacement. Valid active metadata is
not archived; missing archive files or conflicting path/header identities are
errors. No archive-proof result is cached across lifecycle operations.

Existing codex-web `ReadThreadMetadata` and `ThreadMetadata.Path/Cwd/ProjectID`
are sufficient; no codex-web application change or new typed-error classifier is
part of this recovery fix. Keep `ArchiveThread` error behavior unchanged. Call
`ReadThreadMetadata(ctx, id, false)` so the current wrapper omits its undeclared
`excludeTurns` field and uses the schema-valid metadata-only `includeTurns`
default. Do not add transcript/suffix reads to the proof.

Update the normal site/workspace pin chain after review; no host configuration,
extension behavior or App Server version change is required.

### Bootstrap while preserving selected-generation ownership

Add a deliberately narrow operator entry, proposed spelling:

```text
<candidate>/bin/workspace-host recover-archive --source <source> --workspace <name> --session <slug>
```

This packaged recovery interface requires the correction and verification below;
describing it does not authorize execution. It must not
reuse a general “ignore lifecycle journals” flag or teach ordinary switch to
finish unrelated journals automatically.

1. Build/resolve the complete candidate from `--source` and prove the executing
   candidate is that exact immutable package, using the existing source-package
   equality rule. Require a selected predecessor profile and snapshot its target
   and link token. Verify the candidate's protocol and private CLI/state contracts
   against the selected Codex 0.155.0 and old roster/ledger format. Use the same
   site composition; do not install or activate the candidate.
2. Acquire the real exclusive package-transition lock and revalidate the selected
   profile token/target. Resolve exactly one registered workspace and explicitly
   named slug. Validate its existing private archive journal, operation identity,
   mode, retained root identity and phase. Restrict this initial recovery entry
   to `tracking_committed`; refuse missing archive journals, unfinished creation,
   start, fork, agent-team migration, competing lifecycle journals and other
   archive phases. A validated retained `creation.json` in `state: ready` is
   not a conflicting operation; apply the narrow checks below. Do not create an
   archive journal or reconcile creation state.
3. Perform a read-only preflight of root/member identities with the corrected
   proof helper. For this narrow recovery, every retained member still requiring
   roster completion must already have positive archive proof; refuse live,
   unmaterialized, missing or ambiguous members. Confirm the root's existing
   retired identity too. This entry must not turn a failed proof into fresh
   member creation, interruption, unarchive or a new archive attempt.
4. Build the normal `dev_session_invocation` from the **selected predecessor
   package**: its private `dev-session` script, expected generation, profile token,
   runtime authority, tmux/socket paths, retained Codex binary, state paths and
   extension/cluster helper catalog. Keep those unchanged. For this one invocation
   substitute only the proven candidate's immutable `workspace-portal` helper
   into the existing `--portal-command` argument. Do not expose an arbitrary
   executable path or general command string override to the operator.
5. Invoke the selected lifecycle executor for the named archive retry and the
   journal's existing mode. Preserve its existing confirmation/authorization
   path; do not forge portal authorization or use `--force`. The parent holds the
   exclusive transition lock, so use the established inherited-lock/delegation
   convention without reacquiring it. The old executor still takes its creation
   and session locks, verifies committed tracking/exact merge proofs and executes
   ordinary roster/ledger/runtime retirement and journal completion. The candidate
   is a compatible protocol helper, not the new lifecycle owner.
6. On return, verify the selected profile and Codex authority did not change.
   Report completion only when the old executor finished the exact journal.
   Failure leaves the existing journal/retry state intact; partial successful
   roster updates remain safe inputs to the next retry. Reusing this entry with
   no journal must refuse, not start a new archive.
7. After all operator-selected paused journals are completed and the usual
   preflight finds no unfinished operations, run the ordinary stable profile
   switch. Its preselection quiesce still uses the old generation. Because the
   corrected helper already persisted member terminal states, the old idle path
   can now pass. Select and activate the candidate only through the normal
   transition, then restore terminals through the selected new generation.

The new entry is an explicit exception only for the protocol helper used by a
named, late-phase journal. Do not loosen `preselection_session_package`, ordinary
generation rejection or candidate switch preflights. An ad hoc shell wrapper
that edits private invocation arguments is not the deployment procedure; package
and test this recovery interface first. Execution still needs authorization for
the exact session's archive retry; deploying the performance feature alone does
not supply it.

### Retained ready creation records: September 30 correction

The lead reports that the first live adapter attempt failed before mutation
with `conflicting session operation blocks archive recovery`. Both authorized
sessions have normal schema-1 `*.creation.json` records with `state: ready` and
`preserve_tracking: true`. Those records retain creation identity after creation
completes; their existence does not mean creation is unfinished. The earlier
blanket refusal of creation journals in this design was incorrect and caused
the adapter's unconditional file-existence rejection. These are lead-supplied
facts; this architect has not inspected or changed the affected live records.

The correction belongs only in the candidate adapter's conflict classification
and read-only validation. Reuse `workspace-host#read_private_creation_journal!`,
which already validates bounded private creation records and distinguishes
`creating` from `ready` for ordinary package-transition preflight. Do not copy
the creation schema or the session creation/reconciliation workflow into a new
parser. The selected predecessor's `archive` takes the creation and slug locks,
but its late-phase replay does **not** call `valid_stored_creation_journal?`.
Relying on that lock alone to validate record contents would therefore be wrong.

Before root/team proof helpers or the archive executor are invoked, while the
adapter holds the exclusive transition lock:

1. Continue to refuse the exact slug's `start`, `fork`, agent-team migration and
   every competing lifecycle journal. Presence remains sufficient to refuse
   those operation journals, including a symlink at their expected paths; a
   purported ready creation record does not override any of them.
2. Treat absence of the exact workspace/slug `creation.json` as the existing
   supported legacy case. Do not create a replacement. When present, apply
   `require_safe_private_file!` then `read_private_creation_journal!(path, slug)`:
   owned mode-0600 regular nonsymlink file, at most 64 KiB, strict JSON and the
   reader's supported schema/field/value rules. This includes the ordinary
   schema-1 preserved-tracking shape and existing supported schema-2/3 shapes;
   no new schema or exception for malformed records is introduced. Require
   `state == 'ready'`. `creating`, unknown schema/state, bad slug, malformed or
   inaccessible data all refuse; never silently treat them as absence or repair
   them to ready. Preserve existing candidate/predecessor compatibility checks.
3. Reuse the archived manifest already read for archive recovery. Keep its exact
   slug, `creation.state == 'ready'`, retained root-thread and selected socket
   checks. For a present creation record, also require equality between its
   `goal_sha256` and the manifest's `creation.goal_sha256`; a legacy null digest
   matches an absent digest. This is the minimal binding check already used by
   the session's stored-ready-record validator, not a second manifest parser.
   A mismatch refuses before any proof helper or executor call.
4. Validate preserved-tracking provenance fields through the existing reader's
   shape rules only. Do not compare `tracking_plan_sha256`/`tracking_state_sha256`
   to current archived files, or require these fields still to be in the ready
   manifest: they describe the earlier creation snapshot, tracking legitimately
   evolves, and successful creation/revival clears manifest provenance fields.
   Do not compare mutable model/team settings to the creation snapshot either.

The ready creation record is only evidence that no creation is pending; it does
not authorize archival or replace the archive journal's retained-root identity.
The candidate's existing exact archive proof and the selected predecessor's
locked committed-tree/retained-runtime/merge checks remain authoritative. Keep
the exclusive transition lock until the old executor returns, so supported
creation/start/fork/migration commands cannot change the classification between
preflight and replay. Let the executor acquire its normal creation and slug
locks; do not hold a second creation lock across its invocation and deadlock it.
An uncoordinated hostile local administrator is outside the trusted-operator
boundary; the correction adds no new filesystem adversary model.

Exact implementer scope: remove `creation` from the unconditional operation
presence check in `require_archive_recovery_journal!`. In `recover_archive`,
after loading/checking the archived manifest and before `require-archived`
preflight calls, validate the optional ready record using the existing readers
and the small digest comparison above. A small private helper is sufficient.
Keep the other operation checks, old executor arguments, helper substitution,
generation/token checks and journal completion verification unchanged. No
`libexec/dev-session`, codex-web, Go proof, runtime-contract or persistent-schema
change is required for this correction. Update the recovery explanation in
`docs/workspace-portal.md`; the implementer owns those application/doc edits.

Focused regressions belong in `test/workspace_host/archive_recovery_test.rb`:

- Add the normal schema-1 ready preserved-tracking record to the main successful
  recovery fixture, with matching manifest goal digest and valid historical
  provenance. Prove the exact old executor runs, only the helper changes, and
  the ready record stays byte-for-byte unchanged. Its historical file hashes
  may differ from archived file contents and ready manifest provenance may be
  absent. Preserve an explicit successful no-creation-record legacy case.
- Refuse a valid `creating` record, unknown schema/state, bad slug or digest
  binding, invalid preserved-tracking shape, malformed/oversized JSON, symlink,
  nonregular file, unsafe permissions and read failure. Verify no proof helper
  or executor ran and archive journal/roster/profile were unchanged. Reuse
  existing parser tests for exhaustive schema details; add small valid ready
  schema-2/3 and legacy-null-goal cases to guard supported recovery compatibility.
- With a valid ready record present, independently inject `start`, `fork`,
  agent-team migration, revive/removal and every other registered competing
  lifecycle journal. Each must still refuse. Unknown predecessor contracts and
  changed generation after lock wait continue to refuse.
- Run failed-proof and interrupted-executor retries with the ready record still
  present, then complete archive recovery and ordinary package switch. Retain
  the transition/executor lock-order check and existing normal-transition tests
  in `profile_transition_test.rb`; a ready record must not cause deadlock or
  become a reason to bypass an unfinished archive journal.

Compatibility/recovery consequence: this is a correction to classification of
existing state, not a migration. Keep ready records and historical digests
unchanged; do not delete, truncate, rewrite or manually edit them to unblock
deployment. The reported first attempt made no mutation and needs no state
compensation. Build the corrected candidate, run focused checks and required
review, then repeat the same authorized journal-scoped recovery through the
selected predecessor. The failed candidate remains unselected; no profile
rollback, host change or Codex restart is needed. The disposable old-profile/
new-candidate bootstrap check must now include a retained ready creation record
before the next live retry. Acceptance is successful recovery with that record
preserved, followed by the normal switch, while all unfinished-operation cases
still fail closed.

### Compatibility, rollback and verification

No persistent schema or new lifecycle phase is introduced. Existing roster and
submission-ledger readers can load all state produced by the fix. An old package
can read members marked `archived`; it need not understand the new proof method
to quiesce them. Existing journals retain their identities and checkpoints.
No database, generated clients, NixOS options, provider state or host packages
change. The new entry must reject incompatible predecessor CLI/state contracts
rather than assume every historical package can participate.

Before selection, recovery leaves the old profile and App Server running. If a
proof or replay fails, correct the cause and retry the same explicit entry;
do not undo already-proven member archival or roll roster fields backwards.
After selection, recovery remains forward-only: repeat the switch or select a
newer corrected package. `workspace-host rollback`, profile retargeting, manual
journal/roster edits and ledger truncation remain forbidden recovery strategies.

Quick checks and fixtures before mandatory review:

- Reproduce the observed incomplete archived listing for all tested source kinds,
  while exact metadata and header proof succeeds for the retained member. Assert
  that archive proof does not call `ListThreads` or accept unrelated/root/foreign-
  project threads. Keep unrelated discovery tests unchanged.
- Exact-read proof: archived path/ID/cwd/project/header success;
  active path, missing path/file, wrong ID/cwd/project, null current project,
  symlink/nonregular file, sibling archive-like directory, oversized/corrupt first
  record, replacement/race and unavailable RPC. Typed already-archived errors
  alone do not satisfy proof. Cover authority home binding and nondefault homes.
- App Server archive success with lost response, post-success roster-write
  failure, process restart, already-archived retry, unresolved send/deletion
  attempt and cleanup-write failure. No duplicate archive/inject/start/resume
  calls and no erased unresolved receipts. Include retained legacy members.
- Recovery adapter validates candidate/source, registered workspace, explicit
  slug, private journal identity/phase and all preflight proofs. Missing/wrong
  phase/conflicting journal and changed generation after lock wait all refuse
  before mutation. Apply the ready-creation-record exception and focused
  regressions above; it is not an exception for unfinished creation or other
  operation journals. Unknown CLI/schema/protocol predecessor refuses.
- Assert selected old lifecycle executable and generation/token, old extension
  helpers and socket remain in the invocation; only the protocol helper changes.
  Assert no profile set, service restart, candidate quiesce or Codex replacement
  during recovery. Include helper failure, mid-roster interruption and retry.
- Replay `tracking_committed` through ordinary verification, per-member updates,
  runtime retirement and journal removal; then demonstrate ordinary old-generation
  quiesce followed by a valid normal package switch. Restore existing transition
  failure tests; the recovery exception must not broaden normal candidate access.

After committed fixes and independent whole-branch/lifecycle review, use a fresh
verification watcher for the package checks and a disposable old-profile/new-
candidate test covering the full bootstrap sequence. Establish exact 0.155.0
list/read/archive-response behavior with a disposable member and a lost-success
fixture; read-only production probes may corroborate it. Do not use real sessions
to manufacture failure cases. The lead records the exact predecessor/candidate
heads, probe metadata, approvals, journal retry results and final normal switch.

Acceptance requires a positive supported archive proof for every affected member,
no residual journal after an authorized retry, preserved roster/receipt identity,
no new Codex archival attempt for already-archived members, unchanged profile
during bootstrap, and a subsequent normal package switch. Existing portal
functional and performance acceptance still applies, including metadata-cache
periodic full-scan cost in the latency benchmark. The source-filter/exact-read
investigation is complete and implementation can proceed on this design.
Remaining release risks are predecessor/helper contract compatibility and
preservation of archival/identity through crash and retry; the specified tests
and independent review must resolve them before an authorized live retry. A
plausible path name alone is not acceptance evidence.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-29-portal-performance/
