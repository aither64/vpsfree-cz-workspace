# BRIDGE-D: Pi host callbacks, lineage and Plan enforcement

Architect2, 2026-11-12. P6-D accepted; this is the next bounded design package.
Architect0 has technically accepted B1 and the exact B2 policy port/format in
design.md; lead allocates source windows. B2's guard/package and enforcement
implementation remains independent of B1.
Session/current/environment and retained architect2 settings verified. Documentation
skill applied. Source inspection: D `67e08f2f10faa288aefb7e97e2d3eb19d8819eb6`,
C `1a0fd1856ad02023f02670022195948022e89683`, pinned Pi
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`. No application edits or runtime checks.
This extends [P3](design.md), [P5](pi-team-plan.md) and [P6](pi-question-plan.md);
their authority, receipt and retained-state fences still apply.

## Release boundary

**B1 is independently implementable:** bounded duplex callback framing, caller
validation, native origin/linear-lineage proof and reconnect/refusal fixtures.
Wire the existing P5/P6 factories through injected domain handlers. P3 owns the
transport and worker integration; P2 owns portal composition. Existing stores,
receipts and supervisor are sufficient; add no listener, daemon or callback ledger.

**B2 is the small Plan implementation:** an explicit tool allowlist and one trusted
inline policy extension, idle mode change, positive applied-policy observation and
P6 acceptance/ordinary-send composition. It follows B1 but need not delay B1 source.
Advertise each tool only after its domain writer/admission/receipt and native proof
are connected. The presence of a factory or framing version is not that proof.
P5 utility/communication gates remain those in TEAM-I; no invented roster member.

## Transport and concrete ports

Current `pi-runtime/src/protocol.mjs`, `piruntime/worker.go` multiplex requests and
invalidation on inherited stdin/stdout. `piruntime/transport.go` uses one bounded
request/reply per same-UID `control.sock` connection. Extend these existing paths:

```go
// piruntime; additive optional interface, not new required Controller methods.
type HostCallbackConnector interface {
    AttachHost(context.Context, RuntimeRef, HostCallbackHandler) error
}
type HostCallbackHandler interface {
    HandleHostCall(context.Context, HostCall) (HostReply, error)
}
// Optional projection implemented by trusted host composition.
type HostToolProvider interface {
    HostTools() []string
}
type HostCall struct {
    Runtime RuntimeRef
    Subject CallbackSubject
    InputOperationID, AnchorEntryID, NativeToolCallID string
    SelectionToken, Tool, ArgumentsSHA256 string
    Arguments json.RawMessage // decoded only by the named domain handler
}
type CallbackSubject struct {
    Kind string // exactly conversation or utility; exactly one arm
    Conversation *agentbackend.ExecutionHandle
    Utility *UtilityCallbackSubject
}
type UtilityCallbackSubject struct {
    Session agentbackend.SessionRef
    MonitorOperationID, Incarnation, NativeID, Generation string
}
type HostReply struct {
    Outcome string // result, refused, unknown
    Body json.RawMessage // bounded, exact per-tool result; no untyped domain state
    Code string // unavailable, invalid, scope, stale, conflict, canceled, unknown
}
```

P3 owns these private values; higher `pihosttools` composes domain handlers and
imports P3, never the reverse. TEAM-I can supply its utility identity conversion
without making utilities into `ConversationRef`. An absent optional connector
means callback tools unavailable. Capability names in the private worker handshake:
`hostCallbacks:1`, `linearLineage:1`, and later `planPolicy:1`; absent is unsupported.
Do not change the meaning of existing `workerProtocol:1` or advertise unfinished
features. P7 includes these fields only after matching source/checks.

**Available-tool projection (technically accepted B1 clarification, recorded in
design.md).** `AttachHost` type-asserts
the handler's optional HostToolProvider, calls HostTools once, validates and copies
the returned list for that live attachment. An absent interface or nil/empty list
means no host tools, never all installed factories. Trusted `pihosttools` composition
derives the list only from bound, released domain handlers; browser/model arguments,
environment and installed factory presence are not its origin. Accept only sorted
unique exact names from the finite domain-tool table below; unknown,
duplicate or invalid names reject the attachment before registration. No wildcard
or new manifest/store is introduced.

Send that snapshot as `tools` in the existing private host_attach body. At trusted
worker setup pass `hostTools` in the existing init config, containing the intersection
of attachment tools, that exact subject's permitted factory ceiling and any applied
tool-policy ceiling. Register only those factories through customTools; absent
hostTools is empty. Utility gets only its released monitor_operation operations;
Plan publication/mode does not become available from this list without B2 proof.
Tool support, subject authorization and current admission remain separate. Before
forwarding each callback require membership in both the worker's captured set and
the current attachment set, then run the existing domain/identity/input checks.

Reconnect can retain a worker's already captured set when the new attachment still
supports it; extra available names do not silently expand a live worker. If any
captured name is unavailable, block new input to that affected worker and
refuse an unforwarded affected call; a previously forwarded call still uses its
domain's Unknown/reconciliation rules. A disconnected handler is not a new supported
operation. Do not reconfigure tools during a run/callback or add an automatic
reload. Establish a changed worker factory set only through the existing separately
authorized idle creation/load path and policy checks. This adds availability
framing, not execution permission, an attachment lease ledger or a new service.

Worker frames retain schema1/current identity and gain a discriminant:
`event:"host_call"`, `id:<transport UUID>`, and body containing inputOperationID,
anchorEntryID, nativeToolCallID, selectionToken, tool, arguments, argumentsSHA256.
Supervisor replies on stdin with `op:"host_result"`, same id/current identity,
body `{outcome,body?,code?}`. `host_cancel` carries only the same correlation ID.
These frames are dispatched separately from ordinary command replies; an active
Send cannot block them. stdout remains protocol-only; diagnostics use stderr.

`AttachHost` opens the existing socket with a distinct `operation:"host_attach"`
request. After exact runtime/schema/UID validation the connection becomes duplex:
an attachment UUID plus correlated call/result/cancel frames. At most one live
attachment per runtime; reject a second until the previous connection is closed.
Reattachment creates a new transport attachment UUID, not new operation identities.
Ordinary control calls, abort and hold remain independent. Validate both peers as
today; no browser URL, token, socket or process environment selects the callback.

Limits: existing 1 MiB frame ceiling, tighter 64 KiB callback body and existing
domain limits (questions/team text 20,000 bytes); at most 16 outstanding callbacks
per worker and 128 per supervisor. Strict UTF-8, known fields/discriminants,
duplicate-key and correlation checks; overflow refuses before handler admission.
Use a 30-second callback deadline, bounded by the SDK AbortSignal/host context.
Timeout is **unknown after forwarding**, never proof of no effect. These are
bounded in-memory correlation maps, not durable delivery queues.

## Caller authority, identity and recovery

The factory receives a P3 closure, never a model-selected caller. P3 reconstructs
Subject from the owned worker and current runtime mapping, and captures the active
original input receipt before invoking `session.prompt`. Preserve its exact
SubmissionRef/frozen settings until the run is settled; Accepted input is not
finished execution. Utilities use the original monitor input and P3 utility mapping.
Before **any side-effecting host handler**, require that exact original retained
or utility input receipt durably be Accepted, including its native witness. A
prepared/dispatching receipt waits within the bounded callback deadline without
holding receipt/message/store locks or blocking witness publication; Unknown or
NotSubmitted refuses/holds. Native tool origin alone is not accepted-input proof.
The request's echoes must match that trusted state. Revalidate generation, session,
member/utility incarnation and operation immediately before domain admission.

Immutable native invocation identity is `(subject durable identity, original input
operation ID, assistant entry ID, native tool-call ID, tool name)`. Runtime generation,
attachment/correlation IDs and deadlines are execution fences only. Compute argument
SHA256 from the exact UTF-8 JSON emitted by the bridge and verify it at each hop;
the host validates typed arguments. This is not a replacement for the domain's
existing immutable request digest. The native persisted tool arguments must match
the decoded arguments exactly; changed replay conflicts.

The worker proves one persisted assistant message containing exactly this top-level
tool-call ID/name/arguments, descended from the original input witness. Read through
public `SessionManager.getEntries/getEntry/getBranch`; independently reopen the
existing mapped regular history file and compare native ID and exact entry.
Pi emits message_end before persistence, so leave that callback before reading;
do not accept a public event alone. Nested tool calls lack standalone transcript
entries and are **not supported for host callbacks in B1**. Unknown/missing/duplicate
origin refuses without a host effect. No raw JSONL writes/private Pi methods.

The handler uses the existing domain's durable idempotency:

| Tool | Existing authority/result owner |
| --- | --- |
| request_user_input_async / publish_plan | P6 store, exact caller+native origin+arguments; persisted question/proposal ID before successful result |
| report_to_lead / team_message | P5 existing team message ID/envelope/receipt and current sender/recipient admission |
| session_communication | Existing exact-pair grant/message record; lead-only, only after TEAM-I typed codec/admission release |
| monitor_operation | Existing operation record; utility may only status/report its exact original operation; retained caller uses existing lead permissions |

Forward a cancellation to the active handler and abandon the waiter, but never
erase domain state or interpret cancellation as undo. SDK abort does not authorize
session stop or prove descendant exit. A result from the wrong attachment/runtime
is discarded; its durable domain receipt remains authoritative. Do not hold the
supervisor receipt mutex, per-conversation message lock or a store lock while waiting
for the host. Publish-question/plan handlers only validate/read native proof and
write their short store transaction; they do not reacquire the invoking turn's
message lock. Delivery to another member takes ordinary recipient admission.

Lost portal ACK/reconnect: the still-live invocation can reissue its **same**
immutable request through the new attachment, using the domain's serialized
lookup/idempotent admission. Dispatch again only where that domain proves no prior
dispatch and still owns admission; Unknown/Accepted/terminal NotSubmitted never
resend. A domain without such a path is absent/held, not automatically replayed.
After worker/supervisor loss, reconcile domain state and native input/tool-result
history; do not resume the tool by calling a new `prompt`. Browser reconnect simply
reads P6/P5 snapshots. Tool result loss may leave a visible durable pending question
or report even when the model saw an error; do not create a second one to fix it.
Drain/utility settlement includes active callback handlers/waiters and native
tool handles plus original input outcome; SDK idle/final text alone is insufficient.

## Stable lineage with the supported initial branch surface

The pinned public SDK exposes tree entries/parents, but no durable branch-selection
revision. `branch()` only changes the in-memory leaf; reopen chooses the last stored
entry. A latest-leaf or runtime-generation token would be incorrect. B1 therefore
supports **one append-only linear native selection**, matching current P3 operations:
no fork, tree navigation, session switch, content replacement or arbitrary extension
command is exposed. This is a concrete functional question/Plan path, not a future
branch-management framework.

Set `SelectionToken = "linear-v1:" + lowercaseHex(SHA256(LP32-UTF8-v1(tuple)))`.
The exact ordered tuples are:

```text
["conversation", workspace, slug, sessionIncarnation, member,
 conversationIncarnation, nativeID, rootEntryID]
["utility", workspace, slug, sessionIncarnation, monitorOperationID,
 utilityIncarnation, nativeID, rootEntryID]
```

Neither contains generation nor input-operation ID. `LP32-UTF8-v1` is the unsigned
32-bit big-endian element count followed, for each string, by its unsigned 32-bit
big-endian UTF-8 byte length and those exact bytes, without normalization, BOM,
terminator or separators. Reject invalid UTF-8/unpaired surrogates. The cross-language
encoding fixture `["a","é",""]` is hex
`00000003000000016100000002c3a900000000`; Go and JS must also agree on full retained
and utility fixture tuples with non-ASCII path data. It is derived, not another
saved record. P6 itself accepts only retained conversations.
AnchorEntryID is the assistant tool-call entry, never
the current leaf. Native root and anchor must already exist on disk; an empty native
session cannot publish. The same token survives ordinary appends and process restart.

At publish, reload, answer/Plan admission and immediately before ordinary dispatch:
validate unique IDs, one root, every chronological entry's parent equals the previous
entry ID, and public getBranch() equals that complete sequence. Require current
native leaf equal its final entry, exact saved anchor content/tool arguments and
at live publication ancestry to the original Accepted input. For retained P6
actions, the content-aware historical check below verifies the saved origin;
it does not substitute the current input for that original publication proof.
Append-only compaction/model/system/label entries
are allowed while their parent chain stays linear. Refuse branch_summary and content
replacement entries for this first path, even if they would produce a linear tail.
A branch change without append fails the leaf/branch comparison; with append it
fails the complete chain. Divergence after restart remains refused. An unpersisted
external switch that disappears on restart is not a retained native selection;
no imported/live third-party writer is supported.

The trusted inline extension cancels public before-tree/before-fork/before-switch
events with `{cancel:true}`, and P3 exports none of those commands. Native file changes that cannot be
proved as this ordinary linear extension hold affected question/Plan admission.
Supporting actual branch selection later needs an explicit persisted selection
contract; do not silently substitute a new token to make stale answers acceptable.

### Retained P6 origin inspection

Technically accepted B1/P6 clarification, recorded by architect0 in design.md;
lead retains source allocation. The live callback verifier above still proves its original
durably Accepted input before publication. A later question/Plan action cannot
reuse that verifier's current active-input pointer: another turn or restart may
have replaced it. Add this optional retained-conversation read port in `piruntime`:

```go
type NativeOriginRef struct {
    AnchorEntryID, SelectionToken, NativeToolCallID, Tool string
}
type NativeOriginObservation struct {
    Handle agentbackend.ExecutionHandle
    Origin NativeOriginRef
    Arguments json.RawMessage
}
type NativeOriginInspector interface {
    InspectNativeOrigin(context.Context, agentbackend.ExecutionHandle,
        NativeOriginRef) (NativeOriginObservation, error)
}
```

Use the existing bounded request/reply transport and worker command dispatch with
the distinct `inspect_origin` operation, not host callback forwarding. P3 resolves
the exact current mapped handle/native ID/cwd; callers supply no native path.
Require the existing linear-chain/token checks, exactly one top-level assistant
tool call with that ID across the selected history, at the exact anchor and with
the exact tool name. Require existing regular history before public reopen, and
current/reopened identity, entries and anchor equality. Return copied native
arguments bounded by B1's 64-KiB limit, plus the exact checked handle/ref. Invalid
arguments/shape, duplicate IDs, missing anchor, branch divergence or token mismatch
refuse. Missing port, unsupported worker or cold/unavailable native mapping is
unavailable; stale scope/generation refuses under existing P3 errors. Use existing
B1 bounds, correlation, cancellation and current-generation response validation.
No load/create/prompt, callback, file write, policy change or held-state clearing.

The persistence-equality clarification is technically accepted and mirrored in
design.md. For memory-versus-public-reopen equality, compare the complete entries and selected
anchor in their persisted JSON representation: exact `JSON.stringify` output with
no replacer, sorting, pruning or custom normalization. Implementer1's owned SDK
fixture found optional in-memory `undefined` properties that native JSON omits;
JavaScript deep equality would reject that otherwise identical persisted history.
This clarification changes only the persistence comparison. Independently validate
both histories' IDs, parent chain, scope and origin; retain argument shape, bounds
and Unicode checks and refuse serialization failure. Do not weaken native tool
identity or P6's saved-content comparison. Fixture evidence and the focused SDK
rerun remain implementer1-owned; this paragraph does not claim a passing rerun.

This historical observation does not establish a new Accepted input or authorize
a host callback. The trusted domain record came from the original live publication
gate; it supplies saved origin and content. No original input ID is guessed from
the latest turn, no callback ledger is added, and utility authority is unchanged.
The saved caller remains immutable. Host resolution may obtain a current generation
only for the same exact durable ConversationRef; never rewrite caller/token/anchor
to make a stale record pass.

P6 reconstructs expected content from its immutable record and checks returned
handle/ref exactly before comparing arguments. For `request_user_input_async`,
strictly decode `{questions:[{title,options?}]}` with the existing item/text bounds,
rejecting unknown fields, null and wrong types. Compare question order, title bytes,
option order and label bytes to `QuestionRecord.Questions`; stored numeric item and
option IDs must be the existing canonical indexes and are not native arguments.
Only omitted options and an empty options array are equivalent: the existing
`canonical` store function already collapses them. Do not trim, sort, normalize
Unicode, or compare title alone. For `publish_plan`, require exactly `{text}` equal
to `Proposal.Text`, its existing digest, complete origin and `NativeOrigin.EntryID`
equal to caller anchor. P3 knows neither domain's schema; P6 owns these strict pure
comparators. Raw JSON byte equality cannot be reconstructed from existing question
records and is not claimed. No Caller or persisted schema change is needed.

Add `Dispatch.VerifyOrigin func(context.Context, Caller, QuestionRecord) error` in
`piquestions` and `Ports.VerifyOrigin func(context.Context, Caller, Proposal) error`
in `piplan`. The passed caller is host-resolved current authority and the record is
the selected immutable content. Production adapters use NativeOriginInspector;
nil is unavailable for new native effects. Verify outside domain locks under the
existing admission, before new Apply/Prepare/Send. Existing receipt/status lookup
and exact duplicate results remain observational and need no new origin proof;
unknown/terminal outcomes still confer no resend permission.

Plan's private acceptance helper should accept an invocation-local
`inspect(context.Context, ConversationRef, Proposal) (Policy, error)` callback.
The admitted wrapper resolves current caller, verifies origin, then performs its
policy-only Check; the short capture rechecks the exact selected proposal/caller.
Question HTTP response capture needs the equivalent small admitted Store wrapper:
duplicate lookup first, select immutable QuestionRecord outside its short lock,
resolve/inspect there, then pure scope/content/revision/predecessor recheck inside
capture. Neither `Validate` nor any callback in `StateFile.Update` may invoke native
inspection. Live callback publication consumes its already proved HostCall without
a second native call under the domain lock. GET/Snapshot/render remains native-free;
the accepted observation projection below owns display eligibility.

P3 owns optional Go/transport/worker/lineage changes; P6 owns comparators, service
ports and capture wrappers; P2 owns production composition/invalidation. Existing
owner windows apply and lead releases these continuations. Narrow source check at
D HEAD `1e457834e23a2bda09e528ac8c532c16e912c33b2` plus working-tree source:
`pi-runtime/src/{lineage,host-bridge}.mjs`, `host-tools/{questions,plan}.mjs`,
`portal/internal/piquestions/{types,store,service}.go`, and
`portal/internal/piplan/{types,store,service,policy_adapter}.go`.
Fixtures: ordinary append/later input/restart succeeds with the original anchor;
wrong native ID/generation/root/tool/anchor/content or branch refuses; omitted/empty
options compare equally but null, reordered/changed labels and unknown keys refuse;
no active-input dependency, effects or native calls under store lock; capture race
and original duplicate/status lookup remain safe. Pinned SDK fixtures prove public
reopen wiring; design inspection is not execution evidence.

## Plan/Default mapping and mode proof

Use public `createAgentSession({tools,excludeTools,customTools,...})` with an explicit
hard ceiling, no `+/-` modifiers, no ambient extension discovery. Keep current
noExtensions/noSkills/noPromptTemplates defaults; add only the package-owned inline
policy extension through `DefaultResourceLoader.extensionFactories`. Explicitly
exclude `mcp__*`; do not load the MCP factory. This matters: a plain SDK allowlist
otherwise retains MCP tools for codemode/tool_search, and registered deferred or
codemode tools remain callable even when inactive.

| Route | Initial Plan | Initial Default |
| --- | --- | --- |
| Builtins | read, grep, find, ls | same plus bash, edit, write, intersected with effective execution policy |
| P6 | request_user_input_async; publish_plan | request_user_input_async; accepted-plan action is host/browser admission |
| Retained team report/peer; cross-session communication | absent: can wake a less-restricted agent | only released exact host permissions/receipts |
| Monitor/delegated/subagent routes | absent, including shell-driven spawn tools | only released TEAM-I exact utility policy |
| MCP, codemode, tool_search, other custom/extension tools | absent | absent in this initial bridge; independent later mapping required |
| Arbitrary SDK/UI commands, user bash escape | absent | absent; ordinary builtin bash is the admitted Default path |

Do not advertise Plan for a worker whose required installed tool family cannot meet
this mapping. Remedy is either keep that family disabled for the declared limited
Pi capability, or add tested mode-aware registration/execution/delegation checks;
never silently keep it enabled. This does not claim all Codex tools already ported.
Saved role access/instructions remain intact; Default never broadens the effective
policy selected by the host. Plan disallows agent workspace mutation through its
available tools; normal host history/questions/plan writes still occur. It is not
an OS read-only sandbox against the trusted local operator or arbitrary local code.

All admitted tools have `direct` exposure; no reachesTools router or late registration.
At idle mode change, use public `session.setActiveToolsByName(exactNames)`, then verify
`getActiveToolNames()` **and** `getCallableToolNames()` equal the intended set, and
`getAllTools()` is within the registered ceiling. Missing/extra tools fail closed.
The trusted inline extension checks the frozen run policy at before_agent_start and
tool_call, blocks any disallowed call, and supplies explicit Plan/Default instructions
through the public before_agent_start systemPrompt result. Instructions describe
mode/access/optional answers and never replace enforcement. No regex bash filter.
The `tool_call` refusal result is `{block:true,reason:<bounded explanation>}`;
the before_agent_start result uses `{systemPrompt:<retained prompt plus mode instructions>}`.
No mode switch while tools, callbacks, prompt preflight or a run remain active.

The exact optional P3 port and persisted format are authoritative in
[design.md's accepted B2 contract](design.md#bridge-d-sufficient-authenticated-callback-and-linear-lineage-source-release):
`InspectToolPolicy(context.Context, agentbackend.ExecutionHandle) (ToolPolicyProof, error)`
and `ApplyToolPolicy(context.Context, agentbackend.ExecutionHandle, uint64, ToolPolicyTarget) (ToolPolicyResult, error)`.
The uint64 is expected current policy revision. ToolPolicyTarget carries the full
Mode/Revision/Digest/Active/RegisteredCeiling; proof carries current generation,
verified active/callable/registered sets and Applied, with result outcome
`applied|rejected|unknown`. This replaces the earlier provisional mode/digest-only
Apply signature. The policy revision/digest is independent of P4 EffectiveSettings
and submission receipts; P3 owns the exact digest encoding specified there.

For the numeric JSON wire, tool-policy Revision and Apply's expected revision
are integers in `1..9007199254740991` (2^53−1), validated in Go and JS before
mutation. At the maximum, a normal increment refuses; an exact same-target
duplicate may still return freshly verified Applied. This limit applies only
to this tool-policy contract, not unrelated Go uint64 identities/revisions.
The digest continues to exclude revision.

RegisteredCeiling is fixed for a loaded worker: ordinary Apply requires exact
equality with its trusted bootstrap ceiling and retained applied policy ceiling.
Plan/Default changes Active within it; Apply neither broadens nor narrows the
ceiling. Even a narrower list containing today's registered tools is not a new
supported Apply mode. Changed saved access/composition that requires another
ceiling holds affected admission until a separately authorized composition/load
contract supplies the complete new policy; it cannot trigger automatic reload
or be smuggled through an ordinary mode change. Existing Load reapplying an
unchanged retained policy is unaffected. This fixes the initial implementation
boundary without claiming that a new ceiling-replacement operation exists.

Use schema-2 P3 conversation mapping with exactly the accepted ToolPolicy and
PendingToolPolicy additions, and optional complete Revision1 CreateRequest.ToolPolicy.
Schema1 or nil policy remains unavailable; no inferred Default, upgrade or migration.
Utility mode support remains absent. The accepted `piToolPolicy:{policy:1,conversationSchema:2}`
runtime-contract guard/package window must precede policy writers, including cold
mapping retention checks and existing schema4 old-candidate fences. B1 needs none
of these policy-state additions.

**Initial Create replay (technically accepted B2 clarification, recorded in
design.md).** Do not add InitialToolPolicy or
hide its digest in provider settings/submission receipts. A schema2 policy-bearing
Create replay may compare the complete requested Revision1 target with the current
policy only while that policy is still Revision1 and no pending/contradictory state
exists; all existing P3 creation-ID/mapping/native-proof requirements still apply.
A different target, nil-versus-policy payload or creation identity conflicts.
Once current revision is greater
than 1, the original policy payload is no longer provable from this exact two-field
format: refuse Create replay without effects (`ErrUnavailable` with that reason),
even if the current mode/digest happens to match. The existing authorized
Load/Inspect/creation-proof paths remain available under their own preconditions;
they do not become automatic fallbacks or new creation permission.

Fresh Create persists PendingToolPolicy before native setup. A repeated Create
observing pending, unknown or partially applied initialization remains held
(`ErrHeld`); it must not restart setup, clear pending or reissue creation merely
because the request matches. Successful initial publication clears pending only
after the accepted native sets/hook and durable-policy proof. No new ID, field,
ledger, inferred initial target or retry exception is introduced. Fixtures cover
exact Revision1 replay, changed Revision1 target, revision advancement including
return to the same mode/digest, and interrupted pending setup with zero replay effects.

Apply persists pending before native changes, verifies the exact sets/hooks, then
durably publishes applied state before ACK. Inspect is observational and cannot
load, apply or clear a hold. Restart with pending policy remains held; an otherwise
authorized Load verifies the full retained applied policy before input/callback.
Use the full accepted admission, duplicate, failure and fixture rules in design.md;
an SDK string, stored PolicyRevision or cached Applied flag is not enforcement proof.

P6 persists acceptance/operation ID before requesting Default. After exact policy
proof it submits one ordinary message with original acceptance ID and frozen plan
digest/context via P3's existing receipt path. Ordinary question answers similarly
use their saved response ID/envelope. Pass `expandPromptTemplates:false`; no slash,
custom-message privilege or synthetic tool-result injection. Accepted still means
native input acceptance. Busy stays pending before submission; Unknown or terminal
NotSubmitted stays held under the original receipt. A lost mode ACK is inspected,
not permission to repeat a send. Publish-plan completion means a complete persisted
assistant tool invocation carrying the exact proposed text and a successful host
publication; it does not mean the turn or implementation has finished.

**Concrete P6 acceptance sequencing/token (technically accepted by architect0
and recorded in design.md).** The admitted HTTP
Accept wrapper first authorizes/resolves the exact conversation, then reads and
validates existing acceptance identity and selected latest proposal under short
store access. Exact duplicate returns the saved acceptance before any live policy
call, even if newer proposals exist; changed duplicate/second acceptance conflicts.
For a new acceptance, release the store lock and call InspectToolPolicy while the
ordinary host admission ownership is held. Obtain current caller/lineage and
positive idle/eligible/enforced policy proof there, then capture under a new short
atomic update which rechecks the exact proposal, caller and duplicate/CAS conditions.
If they changed, refuse rather than reuse the earlier observation.

No native/controller/lineage observation occurs inside StateFile.Update, including
through injected PolicyCheck or Validate callbacks. Only invocation-local immutable
observations and pure rechecks may be supplied to that transaction; never mutate a
shared FileStore callback to carry one request's proof. Snapshot/Lookup remain
native-free and cannot synthesize positive live enforcement from stored state.
Ordinary admission must exclude competing dispatch/mode changes until capture;
Apply later rechecks its expected revision and current authority as already required.

The existing acceptance.PolicyRevision string freezes this exact ASCII token:

```text
pi-plan-policy-v1:<originalMode>:<originalRevision>:<originalDigest>:<defaultDigest>
```

Reject any other field count/version, whitespace, noncanonical decimal (including
leading zeroes), revision outside 1..2^53-1 or non-lowercase-64-hex digest; maximum
192 bytes. originalMode is exactly plan or default. Digests are P3 ToolPolicyDigest
values, not newly computed P6 encodings. For original Plan, target Default revision
is originalRevision+1 and must be representable before acceptance is saved. For
original Default, target revision is unchanged and defaultDigest must equal
originalDigest: this is an already-applied exact mapping, not a same-revision
composition change. Existing proposal eligibility still applies in both cases.
The acceptance's existing ConversationRef/caller/plan and operation IDs bind the
token's scope; it grants no authority by itself. No schema field, tool-array copy,
provider-policy revision or second ledger is added.

Apply recomposes the full Default target from trusted host composition with the
same fixed registered ceiling, verifies its digest equals the frozen defaultDigest,
and uses the exact derived target revision/expected original revision. Changed host
composition or permissions refuse/hold, never replace the accepted token. After a
lost ACK, Observe uses Inspect only: require positive current-generation Applied
proof for exact Default mode, target revision, digest and full verified sets/hooks.
A later revision with the same digest is not this acceptance. Pending/Unknown or
any mismatch stays held; observation does not call Apply, create a replacement
operation or change token/settings. Existing P3 receipt reconciliation still owns
ordinary input outcome and no-resend semantics.

Fixtures add a native-call-under-store-lock sentinel, proposal change between read
and capture, exact duplicate without Inspect, concurrent acceptances, changed
target composition, original Default digest disagreement, max-revision overflow,
malformed token, and lost Apply ACK with exact target versus same-digest later
revision. These are P6/B2 adapter refinements within existing owner windows.

**P6 browser capability projection (technically accepted B2 clarification,
recorded in design.md).** Keep FileStore
Snapshot/Lookup and HTTP GET/render native-free. P6 may expose a small optional
injected observation/projection port with pure fixtures; without that injection,
CanSelectMode/CanAccept remain false. Supplying the production observation through
P2's existing runtime refresh/invalidation ownership is a separately released P2/P3
composition dependency, not a claim that the current cache already carries this
proof. It remains required for functional UI acceptance; do not replace it with a
P6 polling loop/cache service or leave the dependency unnamed.

The injected value is a typed immutable host observation, not an Applied boolean
or browser token: bind the exact ConversationRef/current ExecutionHandle and
binding revision to the full ToolPolicyProof and the corresponding retained
policy mode/revision/digest/ceiling, no pending/held state, observed idle eligibility,
and the released operation/domain guards plus currently bound host-tool set.
For CanAccept, also bind the exact latest proposal ID/revision/text digest/caller
and its validated current lineage. Pure projection compares those values with
the authoritative scope and current store snapshot; any absent/unknown/mismatched
component leaves the respective control absent. Available operations, host
authorization and provider/auth availability remain distinct.

P2 supplies only its latest coherent, non-invalidated observation. Relevant
runtime/authority/policy/lineage/eligibility changes, pending writes, worker loss,
attachment replacement or domain-capability loss invalidate it until the existing
owner refresh path establishes a new full observation. Wall-clock age or an old
same-generation Applied flag cannot manufacture freshness. Source integration must
prove that invalidation path before enabling the port; B1 invalidation events alone
do not establish a fully wired cache. No native call is hidden in the projection.

These values authorize display only. Every new Accept/mode action still resolves
and admits its exact target and performs fresh P3 Inspect/Apply checks outside
domain locks; rendered controls never authorize an effect. Exact duplicate
acceptance/status behavior remains native-free as already specified. Add pure
fixtures for missing/stale/wrong-generation or policy-revision observations,
proposal/lineage mismatch, handler loss, zero native calls from GET/render, and
fresh action validation despite a positive displayed capability. P2 owns central
composition/invalidation wiring, P3 owns complete runtime proof, and P6 owns the
optional projection adapter; existing lead windows and live gates remain intact.

### Manual mode action

Technically accepted P6-B2 closure contract, recorded by architect0 in design.md;
lead retains source release.
Manual Plan/Default selection belongs to P6's existing handler/browser module;
P2 supplies central registration and trusted composition. It is independent of
proposal acceptance and does not use Codex settings, a synthetic Caller/tool
anchor, or the private acceptance PolicyRevision token. The earlier ModeIntent
validator alone is not a mutation API. Add these small types in `piplan/mode.go`:

```go
type ModeInput struct {
    Mode string `json:"mode"`
    ExpectedRevision uint64 `json:"expectedRevision"`
    ExpectedDigest string `json:"expectedDigest"`
}
type ModeView struct {
    Mode string `json:"mode"`
    Revision uint64 `json:"revision"`
    Digest string `json:"digest"`
}
type ModeResult struct {
    Outcome string `json:"outcome"` // applied, rejected, unknown
    Policy *ModeView `json:"policy,omitempty"` // positive exact proof only
}
type ModeSetter interface {
    SetMode(context.Context, agentbackend.ConversationRef, ModeInput) (ModeResult, error)
}
type ModeAdapter struct {
    Controller piruntime.ToolPolicyController
    Admit func(context.Context, agentbackend.ConversationRef, func(context.Context) error) error
    Resolve func(context.Context, agentbackend.ConversationRef) (agentbackend.ExecutionHandle, error)
    Eligible func(context.Context, agentbackend.ExecutionHandle) (bool, error)
    Compose func(context.Context, agentbackend.ExecutionHandle, string, uint64) (piruntime.ToolPolicyTarget, error)
}
```

ModeAdapter implements ModeSetter. Nil dependencies refuse. Mode is exactly plan
or default; expected revision is an integer 1..2^53-1 and digest is lowercase
64-hex. Browser supplies no tool names, native IDs, generation, access, target
digest or credentials. Under ordinary admission, Resolve must return the current
handle for the exact authorized ConversationRef, including backend/binding/runtime
checks. Nil or schema1 policy remains unavailable; manual selection cannot initialize
it. Require current full InspectToolPolicy proof, released policy/host tools,
no pending/held work and idle eligibility, including tools/callbacks/preflight and
conflicting acceptance/dispatch. Eligible enforces current saved access; Plan never
grants a route to broaden that access. No domain lock spans inspection or Apply.

Compare expected revision AND digest to the fully validated current policy before
composing or applying anything. Mismatch is a no-effect conflict, even when the
requested mode equals current mode. Compose derives the complete target from
trusted current host mapping and the fixed registered ceiling. For the current
mode, use its current revision and require full target equality; return applied
with that fresh proof without Apply. Otherwise checked revision+1 must fit the safe
range; require exact mode/revision, valid P3 digest, allowed active set and unchanged
ceiling. Call ApplyToolPolicy once with the original expected revision. Only an
applied result with complete exact target/current-generation proof yields Policy.
Positive rejected means no new mode proof. An invoked Apply error, malformed result,
unknown outcome or incomplete proof yields unknown with no Policy; never trust a
zero/default rejected result accompanying a transport error. Do not Apply again,
clear pending state, change revision/settings, or create a mode receipt/ledger.

`PiPlanHTTPStore` keeps its current required methods. Add optional
`PiPlanHandler.Modes piplan.ModeSetter`; nil is unsupported. Extend the existing
unmounted handler with `POST <same conversation scope>/pi-plan/mode`, admission
operation `pi-plan.mode`, exact same-origin/auth scope and strict bounded JSON
decoding as the existing workflow helpers. P2's resolver must authorize a manual
policy mutation, not reuse read permission or accept-plan authority implicitly.
Preserve existing authenticated conversation admission and CSRF protections.
Applied returns 200 with ModeResult; positive rejected returns 409 with ModeResult;
unknown returns 202 with ModeResult and means uncertainty, not accepted execution.
Pre-Apply invalid/conflict/unavailable errors retain existing 400/409/501 behavior;
ordinary busy/held errors retain 503. Snapshot suppresses CanSelectMode if the
optional action is absent, even if an observation erroneously claims ModeReleased.
No central route/app.js edit is assigned to P6 by this brief.
Before Apply only, map runtime Scope/Conflict to domain Conflict and runtime
Unavailable to domain Unavailable; Held retains 503. Once Apply is invoked, its
errors follow Unknown semantics above, regardless of their sentinel or default result.

Extend `mountPiPlan` with injected `api.setMode(payload)` and returned/render-hook
`selectMode(mode)`. Enable only when the API exists and the current snapshot has
CanSelectMode plus valid mode/revision/digest; retain shared busy and pending-plan
exclusion. Capture expected revision/digest from that displayed snapshot on each
explicit selection. Send one request; never optimistically change mode or replay
a stored mode request on reconnect. Unknown/network loss disables further action
until an explicit refresh supplies a new coherent, non-invalidated host observation.
The native-free GET may show the current authoritative policy; it does not certify
that an earlier request succeeded. A later deliberate selection requires fresh
ordinary admission and CAS; it is not an automatic retry or Unknown reconciliation.
P2 invalidates the host observation before mutation and keeps it invalid until its
existing refresh path proves a coherent current policy; success/Unknown cannot
locally manufacture a replacement cache entry. Pending/held native state still
refuses. Keep mode uncertainty distinct from the
existing durable accepted-plan ID; no new localStorage authority/token is added.
Do not clear mode uncertainty from a cached pre-request snapshot, even when its
policy bytes happen to equal a later state.
In particular, `update(snapshot)` never clears mode uncertainty. Only an explicit
refresh started after the uncertain request has settled may clear it upon a fresh
successful `api.read` using the real no-store GET. Earlier in-flight GET completions
and pushed updates cannot do so. Use request-local sequencing, not the domain
snapshot revision: policy can change without changing that revision. A fresh read
still depends on P2's coherent invalidation/proof; the browser invents no authority.

P6 owns `piplan/mode.go`, focused fixtures, its existing `web/pi_plan.go` and
`web/static/pi-plan.js` modules. P2 owns the optional field injection, admission op,
mount and observation/invalidation wiring in its central window; P3 retains the
existing policy port. Source release stays with lead. Fixtures cover nil support,
first selection without proposal/caller, unauthorized/busy/stale CAS, same-mode
no-op, safe-integer maximum, changed ceiling/composition, one Apply, transport-error
Unknown despite default rejected, incomplete applied proof, HTTP origin/body/error
mapping, lost ACK/reconnect with no replay, no optimistic mode and native-free GET.
Source checked at D `2dd2af9499fa64602bfce94c20a17b6e41139eca` plus working tree:
`piplan/{types,policy_adapter,policy_projection}.go`, `web/pi_plan.go`,
`web/static/pi-plan.js`, and `piruntime/tool_policy.go`. No execution evidence is
claimed by this design clarification.

## Central composition release boundary

Bounded BRIDGE continuation, 2026-11-12: independent P6 module/read/UI slice
technically accepted by architect0 and recorded in design.md. Full central
technical acceptance also settles the lock span using owner1's existing
Send/callback evidence below; lead retains all source allocation. Source inspected at D
`3872155b55688742355b8dc16b88584f4cb5a303`; P6 module delivery is accepted by lead.
This section wires those modules into the current portal. It adds no policy store,
workflow ledger, polling service, converter or capability inferred from a nil port.

The central source-release assessment is technically accepted in design.md against
the actual matching P3 ports and committed P6/helper/shared-admission consumers.
The matching P3 commit is required before the central commit; real composition
checks are required before registration or capability advertisement. The remaining
historical-resource observation arm is internal compatibility, not a missing public
API. Ordinary Pi BackendTarget/Operations resolver composition remains required
where absent, with native routing separately allocated by lead. Owner2's proposed
Go/routes/types/template window and owner4's sole app.js window do not overlap.

### Actual missing seams and independent slice

`web/server.go:NewContext` constructs the real Manager through
`pi_providers.go:newPiCreationManager`, but retains only PiCreationRuntime and
composes no question/Plan handler or observer. `pi_creation_flow.go` calls Create
without ToolPolicy. `resolveConversation` still immediately requires Codex.
`operation_state.go:runDisplayRefreshes` owns one cancellation-bound coalescing
worker, currently for lifecycle/index only; its caches are not Pi authority.
P3's `worker.go` receives native invalidate frames but `loadOwned` supplies an empty
changed callback. `Watch.Subscribe` polls transcript snapshots; it is unsuitable
for this observation contract. InspectToolPolicy proves native policy but exports
neither complete idle/pending state nor before-effect invalidation.

Release the following P6 module fixes independently with fake host evidence:

- Replace the insufficient `PolicyObservation.ProposalCaller` with
  `Proposal *ProposalObservation`, where `ProposalObservation` contains
  `PlanID string`, `Revision uint64`, `TextSHA256 string`, `Caller Caller`.
  Pure CanAccept projection requires exact latest ID/revision/text digest/current
  caller and lineage; the producer must have verified that exact Proposal's content.
- Add native-free domain-owned `FileStore.LatestProposal(ctx,ref) (*Proposal,error)`
  and `piquestions.FileStore.Questions(ctx,ref) ([]QuestionRecord,error)`. Validate
  scope/private records with existing readers and return detached copies. Genuine
  missing/empty state yields nil/empty; malformed/unreadable state errors. P2 must
  not duplicate private JSON decoders or reconstruct origin from displayed text.
- Fix PolicyStore.Snapshot to project manual mode against an empty valid record
  when plans.json is genuinely absent. This fix is in `piplan/policy_adapter.go`,
  with its adapter/projection fixtures. No proposal is needed to select a mode.
- Own a separate `web/static/pi-workflow-ui.js` API/mount/render helper and fixtures.
  Exact central import/mount ownership is assigned by lead, not implicitly shared.

Readers may live in domain-owned `read.go` files. Detached copies include nested
question options, responses and answer slices. Add an optional pure question
projection to AdmittedStore, leaving FileStore as the storage primitive:

```go
type QuestionObservation struct {
    Current agentbackend.ExecutionHandle
    BindingRevision, ObservedBindingRevision uint64
    QuestionID string
    Revision uint64
    Caller Caller // exact saved caller; do not replace its original generation
    Origin piruntime.NativeOriginObservation
    CaptureAllowed bool
    Callbacks, LinearLineage, GuardQuestionsSchema int
}
type QuestionObservations func(context.Context, agentbackend.ConversationRef) ([]QuestionObservation, error)
// AdmittedStore gains Observations QuestionObservations.
```

Snapshot reads the validated domain record and injected observations without native
calls. Default CanRespond is false when proof is absent, duplicated, malformed or
unavailable. Require exact group ID/revision/saved Caller, Current.Conversation equal
to requested scope and saved durable caller scope, nonzero equal binding revisions,
Origin.Handle equal Current, exact origin anchor/token/tool ID and tool name, all
three required contracts=1, CaptureAllowed, and the existing pure
VerifyNativeArguments against that QuestionRecord. Preserve closed/status/order
restrictions and compare the same selected record, not two racing raw snapshots.
The producer sets CaptureAllowed only from complete current host admission/tool
availability; it may be true while busy because capture sends nothing. No idle
requirement or provider-success inference is added. Missing observation disables
capture without falsely rewriting pending history as a stale branch. Original
response/duplicate/status reads remain native-free and available under read scope.

### P3 complete observation and existing-stream invalidation

The observation/invalidation ports are implemented at P3 6b64c744. The additive
Settings field below is the accepted checked-submission amendment described later;
its implementation and checks remain a separate source prerequisite.

```go
type WorkflowObservation struct {
    Handle agentbackend.ExecutionHandle
    AttachmentID string
    Sequence uint64
    Retained *ToolPolicyState
    Proof ToolPolicyProof
    Settings EffectiveSettings // accepted checked-submission amendment
    Loaded, Pending, Held, Idle bool
    HostTools []string // captured worker set intersected with current attachment
}
type WorkflowObserver interface {
    ObserveWorkflow(context.Context, agentbackend.ExecutionHandle) (WorkflowObservation, error)
}
type WorkflowInvalidation struct {
    Runtime RuntimeRef
    AttachmentID string
    Sequence uint64
    Connected bool
}
type HostInvalidationHandler interface {
    InvalidateWorkflow(WorkflowInvalidation) // short pure host invalidation only
}
```

Use `workflow_observe` on the existing bounded control connection. Require the
current mapped retained handle, schema2 policy, same worker generation, actual
attachment and full package feature support. Never Ensure/Load/Create, clear a
hold, fix a policy or run an input while observing. Under existing conversation
state ownership, combine retained policy/pending settings/pending policy/held
receipts with one new synchronous worker `workflow_observe` result: exact policy
proof plus WorkerSession pending/isStreaming/hostBridge.pending, policy module
running/activeCalls and held flags. The policy module exposes those existing
private state observations to WorkerSession; no SDK-internal introspection.
Idle is true only if every pending/run/preflight/tool/callback count is zero,
no receipt/callback uncertainty or unexpected child exists, and all identity,
attachment, registered/active/callable/instruction checks pass. Missing evidence
is unavailable or a negative observation, never a true default. Return independent
Retained and Proof, not an Applied boolean substituted for either.

P3 keeps one ephemeral runtime-scoped observation sequence and mutation-pending
count. Both reset with the runtime generation, are never receipt/native lineage
identity, and are not persisted. Overflow refuses observation until a new runtime;
no wrap. An observation captures the sequence before and after its bounded reads;
sequence change or nonzero mutation-pending refuses publication. A stable worker
reply is synchronous; native events before/after it retain stdout ordering.

Negotiate `workflowObservations:1` on the existing host attachment only when the
handler implements HostInvalidationHandler and the package/runtime support matches.
Send `workflow_invalidated` carrying only attachment identity and Runtime/Sequence
on that stream. The manager supplies Connected=true to the host callback for a
validated live frame, and Connected=false on setup failure/EOF/cancellation with
the known attachment identity (or empty before establishment); no synthetic frame
is accepted from a peer. Initial attach ACK supplies its current sequence and
invalidates host snapshots before the attachment becomes usable. Before
a P3-controlled effect that can change eligibility, mark mutation-pending, increment
sequence and obtain bounded `workflow_invalidated_ack` for that exact attachment,
Runtime and Sequence. The manager calls InvalidateWorkflow and ACKs only after the
short host map invalidation returns. No native/domain/receipt lock is held while
waiting; existing effect locks and authority are acquired/revalidated afterward.
The pending interval lasts through completion and prevents a refresh republishing
old state at the new sequence. Completion increments/notifies again and requests
refresh; only the pre-effect barrier needs ACK. Lost/missing ACK refuses before
the effect. An uncertain already-crossed effect retains its ordinary Unknown/held
semantics, never retries to repair the notification.

Cover Send/Configure/Apply/Create/Load/Unload and attachment/tool-set changes,
plus retained/utility/resource transitions affecting combined eligibility; P4/P5
callers cannot be assumed to enter a P2 web hook. Activate this barrier only for a
negotiated workflow attachment, preserving earlier B1-only behavior. A P6 runtime
must establish it before first worker Create/input; it cannot advertise workflow
controls while disconnected. Native SDK invalidate/worker exit/stream EOF are
observational invalidations, not a claim of advance knowledge of native events or
crashes. Clear host observations immediately on EOF, protocol error, attachment
replacement or event overflow; reconnect begins empty and requires fresh proof.
Native event delivery never grants mutation permission: every action still admits
and inspects freshly. No new socket, listener, polling subscription or event ledger.

**Historical resource rows after an explicit successor (technically accepted,
recorded in design.md).** Positive Idle may include an original stopped resource
from an earlier generation only through the existing validated `runtime.json`
request history. Reuse `Manager.records`: its exact Session/Instance, full request
digests/configuration and connected ReplacesRequestID chain must validate, and its
current request Runtime must equal s.ref. For each historical resource, join
`records.Requests[handle.Runtime.RequestID]` and require full original Runtime
equality, schema1, exact filename/resource/operation IDs, and
`ResourceDigest(handle.Runtime, record.Request)`. Same Session/Instance alone is
insufficient. Require phase stopped and non-nil ExitCode, matching the existing
`assertRuntimeSettled` resource gate. The ordinary Wait writer's empty process-group
check and the validated successor/H0 predecessor-drain startup gate are the existing
terminal proof; do not demand today's live cgroup be empty or inspect a reused old
numeric PID/process group. Missing/malformed/mismatched or nonterminal historical
evidence holds the observation. Do not newly admit historical rejected rows, which
the existing successor gate does not permit; current-runtime rejected handling is
unchanged. `s.resource` and all resource effects/lookups retain exact current Runtime
checks. This is read-only compatibility within existing ownership/receipts, with
no record repair, new registry, format or native lifecycle call. The supervisor
may retain the exact already-verified launch directory from Supervise in a private
ephemeral field. Historical observation requires successful successor startup
(`reclaimControl`) and reuses validateSuccessorStartup for that exact directory,
then the same derived Manager configuration and records reader. No runtimeConfig
field, caller-supplied directory, new public port or fallback path is introduced.
Missing startup provenance keeps the historical arm unavailable. Source pointers:
`piruntime/runtime_records.go:records`, `successor_proof.go:assertRuntimeSettled`,
`successor_socket.go:validateSuccessorStartup`, `resources.go:ResourceDigest`/Wait;
inspected at D `d681233ed7c143994745a11968dec75a2b16e3c0` plus owned source.
Focused fixtures cover valid predecessor terminal row plus a current idle worker,
foreign/disconnected request, changed full Runtime/digest, missing ExitCode and
historical running/unknown/rejected refusal. No successor lifecycle is executed
by this design clarification.

### P2 shared authority, construction and refresh

Reuse architect0's `web/pi_team_admission.go` authority primitives; do not create
another resolver/lock hierarchy. Session reads/ordinary records use transition SH,
exact selected package/current profile, runtime SH and strict binding/authority;
original-reference reads allow busy/held without load. The conversation-mutation
closure uses runtime EX for acceptance/mode/input exclusion and supplies coherent
Handle, BindingRevision and saved access. Preserve team/message ordering and keep
domain locks inside these closures and outside native calls. P6 callbacks use the
session record-write path, so early callback handling does not acquire a competing
conversation mutation lock. Send must retain its persisted-input ACK behavior,
not wait for model/tool completion while holding EX.
Release EX before waiting for callback/domain delivery settlement or model completion.
The current creation owner holds runtime EX across original initial Send,
Lookup/VerifyCreation and ready publication. Retain this span and the P6 mutation
closure through persisted-input Send ACK. Owner1's existing source and actual-SDK
callback fixtures establish that WorkerSession.send resolves from observePersisted
after exact input reopen and file/directory sync witness. Supervisor receipts.sendOwned
then durably commits Accepted, releases its receipt mutex, snapshots/saves worker
state and returns ACK. Snapshot reads pending/streaming/bridge size without waiting
for a host handler, domain Lookup or model completion. The independent callback
waits for original Accepted and may then wait on P2 runtime SH until EX/ready
publication completes; it is not a prerequisite of the Send witness or ACK.

The new pre-effect invalidation ACK must preserve that independence: its handler
takes no P2 SH/EX, domain lock, native call, c.mu or receipt lock. Add this assertion
to the integration of the new barrier using the existing combined fixture; the
existing evidence does not claim that the new barrier is already implemented.
Do not split EX and Send merely for this callback. Such a split would require fresh
frozen Default revision/digest/admission revalidation after SH acquisition and
through ACK, because SendInput does not carry the P6 acceptance policy token.
No new lock bypass, input field or creation authority is needed.

**Invocation-local composition grant.** The domain Admit callback may carry a
private grant pointer in an unexported context key, minted only inside the actual
withPiConversationMutation/session read-or-record closure after its checks and
lock acquisition. The pointer holds detached immutable admission scope and its
read/record/mutation kind, and expires in a defer when that synchronous callback
returns, including errors/panics. Current/Store.Validate may consume it for pure
exact scope/caller/generation checks without reacquiring locks; they must require
the matching live invocation and sufficient operation kind. Native origin/policy
inspection stays outside domain locks. This carries an already-owned lock scope;
an incoming HTTP context, cached pointer, boolean or caller-supplied value creates
no authority. Do not share/swap a global store callback or allow grant use by a
detached goroutine, later request or more privileged operation. A fresh external
action still enters the actual admission closure. This does not change legacy
Schema2Write's invocation-lifetime rule or its explicit lock ownership.

**Attachment readiness without a new port.** At committed P3 6b64c744, the first
Connected=true notification is the initial attachment sequence before its ACK.
Treat it only as invalidation. The creator may wait on a bounded host-local signal
for a later Connected=true sequence strictly greater than that initial sequence
on the exact same Runtime/AttachmentID and same AttachHost attempt. In P3,
workflowAdvanceLocked emits no notification while workflowReady is false;
acceptWorkflowACK marks ready and then advances/emits. Thus this later notification
proves the initial ACK was consumed, not policy/authority/native readiness. Loss,
replacement, cancellation, overflow or timeout clears the local condition and
refuses Create admission until a newly established attachment proves its own
sequence; do not reuse an earlier attempt's signal. InvalidateWorkflow only clears
the short map and signals the waiter; it takes no admission/domain/native lock and
does not poll. Create still runs all existing current authority/policy/barrier
checks. No Ready method or P3 wire change is introduced by this composition.

**Retained attachment after portal restart.** Architect0 technically accepted this
exact port/source boundary and recorded it in design.md (around line 3052).
Owner1 confirmed the source fit; lead owns release and sequencing.
The first explicit Ensure returns RuntimeStatus.Runtime, but a new Server cannot
recover its InstanceID/RequestID/Digest from PiRuntimeAuthority or ReadStart's
StartRequest. Add this optional port on the same configured Manager:

```go
type CurrentRuntimeReader interface {
    ReadCurrentRuntime(context.Context, agentbackend.SessionRef) (RuntimeRef, error)
}
```

P3 owns new piruntime/current_runtime.go and one private readSavedRuntimeRecord
helper shared with ReadStart. Reuse m.record's strict validated current pointer and
connected immutable request history. Preserve ReadStart's exact missing-record
classification: genuinely absent state, an empty ordinary state directory or only
its validated empty runtime.lock may return os.ErrNotExist; retained artifacts
without runtime.json remain held. Malformed/disconnected/wrong-scope/config-mismatched
records refuse through the existing decoder. Return record.Runtime literally from
that one current record; never reconstruct it from StartRequest, hashes, generation
or directory naming, select a historical request, or search native processes.
ReadStart becomes a wrapper returning the same record.Start with unchanged behavior.

This is a cancellation-aware pure disk read. It creates no directory/lock/receipt,
calls no helper/native service, and performs no Ensure/Load/Configure or auth probe.
A returned ref proves only validated retained identity, not a running/ready worker,
successful prior attachment or permission. No runtime_records decoder/format,
authority field, registry or second parser is added; old state support remains
exactly that of ReadStart. Missing optional support leaves retained attachment
unavailable instead of guessing or starting a runtime.

P2's existing startup/demand refresh work captures the ref under current shared
package/binding/authority admission and requires exact returned Session and current
authority Generation. It then uses the existing AttachHost independent runtime
handshake and same-attempt initial-ACK sequence gate. After waits and before
publishing any positive observation, recheck current authority, read the full
current RuntimeRef again and require exact equality with the attached ref, including
Session, InstanceID, RequestID, Digest and Generation. Generation equality alone
cannot certify the same request; a same-generation replacement also invalidates
the candidate. Complete workflow/domain proof and attachment identity must still
match. Never hold an admission
lock for the lifetime of AttachHost's stream. GET/render/Lookup stay native-free:
they may request existing refresh work but do not attach, wait for attachment or
trigger native recovery synchronously. Failed/cold attachment stays unavailable;
this amendment grants no restart, Load or new lifecycle action.

Owner1's bounded source is current_runtime.go, the ReadStart wrapper in manager.go,
focused current-runtime/ReadStart fixtures and narrow docs/pi-runtime.md. Owner2
retains/uses the actual optional port in its existing composition window. No native
routing writer dependency or new source allocation is inferred. Checks cover exact
schema1/current-successor literal ref, missing versus ambiguous artifacts, malformed
or mismatched current history, cancellation, unchanged ReadStart, and zero host
calls/writes; the P2 fixture uses a new Manager/Server over retained ready state to
prove attachment without Ensure. Existing handshake/projection tests retain their
own scope, and no model/provider or broad suite is requested here.

**Retained attachment verification scope.** The accepted fourth native composition
pass (owner2 reports 4.707s) proves a new Server with the same Manager/config and
an explicit BindPiWorkflowNativeFixture call that reads the full current ref and
performs ensureAttachment before GET. It proves real reattachment/ACK and later
coherent projection, not demand-triggered cold attachment. The separate P3
CurrentRuntimeReader unit case constructs NewManager(m.config) and proves exact
disk identity without host calls. The web observation case seeds a ready attachment
and proves refresh/full-ref race checks. Neither joins those facts into an actual
new-Manager/Server production demand-attachment path; do not describe the fourth
pass as that broader proof.

Owner2 confirms that finite coverage gap. The shortest proposed check uses only
the existing owning fixture and tagged bridge. Owner1 adds a TEST-only Reopen
function to the existing NewP6NativeFixture result, returning actual NewManager
with its original m.config, including the fixture's private verifyProcess and
retainPackage hooks. Do not reconstruct public Config without those hooks or
alter production Config. Owner2 adds an explicit attach boolean to the same
tagged BindPiWorkflowNativeFixture method/interface: initial use true, retained
restart use false. Both modes keep validated detached catalog binding and exact
current-runtime comparison; false skips only direct ensureAttachment. No second
bridge/export scheme, parser, fixture engine or production API is introduced.

One restart-only case closes the old disposable Server, obtains a distinct Manager
through Reopen without Ensure, copies the existing Server/PiCreation config with
that runtime, creates a new Server and binds the catalog with attach=false. A
normal scoped GET supplies the first observation demand. Require no positive
projection from a preattached/test-seeded state, then let the existing background
refreshRequested -> attachRetained path acquire ordinary admission, read the
current ref, attach/consume ACK, recheck full current equality and publish a
coherent view. Assert a fresh attachment ID, unchanged full RuntimeRef, original
receipt availability and no additional native user input/root creation. Keep the
existing synthetic replacement-race checks as separately scoped evidence.
Report the actual command/source/result and these distinctions in the final
packet. This is a proposed lead-owned source amendment, not a source grant or a
request to rerun the unchanged fourth pass; no native3 or broad SDK batch is needed.

SavedAccess follows the owning TEAM admission contract. A member uses its exact
retained roster Access. PiCreationTeam/PiRoster do not store lead Access: resolve
lead access only from validated installedTeams.Catalog matching the original
DirectTeam CatalogDigest, retained team ID and TeamDigest, and its explicit
team_lead.Access. Never infer workspace_write from the lead role, current default
or ExecutionAccess. A missing/mismatched catalog leaves access-dependent lead
composition/mode/implementation unavailable and invalidates positive eligibility;
pure original-reference reads and record gates are unaffected. Supporting a
changed-catalog historical lead later requires an actual retained-catalog source,
not a new field or guessed permission in this package.

New P2 files `web/pi_workflows.go` and `web/pi_workflow_observation.go` own one
Server-local composition object. Retain optional HostCallbackConnector,
NativeOriginInspector, ToolPolicyController and WorkflowObserver from the SAME
Manager constructed by newPiCreationManager; never construct another runtime or
probe credentials. Compose private FileStores at UserStateRoot, admitted question
capture, policy/Mode adapters, original-receipt dispatch services and the existing
question/Plan handlers. Store validators are pure request-local scope checks,
never native calls under StateFile.Update. Read/Lookup authenticates original scope
but does not require idle, active policy or a live worker merely to show receipts.

The aggregate host callback handler composes existing team/utility handlers with
strict retained question/plan publication. HostTools lists only fully released
bound domain handlers. Construct Caller exclusively from checked HostCall subject,
anchor/token/tool-call ID; reject utility P6 calls and model-supplied identity.
The existing P3 Accepted-input/native-origin gate precedes domain side effects.
Return the domain's persisted ID/revision result, including exact duplicate rules.
Invalidate before domain publication/capture; no replacement IDs after uncertainty.

Before a newly reserved root/member's first Create, compose fixed initial Default
Revision1 policy from its frozen saved access, exact selected package and actually
registered approved factories. For a new lead, use the same exact matching frozen
catalog proof above; initial root support remains available with that proof.
Use the accepted fixed ceiling and P3 digest; pass
ToolPolicy explicitly. Team/utility tool support follows their own released
handlers; Plan excludes delegation/MCP/router routes. Capture complete worker
composition before attachment/Create. Repeated creation uses existing exact P3
initial-policy replay refusal rules; nil/schema1 is unavailable, never retrofitted.
Changed composition cannot be hidden by new policy defaults on retry. P2 owns this
small pi_creation_flow.go hunk; no provider/account policy field is repurposed.

**Initial root Send policy proof.** Architect0 technically accepted this corrected
narrow gate in design.md (around line 538); lead retains source sequencing.
Owner2 corrected the branch interpretation:
only createdHere may perform the first initial Send. No InitialDispatchStarted
field or accepted recovery branch exists. Preserve createdHere-only exactly;
retained NativeCreateStarted/native identity never authorizes a new initial Send.

The fresh Create path already establishes ensureAttachment on the exact current
RuntimeRef and its same-attempt initial-ACK proof before Create. After successful
Create and the existing initialized VerifyCreation proof, still under root EX and
outside domain locks, call InspectToolPolicy for the exact handle before that
createdHere first Send. Compare against the exact captured initialPolicy passed
to this Create, not a newly composed retry default.
Require a complete positive proof of retained Default Revision1, its unchanged
full Active/RegisteredCeiling/digest, exact generation and registered/callable set
checks, consistent with the original frozen package, saved access and captured
trusted handler composition. P3's ordinary Send path checks a present current
policy but permits nil policy and does not enforce Default1; it cannot replace
this host initial-policy gate.

The captured initial target and native retained Revision1 policy must agree.
Trusted composition never replaces that target or mutates its ceiling. Schema1/nil,
advanced revision (even same mode/digest), pending/held/unavailable proof or target
mismatch refuses before
the first dispatch. Do not replay Create, Apply a policy, Load, clear pending state
or retrofit an old root to make it eligible. No InitialToolPolicy field, parallel
ledger, new port or provider/settings encoding is added. Keep EX through the
persisted-input ACK and all existing creation identity/input proof.

Every initialization revisit, including a portal restart after native creation but
before an initial input receipt, remains on the original Lookup/Verify completion
path without Send. Do not add fresh policy or attachment availability as a new
historical-proof condition. This preserves original schema1/nil-policy receipt
completion when the existing exact proof
allows it; it does not claim a live worker is available or bypass VerifyCreation's
existing checks. A missing receipt is never evidence authorizing another Send.

Owner2's creation/composition window owns the small gate and its existing typed
fixture. The helper's unavailable Inspect cannot be replaced with an unconditional
success: model the actual target/proof and exact mismatch/nil/advanced cases.
Focused evidence covers successful fresh ACK/Create/Default1 proof followed by one
Send, refusal with zero dispatch, and retry original receipt reconciliation without
new attachment/policy requirements or a Send after a missing receipt. Lead
retains branch/source authorization; no P3 implementation window is created here.

Maintain one in-memory observation map keyed by exact ConversationRef in the
composition object, under a short mutex. Each entry includes current handle and
binding revision, host invalidation counter, runtime Sequence/attachment identity,
saved-access/package/tool identity, full WorkflowObservation, and verified domain
content, including the exact catalog/team/access provenance for lead eligibility.
It is a display snapshot, not durable authority. Invalidate synchronously
BEFORE every P2 mutation/publication/settings/access/binding change and in the
HostInvalidationHandler; clear on shutdown/disconnect. An event schedules existing
display work and never runs native code inside its callback or the map mutex.

Extend `requestDisplayRefresh/runDisplayRefreshes` with a coalesced set of requested
Pi refs, serviced on demand/events by the SAME cancellation-bound worker. Do not
add a timer or use the old transcript Watch polling. GET may enqueue demand but
returns immediately from pure store/cache projection; it never waits for proof.
Bound each pass with the existing cancellation/time budget. Under shared current
authority, capture host counter/scope, call ObserveWorkflow and content-aware
historical origin verification on domain-owned immutable records outside domain
locks, then recheck package/binding/handle/roster/domain revisions and counters.
Publish only if unchanged and the attachment/sequence remains current. Otherwise
leave controls absent and coalesce a later event/demand; no spin retry or TTL.
An already current observation does not enqueue another refresh on every GET.

Publishing or invalidating a display observation also wakes the existing selected
conversation stream. The concrete seam is `backend.Watcher.Subscribe(ctx,Identity)`:
P2 supplies a small Pi-only wrapper around the existing Operations.Watch and a
coalesced per-conversation notification channel owned by the same observation map.
Merge invalidations with normal stream cancellation; add no timer or endpoint and
do not use transcript digest change as evidence of a policy change. The existing
app.js `createConversationSync` apply/reconnect hooks refresh the Pi workflow views
through the standalone helper. If the ordinary Pi neutral conversation route is
not yet composed, its P1 BackendTarget/Operations resolver adaptation is an explicit
P2 dependency, preserving the legacy resolver. This wrapper is notification only;
neither the old native Watch polling nor the browser stream establishes authority.

Populate all piplan.PolicyObservation fields from that complete observation and
actual guard/handler configuration. Questions get positive CanRespond only for
the exact observed group ID/revision/caller/questions content; busy may still allow
answer capture, whereas dispatch/Plan/mode require idle. A missing proof is
unavailable, not historical staleness inferred from a timer. New domain response or
acceptance schedules its existing DeliverNext/Advance under fresh mutation admission;
if busy, keep pending and reconsider on the next observed idle event. GET/refresh
must never itself authorize a new Send/Apply. Use only already accepted durable
domain intents; terminal/Unknown receipt lookup never becomes redispatch. Resumption
uses those domain-owned pending records on explicit runtime attachment/idle events,
not a new queue/ledger or automatic Load. No synthetic initial/team input is added.

### Current settings and checked ordinary submission

Status: architect0 technically accepted this exact amendment and recorded it in
design.md at the checked-submission clarification (around line 3035); owner1
confirmed its P3 source/serialization fit at 6b64c744. Lead owns source release.
Independent central composition remains sufficient, but production
P6 Prepare/Send and advertisement require this implemented seam. Initial creation
settings are not current settings after Configure. Do not impose an inferred
initial-only restriction or obtain settings through effectful Load/Configure.

Add `Settings EffectiveSettings` to the existing `WorkflowObservation`. P3 copies
the complete validated current retained settings under the same c.mu as its
existing live worker settings/policy proof and final sequence/pending check. The
field includes Provider, AccountRef, Model, Thinking, PolicyRevision and Revision;
it is internal host proof, not a browser DTO or credential payload. Missing or
invalid settings cannot support preparation. No parallel settings observer, new
settings digest, schema, worker request or independent cache is introduced.

```go
// Optional piruntime port on the same Manager used by WorkflowObserver.
type CheckedSubmissionSender interface {
    SendCheckedSubmission(context.Context, agentbackend.ExecutionHandle,
        SubmissionRef, SendInput) (SubmissionStatus, error)
}
```

P2's domain Prepare runs inside the already-held conversation mutation EX closure,
outside any domain lock. Obtain a fresh complete ObserveWorkflow result, require
the exact admitted handle, loaded/idle/no-pending/no-held state, current attachment
and policy/host eligibility, and for Plan the frozen expected Default target.
Use its Settings with P3's existing SubmissionDigest over the exact original
domain OperationID, Conversation, Action=`send`, Message, ActionContext and
Retry=false. Persist that full SubmissionRef in the domain's existing opaque
ReceiptRef before the one checked Send. An earlier display observation, initial
intent/CreationProof, transcript fields or a fixture constant cannot substitute.
No native receipt is written during Prepare. Keep the existing EX lifetime through
the persisted-input ACK; this amendment does not split admission or release it
across the preparation-to-send interval.

The new ordinary control operation participates in workflowMutates and its bounded
pre-effect invalidation ACK before taking c.mu. Validate current Handle and exact
SubmissionRef scope, operation ID and Action=`send`. Under c.mu, recompute
SubmissionDigest(ref,input,c.record.Settings) and require equality with ref.Digest
before calling the unchanged sendOwned with that exact ref and input. Settings
Configure uses the same c.mu, so it cannot cross this check and native handoff.
Retain ordinary pending/held/live policy/native dispatch checks, callback/witness
progress and post-lock workflow permit checks. A mismatch refuses before any
receipt creation or dispatch. Do not replace the caller's digest with a newly
computed one. The P2 frozen policy/access checks remain necessary: this port's
settings digest is not a Plan acceptance token or permission grant.

Return the existing typed SubmissionStatus; P2 verifies any positive result names
the exact frozen ref/input and accepted native witness before marking delivery.
An invoked error or unproved result leaves domain uncertainty under that original
ref. Later visits use only original Lookup, including after lost ACK, restart,
settings change, Unknown, NotSubmitted or a missing native receipt. Never recompute
the ref, call checked Send to reconcile, or create another domain operation.
Existing receipt prepared/dispatching replay remains Unknown; the native receipt
engine still creates its first prepared row only inside its original send path.
No backend.SendRequest, receipt encoding, recovery phase or ordinary Send behavior
changes. Missing optional sender/settings support refuses new P6 delivery; pure
GET/Lookup behavior is unchanged. Older helpers cannot silently use ordinary Send
as a fallback, and the same selected-package contract gate applies.

Proposed source boundary: owner1 new piruntime/guarded_submission.go and focused
fixtures, short controller/supervisor/conversation hooks, workflow_observation.go
field/capture and mutation classification, plus narrow docs/pi-runtime.md. No
native routing writer dependency, JS change or receipt engine rewrite. Owner2
consumes the actual optional port in the existing pi_workflows composition window;
owner4's domain signatures and stores remain unchanged. Lead sequences source and
commit windows; this paragraph allocates none.

Focused acceptance covers current post-Configure settings, a Configure/settings
change between observation and checked Send refusing with zero dispatch/receipt,
scope/digest/input mismatch, pending/held/absent proof refusal, successful exact
receipt and original Lookup after lost ACK, and unchanged prepared/Unknown/terminal
no-resend behavior. Reuse the existing socket/barrier fixture for checked Send ACK
ordering and callback progress; extend the finite no-model component fixture for
one domain Prepare -> durable handoff -> checked Send -> exact receipt. Report
actual source/check scope; no broad suite is requested by this clarification.

### Exact routes, frontend and owner windows

**D-owned dispatch between the existing public C handlers.** The supported P1
consumer is `conversation.NewBackendHandler(options conversation.BackendOptions)
(*conversation.Handler,error)`, with
`conversation.BackendResolverFunc(func(context.Context, conversation.ResolveRequest)
(conversation.BackendTarget,error))`. Keep the existing NewHandler/Options and
Codex resolveConversation unchanged. D constructs a second Pi-only handler using
BackendOptions with the same AllowedOrigins, BasePath `/codex`, body/message limits,
operation timeout, shutdown and logger policy. Its neutral resolver returns the
trusted Pi Identity, real Operations and distinct authorization Capabilities;
unsupported optional groups remain nil. It never calls C's private
adaptLegacyTarget or clones that adapter. No C edit/API expansion is needed.

At D's existing `/codex/` mount, install one private dispatcher holding both
handlers. Static assets and non-conversation handling retain the existing handler.
For a canonical conversation request, validate its existing escaped-path/ID grammar
and parseTeamConversationID, then select only from validated durable backend
evidence for this exact workspace/session/member. Unknown, unsupported, mixed or
ambiguous evidence refuses; no descriptor, browser backend flag, missing Pi handler
or default guess can select Codex. A recognized legacy session still uses the
unchanged legacy handler. A validated Pi session uses only the Pi handler; if its
composition is unavailable, refuse rather than falling through. Existing session
API aliases that forward to `s.conversation.ServeHTTP` must reach this same
dispatcher, so they cannot bypass backend selection. No second overlapping mux
registration, generic proxy or service is introduced.

Dispatcher selection grants no authority and holds no outer lock while entering a
handler that will acquire admission. Each owning resolver revalidates the selected
kind and exact current scope under its normal gates after waits, including durable
session/member/conversation incarnations and live generation where required.
Changed/mixed evidence refuses before any native operation. Preserve existing
HTTP authentication, exact origins/CSRF, maintenance checks, operation permissions
and legacy TransformTranscript/ObserveTranscript/PresentTranscript ordering.
Pi mutations retain the accepted admission-to-persisted-ACK lifetime; neutral
Release/MutationLock must not reacquire or prematurely release those locks.
Long event streams must not pin mutation-excluding authority locks: read/Verify
rechecks occur under their existing scoped admission, and stream cleanup retains
the public Release lifetime. Workflow GET/render/receipt Lookup remain native-free;
ordinary transcript reads use only released observational operations, with no
Ensure/Load/recovery or cross-backend fallback. Do not use a backend-dispatch choice
as an implicit recovery permission.

Exact seam inspected at C `a2b58b5e8d5c59cb448453e113b5dd48b20c3477`
(`conversation/backend.go`, `handler.go`) and D
`6b64c7447674340db63b96c1c07cbc2b13878748` (`web/server.go` NewContext,
Handler mount, sessionAPI alias and resolveConversation). Owner2's existing central
window owns this dispatcher/constructor hunk. Native routing adapter allocation
remains separate. Focused fixtures must show legacy assets/callback order unchanged,
Pi never entering Codex resolver, alias/direct agreement, malformed/ambiguous
selection refusal, changed authority after a lock wait, optional operation absence,
unchanged auth/CSRF/permissions and no native recovery from a read. The separately
released creation catalog/initial Default1 fixture is independent of this dispatch
choice.

**Neutral mutation admission lease.** Architect0 technically accepted this exact
public-handler fit and recorded it in design.md's shared admission section
(around line 2251). Owner2 retains its current window; lead owns allocation. C
NewBackendHandler requires a real MutationLock for every mutation. Its actual order
is resolve, defer Target.Release, Verify, MutationLock.Lock, defer Unlock, effect;
Unlock therefore runs before Release. Using the existing messageLock followed by
an Operations-local withPiConversationMutation would reverse the required lock
order and is not supported.

Extract the private common acquisition in web/pi_team_admission.go as
`acquirePiSessionAdmission(ctx,ref,exclusive) (piSessionAdmission,func(),error)`;
the existing with* callbacks delegate to it and retain their checks and lifetime.
Factor the conversation scope/current handle/SavedAccess projection once for use
by both the conversation callback wrapper and the neutral resolver. This is the
same transition SH -> current package/profile -> runtime SH/EX -> exact current
binding/authority gate, with all existing post-wait checks. It is not a second
hierarchy or a new public P2/C interface.

For a supported authorized Pi mutation, the resolver acquires transition SH and
runtime EX before returning the target, validates the exact conversation and
permission, and gives that target the existing real messageLock. Verify and
Operations close over one private active lease containing the detached admission
scope; they do not reacquire runtime or transition locks. After message-lock wait,
recheck cancellation/current identity/access and obtain the fresh native proof
required by the effect before acting, without a StateFile/store lock. Any supplied
Identity must exactly match the lease; no browser context, global active flag or
descriptor can establish it. Unsupported operations remain unavailable.

Every resolver failure releases any partial acquisition internally. On success,
Target.Release expires the lease and releases runtime then transition ownership
exactly once; repeated cleanup must not close a reused descriptor. When acquired,
the existing handler releases the message lock first. Release still runs after
verification/lock failure, effect failure, bad body, denied permission or
cancellation. The callback wrappers also
defer release on error/panic. Do not let a detached operation or later request use
the lease. In particular, do not register automatic lease release on the original
browser context: C Send deliberately detaches browser cancellation only after
admission, retaining the remaining operation deadline and shutdown cancellation
to finish its ordinary native receipt. Keep the lease until explicit Target.Release
after that bounded operation returns. Lease liveness also must not consult the
original browser context's cancellation or require that original context object:
Verify/effects use the context C passes, including the admitted Send's remaining
deadline and shutdown cancellation. This does not let context values mint a lease.
Never call message Unlock when Verify or Lock failed before acquiring it.
No wait for host-handler/domain settlement
or model completion is allowed within this lifetime.

Read/event targets continue to acquire only their existing per-operation SH gates;
no runtime lock or mutation lease survives for an event-stream lifetime. Keep
Codex resolution/callback ordering unchanged and use no successful no-op locker.
Owner2 owns the private shared primitive and central resolver hunks under lead
sequencing; no C change or additional service is required. Focused fixtures cover
lock order, Verify and Lock failures, expired/mismatched lease refusal, cancellation
before admission versus admitted Send completion, once-only release, and a read
stream that does not block mutation. Reuse the existing persisted-ACK/callback
fixture; this clarification requests no new broad harness.

### Ordinary Pi composer initialization and identity

Technically accepted by architect0 in design.md (around line 3104), from the
bounded dispatcher/renderThread/upload/teardown source read and owners2/4's direct
API facts. Lead owns release of the existing app2/central windows. The current
form eagerly captures an empty dispatchThreadID and creates empty-identity upload
keys, while first renderThread later adopts a real threadId. Fix this initialization
boundary without changing Codex's eager initialization, retry behavior or listeners.

Owner2 adds typed `data-conversation-scope`, escaped by html/template, independently
of the P6 descriptor/guards. Its value is the existing piWorkflowNamespace hash of
backend, workspace, slug, session incarnation, member and conversation incarnation.
It excludes NativeID, paths and runtime generation; it is not
piruntime.BackendIdentity.ScopeKey, whose hash also includes NativeID. Reuse the
existing namespace helper rather than creating another encoding. The page's
validated backend gate remains authoritative. Pi native thread attributes stay
empty; the existing conversationID is the selected opaque route (slug or
slug~member), not a substitute for incarnation identity. Missing/malformed scope
leaves Pi composition unavailable, with no Codex fallback. A missing P6 descriptor
does not prevent ordinary conversation operation with a valid ordinary scope.

The route can resolve a newer incarnation after page rendering, so the carrier is
an expected-scope precondition, not authority. Owner4 supplies the same existing
createConversationClient with `options.fetch=scopedFetch`, preserving request
options/authentication/CSRF and setting exactly one
`X-Workspace-Conversation-Scope` header to the frozen page value on its same-origin
Pi requests. P6's existing injected raw fetchRequest uses that same scoped fetch,
including its valid-409/no-store semantics. If present, its descriptor namespace
must equal the frozen page scope before mounting P6. No new client or DTO is added.

Native EventSource bypasses fetch. Append exactly one `conversationScope` query
parameter to the existing Pi eventsPath for initial connection and reconnect.
Owner2 captures only this known events parameter in D, removes only that parameter
from a cloned request before C handles it, and retains the other query/path policy.
Only Pi events may supply scope by query; other Pi routes require the header.
Duplicate header or query values refuse, and header plus query is allowed only
when both exactly agree. D passes the detached expected value through a private
context key to its resolver/adapters; it grants no authority. Under actual owning
admission and again after waits, require exact equality with the current durable
namespace before read or effect, including P6 routes. An old page cannot silently
adopt a replacement incarnation. A long stream retains its original handle and
per-operation SH rechecks; reconnect re-enters the same scope precondition. No C
API change, new stream/client/service or page-selected native identity is involved.

Owner4 delays Pi dispatcher and draft binding until the first current authoritative
neutral snapshot supplies a nonempty actual threadId through that scoped client.
Check sync isCurrent and the page/binding epoch before adoption. Before that point,
preserve textarea text in memory, prevent default form/keyboard submission, and
disable submit/retry/queue controls; create no dispatcher, attempt/upload key or
native request. Do not queue an implicit Send for later identity discovery. The
neutral stream must still bootstrap. Bind once for that exact page scope and
actual snapshot threadId, then use the existing dispatcher/receipt semantics and
explicit user submission. Repeated snapshots of that identity do not remount or
add another listener set. Existing form handlers either delegate to the one active
binding or are installed/removed once with its lifetime; no competing submit path.

All Pi keys for the existing dispatcher, send/queue receipts and any future enabled
upload draft must include the frozen durable scope and actual snapshot identity;
keep the existing record schemas and Codex keys unchanged. For Pi, use the existing
key families with a distinct `pi.<encoded scope>.<encoded threadId>` suffix, retaining
the existing per-attempt ID suffix where applicable. Never read, migrate, merge or
replay old empty/slug-only/Codex keys. Restored records for the exact current key
retain the dispatcher's existing paused/uncertain state and explicit retry rules;
snapshot arrival does not retry them. Keep native thread identity separate from
the storage key rather than replacing currentThreadId with a fabricated identifier.

A later scope/thread mismatch, invalidated request or page teardown deactivates
the binding and removes its listeners/retry scheduling and any owned upload mount.
All canDispatch/async callbacks capture that binding's epoch and exact identity.
Late snapshots cannot adopt identity, and old callbacks cannot change the current
draft/UI or send another attempt. An already invoked operation may save only its
original receipt under its original key; never retarget it to the replacement.
Preserve editable text without automatically moving it to another scope, and
require a fresh authoritative page for a changed binding. No automatic rehome or
new storage ledger is introduced.

Pi's upload slot is currently nil. Keep its upload controls unavailable and do not
call mountUploads or initialize draft/clipboard/metadata storage for Pi in this
package. Ordinary text-only Send uses no attachment IDs and does not fabricate an
upload capability. The existing upload factory can inject a fetch client, but XHR
append and native download anchors bypass that fetch. Any future upload release
must prove every existing path scoped; do not add XHR/download adaptation here.
Codex upload initialization and teardown behavior are preserved by this amendment.

Generic ConversationReady/Interactive/Held page fields remain separate from legacy
Session.Interactive. Current host admission and saved permission govern ordinary
interaction; absent P6 observation must not set generic executionHeld or prevent
the initial stream. Snapshot-bound composer identity is an additional ordinary
gate, independent of P6 capability. Send/interrupt still perform fresh admitted
native checks. Pi does not acquire Codex fork/team/settings behavior; P6 controls
still require their complete positive observation.

**Ordinary P1 capability is independent of optional P6 composition.** Architect0
technically accepted this compatibility boundary and the exact existing
preflight/guarded-writer invariant below in design.md (around line 3331).
Owner1 confirmed committed P3 schema1/2
behavior; owner2 supplied the owning source facts. Lead retains source allocation
and sequencing; this clause waives no required proof.

Generic page interactivity, neutral operation slots, resolver mutation admission
and its active lease must not require piWorkflows, a P6 descriptor, an observation
cache or the complete optional P6 service interface merely to support ordinary
Send/Interrupt. Derive generic availability from the actual configured Pi runtime,
exact common admission, saved permission and real bound optional operation slots.
Keep the page/details projection native-free: a page flag indicates authorized
generic interaction, not a successful native operation. The existing scoped client
and first authoritative snapshot binding remain mandatory. Missing optional slots
refuse their operation; they do not become successful stubs or fallback operations.

Retain transition/profile/package/current binding/full authority/scope/incarnation/
generation/saved-access checks, post-wait verification, real message lock and EX
lease through persisted ACK. Removing composition-specific gates must not remove
the actual retained state's required package support. In particular, absence of
piWorkflows cannot waive policy-layout2/workflow support required by a retained
schema2 mapping or native3 support required by schema3. Use the owning runtime and
existing compatibility/preflight path; no private mapping decoder, schema inference
from nil composition, metadata-only success or caught-error legacy downgrade.

The actual current source boundary is explicit: piPackageInvocation.recheck proves
the selected profile/package and piTeamRecords contract, and piSessionAdmissionLocked
proves binding/authority/original creation identity. Neither is a native mapping
layout lookup. Bind is not that package-layout proof, and ordinary P3 Send validates
the retained mapping/policy/barrier without consuming workflow metadata. Existing
require_compatible_session_backends! invokes pi-team-preflight's
InspectRetainedConversations and require_workflow_contract! at package activation/
transition, requiring the full six-field workflow bundle for retained schema2.
This preflight must cover every retained schema2 mapping, including cold and
binding-retired records. Every first schema2 writer, including current root Create,
requires that full bundle before publication under its existing transition/runtime
ownership. The accepted sufficiency argument is this existing preflight plus
guarded-writer invariant: recheck the immutable selected package/profile after
waits and hold transition SH through the admitted effect. It is not a newly claimed
per-request scan, durable preflight token or another decoder. Unknown mappings or
failed required proof still refuse. Native schema3 remains separately unavailable
until its real guards and consumers are released; it is not enabled by this
schema1/2 clarification.

Retained schema1/nil ToolPolicy remains eligible for its original ordinary P3
Send/Interrupt semantics when those common/state-required gates pass. Nil policy
does not mean Default or B2/Plan safety and cannot enable any P6 effect. New root
creation still requires the accepted captured Default1 policy, actual guards and
createdHere proof; no old mapping is upgraded or retrofitted. A retained present
policy remains enforced by P3's exact current target/generation/native proof.
Pending settings/policy, held state, receipt/callback uncertainty and every other
operation-specific runtime refusal keep their existing meaning.

Generic Send invokes the real ordinary bound operation under its admitted scope;
do not universally require P6 freshPolicy/WorkflowObserver, even when optional P6
composition happens to be configured. Such a requirement would make schema1
unavailable merely by adding the optional service. P6 question/Plan/mode effects
retain their complete fresh policy/idle/content proof requirements. Whenever P6
composition exists, generic mutations still invalidate its observation before the
effect through the same short host map. Present policy/native/attachment failures
propagate; never retry through a less constrained path or clear the composition to
reinterpret failure as optional absence. P3's once-negotiated workflow barrier
remains sticky: lost attachment/ACK refuses rather than downgrading to B1.

Architect0 confirmed the exact lock distinction in design.md (around line 3358).
Interrupt retains its own operation-specific native checks and busy-cancellation
semantics. Do not add Send's idle/receipt-policy gate, wait for the conversation
native Send mutex (`c.mu`) or claim abort proves descendant/effect settlement.
This restriction does not remove C's existing real HTTP MutationLock. Retain the
same s.messageLock(request.ID) for Send and Interrupt and the accepted P2 runtime EX
lease. These outer locks may serialize admission through the bounded persisted-input
Send ACK, but must release before callback/model settlement. Busy Interrupt after
ACK therefore remains available without a native c.mu/idle prerequisite; this does
not promise admission past an in-flight pre-ACK EX owner. A separate `/interrupt`
lock key adds no bypass of EX and is unnecessary. Existing native barrier checks
still apply. Reads/streams remain per-operation SH;
the optional observation wake wrapper may be absent without removing the real
ordinary Watch operation.

Owner2's current central files own the generic page/details, neutral build/resolver,
lease and Send/Interrupt adapter correction. Owner4 receives no new capability or
listener requirement. Focused checks must cover generic configured runtime with
P6 composition absent, schema1/nil ordinary success under proper admission, missing
operation refusal, present-policy mismatch/pending/held failure without fallback,
required-schema package refusal, sticky disconnected attachment, busy Interrupt,
and P6 configured invalidation with unchanged strict P6 effect checks. Keep new
creation Default1 and Codex cases unchanged. No new decoder/API/service/store or
recovery branch is part of this separation.

**Generic details refresh preserves the same Pi binding.** Architect0 technically
accepted this source-sufficient amendment in design.md (around line 3156). It stays
within the existing owner2 view/server and owner4 app.js windows; lead owns source
sequencing. Existing sessionDetails
normalizes legacy interactivity and refreshSessionDetails unconditionally calls
applyRecoveryStatus, so initial Pi carriers alone do not preserve composition.
For validated Pi, owner2 uses the same native-free configurePiSessionPage projection
and emits exactly `sessionBackend:"pi"`, `conversationScope`,
`conversationInteractive` and `conversationHeld` (the last two strict booleans).
Keep legacy Session.Interactive/JSON interactive false. Do not invoke Codex recovery
normalization to manufacture an active Pi recovery status. Unknown or mixed backend
evidence refuses; the existing Codex details branch remains unchanged.

The existing details request must carry the frozen expected conversation-scope
header and selected member, while preserving X-Session-Observation and its checks.
createSessionClient.details uses the page's ordinary request transport, not the C
conversation client's scopedFetch; owner4 must pass the same expectation through
that actual request path. Owner2 compares the namespace under actual owning
admission and after waits before returning the projection, including the exact
selected member. Reads remain native-free. This is the same precondition, not a
new details token or authority grant.

For explicitCodex only, retain applyRecoveryStatus and its existing member behavior.
For Pi, require current read/binding epoch, exact sessionBackend and conversationScope,
and both typed flags before updating ordinary interaction state. Never replace the
frozen scope from payload, invoke Codex recovery, or infer held from an absent P6
observation. Details cannot initialize the first snapshot thread identity, clear
original receipt uncertainty or substitute for fresh native/P6 proof.
A malformed/unavailable refresh cannot turn controls on or clear an
existing hold; retain the existing refresh warning behavior. A confirmed scope or
selected-member replacement invalidates the composer/P6 binding for a fresh page.
Late data does not affect the new binding. Current readyMembers can update the Pi
selector only from that same validated payload; a removed selected member must not
take the legacy automatic redirect-to-lead path. No old draft/attempt follows a
different member, and no Codex team/settings listeners are enabled by the refresh.

Extend the finite composer fixture with first scoped snapshot -> Pi details refresh
preserving interaction/identity; real same-scope held/access loss disabling effects;
missing P6 observation not causing a bootstrap hold; stale/mismatched details and
selected-member removal not retargeting; actual details header propagation; and
unchanged explicit-Codex recovery. No new recovery/lifecycle operation is introduced.

Owner2 owns typed carrier/template/view plus D dispatcher/admission scope checks;
owner4 owns only app.js initialization/scoped fetch/eventsPath/binding teardown and
its focused fixtures in the existing window. No template overlap or new allocation.
Finite acceptance covers empty page identity -> current scoped snapshot -> one
explicit ordinary Send; pre-snapshot no send/key/draft loss; duplicate snapshot
without duplicate listeners; replaced scope/thread and late reads/effect callbacks;
same-key receipt recovery without auto-replay and isolation from other member or
incarnation keys; header/query duplicates, conflicts, reconnect and post-wait
replacement refusal; Pi uploads unmounted/no metadata/XHR/download requests; P6
absence not blocking ordinary composition; and unchanged Codex retry/listeners.
Owners report exact source and focused evidence. No broad UI survey or harness is
required by this design completion.

Use `/api/sessions/<slug>/pi-questions` and `/pi-plan`, with their existing
`responses`, `responses/<uuid>`, `acceptances`, `acceptances/<uuid>` and `mode`
suffixes. Select recipient through one optional `member` query, default lead;
validate exact retained address with no unknown-member fallback. These requests
retain same-origin authenticated/CSRF admission and exact backend/incarnations.
Extend sessionAPIPath narrowly for these suffixes/UUIDs only, route before the
legacy conversation adapter, and never let Pi enter requireCodexSessionBackend.
Permission operations remain `pi-questions.read/respond`, `pi-plan.read/accept/mode`;
mode is separately authorized. Current backend/package/binding checks still gate
all routes; reads may expose retained receipts while effects remain held.

P2 supplies an optional server-authored `piWorkflow` page descriptor with exactly
`{backend:"pi",basePath:"/api/sessions/<canonical-slug>",member:"<retained-address>",namespace:"<opaque-durable-scope>"}`.
The exact template carriers are `data-session-backend` and `data-pi-workflow`.
P2 emits data-session-backend from validated backend selection independently of
descriptor availability: explicit pi or codex, with recognized legacy sessions
normalized to codex on the server. It must not derive that gate from descriptor
presence or successful JSON parsing. data-pi-workflow contains the exact descriptor
as ordinary JSON text escaped by html/template in the quoted attribute; no trusted
HTML bypass or manually concatenated unescaped JSON. Owner4 reads
`body.dataset.sessionBackend` first, then parses `body.dataset.piWorkflow` only for
Pi. Missing/malformed/mismatched Pi descriptor leaves Pi controls unavailable and
does not install Codex handlers. Unknown backend similarly grants no workflow;
the explicit codex branch preserves current listeners and ignores any Pi descriptor.
Member is explicit lead or the selected retained member. BasePath has no query,
fragment or authority; the helper appends only the fixed workflow suffixes and
one encoded member query. Namespace separates backend/workspace/session/member/
conversation incarnations and survives runtime generations. No native path/ID or
generation enters browser storage identity. Absence means no Pi workflow mount.
P6 exports this exact frontend entry point:

```js
mountPiWorkflows({descriptor, roots: {questions, plan, mode, modeStatus},
  fetchRequest, storage, createQuestionCard, onChange})
// returns {refresh({explicit = false} = {}), destroy()}
```

fetchRequest is the raw same-origin fetch function, not app.js's throwing JSON
request wrapper. Automatic refresh reads no-store and calls controller update;
only explicit user refresh may invoke the accepted Plan refresh that clears mode
uncertainty after its settlement fence. Mount and reconnect are not explicit user
refresh. The helper owns cancellation and ignores stale completions after destroy.
P6's standalone UI helper mounts existing mountPiQuestions using
conversationAssets.createQuestionCard and #optional-questions, and mountPiPlan with
an explicit renderer using the existing Plan panel/mode controls. Pinned questions
are sufficient for first functional composition; inline correlation is exposed only
if P2 supplies trusted transcript-entry/group linkage, never text matching.
Skip Codex async-question/Markdown-plan/mode-settings listener registration on
Pi-owned controls at initialization; hiding those controls after mounting cannot
remove competing listeners. Keep unrelated provider settings ownership unchanged.

The API helper uses real no-store reads, exact response/acceptance IDs and the
accepted manual-mode sequencing. Preserve parsed valid 409 rejected ModeResult:
app.js's generic createRequest throws all 409s and cannot be reused unchanged for
setMode. Mount/destroy on the selected durable conversation; pushed updates cannot
clear mode uncertainty. Reuse current connection/explicit-refresh hooks to refresh
the domain views; add no browser interval. Existing Codex rendering remains intact.

| Source package | Owner and exact boundary | Dependency / sufficient acceptance |
| --- | --- | --- |
| P6 projection/read/UI helper | owner4: piplan policy_projection/policy_adapter/read, piquestions admission/read, static/pi-workflow-ui.js, focused fixtures and narrow docs/pi-questions.md | Safely independent using typed fake observations; exact content binding, absent-plan mode and no native GET |
| P3 observation/barrier | owner1: piruntime workflow_observation.go plus short supervisor/callback_types/callbacks/worker/conversation/tool_policy hunks; pi-runtime session/protocol/tool-policy | Atomic complete proof; ordered bounded pre-effect ACK; no lock deadlock, no polling/ledger |
| P2 authority/composition | owner2: shared pi_team_admission.go with architect0, new pi_workflows/pi_workflow_observation, pi_providers, creationflow, operation_state and server route/config/template hunks | Actual package guards + released P3/P6 ports; initialize only new policy; native-free reads and original receipt services |
| Frontend central hookup | proposed owner4 sole app.js window; owner2 retains all template/type carriers | Exact data-session-backend/data-pi-workflow carrier contract and helper; no template overlap; lead releases windows |
| Packaging | P7 | Publish optional workflowObservations:1 only after matching P3 implementation/checks; existing piQuestionsSchema/piPlanSchema/piToolPolicy fences retained |

Checks required in owner fixtures: stale observation racing mutation/ACK/refresh,
ACK timeout before effects, callback witness progress without receipt locks, worker
exit/attachment loss, settings/access/binding change, native event during proof,
pending mutation cannot republish, exact proposal replacement/content mismatch,
absent plan/manual first selection, busy question capture then one idle dispatch,
original duplicate/Unknown no resend, reader GET/Lookup zero native calls, scope and
origin/CSRF rejection, legacy Codex compatibility, frontend teardown and 409 handling.
Functional no-model component evidence must traverse actual callback -> durable
question/plan -> route/view -> admitted action -> ordinary original receipt, plus
manual policy CAS and lost-ACK behavior. Pure fixtures alone do not advertise live
controls. Owner-run checks use existing Nix/monitor rules; this design runs none.

## Retained-lead monitor tools: bounded contract completion

Status: necessary TEAM design item, not source-sufficient yet. Lead requested this
boundary after the completed central checkpoint. Owners2/3 and architect1 confirmed
that no accepted retained-lead Pi monitor start/status/cancel admission, handler or
factory exists. The utility-only monitor handler cannot impersonate it. This
addendum records the exact existing building blocks and missing owning proofs;
it does not freeze a provisional successful handler or allocate implementation.
Architect1 independently owns same-final-Manager constructor assembly and complete
source/resource/callback/utility settlement proof. Those remain dependencies of
the eventual complete package, not work duplicated here.

The existing monitor domain is sufficient for storage and launch mechanics:

- `NewPiOperation(StartRequest,PiOwnerRecord,PiUtilityPolicyRecord,incarnation,at)`
  freezes the original request digest/envelope, utility incarnation and derived
  utility creation/launch IDs; it validates structure, not caller/source authority.
- `Store.ReservePi(ctx,PiTeamWriteAdmission,generation,PiOperation)` uses the
  existing operation file/capacity/admission lock and compares original Owner plus
  RequestDigest for an existing ID. Load the original record on duplicate before
  any policy/incarnation selection; never generate a replacement watcher on retry.
- `PiRuntimeAdapter.Launch(ctx,RuntimeRef,id)` owns utility creation and its original
  input. Its Manager methods enter configured per-effect authority. Do not add an
  outer admission around native Launch or hold a short monitor lock across it.
  Once launch input is reserved, Launch is original Lookup/reconciliation only;
  Unknown, negative or lost replies never authorize another create/bind/send/load.
- `PiReportService.Status(ctx,PiUtilityRecord,inputID,generation)` is utility-only.
  Retained-lead status needs its own exact saved-owner read admission over Store.Get;
  do not fabricate a utility caller or call the Codex Service.Start branch.
- `CancelPi(ctx,PiSessionRecord,generation,id,at)` revokes continuation only and
  has no caller-proof parameter. Its future retained-lead handler must authenticate
  and authorize the current lead independently. It cannot interrupt source commands,
  unload the utility, clear receipt uncertainty or certify settlement/capacity release.

The immutable Pi owner is the exact session/retained lead/original full
SubmissionRef/launch generation. StartRequest remains the existing ID, Brief,
Source and CancellationScope, with the owning digest/validation and ID rules.
Local Source retains its original Argv/Cwd/InputIdentity/Revision/InvocationID;
CI uses its existing provider/run/attempt shape. Parsed tool JSON is only a request,
never proof that the source belongs to this session/input. New starts freeze the
installed verification-watcher policy and applied P4 settings once; duplicates use
the original package/catalog/model/effort/instructions/access/concurrency/settings.
The existing PiPolicyFromCatalog consumer and Server's private validated
installedTeams are available inputs, not an already-composed policy/grant producer.

Three precise missing production boundaries prevent a complete Start contract:

1. **Full active original input, P3 producer.** HostCall exports InputOperationID,
   runtime/subject and native origin/argument proof, but not the full retained
   SubmissionRef. P3's private c.activeRef persists after prompt settlement and
   cannot alone prove active lifetime. Historical NativeOriginInspector and current
   WorkflowObservation.Settings cannot reconstruct original input/settings digest.
   Owner1 confirms a minimal optional same-Manager observational source fit:
   `ReadActiveHostInput(ctx,HostCall) (SubmissionStatus,error)`. Architect0
   technically accepted this exact missing producer in design.md (around line
   2225); it is not an existing method or a complete monitor source release.
   It reuses the existing active verify_origin worker command and original receipt
   owner, with no worker parser/format/ledger/native3 dependency. Capture exact
   retained ref/worker under activeMu, validate call/runtime/subject/input/argument
   hash, read original durable Accepted status plus witness without c.mu/receipt
   waits, perform active origin verification outside locks, then recheck the captured
   tuple/worker/generation/unknown state and context after waits. Return the unchanged
   full original status only on positive proof. The caller must invoke after its
   admission wait and check cancellation at the actual effect boundary; the result
   is an observation, not reusable authority. Adding Ref to HostCall alone would
   not prove post-wait liveness. Owner1 supplied the exact source/check boundary
   below; lead release and implementation remain outstanding.
2. **Source ownership, existing local/CI owner.** Owner2 confirms no current P2
   primitive proves ownership of an actual local invocation or exact CI run/attempt.
   Session admission and WithPiInputRead consume exact scope/full refs but mint
   neither source nor input proof. Architect1's existing source/settlement work must
   identify whether its same authoritative local/CI records can also prove original
   session/caller/input/invocation ownership at Start, or name the exact absent
   owning export. No source command is rerun to manufacture proof; no parallel
   collector/registry or trusted model-supplied descriptor is introduced here.
3. **Retained-lead service composition, P5 domain plus P2 consumer.** After those
   proofs settle, the handler must bind a trusted retained lead from the authenticated
   B1 call, never a utility/roster member supplied by arguments; distinguish new
   Start admission from original-owner status and continuation-cancel. Current
   package/profile/full runtime/session/permission gates and frozen policy/source
   proof must precede durable reservation. Existing WithPiTeamWrite/WithPiInputRead
   are scoped consumers, not that missing authority. PiUtilityEffectVerifier remains
   the existing per-effect consumer for the eventual central implementation. Its
   exact complete lead service/factory signatures are deliberately not invented
   until the two producers above are settled. Utility factory stays status/report
   only; retained start/status/cancel stays unregistered meanwhile.

### Active-input reader: exact source and verification boundary

Status: technically accepted by architect0 in canonical design.md (around line
2274; lead report 62e45ab9). This accepts the exact reader source and verification
boundary below. Lead source/index release remains required; implementation,
checkpoint amendment and complete monitor acceptance are not implied.

Owner1's confirmed smallest package uses new
`portal/internal/piruntime/active_host_input.go` and `active_host_input_test.go`.
The new implementation file declares optional `ActiveHostInputReader` with
`ReadActiveHostInput(context.Context,HostCall) (SubmissionStatus,error)`, the
same-Manager method and the private supervisor helper. The only existing runtime
file hunk is supervisor.go's ordinary invoke case: decode HostCall and call
`s.readActiveHostInput(ctx,call)` (approximately five to seven lines). Add a narrow
paragraph to docs/pi-runtime.md's existing callback section. No controller,
manager, callback_types, callback/worker or receipt-schema change is required.

Reuse m.call, validateHostCall, s.member, activeMu capture/recheck,
receiptEngine.loadOwned and the existing active verify_origin worker command.
Validate the ordinary runtime envelope/current retained subject and context;
utility subjects refuse. Load the unchanged original Accepted status through
ref.retained, never current-settings digest reconstruction or activeRef mutation.
Original native witness/origin agreement and every accepted post-await check above
remain required. Missing optional support is unavailable, with no fallback.

Finite owning tests cover wrong runtime/utility/operation/arguments/token/worker/
generation, Unknown/nonaccepted/missing-witness inputs, cancellation or ref/worker
replacement during active verification, and settled JS input despite surviving
c.activeRef. Prove callback progress while c.mu or the receipt writer is held.
Start with compile/pure checks. If lead releases the component check, extend one
existing Manager/Unix/pinned-SDK callback case using the unchanged supervisorFixture
and committed worker8fed: read the exact full Accepted ref inside a delayed B1
handler, then refuse after original native input settlement. Use the required
fresh watcher for that affected component; no unchanged SDK batch or second
framing/parser/harness is requested.

supervisor.go also has native work in progress. A separate reader checkpoint needs
an isolated tested ordinary-read case patch preserving the parked/current native
hunks. Lead decides that source/index sequencing; this boundary is not permission
to amend the completed checkpoint or to take ownership of native source. No native3
dependency is introduced. Complete retained-lead monitor registration remains
blocked on the source/effect/settlement contracts above after this reader exists.

The eventual sufficient package must preserve original request/creation/input IDs,
early callback versus Accepted receipt ordering, admission before short store lock,
no native operation under a store lock, duplicate/restart original-lookup-only
semantics and Unknown retention. Durable reports do not settle their own reporting
callback. Capacity release requires architect1's complete positive original source,
resource/tool/callback and utility settlement proof; continuation cancellation does
not supply it. Architect1's direct owner1 facts confirm no complete utility
certificate export: LookupUtility proves admission/receipt only, Resources is not
a complete identity inventory, InspectResource covers one known handle, and
ObserveWorkflow is retained-only. An already-unloaded VerifiedExit result may be
bookkeeping rather than proof about the original worker. Original input plus
captured worker incarnation and complete attributable drain need their owning
observational proof; missing restart provenance remains held. The same missing
authoritative local/CI source record must prove Start ownership and later terminal
state. These are architect1's exact dependencies, not a collector defined here.
Existing schema1 Codex and schema2 Pi guards/paths remain, with no
native3 prerequisite or edits to the completed checkpoint.

Finite acceptance, once the contract is sufficient and lead releases it, must use
the existing fixtures: authenticated active retained lead Start with exact source/
policy -> one reservation/create/original launch input; wrong caller/source/input
or stale post-wait proof refuses; duplicate and lost ACK preserve IDs and do not
rerun; original-owner status works while held without activation; cancel suppresses
continuation only; utility cannot start/cancel or act as lead; early report returns
its original durable event before later settlement; incomplete source/tool/callback
evidence retains capacity, complete proof releases it; restart/Unknown has zero
replacement effects; unchanged Codex behavior. No new scheduler, server, client,
ledger, parser or harness follows from this addendum.

## Final-review correction: neutral history cursor and message presentation

Status: technically accepted by architect0 in canonical design.md (lead report
0920a33b), including the exact neutral/legacy cursor limits, D error mapping,
shared projection and HTTP/renderer checks. Lead requested this correction while reviewer0
reviews immutable D db4..cd5fd5 and C dd90..a2b58b5e. Those review trees remain
unchanged. Monitor source/settlement design is independent and remains blocked.
Proposed single implementation owner is implementer0, only after lead explicitly
transfers D adapter ownership and grants source/index windows; this brief allocates
no source. Owner0 confirmed the C facts below against a2b58b5e.

Actual C handler.go rejects page queries above 256 bytes and accepts only a
32-character URL-safe cursor. D piruntime/adapter.go emits the existing base64url
JSON position containing Version, Scope, Generation, Snapshot and End, so a real
continuation fails before its owning reader runs. D also returns invalid_cursor
and stale_cursor, while C accepts only transcript_cursor_invalid (400),
transcript_cursor_expired (409) and transcript_reset_required (409). Separately,
D projects native user/assistant roles unchanged; the shared renderer classifies
those as activity and hides them in Messages. These are composition defects;
neither requires a new cursor store, history parser or browser backend branch.

### Cursor boundary and error semantics

- Preserve legacy NewHandler's exact 32-character URL-safe cursor and 256-byte
  raw-query checks. Set a private constructor-owned handler policy after the
  common NewBackendHandler construction; no public selector or backend-name
  inference, and do not reuse the unrelated legacyQueueReconcile flag.
- NewBackendHandler accepts one nonempty opaque cursor of at most 5462 ASCII
  URL-safe characters (A-Z, a-z, 0-9, underscore, hyphen). This is the unpadded
  base64url ceiling for D's existing 4096-byte decoded position limit. Cap the
  raw query before ParseQuery at 16393 bytes (7 for cursor= plus three times
  5462, allowing percent-escaped permitted characters). Check the decoded token
  bound/alphabet separately; do not decode or interpret adapter positions in C.
  Omitted cursor means newest; present-empty, duplicate/unknown parameters,
  malformed query escapes, invalid alphabet and oversized input remain 400.
- D checks encoded length/alphabet before base64 decoding, retains its 4096-byte
  decoded bound and existing strictDecode/position format. Malformed encoding,
  JSON/field shape, unsupported Version, malformed digest/scope/generation or
  nonpositive End return transcript_cursor_invalid. A structurally valid cursor
  whose Scope or Generation differs from the admitted identity, whose Snapshot
  differs from the current history, or whose End exceeds that history returns
  transcript_reset_required. Do not invent expiry: this adapter owns no expiring
  cursor registry. Preserve full scope/generation/snapshot checks and page order.
- Every successful emitted continuation must fit the same bound. Preserve GET,
  exact origin, read permission, admitted identity, Verify, returned ThreadID and
  at-most-100-entry checks and existing transform/attachment/presentation ordering.
  Cursor errors stay redacted in server logs. Browser cursor reset remains the
  existing expired/reset handling; it grants no resend or mutation authority.

### Presentation boundary

Normalize only the existing D projectTranscript projection: retained user becomes
userMessage; retained assistant and live assistant become agentMessage. Keep
toolResult as activity and keep unknown/native non-message entries excluded as
before. Preserve ItemID, TurnID/latest turn, timestamps, live inProgress status,
text extraction and HTML escaping. Do not synthesize receipt/client-input IDs,
team communication, native authority or a different durable transcript. Snapshot
and page already share this function and must produce identical vocabulary.
The shared transcriptEntryPresentation/transcriptEntryVisible and Messages filter
remain backend-independent; no Pi condition, native-role aliases or new client.
The existing assistant display label is outside this bounded correctness fix.

### Files, dependency, acceptance and finite checks

C source boundary: conversation/handler.go and conversation/backend.go for the
private constructor policy; conversation/backend/types.go documentation of
HistoryCursor; existing conversation/handler_test.go and backend_external_test.go;
test/conversation_browser_contract_test.cjs; docs/reference.md's neutral adapter
paragraph (remove the universal 32-character promise while preserving the legacy
cursor-cache description). No native codex client or browser implementation edit.
D boundary: portal/internal/piruntime/adapter.go and adapter_test.go, with the
existing snapshotWorker/supervisorFixture. A narrow existing D runtime-doc
projection paragraph may state normalization/error semantics. No new production
parser, protocol, persisted schema, service, registry or ledger.

Acceptance must cross the real boundaries rather than stop at direct ReadPage:

1. Through actual NewBackendHandler and the actual Pi adapter, fetch a newest
   page with more than 50 entries, follow its emitted cursor unchanged and obtain
   the remaining chronological rows with the same trusted identity. Repeat the
   cursor without consuming it. D's existing fixture is sufficient; no SDK run.
2. Assert exact 400 invalid and 409 reset JSON codes for malformed, over-limit,
   duplicate/unknown-query, cross-scope/generation and changed-history cursors;
   no generic 503 for these expected dispositions. Cover neutral encoded/raw
   boundaries and legacy 32/256 acceptance/refusal. Preserve 501 paging absence,
   origin/read refusal, page identity/count and hook order.
3. Assert actual adapter HTTP rows use userMessage/agentMessage for retained and
   live messages. Exercise those response-shaped rows in the existing shared
   renderer/browser contract: Messages includes both roles, Activity retains
   toolResult, All retains all supported rows, text/HTML escaping and live status
   survive. Keep the existing Codex presentation/filter and receipt retry tests.
   The Go HTTP assertions must tie the browser fixture vocabulary to the actual
   projection; a direct adapter-only pass cannot certify HTTP paging.

Use C's existing package-derived Go checks and existing Node browser contract,
then D's focused piruntime adapter/HTTP tests in its declared environment. Owner
reports exact commands, tested heads/input graph, failures and the bounded result;
long/uncertain checks follow the existing watcher rule, with no broad SDK batch.

C's tested fix commit must be published before the D consumer pin update. The
same complete package needs the existing D codex-web Go module/checksum and Nix
flake/vendor pin owner window (portal/go.mod, portal/go.sum, flake.lock and the
existing vendor hash in nix/workspace-portal.nix as actually required). Lead may
sequence that mechanical pin work with its current owner; no pin edit is released
here. Verify D compiles/tests against the exact new C commit, not a local replace
alone. No persisted migration or repair is introduced. Old browser assets accept
the normalized vocabulary; old C handler still rejects Pi continuation tokens,
so corrected D must ship with its corrected C dependency. An ephemeral old cursor
may reset through existing refresh behavior; rollback does not rewrite history.
Return the narrow fix and evidence to the same final reviewer after lead release;
do not replace or interrupt the current full review.

### Final-report delta: R1 busy status and R5 terminal diagnostics

Status: technically accepted and source-sufficient, recorded by architect0 in
canonical design.md's combined cursor/presentation section (lead report 4350025f). This
extends only R1/R5 of the final report; the accepted cursor/vocabulary R1/R3
boundary above is unchanged. Lead retains the proposed combined implementer0
package, D adapter transfer and all source/index/pin windows. Frozen D/C review
trees remain immutable; no source allocation or replacement review follows here.

Actual D app.js:5631 sets threadActive only for status active, and its composer
Interrupt gate at 5157 consumes that value. Therefore projectTranscript must emit
active when snapshot.Busy is true, idle otherwise, with the existing snapshot.Held
override still emitting held. This presentation correction applies to Read and
ReadPage through their one projection. It does not prove native settlement,
authorize effects or change ordinary Send/Interrupt admission.

Owner1 confirmed the pinned Pi 1.5.2 AssistantMessage contract from
@earendil-works/pi-ai/dist/types.d.ts: stopReason is required and permits pending,
stop, length, toolUse, error, aborted and deferred; errorMessage is optional string
with no SDK length/escaping bound. Cancellation is aborted, not cancelled. The
separate optional rawStopReason is outside this fix. WorkerSession retains the
whole live message on message_start/update and clears it at message_end; snapshot
returns that raw value plus persisted branch entries. Go workerSnapshot preserves
both. Persisted post-end snapshots are the terminal diagnostic source; nativeEvent
does not contain error text and must not become a substitute producer.

Freeze the following display-only projection in D's existing adapter:

- Extend the existing native assistant message view to read optional errorMessage
  together with stopReason, also for LiveMessage. Use the existing JSON decoding
  and text extraction, not a second history parser or native event collector.
- When the projected assistant text is empty/whitespace-only and the exact native
  stopReason is error or aborted, project one existing kind:error row in place of
  that empty assistant row. Set Text to a diagnostic containing the literal
  stopReason and optional errorMessage. With no message, the reason alone must
  still produce visible nonempty text. Other reasons never imply a failure;
  nonempty assistant content keeps the accepted agentMessage projection.
- Bound the entire synthesized diagnostic Text to 4096 UTF-8 bytes, including
  labels and a truncation indicator when needed. Truncate only at a code-point
  boundary, retain the reason before consuming the error-message budget and
  apply html.EscapeString after bounding. HTML must be exactly the escaped Text;
  never interpret provider diagnostics as markup, links, Markdown or commands.
  The error renderer uses its existing literal-text path. This bound applies to
  synthesized diagnostics and does not silently truncate ordinary message text.
- Preserve the original persisted ItemID, associated TurnID, timestamp and order.
  Live diagnostics retain the existing pi-stream identity and existing live
  TurnStatus; snapshot Busy/Held determines the transcript status. Do not append
  a second synthetic terminal event, fabricate receipt/client-input IDs, infer a
  terminal execution state from the display row or drop the original native data.
  Malformed typed JSON follows the existing decode refusal/skip path; unknown
  stop reasons or errorMessage alone do not manufacture error/cancellation proof.
- Existing exact read identity/admission/page checks remain. An error/aborted
  native result after an Accepted input does not turn that input into NotSubmitted,
  clear uncertainty, enable retry, change Lookup, or alter original admission,
  callback/native policy or recovery state. No classifier, retry action, schema,
  new wire field or C/browser implementation branch is introduced.

Exact additional files are D portal/internal/piruntime/adapter.go and
adapter_test.go, plus the already-scoped docs/pi-runtime.md projection paragraph;
C test/conversation_browser_contract_test.cjs may extend its existing error-row
fixture assertions. Reuse the preceding actual adapter-through-NewBackendHandler
HTTP fixture and existing sharedrenderer contract. No app.js or C API/source
change is required for these deltas. Owner0 confirms kind:error is always visible
including Messages, carries no delivery semantics and accepts this plain-text
projection. Owner1's SDK/source facts require no new SDK execution to validate
this bounded presentation fix.

Add only these finite cases to the combined R1/R3/R5 checks:

1. Actual browser-facing newest/page read: Busy -> active, not running; idle
   remains idle; Busy+Held remains held. Tie active to the existing consumer's
   busy/Interrupt interpretation without modifying its permission gates.
2. Persisted empty assistant error and aborted, each with/without errorMessage,
   remain visible nonempty kind:error rows through actual HTTP and the shared
   Messages renderer. Preserve native IDs/turn/timestamps and verify the same
   projection for a live value when those fields are present, then the persisted
   post-end value without depending on a retained live message.
3. Oversized multi-byte diagnostics remain valid UTF-8 and within the 4096-byte
   Text limit, with a truncation indicator. Include markup/script-shaped strings,
   quotes and ampersands; assert escaped HTML and literal rendered/copied text,
   with no execution or links. Normal text and non-error stop reasons retain
   their existing behavior; malformed types cannot produce diagnostic authority.
4. Preserve the original Accepted result/ref/receipt in the existing admitted
   input fixture while reading the later diagnostic. No new Send, retry flag or
   recovery mutation is permitted. Existing Codex error/filter and receipt tests
   remain unchanged regressions, alongside the accepted R3 cursor checks.

The preceding package's focused Go/Node, exact C-then-D pin and same-reviewer
evidence requirements cover this addendum. There is no persisted migration,
monitor prerequisite, new native launch, broad SDK batch or extra source window.

## CI compatibility correction: supported legacy Codex schema 2

Status: technically accepted and source-sufficient, recorded by architect0 in
canonical design.md's final-review neutral history/presentation section under
CI legacy-Codex compatibility correction. Lead owns source release. Proposed implementer0 owns only
portal/internal/web/pi_workflows.go's workflowPageBackend Codex schema classifier
hunk and existing server_test.go/session_details_lifecycle_test.go fixtures and
focused checks. Implementer2's separate isolated-branch role-helper hunk is outside
this window, even where the product filename is shared. No app.js, C, Pi creation,
role helper, decoder, registry, conversion or dependency-pin change is required.

Evidence is exact D 1e6687750e51842e34641470bff32e87939bd71f and terminal failed
Check 43328502991, recorded in review-transcript-evidence.md. Owner0's trace and
the bounded source read distinguish one product compatibility defect from two
fixture omissions; none is evidence of a flaky test or a reason to rerun unchanged
CI. All three affected files were unchanged through that CI checkpoint.

The owning Manifest.Validate accepts schema 1/2/3 legacy Codex and schema 4 Pi.
Schema 2 requires creation.state creating, initial_goal_sent false and a present
initial_goal_attempted marker; an empty Codex object and absent thread are valid.
The normal session.Find path decodes and validates this manifest before producing
the summary. The real TestSessionWithoutAThreadExplainsHowToStartSharedSessions
fixture follows that path with both goal flags false and codex: {}. Current
workflowPageBackend nevertheless allows only schemas 1/3 after its existing
backend guards and returns 409. This is the product defect.

The smallest product change admits schema 2 alongside 1/3 at that exact whitelist.
Keep the preceding BackendBindingStore.Load classification/conflict checks,
requireCodexSessionBackend creation-record fences and LoadRuntimeAuthority check
unchanged, including propagation of failures other than the existing not-found
case. Keep the owning manifest validation as the production source of supported
legacy state; do not reconstruct it or introduce a generic backend selector.
Schema 0/unknown, malformed/mixed manifests, conflicting bindings, orphan Pi
creation/authority state and Pi-to-Codex fallback remain refused. Absence of a Pi
binding or authority alone is not positive Codex proof: it is only one part of
the existing guarded path plus a supported, validated legacy manifest.

Classification is separate from a verified conversation or write permission.
setWorkflowPageData still sets HasConversation only for Codex with a nonempty
ThreadID. A valid schema-2 no-thread page returns its original explanation and
dev-session start guidance without fabricating a thread, runtime authority,
readiness or native dispatch. Legacy resolveConversation still refuses a missing
verified thread and retains canonical authorization, current identity/authority,
recovery, maintenance, lifecycle, permission and mutation checks through waits.
Existing Codex read-only/writable behavior and Pi classification are unchanged.

The two details cases bypass session.Find and construct Manifest{Slug: example},
which silently supplies Schema 0. Set explicit existing legacy Schema 1 in
TestSessionDetailsReplaceClusterStateAfterStopAndReset and
TestSessionDetailsVerifiedPendingLifecycle, retaining absent thread and all other
fixture state. These are truthful fixture inputs, not permission to admit schema
0 in production. Preserve all cluster secret/busy/reset/stopped assertions and
all verified lifecycle absent/pending/unsafe/conflicting assertions. In particular,
PendingLifecycle runs before classification; unsafe/conflicting still return 503.
Do not change the expected successful 200 responses to 409 to hide the defect.

Finite acceptance/checks within those existing files:

- The real schema-2/no-thread HTTP page returns 200, the existing shared-session
  explanation/start command and existing delete control. It has no fabricated
  conversation/composer authority. An attempted conversation mutation still
  refuses before native Send/creation; classification supplies no missing thread.
- Both corrected details fixtures retain their original successful behavior and
  payload assertions; lifecycle unsafe/conflicting retain 503. Include supported
  schema-2 creating/no-thread details success through the normal loaded-summary
  path, without making GET start, repair, convert or load a backend.
- Reuse the existing small backend/page regression matrix for supported Codex
  schemas 1/3, read-only versus writable authority, valid Pi, schema 0/unknown,
  malformed/mixed manifests and binding/creation/authority conflicts. Production
  malformed-manifest cases go through the owning decoder; synthetic summaries
  claiming success must explicitly use supported schema. Keep no-Pi absence-only
  refusal and prove denied/no-thread cases invoke no native write.

Run the three named failing web tests plus the affected existing backend/page
regressions first in the repository's declared environment. Report exact source,
commands/results and finite scope; wider web/CI work remains lead-owned and uses
the existing watcher rule. No test/build/native action is authorized by this
design assignment. There is no schema migration, new backend or changed persisted
state. Old supported Codex creating records become readable as intended; rollback
only restores the observed page rejection and does not transform those records.
Keep reviewed/current trees frozen until lead's explicit disjoint source window.

### Initial registration CI refusal: evidence and next diagnostic

Current result: owner0 completed the single archive pre-register diagnostic with
the exact ead7/1af5 runtime. Runtime realization qg0 exited 0 in 1059.106 seconds;
diagnostic cgm exited 1 in 110.041 seconds at its intentional diagnostic stop.
Copied metadata.json and stderr were read directly from
/tmp/2026-11-11-pi-codex-migration-review-register-diagnostic/guest-copied/;
owner0 reports their bytes match the raw driver output in diagnostic-check.log.
The probe observed uid/euid 1000, canonical state root owned 1000:100 with mode
0755 and owner rwx access, and canonical owned workspace mode 0755. Selected
profile and portal resolved to the exact recorded 1af5 package. The explicit
scanner argv below exited 1 in 0.908479 seconds, with zero stdout bytes and 44
stderr bytes: `workspace-portal: Pi runtime scope mismatch\n`. Stdin was closed;
there was no timeout, signal or truncation under the original bounds.

This establishes a concrete archive-fixture state-root mode conflict with
InspectRetainedConversations' exact-0700 requirement; workspace mode 0755 is not
that root-mode restriction. It does not establish that changing the mode alone
makes the scanner or registration succeed. Original register never ran in this
diagnostic (the registry was absent), no repair or retry occurred, and VM cleanup
was terminal. Original post-register activation and the distinct creation/fbv6
package remain outside this evidence. The temporary diagnostic hunk is reported
uncommitted/frozen. Any correction and follow-up check require a new lead window;
this result grants none and does not relax an owning permission check.

Initial assessment and proposed diagnostic below are retained to show the
previous uncertainty and bounded evidence plan, factually accepted by architect0.
The Nix expression was source-derived and unevaluated at that assessment; the
owner0 result above is the later execution evidence. No canonical design
amendment was needed for the initial factual acceptance.
Exact source is ead7e362cb2354d908023eb45399b9263b16f5ce, Check
43335486679 attempt 1. Owner0 reports terminal failure: fast passed, creation and
archive failed, host skipped, monitor joined. This task does not monitor that run.
Completed early-job-131590478896.log (archive) and early-job-131590478898.log
(creation), under /tmp/2026-11-11-pi-codex-migration-review-codex-schema2-ci-43335486679/,
byte-match owner0's final copies. Architect2 performed no application/test
execution or source change for the assessment or result recording.

Both guests booted and ran the first workspace-host register as developer through
runuser with XDG_RUNTIME_DIR=/run/user/1000. Workspace is
/home/developer/workspace; source state variable is
/home/developer/.local/state/dev-workspaces. Archive's actual package is
/nix/store/1af5ng3gyyl0j05ap29661fm121bcm19-dev-workspace-0.2.0; creation's is
/nix/store/fbv6cqjr2gl54yd97mkd4abnc3f5rvvw-dev-workspace-0.2.0.
The logs show Pi team preflight reader failed, then profile/bin/workspace-host
_activate failure. They do not show the scanner argv, exit status, stdout/stderr,
effective UID, root mode/owner or canonical paths. PAM reports a developer login;
that is not a captured scanner effective-UID observation.

The source-derived activation invocation is:

```text
PACKAGE/bin/workspace-portal pi-team-preflight --state-root /home/developer/.local/state/dev-workspaces --workspace /home/developer/workspace
```

workspace-host run_pi_team_preflight runs the executing package's helper with
explicit state and all registered workspace roots. It limits stdout to 4 MiB,
stderr to 4096 bytes and elapsed time to 30 seconds, joins the child, then replaces
a nonzero exit with the observed generic error. The log therefore establishes
failure of the child, not which owning validation refused. First register's
pre-registration empty registry avoids this child; registry registration precedes
the installed profile's _activate, whose now-nonempty root set invokes it.

The exact test setup uses plain mkdir -p: session-archive-lifecycle.nix:258 and
session-creation.nix:1058. Mode is a candidate, not an observed guest fact. More
precisely, InspectRetainedUtilities uses ownedDirectory's owner/rwx-bit check,
which can admit 0755; subsequent InspectRetainedConversations explicitly requires
the existing state root to be an owned directory of exact mode 0700 before checking
whether its pi-runtime namespace exists. Earlier scanner namespaces and workspace
canonical/ownership checks can also refuse. Neither a generic error nor success
of unrelated pure tests selects one cause.

Owner0 has no saved local guest or driver state. Both remote logs explicitly show
cleanup, kill QemuMachine and QEMU SIGTERM; local artifacts are logs/status JSON.
Additional remote failed-build/artifact retention is unknown. Use an existing
owner-confirmed retained artifact only if available through its ordinary test
interface; do not adopt a runner, inspect another session or edit raw VM disks.
The available evidence cannot supply the missing guest observations.

Smallest proposed next package is owner0's isolated diagnostic hunk in existing
nix/tests/session-archive-lifecycle.nix, immediately before its register call at
280, after the unchanged profile installation. Keep the original setup/umask;
do not chmod/chown or add a private-mode fix before observation. Under the same
user_prefix, run a short Python read-only probe via the existing machine.execute
interface. Capture:

- os.getuid/geteuid, relevant explicit HOME/XDG/DEV_WORKSPACES state/profile
  selectors only, state/workspace literal paths and realpaths, lstat type/mode/
  UID/GID plus access results, and resolved selected profile/package identity.
  Do not dump the environment, provider configuration or credentials.
- The exact argv list above using that package, supplied to subprocess directly
  without shell reconstruction, stdin closed. Capture return code and separate
  stdout/stderr under the existing 30-second limit and existing output bounds.
  Timeout, signal or truncation must be explicit; no automatic second attempt.
- Print the compact metadata/diagnostic into the driver log and preserve complete
  bounded outputs using the existing driver evidence mechanism before any failing
  assertion. Do not rely on creation's later copy_from_vm finally block: first
  registration fails before that block is entered.

For this diagnostic invocation, stop deliberately immediately after the capture,
before register or later test steps, and label that termination diagnostic-only.
Do not report it as a passing archive check. This is one temporary hunk in the
existing test, not a new harness, product flag or alternate registration path.
Retain the exact immutable ead7 package/module inputs while evaluating this hunk;
changing a test file must not silently select a newly built runtime source graph.
The existing archive test takes pkgs, self and devWorkspace, so owner0 can import
the isolated amended test with self from the exact ead7 flake, pkgs from that
flake's nixpkgs and devWorkspace from its packages.x86_64-linux.default. Before
execution confirm its selected package equals the recorded archive store path.
Use the ordinary nix build --no-link --print-build-logs --keep-failed invocation
for that imported test derivation; retain the exact expression/input receipt.
No existing main flake/default/pin or CI workflow needs editing.

Prospective command, only after lead releases owner0's diagnostic test hunk and
names its isolated path (the environment value is that existing test file):

```sh
PI_REGISTRATION_DIAG_TEST=/absolute/owner0-isolated/nix/tests/session-archive-lifecycle.nix \
nix build --impure --no-link --print-build-logs --keep-failed --expr '
  let
    base = builtins.getFlake "git+file:///home/aither/workspace/ai/vpsfree.cz/repos/dev-workspace.git?rev=ead7e362cb2354d908023eb45399b9263b16f5ce";
    pkgs = import base.inputs.nixpkgs { system = "x86_64-linux"; };
  in import (builtins.toPath (builtins.getEnv "PI_REGISTRATION_DIAG_TEST")) {
    inherit pkgs;
    self = base;
    devWorkspace = base.packages.x86_64-linux.default;
  }
'
```

This is a source-derived command, not a claimed evaluated or executed check.

Cost/stopping condition: one existing archive guest boot/setup and at most one
30-second scanner read, then stop before register. Original logs show about
15 seconds guest uptime at registration; derivation realization may dominate
(the prior job spent roughly ten minutes before failure). Use one fresh watcher
for the authorized build/VM invocation, reuse available exact package inputs and
reassess missing substitutes before an unexpected long rebuild. Do not run both
full VM campaigns or increase their timeouts. Creation's distinct package remains
unproven by an archive-only diagnostic; repeat its corresponding pre-register
hunk only if the first result leaves a concrete package-specific question and
lead releases that next check.

A faster pure owning reproduction may invoke the same packaged readonly scanner
against separate disposable canonical roots owned by the effective user, one
empty state root deliberately 0755 and one 0700, with no retained namespaces.
Capture exact argv/status/output. This can establish the owner's mode-dependent
behavior and expected diagnostic, without register/activation/repair or native
state. It cannot establish the failed guests' actual mode, owner, canonicality,
environment or scanner result. No such reproduction has run or is released here.
If the actual guest probe passes, do not call the original failure transient:
compare captured package/root/registry inputs and stop with the unresolved delta.

Acceptance is a specific first refusing validation supported by actual guest
metadata and scanner output, or an explicitly bounded remaining unknown. Any
subsequent fixture/product fix needs its own evidence-based lead source window;
never relax product permissions or infer success from the generic wrapper error.
R4 review, current owner0 CI/fix ownership and all unrelated work remain separate.

### Root producer compatibility: fixture-only mode correction is insufficient

Status: corrected root-only distinction technically accepted by architect0 in
canonical design.md:4957 (lead report 846d1283). The absence-only exception and
fixture chmod proposals are superseded. Source and verification release remain
lead-owned.

Bounded follow-up at exact ead7 and supported predecessor db4b0fa62633b925e1917ec880737e1776f82cc8
finds a product compatibility boundary, not authorization to chmod the fixtures.
At ead7 workspace-host:3721 and predecessor:3566, with_transition_lock uses
FileUtils.mkdir_p(File.dirname(transition_lock_file), mode: 0o700). It creates a
missing generic state root privately but does not change or reject the mode of an
existing root. Profile-parent setup likewise uses mkdir_p(mode: 0o700), at ead7:789
and predecessor:785. The explicit chmod in write_pending_codex_update applies to
@state/codex because pending_codex_file is @state/codex/pending; registry chmod
applies to the separate config directory. Neither establishes an exact-0700
generic-root requirement. The bounded owning docs describe private registry and
per-workspace/namespaced state; they do not prescribe a generic-root migration.

Thus an existing canonical, same-user, non-group/world-writable 0755 generic root
can be retained by ordinary supported Codex initialization. The observed VM setup
exercises that input. Altering only the two mkdir-p fixture lines to 0700 would
mask the new unconditional reader requirement instead of resolving compatibility.
Do not change either setup, other directory modes or original assertions on that
basis; preserve original failed receipts and the diagnostic result.

The writer join rules out an absence-only exception. Exact ead7 manager.go:59
ownedDirectory admits canonical owned owner-rwx roots (Perm & 0700 == 0700),
including 0755; NewManager applies it to UserStateRoot. Ensure:177 calls
stateDirectory then runtimeLock before reserving/writing runtime state.
receipts.go:166 makePrivateDirectory returns for an existing directory without
chmod or exact-mode validation, then creates missing descendants with Mkdir0700
and parent Sync. A valid 0755 generic root can therefore contain newly written
private pi-runtime state. Owner1 independently confirms the same writer contract,
including supervisor configuration and Create/loadOwnedPolicy consumers. There
is no generic-parent exact-0700 pre-effect gate to rely on.

The necessary product boundary is
portal/internal/piruntime/retained_conversation_inspection.go:
InspectRetainedConversations. It currently subjects the generic user-state parent
to its exact-0700 retained-Pi-directory helper before inspecting pi-runtime
absence. Existing native mappings/namespaces and every record must retain their
strict checks. Superseding the initial absence-only candidate, use a separate
read-only generic-parent check for both absent and present Pi state: existing
real directory with supplied path equal to its canonical resolved path, same
effective-user ownership, owner rwx plus access check and no group or other write
bits. Preserve context/workspace validation; refuse symlinks,
noncanonical paths, foreign/unsafe parents and non-ENOENT lookup errors. Do not
blindly reuse ownedDirectory's broader writable-mode acceptance. Starting at
pi-runtime and throughout its namespace/session/record descendants, keep the
existing exact-0700 directory and exact private-record checks unchanged, including
identity, schema 1/2, HasInstructions validation and inspection budgets. Missing
pi-runtime remains ordinary absence; present symlink/malformed/unreadable state
never becomes absence. Do not skip the complete team scanner or its other domain
inventories, chmod state, create a namespace, repair data or change writer APIs.

This accepted reader distinction requires a lead product source window before
implementation; a fixture-only window is
not source-sufficient. If the owner cannot preserve the strict present-state path
with that bounded parent/child distinction, return the exact reader invariant conflict
rather than force a test pass. Source ownership remains prospective owner0 with
owner5's accepted fold and reviewer0 sequencing controlled by lead.

Finite prospective evidence belongs beside the owning reader in
retained_conversation_inspection_test.go and the existing pi-team-preflight tests:
valid canonical owned 0755 root with absent pi-runtime yields empty inventory;
the actual owning directory/record writer creates private Pi descendants under
a 0755 parent and their exact retained inventory remains readable. Owner0's known
currentRuntimeFixture seam supplies NewManager, reserveRuntimeRecord and actual
writePrivate with Host/Dial hard failures; it can prove this without an SDK worker.
The generic root must be 0755 before the first previously absent pi-runtime/
workspace/session chain is created. Reuse/factor the existing fixture into fresh
owned state rather than chmod only after its private chain already exists. Assert
initial absence, resulting 0700 children and unchanged 0755 parent. Validated
schema-1/2 mapping fixtures are codec inputs; label the evidence as actual
directory/record production and retained inspection, not native Create execution.
No new production helper/export or pure Create port is needed. 0700
absence/present-state behavior remains unchanged; foreign, writable,
symlink/noncanonical and non-ENOENT cases refuse; nonprivate Pi children still
refuse. Preserve all mode/identity/schema/receipt checks below the generic parent
and prove no read mutates paths or modes. Exercise the actual packaged scanner's
no-Pi and retained-state outputs as well as the reader. Run quick owning checks and
normal Go formatting/compile checks before intended commits/review; none ran here.

Real registration still requires the existing archive test's original setup to
pass workspace-host register, profile activation and its established service
readiness assertions. A pre-register scanner pass alone cannot establish that.
Reuse the realized 1af5/459-path closure and unchanged dependencies where valid,
but a product reader change necessarily needs a new exact package identity; do
not claim the unchanged 1af5 binary contains the correction. After source/quick/
review sequencing and explicit lead launch release, one bounded owning archive
verification must use the corrected package, preserve registry/activation guards
and stop at the accepted initial registration/readiness boundary. The distinct
creation/fbv6 package remains a separate check limit. No optional A/B, second
diagnostic, runtime build, VM/check launch or source mutation follows from this
design finding.

## Ownership, acceptance and checks

| Owner window | Concrete deliverable |
| --- | --- |
| P3 / implementer1 | new `piruntime/callbacks.go`, worker framing/duplex attachment, `pi-runtime/src/host-bridge.mjs`, `lineage.mjs`, `tool-policy.mjs`; targeted `worker.go`, `protocol.mjs`, `session.mjs` and supervisor integration, with tests |
| P5 / implementer3 | `pihosttools` domain adapter, reporting/communication/utility factories and existing-store bindings; forward native toolCallID and AbortSignal rather than discarding them |
| P6 / implementer4 | question/plan factory signal forwarding; store/projection/service adapters, ordinary answer/plan mapping and UI snapshots under existing ownership |
| P2 / implementer2 | small portal startup/host handler composition and central routes; retained-state compatibility guard registration, no competing central edit |
| P7 | package approved modules/contract metadata only after matching implementations |

Exact source allocation and any change to existing owner windows need lead release;
this table assigns no competing edit window. Preserve Codex protocols/public APIs.
No C changes are needed for B1/B2; P6 card extraction keeps its separate C transfer.

Quick fake fixtures, owners run in D's Nix environment: wrong subject/generation/
original input/tool anchor; duplicate/changed args; unknown tool; oversized frames;
callback during Send; cancellation/abort without mutex deadlock; portal disconnect
before/after domain commit and lost result; duplicate domain receipt without resend;
reconnect same identity; multiple native tool IDs in one assistant; utility-only
monitor permissions; callback/tool drain accounting. These need no model or login.

Pinned SDK/no-model fixture: create a disposable history with public append APIs,
reopen existing file, prove exact tool-call anchor and stable selection token through
ordinary append, compaction fixture and restart; reject branch/reset/fork/content
replacement/missing file. Instantiate the exact shipped policy/resource factories
with fake provider transport; inspect active/callable/registered tools in both modes,
exercise direct and nested disallowed tool attempts, late MCP registration and
restored loadout, and verify no native dispatch under unknown policy. This validates
supported API wiring, not live provider/model behavior. Long/uncertain checks need
the existing fresh watcher procedure; do not run them as part of this design task.

Functional acceptance later: actual caller-bound question appears, answer is captured
while busy then once natively witnessed under ordinary admission; same IDs survive
lost ACK/restart; wrong branch refuses. Plan has the exact permitted tools, publishes
the exact displayed digest, changes to proved Default once, and admits its original
input once. Retained team/utility acceptance uses P5's independent codec/authority
and settlement proof. No callback/store capability becomes live before those gates.

## Fixed source pointers and limitations

Official Pi at the pin above:

- [ToolDefinition and execute context](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/extensions/types.ts#L600): execute at671; nested calls at404; tree events at867; before-agent policy hook at953/1517.
- [SDK tool selection](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/sdk.ts#L64): explicit tools/excludeTools/customTools and MCP exception.
- [Public session tree](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/session-manager.ts#L1422): getBranch1487, getEntries1538, branch1597; reload last-entry leaf1111; delayed new-file persistence1168.
- [Runtime tool policy](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L1557): public active/callable methods1573–1615, MCP/hidden callable exception1624–1657; message persistence1209–1234; public prompt expansion2175; tree navigation4285–4324.
- [Resource-loader inline factories](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/resource-loader.ts#L303): options313–340, inline loading1174; [read-only builtins](https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/tools/index.ts#L204).

Design/source inference only: no claim that current callbacks, lineage or Plan are
implemented or validated by live execution. Public APIs support the proposed limited
path; fake/pinned-SDK fixtures must establish the exact wiring before advertisement.
No ecosystem extension reuse, private credentials, native calls, lifecycle or deployment.
