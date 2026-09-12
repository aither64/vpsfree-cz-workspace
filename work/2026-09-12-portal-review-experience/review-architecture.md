# Architecture and repetition review

Reviewed the four committed ranges from `review-packet.md` directly, including
their commit series, local repository instructions, shared contracts, tests and
actual dependency graph. The reviewed heads are `codex-web` `bba2ae1d`,
`dev-workspace` `774c2083`, `vpsfree-dev-workspace` `d0ebe39e` and `workspace`
`bfc80f25`.

## Findings

### Important: terminal creation receipts exhaust a lifetime-wide 512-entry budget

Commit `5bcf254f` makes every accepted creation receipt a permanent member of
`Server.creations`. `portal/internal/web/creation.go:101-105` returns an old
receipt forever for a reused request, and `portal/internal/web/creation.go:121-137`
rejects every new creation once the map contains 512 receipts. On restart,
`portal/internal/web/creation_store.go:112-145` loads every primary receipt,
including `ready` and `failed` receipts, without an age or lifecycle condition;
more than 512 files abort `web.New` through
`portal/internal/web/server.go:277-280`. A repository-wide search found no
production removal, retirement or compaction path for either primary receipts
or their completion evidence.

This limit therefore counts the workspace's historical creations rather than
concurrent or recoverable operations. Since normal session names are unique and
dated, a long-lived portal deterministically stops accepting new sessions after
512 creations. Retiring a session worker or archiving/deleting a session does
not release a slot. Keep durable receipts while retry/recovery can still need
them, then transfer or compact the necessary terminal proof under an explicit
lifecycle rule. The safety bound should apply to active/recoverable operations;
terminal history should not make creation or server startup fail. Add coverage
that crosses the retention boundary and preserves idempotency for an incomplete
attempt.

### Important: the authority activity ledger has no retention contract and rewrites all history on each checkpoint

Commit `bba2ae1d` stores all thread intervals and all request boundaries in one
authority-wide ledger (`codex/activity.go:54-67`). State transitions append
intervals (`codex/activity.go:285-299`), while resolved and turn-completed
requests are marked with `ResolvedAtMS` but retained
(`codex/activity.go:345-436`). No `ActivityRecorder` operation retires or
compacts a thread or a resolved request. Stopping a portal worker only removes
the worker (`dev-workspace` commit `774c2083`,
`portal/internal/web/activity.go:99-113`); it does not retire the recorder data.

Every observed event and every reconciliation marshals that whole ledger,
writes and fsyncs a new file, renames it and fsyncs its directory while holding
the recorder mutex (`codex/activity.go:180-227,327-436,451-491`). The portal
reconciles each owned session every five seconds while active and every thirty
seconds while idle (`portal/internal/web/activity.go:132-188`). Work and storage
therefore grow with all historical sessions and request events. At the shared
64 MiB `readLimit` (`codex/client.go:25-29`), the next checkpoint fails, reloads
the last ledger and leaves activity coverage unavailable; every subsequent
checkpoint attempts the same oversized update. This eventually disables the
new timing feature for every thread on the authority.

Define ownership and retirement for completed/archived threads and resolved
request boundaries. Preserve required historical totals in bounded per-thread
summaries or an equivalent compact representation, and avoid an authority-wide
full-file fsync for every poll. Exercise sustained event volume, retirement and
restart at the storage bound.

### Important: one old thread serializes all activity history reads and can block live event capture

Commit `bba2ae1d` holds the single client-wide `turnHistoryMu` across every
paginated App Server request for one thread
(`codex/turn_history.go:74-168`). It then holds the single recorder-wide mutex
while comparing every turn with every retained interval
(`codex/activity.go:494-590`), an O(turns × intervals) calculation. The
WebSocket read loop calls `ActivityRecorder.observe` synchronously
(`codex/client.go:669-687`), so it cannot receive more protocol messages while
that same recorder mutex is occupied.

Commit `774c2083` starts one worker for every owned active session and lets all
of them call `ReadActivity` (`portal/internal/web/activity.go:87-113,132-188`).
The four-second context bounds App Server requests, but it cannot cancel a
goroutine waiting on either `sync.Mutex`. A sufficiently old thread can thus
hold the history lock over many RPC pages and the recorder lock over the nested
aggregation; other session workers time out in a queue, while live lifecycle
events stop being read and recorded. The current provider pagination test uses
41 turns (`codex/activity_test.go:322-402`), and the portal monitor test covers
one worker rather than concurrent long histories.

Use per-thread history synchronization, copy the target thread's recorder state
under the mutex and calculate outside it, and index or sweep ordered intervals
so aggregation is linear in the thread history. Bound or coalesce monitor work
so many sessions cannot create an unbounded synchronized poll burst. Add a
multi-thread stress test that proves a large history cannot delay event capture
or unrelated activity reads beyond their deadlines.

### Advisory: the browser renderer repeats the provider's typed-event registry

Commit `d56ad40d` selects typed events in Go with the list `webSearch`,
`collabAgentToolCall`, `subAgentActivity`
(`codex/client.go:3073-3077`) and normalizes the same cases in
`codex/transcript_activity.go:39-128`. The shared browser renderer repeats that
list before it will render an otherwise valid `entry.activity`
(`conversation/assets/conversation.js:60-65`). The exact-pinned portal then
capability-probes the required export with optional chaining
(`dev-workspace` `portal/internal/web/static/app.js:1922-1935`).

Adding a fourth normalized activity kind requires coordinated edits in both
language layers; omitting the JavaScript whitelist silently falls back to the
generic transcript presentation. Let the presence of validated typed activity
data, or one provider-owned explicit discriminator, select the shared renderer.
Given the exact package/asset pin, the portal can also validate the required
export once at initialization rather than hiding a packaging-contract mismatch
at each call.

## Cross-project contract and pin assessment

The interface ownership is otherwise sound: `codex-web` owns protocol
normalization, passive observation and the shared browser renderer;
`dev-workspace` owns session authorization, lifecycle orchestration and local
repository review; the two downstream repositories only wrap and deploy the
runtime. I verified the actual feature pin chain rather than relying on the
packet: `dev-workspace/flake.nix` and `portal/go.mod` resolve `codex-web`
`bba2ae1d`; `vpsfree-dev-workspace/flake.nix` resolves `dev-workspace`
`774c2083`; and `workspace/flake.nix` resolves the organization wrapper
`d0ebe39e`. Their lock files carry the same nested provider revisions.

The standalone `codex-web` conversation renderer remains the other direct
consumer. The additional production-configuration consumer discovered at
`vpsfree-cz-configuration` `origin/master` currently pins the reviewed base
revisions, `dev-workspace` `bcbaf825` and `codex-web` `269962eb`, and does not
consume the new interfaces. The provider additions remain source-compatible
for that older consumer. Delivery order remains provider, generic runtime,
organization wrapper, then workspace profile.

No Blocking findings were identified. Beyond the findings above, residual
evidence gaps are the packet's unrun live App Server/browser, packaged
upgrade/rollback and long integration checks. The local repository-review
boundary is appropriately isolated behind opaque comparison IDs and a native
Git reader; I found no additional ownership or repetition issue in that path.
