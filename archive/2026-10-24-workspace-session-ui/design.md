# Portal session controls and message delivery proposal

Status: design with upstream-refresh amendment, 2026-10-25. The user approved
implementation of all four fixes. The refresh brief below governs the new
baseline and supersedes conflicting earlier recovery assumptions. This architect
assignment remains investigation/design only. No application changes, tests,
commits, deployment or lifecycle actions were performed by the architect.
The lead owns plan/state and implementation assignments.

Current governing amendment: **Raw Codex 0.164 and naming-source takeover** at
the end of this document. The user rejected the native patch and authorized
prompt-controlled naming plus the named source changes. Earlier patch and
zero-tool naming proposals are retained as rejected history, not execution gates.

## Scope and evidence

Recommend four focused changes in `dev-workspace`: reuse the existing switches
for session settings, make New output depend on changes to displayed content,
accept another message while delivery of the preceding message is pending,
and keep routine queue checks silent.
Reuse `codex-web` delivery and native queue contracts. A new server queue or
Codex protocol change is not justified by the evidence.

Session identity was verified with `dev-session current` and both matching
`DEV_SESSION_SLUG`/`DEV_SESSION_WORKSPACE` variables. Initial investigation read
canonical bare repositories; subsequent assigned amendments also inspected the
owned session worktree. No other session's worktrees were accessed.

The proposal uses these locally cached `origin/master` revisions, without a
fetch or a claim that they are current deployed revisions:

| Repository | Inspected proposal baseline |
| --- | --- |
| dev-workspace | `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` |
| codex-web | `11ec57d2203fc735696fe75a837d47da55a5c6af` |

The former's `portal/go.mod` pins the latter. Initial inspection also read the
older bare local master heads `52dcd471186ef874c5c93f4133744195d4815454` and
`57972192e30fe52ab33b867c8fe4d171f59a7fd5`. Newer cached references were found
before finalizing the proposal. Source locations below use the proposal baseline.
This is source analysis, not a browser reproduction of the user's incident.

## 1. Consistent settings switches

Confirmed: `portal/internal/web/templates/session.html:85` and `:86` already
use native checkbox inputs with `role="switch"` for automatic retry settings.
Per-session notifications (`:93`), Keep open (`:102`), and Play sound in
`templates/notifications.html:33` still use ordinary checkboxes. The established
switch appearance is `.retry-policy-switch` in `static/style.css:280–288`.

Reuse that appearance and interaction for these persistent on/off preferences.
Give the reusable style a generic name or alias and update the existing retry
rows with it. Keep native `input[type=checkbox]` state/change behavior, add
`role="switch"`, retain stable IDs, and associate each label, help and status
with its control. Preserve keyboard Space, label clicking, visible focus,
checked/disabled appearance and a usable touch target. Avoid a second ARIA
checked state that can disagree with the native input. Support reduced motion
and ensure on/off remains distinguishable without color alone.

These are immediate-save controls. Preserve each existing endpoint and ownership
scope: session notification preference, browser sound preference, session hold,
and session-wide retry policy are different settings. Show saving/uncertain
feedback and the last confirmed value; disable the relevant control while its
write is pending. Preserve rereads, revision/identity checks and error recovery;
do not add automatic compensating writes. Retry policy already follows this
pattern in `static/app.js:2761–2827`. Changing appearance does not change when
Keep open is saved or grant permission to change the actual session hold now.

Leave action buttons such as permission/subscription setup and test notification
as actions. Leave acknowledgements, destructive confirmations and creation-form
options outside this settings-only change. The existing Save behavior of the
model/reasoning dialog is also unchanged.

## 2. New output follows displayed content

Confirmed: `static/app.js:4705–4707` shows New output whenever the newest-page
update has any changed entry and the reader is not following. Rendering filters
entries separately at `:4516` and `:4555`. Filtering delegates through
`:324–336` to `codex-web/conversation/assets/conversation.js:76–99`.
Messages hides team traffic and other activity; errors remain visible in every
view. Hidden entries can therefore trigger the button. This explains the
reported behavior structurally, without proving which event triggered it live.

Filtering only the changed keys is insufficient. The current comparison also
includes fields a reader cannot see: `transcriptContent` at `app.js:4446` removes
only timestamps before stringifying the remaining object. Collapsed details,
receipt fields, internal metadata, or raw text superseded by `displayText` can
change without changing the displayed message.

Use the rendered-content projection for the active filter and disclosure state
as the notification criterion. Compare stable entry keys and the fields that
actually determine the visible body, summary/status, questions, attachments and
labels. Exclude transport/receipt metadata, timestamp enrichment, hidden entries
and the body of closed disclosures. A closed disclosure's changed visible
summary still counts. Reuse the rendering decisions so the notification rule
does not drift into a separate approximation of filtering.

Maintain a small unread flag with each existing per-filter view state, rather
than deriving the button from only the last update. A visible content change
while paused sets it. A hidden-only or identical update neither sets nor clears
it. Streaming additions to an already rendered visible message count; repeated
snapshots and timestamp-only changes do not. Following the tail or selecting
New output clears the selected view after showing its latest content. Preserve
the current scroll anchoring and disclosure behavior.

On filter changes, show that view's state and clear it only if that view is
actually brought to its tail. Do not unconditionally clear unread merely for
switching filters (`app.js:4644` currently does). First load, thread replacement,
older-page insertion and historical gap repair establish history, not new-output
notifications. A repair that refreshes an already known streaming item needs a
case distinguishing a new visible final update from newly loaded old history.
Hidden tabs/sections must not acknowledge content solely because a poll ran;
returning to a following view can clear after restoring its tail.

This remains a local follow-tail indicator. It does not change session attention,
Web Push, acknowledgements, persisted transcript entries or server filtering.
It does not introduce a per-message read-receipt system.

## 3. Responsive submission with existing delivery semantics

Confirmed blocker at `static/app.js:4315–4316`: both Send/Steer and Queue next
are disabled by the global `messageDispatchInFlight` flag. `submitMessage` also
returns for that flag at `:5488`. Ordinary Send already saves and detaches the
draft before HTTP (`:5538–5557`), allowing typing and new uploads. Queue next
still locks all form controls (`:5499–5501`) until its request settles. The
existing behavior is documented in `docs/workspace-portal.md:437–454`.

Recommendation: separate capturing a submission from delivering it. On each
explicit submit, validate and save an immutable message/attachment snapshot with
its existing durable attempt ID, detach that draft, show its delivery state and
immediately allow the next draft and submission. Retain generation checks so a
late response never clears, replaces or focuses a newer draft. Extend the same
ownership transfer to Queue next.

Use a small ordered browser dispatch buffer, with one active HTTP mutation per
conversation. It feeds the existing endpoints:

| User action | Existing delivery contract |
| --- | --- |
| Send / Steer now | `/message`; server starts an idle turn or steers the active turn |
| Queue next | `/queue`; native `thread/queue/add` preserves queued work for later execution |

Preserve the chosen action; do not silently turn Steer now into Queue next.
Label locally waiting submissions distinctly from server-accepted queued work.
Once the preceding operation is accepted, dispatch the next without waiting for
model completion. Preserve FIFO dispatch for this browser's accepted submission
sequence. Native queued work retains its existing FIFO and head-only Start
rules. This does not promise one execution order across steers, queued turns,
other tabs, terminal input, team assignments and automatic retries.

The server already serializes conversation mutations
(`codex-web/conversation/handler.go:326`, `conversation/mutation_lock.go`) and
Send/Queue share a per-thread lock (`codex/client.go:4528`, `:5104`). Send reads
the active turn and supplies `expectedTurnId` for `turn/steer`. Distinct accepted
sends may steer the same turn; simultaneous native steer RPCs are not issued by
this client. These locks do not establish browser click-order FIFO for multiple
concurrent HTTP requests. Keep ordered dispatch instead of merely removing the
button guard.

Multiple browser submissions may wait safely in the proposed buffer; native
behavior for several steers pending consumption has not been established here.
Existing native FIFO recovery coverage is present in
`codex/recovery_integration_test.go` and queue/receipt contracts in
`codex/client_test.go`. Native steering order and the turn-ending race remain
implementation verification cases. Preserve today's server decision at dispatch:
`/message` can start a new turn if the former active turn has ended. A requirement
to steer only the originally displayed turn would be a separate API change.

Keep retry identities and original text/attachments through response loss.
Pause automatic draining on an uncertain outcome and reconcile that exact ID;
never retry it as a fresh message or let later submissions silently overtake it.
Definite validation failures retain an editable failed entry; later dispatch
needs an explicit retry or discard of the definitely unsent entry. Dismissing
an uncertain receipt is not proof it was unsent. Existing accepted/observed
evidence must win over a late HTTP failure. Intentional identical messages after
acceptance remain distinct; double-submit and retries of unresolved snapshots
must not duplicate them.

Reuse the existing multi-attempt storage, receipt and upload machinery. Retain
ordered pending intent across reload without automatically resubmitting unknown
attempts. The exact small storage representation and explicit resume behavior
need implementation design/testing: older browser recovery must not mistake a
locally waiting, never-dispatched entry for native acceptance. Storage failure
must leave the draft intact. Bound the local buffer and give an inline error if
it cannot accept another entry. Preserve conversation/member identity and current
authorization, lifecycle holds and retry-policy arbitration at actual dispatch.

## 4. Silent routine queue checks

Added after the original proposal. Identity was reverified; the cached canonical
references remain the baseline hashes listed above. Previously read applicable
workspace/repository guidance and the documentation skill remain applicable.
This is a presentation change, not a diagnosis of queue-read latency.

Confirmed source locations in `dev-workspace`:

- `portal/internal/web/templates/session.html:131` seeds the hidden queue status
  with “Checking queued messages…”.
- `portal/internal/web/static/app.js:5321–5328` renders that text and unhides the
  status for either `state.loading` or `state.warning`.
- `:5330–5360` owns the queue refresh. It reconciles durable queue deletions
  (unless execution is held), then reads the queue under one shared deadline.
  Only a successful valid response calls `renderQueue`; failures retain the last
  rows. Forced requests coalesce into one successor while a read is current.
- Callers are initialization (`:6055`), the regular interval (`:6060`),
  connection/reconnection (`:6048`), observed active-state changes (`:6038`),
  returning from suspended page reads (`:5373`, via visibility/pageshow/focus
  handling at `:3616–3638` and `:3677–3680`), queue removal (`:5302`), accepted
  Queue next (`:5569`), and queue Start (`:5623`). Failure backoff (`:5352`),
  coalesced reruns (`:5357`), and explicit Retry (`:5361`, the only caller with
  `manual=true`) also use this same function. Hidden/paused pages do not start
  reads; pause cancels notices and retries (`:5363–5374`).

The existing timing authority is `codex-web/conversation/assets/refresh.js`:
`refreshPolicy` at lines 3–17 defines initial loading at 750 ms, manual loading
at 250 ms, a 30-second visible failure grace period, a 30-second queue refresh
interval, a 12-second queue request deadline, and retry backoff from 2 to 30
seconds. `createRefreshNotice` at lines 19–74 owns warning and visibility timing.
Loading is already suppressed after a successful value unless the request is
manual. Consequently the visible healthy notice is expected during a slow first
read, including a new page visit. Repeated appearances after an established
successful read were not reproduced and should not be attributed to every poll.

Recommendation: keep the helper and all refresh/deadline/backoff paths, but make
the portal queue status render warnings only. Do not display its loading text
on initial load, routine refresh, reconnect or manual retry. Remove the unused
initial loading copy from the template as well. Do not extend the initial delay,
change global timing constants or add a separate timer. A slow healthy read can
finish silently; a timed-out read still fails through the existing deadline and
warning policy. The 30-second warning grace begins with the first failed read,
not at request start. Access errors and explicit Retry failures keep the shared
immediate-error behavior.

Retain the last confirmed queue during every refresh and error. Before the first
successful response, keep the queue region unassertive: do not invent an empty
queue or show “no queued messages.” When a warning is due, use `state.hasValue`
to distinguish “could not load” from “last result may be out of date,” with the
existing Retry action. While manually retrying an existing warning, keep that
warning visible until success and prevent duplicate Retry clicks using existing
read state; no replacement “checking” notice is needed. Do not hide warnings
with CSS or hide the complete queue region.

This change concerns observation only. Preserve actual queued entries, pending
submission receipts (“Sending…”/“Outcome unknown”), the proposed local waiting
submissions, validation/delivery errors, queue deletion/Start errors, and
connection warnings. Silent polling must not imply that a prompt was accepted
or that an uncertain queue mutation failed.

The reusable mounted UI in `codex-web/conversation/assets/conversation.js:1209–1213`
has a similar renderer, but the portal owns its own renderer. Changing that
mounted UI or the shared helper is unnecessary for this request. A new pure
helper could be authored independently, but would still require wiring in
`app.js` and would add abstraction for a small local change. Prefer a bounded
queue-notice edit at `app.js:5321–5361`, plus the template and tests, serialized
with the unread/composer edits. A dedicated
`portal/internal/web/queue_refresh_presentation_test.cjs` can be authored
independently; its harness registration and source integration need coordination.
Existing `refresh_presentation_contract_test.cjs` and
`page_lifecycle_browser_test.cjs` provide adjacent coverage.

Acceptance: a delayed successful initial read and later background reads show
no checking text; queue rows remain throughout delayed/error reads; initial
failure does not falsely claim a previous queue; persistent failure shows Retry
after the existing visible grace; success clears it; access/manual failures
remain immediate; hidden/restored pages retain current cancellation/grace rules;
actual send/queue receipts and mutation errors remain visible. Use injected/fake
time with the shared notice helper for quick presentation tests, plus the
shipped-browser harness to cover delay, failure, restoration and recovery.
No latency benchmark or native queue behavior change is required for this fix.

## Final-review disposition R3: attachment refusal and recovery

Bounded design amendment for the Important R3 finding relayed by the lead.
Reviewed implementation head: `5293cf5b`, base `b3a6eb2f`. Identity was reverified;
inspection used the owned worktree and pinned codex-web `11ec57d2203f` read-only.
R1/R2 fixes remain with their implementer. No application edits or tests were
performed for this disposition.

Decision: keep the fix inside dev-workspace. Recognize a finite set of exact
pre-submission validation responses for a fresh identity, then expose real
attachment replacement using the existing composer. A new response protocol or
general transaction framework is unnecessary.

The pinned handler establishes the sequence: `conversation/handler.go:590–595`
calls `prepareAttachments` and returns its error before `Client.Send` at `:604`.
Queue does the same at `:694–700`. `conversation/uploads.go:259–291` exposes an
`UploadError` as its exact status/text. Native client failures instead go through
`handler.serverError` and become generic 503 responses. The portal's
`uploads.Backend.Prepare` (`portal/internal/uploads/store.go:836`) only performs
catalog preparation; `prepareSubmission` validates files and encoded prompt
size before publishing its submission. It does not invoke Codex.

Use an explicit status-and-message allowlist, with source-bound tests:

| HTTP status | Exact response message | Owning pre-submission check |
| --- | --- | --- |
| 400 | `message and browser attempt ID are invalid` | pinned handler send/queue validation |
| 400 | `too many attachments` | pinned `prepareAttachments` |
| 400 | `attachment IDs are invalid or repeated` | pinned `prepareAttachments` |
| 400 | `attachments are unavailable` | pinned `prepareAttachments` |
| 400 | `message and attachment references exceed the prompt limit` | pinned `prepareAttachments` after preparation |
| 400 | `Too many files for one prompt` | portal `prepareSubmission` |
| 400 | `An attachment is unavailable, incomplete or repeated` | portal `prepareSubmission` |
| 413 | `Attachments exceed the prompt size limit` | portal `prepareSubmission` |
| 413 | `Message and attachment references exceed the prompt limit` | portal `prepareSubmission` |
| 409 | `An uploaded file is unavailable` | portal `prepareSubmission` file validation |

Do not classify by status alone, substring, case folding, or message text without
an HTTP response status. Do not classify unrelated upload endpoints. The
case/status difference between the two prompt-reference errors is intentional.
The existing blanket text comparison for the generic invalid-message error must
also gain the status check.

This inference applies only to a fresh first dispatch of a newly generated
identity owned by this tab, with no earlier possibly dispatched request and no
accepted/observed evidence. Do not infer freshness solely from a restored
`retry:false` field. A restored unknown entry, retry of an uncertain identity,
transport timeout/abort, generic 4xx/5xx, identity conflict or browser persistence
failure remains unknown. A rejection on a later request proves nothing about
whether an earlier request with the same ID ran. Persist the definite-failure
state before enabling replacement/discard; if that write cannot be confirmed,
retain conservative recovery. A previously persisted definite failure can retain
its edit/discard affordances on reload; it does not authorize reclassifying an
unknown receipt. Preserve R1/R2 ownership/storage recovery changes.

Queue has a post-acceptance `ObserveQueue` call at pinned handler lines 707–711.
Its current portal implementation (`store.go:1051`) decorates and records queue
observations; it does not emit any allowlisted validation error. Its catalog/I/O
failures remain unknown. Do not extend the allowlist to generic attachment errors
or all errors from `uploadError`, because those can occur after native acceptance.
Pin/source contract tests must fail if a future dependency reuses these exact
responses after dispatch; unfamiliar responses stay uncertain by default.

Recovery must change attachment IDs, not merely text. Keep existing Discard
unsent and ordinary text editing. Add a failed-head-only replacement action using
the main composer's current draft and existing upload selection. The user can
remove files, select/upload replacements, or provide text without attachments in
that composer and explicitly replace the unsent head. Show brief guidance in the
failed receipt; do not overwrite an already populated newer composer draft to
restore the old text. Its existing visible/copyable text remains available.

At explicit replacement, validate ready uploads and a nonempty text-or-file
snapshot, preserve the failed entry's send-versus-queue action and head position,
allocate a fresh ID, and take only the current draft's attachment IDs. Reuse the
existing durable attempt save, `replaceFailed`, draft-generation ownership
transfer and recovery ordering. Save/verify the replacement and detach its draft
before dispatching it; late responses must not clear later drafts. Retain the
old failed entry/recovery evidence if replacement cannot be confirmed. Do not
delete uploaded files or reuse the rejected immutable identity with changed
attachments. Discard explicitly abandons that proven-unsent item and lets later
entries progress. Unknown receipts expose neither replacement nor discard.

Implementation boundary: dispatcher classification and failed-receipt/composer
recovery in `portal/internal/web/static/app.js`; existing dispatcher contracts,
`composer_handoff_browser_test.cjs`, and focused portal upload/HTTP tests; short
portal-guide recovery text. No codex-web, upload catalog format, queue protocol,
lifecycle or provider-policy change. Serialize with the in-flight R1/R2 edits.

Required focused evidence before the affected review lane is rerun:

- Real handler plus portal upload backend: unavailable/incomplete/repeated file
  and encoded-reference/attachment-size failures return the exact status/body;
  fake Client.Send and Client.Queue counters stay zero. Exercise both endpoints,
  and retain native/post-Queue observation failures as uncertain cases.
- Dispatcher table cases: allowlisted response on a fresh first dispatch becomes
  failed; identical response after a lost reply, restored unknown identity, or
  explicit uncertain retry remains unknown and holds later entries. Wrong
  status, changed text, transport error and generic 4xx remain unknown. Positive
  acceptance wins over every late failure. Failed-state persistence failure
  does not enable unsafe edit/discard.
- Real browser: fail an attachment-bearing head, retain later waiting items,
  remove/reselect attachments in the existing composer, replace the head under
  a new ID and original action/order, and observe one accepted corrected message.
  Old IDs never reappear. Cover attachment-only input, text-only replacement,
  a newer draft, storage failure, reload and explicit discard. A text-only edit
  retaining invalid attachment IDs must not be presented as a complete repair.

## Upstream refresh brief — 2026-10-25

The lead reports completed local verification on the old feature. The following
is a source-based adaptation brief, not new verification or patch equivalence.
Session and environment identity were reverified. Read-only inspection used
canonical Git objects and this session's owned worktree only.

| Boundary | Exact inspected revision |
| --- | --- |
| Old dev-workspace base | `b3a6eb2fc0b41cf0cb965bf4c39991815d9df734` |
| Published feature before refresh | `064e311e6dc933bc9a0f5d7cd20eaf20eeccbbf9` |
| New upstream base, including `2c847e6d` recovery changes | `10bb047513c82d1310e8fcaa797e8772f948dd8a` |
| Old codex-web pin | `11ec57d2203fc735696fe75a837d47da55a5c6af` |
| New upstream codex-web pin | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` |

### Confirmed contract and recovery decision

New codex-web `conversation/handler.go:591–650` still prepares attachments
before sending. Admitted sends now survive browser cancellation within the
original deadline and shutdown boundary. `Send` errors expose two typed results:
503 with `code: message_not_sent, notSent: true`, and 409 with
`code: message_delivery_unknown, notSent: false`. Client-side error decoding
preserves these fields. `codex/send_delivery.go` and `docs/reference.md:52–65`
establish the proof: unwritten/explicitly refused sends remain prepared;
writer admission and reconciliation consult the shared ledger. Missing history
and interrupted writes remain uncertain. The ledger remains schema 3.

Use the exact typed `/message` nonadmission result as authoritative even for a
recovered or formerly unknown ID. Preserve the immutable message/options and
retry that same ID. Do not overwrite this proof with the feature dispatcher's
current `error.notSent = false` (`static/app.js:310` at the old feature).
Use upstream `unsent` for this retryable state, distinct from feature `failed`
for fresh validation rejection requiring editing/reselection under a new ID.
Neither state drains automatically; explicit recovery controls the next send.
Persist uncertainty before every attempted retry so reload cannot preserve a
stale unsent proof. Acceptance/observation always overrides a late error.

The R3 exact status/text allowlist above remains necessary: attachment preparation
and `/queue` do not supply the new typed proof. Its freshness limitation remains
unchanged. Generic errors, transport failures, persistence failures and untyped
refusals of recovered IDs do not establish nonadmission. Keep source-bound
zero-native-call tests; do not classify all 4xx or all upload errors. This is the
only change to the earlier R3 decision; no codex-web source change is needed.

### Ordered buffer and explicit recovery

Lead scope clarification: the confirmed-copy control remains limited to message
receipts, matching upstream. Unknown queued submissions use exact-ID queue retry
and observation, retaining their ordering hold until resolved. The buffered-head
copy below therefore preserves Send intent; later waiting entries can be sends
or queues. Do not add a queue-copy capability.

Lead disposition: retain automatic hold behind an unknown buffered head.
Ordinary fresh/reworded submissions are captured into waiting in click order;
they cannot overtake the head or existing waiting intent. This intentionally
differs from upstream immediate dispatch of revised wording. Retain Send/Steer
versus Queue next, single active HTTP mutation and readiness/hold checks at
dispatch. FIFO is local dispatch order, not cross-client or native consumption
order; multiple native steer consumption order remains an evidence limit.

Preserve upstream `resendMessageReceipt` (`app.js:5451–5478` at new base):
reconcile the exact original ID first, await that result, and offer another copy
only if it remains unknown. Require its existing duplicate-warning confirmation.
If reconciliation instead proves acceptance or nonadmission, use that state;
do not make a copy. The current dispatcher's fire-and-forget retry needs an
awaitable completion for this bounded path.

For a confirmed copy of the buffered head, keep the original receipt unknown
and its persisted `replacementId`, but substitute the new immutable copy ID at
that head position in the existing order buffer. Waiting entries retain their
relative positions and resume only after the copy is accepted or explicitly
resolved. This releases the original ordering hold by explicit user choice; it
does not mark the original delivered or unsent. Do not reuse `replaceFailed`'s
old-record retirement callback for this operation. Preserve the current draft
and uploader completely. Reuse the one existing receipt store and dispatcher;
do not create another registry or general transaction layer.

Before copy dispatch, save/verify the new receipt, the original's link and the
updated order. A repeated action or reload reuses that saved replacement ID,
never allocates another automatically. Reload remains paused. If interruption
leaves a linked original at the head, recover its saved replacement into that
position only when the existing records agree; otherwise preserve records and
stop dispatch with an actionable storage/recovery error. Audit existing orphan
cleanup/rollback: a replacement reachable from an original link or order entry
must not be deleted as an unused attempt; uncertain readback cannot prove it
unreferenced. Test these short write boundaries rather than adding speculative
metadata. Any need beyond existing IDs/link/order goes back through the lead.

Retain legacy/nonbuffer unknown receipts and their upstream reconcile/copy
controls without making them global automatic holds. Their explicit recovery
must still respect the one mutation lane; a new copy joins the existing order
at the tail unless it replaces its own buffered head. Exclude linked originals
from content-based attempt matching. Preserve `unsent` and `replacementId` in
the existing receipt decoder/encoder (`app.js:821–830` at new base).

### Implementation boundary and checks

The lead has selected implementer1 for the overlapping refresh. Keep this one
serialized package: `portal/internal/web/static/app.js` dispatcher/receipt/store/
submission feedback; `templates/session.html` readiness; affected contract and
browser tests; and `docs/workspace-portal.md`. Preserve the other three fixes
(switches, visible-content unread, silent healthy queue refresh) during conflict
resolution. Carry upstream pins together in `flake.{nix,lock}`,
`nix/workspace-portal.nix`, `portal/go.{mod,sum}`; do not restore the old pin.

Preserve upstream `beginSubmission` generation tokens and stale-banner rules
(`app.js:5507–5526`): late older failures cannot restore a stale banner; newer
successful dispatch/recovery clears it without retiring uncertain receipts.
Carry the operation token through dispatch completion, retry and Queue Start;
capturing waiting intent is not delivery success. Retain initially disabled Send
until conversation assets/state are ready, while allowing repeated captures once
ready. Do not reintroduce a global in-flight guard on ordinary draft capture.

Quick acceptance before affected review:

- Extend `composer_handoff_contract_test.cjs` and
  `submission_notice_contract_test.cjs`: typed unsent on fresh/recovered IDs,
  same-ID retry, uncertainty persisted before retry, late proof wins, stale
  generation suppression and independent Queue Start feedback.
- Preserve `submission_validation_contract_test.go` real-handler assertions
  for the R3 allowlist and fresh-versus-restored distinction at the new pin.
  Typed nonadmission and attachment validation must expose different recovery.
- Extend copy contracts for reconcile accepted/unsent/unknown, declined confirm,
  buffered head with later waiting send/queue, legacy receipt, repeated clicks,
  reload and each receipt/link/order write/readback failure. Preserve both
  identities and the newer draft; no duplicate, orphan deletion or bypass.
- Adapt upstream `message_delivery_browser_test.cjs`, retaining its coverage:
  reworded submission waits, explicit copy retries original then uses one fresh
  ID ahead of later waiting entries, original receipt/link survives reload,
  accepted copy/newer success clears stale feedback, and typed unsent retries the
  same ID. Keep delayed-asset readiness and Chromium **and Firefox** execution.
- Run repository-pinned syntax/aggregate browser contracts and affected Go web
  checks; preserve asset-version/harness registration checks.

After committed adaptations and quick checks, rerun independent affected lanes
against the full new base-to-head range; this intersecting baseline is not a
certified-equivalent refresh. Then use the existing watcher plan for flake
evaluation, CI-aligned fast/package checks, composer/paging/message-delivery
real-browser subtests, and proportionate pinned native/admission coverage. The
browser environment must include Firefox as well as Chromium for the new test.
Old green evidence remains tied to the old head and pin. No unrelated host/VM
suite is added by this brief.

Compatibility: retain existing receipt identities, replacement links, pending
order and schema-3 server ledger; conservative old responses stay unknown.
No new server protocol, database migration or runtime operation is proposed.
New browser dispatch state must preserve old pending records and reload safety;
do not silently drop an unfamiliar state. A later package rollout must ship
matching pinned assets/backend. Prefer a compatible forward recovery while
pending browser intent exists; an older browser cannot be assumed to understand
new order states. Publication, deployment and integration remain separate lead
actions/approval boundaries.

### Follow-up: retain linked replacement proof

Bounded disposition of implementer1's concrete edge report. The owned worktree
was inspected while edits were in progress over `852c37d159f3289b8b2ea45c849d44847e72dc11`;
this is not review of a committed final tree. The ACK retirement loop around
`static/app.js:4350` can remove an observed replacement while its unknown
original still saves `replacementId`. Failed-copy edit/discard around `:5948`
can remove the same referenced target. Both leave reload without the proof it
needs. The receipt codec around `:1000` also needs to preserve `failed`.

Accept the proposed repair inside the existing receipt/order stores:

- Retain a target's observed/accepted proof while any saved receipt references
  it through `replacementId`. Filter these targets before ordinary ACK cleanup,
  and recheck current durable references before deleting after asynchronous ACK.
  Unavailable storage means retain. An intentionally retained proof is not a
  failed cleanup and must not produce an ACK retry loop or starve other eligible
  receipts. An original may retire only on its own positive evidence and when
  it is not itself a referenced target; replacement success never proves the
  original delivered.
- When explicit failed-copy edit/discard retires a referenced target, save and
  verify `state: failed, dismissed: true` in its existing receipt instead of
  deleting it. Keep its original immutable text/attachments and incoming link.
  Preserve `failed` through the codec. Do not redirect the original link to an
  edited message or create a new chain of recovery metadata.
- Reload must not re-enqueue a target only when all three hold: it is persisted
  failed, dismissed, and absent from order. A failed target still in order keeps
  normal failed-head recovery, including interruption between receipt and order
  writes. A missing target is ambiguous, not evidence of deliberate retirement.
  Exclude deliberately retired proof from ordinary content matching/capture.
  Existing unknown/unsent recovery and positive confirmation retain precedence.
- Preserve proof on failed/readback-uncertain writes. No new registry, protocol,
  schema, eager collection mechanism or general transaction framework is needed.

Focused tests: observed replacement plus unknown original through ACK/reload;
original positive evidence followed by ordinary eligible retirement; a link
appearing while ACK is pending; referenced failed-copy edit and discard through
reload; failed/dismissed codec round-trip; interruption with failed target still
in order; no content-matching resurrection; storage-read/write failure retains
proof and never duplicates dispatch. No native test extension is needed for
these browser-storage edges. This clarification was sent to implementer1 and
the lead before finalizing implementation.

### Review disposition: one explicit copy per retained lineage

The lead relayed a preliminary Important finding at committed head `543d7ac7`:
after unknown A creates copy B, copying unknown B creates B→C while A still
references B. The dispatcher then fences C, and reload can append B in the
wrong position. This finding is recorded as reported; no new source investigation
or tests were performed for this disposition. The full review report is pending.

Accepted bounded scope reduction: a receipt targeted by any saved
`replacementId` cannot create another copy. For retained A→B, offer no
**Send another copy…** action on B, and enforce the same inbound-reference guard
at the mutation boundary before allocating a new ID or writing receipts/order.
Use current durable receipts; inability to read them cannot prove eligibility.
Recheck eligibility after any asynchronous reconciliation before creating a copy.
An already saved A→B may still recover B using its existing identity; it must
not allocate C. This narrows the earlier generic copy behavior for replacement
targets, without adding transitive lineage tracking.

Keep A, its link, B, the waiting order and the current draft/attachments intact.
B retains exact-ID retry and positive observation; accepted evidence can release
its existing ordering hold. Typed unsent retry and the separately proven R3
failed edit/discard contract remain unchanged. Existing unpublished nested or
otherwise malformed saved links may conservatively stop recovery. Do not delete
identities, flatten links, infer acceptance or invent a migration to repair them.

Verification boundary: regress A→B with B unknown; B has no copy control and a
direct/stale invocation cannot allocate C, dispatch it or change order/storage.
Cover reload and a saved inbound link appearing during reconciliation. Exact-ID
B retry/observation still works; A remains unknown and its link is retained.
Keep existing first-copy confirmation, one-copy recovery, failed-target retention,
storage-failure and newer-draft tests. Nested fixture state must preserve all
identities without automatic replay. Use the lead's direct step-9 quick checks,
then the owning commit fold and affected independent review disposition. Long
verification stays held until that gate; no native/protocol test expansion is
required for this browser guard.

### Post-review verification appendix: exact pinned environment

Commands below are prepared, not executed by the architect. Run only against
the final committed, independently reviewed refresh head, using a fresh watcher
under the monitoring skill. The lead retains the exact head/pin and logs. The
reported 37-case host proof is separate evidence; do not rerun it solely because
these commands are now documented.

Read-only Nix metadata confirmed the current lock uses nixpkgs
`a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`, Go 1.26.6, Node 24.19.0,
Playwright 1.59.1 and packaged Codex 0.163.0. New codex-web input is
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`. The locked browser selector below
evaluates to `/nix/store/41w7imjg431zlz3ymw6kw7sv5d9y8mpj-playwright-browsers`;
the native package evaluates to
`/nix/store/3lrchzhnd3iiknvkim8ivq77h6i1gdlv-codex-package-0.163.0`.
Evaluation establishes selection, not successful realization or test results.

Use one locked shell expression for all steps (no global npm/browser download):

```bash
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace
verification_shell='
let
  f = builtins.getFlake "/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace";
  p = import f.inputs.nixpkgs { system = "x86_64-linux"; };
  browsers = p.playwright-driver.selectBrowsers {
    withChromium = true;
    withFirefox = true;
    withWebkit = false;
    withChromiumHeadlessShell = false;
  };
  native = f.lib.mkCodexPackage {
    pkgs = p;
    codex = f.inputs.llm-agents.packages.x86_64-linux.codex;
  };
in p.mkShell {
  inputsFrom = [ f.devShells.x86_64-linux.default ];
  packages = [ p.go p.nodejs p.git p.jq p.playwright-test ];
  GOFLAGS = "-mod=readonly";
  NODE_PATH = "${p.playwright-test}/lib/node_modules";
  PLAYWRIGHT_BROWSERS_PATH = "${browsers}";
  PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD = "1";
  CODEX_WEB_TEST_BINARY = "${native}/bin/codex";
}'
```

First, flake evaluation and the exact CI fast selection from
`.github/workflows/check.yml` (includes package; excludes the four separate VM
checks). The watcher should keep each stage's separate log/exit evidence:

```bash
nix flake check --no-build --print-build-logs
nix develop --impure --expr "$verification_shell" --command bash -euo pipefail <<'CHECKS'
check_names=$(nix eval --json .#checks.x86_64-linux --apply builtins.attrNames)
mapfile -t checks < <(
  jq -r '.[] | select(. != "host-module-idempotency" and . != "session-recovery-boot" and . != "session-archive-lifecycle" and . != "session-creation") | ".#checks.x86_64-linux." + .' <<< "$check_names"
)
nix build --no-link --print-build-logs "${checks[@]}"
CHECKS
```

Historical raw-source browser command (retained below): delivery, paging and
composer passed in the lead's reported batch, but this input is incomplete for
the full `portal_improvements` scenario. Its later editor assertion requires
generated assets absent from the raw Go embed. Preserve upstream Firefox
coverage in `message_delivery_browser_test.cjs` and all original assertions in
`portal_improvements`, including the editor. Future full editor browser runs
must use the prepared or packaged input described immediately after this block.
The provider configuration path is an absent file beneath a real disposable
directory, avoiding inherited live provider configuration:

```bash
nix develop --impure --expr "$verification_shell" --command bash -euo pipefail <<'BROWSER'
browser_fixture=$(mktemp -d /tmp/workspace-session-ui-browser.XXXXXX)
trap 'rmdir "$browser_fixture"' EXIT
export DEV_WORKSPACES_CODEX_PROVIDERS="$browser_fixture/absent-providers.json"
export PORTAL_BROWSER_TEST=1
go -C portal test -mod=readonly ./internal/web \
  -run '^TestQuestionBrowser$/(composer_handoff_browser_test[.]cjs|paging_browser_live_test[.]cjs|message_delivery_browser_test[.]cjs|portal_improvements_browser_test[.]cjs)$' \
  -count=1 -timeout=15m -v
BROWSER
```

Correction from execution evidence: preserve
[`refresh-portal-browser.log`](refresh-portal-browser.log) and its exit record.
The raw run failed at `#files-content .cm-editor` after switching to raw mode;
the reported cause is missing generated editor assets, not a waived assertion.
`portal/internal/web/static/source-file.js:49` dynamically imports
`/static/review-editor.js`; `server.go:49` embeds `static/*` at Go compile time
and serves that embedded tree at `:695`. Copying assets after compilation cannot
repair that input.

The repository owns asset preparation in `nix/workspace-portal.nix:36` and
`:286–288`: `reviewAssets` imports `nix/review-ui.nix`, then `preBuild` runs
`cp ${reviewAssets}/review-* internal/web/static/` from the portal source root
before Go compilation. `nix/review-ui.nix` builds the locked
`portal/review-ui/` sources/package-lock and installs the generated editor,
highlight worker, license and dependency manifest. Full editor verification
must follow this existing package path, or use an owned exact-source snapshot
with those matching immutable outputs copied before `go test`. Do not substitute
a synthetic editor, omit assertions or install a separate browser/editor build.

Implementer1 prepared one such input, recorded in
[`portal-editor-prepared-input.json`](implementer1-refresh-evidence/portal-editor-prepared-input.json):
head `01218bf9458aefc8971ac4d31d8da415392d0a25`, tree
`af3991b2e88d0b5c024982c118b4367e835a43e3`, exact source snapshot plus the held
`portal_improvements_browser_test.cjs` fixture and four generated assets from
`/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0`.
The receipt binds source/blob modes, fixture/assets hashes, asset derivation and
input graph, copy recipe, lockfile and codex-web pin; it records no product
source change. This is a prepared-input fixture run, not an unqualified test of
the committed tree alone.

Its exact guarded command is
[`portal-editor-prepared-run.sh`](implementer1-refresh-evidence/portal-editor-prepared-run.sh),
which runs the focused `TestQuestionBrowser/portal_improvements_browser_test.cjs`
from the prepared snapshot using the locked shell above. At this amendment the
lead reports a fresh Luna CLI watcher running it; no completion receipt has
been received here and no pass is claimed. The script's snapshot and hashes are
specific to this run. Future full editor runs must prepare/bind the appropriate
owned input or use the existing packaged route; do not reuse stale provenance.
Retain both the original raw failure and the eventual prepared-run receipt.
This corrects the verification brief only and does not expand product scope.

Run the existing new-pin admission/HTTP contracts directly from the consuming
portal module. These are controlled WebSocket/fake-client tests, not live native
delivery; they cover writer admission, same-ID restart retry, explicit refusal,
shared-ledger races, admitted browser cancellation/shutdown and typed errors:

```bash
nix develop --impure --expr "$verification_shell" --command \
  go -C portal test -mod=readonly github.com/aither64/codex-web/codex \
  -run '^Test(RequestPreservesConcurrentCancellationAndTransportFailure|CanceledSendBeforeWriteSurvivesRestart|ExplicitProtocolRefusalLeavesSendRetryable|SharedLedgerAdmitsOnlyOnePreparedSender|SharedHistoryRecoveryRecordsAcceptanceAtomically)$' \
  -count=1 -timeout=5m -v
nix develop --impure --expr "$verification_shell" --command \
  go -C portal test -mod=readonly github.com/aither64/codex-web/conversation \
  -run '^Test(AdmittedSendIgnoresBrowserCancellationButHonorsShutdown|SendDeliveryErrorsExposeStateWithoutPrivateDetails)$' \
  -count=1 -timeout=5m -v
```

Proportionate existing native coverage, using the exact packaged binary above:

```bash
nix develop --impure --expr "$verification_shell" --command \
  go -C portal test -mod=readonly github.com/aither64/codex-web/codex \
  -run '^TestPinnedCodexRecoveryRemainsColdUntilActivation$' \
  -count=1 -timeout=5m -v
```

The native fixture owns a private home/socket and loopback synthetic provider;
it starts/stops its own App Server and does not address this session. It verifies
cold recovery/activation and native queued FIFO. It does not prove consumption
order of multiple steers or cross-client execution ordering. The browser tests
use real portal assets/templates/uploads with controlled API responses; they do
not prove real model processing. Verify selected tests ran rather than skipped.
No new protocol or live-runtime experiment is required for this refresh. Keep
unrelated host/deployment VM suites outside this batch; existing pre-deployment
gates still apply later. Stop/report an unexpected local kernel build; retain
failure logs for diagnosis rather than blindly retrying.

## Implementation packages and dependencies

No assignments are made by this proposal. If accepted, the lead can split work:

| Package | File boundary and acceptance |
| --- | --- |
| Settings switches | `dev-workspace/portal/internal/web/templates/{session,notifications}.html`, `static/style.css`, relevant settings presentation/browser tests. Existing switch appearance, semantics, accessible interaction and save/error behavior preserved. |
| Visible unread | `static/app.js` transcript helpers/render/view sections, `paging_browser_test.cjs`, `presentation_browser_test.cjs`, `browser_contract_test.cjs`. Visible changes set per-view unread; hidden changes do not; scroll/filter/streaming cases pass. |
| Composer dispatch | `static/app.js` submission, receipt and action-state sections; delivery browser tests and relevant HTTP/native tests. Repeated submissions accepted without draft loss; existing send/queue/retry semantics preserved. |
| Quiet queue checks | `static/app.js` queue-notice renderer, `templates/session.html` queue-status copy, dedicated queue presentation tests and a short portal-guide update. Healthy reads stay silent; existing warning timing, queue rows and real delivery states remain intact. |

Unread, composer and queue-check packages overlap `app.js`; serialize their edits/integration or
have one implementer own that file. Settings can proceed independently with
agreed CSS/markup boundaries. Add concise behavior notes to the owning portal
guide once implemented. A shared `codex-web` helper or protocol modification is
not required by the proposal; any need discovered during implementation goes
back through the lead before expanding repository scope.

## Compatibility, deployment and recovery

Switches and unread tracking are browser presentation changes. Preserve HTTP
payloads, session manifests, retry ledgers, native queue format, lifecycle
journals, role policy and authorization. No database migration, generated client,
CLI, Terraform or NixOS/vpsAdminOS configuration change is proposed.

The browser dispatch metadata is the one new persistence concern: version it
separately or extend only a proven compatible record, preserving existing
attempt IDs and recovery meanings. Test old browser/new server and reload with
pending submissions. No coordinated fleet update is expected. A later rollout
would use the normal user-profile workspace application package and matching
assets, not system pin deployment. Package selection is forward-only here;
recover with a compatible forward fix while retaining all pending receipts.
Do not discard an uncertain submission or local pending buffer during recovery.
No deployment is prepared or authorized in this investigation.

## Acceptance and verification plan

No checks were run: this turn is a proposal based on source inspection. For later
implementation, use the repository Nix environment and these focused cases:

- All persistent boolean settings in the Session Settings view use the same
  switch. Tab/Space, label click, screen-reader name/state, disabled/loading,
  save failure, stale identity/revision and refresh preserve existing behavior.
- Messages-only plus hidden tool/team changes: no badge. Existing visible unread
  plus another hidden change: badge stays. Visible streaming text: badge appears
  when paused, never pulls the reader away. Timestamp/receipt-only and closed
  details changes do not signal new content; visible summary changes do.
- Switching filters preserves each paused view; following/clicking the button
  clears after reaching the tail. Initial/older/repair pages, reconnect, section
  hiding and lead/member replacement do not manufacture or erase unread output.
- Delay the first POST; submit two more distinct messages and Queue next. Every
  draft detaches once, buttons accept new intent, dispatch is ordered, and each
  action uses its original endpoint/ID/attachments. Late success/failure cannot
  modify a newer draft. Test repeated identical intentional text separately from
  double-click and retry deduplication.
- Lose the first reply, reload while entries wait, exhaust browser storage and
  reject an upload. Preserve records and stop uncertain dispatch. Reconciliation
  neither duplicates nor reorders; explicit recovery uses the original IDs.
- Verify sequential steers before model consumption, active-to-idle transition,
  existing native queue FIFO, two browser tabs and automatic retry arbitration
  against the selected native package. Do not infer these from mocked success.

Quick checks after implementation: Node syntax and focused existing browser
contracts; relevant Go web/handler/receipt tests using `-mod=readonly` as required
by dev-workspace. Longer checks after normal independent final review: packaged
flake checks and disposable native/browser delivery tests with delayed and lost
replies. Delegate long or uncertain verification through the monitoring skill.
Implementation of all four fixes is approved; the lead owns assignments and
verification. This architect amendment runs no implementation or review.

## Authorized aitherdev rollout brief — 2026-10-25

Status: preparation design ready for the two assigned input owners. The user
explicitly authorized deploying aitherdev using vpsfree-cz-configuration. This
does not authorize default-branch integration, reboot, session lifecycle actions,
provider switching or unrelated dependency changes. Architect activity remains
read-only investigation and this design amendment; no claim, build or deployment
was performed. Identity/environment were reverified. Applicable workspace and
repository guidance, selected `workspace-host coordination guide`, and the
configuration's aitherdev provider/DeepSeek/update guides were read. Native
Codex is not being upgraded; reuse completed product evidence.

### Scope, deployed baseline and preparation owners

Deploy reviewed/published dev-workspace
`9293e314e6028d71a57595073117b51bdc53c8ff`, based on
`10bb047513c82d1310e8fcaa797e8772f948dd8a`, with codex-web
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`. The lead records final independent
review, local checks and exact-head CI run `40143026250` as passed. The final
base-to-head paths are portal code/assets/templates/tests and the portal guide;
there is no native runtime, host-module, ledger or protocol change in that range.

Read-only baseline evidence, to refresh immediately before activation:

| Item | Observed identity |
| --- | --- |
| Live system and `/nix/var/nix/profiles/system` | `/nix/store/n6b9dmmaw83zx80paglrisy0w5rwnfw8-nixos-system-aitherdev-26.05.20261021.da6dc0e` (both agree) |
| `/etc/confctl/configuration-info.json` | clean `d12a77374b18e15fe7600f95307114e2e1882828`, matching inspected cached configuration origin/master |
| Effective installed host runtime | `/etc/confctl/inputs-info.json`: devWorkspace `10bb047513c82d1310e8fcaa797e8772f948dd8a` |
| Selected workspace profile | `~/.local/state/dev-workspaces/profile` → `profile-187-link` → `/nix/store/8ph05i3nps8xi1jfs450b16aysc16nvg-dev-workspace-0.2.0` |
| Selected package derivation/source | `/nix/store/idaz4jqnjy572qi03shxa26bkjlrgpq9-dev-workspace-0.2.0.drv`; runtime source `/nix/store/r2pxv5h275gk9njy59rbk4ydsjy38hx4-source`, NAR `sha256-fl8Ib9hLHxlGCjJYiAhIZgURmkclzOaBZ0veJDUCq+k=` matching locked `10bb0475` |
| Deployed workspace composition source | `/nix/store/3g4dbw0nzyvc01gfbr08x35slccqnf0v-source`; nested runtime `10bb0475`, extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` |
| Active workspace native package | `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0`; running daemon executable resolves into this package |
| System native package | `/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0`; same version alone is not closure equivalence |
| Existing running services | user `workspace-portal@vpsfree-cz`, `workspace-router`, `workspace-codex@vpsfree-cz` active/running at inspection |

The physical claim identity is `vpsfree:aitherdev`, catalog name `aitherdev`,
aliases `aitherdev.int.vpsfree.cz` and `cz.vpsfree/machines/aitherdev`.
Confctl selector is `cz.vpsfree/machines/aitherdev`, target `172.16.106.40`.
Installed catalog digest is
`sha256:dbc6bc2761e3151ae404401d54bf0dc1350dfb1e8629f13618755b433d3a3a03`;
`profileMachine` is the same physical identity. No repository claim is needed
for preparation. The lead owns the eventual machine claim and activation.

Independent packages assigned by the lead:

| Owner | Repository and permitted input boundary | Dependency/result |
| --- | --- | --- |
| implementer1 | Session-owned `vpsfree-cz-configuration` feature worktree. Existing `flake.nix` maps channel `dev-workspace`, role `devWorkspace` to root input `devWorkspace`. Use `nix develop` then `confctl inputs channel set --commit dev-workspace devWorkspace 9293e314e6028d71a57595073117b51bdc53c8ff`. Preserve generated commit message and only intended generated lock changes. | Clean committed/published configuration pin and effective aitherdev input inventory; no machine/service source edit expected. |
| implementer0 | Session-owned `workspace` feature worktree, not shared master. Change only `flake.nix` direct `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to the exact published feature; generate `flake.lock` with `nix flake update vpsfree-dev-workspace/dev-workspace`. | Clean committed/published composed application input; run final cross-repository checker after configuration pin is ready. |

Preserve extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` and its content
hash, all follows relationships/siblings, and llm-agents
`e85b99217baf13a38fc887b31338b1833f1159c0` in both effective native selections.
Do not add a top-level runtime input, update the extension's lock, install the
application in systemPackages, or update nixpkgs/Home Manager/providers. The
host imports `devWorkspace.nixosModules.host` and uses `lib.mkCodexPackage`;
the portal application remains the composed workspace user profile.

One preflight discrepancy must be recorded, not silently repaired: the deployed
`inputs-info.json` reports Home Manager `c47b2cc64a629f8e075de52e4742de688f930dc6`,
whereas the inspected configuration root lock maps `home-manager` to node
`home-manager_2` at `e28654b71096e08c019d4861ca26acb646f583d8` (other nodes contain
the former). Compare the actual confctl evaluation/build input graph and plan
to the deployed receipt; preserve the existing selection and escalate any real
unrelated effective change. This brief does not diagnose or expand scope to fix
that metadata discrepancy.

### Compatibility and verification gate

No data/schema/API migration is required by the four fixes. Keep pending send
receipts, original/copy links, order metadata, uploads, native submission ledger
schema 3, session/cluster/lifecycle journals and launch markers. Old browser tabs
may retain old controls until reload; server admission semantics already match
the deployed codex-web pin. New browser recovery records must not be cleared to
force rollout or rollback. Workspace recovery remains forward-only.

Both input owners inspect semantic lock diffs, use declared hooks and run quick
input/format checks. Workspace owner runs its existing deployment-contract tests
and, once both locks are final:

```sh
bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/vpsfree-cz-configuration
```

This verifies both runtime identities and canonical portal/site aliases.
Product review and CI apply unchanged to exact `9293e314`; do not repeat its
green suite without new evidence. Apply the mandatory-review skill's mechanical
pin exception only if both final diffs are exclusively that reviewed selection
and generated locks, with unchanged effective siblings/behavior. Any functional
configuration/composition change or unrelated effective dependency change needs
its own quick checks and affected independent review before long builds.
Retain full branch/history and no-migration conclusions for new input commits.

The lead delegates builds/long checks to a fresh watcher after the applicable
review gate. Build the exact committed aitherdev configuration and composed
workspace package, outside machine ownership, preserving source/lock identities:

```sh
# In the configuration worktree's Nix shell:
confctl build cz.vpsfree/machines/aitherdev
# Record the resulting exact generation as GENERATION; copy that generation only:
confctl deploy --generation GENERATION --copy-only cz.vpsfree/machines/aitherdev
# In the workspace feature worktree:
nix build --no-link --print-out-paths .#packages.x86_64-linux.default
```

Copy-only is preparation; dry activation and selection wait for the machine
claim. Preserve configured auto-rollback and normal health checks. Stop/report
unexpected local kernel builds. No broad input update or repeat product/VM test
campaign is implied. Run the workspace composition checks needed to establish
extension/catalog/host agreement, and inspect both candidates' runtime/claim/
cluster contracts against the selected package before activation.

Bind exact system toplevel and generation, profile output/deriver, full
recursive derivation and flake input graphs, clean source commits/trees,
runtime/extension/codex-web/native identities and old/new comparisons in the
existing rollout/review evidence. Do not infer composed native identity from
the standalone product build: its package set can differ. Prove candidate
native executable and launch policy/arguments/capacity equal the running
workspace marker before treating this as a live portal-only switch. Built-in
`workspace-host switch` repeats these preflights under its locks. A refusal or
unexpected native change returns to the lead; do not force a restart, provider
change or system-Codex override.

### Activation, acceptance and recovery

After artifacts/copies/review are ready, the lead acquires only the aitherdev
machine claim and verifies authoritative held status. Recheck actual system,
profile, current source and unfinished effects against preparation. With the
same exact built generation, run ordinary confctl dry activation, inspect its
service/restart effects, then no-reboot switch:

```sh
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev dry-activate
confctl deploy --generation GENERATION cz.vpsfree/machines/aitherdev switch
```

Require no unexpected native-daemon/guest interruption. Keep confctl
auto-rollback enabled as configured; do not use `--disable-auto-rollback` or
`--reboot`. Verify live `/run/current-system`, system profile and config/input
metadata all identify the intended system before the dependent application
switch. A successful live switch with failed profile publication is incomplete.

Then use the ordinary stable command with the held machine ID and exact binding:

```sh
DEV_SESSION_SLUG=2026-10-24-workspace-session-ui \
DEV_SESSION_WORKSPACE=/home/aither/workspace/ai/vpsfree.cz \
DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID \
workspace-host switch --source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/workspace
```

The matching-native live path restarts portal/router and preserves Codex, tmux,
managed terminals, active threads and saved member settings. Do not invoke private
activation/recovery helpers around a refusal. The user-profile command owns
generation/registry/cluster/authority checks, pending transition evidence and
forward recovery; the lead owns safe execution/monitoring across reconnection.

Acceptance: verify exact new profile/system paths and input graph, active
portal/router/native services, authenticated canonical portal and alias routing,
health/readiness, naming availability and existing lead/member conversation
continuity. Preserve the same native PID/executable and launch provenance when
the live-switch path applies. Use existing read-only or disposable naming probes;
do not create/archive a real session merely to test deployment. Providers were
not changed, so do not switch the workspace provider or repeat the separate
DeepSeek upgrade exercise absent a concrete changed provider/native contract.

Confirm served final assets and the four behaviors using safe UI observation or
the already reviewed disposable browser fixture: consistent switches and save
semantics; hidden-only updates do not set/clear visible unread; repeated drafts
enter ordered waiting with exact-ID/explicit-copy recovery; healthy queue checks
stay silent and retain confirmed rows. Real submission/setting mutations in
other sessions are outside this smoke check. Do not claim all UI acceptance from
an HTTP 200 alone; report any item supported only by exact-source test evidence.

On failed system activation, retain the claim, inspect auto-rollback plus both
live/profile results and reconcile the original command before any retry.
On failed profile selection, inspect the selected forward package/pending
transition and retry the ordinary supported switch as appropriate; never select
an older workspace profile or delete pending receipts/journals. Preserve system
generations and native roots. A host-only recovery must not invalidate already
selected application contracts. Escalate uncertain effects before continuing.

Machine retention is required until verified deployment/effects and complete
deployed feature lineage are integrated into approved remote defaults. That
includes dev-workspace and the new workspace/configuration feature commits and
any genuinely unmerged deployed dependencies. Merge approval is currently absent;
deployment does not supply it. Record canonical repositories/targets, exact
deployed/final heads and fresh remote ancestry before eventual release. A later
equivalent successor needs independent lineage proof; a substantive successor
needs a new verified deployment. Once all conditions hold, the lead checks the
exact owned claim, releases and verifies release promptly; no separate UI
approval is required. Release never authorizes session cleanup or lifecycle work.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-workspace-session-ui/>

## Resumed rollout: preserve the newer deployed baseline (2026-10-25)

Status: **refresh design ready**. This section supersedes the earlier rollout's
baseline and candidate selection, not its guarded activation procedure. The user
resumed deployment and explicitly required preservation of already merged
performance/reliability work. The four portal fixes remain the feature scope.
No source/configuration changes, builds, claims or activation were performed by
this assessment. The foreign aitherdev reservation remains untouched; source
preparation can proceed independently, and the lead owns later reservation and
activation. Deployment still grants no default-branch integration approval.

### Authoritative observations and retained history

Session/environment identity was reverified against the exact bound workspace.
Read-only host metadata, selected immutable sources and canonical Git objects show:

| Authority | Observed identity |
| --- | --- |
| Selected application profile | profile 189; `/nix/store/48011krllhj3428878a8h55sb6x4wky0-dev-workspace-0.2.0` |
| Selected application runtime | `9634151b9836311c331a58880fbb4c46133fd98f`; source `/nix/store/d1cnw1bqr3byn3bx4c01grdvm22xa6kw-source` |
| Selected composition | `/nix/store/d2b3y1raszch3ach8r3l4gw9wdds9bjf-source`; runtime NAR `sha256-tJ3kHzGpdNKat4bC7Th/Q6O3gUSTjrmVQU2A9gxVjsw=` |
| Selected codex-web | `8b60554bc10c2a6bcbf9732a8b77ad959c317036`; NAR `sha256-bkEZSKkVAYbthaiyI4onS5eYQXuDj3YV8nbQlzDBeHE=` |
| Live system and system profile | `/nix/store/1bnl145ln79094l10j60cp4631a69vww-nixos-system-aitherdev-26.05.20261021.da6dc0e` |
| `/etc/confctl/configuration-info.json` | clean `2d33a9ca715d305d7b4003e17bbf3e31f1be1d60` |
| Host `devWorkspace` input | `ec53874b6eea73bf65099cf19aa1a4bc5a3336aa` (different from selected application) |
| Deployed native input | `e85b99217baf13a38fc887b31338b1833f1159c0` in host and selected runtime |
| Selected extension | `767dfd587e346168e1443e65ccdb67ce748f3fe3` |
| Active workspace native | `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex` |
| System native | `/nix/store/wz4w670930cksh1ivz13y0gn3c23cjzl-codex-package-0.163.0/bin/codex` |
| Selected coordination catalog | `b79fc86c55e1257ce8959c519eba63e472b0746d10312027e1d4f16d793daa3e` |

SSH `ls-remote` observed runtime master `ec53874b`, configuration master
`aca63e8ac5dea1f6c7ebef91cce0bda97d5420eb`, workspace master
`e91442436091a5e8f8c843fcd673b76fe52ea0e8`, and codex-web master
`872c7ad3962f9fa9b17358244e27f3e3fac59fc5`. These are observations, not frozen
future targets. Runtime `9634151` and codex-web `8b60554` are published at each
canonical repository's `refs/heads/2026-10-25-message-delivery-reliability`.
Their canonical objects/remote refs and installed sources were inspected; no
foreign session records, roster or worktree were accessed. Preserve these exact
dependencies through our published descendant and lock; do not rewrite their
branches. The deployed configuration `2d33a9ca` is not an ancestor of observed
configuration master; do not describe it as literally merged.

Retain the original reviewed `10bb0475..9293e314` range, review and CI40143026250.
Also retain held configuration `eac2877` on `d12a7737`, workspace `cbaa7d94` on
directed base `df1944a2`, their successful build/copy receipts, system
`/nix/store/mljm5jh4mszcxw35scp4fyskymgdy0kv-nixos-system-aitherdev-26.05.20261021.da6dc0e`
and generation `2026-10-25--08-46-20`. The old application candidate
`/nix/store/nz0cj6j634gy3y9hddznz8a0zmgpmhvj-dev-workspace-0.2.0` is now absent;
cause is unproven. None was activated by this session. They are historical
evidence, not candidates to replay against the new baseline.

### Runtime owner: preserve merged and deployed behavior before porting the fixes

Implementer1's runtime package comes first. Fetch in the owned repository under
the normal Git procedure and select the fresh remote master, not the recorded
master merely because it was inspected here. If fresh master contains exact
`9634151`, use that newer master. If `9634151` still descends from master, use
the published `9634151` as the preservation base. If histories diverge, preserve
both current master and the deployed delta through an explicit owned refresh;
report the precise reconciliation to the lead before discarding/replacing any
deployed identity. Do not reset away later merged performance, retention or
reliability changes. Review must prove fresh-master ancestry and preservation of
the deployed delta; where rewritten deployed history is unavoidable, retain
old/new ranges and obtain an explicit independent lineage conclusion.

Port only our reviewed four-fix delta to that preservation base. This is a
**substantive composer integration**, not a certified equivalent rebase:
`ec53874b..9634151` changes `portal/internal/web/static/app.js`, receipt codec,
transient retry scheduling and plan implementation. Keep newer template/asset
versions, `docs/workspace-portal.md`, and existing source/retention changes.
Do not restore old lockfiles, `portal/go.mod`/`go.sum`, provider shutdown wiring,
`plan_delivery.go` lifetime handling, accepted-fork source waiting or archive
behavior from our original base. No codex-web source edits or protocol expansion.

Required interfaces and invariants:

- Keep deployed codex-web `8b60554` support (or a later merged compatible
  successor established by the owner), including HTTP `notSent` and `retryable`.
  Typed authoritative nonadmission remains same-ID retryable even after reload;
  the fresh-only attachment validation fallback remains failed/new-ID recovery.
- Preserve deployed transient retry scheduler/backoff, offline/hidden/busy
  gating, saved retryability and plan-context retry. Adapt its ordinary-message
  retry callback to the existing ordered dispatch owner, so an automatic retry
  cannot bypass waiting order, UNKNOWN holds or another in-flight dispatch.
  Use the existing scheduler and dispatcher; do not introduce a second queue or
  registry. Plan implementation retains its context and existing mutual
  exclusion; do not make it an ordinary reworded message.
  Bounded owner clarification: this routing requirement applies to automatic
  ordinary-message retries. Re-read the current receipt at dispatch time and
  require `unsent` plus `retryable`; a buffered ID may retry only at the FIFO
  head. An ordinary legacy receipt outside the buffer may be adopted with the
  existing `retry: true` path only while the dispatcher is empty and idle.
  Persist its existing ID, text, attachments and Send/Steer intent before any
  send, without changing the draft. Recheck admission through the dispatcher's
  ordinary gates; storage refusal or concurrent capture sends nothing. Do not
  append automatic legacy retries behind existing waiting intent or overwrite a
  newer receipt state. Preserve the existing manual legacy exact-ID
  reconciliation/copy path and its presentation; legacy receipts do not acquire
  a new global hold. Plan-context retries remain on their existing plan path.
  Quick regressions must cover legacy retry deferral with a nonempty buffer,
  empty-buffer same-ID adoption, stale accepted/UNKNOWN scheduler callbacks,
  unchanged drafts, and unchanged manual legacy recovery behavior.
- Preserve immutable ID/text/attachments, repeated Send/Steer capture, current
  drafts, exact-ID retries, one explicit confirmed copy per lineage, linked
  proof retention and failed-attachment removal/reselection. UNKNOWN cannot
  auto-retry or silently release waiting messages. Explicit copy remains the
  deliberate recovery escape. No cross-client/native execution-order promise.
- Preserve stale-feedback generation/readiness gates while allowing capture
  of new drafts; retain accessible switch/save behavior, visible-content unread
  tracking (including hidden deltas), and silent healthy queue refresh.
- Preserve the deployed transactional SQLite submissions and migration fences:
  `submissionStoreSchema=1`, `submissionStorePolicy=1`, archive recovery policy3,
  provider/retry contracts, shared client wiring and forward-only recovery.
  Runtime `docs/workspace-portal.md`, `workspace-host`'s
  `require_compatible_submission_store!`, and codex-web
  `docs/submission-storage.md` own this boundary. Do not replace a database or
  WAL with JSON backups, downgrade to872/9293, or inspect/edit private journals.
  Database existence was not inventoried here; the candidate must support the
  deployed capability regardless, and normal transition checks inspect state.

### Consumer owners: one published runtime, explicitly retained native input

After the runtime owner publishes the new exact feature head, implementer1
refreshes configuration onto fresh master (observed `aca63e8a`). Preserve all
unrelated merged source. That baseline advances root llm-agents to
`ea188d2f072e0ec8d5b71245e228803672801a22`. **The lead selected preservation of
root ea188 for configuration preparation and withdrew the root e85 re-pin.**
The feature runtime retains its independent e85 input. This input selection
does not clear the shared-state activation gate below. The runtime channel
operation remains:

```sh
confctl inputs channel set --commit dev-workspace devWorkspace NEW_PUBLISHED_RUNTIME_SHA
```

`flake.nix` maps these channel/role pairs to inputs `llm-agents` and
`devWorkspace`. Inspect the complete generated recursive graph against the
deployed graph, including each distinct native subtree and follows, rather than
manually editing the lock or updating all inputs. This targeted deployment pin
must be explained in input review; it is not permission to undo merged source
or unrelated dependency updates. Prove the built **workspace** native executable
remains the deployed one; identical version strings are insufficient. Any
unavoidable workspace-native/startup change returns to the lead before activation.

Implementer0 refreshes the workspace consumer onto fresh master (observed
`e9144243`), preserving compact source filtering/storage behavior. Select the
same new runtime through the existing nested
`vpsfree-dev-workspace/dev-workspace` URL and targeted lock update. Preserve
extension767dfd58, siblings/follows and deployed native subtree. No old9293 pin,
top-level runtime input or extension lock rewrite. Then run the existing
`bin/check-dev-workspace-deployment` against both final owned worktrees. Input
owners retain raw locks, semantic graphs, exact new heads and source/output
receipts. Consumer input edits depend on the published runtime, not merely a
local rebase result.

#### Native-input assessment: system tools and managed workspace are separate

The user's preservation instruction also applies to real merged input behavior.
Configuration commit `95f10b507013b5bd245ecd92f45fa0b364f8a70e` advances root
llm-agents e85 to ea188 and its nixpkgs subtree319e4ceb to f20cd90e. Read-only
upstream source comparison confirms this is not metadata-only:

- `packages/codex/hashes.json`: Codex0.163.0 becomes0.164.0 with new source/Cargo
  hashes; `librusty_v8`150.4.0 becomes152.2.0.
- `packages/codex/package.nix` still builds the `openai/codex` release tag and
  installs Codex, code-mode-host and logs_client in the same layout. Its
  daemon-store patch is adapted to newer upstream installation code.
- The recipe adds a conditional pre0.164 certificate-trust backport. Direct
  release `codex-rs/Cargo.lock` reads confirm0.163 has rustls-webpki0.103.15 /
  webpki-roots1.0.5, while0.164 has0.103.16 /1.0.10. The recipe describes
  removal of emSign roots/rejection of revoked eMudhra intermediates. Retaining
  e85 therefore also omits those newer trust changes; no claim of complete
  merged-behavior preservation is valid for that downgrade.

Sources: [exact llm-agents comparison](https://github.com/numtide/llm-agents.nix/compare/e85b99217baf13a38fc887b31338b1833f1159c0...ea188d2f072e0ec8d5b71245e228803672801a22),
the two release-tag Cargo.lock files, and canonical aitherdev
`cluster/cz.vpsfree/machines/aitherdev/config.nix` at aca63e8a. The latter
assembles root llm-agents Codex at14-22, uses it for `codex-ds` at82 and system
packages at224. The selected runtime independently selects its own e85 at
`flake.nix:41`; `libexec/workspace-host:2239` defaults to that package's
`libexec/codex/bin/codex`, with `DEV_WORKSPACES_SYSTEM_CODEX` as explicit override.
The host module does not select the workspace daemon's native package.

**Lead-selected input strategy, conditional for activation:** keep merged root
ea188 for system Codex/codex-ds and preserve e85 in the current feature runtime.
The separate package inputs allow preparation, but do not establish independent
native state or supported mixed-version operation. Exact new output/activation
effects are not yet built or verified. The current runtime package explicitly
checks0.163; do not change that pin/assertion or point its terminal clients at
system0.164 merely to bypass a compatibility refusal.

Input review must record the deliberate system0.164/workspace0.163 split and
verify generated graphs separately. Before activation, verify system package
manifest/helper assembly with proportionate existing checks, candidate workspace
native path and startup marker equality, no system-native override, and dry-run
service effects. A host switch may change standalone tool paths; it must not
restart or repoint the running workspace native service. Any actual daemon
upgrade requirement returns to the lead. No broad upstream changelog audit,
native upgrade implementation, build or live-runtime action was performed here.

#### Shared native state: activation gate remains unresolved

The [workspace update skill](../../skills/update-codex/SKILL.md) requires:
"Also verify the system and packaged
llm-agents Codex versions ... agree." This is not waived by different package
store paths. Selected `workspace-host:3474` defaults its Codex home to
`/home/aither/.codex`; its managed invocation forwards that home through
`DEV_WORKSPACE_CODEX_HOME` (around1490). The actual native process3387667 was
read-only verified as jrsm0.163 with no `CODEX_HOME` override. The system
codex-ds wrapper sets the provider key and profile, not a separate home. Thus
normal system and workspace invocations share native state by default. No
production database, credential or foreign-session records were opened.

Bounded upstream comparison of exact `rust-v0.163.0` and `rust-v0.164.0`
confirms all61 files under `codex-rs/state/migrations`, the state model subtree
and `state/src/paths.rs` are identical. This rules out a change in that SQL
migration set; it is **not complete shared-writer compatibility evidence**.
`state/src/sqlite.rs` changes startup/busy-write retries, persistent journal
initialization and local logs directory/cleanup handling; `migrations.rs` also
changes execution to use busy retries. Native rollout/history, config/auth and
daemon state remain additional boundaries. The inspected guides provide no
supported independent-version contract, and no exact completed0.163/0.164
coexistence test evidence was supplied. No live coexistence claim is made.

Consequently the input-only preparation choice is settled, but mixed-version
activation is not cleared. Absent independent evidence sufficient to establish
the shared-state contract, the supported next scope is a minimal coordinated
upgrade to the already frozen0.164/ea188, through the existing codex-web,
dev-workspace and consumer skill chain. That requires explicit lead disposition,
affected protocol/catalog/naming work only as the exact release demands,
independent final review and exact native/disposable state checks. It also needs
the ordinary idle-session native-switch gate; do not interrupt active sessions
or bypass the foreign machine reservation. No newer release search, provider
feature or native upgrade implementation is authorized by this assessment.

For either a later evidenced coexistence path or coordinated upgrade, retain:

- Full managed DeepSeek profile validation against the exact0.164 config schema
  before system builds, plus assembled manifest/helper/copy/closure checks.
- One real ephemeral DeepSeek request with `--strict-config`, using a private
  isolated Codex home and provider env-key authentication, without copied
  production login credentials. `--help` or an HTTP health check is insufficient.
  After deployment verify the Home Manager wrapper resolves to the intended
  system package and the complete managed profile still loads.
- Separate exact identities for system CLI, codex-ds wrapper, selected workspace
  package and actual daemon; retain original native roots/state and generations.
  Exercise startup and saved-thread resume/fork across the exact binaries in
  disposable state; assess all shared writers and recovery direction. A schema
  match or isolated ephemeral success alone does not establish concurrent use.
- Ordinary host transition checks and service-effect inspection. Never rely on
  system downgrade to read newer native state without demonstrated compatibility;
  workspace recovery stays forward-only and uses the original operation.

### Contract-check owner: selected package versus immutable native launch

Implementer2's diagnosis is retained: historical selected8ph and immutable
launchs4fb genuinely differ in five provider/retry capability fields; the
original `10bb..9293` runtime-contract source is unchanged. This is not path
churn. Do not edit that failed comparison, its evidence or the launch marker to
manufacture equality. The bounded repair has two separate assertions:

1. **Selected application to candidate:** compare complete runtime/state
   contracts against current48011, plus the existing claim/cluster/provider and
   composition checks. For this UI-only delta, require full runtime-contract
   equality. A later merged contract change needs individual compatibility
   disposition; never drop unknown fields or silently default missing fields.
   Missing selected provider/retry or SQLite capabilities must fail.
2. **Actual native launch to candidate startup:** compare exact executable,
   launch policy, actual required native-child capacity and complete argv,
   permitting only the existing validated reporting-policy1 package-path
   equivalence. Require supported live-switch policy in selected, candidate and
   launch packages. The actual launch remains policy/reporting/capacity1/1/0;
   catalog capacity8 is not a replacement. Keep both full raw contracts and
   original launch provenance; selected-owned provider/retry/SQLite fields need
   not retroactively exist in the immutable launcher package.

This split follows selected `libexec/workspace-host`:
`marker_has_semantics?`/`registration_argv_equivalent?` (around1976),
`codex_restart_required?`/`live_package_switch_contract?` (around2226), and
separate session/submission-state compatibility (around2889). It authorizes a
narrow evidence-checker correction, not bypassing ordinary workspace-host
preflight or restarting native to align inventory. Test same-native/older-launch
success, missing selected-state capability failure, genuine native/argv/capacity
change failure and unknown contract-difference refusal. No stale nz0 rerun.

### Review, verification and refreshed preparation

Retain original successful product evidence, but do not transfer it wholesale
to substantive composer integration. Quick checks cover the changed Node
contracts, receipt codec, retry/ordered dispatch interactions, source syntax and
focused Go package/lifetime coverage under the new pinned environment. Include
reload of retryable unsent, automatic retry behind UNKNOWN, draft preservation,
plan-context retry, explicit-copy proof and attachment recovery regressions.
The final affected independent review must assess whole-branch history,
fresh-master ancestry/preserved performance and retention diff, deployed SQLite
compatibility, and complete old/new source/input ranges. The already deployed
SQLite migration is a retained supported boundary, not an unapplied migration
to consolidate away.

After review, the lead selects affected package/native/browser checks from the
existing appendix using the refreshed pin and exact committed source. Reuse
unchanged lane evidence only with its source/environment basis; rerun composer,
delivery and four-fix browser coverage where overlap changes behavior. Editor
browser verification still requires packaged/prepared generated review assets.
Respect repository-required checks, without adding unrelated VM/native-upgrade
campaigns solely because the rollout was resumed. Fresh watcher-owned system
and composed-package builds and exact-generation copy are required; input-only
review covers the deliberate native-role retention and cross-consumer equality.

The fresh composed build must retain a standard explicit owner-local Nix
out-link/GC root throughout preparation and active rollout (for example
`nix build --out-link OWNER_EVIDENCE_DIR/workspace-candidate --print-out-paths
.#packages.x86_64-linux.default`). Record the root and resolved output; do not
reuse `--no-link` as the only retention mechanism. Configuration retains its
normal generation/toplevel. Roots supplement, never replace, exact sources,
recursive inputs, derivations, contracts and native provenance. Retire only
owned disposable roots when no rollout/recovery obligation needs them; no
session lifecycle or cleanup action is implied here.

Before later activation, recapture system/profile/native/contract identities
and recheck fresh remote ancestry. Further drift returns to bounded refresh.
Use the earlier ordinary system-then-user-profile procedure only with new exact
artifacts and the lead's own held machine claim. Recovery is forward to a
compatible963-or-newer runtime; the old held system/profile candidates are not
rollback targets. Preserve naming, health, aliases, current conversations,
native PID/launch provenance, the four UI behaviors and SQLite/retry behavior.
Retention/release must account for all actually deployed feature lineage,
including unmerged runtime/codex-web dependencies, with separate integration
approval. This brief performs no activation and establishes no merge proof.

## Frozen Codex0.164 compatibility amendment (lead selected)

Status: **design ready for dependency-first implementation**. The lead selected
the smallest coordinated0.164 update as necessary compatibility for the approved
deployment. This supersedes the proposed system0.164/workspace0.163 combination
and all earlier unchanged-native/PID acceptance for the final rollout. Do not
activate unsupported mixed-version writers against the shared Codex home.
Preserve the four fixes at runtime
`24e66096ae65a97b1e2d14b68a566f44519a8c2d`, deployed963 behavior and every later
merged performance/reliability change. No latest-release search, provider
feature, new state framework or default-branch integration is included.

Frozen prerequisite identities:

- Version **0.164.0**, llm-agents
  **`ea188d2f072e0ec8d5b71245e228803672801a22`**.
- OpenAI Codex tag `rust-v0.164.0`, annotated tag object
  `fe3b29455488c2e189e43ad5526a107900c5e1b7`, peeled source commit
  **`6aaac694803004a63c6f393d153c96d22521a6b9`** (read-only upstream API proof).
- The frozen llm-agents `packages/codex/hashes.json` specifies source NAR
  `sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=` and Cargo hash
  `sha256-0N2mEGqEl2ZjWqlbraVCWP0eoITgwmT9uO/1w/1eJno=`. Its recipe applies
  `daemon-nix-store.patch`; the new `webpki-bump.patch` is conditional on a
  version older than0.164 and is **not applied** to this selection. Preserve
  exact recipe/patches and transitive locks in evidence. Do not substitute an
  npm binary, unpatched release executable or moving flake reference.

### Prerequisite output and source preparation

Implementer0 owns codex-web compatibility first, from fresh canonical master
(reported8b60554), following its full update skill/reference. A fresh lead-owned
watcher prepares any uncached/uncertain-duration native build; the architect
does not launch it. These are exact prerequisite commands for that watcher,
with a newly owned evidence directory and normal explicit output roots:

```sh
native_evidence=/home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/native-0164-prerequisites
nix build --out-link "$native_evidence/source" --print-out-paths \
  'github:numtide/llm-agents.nix/ea188d2f072e0ec8d5b71245e228803672801a22#packages.x86_64-linux.codex.src'
nix build --out-link "$native_evidence/upstream-codex" --print-out-paths \
  'github:numtide/llm-agents.nix/ea188d2f072e0ec8d5b71245e228803672801a22#packages.x86_64-linux.codex'
```

The owner provisions that private directory; preserve returned store paths,
derivations/input graph and native binary SHA-256. The native file is
`upstream-codex/libexec/codex/bin/codex`, and source root is `source/codex-rs`.
Verify version and resolved paths instead of assuming success from the link.
`.src` is the fetched upstream tree; separately bind applied recipe patches and
show whether they affect the schema/catalog files. Existing mkCodexPackage
assembly remains required for final workspace/system outputs and daemon-copy
checks; the raw upstream output is only an exact dependency prerequisite.

In codex-web's declared Nix environment, using an owned private probe home and
absolute resolved binary/source/schema paths, the quick release checks are:

```sh
CODEX_HOME="$probe_home" "$codex_binary" app-server generate-json-schema \
  --experimental --out "$schema_dir"
python3 test/codex_protocol_contract.py "$schema_dir" codex/client.go
python3 test/codex_ephemeral_config_contract.py "$codex_source/core/config.schema.json"
python3 skills/update-codex-web/scripts/refresh-catalogs.py \
  --source "$codex_source" --version 0.164.0
```

The refresh helper is a source edit owned by implementer0 after this brief.
Use actual0.164 models-manager bytes for the full catalog and the existing
three-field Luna transformation only; update exact hashes/provenance/lengths
and restrictions only where required by the frozen release. Preserve both
supported model/effort pairs, empty tool exposure and fail-closed native utility
checks. Adapt protocol call sites/fixtures only to demonstrated schema/behavior
differences; keep transactional submissions, typed nonadmission, retry policy
and all existing delivery guarantees. Complete focused Go/Node/schema/config
checks and commit/publish the exact dependency before consumer pins. Version
text or generated-schema success alone does not establish native isolation.

### Runtime and consumer boundaries

Implementer1 retains24e66096 unchanged until the published dependency is ready,
then follows `skills/update-dev-workspace-codex/SKILL.md`. Freeze the runtime
llm-agents selection to ea188 using the targeted Nix input workflow; preserve
unrelated inputs. Update exact codex-web flake/lock and Go pseudo-version/sum,
tidy the final module set and refresh `nix/workspace-portal.nix` vendorHash with
fresh dependency derivation proof. No cached fixed-output result substitutes
for validating the final vendor content.

Primary runtime boundaries: `flake.nix`/`flake.lock`, `portal/go.mod`/`go.sum`,
`nix/workspace-portal.nix`, `portal/cmd/workspace-portal/naming_runtime.go` and
its quick/native integration fixtures, installed catalog hashes/byte lengths,
and exact-version package/naming prerequisites. Inspect all relevant consumed
contracts; retain old-version fixtures that intentionally test predecessor
state. Do not globally replace0.163 strings. Preserve mkCodexPackage, provider
selection, SQLite submission schema/fences, accepted-fork/lifetime changes,
ordered retries and every committed four-fix behavior. Any required behavioral
adaptation beyond this exact native boundary returns to the lead.

After dependency/runtime publication, configuration selects the new runtime via
its existing dev-workspace channel and preserves root ea188. The workspace
consumer selects the same runtime via the existing nested override while keeping
extension767dfd58 and unrelated inputs. The system and packaged native versions
must now both be0.164 with exact source/patch agreement, although their assembled
closures can differ. The lead assigns that workspace consumer after implementer0
finishes the dependency; no overlapping repository ownership is implied.
Implementer3 may support owning technical guides after handoff. Keep histories,
old/new ranges and migration provenance explicit; selected963's SQLite state
boundary is deployed behavior and cannot be removed as obsolete history.

### Review and longer verification

Quick checks precede the affected final independent review of the completed
committed dependency/runtime/consumer deliverables. Review includes protocol and
catalog restrictions, naming prerequisites, exact package source/patches,
whole-branch preservation of current master/963/24e, consumer agreement and
native/state recovery. Prior0.163 proofs remain history, not0.164 native proof.
Lead-selected watchers run longer checks after review; prerequisite compilation
above is needed to produce exact-binary quick schema evidence, not permission
to launch long native integration before review.

Required longer evidence, reusing exact completed evidence only when source,
binary, catalog and environment identities match:

- Existing package manifest/helper/materialization/copy/closure checks for
  assembled outputs; pinned protocol and native delivery coverage affected by
  the0.164 change. Retain all four-fix browser assertions and prepared editor
  assets. Do not add unrelated VM campaigns; honor repository-required lanes.
- Existing codex-web `TestEphemeralNamespaceOwnershipIntegration`, then
  `TestEphemeralProtocolIntegration` under `-tags=codex_integration`, separately
  for both supported model profiles with exact binary SHA, source, immutable
  catalogs and IP/nft/sqlite prerequisites from `docs/reference.md`. Prove
  advertised tools, hostile dispatch rejection, cancellation and owned teardown;
  no host-network or deterministic-only fallback.
- Runtime managed naming start/loss/stop/forced-exit checks, original-daemon
  continuity in the disposable harness, and the real positive Luna naming
  canary using the final child profile within its documented budget.
- Private disposable native state:0.163-created saved thread resumed/forked
  by exact0.164, preserved thread/queue/receipt identities, native startup and
  shutdown, plus old-reader inspection before claiming any downgrade support.
  Keep production authentication/state out of these fixtures. Identical SQL
  migration files alone are insufficient; exercise changed journal/log behavior.
- Full managed DeepSeek profile against0.164 config schema before system
  builds; exact assembled system/codex-ds wrapper identity and one real isolated
  ephemeral `--strict-config` provider request under the configuration operations
  guide. Use env-key authentication, not copied production OpenAI login.

### New-native activation and recovery

Implementer2's former same-native/PID comparator is no longer a pass criterion.
Keep its historical diagnostic evidence; after new outputs exist it must
explicitly report **native change / idle transition required**, compare selected
state contracts without erasure, and bind the approved0.164 executable/source,
startup plan and expected new registration marker. Do not turn a native mismatch
into equality, normalize it away or relax ordinary workspace-host checks.

Build/root/copy exact final system and composed application outside machine
ownership as described above. Before first live activation, the lead must hold
its own aitherdev reservation and establish the ordinary idle native cutover
conditions for all affected workspaces. System0.164 and application0.164 are one
coordinated rollout; do not leave a deliberate production0.164/0.163 writer
window while waiting for sessions to idle. Prepare both first, wait without
interrupting other sessions, then follow ordinary system dry-activation/switch
and supported workspace profile switch. Recheck gates after any delay. No reboot,
provider switch, force restart or foreign-owner bypass.

Afterward verify actual new daemon executable/version/PID/start provenance and
registration (a new PID is expected), system/profile/wrapper identities,
terminal/browser agreement, saved lead/member conversation continuity, naming,
health/aliases, providers and the four fixes. Mere CLI version equality is not
daemon proof. Preserve original0.163 launch evidence, all state/journals and
native/system roots. If system succeeds and profile activation refuses or is
uncertain, retain ownership, reconcile the exact original effects and recover
forward through ordinary commands; do not start0.164 system tools against the
shared home to probe a partial cutover. Do not choose an older profile or rely
on system downgrade after new state writes without demonstrated reader support.
The lead owns any interruption/reconnection monitoring and eventual release
after verified effects and separately approved integration of deployed lineage.

### Disposable native-state verification package for implementer3

Bounded inspection found reusable public harnesses, but **no existing command
fully proves a0.163-created state upgrade to a different0.164 binary**.
At canonical codex-web8b60554, `codex/recovery_integration_test.go:241`
(`newRecoveryIntegrationHarness`) owns a private home/cwd/socket, a local
unauthenticated Responses fixture and explicit native start/stop. Its
`TestPinnedCodexRecoveryRemainsColdUntilActivation` checks persisted history,
held queues/goals and restart with one binary. `codex/headless_test.go:182`
(`TestPinnedCodexHeadlessTeamContract`) demonstrates public start/bootstrap,
resume and fork calls, again with one binary. Runtime Ruby tests using fake
commands do not establish native state compatibility.

The smallest additional implementation is **one new codex-web file**,
`codex/native_upgrade_integration_test.go`, owned by implementer3 only after the
lead assigns it. Reuse the existing recovery harness and exported Client APIs;
do not edit `recovery_integration_test.go`, the client, catalog, locks, runtime
or preflight helper files. The new file may use the existing harness's explicit
binary field between stopped phases. Coordinate its additive file with owner0;
owner0 retains repository Git/commit/publication ownership, so there are no
concurrent index/ref operations. If the existing harness cannot safely support
this without shared-file edits, return that concrete gap to the lead first.

Use `//go:build codex_integration` and an explicit
`TestNativeStateUpgrade0163To0164` test. Require absolute executable paths and
expected SHA-256/version for both binaries; absent/wrong prerequisites fail
this selected test rather than silently skipping. Bind old native to retained
jrsm0.163 and new native to the exact completed0.164 prerequisite receipt
(reported SHA256 `d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`),
then repeat or establish byte identity for the final assembled native. Resolve
paths from receipts, not a guessed store basename. Record client commit,
binary/source/patch identities and fixture command with the result.

Test phases, all after final independent review under a fresh watcher:

1. Start exact0.163 in the harness's newly created0700 home/cwd with an allowlist
   environment and loopback-only synthetic provider configuration. No inherited
   production credentials, MCP/project settings or managed sockets. Seed a
   persisted root with distinct user/assistant history through a completed
   synthetic turn, and a separate cold held thread with a saved queue item and
   immutable client ID. Wait for public readback, retain exact thread/project/
   message identities and provider hit counts, then stop and join the owned
   server before changing binaries. Never start both versions on this home.
2. Restart exact0.164 against the same private home. First read cold history and
   the held queue with implicit resume disabled; no provider hit is permitted.
   Explicitly resume only the root, complete a new synthetic turn, fork through
   the public client, and verify inherited old history, new history, distinct
   child identity and source relationship. The held thread/queue must retain
   its identity/order and remain undispatched. Restart0.164 and verify these
   persisted results again. Use existing public read/reconcile methods; do not
   fabricate rollout JSON or edit native SQL to manufacture compatibility.
3. Stop/join0.164 and preserve a complete offline snapshot of the private home
   (including database sidecars), synthetic client receipts and a compact
   assertion manifest **before** the old-reader phase. Run0.163 last against the
   same disposable path to avoid relocating absolute native rollout references.
   Read the0.164-updated root/fork and held queue through public cold reads;
   record errors and any state changes and require zero provider inference.
   Do not resume queued work or silently rebuild/import missing native records.
   Preserve the pre-probe snapshot as new-state evidence, never reuse old-reader
   mutated files as an untouched upgrade baseline. No production state is copied.

Keep upgrade and old-reader results separately identifiable. Any missing
history, changed identity/queue, unexpected inference, unreadable state,
unjoined process or unknown result fails the relevant assertion and the selected
command. Do not turn an old-reader failure into successful downgrade support.
Even successful cold reads prove only the exercised reader path, **not** full
old-version write/concurrency/system-downgrade safety. The deployment recovery
contract remains forward-only; a failed old-reader case goes to the lead for
explicit recovery disposition rather than an automatic rollback recommendation.
Do not add a general migration/backup framework or extend this into concurrent
mixed-version operation.

Proposed exact invocation, from owner0's final reviewed codex-web checkout in
its declared Nix environment (values supplied from retained receipts):

```sh
CODEX_UPGRADE_OLD_BINARY="$old_native" \
CODEX_UPGRADE_OLD_SHA256="$old_native_sha256" \
CODEX_UPGRADE_NEW_BINARY="$new_native" \
CODEX_UPGRADE_NEW_SHA256="$new_native_sha256" \
go test -mod=readonly -tags=codex_integration ./codex \
  -run '^TestNativeStateUpgrade0163To0164$' -count=1 -timeout=180s -v
```

Before review, owner3 may prepare/compile this file and run non-native
prerequisite/assertion tests only; no native process/provider execution or long
campaign. A compile-only `go test -mod=readonly -tags=codex_integration ./codex
-run '^$'` is suitable once owner0's source is stable. The ordinary existing
single-binary tests remain useful regression coverage but do not replace the
new cross-version sequence.

Offline source/schema inspection and fake fixtures can verify prerequisites,
assertion selection and the identical SQL migration inventory. The actual
saved-state upgrade requires these real local native processes; their mock
provider tests native persistence/protocol behavior without external inference
or production authentication. This does not prove real provider compatibility,
full utility tool isolation, naming or live managed-daemon activation: the
already assigned isolated DeepSeek request, exact utility namespace/hostile
dispatch suites, naming canary and ordinary deployment gates retain those jobs.

## Proposed0.164 empty-environment native restoration — REJECTED by user

**Historical proposal, rejected.** The user explicitly directed no Codex patch,
accepted tool availability for naming controlled by its prompt, requested the
named naming-session source takeover and selected Codex 0.164. The following
proposal was not implemented; its conditional build and acceptance instructions
are superseded by the final amendment below. There is no pending patch approval.

Owner0's exact source packet is
[native-empty-environment-proposal.md](codex-web-0164/native-empty-environment-proposal.md),
SHA256 `89ee449d2974a594d9b210edd6b8b73505638edd8254573b9ffb2594ad2928ed`.
It compares the retained0.163 source with frozen0.164 commit
`6aaac694803004a63c6f393d153c96d22521a6b9`. The packet establishes a static
isolation blocker; no native exposure failure has been executed or claimed.
An empty environment currently still registers catalog-selected ApplyPatch.
Its eventual execution error is not equivalent to absent advertisement and
absent native handler registration. No supported ordinary-session config switch
was identified that restores the missing gate: StableEnvironmentTools is
Removed, both accepted catalogs select freeform ApplyPatch, and internal
ToolPolicy/guardian behavior is not an operator utility configuration contract.
Do not filter reported tools, alter catalog apply-patch metadata or weaken the
zero-exposure requirement to make the candidate pass.

### Exact behavioral patch boundary

Change only four registration predicates in frozen
`codex-rs/core/src/tools/spec_plan.rs`:

```diff
@@ add_shell_tools (0.164 around1235)
-    if !features.enabled(Feature::ShellTool)
+    if !environment_mode.has_environment()
+        || !features.enabled(Feature::ShellTool)
@@ add_core_utility_tools: RequestPermissions (around1356)
-    if features.enabled(Feature::RequestPermissionsTool) {
+    if environment_mode.has_environment() && features.enabled(Feature::RequestPermissionsTool) {
@@ ApplyPatch (around1409)
-    if context.model_info.apply_patch_tool_type.is_some() {
+    if environment_mode.has_environment() && context.model_info.apply_patch_tool_type.is_some() {
@@ ViewImage (around1423)
-    if features.enabled(Feature::ViewImage) {
+    if environment_mode.has_environment() && features.enabled(Feature::ViewImage) {
```

These sites suppress registration of the spec **and** handler for empty
environments: shell ExecCommand/WriteStdin or one-shot shell, RequestPermissions,
ApplyPatch and ViewImage. Shell/ViewImage are already false in the utility
policy; their guards restore the same proven environment boundary. Inherited
RequestPermissions may be true and must still register nothing without an
environment. Keep the current55 restrictions and original full/three-field
Luna catalog contracts unchanged.

Retain0.164's full `environments.environments.len()` counting, including
configured attachments that are not yet ready; `has_environment()` is already
true for Single/Multiple and false only for None. Do not restore ready-only
counting, StableEnvironmentTools, old shell argument schemas or other0.163
behavior. Every nonempty-environment predicate remains true, preserving all
new0.164 registrations, defaults, readiness handling and execution policy.
No additional guard removal was proven for `incremental_tools`; its default
promotion is outside this patch. Preserve all native security, database,
logging, performance and provider changes.

### One patched native build through the existing shared helper

The existing `nix/codex-package.nix` copies native files; it cannot patch an ELF
at assembly time. The smallest implementation, if authorized, is a **preceding
source-build override inside that shared helper**, followed by its existing
assembly. Generic dev-workspace owns:

- `nix/patches/codex-0.164-empty-environment-tools.patch` with the four source
  guards and narrowly relevant source regression assertions;
- `nix/codex-package.nix`, conditionally selecting a patched native input for
  exact0.164/source identity, leaving current0.163 and synthetic fixture inputs
  unchanged;
- focused `nix/tests/codex-package.nix`/source-patch checks and
  `docs/codex-package.md`, correcting the current copy-only/no-Rust-change claim
  for this explicit exception and explaining removal/provenance conditions.

Append the patch with `codex.overrideAttrs (old: { patches = (old.patches or [])
++ [ ./patches/codex-0.164-empty-environment-tools.patch ]; })`. Do not replace
ea188's daemon-nix-store patch, postPatch substitutions, preBuild memory/LTO
tuning, Cargo dependency hash, V8, toolchain or security dependencies. Preserve
the daemon patch's substitution of the **new** output path, so its immutable
selection cannot escape to the unpatched prerequisite.

Bind the conditional to version0.164 and the frozen input source NAR
`sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=`; refuse a mismatched
source for this version rather than applying by version string alone. The
implementer must verify the existing derivation's source-identity attribute in
quick evaluation and use that identity directly; no source lookup/latest search
or generic patch registry. The actual retained source is
`/nix/store/10pdz4z8bfg35ysd7aqrhnzdkijpmmwb-source`; its NAR receipt passed.
A read-only query of the retained source `.drv` was unavailable during this
assessment, so no claim is made that its derivation object remains present;
owner evaluation must reconstruct/verify metadata from the frozen input if needed.

Call the selected input `nativePackage` internally and expose it through a
narrow assembly passthru for tests/evidence. The override must depend only on
the incoming raw ea188 Codex derivation and the patch file from the exact
published generic runtime. **No caller `pkgs` attribute may enter that native
override.** Runtime `flake.nix` and aitherdev `config.nix` both already call
`lib.mkCodexPackage` with raw ea188 Codex after final pin alignment. Therefore
both must evaluate to the same `nativePackage.drvPath` and output. Their
materialized wrappers/ripgrep/bwrap closures may still differ with caller pkgs.
Config system Codex and codex-ds use that assembly; workspace App Server,
terminal clients and naming use the runtime assembly. No second patch, Nix
overlay in configuration, new llm-agents fork or broad packaging layer is needed.

Package checks must compare materialized native bytes with `nativePackage`,
not incorrectly with raw ea188. Also prove the version/source/patch selection
and same underlying native derivation for both consumers, so changing the
comparison target does not conceal a divergent build. Inspect embedded native
daemon selection and closure references, not just public launcher paths.
If both callers cannot share that exact override/output, stop and report the
cause; the smallest alternative is one explicitly published patched upstream
package input consumed by both, which needs separate design/authorization.

### Complete packaging slice, review, then new prerequisite

If user approval arrives, the runtime owner may first complete this conditional
packaging/patch/tests/docs slice on the current24e branch while runtime selection
and naming remain coherently0.163. It is a complete authored deliverable with
an explicit dormant0.164 path, not a half-upgraded runtime or a consumer pin to
unfinished codex-web. Quick checks cover exact-source patch applicability,
empty versus one/multiple environment registration predicates (including
not-ready configured environments), source mismatch refusal, unchanged0.163
and fixture behavior, Nix evaluation and both-callers' native derivation equality.
Preserve complete base/head/source and patch SHA evidence.

Commit/publish that slice and obtain its mandatory independent final review
**before uncertain custom compilation**. A new fresh watcher then builds the
reviewed helper against raw ea188, with an explicit owner-local output root.
Concrete recipe (replace the single reviewed packaging SHA and root path):

```sh
nix build --out-link OWNER_EVIDENCE_DIR/patched-0164-assembled --print-out-paths --expr '
  let
    runtime = builtins.getFlake "github:aither64/dev-workspace/REVIEWED_PACKAGING_SHA";
    upstream = builtins.getFlake "github:numtide/llm-agents.nix/ea188d2f072e0ec8d5b71245e228803672801a22";
    pkgs = runtime.inputs.nixpkgs.legacyPackages.x86_64-linux;
  in runtime.lib.mkCodexPackage {
    inherit pkgs;
    codex = upstream.packages.x86_64-linux.codex;
  }
'
```

Use the expression's `nativePackage` passthru to retain the raw patched output/
derivation proof; the assembly root also retains its dependency. Custom native
compilation is a substantial Rust rebuild: the cached raw0.164 executable is
not reusable as the patched result. Nix may reuse frozen fetched Cargo/V8
dependencies, but build duration/resource use is unproven. Retain upstream
build tuning and use the ordinary watcher/escalation workflow.

The new output **must receive a new measured SHA256 and exact derivation/source/
patch receipt**. Raw prerequisite hash `d2af1cd0...f54ae` cannot certify it, and
neither equal0.164 version text nor unchanged source schema is binary identity.
Owner0 may continue source catalog/protocol preparation against frozen0.164;
the four-guard patch does not change catalog bytes or public schema source.
Reuse those unaffected static checks with explicit diff proof, but generate/
validate schemas from the patched exact executable when exact-binary proof is
required. Do not rerun unrelated work or launch native isolation before the
complete combined dependency/runtime/consumer review.

After the patched prerequisite and codex-web publication, complete the ordinary
aligned0.164 runtime/native/naming/catalog/pin updates and consumers. Re-review
affected final deliverables/whole history before long native campaigns. Owner3's
cross-version test, owner2's idle-transition preflight and all native utility/
naming/provider fixtures must consume the **new patched hash/output**, not the
old raw hash. Keep separate old0.163, raw0.164 and patched0.164 provenance.

### Acceptance and recovery limits

Required decisive evidence is empty tool exposure **and absent native registry
dispatch** for both original full GPT5.5 and derived Luna profiles, including
hostile ApplyPatch/RequestPermissions calls and inherited permission enablement.
Also verify normal one/multiple environment controls preserve upstream0.164
tool schemas/registrations, including not-ready attachments, and execute the
existing positive eligible-tool controls. Do not accept a hidden spec with a
registered handler or an environment error after handler dispatch.

Run all already-required patched-binary namespace teardown/isolation, naming,
saved0.163-state resume/fork and old-reader gates, materialized helper/daemon-copy
checks, and system DeepSeek schema/strict-config/isolated provider checks after
the appropriate review. Keep original immutable catalogs and all unrelated
native behavior. The patch introduces no database schema or public protocol
change; it does not justify broad downgrade compatibility claims.

Activation remains the coordinated idle-native cutover with exact new binary
proof and ordinary host guards. Preserve original state, roots and receipts.
Recover forward with the same reviewed patched source or a corrected compatible
successor. Raw0.164 is **not** an accepted utility-isolation recovery target;
0.163 downgrade remains subject to the separate state-reader gate. No code,
patch application, build, native probe, claim or activation was performed to
prepare this proposal, and this document does not supply the pending approval.

## Raw Codex 0.164 and naming-source takeover — governing amendment

**Status: implementation brief ready, 2026-10-25.** The user explicitly rejected
patching Codex, accepted tools for naming controlled through its prompt, selected
Codex 0.164, and clarified that takeover includes **all unfinished naming work**.
The lead accepted the minimal prompted-ephemeral API boundary below. There is no
pending permission or design choice for these packages. No native patch, custom
Rust compilation, native feature expansion or default-branch integration is
authorized by this amendment. The original four portal fixes and all merged
performance, reliability, SQLite and retention behavior remain required.

### Exact source inventory and preservation

Canonical objects and SSH remote refs identified these published naming heads:

| Repository | Source comparison base | Published naming head | Complete source-only series |
| --- | --- | --- | --- |
| codex-web | `872c7ad3962f9fa9b17358244e27f3e3fac59fc5` | `801099102ef9af4a82c1f3853c53d6b442ecd4dc` | `80109910` native retry ownership and safe fresh-attempt proof |
| dev-workspace | `10bb047513c82d1310e8fcaa797e8772f948dd8a` | `529e075ad07e2d967a8af4902584e37527115454` | `6c963d70` dependency selection; `d328def7` naming retry/manual recovery; `5f922701` archive readiness diagnostics; `447aeda8` retirement cancellation; `529e075a` creation-refusal diagnostics |

These bases are verified merge-bases for comparison, not invented historical
session registration bases. Neither source head contains the newer runtime 963
or codex-web 8b605 delivery/SQLite changes. Import the feature deltas onto our
current branches; never replace their trees with the naming heads or apply a
two-endpoint diff that reverses newer master changes. Preserve source heads and
the old/new comparison ranges in review receipts. Consolidate the source's old
dependency-only `6c963d70` into our one final dependency update; do not import its
old lock/module bytes as the selected dependency.

Our runtime starting point is `24e66096ae65a97b1e2d14b68a566f44519a8c2d`, with
`9634151b9836311c331a58880fbb4c46133fd98f` as an ancestor. Its complete feature
series is `8931ad6e` switches, `44b44008` unread, `49bc91a4` composer,
`e36da70a` silent queue refresh and `24e66096` documentation. Owner1's fresh
fetch confirms master still 963 and zero runtime baseline drift. Codex-web starts
from current `8b60554bc10c2a6bcbf9732a8b77ad959c317036`; owner0 freshly verifies
master before its integration. New substantive drift returns to the lead.

The authorized intake by owner3 found both named source worktrees clean and
stable at the exact published heads: no staged/unstaged or nonignored untracked
work, and no relevant ignored source. All 24 source-file snapshots match the
committed blobs; before/after HEAD, index and file identities agree. Thus all
unfinished source found is represented by these published deltas. Evidence:
[intake.md](naming-source-intake/20261025T163000Z/intake.md), SHA256
`51ffd5670f6915da2b9d29a2f19209b6178d10a2f0ba5b044b1ceba011534818`,
plus that directory's summary, final verification, exact inventories and
binary-safe snapshots. No foreign team/runtime/lifecycle ownership is adopted.

The named source's consumer heads `cbf7864a75127a374d65fc9bbb7c4fdd6cea30d1`
(workspace) and `a2ba6fe4ed06584b39ec8144b225e85428a6b036` (configuration) are
provenance only. Regenerate our final consumer pins on fresh defaults. Config's
fresh baseline is `b167cd4388a5c94ff3f978df85b6800fafd1b8af`: retain its disk
retention documentation, all merged inputs and root llm-agents_2 selection at
ea188. Update only its devWorkspace channel to our published final runtime.
Never replay the held eac candidate or source-session consumer pins.

### Minimal API and naming contract

The actual production caller of `RunEphemeralTurn` in the inspected runtime is
`portal/internal/web/session_namer.go`; codex-web has its public API and tests,
and the inspected extension has no Go caller. Keep that public strict API's
existing **Codex 0.163** contract and supported fixtures. Do not silently claim
that raw 0.164 satisfies its empty-tool/absent-registry guarantee.

Owner0 adds one explicit `RunPromptedEphemeralTurn(ctx, EphemeralTurnOptions)`
entry point returning the existing `EphemeralTurnResult`. It reuses the current
bounded private runner, sink and imported retry proof. The old entry point stays
strict by default; do not add a permissive boolean/config escape to its options,
a duplicate runner, an arbitrary policy map, or a general profile framework.
Select the two fixed internal contracts at the entry points. The prompted path
supports the naming pair `gpt-6-luna`/`low` on exact raw 0.164; adding other
prompted profiles is unnecessary. `CanRetryEphemeralTurn` can serve both paths:
its proof concerns stopped execution and cleanup, not absence of native tools.

Retain the existing immutable catalog bytes and strict tests. The prepared
0.164 full and derived Luna catalogs are byte-identical to their 0.163 resources:
full SHA256 `943ca7fe1d19ed019054158303f0dbbd80b3bef43b3aa425a71aa7cb3fb52c2b`,
Luna SHA256 `049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`.
Use one canonical resource per catalog, with reproducible provenance for both
upstream releases. Preserve the three Luna transformations (`direct`, empty
experimental list, Responses Lite false); do not change ApplyPatch or introduce
artificial metadata or duplicate files to distinguish releases.

Catalog validation proves the expected content, not the native version or its
tool-isolation behavior. The strict API cannot distinguish these releases from
identical catalog bytes or a pathname, and must not pretend to do so. Its supported
contract remains strict 0.163; prompted naming supports exact raw 0.164. Actual
consumer executable verification, release-specific native tests and support
documentation establish that boundary. Successful catalog validation alone is
never strict-isolation evidence on 0.164. No new native version negotiation,
path-trust mechanism or arbitrary policy option is needed.

Use existing compatible App Server lifecycle requests and fixed restrictions
as defense in depth: private connection and scratch cwd, ephemeral thread,
empty environments/runtime roots/dynamic tools, read-only sandbox, never
approval, existing MCP inventory handling, instruction overrides and immutable
startup catalog. Do not weaken these settings merely because tools may be
advertised. Existing55 policy/config checks passed against 0.164; a concrete
additional incompatibility must be reported rather than normalized away.

The prompted contract **does not guarantee zero advertised tools, absence of
native handlers, absence of tool attempts, or tool-effect isolation**. Native
tool availability can survive those settings. Naming instructions must explicitly
say to use only the supplied request as data, never use tools, read files, run
commands, browse, delegate or ask questions, and return only the name JSON.
This is model guidance, not an enforced security boundary. No success, denial or
absence of a particular tool is fabricated in reports or tests. Keep rejecting
interactive server requests/questions through the existing bounded private sink;
do not route naming to ordinary approval UI. Global serving policy remains
trusted. Do not give naming the workspace cwd, attachments or team context.

Preserve all source naming behavior:

- One 30-second absolute deadline begins before queue admission and includes
  retries/backoff/cleanup; two operation slots remain held until cleanup ends.
- Owned `willRetry:true` stays in the same native turn. At most one fresh call
  follows only positive transient/settled/cleanup proof, after 200 ms backoff and
  with at least 1 s inference plus 250 ms cleanup remaining. Recheck cancellation
  and budget after backoff. Ambiguous starts, foreign events, failed cleanup,
  invalid output and unknown/permanent failures never authorize a fresh call.
- Resolve provider once per operation; retain model, effort, instructions,
  schema and bounded input through both calls, using fresh private scratch.
- Input remains at most 8192 UTF-8 bytes, without attachment names/paths/content.
  Output remains exactly one JSON `name`, no duplicate/extra keys, two to six
  lowercase ASCII words joined by hyphens, at most 48 bytes; adapter output is
  at most 256 bytes. Only the exact owned completed final answer counts.
- Exhaustion/unavailability/invalid output pauses before base selection or
  reservation. Keep the accepted request/files/settings for Retry naming or a
  custom name. No neutral/heuristic fallback; attachment-only input requires a
  custom name. Explicit cancellation still stops preparation.
- Retain the portal-owned naming child, local socket, no ordinary-daemon
  fallback/automatic respawn, worker cancellation before child shutdown,
  bounded group termination/join and managed-service cgroup boundary. Remove
  only owned scratch after cleanup; failed removal prevents retry/success.
  No session archive/delete/unload action or persisted-thread adoption is added.

### Owner packages and dependencies

**Dependency first — owner0, codex-web.** Import the entire 801099 source delta
onto current 8b605, including `codex/ephemeral.go`, `ephemeral_retry_test.go`,
`ephemeral_test.go`, `ephemeral_integration_test.go`, `docs/reference.md` and
`test/codex_protocol_contract.py`. Preserve current admission/SQLite/transient
delivery behavior. Add the minimal prompted entry point/shared internal selection,
the shared catalogs' dual-release provenance and focused tests. Own associated provider/native
fixtures, `skills/update-codex-web/SKILL.md` and catalog refresh helper changes
needed to describe and reproduce both supported contracts. Preserve strict 0.163
assertions rather than relabeling them as0.164 passes. Reuse completed exact
raw 0.164 schema/config/catalog preparation where unaffected; update request-corpus
coverage if the shared runner moves call sites. Publish a coherent dependency
before runtime pins it. This package is released for implementation by this brief.

**Runtime — owner1, dev-workspace.** Source takeover can proceed independently
on 24e while the final dependency is prepared. Import d328, 5f922, 447, 529 source
deltas, preserving newer behavior where contexts overlap. Owned paths are
`portal/internal/web/session_name.go`, `session_namer.go`, their naming/retry/
preparation tests; `portal/internal/workspacecodex/client.go`, `client_test.go`,
`loaded_retirement_test.go`; `nix/tests/session-creation.nix`;
`test/{archive_lifecycle_browser.cjs,creation_acceptance_browser.cjs,
creation_model.py,creation_refusal_diagnostics_test.py}` and
`test/support/creation_refusal_diagnostics.py`; relevant preparation/package/
portal docs. Retain retirement cancellation causes and bounded sanitized
diagnostics without weakening source-lock refusal or first-failure assertions.

Then select the published dependency in `flake.nix`, `flake.lock`,
`portal/go.mod`, `portal/go.sum`, regenerate the final vendor hash in
`nix/workspace-portal.nix`, and select raw ea188 for packaged0.164. Wire naming to
the new prompted entry point, fixed no-tools instructions and matching catalog.
Update `portal/cmd/workspace-portal/naming_runtime.go`, its tests, package/native
fixtures and naming prerequisite version/hash/length expectations together.
Keep native assembly in `nix/codex-package.nix` unchanged: no patch selection or
overrideAttrs Rust build. A final committed deliverable must not combine
runtime 0.164 with a 0.163-only naming adapter. Source retirement changes do not
authorize any lifecycle execution.

**Independent support.** Owner3's intake is complete. Its already assigned
disposable 0.163-to0.164 state test remains a separate file boundary coordinated
with owner0; it continues using raw d2af. Owner2's new-native idle-transition
preflight remains in deployment-preflight, with no candidate observations or
activation until assigned by the lead. Technical docs can be delegated on exact
paths after owner0/owner1 agree boundaries; Git/index operations stay serialized.
The lead owns final assignments, review, watchers, claims and activation.

**Consumers last.** After runtime publication, configuration owner selects only
the final runtime through its existing dev-workspace channel on fresh master,
retaining root ea188 and all newer merged inputs. Workspace owner updates its
existing direct nested runtime override to the same final SHA, retaining the
extension and unrelated graph. Run the existing deployment consistency checker.
No application system pin, old consumer replay or unrelated input update.

### Quick checks, final review and acceptance

Quick checks in repository-pinned environments cover both entry-point contracts,
catalog/protocol/config validation, complete source retry tests and the current
delivery/SQLite suite. In particular retain native-progress versus fresh-call
distinctions, early/foreign/malformed error handling, post-completion retry-proof
revocation, cleanup failure, deadline/cancellation, unchanged provider/input,
slot ownership and the two-call cap. Check naming prompt instructions, exact
output validation, manual/attachment-only recovery and no early reservation.
Run retirement cancellation regressions and diagnostics parser/browser syntax
checks. Preserve all four-fix quick coverage and package pin/vendor checks.

Complete all intended changes, commits and quick checks, then obtain mandatory
affected final review of the combined histories/diffs, API support boundary,
source takeover, current merged-behavior preservation, native identities and
consumers. There is no patch-equivalence claim for this integration. Review
must explicitly assess no new migration in naming and preservation of existing
SQLite migration/readers; deleting their dependency/docs is a regression.
Only after final review run longer watcher-owned exact-binary acceptance.

Native acceptance now selects **prompted 0.164** for naming, with measured tool
exposure retained honestly. Do not require an empty tools list or absent native
registry for this path; those assertions remain with supported strict 0.163.
Keep real namespace/process teardown, provider routing, no interactive question
admission, output/deadline/retry and managed-child lifecycle tests. Run the real
positive naming canary through the same packaged child/prompt, within 30 seconds.
Provider/mock tests prove protocol and ownership; only real isolated provider
execution proves the selected model's positive naming behavior.

The source session's creation acceptance was **FAILED/unresolved**, including
explicit PLAN/FORK source EX|NB lock refusals. Its prior source/native/browser
passes are retained evidence, not proof this integration is ready. Reproduce or
refute those failures in our owned disposable creation fixture after review,
retaining all assertions and sanitized diagnostics. Require actual naming,
ordinary creation, PLAN and FORK, cancellation/manual recovery, collection
concurrency and package/preparation exclusion. Diagnose a renewed failure; do
not hide it with automatic creation retries, larger timeouts or skipped cases.
Existing browser verification still needs real prepared/package review assets.

Retain the already required disposable 0.163-created state -> exact 0.164 cold
read/resume/fork/restart and old-reader recovery gate, and the system DeepSeek
full-schema/strict-config plus isolated real-provider probe. No old-reader
success alone proves safe production downgrade. No production credentials,
foreign records or live native process are test fixtures.

### Native identity, deployment and recovery

Selected raw package remains llm-agents
`ea188d2f072e0ec8d5b71245e228803672801a22`, Codex 0.164.0, upstream
`6aaac694803004a63c6f393d153c96d22521a6b9`, source NAR
`sha256-iib2+qQcGewC4Ga8cA80sInDJpzdSxDJP0y1DDOouI4=` and executable SHA256
`d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`.
The completed native0164-prerequisite receipts and roots remain valid;
there is no custom-binary prerequisite or new patch SHA. System, codex-ds,
workspace and naming must select assembled copies of these raw native bytes.
Keep merged 0.164 security/reliability/source behavior and existing helper layout.

Earlier rollout ordering still applies: final reviewed system/application builds
and copy/preflight first; retain an explicit owner-local application out-link
through rollout and record the complete input graphs, output paths and roots.
Prepare outside machine claims. Actual new-native activation requires ordinary
idle guards and the correct reservation; never interrupt another session or
run unsupported mixed 0.163/0.164 writers against the shared Codex home. Activate
system before dependent user profile through existing coordinated procedures,
then prove actual daemon/native identities, naming/creation, health/conversation
continuity and the four portal fixes. Preserve old roots, state and original
operation receipts. Recover forward through the original attempt with a reviewed
compatible package; do not infer downgrade safety or restore old submission JSON.
No merge, release, cleanup or source-session lifecycle action follows from
takeover or deployment authorization alone.

## Wrapped capacity error — bounded retry classification amendment

**Status: lead accepted, implementation ready.** The user reported a normal
conversation showing **Turn failed** with this exact native error:

```json
{"additionalDetails":null,"codexErrorInfo":"other","message":"stream disconnected before completion: Codex is at capacity, please try again later","misalignment":null}
```

This is an additional bug fix in the current deliverable, separate from the
four portal fixes and naming takeover. It changes classification in existing
retry owners; it does not add a scheduler, retry accepted original messages,
override disabled retry settings or patch native Codex.

### Evidence and actual retry owners

At codex-web base8b605, `codex/client.go:4412` (`transcriptFailureEntry`) renders
stored `turn.error` as **Turn failed** and retains details for code `other`.
`codex/turn_state.go:36-87` (`ReadTurnState`) reads the exact latest native turn
and preserves `TerminalFailure.Code` and `.Message` only for failed status.
Runtime `portal/internal/workspacecodex/turn_retry_proof.go:21-30` currently
copies only Code into its internal observation. `portal/internal/turnretry/
state.go:222` recognizes `serverOverloaded` as capacity and `cyberPolicy` as
cybersecurity; `other` therefore misses the ordinary capacity controller.

Naming has a separate gap: imported801099's `ephemeralTurnError` accepts typed
overload/internal-server/finite transport failures, but not this exact `other`
message. Owner0's in-progress shared-runner snapshot is SHA256
`abdd93275e8fb9c2e506915d4046f78178f7ce38d6d677e374714617a5cf449f`, with classifier
around1070/1108 and proof wrapper/cleanup/canRetry around35/200/910. These are
read snapshots, not final commit identifiers. There is no `native_error.go` in
this inspected tree; the earlier pointer to that name was corrected.

Frozen raw0.164 source `6aaac694803004a63c6f393d153c96d22521a6b9` confirms:
`protocol/src/error.rs:112` wraps `Stream(String)` with the reported prefix;
its `to_codex_protocol_error` around490-528 maps unhandled variants, including
Stream, to Other. The capacity suffix is reported user evidence, not a literal
found in native source. `app-server-protocol/src/protocol/v2/notification.rs:62`
defines `willRetry:true` as native-owned progress that does not interrupt a turn.
`app-server/src/bespoke_event_handling.rs:1062-1084` sends intermediate StreamError
with true; `handle_error_notification` around1633-1654 records terminal error
and sends false. Neither an error notification nor its message alone proves
settled execution. No native/provider probe was needed or run for this diagnosis.

### Exact change and ownership

**Owner0, codex-web:** add one small shared pure predicate, for example
`IsCapacityFailure(code, message string) bool`, in `codex/capacity.go` with focused
tests. It accepts the existing typed `serverOverloaded` or **only** code `other`
with the exact full message in the fixture above. Use exact case-sensitive
equality: no substring, regex, prefix stripping, whitespace normalization,
recursive unwrapping, generic `other`, arbitrary stream error or 5xx text
matching. Do not reclassify a permanent discriminator even if its message
contains the capacity words. No provider-specific registry is needed.

Call the predicate from `ephemeralTurnError` after its existing error-shape
validation, preserving all current typed classifications and unknown/malformed
handling. Keep native `willRetry:true` on the same owned turn; the predicate
only makes the exact terminal capacity failure eligible for existing proof.
`CanRetryEphemeralTurn` still requires settled owned execution, successful
cleanup and no deadline/cancellation; a string/category alone grants nothing.
The shared strict/prompted runner uses this same classification. Update its
reference statement that messages never participate in classification to state
this single explicit compatibility exception. Leave transcript rendering and
raw `TerminalFailure` fields unchanged.

**Owner1, dev-workspace, after the dependency API is available:** in
`portal/internal/workspacecodex/turn_retry_proof.go`, classify the preserved
native Code/Message with the predicate. Project a positive result to the
existing internal observation Code `serverOverloaded`; otherwise retain Code.
This is an internal policy input, not a rewrite of the native failure. No
Observation/state schema change, persisted message field, UI classifier or
change to `turnretry.Class` is necessary. Update focused workspacecodex retry
tests and the existing portal retry documentation's supported capacity cases.
Owner0/owner1 serialize changes with their current dependency/runtime packages;
this amendment releases these exact additions and the lead owns final review.

### Invariants and acceptance

Ordinary conversations continue through the existing durable controller and
`ContinueFailedTurn`, with the same capacity preference, enrollment baseline,
handled watermark, enabled classes, exact session/thread/provider/settings proof,
loaded/quiescent latest failed turn, empty queue/request holds, admission locks,
backoff and stable continuation identity. Preserve its15/30/60/120/240/300-second
delay policy and jitter. Its visible continuation asks to continue from saved
state and inspect before repeating actions; it never replays the original user
prompt. Partial output/tool results remain in the original failed turn and do
not authorize a fresh original-message send. In-progress/native-retrying turns,
cold or changed threads, unknown admission and missing proof still cannot start
a new continuation. Lost acknowledgements reconcile the same continuation ID.

Do not reset `Handled`, reenroll old failures, clear receipts or enable a user's
disabled capacity setting. A failure already consumed as unsupported remains
subject to existing explicit/manual continuation and enrollment behavior; this
fix does not retroactively replay it. No live repair is authorized here.

Naming retains its separate30-second deadline, two operation slots, native
retry ownership, at most one proof-gated fresh call,200ms backoff and reserved
cleanup time. The new predicate does not restart budget or relax ambiguous
identity, partial/malformed completion, interruption-only or cleanup failure
rules. This path does not use the ordinary conversation scheduler.

Required quick regressions before final review:

- Exact reported JSON, including null optional fields, qualifies; typed overload
  still qualifies. Other text, another stream-disconnect reason, nested/extra
  prefix or suffix, case/whitespace variants, nil/structured/unknown codes and
  permanent error codes with capacity wording do not gain classification.
- ReadTurnState/transcript retain raw `other` and the full message. The runtime
  backend alone projects the positive capacity observation. With the capacity
  preference enabled and existing proof, an owned failed turn schedules once
  after existing backoff; with the preference disabled, no continuation occurs.
- Controller integration keeps partial output/history, latest-turn and queued
  input/request gates, missing settings proof, stale/handled failure suppression,
  stable-ID lost-reply reconciliation and no duplicate original-prompt replay.
  Reuse existing fixtures; add the exact error to the fixture path that exercises
  real ReadTurnState -> RetryBackend -> controller behavior.
- Naming receives this same exact failure as native progress and stays on one
  call; terminal failure plus owned failed completion and cleanup qualifies for
  one fresh call. False notification alone, foreign turn, lost start response,
  malformed/contradictory completion, deadline and failed cleanup never qualify.
  Preserve existing retry-cap/provider/input/slot tests for both entry points.

Include the helper, projection and these tests/docs in affected final review.
No independent long campaign is added for this pure classification fix; reuse
unaffected evidence and include relevant cases in already planned native/naming
verification only where needed. Existing raw0.164/d2af identity, deployment idle
gates, saved-state recovery and no-native-patch decisions remain unchanged.

## Review follow-up: late evidence must revoke ephemeral retry proof

**Disposition prepared; source remains frozen.** This is a bounded design
response to reviewer0's preliminary finding, not an independent review or a
release to implement. The lead releases owner0's narrow fix only after the final
finding and review handoff. Inspected committed codex-web head:
`975746f40fe99c77689ede064197772e2cc25c18`.

Confirmed source boundary: `codex/ephemeral.go` around802-810 returns after
`noteCleanupIdentityLocked` when `s.err` already exists. That identity helper
around947 does not validate completed status/error or async-question semantics.
`consumeLocked` around973 similarly short-circuits after `rejectErrorLocked`,
which checks error notifications only. Therefore previously recorded terminal
failure must not exempt later turn/item evidence from validation. This document
does not claim a test reproduction or replace the reviewer's final grading.

### Smallest correction

Owner0 keeps this inside the existing ephemeral sink in `codex/ephemeral.go`,
with focused tests in `ephemeral_retry_test.go` and the shared strict/prompted
entry-point coverage. Use one bounded, lock-held validation/revocation path for
relevant error, turn and item evidence **before** either prior-error return,
both in direct delivery and buffered replay. Reuse existing envelope, identity,
item/question and failure validators; no second event queue, scheduler, public
option, native change or tool-policy contract is needed.

Retry eligibility is monotonic after contradictory evidence: clear the transient
candidate permanently for this call, preserve failure/cancellation, and never
let a later valid frame restore it. Retain the existing exact connection,
thread and turn checks and mark cleanup ownership ambiguous when appropriate.
The returned error may retain its original safe category; the essential result
is `CanRetryEphemeralTurn(err) == false`. Error messages/diagnostics must not
be exposed or persisted to implement this check.

Once the exact terminal completion establishes settled failure, inspect later
completion evidence even if the call is already unwinding. A success, renewed
in-progress/start, different terminal status, changed error evidence, malformed
status/error/items or conflicting final-answer evidence revokes proof. Validate
async delivery/question metadata on standalone item started/completed events
and items embedded in a completion, including after failure. Those interactive
events still fail without entering ordinary approval/question UI. Native tool
availability remains allowed for the prompted path; this fix must not equate
every non-agent item with an isolation violation.

An ordinary duplicate is not contradictory: the same owned terminal failure
with equivalent validated status/error/item evidence can remain a candidate;
same final-answer item ID/text remains the existing idempotent duplicate.
Comparison concerns consumed semantic evidence, not JSON key ordering or
unrelated timestamps. If remembering the first terminal evidence is necessary,
use a single bounded in-memory snapshot/digest within the sink, not a new
registry or persisted format. A different error that happens to share the same
transient classification is not an equivalent duplicate. Do not loosen the
existing post-settlement error-notification rule as part of this fix.

Any relevant frame processed during cleanup must affect the final retry-proof
decision. Owner0 must ensure no previously cached true predicate survives a
revocation before the helper returns; use the existing private connection
teardown/lock boundary, without adding an unbounded wait or reconnecting. If that
boundary cannot be established by a narrow change, report the concrete issue to
the lead rather than adding transport machinery. Preserve original cleanup
deadline, owned-turn interruption rules and unsubscribe/close behavior.

### Focused acceptance and handoff

Extend the existing deterministic direct-delivery and pre-bind buffered-replay
fixtures: first establish the exact transient failed completion, then deliver
each late case before cleanup/proof issuance. Cases must cover same-owned success,
changed permanent **and different transient** error, malformed completion,
contradictory status/start, conflicting final-answer evidence, and async/question
items both standalone and embedded. Every case returns a nonretryable failure,
starts no fresh turn and performs no foreign or redundant interruption.
Exercise both public entry points through their shared sink.

Positive controls retain one ordinary owned transient failure with successful
cleanup, its equivalent duplicate, consistent duplicate final-answer evidence,
and native `willRetry:true` before terminal settlement. They must preserve their
existing behavior. Keep identity, lost-start-response, cleanup-failure,
cancellation/deadline and capacity-message regressions passing. Runtime naming
still owns at most two calls inside one30-second budget; no runtime classifier,
ordinary conversation controller, catalog or consumer behavior changes here.

After lead release: owner0 implements and quick-checks the narrow fix, commits
through normal ownership and returns it for the appropriate affected review.
Downstream pins follow only the final published dependency. Unaffected review
and test evidence remains retained; no independent native campaign is added by
this planning amendment. No application edit or test was performed by architect0.

### R1 teardown disposition — released bounded implementation

**Status: lead accepted and released after owner0 reads this subsection.** The
final independent report confirms Important R1; this subsection supersedes the
earlier prepared-only/teardown hold for this exact package. Other frozen heads
remain under lead coordination. The same retained reviewer must assess the final
committed, quick-checked repair in affected general, architecture and
risk/compatibility lanes before publication. The previous review did not cover
this additional internal connection-lifetime implementation.

At reviewed975, `runEphemeralTurn` caches `retryable` before `private.Close()`.
`Client.Close` around1033 calls `markDisconnected` around1594, which clears the
sink's transient candidate. `readLoop` around1297 has no caller completion signal.
Moving the predicate after current Close therefore rejects valid retry proof;
leaving a pre-close snapshot can ignore a later processed contradiction. A
revocation token returned while the reader remains active is insufficient: its
consumer can race the next dispatch. Use a finite private-reader completion
barrier instead.

Owner0 owns `codex/client.go`, `codex/ephemeral.go` and focused existing/new tests.
Keep this internal to the already private ephemeral client:

1. When Ensure publishes its ephemeral connection under `connectionMu`, also
   publish one private reader record containing that exact connection pointer,
   generation and `done chan struct{}`. Initialize it before starting the reader.
   The existing reader goroutine closes done exactly once in its deferred exit,
   covering every return: read failure, decode rejection, event processing and
   normal close. Retain the record after detachment so teardown can join it.
   Ordinary clients need no new completion wait or behavior.
2. Complete the existing owned interruption/unsubscribe cleanup under the
   original cleanup deadline. Do not cache a final success or retry decision.
   Capture the private reader record for the exact generation, then use a narrow
   internal local-close operation to atomically set this private client closed
   and detach its matching connection/ready state under `connectionMu`.
   Reuse existing pending-call/settings/disconnect bookkeeping; do not omit
   it or duplicate a transport engine. The local-close branch skips only its
   synthetic `ephemeral.fail(ErrEphemeralServer)`. It does not clear an existing
   failure, reset transient evidence or bypass event validation.
3. This atomic detach is the local shutdown cutoff. An unexpected disconnect
   that wins before it follows ordinary `markDisconnected` and revokes proof;
   a missing/mismatched active generation must not be relabeled an expected
   close. Read errors caused by closing the already detached connection are
   stale-generation teardown notifications and cannot destroy a valid proof.
   Do not add a global "ignore errors while closing" flag or message matching.
   All protocol/item/question failures still reach the sink, including a frame
   already read when local shutdown begins. Never skip such processing merely
   because the client is marked closed.
4. Release locks, call `CloseNow` on the captured connection and wait for its
   reader-done signal, selecting against the **existing** cleanup deadline.
   Do not wait or close the socket while holding `connectionMu`/sink mutex;
   preserve existing lock order (`connectionMu` before sink where both are
   needed). No new reader, reconnect, detached cleanup task, arbitrary timer or
   unbounded join. This client uses ordinary Read, not a new CloseRead/handshake
   mode. The barrier proves completion of application processing for already-read
   frames; it does not claim to drain future remote traffic after local closure.
5. Only after successful join, inspect the final sink failure/eligibility under
   its mutex. Then decide the return value and retry wrapper using the existing
   exact generation/thread/turn, settled-terminal, cleanup and context predicates.
   A late failure must also prevent returning a previously sampled success.
   A missing/mismatched reader after a connection was launched, join timeout,
   shutdown error or failed cleanup produces no positive retry proof. Close the
   socket even on failure; no helper waits beyond its original deadline.
   A typed transient dial failure before any reader/connection/thread existed
   retains its existing separately proved pre-start retry path; do not require
   a nonexistent reader for that case.

The public `Client.Close()` contract and ordinary connection/reconnect semantics
remain unchanged. A small internal factoring of disconnect bookkeeping is
acceptable to implement the exact local-close branch above; arbitrary ordinary
callers cannot suppress transport failure. If implementation requires changing
public Close, shared reconnect policy, or adding a broader reader supervisor,
stop that departure and return the concrete requirement to the lead.

Add deterministic focused tests, without timing sleeps as race evidence:

- Valid owned transient completion plus acknowledged cleanup and expected local
  close still yields positive proof; valid success still returns its answer.
  The no-reader transient-dial case remains valid.
- A frame already returned by Read but paused before sink handling is released
  during teardown. Contradictory completion or async-question evidence revokes
  proof before return; helper cannot finish while that processing is pending.
  Cover the existing pre-bind replay and direct cases too.
- An unexpected disconnect winning before cutoff revokes proof. Expected local
  close after acknowledged cleanup does not. Identity/generation mismatch,
  failed cleanup, deadline expiry and reader that does not finish by the cleanup
  deadline never yield proof. Timeout closes owned transport and adds no retry.
- Existing ordinary Close/pending-request disconnection and generation fencing
  tests retain their behavior. Run focused race checks for the new private
  finalization ordering with bounded fixtures, using the normal quick/check
  ownership rules; no native/provider campaign is needed for this correction.

Preserve R1's monotonic late-evidence validator and equivalent-duplicate controls,
both strict/prompted entry points, native-progress ownership, naming30-second
budget/two-call cap and all ordinary conversation policy. No runtime API/schema,
catalog or native-byte change follows from this internal barrier. Owner0 returns
the complete narrow source/test/doc diff and quick evidence for affected review;
consumer pins update only after the corrected dependency is reviewed/published.

## Native fixture version probe: separate stdout from stderr

**Status: bounded disposition accepted by lead; owner0 implements after lead
reads this complete subsection.** No native rerun is authorized by this record.
Native batch outer26165 settled: stage00 roots and01 namespace ownership passed;
stage02 prompted0.164 failed at its version precondition, before App Server or
protocol acceptance;03-06 did not run. Before/after guards passed and the watcher
reported no process remaining. Preserve the original attempt, roots and raw log:
[02-prompted-0164-luna.log](client-native-verification-preparation/attempt-d0fe57b-01/02-prompted-0164-luna.log).
No cleanup or rewrite of that failed evidence follows from this correction.

Inspected client head is `d0fe57bed9022db526fbe90836a8576dc4e92950`.
`codex/ephemeral_integration_test.go:570-574` invokes the reviewed binary with
`--version`, then compares `CombinedOutput` with the exact expected version.
The reported exit was successful and stdout contained `codex-cli 0.164.0`,
but stderr contained the native helper-alias warning; merging both streams made
the version assertion fail. This establishes a fixture parsing defect, not
native inference, helper, tool exposure, persistence or state compatibility.

Frozen0.164 source `6aaac694803004a63c6f393d153c96d22521a6b9` explains the warning:
`arg0/src/lib.rs:154-166` prints it with `eprintln!` and continues. At318-326,
release builds refuse alias creation when CODEX_HOME is under the native child's
`std::env::temp_dir()`. The fixture's explicit environment omits TMPDIR, so the
child uses `/tmp` even though the outer Go runner has its own TMPDIR. The actual
ordinary and utility App Servers at1759/1768 use the same environment pattern.

The warning has real, bounded consequences: no generated `apply_patch` or
`applypatch` PATH aliases from that setup, and no alias-based sandbox path.
`arg0/src/lib.rs:225-260` retains `codex_self_exe` and falls back to the current
executable for Linux sandbox re-execution; its comment specifically distinguishes
alias behavior on bubblewrap versions without `--argv0`. Existing package PATH
handling also remains. Source proves this fallback exists, not that every helper
or representative control succeeds in this fixture. Do not call the warning
helper-neutral or dismiss a later control failure because `--version` passed.

### Exact fixture correction

Keep child environment, home paths, namespace setup and helper behavior
unchanged. Do **not** add a sibling TMPDIR, enable aliases, inject production
home/config, suppress stderr, alter native code, or allow new persistent symlinks.
Enabling aliases would create home/tmp/arg0-linux symlinks that the existing
`snapshot` around3934-3990 deliberately rejects; changing that boundary is not
part of this parser fix. Never skip or normalize those persistence assertions.

Owner0 changes only the test-owned version capture at:

- `codex/ephemeral_integration_test.go:570-574`, shared by scheduled stage02
  prompted0.164/Luna and stages03-04 strict0.163/GPT5.5 and Luna;
- `codex/native_upgrade_integration_test.go:124-129`, which uses the same flawed
  CombinedOutput comparison for both binaries in scheduled stage06.

A small shared test-only probe/capture helper and deterministic helper tests may
live in the existing integration-test files. Capture stdout and stderr
separately. Require exit success and exact expected stdout using the existing
whitespace convention; no regex extraction, accepting the last line, searching
for a version inside warnings, or accepting a version printed only to stderr.
Bound stdout and fail overflow. Retain stderr in the existing bounded diagnostic
style (for example8KiB tail with truncation identified), including on successful
version checks; keep version, exit status and warning diagnostics distinguishable
in the watcher log. Nonzero exit, timeout, empty/wrong/extra stdout or stdout
overflow must still fail with bounded diagnostics. Preserve the original probe
arguments, context/deadline and exact executable SHA checks.

Scheduled stage05 `TestPinnedCodexEphemeralProviderSelection` has **no version
probe**; its App Server already captures stderr to its private log. No source
change is required there. Keep its selected-provider/zero-wrong-provider and
strict0.163 tool assertions. The stage06 recovery harness environment and raw
native logs also remain unchanged. Do not globally replace unrelated
CombinedOutput calls used for firewall, namespace or command diagnostics.

Quick tests must use deterministic synthetic child output, not a native launch:
exact stdout+warning stderr passes and retains diagnostic; wrong/empty stdout
with correct version only on stderr fails; extra stdout fails; nonzero exit
with correct stdout fails; stdout overflow fails; oversized stderr stays bounded
and visibly truncated without hiding an otherwise valid stdout result. Cover
both expected versions and the helper used at both call sites. Compile the
affected tagged helpers in the pinned Go environment; do not rerun native work
as a quick-check workaround.

### Acceptance and sequencing

The unchanged native control, model/provider routing, exact catalog/native hash,
actual tool observation, lifecycle/cleanup, persistence and old/new state
assertions remain mandatory. The parser correction merely lets those gates run.
Retain stage00/01 pass evidence at its exact input identity; the lead chooses
proportionate reuse and a new guarded watcher attempt for remaining stages after
source/check/review disposition. No success for stage02-06 is inferred, and
no unrelated long campaign is added. If real helper/control/persistence checks
fail next, diagnose that evidence before any further change or rerun.

This is a substantive test-fixture correction, with no intended production-code
change. It creates a new client source SHA; do not call old/new source identical
or silently certify the new head using old receipts. Lead applies mandatory
review policy to the completed committed/quick-checked narrow diff. Owner1 then
refreshes the runtime's exact client source/Go sums and final vendor derivation
coherently; consumers select that final published runtime, keeping all unrelated
inputs and raw0.164/d2af bytes. Current published runtime5eb and configuration508
preparation are not the final build selection until this dependency chain settles.
Hold final builds/pin publication sequencing under the lead, retaining every
prior reviewed head, failure and input receipt. No native patch, deployment,
default integration, lifecycle or cleanup authority is supplied here.

## Native state fixture: bind bootstrap markers to returned thread identities

Status: diagnosis/design ready for lead disposition; **not an implementation or
rerun release**. Implementer0 owns the test correction after lead handoff. This
amendment changes no native/client production contract and does not supersede
the exact-version, real-control or persistence gates above.

The retained attempt is
`client-native-verification-preparation/attempt-8e36734-01/06-state-upgrade.log`,
at client `8e36734a5a5157e21f5719b2e52d6ba4686ec8d5`, tree
`459962e198d4ecdab9fd75b299c8850ff3ce2e48`. Lead reports runner9ef89f1a,
bindingsc67471f9, stages00-05 PASS and all137 source/native/tool guards PASS;
stage06 failed before its first synthetic inference. The corrected version
probes passed for both exact binaries and retained helper warnings. Old0.163
started PID869509 with its private socket ready, then the fixture stopped and
joined it. No native0.164 state transition or old-reader result was reached.

### Cause and evidence limits

At `codex/native_upgrade_integration_test.go:165`, the root/held loop passes
`"Synthetic native upgrade bootstrap " + target.name` to
`BootstrapHeadlessThread`. The caller-supplied marker therefore lacks the
returned native thread ID. `codex/headless.go:75-76` rejects this exact condition
before metadata lookup or `thread/inject_items`: the marker must be nonempty,
at most4096 bytes and contain the destination thread ID. The later fork call
at213 has the same defect: its literal also omits the **fork destination** ID.
Changing only the first root marker would leave held/fork preparation invalid.

The retained `/tmp/codex-native-upgrade-evidence-2425596117/assertions.json`
records root `01a174aa-e088-7d80-84da-00dd4727b746`, root project
`01a174aa-e076-7950-afc0-66dd3863284f`, providerHits0, and empty held/fork,
messages and send receipts. `StartThreadWithSettings` at `client.go:3588`
accepts that ID only after checking native thread/start's nonempty ID, cwd and
requested project. Thus native start returned usable identity; this failure is
an invalid fixture argument, not evidence of a native store/read, timing or
production bootstrap bug. No retry, sleep or timeout increase is justified.

Pinned0.163 source at
`/nix/store/9is267xl3palxb615kk86qlli9nggkf9-source/codex-rs` agrees with this
boundary: `app-server/src/request_processors/thread_processor.rs:1580-1660`
constructs the thread/project response; `request_processors/turn_processor.rs:994`
loads the requested thread and injects the supplied response items. Native does
not invent this application marker. The client injects one developer/input_text
item, then verifies exact destination/cwd/project or fork source and exactly one
matching session_meta and marker in the native rollout (`headless.go:85-172`).
Existing real-native examples in `headless_test.go:249,282` include their exact
destination IDs. Runtime `portal/internal/teamruntime/runtime.go:597` already
constructs its marker with threadID; it is outside this correction.

The evidence directory currently contains only assertions.json and native.log.
Read-only inspection found `/tmp/codex-recovery-2072790345` already absent;
`recovery_integration_test.go:251` registers ordinary harness-root removal.
No architect cleanup occurred. There is no retained rollout/SQLite snapshot for
this failed attempt, so do not claim observed old-store contents or recreate
them. Existing artifacts and attempt records remain unchanged. Source plus the
manifest establish the local refusal without a new diagnostic native command.

### Smallest correction and diagnostics

Keep edits in `codex/native_upgrade_integration_test.go`, plus narrowly related
test coverage if needed. Build each root/held marker from its actual returned
`id`, and the fork marker from `state.Fork`, for example
`Synthetic native upgrade bootstrap root (thread <exact-id>).` Retain root/held/
fork labels for diagnostics. Do not use the root ID as the fork destination;
retain `state.Root` separately as the expected source argument. Use the existing
public bootstrap methods unchanged. Do not relax the marker guard, replace
identity with nonempty/generic evidence, modify native state directly, inject
another history item on uncertainty, or substitute synthetic-only state proof.

Log the bounded fixture phase, role, destination ID, project/source ID, exact
synthetic marker and error on bootstrap failure. Retain those values with the
manifest so a future failure identifies its exact call before examining raw
state. A bounded failure diagnostic may call only public metadata/verification
reads for that known fixture thread within the existing deadline; a diagnostic
read failure must be recorded without masking the original failure. No new
injection, implicit resume or provider request is a diagnostic fallback.

For failures after native startup, retain the stopped fixture's private home
and client-receipt tree in the existing evidence directory before parent cleanup,
using this file's existing snapshot helper. Arrange this only after the owned
client/server have closed and the native process is joined; record snapshot
errors instead of treating partial output as complete. Do not change shared
recovery-harness cleanup, copy production/foreign paths, follow symlinks, or
alter the existing before-old-reader snapshot. This is per-attempt diagnostic
retention, not a new state migration or lifecycle mechanism.

### Checks, acceptance and dependency sequencing

Quick checks are deterministic: exercise the actual fixture marker preparation
for distinct root/held/fork IDs against existing fake-transport bootstrap
coverage, requiring the exact developer item and expected origin. Include the
old missing-ID literal as a refusal before any RPC, and ensure a source-only
fork marker is not accepted for the destination. Preserve the existing
lost-response/no-duplicate and large-inherited-history bootstrap checks. Compile
the tagged state fixture in the pinned Go environment; no native execution is
part of this quick package. The lead selects affected review under mandatory
review policy after the complete narrow test change is committed/quick-passed.

Actual stage06 acceptance remains unchanged: real0.163 creates native state and
completed user/assistant history against the private synthetic provider;
exact0.164 cold-reads identities/messages/receipts without implicit resume,
explicitly resumes only the root, adds a completed turn, forks with the exact
source relationship and survives restart. The held queue retains exact entries,
client IDs and order and stays unloaded/undispatched. Existing one-entry queue
equality is preservation evidence, not a new proof of all FIFO dispatch cases.
Preserve complete message/turn/item identity comparisons, exact reconciled send
receipts, provider hit counts, one-native-at-a-time stop/join, offline snapshots
and inventory. Old0.163's final isolated cold-reader phase must retain old/new
history and queue without inference, report file changes, and leave the
pre-probe0.164 snapshot intact. It proves neither old-version writes nor safe
downgrade/mixed-version operation; recovery remains forward-only. A further
native failure needs its own evidence-backed disposition, not relaxed assertions.

Stages00-05 at8e are valid retained results for their exact inputs. A change
limited to this state fixture and its diagnostics does not alter the passed
prompted/strict/provider production code, helper, catalogs, binaries or scenarios.
The lead may carry that evidence forward with an explicit old/new file-diff and
input-binding comparison; do not label the new head already tested or blindly
rerun the full batch. A fresh guarded watcher should run corrected stage06
after review, with refreshed exact-client bindings and the same raw native
identities, preserving all previous failed evidence. If shared helpers/product
source change, reassess the affected lanes instead.

This test-only correction still creates a new client SHA. Publish it before
coherently refreshing runtime source/Go sums/vendor identity and consumer pins;
hold final builds until that chain settles. No native/package behavior change,
production-state inspection, native patch, rollout, merge or cleanup is authorized
by this subsection. No additional diagnostic command is presently needed to
explain the failure; real storage/resume/fork acceptance remains unproved until
the corrected owned fixture runs.

## Fresh defaults rebase: preserve archive preparation and creation-lock fixes

Status: bounded assessment complete from settled immutable owner receipts;
preparation boundaries below are ready for the lead/owners. User authorization
covers feature rebases and ordinary conflict resolution, not default integration.
No architect source/Git/native/build/claim action occurred. Governing raw0.164,
prompted naming, capacity recovery and four-fix contracts remain unchanged.

### Exact ranges and actual incoming scope

| Repository / owner | Preserved feature comparison | Settled fresh default |
| --- | --- | --- |
| codex-web / implementer0 | `8b60554bc10c2a6bcbf9732a8b77ad959c317036..02533a152223416f159bac2578e88bcbe653f247` | `8b60554bc10c2a6bcbf9732a8b77ad959c317036` (unchanged) |
| dev-workspace / implementer1 | `9634151b9836311c331a58880fbb4c46133fd98f..5eb5bff620a302239179edb4736f0c2196d58437` | `b974f2f3f83792a494610d1ea03f3d69e97bc1a4` |
| configuration / implementer1 | `b167cd4388a5c94ff3f978df85b6800fafd1b8af..508ab4684c1c22e0f8d386353e6fcf87ce2dce63` | `6428e280f06bffabef829a1335b36bac6cad5b9d` |
| workspace / implementer0 | `0905143a3aa18c22a871f47afd76a47877bc32fb..7c3d482cf1000d5608e445b180467c968d9d1262` | `9c4c97cd1d49232cb930ff5037ae124295f04f0f` |

Evidence: `default-refresh/20261025-assessment/{runtime,configuration}/`
assessment-inputs, incoming diffs and rebase-assessment receipts;
`default-refresh/20261025T202809Z/` exact client/workspace inventories and
prepared-file snapshots. Old refs, bundles, reviewed/tested ranges and raw input
graphs remain retained. Workspace's former remote a6ebab6 differs from the
recorded review comparison base0905143; neither is invented as a new baseline.
Do not race moving refs or replace these identities with abbreviated guesses.

Client has **zero incoming commits**. Its fresh default does not contain source
801099; keep the existing imported643898 source unit once, with its recorded
mapping and later retry-proof corrections. The four feature units remain643898,
ccd2ce58 (prompted0.164), ab60a81b (capacity),02533a15 (state fixture).
02533a includes the completed marker correction; relative to passed8e36734,
only `codex/native_upgrade_integration_test.go` changes. Its quick-v2 receipt
reports compile/helpers and137 guards passed. No client conflict or native/API
change arises from this fetch, and no second801 import is needed.

Runtime incoming commits are e4f6180 (archive readiness before shutdown),
5e4e99df (durable lead-assisted archive preparation), a27fd38e (skip occupied
names before runtime EX locking), b974f2f3 (PLAN source wait before destination/
provider admission). Their29 changed paths overlap our feature in six files:
`docs/session-preparations.md`, `nix/workspace-portal.nix`,
`portal/internal/web/{browser_contract_test.cjs,static/app.js,templates/session.html}`,
and `test/creation_model.py`. They do not adopt the original five feature units
or the imported naming/capacity stream; retain those once on the new baseline.

Owner1's ordinary rebase finished cleanly at
`f8a282af7ceae26625366b0659ae3c43fe5d80a5`, tree
`c48b4b40ece8ca89bd70c907866df02562f23038`, with no manual resolutions.
Nine stable patch IDs match; the naming unit differs only in unchanged context
now containing upstream `item: repair_tool or {`. Added/deleted payloads match
for all ten units. Owner1's isolated incoming-diff reconstruction yields that
exact tree;23 nonoverlap upstream files equal b974 byte-for-byte. This proves
source composition, **not** unchanged overall behavior or final acceptance.
Original five literal SHAs are mapped predecessors, not literal ancestors of
the rebased head. The new default b974 and predecessor963 must remain literal
ancestors of the final runtime.

Configuration's sole incoming commit6428 changes only devWorkspace's three
locked identity values963→b974. Root ea188, Home Manager and all other nodes
remain equal. Owner1 has preserved/dropped the obsolete feature pin and now
holds a clean feature at6428 awaiting the final runtime. Workspace090..9c4 has
two tracking-only commits and one functional commit changing only flake.nix/
flake.lock to select b974. No foreign record contents were inspected. Extension
767dfd58, root nixpkgs and source filter are unchanged. Do not restore old b167,
090, a6, source-session consumer pins, or the dirty5eb/d0 preparation as final.

### Compatibility and resolution boundaries

Keep upstream archive readiness, its installed `workspace-archive-check.rb`,
native identity checks and final executor revalidation. The new schema1 JSON
sidecar under `archive-preparations` is persisted compatibility scope, although
there are no incoming SQL migration files or changed existing SQLite readers.
Preserve exact receipt/attempt/journal/target/thread matching; durable intent
before send; same-ID reconcile after uncertain delivery; cancellation/restart;
ordinary receipt parking for older packages; no locks held across repair turns;
and existing journal-bound recovery. Do not renumber/delete this upstream state,
introduce a second registry, claim downgrade safety, or interpret inherited
archive capability as authority to archive this session.

No incoming runtime flake/module/native/catalog/package contract changed.
There is no new native release or protocol selection to resolve. Archive
preparation is a new runtime consumer of existing normal Send/Reconcile APIs;
preserve those semantics and validate its literal request-corpus coverage on
the final client. It must not be routed through naming's private utility or the
browser buffer. Browser FIFO orders that browser's captured intents; it never
promises ordering against this server-owned repair workflow or another client.

In app.js/template/Node tests, retain archive phases, detail text, cancellation
and status actions alongside switches, visible-content unread, immutable FIFO
submissions, UNKNOWN holds/copy recovery and silent healthy queue refreshes.
Queue silence must not hide archive progress/errors. Keep lifecycle readiness
gates and exact send/steer/unsent rules; do not choose a whole ours/theirs file.
The automatic merge is subject to focused behavioral checks, not presumed safe
solely because contexts did not conflict.

Keep a27's occupied-name precheck and its repeat under creation/runtime locks;
custom collisions and unreadable/unknown occupancy still refuse. Keep b974's
exact PLAN source wait/revalidation **before** destination/provider admission
and existing journal recovery independent of the live source. These fixes are
relevant to prior PLAN/FORK lock refusals, but their presence does not prove
actual creation acceptance. Naming still resolves/retries within30 seconds,
then either reserves an accepted name or requires manual recovery; no generic
fallback or changed frozen destination/request identity.

The shared `test/creation_model.py` must keep our named SSE events, overload
counter, native-retry advice and request diagnostics together with upstream
URL query parsing and archive repair tool emission. Naming responses and archive
repair controls retain separate triggers. Preserve both test assertions rather
than making either scenario silently bypass its real native control. Packaging
keeps the new archive-check installation and final coherent vendor hash.

Merged SSH defaults and config/workspace input pins prove publication and
selection in canonical source. They do not prove actual deployment or release
use of b974. No new migration rewrite is needed or authorized; retain inherited
state and record actual deployment provenance as unknown until the lead's later
authoritative rollout preflight. Never infer it from a commit subject.

### Independent execution packages and final pins

Owner0 may complete/publish the already prepared client02533 after the lead's
narrow-fix/review disposition; no rebase delta exists. Owner1 owns final runtime
source/checks on b974, then the one consolidated source/Go sum/vendor update to
that published client. Preserve raw ea188/0.164/d2af and all unrelated inputs.
Do not retain a final d0 dependency or publish a half-aligned native/naming pair.

For the workspace's two dirty prepared pin files, first verify the saved exact
file bytes/hashes and current index/worktree inventory still match the owner's
receipt, with no unrecorded changes. Retain the old feature ref and snapshots.
Retire **only** that owned superseded two-file delta back to recorded7c3 contents
so ordinary feature rebase can proceed; do not reset/stash/clean the repository
or touch unrelated index/records. Since7c3 is solely an obsolete two-file pin,
drop that pin unit in the authorized rebase onto9c4 rather than replaying it over
new defaults. If an index/race discrepancy exists, stop and preserve it for the
lead. Keep the resulting feature at fresh9c4 until the final runtime is published.

Then owner0 writes only the direct nested runtime URL and runs the existing
scoped `nix flake update vpsfree-dev-workspace/dev-workspace`; owner1 selects the
same published runtime through configuration's existing dev-workspace/devWorkspace
confctl channel on6428. These consumer preparations may proceed independently
after the runtime handoff. Keep extension, follows paths and unrelated fresh
default nodes; inspect semantic graphs instead of copying old lockfiles. One
final pin stream per role replaces superseded consumer/preparation pins. Preserve
old source/input receipts, exact new heads and the deployment consistency check.

### Evidence reuse, affected review and verification order

Do not repeat the unchanged client's stages00-05 solely because the runtime
rebased. Bind their8e source range, native hashes/catalogs/toolchain/environment
and executed scenario files to02533; the sole state-fixture diff and no changed
shared initializer/helper support scoped reuse. The lead records that explicit
proof, not an assertion that02533 itself already ran those tests. Marker quick-v2
evidence transfers only to its exact committed source/inputs. Corrected stage06
remains required and unpassed, with all previous assertions and failures retained.

Runtime quick checks must cover the combined app.js/Node contracts and existing
four-fix/naming/capacity suites, plus upstream `TestArchivePreparation*`,
`TestSessionPreparationOccupiedConversationDoesNotBlockNameSelection`,
`TestAcceptedPlanWaitsForPortalConversationAndRevalidates` and
`TestAcceptedPlanJournalRecoveryDoesNotNeedSource`. Include affected team/archive
preflight and Ruby archive-check/creation-lock checks under existing pinned
runners, protocol call-site coverage and the final package/pin consistency
checks. Do not run native tests as quick checks or weaken original assertions.

The runtime baseline adds substantive lifecycle/state/creation behavior, so
review reuse is **not** certified solely by clean replay or reconstruction.
After all intended final changes are committed and quick checks pass, the same
independent reviewer covers affected general, architecture, scope and risk lanes:
combined browser/lifecycle behavior, archive sidecar/parking and normal delivery,
creation lock order, shared provider fixture, package installation, complete
feature history and consolidated pins. Reuse unaffected earlier conclusions
and client narrow-fix evidence explicitly; no unrelated review campaign.

After that disposition, fresh watchers run corrected client stage06 and the
affected runtime browser/creation/naming acceptance on exact final inputs.
Actual NEW/PLAN/FORK, retirement, naming retries/deadlines and managed-native
teardown remain gates. Include the existing packaged archive-lifecycle scenario
because its new repair flow shares the changed provider fixture and now consumes
raw0.164; this is an affected lane, not permission for unrelated host/VM suites.
Prepared editor/browser inputs still require matching generated review assets.
Schema/catalog/DeepSeek receipts may transfer only with exact unchanged raw
native/source/config proof; no blanket transfer of runtime package outputs.

Finally build the exact final composed workspace and system with normal retained
out-links/generation roots, record full inputs/store paths, and refresh the
idle-new-native preflight. No stale candidate is final after source/pin changes.
Machine ownership, live baseline checks, coordinated activation and forward
recovery remain with the lead; preparation supplies neither a claim bypass nor
merge approval. No consequential design ambiguity remains in the observed
incoming diff; unexpected later drift or a conflict outside these boundaries
returns to the lead before resolution.

## Vendor proof: distinguish requested rebuild from historical deriver metadata

Status: bounded methodology disposition ready for lead acceptance; owner1 owns
an evidence-only continuation after release. Preserve the original outer4015
failure, runner exit1, logs, guards, root and parent/watch receipts unchanged.
No application/hash/source change or second build is required by this finding.

Evidence in `runtime-final025/20261025-final/` binds the executed runner SHA256
`11681af277a2957601dfcac6377aef2c99320d3819e05cfe5f7b3baad9b1f27a`.
It runs realization and `nix build --rebuild` as consecutive simple commands
under `set -e`, then verifies the root and writes deriver.txt before asserting
historical deriver equality. Reaching that later file with this unchanged runner
supports **inferred return0 for both Nix commands**, not separately recorded
stage exits. The rebuild log (SHA256
`3adb781ce4f3b18101bb48817c7108c0394c7044ed5b85bcf1b6e7740df6f729`)
explicitly checks final2rxmlh, unpacks source995 and executes configure/build/
downloads/install with published client025. Installed Nix2.34.9 documents
`--rebuild` as rebuilding and comparing an existing output. An empty realization
log alone proves neither fresh execution nor failure.

Read-only queries confirm final
`/nix/store/2rxmlh30jdcicqybdf6h6didfdaavdwn-dev-workspace-0.2.0-go-modules.drv`
is in `--valid-derivers` for output
`/nix/store/lg6qgishdvazi9xz6giji5zhhjb4zzsg-dev-workspace-0.2.0-go-modules`,
and querying that final derivation's outputs returns lg6. Its declared recursive
SHA256 is `sha256-FxFVVTHhdpcPqDZFZfYOfAUnKIYmIdjr7u5dTixmHTQ=` and its source
is `/nix/store/995njbnm8jikcxcsfrn83cjkkblbwkqs-source`.
The existing owned root is a symlink resolving to lg6. Historical `--deriver`
still returns discoveryfa1, whose fake-hash declared output is wjhh, a different
path. Historical registration is not proof of which requested rebuild ran.
Do not require it to be rewritten. Valid-deriver membership alone is likewise
not execution proof; retain the command/log/control-flow evidence above.

The watcher statements “ten guards” and “no root” are contradicted by the11-entry
manifest and actual root inspection; record corrections without rewriting its
original report. The original script never reached SRI/content checks or its
final guard pass. Owner1 reports current read-only hash/module/content equality;
that diagnosis does not fabricate the absent original receipts or turn exit1
into a successful whole-run result.

The continuation must bind hashes of the original runner, logs, exit, deriver,
metadata, final derivation and11 frozen guards, then perform only:

1. Recheck those guards, root target, final valid-producer membership and exact
   final drv output/source/recursive-hash identity. Keep the historical deriver
   value visible as metadata, not a pass/fail equality requirement.
2. Execute the previously unreached `nix hash path --sri` comparison and existing
   guarded `verify-vendor-content.py`: exact22-module set/version, go.mod/go.sum
   source equality, selected025 module and go.mod sums, all52 vendored file
   identities/bytes against published cfjj025, no replacements/exclusions or
   unexpected inventory. Create the previously absent content receipts without
   overwriting evidence. Label them as continuation observations; the helper's
   “fresh vendor rebuild” wording refers to the combined retained proof, not a
   build performed by this continuation.
3. Repeat all11 final guards and record actual continuation command exits and
   final outcome in a new receipt, including that original Nix stage return0
   is inferred from frozen control flow. Do not synthesize old exit files.

Any changed/missing original binding, absent root/final derivation, invalid
producer/output/source relation, hash/content/module/sum mismatch or changed
guard fails this continuation. Diagnose the concrete discrepancy before another
execution. A new structured rebuild is needed only if the original execution
binding cannot be established, its log/control flow is incomplete, or new inputs
require fresh execution; the observed historical deriver mismatch alone is not
such a reason. Never delete/unregister/re-root store state to make metadata match.

If these checks pass, the combined evidence proves the requested final vendor
rebuild and matching dependency content with the stated receipt limitation.
It does not prove application/package/system builds, native state upgrade,
provider behavior or deployment acceptance. All existing review, native and
rollout gates remain separate and unchanged.

## Vendor proof retention: restore the exact missing inputs before continuing

Status: the initial restoration attempt subsequently failed after a partial
effect; see the root-proof correction below. Owner1 prepares the bounded repair,
with execution held for lead release. Preserve its unready continuation draft,
original exit1, missing-input inventory and failed restoration receipts; do not
create a continuation success or rewrite old guards to omit missing paths.

`vendor-missing-bindings-inventory.json` in the same final vendor packet has
SHA256 `98beb6c7454a4eba740d2d329be2469be6dbe3b7ddc0ae998514b0c3ac9f1d39`.
It records three missing paths: final derivation2rxmlh, filtered runtime
source995, and published client sourcecfjj025. All nine direct input derivations
and the two other direct source scripts remain present/hashable. Ten original
guards still match; the eleventh is the absent final .drv. Outputlg6 and its
owned root remain present, but valid-derivers now returns empty. This is not the
earlier positive observation; preserve both dated states. The cause of removal
is unproved. An output root does not by itself retain its producing derivation
or the sources needed for this proof.

The packet retains complete v4 derivation JSON and expected raw .drv SHA256
`17254ce1796ffcb1e5289d0616c90bbbcd81fd0d0d144a92ea78d55cb242c7a1`, but no raw
.drv/export/NAR backup. No exact historical evaluation argv was retained. The
known selector is the unchanged local runtime flake's
`packages.x86_64-linux.default.goModules`; the recipe below is a **new repair
command**, not a reconstructed execution receipt. Other locked source paths
are not established by the packet; do not claim that every source is cached.

### Minimal restoration and roots

1. Before mutation, bind the original runner/log/exit/JSON/metadata hashes and
   ten present guards, the owner's nine input-drv/two script hashes, exact
   runtime HEAD plus its five owned dependency edits, and the saved complete
   source/mode comparison. Preserve the frozen lock identities. Check only the
   finite paths needed by this packet/continuation, including its interpreter;
   do not scan the store. Reserve new, absent owner-local root/receipt names
   under this packet and refuse existing or ambiguous destinations. Keep the
   existing vendor-final-root untouched.
2. Restore the exact published client source from the already present canonical
   Git object02533 using a standard Nix local Git source fetch, with its locked
   NAR `sha256-f5AjJntJvsRGb8ocU6yGQOW+FYhK0TGoYzS3w4gSVbs=`. For example,
   evaluate `builtins.fetchTree` with `type = "git"`,
   `url = "file:///home/aither/workspace/ai/vpsfree.cz/repos/codex-web.git"`,
   exact full `rev = "02533a152223416f159bac2578e88bcbe653f247"` and that
   `narHash`. This is a bounded source-store addition, not a Git fetch/ref change
   or native build. Require its resulting path to be the recorded cfjj source
   and independently compare its NAR and canonical published content. A local
   fetch normalization mismatch must fail; do not accept a different tree or
   change the lock hash to accommodate it. Immediately retain that validated
   source with the standard non-derivation root operation in step5.
3. Reinstantiate the existing, unmodified final package's goModules selection
   from the frozen owned runtime with Nix's normal evaluator, rooting the
   derivation in the same operation. Concrete command shape, with a newly
   reserved absolute OWNER_DRV_ROOT:

   ```sh
   nix-instantiate --impure --indirect --add-root OWNER_DRV_ROOT \
     --option allow-import-from-derivation false \
     --option substitute false --option builders '' --expr '
       (builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-workspace-session-ui/dev-workspace").packages.x86_64-linux.default.goModules
     '
   ```

   This permits evaluation/source addition and derivation serialization only;
   never realize the .drv's outputs or use `--rebuild` here. Do not use the
   fake-hash override or edit source/locks. Prefer available cached sources.
   This evaluator can fetch missing flake sources even with substitution disabled;
   do not describe the command as network-free. If the lead releases such source
   restoration, limit it to cache misses for the inventory's eight frozen
   node/revision/NAR identities, recording each actual fetch/output. No moving-ref
   lookup, lock update, blanket refresh or output substitution is allowed. Without
   that bounded source-fetch release, first establish those cached sources or
   stop before evaluation. Source restoration supplies no application/native
   builder authority. Stop for any path outside the frozen graph or source that
   cannot match it. Disabling import from derivation prevents evaluation from
   launching an implicit build.
4. Require the returned/rooted .drv path to be **exactly2rxmlh**, its raw bytes
   to hash to17254ce, and `nix derivation show` JSON to equal the retained v4
   structure. Require src995, outputlg6, recursive Fx hash and every input
   dependency unchanged. The regenerated source must be exactly995 and match
   the preserved runtime source/mode inventory, including final module sums and
   pin check. Equality is a gate, not an expectation to repair by rewriting
   metadata. Missing/different results stop before continuation.
5. Keep the new derivation GC root for its dependency/source closure, and add
   separate standard roots for source995, clientcfjj and any required
   continuation tool not already retained. For an already validated **non-.drv**
   store path, `nix-store --add-root NEW_ABSOLUTE_ROOT --indirect --realise PATH
   --option substitute false` records a root without building; if the path is
   missing, refuse instead of fetching. Never use this form on the final .drv,
   which would request its outputs. Verify registration through the standard
   command and exact owned-link checks specified below, and separately verify
   the selected .drv reference closure. Do not query global root metadata.
   Record paths, commands, actual exits and hashes in a new restoration receipt.
   Keep existing regular JSON/log/guard evidence outside the store unchanged;
   no retention framework
   or manual store/database edits are needed.

The retained JSON alone cannot establish missing source bindings, so do not use
`nix derivation add` as a shortcut around source restoration. It remains an
ordinary supported metadata facility, not necessary for the preferred declared
recipe above. If re-instantiation cannot reproduce the expected identity, report
the exact differing field/path before choosing another method. Reconstruction
is possible in principle from retained source/lock identities; it is not yet
proved by an executed repair. Missing other cached source closures remain the
bounded preparation uncertainty.

### Root-proof correction after the partial restoration

This supersedes any requirement to use `nix-store --query --roots` to verify
registration. It is ready for lead acceptance; owner1 retains runner ownership
and must bind the corrected recipe before execution is released.

Outer 68600 returned CLI 0/runner 1 after the local source fetch returned 0: its
JSON result was a string and the parser attempted `result["outPath"]`. Retain
that stdout (SHA256
`6807e94c13af443276b327c1a8b8d4f9448ed285f764749893b5b60894d8303e`), failure and
partial-effect receipts. Owner1's reconciliation found cfjj with the exact
locked NAR and all 137 published file bytes, but 2r/995 still absent. Roots-v1
contains only the Python root; existing lg6/root is unchanged. The failed run
does not prove complete restoration. Preserve these paths and use new absent
result/root destinations. Revalidate present cfjj and root it without another
fetch. For any still-authorized missing-source fetch, explicitly project
`{ sourcePath = fetched.outPath; narHash = fetched.narHash; rev = fetched.rev; }`
before JSON serialization. Require exactly those three string fields and their
expected values; a string, missing/extra field or identity mismatch fails. Do
not accept top-level `outPath` coercion or substitute a parser fallback.

Owner1 also recorded that the diagnostic `nix-store --query --roots PYTHON`
printed broader root metadata and Nix pruned two stale automatic root links to
coordination notification outputs. No cleanup command was issued. Preserve the
receipt and actual incidental effect; it supplies no cleanup or lifecycle
authorization. Do not repeat this query or inspect those foreign roots.

The installed Nix2.34.9 `nix-store --realise --help`, `--add-root` section,
documents registration as a GC root, creation of the requested store-target
symlink and an automatic indirect link; it warns against moving root paths.
Use that standard command contract for the following bounded proof:

1. Require an absent, absolute root destination beneath the new owned packet
   directory and a valid, present exact non-.drv target. Preserve the earlier
   command forms and no-builder/substitution limits. The .drv remains rooted
   by `nix-instantiate --add-root`, never by realizing it as an output request.
2. Retain exact argv/tool identity, stdout, stderr and **actual zero exit** for
   each standard root operation. Then `lstat` the exact requested root, require
   a symlink, and check both `readlink` and resolution against the expected
   store target. Require the expected single result; unexpected numbered root
   results, warnings indicating failed registration, absent targets or any
   command/check failure stop the repair with its effects preserved.
3. Repeat the exact owned-link/target checks at final verification alongside
   the frozen input guards. The successful standard command plus matching link
   proves registration under Nix's documented behavior. It is not an independent
   audit of automatic links or the global root database. No global root query,
   root-directory scan, manually computed/written automatic link or store DB
   access is required. No optional registration-link inspection is needed.

Keep these root pathnames and targets unchanged through proof, handoff and
active rollout. A symlink alone, without its successful registration command,
is insufficient; an output root alone still does not prove producer retention.
This proof assumes ordinary Nix GC behavior and no later removal or relocation
of a root; it cannot promise retention against external mutation. Any later
missing target fails the next guard. Original forced-rebuild reuse, all 11
guards, source/derivation equality and the unreached content checks below remain
unchanged; this adjustment grants no build, native or deployment acceptance.

### Repeated client-source absence: conditional exact restoration

Status: bounded amendment ready for lead acceptance and owner1's new preparation
packet; execution remains held. This supersedes the preceding instruction to
require present cfjj without fetching it again. The root-proof method itself
is unchanged.

The owner's `vendor-restoration-v3-preparation-binding-loss.json` (SHA256
`e3dab7da99381e75a8e9b5975cb86b6e8d66ef79b98600fabc7e2e5c93d969b5`)
records cfjj absent again at 2026-10-25T21:36:51.615792Z, with 995/2r still
absent, Python root-v1 and lg6/root intact. All old 653 guards and 605 runtime
file bytes/modes matched before preparation stopped. No new manifest, guards,
ready receipt, root/result directory or restoration execution was created.
Preserve this observation and the earlier validated cfjj observation separately;
neither proves a removal cause or current source availability.

Preparation may describe cfjj as an explicitly missing restoration target,
binding the retained publication manifest and exact canonical Git object025,
locked NAR and expected path. Do not require missing store bytes to generate the
new packet, fabricate their current hashes, or alter the old guard files.
On the one released execution, check the exact selected path again:

- If present, retain it through the standard owned root operation and perform
  the full current NAR/137-file byte-and-mode checks; do not fetch it.
- If absent, permit one standard local `builtins.fetchTree` using only
  `file:///home/aither/workspace/ai/vpsfree.cz/repos/codex-web.git`, full revision
  `02533a152223416f159bac2578e88bcbe653f247` and locked NAR
  `sha256-f5AjJntJvsRGb8ocU6yGQOW+FYhK0TGoYzS3w4gSVbs=`. Require the strict
  three-string projection and exact cfjj path/NAR/revision. Then immediately
  root that valid, present non-.drv path using the new owned destination,
  before the independent NAR/content walk. This ordering also applies to the
  present-path branch: retention is not content acceptance. All independent
  integrity checks must pass before source consumption or final instantiation.

This is the same bounded local-source reconstruction as the original recipe,
now conditional on the new observed cache miss. It permits no remote Git
fetch, changed revision/NAR, lock update, output build or automatic retry loop.
If the path disappears between fetch/presence check and rooting, the standard
no-substitution root operation must fail; preserve partial effects and report
instead of fetching again within that invocation. Fresh absent root/result
names, recorded actual exits, exact owned-link checks and all later source,
derivation, 11-guard and content gates remain required. There is no claimed
atomic fetch-to-root guarantee or explanation for the disappearance. No global
root/store discovery, cleanup or new native/application acceptance is implied.

### Proof after repair

Run all11 original guards after restoration and again around the previously
specified evidence-only continuation. Requery valid-producer membership and
output/source/hash relations; do not reuse the now-stale query as a current
fact. Retain roots through proof, final input handoff and active rollout; no
cleanup is authorized here. A new disappearance or partial repair is a failure
with effects to reconcile, not a reason to delete/re-register the current output.

Exact path+raw SHA+full derivation/source equality restores the identity binding
to the original forced-rebuild log/control flow. Therefore its fresh execution
evidence may still transfer, with the explicit inferred-return0 limitation;
restoration itself is not a build. Finish the previously unreached SRI/module/
sum/52-file checks and record their actual new exits. Do not rebuild merely to
change historical registration or because the same metadata was absent. If
source/derivation identity cannot be reproduced or old execution evidence is
no longer bound, retained build reuse fails; the lead must assess the specific
gap before any new execution. Native/application/system acceptance remains
separate, with all existing gates held until their ordinary release.

## Targeted quick failures: correct two naming fixtures

Status: source-backed diagnosis complete; owner1's bounded test correction is
ready for lead acceptance before edits. No production change or diagnostic
execution is needed to explain these failures. Keep outer 69439, its CLI 0/
runner 1, all original logs, 745-entry manifest and selected source snapshots.
Pin, negative-pin and request-corpus stages passed; go-web failed and all later
stages were not run. The preguards passed; the final guards were not reached.
The go-web log SHA256 is
`117dc4d5934f470ae25c2546bff59936ea5c611bc2bfcd4dd7994049d97581ca`.
The tested range remains b974..f8a282af7ceae26625366b0659ae3c43fe5d80a5 plus the
five frozen final025 dependency inputs, not a new completed runtime head.

### Causes and preserved behavior

`creation_contention_test.go:41` is unchanged from b974. It installs
`normalSessionName` with a missing socket and no model catalog. In b974 that
adapter returned `errSessionNamingFallback`; the old naming worker substituted
`development-session`. The accepted source takeover removed that fallback.
Current `session_namer.go:42` returns `ErrEphemeralServer` for the empty catalog
before creating a client, and `namePreparation` correctly records utility_error
and stops before reservation. Thus the automatic subcase never reaches the
occupied-name precheck. Its observed failure does not establish a lock-order
regression. The custom subcase passes because it does not call naming.

`session_namer_test.go:179` requests `os.Mkdir(..., 0755)` but does not establish
the actual mode. The exact executed runner (SHA256
`28165bc2d276313002d4fe2d2fba787d7c8165f41a412af5c6e78b663f14bc27`) sets
`umask 077` before both its outer and inner stages. No runtime Go test changes
that mask. Under that setup the requested directory is created as `0700`, which
`modelSessionName` is required to accept. The current adapter checks the naming
root with Lstat and exact `0700` before creating scratch/calling the client; the
lifecycle store's mode repair applies to its parent, not that root. The mock
call is consistent with valid private state, not evidence that an actual `0755`
root bypassed refusal. This is source/control-flow evidence; no surviving
per-test directory mode observation is claimed. The other three unsafe-state
subcases passed.

### Owner1 implementation boundary

Limit application-repository edits to these two tests and their explanatory
comments. Keep the final five dependency edits unchanged. Any production,
package, runner-environment or other-file correction returns to the lead.

- In `portal/internal/web/creation_contention_test.go`, inject the existing
  `Config.SessionNamer` test boundary with valid JSON
  `{"name":"development-session"}`. Remove the missing-socket/normal-adapter
  setup from this successful-name collision fixture. Retain the actual portal
  queue/reconcile shared runtime lock and inode check, automatic `-2` suffix,
  attempt 1, handoff, accepted input and same-receipt replay. Assert the automatic
  base/outcome came from the injected model result, with one call and no extra
  call on replay; the custom collision must still refuse with no naming call.
  Count asynchronous calls safely. Describe generated-name collision selection,
  not a fallback. Existing unavailable-socket/error tests continue to require
  stopped preparation and no generic name.
- In `portal/internal/web/session_namer_test.go`, explicitly chmod only the
  owned `session-naming` test directory to `0755` after creation, check errors,
  and Lstat/assert the actual directory mode before invoking the adapter.
  Keep the never-call mock and `ErrEphemeralIsolation` assertion. Check that
  refusal leaves that mode unchanged. Preserve the other unsafe cases and the
  existing `0700` positive fixture. Do not change the process-global umask, runner
  mask, production check, or expectation to accept an unexpected client call.

These fixes preserve archive-preparation schema 1, occupied-name precheck and
its locked recheck, PLAN source waiting, SQLite/lifecycle contracts, prompt-only
raw 0.164 naming, shared retry proof, private paths, the 30-second budget/two slots,
two-call cap, output validation and manual recovery. Existing product docs
already describe these contracts correctly; no product-doc change is needed.
The fixture comments should explain the independent naming stub and explicit
permission setup.

### Verification, exact inputs and review

Owner1 uses the existing pinned environment and unchanged restricted runner
setup. Rerun the existing go-web selection on the corrected final source under
umask `077`; this includes both failures and the retained naming/error/creation/
archive/PLAN assertions. Also run the unsafe-state test alone in a separate
child shell with umask `022` to prove the fixture sets its intended mode under
both masks; do not mutate a running Go process's mask. Then execute the later
previously unrun targeted stages. Use fresh result paths and guards; no retry
of the old frozen packet. Prior pin/corpus results can be retained only with
unchanged relevant inputs/tool identities. No new client/native repetition is
justified by these two test edits.

The package uses `src = self` and `buildGoModule` inherits that source, including
these tests. Consequently old 995/2r and their successful vendor proof remain
historical after edits; do not relabel them as the final source/derivation.
Owner1 must bind the new complete source, source delta, final goModules
derivation and retained roots, with all module/pin/vendor inputs demonstrably
unchanged. Keep Fx only after verifying the expected output/hash/content; no
hash-discovery build or manual metadata adjustment is needed. The existing
fresh-final-dependency requirement applies to the new requested derivation:
prepare one explicit forced-rebuild verification for the parent's watcher
release, record actual command exits, and use valid-producer/output/source
relations rather than historical registered-deriver equality. Preserve old
receipts and both root sets. This paragraph does not itself launch/release
evaluation, rooting or a build.

After final quick checks and commits, include both fixture corrections and
their causes in the already-required affected runtime review (general,
architecture, scope and risk for the combined b974 integration). Bind the whole
final history, five coherent input changes and new source/derivation; these are
test changes, not a mechanical-pin review exemption. Reuse unaffected client025
and exact-native evidence explicitly. Existing post-review stage06, runtime
creation/naming/archive acceptance and final-output/deployment gates remain;
this diagnosis supplies no acceptance, activation or default integration.

## Installed dev-session drift after final source binding

Status: bounded disposition ready for lead acceptance. Accept outer 83971 as
completed source evaluation/rooting under its historical tool identity, with
a separate current-tool drift assessment. This does not certify unchanged
current tools, a vendor rebuild, quick checks or final deployment. Owner1 may
prepare the new quick/rebuild tool bindings only after the lead reads this
disposition; no application or installed-tool change belongs to this package.

### Exact change and timing evidence

The original manifest resolves `/home/aither/bin/dev-session` to
`/nix/store/bhi44p5ifayn90b8bnm1g5srdga46yn1-dev-workspace-0.2.0/bin/dev-session`,
SHA256 `1c63cab393129148833bee5743ad409dc189d0e3df9a0ffb8d48488f31d7fcd2`.
That immutable old wrapper still has those bytes. The same home command is a
symlink through `/home/aither/.local/state/dev-workspaces/profile/bin/dev-session`;
it now resolves to
`/nix/store/fqajxhsmaqg44pl8x2xshgn8q0bl7wr2-dev-workspace-0.2.0/bin/dev-session`,
SHA256 `f2f07c46fc093b3d3c918f24eaf030a485b37b503509f5e20b5a1994573cc418`.
The current profile points through `profile-191-link` to fqaj. The visible
wrapper and intermediate shell wrappers differ only in their exact package
paths. Do not replace either hash with normalized bytes or claim the packages
are globally equivalent.

The delegated Ruby host script is byte-identical, as is the runtime contract.
The packaged private dev-session script differs only by the canonical source
changes in `2a58cf4937d035dd8688aaae92d9e997c3efdb63` (worktree registration waits
for shared readers) and `960dd816b7e56cbdd4af0da15bf0b26257775151` (cold resume
maps typed lock contention to temporary recovery). Its old body matches b974
and current body matches 960dd, apart from the packaged Ruby shebang. The other
32 files in the two entry scripts' literal `require_relative` closure match.
The `run_current`/`current`/`current_slug` logic, environment/workspace identity
validation and host dispatch have not changed. Extension catalog entries retain
their names/roles but have changed source/package paths; no extension action is
called by the binder. This is a bounded command-path assessment, not a complete
package/release or live native assessment. No foreign records were read.

Frozen binder SHA256
`ab6446ecaf33131a57d5c2cccd251df1e2ea9e4ba60f3f989f9580463e39ccd3` calls
`dev-session current` once at entry, checks all 1699 guards before evaluation,
checks tool resolution, then checks all 1699 guards again before writing PASS.
Its actual exit 0/PASS therefore establishes both historical guard passes by
control flow; individual guard timestamps were not recorded. Binding receipt
SHA256 `46a682a188e66aca4f6d11d544c5dd83fd153d32b7f221ff9cc4936ed79659c6`
has mtime 2026-10-25T22:21:32.372555Z; evaluation.exit follows at
22:21:32.373774Z and watcher result at 22:21:36.008574Z. The current profile and
profile-191-link have mtime/ctime 22:21:52.056659Z. These observations support a
profile change after completion. They do not identify its actor, authorization
or exact process-level execution history; no private lifecycle records or
global scans are required to infer a cause.

The parent subsequently found exactly one mismatch in 1699 guards (the home
alias), and the same sole mismatch in the corrected quick packet's 1720 guards.
All 605 current worktree and gg30 source bytes/modes, raw gw45 SHA256
`10e8f8ba47f70e3991bc8c669108637dde932eb72b4b52bd7c0e5f62801de791`, full
source-only derivation comparison, both roots and 13 actual stage exits were
independently rechecked by the parent and passed. Retain those current checks
alongside the historical PASS. The current session/environment binding matches;
the parent also confirmed unchanged full_access and Luna/low/max1 watcher
policy. There is no remaining demonstrated source-binding failure requiring
another instantiation or re-rooting.

### Owner1 packet correction and limits

Keep the original 1699/1720 manifests, ready records, binder, PASS receipt and
all earlier attempts unchanged. The lead's new parent assessment must record
the historical success, later single alias drift, both exact identities and
current source/root checks; it must not report that the old manifest currently
passes. Owner1's new packets reference that assessment and the original binding.

For forthcoming quick/rebuild preparation, make an explicit manifest delta:
replace only the executable binding for the exact home alias with the freshly
observed fqaj path/hash, add its immutable wrapper/private-script identities,
and bind any deliberately edited runner/ready metadata with new hashes. Keep
the old bhi store-path hash as historical evidence. Preserve every other source,
dependency, expected output and tool binding; unrelated drift stops preparation.
Do not globally refresh expected hashes or delete the alias guard. Use new
packet/ready names and fresh execution results, without editing the old binder.

Before invoking `current`, each new runner must check the complete environment
pair, expected command selection, resolved store path and exact wrapper hash.
Invoke the explicitly bound current wrapper and record returned slug/exit with
the tool identity in the ordinary outcome. Retain the installed generation
checks; never pin the old wrapper to bypass a newer profile. Check the home
alias's resolution/hash and all other guards again at the end. Another change
must stop acceptance and be assessed from its actual timing/effects, not trigger
an automatic retry or a tool update. This is a few runner/manifest changes, not
a new tool-resolution or retention framework.

No new evaluation or content rebuild is needed merely to reconcile this alias.
The already-required one fresh gw45 vendor rebuild and corrected quick campaign
remain pending their normal parent releases; no client/native checks are added.
This command-path disposition also does not authorize deploying b974-derived
code over newer merged behavior. The observed current CLI contains the two
later canonical fixes above; preserving merged/deployed behavior remains part
of the lead's final baseline/rollout assessment, separate from source-proof reuse.
No cause, source change, full-package equivalence, default integration, claim or
lifecycle authority is inferred from the profile observation.

## Preserve the second moved default: runtime 960dd and downstream selectors

Status: COMPLETE preservation and execution brief for lead disposition. The
user already authorized rebasing while preserving existing changes. Owner1 owns
runtime/configuration composition; owner0 owns the workspace baseline and later
consumer pin. Lead releases their bounded operations from this written brief.
There is no new user approval gate. This subsection supersedes launching the
historical gw45 rebuild or the tool-only corrected-quick successor: first compose
the final source, then bind and verify that source. Existing receipts and roots
remain intact. Architect performed source/evidence inspection and this design
update only; no rebase, test, evaluation, build or native execution is claimed.

### Immutable inputs and compatibility conclusion

Use `runtime-moved-defaults/20261025T223325Z/assessment.md` (SHA256
`ba26d639aed6aec1a2440904d6003070a7d59bfea90a48783bea218c860a7926`) and its
718-file `packet-sha256.json` (SHA256
`f78a444ffcecfa682bdf7405cae709396456cec818bf28a464b41d8a2e586ea5`). The
parent verified all packet entries. Its pre-SSH snapshots preserve both raw
indexes, complete owned histories/bundles, all 605 runtime files, all 472 config
files and prior evidence. Post-inventory HEAD/index/bytes/modes still match.
Owner0's `default-refresh/20261025T223228Z-readonly/` inventory SHA256
`e22bd20cf7acd66ff6ae62ffa3b57c1fa405b55590d5d96812def22562593158` and manifest
`b03570465fbfac61e5b9a799528eb5f8a078828f55dbc6d19ef0d8f8bcbdd29e` bind the
unchanged client and the workspace selector. References below are exact Git
objects, not moving remote aliases.

| Repository | Preserved current input | Fresh canonical default / disposition |
| --- | --- | --- |
| codex-web | `02533a152223416f159bac2578e88bcbe653f247`, tree `8080b79d073c258611b165a0a5b01fdbcb3aea4c`, clean and published | Default remains `8b60554bc10c2a6bcbf9732a8b77ad959c317036`; no source rebase or new client publication |
| dev-workspace | Base `b974f2f3f83792a494610d1ea03f3d69e97bc1a4`, head `f8a282af7ceae26625366b0659ae3c43fe5d80a5`, plus exactly seven saved dirty paths | Rebase the ten feature commits onto `960dd816b7e56cbdd4af0da15bf0b26257775151`, then restore the seven files |
| configuration | Clean zero-suffix `6428e280f06bffabef829a1335b36bac6cad5b9d` | Advance to `270d348a29a832e552a798ba8bb467152a2d36d6`; later select the final published runtime through its existing channel |
| workspace feature | Clean zero-suffix `9c4c97cd1d49232cb930ff5037ae124295f04f0f` | Advance to `3e72f394a73c33be71fcdc1313d05cc74abb802f`; later update only the existing nested runtime selection |

Runtime incoming commits are `2a58cf4937d035dd8688aaae92d9e997c3efdb63`,
`b75a6a1065449743b6a3c2f859b44bc32fefdc40`,
`78077b0e47bb21571c99ca70b854b6ccca2f7682`,
`4fc8ba11412d22f853764a5f3d5546b540a1f9e3`, and
`960dd816b7e56cbdd4af0da15bf0b26257775151`. They change 19 paths, with four
complete-feature overlaps and zero seven-file overlaps. Preserve these effects:

- Registration alone may wait for shared portal readers after a nonblocking
  shared-lock probe. An active exclusive writer still refuses; validation and
  mutation remain under the original exclusive lock/inode. Do not generalize
  the wait to other session actions or change occupied-name/PLAN admission.
- Archive Retry compares `kind`, `receiptId`, `state`, `phase`, `code`, `options`
  and `currentTarget` across the asynchronous journal/details read. Equivalent
  diagnostic/timestamp refreshes may proceed; changed authority or canceled
  reads must stop the retry. Keep the ordinary request and receipt identities.
- `NewContext` passes startup cancellation through retention, preparation
  reconciliation and compaction; `New` remains the Background-context adapter.
  A stopped initializing service must leave transition admission promptly.
  Operational workers keep their independent context: `Close` parks archive
  preparation before cancelling those workers. Cancellation must not turn
  accepted attachments into failed ownership records or bypass admission.
- Cold resume translates only typed `SessionBusyError` to existing temporary
  recovery/exit 75 and backoff. Preserve permanent identity/lifecycle/malformed
  refusals, lock admission, same retained thread and untouched state while busy.
- The native worktree fixture now establishes ordinary manifest scope before
  starting. Preserve production refusal of manifestless retained state.

No incoming SQL/migration, schema version, serialized record, module, flake
graph, catalog, raw-native selection or package-expression change is present.
This is nevertheless substantive cancellation/lock/browser behavior, so source
composition is not a package-equivalence claim. Retain archive-preparation
schema 1, parking/recovery, SQLite readers, original four UI fixes, full naming
takeover, capacity continuation, private cleanup proof and the client025 marker
fixture. Prompted naming remains raw 0.164/d2af with tools potentially available,
30 seconds including queue/cleanup, two slots/two calls, strict output checks and
manual recovery. Strict reusable utility support remains 0.163. No native patch.

Canonical ancestry and the two new downstream defaults prove merged source and
selection of runtime960dd with NAR
`sha256-yQnkYdToCk8gzhLRVl+psiRthpI77ndaJL38PoIL+BQ=`. The separate current
CLI inspection proves only its documented command path. Full deployed graph,
activation and machine provenance are not inferred. Preserve every new default
behavior even where deployment provenance is unavailable; do not inspect
foreign records to fill that gap. No downgrade/state-reader support follows
from the absence of a new migration; existing forward recovery remains required.

### Owner1 composition and the four conflict boundaries

1. Before mutation, recheck exact f8a HEAD, empty staged delta, raw index and
   all saved bytes/modes against the packet. Account for any untracked paths;
   unexpected changes stop this route. Verify the retained refs/bundles and
   immutable snapshot before temporarily removing any owned working delta.
2. Restore **only** these seven tracked working paths from f8a, leaving the
   index and every unrelated path alone: `flake.nix`, `flake.lock`,
   `portal/go.mod`, `portal/go.sum`, `nix/workspace-portal.nix`,
   `portal/internal/web/creation_contention_test.go`, and
   `portal/internal/web/session_namer_test.go`. Use the ordinary path-scoped
   working-tree restore, never repository-wide reset/clean/stash. The snapshots
   are the authoritative saved bytes; this is temporary removal for rebase,
   not abandonment. Verify the expected clean tracked state before continuing.
3. Rebase the exact b974..f8a ten-commit suffix onto exact960dd in the owned
   runtime worktree, with autostash disabled. Do not replay upstream's five
   commits as new feature commits. Resolve only the four boundaries below;
   any unexpected conflict, changed preserved input or behavior returns to the
   lead before further resolution. Preserve the paused state/evidence on failure.
4. Restore the seven saved working files with their exact bytes and modes,
   after proving their pre-restoration rebased blobs still equal f8a's blobs.
   This proof prevents a saved full-file copy from hiding an unexpected upstream
   edit. Match `seven-owned-paths.json` SHA256
   `7688be6582190673c254ed34b13bcde804ec86d4f0c50ca93bb1f92c10d7f1ff` for every
   file. Both fixture fixes and all five final025 dependency inputs must survive.
5. Record old/new ranges, all ten commit mappings, patch IDs/range-diff and
   exact manual-resolution hunks. Reconstruct the intended combined tree from
   preserved f8a plus incoming patches and the explicit conflict resolution in
   an isolated index, then compare to the rebase; compare the restored seven
   separately. All 15 incoming nonoverlap paths must equal960dd byte/mode-wise.
   All paths outside the declared incoming/restored/resolution sets must retain
   f8a bytes/modes. Do not label the diagnostics adaptation patch-identical.

The exact conflict resolutions are:

| File | Required composition |
| --- | --- |
| `test/archive_lifecycle_browser.cjs` | Keep our bounded, sanitized structured failure diagnostics and timeout. Add `#lifecycle-operation-retry` to their existing `document.querySelectorAll` control selector so Retry appears in the bounded id/tag/hidden/open/disabled projection. Do not restore incoming's old `outerHTML` block or expose response bodies. This is the concrete shared hunk. |
| `portal/internal/web/static/app.js` | Retain the incoming `lifecycleRetryState` and semantic snapshot comparison unchanged alongside the feature's separate composer/unread/queue/switch behavior. No consolidation of archive Retry with message or capacity retry owners. |
| `portal/internal/web/preparation_test.go` | Preserve both existing reconciliation calls' new `server.operationContext` argument and our 30-second/no-fallback/attachment-only naming assertions. Do not substitute startup cancellation into operational work. |
| `docs/workspace-portal.md` | Combine new startup/Close ordering and exit75 recovery paragraphs with the feature's browser, naming and diagnostic contracts. Retain forward-only package recovery; no old naming fallback or isolation promise. |

After the final tree is proved, fold the five final025 input edits into the
existing logical runtime naming/native update (currently6df324a5), rather than
publish another intermediate pin stream. Fold the diagnostics resolution into
its owning feature unit. Keep the two fixture corrections as one focused test
unit or fold them into their owning naming unit with a recorded mapping. Retain
old refs/bundles and original source529/source801 import evidence; no source
import became a new literal ancestor merely because runtime default moved.
Do not duplicate those source deltas. Final whole-history review includes the
new mappings and single final dependency stream. No source further changes
after final binding without a new delta and affected checks.

### Independent consumer package

Owner1 may advance its clean zero-suffix configuration feature to exact270d;
owner0 may advance its clean zero-suffix workspace feature to exact3e72 after
lead release. These are baseline-only fast-forwards, with before/after cleanliness
and ancestry evidence. Preserve obsolete published feature refs as evidence;
do not replay old063/508/7c3/5eb/d0 selectors. Shared workspace masteref1 and its
archive-tracking-only suffix stay untouched; no foreign record content is needed.

Only after final runtime review/publication select that exact runtime in both
consumers: configuration's existing confctl devWorkspace channel and workspace's
existing `vpsfree-dev-workspace/dev-workspace` nested input. Keep all unrelated
nodes, follows, extension767, root nixpkgsd58, configuration root EA/HM/retention
and source filtering. Account explicitly for the final runtime's authorized
025/EA transitive changes; do not copy a whole old lock or invent a top-level
runtime input. Match both effective runtime selections and run the existing
deployment consistency check. Fresh source drift before publication is assessed
from a new exact range rather than silently pinning an older baseline.

### Final source proof, checks and review sequence

Historical outer83971/gw45/gg30 source proof, old forced rebuild, failures and
tool-drift receipts remain valid for their recorded inputs. They cannot certify
this new runtime source. The unrun corrected quick packet must not execute or
receive replacement expected hashes. Prepare new source/derivation/root and
quick packets after composition, recording the exact baseline, full source
inventory (not a hard-coded 605 count), final input graph and source delta.
Rebind current installed wrapper/alias identities using the preceding section's
pre-invocation and final checks; no globally refreshed guard list or old-wrapper
generation bypass. Unexpected unrelated drift stops acceptance.

The module set, published025 source, checksums and vendorHash are unchanged.
Keep Fx only with actual source/output/content proof. Evaluate and root the new
requested goModules derivation through the existing declared recipe, then run
the already-required **one final-source forced dependency rebuild** under the
lead's watcher release. Do not build gw45 first or repeat fake-hash discovery.
Record actual stage exits and bind requested derivation, raw hash, source,
valid-producer membership, output SRI, 22 modules and the 52 vendored file
comparison. Use standard owned add-root receipts and exact symlinks; no broad
root query, manual store metadata changes, old-root removal or output deletion.
Any identity/content mismatch is a new concrete failure, not an automatic retry.

Quick verification uses the declared pinned environment, absent private provider
catalog, disposable sockets/state and unchanged no-native opt-ins. Carry forward
the corrected packet's unrun stages and coverage assertions into a new packet;
run the corrected Go web selection under077 and unsafe-state case separately
under022. Retain naming/capacity/retirement, archive readiness, PLAN/source locks,
browser unit contracts, fixture diagnostics and syntax checks. Add these affected
baseline checks using the existing tests, with explicit root/subcase coverage:

- Go web: `TestWorktreeRegistrationDistinguishesPortalReadersFromWriters`,
  `TestStartupContextLeavesWorkerShutdownToClose`,
  `TestStartupCancellationPreservesAcceptedAttachments`, and
  `TestSessionPreparationPublishedAdmissionConfirmationDispatchesOnce`.
- Go command: `TestServeStopsWhileStartupWaitsForPackageTransition`, exercising
  its actual owned subprocess and transition inode. Its helper test's skip is
  not independent coverage. Preserve the existing naming-child/compile checks.
- Ruby ordinary readiness: existing
  `test_cold_resume_retries_lock_contention_without_changing_retained_identity`
  plus retained permanent-refusal coverage. The native tmux test remains a later
  native check; do not turn its scoped manifest setup into a quick live action.
- Syntax/contract checks cover the combined archive diagnostics and app.js.
  Actual equivalent-refresh/replacement-receipt Chromium and Firefox cases in
  `archive_failure_browser_test.cjs` run after committed final review, alongside
  the already-required affected creation/naming/archive acceptance.

Known bounded non-native checks may run inline; uncertain or longer verification
uses the existing fresh watcher policy. Do not broaden or repeat successful
unaffected suites solely because a commit ID changed. Conversely, old runtime
checks do not prove the new startup/worker lifetime or retry authority behavior.
Bind each reuse to its real source/tool/input scope and report unrun stages.

After quick passes and all intended commits, the same retained reviewer receives
the final runtime whole range/history, explicit overlap resolution, test fixes,
source/derivation and consumer graph. General, architecture, scope and risk lanes
are affected by substantive startup cancellation, worker separation, archive
semantic identity and lock/recovery behavior; no pre-completion source review is
requested. Existing client025 review remains scoped to unchanged client source.
Raw d2af native, catalogs/schema and earlier8e stages00–05 may transfer only where
the existing exact scenario/runner/native/control/persistence input proof still
holds; this does not create a blanket025 or new-runtime native PASS. Corrected
client stage06 still requires real thread/message/receipt/FIFO/cold-read/resume/
fork/restart/offline-old-reader acceptance. Fail rather than infer downgrade
support. No client/provider/native repetition is added solely by these defaults.

Sequence: compose/prove final tree and coherent025 inputs; prepare new binding
and final dependency proof plus quick checks; commit/consolidate and affected
review; publish final runtime; prepare matched consumers and run postreview
native/affected runtime acceptance; build exact final outputs and verify the
deployment graph before activation. Consumer preparation may precede completed
stage06 after the lead's release; acceptance is still required before use.
Keep original mandatory packaged creation/archive and recovery gates. These
operations do not authorize default integration, machine/session lifecycle
changes or any production/foreign-state fixture. No installed package is changed
by this design. Lead retains rollout and readiness decisions.

## Ruby quick continuation through the existing aggregate loaders

Status: COMPLETE bounded method disposition for lead release. Correct only the
session-owned verification invocation/coverage packet, not application or test
source. Owner1 prepares a fresh Ruby-only continuation after lead acceptance;
the parent retains execution/watcher ownership. No test, Ruby require, Nix
operation, source/Git edit or vendor observation was performed by architect.

### Cause and retained evidence

Owner1's `runtime-second-default-final/20261025-final/ruby-loader-diagnosis-v1/`
contains `diagnosis.md` SHA256
`f872d6354c88bd0ddacf4603a71e445e09af46bcfe64baad5d9462e59a0bf583` and
`diagnosis.json` SHA256
`92d8bda2082e2a62f10818dad10a47295b887c8f21f4763bd117968c3005393e`.
Architect read the actual first Ruby failure, aggregate loaders, shard wrapper,
Nix recipe and support boundaries, and matched the nine audited source hashes
and eight selected-fragment hashes. The JSON binds all 42 exact method
identities and proposed argument vectors; it is the selection authority for
this continuation, not a request to discover a broader suite.

Outer89334 actually reached `ruby-archive-check` and failed with 6 runs,
0 assertions, 0 failures, 6 errors and 0 skips. That individual file is a
fragment of `test/dev_session_test.rb`: common support does not load sibling
definitions `NullTmux`/`ManagedTmux` from `lifecycle_commands_test.rb` or
`with_archive_cleanup_fixture` from `archive_cleanup_test.rb`. Similarly,
workspace-host recovery's common helper needs `TransitionHost` supplied by
`suspension_test.rb`, which its aggregate loads. The errors establish an invalid
standalone quick invocation; they do not establish a production defect or a
passing production behavior. Do not make fragments independently runnable by
changing source or copying helper definitions.

`nix/ruby-checks.nix` uses the declared aggregates through
`test/run_ruby_suite.rb`. That wrapper computes its whole-shard selection,
appends its own `--name` filter and validates complete shard coverage. Passing
our bounded filter to it would conflict with that contract. Direct invocation
of the existing aggregate with Minitest's full-identity filter supplies the
same fixture bootstrap while selecting only the already-required methods.

Keep the original exit1, all logs, watcher prose and
`parent-quick-partial-assessment.json` unchanged. Actual node-browser/node-paging
exits are both0; the contrary watcher prose remains preserved with its parent
correction. The six successful Go stages have respective root/leaf counts
49/110, 1/4, 4/115, 7/28, 6/14 and 1/1; the 68/272 sums include the separate
unsafe022 repetition and are not unique aggregate coverage. Tagged compilation
intentionally ran zero tests; Node browser recorded29 cases plus composer, and
paging passed. The parent independently matched all1807 inputs and608 source
bytes/modes after failure. The old runner's final guards were not reached;
the parent check is separate evidence, not a fabricated stage exit.

### Owner1 packet boundary and exact acceptance

Prepare new runner, selection/coverage metadata, guards and result names under
the same owned evidence directory. Do not overwrite the old runner or receipts.
The only invocation change is, for each existing Ruby stage, its aggregate
entrypoint plus `--verbose --name` and the JSON's exact anchored full
`Class#test_method` alternatives (`/\A(?:identity|...)\z/`). Pass the filter as
one literal argument, with no shell evaluation or additional shard filter.
Keep one process and result pair per existing stage:

| Stage | Aggregate | Exact runs |
| --- | --- | ---: |
| ruby-archive-check | `test/dev_session_test.rb` | 6 |
| ruby-archive-retirement | `test/dev_session_test.rb` | 4 |
| ruby-archive-recovery | `test/workspace_host_test.rb` | 17 |
| ruby-archive-exact-receipt | `test/dev_session_test.rb` | 1 |
| ruby-creation-locks | `test/dev_session_test.rb` | 7 |
| ruby-plan-journal | `test/dev_session_test.rb` | 2 |
| ruby-fork-lock | `test/dev_session_test.rb` | 1 |
| ruby-ordinary-readiness | `test/dev_session_test.rb` | 4 |

Extend only the session packet's existing Ruby coverage check to require the
complete expected full-identity set, with each identity occurring once as an
actual verbose test-result record. Do not count identities merely echoed in
the command/filter. Reject missing, duplicate, unexpected or malformed result
records. Require actual process exit0, one final Minitest summary, exact runs
from the table, a positive actual assertion count, and zero failures/errors/
skips. Record the assertion count actually observed; no exact assertion total
has been measured yet and none is invented. Preserve source-controlled loops
and cases without manufacturing separate subcase receipts. This is a bounded
packet-checker adaptation, not a repository test reporter or new harness.

Run only those eight Ruby stages and the previously unrun diagnostic, syntax,
whitespace and final-guard stages. Preserve the declared Nix environment,
umask077, disposable state/socket/provider configuration, real-tmux exclusion
and absent native/live opt-ins. Loading the aggregates is not permission to
execute their unselected native/live tests. Retain existing stop-on-failure and
stage-exit recording, explicit source/mode and current-tool checks before and
after, and no-clobber results. A bootstrap/filter/coverage failure stops the
continuation for diagnosis; do not broaden selection or retry automatically.

Bind the unchanged application608/xcl/alhm source, native/client/module inputs,
existing tools and parent partial-pass receipt in the new packet. Add only the
new runner/checker/selection hashes and explicit old-to-new invocation delta;
recheck the original1807 bindings rather than globally refreshing expectations.
No source change means this method does not invalidate the retained Go/Node
passes or require another source derivation. Reuse them only with their original
actual exits/coverage and current input equality. Final quick acceptance is a
composed receipt linking the historical partial run, parent equality check and
successful continuation; it must not relabel outer89334 as a successful batch.

The separate vendor utility owns its unchanged rebuild packet; this continuation
neither observes nor changes it. Source binding, vendor proof, quick completion,
final committed affected review, native/state acceptance and deployment remain
separate gates. No new application review lane is created by correcting a
session-only invocation, and no review/native gate is waived. If source,
fixtures, environment semantics or selection scope must change, return that
concrete departure to the lead before editing or continuing.

## Restore the one missing vendor input before the final xcl rebuild

Status: COMPLETE bounded method for lead release. Owner2's immutable facts are
accepted; cache availability remains unknown until the exact output request
runs. Owner1 may prepare the small successor verification packet after the lead
reads this method. Execution belongs to the lead's fresh watcher, with one active
utility. Ruby42 continuation preparation and acceptance remain independent.
Architect only read assigned evidence/manuals and wrote this subsection.

### Exact failure and availability boundary

Evidence is `runtime-second-default-final/20261025-final/vendor-dependency-diagnosis-v1/`:
receipt SHA256 `8959c7dd2870175bb9b967217f46923dd7ca0172ec497e9bcee9fa7226bd6eec`,
diagnosis SHA256 `a09c74b8563bda18db62b68424123dfde2497ca7dead9bc6cd3ec9f5db91330a`,
21-file manifest SHA256 `0d388c15d6dac8cb3185a8012382c3ea0ceebaebde773b027b477bdf2a633e1d`.
The parent's `parent-diagnosis-assessment.json` accepts these facts and retained
original inputs. Preserve the original outer7837 attempt: first ten stages0,
requested target stage1 after25.461 seconds, runner1. Its global
`substitute=false` disabled missing dependency substitution. The finite declared
failure route is xcl→Git324j→pkg-config5z8→stdenv906→mesccpz3→stage02kbbz.
The stage0 diagnostic propagated back to xcl before the target started its own
phases. Neither existing lg6 nor xcl's preexisting valid-producer registration
proves a fresh build. No source or native defect is established.

The frozen target is
`/nix/store/xcl55br6w0piydf9dap79pwmp1jgjpzk-dev-workspace-0.2.0-go-modules.drv`,
raw SHA256 `ffef7e12d5e119a74b8271dc019a4c5d69a35281216402690857f0a7c8d30ba5`.
Its exact nine selected outputs are below. All nine derivation identities/raw
hashes and all output declarations are retained in the diagnosis; selecting jq
`bin` instead of its unselected `out` is material.

| New owned root name | Exact selected output | Diagnosed availability |
| --- | --- | --- |
| git-out | `/nix/store/g14fri80i39za36cqhi5pxrprnwp0kaj-git-minimal-2.54.0` | Absent/invalid; cache unprobed |
| bash-out | `/nix/store/rzl7zd3zx56vl7m55x1l49sr4xx2bb7y-bash-5.3p9` | Valid/present |
| review-assets-out | `/nix/store/hllcfkaav40y98j1v7vl3gkikgpd0w75-workspace-repository-review-assets-1.0.0` | Valid/present |
| cacert-out | `/nix/store/206m56yfhycp91zp3y6ry3ddirqflnxs-nss-cacert-3.126` | Valid/present |
| jq-bin | `/nix/store/vkjzswzi7r1ayxa0xr920bjrzmi04x7v-jq-1.8.2-bin` | Valid/present |
| stdenv-out | `/nix/store/843sqza79ns6k8n7sykxwmy04s741jzn-stdenv-linux` | Valid/present |
| bash-interactive-out | `/nix/store/pkf547jp8a92k4wmxikkyby58w10pysr-bash-interactive-5.3p9` | Valid/present |
| go-out | `/nix/store/3yh8g6m3balbhzxsx77jlyyx443bxqii-go-1.26.6` | Valid/present |
| shell-wrapper-out | `/nix/store/bnpp6hwrlvcdyijh5fpqyn13m11sy8rp-make-shell-wrapper-hook` | Valid/present |

The eight present outputs' runtime-requisite union has73 valid/present paths.
This is not Git's missing closure or the entire recursive build graph. Target
sources alhm, l622/source-stdenv.sh and shkw/default-builder.sh, published025
source cfjj and existing lg6 are valid. Runtime alhm NAR is
`sha256-U0nvYqqpbToyaBuT7otTMedVCBpPtxDI87CuMtc4OY8=`; cfjj NAR is
`sha256-f5AjJntJvsRGb8ocU6yGQOW+FYhK0TGoYzS3w4gSVbs=`. Preserve the accepted
full608/137 source byte/mode manifests and exact three-source graph.
These are timestamped observations, not guarantees against later disappearance.
No cause of disappearance, full toolchain closure availability or cache absence
is inferred. Partial unrelated builds/download attempts stay recorded without
cleanup or invented completion claims.

### Two distinct operations: availability/retention, then target proof

Prepare fresh no-clobber packet/results and a new explicitly owned root directory
`runtime-second-default-final/20261025-final/vendor-selected-output-roots-v1/`.
Refuse an existing/ambiguous directory or destination; preserve any partial
effects on failure. Do not rename, replace or add entries to the17 existing root
locations. Retain the old runner450d, ready9264, manifest339c, guards6552,
source certificate605b and all failed result bytes. New metadata explicitly
records the added roots and actual restoration; do not retain old fields claiming
that no realization/root operation occurred in the new attempt.

1. Before a store mutation, verify the complete session/environment/tool binding,
   all2483 original expectations,608 runtime and137 client bytes/modes, the
   accepted raw xcl/full derivation JSON/source/output relation, nine exact input
   derivations/selectors, and17 old root links/targets. Check validity/existence
   of the eight diagnosed-present outputs, their73-path closure, all three
   sources, cfjj and lg6. Unexpected missing inputs or changed identities stop;
   this package permits restoration only of g14, not expanding the request to a
   newly missing derivation/output or recreating source.
2. Register one new root for each of the eight already-valid selected output
   paths using standard `nix-store --realise OUTPUT --add-root OWNED_ROOT`,
   with substitution disabled, fallback false and builders empty. Every OUTPUT
   is the exact non-derivation store path in the table. This is retention only;
   a path disappearing before realization must fail, not build or fetch. Record
   each actual argv/exit/stdout/stderr and exact symlink/target. Retaining these
   outputs retains their runtime references through the ordinary Nix GC graph.
3. Restore and immediately root only Git's output in the **same** standard
   realization command, avoiding a separate unrooted interval. The exact shape
   is below; the owner uses the packet-bound installed Nix2.34.9 `nix-store`
   entrypoint and the literal absolute owned root path:

   ```sh
   nix-store --realise /nix/store/g14fri80i39za36cqhi5pxrprnwp0kaj-git-minimal-2.54.0 \
     --add-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-workspace-session-ui/runtime-second-default-final/20261025-final/vendor-selected-output-roots-v1/git-out \
     --option substitute true --option fallback false --option builders '' \
     --option max-jobs 0 --option allow-import-from-derivation false \
     --option accept-flake-config false --option flake-registry ''
   ```

   Preserve the ordinary configured substituters, trust/signature policy and
   daemon/store selection. No new cache/key/trust override, source fetch,
   `--ignore-unknown`, `--force-realise`, `.drv`, flake/installable selector or
   build fallback is allowed in this restoration request. In particular, never
   pass Git324j or xcl here. The installed `nix-store --realise` manual states
   that a non-derivation path is substituted with its closure or fails when no
   substitute is available. That argument type supplies the no-builder boundary.
   `max-jobs=0` is supplemental: installed documentation explicitly exempts
   `preferLocalBuild` derivations, so concurrency settings alone are not proof.
   Cache unavailability, authentication/signature/network failure, unexpected
   builder activity or nonzero exit stops without recursive toolchain build,
   cache-policy changes, bootstrap repair or automatic retry. Record partial
   downloaded paths/roots from the command's own evidence; do not scan globally.
4. Require actual exit0, exact g14 validity/existence and its new owned symlink.
   If it became valid independently before the command, report actual reuse,
   not a fabricated download. Enumerate runtime requisites of exactly the nine
   selected outputs with the existing bounded query, verify every returned path
   valid/present, and retain that actual union (not an assumed73 count after Git).
   Record exact output/root mappings and timestamps. Standard add-root exit plus
   the owned symlink/target proves the registration operation, without claiming
   an independent global registration audit. No `--query --roots`, global
   gcroot scan, manual auto-root/DB writer, delete/unregister or metadata repair.
5. Preserve and recheck all17 original roots alongside the nine new output
   roots. Old direct roots already retain xcl/alhm, cfjj and lg6; xcl's declared
   reference graph retains its input drv files and both source scripts. Verify
   that exact graph and all three source paths again. No duplicate source root
   is needed on this evidence. An absent/changed root or source stops instead of
   silently reconstructing it. An output root alone is never treated as proof
   that its producer derivation is retained; xcl has its own existing root.
6. Record a distinct availability/retention outcome, all actual exits, current
   closure and root observations, then repeat full source/JSON/raw drv/tool/
   alias and2483 guards. Only this successful boundary permits the separately
   released final target proof. Preparation or substitution success alone does
   not certify vendor execution, contents, quick checks or native acceptance.

The new output roots use a separate group so the old17-root inventory remains
unchanged and independently checkable. No owner should broaden this into a
retention framework or restore the intermediate failed build chain. If configured
caches cannot supply g14, the concrete blocker is its unavailable exact output;
return the actual command evidence to the lead instead of changing dependencies.

### One real final requested rebuild and unchanged acceptance

After the availability boundary and lead release, use a fresh final-proof result
directory and the same requested command as the failed packet:
`nix build --no-link --rebuild --print-build-logs /nix/store/xcl55br6w0piydf9dap79pwmp1jgjpzk-dev-workspace-0.2.0-go-modules.drv^*`,
with its existing no-IFD, `substitute=false`, empty builders, no flake-config and
empty registry settings. All nine selected outputs and their runtime closures
must already be valid and rooted immediately before this command. Retain the
normal build-capable max-jobs setting for this target; the restoration-only zero
override must not leak into it. The target remains the sole permitted builder;
unexpected dependency/toolchain building is a stop-and-report condition, not a
reason to let another bootstrap campaign finish. A root/precondition failure
does not trigger automatic restoration or another target attempt.

Keep the existing exact raw drv/full JSON/input/output/source identity checks,
actual per-stage argv/exit/timing/stdout/stderr receipts and source/tool guards.
Require evidence that **this requested xcl target** actually started and unpacked
exact alhm, then completed its own unpack/patch/configure/build/install phases
and vendor operation with exit0. Do not accept phase strings belonging to other
derivations, a producer registration, preexisting lg6 or empty reuse log. Preserve
the exact output relation and positive valid-producer membership after execution;
record historical registered-deriver metadata honestly without requiring equality.

Recompute output NAR SRI and require
`sha256-FxFVVTHhdpcPqDZFZfYOfAUnKIYmIdjr7u5dTixmHTQ=`. Run the unchanged complete
22-module/version/checksum and52-file published025 byte/inventory verification.
Recheck608 runtime and137 client bytes/modes, the raw target and sources, all2483
original guards, new packet/retention guards and all26 owned links after proof.
Any content/identity/phase failure stops without retry, output/root deletion or
hash adjustment. Preserve historical7837 failure and the separate restoration
outcome even if the new final proof passes.

This is a dependency-availability correction to the already-required final
vendor proof, not an application/source/native design change or a new review
campaign. No extra client, Go, Node or Ruby repeats follow from it. Final quick
completion, committed affected review, real state/native/runtime acceptance,
consumer pin/output builds and rollout remain their own gates. Nothing here
authorizes default integration, production-state changes, session lifecycle or
cleanup. No additional user permission gate is needed for the lead's bounded
release within the authorized verification work.

## Remaining naming acceptance: concrete entrypoints and preparation gaps

Status: bounded read-only answer to owner2's static acceptance preparation.
This records a missing prepared invocation, not a new implementation release.
Lead disposition is requested in report `c6ebda6a-2941-469c-b2de-50b0a380e603`;
independent package/browser preparation may continue. No test/native/provider,
build/evaluation, mutable consumer-pin read or foreign-record inspection ran.

The accepted runtime `44a483c61d68da59ca915dc5bb4f1a4790a62183` source
`/nix/store/alhmfv9zw2j0p12hifm83vpxw4imzn23-source` contains the two tagged
entrypoints `TestManagedNamingRuntimeIntegration` and
`TestNativeNamingRuntimeHTTPFailure` in
`portal/cmd/workspace-portal/naming_runtime_integration_test.go` (SHA256
`dd2fa7527902e8599bdd1f7a88ba6f98d81b8111f060e393537eda4f4dba51aa`). Its manifest
validator requires the explicit disposable-NixOS marker, uid1000, unified cgroups,
exact immutable package/source/test-binary paths and hashes, source heads,
protected ancestors and installed-resource guards. Its counter command requires
`/run/current-system/sw/bin/managed-naming-smoke-counter` through the reviewed
sudo boundary. Selected source has no implementation/export for that setup
outside the test's caller; `flake.nix` exports creation/archive lifecycle checks
but no managed-naming fixture selection. The inspected own preparation records
did not identify a retained runnable VM wrapper/manifest/compiled-binary receipt.
This is a scoped inventory conclusion, not a claim that no historical artifact
exists elsewhere. Lead may supply an exact retained owned selection.

Plain host `go test`, a marker environment variable, or a fabricated manifest
cannot replace these prerequisites. The existing test implementation is useful;
the missing preparation is its disposable VM/user-manager/network-counter setup
and exact final package/test-binary manifest. A new wrapper or fixture build must
receive its own bounded preparation assignment rather than being implied by the
current static recipe task. Preserve the original identity/egress/teardown checks.

The managed harness unconditionally creates synthetic auth/config and loopback
providers; its canary port tests denied network access. That canary is unrelated
to the required real positive `gpt-6-luna`/low naming result through the packaged
child/prompt within30 seconds. Creation's synthetic provider and the client
protocol fixture also cannot prove that gate. No concrete real-provider naming
invocation was identified in the inspected own packet. Keep the gate pending an
exact retained recipe or separately assigned bounded preparation; do not invent
a provider result, change credentials, weaken the synthetic fixture or introduce
a generalized harness. Existing PLAN/FORK failure provenance and all other
creation/lifecycle acceptance remain unchanged.

Immutable configuration guidance is available without reading owner1's mutable
pins: canonical `repos/vpsfree-cz-configuration.git`, revision
`270d348a29a832e552a798ba8bb467152a2d36d6`, paths `AGENTS.md`,
`skills/update-aitherdev-codex/SKILL.md`, and
`docs/operations/codex-deepseek-aitherdev.md`. These exact objects are byte-equal
to the existing owned `deepseek0164-preparation/source/` snapshots at those paths;
SHA256 respectively `c74ce3d5314c62d918ef97031c766222ee961190aa4878803f24022b1e0d0601`,
`60f4db902f58a9183717d09599d1217cabd436e8b12dba08013295c4452b5747`, and
`c2ae7f205e9aa01fa5a02308921f4577b4a6d2c4995144ffe2746e08865a4847`.
Owner2 may read those snapshots or the exact Git objects. Final consumer source
equality still belongs to owner1's pin receipt. Existing
`deepseek0164-preparation/receipt.md` and `future-verification.md` retain the full
schema result and output-gated isolated DeepSeek request; they supply no Luna
naming acceptance and no authorization to read a production key/home.

## Browser acceptance selector correction for Keep open

Status: confirmed static mismatch, narrow correction prepared for lead
disposition; no application/test-source edit or browser run by architect.
Owner2 reported this while preparing the existing acceptance selectors.

In accepted44a/alhm, `portal/internal/web/templates/session.html:104` exposes
Keep open as the intended native checkbox input with explicit `role="switch"`.
`portal/internal/web/presentation_browser_test.cjs:328,329,332` still locates it
as `getByRole("checkbox", {name: "Keep open", exact: true})`. An explicit switch
role overrides the implicit checkbox role for the semantic locator. The
`TestQuestionBrowser` wrapper includes this script, so this is an affected
acceptance-input mismatch, not an assertion that the browser test has actually
run or failed. It does not establish a production switch defect.

Smallest owning source correction: change those three locator roles to `switch`,
keeping exact accessible name, `.check()`, enabled/checked assertions, successful
hold-save behavior, failed POST503, requested hold=false, restored checked state
and visible failure diagnostics. `.check()` still targets the same native
checkbox input; no alternative selector, skipped block or template rollback is
needed. Do not silently patch a copied test, omit this script from its wrapper,
weaken the settings failure assertions or add a new parallel test framework.
The implementation owner is assigned by the lead; owner2's static packet labels
the current selector blocked while preserving the exact current-source recipe.

The focused change needs syntax verification and retained owning browser
acceptance on the corrected source, with the normal final-review/narrow-fix
disposition made by the lead after commit and quick checks. No standalone
new regression test is needed for this locator correction. This diagnosis adds
no reason to repeat unaffected client/native/Go/Ruby results. Preserve old44a
receipts; a repository test edit changes the runtime self-source NAR and may
change the selected package/goModules derivation, so it cannot inherit the
44a/alhm/xcl label. Bind the final corrected source and derivation explicitly,
apply the existing final-dependency proof requirements and assess unaffected
result reuse by actual inputs. Group final source preparation with any other
already-required acceptance corrections before publishing or rebuilding; do
not launch a stale acceptance packet to obtain a predictable locator timeout.

## Naming acceptance preparation: managed VM and separate real positive canary

Status: complete bounded design proposal for lead disposition, 2026-10-26.
This supersedes the missing-recipe disposition at line3856 only by specifying
the required implementation. It is not an implementation or execution release.
Architect inspected immutable44a/alhm and selected source documentation only;
no evaluation, build, test, native/provider request or host operation ran.
Owner3 is the proposed implementation owner, alongside the separately released
three Keep-open selector changes. Owner2 retains package/browser preparation;
owner1 retains final source/dependency/consumer binding. Lead serializes their
overlapping runtime work and releases subsequent operations.

### Source findings and minimum committed boundary

The existing tagged tests in
`portal/cmd/workspace-portal/naming_runtime_integration_test.go` enforce actual
UID1000, cgroup v2, immutable manifest/binary/package resources, native/catalog
hashes, denied-dial counter evidence, ordinary continuity and owned stop/join.
Neither the runtime flake nor an accepted retained receipt supplies their
disposable VM, counter or manifest builder. Their factory unconditionally writes
synthetic credentials and loopback-provider configuration. Its denied-network
canary cannot establish a real positive naming result. Transient session scripts
alone are insufficient: new verification logic belongs in committed runtime
test/Nix/documentation source and mandatory review.

One further prerequisite is source-proven. `startUnit` passes
`--workspace-name naming-smoke`, while `privateCase` creates no host registry
entry and its clean environment supplies no host profile selection. Production
`namingProviderArguments` calls the packaged `workspace-host provider native-args`.
`libexec/workspace-provider-sessions.rb:90-91,107` requires that registry entry
and exact selected profile; `libexec/workspace-host:3337` checks the profile.
The CLI requires a nonempty workspace name (`main.go:359`). Thus merely booting
the old fixture in a VM cannot satisfy this path. This is a static fixture
prerequisite finding, not an executed failure or a production defect.

The bounded source package has four owning paths, in addition to the existing
three-selector correction:

1. `portal/cmd/workspace-portal/naming_runtime_integration_test.go`: retain both
   existing tests/assertions; add private registry/profile setup and one
   opt-in `TestRealNamingRuntimeCanary`. Share only existing identity, HTTP,
   process and teardown helpers; use two explicit fixture constructors, with
   common initialization factored only where necessary. No general scenario
   engine, injected production namer, copied naming prompt or production API.
2. New `nix/tests/naming-runtime.nix`: bounded fixture-binary/manifest builders
   and two disposable NixOS definitions, using `pkgs.testers.runNixOSTest`.
   Keep the fixed counter helper and driver scripts here unless their size
   requires an adjacent test-only source file; report that file split to lead.
3. `flake.nix`: export the narrow test constructor
   `lib.mkNamingRuntimeTests { pkgs; package; provenance; }`, bound to this
   flake's `self`. Return only `fixture`, `manifest`, `managed` and
   `realCanaryDriver`. Do not add real inference to `checks`, package build
   phases or default CI. The managed test needs the explicit final composed
   package and genuine provenance; do not invent extension/workspace heads to
   manufacture a generic default check.
4. `docs/codex-package.md`: document the constructor, prerequisites, exact
   selectors, separate synthetic/real claims, safe launch and failure recovery.
   Link from the existing naming release-boundary text; no new operations
   framework or unrelated documentation rewrite.

No change is proposed to `naming_runtime.go`, `session_namer.go`,
`session_name.go`, provider policy, native source, module declarations, catalogs,
production systemd units or ordinary conversation handling. If implementing the
brief needs such a change, return the concrete reason to lead before editing it.

### Immutable selection, build and manifest dependencies

The inspected baseline is runtime `44a483c61d68da59ca915dc5bb4f1a4790a62183`,
tree `3bbfa411eeb6a53be9837ae70effabb0373609dd`, source
`/nix/store/alhmfv9zw2j0p12hifm83vpxw4imzn23-source`. The final fixture must instead
bind the reviewed successor containing all intended test/export corrections.
Use that successor's locked root nixpkgs: presently root edge `nixpkgs_2`,
revision `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`, NAR
`sha256-r2f1oUwixlgq9zOdYLqJLfS/lWBT60/IITjhTKI59JU=`. Do not use ambient nixpkgs
or the separate llm-agents nixpkgs node. The inspected NixOS testing interfaces
provide `runNixOSTest`, `.driver`, fixed driver test scripts,
`virtualisation.additionalPaths`, `sharedDirectories` and `restrictNetwork`.
The Go builder provides `buildTestBinaries`; these are existing interfaces,
not a request to add another VM runner or alter the installed toolchain.

The constructor takes the actual final assembled application derivation from
the accepted workspace package selection, including the actual extension/team
resources. It must assert that `package.src` is this runtime source. The caller
supplies a nonsecret provenance object derived from exact committed consumer
inputs: runtime/provider/extension/workspace heads, protected ancestors and
source/input receipt identities. Heads must be real selected revisions with
ancestry/input proof; syntactically valid dummy hashes are not provenance.
The runtime head must identify `self`; provider remains the actual selected
llm-agents head, currently `ea188d2f072e0ec8d5b71245e228803672801a22`.
Final extension/workspace revisions come from owner0's final receipt, not from
an inferred or stale consumer pin. Preserve protected runtime ancestor9634151
and extension ancestor399c330 exactly as the current validator requires.

Compile only `cmd/workspace-portal` with tag `naming_runtime_integration` into
an immutable Go test executable, using the selected package's Go toolchain,
source, pin check, review assets and exact `package.goModules`. Prefer the
existing `buildGoModule` test-binary support, explicitly reusing `goModules` and
the package's required `postPatch`/`preBuild` inputs. Disable test execution for
this compile derivation, not application checks. Install the test binary only;
do not inherit the application's post-install activation checks/wrappers into
this fixture. Prove the evaluated source/vendor/compiler/tag identities.
No source copy may receive an uncommitted patch; no second hash discovery or
separately selected module set is needed. If an override does not reuse the
expected `goModules`, stop at evaluation and correct the expression before build.

Generate the existing schema1 manifest in a separate nonsecret derivation after
the actual package and fixture output exist. Hash the final installed executable
after fixup, required package files, every installed agent-teams resource, and
required owning sources. Include the new fixture/Nix source and `session_name.go`
within the existing32-source limit; retain the512-package-file bound. Use actual
canonical store paths and actual package derivation, never guessed result paths.
This ordering avoids a manifest/binary self-reference. The manifest generator
must fail on missing resources, mismatched source/provenance or an exceeded bound.
Outside-VM receipts separately bind derivations, complete source/input graph and
manifest hash; the Go validator does not prove Git ancestry or derive provenance.

Keep exact raw0.164 native source10pdz and executable SHA
`d2af1cd0ea4187d413c237e80204e94ffcd5c7d8142840a662156b89750f54ae`, catalog SHA
`049042aaadcf2f19722fa1e893f926d2bdbd4d0ff092d80704ff4256e2a45fb1`/62680 bytes,
and client025 unchanged. The package exposes the native child at
`libexec/codex/libexec/codex/bin/codex`; retain actual resolved executable proof.
No custom Codex build, native patch or materialized-resource allowance changes.

### Managed disposable VM and private registry correction

Use a fresh x86_64 NixOS test VM with user `developer`, UID1000, lingering user
manager, unified cgroups and the exact candidate/fixture/manifest closures in
`virtualisation.additionalPaths`. Wait for `user@1000.service` and the user bus;
invoke the immutable fixture as that user with actual
`XDG_RUNTIME_DIR=/run/user/1000` for its systemd control commands. The existing
per-case clean environment retains its private home/XDG directories. Supply
`MANAGED_NAMING_SMOKE_VM=disposable-nixos-user-manager-v1` and all four existing
manifest/package/source/binary variables with generated exact values. Marker
checks supplement real UID/systemd/cgroup/output evidence; they replace none.

The guest's declarative nftables setup owns one private `inet` table with named
counter `denied` and an output chain restricted to UID1000. Permit fixture
loopback traffic except TCP39991; reject that port and deny other UID1000
network egress through the named counter, covering IPv4 and IPv6. The VM also
uses `restrictNetwork = true`. Existing Go probes must prove actual failed dial,
counter increase, zero listener hits and successful mock GET404, then no further
denied packets. Do not reset the counter between that baseline and teardown.
Install only in this guest a fixed no-argument
`/run/current-system/sw/bin/managed-naming-smoke-counter` which executes the
pinned `nft -j list counter inet <owned-table> denied`; reject arguments. Sudo
permits developer to run only that fixed command without a password. No generic
nft/shell sudo grant, host firewall installation or global counter inspection.

For each private case create mode0600 schema1 registry JSON:
`{schema:1,workspaces:[{name:"naming-smoke",root:<actual-private-workspace>,
hostname:"managed-smoke.example.test",aliases:[]}]}`. Its parent and state
directories are mode0700/UID1000. Set `DEV_WORKSPACES_CONFIG` to that file,
`DEV_WORKSPACES_STATE` to that case's state,
`DEV_WORKSPACES_PROFILE` to its existing exact-package profile link, and
`DEV_WORKSPACES_CODEX_PROVIDERS` to a deliberately absent private catalog path.
Assert absence of saved provider state there. These are test data for the real
read-only provider projection, not calls to host `register`, activation or
session creation. Retain nonempty workspace name, exact profile checking and
the existing assertion that no registration marker was created. Update the
fixture comment to distinguish a private registry record from host registration.
No ambient registry/catalog/home may satisfy this setup.

Run two explicit fixture invocations, serially, with `-test.count=1 -test.v`:
`-test.run '^TestManagedNamingRuntimeIntegration$'` and
`-test.run '^TestNativeNamingRuntimeHTTPFailure$'`. Preserve the five managed
subcases: one child/two concurrent slots/third queued; missing home; child loss
without respawn; MainPID TERM; MainPID KILL. Preserve HTTP-listener failure's
worker join before native owner close and ordinary synthetic continuity.
Do not shorten existing150/155-second systemd stop bounds or change the30-second
naming budget. Bound whole invocations, for example20 minutes and5 minutes,
with a finite30-minute driver budget including startup and teardown. Missing
prerequisites, missing tests, skips or cleanup errors fail the gate.

### Separate real positive canary and credential interface

Add `TestRealNamingRuntimeCanary` under the same build tag, run only by an
explicit real-canary selector and opt-in marker. The two existing managed
selectors never enter it. Its constructor shares the validated manifest,
process ownership, ordinary synthetic-control/proxy, HTTP admission and teardown
helpers. It does not call the synthetic naming-home writer and overwrite its
results later: naming uses a separately supplied private fixture home from the
start. Keep the ordinary control explicitly synthetic and label its receipts
accordingly. A real naming mock/provider must not be available as a fallback.

Supported serving interface is `DEV_WORKSPACE_CODEX_HOME` pointing to an existing
absolute private home; production `namingRuntimeEnvironment` supplies it as
native `CODEX_HOME`. Native0.164 accepts its own `config.toml` and auth storage
(`codex-rs/login/src/auth/storage.rs`, `auth/manager.rs`), including a separately
provisioned test account's auth.json. The host provider token-file projection is
another existing product interface, but this bounded canary uses the default
OpenAI provider in a fixture home, with no host provider catalog. Do not assume
`OPENAI_API_KEY` in ambient environment is equivalent: native's default provider
has no `env_key`, and CODEX_API_KEY handling has a caller enablement condition.
Do not introduce a new credential helper or change native/provider auth policy.

Native `model-provider-info/src/lib.rs:430-448` selects
`https://chatgpt.com/backend-api/codex` for its supported ChatGPT auth modes and
`https://api.openai.com/v1` otherwise. Select and record the actual supported
fixture account mode/route without exporting its credential contents; leave
native endpoint overrides unset. Do not assume an API-key account can access
Luna just because a subscription can. Fresh usable fixture auth is a launch
input; unexpected refresh or additional destination requirements stop for lead
disposition instead of silently expanding network or credential policy.

The launch prerequisite is an explicitly supplied, dedicated disposable test
home/account authorized for the real Luna endpoint. It must not be the operator's
production Codex home or a copy of its auth/keys. No such credential or model
access has been established by this design. A supported interface is not an
availability receipt. If the lead cannot supply this owned input, complete the
secret-free build/preparation and report this concrete real-canary blocker;
do not use production credentials or infer success from synthetic tests.

The real driver is built without credentials and runs outside the Nix build
sandbox after separate release. Use the existing QEMU `sharedDirectories`
interface with a runtime-only directory variable, e.g. `NAMING_CANARY_HOME`,
mounted as a fixed guest private native home. Mount only that dedicated directory,
never its parent or the host HOME. Validate canonical directory/UID1000/private
modes, actual mount and declared nonsecret config before starting the test;
the native child opens auth itself. Do not serialize credential values into
Nix strings/store, argv, environment receipts, manifest, driver logs or artifacts.
Do not use the test driver's base64/shell copying function for credentials.
The home is writable for native owned state; keep it private and separately
retained after failures, without exporting its diagnostic database/auth files.

Use a separate fresh VM definition/driver for real mode. Retain the UID/user
manager/cgroup/manifest/native/resource assertions and the blocked TCP39991
probe. Its explicit egress policy differs only as needed for real HTTPS and
the guest's declared DNS resolver; keep forbidden traffic counted and no
unsolicited inbound/host-service access. Bind actual nonsecret provider hostname,
TLS route and allowed destinations in the launch receipt; reject loopback/mock
endpoint configuration for naming. No TLS interception, response substitution
or rewriting to a synthetic provider. Any additional endpoint/credential-policy
requirement returns to lead before widening this recipe. The egress change does
not establish native tool isolation; the prompted contract still permits native
tool availability and makes no claim about their absence/effects.

Start one actual packaged portal user unit using the private registry/profile
setup above, the supplied naming home and existing fixed failure CLI helpers.
Observe its one exact native child, UID/PID/start/group/cgroup, catalog path and
`sessionFlags` origin before admission. Submit one public synthetic goal through
the real `/sessions` form/POST path with no custom name, no attachments, a fresh
request UUID and the installed team catalog. This reaches the actual production
`runPreparation -> namePreparation -> normalSessionName ->
RunPromptedEphemeralTurn`; never inject a `SessionNamer`, copy its prompt into a
test call, or issue a direct ordinary conversation turn as a substitute.

Require the same accepted request/receipt/attempt to acquire a schema-valid
generated base with `NamingOutcome=model` within30 seconds, measured from
admission with a monotonic deadline, and retain the sanitized production
`duration_ms/outcome/category` evidence. The existing worker owns its one30-second
budget, two slots, native willRetry handling, at most two proven-clean fresh
calls and backoff; the driver performs no second request, provider retry loop or
budget reset. Fixed CLI failure prevents starting any development session/team
after naming/reservation; it is not a naming failure and cannot count as full
creation acceptance. Prove no real session was initialized and no naming call
used the ordinary proxy. The resulting name need not match a hardcoded phrase;
it must satisfy the production schema, with no fallback/custom outcome.

### Teardown, launch gates and verification evidence

Both drivers must preserve the fixture's recorded-unit cleanup, worker-before-
child shutdown order, native process-group stop/join and cgroup-empty evidence.
Do not stop a user slice, host service or existing daemon. A test failure still
runs cleanup and records its separate result. If in-guest cleanup cannot prove
all owned processes stopped, retain failure and private state; the outer NixOS
driver must stop/join its owned QEMU process with finite bounds. VM termination
contains the fixture but does not turn a failed native cleanup assertion green.
Never reuse an interrupted guest/test-home result as a clean positive run.
Retain original logs, input manifests and partial receipts; retry requires
diagnosis and a new attempt identity. No session lifecycle or automatic cleanup
of retained evidence is included.

Implementation quick checks are the selected Nix environment's formatting/
syntax and bounded tagged compilation, existing naming/private-state/retry
unit checks, focused fixture-manifest/environment validation, and the three-role
browser selector syntax check. Add meaningful negative checks for wrong manifest
identity/missing private provider setup and for refusing a real selector without
its distinct opt-in/home; they must not launch native/provider during quicks.
Evaluate the fixed output graph and inspect VM UID/sudo/counter/closure and
managed-versus-real separation when lead releases evaluation. No actual VM test
or real provider call belongs in quick compilation or package build phases.

Commit all intended fixture/export/doc/selector changes, then send the exact
series/final diff and quick results to the retained reviewer. The new host-
fixture/credential boundary needs affected general, architecture, scope and
risk review;44's old report cannot cover it. This design record itself is
planning, not a claim of completed-deliverable review. Preserve no-migration
history and prior production compatibility conclusions where inputs are unchanged.

After review and lead release, owner1 binds the final source and final application
dependency derivation, performs the existing required final dependency proof
once, and refreshes coherent published runtime/consumer selections. The hash
remains Fx only if actual module/content proof agrees; no repeated discovery is
called for. Old44/alhm/xcl/source/vendor and client025 native receipts stay
historical. Reuse unaffected client protocol/state results only with actual
unchanged binary/schema/client/scenario inputs; new runtime source is not44.
No reason is introduced to repeat unaffected long native checks blindly.

Freeze an owned nonsecret selection expression that calls the new constructor
with the final package/provenance. Once its identities are accepted, the future
build selections are exactly `fixture`, `manifest`, `managed.driver` and
`realCanaryDriver` from that expression. Record actual JSON outputs/derivations,
retain their closures with ordinary owned roots, and preserve earlier roots.
Building a driver is preparation, not a passing test. Guest images/toolchain
dependencies must use the ordinary declared Nix/cache policy; an unexpected
local kernel/toolchain build stops for diagnosis under verification guidance.
No live helper installation/profile switch is needed.

The output-gated launch is the actual returned driver's
`bin/nixos-test-driver -o <fresh-owned-output-directory>`, first managed, then
separately real with its private-home input present. Use the fixed compiled
selectors above, and `^TestRealNamingRuntimeCanary$` only for the real driver;
cap the latter at5 minutes overall including bounded stop/join. A fresh
policy-selected watcher owns each long invocation; max1 utility remains in
force. Pre/post guards bind exact source, package, manifest, fixture executable,
native/catalog, driver scripts, tools and owned roots. Collect actual exits,
exact non-skipped test identities, sanitized result/timing and teardown proof.
No guessed store path, unbuilt package, missing credential, stale44 label or
successful driver build releases an acceptance launch.

The changes are test/export/documentation only: no persisted-format migration,
production credential relocation, application activation or rollback policy
change. Release still requires the managed checks and real positive result,
plus all previously required package/browser/creation/state/provider gates.
Missing real account/model access is an explicit remaining input dependency,
not permission to weaken either gate. Final source binding/build/publication
remain held until lead accepts this complete source boundary and implementation
is ready for its normal quick/commit/review sequence.

## Naming fixture composed hooks: diagnostic boundary and conditional correction

Architect0, 2026-10-26. This amends only the compile-only fixture composition in
the naming acceptance design above. It is a design disposition for lead review,
not an execution or source-edit release. Current/session environment agree;
live roster revision32 retains architect0 as ready Astra/xhigh/workspace_write.
Session, documentation, verification, lifecycle and team guidance and the
documentation/monitor/review procedures were reread. No Nix, build, test, native,
provider, VM, Git or application-source operation was performed for this design.

### Evidence and unresolved observation

The frozen [owner3 diagnosis](naming-runtime-fixture-hook-diagnosis-v1/diagnosis.md)
has SHA256 `ff7d75c6810c8494dc635aeef64a996925b11ec9e3627379701af5f4582d16a1`;
its [evidence](naming-runtime-fixture-hook-diagnosis-v1/evidence.json) has SHA256
`957ffcfa48043f382a226d0f1137975a82585d63ecce9c09b9432076ad9ed01c`.
Both hashes, the four proposed packet files, exact cited store-source files and
five actual v3 attempt files were independently matched by file-only reads.
Outer67455 remains runner1; stage01 was Nix1 in7.010813s, with empty stdout and
the original inspector's line106 conjunction failure. Final identity/guards
passed and the recorded groups settled. This establishes neither hook's actual
value; it does not establish that postFixup was forced. No output identity,
availability, recursive graph or build result exists from that attempt.

At runtimec31 source5dg, `nix/tests/naming-runtime.nix:28–51` clears postInstall
and postFixup inside the replacement buildGoModule. Extension767 source lfmic,
`flake.nix:158–164`, wraps the runtime package in overrideAttrs and appends its
migration symlink to postInstall. Workspace0c source iqym adds its update skill
through an argument override and does not clear hooks. Retained test-root a5cc
`lib/customisation.nix:162–191` explicitly replays an attribute overlay around
argument re-entry. That supports the indicated ordering defect; it is not a
certificate of the uninspected package-root d58 implementation. The extension
hook is legitimate for the installed application, but it does not belong to a
fixture that only installs a compiled test binary. No product defect or actual
fixture build failure is inferred.

### Accepted diagnostic method, subject to separate lead release

The [observer](naming-runtime-fixture-hook-diagnosis-v1/observe-hooks.nix), SHA256
`cee59bb28010093c21359cf94b575f56e3863fa069aa39a7f8c57f3728ebb92a`, and
[proposal](naming-runtime-fixture-hook-diagnosis-v1/observation-proposal.json),
SHA256 `1b5067215ccb5f5128e136c823397481d40b1dbf7b627312ca60c15671484131`,
are suitable for the bounded observation. Owner3 prepares the successor envelope
only after lead accepts this method. A fresh parent-released watcher owns any
actual invocation; this amendment authorizes neither preparation by another
owner nor execution.

Retain the exact proposed argv array, selection-context SHA256
`cb5cb835d52c5f04513501f217e9958cb17d79bd750477ae11886b81d1134fab`, and final
binding SHA256 `80dd48cf8d10aab8cc0f563ac18a0855fb03e28c464f0d2a819358f9921b7b1d`.
Comparison with actual v3 confirms only argv indices4 and6 change: a separate
observer file and the applied function name, with the same binding path. The
proposed working directory changes to the observer directory; imports/binding
are absolute and the context's relative snapshots remain context-relative.
No original inspector, assertion, selected input or package override changes.
The context's identity, full-lock, provenance and constructor prerequisites
remain enforced; the observer does not execute the inspector's later policy
assertions and cannot stand in for their acceptance.

Modern eval retains --json/--file/--apply/--offline, IFD=false, substitute=false,
empty builders, max-jobs0, accept-flake-config=false and empty registry exactly
as proposed. Evaluation may write derivation metadata/caches; it is not a
read-only-store operation. Offline has the already accepted documented scope,
not a network-isolation guarantee. No output build, root operation, query,
source-selection change, retry or automatic continuation is part of this step.
Preserve the180s/16MiB limits, finite recorded-group settlement and unconditional
finalization guards from v3. Use new no-clobber results and actual tool/session,
source, binding and input pre/post guards, preserving original packets.

Accept an observation as usable diagnostic evidence only when all of these hold:

- Actual eval exits0; stdout is complete JSON with the exact observer schema,
  keys and diagnostic-only scope. No truncation, ignored-setting warning,
  unresolved group, source/tool drift or failed finalization is accepted.
- Workspace0c, extension767, runtimec31, test-root a5cc and package-root d58
  revisions match the binding/context. Known source paths match retained
  receipts; a newly reported nixpkgs source path is observed metadata only.
  Package and fixture sources both equal5dg. Names and derivation/output fields
  have their declared string types and store-path shapes. New derivation/output
  values are recorded, not guessed or called currently available.
- All four exposed package/fixture hooks and their four drvAttrs counterparts
  are recorded verbatim as string or null, with null retained as absence. Never
  coerce null to empty, trim away content, or treat the wrapper's attributes as
  sufficient evidence of the builder's effective hook values.

The specific correction below is confirmed only if exposed and drvAttrs values
agree, fixture postInstall is exactly the extension migration-symlink suffix
from the composed package hook (same observed tools path, no additional command),
and fixture postFixup is actually empty. Compare the full returned strings with
the cited source; retain their raw bytes. Product install/fixup hooks must remain
present and consistent with the source. A null, unexpected extra command,
postFixup content, mismatch between exposed/builder values, or different failure
requires a narrow follow-up disposition. A successful observation is never
compile-only, VM-policy or naming acceptance, even if both fixture hooks happen
to be empty.

### Conditional implementation boundary

If those observations confirm the outer append, owner3's smallest source change
is confined to runtime `nix/tests/naming-runtime.nix`: apply the two empty hooks
to the final composed fixture, after package.override returns:

```nix
fixture = (package.override {
  # Existing replacement buildGoModule, attributes and goModules override.
}).overrideAttrs {
  postInstall = "";
  postFixup = "";
};
```

Keep the existing inner clears and replacement builder. In particular, moving
buildTestBinaries into only an outer overrideAttrs would retain the application's
go-install build phase and is not this correction. Preserve exact package.go,
package.goModules, source, postPatch pin check, preBuild review assets, vendorHash,
tags, subPackages, doCheck=false and empty checkPhase. A short adjacent comment
should explain that extension overlays can reintroduce hooks after builder
re-entry. The package and extension product hooks remain unchanged. No new
helper/export, mock package, directory creation, conditional hook execution,
native invocation or production behavior change is needed.

The original inspector SHA256
`8e21b2457a343c819e1e6bba9c02b391c98555b60d5b3bdf0e8a4c1d918d1ff3` remains
immutable. A separately prepared successor must retain all its logical
assertions, including exact empty hooks, test-c compilation rather than install,
compiler/modules identity, manifest bindings and complete managed/real VM
policies. Only newly accepted immutable source/input/provenance bindings change.
Use the same diagnostic projection on that final selection to establish both
exposed and effective drvAttrs hooks are empty; do not weaken line106 or replace
the full inspector with that projection. No separate application documentation
change is needed: docs/codex-package.md already states the compile-only contract;
the nearby source comment records the composition rationale.

### Quick checks, review and final-input dependencies

After separate source release, owner3 reports the exact one-file diff, preserves
the frozen c31 tree/failed attempts, and runs the declared Nix syntax/format quick
checks appropriate to this delta. Commit all intended changes and give the
retained independent reviewer the affected general/architecture scope and the
fixture's compile-only safety boundary before long checks. This changes a
previously unassessed composition boundary, so it needs affected review; it is
not an evidence-only edit or a reason for an unrelated full review campaign.
Preserve protected runtime9634151/extension399c330 ancestry and a single final
implementation/input-update stream, with old/new history and equivalence proof.

The new fixture source changes the runtime source NAR and source-bound derivation
identities even if module payloads stay identical. Old c31/5dg vendor, source,
browser and consumer receipts stay historical; do not relabel them final.
Prepare one coherent successor source/derivation and affected vendor proof under
the existing exact-final method, retaining Fx only on actual module/hash/content
proof and without repeated hash discovery. Generic runtime vendor proof does not
establish equality to the workspace d58 package's compiler/modules. Bind the
fixture to the actual composed package, as the existing inspector requires.

Owner0/owner1's ordinary consumer update routes must select the same newly
published runtime, preserve extension767 and unrelated lock nodes/edges, and
produce new complete source/input/provenance receipts before final naming
evaluation. No speculative pin or source hash is part of this design. Reuse
unchanged Go/Ruby/browser/client/native scenario passes only with actual relevant
input identity proof and an explicit old/new mapping; full self-source equality
no longer holds. The hook-only change alone does not require repeating unchanged
client/native tests or creating a custom native binary.

Once the final selection is accepted, run the unchanged full inspector plus
effective-hook evidence, immediate metadata availability/identity checks and
separate recursive graph inspection before any newly released build. Previously
unrun assertions remain unrun until those commands actually succeed. Then use
the existing fixture/manifest/driver build and managed/real acceptance sequence;
building a fixture or driver is not test acceptance. Dedicated real-account
availability, UID1000/user manager/private counter/egress, prompt30s/two-slot
behavior and native stop/join requirements remain unchanged. Unexpected failure
stops its stage, preserves evidence and owned resources, and returns to lead;
no automatic retry, cleanup or acceptance fallback is introduced.

No database/on-disk schema, public API, protocol, runtime option, deployment or
rollback contract changes. Installed behavior and migration hooks are retained.
Deployment, default integration, claims and lifecycle operations remain outside
this disposition. The session remains open; lead owns state/checklist and release.

## Reconfirmed capacity/other report: existing fix, no additional source change

Read-only reconciliation on 2026-10-26, after the lead identified the identical
error in this plan's Decisions. Session/current/environment pair and live roster32
match; architect0 retains Astra/xhigh/workspace_write. This is an investigation
result, not a new implementation or execution release.

The exact reported JSON, including null `additionalDetails` and `misalignment`,
is already the `reportedCapacityJSON` fixture in client025
`codex/capacity_test.go`. Immutable client
`02533a152223416f159bac2578e88bcbe653f247` at
`/nix/store/cfjj8pdplzk3vw154wk1ab9cc10kx9mk-source` implements
`codex.IsCapacityFailure`: typed `serverOverloaded`, or exactly code `other`
with message `stream disconnected before completion: Codex is at capacity, please try again later`.
It does not match arbitrary other/disconnect errors, altered wording, auth or
quota errors. No native producer change is required by this observed payload;
this assessment does not certify the producer's internal error mapping.

Runtime `f520a39511602cf83f3dda96b6a007a596d3b258`, immutable source
`/nix/store/2d5da9m3jl0fr0ldzzrsyxba18i3chgy-source`, pins that exact client in
both flake.lock and portal/go.mod. Its
`portal/internal/workspacecodex/turn_retry_proof.go:21` cold-reads the latest turn
through `ReadTurnState`, applies the shared predicate to the raw code/message,
and maps only the internal retry observation to `serverOverloaded`. The durable
controller uses this path for newly completed turns and persisted completions
on later polls/restart; browser event text is not the retry authority. Raw
history stays `other`. Client `transcriptFailureEntry` intentionally still shows
“Turn failed”, the message and the raw JSON, so that display alone does not show
whether the fixed classifier is loaded or the turn is eligible.

Existing regression evidence is sufficient for this report:

- Client `codex-web-naming/run-go-quick-naming-tmp-v2.sh` ran the untagged
  `go test -mod=readonly ./... -count=1` suite once; retained
  `go-all-naming-tmp-v2.exit` is 0/29s and its log records codex package PASS.
  The retained input manifest matches client025's capacity.go, capacity_test.go,
  turn_state.go and continuation.go exactly. Tests cover the exact JSON,
  negative near-matches, strict/prompted terminal proof, raw projection and
  cold-read preservation. This is historical non-native evidence: later
  client.go/ephemeral.go bytes differ from that earlier manifest, so do not
  describe the entire old client run as a final025 execution.
- `runtime-second-default-final/20261025-final/quick-results-v1/go-retry-retirement.log`
  and `.exit` record actual stage exit 0, including PASS for
  `TestRetryLoadedTerminalStatusController/idle/wrapped_capacity/`, its
  `systemError` counterpart, and `TestRetryCapacityObservationRejectsNearMessages`.
  The test uses actual managed admission/backend/controller/continuation,
  asserts the existing 15s initial delay, one start, no duplicate on another
  poll, unchanged partial answer/tool history, and refusal under existing holds.
  Its four-root/115-leaf coverage is this stage's scope; the original whole
  batch's later Ruby failure remains a failure.
- File-only comparison against that packet's `final-composed-source.json`
  confirms f520 has identical retry backend/test, controller/state, web retry
  adapter, portal/go.mod and go.sum. Backend SHA256 is
  `72b1b82785e20cf1caba731d0c03e3ae4ee5936d3b2eda7de20871ee8626a50c`;
  test SHA256 is `5b1711d6597dbe0c5cc8b3a1b1e4d1dc4533b3d0d0c846effd628cd9f764cfe7`.
  Accepted final source binding remains
  `runtime-f520-source-preparation-v1/parent-actual-source-binding-assessment-v1.json`.

Deployment is the outstanding delivery boundary. The retained current state
records reviewed/published/source-bound f520 and no application/system/profile
build or deployment begun. The earlier accepted fqaj/profile191 observation
proved only the dev-session command closure's later2a58/960dd behavior; it did
not identify the serving portal's complete source/client graph. Neither that
partial evidence nor the UI JSON certifies the failing turn's loaded binary.
No production scan was performed. Thus the exact fix is already in the
candidate awaiting rollout, but this investigation cannot conclusively assign
the reported instance to a particular deployed revision or eligibility hold.

Disposition: no implementer3 source package, new client/runtime pin, duplicate
test, source binding or vendor rebuild is justified by this repeated report.
Continue the existing final-input/acceptance/output/deployment gates. Preserve
retry count/backoff, cancellation, admission/auth/provider checks, terminal
proof and unknown-submission reconciliation. Schema1 and rollback contracts
remain unchanged. Already-handled or enrollment-baseline failures are not
retroactively retried on deployment; do not reset records or resubmit the
original request to manufacture a retry. Existing
`docs/turn-retry-recovery.md` documents this behavior. If the same failure is
reported on an accepted deployed successor, the missing bounded evidence is
the actual serving package/client identity plus that exact turn's retry
status/eligibility and terminal state, under a separately scoped read-only
observation. Do not broaden matching or assume all failures must retry.

## Independent workspace consolidation: guard only consumed inputs

The saved v2 failure demonstrates that refreshing the expected local shared
master preserved an irrelevant scheduling dependency. For this independent
two-file feature amend, remove only its local-master query/equality from a
small adapter guard, preserving the original guard historically. Keep every
own source/index/ref/tool/hook check and the separate fresh SSH master3e72 and
feature0c gate. No dynamically accepted master, tracking-prefix exception,
shared lock, rebase or Nix repeat. The operation consumes its exact owned
HEAD/tree/generated pair and fixed parent, not the shared checkout's ref.

[Exact scope correction and implementation boundary](workspace-f520-feature-guard-scope.md)
supersedes the earlier ef1→7d5 refresh recommendation. Both failed attempts
remain failed; this is a design disposition, not execution or integration
authorization. Owner0 prepares the small successor; lead owns release.

## Browser metadata continuation: optional own-process observations

For a directly launched, prevalidated no-shell command, immediate `/proc`
cmdline/exe snapshots supplement the bound launch receipt; unavailable snapshots
do not justify cancelling the child. Actual nonempty contradictory observations
still fail, and real command exit/output/settlement/postflight gates remain.
[Exact observation correction and saved-graph reuse boundary](browser-own-process-observation-scope.md)
preserves both failed attempts and reuses the successful complete v2 graph.
Owner2's continuation performs fresh required raw/root-DB admission and only
the unfinished selected availability query, with no recursive/eval/root/build
repeat. This is verification-method design only; lead owns execution release.

## Saved f520 browser graph: availability-aware next gate

[Complete saved graph assessment](browser-f520-saved-graph-assessment.md) accepts
the declared generic-runtime topology, with no output-content or final d58
package equivalence claim. All3510 drv/521 sources were available;3205 missing
outputs are not a build plan. Assets hllc already exists. For the two absent
requested shell/browser roots, stop dependency traversal at available outputs:
only exact stdenv outputmhm is a missing non-root prerequisite. Prepare its
standard output-only trusted-cache admission separately; a miss stops without
building bootstrap/toolchain/kernel dependencies. Do not restore the already
available asset output's unused npm build ancestry or repeat recursive metadata.

Retain the c31 exact-root build/retention method under fresh f520 input proofs;
no forced asset rebuild or additional builder is admitted. Explicit browser
selection remains Chromium+Firefox despite the default Playwright bundle's
additional engines elsewhere in the graph. Actual tool/engine/four-asset
content, browser tests and final workspace d58 composition remain separate
gates. Owner2 prepares; lead releases execution and owns state.

## Exact fqaj-to-fa7 consumed coordination-tool admission

[Bounded successor disposition](dev-session-fa7-tool-admission.md) admits the
parent-observed dev-session resolved path/SHA pair only for the existing current
and same-session roster readers. Owner0's new outer tool map and deep-copied
imported `G.S` must change exactly the two tool leaves after complete original
spec equality; original modules/specs/manifests and failed attempts stay intact.
Record and validate actual metadata URL separately from any derived URI.

Owners1/2/3 apply the same exact transition only at the saved system hostTools,
browser command/context/current-guard row, and naming launchTools admission sites
identified in the disposition. All other tool/source/index/environment/role
checks remain. Historical current-guard hashes are not relabelled as matching.
This is a verification-method correction, with no package equivalence, serving
portal identity, application change or execution release inferred. Lead accepts
each successor and retains the original operation boundaries; session stays open.

## Fresh upstream rebases after user steering

The user's direction to rebase and preserve existing changes supersedes the
pending old-head provenance completion. Do not finish extension-only ancestry
work or gate rebasing on another7476/61af/f520 certificate. Existing source,
root, review and failed-operation records remain historical at their exact
inputs; do not run their old source/lock guards against refreshed trees.

Owner0 owns workspace/client Git work; owner1 owns runtime/configuration Git
work. Use their fresh fetched default, feature, status, preservation and diff
snapshots. Preserve exact pre-rebase feature refs and any owned dirty changes
before ordinary feature rebases. Do not reset, stash broadly, mutate the shared
checkout/index, inspect foreign tracking contents, or discard changes to make
replay clean. A clean ordinary rebase is already authorized; substantive
conflicts go to architect/lead with the exact competing hunk and its owning
behavior before resolution. No additional launcher or release framework.

For workspace, compare fresh remote master with current shared local master by
ancestry and changed-path inventory first. Tracking-only advance is independent
of feature work and creates no local-master equality gate. Read only relevant
source/lock changes established by that inventory. If shared master contains
substantive source absent from the remote target, report that exact difference
so the base choice preserves it; do not silently claim the remote contains it.
Leave all shared working/index/tracking changes intact throughout.

Compose feature intent with upstream behavior rather than choosing either side
wholesale: preserve current session settings/unread/composer ordering, retry
identity/backoff/cancellation, naming private-state/budget/manual-recovery and
fixture boundaries, and archive schema1/semantic retry/lock/startup recovery
contracts. Preserve newly introduced upstream behavior and inputs as well.
Lock conflicts require the actual incoming and feature graphs, including edges
and follows; never restore an entire old lock or downgrade unrelated inputs.
Runtime/client changes precede any final consumer selection refresh. No Nix
regeneration, source/root operation, build or deployment is part of this phase.

After replay, owners supply the exact old/new bases and heads, complete series,
range comparison and final changed paths. Separate patch-equivalent replay from
new behavior or conflict resolution; transfer prior checks/review only where
their relevant patches and inputs are proven unchanged. Scope new quick checks
and affected review to the resulting source and interactions before later
builds. Keep one final dependency-update stream and supported ancestry/state
contracts; no old deployed or preserved nonancestor commit becomes literally
merged by assertion. Concrete conflict guidance follows the fresh snapshots,
without duplicate Git observations by architect. Lead owns coordination;
integration, deployment, claims and lifecycle actions remain outside this work.

## Workspace paused7476 replay: retire the superseded consumer pin

The saved `workspace-client-rebase-20261026-v1/workspace-paused-rebase.json`
identifies exactly old7476 onto d1efa51a9b2dfd46c825652bd401b9014f1ff639.
Its actual conflict is the runtime URL/revision/NAR/epoch in flake.nix/flake.lock.
Incoming d1 includes remote dacd3d7afb20f42c6f7bf95b767fb73fbbd61ea4 and its
observer/catalog-capacity9 source changes; the local suffix is tracking only.
The old7476 complete feature unit changes only these consumer input files.

Owner0 resolves this specific paused rebase with ordinary `git rebase --skip`.
Do not hand-merge a generated lock, keep auto-merged portions of the old pin, or
restore oldf520. Skipping the single superseded consumer unit must finish on d1
with a clean feature worktree/index and zero feature commits above that base.
Use ordinary final head/status/series evidence to confirm that result; any
additional paused commit or unexpected change goes back to lead. Shared master,
shared index and tracking contents are untouched. The preserved7476 ref/bundle
and failed replay remain historical.

This temporary zero-feature range is a preparation state, not final delivery:
the runtime/client implementation remains preserved. Owner1's saved ordinary
runtime replay already completed at ec93e57d34c038e551af53b8b0f7d26de3f07c03
over9baeea528f2e270332afa13786ec85a49a68e4c3, all11 units patch-equivalent to
f520 and no conflicts. Client025 remains on unchanged8b base. After the final
runtime successor is published and its actual source identity is established,
owner0 makes one normal final consumer pin to that successor, regenerating its
complete nested graph by the normal method. Preserve incoming observer/catalog
source and extension767/root follows; the successor runtime's client025/providerEA
and nested input choices return through that graph, not a stale hand-copied lock.
Configuration must likewise ultimately select the combined runtime successor;
its concrete conflict disposition depends on owner1's saved config snapshot.
No Nix/pin generation, build, publication or integration is released here.

## Configuration61af disposition and ec93 observer interaction checks

The same consumer-pin disposition applies to configuration's sole61af replay
onto7eaaafd718809e16867c9b4614f9b2e2d54fa62a. Saved pause/todo/conflict evidence
in `runtime-configuration-rebase-20261026-v1/vpsfree-cz-configuration/` showed
only the obsolete generated pin, with incoming9ba versus oldf520 and unchanged
64-node graph topology. Lead released the ordinary skip; owner1's saved
`final.json` now records clean7eaa, zero feature commits and full64 graph equality
to the fresh default. The preserved61af ref/bundle remains. No hand-merged lock
or partial old pin is required. One normal final configuration pin will select
the published combined runtime successor, as for workspace; this is not final
consumer delivery yet.

Runtime's saved `dev-workspace/rebase.json` and `range-diff.stdout` in the same
packet establish actual successful replay from960dd/f520 to9ba/ec93, with all11
units `=` and clean owner-reported status. Exact new head is
ec93e57d34c038e551af53b8b0f7d26de3f07c03. Incoming source diff SHA256 is
8b3dc0412a5978c79ad819af0139290f0aebc02ce63270292684c9d05f8a47c0;
range-diff SHA256 is
c637f9f27feeed96bf9562d47fa66c4b6e07e5b0db4176f7bddc8d58ea85dc9a.
There is no incoming module/input-lock change. Actual feature overlaps are
`docs/workspace-portal.md`, `portal/internal/web/static/app.js` and
`portal/internal/web/templates/session.html`; replay needs no source correction
on the evidence reviewed.

Preserve these combined behaviors and use them as the affected review boundary:

- Incoming progress observation requires a ready read-only observer and active
  development; it does not enroll existing teams, wake idle leads or displace
  manual work. Its optional private state, stable submission identity, uncertain
  recovery and exact owned-turn deadline remain separate from roster/lifecycle
  schemas. Existing archive schema1, generation and retirement guards remain.
- `workspacecodex/progress.go:SendProgressCheck` holds the retry-admission
  transaction across `sendWithRecovery`, refuses owned manual retry work and
  creates no ordinary automatic-retry snapshot. Manual `SendWithOptions` retains
  ordinary admission. The feature's exact wrapped-capacity classification must
  continue to retry admitted manual work without admitting scheduled observation
  into the retry controller or broadening all `other`/disconnect failures.
- `web/progress_observer.go` runs under `operationContext`/`operationWG` and is
  joined by `Close`; startup cancellation stays distinct. Preserve accepted
  attachments and retirement cancellation. UI observer status uses `textContent`,
  shared refresh deadlines/notices and visibility cancellation. An uncertain
  toggle write is followed by a read, never a repeated POST. Keep feature switch
  roles, unread/composer order and silent healthy refresh behavior alongside it.

Owner1's focused quick batch should cover the existing `TestProgress*` tests in
`internal/progressobserver`, `internal/web` and `internal/workspacecodex`, plus
`TestRetryLoadedTerminalStatusController`,
`TestRetryCapacityObservationRejectsNearMessages`,
`TestRetryRetentionUnknownAutomaticAtCapHoldsManual`,
`TestStartupContextLeavesWorkerShutdownToClose`,
`TestStartupCancellationPreservesAcceptedAttachments` and
`TestDirectThreadPageShowsLifecycleAndTeamControls`. Run in the repository's
selected environment with explicit `go test -mod=readonly`; confirm the Node
wrapper `TestProgressBrowserPresentation` executes rather than skips. Existing
synthetic Node contracts `browser_contract_test.cjs`,
`composer_handoff_contract_test.cjs`, `paging_browser_test.cjs` and
`queue_refresh_presentation_test.cjs` cover the overlapping app behavior. Reuse
any of these already included in owner1's current batch; do not launch duplicates
or introduce a harness. Success means the selected tests actually pass, with
owned processes settled; a failure goes to its owning interaction before retry.

After quick checks, give the retained reviewer the complete11-unit old/new range,
final diff and existing migration conclusion, concentrating new review on these
observer interactions and the overlapping documentation/UI. Patch equality
preserves earlier review scope but does not certify new baseline interactions.
No blanket repeat of unchanged client/native checks follows from this rebase.
Longer required package/browser/naming checks still bind the final combined
source and inputs after applicable review; oldf520 source/build receipts remain
historical and do not prove an ec93 derivation. Final normal consumer generation
must preserve upstream observer/catalog-capacity9 and extension/root-follows
while selecting the combined runtime/client/provider graph. This brief adds no
application edits, operations, integration or deployment release; owners retain
their existing execution boundaries and preserved predecessors for recovery.

## ec93 delivery: reuse completed work and evaluate the final composition

Saved acceptance91422890 proves published ec93/617/source929/MlyRA and unchanged
eight dependency inputs; publication023fb8e1 includes resolved A1 checks without
a source correction/review rerun. Saved f520609 versus ec93617 inventories show
five changed existing files, eight added observer files and no removals. Recipes,
flake/lock, module files, naming fixture/test and all14 review-ui files are exact
in mode/blob/bytes/hash. Configuration acceptancee7634b39 proves local73acc, one
generated unit/full64 topology. Final workspace head and published consumer
source/NARs remain pending. Reuse completed source/publication/review/quick proof;
do not rerun old wrappers or claim old source/build results for the new head.

After matched consumer review/publication, the next compact batch is:

1. **Final d58 composition first:** rebind the existing full naming inspector to
   actual consumers/ec93. Select `workspace.packages.x86_64-linux.vpsfree-dev-workspace`
   and the runtime's `lib.mkNamingRuntimeTests` with that package, actual
   provenance and locked a5cc test pkgs. Learn package/fixture compiler,
   goModules, native/resources, assets, manifest and driver identities. Preserve
   all compile-only/VM assertions and exposed/effective drvAttrs hook checks:
   fixture hooks empty, product hooks intact, fixture source/compiler/modules
   equal the package. No additional hook-only diagnostic on success.
2. **Browser reuse comparison:** evaluate the existing browser-environment
   selector once for ec93; compare all9 identities plus shell drv/output against
   f520. Only runtimeSource is expected to change, but accept actual evidence.
   Equal raw root derivations, selected outputs, tool inputs and filtered asset
   source permit reuse of graph6a0ab1db and demonstrated hllc asset scope, without
   another recursive query/asset rebuild. Inspect only changed roots. Actual
   output/tool/engine and four generated asset-file admission remains necessary;
   source hash alone proves neither output identity nor browser acceptance.
3. **Final configuration selection:** reuse its new accepted publication metadata.
   One corrected selector derives `p = f.confctl.buildPlan."cz.vpsfree/machines/aitherdev"`
   and `o = f.confctl.build.${p.key}`, capturing actual key/inputs/machine and
   toplevel/autoRollback `{ derivation = ...drvPath; output = ...outPath; }`.
   No duplicate buildPlan query is needed for the same captured fields. Apply
   the accepted exact four qualified-URL metadata differences; never replay
   failed bootstrap/schema/partial-graph attempts. Reuse demonstrated unchanged
   source-role/NAR/raw-root/subgraph facts; inspect only missing current role or
   changed graph facts. Actual root HM/EA paths govern, not inputsInfo's alias.

These use existing no-build settings, exact-lock retrieval scope and declared
selectors. Unknown final identities stay null. Immediately establish actual drv
files/raw metadata and retain needed objects through the accepted metadata-root
primitive; never pass a drv to output-only realise. No new runner/framework.
Before builds, admit current selected outputs/runtime closures and stop graph
traversal at usable outputs. Restore only exact missing prerequisites through
standard trusted caches; misses stop before bootstrap/toolchain/engine-source or
local kernel builds. Historical mhm absence is not a current restore instruction.

F520's accepted v43/lg6/Fx forced proof and22-module/52-file content proof
(assessmentb604850c) remain reusable in their exact scope. Compare the evaluated
final dependency recipe/compiler/inputs, output and content before transfer;
new drv/producer membership does not prove execution. If the retained exact-final
requirement needs a distinct final dependency target, prove that target once,
not both intermediate generic ec93 and final d58; never repeat v43 or rediscover
Fx. Build only admitted final package/fixture/manifest/drivers and system outputs.
System Codex/HM and the d58 user-profile application remain distinct; normal
confctl build creates a local generation, not a deployment.

Then complete only still-unrun final-input package/creation/archive, affected
Chromium+Firefox/question-browser and managed naming scopes from existing briefs.
Retain successful quick/client/native scenario evidence only for matching inputs;
changed observer app/template bytes prevent blanket browser-result transfer.
Actual system/assembly/profile/catalog output checks remain. Real Luna/low30s
naming still requires a dedicated isolated home/account: synthetic success and
production credentials cannot substitute. Independent non-real work can proceed.
Lead owns release/state; this saved-only brief authorizes no operation or
consumer edit. Session stays open.

## Current47697/73acc naming provenance: saved facts and remaining inputs

The committed consumer heads are workspace
47697bf33265a828b93b25bff31df192adf7c62d over
d1efa51a9b2dfd46c825652bd401b9014f1ff639, and configuration
73acc875314e940cab861cc871f39d8896c2607f over
7eaaafd718809e16867c9b4614f9b2e2d54fa62a. Each has one final generated-input
unit, with no migrations. Saved workspace `workspace-ec93-pin-20261026/final.json`
(b1e81801), `generated-inspection.json` (57da8be3), configuration
`runtime-configuration-rebase-20261026-v1/configuration-ec93-pin-results-v1/final.json`
(afcb7493) and matched `workspace-ec93-pin-20261026/checker.json` (74dc955a)
bind these heads and complete35/64-node locks, including unchanged edges/follows.
The checker actually passed0/.304s; it is not publication or output acceptance.

Both select ec93/source929/MlyRA from accepted91422890. The complete nine-node
runtime mapping is: workspace `root -> dev-workspace`, with all eight dependency
names unchanged; configuration `root -> devWorkspace`, `nixpkgs_2 -> nixpkgs_4`,
`nixpkgs -> nixpkgs_3`, with the other six names unchanged (`codex-web`,
`llm-agents`, `bun2nix`, `flake-parts`, `systems`, `treefmt-nix`). The saved graph
comparisons preserve all eight dependency bodies and effective edges. Thus
client025/providerEAea188/test-root a5cc/nested f20 remain selected; workspace
extension767 and package-root d58 remain separate unchanged inputs. This records
the actual committed graph, not yet the final immutable consumer source paths.

Protected runtime963 reaches ec93 through saved facts, without promoting ac275:
`default-refresh/20261025-assessment/runtime/assessment-inputs.json` (e75fcaa6)
records963 as merge-base with b974; the accepted five complete parent links in
`runtime-moved-defaults/20261025T223325Z/runtime-incoming-inventory.json`
(ee683572) connect b974 to960dd. Actual exit0 records
`runtime-configuration-rebase-20261026-v1/dev-workspace/base-ancestor.json`
(c637f813) and `new-base-ancestor.json` (4a5162c4) establish960dd ->9ba ->ec93.
The same packet's complete11-unit `range-diff.stdout` (c637f9f2) and accepted
refreshed review establish feature preservation. Oldf520/c31 and old consumer
heads remain preserved predecessors, not literally merged ancestors.

The historical ac275 summary records extension399 ->767, but this inspected
packet still lacks an independently accepted execution/complete-chain basis
for that pair. Keep that one boolean pending. Owner0 can include exactly this
read-only command in ordinary publication preflight, using its admitted Git:

```sh
git --no-optional-locks --git-dir /home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-dev-workspace.git merge-base --is-ancestor 399c33023a568a8d7a21e4e4df52829628720a28 767dfd587e346168e1443e65ccdb67ce748f3fe3
```

Exit0 proves the exact fixed pair; exit1 disproves it and other errors leave it
unknown. Retain ordinary argv/exit evidence, with no fetch, ref change or new
campaign. This is a proposed preflight addition, not execution release.
Remaining binding facts are that result and owners' accepted published consumer
source/NAR/epoch/URI receipts with full locks equal to these committed graphs.
Those source fields remain null until supplied. Current fa7 reader admission
stays unchanged; this note adds no tool observation, repeated manifest, ancestry
packet or consumer edit. Lead may bind these existing records directly for
owner3's minimal continuation; no current application/output/deployment claim
follows from the bookkeeping.

## Unlaunched composition: exact fa7-to-w6 reader admission

Extend the accepted25a7/dcca reader-only method to selected
`/home/aither/bin/dev-session`, resolved exactly to
`/nix/store/w6j9bzbv7m04h7snndb5bs9jj39jd2kc-dev-workspace-0.2.0/bin/dev-session`,
SHA256 `01eddac8516af4eb2e9f87b105ec773eb96fd6678010b8c5929a362c9f4f842f`.
Static reads confirm that and prior fa7/579 hashes; both wrappers are580 bytes.
Only their extension-catalog and exec workspace-host package paths differ.
Interpreter, arguments and environment defaults are identical. Current exits0
with the exact bound slug, both environment markers match, and roster38 retains
ready architect Astra/xhigh/workspace_write. Lead and owner3 report the same
reader contracts. No incompatibility is established for `current` and exact
same-session `team list --as-is`; transitive package/library, serving portal and
lifecycle compatibility are not established or needed for this admission.

For the reported never-launched composition, owner3 may prepare only this delta
after lead accepts it: preserve byte-exact active bindingb9182eb7 and release3c3
in exclusive backup files **beside** them in
`naming-runtime-ec93-final-composition-v1/`, then change only active
`launchTools.dev-session.realpath` and `.sha256` to the pair above. Assert the
whole old binding hash and exact two-leaf parsed difference. Selected entry,
all other tools, source/provenance and null fields stay unchanged. Parent release
binds the new active binding hash and this exact reader admission, retaining
every execution scope/cap/destination/settlement/postflight condition. Old release
is preserved as superseded before execution, never relabelled as a w6 receipt.

Saved evaluate.py consumes that active binding in both tool/current guards.
Its packet hashes bind `final-bindings.proposed.json`, not active
`final-bindings.json`; retained inputs do not bind the active files. Therefore
code, proposed binding, packet hashes, ready file and inspectors can remain
byte-exact. Keep the reserved `attempt-ec93-final-composition-01` and
`metadata-roots-v1` absent: putting backups inside the reserved attempt directory
would conflict with the existing exclusive mkdir. Reuse that still-unlaunched
destination; this is not a retry or a new packet. Any discovered launch/effect
invalidates this unlaunched adaptation and requires reconciliation first.

Workloads1/2 may apply the same two-field reader admission at their existing
consumed sites only, preserving any explicitly bound historical copies and all
other guards. No six-tool re-observation, automatic expectation refresh, driver
edit, guard/evaluation/root execution or product test is indicated. Further
resolution/hash or reader-contract drift still refuses. Lead owns preparation
acceptance and execution release; source/Git windows and session remain open.

## ec93 composition inspector: flattened builder environment

The saved v2 failure at `inspect-selection.nix:111` is an inspector API error:
`fixture.env` is absent. Preserve that failed attempt and its empty stdout;
no composition, retention or graph success follows from it. This amendment is
verification-method only; it changes no product, fixture, pin or deployment.
Current/session environment and roster38 still match architect0's retained
Astra/xhigh/workspace_write settings.

Exact sources inspected: runtime ec93 at
`/nix/store/929i467d322mccddjs9x2ah05ksc99zl-source`, extension767 at
`/nix/store/lfmiclfqmpw7bs99lil6x5f83ba1j070-source`, package nixpkgs d58 at
`/nix/store/9g5ii96ynv0cgdnninnv0rw37w5aai63-source`, and test nixpkgs a5cc at
`/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source`. Runtime
`nix/tests/naming-runtime.nix:29` uses **a5cc's** buildGoModule with the exact
package compiler and goModules; the product package uses d58. Both selected
`pkgs/build-support/go/module.nix:219` implementations define the same six Go
environment fields. Both `pkgs/stdenv/generic/make-derivation.nix:222,960,1068`
remove the input `env` container, conditionally restore it for structured attrs,
and always pass `derivationArg // checkedEnv` to `derivation`. Thus the public
derivation and its `drvAttrs` expose these values at top level, with their
original types and string contexts. Runtime's package supplies no env override;
its `meta.mainProgram` also contributes `NIX_MAIN_PROGRAM` through checkedEnv.
Extension's assembly changes postInstall, not this environment representation.

Owner3's smallest correction in the successor **inspector only** is:

```nix
assert fixture.GOTOOLCHAIN == "local"
  && fixture.CGO_ENABLED == package.CGO_ENABLED;
# In the existing fixture declaration object:
declaredEnvironment = {
  inherit (fixture) GOOS GOARCH GO111MODULE GOTOOLCHAIN CGO_ENABLED GOFLAGS
    NIX_MAIN_PROGRAM;
};
```

This fixed projection records the selected builder's environment declarations;
it is not the entire process environment. Do not reconstruct values from the
compiler, stringify them, strip their context, probe alternate shapes or add
`tryEval`. Keep v1's needle-only context fix. The raw derivation JSON `env` used
by `verify-evaluation.py` is a different interface and remains unchanged; do
not replace it with this Nix-language projection or accept structured data by
fallback. Selected ordinary builder recipes support its existing reads; saved
Nix JSON also contains structured dependency nodes, which traversal does not
mistake for the selected fixture/manifest/driver/counter declarations.

The remaining inspector reads were checked against these selected recipes:
Go phases/options/compiler passthru and fixtureContract; manifest passthru and
buildCommand; writeShellScriptBin/writeTextFile's `text`; NixOS testing
`driver.nix` testScript/passthru, `run.nix` config, `nodes.nix` nodesCompat, and
`driver-configuration.nix`'s serializable configuration; qemu-vm shared-directory
fields/default shares/additional system path and sudo rule fields/defaults.
No further missing-attribute correction is established. This static audit does
not certify effective module values: retain all existing exact compiler,
modules, source, assets, hooks, UID, sudo, egress, shares, VM, driver and raw-graph
assertions so an actual composition mismatch still fails visibly.

Owner3 owns the bounded implementation and lead-authorized rerun. Preserve
original packets; rebind only changed method bytes through the existing
preparation. No new framework, source review, product rebuild or source edits
are indicated by this error. Acceptance still requires complete evaluated JSON,
the existing raw graph verification and normal guards/settlement; none was run
by this static diagnosis. A different product mismatch returns to lead with
its actual evidence. Session remains open.

## ec93 composition inspector: inherited TERMINFO sudo baseline

Saved v3 stderr (`naming-runtime-ec93-final-composition-v3/attempt-ec93-final-composition-01/01-evaluate.stderr`,
e39a8507) identifies an incorrect empty-string expectation, not a demonstrated
product failure. In the same selected a5cc source
`/nix/store/nqkh6j5xlyvlw4hlrw4ybpq1cis79szf-source`,
`nixos/modules/config/terminfo.nix:20,89` defaults
`security.sudo.keepTerminfo` to true and contributes exactly the two
`Defaults:root,%wheel env_keep` lines. `security/sudo.nix:208,229,266` declares
extraConfig as lines, keeps root/wheel command rules separate, and appends the
extra text to sudoers. The saved actual string, including both initial newlines
and the final newline, is the bounded baseline to match.

These user-scoped Defaults preserve TERMINFO_DIRS/TERMINFO for an invoking root
or wheel member; they grant no executable or run-as permission and do not apply
to developer merely because its counter command runs as root. The selected
fixture makes developer UID1000 with no auxiliary groups; users-groups.nix
defaults a normal user's primary group to users and does not add it to wheel.
The explicit developer rule still grants only the argument-rejecting counter
wrapper. This contribution changes neither that rule nor nftables, egress,
namespace, user-manager or fixture isolation. No safety/product correction is
indicated by this saved difference.

Owner3 may replace only the empty-string assertion in the common policy
function with this exact literal comparison under lead's conditional release:

```nix
assert node.security.sudo.extraConfig == "\n\n# Keep terminfo database for root and %wheel.\nDefaults:root,%wheel env_keep+=TERMINFO_DIRS\nDefaults:root,%wheel env_keep+=TERMINFO\n";
```

Do not trim, normalize, accept arbitrary nonempty text, disable keepTerminfo or
change the fixture. Retain actual `sudoExtraConfig` in output, the exact
developer sudo-rule assertion, UID/group checks and all policy/raw-graph checks.
The same selected source also confirms the remaining statically decidable
assumptions: driver lint/type-check defaults are false for their skip options;
the fixture supplies exact timeouts and script literals; driver testScript
comes from testScriptString; QEMU adds the already-modelled shares and system
path. Test instrumentation's nameserver override has priority150, so the
fixture's ordinary priority100 managed/real declarations prevail. No other
policy-expectation change is established. Effective values still require the
complete evaluation and existing assertions; this is not a passed evaluation.
Preserve v3 as failed. Only this inspector method changes; source/pins and prior
fixes remain intact. No new certificate, framework or execution by architect.

## Preserve the deployed observer while replaying ec93

Owner0's saved `runtime-observer-preservation-rebase-20261026/` fetch/history
proves old base `9baeea528f2e270332afa13786ec85a49a68e4c3`, preserved feature
`ec93e57d34c038e551af53b8b0f7d26de3f07c03` (11 units), and fresh remote master
`f8b94441a6b5066973a72284955b793b301c60ac`. Its three incoming units are
`54e968ae169e9ca96744b045ecc4a7536e62bcb2` (cold observers),
`120c7b9c4a55c63d168b0859099a6829505bbcdf` (session settings), and f8b94441
(scope/working-time evidence). The 17-path incoming inventory has no flake/lock
change. Owner2's saved `runtime-ec93-browser-results-v1/deployed-baseline.md`
(d9d0dc00) binds selected jgj to source
`/nix/store/lyln6zqfw234ckh417dwdmanskdk4l55-source`. Owner0's saved
`selected-observer-witnesses.json` proves all17 incoming paths plus flake.nix/
flake.lock byte-equal to f8b94441, with no missing/different witness. This binds
the relevant deployed observer and flake graph to the exact rebase base; it does
not assert whole selected-source Git equality. The other three candidate
commits differ or miss witnesses. Actual incoming/feature overlap is only
docs/workspace-portal.md and templates/session.html. ec93's known source
remains929/MlyRA. Preserve all old refs
and results; owner0 alone owns ordinary rebase and conflict edits.

Rebase the preserved 9ba..ec93 feature range onto exact f8b94441. Keep incoming
observer implementation and its new files, including repository progress
evidence and instructions. Preserve the API's independent enabled/interval
writes, integer1..1440 bounds, explicit check while paused/idle without unpausing,
and ordinary lifecycle/admission/duplicate-pending refusals. Background checks
still require active work; cold ready observers can start. Keep exact pending
send identity, retry-admission lock and typed ErrProgressCheckDeferred: only a
first refusal proven before dispatch clears Pending; later uncertain sends
remain recoverable. This must compose with our client025/capacity retry changes,
without enrolling scheduled observer turns in ordinary automatic retry.

Both old and new observer records are schema1. Incoming IntervalMinutes,
PreviousEvidence and Pending.EvidenceComplete must survive load/save; ec93's
older writer would omit them. Retain zero/missing interval's15-minute default,
evidence-gated on-track results, matching resolution key/evidence, repeated
concern escalation and unavailable behavior. Preserve upstream same-session
evidence boundaries and the exact-stock-only scheduled instruction adaptation;
do not rewrite saved custom roster instructions or settings. No migration,
state reset or downgrade to the older observer writer is proposed. Recover
forward with an observer-preserving package if activation later needs repair.

The likely composition boundary is `templates/session.html` and the two docs:
retain the progress panel in **Settings**, all interval/form/save/Check-now IDs,
status/banner and single mount; retain our notification/Keep-open/retry switch
roles, labels, descriptions and silent queue text. Keep both documentation
intents. Do not take an entire old template or lock. Actual incoming inventory
does not change app.js/server.go; their ec93-vs-selected differences largely
reflect our feature, not incoming deletions. Preserve our app.js FIFO/uncertainty,
filtered unread, retry and queue behavior byte-exact when replay permits.
Actual other conflicts go to lead/design with their hunk, without dropping an
incoming unit or silently accepting a feature rollback. Keep one final native/
client dependency stream and the existing naming/fixture intent. Consumer pins
must ultimately select the composed successor, never restore ec93 over it.

After replay, owner0 records range-diff of9ba..ec93 against f8b94441..successor
and only real conflict-resolution deltas. Focused quick check in the declared
environment, from portal: `go test -mod=readonly ./internal/progressobserver
./internal/repository ./internal/web ./internal/workspacecodex -run '^TestProgress'
-count=1`. This includes existing observer CJS through TestProgressBrowserPresentation;
Node must be available and that check must run rather than skip. It covers
interval persistence, paused explicit checks, cold start, same-session evidence,
stock/custom instructions, repeated concerns and retry refusal/reconciliation.
Retain existing capacity/loaded-terminal regression evidence when its inputs
remain unchanged; rerun only a genuinely changed interaction. The changed
Settings template requires only the existing TestQuestionBrowser presentation
subcase after quick checks/affected review, with matching assets; preserve the
other completed browser scopes where relevant code/assets/inputs are unchanged.
No full browser/package/VM campaign follows from this rebase.

Affected final review is the committed observer/feature composition, schema1
preservation, scheduled-versus-manual retry boundary, Settings coexistence and
complete11-unit history/range equivalence. Use retained reviewer and the
applicable general/architecture/scope/risk lanes; do not reopen unaffected UI,
native protocol or fixture design. Deferred managed/native-retirement/creation/
archive suites remain deferred and real Luna remains removed as a rollout gate.
This brief authorizes no deployment or default integration. No launcher,
certificate, graph campaign or product edit by architect is needed.

## Current delivery scope: six UI/capacity units on native0.163

The user's clarified priority and lead's scope decision supersede the11-unit
replay and coordinated-upgrade rollout above. Deliver only the four UI units
`2b1d08b776e30a9c9c3047ee9db05a8f86012fd7`,
`cd5516dd61b48e05c7aa4fd2fc107e7304e6d9d5`,
`e7bfd67e65dd3f9b391dd21691bd34c1b9012da4`,
`f36bfa94cc11a6195f86a05798fb08eab62c0ac2`, docs
`06aa126467f3191ec58e85b03000d17a44a8b930`, and capacity retry
`5f3444194ef37e6dd997adeed708aa866af47943`, on fetched
`f8b94441a6b5066973a72284955b793b301c60ac`. Preserve the current observer
composition/fields/settings described above. Leave system/configuration,
native0.163, client8b605 and existing provider/catalog selection unchanged.
Exclude raw0.164/naming fecb808d, fixture ec93, archive/creation diagnostics
06b6c381/b961daf9 and retirement5ef53277. Preserve their old refs/results for
later work; they are not part of this deployment or its gates.

**No client backport is needed.** Exact8b60554bc10c2a6bcbf9732a8b77ad959c317036
`codex/turn_state.go` already cold-reads the latest failed turn and retains raw
TerminalFailure.Code/Message. Its `continuation.go` proves exact loaded terminal
identity and submission/prompt/queue fences without restricting the error code.
The only new production client dependency in5f344 is IsCapacityFailure. Replace
that helper call in runtime `retryBackend.Observe` with this exact local test:

```go
if o.Code == "other" && s.TerminalFailure.Message == "stream disconnected before completion: Codex is at capacity, please try again later" {
    o.Code = "serverOverloaded"
}
```

Typed serverOverloaded is already preserved by the surrounding assignment.
This is runtime retry policy, not a client/native normalization. Keep native
error/transcript bytes, both live and persisted completion handling, policy
enablement,15-second initial backoff/count/cap, cancellation, auth/provider and
managed execution proof, unknown-send identity, handled/baseline exclusions and
continuation text unchanged. Never replay original input or re-enroll old
handled failures. Keep5f344's negative-message/held-state/history/uncertainty
tests. Retain current docs'0.163 native context description; add only the exact
capacity behavior. No go.mod/go.sum, flake input, vendor, model or catalog change
is necessary. There is no client implementation package for owner3.

Owner0 composes these six units in its owned worktree, preserving any paused
replay effects before ordinary abort/replay or selective rebase. Do not reset
the shared checkout or discard current upstream changes. At session.html keep
incoming progress controls in Settings and our accessible switches/silent queue
markup; keep both docs' intents. Incoming observer files stay intact. The first
UI commit already contains the three presentation-test checkbox→switch locator
corrections; no naming-fixture commit is needed to obtain them. Fold the local
predicate adjustment into the capacity unit and retain a six-unit final series.

Quick checks cover the existing UI unit scripts plus `go test -mod=readonly
./internal/progressobserver ./internal/repository ./internal/web
./internal/workspacecodex -run '^(TestProgress|TestRetryLoadedTerminalStatusController$|TestRetryCapacityObservationRejectsNearMessages$|TestRetryRetentionUnknownAutomaticAtCapHoldsManual$)'
-count=1` from portal in the declared environment. Keep existing test bodies;
do not create another harness. After committed affected review, run the existing
affected browser batch once on this final composition with matching assets;
preserve prior PASS as its actual scope, without a source-hash-only transfer.
Review covers six-unit final intent, the two overlap boundaries, exact local
retry classification on client8b/native0.163 and unchanged observer persistence.
Do not reopen excluded naming/upgrade design or restore its VM environments.

Build only the final composed workspace profile and normal dependencies, then
use the supported same-native profile transition after checking that actual
selected/candidate native identity agrees. Existing system/config pins remain
deployed; no system rebuild/activation is part of this delivery. Post-switch
portal health, preserved observer controls, UI behavior and conversation
continuity are the relevant effects. No canary, managed VM, native-upgrade,
native-retirement, creation/archive campaign or old source/graph/provenance
packet is required. A real conflict, failed relevant check or changed native
identity is handled concretely rather than silently widening this scope.

The configuration's devWorkspace9ba pin may intentionally differ from the
focused application head. The inspected9ba→f8b17-path delta is observer
application/test/docs only, and these six feature units do not alter consumed
NixOS/host modules, installed host CLI/lifecycle interfaces, native package,
protocol selection or cross-system persistent formats. Browser-local UI state
and the already-deployed observer's private fields do not require a system pin
refresh. Current native0.163/client8b inputs remain the same; preserve the35-node
workspace graph except the one intended focused runtime pin. The deployment
checker's hardcoded system/application runtime-head equality describes the
earlier coordinated-upgrade scope and is not an applicable acceptance condition
for this profile-only rollout. Record the intentional head difference and the
unchanged consumed host/module/native contracts in the ordinary rollout record;
do not edit the checker, manufacture a pass or repin/rebuild the system merely
to satisfy it. Actual same-native transition checks still apply. A newly found
host/native/interface change would invalidate this bounded compatibility reason.
