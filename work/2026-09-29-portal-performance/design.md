# Portal performance design and verification brief

Design owner: architect0. Status: implementation brief, 2026-09-29.
Scope and acceptance target come from [plan.md](plan.md). The lead owns
implementation assignments, verification evidence, pin updates and rollout.
This brief does not authorize any lifecycle operation or deployment.

Latest scope amendment: the deployed pagination passed functional checks but
failed the live latency gate. The host-auth amendment at the end adds a bounded
bcrypt-cost option and an aitherdev-only system configuration change. It
supersedes the earlier exclusion of host-module/system-pin work for this narrow
purpose; the workspace application still belongs to its user profile.

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
| Host-auth follow-up | dev-workspace `nix/host-module.nix`, host module checks/VM tests and host documentation; vpsfree-cz-configuration aitherdev `config.nix` plus its confctl-managed `devWorkspace` input pin. See the final amendment for exact scope and security/latency acceptance. |

Keep durable feature semantics in codex-web's reference and dev-workspace's
portal/session guides. Keep individual benchmark results and rollout evidence
under this initiative. The architect edits only this design document. There
are no namespace migration, cluster-provider, model-policy, lifecycle-tier or
persistent schema changes in scope. Host configuration and NixOS module work are
limited to the later bcrypt-cost amendment.

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
authorized rollout smoke checks after these pass. The later host-auth amendment
requires the host-module VM checks before its system deployment; it introduces
no namespace migration.

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
host/node coordinated upgrade or on-disk format conversion. The later host-auth
amendment adds one NixOS option and regenerates its derived htpasswd when needed.
New and old HTTP/browser clients remain compatible as described above. Activity
and archive sidecars remain readable by the existing generation. New cache
tokens are disposable on process replacement; durable send receipts are not.

Before switching, record the running profile/store path, all source heads and
the matching recovery source/package. Verify existing lifecycle, team, authority
and cluster-state transition preflights. Deploy the complete consuming package
with the stable `workspace-host switch --source <workspace-feature-worktree>`.
Do not install only the generic package and lose site extensions. The application
rollout itself does not use system pins. The later host-auth amendment separately
defines the narrowly scoped confctl/system deployment and derived-hash update.
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

Status: exact archive proof and the ready-creation correction are implemented.
The corrected live attempt safely exposed a legitimate partial team archive.
September 30 database/source evidence establishes no Codex archive-state
inconsistency. The next correction is an exact, idempotent retained-team archive
step inside the journal-scoped adapter, before final proof and predecessor
replay; see the partial-archive amendment below. No Codex patch or version change
is needed. Keep exact
`thread/read` plus archived path/header identity proof and the narrow packaged
recovery adapter below. This amendment expands application scope
only to recovery of already-started archive journals and their general member
archive-proof defect. It does not authorize this architect to operate another
session or authorize any new archival, deletion, interruption or restart.

### Failure and evidence boundary

The lead reports archive journals for
`2026-09-26-codex-queue-ledger-capacity` and
`2026-09-27-architect-lead-policy` paused at `tracking_committed`. The initial
report said their members had archived rollouts and that repeated archive calls
reported already-archived threads, while roster completion remained pending.
The September 30 exact investigation below disproves that blanket premise for
the September 26 implementer and reviewer. Earlier narrative reports do not
establish a per-ID archive outcome. No session state was changed by this architect.

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
`thread/read` succeeds for omitted members with matching cwd. The earlier
assertion that every omitted member also had an archived rollout is superseded
by the September 30 evidence below. The source-filter-only fix is disproven; there is
no remaining probe gate on the implementation choice. Later source and database
evidence below explains why these filtered discovery requests are not exhaustive,
including the default model-provider filter. The completed candidate build does
not itself include or verify the partial-team recovery correction.

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
The root recovery preflight and final member proof accept only proven archived.
The journal-scoped team completion step below also accepts positively identified,
materialized active members after normal idle/receipt checks. Ordinary lifecycle paths
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
3. Under the normal creation and slug locks, revalidate the exact existing
   journal, ready creation binding and committed archive tree/recorded merge
   proofs using the existing lifecycle verification routines. Prove the root's
   retained archived identity, then invoke the candidate's nonforced,
   retained-only team archive step. It reconciles already-archived members and
   archives positively identified materialized active members only after normal
   idle/receipt checks. Run final `team require-archived` before predecessor
   replay. The detailed contract below forbids fresh-member recycling,
   replacement, interruption, unarchive and start/resume. Release the creation
   and slug locks before invoking the predecessor; keep the transition lock.
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

The new entry is an explicit exception only for the protocol helper and retained
team completion used by a named, late-phase journal. Do not loosen `preselection_session_package`, ordinary
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

### Partial member archival: September 30 proof investigation

The corrected attempt in `recover-2026-09-26-ready-corrected.log` exited 1 at
`team require-archived` with `member implementer0 is not archived`, before the
selected lifecycle executor. Lead comparison confirms profile, archive journal
and creation journal were unchanged. The ready-creation correction is not the
cause of this second refusal.

The authorized read-only investigation inspected only the exact September 26
roster, retained members' metadata and first `session_meta` headers. The roster is
`/home/aither/.local/state/dev-workspaces/codex-teams/vpsfree.cz-8a2a555cb2f65b33/2026-09-26-codex-queue-ledger-capacity.json`.
Its root remains `01a0dd8a-4d12-7631-a6ea-81d62952b388`; all three members remain
`ready`. Roster `updatedAt` and filesystem mtime remain September 26 11:47:47 UTC.
The lead's exact `thread/read {threadId,includeTurns:false}` projections are in
`sep26-member-metadata.jsonl`; this architect's socket access was denied before
any RPC. No conversation turns or body were read or recorded.

| Member | Retained thread | Retained project | Exact rollout under `/home/aither/.codex` |
| --- | --- | --- | --- |
| architect0 | `01a0dd8a-d01d-7a40-888b-e85dfd40d9eb` | `01a0dd8a-cfe9-7b92-841e-11b272c86d7c` | `archived_sessions/rollout-2026-09-26T13-47-37-01a0dd8a-d01d-7a40-888b-e85dfd40d9eb.jsonl` |
| implementer0 | `01a0dd8a-e0a6-7e33-a0a5-88498c5119dc` | `01a0dd8a-e054-7923-9e21-2f2859c1dd0a` | `sessions/2026/09/26/rollout-2026-09-26T13-47-41-01a0dd8a-e0a6-7e33-a0a5-88498c5119dc.jsonl` |
| reviewer0 | `01a0dd8a-ec3a-7292-ade8-da33e88631fa` | `01a0dd8a-ec0f-7d92-ab67-d46637ffb354` | `sessions/2026/09/26/rollout-2026-09-26T13-47-44-01a0dd8a-ec3a-7292-ade8-da33e88631fa.jsonl` |

All exact reads return the retained ID/project, original session cwd, source
`vscode`, `ephemeral:false`, paginated history, no fork and `status:notLoaded`.
The regular nonsymlink files' first headers match ID/cwd, originator
`dev-workspace` and CLI 0.155.0. Exact filename searches find no archived copy
for implementer/reviewer. Their rollout mtime and API `updatedAt` remain their
September 26 creation timestamps; lead metadata also confirms original ctimes.
There is no evidence of recent rematerialization, replacement or changed roster
identity. `notLoaded` is not a proof of idle turns, empty prompts/queue or resolved
submission attempts. Current metadata/path evidence establishes active rollout
placement for those two members, not permission to archive them.

The candidate's `ProveArchivedThread` returns `ArchiveActive` for these validated
`sessions` paths; `RequireArchivedAll` correctly refuses that state. It passed
the first member's archive proof and stopped at the implementer, so its first
error does not mean the reviewer is archived. Do not classify an active path as
archived, fall back to an archived-looking filename, swallow an archive error,
or edit the roster to meet the adapter's prerequisite.

#### Corrected evidence and root cause

The lead's subsequent read-only `state_5.sqlite` inspection supersedes the
earlier inconclusive escalation: September 26 root and architect rows are archived
with archived paths; implementer and reviewer rows are active, with
`archived_at NULL` and the same active paths as exact metadata/filesystem proof.
September 27 root and all three members are archived with archived paths, while
its roster members remain ready. Database, exact reads and filesystem placement
agree. These are lead-supplied exact-row facts; this architect did not open the
production database. The earlier blanket claim that all September 26 members
were archived was wrong. There is no observed rematerialization, replacement,
retained-identity change or Codex archive-state inconsistency.

The four empty responses in `sep26-member-list-state-db.jsonl` used exact cwd,
project, `sourceKinds:["vscode"]`, both archive flags, `useStateDbOnly:true`,
limit 100 and ascending cursor exhaustion. They **omitted `modelProviders`**.
The pinned App Server's `list_threads_common` defaults that filter to its
configured provider; the inspected rows have `model_provider=openai`. They were
therefore not an exhaustive state-table query. Do not infer missing rows or
archive corruption from those responses. A future metadata-only diagnostic,
if needed, must specify `modelProviders:["openai"]` for these records (or an
explicit empty provider array when testing the pinned all-provider contract),
keep `useStateDbOnly:true`, and project only ID/project/cwd/path/source and cursor.
No further production list probe is required to choose this fix.

The pinned source inspected for this investigation is
`/nix/store/z9n086iaxqm6731352hgrx7zz06vddj3-source/codex-rs`, rust-v0.155.0.
That source path was unavailable on the final reread; the references below are
from the earlier source inspection, with the provider-default behavior confirmed
by the lead. Do not substitute another Codex version when reproducing it.

| Source reference beneath `codex-rs` | Consequence |
| --- | --- |
| `app-server/src/request_processors/thread_processor.rs`, `list_threads_common` | Omitted provider filters use the server's configured provider. Discovery is filtered, even when project/cwd are exact. |
| `state/src/runtime/threads.rs:1255` and `:1417` | Ordinary state listing also excludes empty previews; relation/section exceptions do not make every project query exhaustive. Empty preview is a separate source-supported omission mechanism, not a measured claim about these production rows. |
| `thread-store/src/local/list_threads.rs:256` and `rollout/src/list.rs:820` | Project-filtered listing uses state DB; filesystem discovery also requires a discoverable preview. Changing only sourceKinds cannot supply exhaustive proof. |
| `thread-store/src/local/read_thread.rs:30`, `:92`, `:260`; `thread_rollout_resolver.rs:94` | Exact read uses retained metadata/current rollout resolution and can read header-only histories omitted by discovery. Paginated current-path selection intentionally avoids arbitrary stale fallback. |
| `app-server/src/request_processors/thread_processor.rs:1691`, `:1701`, `:1754`, `:2993` | Archive reads the exact unarchived thread and delegates locked archival; metadata-only read includes archived threads. Archive does not depend on thread/list. |
| `thread-store/src/local/archive_thread.rs:16`, `:75`, `:132` | Archival takes lifecycle/writer locks, moves exact selected/owned rollout paths, marks state archived, and compensates filesystem moves if the state update fails. |

The old worker resumes an existing journal before passive observation. Its old
team idle check treats a member omitted by archived discovery as nonarchived;
queue inspection then reaches Codex's archived-session error. That error is not
evidence that the currently active implementer/reviewer was archived. The old
team loop can archive a member successfully and fail the subsequent listing
proof before updating its ready roster state; later members remain untouched.
Normal lifecycle order is root retirement, then team archive, then the
`thread_retired` checkpoint. This explains both a mixed partial team phase and
an all-archived team with stale ready bookkeeping. No specific historic scan is
claimed to have moved a particular file without its per-ID trace.

**Decision:** retain the exact archive proof. Fix the recovery adapter in
`dev-workspace`; no Codex patch, packaging patch, version change or separate
Codex repair/escalation is needed. No further codex-web behavior change is
required. The supported primitive for a verified idle active member is normal
exact `thread/archive`, followed by positive exact proof. Use it through the
owning recovery operation, not an ad hoc private helper command. Existing
`ArchiveAll` already implements the idempotent mixed-state proof/receipt/roster
sequence. The remaining defect is the adapter requiring every member already
archived before it can reach that sequence.

#### Selected recovery sequence and implementation boundary

Put the member action **inside `workspace-host recover-archive`**, after the
existing candidate/source, selected generation/token/Codex, registered workspace,
archive journal and ready-creation checks. The archive journal remains the
operation authority. The candidate remains unselected throughout. Preserve the
existing CLI's explicit named-session authorization; a deployment request or an
ordinary switch must not invoke this exception automatically.

The ordered sequence is:

1. Hold the existing exclusive transition lock. Acquire creation then slug
   locks in the normal lifecycle order for the helper phase. Re-read the exact
   journal/manifest/optional ready creation record under those locks; require
   the same operation ID, schema, mode, root, `tracking_committed` phase and
   generation observed at entry. Reject competing operations as before.
2. Before the newly introduced member mutation, re-use the lifecycle verifier
   for the committed archive tree and exact recorded merged heads. The previous
   adapter deferred this to the predecessor because its preflight was read-only;
   that deferral is no longer sufficient. Use the existing
   `verify_committed_archive_tracking!` logic, including ordinary complete versus
   abandoned semantics. Do not merely trust the phase string or duplicate the
   Git/tree/manifest algorithm in the host command. A small candidate-packaged
   verification entry around `DevSession::Runner` may expose these existing
   checks and locks; it must only load an existing journal, never create,
   reconcile, advance or finish one. This is verification reuse, not permission
   to execute the candidate's lifecycle command. Preserve predecessor contract
   compatibility, and test this verifier against the selected generation.
3. Run the existing candidate `thread require-archived` on the exact root and
   selected authority/home. An active/missing/ambiguous root refuses before any
   member mutation. This preserves the normal root-before-team ordering. Keep
   the root retirement active-sibling refusal in the predecessor's ordinary
   replay; do not weaken it or rely on discovery hiding siblings.
4. Run the same candidate helper's **nonforced retained-only** team archive on
   the exact workspace/slug/root/cwd/socket/home/authority tuple. Proposed private
   invocation is `workspace-portal team archive --retained-only` with the same
   identity arguments as the existing `team require-archived` call. Retain the
   normal bounded command context. Do not let the operator select an arbitrary
   executable, roster path, socket or shell fragment.
5. Run `team require-archived` after successful helper completion. It remains a
   strict proof gate; do not redefine active as archived or replace it with
   successful helper exit alone. Release creation/slug locks before predecessor
   invocation so it can acquire its normal locks. The parent retains the
   exclusive transition lock across this handoff.
6. Replay the exact selected predecessor's `dev-session archive` with the
   journal's existing mode and only its portal helper substituted. It rechecks
   tracking/merge/runtime identity, repeats ordinary root/team retirement
   idempotently, advances checkpoints, retires runtime and removes the journal.
   The candidate helper phase does none of those journal/runtime actions.
7. Verify unchanged selected profile/token/Codex and completion of the exact
   journal. Only after all authorized paused journals complete may ordinary
   preselection quiesce and package selection proceed. Deployment remains blocked
   until then; this amendment is a supported completion path, not a bypass.

The retained-only guard is necessary despite the current members being
materialized. `teamruntime/runtime.go:1611`'s normal `archiveAllLocked` can call
`recycleFreshMemberLocked` and `retryCreatingLocked` before idle checks. Recovery
must never enter that branch. Add a narrow policy/entry sharing the existing
archive implementation, rather than copying its archive/receipt logic. Under
one team operation lock, load the roster and validate **all** outstanding members
before any Codex or roster mutation: ready, retained thread ID, no retirement
intent, expected project where recorded, exact metadata/cwd/authority binding,
and either positive archived proof or a positively materialized active rollout.
Existing terminal members retain their ordinary exact retired-identity and
receipt-cleanup checks. An absent roster retains the supported root-only case;
malformed/ambiguous state is not absence.

For active members, combine existing exact archive classification with
`HeadlessThreadMaterialized` for current project-backed members; retain the
existing legacy identity contract where applicable. Missing rollout, fresh
metadata, pending replacement/removal, unknown/creating state or any identity
conflict refuses. Recheck through normal idle/archive/proof calls under the same
operation lock. An explicit retained-only policy must continue to refuse if a
file disappears after initial validation; do not fall through to fresh-member
recovery. Do not expand active compatibility by creating a missing project or
by accepting an unproved format. No turn content is needed for the materialization
check. Normal turn-status/prompt/queue/receipt inspection remains mandatory.

Then reuse the existing nonforced idle sweep: already-archived members require
resolved submission attempts without querying an archived queue; active members
require exact identity, idle turns, no pending prompt, no queued message and
resolved submission attempts. `notLoaded` alone is insufficient. Only active
members receive `ArchiveThread`. On success or uncertain response, require fresh
exact archive proof. Clear attempts only through existing resolved-attempt cleanup
after proof, then persist that same member as archived. Keep all IDs/projects
and unresolved receipts. Never call interrupt, unarchive, start, resume, injection,
project creation/deletion or member replacement from this route.

A process interruption can leave more members archived, some ready bookkeeping,
and the same `tracking_committed` journal. Retry re-proves exact states and
continues: it does not unarchive to compensate or repeat archive for a member
already proved archived. Helper/proof failure prevents predecessor execution;
predecessor failure leaves ordinary journal recovery intact. Completed member
retirements are durable forward progress, not a transaction to reverse.

Exact implementer file brief:

- `libexec/workspace-host`: insert guarded retained-team completion between root
  proof and final team proof; retain all source/profile/journal/creation guards,
  predecessor invocation and postcondition checks. Use the existing session
  verifier/lock implementation for the new pre-mutation check.
- `libexec/dev-session`: only a small reusable verification/lock entry if needed
  to call the existing committed-archive verifier without journal/runtime
  mutation. Do not introduce a second lifecycle executor or broaden archive
  command flags for the predecessor. Keep journal/schema contracts unchanged.
- `portal/internal/teamruntime/runtime.go` and
  `portal/cmd/workspace-portal/main.go`: expose the retained-only nonforced policy
  privately and reject it on unrelated commands; share normal archive logic.
  Require the same deployed authority arguments as archive preflight. Ordinary
  archive and forced deletion keep their existing fresh-member contracts.
- Tests: `test/workspace_host/archive_recovery_test.rb`, existing session archive
  verifier tests, `portal/internal/teamruntime/runtime_test.go` and focused CLI
  tests. `docs/workspace-portal.md` must explain partial-team recovery and its
  failure/retry boundaries. The architect edits only this design document;
  application/tests/project docs belong to the implementer.

#### Focused tests and disposable reproduction

Required regressions before another live attempt:

- One archived plus two materialized active ready members: root proof precedes
  the helper; only the two active exact IDs receive archive requests; all three
  reach archived bookkeeping without changed thread/project identity. Final
  proof precedes the selected executor. Include provider-filtered empty lists.
- All members archived but ready roster: no archive/start/resume calls; resolved
  receipts are reconciled and roster states persist. Exercise the September 27
  shape independently of the mixed case.
- Interrupt after archive acknowledgement, after proof but before cleanup, after
  cleanup but before roster write, between members, and before executor entry.
  Repeat the same recovery and preserve exact identity and the existing journal;
  no duplicate archival of proven archived members or loss of unresolved attempts.
- Wrong/missing root proof, journal phase/operation/root/workspace, incompatible
  predecessor, changed generation/token, unfinished creation or competing
  operation, dirty/mismatched committed archive and changed recorded merge proof
  all refuse **before the team mutation**. Ready creation records remain byte
  identical. Predecessor is never called on failed final team proof.
- Active turns, pending prompts, queued messages, unresolved attempts, missing
  active rollout, fresh/unmaterialized member, replacement/removal intent,
  malformed roster and metadata/header/authority disagreement refuse. Assert
  zero fresh-member recycle/start/resume/inject/project calls. Add a disappearance
  between precheck and archive to prove it cannot activate the ordinary recycle
  branch. Keep unrelated normal archive/fresh-member tests passing.
- Verify transition -> creation -> slug -> team-operation lock order, release of
  creation/slug locks before predecessor reacquisition, and generation rejection
  after a wait. Existing normal switch/candidate switch still refuse unfinished
  journals; root active-sibling rejection and unsupported predecessor rejection
  remain intact. No profile/service/Codex mutation during helper recovery.

A synthetic pinned-App-Server reproduction can corroborate the source without
production access. It is a verification brief, not a run performed here:

1. Allocate a fresh disposable directory containing synthetic workspace, isolated
   `CODEX_HOME`, socket and application state. Assert no path/ID equals a real
   session or production home/socket. Use exact pinned 0.155.0 binary
   `/nix/store/5ic3470w8g40xyzqypbdzsvz9y3251ky-codex-0.155.0/bin/codex` and generated
   schemas. Copy no production database, rollout, config or credentials. Use the
   App Server test harness/mock provider; model network calls are unnecessary.
2. With the normal app-owned headless setup, create one synthetic root and three
   project-bound members, paginated persistent histories, and fixed developer
   bootstrap markers. Save only generated IDs, metadata/header identity and
   operation results. Archive the root and one member through supported exact
   requests; keep the roster ready to model interruption before bookkeeping.
   A second fixture archives all members while retaining ready bookkeeping.
3. Compare exact reads with state-only listings using omitted, mismatching and
   explicit matching provider filters, both archive flags and bounded cursor
   exhaustion. Record source/preview policy independently; developer-only
   fixtures may be omitted even with a matching provider. Do not insert a fake
   production user turn or change a production provider to make a list pass.
4. Run the packaged recovery against disposable predecessor/candidate profiles
   and a valid committed synthetic late journal. Verify mixed and all-archived
   completion, lost responses and helper interruption/retry. Confirm unchanged
   predecessor selection until its exact journal completes, then exercise normal
   switch. Any App Server restart or fixture corruption injection is confined to
   these disposable test resources. Nothing runs against production members.

Quick checks use the declared Nix environment: focused Ruby recovery/session
verifier tests and syntax, focused Go teamruntime/CLI tests, and `git diff --check`.
After committed implementation and independent lifecycle/mixed-generation review,
use the required fresh verification watcher for complete Nix/package checks and
this disposable end-to-end test. If a future fixture actually contradicts exact
Codex archive/read state, preserve it and reopen a separate upstream issue; the
current evidence does not justify a speculative Codex patch.

Acceptance is the tested ordered helper sequence, fresh proof for each archived
identity before receipt cleanup, successful selected-predecessor journal
completion, unchanged profile/Codex during bootstrap, and a subsequent ordinary
package switch. Live recovery remains separately authorized and was not attempted
by this architect. No manual database/filesystem/journal/roster repair, no
unarchive, no candidate selection before recovery, and no host configuration
change is part of this design.

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
periodic full-scan cost in the latency benchmark. Exact archive proof remains the
selected implementation. The September 30 database/source evidence closes the
suspected Codex inconsistency: the adapter must complete the legitimate partial
team phase under the guarded retained-only contract above. No Codex patch or
version change is needed. Review and verify that correction before another live
retry; unfinished journals still block deployment. Predecessor/helper
compatibility and crash/retry preservation remain verification requirements.
A plausible path name or an empty listing is not acceptance evidence.


## Host-auth amendment: failed live latency gate

### Evidence, ownership and selected fix

The lead deployed reviewed application package
`/nix/store/bn4wz9lbvikp8bkfv10xaw8i4v9ffzl4-dev-workspace-0.2.0`.
`browser-benchmark-deployed-no-scan.log` records 30 successful loads, 30 paged
responses, zero legacy responses, 11 rendered messages and no page exceptions.
Nearest-rank p95 usable time is **8.725 seconds**, so functional correctness has
not met the unchanged **2-second** performance gate. One HTTP error response is
also counted in that log; retain/classify response failures when comparing the
next run rather than describing the run as error-free.

Lead resource timing places about 1.49 seconds in document Basic Auth TTFB,
1.17/0.83 seconds in asset batches, and 3.35 seconds waiting for ten concurrently
launched API calls. The successful `/thread/page` request itself takes about
0.69 seconds. The host's synthetic `htpasswd` measurements are approximately
336 ms per cost-12 verification versus 14 ms at cost 5; ten cost-12 checks match
the roughly 3.36-second API delay. These measurements and the module's literal
`htpasswd -niBC 12`/cost-12 validator identify authentication CPU as the dominant
remaining bottleneck. They do not prove every delay is bcrypt or guarantee that
reducing its cost alone will meet the browser gate.

**Selected implementation:** add
`services.dev-workspaces.auth.bcryptCost` in dev-workspace's host module, with
`lib.types.ints.between 4 17`, **default 12**. Set **5 only on aitherdev** in
vpsfree-cz-configuration. The documented Apache `htpasswd -C` range is 4 through
17; use an integer option, not arbitrary shell text, a hash-prefix override or
an automatic hardware-dependent calibration. Costs 4 and 17 are supported
boundary values, not recommendations for this deployment. Keep the generic
example/default at 12 so unrelated installations retain their existing cost.
[Apache htpasswd reference](https://httpd.apache.org/docs/2.4/programs/htpasswd.html).

This is the smallest change to the measured bottleneck: no auth cache, bearer
session/cookie scheme, bypass for assets/API/SSE, password rotation, browser
request batching change or application protocol change. TLS, per-request Basic
Auth, nginx Authorization-header stripping, host firewall/access scope and file
permissions remain required. A user-profile package switch cannot change this
system-owned htpasswd; **vpsfree-cz-configuration is now an affected project**.
The previous no-host-change constraint is superseded only for this amendment.

### Security rationale and exact generation contract

The password source is generated by `openssl rand -hex 32`: 64 printable ASCII
hex characters representing 256 random bits. At 64 bytes it fits within bcrypt's
72-byte password limit. Lower cost reduces the work of every offline/online
guess; it does not remove the impractical search space of this independent
random secret. The theoretical bcrypt work reduction from 12 to 5 is 128-fold;
process overhead means measured wall-clock ratios need not match it. Faster
online guesses are an accepted tradeoff for this random credential, and lower
per-request CPU also reduces the authentication work an attacker can impose.
This does not claim denial-of-service prevention.

The low-cost site exception depends on the generated secret retaining its
entropy and secrecy. A file matching 64 hex characters does not prove randomness;
the deployment relies on the established generator/provenance, not syntax alone.
Human-chosen or reused passwords are outside this justification. Ordinary
password-storage guidance recommends bcrypt work factor at least 10; retaining
12 as the generic default and documenting the aitherdev exception avoids turning
this decision into a general password recommendation.
[OWASP Password Storage guidance](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).
A reader of the protected plaintext password already has the credential at any
cost; the change preserves the trusted-local-operator boundary and existing
root/group-readable files. Never print a real password, Authorization header
or htpasswd record in logs, test output or deployment evidence.

Use the same validated option for both hash generation and acceptance:

- Pass the decimal integer to `htpasswd -niBC <cost>` and supply the existing
  password on stdin. Keep credentials out of argv and the Nix store.
- Compute an exact two-digit encoded cost (`5 -> 05`, `12 -> 12`) at Nix
  evaluation. The regex for aitherdev must be
  `^[^:]+:\$2[aby]\$05\$[./A-Za-z0-9]{53}$`; at default it remains the same
  regex with `12`. Do not accept any two digits or unpadded `5`. Retain separate
  exact username equality, the complete-file/single-entry check, the existing
  terminal-newline convention, regular/nonsymlink checks, owner/group/mode
  checks, and `htpasswd -vi` verification against the current password source.
- An otherwise valid cost-12 hash is invalid for declared cost 5 and vice versa.
  Reject the cost mismatch before doing expensive password verification. A
  current-cost hash still has to verify; matching shape alone is insufficient.
  Preserve validation of the 64-hex password file; malformed persistent password
  state fails rather than causing silent credential rotation.
- Reuse the existing substrate `flock`. Generate in a mode-restricted temporary
  file in the htpasswd's own directory, set `root:<nginx group>`/0640, validate
  the candidate with the same exact-cost/password checks, then `mv -T` over the
  live htpasswd. Never truncate/rewrite the live file in place. Generation or
  validation failure leaves the prior auth file and password intact and exits
  nonzero. A crash may leave only a private staged file; retry validates the live
  output and publishes a complete candidate, without sweeping unrelated state.
- The first cost change produces a new salted hash only. Password bytes/inode,
  username, CA, TLS pair and unrelated state stay unchanged. Once reconciled,
  the same declaration preserves htpasswd bytes and inode on rerun; do not
  rehash merely because bcrypt generates a fresh random salt. Existing renewal
  and activation paths use the same option and validation rule.

### Exact files and verification brief

Implementation belongs in these repositories/files:

| Repository/files | Change |
| --- | --- |
| dev-workspace `nix/host-module.nix` | Integer option/default/bounds, exact padded-cost regex and generation argument; reuse atomic reconciliation. |
| dev-workspace `nix/tests/host-module.nix` | Evaluate default/custom/boundary/invalid options and inspect generated reconciliation behavior. |
| dev-workspace `nix/tests/host-module-idempotency.nix` | Real nginx/auth checks and 12 -> 5 -> 12 -> 5 generation/idempotence/failure coverage in the disposable VM. |
| dev-workspace `test/host_auth_benchmark.py` (new focused harness), `flake.nix` if needed | Synthetic credential verification report and deterministic generated-cost regression check using declared Apache tooling. Keep it separate from browser measurements and VM timing assertions. |
| dev-workspace `docs/workspace-portal.md` | Explain option, random-secret exception, cost regeneration, mixed-system-generation behavior and rollback. |
| vpsfree-cz-configuration `cluster/cz.vpsfree/machines/aitherdev/config.nix` | Set `services.dev-workspaces.auth.bcryptCost = 5` beside the existing auth username. |
| vpsfree-cz-configuration confctl-managed `flake.lock` | Pin the reviewed generic module revision through channel `dev-workspace`, role `devWorkspace`, input `devWorkspace`; keep generated pin commit history. |

Do not change codex-web, Codex/llm-agents, system model configuration, site
extension behavior, TLS/security defaults for other hosts or the consuming
user-profile pin chain solely to deliver this host option. The module input
already exists in configuration `flake.nix`; aitherdev's `module.nix` already
selects channel `dev-workspace`, and `config.nix` imports its `nixosModules.host`.
An additional flake input or system installation of the workspace application
is unnecessary. Lead/implementer own any tracking or project-document edits
outside this architect's design.md-only assignment.

Quick deterministic checks, in repository Nix environments:

- Assert default 12 and evaluated custom 5; option type accepts integer bounds
  4 and 17 and rejects 3, 18, fractional values, strings and null. Inspect the
  generated script for matching exact padded regex and generation value at 5,
  12 and boundaries. Do not actually hash at 17 just to test the upper bound.
- Generate an isolated cost-5 credential with the packaged `htpasswd`; parse
  its encoded cost and verify correct password succeeds and incorrect password
  fails. A harness expecting cost 5 must fail immediately on a cost-12 fixture,
  before timing it. This catches an accidental hardcoded generation cost without
  relying on machine speed. Ensure a cost-12 declared fixture remains supported.
- Preserve/refuse the existing malformed shape, extra username/record, unsafe
  file type/mode, wrong user and wrong password cases. Specifically test `$5$`,
  `$04$` and `$12$` rejection when `$05$` is declared, supported `$2a/$2b/$2y`
  variants where the packaged verifier supports them, and unchanged permission
  and source-password checks. Shape acceptance never overrides verifier failure.
- Run `nix flake check --no-build --show-trace`, the focused host-module check,
  formatting/shell checks and `git diff --check`. Evaluate the actual aitherdev
  configuration and require its option and generated script to select 5 before
  allowing deployment; a generic custom-option fixture alone cannot catch a
  site override being dropped.

After implementation commits and required independent security/compatibility
review, run the NixOS VM test through the fresh verification watcher. Extend its
existing specialisation pattern to switch cost while keeping all other host
settings equal. Verify authenticated proxy success and unauthenticated/wrong-
password rejection at each cost. Validate `$12$` initially, `$05$` after the
site-like switch, `$12$` on rollback, and `$05$` on reapply; a second reconciliation
at each setting must preserve auth bytes/inode. Password, CA and TLS outputs
must remain identical through cost-only switches. Reuse existing locking and
malformed-state tests; include interrupted/failed auth generation before atomic
publication and a concurrent reader that sees only a complete old/new auth file.
Test a valid same-cost hash for the wrong password is regenerated successfully.
Never disable auth or accept a malformed file as failure recovery.

The focused benchmark uses fresh synthetic 64-hex secrets, local temporary files
and stdin only, never production credentials or the live auth file. Use the
Apache executable selected by the tested Nix environment. Report executable
revision, declared/encoded cost, sample count, all verification outcomes, median
and p95 per-verification elapsed time, and totals for five batches of ten serial
verifications; warm up outside the sample. A cost-12 comparison uses its own
synthetic hash and reports the ratio. It must verify cost labels, not infer cost
from speed. The reproducible CI gate is exact encoded cost plus verification
behavior. Do **not** add a millisecond unit-test assertion or a required speedup
ratio: scheduler load, process launch and VM/CPU differences make those flaky.

On otherwise quiet aitherdev, use **0.5 seconds for a ten-verification cost-5
batch** as the diagnostic auth budget (all five measured batches), against the
observed roughly 0.14-second expectation. Exceeding it blocks acceptance pending
investigation of host load/tooling and a recorded rerun; it does not automatically
lower the cost or replace a failed browser sample. Timing is measured during
rollout, not a portable unit-test contract. Exact cost checks prevent silent
regression to 12 even if a fast CI machine masks its delay.

### System ordering, compatibility, rollback and recovery

There is **no session, database, runtime-authority, journal, manifest, ledger or
protocol format migration**, and no Codex version change. The htpasswd is derived
state in the existing bcrypt format. New nginx/old nginx consumers already read
that format; changing its cost does not rotate the shared password or invalidate
browser Basic Auth credentials. Existing unconfigured deployments still produce
cost 12 and should preserve valid files. The new Nix option is additive: an old
module revision cannot evaluate a configuration that sets it. Pin the supporting
module and site assignment together; rolling the pin back alone while retaining
that assignment is unsupported and should fail evaluation.

Ordered delivery, separate from the already deployed user-profile application:

1. Review/verify the dev-workspace module change and exact host-module diff. In
   this initiative's configuration feature worktree, use
   `confctl inputs channel set --commit dev-workspace devWorkspace <reviewed-rev>`
   for the exact feature revision (or normal channel update for an accepted
   published revision). Do not manually edit a channel-owned lock. Inspect
   transitive changes; keep nixpkgs, llm-agents and unrelated host inputs fixed.
2. Add the aitherdev-only setting, record exact module/config/system revisions,
   inspect its evaluated cost and generate the configuration diff. Build only
   `cz.vpsfree/machines/aitherdev` with `confctl build`, then run
   `confctl deploy cz.vpsfree/machines/aitherdev dry-activate` and inspect its
   service/activation plan. No remote default-branch integration is implied.
   An unexpected local kernel build still requires stopping and investigation.
3. After applicable system-deployment authorization, deploy that reviewed host
   configuration with the supported confctl switch flow. Preserve the active
   application profile and App Server; no workspace package switch, Codex restart
   or session quiesce is required for this auth-only change. Avoid concurrent
   system activations/manual old reconcilers. Let an in-flight old renewal finish
   before switching; the substrate lock serializes writers, but does not choose
   which generation's declared cost should win.
4. Confirm the selected system's reconciliation completed and its renewal unit
   uses that generation. Check only the encoded cost/ownership/mode and success
   results, without recording the full hash. Verify same-password authenticated
   access, unauthenticated/wrong-password denial and TLS, then run the selected
   reconciler again to establish idempotence. If an older in-flight process wrote
   last, finish it and rerun the selected reconciler; do not edit htpasswd by hand.
   Routine system activation/renewal supplies nginx configuration/reload handling;
   do not add an application restart merely for a changed hash file.
5. Re-run the browser gates below on the recorded system + user-profile pair.
   Do not claim the initiative ready for use from the synthetic timing alone.

System rollback is distinct from the forbidden earlier **user-profile** rollback.
A previously built compatible system generation still accepts the unchanged
password; its old literal cost-12 validator will detect `$05$` and atomically
regenerate `$12$`. A new module with `bcryptCost = 12` does the same. A rollback
therefore restores compatibility but can restore the latency failure. It does
not restore the old hash bytes, since the regenerated salt changes; a subsequent
same-generation rerun must stabilize. Reapplying the cost-5 system regenerates
`$05$` once. Test these transitions before live use and never run old/new
reconcilers concurrently as an ongoing arrangement.

If generation/verification fails, retain the complete previous auth file and
report failed activation. Do not delete the password, weaken TLS/auth, expose an
unauthenticated fallback or manually patch credential files. Recover through a
corrected declared module/configuration or a compatible system-generation
rollback, using the same substrate lock and verification. Confirm actual encoded
cost after recovery; a selected generation alone does not prove reconciliation
succeeded. Retain ordinary forward-only user-profile recovery rules.

### Live acceptance and remaining risks

Keep both original gates: **30 authenticated browser loads with no scan and 30
with an overlapping observation-only/dry-run scan, each p95 usable <= 2 seconds**,
nearest-rank 29th sorted sample. Use the same browser/viewport/cache policy and
navigation-to-usable definition, count failed loads/timeouts, and preserve
functional checks for recent paging, older history, receipts/uploads/prompts and
SSE gap recovery. For the paging-capable target require paged responses, zero
legacy fallback and no page exceptions; record/classify every failed HTTP
response. Do not hide delays by preloading assets outside the established policy
or subtracting auth time from usable time.

Record document/assets/API resource timing and CPU after the system change,
along with synthetic auth measurements and exact selected system/profile paths.
Ensure runs cover a natural metadata-cache maximum-age expiry (60 seconds),
including periodic bounded full-scan cost; space navigations or extend observation
as needed without changing how each load is timed. The scan must actually overlap
measured loads and remain a dry run; this design authorizes no new session
archival. Preserve existing 5-second active/30-second idle activity and scan-lock
acceptance requirements.

The cost-5 reduction is selected from measured evidence, not a promise of an
end-to-end result. Residual RPC/startup/asset latency may still miss 2 seconds;
if either browser gate fails, keep the initiative open, retain the failure
samples and investigate the remaining critical path. Do not silently relax the
gate, lower the site cost again, change other deployments' defaults or declare
success from 30 functionally successful loads. Only design.md was changed by
this assignment; implementation, security review, VM checks and host deployment
remain separate work owned by the lead/implementer.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-29-portal-performance/
