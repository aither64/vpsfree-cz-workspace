# Pi message delivery design

Design owner: architect0. Scope is the three parts in `plan.md`: observation
contention, durable portal admission and safe delivery, and lightweight worker
verification. Application implementation belongs to the retained implementers;
the lead accepts package release and owns allocation. No live session/package
mutation, merge or deployment is part of this assignment.

## Bases and evidence boundary

- dev-workspace starts at deployed `f3bd843f9858b87cef66d0949706f8af16ba9b13`,
  also the fresh remote feature ref
  `origin/2026-11-22-pi-provider-fallback-preparation-reservation-fix`.
  Fresh default `0abe5fe48955b1bcdc8cc368fcb27e11e0676f70` is an ancestor eight
  commits behind it. Preserve those deployed prerequisites. Final review covers
  the full default-to-final-head series and identifies the eight inherited
  commits separately from this initiative. Do not rebase onto the older default
  and lose their behavior.
- codex-web starts at deployed/fresh default
  `3209aa7bf93e2c7067b07494d1b254741812d714`, already selected by the deployed
  portal's `go.mod`. Both own worktrees use branch `2026-11-23-pi-message-delivery`.
- Evidence is bounded to these owning trees, their docs/tests, and same-session
  I0/I1 investigations. No peer-session content is retained here.

## Package release status

| Package | Proposed owner | Status and dependency |
| --- | --- | --- |
| A: observation admission and demand | implementer0 | Completed; lead owns final combined acceptance/evidence |
| B: durable portal input and shared browser contract | implementer1 | Lead accepted and assigned; dispatch integration depends on C ports |
| C: lightweight worker proof and checked input | implementer0 | Lead accepted at 74f4a6f4fbc9d62575defa5a33b44dc5563ee2ae; capacity confirmed |
| V: native delivery verification source | implementer0 | Sufficient settled brief below; lead allocates, commit follows B behavior, long execution follows review |

The lead sequences commits/index operations in the shared feature worktree.
Parallel disjoint edits are safe; no repository merge claim is needed.
Package D is complete after the bounded consistency pass. No substantive design
blocker remains. The lead owns state.md/portal tracking; architect0 edited only
this design and supplied direct current-package interfaces to the implementers.
No application test or performance result is claimed from this read-only design
investigation. The stable session page is
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-23-pi-message-delivery/.

## A: observation admission and demand (settled)

### Evidence and change

At the deployed base, `pi_workflow_observation.go:refreshRequested` calls
`reconcileOriginal`, which unconditionally invalidates the snapshot. A successful
refresh followed by `drain` calls `questionService(ref, false).DeliverNext`.
`piquestions.Service.DeliverNext` enters `Admit` before reading/selecting any
response. Its mutation admission waits for the exclusive runtime lock and
invalidates again, even for an empty/all-Accepted store. This destroys a fresh
observation and creates more demand. Failed in-flight refreshes do not consume
new display demand; native events mark all known conversations for drain.

Implement a cheap read-admitted persisted-work preflight before exclusive question
delivery. It must inspect validated owning records, without native calls or a
mutation grant. Empty/all-Accepted records return without exclusive admission,
mutation invalidation or native work. A positive preflight is only a scheduling
hint: reread and select the oldest eligible response under the existing exclusive
admission before preparing/sending. Preserve caller, origin, policy, current
authority, scope, package and access checks there. Nonpending handoffs remain
Lookup-only; Unknown and NotSubmitted never become fresh sends. Plan acceptance
already has a read snapshot; retain its actual-work checks.

Remove unconditional reconciliation invalidation. Invalidate when persisted or
native evidence actually changes, before effects where the existing ACK contract
requires it. Unchanged receipt lookup or an empty drain must not discard a valid
snapshot. A failed proof stays unavailable; a stale snapshot never gains authority.

Track one outstanding/in-flight observation per conversation with distinct
display versus real delivery/invalidation demand. Coalesce GETs against the same
in-flight revision even when proof fails. Back off failures (initial 1 second,
exponential to 30 seconds); repeated GETs and duplicate events cannot reset the
deadline. A genuinely changed runtime/attachment/revision invalidates immediately,
but repeated churn still gets at most one pending refresh and bounded attempts.
Retain real accepted-intent work durably in its existing store and keep one
delivery demand until serviced or positively blocked. Display failure must neither
manufacture delivery nor lose accepted intent. Success resets backoff. Use the
existing display worker/tick/wake mechanism; no new per-view goroutine/ticker.

Foreground priority is an in-process scheduling rule, never an authority bypass.
Normally defer starting background work for a session with a waiting/active
foreground Send and cooperatively cancel read-only background work. Yield between
conversations and reconciliation/attachment/proof/drain stages. Never cancel an
admitted native effect or its receipt continuation. Do not hold the observation
map mutex while waiting for runtime/native/store locks.

The lead accepted a bounded fairness refinement: when due background work remains,
allow at most eight foreground admissions, then reserve one eligible round-robin
background conversation pass before admitting another foreground burst. Failed
work remains backed off and cannot reserve until due. The reserved pass is
protected from cooperative foreground cancellation; already admitted foreground
effects finish normally. Its ordinary bounded context remains in force. Release
the reservation on every background exit, including failure/timeout. Parent
deadline expiry is a failed attempt subject to backoff, not a foreground yield.

Use one context-aware helper
`acquirePiForeground(ctx, SessionRef) (release func(), err error)`. It atomically
checks the burst/reservation and registers the granted foreground turn under the
existing scheduler mutex; when blocked it waits on existing wake/completion
channels without that mutex. Cancellation before grant creates no registration;
successful callers immediately defer the idempotent release. This replaces the
earlier separate wait/register proposal: a timing gap is not fairness evidence.
Both A's message resolver and B's dispatcher call it before runtime admission.
Existing locks and fresh checks remain decisive. A reserved background pass can
still cost the existing six-second ordinary worker budget (plus completion of an
already admitted effect); disclose and measure that cost against healthy latency,
never infer <1 second from the burst constant. No new authority lock is introduced.

### File ownership and interfaces

A owns `portal/internal/web/pi_workflow_observation.go`, its tests, a new focused
observation scheduling test if useful, `portal/internal/piquestions/service.go`
and its tests if a reusable preflight is needed, and the observation sections of
`docs/pi-questions.md` / `docs/pi-runtime.md`.

In `portal/internal/web/pi_workflows.go`, A owns only `drain`,
`reconcileOriginal`, and the small foreground registration/release hook at the
start of `resolvePiBackend` message mutation admission. A may add a narrowly
named read-admission helper if existing `withRead` suffices. It does not redesign
`pi_team_admission.go`, Send/Verify, attachments, handlers or browser dispatch.
B/C must not edit these A regions while A executes; their changes to other
regions can proceed after lead allocation. Report helper signatures to architect0
and lead before B integration. Shared fixture writes and Git mutations use the
lead's exclusive windows.

### Acceptance and quick checks

- Hold a shared session lock: an empty/all-Accepted question drain completes
  without waiting for exclusive ownership, native calls or invalidating a fresh
  observation.
- Race a positive preflight with changed response, member/incarnation, access,
  origin and policy. Exclusive reread refuses stale work; two drainers cannot
  prepare/send twice. Original handoff/Unknown/NotSubmitted remain lookup-only.
- Repeated failed proof, in-flight GETs and event churn produce bounded refresh
  and Host.Inspect counts. A foreground Send gets the next available admission;
  other sessions and eventual background reconciliation still progress.
- Repeated no-op reconciliation preserves the fresh result. Attachment loss,
  same-generation worker replacement, stale sequence and actual invalidation
  remove its authority. Recovery after failures services pending delivery.
- Focused Nix-shell Go tests: `go -C portal test -mod=readonly
  ./internal/piquestions ./internal/web -run '<focused observation/drain tests>'`;
  include existing question service and workflow observation tests. Run the
  owning package's quick suite and required hooks before commit. No longer
  integration/performance campaign before independent final review.

Evidence: exact base/head, changed files, focused test commands/results,
deterministic refresh/native call bounds, unchanged wire/record schemas, and any
remaining scheduling limit. A changes no persisted format, native protocol or
receipt semantics, so is independent of B's queue state machine and C's worker
capability.

## B: durable portal delivery (settled)

The lead accepted a private portal-owned SQLite store, an additive opt-in shared
HTTP/browser contract, and C's checked native input port. A queued receipt means
the portal durably owns the original input, not that Pi accepted it. Direct team,
communication, questions/Plan, creation and utility consumers keep their existing
native acceptance contracts. Do not route those producers through this queue.

### Shared HTTP and browser interface

Extend codex-web's neutral optional operations with an application-owned durable
delivery provider. Use `/conversations/:id/deliveries` for POST admission and GET
current pending/recent statuses, and `/conversations/:id/deliveries/:clientId`
for exact status. Add an optional `durableDelivery` capability. The existing
`message`, native `queue`, SendResult and native Pending contracts are unchanged.
An absent capability/provider returns unsupported, without selecting another
backend. The legacy constructor and standalone example need not implement it.
Receipt reads remain available through their owning local authorization when
retained queue records exist but new admission is unsupported. Collection metadata
separately reports whether a new input can be enqueued; losing a worker capability
must not hide or replay an existing delivery. B's neutral provider name is
`backend.DurableDeliveries`; naming its shared values is B-owned.

POST input is version 1, original `clientUserMessageId`, text, ordered attachment
IDs, explicit `delivery` (`steer`/`followUp`, or empty legacy mode when explicitly
advertised), and an opaque server-derived `selection` digest. It has no socket,
native target, permission, effective settings or generation supplied as authority.
The selection digest binds the server's full saved target/settings/policy tuple
shown by the local delivery metadata response; it cannot authorize arbitrary
browser settings. Metadata and the selected settings controls must agree before
Send. A stale selection refuses new work admission; a definitive refusal may
persist only the negative admission identity described below.

Successful admission returns HTTP 202 with a separate versioned DeliveryStatus
envelope, never a SendReceipt: original ID, scope, mode, sequence, state, timestamps
and optional exact native receipt or bounded failure reason. Valid states are
`queued`, `dispatching`, `pending`, `sent`, `not_sent`, `unknown`. The new envelope
also has optional `retired` (boolean, omitted/false by default); true requires
`unknown` with no acceptance receipt and the exact owner proof described below.
Only `sent`
contains native acceptance evidence and may display Sent. `queued` is durable
portal acceptance; `pending` is positive native enqueue; neither means consumed.
HTTP 202 itself never implies Sent. Same ID plus identical immutable request
returns the existing status, including after response loss; changed text, files,
mode or selection conflicts. IDs preserve exact supported spelling.

Delivery routes validate `X-Workspace-Pi-Generation` syntax/cardinality but do
not require that browser observation to equal CURRENT. Stable scope/incarnations
and fresh local identity/access joins authorize status and identical create-or-get
after a successor, without a page reload. Preserve resolver-to-Verify consistency
within the current request and native routes' strict generation checks. A new ID
still requires the current full selection digest; changed existing-ID payloads
conflict. Test old valid headers across a successor, stale new selections,
malformed headers, revoked/wrong scope and unchanged native-route refusals.

GET collection is bounded: all outstanding rows (maximum 20 per conversation)
plus a combined recent terminal/retired-disposition window (up to 100), with exact-ID lookup retained for old
attempts. Collection status is useful after closing/reopening a tab, independent
of browser sessionStorage. Do not truncate unresolved rows or delete durable
deduplication identities by age. Do not add edit/reorder/cancel API in this scope.
Only proved retired Unknown leaves outstanding capacity; ordinary Unknown still
counts and blocks. Both shared validation and browser consumers use this rule.

### Definitive local admission refusal

Lead accepted the following minimal recovery correction. A generic POST failure
cannot prove that another same-ID create-or-get did not admit work. Keep a private
negative identity in the same SQLite authority, keyed by stable scope/original ID,
with version, the exact canonical DeliveryRequest, bounded refusal code and
timestamp. Retain the authentic server-resolved `agentbackend.ConversationRef`
as private scope evidence, including its real native ID and incarnations. Validate
it with the existing strict local joins/ref codec and bind the opaque scope to
that same stable scope. It is neither a SubmissionRef nor execution selection:
it grants no work/native effect and does not assert acceptance. Never synthesize
a native ID or expose this private evidence in the browser refusal proof.
It is not a work row and has no fabricated submission ref, execution
selection, sequence or native receipt. Valid local scope/access and request
syntax are prerequisites; auth/transport/storage/missing cases grant no proof.

`Reject(scope, request, code)` uses the same serialized write transaction/key as
Admit. First resolve an existing admitted or refused identity: identical request
returns its saved status/proof, changed request conflicts. Otherwise durably
commit the negative identity. Admit must consult both identities before creating
work; concurrent Admit/Reject has one winning disposition. Refusal IDs cannot
later enqueue, survive restart/preflight and are retained indefinitely. Do not
introduce another dispatcher, retry mechanism or transitional migration.

Settle the new shared types as:

```go
type DeliveryNotQueuedProof struct {
    Version int                 `json:"version"` // 1
    Scope string                `json:"scope"`
    Request DeliveryRequest     `json:"request"`
}
type DeliveryError struct {
    Code string
    NotQueued *DeliveryNotQueuedProof
}
```

The error envelope exposes `notQueued: true` and `proof` only for this validated
durable result. Proof.Request includes version, original ID, selection, canonical
message, ordered attachment IDs and delivery mode; no reason string is authority.
The shared handler validates it against the authenticated scope and exact
canonical submitted request. The client/helper checks the complete typed proof
against the saved attempt (absent attachment list canonically equals empty;
preserve its order). A boolean alone, wrong version/scope/ID/selection/text/files/
mode, malformed proof, or generic error must not clear local state.

Only the matching proof lets the helper remove its browser admission. Preserve
the current draft/files and surface the refusal; a later explicit Send uses the
current selected settings and a new ID. Do not automatically Send, clear a newer
draft or downgrade to legacy. Native NotSubmitted and queue not_sent are distinct
contracts. Tests cover both Admit/Reject race orders, exact/changed duplicates,
lost refusal reply and restart, late original POST after a new explicit attempt,
forged/mismatched proof and generic errors retaining the saved admission.

The final unpublished queue v1 includes these negative identities directly;
disposable earlier fixture schemas are reset. B batches this provider change with
retired status into one final shared-provider commit/check/pin set. B owns store,
API/browser/preflight integration; lead owns any new visible text.

### Shared browser continuation

Add shared client methods and a small durable-delivery helper in codex-web; retain
the existing durable storage/target identity primitives and receipt rendering
conventions. Both shared mountConversation and the actual dev-workspace composer
must recognize the new capability and use those methods. The portal's existing
`createMessageDispatch` remains for legacy dispatch; it stops owning native sends
once the server has acknowledged this original input. No backend-name branch is
needed in shared UI: capability and typed status choose behavior.

Save the original attempt in browser durable storage before POST and use that same
ID when the response is lost. The new endpoint is explicitly create-or-get;
repetition can safely create a missing queue row because it cannot bypass the
server's durable dispatch claim. This does NOT change legacy `/message` retry:
`retry:true` with no native receipt remains Unknown. Never convert an already
uncertain legacy attempt into a fresh durable submission or mint a replacement
automatically. On a server queue acknowledgement, clear only the submitted draft
revision; preserve text/files edited while the request was in flight. Reopening
loads server statuses and original text under the exact current conversation
scope. A late reply cannot update another member/session incarnation.

The durable composer may bind from the already scoped ready page identity/native
ID before transcript readiness. Disable new admission until local metadata is
valid. First metadata may initialize visibly empty settings controls once; later
refresh/Send must not silently replace a selected model, effort or policy mode.

Lead accepted a separate latched selection baseline in both the actual portal
composer and shared mountConversation. Latest polled metadata/status is distinct
from the initially verified selected scope, opaque digest and visible summary.
Background metadata polls and transcript refresh never advance this baseline.
A different digest makes it stale and blocks new durable Send, even when visible
model/effort/mode still match. Preserve current draft/files and saved original IDs.
Only successful explicit settings/mode save followed by exact same-scope local
confirmation, or an existing explicit page/selection refresh, establishes a new
baseline. Late, failed or wrong-scope responses cannot re-arm it. Ordinary status
refresh and original-ID recovery must not serve as implicit selection confirmation.

Send captures the latched scope/digest/visible summary plus draft/files before its
fresh GET, then compares exact returned scope/digest and all visible settings/mode
against that capture. Apply the same rule in both consumers. The current opaque
digest includes execution generation/binding evidence, so requiring explicit
refresh after those alone change is an accepted conservative limit for new Send.
Already-admitted queue continuation and status recovery remain unchanged. Do not
add a logical-digest API, new UI action/framework or reinterpret native state.

Focused checks: a background poll changes digest while visible values remain
equal before Send, yielding zero POST and no draft/files/ID loss; explicit save/
refresh confirms and re-arms only the exact current scope; late/failed/wrong-scope
confirmation cannot re-arm; unchanged polls remain safe. B owns consumer source
and tests, using shared mount metadata/submission/settings-save paths and actual
portal metadata/submission/settings/mode confirmation paths. V interfaces/source
are unaffected. Lead owns the separate commit/history direction and writing pass.

Metadata failures do not select legacy
Send; explicit unsupported capability permits the retained legacy path only for
new work, never replay of an existing durable attempt.

Use Queued, Sent and an actionable failure presentation. `not_sent` permits copying
the saved text into a new draft for an explicit new submission. `unknown` offers
original-ID status checking and the existing explicit recovery route; it never
offers automatic resend. Hiding a card is presentation only. Lead owns the final
user-facing writing pass. No unconditional generic-202 success path may consume
the new envelope as a legacy receipt.

### Local admission: no Pi or long runtime lock

Use a separate resolver path for the new delivery operations. Its required
Verifier verifies application/local scope only and is documented as such. It
must not call Runtime.Bind, Verify, InputDelivery, Host.Inspect, workflow proof,
transcript reads, attach/load/start, or acquire the session runtime shared or
exclusive lock. Those locks may be held across slow native effects. This new
path grants only durable storage/read authority, never native execution.

Before storing, validate exact origin, bounded request/ID/mode, current selected
package invocation, ready durable session binding and authority projection,
session/member incarnations, native ID, saved member access and lifecycle/provider
admission, and the server-selected local settings/policy tuple. Reuse the existing
strict local readers and identity joins (including retained creation/catalog and
tracking evidence); extract the native-free part rather than skipping checks.
C supplies a strict disk-only selection reader for the saved conversation record
and CURRENT frozen package. Missing, malformed, pending settings/policy, held,
contradictory or unsupported records refuse. No latest-default inference.

Local selection is an observation at admission, not a promise that it cannot
change afterward. Read/join the relevant local tuple, prepare/pin the exact
attachments through the existing uploads owner, then reread and compare the tuple
before the short queue commit. A conflicting change refuses before acknowledgement;
a change after that final observation is caught by dispatch. These atomic-file
reads do not acquire a native-effect lock. They do not claim a cross-record
transaction or allow contradictory revisions. A queue receipt remains truthful
if authorization later changes: it saved input, it did not authorize execution.

Hold only existing shared package-transition admission (recheck the invocation
after acquiring it), the attachment store's short local transaction, and the
queue's short SQLite transaction as needed. Its HTTP MutationLock, when required
by the shared handler, is queue-admission-only; do not reuse `messageLock`, which
may be held by a slow native send. Never hold the SQLite write
transaction during attachment work, native calls or runtime-lock acquisition.
Package switching can legitimately make local admission unavailable; normal
Send/observation effects must not block its queue receipt. Pending lifecycle at
the local check refuses. Test queue admission while the session's exclusive
runtime lock is held by a blocked fake native send, not just with a fast mock.

Upload Prepare already freezes scope/kind/original-ID/text/file order and wire
text and pins files. Reuse it before acknowledgement. The queue stores both
display text and exact prepared wire plus ordered attachment IDs/scope. A crash
after upload pinning but before queue commit can leave a conservative pending
pin; same-ID retry recovers it. Never report Queued before both are durable. A
native observation releases references through the existing owner; failed or
ambiguous records retain files unless the owning positive no-effect cleanup
contract explicitly permits release. Do not invent age-based attachment cleanup.

### Persistence and dispatch state machine

Put the queue in a private version-1 database in the existing workspace-scoped
portal state directory, e.g. `portal/<workspace-hash>/input-delivery.sqlite`.
Use pinned `modernc.org/sqlite`, indexed exact-key transactions, WAL and full
synchronization, private files/directories and synced newly created ancestors.
Do not repurpose codex.Client's private submission database or add artifacts to
Pi member/submissions roots: retained readers strictly whitelist those formats.

Minimum immutable row: full stable conversation reference; exact original ID;
monotonic per-conversation admission sequence; canonical request/digest including
display and prepared wire, ordered attachment IDs/scope, mode and selection;
full accepted RuntimeRef/handle, settings, policy mode/revision/digest and access;
saved native SubmissionRef/SendInput; schema and accepted timestamps. Mutable
columns hold phase, bounded reason, next-attempt time for pre-dispatch delay,
the monotonic owner-proved retired disposition,
actual dispatch RuntimeRef/handle/generation/time and exact terminal receipt. Unique key is stable
conversation plus client ID, never generation. Scope/phase/sequence indexes avoid
loading all history or receipts for an admission/lookup. Use conditional updates
for one winner at dispatch; do not add a distributed lease subsystem.

1. Commit `queued` only after local validation and upload pinning. The commit is
   the durable receipt boundary. HTTP disconnect afterward cannot cancel work.
2. A server-owned bounded worker scans indexed due rows on startup and wakes on
   admission/state change. It survives tab closure and does not rely on polling
   browsers to advance delivery. Use a small bounded worker pool (at most four),
   at most one native dispatch in flight per conversation, and round-robin due
   conversations. There is no network/native wait inside a DB transaction.
3. Before claiming dispatch, call A's
   `acquirePiForeground(ctx, SessionRef) (func(), error)` and acquire the existing transition,
   runtime exclusive and message admission in their established order. Revalidate
   current host package, lifecycle/provider admission, exact bound conversation,
   full CURRENT runtime/handle, saved access/settings/policy, attachments and
   required frozen capability. A definitely-unsent queued row may use a proven
   ready successor as specified below; that changes execution evidence only.
   No logical retargeting, settings refresh or worker start.
   Prove live worker identity/instructions/capabilities and required workflow
   attachment/ACK. Hold ordinary effect admission through the native enqueue ACK.
4. A transient failure strictly before dispatch keeps `queued` with bounded
   backoff, including an unavailable/unloaded/preparing successor. Proven logical
   target/access/settings/policy/instructions/files or capability changes become
   `not_sent` with an actionable reason. Execution generation or binding revision
   changes alone do not establish a logical change. No record past the dispatch boundary can take this
   shortcut. Do not scan history to decide a local pre-dispatch outcome.
5. Commit `dispatching`, its original native ref and actual verified execution
   RuntimeRef/handle before invoking C's checked port. Exactly one conditional
   transition from queued owns this call. A crash
   after this commit, even before a socket write, is conservatively ambiguous;
   restart never claims it again. This is the documented no-replay boundary.
6. C rechecks the frozen logical tuple and freshly claimed execution evidence
   under the supervisor conversation lock immediately
   before the original native delivery path. Positive native Pending becomes
   `pending`; exact Accepted witness/receipt becomes `sent`; positively proved
   no-effect refusal becomes `not_sent`. Transport timeout/EOF, persistence
   uncertainty or unsupported/malformed reply after the boundary is `unknown`.
7. `dispatching`, `pending` and `unknown` recovery is observation only through the
   saved original ref. Fresh native receipt proof may advance to sent; a missing
   receipt remains unknown. It never replays, changes ID, changes digest or
   reconstructs acceptance from matching text. A new runtime generation does not
   open another attempt. Queue-store failure after native Accepted is recovered
   by original receipt lookup.

Preserve admission order into native dispatch. A positively acknowledged native
followUp may be passed by a later steer so steering still acts on the active run;
the native queue owns consumption order. Unretired Unknown or in-flight enqueue
blocks later dispatch for that conversation. A terminal proved not_sent or exact
explicit retirement can release the next row. Other conversations continue fairly. Native capacity is bounded at 20;
the portal must not claim infinite admission or retry an immutable terminal
native NotSubmitted. An unavailable native runtime does not consume the local
queue receipt budget.

Lead accepted a bounded responsiveness correction for original-ref observation:
only a positively proved Pending result uses
`next_at = min(now + 200ms, persisted DispatchAt + 1s)` while claim age is less
than one second. Thereafter use the existing two-second interval. Unknown and
errors keep two seconds. Persisted DispatchAt anchors the window; GET, process
restart and repeated lookup cannot restart it. Use existing fields and scheduler
tick only, with no new timer/event subsystem, schema, native Send or receipt change.

Among eligible Pending rows order by next_at then sequence, preserving queued
FIFO, unretired Unknown/inflight barriers, one active operation per conversation
and the four-worker round-robin bound. An old followUp must not monopolize receipt
observation ahead of a later steer or other conversations. Test deterministic
lookup counts/window expiry, long-Pending fallback, restart without window renewal,
old followUp/later steer and peer progress before B's final owning suite. Observe
the existing 250ms scheduler tick and call costs in measured public Sent latency;
this cadence does not establish a strict public one-second result. V's separately
proved native-Accepted timing hook remains the acceptance metric.

### Explicit retirement preserves original Unknown

The existing explicit runtime input-retirement operation remains the sole owner
of this recovery. It preserves original native receipt bytes/Unknown forever and
permits a distinct later input after its stopped predecessor and successor proof.
Do not add a queue retirement/cancel/reorder command or infer retirement from a
held state, arbitrary reason, missing receipt or synthetic Unknown projection.

C's new queued-only Lookup result carries unchanged Status plus RetiredUnknown.
True requires the raw exact original owned receipt and complete strict
`readInputRecoveries`/`retiredInput` proof: exact original ref/input/settings/digest
and receipt SHA, retired phase, source/current-successor lineage, valid terminal
stop/RetiredAt and validated member snapshots/history identity. Decode the whole
owning recovery directory; prepared, missing, different ref/owner or any malformed
record cannot grant true. Existing schema-1 receipts and legacy lookup/retry
envelopes remain unchanged. A retained-owner fallback must establish the same
proof through its owning codec and preserve unavailable/unsupported outcomes.

B accepts this flag only from successful original-ref Lookup after validating
the returned unchanged status against Admission. Persist a monotonic indexed
retired disposition only with phase unknown/no acceptance and existing dispatch
evidence. Never change Admission, original receipt/dedup identity or Unknown to
sent/not_sent/queued. Due selection and the claim CAS skip only proved retired
Unknown as a barrier and never select that row for Dispatch. Retired rows leave
active capacity and join the combined bounded 100-row recent disposition window;
exact-ID reads remain indefinitely. Other Unknown rows still block. Later distinct
inputs retain all fresh authority, settings, runtime-continuation and native
admission checks; the portal flag alone grants no native authority.

Focused tests: completed exact retirement permits a later distinct input without
any call for the original ID; original receipt bytes/status/dedup stay unchanged;
portal restart and native successor preserve the disposition; prepared/missing/
wrong-ref/source/lineage/malformed records and arbitrary reason strings cannot
release; more than 20 retired records obey work capacity/collection bounds while
old exact-ID lookup remains available. C owns proof/new lookup type; B owns its
adapter, indexed disposition/store, shared status and collection consumers.

### Restart boundary and pre-claim successor continuation

The lead accepted this correction to the initial full-runtime-equality rule:
generation is execution evidence, not a selected logical target or deduplication
namespace. A row durably still `queued` has never crossed this queue's dispatch
claim and may continue after native replacement. Preserve its entire immutable
Admission, browser selection digest and original Ref/Input/ID, including the
original admitted runtime as provenance. Do not rewrite these to a new selection.

Under fresh ordinary effect admission, resolve the exact original conversation
(workspace/session/member incarnations and native ID), access, full settings,
full policy, instructions digest, delivery mode and attachment scope/wire. All
selected logical fields must remain exact. Validate fresh owning binding joins;
its revision may change only when those strict joins still prove the exact
original logical fields. An unrelated revision is not permission to retarget,
nor a reason by itself to reject the legitimate successor publication path.

C's narrow read-only continuation method must prove that the complete original
RuntimeRef occurs in the connected predecessor chain of the complete exact
CURRENT RuntimeRef in existing strict runtime records. Compare full refs, not
just generations, InstanceID or membership in an arbitrary history map. Existing
record validation supplies launch/config digests, configured roots/account
bindings, one instance, unique generations and the complete ReplacesRequestID
chain. This proves ancestry only; it does not prove native readiness or grant
effects. ReadInputSelection, current authority and native identity/attachment/
settings proof still run normally, with current evidence repeated before effect.
No implicit Load, Ensure, start, resume or worker upgrade is allowed.

B's Driver claim callback accepts `ExecutionEvidence{Runtime, Handle}` and stores
DispatchRuntime/DispatchHandle and the actual DispatchGeneration in the same
queued-to-dispatching CAS. B passes the fresh verified InputSelection plus the
original admitted RuntimeRef and unchanged native Ref/Input to C. C independently
rechecks the exact original-to-current runtime chain and original ref digest;
B's assertion alone is insufficient. A successor race before claim either
revalidates safely or leaves queued; after claim it follows the no-replay rule.
Never select another execution after that claim. Implement this directly in
final queue schema v1; earlier unpublished/unconsumed fixture DBs are disposable,
so no transitional migration is added.

| Durable phase at interruption | Portal restart with same native owner | Supervisor/worker replacement |
| --- | --- | --- |
| queued | Resume the same ID/ref after fresh checks. | Wait/back off while unavailable; continue once through a proven ready CURRENT successor with exact logical selection. Proven incompatibility is not_sent. |
| dispatching, including claim-before-wire crash | Original-ref lookup only. Exact Accepted becomes sent, exact live Pending stays pending, missing/unproved evidence is unknown. | Same lookup-only rule through original owner lineage; no new dispatch or execution selection. |
| pending | Retain only with exact live owner; reconcile eventual exact Accepted. | Lost live owner means unknown unless original acceptance is proved; never reconstruct native queue. |
| unknown | Original lookup may prove sent or native NotSubmitted; otherwise unknown. | Identical lookup-only rule across generation changes. |
| unknown + owner-proved retired | Retain Unknown and original dedup; release only ordering/capacity for distinct later work. | Preserve the exact retirement proof/disposition; never dispatch the original again. |
| sent / not_sent | Preserve terminal evidence, no attempt reset. | Preserve terminal evidence; generation is not a new ID namespace. |

Focused tests cover queued portal restart and legitimate native successor with
exactly one append/same ID; actual successor binding publication revision;
unloaded/preparing/unavailable successor with no implicit start; wrong/noncurrent/
unrelated full runtime ref and each logical mismatch; successor races around
proof/claim/native check; actual execution fields committed at claim; immutable
repeat-ID request/status after continuation; crash after claim before wire with
zero redispatch; lost Pending owner and later original Accepted reconciliation.

### Ownership, checks and completion evidence

B owns codex-web `conversation/backend/operations.go`, additive delivery types,
`conversation/backend.go`, `conversation/handler.go` (or an extracted delivery
handler), `conversation/assets/conversation.js` and a small shared delivery module,
their external/HTTP/browser contract tests, and `docs/reference.md` with links to
owning storage semantics. It must cover the shared mount as well as portal use.
Do not generalize or migrate the Codex native queue/database.

In dev-workspace B owns new `portal/internal/inputdelivery/` store/dispatcher
types and tests, new `portal/internal/web/pi_input_delivery.go` and tests,
delivery initialization/shutdown hooks in `server.go` / `operation_state.go`,
local resolver selection in `pi_workflows.go` (outside A's drain/reconciliation
and scheduling hook), the composer delivery integration in `static/app.js`,
upload integration tests (change upload owner only if its existing contract
cannot meet pinning), and focused browser tests. B owns the queue portions of
`docs/workspace-portal.md` and the shared backend contract README. C owns all new
native ports/local record reader. B consumes those ports; it does not patch
native receipts or duplicate their codecs.

B also owns queue retention/package preflight integration in
`portal/cmd/workspace-portal/pi_team_preflight.go` and tests,
`libexec/workspace-session-backends.rb`, `libexec/workspace-host` and focused host
tests, plus its additive portal capability field in `runtime-contract.json`.
C owns separate fields in that JSON; serialize that short edit. Extend the
existing preflight source inventory with queue dependencies using a strict local
read-only queue reader, rather than a second daemon or compatibility manifest.
The source tree's inspection of arbitrary retained state creates no queue DB.

Release B now for shared API/browser/store/local admission work against the
settled port contract below; dispatch integration awaits C's checked port and
mixed-version tests. Do not advertise the feature until the complete wiring is
present. Pin codex-web Go dependency and browser/Nix inputs together; lead
sequences publication/pin windows after its commit. No fake production fallback
to make incomplete wiring pass.

Quick tests: indexed atomic same-ID and changed-payload races; failure at commit;
zero native/Host.Inspect calls and no runtime-lock wait at admission; uploads and
scope selection; full dispatch boundary fault injection; GET privacy/scoping;
legacy HTTP/native Pending/Unknown contracts; actual composer draft/status/tab
handoff contracts; strict package preflight with missing/malformed queue state.
Use owning Nix environments, focused `go test -mod=readonly`, Node contracts and
required hooks. Deliver exact heads, affected files, commands/results, schema
provenance (new queue v1 only; no native migrations), docs and remaining gaps.

## C: lightweight proof and checked input (settled)

C owns the runtime dependency needed by B as well as part 3. The supervisor and
worker play different roles: the supervisor owns durable receipts/locks/settings
and checked enqueue; the JS worker owns actual native session/instruction proof
and the unchanged persistence witness. A runtime's frozen AppStorePath packages
both. An installed portal contract alone cannot confer either capability.

### Local selection and checked port

Provide `ReadInputSelection(ctx, handle)` as a strict disk-only Manager reader,
returning full RuntimeRef, handle, effective settings, retained policy
mode/revision/digest, instructions digest, held/pending state and frozen
checked-input support. It validates CURRENT/request lineage and the existing
conversation record/ownership codecs. It does not lock the live runtime, call
Host.Inspect, load native history, make an RPC or grant effect authority. Keep
pending settings/policy and malformed optional fields visible as refusal. B uses
this plus portal binding/access/creation evidence, never as native readiness.

The settled B/C Go seam is the following optional interface in piruntime (normal
JSON casing follows existing runtime conventions). B may fake this interface for
focused store/web tests; C implements it on Manager. No main Controller expansion
or legacy SendRequest field is needed.

```go
type InputSelection struct {
    Runtime RuntimeRef
    Handle agentbackend.ExecutionHandle
    Settings EffectiveSettings
    Policy *ToolPolicyTarget
    InstructionsDigest string
    CheckedInput, Held, PendingSettings, PendingPolicy bool
}
type QueuedInputRequest struct {
    OriginalRuntime RuntimeRef
    Selection InputSelection
    Ref SubmissionRef
    Input SendInput
    Delivery string
}
type QueuedInputResult struct {
    Status SubmissionStatus
    // True only for a positively proved refusal before native dispatch.
    // It is separate from Status so it cannot fabricate a native receipt.
    NotSubmitted bool
    Refusal string
}
type QueuedInputLookupResult struct {
    Status SubmissionStatus
    RetiredUnknown bool
}
type QueuedInputController interface {
    ReadInputSelection(context.Context, agentbackend.ExecutionHandle) (InputSelection, error)
  PreflightQueuedInput(context.Context, agentbackend.ExecutionHandle) error
    ValidateInputRuntimeContinuation(context.Context, RuntimeRef, RuntimeRef) error
    DispatchQueuedInput(context.Context, QueuedInputRequest) (QueuedInputResult, error)
    LookupQueuedInput(context.Context, SubmissionRef) (QueuedInputLookupResult, error)
}
```

`Policy == nil` is an explicit absence in a valid legacy record, not permission
to synthesize Default mode. When present, preserve the full validated policy
including ordered tool sets, and compare it under the supervisor lock. The
selection digest binds absence/presence. `CheckedInput` comes from the frozen
CURRENT contract; Held/Pending flags are local reasons to refuse admission, not
cached live proof. A valid unloaded conversation mapping makes
ReadInputSelection return ErrUnavailable for new admission; do not fabricate a
Held flag or imply native readiness. A valid retained package without the new
capability returns CheckedInput=false. Existing delivery status/receipt reads
must not depend on a successful new-admission selection or load the worker.
Lookup may return only Status.Phase Unknown with RetiredUnknown=false for genuine absence;
Accepted/Pending must carry and validate the exact original receipt/ref evidence.
Only Dispatch may return the separate positive pre-effect refusal. Errors alone
never prove non-submission. B never stores a synthetic native Accepted receipt.

Add a frozen package field `piCheckedInput: 1` and new versioned supervisor
operations `input_delivery_checked_v1` and `input_lookup_v1`. Request types are
separate from the old strict `conversationRequest`/SendRequest wire. The dispatch
request contains original admitted RuntimeRef, freshly selected exact handle,
original SubmissionRef, SendInput, delivery mode,
expected EffectiveSettings and policy mode/revision/digest. Recompute the native
SubmissionDigest and require equality. For explicit modes use the unchanged
`pi-delivery-v1:<mode>` context and original Retry=false. For an advertised empty
mode preserve the exact existing legacy context/semantics. The continuation
method's arguments are original admitted runtime followed by expected CURRENT;
it is disk-only, with context checks and strict full-ref chain validation. Checked
dispatch repeats that owning validation and validates original ref/input/settings
digest against the new execution evidence before entering the native path. It
never mints a replacement ref or trusts a browser/web assertion of ancestry.

Under the same `c.mu` that protects native input admission, recheck the full
conversation/generation/settings/policy tuple before any receipt/native effect,
then enter the existing receipt/native input implementation. Refactor internally
to avoid releasing/reacquiring that lock between check and enqueue. The new
operation belongs in `workflowMutates`, preserving initial invalidation ACK,
permit validation, instruction proof, held/pending checks and host-tools policy.
Do not silently call ordinary Send when the port is absent. A mismatch is a
typed positively pre-effect refusal; errors after invoking the native send path
must carry the original ambiguous outcome, never a broad NotSubmitted wrapper.

For an already-existing exact original receipt, Dispatch may resolve that evidence
under its owning lock before comparing mutable current settings/policy. Validate
the request shape, stable subject and owning route first, and require exact saved
ref/input/settings digest agreement. This branch is lookup-only: no receipt
creation, send, or fresh dispatch grant. It preserves Accepted/Pending/Unknown
after settings changes; an existing Unknown must never become a positive
NotSubmitted merely because selection is now stale. A changed existing ref is a
conflict. Only genuine absence enters fresh frozen-selection checks. Stale runtime
authority cannot be adopted through this branch; use the separately owned Lookup
path or report unavailable/unknown when original evidence cannot be resolved.

Lookup takes the full original ref and verifies the saved immutable input/settings
digest and native witness. It may project Pending only from the supervisor's
exact live input owner; saved dispatching/prepared without that owner is Unknown.
Missing receipt is Unknown. It has no enqueue branch. Older receipt/schema owners
and utility roots stay unchanged. Status remains valid for original receipt
reconciliation after current generation/settings changes; fresh execution is
separately forbidden. Use original owner/lineage recovery when no current owner
can answer, not a new native attempt.
Only the new `input_lookup_v1` response uses QueuedInputLookupResult. Its strict
envelope and Manager validation require RetiredUnknown to accompany an exact raw
Unknown receipt with complete owner retirement proof; legacy envelopes do not
gain fields. C's scalar identity work remains independent of this lookup delta.
For a retained non-fork owner without the new lookup operation, existing
VerifyCreation with exact mapping CreationID/HistoryRef and original receipt ref
may supply its existing verify_history proof. It must load/start/send nothing.
Fork or otherwise unsupported/unavailable proof remains Unknown/unavailable;
disk metadata or matching text alone is not a replacement proof.

### Lightweight identity

Add frozen `piConversationIdentity: 1`, a distinct `identity_v1` worker/supervisor
operation and strict scalar reply. Include native session ID, owned history path,
provider/model/thinking, persisted/held/busy state, instructions digest and
supported input version needed by callers. Derive identity from the actual live
SessionManager/AgentSession plus checkInstructions, not just echoed request data.
No getBranch(), transcript construction, serialized history/hash or unrelated
receipt scan is allowed on this proof path. Existing snapshot/init/send replies
retain exact legacy shapes.

Manager Bind/adapter Verify and new capability checks choose the light path only
from the CURRENT runtime's immutable package contract, then perform a real fresh
request. workerProcess must compare InstructionsDigest for the new typed reply
just as it does for workerSnapshot; preserve protocol slot identity, current
process/host evidence and all expected settings/history-owner comparisons.
Never reuse a prior live proof merely because the same handle or package remains.
Immutable package capability parsing may be cached by store path; authority,
process, instruction and state proofs may not. Do not change read/history,
snapshot, fork or acceptance witness semantics merely to improve the timer.

A positively verified identity may carry Held. Keep existing held transcript
reads available: InputDelivery/BindRead may project capability false after valid
fresh identity proof, while Bind/Verify and effect admission refuse Held. Combine
local held/pending restrictions conservatively. Identity/proof errors remain
unavailable, with no fallback or fabricated state. Test held-readable/capability
false/effect-refused behavior and advertised identity failure without fallback.

Retained workers without the light capability use the exact legacy snapshot
verification path. They remain functional with their known history-linear cost.
Retained workers without checked-input support have no new durable-delivery
capability; their old browser/send routes remain supported. A new portal does not
upgrade retained supervisors or workers. Test the new portal against the exact
deployed frozen pair and the new matched pair, plus malformed claimed capability
and a wrong/missing new worker reply. Failure of an advertised op is unavailable,
never an implicit fallback after an attempted new dispatch.

C owns `portal/internal/piruntime/queued_input.go` (new checked port/selection
reader), `input_delivery.go` internal locked helper, `controller.go`, `adapter.go`,
`worker.go`, `supervisor.go`, `protocol.go`, `workflow_observation.go` mutation
classification and their focused tests; `pi-runtime/src/session.mjs`, worker and
protocol operation registration, corresponding tests/fake-worker fixtures; its
two contract fields and native sections of `docs/pi-runtime.md`. Preserve A's
observation docs paragraph; serialize shared doc/contract edits. No web/composer
or queue-store ownership. C follows accepted A and requires capacity confirmation.

Quick acceptance: count/throw getBranch and prove new Bind/Verify succeeds without
it; wrong native ID/history owner/settings/instructions/process/capability and
held state fail before send; no cached live proof across replacement. Race settings
or policy change against the checked enqueue and prove no changed-selection send.
Exact same-ID/ref returns original evidence; changed ref conflicts; missing lookup
is Unknown. Crash points preserve native receipt contracts and no replay. Run
focused piruntime and Node worker/session/protocol tests in Nix, including strict
retained wire fixtures, before commit. Deliver exact heads and compatibility proof.

## Compatibility, retention and recovery

Native schemas/receipt bytes and old HTTP message/native queue envelopes are
unchanged. The only new persisted format is the isolated portal queue v1. The
only new worker/supervisor interfaces are advertised versioned operations. Shared
UI consumes an optional neutral capability; Pi protocol details stay in its
adapter. codex-web old consumers and custom client embeddings retain their API.

Add `piPortalDelivery: 1` to the selected portal package contract. Existing package
transition/preflight must retain and inspect queue dependencies and reject a
target without that capability while queue records remain. Use the existing
current-package preflight/target validation ordering; prove both ordinary switch
and activation/recovery checks, not only a metadata declaration. Unknown/corrupt
queue state fails closed. Old native workers need not read this separate store.
Do not change member artifact whitelists or retrofit queue rows into receipts.

Preflight source kind is `portal_delivery`, within the existing output envelopes.
The inspector includes authenticated ConversationRefs from negative identities as
well as work rows, so a negative-only database still requires piPortalDelivery:1.
Reuse the existing SessionRef/lead/member scanner joins; do not add a workspace-only
claim schema. Test negative-only state rejecting an incapable target, capable
inspection without source writes, and wrong/malformed ref or scope evidence.
For strict no-write inspection, copy the existing database and present WAL into
one private disposable directory while the caller holds ordinary exclusive
package-transition ownership. Copy bytes, not hardlinks; do not copy/rely on the
SHM index. Run SQLite recovery/read-only SQL only on that copy and remove it on
every return. Never initialize, checkpoint or open the source through SQLite to
make inspection succeed. The same exclusion must cover every queue mutation and
checkpoint/last-connection close; a comment or query_only setting does not prove
this. A caller without writer exclusion cannot use sequential copying as a
consistent snapshot. Inspect source ownership/modes and reject orphan/malformed
state as already required. Focused fixtures retain committed rows only in WAL,
omit SHM, and assert all source names/bytes/modes unchanged on success, failure
and cancellation; ordinary reads may update access times. SQLite's
[WAL contract](https://www.sqlite.org/wal.html#the_wal_file) explains why the WAL
must accompany the database and why read-only opening alone is insufficient.

Production queue DB calls, initialization/reconnection and connection close use
shared transition admission, including result writes after native admission has
ended. Actual pool connection lifecycle must not escape that gate. Normal WAL
auto-checkpoint remains enabled inside the committing operation's gate; disabling
it alone would allow growing WAL/copy costs. Package switching already stops and
joins portals under exclusive transition ownership (`drain_portal_services`), so
terminal shutdown cannot block trying to acquire a shared lock for SQLite close.
Stop new queue operations, cancel/join workers, then attempt gated close with a
bounded/cancel-aware or nonblocking acquisition. If unavailable, explicitly report
deferred close and retain the inert connection until process exit, without a
SQLite close/checkpoint or delayed cleanup. This exception is terminal teardown,
not permission to keep using an ungated store. A canceled result write preserves
the existing dispatching claim and recovers by original native receipt lookup on
restart. Test EX-held shutdown completion, zero source close/checkpoint, and
next-start WAL recovery; do not require an uncertain native send to repeat.

Queue rows survive portal restart, native restart and user-facing card dismissal.
Session/member disappearance, incarnation change, stopped/archived state, access
or selected settings change is never permission to retarget a queued input. The
server stops fresh dispatch and records the appropriate positive pre-dispatch
failure or retained ambiguity. Retain text and attachment ownership for diagnosis.
No lifecycle cleanup is executed in this initiative and no new automatic
session-closing behavior is introduced. Future explicit lifecycle actions must
not cause a revived session to auto-send inputs whose selected scope changed.

Deployment instructions only: publish/pin matched codex-web source and assets,
install a compatible portal, then separately perform an explicitly authorized
ordinary retained-runtime upgrade where checked/light capabilities are wanted.
The legacy runtime remains available before that upgrade. Preserve the queue DB,
WAL and existing native receipts through package transitions/backups; restore
forward with a capable package, never discard queue/receipt state to get past a
guard. A queue is not confirmation that native effects or external tools stopped.

## Verification and performance campaign

### V: native delivery fixture source (sufficient settled brief)

Owner is implementer0 after lead allocation. This completes the originally
required executable verification source. Reuse the existing central/P6 native
fixture; do not create a service, harness, general fault framework or new runtime
interface. B retains all untagged web/store/composer/upload/preflight tests and
the hydrated browser fixture. V integrates the real native delivery path and
reports which B assertions it composes; it does not duplicate those test suites.

V owns new `portal/internal/piruntime/pi_message_delivery_integration_test.go`
with build tag `pi_native_fixture`, package `piruntime_test`, and new tagged
`portal/internal/piruntime/pi_message_delivery_fixture_test.go`, package
`piruntime`, for narrow internal fixture configuration, counting and fault access.
No production `.go` file may refer to `_test.go` P6/fakeHost definitions. If needed,
lead permits only a context parameter seam in existing `supervisor_test.go`:
ordinary callers retain the 20-second default; the new caller supplies a bounded
context derived from t.Deadline before Serve/worker startup. Do not duplicate
bootstrap, use globals, alter production timeouts or edit B-owned files. Lead
owns the short shared Git/index window; V edits are disjoint during B's window,
then V commits after B's behavior/provider/pins settle.

Owning helper facts checked for this brief:

- `p2_central_workflow_integration_test.go` supplies `centralIntentWithProviders`,
  `centralPublishReady`, `centralRequest`, `centralDecode`, and retained-ready
  HTTP/authority/catalog composition. Its seed proves real native creation and
  Accepted witness but does not exercise public naming/root allocation. Retain
  that disclosure. The existing team seed is explicitly lead_reviewed only.
  Its intent helper hardcodes p3-model/high; reuse its composition pattern, not
  that incompatible selection, for V's canonical four-member catalog.
- `P6NativeFixture` in `tool_policy_test.go` exposes Manager, Runtime, Settings,
  Context, Attach, Idle, Reopen and upgrade/fault helpers. `Reopen` recreates a
  Manager, not a supervisor or worker. `NewP6NativeUpgradeFixture` supplies the
  existing successor/terminal-host fixture; its stop/drain/process are synthetic.
- `supervisorFixture` owns the actual Unix transport, supervisor locks and Node
  worker using the pinned SDK. Its default fake Host.Inspect must be wrapped and
  counted, never replaced with a cached response. Its checked/identity contract
  readers default false, so V must enable the real immutable CURRENT readers for
  `piCheckedInput` and `piConversationIdentity` before measuring the new path.
  Validate PI_CENTRAL_APP_ROOT and worker metadata against the exact candidate.
- The existing source-only fake worker imports production `runWorker`/persistence
  and the SDK faux provider. Its small finite response script is not a 220-send
  workload. A small V-local generated entrypoint may configure enough deterministic
  responses through that same SDK provider API, importing the actual protocol,
  session and sync functions. No replacement identity, enqueue or acceptance code.

Entrypoints are `TestPiMessageDeliveryNativeRecovery` and
`TestPiMessageDeliveryNativePerformance`. Require explicit PI_PROBE_PACKAGE,
PI_CENTRAL_APP_ROOT and PI_CENTRAL_CATALOG_FIXTURE when these named tests execute;
missing/invalid inputs are failures, not successful skipped campaign evidence.
Record exact immutable package/SDK/worker paths, catalog digest, both repository
heads and test binary/input identity. Preserve source-only/no-network faux model
behavior and temporary accounts; no live session/profile/package changes.

The four-member catalog prerequisite is prepared under this session's ignored,
untracked `v-fixture/`: `catalog.nix` is the exact generator expression,
`catalog.json` its output, and `validation.json` records input/output hashes.
It imports the existing workspace `config/agent-teams.nix`, retains delegated
role settings/instructions and work/utility policy, and constructs a separate
`delivery_fixture` team with implementer count 1 and max_open_agents 4. Set both
defaults to that team, retain only that team in the disposable config and set
required_native_child_threads to 4. The four expanded members are architect0,
implementer0, observer0 and reviewer0. This is generated fixture data, not a
change to the real retained team. `nix/agent-teams.nix` receives that teamConfig,
the worktree flake's locked nixpkgs.lib and builtins.toFile as writeText; assert
generated.valid and evaluate generated.catalogData. Regenerate from workspace root:

```sh
nix eval --impure --json --file work/2026-11-23-pi-message-delivery/v-fixture/catalog.nix \
  > work/2026-11-23-pi-message-delivery/v-fixture/catalog.json
export PI_CENTRAL_CATALOG_FIXTURE=/home/aither/workspace/ai/vpsfree.cz/work/2026-11-23-pi-message-delivery/v-fixture/catalog.json
```

Validation-only preparation passed: canonical generator's valid assertion, exact
four-member expansion, recomputed catalog/team SHA256 and all generated native
variant names. Catalog digest is
`70a47ec7c140d5595e568ab213304fcded77f4a2075d7ffbfaa9d4fa7d195093`,
team digest `5d1fc8c481f0bb3313ef31893d2937aa08f6dc2b98863fbcce163270790a405c`,
output file SHA256 `adb05d10ba504cd3951631f07c450d16a753f75856b41d9c6ad50ecdaaa91aed`.
Owning generator SHA256 is
`f89d3736a83dbd41916e0756678e91131460fa8ca624ffd7fbfc192b39ca8265`;
settings input SHA256 is
`acce62d51bae4686c86c1d0e8532bed7e47f0c9e3026d046095718cf1702ef89`.
The V test still performs the owning Go Catalog.Validate/FindCatalogPreset
before native setup; no Go/native campaign was run for this preparation. Recheck
the recorded hashes if generator/settings change; do not reuse digests after edits.

Construct one authentic disposable lead plus four member conversations sharing
the session runtime admission boundary, using a valid typed catalog, owning
binding/roster/creation stores and real native Create/proof. Each member has a
distinct native ID/incarnation and preserved settings/policy. Do not count five
HTTP clients targeting one native conversation or the existing two-person seed
as the team workload. Use actual portal handlers/new delivery routes, SQLite
WAL/FULL store and dispatcher, Manager/supervisor/worker, fresh scalar proof,
native history persistence and exact witness. Observe/count wrappers must delegate
the real operation and preserve locking/order; no fake Send/Lookup/identity/store.

R1 review correction: retain the original concrete *workerProcess returned by
s.start. Production load/unload uses that concrete endpoint to establish shared
topology and detach ownership; a wrapper implementing worker is not equivalent.
V may observe the existing host.input io.WriteCloser once per physical host,
installing it under host.writeMu. Write already executes under that mutex: delegate
directly without reacquiring it or recursively calling host.write. Forward every
frame and Close unchanged. Decode exact request op/identity/body for attribution;
callback/result frames remain untouched. Separate attempted/full/failed writes
and injected errors; this seam cannot count arbitrary Call reply failures.
Only workflow_observe may inject an error after its real delegated write. Retain
outcome/witness/hold assertions and label this as an injected observation failure.
Use the existing context-bearing Manager Dial seam for admission RPC attribution,
alongside delegated Host.Inspect counts. No topology assignment or production API
change is permitted. The narrow TestPiMessageDeliveryNativeBootstrap must create
the authentic five-conversation setup, unload/load an ordinary member and prove shared
topology/native identity and stable sibling PID/witness before the larger matrix,
on the final revised candidate scheduled by lead after compile/syntax checks.

Concrete five-conversation seed: use a validated disposable supplied catalog whose
selected default preset has four members. Call FindCatalogPreset then the existing
ProjectPiPreset exactly once on that canonical source preset, as ordinary new Pi
selection does. CatalogDigest remains the source catalog; TeamDigest is the owning
derived digest. V composes, freezes and validates its intent and per-member provider
overrides from those exact projected model/effort/access/instructions before native
Ensure; the faux offline provider/catalog registers the exact chosen model IDs
and supported efforts. Reasoning=true alone does not establish support for every
frozen effort in the faux SDK model. V may supply explicit thinkingLevelMap on
those same faux model objects before native provider registration. An SDK-only
preflight must check every saved model/effort pair with the selected SDK's actual
supported-level/clamping functions and require the effective effort to equal the
request. Keep the real provider/stream/SDK and assert the delegated Create result's
full saved Settings tuple; do not lower xhigh, rewrite the expected tuple or relax
binding/authority/roster/intent joins. Preserve stage diagnostics for a failed
proof. This declares synthetic provider capability, not real model reasoning
performance. Do not rewrite canonical catalog JSON/digests or central
helpers. Retained-ready describes the root seed boundary, not a requirement to
use an unprojected preset. Saved intent/roster/settings stay frozen across reopen
and successor tests; never project a retained roster again. Stamp each seeded
history with its own saved member model/settings. Preserve original Start/runtime
request identity and all production creation guards, without claiming public
creation coverage. Real lead Create/Accepted proof precedes `centralPublishReady`.
V's retained proof also requires coherent PiCreationServices: available() checks
Runtime, a valid Catalog, Selection and StartRequest before any retained native
proof. Prefer the existing NewPiCreationServices composition where the disposable
faux configuration is actually supported; do not change production configuration
validation to admit it. Otherwise V-local closures may return only the exact
captured original selection and Start after strict context/session/preset/reserved
conversation/intent/revision checks. Return errors for any differing input, copy
mutable values and never perform Ensure/load/start/send from these closures.
Preserve the original Start tuple, including request ID and binding provenance;
do not rewrite it to make public-creation checks pass. This supports only the
explicit retained-ready fixture boundary, not a new creation implementation.
Add a pure coherent-service prerequisite regression before another Bootstrap:
validate the captured supported input and wrong scope/preset/reservation/intent/
revision refusals without native calls. The real retained proof keeps every
binding/authority/roster/intent join and actual Lookup/VerifyCreation witness check.
Save all four exact
reserved members as creating through `Store.SavePi(ctx, server, generation, 0,
roster)` with the intent's catalog/team digests, access/settings and incarnations.
Then POST `action: assign` from lead to each member through
`/api/sessions/:slug/team`, with distinct original assignment IDs and current lead
scope. This is the existing first-assignment path, not a separate `/assign` API.
Require `ReadMemberAdmission` to prove each original Accepted witness, then reload
the published ready binding/roster and obtain each member's real scoped identity.
Check five unique native conversation IDs in one SessionRef/CURRENT generation;
use the candidate's shared worker topology when advertised. Seed assignments and
their history/receipts are reported setup, excluded from measured warm/send samples.
Do not truncate a larger preset or change member settings while reusing its old
digest; prepare/validate the disposable fixture catalog independently of live team
settings. The central helper's lead_reviewed assertion does not apply to this seed.

Reuse B's public/testable composition points. A runtime wrapper embedding the
real Manager may capture checked-dispatch entry/completion or inject a lost reply
after the underlying call. Hold actual runtime admission for pre-claim stalls;
the checked-dispatch entry is already after B's durable claim. Faults must be
named by their real boundary. A closed HTTP response is not a native crash, a
Manager Reopen is not worker replacement, and Close is graceful shutdown rather
than process loss. For a true process-loss case use a child mode of this same
test binary and only owned disposable processes/state, or report the graceful
case separately. Restart a fresh web.Server/dispatcher on the same durable store.
Use existing successor/retirement commands and proofs inside the disposable
fixture; never edit live or original receipt bytes to manufacture a result.
For the missing/malformed negative case only, V may quarantine an exact completed
fixture receipt outside all strict native receipt/member roots, then test absence
and an intentionally malformed placeholder at its original disposable path.
Quiesce/join writers or hold the existing exclusion before this deterministic
fault. Preserve original bytes/mode separately and restore that exact file during
fixture cleanup after readers/writers finish; compare its digest before/after.
Never fabricate a valid Accepted/Unknown record. Assert no extra native send/user
append across absence, malformed read and restoration. This is explicit storage
fault injection, not a supported receipt repair or retirement operation.
For this case, closing/joining the portal followed by the supervisor's existing
`inputTasks.Wait` is a sufficient receipt-writer boundary when no other client
can admit inputs. Registration precedes Pending return, and completion follows
all of `finishInput`, including commit and final observation. Capture the exact
Accepted/ref/witness bytes after that wait; repeat the closed-portal/writer wait
before malformed replacement and restoration. Do not call mutating `Idle`/Load
after Close has revoked the workflow attachment. Lookup-only negative reads do
not create receipt writers. Continued SDK assistant history is allowed; this
boundary proves receipt-writer completion, not native idle, and leaves the exact
original witness and single user append/enqueue assertions intact.

Required integrated matrix (B retains exhaustive local/browser permutations):

| Case/boundary | Native integration assertion |
| --- | --- |
| POST success, same-ID concurrent/repeated request, changed payload; lost HTTP reply/closed client | One original immutable queue identity, at most one native enqueue/user append, exact Accepted witness; conflict for changed request. Server completes without a live browser. Hydrated tab/DOM evidence remains B's. |
| Portal restart before claim; native ready successor before claim | Same definitely-unsent row continues once only through exact logical selection and proven CURRENT ancestry, including fresh binding revision. Unavailable/unloaded/preparing waits without implicit load/start. |
| Portal/native interruption after claim before wire, after enqueue/Pending, after native persisted acceptance before portal result | Never dispatch original again. Zero append is allowed after claim-before-wire; missing proof is Unknown. Pending needs exact live owner; lost owner becomes Unknown. Original receipt proof alone may recover Sent. |
| Settings/policy/instructions/access/member incarnation/lifecycle changes | Before claim: positive logical mismatch not_sent, temporary unavailable queued/backoff. After claim: original lookup only. New stale selection/header syntax and exact scope checks compose B's local tests. |
| Empty/all-Accepted questions, real pending question, failed/inflight GET+event churn | No exclusive/no-op invalidation for empty work; real effect retains rechecks. Host/worker calls bounded by A backoff, foreground proceeds, question work progresses under sustained sends. |
| FollowUp held behind a native turn, then steer | Positive live Pending permits later steer; native consumption order and eventual exact receipt follow real SDK behavior. Unknown/inflight barriers block later work. |
| Native receipt missing/malformed; repeated ID after restart | Unknown/unavailable/conflict as specified, never text-based acceptance or a new attempt. Verify actual native entry and receipt identities/counts. |
| Exact explicit retired Unknown, prepared/wrong proof; restart | Completed owner proof releases only later distinct work/capacity; original Unknown/receipt bytes/dedup unchanged. Unproved/prepared/malformed retirement remains blocking. |
| Durable negative admission proof, response loss/restart and late duplicate | Same-ID proof survives; no native ref/work/enqueue for refused ID. Later explicit fresh selection/new ID can send. Compose B's concurrent Admit/Reject, forged-proof, negative-only preflight and hydrated draft tests by exact evidence. |
| Four busy members/lead, one failed peer, sustained foreground | No same-conversation concurrent dispatch, worker pool <=4, round-robin peer progress and A's eight-grant reserved-background boundary; failed peer cannot consume all progress. |

Use real locks and channel barriers for fault placement; avoid timing sleeps as
proof of reaching a boundary. Preserve B's store fault tests for commit failure,
uploads, capacity/collection and transition-copy/close guarantees. V records
exact test names/commits for those dependencies in its completion packet.
Member access is immutable through ordinary SavePi. A disposable validated roster
replacement may inject a selected-access fault without claiming a supported access
editing API. Preserve the normal writer's refusal and all owning join checks;
never weaken them to make the fixture reach dispatch. Distinguish a positively
proved logical mismatch (not_sent before claim) from invalid/unavailable authority
that refuses earlier. Both must prevent new native effects; report the actual
boundary/outcome and do not claim public access-change coverage from raw replacement.

The same fault boundary applies to `preclaim_member_incarnation`. Ordinary
`BackendBindingStore.CompareAndSwap` preserves each conversation's incarnation
and ready tuple (`session/backend_publication.go`); first assert
`ErrBindingConflict` and unchanged exact binding bytes. A typed binding that
passes `Validate` may then replace only the disposable fixture's binding file
under runtime EX with its other writers quiesced. Validation proves record shape,
not current ownership: deliberately retain the original authority, roster and
native mapping so their disagreement exercises the existing strict joins. After
releasing the exclusion, establish that an actual revalidation attempt occurred;
accept queued/backoff for unavailable ownership, or `not_sent` only from the
ordinary positively proved incompatibility path. Assert unchanged original
Admission/ID and zero dispatch, enqueue and native user append for that ID.
Preserve original bytes; any restoration occurs only after the dispatcher and
fixture writers have joined. Label this unsupported owner-incarnation fault in
the evidence. It does not establish supported remove/add coverage or permit a CAS
relaxation; keep that lifecycle evidence separate without broadening this case.

Performance source must expose selectable ordinary Go subtests for each history
size (short, 10,000, 100,000 entries) and workload: idle healthy, five-conversation
healthy activity, failed/held churn, and deliberately delayed followUp. Seed valid
user/assistant/tool histories through the pinned SDK SessionManager while no
worker owns the file, then load through ordinary owner proof; never fabricate
Accepted receipts or modify a loaded transcript. Verify actual entry/byte counts
and parent chain before timing. Record actual receipt count (including bootstrap,
warmup and generated inputs); respect the native receipt capacity rather than
claiming 100,000 receipts from a 100,000-entry transcript. Setup/load cost and
worker memory belong in the evidence even when excluded from warm latency.

Each executed history/workload cell warms 20 operations then collects >=200
independent original IDs. Use enough deterministic turn completions and drain
between bounded batches to avoid accidental capacity artifacts. Seed all active
conversations to the declared history workload and record per-conversation counts.
Healthy cells include real per-second team/display activity and question demand.
Churn cells drive and count failed refresh attempts/events and Host.Inspect calls,
reporting achieved rates against the original 96 failed refreshes/580 inspections
per four minutes; duplicate demand must not reset backoff. Held effects hold the
real native admission lock while HTTP durable admission remains measured. FollowUp
waiting on a model/tool is reported separately from healthy delivery latency.

Measure with monotonic clocks. Receipt timing begins after complete request body
availability and ends only after durable queue commit. A full HTTP 202 duration
is an acceptable conservative upper bound (report it as such, including handler/
loopback overhead); never call a pre-COMMIT CreatedAt timestamp durable completion.
Native acceptance ends after the real checked operation proves persisted Accepted
and exact witness, not Pending or a queue status assumption. If no existing seam
gives exact admission-commit time, report HTTP-start-to-native-Accepted as a
conservative upper bound for commit-to-Accepted; do not subtract an overlapping
HTTP response timestamp or label it exact delivery latency. Polling adds a stated
sampling bound. A direct commit timestamp seam, if needed to resolve a failing
bound, stays with B and needs a narrow agreed boundary; no telemetry framework.

For the new checked-input path, V may timestamp entry to the existing real worker
`input_commit_v1` frame write at the serialized stdin seam. `finishInput` reaches this call
only after exact witness checks and successful Accepted receipt persistence.
Record the first monotonic timestamp keyed by full conversation scope/original ID
(plus execution identity for evidence), require the full unchanged delegated
write to succeed, and validate
the exact original receipt/witness independently through Lookup. The timestamp is
an upper bound on durable native acceptance, not the worker commit completion or
an exact queue-commit timestamp. Write entry is later than Call entry and includes
serialization/lock scheduling; record any write failure separately, not as a
successful observed commit write. HTTP-body-available to this event is a conservative
delivery upper bound. Missing events, call/proof failures and held outcomes remain
explicit samples/outcomes, never zero-duration successes. A later worker commit
failure must still be reported even though receipt persistence preceded it.

Report public Sent observation separately: portal reconciliation and browser
polling can delay it after native Accepted. The accepted one-second target ends
at exact native acceptance, so public polling delay must neither falsify that
metric nor be hidden from user-visible latency evidence. This V-only observation
adds no production field, receipt/schema, callback or acceptance shortcut.

Assert p95 durable receipt <250ms and healthy acceptance <1s on the qualifying
long-history/team cells; conservative upper bounds below target prove the target,
while an over-target upper bound alone cannot attribute the failing component.
Collect p50/p95/p99/max, success/Unknown/refusal/failure counts, all sample counts,
per-ID phases/times, native append/enqueue/receipt/witness counts, exact settings/
scope, Host.Inspect/native proof counts, queue depth/oldest waiting, per-member
progress and reserved-background pass counts or proven observed opportunities.
Do not discard failed samples or mix held/followUp/cold startup with healthy data.
When a cell times out or cannot seed the requested history, report partial actual
counts and an unmet cell, not a smaller workload as a pass. Preserve witness cost.

The finite fixture's fake host does not measure real systemd/sudo/process-inspection
latency; faux provider omits remote model/network service latency. Local handler or
loopback HTTP is not production TLS/reverse-proxy performance. State these limits
per result. After review, existing `checks.x86_64-linux.pi-runtime-host` covers
physical host ownership/start/stop/drain with its synthetic supervisor, while
`checks.x86_64-linux.session-creation` includes the actual packaged Pi/public
creation and cold reconnect path. The latter is the selected combined host/portal
compatibility check. Neither existing VM establishes this queue's p95 by itself;
do not add V-owned VM edits or claim a physical deployed latency result.

Quick gate before final review (inside own dev-workspace, final B pins preferred):

```sh
nix develop --command env GOWORK=off go -C portal test -mod=readonly \
  -tags=pi_native_fixture -run '^$' ./internal/piruntime
```

Compilation must include both new files and all existing tagged helpers. It proves
types/build only, not SDK execution, fixture readiness or latency. Use an agreed
own-worktree GOWORK only while B's pin is pending, label that check provisional,
then repeat the final compile against committed pins. Run required hooks, commit
all V source, and provide exact base/head/file inventory and compile evidence for
lead's final review packet. No long/native campaign before that review resolves.

After review, lead schedules bounded monitored batches with explicit immutable
inputs, first `-run '^TestPiMessageDeliveryNativeRecovery$'`, then performance cells
under `TestPiMessageDeliveryNativePerformance` with a declared -timeout/cell budget
derived from the >=220 operations and fixture setup. Use -count=1 and record every
selected cell/timeout. No new local service is needed for in-process handlers;
any independently launched temporary server must use existing dev-session service
registration. Store compact summaries in session state/evidence, raw per-ID JSONL
and logs as untracked disposable session-owned artifacts; do not put prompts,
credentials or large benchmark output into project commits. Lead owns observation,
long-check allocation, final acceptance and cleanup authorization.

V's release dependency is the accepted A/C contract plus B's settled HTTP/store
and proof schemas. Source can proceed now in its disjoint files; final composition
compile/commit waits for B's final provider and behavior. Missing instrumentation
is a precise dependency to resolve directly with B/architect, not permission to
mock the affected path or broaden source ownership. No performance result is
claimed by this brief.

All intended substantive changes must be committed and quick checks pass before
the lead invokes independent final review. Review covers complete base-to-head
history/migrations, API/protocol, authority, queue-state compatibility, docs and
actual shared consumers. Longer integration and performance runs follow review
finding resolution. Use the monitor skill for uncertain/long runs, disposable
state/sockets/accounts, and no live session/profile experiments.

The inherited dev-workspace default-to-base series is:

| Commit | Prerequisite |
| --- | --- |
| 0bb3697d | portal: hide new output at the transcript tail |
| 5852fd97 | pi: exit cleanly after a signal closes the supervisor listener |
| 02f7b7e1 | portal: refresh on return to Conversation |
| 2f95680d | archive: reuse worktree listings within validation passes |
| 16827c67 | pi: avoid rebinding before message verification |
| 5d7bb545 | pi: prepare sensitive creation before publishing journals |
| 7fbe933b | docs: clarify interrupted sensitive Pi creation |
| f3bd843f | sessions: recognize supported portal preparation reservations |

For B/C integration use a disposable actual portal HTTP server, real local
admission/SQLite/attachment path, real Manager/supervisor transport and locks,
new JS worker with native Pi SDK and a deterministic provider where possible.
Protocol fakes may inject faults and remove model latency, but must not replace
the locks, host-inspection count, scalar proof, native history witness or durable
record paths being measured. Label a protocol-only result as such. Use the
existing fake-provider/native fixture infrastructure; no new benchmark service
framework. Measure baseline f3bd/3209 and final new pair, and mixed retained pair
where applicable, with identical fixtures.

Required correctness cases: repeat identical and changed ID/payload concurrently
across tabs; HTTP reply loss; tab closure after durable acknowledgement; restart
portal before dispatch claim, after claim/before wire, after native enqueue and
after native witness/before queue result; restart supervisor/worker at those
native boundaries; queued settings/access/policy/member/runtime/lifecycle changes;
missing/malformed native receipt; long pending followUp followed by steer;
capacity/refusal; multiple conversations and continuous background churn. Assert
actual native append/enqueue counts (at most one per original ID), exact native
witness/receipt, preserved mode/selection and bounded fair progress. Uncertainty
is a valid required outcome at crash boundaries, not a reason to replay.

Performance fixtures: short history, 10,000-entry history and 100,000-entry
history with representative user/assistant/tool entries and receipt counts;
lead plus four active members; concurrent 1-second activity/display demand and
an explicit failure/churn workload comparable to the reported 96 failed refreshes
and 580 host inspections in four minutes. Record actual achieved rates and host
inspection/refresh counts, not merely configured timer rates. Include empty
question stores, genuine pending questions, repeated events and one failing
conversation beside healthy ones. Separate warm healthy delivery from cold start
and unavailable/held-runtime cases. Warm up 20 operations then collect at least
200 independent operations per measured history/workload cell using deterministic
turn completion so capacity is meaningful. Report p50/p95/p99, max, failures,
sample count, concurrency, machine/filesystem, revisions and fixture limits.

Durable latency starts when the server receives a complete POST and ends when
the durable queue commit completes; also report HTTP round-trip separately.
Require p95 <250 ms under the long-history/team workload, including a stalled
native effect holding the runtime lock. Native calls/Host.Inspect must be zero
on that admission path. Healthy delivery starts at queue commit and ends only at
the exact persisted native acceptance receipt (also report end-to-end from POST).
Require p95 <1 second for idle prompt/healthy consumable steer. A followUp waiting
for an active model/tool turn is intentionally not eligible; report its enqueue
latency separately and verify eventual exact acceptance after the turn releases.

Record queue depth, per-conversation oldest waiting time and progress of healthy
background observations/question deliveries while sending. A failed conversation
cannot consume all worker slots or starve healthy peers; sustained foreground
traffic must still permit background progress at bounded scheduling boundaries.
Deterministic quick tests assert attempt/count/fairness bounds; the longer campaign
reports observed wall-clock bounds. The exact native witness intentionally still
reopens/syncs and verifies history; if that cost misses the delivery target,
report the measured failing component and return to the lead. Never weaken its
proof, redefine Sent, hide failed samples or claim the target from admission-only
measurements. No performance result has yet been measured by this design package.

## P: failed-cell diagnosis and bounded measurement correction

The first executed `10000/team_activity` cell at dev-workspace
`79dd02b09e25e38d8d833185d0e4c3acc7fef7b5`, codex-web `db79231a4e5513bf439493efab75378bc7d84c04`,
failed its targets. Preserve its original workload and evidence:
`/tmp/2026-11-23-pi-message-delivery-perf-10000-team-79dd.log` and
`/tmp/pi-message-delivery-perf-10000-team-79dd.Qvjj6W/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl`.
It has 20 warm plus 200 measured inputs, all 200 measured Sent, 40 per conversation,
and one enqueue/user append per original ID. Durable HTTP upper p95 is 378.380 ms;
HTTP-to-post-persistence native commit-write upper p95 is 3566.576 ms. Neither
upper-bound failure attributes time to SQLite, local validation or native witness.
Admission made zero attributed Host.Inspect/runtime-dial calls. The fake host,
offline provider and in-process HTTP limitations remain explicit.

The owning artifact/source pass establishes these limits and hypotheses:

- `activity.questionID` is empty: no submitted response intent is evidenced.
  `QuestionAcceptedNS=0` is a failed fairness probe, not proof that an admitted
  response starved. Response eligibility needs a fresh session-wide observation;
  member events can invalidate publication while prior native completions run.
  The 17 origin-inspection calls do not establish a successful origin proof.
- Counter deltas span warmup and measurement, while the rate denominator covers
  only measurement. Raw deltas include 1622 Host.Inspect, 783 identity calls,
  440 history verification calls, 220 snapshots and 121 workflow observations.
  The reported 8.338 inspections/second is not a correctly aligned measured rate.
- Each accepted input performs a full `finishInput -> observeState -> snapshot`
  after the commit-write hook. This and synchronous history verification can
  delay sibling operations on the shared Node event loop. Durations are unmeasured.
  Half the 440 verification calls are the fixture's independent post-Sent Lookup;
  the other half are production original-ref reconciliation and remain mandatory.
- Maximum checked-port concurrency one is consistent with the existing session
  exclusive admission. It does not establish a worker-pool or pipe-mutex defect.
  Status phase times are completed HTTP observations, not native stage timestamps.
  The 10 ms polling sleep does not bound status-handler latency. The five reported
  RSS entries refer to one physical shared worker PID and must not be summed.

### P0 measurement correction: sufficient independent brief

Lead accepts this bounded V correction independently of P1 cost attribution.
Owner implementer0; only the existing tagged
`portal/internal/piruntime/pi_message_delivery_integration_test.go` and
`portal/internal/piruntime/pi_message_delivery_fixture_test.go`. Preserve the
concrete worker endpoint, shared-host topology, all production paths and original
receipt/identity/settings/authority/witness checks. No production optimization,
new protocol, persistence schema or generic telemetry framework is authorized.

1. Capture counter snapshots and elapsed-time endpoints for the same interval.
   Keep warmup, measured activity and post-measurement proof work identifiable;
   keep every raw count and failure. Report achieved activity rates, not timer intent.
2. Label the 10 ms value as polling sleep. Retain HTTP-observation times and the
   existing conservative native hook without calling either an exact stage timer.
3. Record bounded endpoint/method/status/outcome evidence for activity, question
   eligibility, response POST/status and delivery-status reads. Count all issued
   requests, including collection reads. Preserve question existence, CanRespond
   and available refusal/proof fields. A response ID alone is not admission: retain
   the actual response POST outcome and persisted response identity before making
   a delivery-fairness claim. Unknown failure detail remains explicitly unknown.
4. Defer only the fixture's extra independent original-ref Lookup until all four
   batch timed endpoints have finished. Run that Lookup's complete original
   receipt/ref/input/mode/settings/witness assertions before starting the next
   batch, together with per-ID enqueue/checked-call counters. Keep the existing
   independent disk-history/user-append and Idle audit at the end of the cell;
   do not add a history scan or wait for native/model idleness between batches.
   Those added quiet intervals would change sustained-foreground fairness and
   the workload beyond the accepted Lookup deferral. Preserve every final history
   and at-most-once assertion. Keep the production Lookup and native persistence
   witness in the timed path. Keep failed/missing endpoints in the sample set;
   do not validate only successes. Record this as a revised workload, never
   retroactive success for 79dd.

The next native experiment is a diagnostic, not a percentile acceptance campaign:
one authentic five-conversation setup with 10,000-entry histories, one concurrent
four-input batch and the existing genuine optional-question path. Use bounded
existing test seams to correlate complete-body HTTP, local selection, checked
dispatch/Lookup and exact native request-frame entry with question eligibility
and response outcomes. Preserve actual operations and all independent proofs;
do not manufacture a respondable snapshot or an admitted response. Any missing
stage boundary remains an attribution limit. The settled diagnostic entrypoint
is `TestPiMessageDeliveryNativeStageDiagnostic`, within the same two V files:

- Reuse `deliveryNativeRuntime` to delegate ObserveWorkflow, InspectNativeOrigin,
  DispatchQueuedInput and LookupQueuedInput exactly once, recording entry, return
  and bounded outcome. These are inclusive Manager durations, not worker execution
  times. Retain the original endpoint types and all exact returned proofs.
- Extend the existing concrete-host input tap only to record frame UUID, operation,
  full execution identity and input ID when present, with serialized write entry
  and successful full-write completion. Preserve exact bytes, Close and the owning
  writeMu; do not wrap/replace worker endpoints or intercept native responses.
  Never attribute a snapshot to a guessed original input.
- Record HTTP method/endpoint/status and diagnostic interval (initial, batch,
  quiet); question ID/revision/state/CanRespond/option presence; actual response
  POST outcome and persisted response identity/status. Flush existing
  centralDiagnostics. Before/after-call publication failures may remain opaque:
  HTTP capability/outcome plus delegated runtime result are the evidence, not a
  fabricated private publication predicate.
- Observe initial eligibility for at most 6 seconds, then run the one four-input
  batch with the existing per-input deadline, then at most 10 seconds of quiet
  question eligibility/response observation. Initial observation does not consume
  the response before the batch; label any response admitted during the batch or
  quiet interval accurately. Do not force eligibility or replay a response. Keep
  missing/failed/timed-out endpoints and all subsequent exact proof assertions.
  The diagnostic's final Idle/disk-history audit follows the quiet observation
  window; it does not manufacture an eligibility opportunity within that window.
- Use a 3-minute Go timeout for the combined diagnostic: the observed roughly
  38-second setup, 6-second initial window, existing 75-second batch deadline,
  10-second quiet window and join margin do not fit a 2-minute outer deadline.
  This is a bounded stage probe, with no latency percentile or fairness-success
  assertion. A missing respondable question is an explicit result, not a skip.

Full native operation completion remains unavailable at the input seam; serialized
writes are not native completion times. No production/output interception is
added to fill that gap. The proposed run is the ordinary tagged test with
`-count=1 -timeout=3m -run '^TestPiMessageDeliveryNativeStageDiagnostic$'` and
`-trace=<owned-artifact-path>`, using the existing exact candidate/catalog/SDK
environment. P0 source and quick checks are independent; the combined P0/P1
candidate supplies the local/commit regions needed for cost attribution in the
single lead-owned run. No 100,000-entry or full matrix run is authorized here.

Quick gate: tagged compile-only plus focused pure fixture tests for any changed
observation/aggregation logic, and Node syntax only if fixture JS changes. Deliver
the exact source diff/head, expected diagnostic command/output and remaining
attribution limits. Lead owns the source/commit window, affected independent
review and one bounded native execution after the required gate. P1 retains local
admission/dispatch diagnosis; application corrections require its owning evidence
and lead acceptance. Durability, exact witness, fairness and latency targets stay
unchanged.

### P1 local and dispatch timing: sufficient instrumentation brief

Lead accepts timing before optimization. Owner implementer1; production source
boundary is only `portal/internal/web/pi_input_delivery.go` and
`portal/internal/inputdelivery/store.go`, plus their existing focused test files
if a meaningful changed instrumentation boundary needs coverage. P0 owns both V
files and the first index/commit window; P1 edits are disjoint and its commit
follows P0 and the separately assigned F2 fixture correction. P1 source execution
requires lead release after I1 completes F2 and confirms capacity; this design
brief does not stack implementation assignments. No `pi_team_admission.go` edit
is included: the initial session
admission region deliberately includes lock wait and its owning validation.
An exact grant marker there needs a separately accepted boundary if this aggregate
dominates. No authorization, join, upload, SQL, lock order or native call is removed.

Use standard Go `runtime/trace` tasks, regions and bounded events. Tracing remains
inactive unless the ordinary test/runtime trace is enabled; no new logger,
observer interface, metrics service, timer, configuration flag or retained state.
Correlate only operation kind, original client ID, phase and bounded outcome;
never log message/attachment contents, provider credentials or full mutable state.
P0 may wrap each fixture HTTP call in a standard trace task so resolver regions
preceding body decoding share its identity. P1 creates a task for each driver
attempt/lookup with the saved original ID. Normal context cancellation and
authority still flow unchanged. This is diagnostic overhead, not target-pass data.

Place regions only at existing boundaries needed to separate these stages:

| Boundary | Exact scope and interpretation |
| --- | --- |
| Local resolve/joins | `resolvePiDelivery` total, its transition acquisition and ready-identity call; `piLocalDeliveries.local` for each repeated ready-identity/projected-access join; `selected` for local runtime selection. Keep initial/final rechecks distinct by enclosing Admit phase or call order. |
| Admission work | `AdmitDelivery` total; existing original-ID `Store.Resolve`; upload scope/Prepare block; existing `Store.Admit`. Success/error/conflict is observable without changing control flow. |
| Store waits/SQL | In `Store.access`, distinguish initial registration-mutex wait, transition-gate entry-to-callback admission, connection-mutex wait and the existing SQL callback. Preserve both mutex acquisitions, cancellation and close bookkeeping. Do not label the whole gate invocation as lock wait when it includes SQL. |
| Durable creation | In `Store.admit`, bracket actual `COMMIT` Exec and emit success only immediately after that Exec returns nil. Existing-ID/conflict/rollback paths never emit a new durable-admission event. The same trace clock relates this to complete-body HTTP start. |
| Durable claim/results | In `Store.update`, bracket the real autocommit UPDATE; record original ID/from/to and CAS outcome. Emit claim completion only for successful queued-to-dispatching CAS, after RowsAffected proves one row; identify that marker as a post-commit upper bound. Keep queued retries/results distinguishable. |
| Dispatch admission | `piDeliveryDriver.Dispatch` total; foreground acquisition; `acquirePiSessionAdmission` aggregate; selection/continuation; outer `lease.run` and callback entry. This separates waiting/owning recheck before the effect callback without inventing an exact runtime-lock grant. |
| Effect work | Existing message-lock acquisition; Bind plus Verify; upload validation; claim callback; checked-input port entry/return. Keep all real checks and their order, and trace every return path. |
| Recovery work | `piDeliveryDriver.Lookup` total with original ID and result; preserve original-ref-only recovery. |

These regions may nest; do not sum overlapping totals. Existing function names
and Go scheduler/blocking stacks provide detail inside a region without a new
instrumentation framework. Standard trace events at actual successful commit
return resolve the missing durable endpoint; native acceptance remains P0's
independent persisted-receipt/witness proof and commit-write upper bound.

Quick checks are the existing focused native-free HTTP/admission/store regression
batch, including cancellation and commit failure, plus tagged compile with P0.
No native execution is part of implementation. Deliver source/head, exact region
inventory and interpretation, normal tracing-disabled behavior, quick results
and remaining grouped boundaries. Retained independent review assesses these
production diagnostic additions after commits/checks and before the lead launches
the single P0 four-input diagnostic with ordinary `go test -trace=<artifact>`.
Do not rerun 200 samples to attribute stages. The resulting table must distinguish
local validation, commit, scheduling/admission, checked port and native-proof
uncertainty before any performance correction is proposed.

## P2: four-input attribution and independent corrections

The stage diagnostic used exact dev-workspace
`06680120cd3004afe785043c47781e15cbae66b7` and
`/nix/store/aijwyqbp8fiwizw2kf9348xjxiz2yfi3-dev-workspace-0.2.0`, with the same
SDK/catalog and codex-web input as P. It completed with four Sent inputs, exact
Accepted/ref/input/settings/witness proof and one checked dispatch, enqueue and
native user append per original ID. This is a traced four-input diagnostic, not
a percentile, zero-overhead or sustained-fairness acceptance result. Original
79dd failures remain unresolved; P0 changed fixture verification timing.

Evidence lives under `/tmp/pi-message-delivery-stage-06680120.KZPkOb/`:
`TestPiMessageDeliveryNativeStageDiagnostic.jsonl`, original `trace.out`, existing
`trace.parsed`, and I1's streamed `P1-events.txt`/`P1-four-ID-table.json`. Reuse
targeted extracts; do not reparse the binary or load the 3 GB parsed file wholesale.
I0 owns native/question attribution; I1 owns local/commit/dispatch attribution.

Times below are milliseconds. IDs show their final four characters; all original
IDs retain the complete 32-character value in evidence. HTTP start is each trace
task's start, inside the complete-body sample interval. The unresolved outer-start
offset is at most 0.021 ms (plus trace quantization); no marginal percentiles are
subtracted. Commit-to-acceptance uses the existing sample hook, not the later
formatted trace log. It is a post-persistence request-write upper bound, not native
worker completion. The claim marker follows successful autocommit and the one-row
CAS check; its time is a post-commit upper bound, not an exact disk syscall time.

| Original / member | HTTP response | Successful COMMIT offset | Five disjoint ready joins | COMMIT region | Commit to claim | Commit to acceptance-hook upper |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1007 / lead | 239.071 | 238.627 | 191.149 | 3.969 | 939.052 | 1477.888–1477.898 |
| 1008 / architect0 | 279.659 | 279.303 | 214.284 | 2.648 | 1707.897 | 2160.347–2160.363 |
| 1009 / implementer0 | 268.924 | 268.225 | 218.246 | 3.556 | 322.388 | 809.633–809.652 |
| 100a / observer0 | 284.981 | 284.226 | 227.409 | 3.360 | 2266.326 | 2803.602–2803.609 |

Five ready/local joins account for about 80% of HTTP time in this probe. Two
selection reads add 30.038–34.644 ms. Upload work is 0.804–14.431 ms; SQL callback
excluding COMMIT is 1.726–4.809 ms. Most store waits are sub-millisecond, with one
6.238 ms connection wait and one 8.976 ms initial registration wait. These are
nonoverlapping elapsed categories, not CPU measurements. SQLite COMMIT is not
the principal admission cost here; no authority check may be dropped on that basis.

| Original | Foreground wait | Session-admission aggregate | Bind + Verify | C checked port | Manager Dispatch (inside C port) |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1007 | 0.105 | 509.484 | 360.412 | 126.764 | 126.700 |
| 1008 | 0.020 | 1464.592 | 147.101 | 107.578 | 107.521 |
| 1009 | 0.024 | 160.102 | 80.541 | 121.035 | 120.988 |
| 100a | 0.034 | 1834.923 | 352.942 | 142.996 | 142.948 |

Session admission includes lock wait and owning validation; their split remains
unknown. Bind/Verify and C-port work are nested within the effect/lease interval;
the Manager column nests inside C and must not be added again. All four C calls
returned Pending without error. Native enqueue-frame write entry followed C entry;
successful serialized writes took 0.148–2.299 ms, with commit-frame writes
0.161–0.236 ms. Those durations do not measure native execution. Production
Accepted Lookup took 134.160–477.999 ms inclusively. Deferred independent fixture
proof took 79.505–165.559 ms after the timed endpoints and retained every witness.
No native/session-lock optimization follows from grouped times alone.

### F3: question fixture contract correction (sufficient, lead accepted)

The lead question was genuinely pending with options and CanRespond=true in three
initial and four quiet observations. The only response POST occurred in the quiet
interval and returned 400. Its `answerID = s.id()` produced 32 hex characters,
where `piquestions.ValidID` requires the hyphenated UUID generated by
`piquestions.UUID()`. `validAnswers` rejects that ID before persistence. The four
response GET 404s are invalid-route rejection, not evidence about a missing valid
original receipt. No response was admitted and no scheduler starvation or progress
is established. The reviewer 403 and neighboring activity/collection 404s occurred
in the canceled stop tail; they do not prove access loss.

Owner implementer0 after completed P2 diagnosis/capacity, per lead allocation;
first index window. Limit source to the two existing tagged V files and the
existing `web/pi_questions_test.go` only if needed for the owning regression.
Use `piquestions.UUID()` only for question response IDs; preserve durable delivery
IDs, exact question ID/revision/choice, genuine CanRespond evidence and admission
checks. Preserve exact same-response status/persistence sequence matching.

Prove the boundary through the actual `PiQuestionHandler` and disposable
`piquestions.FileStore`, using a published question and correct Origin/JSON headers:
32-hex response ID is rejected without persisted response; generated UUID is
accepted with matching ID/question/revision and positive sequence, and exact GET
recovers it. Reuse existing handler/store test setup; this regression is an ID/wire
contract proof, not native eligibility/fairness evidence. No production validator,
route, capability, authorization or native receipt changes.

Normalize method/path before JSON decoding so non-JSON failures retain their
operation identity. Record Content-Type, bounded generic plaintext error and
request-context cancellation at completion. Existing `workflowError` uses standard
HTTP status text; retain only known generic errors (including ordinary not-found
text), not arbitrary body echoes. Never retain request contents, authentication
headers or credentials. Preserve raw failure counts and identify the canceled
stop tail instead of turning it into success or access-loss evidence. Extend the
existing outcome helper/tests, with no logging framework.

Quick gate: focused actual handler/store ID regression and existing pure outcome,
counter/pipe checks, plus tagged compile-only. Commit under the lead's window and
include this fixture correction in affected review. It is independent of local
admission optimization. No native rerun is authorized by this brief; corrected
200-sample performance/fairness acceptance remains required after verified source.

### P2 local admission correction (sufficient, conditional safety proof satisfied)

Lead accepted the private-read ordering alternative subject to owning proof.
I1's bounded inspection confirms `inputdelivery/refusal.go:Resolve` only reads the
existing queue/refusal identity, decodes it and compares the complete request.
Its retained-connection `Store.access` gate/mutex/cancellation bookkeeping introduces
no queue/refusal row, upload action, native work or exposed result. It performs no
BEGIN/COMMIT/Admit/Reject. This satisfies that condition; no additional trace is
needed to establish the selected correction's boundary.

Reject the earlier proposal to reuse pre-Resolve authority: the existing fresh
post-Resolve access/scope join prevents stale upload/catalog actions and refusal
tombstones. `piSessionUploads` validates its supplied admission and removal history;
it is not a substitute for fresh authorization. A final rejection after uploads
would not preserve that earlier boundary.

Owner implementer1 after its P2 completion/capacity and explicit lead release;
I0's F3 index window precedes this commit. Source boundary:
`portal/internal/web/pi_input_delivery.go` and its existing focused test file.
No store, shared-provider, browser, worker, protocol or schema change is needed.
Use a private `verifyCurrent(ctx, id) (piConversationAdmission, error)` helper
which performs the complete existing Verify contract and returns its freshly
proved admission; public `Verify` remains a wrapper with the same behavior.

For `AdmitDelivery` only, the settled order is:

1. Check exact bound identity and structural scope before touching the store,
   using the existing canonical scope encoder and host-profile check. Do not
   infer a different conversation, refresh a selection or accept a supplied scope.
2. Capture the result/error of private read-only `Store.Resolve`. Do not return,
   expose a status/proof, or act on any disposition yet. This intentionally moves
   this private SELECT ahead of the provider's own full authorization; the HTTP
   resolver and shared HTTP Verify still precede it unchanged.
3. Run mandatory fresh `verifyCurrent` after Resolve, including current host
   profile, complete ready/retained identity, projected access, generation and
   conversation-message permission. Failure overrides every captured outcome:
   existing row, conflict, negative proof, storage error, cancellation or not-found.
   Direct provider callers receive no result without this full check.
4. Only now process the captured Resolve result under its existing semantics.
   For a new ID, use this same freshly proved admission for the initial selected
   tuple. There is no intervening wait/effect before this initial selection that
   justifies discarding the fresh proof and repeating the identical join.
5. Preserve selection/mode validation, refusal ownership, uploads and the complete
   existing final post-upload `local` + `selected` reread/full-tuple equality before
   durable admission. Preserve dispatch's separate fresh authority and native
   preflight before claim, and its checked effect proof afterward.

No authority result is cached in context, on the provider or between calls. Each
Verify invocation stays fresh. No stale pre-read proof grants an upload/refusal.
The only reduced work is one discarded full join per new POST: observed cost of
that join was 35.907/39.600/42.386/46.191 ms for the four traced IDs. This call-count
reduction is demonstrated; neither its eventual latency nor target success is
established. Status/collection and legacy/native paths retain their contracts.

Focused acceptance uses existing native-free real handler/store fixtures and
deterministic barriers, not sleeps or new production hooks:

- Wrong bound identity/scope refuses before Resolve. During Resolve, revoke access
  or change scope/binding/current generation; full post-read verification must
  prevent uploads, Admit/Reject and exposure of status or negative proof.
- Exercise each captured outcome (existing exact ID, changed request/conflict,
  durable refusal, not-found and store/cancellation error) with post-read auth
  failure; authorization failure wins. Include direct provider calls so shared
  HTTP verification cannot hide a missing provider check.
- With valid current authority, exact old IDs retain immutable status/refusal
  recovery despite selected settings changes; changed requests still conflict.
  New IDs retain capability/retained-worker and stale selection refusals.
- Changes during upload preparation remain caught by the final fresh tuple check
  before queue persistence. Preserve existing native-lock-held/local-zero-RPC,
  attachment scope, concurrent dedup/refusal and recovery regressions.

Keep trace regions truthful after the refactor, with no extra instrumentation
package. Run the focused affected HTTP/admission tests and required quick checks,
commit, then give the retained reviewer this ordering delta and full error/proof
precedence. Lead owns the rebuilt exact candidate and corrected 200-sample cell;
no new native diagnostic, 100k campaign or performance claim follows automatically.
Native/session-exclusive optimization remains separate and unreleased: grouped
wait/proof cost cannot justify moving resumable unclaimed work past the claim into
Unknown or dropping positive live preflight, exact history witness or fresh checks.

## N1: explicit single pre-claim live preflight (sufficient narrow brief)

N0's owning-source pass establishes that current `Manager.Bind` and the returned
`conversationAdapter.Verify` both call `verifyConversation` with the exact handle.
The checked queued driver currently invokes them consecutively. Keep one complete
positive live probe before durable claim; removing both would move pre-existing
unavailability across the claim and turn resumable queued work into Unknown or
another post-claim outcome. A live probe is not a guarantee that the process cannot
fail afterward. All post-claim ambiguity remains original-ref Lookup-only.

Make this dependency explicit on the existing optional `QueuedInputController`:

```go
PreflightQueuedInput(context.Context, agentbackend.ExecutionHandle) error
```

Its success means one fresh positive proof of the selected exact handle's live
worker availability under the owning Manager's current identity, instruction,
settings and held-state checks. It does not grant authorization, checked-input
capability, a durable receipt, or authority for a later effect. The caller retains
the existing local selection/capability/lineage gates. The Manager implementation
checks context cancellation, calls existing `Bind` exactly once and discards the
returned operations, then checks cancellation again after successful Bind. Calling
Bind preserves its handle validation, complete `verifyConversation` path and final
`activityAvailable` frozen-contract/error check; calling only verifyConversation
would omit that last existing check. No operations or proof are retained/cached.

At the existing queued-driver pre-claim site, replace Bind plus immediate adapter
Verify with the required `controller.PreflightQueuedInput` call. Keep existing
unavailable error classification so a failed preflight does not claim, enqueue or
create a new attempt. Missing support fails closed through the optional controller
boundary; do not silently fall back to a plain Bind, generic Verify or Send.
There is no concrete-type branch and no change to generic Bind/Verifier contracts.

Leave every lease and local join unchanged: transition SH and session EX lifetime,
lease active/context checks, fresh local identity/access/current joins, message
lock, current profile, workflow attachment ACK, invalidation and permission grant.
Retain uploads and all checked-send/CURRENT/lineage/host inspection/handshake/process
checks before the native effect. In particular retain both C's outer admission
check and `inputDeliveryLocked` checks: `c.mu` does not freeze workflow permits,
attachments or callbackUnknown. `finishInput.holdInput` can change held state
without that mutex. No settings/policy/instruction/history witness check is removed.

Compatibility and immediate consumers:

- Production Manager implements the method by the existing path above. Its
  frozen-current scalar/legacy identity selection and strict error behavior remain
  unchanged; declared scalar failure never falls back. A legacy worker with no
  checked-input capability remains ineligible for new queued admission. Ordinary
  legacy `/message`, Bind, Verify and native receipts remain exact supported paths.
- V's `deliveryNativeRuntime` embeds Manager and inherits the method. Its concrete
  worker, frame observer, checked dispatch and exact witness paths stay unchanged.
  Generic `centralCreationRuntime.Bind` delegation is not changed or treated as an
  implicit checked-queue proof contract.
- The direct checked mock `localDeliveryRuntime` must implement the new method with
  fresh live/exact-handle and before/after context checks plus focused failure/race
  controls. Unrelated generic Bind/Verify mocks and freshness tests remain unchanged.
- This is an internal Go optional-port extension within the packaged portal, not
  a new native operation/capability bit or persisted format. No worker/supervisor
  wire, package contract, shared HTTP/browser interface, receipt or schema changes.

Proposed owner implementer0 after N0 completion/capacity and lead release. Files:
`piruntime/queued_input.go`, its owning tests (and `conversation_identity_test.go` only if its
existing proof fixture is reused), `web/pi_input_delivery.go` and its owning tests,
plus the queued-delivery contract in `docs/pi-runtime.md`. Paths are under
`portal/internal/` except the documentation. Runtime/test/docs edits can be
independent of I1's local correction; shared driver/test edits wait for I1's
completed source/index window. Lead controls that sequencing and final release.
Keep the existing trace truthful by naming the driver region as a single preflight;
historical Bind+Verify timing stays labeled as the 0668 observation.

Focused acceptance and quick checks:

1. Actual Manager preflight performs exactly one existing live identity proof on
   the scalar path, preserves retained legacy proof/frozen-contract refusal, never
   Load/Ensure, and fails cancellation both before and after proof. Existing generic
   Bind/Verify freshness tests still prove independent fresh calls.
2. With an otherwise eligible saved selection, unavailable/unloaded/preparing,
   stale-live/held or canceled preflight leaves the original row unclaimed and
   retryable with zero native enqueue. Once availability recovers, that original
   immutable ID/ref/input sends at most once. Preserve existing terminal handling
   for positively changed logical selection; this package does not redefine it.
3. Assert preflight completes before claim; changes to identity/process/settings,
   policy, instructions, held/callback or permit after preflight remain caught by
   the unchanged checked effect path. An unavailable wire after claim stays
   Unknown and Lookup-only; never requeue or replay it.
4. Run focused owning Go preflight/driver/queued-input tests, existing relevant
   freshness and ambiguity regressions, and tagged compile to prove V composition.
   No new native run/build or benchmark is included in implementation.

Deliver exact changed paths/head, optional-port consumers, checks and preserved
mixed-version/recovery behavior. Commit all intended changes and obtain affected
independent review before the lead builds/runs corrected performance acceptance.
No additional lease-join, native readiness, witness or scheduler optimization is
released by this brief. Neither the 0668 four-input probe nor the call-count
reduction establishes the 200-sample latency/fairness targets.

## P3: corrected probe comparison and remaining native constraint

The corrected StageDiagnostic used exact
`e6626ff692bc99c3d9efb0fe428333dfe29759fc` and
`/nix/store/ar1z2lz18yfxfwidx9jd4lj6q6x19iki-dev-workspace-0.2.0`; the native worker,
SDK and catalog tuple are unchanged. Machine evidence is
`/tmp/pi-message-delivery-corrected-probe-e6626ff6.MrNuiB/TestPiMessageDeliveryNativeStageDiagnostic.jsonl`
with `trace.out`, the single streamed `events.txt` (7,975 lines), and I1's
`P3-four-ID-table.json` in the same directory. The utility test log is a captured
tool transcript, not direct raw stdout/stderr; JSONL/provenance/binary identity and
exit status are the run evidence. The extraction log is
`/tmp/2026-11-23-pi-message-delivery-corrected-trace-events-e6626ff6.log`.
Do not reparse the binary or recreate a multi-gigabyte textual trace.

All four inputs were Sent with exact Accepted proof and one checked call, enqueue
and native user append each. F3 also produced a genuine admitted question response
and later Accepted observation. This additional work and a different dispatch
order make the workload different from 0668, not a controlled per-ID regression
comparison. Neither four-sample run establishes p95 or sustained fairness; the
original failed 200-sample acceptance remains unresolved.

Times are milliseconds, using the same trace/sample endpoint qualifications as P2.
The outer sample-start alignment widths are at most 0.015369/0.018671/0.023152/
0.007244 ms in row order, plus trace quantization.

| Original / member | HTTP task | Successful COMMIT offset | Four disjoint ready joins | COMMIT region | Commit to acceptance-hook upper |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1007 / lead | 198.545 | 198.052 | 146.111 | 11.665 | 3195.798–3195.814 |
| 1008 / architect0 | 215.963 | 214.055 | 161.189 | 3.090 | 1126.092–1126.111 |
| 1009 / implementer0 | 209.123 | 208.671 | 159.021 | 3.231 | 2368.999–2369.022 |
| 100a / observer0 | 233.286 | 231.868 | 170.993 | 4.808 | 1749.321–1749.328 |

The local correction demonstrably removes one of five joins. Two selection reads
still total 26.024–31.426 ms; uploads take 0.562–0.903 ms. Successful COMMIT offsets
are below 250 ms in these four observations only. They do not establish the required
long-history/team p95, and traced timing is not zero-overhead timing.

| Original | Session-admission aggregate | Lease inclusive | Single preflight | C checked port | Preflight start to matching identity request entry | Full-write log to preflight return |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 1007 | 2014.120 | 612.042 | 323.644 | 242.542 | 23.893 | 299.727 |
| 1008 | 345.719 | 232.558 | 47.454 | 133.324 | 24.832 | 22.545 |
| 1009 | 1313.669 | 561.030 | 386.407 | 112.996 | 31.867 | 354.504 |
| 100a | 617.782 | 607.704 | 417.079 | 132.672 | 22.732 | 394.320 |

These stages nest; do not add lease, preflight and C totals. Foreground acquisition
is only 0.017–0.030 ms. Each preflight contains exactly one matching identity_v1
frame, joined by the full ExecutionHandle, with a successful full write. Actual
serialized write durations are 0.108–0.172 ms. For three inputs, almost all of the
slow preflight lies after the request write, not in local/host/supervisor pre-write
work. The entry/return logs have small observation offsets and are not worker
reply-completion markers.

The checked-dispatch order is now architect0, observer0, implementer0, lead.
From session-admission return to lease end, their proven minimum exclusive holds
relative to the earliest HTTP task are [571.439,824.671], [864.308,1493.862],
[1539.582,2125.921], and [2218.504,2847.841] ms. Other owners' disjoint holds overlap
lead/implementer0/observer0 admission aggregates for at least 1469.124/882.786/
253.232 ms. These are **exclusive-lock unavailability overlaps**, not measured
time blocked inside LockRuntimeExclusiveContext: pre-lock work and scheduling are
not separately marked. They establish a serialization constraint without an
invented exact wait decomposition. Post-release driver defers are excluded.

The real question POST spans [519.774,3455.177] ms, with 2098.461 ms overlapping
other owners' proven holds. Its own native-origin capture is proven EX-held work
at [2891.089,3388.659] ms, after all four driver minimum holds; it overlaps the
lead's asynchronous input-wait-to-commit interval, not the lead's C-port interval
[2604.828,2847.303]. Overlap does not assign the whole capture duration as delay
to the lead. The question's native Send begins at +4278.513 ms, after the last
queued public Sent at +3524.290 ms, and cannot explain earlier queue latency.
Public question Accepted at +6707.560 ms follows the genuine POST202/persisted
sequence 1; POST-to-observed-Accepted 6187.795 ms and 202-to-observed-Accepted
3252.290 ms include public polling. All 17 HTTP failures are explicitly canceled
stop-tail outcomes, not observed active access or product failures.

### Remaining boundary; no additional optimization released

The dominant measured delivery stages are session admission and the preflight/C
work serialized under it. The slow preflight's unexplained component is now
specifically **after successful identity request write and before preflight return**.
That interval includes the native/control reply plus Manager's post-reply exact
proof, ReadInputSelection and activityAvailable checks. Existing events lack the
correlated response-completion boundary needed to partition it further. Do not
label it worker CPU, conversation-mutex wait, fsync or a particular history scan.

The scalar identity operation remains constant-size metadata work. Other required
history operations share the Node process: Accepted Lookup reopens/verifies the
exact original witness; finishInput's post-hook snapshot updates Thinking,
HistoryFile, Persisted and held mapping state. Their request intervals overlap
sibling preflight/C work, but current evidence does not prove one removable scan
or a safe replacement. Keep positive pre-claim availability and every fresh
CURRENT/profile/host/identity/settings/instructions/policy/ACK/permit/callback/
held check and exact witness. Do not weaken EX/SH, cache proof, or move unavailable
unclaimed work into post-claim Unknown to improve this measurement.

N0's separate possible private reuse of captured host Binding/Authority/SavedAccess
under uninterrupted session EX and transition SH is not released here. Generic
lease.run cannot be weakened, and these timings do not isolate that join's benefit.
No further redundant native proof or worthwhile safe performance correction was
established by this bounded pass. If the lead elects further attribution, the
minimal missing evidence is the correlated control/native response-completion
point within the already identified preflight interval; this is a precise evidence
boundary, not authorization for another marker, profiler, source edit or native
run. No extra inventory, full parse, 200-sample or 100k campaign is started by P3.

## Existing receipt checkpoint: bounded acceptance-endpoint brief

I0's single owning-source pass at e662 confirms an existing test-only seam. In
`finishInput`, successful `saveOwned(Accepted)` precedes `point("receipt")`, while
`e.mu` is held and the completing `liveInputs` owner remains present. The owner is
deleted before that mutex is released. `saveOwned` uses `writePrivateBytes`, whose
successful return follows temporary-file write, Sync, Close, Rename and parent
directory Sync. The earlier native/witness checkpoints do not establish durable
acceptance. No production callback, native operation, wire field, receipt or
schema change is needed to observe the existing receipt checkpoint.

The callback takes only a point string, so that string alone cannot identify a
sample. For timed dispatches, V registers an immutable copy of the exact
`QueuedInputRequest` after the existing before-dispatch hook and before delegating
to Manager once. Retain full Ref/Input/Settings, selected handle and full execution
runtime, not merely the client ID. At the receipt checkpoint, capture `time.Now()`
on entry, before observer verification I/O. Under the already-held engine mutex,
inspect its live owners using the existing nonlocking strict `loadOwned` reader.
Require one unique Accepted-and-still-live candidate, exact retained ref, input,
settings/digest and execution generation, plus the NativeWitness session, entry
and effective digest matching the registered full expectation. Previous completed
Accepted files have no live owner and cannot identify this event. Other pending
owners remain prepared/dispatching. Publish the captured time only after that
exact match succeeds; never infer identity from latest file, text, mtime or bare ID.

Keep ordinary untimed work outside the sample set. For an expected timed result,
missing, malformed, wrong-scope/execution, ambiguous or absent-live-owner evidence
leaves the checkpoint time unavailable and fails its measurement assertion.
Do not substitute the later commit-write hook, a wall-clock receipt field, or
public Sent. Repeated observations cannot replace the first valid identified
timestamp. Retain the same in-process monotonic clock as HTTP start. This is an
**identified post-durability checkpoint upper bound**, not the exact fsync return,
SDK consumption time or worker commit completion. An upper bound above one second
alone still cannot prove the underlying acceptance exceeded one second.

The observer must not relock `e.mu`, take `c.mu`, call Manager Lookup/Inspect/
ReadInputSelection, issue native work or call Idle. Capture immutable fixture owner
data when installing it; use only the protected live-owner map, strict local
receipt reader and a short existing counter lock inside the callback. Preserve
the existing engine-to-counter lock order; registration/getters must not hold the
counter mutex while taking the engine mutex. Observation failures are measurement
errors only and cannot change production checkpoint return values or records.

Compose with the existing `FailReceipt` behavior explicitly. Its matching fault
currently returns before delegating to the prior callback. Install the observer
as the outer wrapper after fault setup, observe first, then delegate exactly once
and return the exact delegated error. Preserve restoration, and re-arm the observer
before later timed dispatch when restoring the fault wrapper would remove it.
A later outer injector that suppresses observation produces missing metric
evidence, never fabricated success. Do not replace or swallow injected failures.
The current retirement case faults at `native` and expects no Accepted endpoint.
Receipt-checkpoint faults and subsequent commit/snapshot failures must retain their
original holds/errors even when an earlier durable timestamp was captured.

Proposed owner is implementer0 only after lead allocation. The complete file
boundary is the existing tagged `portal/internal/piruntime/`
`pi_message_delivery_fixture_test.go` and
`pi_message_delivery_integration_test.go`. Reuse their existing expected-request,
counter and sample structures; no production helper, general observer framework,
new profiler, extra response marker or runtime interface. Keep the existing
commit-write upper, public Sent, exact independent Lookup/ref/input/settings/witness
assertions, enqueue/user-append counts and all late error/hold evidence distinct.
The checkpoint does not replace any of these proofs or make a held sample healthy.

Focused quick proof covers exact full-scope/execution attribution; multiple live
pending IDs and a sole completing Accepted owner; wrong/missing/ambiguous evidence;
old Accepted without a live owner; first-event stability; and callback fault,
delegation, restoration and lock-order behavior. Use the actual existing owning
receipt writer/reader in disposable native-free fixtures where applicable, so the
test proves this seam rather than a newly invented persistence substitute. Compile
the tagged suite and run the affected native-free fixture checks. Record observer
verification duration separately from delegated fault behavior using the existing
fixture counters. Capturing entry time excludes that observer work from this
sample's endpoint, but its receipt reads/mutex occupancy can delay sibling work;
report that overhead and the changed measurement method without claiming zero cost.

Deliver the normal commit and focused evidence for affected independent review
before any native acceptance run. Lead owns allocation, review/build sequencing
and the next bounded 200-sample cell. No additional native probe is required by
this brief, and neither prior four-sample data nor this seam establishes the p95
targets. P3 component attribution stays closed; no native guard, witness, EX/SH,
authorization, settings, recovery or no-replay behavior changes are released.

## P4: scalar metadata after accepted input (sufficient narrow brief)

The final audited 10k/team cell at
`176706a605119b64f4efd24f0b2f25957caa7298` completed 20 warm and 200 measured
inputs, all Sent with exact independent Accepted witnesses, 40 per conversation.
Use only the final `auditCompleted:true`, `partial:false`, `passing:false` summary
in `/tmp/pi-message-delivery-perf-10000-team-176706a6.rd3wbgfz/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl`;
the direct raw log is
`/tmp/2026-11-24-pi-message-delivery-perf-10000-team-176706a6.log`.
Measured p95 HTTP upper is 296.507316 ms, identified post-sync checkpoint upper
3085.647177 ms, commit-write upper 3086.875387 ms, and public Sent upper
3488.572189 ms. The genuine question reached Accepted during measured foreground
work. Late hold/commit-write/delegate errors are zero. The measured interval has
201 snapshots, 400 verify_history calls and 200 enqueue/commit calls each;
receipt observation performed 200 reads without errors, totaling 378.113111 ms.
These counts do not assign durations to individual operations. P3 attribution is
closed; the latency targets remain unestablished, with the receipt target missed.

### Owning proof and accepted semantic boundary

`finishInput` persists the original exact Accepted witness, passes the receipt
checkpoint, obtains `input_commit_v1` acknowledgement, then takes `c.mu`. Only
when `c.worker == live.worker` does it call `observeState`. That caller discards
the returned state, but requires its mapping persistence and error/hold behavior.
`observeState` consumes the following worker fields; each already exists in the
strict `workerIdentityProof` returned by `identity_v1`:

| Field | Live source shared with snapshot | Required post-input use |
| --- | --- | --- |
| NativeID | SessionManager.getSessionId | Match the owning native identity |
| HistoryFile | SessionManager.getSessionFile | Validate owning history directory and save actual path |
| Persisted | existsSync of that live history file | Refresh mapping flag, not replace a durability witness |
| Model / Provider | AgentSession.model | Match saved model/provider |
| Thinking | AgentSession.thinkingLevel | Save actual observed thinking, not require old-value equality |
| Busy / Held | Same pending/input/streaming/host-call and held flags | Preserve state projection and held precedence |
| InstructionsDigest | checkInstructions | Preserve actual instruction proof and workerProcess digest comparison |

SDK 1.5.2's ID/file getters return their current scalar fields. Its `getBranch`
walks the parent chain; snapshot then renders bounded entries and hashes serialized
history. `observeState` consumes no entries, live message, leaf, history digest,
history position or total. This snapshot is not an independent linear-history or
durability proof. `observePersisted` still validates the exact user object, captured
prefix, allowed ancestry, independently reopened native history and storage sync
before Accepted. Original Lookup still performs its full verifyHistory/witness
proof. Neither changes.

Lead accepted the explicit narrowing of this one metadata-refresh site. It no
longer constructs transcript pages/hashes or treats a display-only 512 KiB entry
failure as a new post-input hold. Those checks and errors remain unchanged in real
transcript/full-snapshot consumers. Do not describe this as preserving every
snapshot-only error at this site; add focused separation tests and document it
beside the runtime contract. No snapshot or witness result is cached or fabricated.

### Private implementation boundary

Add a private post-input observation helper, called only from the existing
`finishInput` site after acknowledged commit and the same-worker check under
`c.mu`. Select support with the existing `readConversationIdentityContract` against
**this supervisor's immutable `s.launch.AppStorePath`**. Never use the installed
portal/profile, a new CURRENT successor, metadata protocol number, or a trial RPC
to infer support. Valid absence of `piConversationIdentity` delegates to the exact
existing `observeState` snapshot path. Contract read/parse/version failure returns
an error. Advertised support issues one fresh `identity_v1` through the current
worker with the existing strict typed decoder, exact frame identity and instruction
digest enforcement. Any scalar failure returns an error, with no snapshot fallback.

Share only the existing application of observed metadata: native identity and
owned-history-directory checks, saved model/provider equality, actual Thinking/
HistoryFile/Persisted updates, `c.save`, then existing receipt-held and callback/
pending/held state aggregation with the same ordering and locks. A small private
metadata value/helper may carry these consumed fields; it must not masquerade as
a complete transcript snapshot. Generic `observeState` continues to obtain a full
snapshot before using that common application. All other callers, including load,
ordinary state, configure, legacy Send and unload, retain their existing operation.
Do not switch generic observation to identity or change its error contract.

Do not call `identityProofLocked`: it intentionally requires saved Thinking and
HistoryFile equality, whereas this post-input path refreshes their actual values.
Do not refresh InitialSettings, settings revision, policy, instructions, history
locator, generation, owner or worker selection. Preserve `c.save` failure behavior,
receipt-read errors, callbackCount/callbackUnknown under activeMu, worker Held,
HeldReason, PendingSettings/PendingToolPolicy and returned generation exactly.
A successful Held projection remains Held; it is not an additional native hold
command. Existing observation errors still reach `holdInput`. Do not turn an
already Accepted receipt back into Unknown or resend it after any later failure.

Keep the complete finishInput context/lifetime, inputTasks join, deferred
workflowChanged, worker commit notification, mutex boundaries and same-worker
replacement check unchanged. Native commit failure still holds before observation;
observation/save failure still holds afterward. Positive pre-claim availability,
EX/SH, authority/profile/settings/ACK/permit/callback checks and all native receipt
recovery remain outside this correction.

### Ownership, compatibility and verification

Proposed owner: implementer0 after explicit lead allocation and an exclusive source/
index window. Exact files are `portal/internal/piruntime/input_delivery.go`,
`conversation.go`, `input_delivery_test.go`, `supervisor.go`, `supervisor_test.go`,
`pi-runtime/src/protocol.test.mjs`, and factual `docs/pi-runtime.md` text. The two
supervisor files are limited to a private contract-reader seam following the
existing Manager pattern: production defaults to the existing frozen-package
reader; fakeHost uses its Manager's existing exact fixture reader (legacy false
by default, actual frozen reader in V). Do not create a public option, capability
cache or new package format to accommodate fake paths. No V measurement changes,
worker implementation changes, browser/provider edits or new runtime contract bit
are needed. Lead owns the documentation writing pass after facts settle.

Lead approved one additional actual-consumer adjustment in tagged
`portal/internal/piruntime/pi_message_delivery_fixture_test.go`:
`CheckpointFinishFaultComposition/snapshot` explicitly selects valid legacy
absence on the fixture supervisor's private frozen-contract reader before
finishInput. Limit this to the conditional and explanatory comment for that case;
keep its exact snapshot fault, late hold and checkpoint evidence assertions.
The checked fixture otherwise declares scalar support, so retaining its old
snapshot assumption would test the wrong branch. New scalar failure coverage
stays in `input_delivery_test.go`. This exception changes neither V metrics nor
runtime bootstrap and suppresses no fault or proof requirement. I0 retains this
source/index window; I1's disjoint F4 commit follows it as allocated by lead.

An old retained supervisor keeps its old implementation. The new supervisor uses
its own frozen worker package: a declared legacy pair retains the exact snapshot
reply and cost; a declared scalar pair uses the unchanged identity_v1 reply. A
claimed scalar package with an old/malformed/unavailable worker fails held without
fallback. Installing a portal alone does not change a retained runtime. There is
no migration, receipt change, upgrade prerequisite or new persistence namespace.

Required focused quick checks:

1. At actual finishInput completion, assert original Accepted/witness bytes and
   native commit acknowledgement precede exactly one post-input identity request;
   no post-input snapshot is made on the supported path. Replace or remove the
   worker before the existing final check and prove it is not queried or mutated.
2. Compare common metadata application for scalar and snapshot fixtures: actual
   Thinking change, owned HistoryFile refresh, Persisted flags, busy callbacks,
   worker/receipt/callback/pending holds and unchanged returned generation/settings.
   Wrong native/model/provider/path/instructions, malformed scalar, canceled/error
   call, corrupt receipt or mapping-save failure must preserve the original hold/
   error and no-replay behavior, with no fallback. Use existing receipt fault tests
   for failures before/after Accepted and commit, not a second receipt engine.
3. Prove frozen-package support selection and explicit legacy fallback; an
   installed/newer package cannot enable an older retained pair. Cover advertised
   scalar failure and real strict instruction/reply checks. Legacy snapshot bytes,
   ordinary state/load/configure/Send and full transcript consumer behavior stay
   unchanged, including display-bound errors.
4. Extend the existing Node scalar test to compare all consumed live fields with
   snapshot under normal data, then make branch traversal fail or supply an oversized
   display entry: scalar metadata remains available, full snapshot still refuses.
   Preserve instruction-loss refusal in both paths. Do not simulate this by returning
   cached metadata or bypassing the actual WorkerSession methods.
5. Run focused affected Go input-delivery/observation/identity/legacy receipt tests,
   the owning Node protocol checks and tagged compile. No native launch, build,
   profiler or longer campaign belongs to implementation's quick-check package.

After all intended commits and quick checks, obtain affected independent review
of this semantic boundary, full consumer/error mapping and retained pairing.
Lead then owns the rebuilt exact candidate and the same bounded 20-warm/200-measured
10k/team acceptance cell with the existing real five-conversation fixture. Preserve
all independent witnesses, exact original IDs, one enqueue/user append each, final
audit and late-health checks, genuine question progress, endpoint definitions and
observer-overhead disclosure. Existing counters should show scalar metadata in
place of each supported finishInput snapshot; unrelated full snapshots remain.
Do not reduce the production or fixture verify_history assertions to improve time.

The removed full snapshot occurs after this input's durable acceptance checkpoint;
the plausible benefit is reduced subsequent shared-Node work and c.mu occupancy
for siblings/later inputs. Its duration and saved latency have not been measured
in isolation. Mandatory witness/history work and local HTTP joins remain, so this
brief promises neither target. Report the actual p95 values and limits; a high
checkpoint upper alone is not an exact underlying acceptance measurement. Larger
history/matrix execution requires the lead's next decision after the affected
target result. N0 private lease-join reuse and further profiling remain unreleased.

## F4: creation VM retained-start refusal parsing (sufficient fixture brief)

Exact 1767 CI run 45348306901, attempt 1, passed fast/archive and failed creation
job 138288188603. The full direct log is
`/tmp/2026-11-24-pi-message-delivery-ci-45348306901-creation.log`.
Its final stack is generated test-script line 1241 to `session_source` line 52,
not `creation_wait_started`. Source is `nix/tests/session-creation.nix:1464`, in
“proxy-created roots regain source permission and actual managed clients.”
The failing invocation is the retained no-goal `start --as-is --no-attach --json`
for `2026-11-24-before`. It exits 1 on attempt one with a bounded diagnostic line
followed by the exact ordinary “another dev-session command is changing” refusal.
There is no evidence of a replay, corrupted journal or successful start at this
failure. Per lead's source comparison, the preceding passing e662 creation job
had identical production/VM source; T0 changed tagged fixture files only.

### Mechanism and intended contention contract

`session_source` already permits a 20-second total bounded retry window for the
two fixed start/sync commands, sleeping at most 250 ms only after a known exact
pre-admission refusal. Its current predicate accepts only the refusal string with
an optional final newline. Retained start now writes
`dev-session retained-start contention: <JSON>` before that same refusal. The
helper therefore treats a valid busy response as an unrelated error and aborts
immediately instead of using its existing allowed pre-admission retry branch.
This is a demonstrated fixture output-contract mismatch, independent of which
actor caused the original lock conflict.

In `libexec/dev-session`, no-goal start requests diagnostics at its ordinary
`with_slug_lock`. `with_host_lock` attempts EX|NB, emits the optional diagnostic
only after acquisition fails, then raises SessionBusyError without yielding to
the retained-start body. Do not change acquisition, waiting policy, generation/
provider checks, lifecycle authority or journal recovery. Existing
`test/dev_session/ordinary_readiness_test.rb` cases prove SH and EX refusal leave
manifest bytes intact, create no start/creation journal or authority, make no
native call, and release the outer creation lock. Diagnostic failure leaves the
same refusal; diagnostic success is bounded to one line of at most 8192 bytes.

The log's two READ rows for portal PID 22351 are a later, non-atomic sample on the
same observed inode. The record explicitly says
`subsequent_nonatomic_sample_not_cause`; it does not identify the original failed
flock's holder. The portal intentionally remains active here: the preceding stage
stops only the proxy transport and restores the original socket, then the stage
proves source permission/client recovery. Existing portal retry reconciliation
can take shared runtime admission (`turn_retry.go:261`); that is consistent with
the later sample, not proof of the exact cause. Do not stop the portal, infer a
lock leak, or relax success assertions to manufacture a quiet fixture.

### Minimal correction and acceptance

Proposed owner: implementer1 after explicit lead allocation; disjoint fixture
source may proceed alongside P4, with its Git/index window after P4 as assigned
by lead. File boundary is `nix/tests/session-creation.nix` only. Keep the existing
command construction, returned success output, total deadline, integer execution
timeout, attempts/error reporting and sleep bound. Introduce a small pure predicate
for recognizing this helper's permitted pre-admission refusal; do not add a general
CLI parser/retry framework or production flag.

The predicate continues to accept the existing exact one-line refusal for either
fixed command. It additionally accepts **start only**, status exactly integer 1,
and exactly two lines (optional final newline): one bounded diagnostic with the
fixed prefix and one exact refusal for the requested slug. Require a valid JSON
object in the diagnostic with `requested == "EX|NB"`, the exact fixture runtime
authority path for that slug, and
`interpretation == "subsequent_nonatomic_sample_not_cause"`. Do not use holder
PIDs, modes, process names, sample freshness or observed path status as retry
authority. The known command's exact final refusal and pre-yield owning code
establish that boundary; the optional JSON is preserved diagnostic context.

Reject malformed/oversized/wrong-path/wrong-operation diagnostics, duplicate or
extra lines, output containing any other error/success material, wrong-slug
refusals, noninteger/non-1 failures and execution/transport exceptions. Do not
strip arbitrary prefixes, match only the last line, or accept substrings. A missing
diagnostic remains compatible through the original plain-refusal form. Do not
recognize diagnostic-prefixed output for sync or any new action. Status 0 still
returns its original bytes for the existing JSON/identity assertions; no error is
treated as successful start. Unknown or possibly admitted outcomes are not retried.

Put compact pure parser/regression assertions beside the helper in the existing
test script, using a normalized version of the actual two-line failure and the
negative cases above. Prove plain refusal, diagnostic refusal, then successful
start preserve the current bounded loop behavior; persistent busy still reaches
the original deadline, and unknown output stops on the first attempt. A quick
source-derived Python check must execute these exact pure helper definitions and
cases without booting a VM, not a separately reimplemented classifier. Preserve
existing Ruby retained-start SH/EX and diagnostic-failure coverage; run those
focused owning cases as the production contract oracle. No production source or
new test framework is needed. Nix/test-script syntax validation is also required.

The VM's positive assertions stay intact: same original slug/thread, source socket
permission epoch, active source native unit and PID/invocation, original retained
team/creation proof and managed-client session/pane identity. Do not retry initial
goal submission, recreate a session, regenerate journals, or weaken source-ready
proof. The helper change repairs recognition of an already authorized fixture
retry; it does not turn production EX|NB into waiting or add a recovery policy.

Deliver the normal focused fixture commit and quick-check evidence for affected
independent review, sequenced after P4's index window. Lead owns any exact-candidate
creation VM/CI rerun after review; no rerun or lifecycle action is authorized by
this design investigation. A later deadline or different error must be reported
as new evidence, not hidden by a longer timeout or broad retry. This package does
not reopen P4, P3 attribution or unrelated lifecycle behavior.

## P5: current native history proof constraint (bounded investigation closed)

The reviewed/published source is
`474872b602afa0813e6a17a951646b5cf5a91a06`. Its final 10k/team campaign completed
20 warm and 200 measured inputs, all Sent, 40 per conversation, with the exact
independent Accepted audit complete and no late hold, failed commit-write or
receipt-delegate error. The genuine question reached Accepted during foreground
work. Selected final fields in
`/tmp/pi-message-delivery-perf-10000-team-474872b6.jkref_88/TestPiMessageDeliveryNativePerformance-10000-team_activity.jsonl`
show `auditCompleted:true`, `partial:false`, `passing:false`. Direct raw output is
`/tmp/2026-11-24-pi-message-delivery-perf-10000-team-474872b6.log`.

| Existing endpoint | Measured p95 |
| --- | ---: |
| HTTP durable receipt upper | 370.709134 ms |
| Identified post-sync checkpoint upper | 4180.481215 ms |
| Native commit-write upper | 4182.023815 ms |
| Public Sent upper | 4831.779510 ms |

The measured interval contains one full snapshot, 772 identity calls, 400
verify_history calls and 200 enqueue/commit calls each, plus 185 workflow
observations, 25 origin inspections and one ordinary Send. Receipt observation
performed 200 reads with zero errors, totaling 431.313831 ms. This confirms P4's
operation selection was exercised; different order/background activity and run
noise prevent assigning a latency regression or saving from the two campaigns.
Counts are not operation durations. The targets remain unestablished; an upper
bound alone does not measure the exact underlying native acceptance time.

### Required work in the inspected owning chain

The bounded pass covered WorkerSession `makeInput`, `observePersisted` and
`verifyHistory`, their `linearEntries`/storage-barrier helpers, original queued
Lookup's exact receipt join, immediate tests, and the methods they use in the
pinned SDK 1.5.2 SessionManager (`9hf2a7rz231w2pn50s4jlmrgs4007xc5`). No further
SDK/tree inventory, trace parse, native run or component attribution was performed.

- Admission captures the entire selected linear prefix and leaf. After consumption,
  observePersisted validates the current full linear selection, compares that
  captured prefix, finds exactly one occurrence of the caller-owned native user
  object, checks exact text and allowed intervening ancestors, and obtains the
  current history file. These observations occur at different stages; the earlier
  capture cannot replace the post-effect check.
- A fresh SessionManager.open independently loads disk history. Native ID/cwd and
  serialized complete linear entries must match the live selection before the
  owning file identity check and file/directory sync. Serialization intentionally
  uses native JSON semantics, including omission of optional undefined properties;
  replacing it with generic object equality would change the proof contract.
- Later original Lookup strict-loads the original receipt and validates its exact
  ref/input/settings digest, witness and generation lineage. Accepted then requires
  a fresh verify_history against the current file: full linear validity, native
  ID/cwd, exact original entry/parent/message and allowed ancestry back to the saved
  previous leaf. Missing or unverified evidence stays Unknown/error. This later
  independent observation is not redundant with the earlier receipt or another
  fixture Lookup, and cannot be shared, cached or deferred under this brief.

The SDK's SessionManager.open performs bounded header discovery followed by one
full loadEntriesFromFile parse and index construction. For the large-header
fallback, it passes the already loaded entries into the constructor; it does not
parse the whole file a second time. The loader preserves the SDK's current header,
line-loading and migration behavior. This path does not construct AgentSession,
model context or transcript display pages. getEntries makes a shallow array of
non-header entries; getBranch walks the selected parent chain into another shallow
array referencing the same objects. There is no second full object/display
reconstruction analogous to the post-input snapshot removed by P4.

linearEntries checks the complete record sequence for nonempty/unique IDs, exact
linear parents and prohibited branch/context edits, then compares selected leaf
and full selected branch. The existing count/index accessors do not by themselves
prove those facts: an indexed count can lose duplicate IDs or ignore the distinction
between complete history and selected branch. Replacing this combination with a
different per-entry algorithm would require a new equivalence proof, rather than
reuse an existing qualified history-proof seam. No such replacement is proposed.
Similarly, passing known cwd as SessionManager.open's cwdOverride skips header
discovery but makes getCwd caller-supplied, so the current independent disk-cwd
comparison becomes circular. It is not an admissible optimization.

### Decision and remaining constraint

No sufficient safe implementation package was demonstrated by this source pass.
With the required full-current-history proof and existing pinned SDK interfaces,
fresh Accepted verification continues to require work proportional to the current
history's bytes/entries. Its parse, serialization and traversal sections execute
synchronously on the shared Node event loop. That establishes a structural cost,
not its measured contribution to this campaign's latency or proof that one second
is impossible. No timing claim is inferred from the 400 verify_history calls.

Keep the current implementation, exact witnesses, independent reopen/sync, retained
settings/receipt semantics and all authority/preflight/EX checks. No parser, native
client, proof cache, stat shortcut, worker pool/IPC/protocol/schema change or proof
removal/deferral is released. N0 lease reuse remains separate and unreleased.
Immediate lineage/session/queued-Lookup tests were inspected as evidence, not run
or weakened; there are no implementation files or new quick/long checks to assign
from P5. Only this design record changed, with documentation diff validation.
Lead owns the subsequent product/implementation decision and user report. The
larger matrix remains held; this closure does not request another marker, profiler,
native diagnostic or benchmark to continue the same bounded investigation.

## P6: standard worker CPU profiling feasibility (closed constraint)

No qualified conventional capture path was demonstrated within the unchanged-source,
no-wrapper/no-install boundary. This was metadata inspection and one permitted
vanilla Node flag query, not a profiler or native test run. The exact retained
4748 artifact identifies app
`/nix/store/349aqdz8qil4yfag2h4fb7avkw2sarzj-dev-workspace-0.2.0`, SDK `9hf2a7...`,
and worker `sf66v6...`. Its `share/dev-workspace/pi-worker.json` is the fixture's
owning Node/entrypoint input; the fixture does not substitute a profiling launcher.

The pinned Node query reports v22.23.2 and permits `--cpu-prof`, its directory/name/
interval options, `--perf-basic-prof` and inspector options in NODE_OPTIONS;
`--prof` is not allowed there. The query used
`/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`, which reports
the underlying slim executable
`/nix/store/2gd4h12irmnanhg33md2rpjygrsj5ypb-nodejs-slim-22.23.2/bin/node`.
No SDK/session was loaded and no profiling option was enabled by that query.

`startWorkerHost` invokes only `exec.Command(metadata.Node, metadata.Entrypoint)`
and builds a fixed inherited-environment allowlist excluding NODE_OPTIONS. The
existing V constructor preserves this worker startup. Parent test environment
options therefore cannot enable the actual child profiler, even though Node itself
recognizes them. Changing metadata, executable/arguments, environment admission or
adding a wrapper would exceed this package's boundary.

There is also no guaranteed orderly profile-finalization boundary in the unchanged
StageDiagnostic. It joins its HTTP/proof/background work, but fixture cleanup and
the fixture host Stop call `piDeliveryKillWorkers`, using Process.Kill and waiting
for host closure. SIGKILL does not guarantee normal profiler finalization. Do not
change worker lifetime/cleanup or launch a test hoping that a complete profile
survives. Worker EOF has orderly protocol cleanup, but this fixture does not expose
it as an authorized profiling settlement seam.

OS perf was absent from PATH and the standard current-system, per-user and home
profile executable locations. Metadata showed perf_event_paranoid=2,
ptrace_scope=1 and zero current effective/permitted capabilities. These facts do
not prove all OS profiling impossible; they do not establish an available permitted
attachment route either. No tool was installed, permission changed or attachment
attempted. The one vanilla query exited normally; no profiler or native child was
started and no command effect remains to settle.

P6 therefore supplies no executable one-run brief and allocates no implementation.
Keep P5's proofs and the frozen worker/startup boundary intact. No new debugger
client, daemon, callback, hook, marker, protocol or cleanup layer is proposed, and
no further profiler inventory or native follow-up is requested. Lead owns any new
scope decision; StageDiagnostic and the larger matrix remain unlaunched by P6.

## P7: serialize current input history once (sufficient implementation brief)

Status: ready for lead allocation to implementer0; no remaining design blocker.
Base is reviewed `474872b602afa0813e6a17a951646b5cf5a91a06`. The user requests a
profile-driven reduction of repeated history serialization and the affected
200-send rerun. The successful unprivileged overlay profile in
`/tmp/pi-node-sample-ybjldlex/findings.md` supersedes P6's capture limitation.
Its batch sampled about 424 ms directly in observePersisted and 258 ms in
makeInput, with serialization prominent; parsing, SDK cloning and GC also cost
CPU. This supports the narrow change below, not a claim that it explains the
whole latency gap or will meet the targets. The reported 7,290 synthetic matches
are representation evidence only, not production proof or performance acceptance.

### Boundary and exact comparison

I0 owns `pi-runtime/src/session.mjs` and focused additions in
`pi-runtime/src/input-delivery.test.mjs`. A short factual explanation beside native
input persistence in `docs/pi-runtime.md` may accompany them; lead owns its final
writing pass. Existing session, lineage and persistence tests are check inputs,
not an invitation to refactor those components. No Go, browser, SDK, fixture,
benchmark, protocol, capability or schema change is needed. Lead allocates the
source/index window and accepts the completed package.

Keep makeInput's admission-time `linearEntries`, prefix count, complete
`JSON.stringify(prefix)`, selected leaf and original input object unchanged.
Those frozen bytes prove an earlier observation; they cannot be reused as the
post-consumption history. In observePersisted, after its existing await and live
pending-owner gate, validate current `linearEntries` and serialize that current
array exactly once into a function-local string. Reuse it for both comparisons:

- Reject a current entry count smaller than the captured prefix count. For equal
  counts, require exact equality to the complete captured prefix JSON.
- For a longer current array, require it to start with the captured JSON without
  its final array-closing `]`, and require the next code unit at that exact saved
  offset to be `,`. This is the boundary after the last captured element, not a
  search for a delimiter in message text. Production prefixes are nonempty because
  the unchanged `linearEntries` refuses empty selections; retain that refusal.
- After the existing fresh `SessionManager.open(file)` and native ID/cwd checks,
  require `JSON.stringify(linearEntries(persisted))` to equal the same complete
  current string. Disk data must still be freshly loaded and independently
  serialized; matching the prefix alone is insufficient.

Use the native JSON serialization exactly as today: no replacer, spacing,
canonical key sorting, parsing back to objects, per-entry hash, truncation or
display projection. Preserve object-key and array order, omitted optional
undefined properties, native number/string escaping and complete lengths. The
boundary offset is a JavaScript string/code-unit length, not UTF-8 byte length;
Unicode or escaped delimiters must not move it. The existing input byte bound is
unchanged. Equality is of the same JSON representations, not raw JSONL file bytes
or a new semantic-object comparator. For the SDK's JSON history records,
serializing the first N elements yields exactly that portion of the whole array
at the same indices; the explicit count and boundary checks preserve the old
slice comparison without serializing those objects again.

There is no await or SDK effect between current capture and the synchronous
independent reopen/comparison/sync in this owning path. Keep that property: the
string is local to this one observation and is never cached on the session,
manager, pending input or another request. A later invocation computes a fresh
current representation. Do not reuse it for verifyHistory, another accepted
input, callback origin, snapshot or sibling. This removes one repeated near-full
prefix serialization per successful observation; makeInput's earlier capture and
the independent disk serialization remain required. It does not remove their
linear cost or promise a measured saving.

### Proof, compatibility and recovery

Keep complete linear validation on both live and reopened histories, including
unique IDs, exact parents, selected leaf/branch and prohibited edits. Keep the
exact caller-owned consumed message object, one observed event/one matching entry,
literal effective text, and ancestry through allowed assistant/tool/system,
append-only compaction and already witnessed users. Foreign users, reordered or
changed prefixes and missing/ambiguous evidence remain Unknown and held. A failed
comparison or serialization must never produce Accepted; retain owning failure
handling and do not introduce a retry or fallback to weaker evidence.

Keep file existence/type/owned-directory checks, independent native ID/cwd, the
observed file identity and `syncHistory` file/directory barrier before resolving
Accepted. The original witness fields, witnessed-users update, result resolution,
commit handshake, receipt durability, callback gates, late holds and no-replay
behavior remain unchanged. Original Lookup still reopens and independently
verifies the original entry/ancestry/witness against current history. Neither
production nor fixture proof is removed or deferred.

Both legacy send and queued steer/followUp use these same private WorkerSession
methods and need coverage. Retained workers keep their frozen implementation;
new workers use the optimization with identical protocol and persisted records.
No capability gate, migration or mixed-generation handshake is added. Existing
upgrade, settings, authority, preflight, EX/SH and recovery rules remain intact;
no worker is restarted or input resent to apply this change. Recovery from a
failure remains the original Unknown/hold and Lookup-only contract. Selecting a
candidate or a later repair follows the existing forward package procedure.

### Meaningful checks and delivery gate

Quick checks in the pinned repository environment must exercise the production
makeInput/observePersisted path, not only a copied comparator. Add a compact
table using the old two-comparison expression as a test oracle for supported
records: equal/extended/shortened history; changed or reordered prefix; changed
object insertion order; optional undefined; Unicode, supplementary characters,
escaped quotes/backslashes/control text and delimiter-like contents. Preserve
the existing empty-history rejection. Include a fresh disk copy which differs
only after the captured prefix, proving the full current-versus-disk comparison
still refuses, plus live-prefix mutation after capture. Every refusal must avoid
an Accepted witness and the successful sync/commit path.

Use the existing real pinned SDK fixtures to prove accepted legacy/queued input,
one native user append and exact witness, append-only compaction, intervening
witnessed users, foreign-user refusal, retained reload/original verification and
sync failure with Unknown/hold/no second input. Existing cases already cover much
of this: run focused `input-delivery.test.mjs`, the relevant persisted-witness and
sync-failure cases in `session.test.mjs`, and unchanged lineage/persistence cases.
Add only missing path-level comparison regressions. Run Node syntax checks and
the declared quick worker tests with the existing pinned `PI_PROBE_PACKAGE`;
do not fetch/build another SDK or add a timing threshold/microbenchmark. Report
exact commands, base/head, files, outcomes and any uncovered supported case.

After the focused commit, quick checks and affected independent review, lead
owns one unchanged `TestPiMessageDeliveryNativePerformance` 10,000-history /
team_activity cell: 20 warm plus 200 measured, with the same batch/background
question workload, endpoint clocks, checkpoint observer and complete final audit.
Use the built exact candidate and the existing fixture; no overlay/profiler or
new telemetry is part of acceptance. Retain HTTP p95 <=250 ms and identified
post-sync acceptance-upper p95 <=1 s, all 200 Sent/40 per member, exact independent
witness/settings/input/ref checks, one enqueue/checked/native user append each,
genuine question progress during foreground and existing fairness assertions.
Report final `auditCompleted:true`/`partial:false`, errors/holds, observer overhead
and complete child/effect settlement even on a latency failure. Preserve the
4748 failed evidence and do not infer causal per-stage savings from counts or
different execution order. A passing smaller representation/proof check does not
establish p95. If this cell still fails, report that result before any further
optimization or larger matrix; no automatic additional run is released here.

## D0: prepare Aitherdev deployment through configuration and workspace pins

Status: sufficient source briefs, with disjoint D0-W ready for I0 and D0-C for I1
after lead allocation. Preparation only: no activation, dry activation, reservation,
merge, reboot, native session operation or lifecycle action is authorized. The user
accepted the current improvement and deferred further tuning. Freeze runtime
`75c810a2eb0f8631dd4450e9dc3947bd491f501d` and its codex-web input
`db79231a4e5513bf439493efab75378bc7d84c04`; neither package reopens application work.

The last 20-warm/200-measured cell remains failed and partial: all measured inputs
were Sent with exact independent per-batch witnesses, but the final Idle audit
refused unresolved work. Final append/health/memory audits did not complete;
latency/fairness assertions were not executed. Retained sample p95 values are
296.722 ms HTTP and 3064.623 ms post-sync checkpoint upper. The admitted question
was still pending, with no Accepted/fairness proof. User acceptance of preparation
does not convert these limits into a performance pass or complete native audit.

### Inputs and present installation

The source-only pass read the installed `workspace-host coordination guide`,
workspace deployment/Git/lifecycle procedures, configuration AGENTS and its current
`docs/operations/pi-runtime-aitherdev.md`. The latter is the reusable site guide;
an older configuration revision's workspace-coordination page is obsolete and its
retention language must not override the installed guide. No new deployment guide
or per-release report belongs in the configuration repository.

- Own configuration checkout is at `worktrees/2026-11-23-pi-message-delivery/vpsfree-cz-configuration`,
  base `11d6d55924d531d6311dc5a98283d980c9818bb0`. Its creation succeeded despite
  post-checkout hook exit 78; lead reconciled registration. I1 repairs the declared
  development/hook environment, without recreating the worktree or bypassing hooks.
- Own workspace checkout is at `worktrees/2026-11-23-pi-message-delivery/workspace`,
  base `68c9949d22bd486630974d11307bbc11e517d8ec`; its extra baseline commits are
  tracking-only per lead. Shared workspace master remains unchanged.
- Both locks currently select runtime `0abe5fe48955b1bcdc8cc368fcb27e11e0676f70`.
  Configuration channel `dev-workspace`, role `devWorkspace`, maps to flake input
  `devWorkspace`; Aitherdev lists that channel in its machine module. Workspace
  selects it through the direct nested URL
  `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url`.
- Preserve extension `bf12ac71a8a00b1581eed5352f99c1b2daaeff5b`, NAR hash
  `sha256-hlCQCMgmNe8qa1fbujQiWduylaOVla9rz0jtOy22LV8=`, existing follows edges,
  site models/providers, team/catalog, coordination/claim policy, KB extension,
  cluster providers and all sibling inputs. No top-level runtime input or extension
  lock edit is needed. The runtime's transitive codex-web change is intentional.
- Selected user profile is
  `/nix/store/60kkim4kzpy1cp2qvbbyfyd4n5nvy3jf-dev-workspace-0.2.0`, with managed
  team digest `7659519e2fbe326ba88f3f4e4b07169f291b61a907be06e5b9e374d27fced37e`
  and the Aitherdev profile target/legacy bridge. Generic app candidate
  `/nix/store/2vk8nlip55qvr99qis1fhac60sc76psf-dev-workspace-0.2.0` has
  `agent_teams.managed:false` and `profileTarget:null`: it is runtime verification
  evidence, not the site deployment package. Build the composed workspace output.
- `/run/current-system` and `/nix/var/nix/profiles/system` both resolve to
  `/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
  Installed confctl metadata records configuration `109d789f0a4ee875f8bd27a0b72ea76c38ee234a`,
  runtime `f3bd843f9858b87cef66d0949706f8af16ba9b13`, effective nixpkgs `94c3211b...`,
  home-manager `c47b2cc6...` and llm-agents `91ff550f...`. Installed helper is
  `/nix/store/xhc71rg58zl44927y9j43s2l23f1r606-workspace-pi-host/bin/workspace-pi-host`;
  system Codex is `/nix/store/naycl3an1c85vhzabscy8qdbr7m1am8c-codex-package-0.170.0/bin/codex`.

### D0-W: composed workspace pin, I0

Own only workspace `flake.nix` and generated `flake.lock`. Change the existing
nested runtime URL to exact 75c810, then generate the lock with
`nix flake update vpsfree-dev-workspace/dev-workspace` in that checkout. Compare
semantic input paths and complete locked identities, not incidental node names.
Keep extension revision/hash and all unrelated inputs/follows unchanged. Confirm
the new nested runtime selects exact db792 codex-web, the existing Pi SDK and
existing native Codex selection. No catalog, policy, model, provider, skill or
application changes. This source work is independent of the configuration hook
repair and final system provenance comparison.

Deliver a focused normal commit, clean owned paths, final base/head and semantic
lock diff, declared formatting/hooks and small existing deployment-contract check.
The composed checks/build below follow lead sequencing; no extra native campaign
or performance investigation belongs to this package. Cross-lock comparison waits
for D0-C without blocking D0-W source completion. Lead owns writing and review.

### D0-C: configuration channel pin and host-impact proof, I1

Own only the generated configuration lock changes produced in the declared shell
by `confctl inputs channel set --commit dev-workspace devWorkspace 75c810a2eb0f8631dd4450e9dc3947bd491f501d`.
Keep the generated changelog/commit text and hooks. Repair missing hook dependencies
through the repository's declared environment, with no source lock/dependency
changes merely to work around that environment. Do not hand-edit the channel lock,
change machine channels, bump nixpkgs/llm-agents/home-manager or add the application
to system packages. Preserve the current channel mapping and review expected
transitive runtime/codex-web changes separately from unrelated lock churn.

The runtime host module, host paths, Pi host Nix package and both host executables,
and Codex wrapper source are identical between installed runtime f3bd843 and
target 75c810. No feature-required host behavior change is demonstrated. The fresh
configuration baseline nevertheless contains other newer root locks, and root
names/revisions do not equal the recorded effective machine inputs. Therefore
evaluate the exact Aitherdev role/input mapping and relevant helper, template,
sudo/drop-in and Codex package outputs for the final candidate versus the installed
system. Record full effective hashes/revisions and store paths. A changed toplevel
path due only to confctl revision metadata is not a required host upgrade; an
incidental broader system update is not authorized by this runtime pin.

If existing installed host artifacts are compatible/equivalent, prepare profile-only
activation and leave the system selected. If output comparison reveals a real host
prerequisite, report its exact delta for lead scope decision; do not silently add
host changes or execute the generic guide's system switch. This remaining artifact
check is a deployment-path gate, not an unresolved contract blocking the pin commit.

### Combined preparation checks and held execution

Once both locks are final, run the existing
`bin/check-dev-workspace-deployment --workspace-root WORKSPACE_CHECKOUT --configuration-root CONFIGURATION_CHECKOUT`.
It proves matching exact generic runtime identities and the site hostname/alias
contract. Also compare the complete input graph and prepared package metadata:
the checker alone does not prove preserved extensions, native packages or host
artifact identity. Record exact committed sources before builds; confctl embeds
the configuration revision. Source/review evidence for immutable 75c810/db792 is
reused within its tested scope, with the failed partial performance result retained.

After normal commits/quick checks and affected independent review, lead owns the
bounded build batch and watcher allocation. Build the composed workspace default
with `nix build --no-link --print-out-paths .#default`; run its existing
`pi-runtime-composition`, `agent-team-policy`, `cluster-provider-composition`,
`tracking-source` and `deployment-contract` checks. These prove the actual site
package, not generic2vk8. Reuse unchanged broader source-check evidence rather
than repeat the performance cell. Use exact-machine confctl evaluation/build only
as needed to settle the prepared system artifacts, with no activation; a kernel
build unexpectedly required by unrelated baseline churn returns to lead diagnosis.
Keep build paths/derivations, input graphs, selected-profile predecessor and the
system/profile impact decision in existing session evidence, outside config Git.

Any later activation requires a separate user instruction and a fresh, exact
schema-2 machine claim for registered repository `vpsfree-cz-configuration`,
selector `cz.vpsfree/machines/aitherdev`, adapter `confctl`, with no repository
claim bundled. Verify its typed mapping before the intended batch. Preserve
`profileTarget` and the `machine:vpsfree:aitherdev` compatibility bridge. Neither
this brief nor a successful build acquires that claim or permits a dry activation.

Held command plan: if a real host change is separately approved, normal
`confctl deploy cz.vpsfree/machines/aitherdev dry-activate` and no-reboot `switch`
of the exact prepared generation precede the profile. Retain confctl rollback
and verify both live-system and system-profile identities. Otherwise skip both
system actions. In either authorized path, ordinary `workspace-host switch --source
WORKSPACE_CHECKOUT` selects the composed profile under `DEV_WORKSPACE_CLAIM_ID`
and this session's exact slug/workspace environment. Do not use the generic app
artifact, private activation helpers, forced compatibility or an invented preflight.

Normal switch preflights retain original lifecycle/creation/cluster/authority
records, runtime bindings, claim readers, machine identity, native invocation and
policy checks. Do not assume same Codex binary means a live cutover is permitted;
the actual launch policy and helper schema also govern. A refusal is a blocker for
later activation, not permission to alter records or stop sessions. No maintenance
enablement, worker upgrade, daemon reconciliation or native effect is implied.
Retained Pi supervisors/workers keep frozen packages and capabilities; a new portal
does not install new checked/scalar behavior into those workers. Legacy reads/send
and original receipt recovery remain supported, absent checked capability remains
unavailable, and any later ready-session upgrade needs its own authorization.

Post-activation verification, if later authorized, must cover the composed package,
portal/router/coordinator health, exact selected native/helper provenance and
retained Codex/Pi identities/settings/receipts without resending an input. Preserve
Unknowns and queued work. Interrupted selection resumes the original forward
target through the ordinary switch/recovery path; never roll back by guessing,
clear pending state or recreate a request. Machine release follows the installed
guide only after settled verified effects and integrated deployed feature lineage;
integration requires separate approval. Preparation ends with reviewable pins,
artifacts, limits and this held command plan, leaving every session open.

## D3-R: lifecycle use of an already attached Pi runtime

Status: sufficient narrow source brief for lead release to I0. This corrects
ordinary archive interruption and retirement; it does not change archive policy
or authorize an operation. Operational recovery of an older installed package is
separate below. No peer identifiers or private runtime evidence belong here.

The standalone `pi-runtime lifecycle` consumer constructs a new workflow
composition. Its attachment map cannot see the serving portal's attachment.
Both `Manager.InterruptLifecycle` and `Manager.Retire` currently call that
composition's ensure callback unconditionally. The supervisor correctly permits
only one host attachment, so the second connection refuses even when the existing
portal attachment could serve every required invalidation ACK. The web fixture's
fake interruption path currently ignores ensure, hiding this consumer mismatch.

### Owning correction and retained proof

Use one private lifecycle readiness helper at the existing ensure sites in
`portal/internal/piruntime/lifecycle_capture.go` and `lifecycle.go`. Preserve the
existing callback signature and nil-callback refusal. After the existing exact
current-runtime, member and receipt admission, identify a loaded captured member
and call the existing `Manager.ObserveWorkflow` with its exact execution handle.
A successful, Loaded observation proves the existing global workflow attachment
is ready: the existing transport validates runtime/handle, attachment ID,
sequence, settings and native policy proof, while the supervisor checks unchanged
attachment/sequence and zero mutation-pending count before returning. Do not
require Idle merely to establish attachment availability: a known accepted busy
input must still reach the existing explicit abort path. This observation is
ephemeral availability evidence, never an effect permit or drain proof.

On that positive observation, omit only the attempt to establish a second
attachment. Do not retain or cache the observation. A missing attachment or
otherwise unavailable observation may take the original ensure callback once;
it must succeed normally, including initial ACK. No loaded member likewise uses
the original ensure behavior. Cancellation and scope/held/integrity failures
remain errors, never positive readiness. An unavailable probe is not permission
to replace an attachment: the ordinary exclusive attach may still refuse. There
is no retry of abort, unload, native input or any possibly executed mutation.

Keep all existing subsequent checks. Interrupt retains CheckLifecycle, exact
snapshots, Held refusal and the accepted-owner abort decision. Retire retains
all-member snapshot and fresh workflow idle/settings/policy checks before the
first unload, each unload's live shared-worker fence, exact unchanged mappings,
settled receipts, original host execution identity, Stop receipt and native drain.
Abort/unload still acquire their own fresh global invalidation ACK and mutation
permit. Losing/replacing an attachment after the probe must refuse through those
checks, not reuse the probe as authorization. Callback Unknown/held facts remain
decisive. Do not alter supervisor attachment exclusivity, workflow observation,
general callback composition, policy admission, or native worker protocols.

### Files, checks and compatibility

I0 owns the two runtime implementation files, focused existing
`portal/internal/piruntime/lifecycle_test.go` coverage, and
`portal/internal/web/pi_lifecycle_test.go` only as needed to cover the actual
standalone lifecycle consumer and borrowed parent lock. Keep a short factual
contract paragraph in existing `docs/pi-runtime.md`; update the archive recovery
guide only if an operational instruction changes. Lead owns final writing and
allocation. No new interface, capability, wire message, receipt or journal schema,
native client, polling loop or framework is needed.

The primary native-free regression uses real Manager/control Unix transport and
the existing supervisor/policy worker fixtures. Establish a portal-like workflow
attachment and initial ACK, then invoke real InterruptLifecycle and Retire from
an independent lifecycle composition. Assert no second attachment, original
attachment identity retained, ACK-gated busy abort, subsequent quiescent unload
and positive stop/drain, with no Load/Send/replay. Contrast an isolated consumer
where the original ensure establishes the attachment normally. Cover canceled,
unavailable/unready, changed-generation and malformed proof cases, plus attachment
loss between probe and mutation, held/Unknown receipt, and busy/pending retirement
refusals. Reuse existing lower-level ACK replacement/race coverage where exact;
do not duplicate a large matrix. The public CLI/web consumer must no longer be
represented solely by a fake that ignores its ensure callback.

Quick checks are the affected lifecycle/workflow tests and exact standalone
lifecycle/borrowed-lock tests in the declared environment, followed by normal
hooks. Commit and affected independent review precede the existing bounded
creation/lifecycle integration lane selected by lead. No performance cell or new
native campaign is implied. A retained supervisor that supports the existing
workflow observation/ACK contract needs no restart or upgrade; an older worker
without a successful observation retains ordinary ensure and refusal behavior.
Rollback changes no persisted format. Original journals remain retryable through
their saved ordinary lifecycle operation.

### Recovery before profile activation

The installed package's lifecycle gate still blocks profile switching while an
archive is unfinished; this source fix does not waive it. An orderly portal
service cutover can release its attachment: Close cancels and joins attachment
goroutines; socket close clears supervisor attachment/readiness and advances its
sequence without directly stopping/unloading a session or rewriting authority.
However, an already forwarded callback can become Unknown/held on disconnect.
Therefore service stop is a qualified deployment operation, not proof that every
native effect is idle and not a durable fix for future archives.

Lead may separately choose a held-machine deployment service boundary, confirm
orderly portal exit and attachment release, then use the installed ordinary
archive command to resume the explicitly authorized original operation. Every
receipt/quiescence/hold/drain check stays active; a new refusal stops recovery.
Restart the selected portal on failure rather than edit evidence or bypass the
package gate. On successful ordinary recovery, proceed with the reviewed new
profile through normal activation. This brief authorizes no service stop,
lifecycle command, private helper, forced activation or live RPC by the architect
or implementer. The source fix and its actual consumer regression are required
before calling the underlying defect fixed.

### D0/D3 final selection amendment

The reviewed D3 fix at runtime `3961d7285abc6c996206bc50a7cd68977086312b`
supersedes D0's initial 75c810 preparation target. Lead reports passing quick
checks and independent review with no findings. Final workspace
`dbb6c4bcc711ab3718646e266a4a6379003b42df` and configuration
`844ffe5ed7b3bd541872a57112d7cabff81ab778` each contain one pin update to 3961;
final mechanical review also found no issues. Earlier revisions and performance
results above remain historical evidence, not the final deployment selection.

The existing source-composition, extension/input preservation, policy, retained
worker, authority and recovery contracts remain unchanged. Deployment remains
profile-only with the compatible installed host; no system activation is added.
The user has authorized Aitherdev deployment and explicitly confirmed resuming
the existing archive. Private target details remain outside this document.
Neither authorization grants repository integration or additional lifecycle work.

At this checkpoint the composed build is running. Machine ownership, any ordinary
portal service cutover, archive recovery and profile activation remain pending
lead execution and verification. Review completion does not establish deployment
or archive completion; all existing activation gates and recovery proofs apply.

## P8: release committed input prefixes and retain final-audit failure evidence

Status: sufficient independent briefs for lead allocation to I0 (P8-M) and I1
(P8-F). Both start from merged runtime
`3961d7285abc6c996206bc50a7cd68977086312b`; use new development commits only.
The user requests further performance tuning. No live deployment, claim,
integration or session lifecycle operation belongs to these packages.

### P8-M: release the dead serialized prefix at queued-input commit

I0 owns `pi-runtime/src/session.mjs` and
`pi-runtime/src/input-delivery.test.mjs`, with an optional short contract sentence
beside existing input persistence documentation in `docs/pi-runtime.md`. Lead
owns writing/review. No SDK, Go, protocol, metadata, fixture or package-input edit
is needed. There is no remaining source-design dependency on P8-F.

The saved profile in `/tmp/pi-node-sample-ybjldlex/findings.md` used runtime
474872b6 and sampled about 277 ms of GC in its four-input batch. It predates P7
and cannot establish current GC time, retained heap size or latency savings.
Current source independently proves a narrower retention mechanism: makeInput
stores the complete admitted history as `prefixJSON`; commitInput retains the
same input object in `acceptedInputs`, capped at 20 per member. Across five
members that can retain 100 complete serialized prefixes after their proof duty
ends. P7 already removes repeated current-prefix serialization and remains intact.
This change makes those completed strings eligible for collection; it does not
reduce the required serialization count or promise an RSS/latency improvement.

Clear only the private `input.prefixJSON` reference in commitInput's successful
branch, after its existing delivery/witness/finished admission and committed
transition, before returning the unchanged `{committed: true}`. Assigning
`undefined` is sufficient; do not replace the input object or create a compact
parallel receipt type. Preserve every other field, map capacity/order, active
input identity and workflow notification. Do not change legacy send or release
prefixes in makeInput, observePersisted, hold, abort, Unknown, refusal or failure
paths. An invalid commit must leave the original input and prefix untouched.

The ordering is already owned: observePersisted validates the frozen prefix,
exact consumed object/text and allowed ancestry, independently reopens/compares
disk history and syncs it before resolving Accepted. Go finishInput validates
that result, durably saves the original Accepted receipt and passes its receipt
checkpoint before requesting input_commit_v1. Failures before that request retain
the existing hold behavior and do not reach this cleanup. A lost commit reply or
later metadata failure can still hold the worker; it does not undo Accepted or
authorize replay, and retaining obsolete prefix bytes cannot resolve that error.

All production reads of prefixJSON are inside observePersisted after its
`finished`/owning-input gate. Its synchronous proof section has no await after
that gate. Commit requires finished+witness, so a later scheduled observation
returns before using the cleared field. HostBridge uses operationID, witness and
committed state, with fresh inspectOrigin disk proof; protocol lookup preserves
the same object through inputs, acceptedInputs and activeInput. Original
verifyHistory independently reopens disk and checks the supplied original witness
and ancestry; it does not use prefixJSON. Retain all those paths, native input
objects, settings, witnessedUsers and receipt identities unchanged. This is
neither a history cache nor permission to weaken callback/attachment ACK checks.

Quick tests must use the actual WorkerSession commit path. Show a substantial
prefix survives Pending and Accepted-before-commit, then is absent from the same
object retained by acceptedInputs/activeInput after commit. Multiple committed
entries must retain zero prefix strings while a separate pending input keeps its
original bytes; preserve the existing 20-entry limit. This is a deterministic
reachability assertion, not a forced-GC, heap-size or elapsed-time test. Keep P7's
prefix-mutation and fresh-disk mismatch oracles, and assert aborted/Unknown and
unwitnessed commit refusals retain their prefix. After successful commit, prove
unchanged exact witness and independent verifyHistory, plus a real HostBridge
origin verification from retained accepted provenance. Preserve native append
counts and no replay. Use the existing pinned SDK and relevant input-delivery,
session persistence/lineage and callback coverage; add only missing checks in the
owned test file. Run declared syntax/quick checks and normal hooks, then commit.

There is no wire, persisted-format or capability change. Retained workers keep
their implementation; only newly launched workers from a later selected package
release these private strings. No worker restart or deployment is authorized
here. Recovery remains original receipt/Lookup-only and held-state behavior.

### P8-F: preserve the existing final-audit failure boundary

I1 owns the two existing tagged V files,
`portal/internal/piruntime/pi_message_delivery_integration_test.go` and
`pi_message_delivery_fixture_test.go`, plus a narrow test-helper extraction in
`portal/internal/piruntime/supervisor_test.go`, where waitIdle owns the Load/error
boundary. Preserve waitIdle's signature as a fatal wrapper around an unexported
error-returning waitIdleResult helper containing the single existing Load/wait
loop. Its test-only loader argument may receive `m.Load` from ordinary callers
and a deterministic one-call loader in the child-fatal regression; this adds no
production hook. Return that call's last state, attempt count and original error; the tagged
fixture writes its synced failure evidence before the same fatal. No additional
RPC, duplicated polling loop or diagnostic callback interface is needed.
Lead confirmed independent capacity and owns release; the current commit/index
order is I1 first, then I0 after its separate read-only fact package. Production P8-M can
proceed independently; P8-F must be checked/reviewed before the next 200 cell.

I1's bounded diagnosis found no proven fixture or product correction in the old
75c810 failure. All 220 warm/measured inputs reached Sent with independent batch
proof, but the final audit failed immediately with ErrHeld. Its exact member,
Load return state and inner failure boundary were not retained. A pending question
or observed Held flag alone can produce a busy/held state with nil error, so
neither establishes this fatal's cause. The accepted question stayed pending in
the last successful observation; neither native enqueue nor starvation is proved.
The affected fixture/Load paths are unchanged at 3961. Keep the failed partial
result and missing final audit/fairness proof explicit.

Add synced begin/end rows around the existing final-audit calls with exact
member/execution handle and stage. At waitIdle's existing fatal, record its
iteration, context/error class and the already returned Load state before the
same fatal. callRaw already decodes a response before returning its held error;
preserving that value can distinguish a reached supervisor response from an
upstream failure. Do not claim it identifies a more specific cause than it does.
Use existing JSONL/central diagnostic synchronization, bounded structured fields
and existing completion-evidence child-fatal tests. Verify evidence survives the
fatal and run tagged compile. No extra native/authority call, new observer,
production hook, poll, retry, post-foreground question drain or changed deadline.
Do not move audits, hide errors or convert later question completion into a
foreground fairness pass.

### Combined acceptance

Normal committed quick checks and affected independent review precede the
lead-owned exact candidate build and one existing 10k/team_activity cell with
20 warm plus 200 measured inputs. Keep all endpoint clocks, checkpoint observer,
background question workload, per-input independent witness/ref/settings proofs,
final Idle/history/health audits and fairness assertions. No profile/overlay,
new timing framework or larger matrix is part of this brief. Preserve HTTP p95
<=250 ms and post-sync acceptance-upper p95 <=1 s as targets, not predictions.
Report final auditCompleted/partial/passing status, all failures/holds, question
progress during foreground, observer overhead and complete child settlement.
If the same audit fails, use P8-F's preserved boundary to select the next bounded
correction; do not repeat an unmodified run or weaken the audit. No causal speedup
claim follows from comparing different-order/background runs alone.

## P9: returning-tab transcript delay — bounded diagnostic brief

Status: source facts sufficient to define one diagnostic; no production
optimization is justified yet. The user reports Pi transcript refresh taking
5–10 seconds after returning to a tab, slower than Codex. Lead has asked which
session/tab is affected. I0 completed the immediate source pass; the architect
has not repeated its inventory or run a browser, native worker or live request.
P8 implementation and review proceed independently.

### Settled source facts and missing evidence

At runtime 3961/db792, both backends use the shared conversation sync controller.
Visibility restoration from suspended state connects SSE and schedules a page
read immediately. Focus recovery has a 250 ms debounce and may retain a healthy
stream; there is no demonstrated fixed 5–10 second resume delay. SSE onopen can
cancel an earlier read and start another, but the required fresh-read/event-gap
semantics must be understood before changing that behavior.

Pi's fresh page performs scoped admission and request-local BindRead, followed
by transcript snapshot/proof work. The Node snapshot bounds displayed entries
but still walks and serializes/hashes the whole branch; Go projects original
Accepted receipt witnesses under its existing conversation lock. These are
history-dependent operations, not measured causes of the reported delay.
Codex uses its bounded turns/items page and AppServer notifications. Current Pi
activity-capable watches use attachment listeners; only the older unsupported
path uses snapshot polling. Determine the actual frozen worker contract and
connection outcome before attributing any delay to legacy polling. Shared DOM
rendering and retained-row work can also consume browser time.

There is no actual visibility-to-request, request/TTFB/body, parse/apply or render
timing for the affected tab. Neither an HTTP-only read nor a synthetic dispatched
visibility event reproduces real browser background scheduling. No browser
connector or access to the user's existing browser performance stream is
available here. Shell/Playwright access can create another browser, not observe
that existing tab. This is the concrete tooling/evidence gap; do not request
privileged browser settings or open a debugging service to bridge it.

### Preferred single observation

After lead identifies the target and selects an available capture route, capture
one ordinary hide/return cycle of an already-loaded affected Pi tab using the
browser's existing Performance and Network tools. Preserve its normal model,
session, tab state, network, cache and service-worker behavior. Start recording
before hiding, return once, and stop after the first completed fresh transcript
render or a bounded 20-second post-return observation if it remains stale. Do
not send an input, reload the session, change settings, clear caches or repeatedly
toggle visibility. User-provided capture is optional evidence, not an assumption
that the assistant can control that tab.

Retain only the necessary timing facts: actual visibility/focus/pageshow event,
transcript request initiation/queueing, response headers and body completion,
canceled versus completed requests, SSE connection/open/disconnect, JSON/apply
work and the subsequent transcript render/paint. Include overlapping detail,
activity and workflow requests with their statuses so a later side request is
not mistaken for transcript completion. Use existing DevTools function samples
and task/paint boundaries where available; label sampling/bounds explicitly if
an exact render endpoint is unavailable. Browser capture overhead is diagnostic
and does not establish a production percentile.

The report should separate: event-to-request delay; request-to-first-byte and
body time; body-to-parse/apply/render time. A long HTTP interval groups server
queueing, authority, native work and transport until narrower evidence exists.
Only if it dominates should lead inspect existing read-only server request logs
for the same normalized endpoint/time/status, and only recorded durations can
be used. Do not infer lock/native CPU durations from that total or create new
server hooks in this package. Multiple canceled reads establish their occurrence,
not how much unreturned server work executed.

### Disposable reproduction and stopping boundary

If the actual browser capture is unavailable, lead may separately release one
ordinary Playwright reproduction against an existing qualified disposable portal
and Pi supervisor fixture. It must use the same packaged browser assets/protocol,
real page/SSE endpoints, recorded worker capability and comparable history size.
Use real tab foreground/background transitions, not only an injected event. Keep
normal admission, receipts and render behavior, with standard browser tracing
and request timing. No SDK/worker override, cache, injected delay, extra send,
general tracing framework or production source edit is part of this diagnostic.
Fixture preparation must be explicit if no such browser-ready fixture exists;
the current shell capability alone does not prove that prerequisite.

An isolated browser can measure that fixture's scheduling/request/render split;
it cannot establish the user's tab's background throttling, prior DOM state,
connection history or original 5–10 second cause. Stop after one bounded cycle,
join the browser and any explicitly owned fixture children, and report the
observed split or non-reproduction. Keep target sensitivity and credentials out
of tracked evidence; use compact nonsecret facts or verified ignored/untracked
artifacts as the session-read rules require.

No application files, source/commit window, live deployment, claim or lifecycle
action is released by P9-D. Lead owns target/capture selection and any execution
package. The next design decision must follow the measured dominant interval;
do not preselect hash removal, cache reuse, timer changes or dropping an SSE
refresh. Any later correction must preserve common backend UX, exact freshness
and identity, original receipt/witness projection and attachment ACK authority.

## P10: one current shared-worker CPU profile

Status: sufficient source-free diagnostic preparation brief for lead release to
I0, followed by one fresh verification utility run. No repository application
edit or commit is needed. The existing unprivileged inspector route is qualified;
this is not a repeat of P6 feasibility work. P9 remains parked with lead owning
the user's target/capture decision. Question eligibility diagnosis is independent
and must not expand this profiling package.

The 3054 actual200 finished all final audits, with all 220 warm/measured inputs
Sent and exact independent evidence. Its final result remains failed:
auditCompleted true, partial false, passing false; p95 HTTP 286.087 ms,
post-sync checkpoint upper 2979.109 ms and public Sent 3389.812 ms. The question
never became respondable in the retained successful observations. There is no
demonstrated causal speedup or reproduced final Held failure. Do not rerun that
cell unchanged. The bounded new question is which CPU categories dominate the
current shared Node's four-input acceptance interval after P7/P8, versus idle.

### Exact inputs and preparation ownership

Use clean runtime source `3054dda39eb1fd67347122413bf72e5d82f68ba4` in the
registered development worktree, codex-web
`db79231a4e5513bf439493efab75378bc7d84c04`, and canonical candidate
`/nix/store/pxw8ngf2aknagbg2s2a1wc3w50jdaa82-dev-workspace-0.2.0`.
Do not pass its `/tmp/pi-message-delivery-candidate-3054dda3` symlink as the app
root: the fixture deliberately requires a canonical immutable store path.
The candidate manifest selects Node
`/nix/store/gf597zf0ysgbngwb92baxgxjd02px6jh-nodejs-22.23.2/bin/node`, worker
`/nix/store/157f5yaw4azjyp07klcw7vzqf13vq50f-dev-workspace-pi-worker/libexec/pi-runtime/worker.mjs`
and SDK `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`.
Use the existing session `v-fixture/catalog.json`, SHA256
`adb05d10ba504cd3951631f07c450d16a753f75856b41d9c6ad50ecdaaa91aed`;
do not regenerate catalog selections from the live installation.

I0 owns only a fresh mode-0700 `/tmp/pi-node-sample-3054dda3.*` artifact directory.
Reuse `/tmp/pi-node-sample-ybjldlex/{sample.py,sampler.mjs,analyze.py}` as the
starting scripts. The old sample.py hardcodes a removed temporary checkout and
the 4748 candidate, so it cannot be run unchanged. The old begin/finish files
already exist; never reuse that output directory or overwrite its evidence.

Create fixture.go from the exact CURRENT 3054 tagged fixture, not the saved old
overlay. Insert only the same qualified one-line prepend before its existing
generated delivery-worker.mjs write: an ES module import of the fresh directory's
sampler.mjs. JSON/Go-quote the file URL normally. The old overlay differs from
exact 4748 by only that import line; require the current overlay diff to have the
same boundary and retain all current P8 diagnostics. overlay.json maps only the
absolute current `portal/internal/piruntime/pi_message_delivery_fixture_test.go`
to this private copy. Runtime modules still come from canonical pxw8; no SDK or
worker source is patched, no debugger socket is opened, and permissions are
unchanged.

Adapt sample.py's repo/package/catalog/output constants to these exact inputs.
Keep its existing one test-child execution, diagnostic_http initial/quiet marker
triggers and 25 ms passive child CPU counters in that same run. There is no
separate passive experiment. Remove the automatic compilation from the run path:
I0 prepares test.bin explicitly so the utility runs a known hashed binary once.
The runner must wait for its test child and report its exact status even if local
artifact processing fails; unresolved child effects must remain explicit. Do not
add retries, RPCs, new timers, flags, sampling algorithms or a general runner.
Keep sampler.mjs's existing inspector start/stop and nonpersistent watcher;
analyze.py retains the existing checkpoint-based clipping, with only input and
validation adaptations needed for this run.

### Preparation checks and exact held run

I0 performs script syntax checks and the following compile in the declared Nix
environment, with ROOT replaced by the fresh absolute artifact directory and cwd
the exact runtime `portal/` directory:

```sh
go test -mod=readonly -tags=pi_native_fixture -overlay=ROOT/overlay.json \
  -c -o ROOT/test.bin ./internal/piruntime
```

Compilation is not native execution. Record source head/clean status, overlay
diff, script/overlay/binary hashes, canonical candidate manifest and catalog hash.
Compare packaged session.mjs/protocol/persistence inputs to the intended source;
retain the current candidate/SDK provenance, not old fixture hashes. Deliver the
absolute runner command and cwd, exact environment and script receipt to lead.
No new package build, test execution, profile run or commit belongs to I0 prep.

After lead accepts preparation, one fresh watcher resolved through the installed
verification-watcher policy owns the uncertain execution. From the same declared
environment it runs `python3 ROOT/sample.py`; the prepared runner invokes exactly:

```sh
ROOT/test.bin -test.v -test.count=1 -test.timeout=3m \
  '-test.run=^TestPiMessageDeliveryNativeStageDiagnostic$'
```

Set PI_CENTRAL_APP_ROOT to canonical pxw8, PI_PROBE_PACKAGE to SDK9hf,
PI_CENTRAL_CATALOG_FIXTURE to the original canonical catalog file,
PI_MESSAGE_DELIVERY_ARTIFACT_DIR to ROOT/out, TMPDIR=/tmp and GOWORK=off.
Retain the qualified runner's removal of NODE_OPTIONS and unrelated provider/
browser overrides; do not introduce installed credentials or live session state.
Capture complete direct stdout/stderr and exact exit status. Preserve the existing
five-conversation authentic 10k seed, genuine question, six-second initial
observation, one four-concurrent-input batch, ten-second quiet interval and all
original witness/history/Idle/audit checks. No extra Go trace, 200-cell run or
native operation is authorized by this brief.

### Evidence, interpretation and settlement

Bind the single profile to the fixture's exact Node child: parent test PID,
worker PID, process start ticks and expected delivery-worker.mjs command. Preserve
the actual fixture workspace root for final process settlement. The script's
direct-child discovery is observation, not authority to attach to another
process. Inspector runs only inside that disposable child. No profile-error,
missing/ambiguous worker, missing checkpoint or uncovered batch may be silently
treated as a valid profile; preserve and report incomplete diagnostic evidence.

Require all four original sample IDs with exact Accepted witness/ref/settings
and one native user append each, completed final audit and settled fixture work.
Retain question outcomes honestly; eligibility/progress is not forced and four
inputs do not prove sustained fairness. If the test fails, retain its exact
failure and profile coverage limits without rerunning or inventing acceptance.
Use the existing monotonic/wall observations to check profile coverage and clock
drift. Clip analysis from the earliest of the four sample HTTP starts (identified
checkpoint time minus that sample's acceptance upper) through the latest exact
checkpoint upper. Verify all four endpoints lie within the captured profile;
report clock precision/alignment uncertainty rather than a new timestamp system.

Report top sampled SELF CPU categories and source frames for current
serialization, SDK parse, model-context clone, GC and idle. Parent stacks explain
ownership but must not be summed with their children. These samples cover the
shared worker and concurrent question/background work; they do not establish
per-input exclusive CPU, native reply completion, syscall timing or production
p95. Disclose inspector/counter/checkpoint overhead, and do not treat a difference
from the old 4748 profile as an isolated causal improvement.

The utility must join every owned command/cell and test child, account for the
profile stop/file and exact fixture worker/process tree, and report any remainder
as incomplete. Timeout or test exit alone does not prove native settlement. A
remaining process must not be hidden by broad kill/cleanup; lead owns any needed
precisely scoped recovery. Preserve artifacts, leave repository source unchanged,
and stop after this one diagnostic. Lead/architect use its current category result
to choose one subsequent production correction, not another broad inventory.

### P10-E/W: independent validation of the completed profile window

The one diagnostic test passed in 60.34 seconds with all four original Sent/
Accepted proofs and final native-append audits; all owned processes settled.
The runner nevertheless exited 1 with `worker identity changed`, and the strict
analyzer exited 1 before producing categories. Both failures remain authoritative
and their files/assertions must remain unchanged. The rejected identity candidate
was not recorded, so its cause cannot be classified as replacement, changed
command, zombie/exit transition or another field change.

I0's bounded read-only diagnosis establishes a narrower positive basis. The
retained capture (artifact-root suffix imi51nn8) has 2,181 accepted CSV rows for
test parent 2322360, worker PID 2322417, start ticks 212635123 and the exact
fixture delivery-worker.mjs command. The runner writes each row only after the
existing parent and complete identity comparison succeeds. The last accepted
row is 12:46:53.398033716Z; rejection follows it. The saved profile spans
12:46:25.507744–12:46:34.550919Z. All four HTTP starts and checkpoint uppers lie
inside it; their combined window is 12:46:30.905667781–12:46:33.781592810Z.
Thus the rejection is outside the measured window by more than 19 seconds, and
outside the completed profile by more than 18 seconds. This does not recover the
missing rejected tuple or prove its cause. The profile's existing clock samples
show about -0.104 ms wall/monotonic offset drift, with substantially larger
coverage margins on both ends.

Lead accepted one separate P10-W read-only validator/category calculation owned
by I0, bounded to five working minutes. It may write only a new local validation
report/script; it must not edit the raw profile, CSV, JSONL, run/preparation
receipts, original runner or strict analyzer. No new native/profile/test run,
fallback acceptance, assertion removal or marker is authorized.

Before computing categories, require positive checks of the exact artifact hashes
and prepared source/app/SDK/catalog/binary/overlay provenance; the profile's PID
against the recorded worker tuple and accepted identity rows covering the whole
profile/batch; monotonic counter/clock records and profile sample/delta validity;
all four original full-ref/witness checkpoints, Sent results and final append
audits; and each reconstructed HTTP start/checkpoint lying within the saved
profile with disclosed alignment limits. Bind the error-order conclusion to the
actual runner statement order and last accepted row, not a guessed error time
or file mtime. A missing condition must reject window analysis.

Only after those checks may the separate analysis reuse the existing clipped
SELF-time calculation and print compact top categories/owning stacks. Its result
is explicitly `validated profile window; original runner/analyzer failed;
terminal identity-rejection cause unknown`, not a wholly passing capture. Keep
shared-worker/background and profiler-overhead limits. This result may select one
narrow subsequent production proposal; it does not attribute the user's tab delay
or authorize an SDK patch, new parser, cache, worker pool, protocol project or
another profiling experiment. If no conventional correction preserves the
existing proof contracts, close P10 with its dominant cost and exact constraint.

### P10 result and P10-SDK sufficient source package

P10-W independently validated the retained window and left the original failed
runner/analyzer untouched. In its 2875.925 ms four-input interval, sampled SELF
times were: idle 834.815 ms, SDK parseSessionEntryLine 414.907 ms, structuredClone
380.961 ms, observePersisted 277.934 ms, makeInput 231.184 ms, GC 212.907 ms,
linearEntries 52.333 ms and getBranch 46.178 ms. Other frames account for the
remainder. Passive counter brackets put main-thread CPU at 2026.941–2054.290 ms
and run-queue wait at 0.724 ms. These are this instrumented shared-worker window's
measurements, not per-input costs, old/new causal improvements or tab-refresh
attribution. observePersisted SELF is not proof that all its time is serialization.
Fresh parsing under both original verifyHistory and observePersisted remains
required; no parser, cache, history truncation or witness deletion is proposed.

One narrower candidate is demonstrated. Most cloning samples descend through
the pinned SDK's emitContext, called by its createAgentSession transformContext
callback. The callback currently delegates whenever an extension runner exists,
even with no context listeners. emitContext then deep-clones the complete
messages before finding no handlers. The worker's trusted inline extensions
register neither `context` nor `context_with_system`. The Agent transformContext
contract explicitly permits returning the original messages; the SDK's existing
no-runner path already does that. The separate direct emitContext API and all
listener paths must retain their current deep-copy semantics.

Lead has accepted this bounded SDK source/package change as task-required tuning.
Status: sufficient implementation brief for I0, one complete package. Start from
3054 and add one focused development commit; no merge/deployment is authorized.

#### Source and package boundary

I0 owns dev-workspace `flake.nix`, one new
`nix/patches/pi-sdk-context-no-listeners.patch`, one focused
`test/pi_runtime/sdk-context.test.mjs`, and the necessary short factual updates in
`pi-runtime/README.md` and `docs/pi-runtime.md`. Lead owns the final prose pass
before commit. No owning Pi checkout, fork, remote publication or new package
export is needed. No flake.lock, upstream.json, npm lock, catalog, version,
capability, wire, receipt or schema change belongs to this package.

The patch touches only upstream
`packages/coding-agent/src/core/sdk.ts` at createAgentSession's existing
transformContext callback. Read extensionRunnerRef.current per invocation;
return messages if no runner, or if both
`runner.hasHandlers("context")` and
`runner.hasHandlers("context_with_system")` are false. Otherwise call the
unchanged runner.emitContext. Do not cache the handler result, alter runner.js,
skip either event phase, or replace the downstream forced-system-prompt and
hidden-tool projection wrappers. The listener check and dispatch have no
intervening await. Registration changes between requests therefore remain
visible; actual listener execution, mutation isolation, order and error behavior
stay owned by emitContext. Direct callers of emitContext still get its original
deep copy even when it has no listeners.

Select the patched package centrally in mkPiWorker using the upstream package's
normal `.override { source = patchedSource; }`, with patchedSource produced by
ordinary `applyPatches` from the exact existing pi input and that one patch.
Retain the assertion joining pi.rev to upstream.json. The exported package is
made with callPackage and accepts `source`; its internal workspacePackages uses
that source and locked npm dependencies, hydrates the same catalog, runs
`npm run build:offline`, packs all eight workspace packages, then installs those
tarballs through the existing packageSourceOverrides. This rebuilds coherent
unbundled SDK and CLI assets from the TypeScript edit.

Do NOT use top-level overrideAttrs/patches: the final pi derivation's source is
the installer lock and dontBuild is true, so that would not rebuild the owning
TypeScript workspace. Do not edit installed node_modules/dist JS or monkeypatch
the running worker. The upstream input remains
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc` as already declared in upstream.json.
Preserve its existing source NAR, upstream/root locks, model catalog, Node and all
other input selections. The derived patched source and resulting SDK output will
necessarily have new store identities; record those explicitly rather than call
them the unchanged SDK9hf artifact. The existing pi-worker passthru.piPackage is
the exact build/test target; do not add another selector or export.

#### Quick proof and artifact selection

The selected Pi package realization is a necessary prerequisite for its quick
conformance tests, not permission for a full application build or long native
integration test. Lead allocates a fresh verification utility for the uncertain
SDK build/check batch. From the declared repository environment, the exact
selected target is:

```sh
nix build --no-link --print-out-paths .#packages.x86_64-linux.pi-worker.piPackage
```

Use that returned canonical path as PI_PROBE_PACKAGE for the new test and the
existing public-package loader. Never substitute installed/old9hf merely because
both package versions still say 1.5.2. Verify the built SDK guard and retained
direct runner implementation, exact Node/catalog/input closure and source-patch
provenance. Keep a reviewed original-to-patched source diff showing only the
owning guard; ordinary source rebuild/type checking is required. No dependency
install or lock regeneration outside the existing Nix package is needed.

The focused Node regression must exercise actual createAgentSession/agent
transformContext from that built public SDK, not a copied callback. Use existing
offline faux/model/session helpers and finite disposable state. Cover no runner
where the public fixture permits it, and a runner with only unrelated listeners:
the transform boundary returns the same messages identity and does not invoke
emitContext/deep cloning. Direct emitContext on the same supported messages must
still return distinct deep-copied objects. With either context listener type,
including a nested in-place mutation, assert original messages stay unchanged
and expected transformed values arrive. With both, assert existing phase order,
system/tool restoration and error reporting. Add a handler between two requests
and prove the next invocation uses it; no cached no-listener decision is allowed.
Retain actual forced prompt/tool-policy output and unchanged history values.
Use a narrow test spy only to observe the existing method/clone boundary; no new
test harness or production seam is needed.

Run the focused new artifact test plus the existing input-delivery, lineage,
session persistence and tool-policy cases affected by this selected SDK. Keep
exact witness, fresh reopen/sync, no replay, callback origin and policy assertions.
Run syntax/format/hooks and one normal focused commit after lead's factual prose
pass. Independent final review follows all intended source and quick checks; it
must inspect the source-patch application, actual compiled artifact coverage and
the complete input delta. A passing source-string check alone is insufficient.

#### Compatibility, recovery and longer acceptance

This changes only a no-listener transform path whose documented result may be
the original messages. It does not change the direct deep-copy API or any active
extension's mutation semantics. Existing supported message values, event order,
system prompt/tool projections and dynamic registration retain coverage. Unknown
or failed package construction does not select an ambient SDK or update runtime
state. No durable state migration or rollback repair is necessary.

Retained workers keep their frozen SDK/Node/package; new workers from a later
candidate use the rebuilt coherent artifact. Existing host instructions,
authority, positive availability, attachment ACK/permits, receipts and original
Lookup/history proof stay unchanged. There is no current live deployment or
worker restart in this package. Update the README's previous unpatched-source
statement and explain the exact local source patch beside the existing pin, with
its removal condition if a future reviewed upstream revision incorporates it.

After the focused commit/quick proof and affected review, lead may allocate the
exact application candidate build and one existing 20-warm/200-measured
10k/team_activity acceptance cell. Keep final audits, question/fairness checks,
endpoint clocks and observer overhead reporting unchanged. There is no further
profile, larger matrix or unconditional rerun. The sampled clone category is a
candidate cost, not a predicted 381 ms saving or target-pass promise. P9's actual
5–10 second returning-tab symptom remains outside this attribution.

### P10-CI: realize the existing patched source before no-build evaluation

Status: sufficient bounded I0 packaging correction, accepted by lead. Exact
022646d73bde4fbc468ed68835499158e8727b2c fast CI 45403167502 failed at
`nix flake check --no-build --print-build-logs`, before the build step. The exact
workflow invokes no nix-eval-jobs command; that initial hypothesis is superseded.
The full raw log is retained at
`/tmp/2026-11-24-pi-message-delivery-0226-ci-fast-job.log`.

The source override passes an applyPatches derivation to upstream nix/package.nix.
That package imports source/packages/coding-agent/package.json during evaluation
and also reads source-based npm locks. Evaluation therefore requires the patched
source to exist. The CI trace reaches the xs767 patched-source package.json and
fails because its j74 source derivation is not valid in that evaluation context.
Local SDK realization had already made the source readable, so its successful
build did not cover this cold no-build check. This is an evaluation prerequisite,
not a failed TypeScript guard or evidence for changing runtime proof behavior.

I0 owns only `flake.nix` and `.github/workflows/check.yml` for the functional
correction, plus a brief amendment of the existing SDK provenance documentation
if needed. Factor the existing applyPatches expression into a narrowly named
helper/value reused unchanged by mkPiWorker and a directly buildable
`packages.x86_64-linux.pi-sdk-source` output. This output must expose exactly the
existing source derivation, independently of evaluating the SDK package's JSON
metadata. Preserve the existing source name, pin, patch list/bytes, stdenv/platform
inputs and central source.override; no new preparation framework or duplicate
packager. The upstream TypeScript/source-rebuild route remains unchanged.

Add one ordinary CI step immediately before Evaluate all checks:

```sh
nix build --no-link --print-build-logs .#pi-sdk-source
```

Leave the existing all-check evaluation command, check selection, build commands,
assertions, action versions and other jobs unchanged. This step realizes only
the patched source, not the SDK or application. Underlying import-from-derivation
remains: document that no-build all-check evaluation needs this source preparation.
Do not claim general IFD removal. No metadata/lib interception, string rewriting
of upstream Nix, installed JS patch, relaxed check or ambient package fallback.

Before amendment, retain 0226's reviewed source/head and exact patched-source,
SDK, worker and full-application derivations, store outputs and input graphs.
Quick validation runs the new source-preparation target followed by the exact
unchanged `nix flake check --no-build --print-build-logs`, plus normal formatting/
hooks. Lead assigns a fresh utility if that batch is uncertain. Do not delete
store paths or disturb the shared Nix store to simulate a cold runner. Final-head
cold CI after this actual correction is required; an unchanged rerun is not proof.

Compare both the existing source/SDK outputs and the complete application
derivation/input/output graph to 0226. Exact identity permits reuse within the
corresponding verified scope. If the full application changes, name the precise
input delta (including any source/provenance-path change), establish reviewed
runtime equivalence where possible, and let lead select the affected check before
any full run. Do not assume SDK equality alone proves application identity or
repeat the native 200 automatically. Locks, upstream NAR, catalog, Node, patch
semantics and every unrelated runtime input must remain unchanged.

Lead directs folding this packaging correction into its owning unmerged SDK
commit with a normal amend, preserving hooks and unrelated work. Retain old 0226
provenance, old/new base/head and range-diff/equivalence evidence. Independent
affected review must cover the changed packaging/CI prerequisite and the complete
three-commit development series, with no leftover fixup commit. Earlier review
continues to support only unchanged behavior; it does not approve this amendment.
No repository-default integration or deployment approval follows.

The exact 0226 native200 has now settled: all 220 inputs Sent and appended once,
all 32 final-audit boundaries completed, auditCompleted true/partial false, and
the genuine question reached Accepted during foreground with fairness passing.
Only latency failed: p95 HTTP 282.851 ms, post-sync upper 2820.310 ms, public Sent
3127.096 ms. These are retained failed-target results, not a causal saving claim.
Packaging correction and final-head CI remain required for readiness. This
package adds no performance investigation, profile, native run or live action.

## D2: integrate and deploy the two reviewed optimizations

Status: sufficient deployment amendment; no design blocker. The user now directs
"merge & deploy the two optimizations, then proceed with investigation on how to
improve responsiveness" and reports every Pi tab affected. Lead records approval
for runtime and necessary matching workspace/configuration pins into their remote
defaults, followed by Aitherdev deployment. This supersedes the earlier preparation
only boundary. Responsiveness investigation starts after verified deployment and
machine release; it no longer waits for selection of one affected tab. P9's shared
immediate refresh path remains source evidence, not an attribution of the delay.

### Sources, ownership and host decision

Select reviewed runtime `b07fec04174ef5303356fea54a326bce578d30e6`, retaining the
three-commit series above deployed `3961d7285abc6c996206bc50a7cd68977086312b`.
The two changes release the dead private prefix after successful commit and skip
SDK context cloning only with neither listener phase present. P10-CI review and
final generic artifact comparison cover the packaging amendment; the measured
0226 result remains historical evidence with complete audits and question fairness
passing but latency failing. Neither a target pass nor a tab-latency fix is claimed.

I0 owns runtime integration preparation; I1 owns the two mechanical pin streams
under lead's direct brief. Workspace files are `flake.nix` and generated
`flake.lock`, preserving the direct nested runtime override. Configuration changes
are only the existing `dev-workspace` channel's `devWorkspace` lock selection,
generated through confctl. Keep one new pin per stream; never amend previously
merged rollout commits. Preserve extension bf12ac71, provider db79231a, all sibling
inputs/follows, model/provider configuration, managed team settings, claim policy
and legacy machine bridge. Lead owns review acceptance, integration, builds,
activation, verification and release; architect edits only this design amendment.

Use the accepted D0/D1 host-impact proof and rollout. The complete 3961-to-b07f
source diff changes no host module, host paths, helper/session-entry source,
Codex wrapper or lock. The SDK override belongs only to `mkPiWorker`;
`pi-runtime-host.nix` still constructs its tools from the independent unchanged
`pi-runtime-host-package.nix`. With unchanged relevant effective machine inputs,
the installed helper xhc71, template 8q48, drop-in br5i and sudo bytes/order retain
their prior proof. A different application SDK does not require new host support.
I1 must identify any relevant input delta introduced by baseline refresh; an actual
host prerequisite returns to lead before widening scope. No new host inventory,
evaluation harness or whole-system build is needed for this unchanged contract.

Deployment is PROFILE ONLY. Preserve both system selections at
`/nix/store/k79k3l35lnhfikw65zwnacag112w7z9p-nixos-system-aitherdev-26.05.20261121.94c3211`.
The site guide's initial host-install sequence does not require reinstalling an
already equivalent prerequisite. No confctl dry activation, system switch, reboot
or unrelated system/Codex update belongs to D2.

### Artifact and integration gates

The current profile is
`/nix/store/waw0fw7vmz4z0f5ym5cjh8p4ij0xqq70-dev-workspace-0.2.0`.
Generic `/nix/store/yfkkdq85248gwdbmh0hbffkic8mgsnq4-dev-workspace-0.2.0` is verified
runtime evidence, not the site deployment profile. From the final committed
workspace/configuration pins, run the existing cross-lock checker:

```sh
bin/check-dev-workspace-deployment --workspace-root WORKSPACE_CHECKOUT --configuration-root CONFIGURATION_CHECKOUT
```

Reuse P10's exact source/SDK/worker proof and generic artifact comparison within
their scope. Ensure the existing patched-source prerequisite is realized before
no-build evaluation; preserve all checks. After normal pin quick checks and
applicable review, lead allocates one composed build/check batch in the workspace
checkout: `nix build --no-link --print-out-paths .#default` and the existing
`checks.x86_64-linux.{pi-runtime-composition,agent-team-policy,cluster-provider-composition,tracking-source,deployment-contract}`
outputs. Record the full composed path/derivation, committed source heads, complete
semantic input graph and worker/SDK/Node paths. Compare selected and candidate
metadata: managed catalog, extension, models/providers, claim readers/typed target
and legacy bridge, live-switch policy and native Codex package must be preserved.
Account for expected worker/SDK/application changes explicitly; generic package
identity cannot substitute for composition proof. No further native200 or profile
campaign is required by this mechanical deployment package.

Finish applicable final-head CI and retain review/history evidence. Integrate the
approved runtime, workspace and configuration heads through separate short claims,
normal fast-forward/hooks/SSH pushes and fresh remote ancestry proof. Shared
workspace integration also takes its nonblocking tracking lock. Release each
repository claim before waits or records; stale preparation returns outside the
claim. If a rebase changes source, retain old/new ranges and reviewed equivalence,
refresh pins and repeat affected checks. Build/copy the exact final composition
before acquiring the machine; do not substitute an older composed result.

### Activation, retained workers and release

Lead acquires a fresh schema-2 machine claim for registered
`vpsfree-cz-configuration`, selector `cz.vpsfree/machines/aitherdev`, adapter
`confctl`; the previous rollout's released claim cannot be reused. Verify its held
status and typed mapping once for the intended committed batch. Use ordinary
`workspace-host switch --source WORKSPACE_CHECKOUT` with `DEV_WORKSPACE_CLAIM_ID`
and this exact session/workspace identity. The installed coordination and switch
contracts retain all lifecycle, creation, cluster, package-generation, authority,
invocation, policy and claim preflights. Any refusal is diagnosed at its owning
boundary; it never permits a private helper, state rewrite or session stop.

Retained Pi supervisors/workers keep their original package roots, capabilities,
settings, histories and receipts. Profile selection does not upgrade them or
silently apply the new SDK/prefix behavior. No new wire/schema/API or receipt
migration is introduced; original independent history/witness/no-replay and
attachment ACK/permit proofs remain. Separate session lifecycle authorization is
still required for any later worker upgrade. Preserve this limitation when
reporting the rollout's effect on existing tabs.

Verify the actual selected composed path, unchanged system paths and host support,
portal/router/coordinator health, native Codex identity/settings and retained Pi
identity/receipt continuity through existing non-mutating checks. Confirm startup
and naming availability without sending test prompts or creating a session merely
for verification. Preserve unknown operations and join all activation effects;
interruption resumes the original forward target through ordinary recovery.
An incompatible predecessor or deleted record is never a rollback strategy.

In existing rollout/review receipts, retain source/input graphs, exact deployed and
final heads, canonical targets and fresh remote lineage proof, plus any reviewed
equivalent successor. Once effects are verified and the complete deployed lineage
is integrated into approved defaults, lead checks the exact owned claim, releases
it and verifies released status promptly. UI responsiveness investigation then
continues without holding the machine; no separate UI acceptance is a release
gate. No archive, deletion, session stop or cleanup is authorized by D2.

### D2-SDK: keep patched SDK selection independent of consumer packages

Status: sufficient I0 correction, canonical runtime-owned builder accepted by lead.
The first composed68c build failed its existing exact-SDK assertion: actual
`/nix/store/46m43wcaa26hcb2yg4jlsb7g0v8m82zd-pi-1.5.2`, expected
`/nix/store/nvwxl97fj19gvy9bnvr8s485jpn5hjmm-pi-1.5.2`. Retain the failure in
`/tmp/2026-11-24-pi-message-delivery-composed-68c12c44-build-exact.log`.
No activation occurred. The assertion correctly protects the canonical SDK
contract; it must not be weakened, redirected to the observed path or removed.

Immutable derivations establish the mechanism. The extension's mkPackage forwards
site pkgs to runtime mkPackage, which calls mkPiWorker with those packages.
mkPiSdkSource currently also takes those packages, so applyPatches uses site
nixpkgs d58a46e3 instead of runtime nixpkgs a5cc6f2c. Site source derivation
lf8vcn8iyidnmhwfy41wckqixilmd2g1 produces bdzasgisc0rzczqwdjx0bzz30m20ghcr;
generic j74qnl5sjv4gln74gpm85zdp2j1ddrfb produces xs767f5if7a48a5sclmsrasi2bz3x4qz
(all have the pi-sdk-context-source suffix). They have identical upstream source,
patch, builder-script inputs and patch phases, but different stdenv/bash derivations.
Both source NARs are `sha256-X3eyG/ZKadUUtVVpYa24tjBwCbg30ROI6tLc4A3ucq0=`.

Upstream reads that source path into workspacePackages and npmDeps; it therefore
produces different SDK derivations despite identical source bytes. Both SDK builds
retain the same upstream compiler, hooks and Node gf597zf0ysgbngwb92baxgxjd02px6jh.
The site SDK derivation apw06nafv9p5wc98rmm56iraykvv657l and canonical
lrqcqfx5nfm1bjdanpy5jwjrwjs1izvz each have 2849 recursive nodes: 2774 identical
common nodes and 75 unique nodes on each side, including source-builder ancestry
and downstream package propagation. All 15328 file/link entries match except
bin/pi's exact self path and eight workspace-tarball resolved paths in the installed
.package-lock.json. SDK/runner/AgentSession modules are byte-identical. SDK NARs
still differ (site `sha256-DdUHRVoQlkMoDES2sCppPSdedyYkIksb4AmmESmHSjA=`, canonical
`sha256-olnZQwmLmbvsozq+cwG1mi6xtfSetZthzrCRcKSr/6A=`); do not call whole outputs equal.

I0 owns `flake.nix`, the focused existing `nix/tests/pi-worker.nix` contract check,
and one factual sentence beside source preparation in `pi-runtime/README.md` if
needed (lead prose pass). Make private mkPiSdkSource accept a platform rather than
consumer pkgs and obtain applyPatches from runtime's own locked nixpkgs imported
for that platform. Both mkPiWorker and exported pi-sdk-source use this one helper.
Keep worker assembly on caller pkgs; keep upstream Pi package override and Node
selection unchanged. This preserves the already-tested generic j74/xs767/lrqc/nvwxl
identities and makes site composition select them too. Do not switch source
preparation to Pi's separate nixpkgs, which would introduce a third artifact.
No new export, protocol, lock, patch, version, catalog, worker JS or host change.

Before another full application build, prove generic pi-sdk-source and SDK exact
derivation/output identity to b07, then exercise the same private mkPiWorker with
an independently pinned existing package set (Pi's already-locked nixpkgs is
sufficient). Add evaluation assertions to the existing worker contract check that
its SDK derivation/output and Node equal the ordinary worker's. Pass that alternate
worker privately from flake.nix; do not export a test API or add an input. Compare
SDK identities rather than whole worker paths, since caller worker-assembly tools
may legitimately differ. The previous composed failure is the concrete failing
consumer proof; the unchanged site assertion remains the final consumer test.

Lead allocates the focused source-preparation then unchanged no-build evaluation
batch, including the new assertions, and any affected worker/artifact checks.
Retain all prior checks. SDK tests may be reused only after exact source/SDK/Node
identity is proved; otherwise report the precise delta before widening verification.
No fresh SDK build, 200-input run or profile is automatic. Record final worker and
application graph differences separately: source-provenance relocation and caller
assembly changes are not blanket application identity. The final composed build
and five unchanged checks remain necessary after the pin refresh and review.

Runtime b07 is already merged: deliver a new focused commit above it, never amend
merged history. Lead owns affected review and final-head CI. I1 then regenerates
and amends only the two still-unmerged D2 pin streams to the reviewed final runtime,
preserving extension and all unrelated inputs. Run the existing cross-lock checker;
repeat the exact composed batch only after focused identity proof passes. No site
check or extension source edit is needed. D2's profile-only, retained-worker,
admission, forward-recovery and claim/release contracts remain unchanged. Build
failure leaves the current system/profile selected; deployment and responsiveness
investigation retain their required order.

### D2 configuration baseline reconciliation

Fresh configuration default `4694ca977a6816687e932b2b921a3e103f059224` advances
844ffe only in three vpsadminos role lock nodes and
`cluster/cz.vpsfree/nodes/common/all.nix` OOM policy. Preserve these upstream changes
when replacing the unmerged D2 pin. The complete lock-node comparison leaves root
mapping and all other nodes unchanged, including devWorkspace, nixpkgsStable,
home-manager, llm-agents and confctl. Aitherdev is spin nixos and selects only
nixos-stable/home-manager/llm-agents/dev-workspace. Its standalone config imports
hardware, disk cleanup, KB staging, home-manager and the selected host module;
it does not import the node common module. The unchanged pinned confctl loader
selects that exact machine config plus spin-specific modules and metadata modules,
not other machines' config.nix files. The shared module lists and overlays are
also unchanged. Thus this baseline delta changes no Aitherdev helper/session-entry,
template/drop-in/sudo or Codex-wrapper effective input. Reuse the prior D1 host
proof; PROFILE ONLY remains supported without a system build or activation.
Final runtime-pin and composition checks remain separate required gates.

### D3 responsiveness: first deployed read-path milestone (2026-11-24)

Status: bounded investigation complete; sufficient next diagnostic below, subject
to lead allocation. No production optimization or source release is claimed.
The user reports every Pi tab slow, so choosing a particular affected session is
no longer a prerequisite. Deployment precedes this investigation: runtime e61d3b7e,
workspace f618f0e6, config d8225a89, composed g7wv, verified and machine released
at 15:10:43Z. Existing workers retain their frozen packages; this work does not
upgrade or restart them. Current portal source is e61d3b7e and shared browser
provider db79231a. P10's sampled acceptance CPU is not tab-latency attribution.

Architect's bounded local Unix-socket sample made seven GETs, all joined: one
unscoped Pi details request correctly returned 409, one Pi shell returned 200,
then five scoped/comparator reads returned 200. Bodies were discarded; the shell
was held only in memory to obtain its existing scope header. The Pi target was
ordinary; no target identifiers or message content are retained here. These are
single observations on different Pi/Codex histories and workload, without browser
scheduling, transport or rendering time. They establish neither percentiles nor
an all-session ratio.

| Read | TTFB / total | Body bytes | Existing server timing |
| --- | --- | --- | --- |
| Pi thread/page | 1.248892 / 1.249114 s | 73759 | total 1247.02 ms |
| Codex thread/page | 0.147169 / 0.147328 s | 74916 | total 145.53 ms |
| Pi activity | 0.723981 / 0.724197 s | 695 | total 721.22 ms |
| Pi details | 3.663789 / 3.664045 s | 31184 | repo_status 2712.58, services 821.55 ms |
| Codex details | 3.477653 / 3.477877 s | 38550 | repo_status 1770.99, repo_validate 852.01, services 791.95 ms |

The sample demonstrates backend wait on Pi reads with negligible body-transfer
time. Details is expensive on both backends, chiefly repository/services work.
Existing Pi Server-Timing exposes no admission/worker/receipt split, so the
1.25-second page response cannot yet be assigned to any one of those stages.

The current transcript path performs scoped admission, request-local BindRead,
verification and fresh read admission. piruntime transcript_snapshot selects the
frozen worker's supported operation. Current session.mjs snapshot bounds displayed
entries but hashes JSON of the entire branch; conversation.go transcriptSnapshot
then holds its mutex while reading owned receipts and matching exact Accepted
witnesses. Codex requests thread/read without turns and reads a bounded page.
These are cost mechanisms, not measured substage attribution. Cancellation removes
a worker-call waiter; it does not cancel already dispatched synchronous JS work.
Do not infer the current worker path or legacy polling capability from the portal
package alone, or remove fresh ancestry/receipt checks to improve a measurement.

I0's browser pass establishes immediate shared visibility recovery and a common
keyed renderer, with no Pi-only fixed 5–10-second delay. SSE-open intentionally
cancels a pre-open page read and starts a fresh one. Pi adds delivery collection
polling every two seconds after completion, including empty/terminal results;
its send branch awaits a collection refresh before POST and local acknowledgement.
The collection uses ready-identity checks, bounded SQLite List and disk-only
ReadInputSelection (controller.go); it does not invoke a native snapshot or the
dispatcher's original-receipt Lookup. Its cost remains unmeasured. Pi also starts
question/plan refresh pairs from mount, transcript apply and connected transition.
Those calls can overlap and run after transcript render. No contention or render
latency is established by that source fact.

**One next diagnostic, no application changes.** Lead may allocate one owner a
single serial-versus-concurrent comparison on the same existing ordinary Pi
conversation: thread/page, activity, deliveries, pi-questions and pi-plan. Use
the existing scoped public routes and unchanged identity/settings; at most one
shell GET to obtain scope, then one sequential pass and one concurrent pass of
those five GETs (11 GETs maximum, 10-second per-request limit, 90-second total
bound). Discard bodies and record only endpoint class, status, TTFB, total, byte
count and existing Server-Timing. Stop on identity refusal or timeout; do not
retry, send input, create a conversation or change native state. Join every
client before reporting. This intentionally models one page's overlapping read
work; it is not a capture of the user's browser or a sustained load test.

Acceptance is a compact same-target route table identifying whether delivery and
workflow reads are independently slow and whether this one overlap amplifies
page/activity delay. Retain errors and cancellation limits; a canceled HTTP waiter
does not prove native work was canceled. No harness, production hook, package,
schema, cache, authority or recovery change is needed. This diagnostic requires
no build, native campaign or 200-input rerun. Identity/sensitivity checks and exact
route/scope review are its preflight; all raw identifying evidence stays in chat
or verified ignored, untracked own files. Lead owns further source allocation.

The original browser's event-to-request, canceled/fresh GET, parse/apply and paint
timeline remains missing. No connector exposes it here; shell requests or a new
Playwright browser cannot establish that original timeline. Workflow single-flight
is a possible later conventional reduction, but is not released: its contract
must preserve explicit refresh recovery, post-mutation fresh reads, response epochs
and destroy/scope cancellation. No latency improvement is claimed. The ten-minute
first milestone stops here without another inventory or performance campaign.

D3-R first attempt stopped after its shell GET (200; TTFB 1.517979 s,
total 1.520534 s, 50767 bytes). The preparatory regex searched every
data-conversation-scope attribute, although session.html emits the intended body
attribute and descendant team-control attributes. The script rejected ambiguous
or missing scope before all ten endpoint reads; their results remain missing.
Discarded HTML prevents recovering the exact match count or values. This proves
a parser limitation, not an identity or backend refusal. Preserve the failed
script and receipt; all clients and watcher effects joined per I0's report.

For a separately allocated attempt, use a standard HTML parser on the shell held
only in memory. Require one body element and exactly one scope attribute on it;
reject duplicate attributes, missing/multiple bodies or a value outside
pi-workflow-v1 followed by a colon and 64 lowercase hexadecimal digits. Ignore
descendant scope attributes. Check synthetic body-plus-team-controls and the
negative cases locally before any request. Do not pick the first arbitrary match
or derive a replacement from runtime records. The unchanged 11-GET, per-request
and total bounds apply to that new attempt; this correction authorizes no retry.

#### D3 final bounded read receipt and priority

Lead's literal-launcher run completed successfully: 4.523578 seconds, eleven
GETs all 200, all clients joined, no bodies or identifiers retained. Scope shell
took 0.557867 seconds. The body-parser checks passed; the intervening wrong-path
launch made zero GETs. Both earlier failed receipts remain preserved. Successful
timings are in `/tmp/pi-d3-r2-ev89ayyx/timings.json`; raw receipt is
`/tmp/pi-d3-r3-run.log`, SHA256
`acebf6b5621010460f3a62d99646450b8ea426c5f86b0cbaf520df2802e1b678`.

| Same Pi conversation, total seconds | Serial | Concurrent |
| --- | ---: | ---: |
| thread/page | 1.211839 | 1.309754 |
| activity | 0.786367 | 0.808882 |
| deliveries | 0.149735 | 0.218275 |
| pi-questions | 0.166452 | 0.145808 |
| pi-plan | 0.105835 | 0.146410 |

Page bodies were 67706 bytes in both passes; body-transfer time was negligible.
Existing Server-Timing totals were page 1210.35/1307.88 ms and activity
785.14/807.62 ms. The other three routes provided no substage timing. This one
sample shows no large overlap amplification: page increased about 98 ms and
activity about 23 ms. It does not establish percentiles, stable concurrency
effects or the user's browser cause. Identical byte counts do not prove identical
content. Delivery/workflow reads were substantially shorter than page/activity
in this sample; shipping workflow coalescing as a demonstrated remedy is not
supported. Pre-send feedback and redundant reads remain source observations.

The single next diagnostic priority is a bounded page/activity substage timing
capture: distinguish fresh admission, native snapshot RPC elapsed time and owned
receipt projection at their actual owning boundaries. Record absent stages as
absent; do not infer receipt time from the HTTP remainder or call native elapsed
time CPU time. Current HTTP headers cannot supply that split. A separately
allocated narrow instrumentation decision would be needed, reusing existing
bounded diagnostics where applicable; no new wire protocol or tracing framework
is proposed or released here. Measure existing calls only, preserving identity,
freshness, cancellation, exact history/witness checks and attachment authority.
The original browser scheduling/parse/render/paint gap remains independent.
This closes the bounded phase with measured server-delay evidence and an explicit
attribution gap, without a new probe, source change or automatic campaign.

### D4: preserve the original receipt during ordinary browser retry

Status: sufficient independent I0 implementation package, subject to lead release.
The screenshot remains outside VCS. Its controls identify the legacy browser
outbox, not the portal-owned delivery collection. Read-only evidence establishes
a retained worker with piInputDelivery 1 but no piCheckedInput, an empty portal
collection and canEnqueue false. These facts establish compatibility relevance;
they do not identify either pictured request. Owned native receipt metadata was
Accepted at observation time, but no browser ID was available to join the cards
and no fresh native witness verification was performed by this investigation.
The user saw the uncertain message only in its recovery card. Preserve that
observation without treating it as proof of non-dispatch. Target names, message
text, original IDs and the screenshot are not design/test fixtures.

The independently established defect is the ordinary no-delivery retry path.
Browser retryMessageReceipt submits the saved ID and wire input with retry true.
conversationAdapter.Send currently forwards it to ordinary send. supervisor.send
includes Retry in SendInput and recomputes SubmissionDigest with current settings;
receiptEngine.sendOwned then requires the exact original ref, input and settings.
An original Retry false receipt therefore conflicts with that inquiry. If the
receipt is missing, ordinary send has no retry-only refusal before native dispatch.
Native delivery-mode retries already have their separate lookup-only behavior.
Do not alter native receipt hashing or utility input semantics to repair this
HTTP consumer mismatch.

**Owner/files/interface.** One implementer owns the complete correction in
dev-workspace above e61d3b7e: portal/internal/piruntime/adapter.go (including a
private helper), portal/internal/piruntime/adapter_test.go and a short owning
paragraph in docs/pi-runtime.md. Existing queued_input_test.go may gain a focused
retained-lookup assertion only if the adapter regression cannot cover that same
boundary without duplication. Lead owns final prose, index allocation, review and
integration decisions. No codex-web, browser/UI, worker/SDK, lock, version, schema,
protocol, public interface or capability change is needed. No peer records change.

At conversationAdapter.Send, treat Retry true with empty Delivery as an inquiry
only. Resolve the original full reference through the strict private receipt
decoder for this exact owned conversation and ID; validate the current adapter
handle/generation, mapping, owner kind and operation before using the result.
Compare exact prepared wire input and ActionContext with the stored original,
and reject a native delivery-mode/action mismatch. Retain the handler's existing
attachment preparation and original-ID conflict checks. This is not a text search.
Use the stored immutable Ref/Input/Settings/Generation; never regenerate its
digest from current settings or replace its saved Retry value. The incoming
Retry flag selects inquiry behavior at this HTTP adapter boundary only.

Delegate proof to existing Manager.LookupQueuedInput with that exact full ref.
It uses input_lookup_v1 for checked workers and the retained native creation
verifier for supported non-fork workers. Preserve all its generation ancestry,
strict receipt, independent history/witness, current-runtime and no-load checks.
Disk Phase Accepted alone must not produce Accepted. Missing original stays
Unknown with zero sends; malformed, differently owned or mismatching originals
stay Unknown/error. NotSubmitted remains its evidenced terminal outcome, never
new dispatch permission. Prepared/dispatching/Unknown cannot be promoted without
the existing positive proof. An unexpected Pending on the ordinary path cannot
be represented as successful acceptance. Original receipt bytes remain unchanged.

Fresh ordinary Retry false sends, explicit steer/followUp retries, portal queued
input, native send operations and utility grants retain their existing behavior.
Keep current HTTP origin/scope/admission, mutation lock, host/profile, Bind/Verify
and attachment ACK gates. The existing piAdmittedConversation.Send lease still
checks current authority/access and completes ensureAttachment before binding.
After the adapter chooses inquiry-only behavior, the existing lookup contract
owns proof: input_lookup_v1 and verify_creation deliberately do not acquire a
native mutation permit or run send-specific checkInputAdmission. Do not add a
native mutation or new observational operation to reproduce those effect gates.
Actual send ACK/permit, callback/policy readiness and checkInputAdmission remain
unchanged. Conservative persisted mapping held/pending guards may refuse the
inquiry; a positive old receipt grants no new effect authority. Do not bypass an
existing front-door refusal to make lookup work.
This package does not promise recovery through an unavailable/held front door or
an unsupported retained fork. It adds no fallback, reload, native retry or resend.

**Acceptance and quick checks.** First reproduce through the actual shared HTTP
handler and Pi adapter/Manager using existing native-free Unix supervisor fixtures
with an explicitly retained unchecked launch contract (piInputDelivery 1,
piCheckedInput absent). A modern checked-only fixture does not cover the failing
consumer. Send one ordinary Retry false request, retain its exact receipt, then
submit the same ID/wire with Retry true. Require the original HTTP Accepted ID
and entry after the existing retained native witness verifier, one total native
send, zero enqueue/load/restart, and unchanged receipt bytes. Extend only the
existing fake worker's needed proof operations; do not stub the lookup result.

Cover missing original (Unknown, no file/native send), changed wire/action/mode,
foreign/corrupt owner, unresolved phases, failed native witness, wrong generation,
and terminal NotSubmitted without replay. A supported current-settings change
must not alter the original digest; an unavailable front-door or proof still
refuses. Include a stored Retry true historical original as immutable data.
Confirm fresh Retry false and existing native-mode retry tests still pass, and
that direct native/utility immutable-input tests are unchanged. Run focused
adapter/queued-lookup and existing portal message-boundary tests in the declared
Nix environment with go test -mod=readonly, then the affected package checks.
These are planned checks, not tests run by architect.

After the focused committed correction and independent review, lead chooses
applicable final-head CI/package checks. No 200-input campaign, profile, live
peer retry, upgrade or deployment is automatic. This portal-side fix supports
the retained unchecked runtime through its existing verifier; no worker restart
is required by the design. Reverting it changes no stored format but restores
the broken retry behavior. No original record is migrated, rewritten or replayed.

Screenshot attribution remains open: saved browser delivery/action flags, original
IDs and FIFO membership are missing. An idle-only attempt while Working and an
Unknown FIFO head are different possible Resume gates; an enabled retry button
also does not establish that its handler will dispatch. Do not modify these
controls or convert a waiting entry to steer as part of this package. The narrow
server correction is independently testable, not a claim that either pictured
message has been recovered or that the complete reported problem is fixed.

### D5: compact status attached to its message

Status: sufficient independent frontend package for I1 after its D5-F report and
lead allocation. Base behavior inspected at runtime e61d3b7e/provider db79231a;
D4-M now occupies only its three backend/docs files and reports its index released.
The second screenshot is outside VCS; no peer content or identifiers enter this
design or fixtures. I1 owns the separate read-only question of actual progress.
This package corrects independently demonstrated presentation defects and does
not claim to restart or unblock a native turn.

The large bare Queued bar is submitPortalDelivery assigning the initial POST
status to message-submission-status, whose template class is notice warning.
Later collection polls do not update or clear that successful initial notice.
mountDeliveryStatuses separately emits an unclassed article and two paragraphs
for message and state. The portal's compact message-receipt styles therefore do
not apply to those children; default paragraph spacing separates text from Sent.
The shared mountConversation consumer repeats the initial-status notice. This is
render structure and duplicated stale status ownership, not proof that a stylesheet
failed to load. Both consumers must use one shared delivery-status view.

**Files and owner.** I1 owns codex-web conversation/assets/deliveries.js,
conversation.js and conversation.css, their existing
test/deliveries_browser_contract_test.cjs and conversation_browser_contract_test.cjs,
and a short delivery-presentation paragraph in docs/reference.md if useful. It
also owns runtime static/app.js, static/style.css only for integration with existing
receipt theme rules, templates/session.html for required asset cache versions,
and portal_delivery_composer_contract_test.cjs under portal/internal/web. Update
existing import/cache-version consumers narrowly where necessary. No duplicate
renderer or runtime copy of provider code. After provider commit/publication,
I1 updates only that dependency through the normal matching flake.nix/flake.lock
and portal/go.mod/go.sum flow and existing pin check. Preserve every other input.
Lead sequences index windows after I0, reviews the complete dependent series and
does final user-facing prose. I1 must report D5-F completion/capacity before edits.
No runtime adapter, native source, delivery database, I0 docs or backend change.

**Presentation contract.** One compact row associates the complete literal message
with a small adjacent state label. Use existing neutral receipt/queue colors,
type scale, borders and control styles; remove default paragraph margins and
extra space reserved for nonexistent close controls. A short message with no
action fits one row at desktop width; on narrow screens text and state wrap
together without horizontal overflow. Long text remains readable and wraps.
Use shared component classes in the provider stylesheet; both consumers receive
the same structure, with only existing portal theme adaptation. No bare full-width
success notice, detached terminal label or second status for the same request.
The existing global error notice remains available for failures without a safely
associated record. Do not clear an unrelated or newer failure when one input
succeeds. Empty status collections take no blank vertical space.

Preserve status distinctions from the existing wire contract: queued means saved
and waiting for dispatch; dispatching means submission is in progress; pending
means queued in the native runtime but not yet witnessed in history; sent means
the exact native input was Accepted with its receipt. It does not mean assistant
processing or reply completion. Lead's settled compact labels are queued: Queued;
dispatching: Sending; pending: Awaiting acceptance; sent: Accepted;
not_sent: Not sent; unknown: Unconfirmed. Accepted has the concise explanation/title:
"The runtime confirmed this input. A response may still be pending." Keep it
available without an always-visible tall help block. Do not add a Pi name branch
to the shared component. Unknown means acceptance cannot be confirmed,
never proof of non-delivery. not_sent retains positive refusal meaning. Keep
failure explanations and existing Check delivery/Copy to draft actions adjacent
to their message, compact and keyboard accessible. Copy never sends; Check only
reads. This package adds no retry/drop/delete/automatic send or FIFO reordering.

**One view owns updates.** Feed the validated POST status to the same mounted view
that displays collection reads, rather than assigning it to the global success
notice. A small present(status) method on the existing returned view is sufficient:
validate the established scope and exact status, update the row by original ID,
and render its positive response immediately. Retain no browser storage/schema
or cross-conversation cache. An older collection request already in flight must
not overwrite that status or remove its row; use a view-local read generation
and one dirty follow-up through the existing refresh path. The normal post-submit
refresh must start after presentation or join that follow-up. Fresh later collection
results remain authoritative; don't invent timestamp ordering or infer transitions
from message text. If the follow-up read fails, retain the evidenced row with
compact stale/unavailable feedback, not an invented outcome. This is a bounded
view update, not a new polling or status framework. Preserve existing poll cadence,
current-scope guards and destroy cancellation behavior.

Keep each row tied to its original ID through updates. Status text, not color alone,
conveys state. Preserve keyboard focus on a surviving action across ordinary polls;
polite status announcements should report changes rather than reread full message
content every two seconds. Literal user text remains textContent, never HTML.
No transcript deduplication by matching text, no claimed run progress, no removal
or expiry of server records, and no changed retention contract. Legacy browser
outbox and unchecked workers keep their existing dispatch/recovery rules and UI.
Unsupported delivery capability still follows its existing explicit path.

**Acceptance/checks.** Extend existing provider mounted-view and both consumer
fixtures with short/long messages, narrow wrapping, empty state and every wire
state. Prove queued-to-sent updates the same message row and leaves no stale global
Queued notice or detached duplicate Sent; sent requires the existing valid exact
receipt. Cover POST response during an older GET, failed refresh after response,
wrong scope, destroy, unrelated/newer error preservation and independent IDs.
Check no POST on poll/check/copy, unchanged immutable original requests, selection
checks, draft edits and attachment preservation. Keyboard focus and status
announcements must survive updates without repeated full-message announcements.

Run focused Node/browser contract and syntax checks from each declared Nix
environment; retain existing durable admission/recovery checks. Before final review,
use the established disposable browser fixture with synthetic content to inspect
actual applied CSS at desktop and narrow width, normal and error states. No live
peer UI/storage or screenshot content is a fixture. A DOM-only test cannot certify
spacing; retain a local synthetic screenshot or equivalent geometry evidence.
Uncertain browser/build checks go through lead-owned verification allocation.
After quick checks and commits, independent review precedes longer package/CI
checks. No native run, profile, 200-input campaign or deployment is automatic.

The change requires a portal/provider asset update only; existing worker packages,
receipts, API and persistent browser records are unchanged. Rollback restores the
old presentation without data conversion. Actual peer dispatch/progress evidence
may justify a separate backend correction, but does not block this settled UI
repair or let an accepted input be described as a completed response.

D5-F completed without a current receipt join: two bounded peer GETs yielded
one 409 without state and one non-JSON result whose HTTP status was not retained
before decode failure. No full scope/original ID/native receipt proof was obtained;
all effects joined. Neither result establishes acceptance, non-delivery, a held
runtime or stalled native progress. No further forensic attempt is part of this
package. I1 reports capacity; the sufficient UI package is ready for lead allocation
independently of that unresolved progress question.

D5-P resolved the current public-state gap at approximately 17:43Z with exactly
three successful read-only GETs, all clients joined. Source-derived body attributes
provided the opaque conversation route ID, exact scope and native identity; no
target identifiers, bodies or content were retained. The collection had one steer
entry in sent state with a receipt matching its original ID and a nonempty entry
ID, and no queued/pending/unknown entries. Creation-to-last-update was 2.371 seconds.
The collection was enqueue-capable. This is the public durable projection of its
previously established Accepted receipt, not a new independent native-history
verification performed by this diagnostic.

The exact-native activity observation was eight milliseconds old at reading and
reported idle, latest turn completed, no blocking request, no wait reason, two
turn messages and zero turn tool calls. The latest turn lasted about 13.887 seconds
and completed about 12.380 seconds after the delivery's last update; completion
was about 671 seconds before this observation. Activity coverage was incomplete,
so no broader timing claim follows. The current server state does not show stuck
delivery or an active waiting turn. The screenshot lacks an original ID, so it
cannot conclusively join that card to the sole current row or prove what reply
content the browser rendered. The stale global Queued notice remains independently
proved by source. No resend, transcript-body read or further probe follows from
this receipt; browser freshness/rendering remains a separate possible gap.

## D6: coherent display from independent activity and transcript feeds

**Sufficient minimum brief; lead release required.** I0 owns implementation after
I1 releases D5 source/index ownership. Runtime files: `portal/internal/web/static/app.js`,
existing `portal/internal/web/message_delivery_browser_test.cjs`, narrowly related
activity presentation tests, session-template asset version if required, and one
behavior paragraph in `docs/workspace-portal.md`. No provider/backend/worker/API
change. Preserve D5's compact delivery rows. Lead owns final product wording.

**Evidence and authority.** The current work label ORs transcript `threadActive`
with activity `latestTurnStatus`, while elapsed text comes from activity alone.
Active transcript plus completed idle activity therefore produces Working plus
idle waiting time; the reverse arrival order can preserve older in-progress
activity after an idle transcript. This is a source-proven display defect, not
a join to the screenshot or proof of delivery failure.

Pi transcript `latestTurnId` and activity `currentTurnId` both identify the last
persisted user entry (`piruntime/adapter.go`, `pi-runtime/src/activity.mjs`). Codex
uses its latest native turn ID in both projections. IDs support equality only.
Transcript has no timestamp comparable with activity `observedAtMs`; Pi can also
be busy before a new entry persists. Equal IDs therefore cannot establish a
cross-feed winner. The minimum safe fix displays unavailable on disagreement.

**Display rule.** Use one small display-only projection for work label, current
elapsed/counts, waiting CSS and tab title/ARIA/indicator. Never assign
`threadActive`, `threadIdle`, dispatch readiness/revisions, interactive/held state,
host gates, queue controls or receipt state from this projection.

- Use the last successfully applied **newest** transcript for the current binding;
  history/repair pages cannot replace display evidence. Activity must belong to
  the same nonempty thread and current read/binding generation. Two present turn
  IDs must match. Missing optional IDs permit only mutually consistent states,
  never a completion override or completion-triggered refresh. Both absent with
  idle/no turn is a supported empty conversation.
- Require a successful current activity read, no snapshot stale flag and the
  existing timing clock's freshness budget. Include local request duration in
  freshness so an expired delayed response cannot become fresh just by arriving.
  Keep existing budgets, pause/resume and cancellation. Failed latest activity
  read, known transcript read failure, missing evidence or invalid identity makes
  the current display unavailable. Clear transcript failure only on a successful
  current newest apply, not SSE opening. Do not invent browser/server clock order.
- Active transcript agrees with activity working/waiting, or unclassified with
  inProgress status. Idle transcript agrees with idle activity and terminal
  completed/failed/interrupted status (absent status allowed for empty/legacy
  feeds). Explicit contradictory activity state/status is unavailable. Active+
  idle and idle+inProgress remain unavailable in **either arrival order**, even
  with equal turn IDs. Do not choose a winner by response arrival.
- Unavailable uses the existing Activity unavailable presentation consistently
  across label/title/ARIA, suppresses current running counts and waiting duration/
  decoration, and freezes historical timing with its unavailable/partial marker.
  When consistent, retain existing Working/classified waiting/Idle/team behavior.
  An idle elapsed interval is idle, not active waiting. Unclassified stays explicit;
  team status cannot mask an unavailable selected member. No extra bar/redesign.

**Convergence without a new poller.** Fresh idle terminal activity with exact
nonempty matching thread/turn and positive completion time no later than its
observation may call existing `sync.scheduleRefresh(0)` once when the newest
transcript remains active. Consume one view-local binding/thread/turn/completion
marker before scheduling; do not key it on changing observedAt or add timers/
retry loops. Reset on binding teardown. This requests ordinary fresh transcript
proof, never sets Idle. Existing sync owns single-flight, dirty follow-up,
cancellation/retry and all normal read/application gates. Failure or continued
disagreement remains unavailable; identical completion polls do not cause more
reads. Reverse-order disagreement recovers through existing activity cadence/
focus. A different/newer turn cannot be hidden by an old completion. Missing
completion/turn evidence causes no added refresh. No replay/send/resume/restart.

**Acceptance/checks.** Extend the existing independent-feed browser fixture with
separate turn IDs/states and deferred responses. Cover active transcript then
idle completion, idle transcript then delayed in-progress activity, and both
convergence orders. Assert unavailable during disagreement and coherent final
label/elapsed/ARIA/classes; send/settings/interrupt gates remain unchanged until
their ordinary transcript path changes them. Cover newer turn, matching-ID busy
before persistence, legacy missing IDs, empty history, wrong thread/binding,
snapshot stale, expired/delayed read, latest-read failure, hide/resume and recovery.
Prove one completion invalidation, no repeated refresh after failure/conflict,
none from mismatched/missing identities, and no mutation from display projection.
Existing queue dispatch remains subject to its original gates.

Run focused syntax/presentation checks and the existing disposable independent-
feed browser test in the declared Nix environment, including representative Codex
and Pi behavior. The coupled team-activity fixture alone cannot prove ordering.
Lead allocates uncertain checks after I1 release; committed quick-checked changes
receive independent review before longer package/CI checks. No native campaign,
live probe or source change by architect. Portal assets work with retained workers;
rollback restores presentation without migration or receipt conversion. No new
merge/deploy authority. Screenshot-specific browser state remains unjoined.

## D7: deploy verified delivery and status fixes from feature heads

**Sufficient operations amendment.** The user's new "deploy it when verified"
authorizes deployment of D4's retained-session retry correction, D5's compact
shared delivery UI and exact provider pin, and D6's coherent display. It does
not explicitly authorize their integration into remote defaults. D2's prior
merge/deploy direction has already been fulfilled. Deploy reviewed feature heads;
do not merge any new provider/runtime/workspace/configuration default or acquire
a repository merge claim while waiting for separate integration approval.

I1 owns the minimal matching workspace/configuration pin package after D5's final
packet/capacity and I0's final D6 published head. Runtime currently
`96b00bd09ef0d07ec784b22a67492c0a40ff201e` contains D4/D5 above merged e61;
the target is its final reviewed D6 successor, not this interim head. Provider
`b67d86a889cf3ac88d78f03d2dcd5f061f95d0b2` is already selected by runtime's
Nix/Go/vendor inputs. Use fresh remote defaults for pin preparation, preserve
unrelated changes, and add one new pin commit per stream; never amend merged D2.
Workspace files remain `flake.nix` plus generated `flake.lock`, using the existing
nested `vpsfree-dev-workspace/dev-workspace` override/update command. Configuration
uses its existing `dev-workspace` channel, role `devWorkspace`, with confctl's
exact-feature `inputs channel set --commit` flow. No extension/configuration
feature change or system deployment is included.

**Provider-lock host decision.** Source inspection of e61 through 96b00bd proves
that only the root codex-web lock node changes: db792 to b67 (new NAR
`sha256-QezhmlDrsAPt860BSR5tj8HwLSvKn8Ji1gBVkL3OQpU=`). All other runtime input
nodes remain unchanged. Provider changes are shared browser assets, example cache
references, tests and reference prose; the native model catalog and Go/native
protocol source do not change. Runtime adds the D4 adapter correction, assets,
their tests/docs and vendor hash. D6 has no host dependency.

The actual dependency boundary permits reuse of D1/D2's host proof despite this
intentional root-lock change:

- `flake.nix` exports `nixosModules.host` by importing `nix/host-module.nix`.
  That module imports unchanged host paths and `pi-runtime-host.nix`. Its
  `pkgs.callPackage ./pi-runtime-host-package.nix` receives machine packages and
  owner UID/home/name/state root only. The package reads the two individual,
  unchanged helper/session-entry files; it does not consume codex-web, the root
  lock or the whole runtime source. The template and sudo rule depend on this
  helper and unchanged module options.
- Aitherdev's `config.nix` selects the native Codex wrapper through unchanged
  `lib.mkCodexPackage { pkgs; codex = llmAgentsPkgs.codex; }`. That function takes
  only those two arguments; no provider/root-source dependency is captured.
  The portal drop-in remains its two fixed Pi environment settings and preserves
  ExecStart. Provider source is used by the application package/catalog path,
  not these installed host prerequisites.

I1 compares fresh baseline Aitherdev role mappings/complete relevant locked input
closures and module/options/helper/Codex-wrapper source against the accepted D2
baseline. If unchanged, the above dependency proof reuses installed helper xhc71,
template 8q48, drop-in br5i, sudo bytes/order and native Codex proof without a
system evaluation/build. If a relevant baseline delta exists, name it and use
only the existing D1 targeted artifact/metadata comparison needed to decide
compatibility; return a real prerequisite change to lead before expanding scope.
Do not treat arbitrary root lock/node names as effective package proof.

I1's minimum comparison is the D2 `f618` workspace/`d822` configuration baseline
through fresh defaults and final pins. Compare runtime `nix/{host-module,host-paths,
pi-runtime-host,pi-runtime-host-package,codex-package}.nix`, the two
`libexec/workspace-pi-{host,session-entry}` files, and their flake export wiring.
Configuration evidence covers unchanged Aitherdev `module.nix`, `config.nix`,
`dev-workspace-site.nix`, selected import/module/overlay wiring, and root-role
closures for nixpkgsStable, home-manager, llm-agents and confctl. The runtime role
and its codex-web child are the intentional pin exceptions. Preserve owner
UID/home/group, enable/state-root values, helper sudo rule and wheel ordering,
the two-variable portal drop-in, and native Codex function arguments. Unchanged
owning source and complete relevant inputs prove these options without listing
or evaluating the entire system.

Prior proof anchor is this session's `D1-host-impact.json`, SHA256
`2af3ddc5149f6ace966a34eede6b975edce494f66eae72ba3e98fc427ee0ce68`, linked from
`rollout.md`'s Settled host route and carried forward by D2. It proves installed
Pi prerequisite equivalence, **not equality of the entire candidate system**:
the unrelated configuration baseline already selected candidate Codex 0.171
versus installed 0.170. Do not require that old excluded system candidate to equal
the installed wrapper, or switch it to obtain equality. Preserve installed native
Codex and prove D7 adds no new wrapper input change relative to D2. Fresh default
ce54d0c9 changes only geminabox Gemfile.lock/gemset.nix; I1 preserves it and checks
its exclusion from the above prerequisite dependencies. No new host inventory.

**Verification gate.** Final pins must pass the existing cross-lock checker,
normal pin quick checks and applicable final-series review. Preserve all source/
receipt/effect guards and the patched-SDK source realization prerequisite.
Lead then allocates the D2 composed `default` plus the same five checks:
`pi-runtime-composition`, `agent-team-policy`, `cluster-provider-composition`,
`tracking-source`, `deployment-contract`. Finish applicable exact-final-head CI.
Use the actual composed output, never the generic runtime result or old g7wv.
Retain final provider/runtime/workspace/configuration heads, source/input graphs,
app derivation/output and checks in existing rollout/review receipts. Confirm
canonical SDK/Node and unchanged worker modules/contract, native Codex package,
catalog, managed team/model/provider selections, extension and typed target/
legacy bridge metadata. The provider source delta and expected app/source/vendor
identity changes are explicit; D2 proof cannot certify the new application bytes.
No native run, profile, benchmark or whole-system check is added.

**Ordinary profile activation and recovery.** Reuse D2's procedure with a fresh
schema-2 machine claim for `vpsfree-cz-configuration`, selector
`cz.vpsfree/machines/aitherdev`, adapter `confctl`. Prepare builds/copies first;
verify the exact held target once for this committed batch. Lead runs ordinary
`workspace-host switch --source WORKSPACE_CHECKOUT` with its claim ID and exact
session/workspace identity. All installed transition, lifecycle, generation,
authority, cluster and recovery checks remain mandatory. Preserve selected system
and system profile k79 and the installed native Codex. No confctl activation,
system switch, worker upgrade/restart or session lifecycle action is authorized.

Before/after activation, use D2's bounded metadata-only continuity check for the
existing nine retained Pi unit/PID/start-tick/worker identities; report any actual
inventory difference rather than silently adopting or restarting one. Verify the
selected composed path, portal/router/coordinator health and existing three HTTP
routes, native Codex identity/settings, and unchanged system/host prerequisites.
Do not send test messages, create a session or retry any user's original input.
The portal retry/UI fixes apply to retained sessions without worker replacement;
they do not establish a screenshot-specific delivery outcome or reply completion.
Join all switch effects. An interruption follows the original forward recovery
target; no private helper, record rewrite or unsupported rollback is permitted.

After verified feature deployment the machine remains held because separate
default-merge approval and complete deployed-lineage proof are still missing.
Lead can present the concrete verified result and request that approval; hold no
repository merge claim during the wait. Once approved, integrate each final
deployed dependency through the existing short-claim procedure with fresh remote
ancestry evidence. Rebased successors require retained old/new equivalence proof;
substantive successors require their own verified deployment. When effects and
complete approved integration are proven, inspect the exact owned machine claim,
release promptly and verify released status. Session stays open. No independent
UI acceptance or extra release instruction is required after those gates pass.

## D9: creation CI duration, bounded evidence and next diagnostic

**Investigation complete; reduction implementation is not yet sufficient.** The
user wants the entire required creation check near five minutes, with ten minutes
an upper bound, not a per-shard figure. The current deployment keeps its existing
final CI gate. No workflow, test, source, CI run or live session was changed by
this investigation. Lead owns any separate implementation allocation.

Read only the owning workflow, `nix/tests/session-creation.nix`, its browser/model/
transport helpers, two successful job logs and one current job status. At the
status read, b0 run 45466397506/job 138702342143 remained in progress, creation
step started 19:05:06Z. Unavailable unpublished logs do not prove a stall, failure
or current-stage location. The owning fixture/workflow files are unchanged between
e61 and current b0, but prior timings are not measurements of b0's active job.

Successful baselines are e61 run 45414878045/job 138518268181 and b07 run
45407328539/job 138491452523. Complete logs are
`/tmp/pi-ci-duration-e61-138518268181.log` (SHA256 b1f1bfbde6806c1b75f34e52074f61f17d4b0eec9257fea8b6c00092599029ba)
and `/tmp/pi-ci-duration-b07-138491452523.log` (SHA256 d99fed73bfe3f786046a14833794ad782859007736fc5bda4ae24d9d71baa46e).
`/tmp/pi-ci-duration-summary.json` retains extracted subtest boundaries. The first
download was refused by gh's escape-sequence output guard and saved zero bytes;
explicit raw output then obtained these same two authorized logs. No third log.

| Elapsed stage | e61 | b07 |
| --- | ---: | ---: |
| Complete creation job | 35m59s | 35m13s |
| Nix creation step before VM derivation starts | 211.05s | 204.64s |
| VM script, including boot and evidence copying | 1936.17s | 1898.88s |
| Initial VM boot/user-unit wait | 15.20s | 15.77s |
| Shipped portal/native/provider setup subtest | 15.20s | 15.36s |
| Creation, naming, fork/plan, transport recovery and deletion subtests | 799.40s | 795.55s |
| Four maintenance bootstrap/pause/deadline/failure-recovery subtests | 913.11s | 885.86s |
| Pi creation/cold reconnect and final Codex usability subtest | 178.56s | 172.19s |

Rows within the VM are components of its total, not additional job time. Nix
fetch/evaluation/build overlap in their first 205–211 seconds, so these logs do
not justify independent additive fetch/build totals. Two application variants
build concurrently in about 50 seconds each, not 100 seconds on the critical
path. Boot and setup are small. Fast/archive jobs run independently: their elapsed
times must not be added to creation, and reducing creation does not make the
current roughly 19-minute fast job a five-minute whole-CI result.

**Actual expensive paths.** This is one sequential VM script with 19 subtests,
including setup. Maintenance cases take respectively 211/208 seconds (bootstrap),
177/179 (cooperative), 234/207 (deadline/Stop), and 292/292 (failed target/recovery).
The failed-target case is the longest stable individual scenario. Journal
timestamps show six portal stop intervals in e61 of 27.502, 26.625, 30.217, 29.923,
29.970 and 29.687 seconds; b07 has five comparable 27–30 second intervals plus
one 0.344-second stop. Native Codex stop intervals are below 0.3 seconds. The
portal delays account for about 174/144 seconds inside maintenance; they identify
a repeatable shutdown boundary, not its internal cause or permission to shorten
grace/kill contracts.

There are 23 serial browser CLI calls, totaling 837.00/826.53 seconds across the
suite, overlapping the scenario totals above. Ordinary creates/fork/plan commonly
take 50–60 seconds; retries/recovery about 39–43 seconds; finishing/reconnect about
30–36 seconds. Each invocation launches Chromium and runs real packaged UI/native
operations. Existing success output lacks phase durations, so launch/navigation,
creation readiness, hydration, follow-up and browser close cannot be separated.
The synthetic external model answers locally; logged naming examples complete in
hundreds of milliseconds. Model-catalog decode errors are visible, but no timed
span proves they dominate. Neither artificial slow inference nor browser startup
alone is an established explanation for all these seconds.

Maintenance status is polled through the ordinary public CLI 386/350 times,
consuming 334/313 seconds of command wall time while operations also run. Those
seconds are observation overlapping progress, not demonstrated avoidable delay;
removing polls or reading private records would not establish equivalent coverage.
The fixture's 300-second deadlines and 60-second barrier cap are bounds, not
fixed sleeps. Changing them is not a performance fix.

**Why a shard-only five-minute promise is unsupported.** Existing subtests share
the explicit source (fork/plan, initial-send proof, later usability), automatic
retained team (maintenance participants), before/after proxy roots (restored-client
and bootstrap proof), and alternating original/target package state. Concurrent
execution in the same VM would invalidate these contracts. Independent VMs would
need real creation/setup and package-state prerequisites repeated. Keeping the
observed longest scenario and preparation unchanged already gives roughly
8m17–8m23 before repeated setup; isolation could change that time and has not
been measured. Moving all four maintenance cases to one parallel job still leaves
about 15 minutes of serial work. Thus no sufficient shard layout currently proves
the five-minute target or even a safe full-coverage ten-minute completion. Do not
rename the slow work out of the required aggregate or report only a fast shard.

**Smallest sufficient next diagnostic package, if lead allocates.** One implementer
adds bounded success/failure phase timing to the existing fixture, only in
`test/creation_acceptance_browser.cjs` and `nix/tests/session-creation.nix` plus
their existing focused helper tests. Use monotonic clocks and existing operations:
browser launch/context, navigation/settings, admitted-to-ready, hydration,
follow-up and close; maintenance prepare, first observed phase changes, target
barrier entry/release and complete, with existing status-call count/duration.
Emit short phase/duration/outcome lines on success as well as failure. Retain
all current deadlines, assertions, public status calls, native identities,
independent receipts, no-replay and lifecycle recovery evidence. No added RPC,
retry, poll loop, private-state reader, production timer or profiling framework.
Record existing journal stop/start times alongside phases without changing them.

Focused tests verify timers finalize on success/error and existing assertion
failures still propagate; syntax/fixture checks precede review. Run the instrumented
fixture once only in a separately allocated verification milestone or its next
required CI, not by restarting b0. That result should settle the largest browser
phase and whether portal shutdown dominates a particular maintenance phase.
Then select one conventional correction at its owning boundary, or isolated
groups with proven setup/state independence. Measure complete creation elapsed
including all preparation, every required group and aggregate success; retain
both total work and critical path, with the near-five-minute goal and ten-minute
ceiling explicit. No promised speedup follows from current evidence. Current
deployment proceeds under its existing owner and gate independently of D9.

## D9-E: essential creation gate; extended lifecycle coverage is opt-in

**Sufficient for I0 release.** The user explicitly permits reduced coverage:
"test just essentials" and "implement it as you see fit... the goal is for the
CI to not take so bloody long. don't let this stop deployment of the feature you
have prepared however." This supersedes D9's full-coverage requirement and its
timing-only next package. Stop timing expansion; preserve the already saved
prototype patch and restore only I0's uncommitted timing changes before this
implementation. No production assertion, native contract or runtime guard changes.

I0 owns one focused package in `nix/tests/session-creation.nix`, `flake.nix`,
`.github/workflows/check.yml` and the existing README verification paragraph.
Keep `test/creation_acceptance_browser.cjs` and its helpers unchanged after
restoring the prototype unless a small existing consumer adjustment is necessary;
do not introduce timing rows, a parser framework or a second fixture. Lead owns
final prose, review acceptance and check allocation.

**One VM and shared existing fixture.** Add one explicit boolean fixture argument,
`extended ? false`. Keep the existing `checks.x86_64-linux.session-creation` as
the essential required check. Export the same fixture with `extended = true` as
`packages.x86_64-linux.session-creation-extended`, reached by
`nix build --no-link --print-build-logs .#session-creation-extended`. Deliberately
keep the extended derivation outside `checks` so ordinary flake checks and the
workflow's dynamic fast-check list do not accidentally rebuild the old campaign.
Use distinct test derivation names. Workflow display name/step must read
"Session creation smoke"; document the explicit output as "Extended session
lifecycle/recovery". The existing required creation job still runs the same
essential output command; no action-version or unrelated CI changes.

**Essential assertions.** Retain authentic shared package/host/native services,
authenticated Chromium, loopback synthetic external model and Pi TLS trust. Run
only two creation scenarios after setup:

1. Explicit-name/default-provider Codex Solo through the actual public form,
   accepted request/ready receipt, exact canonical document/native target,
   visible initial assistant reply, one usable follow-up and browser reload.
   Use existing `browser("create", "explicit", provider="primary")` and
   `proof("explicit", "primary")`. Retain independent native history, matching
   manifest/journal/completion identities, exact original-input count one,
   no orphan/duplicate native roots, submitted model/effort/instructions and
   default notification state. Attachments and their extra assertions are
   extended-only; the essential input is plain text.
2. Pi Solo public form, 202/ready/canonical page, exact scoped native UUID,
   visible original and assistant reply, one follow-up, browser reload and
   existing `pi_proof("pi-solo")`. Preserve independent stored original ref/
   Accepted witness joined to exactly one native history entry, correct
   backend/settings/role instructions, runtime/worker identity, host namespace
   and CA checks. Keep the existing strict TLS setup/probe and loopback-only
   provider fence; a cold portal restart, CLI worktree lifecycle, second Pi
   reconnect exchange and final repeated Codex exchange are extended-only.

Keep the full existing proof functions and failure propagation. Do not substitute
mocked native receipts or merely check a 200 page. No need to add another send,
retry, native prompt or comparison campaign. Basic initial/follow-up/reload reads
must retain original IDs and never replay the original message.

**Extended coverage retained, not deleted.** Guard the existing sequential middle
campaign and Pi's additional tail with the boolean. Preserve its original order,
dependencies and assertions: managed ascending-input proof, automatic/error/retry
naming, alternate providers, sensitive teams, attachments, forks/plans and settings
restoration, transport interruptions/lost replies/proxy-root recovery/deletion,
all maintenance bootstrap/cooperative/deadline/Stop/startup-failure recovery, Pi
CLI worktrees/cold reconnect and post-Pi Codex usability. The initial explicit
scenario enables its original attachment option in extended mode. Both existing
`finish explicit` calls that depend on planning/maintenance are extended-only.
Keep original/target package transitions wholly inside that mode, and include
`maintenanceTarget` in VM additionalPaths only for extended. Existing shared
helper definitions may remain; no costly refactor or independent shard project.
Success/failure evidence exports remain available for both modes. A tiny existing
success summary should identify smoke versus extended and the two completed
backend creation cases; missing either essential case must fail, not skip.

**Checks and timing.** Quick-check Nix formatting/evaluation and the generated
Python syntax for both modes; inspect/assert the exact selectors and that the
extended output is absent from routine check enumeration. Existing browser helper
checks stay applicable because their contract is unchanged. Review the committed
whole package and preservation of extended assertions before one actual essential
VM run under lead-owned verification. Do not run the full extended campaign just
to prove its export. The prior full passing source remains its baseline; its
mode-selected generated script must retain the old scenario sequence and checks.

Historical serial times suggest approximately 30 seconds boot/setup, 65 seconds
for the complete Codex case and roughly one minute for initial Pi creation/proof,
plus 205–211 seconds cold Nix preparation. This supports an initial estimate near
six minutes, not a verified five-minute result; the optional maintenance package
is also removed from essential preparation. Measure complete required-job elapsed
from setup through both cases/evidence, including fetch/build, with near five
minutes the goal and ten the upper bound. Use the actual essential run to decide
whether any further cost reduction is needed. No extra instrumentation campaign,
shortened contract deadlines, assertion weakening or per-shard metric substitution.

## D7 acceptance amendment: prepared feature deployment remains separate

The user's explicit reduced-coverage instruction and "don't let this stop
deployment of the feature you have prepared" remove the broad legacy creation/
maintenance job as a blocker for the already prepared b0 feature deployment.
Lead may deploy the unchanged reviewed b0 runtime, exact matching pins/composed
artifact on its passed fast/archive CI, source/browser checks and composed checks.
The still-active full creation job remains additional evidence; do not report it
as passed, cancel it, or imply the new essential test has run. D9-E is a separate
test/CI package with its own final review and essential-VM verification, not an
unreviewed change to the selected deployment candidate. Any actual failure that
arrives is assessed on its evidence, not suppressed by the scope change.

D7's profile-only switch, unchanged system/native Codex, frozen retained workers,
health/identity verification and ordinary recovery remain mandatory. This steering
still does not explicitly approve new default merges. Keep machine ownership
after verified deployment until separately approved complete lineage is integrated;
hold no repository merge claim while waiting for that approval. No new lifecycle,
worker upgrade, peer recovery or automatic deployment of the later CI package.

## D9-F: essential push checks and explicit extended verification

**Sufficient brief for one follow-up I0 package after D9-E (2392f0bf).** The
user's whole-CI goal and explicit coverage reduction supersede retaining all Ruby
and archive cases on every push. This changes verification selection, not runtime
contracts. Lead accepts/releases this package; no new work was assigned during
investigation. D9-E creation smoke stays independent and required. The deployed
b0 feature, pins, system and retained workers remain unchanged.

**Measured cause, one completed log.** Exact b0 fast job 138702341838 took
19m02s. Raw `/tmp/pi-ci-duration-b0-fast-138702341838.log`, SHA256
`247b1690d5bf6aeec6a1d4b318503284472b6393c39965b5625027a0fecf6430`.
No additional creation/archive log was requested.

| Boundary | UTC / measured elapsed |
| --- | --- |
| Pi patched-source preparation | 19:05:05.841–19:05:25.945; 20.1s |
| All-check evaluation without builds | 19:05:25.945–19:06:15.618; 49.7s |
| Last dev_session shard | 19:11:08.502–19:17:39.868; 390.673s reported |
| Complete Ruby aggregate | 19:17:39.995–19:17:40.122 |
| Checked app compilation | starts 19:17:40.232; about 59s |
| Checked app checkPhase | 19:18:39.932–19:23:54.831; 314.9s |
| Largest reported Go package | internal/web 243.867s; workspacecodex 86.485s |

`nix/workspace-portal.nix` embeds `rubyChecks.all` in the checked app's
checkPhase. Nix therefore cannot begin that derivation, including compilation,
until every Ruby shard has completed. Nine app derivations also build for
package/composition variants. Several overlap; their durations must not be
summed. Ruby's four dev_session shards report about 205, 207, 305 and 391 seconds;
the last begins almost four minutes after the first. Existing hash-based shards
are not duration-balanced. Scheduler contention is plausible, not separately
measured. Go package reports are buffered and package work overlaps. Source
preparation/evaluation is not the dominant cost; dependencies are fetched and
built, so a warm local run cannot establish cold GitHub duration.

Lead's completed-run receipt adds archive 12m34 and creation 49m21, all successful.
Those are independent job durations, not additive. Creation reduction alone
would leave the measured 19m02 fast floor. Moving archive to explicit extended
verification is therefore part of the authorized essentials decision.

**Owning files and minimum change.** I0 owns `nix/workspace-portal.nix`,
`nix/ruby-checks.nix`, `nix/tests/package-check-separation.nix`, `flake.nix`,
`.github/workflows/check.yml` and the existing verification documentation.
Use the normal source/index window after D9-E. No new test runner, CI matrix,
cache service, timing framework, production code, lock or native package change.

1. Remove only the full-Ruby dependency from checked package checkPhase.
   Keep all `go test ./...` packages, positive/negative auth, receipt, cache,
   admission and input contracts, existing Go test options, Node checks,
   checked assets, pin and protocol checks unchanged. `doCheck` now means the
   application checks; full Ruby remains its explicit existing check output.
2. Keep every current Ruby shard and `ruby-verification` accessible. Add one
   small essential aggregate using the existing `check_ruby_shards.py` and
   existing whole single-shard suites: workspace_host, coordination_claims,
   machine_identity, coordination_admission and integration_certification.
   Export it as `ruby-essential-verification`. Do not filter individual test
   methods, change shard assignments, or label that subset full Ruby coverage.
   Both aggregates must retain complete unique coverage for their declared
   suites; full aggregate still includes all original suites/shards unchanged.
3. Required fast job is named **Essential application contracts**. Build the
   checked `package`, `ruby-essential-verification`, `package-check-separation`,
   `codex-package`, `pi-worker`, `pi-runtime-host-unit`,
   `pi-runtime-host-environment`, `ruby-source-filter`, `host-module`,
   `host-auth-benchmark`, `host-package-contract` and `generic-source` together
   in one Nix invocation. Keep ordered Pi source preparation and unchanged
   all-check `flake check --no-build`. No dependency on creation or extended jobs.
   These targets preserve the existing quick host/identity/admission contracts;
   a selected missing check must fail rather than silently disappear.
4. Full Ruby, extension-catalog, agent-team-catalog and user-namespace package
   variants move to an explicit **Extended Ruby and package composition** job
   on workflow_dispatch. Build existing full `ruby-verification` and those three
   existing checks; no assertion deletion. Archive becomes **Extended session
   archive/recovery**, dispatch-only, retaining its exact existing check command.
   Host VM lifecycle coverage becomes explicitly dispatched **Extended host
   lifecycle**, retaining all three original host check commands. Keep every
   check output and the normal full `nix flake check` available; required push
   coverage is the named essential job plus D9-E **Session creation smoke**.
   No path-filter framework or per-shard success substitute.

**Coverage and compatibility contract.** Document exact manual commands, including
`nix build --no-link --print-build-logs .#checks.x86_64-linux.ruby-verification`
and the unchanged archive/host/composition selectors. Full Ruby and relevant
extended VM/composition checks remain required before integrating changes to
session lifecycle/collection, host activation, recovery, coordination ownership
or package composition respectively. Portal auth/input/receipt changes retain
all application tests on every push. Ordinary UI pushes no longer imply a broad
native lifecycle campaign. Formatters and commit hooks remain required. Update
package-check-separation's old Ruby dependency assertion to require its absence
from both checked packages, while preserving production/test isolation, checked
assets and application command assertions. Its actual-workflow selector check
must prove the exact essential target set, complete existing extended exports,
and absence of full Ruby/composition/VM targets from routine builds. Merely
changing an expected string without preserving these checks is insufficient.

**Acceptance and checks.** Quick Nix formatting/evaluation and the existing
package-check-separation check establish both selected sets and dependency
separation. Verify essential/full aggregate inputs against existing suite names
and preserve the unsharded diagnostic mode and shard validator unchanged. Review
the final combined D9-E/F commit series before the already planned essential VM
and one fresh exact-head CI run; use that run's existing timestamps for total
required-pipeline elapsed and each required job. Do not rerun old b0 or run the
full extended matrix solely to demonstrate its invocation. The old complete
passing source is its baseline; changed aggregation/selector checks are affected
quick verification. Failures remain failures and must not be relabeled optional
within a selected job.

**Target and limit.** Aim for creation smoke and essential application checks to
finish near five minutes in parallel. This evidence does not promise that result:
the old application checkPhase alone took 5m15 plus compilation and cold setup.
Removing Ruby serialization and the additional composition builds removes the
known long chain and competing work, but cold package preparation and unchanged
Go web work may still exceed five minutes. Measure complete required CI elapsed,
including setup, builds, both jobs and success, not the shortest job or a warm
local check. If above target, report the remaining measured phase before another
package; do not weaken auth/receipt assertions or shorten contract deadlines.
No new deployment is needed for this CI-only package; rollback restores selectors
and dependency wiring without persistent-state effects. No default merge or
machine release authority follows from this brief.

## D11: retire delivery status once its exact input appears in the transcript

**Sufficient for lead release to I0.** The user clarified that the message was
already delivered and answered: the remaining status bar is the problem. This
closes the native delivery investigation for the identified current row. Scope
is display retirement only, shared by the provider and portal consumers. No new
native diagnosis, input, resend, receipt mutation, timer or queue implementation.

**Evidence and limits.** Four bounded public GETs succeeded and all clients joined.
The exact current body scope/native identity matched collection, activity and
transcript. The sole sent row's original ID and receipt turn joined the transcript
user entry and associated assistant entry, and matched latest/current turn identity.
Activity was idle/completed. Admission to turn start was 1.616 seconds and to
completion 15.503 seconds; this is one historical exchange, not a general latency
claim. The public transcript's original ID is attached through the supervisor's
owned accepted-input witness, matching native user entry ID and digest, rather
than a text comparison. No independent native-history read or new native effect
was performed. Screenshot identity remains unavailable, but the user has now
confirmed the completed exchange was overlooked. Identifying evidence stays in
an ignored, untracked mode-0600 own-session file; no peer identifiers or message
content belong in tracked records.

The source defect is independent of screenshot identity: inputdelivery Store.list
returns open rows plus the latest 100 terminal rows. Shared deliveries.js renders
every returned row and removes only IDs absent from the collection. Neither durable
consumer observes rendered transcript messages. A historical answered Accepted row
can therefore remain indefinitely until displaced by newer terminal records.

**Owner and files.** One implementer owns the complete package after the accepted
D9 source/index release. Provider: `conversation/assets/deliveries.js`, its existing
unit/mounted-consumer tests, and `conversation/assets/conversation.js`. Runtime:
`portal/internal/web/static/app.js`, existing focused delivery browser fixture,
and a short owning portal-guide correction. Include necessary existing asset
import/cache versions, standalone example version assertion, and the normal exact
provider Go/Nix/vendor pin flow. Reuse D5's shared renderer, styles, labels and
focus behavior; no copied portal-only filtering implementation or backend change.
Lead owns final prose, Git/pin sequencing and later deployment authorization.

**Small shared interface.** Add one display-only observation method to the mounted
delivery view, for example `observeTranscript(entries, scope)`. Reuse existing
validated transcript application sites; do not add a separate history reader.
The method accepts observations only for the mounted collection's exact scope,
while its existing `isCurrent()` guard is true. The consumer must already have
accepted the page for its current native/thread binding and generation and applied
those entries to its current transcript. Ignore paused, aborted, stale, foreign,
failed or not-applied reads. A collection alone, activity alone, identical text,
timestamps or an assistant response alone cannot supply this observation.

Retire a row from this view only when its validated state is `sent`, its receipt
original ID equals the row's original ID, and an applied `userMessage` entry has
that same nonempty original ID and the matching receipt turn ID. Do not hide
another same-text message, or a different receipt tuple reusing an ID. No need to
infer completion: once the actual input is in the conversation, native transcript
and activity already show subsequent work or a reply. This changes no meaning of
Accepted and makes no promise of assistant success.

Retain observations in memory for this mounted scope; no localStorage or
sessionStorage change, codec migration, new poll or expiry. Clear observations
on destroy/rebinding. A reload reconstructs them from its normally loaded valid
transcript. Handle both arrival orders: transcript before collection and collection
before transcript, including initial load and immediate POST presentation. Reuse
the consumers' already applied transcript snapshot when collection metadata first
arrives, and observe again when valid transcript pages are applied. Do not fetch
older history to clear a row. An already observed same-tuple sent row stays hidden
across ordinary polls and POST/read ordering. A newly returned non-sent state or
changed tuple remains visible; observations never hide queued, dispatching,
pending, not_sent or unknown records, including retired unknown records.

**Consumer seams and authority.** Portal's existing `renderThread` /
`observePageReceipts` path already has current-thread, page-current and Pi scope
checks; attach the durable observation after the current page is accepted/applied.
Provider's mounted `renderThread`/history application has the corresponding
current-page guard. Both pass the exact collection scope and only their current
applied transcript. Keep the full unfiltered validated collection for onMetadata,
selection checks, sender admission/recovery and subsequent refresh. Filter only
visible status rows. Preserve existing single-flight reads, POST generation/dirty
rerun, errors, settings and selection guards. No sender-store remove, native
acknowledgement, delete/drop endpoint, lookup POST, new HTTP call or replay is
part of observation. Legacy outbox observation remains unchanged. Terminal rows
whose input is outside loaded history may remain visible; manual dismissal is
not necessary to fix this proved case and is deferred to avoid another state
mechanism.

**Acceptance and verification.** Existing shared tests cover exact match removal,
same text/different ID, missing/foreign scope, wrong turn, invalid/changed receipt,
all non-sent states, read failure, destruction, stale POST/GET generations, both
arrival orders, reload-style initial collection/history order and a successful
retained row not returning on the next poll. Assert metadata still contains the
row and observation issues zero requests/writes/sender mutations. Exercise both
actual consumers, not just a copied predicate. Keep action focus for surviving
unrelated rows and hide the empty panel without introducing a new live region or
completion announcement. Use the existing targeted portal browser fixture for
sent row -> exact applied user entry, with unknown/queued controls remaining
visible and send gates unchanged. First run the existing provider/mounted and
runtime source-level quick tests plus formatting/pin checks. After final committed
combined review, lead allocates only the affected browser check/required final CI;
no native replay, peer probe or new lifecycle campaign. This package does not
restart or upgrade workers. Recovery is reverting UI/provider selection; stored
receipts and runtime state are untouched.

D11 implementation clarification: the shared provider can accept a different
thread in an existing mounted history, while the delivery collection remains
pinned to its first scope. Give the new observation method a stable thread-ID
argument, passed by both consumers after accepted synchronous application. Pin
its first valid nonempty thread with the collection scope. An actual current
thread change clears observations and disables retirement for that old mounted
binding; raw status rows are visible again. Do not adopt another thread under the
old scope or destroy/remount the sender/view as part of this small change. Existing
unmount/new mount establishes the new binding. Same-thread history reset/repair
preserves positive observations. Invalid/foreign/stale calls neither establish a
binding nor erase valid observations. After a read error, a previously proved
same-tuple sent row remains hidden; the existing refresh error is shown and no
new observation is inferred. Unknown/non-sent/changed tuples remain visible.
These rules affect display filtering only, not existing metadata or effect gates.

## D10 output-only timing clarification for the next required D11 CI

The sole saved c8 fast log contains 23 Go package result lines, zero verbose
per-test results and zero per-test JSON events. It establishes package totals,
not which cases account for web's 240.598 seconds. Do not select coverage cuts or
attribute that time to individual fixtures from the package total.

**Sufficient tiny change, only if lead includes it in I0's current package.** In
`nix/workspace-portal.nix`, change the existing command from `go test ./...` to
`go test -json ./...`. Update the owning exact command assertion in
`nix/tests/package-check-separation.nix` to that same string. Preserve every test,
package, GOFLAGS/vendor setting, checkPhase environment, assertion and exit code.
Use Go's direct output: no pipe, tee, filter, parser, timing helper, extra run,
count/cache/timeout/parallelism change or new workflow step. This affects check
output only; production package behavior and selected deployment are unchanged.

The existing Nix sandbox and temporary fixture HOME remain the privacy boundary.
JSON emits successful test logs as well as outcome events; fixtures stay synthetic
and no live session, credentials, transcripts or new environment access is added.
Retain the ordinary CI log rather than adding uploaded body/debug artifacts.

The existing quick package-check-separation assertion verifies the intended
command; ordinary final review covers the two-line change. The next already
required exact-head D11 CI supplies the only execution evidence. Its standard
Go events with Test/Elapsed identify actual case durations, including failures;
package events and existing Nix phase timestamps preserve the overall critical
path. Later analysis must not add overlapping packages or parent/subtest elapsed
times. No extra local Go/VM campaign is needed for this output change and no
five-minute outcome is promised. If including it would delay the status fix,
leave it for the next otherwise required check instead.

## D12: successful deliveries leave the status list without browser memory

**Sufficient for lead release to I0.** Lead accepted the material decision: this
list represents outstanding or actionable delivery statuses. A validated `sent`
record no longer belongs in its persistent presentation, regardless of loaded
history. This supersedes D11's transcript-observation retirement mechanism. It
neither claims assistant completion nor changes what qualifies as native acceptance.
One implementer owns the complete provider/runtime follow-up; preserve all merged
history and add normal focused commits. No new browser storage, server write,
acknowledgement endpoint, tombstone, expiry timer, history scan or native action.

**Source diagnosis.** At provider 30bf3636 and runtime d15735fa, the view's
`observed` Set is local to each mount and is cleared by destroy. Reload starts
with no observations; only applied history pages add matching original/turn IDs.
Thus messages outside the initially loaded page reappear until scrolling loads
them. Runtime Store.list still returns open records plus the latest 100 terminal/
retired records, and piLocalDeliveries copies them to the provider. The shared
HTTP handler validates and publishes them unchanged. This explains both why the
browser forgets and why the server returns the old notices. The source-only
investigation made no peer, native, CI or network requests.

**Owning interface and implementation.** In `codex-web/conversation/deliveries.go`,
keep the full existing provider collection validation first: scope, version,
count limits, all states/receipts, unique IDs and outstanding count. Only after it
passes, publish a copy of the collection whose entries exclude exactly
`State == "sent"`. Preserve order, non-nil empty entries, settings, scope,
selection, delivery modes and canEnqueue. Do not mutate a provider-owned backing
slice or suppress malformed sent rows before validation. This is the common
HTTP presentation boundary for every DurableDeliveries provider; do not add a
Pi-only duplicate filter or change the store's retention/query/dispatcher logic.

`GET deliveries/:id` and `POST deliveries` continue returning complete validated
statuses, including sent receipts. Same-ID same-wire POST remains create-or-get;
changed wire still conflicts. The stored original, native witness, attachment
references and duplicate-suppression identity remain untouched. A missing row in
the collection is never proof of non-delivery or permission to resend. Selection,
authentication, host authority, locks, receipt validation, enqueue limits and
native dispatch/recovery remain unchanged.

In shared `conversation/assets/deliveries.js`, filter every validated sent row
from rendering, including `present(sent)` after a POST and collections from an
older server. A queued/pending card transitions out immediately upon a validated
sent result, even if the following collection refresh fails. Keep all other
states, including not_sent and both ordinary/retired unknown, with their existing
actions and error behavior. Do not weaken validation because the row will be
hidden. Preserve full metadata delivered by that server to onMetadata, single-
flight reads, POST-generation fences, dirty rerun and surviving action focus.
Do not change the existing bounded retention of other historical records.

Remove D11's observed-ID Set, transcript binding/retirement-disabled state and
matching/filter logic. Remove the now-unnecessary observation helper/calls from
both `conversation/assets/conversation.js` and runtime
`portal/internal/web/static/app.js`; ordinary transcript/legacy receipt observation
continues unchanged. Keep at most a trivial documented `observeTranscript`
no-op returning false on the mounted view for compatibility with already shipped
consumers or cached assets calling that public method. It holds no observations,
validates no transcript and drives no request. New consumers do not call it.
Keep deliveryStatusPresentation and wire state/receipt validation compatible;
removing the notice does not remove the sent state from the protocol.

**Files and package boundary.** Provider owns the handler, shared view and mounted
consumer above, `conversation/deliveries_test.go`, existing delivery/mounted-browser
contract tests, and the owning `docs/reference.md` delivery section. Runtime owns
removal of its observation call/helper, a focused existing HTTP inbox regression
in `portal/internal/web/pi_input_delivery_test.go`, the existing message-delivery
browser fixture and the short `docs/workspace-portal.md` status paragraph. Include
only necessary existing asset import/example cache-version updates and the normal
exact provider Go/Nix/vendor pin update. Lead owns final user-facing prose and
publication/review/pin/deployment sequencing. No native, worker, store schema,
selection catalog or host-helper changes are needed.

**Compatibility and recovery.** This is a smaller collection view under the
existing at-most bounds, not a deletion or new state. New server plus old client
omits historical successes; old client may briefly present a successful POST
until its next collection read. New client plus old server validates but does not
render sent rows. Both current consumers use POST/exact-ID contracts for original
request recovery, not collection membership. Frozen workers and legacy outbox
paths retain their existing behavior. Reload/new tabs need no stored seen marker
and no earlier history page. Rolling back presentation can show old notices
again, but cannot lose a receipt or replay input. No migration or retention cleanup.

**Acceptance and quick checks.** Extend existing tests, rather than introducing
another harness:

- Generic HTTP collection with all supported states omits only valid sent rows;
  malformed sent receipts, duplicate IDs, wrong scope and original count limits
  still fail. Provider input slice and metadata are unchanged. Exact-ID GET and
  repeated same-request POST still return the original sent receipt.
- Existing runtime fake-backed HTTP fixture proves accepted originals remain in
  the store and recover through direct GET/repeated POST after collection omission,
  with zero additional native sends, enqueue or worker starts. Unknown/queued/
  pending/not_sent remain present; no database bytes/authority are rewritten by
  a list read. Reuse its existing receipt fixtures and assertions.
- The decisive regression has two sent records whose exact user entries are older
  than the initially loaded history. On a fresh mount both notices are absent
  before any older-page read. Load older history, destroy and recreate the mounted
  consumer with all browser observation state discarded, and repeat: neither
  notice returns. Exercise both actual consumers. Also supply an older-server
  collection still containing both sent rows to prove mixed-version behavior.
- Verify immediate queued/pending -> present(sent), late older GET, failed next
  refresh, empty-panel/error visibility, same-text unknown/queued controls and
  a later distinct input. No transcript match, completion guess, automatic history
  request, localStorage/sessionStorage write, retry/drop or extra POST is allowed.
  The compatibility no-op must not alter presentation or trigger work.

Run focused provider Go HTTP contracts, existing Node/mounted-consumer tests,
focused runtime HTTP tests, and formatting/pin checks before final independent
whole-series review. Lead allocates the affected existing browser regression and
ordinary exact-final-head CI afterward; no native delivery/performance campaign
or peer reproduction is part of this package. The browser regression must fail
against D11's fresh-mount/history-limited behavior. Report real checks and mixed-
version limits; do not call a retained receipt deleted or an accepted input a
completed assistant response. Package contracts are settled; no remaining design
blocker.

## D13 — held callback diagnosis and recovery boundary

Status: bounded diagnosis accepted; recovery design remains blocked on a supported
settlement operation. No implementation or operational mutation released.
Private peer identities, content and receipt evidence remain outside this file.
The four permitted public reads completed; no further live requests are needed
for the source-design continuation.

The owning contract in `docs/pi-runtime.md` (Host callbacks) sets a 30-second
callback deadline. After forwarding, cancellation, disconnect or an unknown reply
preserves Unknown and durably holds the originating conversation. Domain stores
own idempotency; there is no callback ledger or automatic replay.
`piruntime/callbacks.go` records `forwarded callback outcome unknown` and invokes
the worker hold. `conversation.go` refuses new input while either the saved hold
or in-memory callbackUnknown remains. SDK idle and an aborted assistant entry do
not settle the host effect. A missing exact submission record does not prove
nondispatch. Team initial-assignment reservations and native submission receipts
are separate authorities; a conflicting reserved ID cannot be substituted for
the callback's original ID.

The inspected public recovery paths do not clear this independent callback hold.
Ordinary runtime upgrade requires settled idle members; unknown-input retirement
explicitly refuses independent callback holds. Terminal callback retirement is
owned by archive/delete, not a resume mechanism. No supported command can safely
be offered to restore sending from the presently established evidence. Do not
edit private records, clear worker flags, replay the callback, replace its ID,
restart the frozen worker or use lifecycle as a workaround. A portal update does
not replace the retained supervisor or add an operation to it. A future positive
domain receipt alone would not clear the existing in-memory and durable holds.

There is also an independent presentation defect: the fresh matching transcript
can say `held`, while `projectActivityDisplay` admits only active/idle agreement
and maps held plus unclassified activity to unavailable. Send correctly remains
disabled through selection/admission and transcript readiness. The historical
aborted assistant row is native history, distinct from a current HTTP read error.
A minimal eventual UI correction can consume the existing held transcript state
and show an on-hold/input-blocked explanation in the existing activity and
`message-input-status` elements. Preserve thread/turn/binding/freshness fences;
failed or stale reads remain unavailable, unclassified timing is not idle, and
no display result changes readiness or clears an effect guard. Do not invent a
specific callback reason from a generic held status or expose private arguments.
This presentation correction cannot restore sending and is not task completion.

D13-R is a source-only feasibility continuation: prove whether the existing
immutable domain reservation can establish nondispatch for an exact conflicting
callback, and whether an ordinary reviewed upgrade/recovery boundary can replace
a frozen held supervisor only after positive domain settlement and all-owner
native drain. No source implementation, tests, builds, CI or live effects are
part of this design step. Lead owns any consequential scope/operational decision;
I0 owns any subsequently released complete implementation package.

### D13-P — sufficient independent prevention package

User steering removes the independent UI option above from active scope. The
required outcome is safe continued team delivery and recovery, not different
status wording. This package prevents one established false-Unknown path; D13-R
remains necessary for the already-held retained case.

Owner after lead release: I0. Files: `portal/internal/web/pi_teams.go`, its existing
`pi_team_add_test.go` fixture (and its fixture helper only if needed), and the
Host callbacks/team delivery paragraph in `docs/pi-runtime.md`. Keep the short
source/index window exclusive to I0. No provider/browser/worker/pin/CLI changes
are required for this package.

The deterministic defect is that `WithDelivery` marks the invocation
`piTeamUncertainEffect` before `ReservePiInitialAssignment`, including its pure
immutable-ID conflict refusal. `preSendRefusal` then deliberately declines to
certify no effect. The host handler returns an error and AttachHost converts it
to transport Unknown; the supervisor conservatively holds the caller. This is a
source-proven adverse path, not a claim about which historical transport event
occurred.

Smallest repair: in the existing creating-member branch, after validating and
selecting the current roster member and BEFORE ready-proof collection,
reservation or any materialization attempt, reject a nonempty InitialInputID
which differs from this exact message ID. Set the ordinary stage to
`initial_reservation`, keep `piTeamNoEffect`, and return the existing
`teamruntime.ErrPiConflict` (alias of `piruntime.ErrConflict`). The existing owning
`piTeamPreSendRefusal` then certifies materialization `unattempted`; the host
handler returns its normal `HostReply{Outcome:"result"}` and nil transport error.
Reuse that interface; do not add a generic catch-and-ignore error conversion.
The reservation method retains its authoritative conflict check for all callers
and races. Its effects remain conservatively unknown if reached without this
positive precondition. The precheck is stable because nonempty initial ID and
member incarnation are immutable and ready cannot return to creating; no state
write or receipt absence is used as proof. Cancellation still preserves Unknown.

Same-ID requests follow the original reservation/materialization/native lookup
path unchanged, with exact body/action/settings equality and native no-replay.
Empty reservation, wrong identity, stale generation, unknown creation/write
outcome, actual Send entry and cancellation keep existing refusal/Unknown rules.
No missing receipt implies nondispatch. No existing hold is reset. The standard
result reply already works with retained supervisors, so this portal-side fix
benefits future callbacks from existing unheld sessions without worker upgrade.

Acceptance: reproduce old error -> Unknown for a creating target with a different
immutable initial ID; after repair the actual team host handler returns the
bounded existing pre-send result with zero reservation writes, zero Create,
zero Send and unchanged roster/binding/receipts. Cover both original UUID and
compact original caller input, same-ID retry, empty reservation, and cancellation.
Retain the existing policy-held/created-empty, uncertain creation and Send-Unknown
cases. Prove genuine uncertainty is not relabeled and ordinary valid result
replies do not set the supervisor callback hold using existing transport tests.
Run the focused web/teamruntime/callback tests plus formatting and required hooks;
no live peer reproduction. Commit and independently review normally. No extra VM
or native campaign is justified for this result-classification change. Lead
owns publication/deployment and operational scope. This brief is sufficient and
independent of the unresolved legacy recovery transition; it does not complete
restoration of the already-held conversation.

### D13-R — sufficient bounded recovery contract, pending lead release

This is a proposed supported extension, not a command present in the deployed
package. It is limited to a held team callback whose initial-assignment conflict
can be positively settled, with any materialized creating recipient positively
proved empty. It does not recover arbitrary unknown host operations. The actual
conversation is eligible only if the operation's complete preflight passes;
existing bounded evidence is not a substitute for that proof.

**Owner and interface.** I0 owns the complete dependent runtime package after its
D13-P commit/index window closes. Extend the existing private operator upgrade
route and `workspace-portal pi-runtime upgrade` command with mutually exclusive
`--recover-team-conflict <original-team-message-id> --member <sender-address>`.
Keep the ordinary request UUID, expected predecessor generation, workspace,
slug, socket and Origin arguments. HTTP uses `recoverTeamConflict` plus `member`;
reject mixing it with unknown-input retirement. The server derives native
origins, target, message bytes, package/profile and complete member set. The user
never supplies replacement text, an assumed outcome, a clear-hold boolean or a
subset of owners. The result adds disposition `recovered-team-conflict` with the
selected original ID; retain explicit CLI validation for ordinary and input-
retirement replies. This mode grants no Send/Create/Configure or team mutation.

Add one operation-specific manager request/proof path beside `upgrade.go` and
`input_recovery.go`, not a callback replay service. The upgrade hook obtains a
short-lived typed team settlement proof from the owning web/teamruntime code.
It contains exact session/runtime generation, original caller/input/origin,
argument digest, recipient incarnation, roster/binding revisions and digest,
settlement kind and exact receipt/native witness or immutable conflict evidence.
Only the owning verifier constructs it. An error string, Native toolResult text,
operator assertion or missing file cannot construct a positive proof.

**Read-only preflight before reservation or Stop.** Under the existing selected-
package/transition admission and exclusive session runtime ownership:

1. Capture the complete current roster, binding, authority, original creation/
   addition selections and all mapped member/utility/resource owners. Require
   exact predecessor/generation. The selected sender has exactly the known
   forwarded-callback hold; other independent holds, pending settings/policies,
   unresolved native inputs or active utilities/resources refuse. Snapshot each
   loaded member with the existing old protocol; require matching identity,
   settings, instructions and not busy. Do not interpret held Idle=false as
   native quiescence proof.
2. Capture each held member's complete stable linear native history and all
   original Accepted input witnesses. Extract every potentially forwarded host
   call, not only the selected last error. Require unique native tool-call IDs,
   exact original input joins, unchanged before/after history hashes and an
   independent existing `InspectNativeOrigin` read for exact anchor/tool/arguments.
   That old public reader permits held persisted conversations. Reuse/extract
   the read-only capture logic already used by lifecycle, keeping its existing
   checks; never invoke terminal retirement or its authority. Every non-host
   native tool invocation must have its unique persisted terminal tool result.
   Unsupported host domains or an unjoined invocation refuse this narrow mode.
3. Settle every captured team call through its existing domain. An exact
   Accepted submission requires full immutable envelope/action/settings/digest
   match and independent native witness verification through the existing
   creation/history reader. A durable NotSubmitted receipt requires its complete
   valid immutable original and no witness. Pending/Unknown/dispatching,
   malformed/mismatched receipts or unverified acceptance refuse.
4. For a missing team submission, accept only one of two positive proofs. A
   still-creating target with the same member/incarnation and a different nonempty
   reserved initial ID proves the callback could not pass reservation: SavePi
   never changes a nonempty initial ID or reverts ready to creating; AppendPi
   preserves old members and RemovePi retains addresses as tombstones. Verify the
   retained source contract and exact current binding rather than trusting a
   timestamp. Alternatively, the call is exactly the reserved initial ID and
   its target passes the positive created-empty proof below. In that case only
   initialization is settled; the assignment remains unsent. These rules never
   infer nondispatch from missing receipts. Require at least one captured call
   matching the operator's sender/original ID and the immutable-conflict kind;
   duplicate occurrences must agree on full immutable content and target.
5. For each mapped creating target, preserve its existing ID and reservation.
   Require its exact saved creation ID, initial settings/instructions/policy,
   current generation, no pending/held state, no submissions and no persisted
   history, PLUS existing `VerifyCreation(..., nil)`, matching nonbusy snapshot
   and existing workflow observation with actual Idle=true. The last two absence
   checks are integrity constraints on a positive native empty proof, not effect
   evidence by themselves. Other creating forms refuse. Unmapped untouched
   reservations retain ordinary upgrade rules. Prove all other loaded members
   ordinarily idle; no extra live owner may be omitted.
6. Recheck roster/binding, all exact mapping bytes, history hashes, receipts and
   runtime identity after native reads. The exclusive session owner fences team
   domain writers; preflight failure leaves all original state untouched. Read
   methods must not request input, repeat a callback, publish readiness or repair
   an initial assignment.

These proofs are constructible with the retained public reads: InspectNativeOrigin,
VerifyCreation, snapshot, workflow observation for the nonheld empty/ready owners,
and exact stored domain records. The held caller's idle aggregate is deliberately
not used. Complete native tool-result coverage and settled host domains precede
host replacement; physical process/resource drain is established after Stop.
If any required origin/domain/native evidence is unavailable, return that exact
blocking stage. Do not weaken this predicate to make a particular session pass.

**Sealed upgrade and crash recovery.** Use the existing upgrade request ownership
and successor reservation. Add one bounded private operation journal keyed by the
upgrade request UUID (for example `team-conflict-recoveries/<request>.json`),
mode0600 and the normal strict codec/fsync rules. Store source and successor
Start/runtime identities, mode/original selector, exact roster/binding and member
before-image hashes, history captures, settlement proofs/digests, target package,
phase and exact host terminal observation. Message bodies remain in their original
histories/receipts. This is an upgrade journal, not a new domain delivery ledger.

After complete proof, durably save preparation and reserve the exact successor
using existing ordering/fencing; repeat the snapshot/proof identity checks before
any effect. If interrupted between reservation and journal publication, the same
UUID must identify the matching preparing successor and reconstruct only the same
preflight, never choose a new target or infer Stop. Retain both package roots.
Use the existing exact host Stop operation on the predecessor and require its
matching terminal receipt plus positive cgroup/process drain. Never ask the old
supervisor to clear a latch or add an unsupported RPC. Recheck stable final history
and exact domain/mapping bytes after Stop before marking the journal settled.
A lost Stop reply resumes by inspecting that same host operation; no arbitrary
kill/restart or terminal-lifecycle helper is used.

Only after that durable settlement may the manager write the existing mappings
as unloaded and clear exactly the captured forwarded-callback hold. Preserve
native ID, history bytes/ref, creation ID, settings, instructions, policy, original
receipts and initial reservation. The journal retains the original hold/before
state. The old process must already be positively gone, so its in-memory latch
cannot race this change. Resume existing successor Ensure/Load/attachment and
publication. Load persisted histories unchanged; load proved-empty members with
the existing EmptyProven path and the SAME native ID, without a synthetic input.
Reverify empty/idle status afterward. Keep their binding/roster state creating
and their reserved initial ID; they do not acquire a native input receipt or
ready publication. Extend the upgrade projection to carry proved retained-empty
owners separately from ready members, without weakening ordinary projection.
Publish new authority only after all owner/history/settings proofs pass.

Before preparation, failure has no effects. After preparation, failure retains
the exact pending operation, package roots and fences for same-UUID retry. After
Stop, never revive the old process or roll back to an unproved hold-free mapping.
After partial mapping/start/publication, compare each original or expected after
image and resume idempotently; foreign changes refuse. Do not rewrite receipts.
No automatic compensation may send the original assignment, clear another hold
or discard the journal. Completion requires ready successor and exact authority;
a lost final response returns that same completed operation after revalidation.
Old input-retirement journals and ordinary upgrades remain byte/behavior compatible.
A selected older package cannot finish an in-progress new recovery; retain/use the
recovery-capable selected package until completion. No general migration is needed.

**Files and checks.** Runtime ownership is `piruntime/upgrade.go`, one adjacent
team-conflict recovery implementation/test, and only necessary shared read-only
capture helpers from lifecycle/input recovery; keep lifecycle mutation paths
unchanged. Web owns `pi_runtime_upgrade.go`, team-domain proof helper beside
`pi_teams.go` and tests. Session owns the narrow retained-empty upgrade projection
in `backend_publication.go` and tests. CLI owns `pi_runtime_upgrade.go` and tests.
Update `docs/pi-runtime.md` with this exact supported recovery and refusal path.
No browser/provider/native worker/host-helper change or callback ledger.

Quick acceptance must include a faithful old-protocol fake that rejects any new
RPC: held sender, exact original native origin, a different immutable reserved ID,
positively initialized empty recipient, zero extra inputs and preserved identities.
Prove all three settlement kinds, original same-ID/body matching, complete history
and tool results, and negative wrong/changed target, reused ID with changed body,
missing origin, corrupt/Unknown receipt, ambiguous history, unrelated callback,
active tool/resource/utility, nonempty creating target and independent hold.
Checkpoint failures at preparation/reservation/Stop response/drain/journal/mapping/
start/publication; same UUID must recover once, changed UUID/content/package must
refuse, and all receipt/history bytes remain unchanged. Test ordinary upgrade and
unknown-input recovery unchanged, plus CLI/frontend authority/input rejection.
After quick checks and independent full-series review, run one existing actual Pi
runtime integration fixture using the retained predecessor package and shared
worker topology. Induce the conflict path and a dropped callback result in the
fixture, recover through the public command, then prove one subsequent ordinary
input can start once. Do not use a live peer or duplicate native campaigns.

The eventual public operation, ONLY after implementation/review/verification and
separate exact peer-runtime mutation approval, is:

```sh
workspace-portal pi-runtime upgrade \
  --workspace '<verified workspace>' --slug '<explicit affected session>' \
  --request '<one saved new upgrade UUID>' \
  --expected-generation '<verified retained predecessor generation>' \
  --socket '<registered private portal socket>' --origin '<canonical origin>' \
  --recover-team-conflict '<original conflicting team-message ID>' --member lead
```

Lead must present the fully bound command and its effects: replace the session's
frozen supervisor/workers after positive proof/drain; preserve all histories,
receipts, identities and the unfinished initial reservation; send nothing. This
operation is not currently authorized. It restores admission only if every proof
passes. It does not claim the conflicting assignment was delivered, automatically
retry the earlier reservation, or resolve arbitrary unknown external effects.

D13-R preflight clarification: also obtain the held sender's existing workflow
observation and validate its exact applied tool-policy proof, settings,
attachment/generation and Pending=false. Held=true/Idle=false is expected and
must not be relaxed into an idle certificate; native policy failure still
refuses. Require the frozen predecessor's declared contract/provenance to cover
the inspected immutable roster/initial-assignment rules. The first supported
compatibility target is the exact retained predecessor exercised by the fixture;
unknown legacy implementations do not acquire this proof by sharing a filename
or status label. Complete tool-result coverage excludes unfinished native tools,
and exact host drain remains a separate required physical proof after Stop.

D13-R historical-domain clarification (lead requested): the earlier wording
"unsupported host domains" does not mean rejecting every historical publication
whose tool is not team_message/report_to_lead. Include the other existing retained
conversation host domains as finite read-only cases. A question publication is
settled by the exact validated `FileStore.Questions` record, immutable caller and
native-origin/content verification using the existing domain verifier. It need
not be answered or closed: publication is the callback effect. A plan publication
is settled by its exact validated durable Proposal and the existing native-origin
and argument verifier; a newer proposal does not erase that proof. Add only the
smallest detached historical-proposals/original-call accessor alongside piplan's
existing readRecord, because LatestProposal cannot cover old calls. Do not replay
Publish or decode domain files independently in web. Later question response or
plan acceptance deliveries have their own native receipts; pending/unknown
associated effects retain ordinary refusal. Unrecognized domains, absent durable
publication, wrong origin/content or genuinely ambiguous outcomes still refuse.
monitor_operation is utility-owned and does not become an allowed conversation
publication. No successful-looking toolResult text substitutes for domain proof.

Reuse the existing upgrade and input-recovery strict codec, private publication,
retention, member/history capture and retry fences. The example journal directory
above is not a requirement to create a parallel transition framework. Keep the
new mode's bounded typed evidence distinct, while sharing established transition
ownership and recovery primitives. Old journals retain their exact codec and
semantics. I0 settles the compiling core request/result contract before lead
releases the separately owned CLI package to I1.

D13-R wire contract settled with I0/I1: request fields remain `workspace`,
`requestId` (UUID), `expectedGeneration` (64 lowercase hex); new mode supplies
`recoverTeamConflict` (exact lowercase UUID or compact32hex original team-message
ID) and `member` (sender). Reject mixing this mode with `retireUnknownInput` or
`inputDigest`, and reject member without a valid mode. Core type is
`TeamConflictRecovery{OperationID, Member}` and
`UpgradeRequest.RecoverTeamConflict *TeamConflictRecovery`. The existing reply
adds `TeamMessageID string` with `json:",omitempty"`, retaining the capitalized
Go JSON key. Ready recovery requires `Disposition == "recovered-team-conflict"`,
exact TeamMessageID echo and no InputID/InputDigest. Nonready preparing/starting
responses carry no completion disposition or TeamMessageID and are reported as
unfinished with the SAME operation UUID. Ordinary/input-retirement replies may
not carry TeamMessageID. Strict reply decoding, identity/generation checks and
original spelling remain mandatory; no replacement text/digest/recipient inputs.
The runtime refuses this mode without its owning proof hook. I1 owns only the CLI
paths after I0's compiling contract handoff and lead's index sequencing.

D13-R legacy provenance clarification: installed applications do not retain the
Go source needed to inspect old transition writers. The first accepted legacy
entry is therefore a bounded source-owned compatibility entry for the exact
original application output recorded by D2, rather than an invented installed-
source check or an operator-configurable allowlist. Our existing rollout receipt
binds output `g7wvpp2nc9cvsa8pdf1azfdib80kkcjm-dev-workspace-0.2.0` to derivation
`yqls64i2j3b9zf1v6wrlwbckpvm80z8b-dev-workspace-0.2.0.drv`, reviewed runtime source
`e61d3b7e59f07f89df50d23e23d7800d4b13cabf`, source NAR
`sha256-EhJ65DcpmTpl+ftuyf7EI0D4z8nrJGS4hni7tzMyKrc=`, composed workspace
`f618f0e698e66825fe1ab9d4f4d5948e71de6aa1` and configuration
`d8225a89541e12835ac47f179f4b13f7de00ee60` (rollout.md D2 final composed receipt).
The roster, initial-assignment, addition and removal owning sources remain
byte-equivalent from e61 to the inspected implementation baseline.

Match this entry only against the canonical original AppStorePath from validated
saved Start/launch provenance, together with the complete existing record/read
contracts and exact predecessor identity. A caller/env/current-profile string is
not source authority. Codec labels alone do not certify recovery. Unknown legacy
outputs refuse; the new manager supplies the recovery mode, so the old package
need not advertise a nonexistent recovery RPC. Document this bounded legacy
support with the owning recovery contract. Avoid accidentally retaining an old
Nix closure solely through a compiled full-store-path literal. No new source
provenance framework, dynamic registry or caller override is part of this fix.

D13-R package-transition guard clarification: the implemented first journal write
follows reserveSuccessorRecord and retention of both requests, so the existing
preparing-successor/authority-mismatch guard covers first publication and the
reservation-before-journal interruption. It does not cover the full journal
lifetime: successor ready authority is published before the final journal
completion, and complete journals retain same-UUID replay obligations. The new
session-root journal directory must be included in retained-state inventory.
Documentation alone is insufficient to protect this boundary.

Declare `piTeamConflictRecovery: 1` as the minimal exact-scalar package capability.
Check the selected target with the owning reader before the first reservation or
journal mutation. The existing retained inventory must validate every R journal
with its owning strict codec and exact runtime/selector/member joins and emit a
bounded existing-style source claim. Every prepared, settled or complete journal
requires that capability in target package preflight, independent of the current
hold flag or ready authority. Add the corresponding source kind and require helper
to the existing Go preflight/Ruby package guard path; reuse the ordinary guard
structure. Do not reinterpret piInputRecovery:1 as support for the new codec,
remove audit records to permit downgrade, or replace the unfinished-successor
fence. Malformed/orphan journals refuse. No new marker subsystem is required.

Extend existing focused retention/package tests across reservation-before-journal,
prepared, settled before/after ready publication, and complete phases. Missing,
null, wrong scalar type and unsupported capability version refuse; exact integer1
passes the capability check while other ordinary unsettled-state guards still
apply. Inventory remains observational and invokes no native lifecycle/input
operation. I0 acknowledged this closure in the existing sole-owner core package;
its reported old-protocol/checkpoint quick results precede these guard edits and
must not be represented as validation of the added gate.

D13-R source eligibility is not permanently restricted to one legacy artifact.
Version1 of `piTeamConflictRecovery` also promises the immutable initial-conflict
semantics relied on by this recovery: nonempty initial reservations cannot change,
ready cannot revert to creating, addresses/incarnations are not recycled, and the
owning recovery codec/operation remains supported. Eligible original sources are
therefore the exact documented pre-marker legacy output OR a validated original
package declaring exact integer1. Both branches still require every existing
read/record/native-origin/domain/empty-owner/drain proof. Read the marker only
from the immutable package joined to original saved Start/launch identity; neither
selected-current-profile nor caller input grants eligibility. Unknown pre-marker
sources refuse. This definition adds no callback domains, replay or clear-latch
operation. Add predicate tests for a distinct marked source and malformed/unknown
source declarations.

D13-R native fixture evidence boundary: pointing Start.AppStorePath at the old
package does not execute its supervisor or worker. The scoped proposed check uses
the retained predecessor Node/SDK and production worker protocol/session/persistence
import graph with the existing faux provider, then the current successor. The
existing in-process supervisor can establish source-equivalent predecessor
behavior only while its actual RPC-owning sources are byte-identical to e61:
supervisor.go, conversation.go (including shared topology), callbacks.go,
callback_types.go, workflow_observation.go, worker.go and protocol.go. Freeze and
record that comparison for the tested head, retain the finite old-operation
refusal checks, and reassess if those bytes change. This is not an executed old
supervisor binary or real systemd/host-stop proof; keep the finite host terminal/
drain boundary explicit. Lead must accept this coverage before the native check
or final claim. No additional host harness/campaign is implied.

Lead accepted the retained-fixture boundary above for preparation. Exact old-side
files/contracts/inputs and e61-to-final byte equivalence belong in the final
packet; independent review must assess that equivalence and its limitations.
One affected existing native fixture may be launched by lead only after all
intended source/docs are committed, quick checks pass and review is complete.
This allocation is not readiness or launch approval and grants no live peer
mutation. Actual peer eligibility and host preflight remain later prerequisites.
Future capability1 plus the bounded legacy source eligibility is also accepted.
The preparation boundary was relayed to I0; no further investigation is queued.

D13-R extended verification selection: README's full Ruby requirement applies
because this recovery changes Ruby retained inventory and target package guards.
After final independent review, include the separately exported
`checks.x86_64-linux.ruby-verification` in the related batch; do not make it an
application dependency or repeat it before review. Retain the one approved
retained-native recovery fixture, routine creation smoke and exact composed/
application checks already allocated by lead.

No additional extended target is required for the presently inspected behavior.
`session-creation-extended` covers broader creation/naming/fork/maintenance cases;
`session-recovery-boot` covers Codex provider switch/boot repair;
`host-module-idempotency` covers substrate authentication/TLS activation; and
`pi-runtime-host` covers the unchanged privileged launcher/Stop/drain contract
with a synthetic application. Their owning behavior is not modified here.
The archive VM's explicit predeployment requirement applies if archive/revive
workflow behavior changes. Preserve focused Go lifecycle checks and independent
review of the shared read-only capture extraction; no archive mutation was
allocated. Extension/agent-team catalog and user-namespace outputs cover
unchanged generator/wrapper/namespace variants, so the new recovery marker alone
does not require those additional application builds.

This is scope selection, not a claim that prior outputs passed the final
changed derivations. Reuse prior evidence only with exact derivation/input/output
identity proof for its original scope; source similarity alone is insufficient.
The retained-native fake-host limitation remains explicit. Final diff expansion,
a changed host/lifecycle contract or a relevant failure reopens only the affected
selection. Lead owns the batch, stopping condition and launches; this clarification
ran no evaluation, build, check, network request or live operation.

D13-R completion retry clarification: use the owning domain's typed read-only
`Published(ctx, successor RuntimeRef) (bool, error)` to prove exact publication
from validated binding, authority and roster records. Saved Start or the package
marker alone is insufficient. This predicate answers whether this successor was
published, not whether it is presently idle, unheld or ready for another input.
A later input or independent hold must not turn proved publication into false.
Missing, inconsistent or unreadable required evidence returns an error, never an
absence-based permission to resume effects.

For a settled or complete journal with positive publication proof, validate the
saved source/successor and receipt identities, immutable mappings and unchanged
original history prefix; allow subsequent appended history. Complete the same
journal if necessary and return the original result without attachment, Load,
hold clearing or Publish. The result certifies the original operation, not current
worker health. A settled journal without publication follows the existing fenced
unfinished recovery path; complete without publication refuses. Keep all request,
generation and corruption refusals. Focused regression covers both journal phases
after later input and a later independent hold with zero native/lifecycle effects,
plus publication-read error, changed original prefix and complete-without-proof.
No new public wire, state machine or live operation is introduced.

Operator preparation is private in `private/d13-recovery-command.json`, verified
ignored/untracked and mode0600. Its exact original operation identity and JSON
argv are now prepared from the authorized bounded mapping/history extraction.
The saved request UUID is unchanged; final reviewed runtime/target, fresh positive
recovery preflight and authorization remain pending. This establishes historical
command identity only. No peer command or identifying evidence belongs here.

D13-R retained-provider fixture clarification: the known legacy package has no
synthetic fixture provider/model, so the central helper's hardcoded selection is
inapplicable. `deliveryNativeIntent` also constructs a synthetic catalog and is
not a substitute. Keep production catalog bytes/digest, eligibility, capability
and selection validation intact. Before the existing fixture's first Ensure,
load the original immutable package with `piproviders.LoadInstalled`, validate
its full Default selection, and project account bindings through the existing
owning account codec. Pass those bindings as explicit fixture-only input before
Ensure; never replace retained manager bindings afterward. Keep current callers'
synthetic defaults unchanged. Pass low-level typed fixture options into the
internal runtime helper; do not introduce a piproviders-to-piruntime import cycle.

For this case only, parameterize the existing central intent builder with the
validated original package/default policy. Freeze every reserved member through
FreezePiCreationSelection and derive model/provider/thinking from that frozen
result. The existing lead_reviewed catalog exporter must use the matching model
and effort with exactly reviewer0/read_only and its ordinary typed validation.
Do not replace the original catalog with the target package's default or silently
trim its selection chain. The existing temporary faux wrapper registers the
resolved original native provider/model identities, retaining original Node/SDK
and production worker imports; it must prove execution stays on the faux provider
with temporary auth and no network/credential use. Refresh allowNetwork:false
alone is not proof that later inference cannot reach a real provider.

This is a narrow test-fixture seam in existing P6/central/exporter and R fixture
files, not a production override or a new harness. Native-free preparation must
validate the exact installed input, frozen team/settings/account joins and faux
route configuration before the one post-review native run. Preserve all source
eligibility, capability, history, no-replay and later-input assertions. The prior
fb499 quick result does not validate this new prerequisite correction; I0 owns
the source follow-up and applicable quicks, lead owns release/review/run ordering.

R-D13-2 journal sizing: enforce the existing 1 MiB private-record limit on the
complete aggregate before reservation publication, retention or Stop. Construct
the successor once with the existing pure constructor and expose that same record
to a narrow private admission check immediately before reserveSuccessorRecord
writes the current pointer. Marshal the prepared journal and its settled/complete
projections, including the newline added by writePrivate; all must fit. For an
already reserved/no-journal retry, size the exact saved successor before further
effects. Individually valid captures do not establish aggregate serializability.

Do not budget an arbitrary allowance for extensible raw HostObservation fields.
Keep the Stop field/type and store normalized terminal evidence after its full
receipt passes validation. Retain exact LaunchRequest, Digest,
Unit, boot/invocation/cgroup identity, phase/outcome/result/load/active/job, and the
drain keys used by validTerminalReceipt, verifyCurrentDrainAt and
terminalPriorBootDrain: empty, boot_id, invocation_id when present, control_group,
load_state, active_state and job. Never invent a missing proof key, coerce a value
or discard a field consumed by these validators. The normalized receipt must
retain the same validation result
and the existing drain check remains mandatory.

Use the exact qualified source host identity and frozen launch strings to project
the maximum normalized terminal encoding, including the optional invocation proof
and longest accepted finite state alternatives. Preserve the existing Stop fence
and require returned identity equality; the preflight projection is a size bound,
never manufactured terminal evidence. Requalify before Stop on interrupted retries
using the existing observational path. No raw timestamps, diagnostics or unused
drain extensions may enlarge the new persisted projection. Captured content,
PreparedAt and identities remain fixed; remaining journal growth is therefore
explicitly bounded by phase and this projection.

I0 owns the focused boundary regressions: valid per-record captures exceeding the
aggregate limit cause zero reservation/retention/Stop; the largest allowed capture
plus longest terminal/complete encoding fits; unused large drain extensions add
no journal growth; changed or missing required terminal identity/proof refuses.
This clarification adds no storage format, protocol, lifecycle authorization or
independent verification campaign. Lead retains review and check sequencing.

R2 final lost-Stop-response contract: SourceHost is required and validated as an
identity-only value in every saved schema1 team-conflict journal phase. It binds
the exact source launch/digest/unit/boot/invocation/cgroup before reservation and
is included in the aggregate bound. Capture replay preserves it exactly; retries
never adopt a different invocation. Missing, null or invalid SourceHost in an
existing journal refuses before further effects. Completed replay validates its
saved fence and original proofs without initialization, Load, clear or Publish.

There is no known merged, released, deployed or externally consumed team-conflict
journal predating this unreleased package. The earlier nil-field adoption and
compatibility proposal was based only on branch iterations and is withdrawn;
remove its code and tests. Finalize schema1/capability1 directly, with no old813
reader or rollback-support claim. Genuine older input-recovery and other existing
formats retain their separate contracts and package guards.

An ABSENT journal is distinct from an existing journal missing SourceHost.
Preserve the current-code reserve-before-first-journal crash path: requalify the
original source under the complete existing proofs, reuse the exact saved
successor reservation and request UUID, construct the required identity fence and
enforce the aggregate size bound before publishing the journal or taking further
effects. The first journal still precedes Stop. Replace the obsolete nil-field
replay test with missing-required-identity refusal; retain lost-Stop, drain,
completed read-only replay and absent-journal crash regressions. Optional
DrainProof.invocation_id semantics remain unchanged and are unrelated to the
required SourceHost field.

R native setup regression: the recovery call supplied only two variadic settings
flags while the conflict branch requires a third; it therefore selected the
synthetic provider intent against the actual retained catalog. Route both the
native recovery case and existing RetainedSetup test through one named
teamConflictSeed(t, prepareOnly) wrapper containing the correct flags once.
Preserve the ordinary centralNativeSeedWithUpgrade signature/default behavior by
forwarding to an internal test helper with prepareOnly=false. The preparation
path returns its actual fixture, frozen intent and current catalog immediately
after original and candidate package/intent validation, before profile/server,
attachment, native Create or Send. Existing setup assertions inspect that returned
tuple rather than rebuilding an intent outside the constructor branch.

The quick must reproduce the same failure with the old two-flag entry and pass
with the corrected entry on exact retained/candidate/SDK/catalog inputs; missing
inputs or skipped setup are not acceptance. This executes the existing in-process
fake supervisor setup only, not a native worker/model or real host lifecycle.
Keep the change in the two existing fixture files, with no environment mode,
production override or new harness. Candidate artifact retention is a separate
lead-owned prerequisite. I0 owns the focused repair/check and evidence; lead owns
review and any subsequent affected native run.

R native asynchronous acceptance clarification: input_delivery_v1 returns Pending
after a positive same-process enqueue ACK and persists Accepted asynchronously.
The trigger is submitted once. Permit only Pending or Accepted with no initial
error, then use the existing bounded centralWait and read-only Manager.Lookup for
the exact original SubmissionRef/digest, message, pi-delivery-v1:steer context and
frozen settings. Require matching Accepted receipt and native witness before
capturing recovery evidence. A durable dispatching/Unknown observation while the
receipt finishes is not acceptance; timeout, held state or tool text cannot
substitute. No resend, retry POST, Load or new native input is part of the wait.
Preserve the separate dropped-once/held-idle join, original byte snapshots and all
later no-replay/recovery/count-one assertions. This corrects fixture expectations,
not the production acceptance contract.

For fixture-only corrections, finish the affected native check before another
pin/CI refresh. The rooted source878 diagnostic app may supply immutable inputs
while the test binary, in-process manager/supervisor/web and locally built CLI use
the corrected committed Go source. The fixture's tracking helper uses current
source Ruby. The candidate app's Go executable is validated for presence and
package shape, not executed as the tested supervisor or CLI; this is not a claim
to have run the final packaged binary. Original retained-worker/source-equivalence
and fake-host/drain limits remain unchanged.

Record both identities explicitly: tested source head/binary/fixture inputs and
the diagnostic app output/derivation plus the actual consumed metadata and worker,
Node and SDK paths/derivations/input graph. Reuse the existing bounded source and
immutable-input inventory; do not restart an inventory campaign. After one full
positive native result, build/check the final intended source/artifact once and
close the bridge with exact identities for every consumed immutable worker/SDK/
Node input and validated metadata content, including provider/default/model/team,
runtime capability and supervisor/worker manifests. Validate the final canonical
app path under the ordinary package checks. A changed app output alone does not
invalidate an unchanged independently identified worker input, and matching trees
alone do not prove derivation or runtime-input equality. Any changed consumed
input or production Go behavior reopens the affected verification; unrelated CI
or pin refresh is not evidence of native success. Required final review, exact-head
CI and composed/package checks remain, under lead allocation, with no waiver or
blanket application-equivalence claim.

R empty-load correction — sufficient contract accepted by lead; released to I0.
The one allocated native diagnostic reached settled Stop/drain, successor ready,
two attachment ACKs and two Loads, then refused before Publish. An initialized
empty member keeps its native ID and HistoryRef but the existing SDK creates a
new unsaved planned history filename on Load. Ordinary sameUpgradeMember compares
the old filename; the finite fake had incorrectly kept it. This is a product
comparison mismatch exposed by real SDK behavior, not a host/attachment failure.

Keep conversation.go, supervisor/worker protocol, the retained SDK and ordinary
sameUpgradeMember unchanged. Only a member classified by the sealed R journal as
creating and positively empty may vary its planned HistoryFile during successor
Load. Before settlement the captured mapping bytes/hash remain exact. After
settlement, an R-specific comparator may normalize that one field for equality
only when actual generation is the exact successor and the current mapping is
valid for the identical native ID, creation ID, HistoryRef and member-owned history
directory. Preserve every other immutable field and the existing allowed worker
generation/load metadata differences. Apply the same rule to interrupted mapping
validation; do not repair, rename or rewrite native histories to fit the capture.

Before publication, still require positive current empty creation/snapshot/workflow
proofs, no persisted history or receipts, unchanged initial settings/instructions/
policy and the exact reserved initial assignment. Reuse the owning empty-member
checks with the explicit successor generation; do not mistake disk absence alone
for initialization proof. Validate both the original and new planned locator are
absent when different at this stage. Unexpected persistence, new input, foreign
path, different identity, changed policy/settings or pending/held state refuses.
Originally persisted members retain exact HistoryFile and original history-prefix
proofs with no exception.

Published/completed retry has a different purpose: it returns the historical
result and must permit legitimate later input and independent holds. For a member
proved originally empty, the original persisted prefix has length zero and its
old unsaved filename was never a persistence identity. Validate the current owned
mapping and immutable native/creation/HistoryRef identity without requiring that
obsolete filename or fresh emptiness, and retain exact original receipt hashes.
Keep originally persisted prefix checks unchanged. No Load, clear, Publish, new
receipt, or new mutable-history scan is added to completion replay.

No new journal field or size allowance is needed: retain the original capture
unchanged and derive the exception from its existing positive empty classification.
The journal's pre-reservation bound is unchanged. Owning changes are confined to
R helper/comparator use in upgrade.go and team_conflict_recovery.go, the existing
finite and native fixtures, and the owning recovery documentation. I0 should
make the finite empty Load choose a different planned filename, then cover first
success, interrupted successor Load before publication, same-UUID published replay
after a later accepted input/independent hold, and negatives for persisted members,
wrong identity/path, unexpected input/persistence and any other immutable change.
Lead accepted this consequential contract and released I0 to implement the narrow
package. I0 owns focused regressions, quick checks and the committed deliverable;
limited independent affected review follows those checks and precedes the one
lead-allocated affected native verification. Routine private comparator/hook
signature clarification remains direct between I0 and architect0. No new domain,
generic path relaxation or branch-iteration legacy-format support is authorized.
No real peer recovery, production launch or current operational eligibility is
established by this proposed fix.

R diagnostic allocation amendment for product fix
4f764ff6cc0f7b26fffdfcd3108ace5a75971c98: the earlier fixture-only bridge does not
reuse an earlier native result as proof of this changed Go behavior. After the
assigned limited independent review, the next affected native run executes the
new committed Go test/manager/web/supervisor and source-built CLI. The rooted
source878 app remains a diagnostic immutable-input supplier; its Go executable
is not run. This tests the changed behavior with unchanged retained/candidate
worker, SDK, Node, provider and runtime-contract inputs, subject to the owner's
recorded exact consumed-file identity evidence. Seven predecessor RPC-owning
sources remain unchanged; this correction adds no protocol, journal field or
schema. No new source or artifact audit was performed for this clarification.

Reprepare only the changed Go test/CLI compilation and existing source-hash receipt
at the tested 4f head; prepare its CLI build dependency outside the fixture deadline
as already agreed. No immutable worker/metadata rebuild is required for the
diagnostic run while those consumed inputs remain exact. Current-source Ruby and
fixture wrappers retain their separately recorded identities. Changed consumed
metadata, worker/SDK/Node input, provider configuration or runtime contract would
require re-preparation of that specific dependency before relying on the run.

After one full positive result, the final new application must be built from the
intended final source and pass the allocated final source/package/composed/CI
checks. Close the consumed-input bridge with exact output/derivation/input
identities and metadata content, recording source878 diagnostic app and final app
separately. The old app is not claimed equivalent to the corrected product and
cannot serve as the corrected deployment or operational recovery artifact. Final
packaged-binary execution is not established by the in-process native fixture.
Lead owns review completion, launch and final acceptance; no live approval follows.

R fixture capability clarification: the finite supervisor defaults checked-input
and conversation-identity readers to false. The explicit immutable-package setup
must restore readCheckedInputContract and readConversationIdentityContract before
Ensure, alongside its existing production transcript/input-delivery/activity
readers. Preserve synthetic defaults and read actual saved predecessor/successor
package contracts; no constant-true capability or admission override is allowed.
The existing preparation assertion should verify both exact package inputs and
manager reader wiring. This is a fixture-only correction; completed recovery and
read-only replay are scoped positive evidence, while public admission and later
input still require the remaining affected end-to-end check. Lead owns release,
review and native allocation; production readiness/dispatch semantics stay intact.

R operational refusal diagnostic — proposed sufficient brief, awaiting lead release.
The reconciled public attempt made no reservation/journal or recovery effects.
Do not retry Upgrade merely to recover its erased error. A separate process cannot
reuse the portal's existing host attachment: attachHost rejects a second one.
NewContext also starts reconciliation/dispatch work. Therefore the team-preflight
checkpoint alone does not make a standalone full Upgrade replay observational.

Use one private test-only bridge to the existing captureTeamConflict with live=true
and previous=nil, after actual source Inspect. Assemble the actual production
Manager/config, read-only admission and piTeamConflictDomain using existing owning
functions and the saved command's identity; never fake a domain proof or capability.
Private Go overlays at the existing tagged web/piruntime fixture seams may expose
these functions without changing installed product source. Avoid NewContext and
background services. Preserve package/profile/provider/account/state/host/authority
bindings, ordinary locks, source identity and absence of any saved operation/journal.
The current portal keeps its attachment. Permit only existing observational native
snapshot, verify_creation, workflow_observe and inspect_origin calls; unavailable
attachment/readiness is a result, not permission to attach, replace or bypass it.
No Upgrade, Ensure, Stop, Load, clear, Publish, receipt write or send is reachable
from this diagnostic entry. Capture ends in memory before reservation by construction.

I0 owns the private preparation and bounded observation only after lead release.
Compile before the observation; one execution expected within30s, hard context45s,
stopping at the first error, capture success or timeout, without retry. Keep the
wrapped error (bounded4KiB), configuration/hash receipt and pre/post existing durable
identity/effect comparison in ignored/untracked0600 private files. No bodies,
credentials or peer identifiers enter tracked records/chat. Report source-inspect
failure, capture failure, or capture-complete/public-cause-unresolved. Success does
not establish full preflight or reproduce the portal attachment stage. No new public
dryrun, logger, installed helper, framework, deployment or operational retry follows.


D14 historical terminal policy refusal — sufficient finite tool/stage extension;
awaiting lead acceptance/release after the completed local callback matrix. I0 owns the complete follow-up above
merged runtime91; architect owns this brief. Do not rewrite merged history.

The additional supported disposition is `terminal_policy_refused`, only for a
NONSELECTED historical invocation whose exact tool is `team_message` or
`report_to_lead` and whose exact stage is `caller_policy` or `recipient_policy`. Its positive proof is the
original saved native terminal reply produced by the already qualified frozen
legacy package/source and fixed worker/SDK/hook graph. That producer refuses a
canceled context, uncertain effects or entered dispatch before emitting the exact
held/{caller_policy,recipient_policy}/held/unattempted tuple. Its materialization state never resets;
the fixed graph disables external extensions and has no tool-result override.
Thus this proves that invocation stopped before effects. Current READY state,
missing receipt, arbitrary tool text and generic SDK result persistence prove
nothing of this kind. This does not assert the historical cause of transport loss.

Use the existing exact legacy saved-Start/package provenance predicate, further
bounded to its reviewed fixed result-producing graph. Do not infer producer
semantics from the selected profile, generic recovery capability or caller labels.
Other source generations retain existing supported recovery behavior but do not
gain this terminal-result proof without an explicitly qualified producer. The new
reader capability below is NOT producer authority. No source-hash registry is
needed; the existing accepted legacy identity is sufficient for this correction.

Transient interface: keep raw native result projection local to the R capture
helper rather than changing shared adapter/old-RPC structs. A private pure parser
accepts the raw matched message and expected native call ID/name, returning a
small typed terminal-refusal projection or an error. Carry an optional projection
on TeamConflictCall into Settle, populated only by the R history capture path;
include the matching result entry identity for exact revalidation. No public wire
field, worker change, result body in the journal, or generic lifecycle relaxation.
The full original raw-history digest and prefix fence remain authoritative.

The parser requires role toolResult, explicit isError=false, exact native call ID,
toolName equal to the original call and in the exact two-tool set, one text
content block, and a details object. Decode both
text JSON and details with the existing strict duplicate-aware codec: exactly
four keys and string values disposition=held, stage in the exact two-stage set,
reason=held, materialization=unattempted, with equal objects and no trailing JSON. Reject
missing/null/wrong types, duplicate keys, extra fields/blocks and any other tuple.
The owning projection also requires exactly one original call and one following
result in the same validated linear history, exact name/arguments/native origin
and Accepted user-input binding. Reject mismatched, orphan, duplicate or foreign
results. Any invocation whose sender/message ID matches the requested selector
cannot use this proof; the selected operation still needs initial_conflict.

Settle retains exact current binding/roster/intent, target membership, original
envelope and admission reads. Preserve the accepted e5 receipt-precedence fix:
first honor a valid matching receipt under its existing proof, including a later
same-ID success after an earlier refused invocation. Only with no exact receipt
may the terminal-refusal branch apply. Only a successful strict proof with absent exact
submission receipt may return terminal_policy_refused; lookup errors or a
contradictory receipt refuse this path. Existing positive receipt classifications
remain unchanged. The aggregate independently checks the proof/source/call
binding, exact target and absent receipt, preserves duplicate-message argument
checks and never sets selected-conflict matched from this kind. All other owners,
callbacks, native origins and history proofs remain mandatory. Unknowns refuse.
Do not relabel this as receipt-backed not_submitted. Seal the validated projection
in the existing evidence digest; persist only the new Kind and existing fields.
Use the same capture/revalidation for interrupted pre-effect replay. Existing
settled/Published completion retains original-history-prefix and saved evidence
fences, without native replay, fresh empty RPC, Load, clear or Publish.

Compatibility is a real obligation because runtime91 is merged and deployed.
Preserve piTeamConflictRecovery:1 and all existing journal kinds/schema1. Add
supplemental runtime-contract integer piTeamConflictTerminalRefusal:1, parsed
strictly like the existing recovery marker (missing means unsupported; malformed
or other versions refuse). Require it on the target package BEFORE reserving a
successor whenever capture uses terminal_policy_refused, and before resuming such
a journal. Keep the existing reservation-without-journal crash path and unfinished
successor fence; no new journal publication precedes that fence. No new journal
field or migration is needed; the longer Kind participates in existing exact
pre-reservation serialized-size admission.

Extend existing retainedTeamConflictMembers/ConversationRetention inspection to
flag HasTeamConflictTerminalRefusal when any validated journal contains this Kind.
Inspect prepared, settled and complete journals, not just pending transitions,
without native calls or inference. Keep HasTeamConflictRecovery as well. The
existing pi_workflow_preflight scanner emits an additional stable claim kind
team_conflict_terminal_refusal; add it to the existing Ruby TEAM_SOURCES and
workspace-host target guard, requiring the supplemental marker AND base cap1.
All old journals keep their original capability requirement. Unknown journal
kinds, malformed records or uninspectable inventory remain errors. Old91 readers
reject the new Kind; they must not be claimed compatible. Package selection and
activation must refuse an incapable target while any such journal is retained,
including complete results needed for same-UUID replay. This reuses the existing
inventory/activation path, not a new storage or version framework.

Rollback before first new journal remains the ordinary supported path, subject
to existing reservations/fences. After a journal with the new Kind exists, remain
on a capable package or move forward to one; do not delete/convert journals or
switch to91. Existing91 state remains readable by the new implementation. The
actual refused operation has no journal, so this follow-up does not migrate it.
No second operation UUID or automatic retry is introduced.

Files: R capture/helper and tests in portal/internal/piruntime, owning
portal/internal/web/pi_team_conflict.go and tests, existing conversation-retention
projection and portal/cmd/workspace-portal/pi_workflow_preflight.go, runtime-contract
producer, libexec/workspace-session-backends.rb and libexec/workspace-host with
owning inventory/package tests, and existing runtime/recovery documentation.
I0 owns source/docs/checks/normal commits; no overlapping owner or CLI wire change.
Architect source work ends here. Lead owns full release, review and operations.

First observable check is a native-free faithful synthetic linear history with
earlier READY-target/absent-receipt terminal refusals covering all four tool/stage
pairs and a distinct later selected initial conflict: demonstrate the old owning boundary refuses, then the
new proof settles only that earlier call. Parser/projection negatives cover all
shape/binding failures above, wrong source/hook provenance, attempted/uncertain or
arbitrary replies, selected-operation misuse for either tool, report arguments
containing a caller-supplied target, wrong fixed lead target, and mismatched actual
tool names. Preserve the valid-receipt-precedence regression. Add a remaining genuine unknown
to prove aggregate recovery still refuses before reservation or effects. Owning
recovery tests cover saved/replayed new Kind, unchanged original selector/receipt
and zero extra dispatch, interruption and Published replay after later input/hold.
Inventory checks cover every phase, complete retention, absent-journal crash,
old journals, malformed marker and refusal of base-cap1-only target before effects.

Run focused existing Go/codec/inventory quicks first; report old-red/new-green and
exact commit/files/gaps. No live callback or SDK run is needed to establish the
parser failure. After committed quick-green output, lead allocates limited
independent affected review, then only the affected native/package/composed checks
needed by changed inputs (full Ruby if its inventory plumbing changes). Preserve
exact consumed-input reuse limits; do not repeat an unrelated VM campaign. Final
artifact/pins, a fresh machine claim and the original saved same-UUID public
operation remain lead-owned readiness steps. This brief establishes a supported
path past the identified blocker, not eligibility or restored monitoring/sending.

Frozen producer qualification for this finite extension: e61
pihosttools/team.go strictly parses report arguments as message_id/message and
fixes its target to lead; piTeamService.Report immediately delegates to Peer with
the original ID/text. It has no report-specific earlier effect. The shared
HostCall branch and reporting.mjs use the same typed refusal serializer and
text/details projection while preserving the actual tool name. After successful
caller participant validation, WithDelivery sets recipient_policy and calls the
same participant reader, with only the target activity read added. That path
projects policy and performs admission/creation/fork/tool-policy/transcript/activity
reads; it does not reserve, Create or Send. Only after it succeeds do delivery
admission and the delivery callback run. Every preceding materialization changes
the effect state away from zero without resetting it; canceled/uncertain or
send-entered states cannot produce this typed proof. PiDelivery marks attempted
before Native.Deliver and never reclassifies an entered send. Therefore both
stages under this exact producer can attest the same invocation-level absence of
dispatch/materialization effects. A stage label alone never supplies that proof.

The completed private matrix supplies nine additional uniquely joined terminal
results in the two-tool/two-stage set; their exact reason is held, isError is
false, and strict text/details agree. This resolves the locally identified class
gaps in one design. It does not certify the entire live capture: existing Accepted
receipt/native Bootstrap checks still run and their per-receipt native results
were not retained. Any future allocated observation must retain bounded callback
index/tool plus Settle versus Accepted-creation/Bootstrap failure stage, rather
than erase these into another generic first-error result. No observation is
allocated by this brief, and no private matrix identities/bodies enter source.

D14 is unpublished and has produced no new-kind journal. Rename its unmerged
caller-only Kind directly to terminal_policy_refused and consolidate its tests/
docs; do not support the obsolete caller-only spelling or add a migration or
second marker. The final piTeamConflictTerminalRefusal:1 reader denotes exactly
this finite policy-refusal proof contract. Merged runtime91 and its old kinds stay
unchanged. This is a supported finite extension of the existing proof, not a new
domain, generic error-result trust, or permission to retry the live operation.

D14 finite producer seam clarification: an unexported Config
teamConflictTerminalProducerContract func(string) error may mirror the existing
private reader seams. Its argument is only the validated original saved
Start.AppStorePath. Nil selects the strict production verifier; existing
predecessor-contract checks remain independent and mandatory. The finite fixture
accepts its one explicit synthetic producer path and rejects all others. This
avoids a retained-store/model/account dependency in finite CI while detecting
wrong-path plumbing. Separately test production default rejection of an
unqualified package, including reader-capable packages. No public or environment
override is introduced. Finite positives prove the consumer under supplied
producer semantics; the frozen legacy producer's authority remains the separate
reviewed source proof, not a claim that finite CI executed that producer.

D14 diagnostic availability boundary: retained supervisor workflow_observe requires
an existing workflow-ready host attachment, no pending workflow mutation and no
overflow before invoking the worker. Snapshot success does not prove that gate;
other record/native-response/final-sequence failures also return unavailable.
Direct capture omits Upgrade's EnsureAttachment, so the missing precondition is
possible but not established as the observed cause. The normal portal display
refresh performs original-receipt lookup reconciliation and attachRetained before
refresh. It reuses a healthy same-runtime connection but may replace a lost one;
a Connected event queues existing delivery drain. Thus a public page/workflow GET
cannot be promised as a no-send/no-replacement initialization probe. Held policy
also prevents a normal cached display observation even with a healthy attachment.
The necessary next evidence is the owning connection's setup reply/matching
workflow ACK and current identity, or its retained exact failure event. The
existing refresh log may retain an error but there is no identified public
attachment-state reader or retained subcause for this failed capture. No new
observation, attachment, retry, profile change or product fix follows from this
source finding; lead allocates any further observation and I0 owns its recipe.


D15 consumed recovery continuation — sufficient narrow brief, awaiting lead release.
I0 owns one follow-up package above consumed b3: R continuation and HTTP reader
selection, focused tests/comments and existing recovery docs. Preserve b3 history,
existing schema1/Kind/capabilities and the actual journal/UUID/target unchanged.
No live retry, worker stop, private repair or target substitution is authorized.

Two source defects compose: R unconditionally fresh-checks the old cgroup after
settlement, although the owned successor now occupies that path; the HTTP same-UUID
handler also requires saved target app/profile-generation equal the current reader.
Fix both before claiming that deployment of a corrected reader can resume.

Keep prepared handling unchanged: full live proof before reservation, exact
SourceHost/terminal receipt and fresh positive drain, then offline domain/history/
receipt equality BEFORE the first settled+Stop save. A valid saved settled or
complete journal makes Stop immutable historical evidence. Always validate it
against original source launch/digest and exact SourceHost, current saved successor,
Start and selector. It is not a fresh description of the reused cgroup.

After that static validation, check owning Published and retain the existing
original-prefix/mapping/receipt replay validation. A published exact starting
successor returns its original result (marking a lost-final-response settled
journal complete if needed), with no native/host inspection, fresh drain, Load,
clear or Publish. Complete without positive publication refuses. Later input and
independent holds remain compatible with this historical replay.

For an unpublished settled journal, admit only its exact current successor and
existing phases. If current.Phase is preparing, retain fresh old-source drain
before further work; unchanged ordinary successor preparation/H0 Start also
requires it. If current.Phase is starting, do not require current emptiness of the
old cgroup path: that marker is the existing durable entry before host Start, not
proof of readiness. Preserve all mapping afterimage/original-history/receipt
checks, then use ordinary Ensure/Inspect on the exact saved successor. It must
prove host launch identity, config hash, owned handshake, process identity and
ready phase before successor attachment and Load. Existing no-host-intent recovery
keeps its own positive absence/drain gates. Unknown/mismatched successor, invalid
Stop/SourceHost or changed saved evidence still refuses; no foreign occupied group
can authorize a successor. No generic verifyDrain relaxation or host change.

Reader/target compatibility: pi_runtime_upgrade.go103-111 currently blocks newer
readers. Only when recoverTeamConflict is valid AND current request ID equals the
submitted saved UUID, read and reuse Start exactly. Keep exact session/incarnation,
UUID, predecessor, binding revision and registered ProfilePath checks; permit saved
AppStorePath and saved ProfileGeneration to differ from the currently selected
reader. Never overwrite them. Validate current reader/package/profile independently
through existing admission/validatePiPackage and existing recovery-reader capability
checks; validate saved target/package and journal-required capabilities through
Manager as before. The corrected selected package supplies the reader; saved app,
profile generation, launch digest, native IDs and worker execution target remain
frozen. No new wire flag/field, schema, marker, registry or private operational API.
Ordinary upgrade and input retirement retain their existing selected-target rules.
No reservation/journal means ordinary new selection; a reserved no-journal crash
uses its exact saved Start and existing preparing recovery. Final reply still names
the saved execution target. A newer reader is not a target retargeting operation.

Files: portal/internal/piruntime/team_conflict_recovery.go and existing recovery
fixtures/tests; portal/internal/web/pi_runtime_upgrade.go and owning HTTP tests;
existing runtime/recovery docs. Reuse Manager/host/public reader methods without
changing worker protocol, H0 contract, CLI shape or package inventory. The source
selection/receipt-precedence/unknown-domain proofs remain unchanged. Root owns
current-reader deployment and fresh operational identity/claim/approval; I0 owns
all source/check/fix/commit work after release, including supplied final-artifact
preparation. Architect edits only this brief.

Meaningful quicks: drive an actual settled recovery fixture to current starting
with the same saved cgroup now populated by the exact successor. Use the production
fresh-drain checker against its existing fake filesystem seam (not always-success
verifyDrain) to demonstrate old-red/new-green and preserve fresh-drain refusal at
prepared/settled-preparing. Test partial Load continuation and Published/complete
replay after later input/hold with zero native/Load/clear/Publish counts. Negatives:
wrong current/successor/Start/selector, altered SourceHost/Stop, changed prefixes or
receipts, missing publication and failed successor handshake/readiness. HTTP owning
test uses different current reader and saved target/profile-generation, proves
unchanged Start reaches Manager/result, and refuses changed scope/profile PATH,
stale reader, mismatched predecessor/expected generation and unsupported saved
capabilities. Preserve the no-journal reservation crash and ordinary/retirement
changed-target refusals. Use no peer IDs/body or live state in fixtures.

After focused Go/HTTP/codec quicks and normal commit above b3, independent affected
review covers both fixes and consumed-state compatibility before the one allocated
related native/artifact check. Native fixture retains its existing host-simulation
limits; finite production-checker regression owns the reused-cgroup distinction.
New reader package must pass affected package/composed/CI checks; actual successor
continues from the retained saved target. Reuse unchanged Ruby, worker/SDK/provider
and other evidence only with exact consumed-input identities; no Ruby rewrite or
unrelated campaign is part of this package. Existing consumed formats need no
migration. Old b3 reader remains unable to complete this state; rollback to it
preserves the record but is not a restoration path. Keep a corrected capable
reader and the frozen target available. Actual readiness and any later operational
refusal remain unknown until root's supported same-UUID continuation; no standalone
capture success is a readiness gate.


D15 package-selection continuation — sufficient separate follow-up above fd03;
awaiting lead release, including the conditional target capability below. I0 is
sole owner. Consumed b3/journals, prior D15 commits and all operational identities
remain unchanged. This is compatibility observation, never authority publication.

The refusing Ruby current_runtime_projection! only accepts a starting current
runtime whose generation equals ready authority. Existing Go inventory validates
R journals but exports no relation explaining an unpublished successor. Both the
installed predecessor and fd03 therefore reject this valid interrupted state.

Extend the existing owning retained R inspection pass, using the existing runtime
and journal decoders, to return an optional typed projection for exactly ONE
current settled team-conflict recovery with current successor phase starting.
Source/successor must be exact retained records in the same validated chain and
instance; CurrentRequestID, successor RequestID, saved Start and Start's predecessor
must join the journal exactly. Require settled Stop, valid original terminal
receipt, exact SourceHost identity, valid selector/domain/call journal, supported
saved target/required reader capability and existing permitted before/after member
mapping plus original-history/receipt checks. No native readiness or current old
cgroup emptiness is required for this inventory. Do not duplicate the Go journal
codec in Ruby. Ambiguous/malformed/mismatched retained state remains an error.
Prepared, complete or unrelated upgrades do not earn this exception. Complete
requires normal successor authority; no-journal mismatches still refuse.

The Go-to-Ruby interface is one optional property on the existing schema3
piRuntimes item: teamConflictRecovery = {requestId, sourceGeneration,
bindingRevision, phase}. Values are the exact saved request UUID, source hex64,
positive integer saved binding revision and literal phase=settled. The surrounding
session/generation/phase identifies the current starting successor. Populate it
from the same successful retained-record inspection that emits retention claims;
never from labels, directory names or current activity. A private Go result may
carry the complete typed relation, but the JSON projection carries only these
fields. No new on-disk record or protocol schema is required.

Ruby team_preflight! strictly validates the optional object's exact keys/types,
sourceGeneration != current generation, and starting outer phase. The existing
current_runtime_projection! retains its normal equality path. Only on mismatch,
with this positive projection, may it accept READY authority at exactly
sourceGeneration, matching the selected binding/session/incarnation and the
projection's bindingRevision. No missing authority or starting authority qualifies.
The operation must preserve that authority, binding, mappings, original receipt
and saved target byte-for-byte. Target capability checks run before accepting this
exception and at every existing prepare/locked activation/selected activation/
completion recheck; fresh inventory is still required at those boundaries.

A supplemental exact integer piTeamConflictRecoveryTransition:1 is necessary
ONLY while relying on this authority-mismatch exception. Existing base recovery1
and terminal-refusal1 demonstrably do not identify a package whose activation
reader can accept this state. Without a new target check, a corrected installed
executor could select an old cap1 target and discover refusal only after profile
selection. Reuse the existing runtime-contract publisher/strict scalar reader and
package preflight guard for this one requirement; preserve all base/journal-kind
capabilities. The marker asserts compatibility preservation, not operational
readiness or new proof authority. No version registry, migration, blanket old-reader
claim or changed journal follows. Ordinary matching authority and old journals
keep their current requirements. Lead acceptance of this narrow marker is part
of release; it cannot be replaced by an unchecked package label.

Use the existing PUBLIC reviewed candidate entry:
  <corrected-package>/bin/workspace-host switch --source <exact-source> --from-candidate
The source must build that exact unselected executor. The entry uses its own Go
preflight reader, verifies the installed profile token and candidate generation
lock, and repeats ordinary compatibility/coordination/registration gates. It
selects that corrected reader package through the existing transaction and then
runs its own activation checks. It does not retarget the frozen runtime Start or
publish the predecessor authority. Installed G5 switch cannot supply the new
reader; fd03 lacks this correction. No direct _activate, profile edit, journal
repair or old-worker control is a supported substitute. Root owns concrete final
paths, fresh held claim, prepared selection and any resulting recovery. Same UUID
continuation follows only after reader activation is verified.

Files: existing piruntime retained inspection/R projection and its tests;
portal/cmd/workspace-portal/pi_team_preflight.go and owning tests;
libexec/workspace-session-backends.rb, workspace-host and their existing profile
transition/backend tests; runtime-contract marker producer and owning recovery/
package-update documentation. Keep files/index with I0; no CLI or native/H0 change.

Smallest faithful old-red/green uses an actual existing finite recovery fixture
stopped after settled+successor-starting, before authority publication, with its
original Stop and unloaded/partially loaded mapping afterimages. Feed the owning
Go inventory into Ruby compatibility: old code refuses the exact mismatch; new
code accepts only the joined relation and a capable target, with unchanged durable
bytes. Then exercise existing candidate-entry prepare and selected activation
rechecks with this fixture. Negatives cover absent/malformed/duplicate projection,
wrong current/source/selector/Stop/binding/target, other pending upgrade, altered
mapping/history/receipt, prepared/complete mismatch, missing or starting authority,
unknown/new marker values and old target refusal BEFORE selection. Normal matched
successor and original-generation cases stay green. No fake boolean may replace
the owning journal relation.

Run focused Go inventory/Ruby backend/profile-transition quicks and commit above
fd03, then independent affected review. The changed Ruby package-selection inputs
require the separately exported full Ruby check after review; prior 708-second
Ruby success remains evidence only for its old inputs. Preserve unrelated native,
SDK/worker/host and D14 evidence with exact consumed-input identities. Select only
additional package/composed checks justified by the new metadata/gate; no new
callback/native campaign. Actual corrected-reader activation and same-UUID recovery
remain root-owned operations with unknown final live eligibility. No operation is
authorized by this brief.

Package-selection projection clarification: complete the existing mandatory
retained inventory validation and claims independently of the optional transition
proof. Static journal/source/successor/Start/SourceHost/Stop corruption, mandatory
mapping identity/codec failures and cancellation remain errors. Only additional
unfinished-transition qualification may fail by omitting teamConflictRecovery:
nonqualifying afterimage, actual original-history/receipt equality or saved-target
capability must not reject the previously supported normal authority-matched path.
Continue all mandatory inventory checks and retain its ordinary dependency claims.
Omission asserts neither publication nor readiness. Ruby accepts normal exact ready
authority/current-generation equality as before; any mismatch still requires the
positive exact relation and capable target. Test settled-but-Published lost-final-
response plus later legitimate input/hold: no optional projection, matching
authority succeeds, predecessor authority refuses; corrupt static evidence still
fails both. No authority transport, generic error suppression or new reader.

D16 retained lead access — sufficient forward-admission package; awaiting lead
release. I0 owns application code, fixtures, focused checks and commit above
3a60; architect owns this brief. The completed recovery and its frozen execution
target are not reopened. The observed resolver refusal is before BindRead: the
original nonfork creation wire lacks lead Access, and piSavedAccessLocked requires
its catalog digest to equal today's installed team catalog. A newer reader cannot
supply an older session's permissions from its defaults. Later native eligibility
is not established by fixing this predicate.

Use one private, read-only retained-lead-role helper in the web owner, consumed by
piSavedAccessLocked and piTeamService.participant. Preserve the exact current
catalog fast path. On a valid current catalog with a different digest, use the
existing piInitialStartReader to read the explicitly named original creation
request, after the existing ready binding/roster/intent/evidence admission. Reuse
the ready creation-journal/intent join in pi_retained_catalog.go: journal ready,
native present, exact intent; Start and Runtime match the session and original
RuntimeRequestID, no predecessor, BindingRevision=1, and Runtime.Generation equals
the original journal NativeGeneration. This lookup must also run when provider
catalogs happen to match: provider equality is not team-catalog provenance.

Validate the original canonical package root (absolute/clean and EvalSymlinks
equal to the saved literal), load its team metadata with the existing strict
agentteams.LoadInstalled reader, and require Managed, a catalog,
the exact saved CatalogDigest, team ID and team_lead role. Retain the existing
base-or-Pi-projected TeamDigest comparison, parameterized by that proven catalog;
the projection comparison only verifies provenance and never changes a retained
preset. Require explicit Access in read_only/workspace_write. Return a role copy;
participant keeps its existing saved lead model/effort/instructions overrides
before ProjectPiPolicy. No fallback to a current role when original proof fails,
no digest-only source search, new catalog registry or synthetic permission.
This team-only metadata lookup does not add validatePiPackageRoot's executable
payload checks. The owning ReadInitialStart/record and ready-journal join supplies
source identity; the strict installed team reader supplies catalog validity.
Existing validatePiOriginalCatalog full-package/provider checks remain unchanged
where already required. Strict temporary metadata fixtures may test this reader
without a production override; they do not replace the owning original-Start join.

Keep current installed metadata validation, provider/account/model validation,
current binding/ready authority/generation, roster member identity, native
settings and tool-policy checks mandatory. Fork lead access and nonlead saved
roster permissions are unchanged. New preset selection and initial creation stay
on the current catalog; initialPiWorkflowPolicy's nonlead retained-materialization
branch already uses saved member access. Do not broaden piSourceTeamMatches
globally. The helper grants only the originally explicit access: no new tools,
permission escalation, account or model scope. Original Start is access provenance;
current saved execution Start still governs BindRead/InputDelivery/native checks;
selected package remains the reader. No persisted field, schema, capability,
journal/authority edit, retargeting, lifecycle action or recovery replay is needed.

Files: portal/internal/web/pi_retained_catalog.go, pi_team_admission.go,
pi_teams.go, their owning tests and pi_activity_test.go; a short owning runtime/team
documentation explanation. A private helper file is acceptable if clearer.
Preserve shared adapters, worker/SDK, runtime protocol, Ruby inventory and package
selection. Missing original package/provenance is a supported refusal, not repair.
The original package already has the owning indirect Nix GC root: initial Ensure
retains instance/package-root (manager.go:309-330, retainPackage at 166-168), and
successor retention preserves it while freezing each requests/<UUID>/package-root
(successor.go:58-91, 107-121). Team-conflict preparation retains both requests
before successor start (team_conflict_recovery.go:983-986). ReadInitialStart reads
the retained request chain, not a profile generation. Thus ordinary profile
generation collection must leave the original runtime root and full package
closure available; completion does not retire that dependency. Preserve this
existing ownership, with no extra catalog copy, registry or retention format.
Use existing successor retention/ReadInitialStart regression evidence and assert
the D16 reader still selects original evidence after current-target change. This
source contract is not a new claim that a live GC operation was exercised.
Rollback preserves all records but the previous reader still refuses differing
team catalogs; it is not a usability-restoration path for that combination.

First acceptance is faithful old-red/new-green through the actual HTTP resolver
and read admission: original catalog A, valid newer reader catalog B, original
Start/journal A and current successor authority; GET reaches existing BindRead,
Verify and activity exactly once with no mutation. Extend existing fixtures and
strict installed-metadata readers, with synthetic data only. Cover both equal
provider/different team catalogs and the existing retained-provider path. Assert
original read_only is not raised by B's workspace_write, and original
workspace_write is retained rather than replaced by B's defaults. Exercise the
owning team participant path and ordinary write admission with saved settings;
live Send is not a test or diagnostic requirement.

Negatives: missing reader/root/catalog/role/explicit access, malformed installed
metadata, unmanaged catalog, wrong catalog/team digest, foreign session/request/
generation, successor substituted for original Start, nonready or mismatched
creation journal, stale binding/authority/ref, and missing current metadata.
Unknown access refuses. Retain fork/nonlead/current-catalog behavior and new-preset
current-catalog refusal. A later BindRead or Verify refusal must remain a refusal,
with no activity success or mutation. Assert native identities, original retained
state and completed recovery bytes are unchanged by admission.

Run the focused owning web admission/catalog/activity/team quicks, commit all
intended changes, then limited independent affected review of permissions and
retained-source provenance. Use existing package/composed checks for final changed
inputs; reuse prior Ruby/native/worker evidence only for exact unchanged inputs.
This package changes no recovery, lifecycle, host or package-composition contract;
no archive/boot campaign or full recovery/SDK rerun follows merely from this
admission correction. Reassess required checks if implementation crosses that
boundary. Root owns final artifact/selection and any bounded ordinary monitor/send
verification under current approval. No additional live observation is allocated
by this brief. Implementation can proceed on this settled boundary independently
of unproved later BindRead/Verify predicates; a concrete later failure returns to
lead rather than broadening this package.

Tab-refresh activity/timing presentation — sufficient independent I1 package,
awaiting lead release. User requests the last known values during tab activation
refresh. This is separate from reader activation and the retained-lead admission
fix. I1 owns app.js, its affected browser tests and any short owning UI comment;
I0 retains runtime/activation work. Architect owns this brief. No backend, native,
HTTP contract, persistent storage, readiness or recovery change is required.

The current app.js createTimingClock (955+) retains elapsed time but marks it stale
on pause. suspendPageReads/resumePageReads (4728+), pauseTiming/resumeTiming
(5219+) and updateCodexWork (5133+) immediately turn that presentation into
unavailable via currentActivityDisplay/projectActivityDisplay. The existing
message_delivery_browser_test.cjs PI_ACTIVITY_ONLY held-resume assertion expects
this behavior; change that expectation for the user-requested display semantics.

Keep strict projectActivityDisplay and currentActivityDisplay as the fresh
evidence projection. Retain one page-local last successful presentation, scoped by
the existing activityDisplayBinding tuple (backend, conversation, member, Pi scope,
thread) and invalidated when that identity/scope is no longer valid. A small
presentation helper beside the existing activity helpers may make this testable;
do not add a general cache, storage, request framework or backend-name UI branch.
No member's values may appear for another member, conversation or replacement
incarnation; a new document starts without retained display.

During hide/resume or same-target refresh, preserve the last successful activity
label, counts and timing display while replacement reads are pending. Freeze the
last rendered elapsed values: hidden/waiting time must not be added to a presumed
working/idle state. Expose refreshing/pending status through the existing status
presentation without replacing the values with unavailable. A validated current
response replaces the display and becomes the new retained success. If no success
exists, show the ordinary loading/pending state until the first result; do not
invent activity, zero durations or an idle state.

Retention is display only. It must not set fresh/available, dispatchReadReady,
input or workflow capability, send eligibility, connection readiness, or trigger
completion reconciliation from old evidence. Keep the waiting/attention decision
on its existing fresh projection. Preserve strict wrong-thread/turn, inconsistent
snapshot, stale response, scope-loss and completed request failure behavior. A
known completed activity/transcript failure or current incompatible response shows
the existing unavailable/error presentation; cached totals may remain only with
the existing unavailable indication. Starting a retry must not hide that failure
behind the old healthy display. Scope retirement clears retained presentation;
pause-induced cancellation of an obsolete read is not a new request failure.

Reuse existing pageReads epochs, activityRead slot and Pi scope fences. Apply
success/failure or update the retained presentation only for the still-current
read and exact captured activityDisplayBinding. Late success/failure/finally from
a canceled, superseded or other-target request cannot overwrite newer values or
release its slot. Transcript/activity results keep the existing consistency join;
do not classify every unavailable projection as a refresh. Use the existing
pending/read completion and deadline/error signals, without a new polling cadence
or unbounded failure-suppression grace period.

Files: portal/internal/web/static/app.js; extend existing
read_cycle_browser_test.cjs and/or browser_contract_test.cjs for deterministic
deferred-response coverage; update the affected PI_ACTIVITY_ONLY section of
message_delivery_browser_test.cjs and page_lifecycle_browser_test.cjs where needed.
First quick old-red/new-green: successful idle or working display, hide/resume,
held same-target activity response, unchanged labels/counts/frozen timing until
fresh response settles, then updated values. Cover first load, completed activity
and transcript failure, failed retry still pending, recovery after success,
foreign member/thread/scope, stale/out-of-order settlements, and no dispatch-gate
change. Retain existing mismatch/freshness/terminal-completion tests. Test both
browser visibility wake and entering Conversation without duplicate reads.

Run syntax and focused existing Node contract/read-cycle checks before committing,
then independent affected review. After review, use the existing bounded activity
browser case and relevant lifecycle timing-wake assertion against disposable state;
do not launch the full native recovery or archive campaign. Root owns final package,
pin/integration/deployment ordering with any concurrent I0 work. Ordinary package
checks remain required for changed inputs; unchanged backend/Ruby/native evidence
can be reused only within its actual input scope. Rollback changes only in-memory
presentation and restores the old flicker; there is no migration. Root owns final
user-facing copy and actual usability confirmation. This brief authorizes no live
probe, resend, recovery replay, holder action or lifecycle change.

Date-separator addendum — sufficient scope amendment for the same I1 UI package,
awaiting lead acceptance. I1 retains app.js/test/index ownership; report the
activity/timing milestone independently when ready. No second implementation
task, new deployment dependency, backend/wire/schema or renderer framework.

Source boundary: renderThread calls transcriptTimestamps.observe on refresh;
createTranscriptTimestampPresentation retains exact timestamps but not previously
shown approximate timestamps. Reobserving the same entry with metadataPending
can therefore return an empty dateKey while its body remains unchanged.
patchTranscriptEntries builds no date node in that state and removes the old
separator, then recreates it when the date returns. Its existing local-day plus
occurrence key already preserves a separator for unchanged exact timestamps.
This is a concrete source reproduction path, not proof of the live message's
uncaptured metadata flags. Do not rewrite keyed rendering on that inference.

Smallest correction belongs inside createTranscriptTimestampPresentation: retain
the last actually displayed valid timestamp presentation per existing entry key
for the current thread, including its approximate quality. During a later pending
metadata episode or notice reset, reuse that known display instead of returning
an empty dateKey. Keep exact observations authoritative and separate; never
promote an approximate timestamp into the exact cache. Prefer retaining the time
value/quality and using the existing formatter so local-day/timezone formatting
stays unchanged. Reuse the current helper/maps and identity rather than inventing
another cache service. Thread change/destroy clears this retained state; existing
current-response/scope guards continue to reject another target's replies.

No valid date on first appearance still follows existing initial pending/fallback
behavior. Empty history or a newly streaming entry without a known timestamp
gains no fabricated separator. A fresh valid timestamp/date correction replaces
the old display, with exact superseding approximate as today. A completed
nonpending observation with no valid fallback does not reuse an approximate date
forever; preserve the existing exact-evidence rule for later missing metadata.
Actual message removal, filter change, a different local day, prepend pagination
and target change still rebuild the correct visible date groups through the
existing patcher. Do not suppress refreshes, freeze all separators or alter
timezone semantics. Retain the message node, selection/disclosures and scroll
anchor when its content and day grouping are unchanged.

Files: app.js helper above, refresh_presentation_contract_test.cjs, and the
existing recovery_display_browser_test.cjs single-message fixture. Smallest quick
old-red/new-green uses one immutable timestampApproximate entry: display it with
metadata complete, alternate pending/complete observations with the same key/time,
and require the dateKey/label and approximate quality to remain stable. Add the
existing warning-shown then hide/resume path, exact correction to another day and
thread reset; keep the no-date first observation negative. No live data fixture.

After quicks/commit/affected review, extend that existing browser scenario with
repeated background refreshes: capture the .transcript-date node and message
position after initial display; require continuous connection/same node, one
separator, no removal/reinsertion and stable message geometry for unchanged
content. A MutationObserver can record removed nodes so an eventual-state check
cannot miss flicker. Exercise one genuine day correction and the existing
pagination/anchor checks within their owning fixtures; no exhaustive new matrix.
If the fixed immutable exact-time case still churns, I1 reports that concrete
different cause before expanding renderer changes. This addendum does not delay
the already completed exact-target/deployment finding or authorize live probes.
