# P6-D: optional questions and Plan in Pi sessions

Owner architect2; 2026-11-12. DESIGN-D accepted; this is the sole executing
design package. Implementer4 owns P6 source after lead release; architect0 owns
technical acceptance in design.md and has accepted the independent P6-A boundary.
Exact session/environment and retained
workspace-write roster verified; unchanged procedures/documentation skill reused.
Source inspected at D `46fd1886ebebd20caba792d3aea218c42556f857`, accepted C P1
API and pinned Pi evidence H. No application edits, tests/builds or live actions.

## Sufficient independent release

Release **P6-A**: typed question/answer store, pure validation/selection,
projection and browser-controller fixtures; Plan proposal/acceptance identity
and mode-intent validation with fake ports. None requires a live worker, auth,
H0 or native admission. Implementer4 may add the isolated files below; central
registration remains with its owners. No operation is advertised merely because
its type/store exists. P6-B live integration requires the exact gates below.

Preserve the current choice-plus-free-text card and Codex behavior. Host-owned
Pi records, not transcript text or localStorage, determine question state and
reply order. An optional tool durably publishes then returns pending immediately;
it never awaits a blocking SDK/RPC dialog. Preselection/time is not an answer or
approval. No question platform, generic workflow engine or new message ledger.

## Identity, files and API

Use P2's `agentbackend.ConversationRef` for the exact Pi session/member/native
identity and incarnations. ExecutionHandle.Generation is current proof only.
Host authorization, operation support and dispatch admission remain distinct.
Browser/model arguments never select sender, native path, generation or recipient.

New D files owned by implementer4:

- `portal/internal/piquestions/{types,store,service,projection}.go` and focused
  tests: question records and answer intent only; imports domain identity and
  small injected ports, not web/server, Codex transport or worker internals.
- `portal/internal/piplan/{types,store,service}.go` and tests: immutable proposal,
  acceptance and mode intent; no second transport or tool-policy implementation.
- `portal/internal/web/pi_questions.go`, `pi_plan.go` and focused handler tests;
  `static/pi-questions.js`, `pi-plan.js` and browser fixtures. Constructors take
  injected authorization, storage, projection and dispatch ports.
- `pi-runtime/src/host-tools/questions.mjs`, `plan.mjs` and pure fake-host tests.
  P3 owns import/registration and all worker entrypoint/policy changes.

P2 alone integrates `server.go`, `app.js`, main/CLI and session mutation routing;
P3 integrates worker bridge/registration; P4 supplies resolved provider policy;
P7 packages assets/feature metadata. Supply small integration hunks, do not edit
their windows. C edits need explicit lead transfer, even while C is idle.

Per conversation private state:
`<UserStateRoot>/pi-questions/<workspace hash>/<slug>/<session incarnation>/<member>/<conversation incarnation>/questions.json`
and corresponding `pi-plans/.../plans.json`. Use existing canonical workspace
hash/private-state helpers. These stores do not choose a backend or own native
history. Each schema-1 file is owner-only 0600 in 0700 directories, strict typed
JSON with duplicate/null/unknown-key rejection, atomic replacement and file/
directory fsync under one short sibling `.lock`. Maximum 4 MiB/file; refuse
capacity exhaustion without pruning retained evidence. No automatic collection.

Before live store writers are registered, supply P2 a narrow compatibility hunk:
advertise `piQuestionsSchema:1` / `piPlanSchema:1` only for implemented readers/
writers, and refuse package targets lacking the matching field when that store
has retained state. Reuse P2's existing durable Pi-state preflight and locks;
no generic schema-guard framework or P6 edit to central host files. Pure fixture
stores are independent; compatibility registration is a live-writer gate.

Freeze these Go boundaries (routine file splitting remains implementation):

```go
// piquestions; every scope comes from trusted P2 resolution.
type LineageRef struct { AnchorEntryID, SelectionToken string }
type Caller struct {
    Handle agentbackend.ExecutionHandle
    Lineage LineageRef
    NativeToolCallID string
}
type Question struct { ID, Title string; Options []Option }
type Option struct { ID, Label string }
type PublishInput struct { Questions []Question }
type Answer struct { QuestionID, ChoiceID, Text string }
type ResponseInput struct {
    ResponseID, QuestionID string
    QuestionRevision uint64
    SupersedesResponseID string
    Answers []Answer
}
type Store interface {
    Publish(context.Context, Caller, PublishInput) (QuestionView, error)
    Snapshot(context.Context, agentbackend.ConversationRef) (Snapshot, error)
    AcceptResponse(context.Context, agentbackend.ConversationRef, ResponseInput) (ResponseView, error)
    Close(context.Context, Caller, string, uint64) (QuestionView, error)
}
```

QuestionID in ResponseInput identifies the published question set/card group;
Answer.QuestionID identifies an item within it. Publication supplies 1–3 items,
titles at most 4096 UTF-8 bytes, at most 32 choices/item with 512-byte labels;
free text is always allowed. Item/choice IDs are assigned by the host from their
original indexes, not label text. NativeToolCallID is nonempty/bounded and supplied
by P3's authenticated callback, never accepted from tool arguments. Repeated
same caller/tool-call identity plus identical input returns the same question ID;
changed input conflicts. Mint and persist one host question UUID before ACK.

The initial revision is 1 and question content is immutable. A changed question
uses a new tool call/ID and explicitly closes the old one; this first source
does not add in-place editing/version chains. The revision still fences stale
forms and is checked exactly. Closing is same-caller only, retained/idempotent,
and does not erase previously accepted answers. No timeout automatically closes
or answers an optional question.

LineageRef is adapter proof: AnchorEntryID is the native publication anchor;
SelectionToken identifies the selected branch across normal appends/restart.
It is **not** worker generation or the moving latest leaf. P3 must supply and
validate it; exact implementation is a named live gate. Ordinary new turns do
not stale a question. Branch switch, changed incarnation, closure or unknown
lineage holds/rejects new delivery, never silently retargets another branch.
Read-only snapshots may display stale records with disabled actions.

## Immutable answer intent and ordered corrections

Each file binds schema, full ConversationRef, monotonic snapshot revision and
next response sequence. Each question record retains question UUID/revision,
caller tool-call identity, lineage, immutable questions, creation time and
open/closed state. Responses append immutable response UUID, question revision,
sequence, supersedes ID, typed answers and accepted time. Delivery references
point to P3's existing operation receipt; its native witness is not duplicated.

Under the store lock, validate authorization and current question revision, then
append response plus pending delivery intent in **one atomic write before ACK**.
The same response ID/payload returns its saved result, even after later replies;
the same ID with different payload is 409 conflict. First response has no
supersedes ID. A correction must name the exact latest response for that question;
concurrent edits from the same predecessor conflict and retain the losing draft.
Responses may answer a subset of the group's items. Every subsequent response,
including an answer to a previously unanswered item, names the latest group
response as its predecessor. The projection folds ordered responses by item ID,
replacing only the explicitly answered items and preserving the others; reject
duplicate item IDs within one response. Still-unanswered cards remain usable.
Changing a previously answered item requires the explicit correction action.
The supersedes field orders group submissions; it does not erase unrelated
answers or prior evidence. This preserves the existing per-item Send answer UI.
Answers may contain a valid choice plus text or nonempty free text, never a
preselected implicit answer. Canonical answer text plus envelope must fit the
existing 20,000-byte message bound; reject before acceptance if it cannot.

Correction does not replace evidence the agent may have used. It has a new
immutable response ID and ordered delivery after its predecessor. Do not drop
pending predecessors or coalesce corrections. Unknown blocks dependent delivery;
terminal NotSubmitted remains visible/held and is not silently retried or bypassed
with a new ID. Corrections can be captured while held, but live progression past
that held predecessor needs the separately accepted attempt/resolution policy.
Unrelated ordinary user input retains its existing host rules.

Question publication takes existing runtime/caller validation and only its short
store lock: it must not wait for an answer or acquire the native message lock
held by its invoking turn. Answer acceptance is a host data write and may occur
while the exact recipient is busy/held. Archived/retired/unauthorized recipients
refuse; a stop/recovery hold is never cleared by answering. Runtime restart can
rebind the same logical recipient after proof; native identity replacement cannot.

## Live tool and ordinary-input mapping

Pure SDK factory:
`createQuestionTools({host, boundCaller}) -> ToolDefinition[]`, exporting
`request_user_input_async` with existing `{questions:[{title,options?}]}` input.
It calls `host.publishQuestion(nativeToolCallId, params)` through P3's injected,
caller-bound bridge, not a model-supplied URL/socket. Return only persisted
question ID/revision/pending status. Validation/storage failure returns error,
never an apparently published card. `plan.mjs` may supply a small trusted
proposal-publishing tool with the same binding; neither tool executes answers.
No startup installs, community extension or blocking question example is reused.

Answer dispatch uses only P3 `Controller.Bind(handle)` nullable `Send`, and
`Lookup(SubmissionRef)` with P3-owned digest calculation. Freeze action context
`question-answer:<question UUID>:<revision>:<response UUID>` and operation ID equal
to response UUID. The message is a deterministic ordinary-text envelope containing
question IDs/titles, typed answers, sequence and correction attribution as
JSON-escaped **data**, preceded by a fixed explanatory sentence. It never begins
with user text/slash commands, interpolates a prompt template or elevates an
answer to host/system instructions. Serialize once; freeze exact message/options
before handoff and validate its digest through the owning P3 helper.

Under ordinary P2 transition/runtime/team/message admission, a small
`DeliverNext` service chooses the next eligible pending response, records its
stable handoff intent, releases the store lock and invokes the proved ordinary
send mapping. It is a bounded question-specific drain, not a new scheduler.
Existing worker invalidation/idle events or explicit status checks may trigger
one drain; no independent worker service/poll loop. Busy sends are currently
unsupported: keep pending **before** calling Send. Never call it merely to learn
busy state and consume the response's terminal NotSubmitted receipt. A race may
still produce terminal NotSubmitted; keep it visible/held. No steer/follow-up
slot is advertised until separately proved.

After a crash/lost reply, consult Lookup on the exact original identity. A
prepared/dispatching/unknown or absent uncertain handoff remains held unless
P3 supplies positive permitted reconciliation. Accepted shows delivered to the
native conversation, not read/acted-on by the agent. Same-ID replay never sends
again. Recheck current branch/recipient/policy and all holds before the first
handoff; recovery Lookup itself never executes input or changes modes/settings.

Live question gates: P2 current binding/caller authorization and ordered locks;
P3 authenticated host callback, stable lineage proof, persisted receipt/digest
helper and tested ordinary envelope witness; idle/hold observation plus admitted
dispatch. P3 owner confirms these callbacks/branch mappings are not yet released;
ordinary production witness alone does not prove this whole path. Pure store,
tool-factory and fake-dispatch fixtures are independent.

## HTTP, projection and browser interface

New `pi_questions.go` handler is mounted by P2 beneath the existing resolved
conversation route, with `GET pi-questions`, `POST pi-questions/responses` and
observational `GET pi-questions/responses/<response UUID>`. The constructor takes
the existing origin/auth/ResolveRequest-based admission seam; it does not parse
native IDs from browser input. Required methods/permissions are separate from
supported features. Existing exact-origin, content-type, request-size, shutdown
and bounded-context rules apply. GET never resumes a worker.

200 returns a typed snapshot/known response; 202 acknowledges a durably captured
answer with its explicit pending/held/delivered status, not native acceptance.
Malformed fields 400, oversize 413, stale revision/closed question/changed lineage
or immutable-ID conflict 409, absent authorized object 404, denied access existing
403 behavior, unsupported feature 501, transient store/admission failure 503.
No private paths/raw SDK errors; never translate generic failures into notSent.

`QuestionView` exposes opaque question ID/revision, display recipient, item/choice
IDs/text, latest response and typed pending/held/delivered/stale/closed status,
server snapshot revision and explicit allowed actions. No native proof token,
socket, credential or raw runtime handle. Reconnect loads a full bounded snapshot
and merges by snapshot revision; old responses cannot roll back newer state.
Use existing Watch invalidation and refresh behavior, not a new event replay API.
LocalStorage retains only drafts and the exact pre-network response ID/payload.
Server snapshots determine persisted/delivered state. Preserve drafts on all
stale/failed replies; refreshing never auto-submits.

New D browser factory:
`mountPiQuestions({root, api, storage, namespace, renderCard, onChange})`
returns `{update(snapshot), inline(entry), renderPinned(container), destroy()}`.
`api` offers `read`, `respond`, `responseStatus`; its request wrapper is injected.
The existing composer remains independent. A correction is an explicit new
action using a fresh response ID/supersedes value; a check action only queries
delivery. Display the server's held/NotSubmitted state without the legacy
automatic-retry affordance. Normal turn completion or ordinary user input does
not silently close server-owned optional questions.

Proposed C transfer: extract a presentation-only `createQuestionCard` export
from `conversation/assets/questions.js` (existing DOM/classes/keyboard helpers),
with explicit question/draft/view-state and submit/change/dismiss/check callbacks.
Keep `createAsyncQuestions` defaults and legacy reply envelope byte-compatible;
its old state machine remains the Codex owner. The new D wrapper passes server
state to the card. No C Go DTO change is needed for the first store-backed panel;
existing neutral AsyncQuestion projection can attach inline display by anchor
when P3 supplies actual provenance. No synthetic native transcript entries.
Without lead C transfer, implementer4 can test D controller against fake renderCard.

## Plan/Default and accepted-plan identity

Pi initially advertises no Plan/mode capability. P6-A can implement pure stores
and browser selection logic now; actual Plan support requires P3 to apply and
confirm the selected mode's host policy across **all** enabled built-in/custom/
MCP/codemode/delegated tool paths, including instructions/resource loading.
Mode is independent of account/model selection and retained member access.
Do not treat PolicyRevision or a saved mode string as enforcement. Do not use
the upstream regex-bash example or claim stronger OS read-only isolation than
the current trusted-host contract. Unknown effective policy disables Plan and
implementation controls. Default may not broaden the member's allowed access.

`piplan` stores immutable proposals `{planId,revision,ConversationRef,LineageRef,
nativeOrigin,text,textSha256,complete}` and acceptances
`{acceptanceId,planId,revision,textSha256,originalMode,targetMode,policyRevision,
operationId,phase}`. textSha256 is SHA-256 of exact displayed UTF-8 plan bytes;
do not normalize accepted plan text. `nativeOrigin` must be a proved completed
native plan/tool publication, not a Markdown heuristic. Bounded max plan/message
size is the existing 20,000-byte input limit. Phase is only prepared/mode_pending/
dispatch_pending/held/accepted; native outcome stays in P3 receipt.

APIs: `PublishProposal(ctx,Caller,text,NativeOrigin)`,
`Accept(ctx,ConversationRef,{acceptanceId,planId,revision,textSha256})`,
`Snapshot(ctx,ConversationRef)` and observational `LookupAcceptance(ctx,ref,id)`.
Plan publication is caller-bound/idempotent like questions and never accepts
itself. Acceptance requires current active session, exact selected backend/member/
lineage, completed current proposal, idle eligible recipient and authorized
mode policy. Repeated identical acceptance returns the retained result before
checking a now-newer plan; changed ID payload conflicts. A fresh acceptance of
a stale/newer-superseded proposal refuses. Same plan cannot acquire a second
implementation operation merely through another browser tab/ID.

Persist acceptance + fixed operation UUID before applying Default. Under the
ordinary conversation mutation owner, apply and positively confirm effective
Default policy, then send the immutable implementation request through P3 with
action `plan:<planId>:<textSha256>`. The body includes the exact accepted plan as
data, so later model context changes cannot replace it. Mode-change lost ACK
requires observational reconciliation, not blind repetition; uncertain policy
or input holds the same acceptance. Do not roll back to Plan after a potentially
submitted implementation or mint a new operation ID. NotSubmitted is terminal
under current P3; duplicate acceptance checks it without redispatch/settings
changes. Question and Plan admission serialize with ordinary input; store locks
are released before native calls. No cross-backend/new-development-session Plan
action is exposed by this initial source; P2-C kind=new remains unchanged.

New `mountPiPlan({root,api,storage,namespace,onChange})` reuses current Plan panel
controls and mode button rendering through injected DOM hooks, with snapshots,
exact ID/digest, explicit supported actions and accepted-ID status checks.
P2 supplies tiny `app.js` hooks; legacy renderPlanActions/implement-plan routes
remain unchanged. Mode selection UI appears only with actual enforcement;
intent/selection fixtures never imply availability. Accepted plan approval is
limited to that implementation request, not merge/deployment/lifecycle permission.

## Checks, dependencies and source limits

Pure fixtures cover duplicate publish/lost ACK; tool-call changed payload;
response-ID immutable retry; choice plus free text; no preselection submission;
ordered concurrent corrections; stale revision/closed/branch/incarnation;
reconnect without worker; capacity/private-file/strict-schema refusal; crash
after capture/handoff; Unknown/terminal NotSubmitted without resend; preserved
draft/keyboard/focus; Plan exact digest/duplicate tabs/newer plan; mode ACK loss;
no policy support means absent controls; no native call from any read/render.
Use fake auth/caller/lineage/admission/receipt ports, no live providers/tools.

Quick checks after implementation in D's Nix environment: focused
`go test -mod=readonly ./internal/piquestions ./internal/piplan` from portal,
selected new web handler fixtures and `node --test` for new browser/host-tool
fixtures. Retain existing optional_questions_browser_test.cjs,
required_question_keyboard_browser_test.cjs, plan_decision/plan_delivery Go
cases. If C transferred, run its existing questions/browser contract checks
plus new presentation fixtures. Long/uncertain checks require fresh watcher;
lead owns final review after committed source/quick checks. No tests run here.

Live gates remain explicit and separable: host callback + lineage (publish),
proved data-envelope ordinary dispatch/receipts (answers), enforced mode policy
plus bound proposal publication (Plan), accepted-plan dispatch mapping (implement).
H0/P2 writer/native ownership remain prerequisites for all real execution.
No fresh provider/login proof is required for pure source or fake fixtures.

Sources: accepted [H evidence](extension-and-question-evidence.md),
[main plan](implementation-plan.md#host-tools-teams-questions-and-plan),
[P1/P2 contracts](implementation-contracts.md), design.md P3 source brief;
C `conversation/assets/questions.js:38–270`, `codex/async_questions.go:10–25`,
neutral `conversation/backend/types.go`; D `web/static/app.js` current
createAsyncQuestions/renderPlanActions/saveCollaborationMode seams,
`web/server.go:2740–2905`, `web/plan_delivery.go`,
`piruntime/types.go`, `pi-runtime/src/session.mjs`. P3 owner confirmed busy
steer/follow-up, Plan enforcement and host callback/lineage are not released;
durable supervisor receipts are still implementation work. No upstream inventory
or extension shopping repeated. New Pi-only host formats; no legacy conversion.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>
