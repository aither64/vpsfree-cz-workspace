# DESIGN-C: additive neutral conversation contract for P1

Owner architect2; 2026-11-12. Sufficient P1 brief accepted by architect0;
lead owns allocation. N was accepted before this package; current/env and retained
workspace-write roster verified. Only this file is owned. Actual C feature
worktree was clean at base/head `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce`.
Read C/workspace instructions and reused unchanged applicable procedures and
documentation skill. No application edits, builds or tests were executed here.

## Release and compatibility decision

P1 is independent of P0's SDK/RPC/launcher/Daybreak decisions. Implement the
neutral surface, legacy adapter and HTTP/browser compatibility using fixture
backends now. Actual Pi execution and supported-operation declarations wait
for P0; do not invent native admission or enable automation from a host outbox.
Architect0 records the accepted release in `design.md`; lead assigns execution.

Add a leaf package **`conversation/backend`**, importing only the standard
library. It owns independently declared presentation DTOs, operation groups
and errors. It imports neither `codex` nor parent `conversation`, and never D.
Keep public `codex/*`, existing `conversation.Client`, `Target`, `Options`,
`Resolver`, optional interfaces and upload/retry APIs unchanged. Do not replace
them with aliases to neutral types, add required methods, or change field types.

Add to parent `conversation`:

```go
type BackendResolver interface {
    ResolveBackend(context.Context, ResolveRequest) (BackendTarget, error)
}
type BackendResolverFunc func(context.Context, ResolveRequest) (BackendTarget, error)
// ResolveBackend invokes the function, like existing ResolverFunc.
func NewBackendHandler(BackendOptions) (*Handler, error)
```

`BackendOptions` has exactly the existing Options transport/configuration fields
with `Resolver BackendResolver` substituted. Keep `NewHandler(Options)` as a
compatibility constructor adapting its resolver into the same private neutral
dispatch path. Do not duplicate the HTTP server or change `/codex` default,
routes, browser storage namespace, JSON keys, entry kinds or existing callers.
D still depends on C; the repository name does not require a rename/split.

`BackendTarget` contains `Identity backend.Identity`, `Operations backend.Operations`,
`Capabilities Capabilities` (authorization), `MutationLock MutationLocker`,
`Release func()`, optional `ModelCatalog func(context.Context) ([]backend.Model,error)`,
`Attachments backend.AttachmentPreparer`, neutral `TransformTranscript` and
`PresentTranscript` callbacks, and the **existing parent** `Retry RetryProvider`
and `RetryActivity RetryActivityProvider`. These parent retry types already have
no Codex dependency; do not move or duplicate them into the leaf.

## Identity and operation groups

The following names/signatures are the P1 interface boundary. `id` below means
the trusted `Identity` value, not browser-selected native identity.

```go
// Server-only value, never marshalled as a browser response.
type Identity struct {
    BackendID      string // adapter kind selected by the host
    ScopeKey       string // stable host-owned conversation/member incarnation
    ConversationID string // native ID interpreted only by this adapter
    Directory      string // canonical trusted cwd
    Generation     string // current execution authority, not receipt identity
}
type HistoryCursor string
type Verifier interface { Verify(context.Context, Identity) error }
type Reader interface { Read(context.Context, Identity) (Transcript, error) }
type PageReader interface {
    ReadPage(context.Context, Identity, HistoryCursor) (TranscriptPage, error)
}
type PendingReader interface { Pending(context.Context, Identity) ([]Prompt, error) }
type Sender interface { Send(context.Context, Identity, SendRequest) (SendResult, error) }
type SendAcknowledger interface {
    Acknowledge(context.Context, Identity, []SendAcknowledgement) ([]string, error)
}
type QueueReader interface { ListQueue(context.Context, Identity) ([]QueueEntry, error) }
type QueueWriter interface {
    Queue(context.Context, Identity, QueueRequest) (QueueEntry, error)
    Delete(context.Context, Identity, string) error
    Start(context.Context, Identity, string) error
}
type QueueDeletionCompleter interface {
    DeleteWithCompletion(context.Context, Identity, string, func() error) error
    ReconcileDeletions(context.Context, Identity, func(string) error) error
}
type Interrupter interface { Interrupt(context.Context, Identity) error }
type SettingsClient interface {
    Models(context.Context, Identity) ([]Model, error)
    Modes(context.Context, Identity) ([]CollaborationMode, error)
    Update(context.Context, Identity, SettingsUpdate) (Settings, error)
}
type PromptResponder interface { Respond(context.Context, Identity, PromptResponse) error }
type LegacyPromptResponder interface {
    Decision(context.Context, Identity, string, string) error
    Answers(context.Context, Identity, string, map[string]map[string][]string) error
    Snooze(context.Context, Identity, string) error
}
type Watcher interface { Subscribe(context.Context, Identity) (<-chan struct{}, func(), error) }
type PendingRevisionProvider interface { PendingRevision(Identity) uint64 }
type ActivityProvider interface { ReadActivity(context.Context, Identity) (ActivitySnapshot, error) }
type AttachmentPreparer interface {
    Prepare(context.Context, string, string, string, []string) (string, error)
    QueueDeleted(context.Context, string) error
}
```

`Operations` is a struct with one explicitly nullable interface slot for each
group above: `Verify Verifier`, `Read Reader`, `Page PageReader`,
`Pending PendingReader`, `Send Sender`, `Acknowledge SendAcknowledger`,
`QueueRead QueueReader`, `QueueWrite QueueWriter`,
`QueueCompletion QueueDeletionCompleter`, `Interrupt Interrupter`,
`Settings SettingsClient`, `Respond PromptResponder`,
`LegacyRespond LegacyPromptResponder`, `Watch Watcher`,
`PendingRevision PendingRevisionProvider`, `Activity ActivityProvider`.
`Verify` is mandatory. Other slots describe support, not permission.
No wrapper may advertise an optional operation merely because its Go method
set always includes it. The legacy adapter populates page/bound response/
pending revision/completion slots only when the original client implements the
corresponding original optional interface. Preserve unbound-response fallback
only for legacy clients; a token-bearing request must never use it.

Validate trusted identity/canonical directory and run Verify under the existing
bounded request before operation dispatch. Preserve exact origin-before-resolve,
resolver release lifetime, mutation locking, payload limits and cancellation
ordering. D supplies its session/member/roster authority through ScopeKey and
resolver admission; C must not learn workspace schemas or create runtime owners.
Legacy adaptation derives its identity from the original trusted thread/cwd;
it must not change any native receipt namespace. ScopeKey and ConversationID
stay stable across Generation changes. Stale handles are revalidated by their
owning adapter; C never manufactures a fresh submission ID on reconnect.

## DTO and wire ownership

All leaf DTOs are real independent structs, with explicit projections in the
legacy adapter. No aliases/embeddings of `codex` types and no generic native-RPC
`any` envelope. Keep the existing browser presentation wire shape for P1.

| Leaf DTO | Exact source shape to preserve at C base |
| --- | --- |
| `Transcript`, `TranscriptEntry`, `TranscriptPage` | `codex/client.go:190–237`; preserve all exported fields/tags, nested communication, citations, optional questions/replies, attachments and activity. Page uses `*HistoryCursor` for `olderCursor`; same JSON string/null and existing 32-character opaque cursor validation |
| Nested presentation | Exported fields/tags of `attachments.go`, `async_questions.go`, `citations.go` (`CitationSource`, public `CitationSpan` fields), `transcript_activity.go` (`TranscriptActivity`, `ActivityLink`, `ActivityAgent`); do not copy native parsing algorithms or private citation refs |
| `Prompt`, `Question`, `Option`, `PromptResponse` | `client.go:155–188`, `prompt_response.go:10–17`; retain existing bounded Params/Item presentation maps because legacy browser consumes them, but add no native dispatch through them. Typed questions/decisions/token/authority fields remain canonical |
| `QueueEntry`, `SendReceipt`, `SendAcknowledgement` | `client.go:612–618,239–244,456–459`; exact browser IDs/digest fields and omission semantics |
| `Model`, `ReasoningEffortOption`, `CollaborationMode`, `SettingsUpdate` | `client.go:677–691,557–560,516–520`; model names and efforts remain strings validated against the trusted catalog, no hard-coded Codex model set |
| `Settings` | Existing returned `ThreadSettings` JSON projection, including `modelProvider`, `projectId` and independently typed policy/MCP presentation fields if present. These remain output metadata; request input is only SettingsUpdate, never executable policy |
| `ActivitySnapshot`, `ActivityBlockingRequest` | All exported fields/tags of `codex/activity.go:16–57`, including coverage/approximation and null/omission semantics; do not invent complete metrics for another backend |

`Transcript.ThreadID` remains the compatibility wire spelling for an opaque
conversation ID; it grants no access and is not parsed as a Codex UUID. Preserve
the existing page/response identity checks against the resolved conversation.
Native IDs/order remain adapter-owned provenance, not a new storage/export
standard. Original history and native receipts remain untouched.

## Send outcomes and error compatibility

```go
type SendRequest struct {
    Message string
    ClientUserMessageID string
    ActionContext string // host-only; current browser supplies none
    Retry bool           // same original ID/payload, never a fresh attempt
}
type QueueRequest struct { Message, ClientUserMessageID string }
type SendOutcome string
const (
    Accepted SendOutcome = "accepted"
    NotSubmitted SendOutcome = "not_submitted"
    Unknown SendOutcome = "unknown"
)
type SendResult struct {
    Outcome SendOutcome
    Receipt SendReceipt
    Retryable bool // meaningful only for positively proved NotSubmitted
}
```

Attachments are frozen/prepared before Send/Queue as today; preserve canonical
message text and digest across all presentation. The adapter owns durable
intent, acceptance proof and reconciliation. Generation is never a new receipt
key. `Accepted` proves admission, not finished tools; `NotSubmitted` requires
positive pre-acceptance proof; `Unknown` holds the original identity. An error
with no known disposition must not be converted to NotSubmitted.
An empty or unrecognized SendOutcome must never produce success or positive
NotSubmitted; return a generic failure without granting resend permission.

For the legacy adapter, Retry runs original `Client.SendAttempted` before
original `Client.Send`, with the same arguments/order. **Its boolean is not an
acceptance result:** true can identify a prepared receipt; false does not prove
no prior effect. Preserve its errors, then let original Send perform native
reconciliation. Do not add a new outcome-lookup method to old Client or infer a
result from its history. Pi/P0 may later implement lookup internally; P1 does
not require an unproved receipt API.

Leaf errors: `CursorError{Code string}`, `PromptError{Code string, NotSent bool,
Message string, Err error}` and a neutral legacy-service-error wrapper retaining
an internal cause for logging/`errors.Is/As`. Use explicit adapter projections
with `errors.As`; never match error strings. Original Codex errors remain
reachable through Unwrap where wrapped. Send's typed original not-sent/unknown
errors map to SendResult outcomes; unclassified legacy errors retain the old
generic 503 response, not a newly asserted delivery fact.

Preserve existing HTTP status/body exactly on the old constructor: Accepted
202 with the existing receipt; NotSubmitted 503 `message_not_sent`, `notSent:true`
and original Retryable; Unknown 409 `message_delivery_unknown`, `notSent:false`.
Cursor invalid is 400, expired/reset 409; retain bounded current messages and
codes. Prompt changed is 409, invalid response 400, other prompt errors 503,
with exact Code/NotSent/message behavior. Bound-token absence still returns
reload-required and never falls back. Internal errors/paths/cursors/secrets are
not exposed. Keep browser retry scheduling limited to positively unsent,
retryable attempts; Unknown is not automatically resent.

## Preserve original native presentation objects

The legacy adapter reads the original `codex.Transcript`/page and runs
**TransformTranscript → original AttachmentProvider.ObserveTranscript →
PresentTranscript on that same native object, then projects once to neutral**.
Do not perform codex→neutral→codex roundtrips before callbacks: CitationSpan
contains private native refs, and callbacks may depend on native metadata.
Check native page identity/entry bound before hooks as currently required;
attachment failure prevents PresentTranscript. Neutral target callbacks are
nil for this adapter, preventing duplicate execution.

Likewise run native ObserveQueue before projecting list/new queue entries;
preserve attachment-only prompt preparation and QueueDeleted completion ordering.
Neutral backends may supply their own typed Transform/Present callbacks; any
native/storage decoration belongs in their Reader/QueueReader implementation.
AttachmentPreparer intentionally has only Prepare/QueueDeleted, so no fake
neutral-to-native observation path is needed. Existing public UploadStore,
Upload/UploadTarget and NewUploadHandler remain unchanged and outside this
handler adaptation; no new upload framework is released by P1.

## Route coverage, support and files

Preserve every existing operation: thread/page→Page; thread→Read;
pending→Pending; activity→Activity; models/modes/settings→Settings (trusted
ModelCatalog overrides model listing/validation); message→Send;
message-ack→Acknowledge; queue reads/writes/start/delete→queue slots;
attachment-aware deletion/reconcile→QueueCompletion; interrupt→Interrupt;
respond→Respond or valid legacy fallback; events→Watch plus optional
PendingRevision. Parent retry/retry-activity routes keep their existing providers.

Capabilities remain authorization grants. Check permission/method before
invoking a supported operation. New neutral targets with absent operation
support refuse, never succeed as a no-op. Preserve legacy optional absence:
page 501, activity/retry provider absence 404, attachment deletion/reconcile
without completion 503, and pending-revision advertisement only with pending
authority. No new public capabilities endpoint is required; D configures the
limited pilot UI from the same trusted operation/support selection. Keep event
invalidation/heartbeat/reconnect behavior; do not turn it into native event replay.

Implementer0 owns C P1 edits: new `conversation/backend/{types,operations,errors}.go`,
parent `backend.go`, `backend_codex.go`, targeted private handler/route helpers,
and tests/docs for this API. Exact file splitting is routine implementation;
semantics above are settled. Retain public definitions even if moved to a
compatibility file. Generic dispatch imports leaf only; Codex imports stay in
legacy compatibility/projection files and unchanged legacy upload definitions.
No `codex/` native algorithms, protocol corpus, ledger schema, repository rename,
D pins, or application integration changes belong to P1. P6's later C edits
follow P1's interface/commit window; D pin ownership remains the plan's P7.

## Acceptance and remaining dependencies

Quick verification in C's declared Nix environment: existing Go conversation
and codex tests plus compile of example/external legacy callers; existing
conversation/sync/questions/delivery-retry browser contracts. Add meaningful
neutral fake-backend tests for route parity, denied versus unsupported support,
wrong identity, generation-independent retry IDs, bound-response fallback,
optional-slot absence, callbacks on native objects and private-metadata
preservation. Keep TestTranscriptPresentationOrder,
TestTranscriptPresentationPreservesCitationIdentity, send delivery, cursor,
queue deletion and pending-revision regressions passing. Test exported DTO JSON
equivalence, nested fields and nil-versus-empty behavior against representative
actual native projections; no reflection/JSON roundtrip as production adapter.

No native schema/state/history migration exists in this package. No long/live
checks run for this design; implementation uses ordinary quick-check, review
and monitor rules. P0 blocks only concrete Pi workers/admission/support;
P2 owns session binding/version fences; P6 owns new question semantics. None
blocks this P1 compatibility implementation. New operations beyond the existing
HTTP/browser surface require a separate sufficient brief, not speculative stubs.

Sources inspected: C base `conversation/{handler,uploads,retry,retry_activity}.go`,
native DTO files named above, `presentation_test.go`, send/cursor/prompt/events
tests, and browser conversation/sync/delivery-retry modules. No broader source
inventory, credentials, lifecycle or application mutation. This planning brief
does not trigger automatic final review.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## DESIGN-D / P2: durable binding and runtime authority

Architect2, 2026-11-12; DESIGN-C completed and accepted before this allocation.
D source base/head inspected: `6587c4c1cedabee95bcc52f4667e7d33e3a82859`.
Implementer2 owns P2; architect0 has accepted the independent boundary and
recorded it in `design.md`; lead releases execution. **Release the types, strict readers, pure validation and
resolver-selection fixtures independently of P0/H0. Creation, writes and live
dispatch remain held at the concrete fence gate below.** No new creation method
may report support or success until its real implementation satisfies that gate.

### Durable and live records

Use existing trusted `UserStateRoot`, canonical workspace and authority-directory
configuration. These are host inputs, never browser/model paths.

| Record | Exact proposed path and contract |
| --- | --- |
| Canonical Pi binding | `<UserStateRoot>/session-backends/<lowercase sha256(canonical workspace UTF-8)>/<slug>.json`; same workspace hashing as `session.RecoveryStore`/`userstate.WorkspaceDirectory`. New **binding schema 1**, explicitly `backend:"pi"`, `backend_contract:1`. This durable record survives portal/supervisor restart and loss of runtime files. |
| Pi live authority projection | Existing `<AuthorityDir>/<slug>.json`, new **authority schema 2**, explicitly Pi. This is derived execution evidence, never the durable backend selector. Keep `<slug>.lock` and `<slug>.creation.lock` at their existing paths. |
| Existing Codex | Existing schema-1 runtime authority, manifest, recovery, creation receipts and roster remain byte-for-byte unchanged. Validate by their existing readers, then normalize backend=`codex` in memory only. Do not add Pi keys to schema 1. |

Pi binding schema 1 has exactly these fields (snake_case):

```text
schema: 1
backend: "pi"
backend_contract: 1
workspace: canonical absolute workspace
slug: existing valid session slug
session_incarnation: random 64-character lowercase hex, retained across restarts
creation_receipt_id: exact owning creation identity, nonempty bounded string
revision: positive uint64, incremented by each authorized binding update
state: "creating" | "ready"
conversations: nonempty array of {
  address: "lead" | existing validated retained member address
  incarnation: random 64-character lowercase hex
  state: "creating" | "ready"
  native_id: nonempty bounded native Pi session ID, required only when ready
}
```

There is exactly one `lead`; addresses are unique. A ready binding requires a
ready lead; creating members are never dispatchable. The `native_id` may be
absent or valid/nonempty while creating; null or empty is
always invalid. A present value does not change that member's creating state.
All present native IDs must be unique, including creating members. Native
IDs are opaque, not paths or Codex UUIDs. The adapter proves their association
with its owned history before they grant any operation. IDs/strings are bounded
at 4096 UTF-8 bytes; the complete file is bounded at 64 KiB. Require integers,
exact required keys, no nulls/duplicate keys/unknown keys/trailing JSON, owner
UID regular mode-0600 files in private mode-0700 directories, matching workspace
and slug. Reject unsupported schema/backend/contract. Do not create directories,
repair records, mint identities or refresh timestamps during a read.

Pi authority schema 2 has exactly `schema`, `backend`, `backend_contract`,
`workspace`, `slug`, `session_incarnation`, `binding_revision`, `generation`,
`state`. Values are `2`, `"pi"`, `1`, the matching durable tuple/revision, a
nonempty 64-character lowercase hex execution generation, and `"starting"` or
`"ready"`. Apply the same private file/strict JSON bounds. No fake Codex/tmux
fields. P3 owns transport/socket/process/namespace proof separately; a ready
projection alone is not execution permission. Generation changes on supervisor
replacement; it does not change session/member/native identity or receipt keys.

Membership/settings permissions remain the host roster's responsibility. This
binding maps identities and never grants role access. P5 must match its retained
member/settings incarnation against this mapping under existing operation locks;
it cannot reuse the Codex-only roster writer for Pi. Changing a member's native
conversation changes its incarnation and invalidates old handles. Restarting the
same conversation preserves it. There is no backend-changing update method.

### Minimal types and read API

New `portal/internal/agentbackend/identity.go` is a stdlib-only domain leaf;
it imports neither `session`, `teamruntime`, `workspacecodex` nor Pi transport.
Native adapters may consume it. Keep existing exported Codex APIs intact.

```go
type Kind string // only Codex="codex" and Pi="pi"
type SessionRef struct { Workspace, Slug, Incarnation string }
type ConversationRef struct {
    Session SessionRef
    Backend Kind
    Member, Incarnation, NativeID string
}
type ExecutionHandle struct {
    Conversation ConversationRef
    Generation string
}
// In session/backend_binding.go; typed records mirror the exact schemas above.
type BackendBindingStore struct { Root, Workspace string }
func (s BackendBindingStore) Load(slug string) (BackendBinding, error)
func (b BackendBinding) Validate(workspace, slug string) error
func (b BackendBinding) Resolve(member string) (agentbackend.ConversationRef, error)
func LoadPiRuntimeAuthority(directory, slug, workspace string) (PiRuntimeAuthority, error)
func (a PiRuntimeAuthority) ValidateBinding(b BackendBinding) error
```

Return typed distinctions `ErrNotBound`, `ErrUnsupportedBinding`,
`ErrBindingConflict`, `ErrConversationNotReady`, `ErrStaleExecution` (wrapped
causes remain available); malformed/private-file failures are errors, not absence.
The shared sentinels live in `agentbackend`; `session` may alias them.
Unsupported schema/kind/contract maps to Unsupported; valid mixed evidence,
orphan Pi projection and tuple/revision mismatch map to Conflict. Comparing a
supplied handle's generation with current matching authority yields
StaleExecution on mismatch. `ValidateBinding` compares durable tuple/revision,
not generation; handle validation also checks ready states and exact member,
conversation incarnation and native ID. Use `errors.Is`, never text matching.
The load API never returns a successful
empty binding. New `session/backend_selection.go` owns the small selection
function over **already validated** legacy evidence and typed Pi records. It
does not become a second parser for legacy manifests/receipts. Keep any native
`RuntimeAuthority` compatibility member on this parent selection, not the leaf.

Legacy conversation incarnations use existing validated root/member/native
identity evidence. If an opaque ScopeKey is needed, hash that canonical tuple
in memory; this is a projection, not newly invented historical provenance. Do
not use tmux identity/socket epoch as a fresh receipt namespace. Terminal-only
schema-1 authority may identify the legacy backend without proving a runnable
conversation; preserve the existing refusal/recovery path.

| Observed validated state | Selection/result |
| --- | --- |
| No Pi binding; known valid legacy authority/retained Codex evidence | Codex through unchanged legacy validation, including its existing cold/archive recovery requirements. Absence by itself is never the proof. |
| No binding, no authority and no retained backend evidence | `ErrNotBound`; no auto-adoption or creation. |
| Pi binding; no live authority | Pi remains selected; inactive/held. Proven history may be read through its adapter; no execution claim or Codex fallback. |
| Pi binding plus matching schema-2 projection | Pi selected; dispatch additionally requires matching current generation, member/roster authorization, lifecycle/admission and P3 runtime proof. |
| Schema-2 projection without durable binding; Pi plus Codex evidence; tuple/revision/backend mismatch | `ErrBindingConflict`; no repair, downgrade or fallback. |
| Unknown version/backend, malformed record, missing ready native ID | Refuse; never reinterpret as legacy. |

Portal selection uses opaque session/member route IDs. New neutral resolver
composition belongs in `web/backend_resolver.go`; keep the old Codex resolver
path unchanged until its adaptation is exercised. Map the selected trusted
tuple into C's `backend.Identity`, not the reverse. `ScopeKey` identifies stable
session/member/conversation incarnations; `Generation` is current execution
proof. Backend support, user authorization and execution admission are separate.
No registered Pi sender/create/interrupt capability exists just because a reader
or stub exists. P0/H0 failure must not disable legacy operations.

Submission identity is the stable tuple `(backend, workspace, slug,
session incarnation, member, conversation incarnation, native ID, action,
client input ID, canonical payload/options digest)`. Execution generation is
attempt evidence only. Unknown keeps that exact identity held; no replacement
UUID, optimistic retry or inferred acceptance. This defines comparison inputs,
not a second submission ledger or a changed Codex receipt format.

### Exact write-release gate and ownership

Source establishes **reader refusal, not complete writer fencing**: old Go
`LoadRuntimeAuthority` rejects unknown fields/schema; Ruby
`validate_session_authority!` does likewise. However old
`write_session_authority` builds schema 1 and renames it over the path without
validating the previous record. `workspace-host` currently scans only records
containing `tmux_identity` for its authority policy fence. Its live authority
directory is runtime storage. Therefore neither a durable sidecar nor schema 2
alone establishes downgrade/reboot safety.

Before creation/writes release, implementer2 must prove these concrete changes
with disposable Go/Ruby fixtures and report the exact modified call sites:

1. Add `sessionBackendBindingSchema:1`, `sessionBackendBindingPolicy:1` and
   `runtimeAuthoritySchema:2` to the shared runtime contract, retaining existing
   Codex/identity policy fields. Reader support for authority schemas 1 and 2 is
   explicit. New package transition/activation preflight scans **durable**
   session-backends state even when runtime authority is absent, and refuses
   candidate packages lacking exact supported binding policy/schema. Include
   existing switch/activation/compensation entry points; a target's extra JSON
   key is not evidence that its old code enforces the policy.
2. Preserve transition SH → creation lock (new destination only) → runtime EX
   → team operation/short roster locks. Revalidate current package generation
   after waiting and reload binding under the runtime lock before any authority
   overwrite/deletion, native create or recovery action. Existing Codex writers
   explicitly refuse a Pi binding; Pi writers refuse any legacy evidence or a
   different incarnation. No blind overwrite. Ordinary reads do not acquire
   creation locks or publish runtime state.
3. Exercise old installed/waiting wrapper against a changed host profile/token,
   new wrapper against existing Pi state, old reader against schema 2, and
   selection of an old candidate with durable Pi but no runtime files. Existing
   `validate_host_generation!` checks profile realpath/token after transition
   lock; preserve that check and the portal's current-host checks. Direct
   historical private helpers without installed bindings are outside the
   supported operator flow, not an excuse to omit ordinary entry-point fences.
4. Persist the explicit Pi request/backend and creation identity before native
   creation in a separately versioned creation receipt; legacy receipt schemas
   1–3 remain untouched. Exact new creation-receipt/journal fields and publish
   order are a **remaining creation-only gate**, not part of this reader release.
   Reserve and publish the durable binding under the existing creation/runtime
   locks; retry the same identity. No crash gap may become fresh Codex creation.
5. Legacy archive/delete/revive/resume/sync/team/recovery dispatch must either
   use the Pi-aware owning implementation or refuse Pi before any mutation;
   none may run the old Codex path on missing runtime files. Keep known Codex
   paths operational. Pi automatic recovery/teams remain disabled until their
   separate native and host proofs exist. This gate adds no migration/archive
   converter and authorizes no live lifecycle action.

Implementer2 owns new `agentbackend/identity.go`,
`session/{backend_binding,backend_selection,backend_authority}.go`, focused
fixtures and the reserved central P2 window. Existing
`session/{authority,recovery,contract}.go`, `runtime-contract.json`,
`web/{server,creation,creation_store}.go`, `cmd/workspace-portal/main.go` and
`libexec/dev-session` require a later named central window before edits; none
is released by this reader subset. Future `libexec/workspace-host` edits retain
the existing P3/H0 ownership and require explicit lead sequencing with P2 fence
work; this brief does not reassign that file or the host module. P3/P5 coordinate
central integration through implementer2 without overlapping edits. No dependency
pins or C changes belong here.

### Acceptance and source pointers

First release checks: valid schema-1 fixtures preserve exact legacy selection
and bytes; strict Pi binding/projection fixtures cover wrong workspace/slug,
unknown schema/backend, duplicate/null/missing fields, ready/creating members,
revision/generation mismatch, missing durable/live records and conflicting
legacy evidence. Repeated reads must not create files or change bytes. Same
receipt identity across restart and changed member incarnation rejection are
pure tests; they do not claim native acceptance. Reader failure must not invoke
any legacy writer or Pi transport. Ownership, limits and no-browser-native-input
checks use the repository's trusted-local-operator boundary.

Implementer quick checks use D's Nix environment and focused
`go test -mod=readonly ./internal/session ./internal/agentbackend` from `portal/`,
then the affected resolver fixtures when wired. Ruby writer/transition checks
and installed lifecycle checks are later fence acceptance, under normal monitor
rules when long/uncertain. No tests/builds/native actions were run for this design.

Fixed D source pointers: `portal/internal/session/authority.go:159–250`
(strict legacy authority), `recovery.go:44–115` (durable workspace-scoped state),
`runtime-contract.json`/`contract.go:58–101` (shared contract),
`teamruntime/runtime.go:625–679` (private roster/operation locks),
`web/server.go:3875–3990` (resolver lock/revalidation),
`web/creation_store.go:411–430` (legacy receipt schemas),
`libexec/dev-session:3297–3416,9900–9913,10022–10050`
(reader/writer/generation checks),
`libexec/workspace-host:3093–3101,3288–3332,3825–3833`
(incomplete current authority scan, target check and runtime path).
No native state/history/schema migration is proposed; new formats are Pi-only.

### P2 continuation: independently releasable guards

2026-11-12 continuation; reader subset accepted at
`063c4a4b151aff3d8d8d16712c688e4a9fa9ac9c`. Guard source inspected at D
`23b35d5368a27bd189ef7b895dbbfbde4dc0d331`; existing central functions below
retain the inspected base behavior. This section supersedes the earlier
unspecified writer gate with concrete guard work. **P2-G can implement guards
and synthetic compatibility fixtures now, independently of native Pi/H0.** It
does not create Pi records, enable Pi execution or release creation/UI wiring.

**Conservative P2-G publication:** advertise only the implemented
`sessionBackendBindingSchema:1`, `sessionBackendBindingPolicy:1` and
`runtimeAuthoritySchema:2`. This policy includes refusal of unimplemented Pi
creation formats. Until P2-C is implemented and checked, every schema-4 receipt
or journal refuses with explicit unavailable validation; a Pi binding with
neither retained receipt nor journal is a conflict. Accordingly P2-G alone
permits no Pi-bearing package transition, even with matching target metadata.
Positive metadata compatibility is tested separately from transition success.
Do not publish `piCreationSchema:4` merely because its design is accepted; it
requires the complete implemented and verified P2-C format/guard contract.

**Durable package preflight.** Add one narrow
`require_compatible_session_backends!(package, entries = registry.entries)`
beside the existing host compatibility checks. It reads the canonical
`session-backends/<workspace hash>/<slug>.json` namespace with the P2 strict
schema and rejects unsupported/malformed records. Also inspect schema-4 Pi
receipts in the existing `private_portal_creation_directory(entry)` and their
existing creation journals: acceptance can precede durable binding publication.
Missing directories mean no such state, never permission to invent it. No scan
of native history, auth, peer sessions or an additional registry is required.
This describes application behavior over registered state, not permission for
agents to inspect other sessions during this task.

For complete P2-C support, target runtime-contract metadata must exactly support
`sessionBackendBindingSchema:1`, `sessionBackendBindingPolicy:1`,
`runtimeAuthoritySchema:2`, `piCreationSchema:4`. Retain all existing policy
checks and authority schema-1 support. `piCreationSchema:4` covers the complete
Pi receipt/journal/completion/tracking shapes below, not merely their version
integer. A malformed/unknown Pi record refuses
before changing profile, roots, units, Codex, tmux or tracking. Add the check to
these actual existing entry points, without a separate transition engine:

| Existing host entry point | Guard placement |
| --- | --- |
| `register` (existing profile), `prepare_profile` | Alongside `require_compatible_runtime_authorities!`, before registration effects/selection; preparation is not final proof. |
| `validate_candidate_preparation!`, used by `activate_candidate` | Repeat under transition exclusion before drain/quiesce/selection, including reacquisition after maintenance waits. |
| `activate` | Repeat against `package_root` before `effects_started`, links or service changes; candidate self-activation cannot bypass it. |
| `recover_archive` candidate preflight | Preserve its existing old-journal recovery purpose; add compatibility check at the existing candidate check group, never reinterpret a Pi session as an eligible Codex archive. |
| `complete_candidate_activation`, `restore_quiesced_sessions`, `reraise_after_terminal_restoration` | Revalidate the selected/restoration package against durable state before invoking session helpers. Do not make a rejected Pi binding disappear to make restoration succeed. |

Keep `with_current_generation_lock`/`with_candidate_generation_lock` profile
token checks and CLI `validate_host_generation!` after transition acquisition.
Portal mutation/creation retains `requireCurrentHostProfile` after waits.
Before profile selection, existing compensation may restore the still-selected
predecessor **only if compatible**. After actual profile selection, retain the
forward package, pending evidence and existing recovery error; no rollback,
deletion of Pi state or compensating native create. Public rollback remains
refused. An incompatible restoration fails visibly while retaining evidence.

**The unchanged old-candidate fence is concrete.** At the fixed base,
`require_no_unfinished_lifecycle_operations!` reads every existing
`*.creation.json` through `read_private_creation_journal!`, which rejects schema
4 even when state is ready. Its `unfinished_portal_managed_creations` rejects
receipt schemas outside 1–3 before checking ready/conflict. This covers old
`--from-candidate` as well as old ordinary activation: a new sidecar alone would
not. P2-C must publish its ordinary schema-4 receipt before any Pi effect and
retain its schema-4 creation journal for the lifetime of the Pi binding. Receipt
cache retirement may occur only after that journal is durable and checked.
No new marker format is needed. Missing both retained fences with Pi state is
a conflict requiring repair, not normal operation. Test the actual predecessor
readers/entry points; do not claim that new metadata can patch old binaries.

**Legacy writer/lifecycle refusal.** Add a narrow validated
`require_codex_session_backend!(slug)` at the old mutating admission boundary
and as a final check inside `write_session_authority` and
`delete_session_authority`. It refuses a Pi durable binding, schema-4 receipt or
journal, and unsupported/malformed backend evidence; known legacy absence keeps
existing validation. Recheck under the runtime lock, not only before waiting.
`with_slug_lock` currently loads authority before its lock; preserve its waiting
behavior but move/repeat the decisive backend/authority proof inside the lock.
Do not force schema-2 live authority through the legacy schema-1 loader.

Guard `start` (including existing-destination retries), `resume`, `sync`, fork
source/destination, native reconciliation and archive/delete/revive before
their first native, worktree/tracking, journal or recovery mutation. The latter
use `archive_with_access`, `delete_with_access`, `revive_with_access`; insertion
must precede lifecycle capacity/journal publication and cleanup discovery with
effects. Automatic archive and boot recovery skip/refuse Pi explicitly instead
of invoking Codex recovery. `publish_failed_creation_delete_authority!`,
`ensure_retirement_identity!` and `reconcile_native_client!` retain final
Codex-only guards. Go web routes retain the existing resolver on Codex;
schema-4/Pi branches refuse unsupported mutations before using `Config.Codex`,
`RecoveryStore`, team or creation workers. No unconditional success stub.

Lock order stays selected-package transition SH → existing provider/creation
admission → creation lock when needed → runtime EX → team operation/short roster
locks. Ordinary conversation dispatch keeps its existing SH/EX distinctions.
No new global lock; no lock upgrades or acquisition of creation locks while
holding a lower runtime/team lock. A final writer check must assert/reuse its
caller's held ownership, not recursively lock it.

**P2-G file window and acceptance.** Implementer2 owns the narrow guard logic,
`runtime-contract.json`/Go decoding additions, CLI guard calls and focused tests
only after lead release. A small shared Ruby backend validator may be factored
for the two existing callers; no catch-all format guard framework. All
`workspace-host` changes remain coordinated with existing P3/H0 ownership and
require lead's explicit edit window; this does not reassign the file.
Unrelated pins/build inputs remain untouched.

Extend existing `test/workspace_host/profile_transition_test.rb` and
`live_switch_test.rb` cases for candidate self-activation, failed forward
activation, preselection compensation, stale candidate and interleaved
completion; `test/dev_session/{lifecycle_commands,tracking,preparation_reservation,
ordinary_readiness,tmux_identity}_test.rb` cover writer/CLI refusal. Add focused
Pi fixtures for: durable binding with no runtime files; schema-4 receipt before
binding; ready schema-4 journal after receipt cache retirement; unchanged old
candidate refusal; compatible current package; unsupported contracts; malformed
state; generation changed while waiting; legacy writer attempts with byte-for-
byte unchanged Pi files and zero fake native/tracking/service effects. Keep
known Codex regression cases passing. Include `TestBackendSelectionRequiresPositiveEvidenceAndNeverFallsBack`
and resolver no-Codex-call fixtures. No live accounts/runtime probes are needed.

Guard source anchors at D base: `workspace-host:626–855,1211–1268,2568–2696,
2764–2808,3333–3368,3574–3603`; `dev-session:3297–3416,4063–4085,
4150–4197,8444–8483,9900–9913,10022–10050`; web creation
`installCreationLocked`, `initializeCreation`, `proveCreation` and the accepted
P2 reader package. New source is implementation work; no checks were run by
the designer.

### P2-C: explicit Pi creation, publication and forward recovery

P2-G and the P2-C format/publication contract are technically accepted by
architect0. P2-C releases format, writer and fake-adapter work after lead
acceptance; **live/full Pi creation still
requires the released P3 create/history/input adapter and H0 execution proof**.
Schema 4 alone never establishes compatibility: validate its complete shape and
cross-record identity. Keep schemas 1–3 and the existing Codex call path unchanged.

Use the existing accepted-request/receipt machinery and namespaces:
`portal/<existing workspace identifier>/creations/<slug>.json`, existing
`<slug>.<receiptId>.complete.json` and its `.request` companion, and
`<workspace>/worktrees/.locks/<slug>.creation.json`. No second request registry.
Preserve existing preparation request UUID, 64-hex receiptId, deletion-history
epoch, exact-owner retry, sensitivity and tracking ownership. Any preparation
that supplies a destination receipt must hand off the same receiptId and explicit
backend; its absence/default retains Codex. Never reinterpret an old accepted
request as Pi. Initially Pi accepts only `kind:"new"`; Pi fork/plan-derived
creation stays unsupported until its separate semantics are released.

**Exact new receipt shape.** Schema-4 outer keys are the existing schema-3
`schema,workspace,request,receiptId,deletionHistorySha256,attempt,state,phase,
startedAt,updatedAt,validated,goal,model,effort,directTeam`, optional `error`, and
required `pi`. No agentTeamBinding keys. `request` allows only `kind,slug,goal,
backend`, optional `sensitive,model,effort,provider,team,catalogDigest,
browserNotificationsEnabled`; backend is exactly `pi`, kind exactly `new`.
`directTeam` retains the existing resolved host preset shape/settings, without
changing any legacy roster. Explicit selection or the installed default is
resolved before receipt publication; do not silently drop selected members.
Pi provider/catalog validation supplies the resolved `goal,model,effort`,
`pi.provider` and the complete `pi.selection` below before publication, without
login/model requests. Thus schema-4
`validated` is true; the immutable settings/normalized goal are already frozen.
Authorization/account availability is still separately checked at execution.

The required `pi` object has exactly:

```text
backendContract: 1
sessionIncarnation: 64 lowercase hex
conversations: [{address: "lead" or selected member, incarnation: 64 lowercase hex}]
provider: resolved bounded provider identifier, never credentials
initialInputId: existing lowercase submission UUID format
selection: immutable provider selection snapshot defined below
```

The array has exactly the lead and selected preset members, unique addresses and
incarnations. All these values are minted/frozen once before the first receipt
save, reused on retry, and map directly to the schema-1 durable Pi binding.
Use existing receipt bounds, duplicate/null/unknown-key checks and private atomic
write/fsync rules. Receipt `state` remains `running|paused|failed|ready|conflict`;
`attempt` is UI/executor attempt metadata, never a new native/input identity.
Use existing phase/error reporting; native uncertainty is a held condition, not
a separate retry queue or implicit cancellation state.

**Provider selection freeze (P2/P4 clarification, 2026-11-12).** The above
`selection` is required; the earlier five-field Pi object is incomplete and must
not be accepted or written. No live schema-4 creation was released against that
incomplete shape. Keep schema 4 and reject the incomplete shape; do not add a
compatibility/defaulting path. This is part of the original creation receipt,
not another selection ledger. Its exact keys are:

```text
schema: 1
catalog_digest: 64 lowercase hex, P4 hash of exact packaged catalog JSON
policy: {
  session: {workspace, slug, incarnation},
  revision,
  default: {revision, selection: {chain, budget, fallback_on}},
  overrides: [{member: {address, incarnation}, value: {revision, selection}}]
}
members: [{
  address, incarnation,
  source: "session_default" | "member_override",
  policy_digest: 64 lowercase hex,
  settings: {
    provider, account_ref, model, thinking, policy_revision, revision
  }
}]
```

Every nested `selection` uses exactly `chain,budget,fallback_on`; chain is the
ordered nonempty array of P4 `Target` objects with exactly
`provider_id,account_ref,model_id,thinking`. Budget has exactly
`max_extra_attempts,max_hops`; categories are P4's validated failure-category
strings. Empty overrides/categories are explicit arrays, not null. The policy
wire keys match P4's schema-1 store, but P2 uses its own typed wire projection;
do not expose/import private `document` or `storedSession` types. Decode back to
public `piproviders.Policy`, retaining exact SessionRef/revisions/default/overrides.
No auth material, credential store paths/keys, provider endpoint or catalog account
objects enter this snapshot; `account_ref` is the existing nonsecret logical ID.

The initial policy/session/default and any override revisions are 1. `members`
contains exactly the reserved conversations in their same order, including lead;
override keys must name those exact address/incarnation pairs. For each, use
`piproviders.Resolve(exactCatalog, frozenPolicy, reservedMember, 1)` once before
publication. Freeze its Source, PolicyDigest and all EffectiveSettings fields:
`provider` is the resolved **native Pi provider ID**, `account_ref` the logical
account, `policy_revision` equals PolicyDigest and settings revision is 1.
Outer `pi.provider` equals lead settings.provider; existing lead model/effort and
retained directTeam choices must agree with the host's validated P4 projection.
Do not silently repair a mismatch or change a saved member's instructions/access.
These are desired immutable settings, not proof of native applied settings.

P4 alone owns policy digest bytes. Validation uses DecodeCatalog/ValidateCatalog,
ValidatePolicy and Resolve with the **exact same catalog digest**, then compares
the full frozen result, not just labels/digest. Do not copy private policyBytes,
invent another provider mapper or re-resolve latest defaults/policy/team on retry.
If that exact catalog is unavailable or the current trusted catalog differs,
creation holds; a current catalog is not permission to reinterpret an accepted
receipt. No full credential-bearing catalog snapshot is required. Preserve the
selected package/catalog availability under existing retention, or report that
specific resume dependency. Fresh account/model admission may refuse execution
but cannot change the frozen tuple. Initial root Send and later first-member
assignment consume these settings with the original input IDs/P3 receipt digest.

The full ordered fallback intent is already frozen by policy/default/overrides,
including budget/categories and catalog digest. **Executable fallback is absent
in this creation release.** P4 currently returns only nonexecuting PlanNext targets
and no native per-fallback settings builder; P3 terminal NotSubmitted never
redispatches. Do not shorten/re-resolve a chain (which changes its PolicyDigest),
claim candidate settings applied or activate a fallback from this snapshot.
Enabling fallback requires the separately accepted P4 native-target/settings API
and P3 attempt contract; that does not block the frozen primary creation path.

Copy this exact typed selection value to the existing companion/journal as
`provider_selection`, and completion evidence as `providerSelection`. Compare
full values at recovery/completion and retain it in the journal after receipt
cache retirement. No new snapshot digest recipe is necessary: P4 catalog and
per-member PolicyDigest remain authoritative and existing receipt identity plus
full equality fences these records. Keep existing record-size limits; refuse an
oversized selection before receipt publication rather than silently truncate it.
Focused fixtures: two accounts with same model, per-member override, changed
catalog/default on retry, wrong incarnation, edited budget/chain/category,
settings-policy digest disagreement, snapshot surviving receipt retirement,
incomplete five-field Pi shape refusal, and primary-only execution despite
retained fallback intent. P2 owns format/creation tests; P4 owns resolver truth.

**Exact immutable request companion and journal.** Both use schema 4 and the
following snake_case identity fields:
`schema,workspace,slug,backend,backend_contract,receipt_id,
deletion_history_sha256,session_incarnation,conversations,goal_sha256,
model,effort,provider,provider_selection,direct_team,initial_input_id,sensitive`.
Backend/contract are `pi`/1; `sensitive` is an explicit boolean; conversations
match the receipt's reserved address/incarnation pairs; goal_sha256 is the
existing normalized creation-goal digest. The companion contains only those
fields. The journal adds required `state` (`creating|ready`) and
`native_create_started` (boolean), optional `native_generation` and `native`.
When native_create_started is true, native_generation must be the recorded
64-hex P3 execution generation; otherwise both optional fields are absent.
`native`, when present, has exactly `native_id` and `history_ref`, nonempty
bounded strings returned by the owning adapter. history_ref is an opaque
adapter-owned locator, never a browser path. It must resolve within that
session/member's approved durable history root. A ready journal requires native
identity/history proof and the accepted initial-input receipt. No run_codex or
tmux fields; do not run this through `ready_creation_journal`'s legacy rewrite.

These journal/companion records contain no goal text, credentials, arbitrary
RPC payload or replicated message ledger. Compare their full frozen values with
the current receipt and completed-removal epoch before each resumed effect.
The initial input's native witness/outcome belongs only to P3's existing host
operation receipt, addressed by the frozen initialInputId and exact conversation
tuple. P2 never infers acceptance from a journal flag or creates another ledger.

**Publication and crash order, under the accepted locks:**

1. Under existing `withCreationMutation`/`installCreationLocked` ownership,
   recheck current package, destination freshness, preparation owner, deletion
   epoch and no conflicting legacy/Pi state. Persist/fsync the schema-4 receipt
   before acknowledging browser acceptance or starting an asynchronous worker.
   This is acceptance of a creation request, not acceptance of its native input.
   The old host's receipt parser now refuses package downgrade.
2. The same worker reacquires transition SH and validates current profile,
   then creation/runtime EX ownership. Require the still-current exact receipt;
   write the immutable `.request` companion, then schema-4 `creating` journal
   with native_create_started=false, using existing private atomic writers.
   Publish the durable Pi binding at revision 1 with the same session/member
   incarnations, every conversation creating and no native IDs. A crash between
   files resumes only this receipt; it cannot become fresh Codex creation.
3. Prepare ordinary owned tracking/resources through the existing creation
   helpers without calling Codex initialization. P3/H0 may establish the exact
   session boundary and a schema-2 starting projection; that projection does not
   authorize native calls. Before native create, durably set
   native_create_started=true and the exact generation in the journal. Invoke
   **only** the released create adapter with the frozen receipt/member identity.
   Record its returned native ID/history locator atomically. A failed or lost
   response after entering create remains Unknown unless that adapter positively
   reconciles the same create intent; never mint a replacement ID.
4. Initial input runs only on this exact newly-created worker/conversation under
   the same initialization owner, using the frozen initialInputId, goal and
   exact frozen lead selection/settings and host policy. This is not generic
   ready-session dispatch.
   P3 binds full immutable options and payload to its original operation receipt.
   Publish Accepted only after its supported persistent native witness; a
   timeout/exception/missing file alone is Unknown. In the currently released
   P3 contract, duplicate NotSubmitted returns the terminal negative receipt;
   it does not redispatch or change settings. Initial-input NotSubmitted stays
   held and visible. Refuse automatic and explicit redispatch until a separate
   attempt contract is accepted; do not mint a new initialInputId or repeat
   native creation to bypass the hold.
5. After persistent native identity/history proof, and Accepted initial input,
   publish the lead's native ID/ready state in the durable binding, incrementing
   revision. P3 proves the current generation and updates its matching live
   projection. Keep uncreated members creating/held; never claim their tools or
   automation ready. The portal may show the root session usable while stating
   those member states explicitly. Member initialization remains P5-owned.
6. Publish backend-aware tracking projection and schema-4 completion evidence,
   then mark the retained schema-4 journal ready, then save the portal receipt
   ready. Each step is repeatable from matching durable proof; no repeated native
   call is needed. A final-status save failure reconciles these same records.
   Keep the journal while the Pi binding exists. Receipt-cache retirement must
   first prove the matching ready journal/binding; no retained-fence gap.

Completion evidence uses schema 4 and exactly `schema,workspace,slug,backend,
backendContract,receiptId,sessionIncarnation,bindingRevision,conversations,
nativeId,initialInputId,initialSubmissionDigest,goalSha256,model,effort,provider,providerSelection,catalogDigest,teamDigest,
team,trackingDevice,trackingInode`. Conversations are the reserved identities,
not invented native members. The goal/options, native ID, initial receipt,
tracking inode/device and ready binding must all match when `proveCreation`
handles schema 4. Ready is root-session readiness, not proof that all members
have executed. Original schema-1–3 completion proof stays unchanged.

**Retained root input proof after cache retirement (technically accepted by
architect0 and recorded in design.md; lead retains source release).** The required completion field
`initialSubmissionDigest` is the exact lowercase 64-hex `SubmissionRef.Digest`
from the original positively Accepted root input, verified through P3 before
completion publication. It is an opaque reference into P3's existing receipt,
not another digest algorithm, input copy or ledger. This amends the initial
schema-4 source format while production adapter registration remains unreleased;
incomplete shape refuses rather than being inferred/backfilled. It does not
claim a migration of externally consumed state.

For Pi only, `retireCreation` removes the bounded mutable portal cache receipt
and its in-memory cache entry after proof. It **retains** the existing immutable
`.request` companion and `.complete.json` completion evidence, together with
the ready schema-4 creation journal, for the lifetime of the durable Pi binding.
Their paths remain the existing receipt-ID-qualified paths, with their current
private permissions/strict schemas; no new store or directory. Retained proof
files are not pending creation-cache entries. Receipt absence is acceptable only
for this completed retained proof when binding, companion, completion, journal,
creation ID and removal epoch all match. It cannot authorize a fresh/resumed
creating request. Keep original Codex retirement untouched. This is source
retention behavior, not permission for any lifecycle action or cleanup.

After cache retirement, reconstruct the full original root SubmissionRef from
the retained exact workspace/slug/session incarnation, reserved lead incarnation,
backend Pi, completion/journal native ID, `initialInputId`, fixed action `send`
and `initialSubmissionDigest`. Derive no part from the current default, native
latest leaf or a different receipt. Existing `Controller.Lookup` accepts that
full reference and observationally returns P3's original Input/Settings. Require
exact reference and Accepted phase, no refusal, `Input.ActionContext == "initial"`,
`Input.Retry == false`, `MessageDigest(Input.Message) == goalSha256`, exact frozen
lead settings, and `SubmissionDigest(ref, Input, Settings) == ref.Digest` using
P3's existing function. The accepted root initial text is the normalized receipt
goal itself; do not add a hidden prompt wrapper to bypass that equality.

Then apply the existing exact CreationVerifier/native history/witness checks
with the current authorized handle and retained journal historyRef. Lookup alone
does not prove persistent native acceptance or grant execution. This reuses the
original text already retained by P3 rather than copying it into another record.
It needs no new partial-ID lookup method, worker start, native send or current
provider-policy resolution. Missing receipts/history, Unknown/NotSubmitted,
digest/goal/options mismatch or unavailable observational proof holds admission
and retirement; never infer acceptance from the journal's ready flag.

Thus root receipt-cache retirement may occur while reserved members remain
creating, **once this retained-proof reader/writer path is implemented and
checked**. Until then hold Pi retirement as implementer2 proposed. Root/member
readiness and original completion revision semantics stay unchanged. Reuse the
accepted transition/runtime retirement ownership and strict package guards;
do not create a retention exception which old candidates can ignore.
Fixtures cover cache removal with member-creating followed by successful root
verification/member publication; unchanged retained proof bytes; missing/altered
digest, original input/settings/goal mismatch, partial proof-file loss, cold
observational refusal without native action, old-target refusal and unchanged
Codex cache retirement. An authorized later binding-retirement path owns the
proof files' eventual disposition; this clarification adds no such operation.

**Root completion versus later member revisions (technically accepted by
architect0; design.md records the release boundary).** Completion `bindingRevision` records the revision
at the original root-completion publication; it is immutable historical proof,
not the current execution version. Require equality with the locked current
binding when first writing that evidence. A later selected-member ready CAS may
advance the binding and its live projection without rewriting root completion,
the root journal, initial receipt or frozen provider selection.

For later `proveCreation`/receipt-cache retirement, permit
`completion.bindingRevision <= currentBinding.revision` only together with all
existing full creation proof, including exact workspace/slug/backend/contract,
session incarnation/creation receipt/removal epoch, frozen options and complete
provider selection, reserved conversation addresses/incarnations/order, exact
ready lead native identity/history and original Accepted initial-input witness,
tracking identity and the matching retained ready creation journal. The current
binding must independently validate and remain ready. A greater historical
revision, changed/extra/missing reserved identity, replaced native lead, missing
or contradictory journal/witness, or partial publication is a refusal; inequality
alone is never proof. This narrow allowance covers the supported monotonic
selected-member creating-to-ready publication, not add/remove/rebind/migration.
Do not infer valid progression from numeric revision distance or presumed no-op
updates, and do not rewrite historical completion to manufacture a match.

Current execution validation is unchanged: a live authority used for readiness
or dispatch must match the **current** binding revision and exact current
generation. Never compare it only with the old completion revision or treat the
historical event as execution permission. Preserve existing cold/history/retirement
requirements; this comparison does not start/load a worker or repair missing proof.

Before the first selected-member ready CAS, its host admission must prove root
completion with the matching ready creation journal/evidence, not only a
binding whose lead is ready. Thus member publication cannot race the original
completion-evidence/journal publication boundary. Member CAS/projection recovery
retains its accepted exact revision and partial-publication checks. No extra
root-evidence update or cross-file transaction is added to that port.

Source basis: `BackendBindingStore.CompareAndSwap` in
`session/backend_publication.go` preserves session/creation identity, reserved
list/order/address/incarnation, established native IDs and every ready entry;
`web/pi_member_publication.go` only advances the selected member and same-generation
projection. Focused fixtures: root revision2 then member revision3 validates the
original completion unchanged; historical revision above current, altered root/
reserved tuple/options, missing ready journal and stale projection refuse;
member publication before root completion refuses; lost member-projection ACK
reconciles without touching root evidence. No live or schema expansion is implied.

**Missing history and rollback.** `SessionManager.open(missing)` creates a new
native identity and therefore is never a recovery primitive without prior
owned-file existence and exact retained ID proof. P3's load operation must
positively open the recorded existing history and compare its native identity;
absence, corruption or mismatch holds recovery and cannot call create. Before
native_create_started, the same accepted receipt may resume preparation.
After it is set, an absent native result/history is Unknown, even if the process
died before sending a useful result. Retain records/resources and report the
hold; no automatic file deletion, backend fallback, compensating session or
receipt-ID change. Cleanup/deletion requires its separately authorized lifecycle
path. Package failures keep the existing forward-only recovery rule.

**Minimal dispatch and files.** Add typed schema-4 branches in existing
`creation_store.go`, `creation.go` (`installCreationLocked`, `initializeCreation`,
`proveCreation`, retry/retirement), and the exact corresponding CLI receipt/
journal helpers. Dispatch schema-4 initialization through an additive P3-backed
creation interface, never `Config.Codex`; unregistered capability refuses before
effect. Load uses accepted P2 selection and the released adapter's existing-ID
proof; no public generic create/load facade with optimistic stubs. Keep legacy
manifest projection unchanged; new Pi tracking must be explicitly backend-tagged
and resolve against the private binding, without forged `codex` metadata. Any
new manifest fields stay typed in `session/manifest.go` and are checked against
binding rather than becoming authority. Web/server/main/CLI and workspace-host
edits use lead's existing central/owner windows. No default backend change.

**Pi tracking CLI handoff (P2-C clarification; technically accepted by architect0
and recorded in design.md; lead retains source-window allocation).** Reuse Ruby
tracking authoring through an explicit backend=pi
branch at `CLI#run_start` / `Runner#start`, before their legacy Codex checks or
effects. `--no-codex` is not this branch: the existing path still selects tmux,
loads Codex authority and calls Codex-only creation/runtime lock helpers.
Require the exact retained schema-4 receipt, companion/journal and removal epoch;
do not expose a tracking phase for an unaccepted request or adopt existing work.
The two internal phases are `prepare-tracking` and `complete-tracking`; both
refuse attach, Codex/tmux actions and provider/team re-resolution.

Go's existing `runCreationCommand` retains transition SH and passes its existing
transition FD. Across a Ruby phase the parent holds **no** creation/runtime/team/
message lock. The child takes the existing creation admission, creation lock and
runtime EX in order; use a typed Pi branch of the lock helpers, not a switch
which bypasses backend checks. Revalidate selected package, preparation owner,
receipt identity/full frozen selection, removal epoch and expected binding after
waiting. Internal writers assert/reuse this held ownership, never recursively
take the same locks. On child exit, Go reacquires creation/runtime ownership and
reloads/revalidates all records before another effect. Durable request/journal
ownership bridges the phase gap; no new FD-lock or operation registry is needed.

`prepare-tracking` reuses `ensure_tracking_files`, goal seeding/validation and
the schema-4 `ensure_portal_manifest`/`new_portal_manifest` projection. Preserve
sensitivity, existing tracking/Git policy and unrelated files. It does not call
legacy `prepare_creation_journal`, `ready_creation_journal`,
`write_portal_creation_evidence!`, native initialization or authority cleanup.
Go remains the schema-4 intent/journal/native-proof owner.

Before `complete-tracking`, Go obtains the full current CreationVerifier and
original Accepted-input proof, and passes its exact expected binding revision/
generation/receipt tuple to the child. Under its locks Ruby checks that tuple
against the same retained records and writes only the tracking ready projection;
it does not declare native completion or mark the journal/receipt ready from a
boolean. Return a bounded typed result binding phase, workspace, slug, receipt,
session incarnation and tracking device/inode. Go then reacquires its locks,
repeats authoritative native/input and tracking-identity proof, and publishes
completion evidence -> journal ready -> receipt ready in the accepted order.
The projection alone cannot admit a creating conversation. Lost child ACK or a
crash resumes the same phase/IDs, and a changed tuple holds without cleanup.

Actual seams inspected for this clarification: `libexec/dev-session` start869,
ensure_tracking_files3059, receipt helpers4246/4457, manifest4775/4804,
creation/runtime locks8493/8511 and run_start10258; Go `web/creation.go`
initializeCreation890 and `web/server.go` runCreationCommand1723. Focused fake
fixtures must cover phase lock exclusion/order, stale package/removal/binding
after the handoff, lost child ACK, prepared-only tracking, completion interrupted
after projection, and zero Codex/tmux/native effects from either Ruby phase.
Exact argv/result projection may be settled within P2's assigned source window;
these ownership and revalidation requirements must remain explicit.

The narrowly assigned startup forwarding hunk for `web.Config.PiAuthDirectory`
and exact `--pi-auth-dir` forwarding is supplied by P7 and applied through
implementer2's active central window, as coordinated by lead/architect0. It
does not authorize competing `workspace-host` edits or designer source edits.

The initial Pi `portal.yml` projection uses **manifest schema 4**, required
`schema,slug,backend,creation,repositories`, optional `sensitive,artifacts`.
`backend` has exactly `kind:"pi",contract:1,session_incarnation:<64-hex>`;
`creation` has exactly `state:creating|ready,goal_sha256:<64-hex>,
initial_goal_sent:<boolean>`. Repositories/artifacts retain their existing
typed item shapes, with explicit repository scope (an empty array is valid).
No codex, tmux, native path/ID, fork or archive metadata is introduced in this
initial new-session projection. Write creating/false with owned tracking in
step 3; write ready/true only with step 6 proof. Preserve normal state.md
lifecycle independently. Both Go and Ruby strict manifest readers gain this
explicit branch; legacy schemas and their meanings remain unchanged. A manifest
without matching durable binding is insufficient for Pi routing or repair.
The original strict manifest decoder at `manifest.go:508–627` and
`libexec/dev-session` load/write_portal_manifest own this adaptation.

Acceptance fixtures exercise a crash after every numbered durable boundary,
same-receipt replay, changed backend/settings/epoch refusal, unknown native-create
and initial-input results, missing/wrong native history, forged ready projection,
retained schema-4 old-candidate refusal, correct initial-input witness reuse,
held member rendering, receipt-cache retirement continuity, and unchanged Codex
creation/archive/recovery. Use fake released-interface adapters and existing
`web/creation*_test.go`, CLI creation/preparation tests and host transition tests.
Native/H0 proof remains a specific gate for the real adapter, not a blocker to
these formats/guards/fixtures. No application edits/tests/runtime calls were
performed for this design.

### P2/P5 clarification: selected-member ready publication

The retained-member publication port belongs to P2's host composition, not P5
or the stdlib identity leaf. Its concrete boundary is:

```go
type MemberPublication struct {
    Binding session.BackendBinding
    Authority session.PiRuntimeAuthority
    Complete bool
}
PublishMemberReady(ctx context.Context, expectedRevision uint64,
    handle agentbackend.ExecutionHandle, creationID, bootstrapOperationID string,
) (MemberPublication, error)
```

These arguments are references, not caller-certified proof. P2 verifies the
existing creation mapping, persisted native identity/history and required
bootstrap Accepted witness through its injected authoritative P3 verifier.
Create with Persisted=false alone leaves the member creating. Compare the
reserved address/conversation incarnation, current generation, actual roster
settings/access and expected binding revision. Do not mint new IDs or change
settings here. Fresh monitor-owned utilities are not retained members; their
separate authority remains an explicit gate, not a new P2 conversation entry.

The port owns transition SH → runtime EX → team operation/short roster locks;
callers enter without those locks. Preserve package revalidation after waits.
No native create/dispatch is performed and no external call occurs under the
short file-store lock. Atomically publish the binding CAS first, then update
the live authority's matching revision without changing generation. Return
Complete=true only after both match. A projection-write failure returns the
durably observed binding, Complete=false and an error; normal dispatch rejects
the mismatch. The exact already-ready member/creation proof is idempotent and
may finish that projection under current authority without another revision
increment. Conflicting incarnation/native identity or unrelated revision refuses.
Implementer2 owns implementation after lead release; P5 requests this port and
never writes the binding/projection itself.
