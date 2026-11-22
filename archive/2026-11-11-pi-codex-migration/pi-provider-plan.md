# P4: Pi provider, account and member policy

P4-D, architect1, 2026-11-12. HOST-DESIGN completed/accepted before this
assignment; current/environment and retained Astra/xhigh/workspace-write roster
verified. Only this file is owned. Architect0 accepts the sufficient brief;
lead allocates implementer5. Implementer1 owns P3 execution/settings/receipts,
implementer2 central integration, and packaging remains P7-owned. No application
edit, build, prototype, credentials, login, model call or Daybreak exploration.

## Sufficient boundary and explicit limits

Release **pure catalog/account/route validation, session-default/member-override
resolution, private policy storage, settings coordination and a non-executing
fallback planner**. Keep current Codex catalogs, auth, provider switching and
defaults unchanged. P4 is Pi-only; it consumes trusted P2 identities and the
actual P3 settings API without changing H0/P2 or submission formats.

Ordinary supported provider paths are independent of unverified Daybreak.
An unavailable account/model route is reported as unavailable with its exact
gate; no silent replacement with a similarly named model. Source/fake tests
can complete without credentials. Real provider availability remains a
separate route-specific check, not evidence fabricated by a passing fake test.

Automatic fallback **remains required in the accepted overall implementation
scope**; this independent slice does not silently remove it. **No host fallback
sender is released by this slice.** P3 freezes settings in each
submission receipt and returns the retained result on same-ID retry, including
NotSubmitted. It has no parent/child attempt mapping. P4 cannot change settings
under that ID, mint a hidden ID, replay Accepted/Unknown or replay tools. The
planner can identify a candidate after positive no-submission/no-effect proof;
execution remains unavailable until a separately accepted attempt contract.
This is a concrete dependency, not a new ledger or generic retry platform.

## Concrete P3 interop

Implementer1 confirmed these existing declarations in
`portal/internal/piruntime/types.go` and the following semantics:

```go
type EffectiveSettings struct {
    Provider, AccountRef, Model, Thinking, PolicyRevision string
    Revision uint64
}
type SettingsResult struct {
    Requested, Effective EffectiveSettings
    Outcome string // "applied", "rejected", "unknown"
}
// P4 depends only on this narrow view of P3's existing Controller:
type Configurer interface {
    Configure(context.Context, agentbackend.ExecutionHandle,
        piruntime.EffectiveSettings) (piruntime.SettingsResult, error)
}
```

`Provider` is the resolved native Pi provider ID, `AccountRef` an opaque trusted
account binding, `Model` the exact canonical model ID and `Thinking` one supported
native level. `PolicyRevision` is the resolved-policy content digest below,
**not** the P2 binding revision. `Revision` is target-new effective settings
revision: current+1 for a change; same revision plus identical complete settings
returns the verified previous applied result; lower/skipped revision or changed
settings under the same revision rejects. P3 Create owns initial settings at
revision 1; Apply requires verified complete nonempty current settings with a
positive revision and rejects empty/current-revision-zero input before Configure.

P3 serializes Configure with member dispatch, requires idle plus no unresolved
receipt/tool effect, and verifies the execution handle. `rejected` means no
native mutation; partial mutation, loss of reply or uncertain error means
`unknown` and a hold. Never synthesize successful rollback or infer NotSubmitted
from an exception. The accepted [provider-switch contract](design.md) supersedes
the earlier blanket AccountRef-change veto. Compare Provider and AccountRef as a
pair: an unchanged pair permits ordinary model/thinking changes; changing only
one component rejects. A change to both may proceed after complete P4 target/
policy validation and strict canonical projection, with P2 admitting the actual
target. P3 verifies both old and new pairs against its frozen startup map under
the current idle/no-unresolved-operation admission before native mutation. This
does not enable same-provider account replacement or native fallback.

P4 imports `piruntime` and `agentbackend` one-way. P3 does not import P4.
P4 owns no direct SDK invocation, private worker framing or entrypoint edits.
Native startup/provider injection remains P3-owned under its assigned integration
window; provider route selection alone is not configuration of that transport.

## Typed catalog, policy and projections

Use new `portal/internal/piproviders/{types,catalog,policy,resolve,settings,
fallback,store}.go` and focused adjacent tests; routine file splits are owned by
implementer5. Public names below are the consumer boundary; private JSON helper
layout stays with this package. No new fields in Codex catalog/state files.

```go
type Target struct { ProviderID, AccountRef, ModelID, Thinking string }
type Budget struct { MaxExtraAttempts, MaxHops uint32 }
type Selection struct {
    Chain []Target // primary first
    Budget Budget
    FallbackOn []FailureCategory // explicit, unique; empty disables planning
}
type VersionedSelection struct { Revision uint64; Selection Selection }
type MemberKey struct { Address, Incarnation string }
type Override struct { Member MemberKey; Value VersionedSelection }
type Policy struct {
    Session agentbackend.SessionRef
    Revision uint64 // CAS/version of this policy document only
    Default VersionedSelection
    Overrides []Override
}
type Resolved struct {
    Session agentbackend.SessionRef
    Member MemberKey
    Requested Target
    Settings piruntime.EffectiveSettings
    Chain []Target
    Budget Budget
    FallbackOn []FailureCategory
    Source string // "session_default" | "member_override"
    CatalogDigest, PolicyDigest string
}
func ValidateCatalog(Catalog) error
func ValidatePolicy(Catalog, Policy) error
func Resolve(Catalog, Policy, MemberKey, uint64 /* target settings revision */) (Resolved, error)
func Apply(context.Context, Configurer, agentbackend.ExecutionHandle,
    piruntime.EffectiveSettings /* verified current */, Resolved) (piruntime.SettingsResult, error)
func ProjectRuntimeAccounts(Catalog, []Target, string /* canonicalCredentialRef */) ([]piruntime.AccountBinding, error)
func SelectableRuntimeAccounts(Catalog, string /* canonicalCredentialRef */) ([]piruntime.AccountBinding, error)
func PlanNext(Resolved, AttemptEvidence) (FallbackDecision, error) // pure, never sends
```

`Catalog` has schema 1, exact immutable-input digest and bounded slices of:

| Type | Required fields / meaning |
| --- | --- |
| `Provider` | `ID`, `Label`, `NativeID`, `RuntimeConfigRef`. IDs resolve host-approved immutable provider definitions; no browser URL/header/executable input. |
| `Account` | `Ref`, `ProviderID`, `CredentialRef`, `CredentialKey`, `AuthKind`. CredentialRef resolves host Manager configuration; it is not a token/path in public output. AuthKind describes the selected supported mechanism, not entitlement. |
| `Model` | `ProviderID`, exact `ID`, display `Label`, explicit supported `ThinkingLevels`, supported input/tool capabilities, and immutable capability evidence reference. Unknown capabilities stay unavailable. |
| `RouteGate` | Exact provider/account/model tuple, `State` (`available`, `unavailable`, `unverified`), stable `ReasonCode`, nonsecret `EvidenceRef`. Availability requires both supported adapter/configuration and the applicable route proof; credential presence/catalog listing alone does not prove entitlement. |

Start with trusted typed catalog input to the package; P7/central composition
owns its eventual packaged source and path. No new `/etc` service, background
discovery or reuse of Codex's strict catalog reader. Bound IDs to the existing
identifier convention and strings to 4096 UTF-8 bytes without controls; require
unique IDs, valid references and no duplicate physical models/account mappings.
Cap catalog input at 1 MiB, 64 providers/accounts and 4096 model/route entries.
Unknown schema/enum/fields, duplicate JSON keys or inconsistent gates refuse.
Publish only ID/label/model/thinking/gate summaries, never private config refs,
credential paths/keys or raw provider errors.

Canonical account identity is its configured native credential store/key.
One actual grant has one canonical refresh authority; aliases cannot create
independent token slots. All workers sharing that grant use the same canonical
containing auth directory/sidecars and see replacement. Distinct actual accounts
need distinct explicit configured store/key bindings, never copied grants.
Only mappings P3 can actually apply are selectable. `auth_directory` is trusted
Manager startup configuration, **not** a machine path embedded in the immutable
worker manifest. Member history/settings/resources remain private.

P4's `SelectableRuntimeAccounts(c, canonicalCredentialRef)` supplies the complete
startup union of available routes with exact canonical store/native-key mappings,
including eligible providers not selected by initial primaries. Validate the
catalog, skip unrelated unsupported/unverified mappings, deduplicate identical
pairs, sort by native Provider and reject ambiguous mappings or the existing
64-pair bound. An empty union makes Pi unavailable. P2/P7 freeze this union in
P3's existing runtime configuration; no browser/model input expands it or causes
an implicit restart.

`ProjectRuntimeAccounts(c, targets, canonicalCredentialRef)` strictly validates
the actual requested targets: `Account.CredentialRef` equals P3's fixed
`CanonicalCredentialRef` (`canonical`) and `Account.CredentialKey` equals the
native Provider ID. Unsupported selected mappings refuse. At use, the strict
projection must be contained in the frozen startup union. With fallback execution
disabled, mapping projection covers the resolved primary; later native fallback
must cover every enabled physical target. Neither view truncates or re-resolves
the immutable policy, changes CatalogDigest, or relaxes all-chain route
availability. Raw catalog gates alone do not make a route selectable: central
composition intersects them with runtime-map support and complete policy admission.

Resolve the member's exact address **and conversation incarnation** override,
otherwise inherit the session default. No wildcard role/profile/provider-global
mutation. Clearing an override is explicit and returns to inheritance. Changing
the default affects only inheriting members' desired settings; busy/held members
keep their actual settings until a permitted Configure boundary. Existing
overrides remain unchanged. Do not claim an atomic all-member provider switch.

Require a primary plus at most seven fallbacks; reject repeated canonical
provider/account/model tuples, including aliases, regardless of thinking label.
Reject virtual-to-virtual targets. A requested thinking level must be listed
for the exact model; default levels must be explicitly resolved before Configure.
Do not silently reinterpret or clamp the user's request in P4. If native Pi
later reports a different effective level, show both and its reason rather than
rewrite requested state. An unavailable fallback destination refuses policy
activation instead of silently skipping an intended account/model.

`PolicyDigest`/P3 `PolicyRevision` is SHA-256 over one P4-owned fixed ordered
JSON-array encoding of: schema 1, catalog digest, source, selected source's
revision, ordered fully resolved route tuples, budget and sorted FallbackOn
categories. It excludes unrelated
members, global document Revision, runtime generation and settings Revision.
Use one digest function and byte fixture; explicit JSON escaping/UTF-8 and
integer encoding are fixed by that implementation, never map iteration order.
An unrelated override therefore cannot change another member's effective policy.

Return typed sentinel errors for invalid catalog/policy, unavailable route,
stale policy, unsupported account switch and held runtime; use `errors.Is`, not
human-message matching. `Apply` checks the handle's member/incarnation against
the resolved policy, invokes Configure once and preserves its result/error.
An empty/unrecognized outcome becomes held Unknown, never applied. The caller
supplies verified complete current settings under P3/session admission; Apply
rejects empty/revision-zero current values and unsupported pair changes before
Configure. Initial setup remains Create-owned. P3 remains the final revision
authority, so a stale supplied snapshot cannot overwrite newer settings. Supported
pair switches preserve the same native conversation/history and use public model/
thinking APIs without shared-default writes, prompts or new input IDs. Verify
private effective state before applied; partial mutation/save or lost reply holds
Unknown. Exact account-source/override checks remain owned by the accepted
[P3/P4 canonical account contract](design.md), not inferred from account labels.

## Storage, switches and truthful actual settings

Own `<P3 session state root>/provider-policy.json`, schema 1, mode 0600/private
0700 parent, bounded 64 KiB. Fields are `schema`, `session`, `revision`,
`default`, `overrides` matching the types above with explicit snake_case names;
overrides carry address/incarnation/value. Use a dedicated `provider-policy.lock`
and atomic/fsynced compare-and-swap publication. P2 verifies scope/admission
before calls; no reading or writing its authority files here. Expose
`Store.Load()` and `Store.CompareAndSwap(expectedRevision, nextPolicy)`; reads
never create/repair and unsupported/malformed state is not absence.

The desired policy is published separately from actual effective settings.
Increment document Revision for each change; increment Default.Revision only
for default changes and the affected override revision only for its edits.
P4 stores no second copy of P3's configure/submission ledger. After desired-state
publication, configure only eligible members through P3; preserve desired/applied/
held distinctions on partial progress or restart. Never hold the policy file lock
while awaiting a worker. Recheck current desired digest before applying; a stale
request refuses rather than overwrite newer policy. Central admission ordering
serializes policy changes and per-member Configure as supplied by P2/P3.

Requested view contains source, requested primary/chain/thinking and policy
digest. Effective view comes from verified P3 settings (provider/account/model/
thinking/settings revision/policy digest). Actual dispatch view comes from
observed physical native response/request evidence: physical provider, model,
API, effective thinking and timestamps; account is the configured dispatch
binding, labelled as such rather than an independently proven provider identity.
Missing dispatch evidence is unknown, never inferred from desired settings.
Switching preserves native conversation/history identity; it does not clear
receipts, replace tools, change permissions or replay input.

## Error evidence and finite fallback planning

`AttemptEvidence` is a typed **input observation**, not a new persistent ledger:
original P3 SubmissionRef, resolved policy digest, ordinal/chain index, actual
route when known, native request/entry witness when available, submission outcome,
effect certainty, failure and shared cumulative retry/hop counts. A `Failure`
contains stage (`selection`, `configure`, `transport`, `provider_response`,
`tool`), category, allowlisted structured code/status, evidence kind/reference
and timestamp. Never persist credentials, raw headers or unrestricted error bodies.

Use these exact observation/decision field names (string enums validate strictly):

```go
type FailureCategory string
type Failure struct {
    Stage string
    Category FailureCategory
    Code, EvidenceKind, EvidenceRef string
    HTTPStatus int // zero means absent
    ObservedAt time.Time
}
type AttemptEvidence struct {
    Submission piruntime.SubmissionRef
    PolicyDigest string
    Ordinal, ChainIndex, ExtraAttempts, Hops uint32
    Actual *Target
    NativeRequestID, NativeEntryID string
    SubmissionOutcome string // "Accepted", "NotSubmitted", "Unknown"
    Effects string // "none", "possible", "observed"
    PartialOutput bool
    Failure Failure
}
type FallbackDecision struct {
    Outcome, Reason string
    Next *Target
    ExtraAttempts, Hops uint32
}
```

Empty proof fields do not establish no submission/effects. `Effects=none` must
come from P3's positive evidence, not a classifier guess. The planner checks
chain index/actual tuple/counters, policy digest and exact conversation/member
scope before offering a candidate; next counters include its prospective hop.

Categories distinguish configuration/auth, refresh/storage, model unavailable,
rate/overload, quota/billing, transport, structured policy/content, context limit,
text refusal and unknown. Only exact known adapter codes/statuses earn a category;
unclassified exceptions remain unknown. Flattened error regex, HTTP 429 alone,
or ordinary refusal text cannot prove quota versus throttling, no submission,
or safe replay. Credential refresh/storage failures hold that route and cannot
be repaired by copying auth or silently changing credentials.

`FallbackDecision` returns `stop`, `held`, `exhausted`, or
`candidate_execution_unavailable`, with reason, optional next Target and counts.
It has **no send callback**. Candidate selection requires positive P3
NotSubmitted plus positive no-native/tool-effect proof, matching frozen policy
and a policy-enabled retry category. Accepted, Unknown, partial output, any
uncertain/completed tool effects, text refusal, cancellation or stale evidence
stop/hold automatic action. Structured policy errors are not automatically
eligible: only a separately accepted exact-code policy can allow the planner.

Budget defaults are zero extra attempts/hops. An explicit fallback policy may
allow at most seven extra attempts and at most seven hops; hops cannot exceed
extra attempts. Each transport retry, native agent retry or provider hop consumes
the same cumulative extra-attempt budget for the original submitted operation;
a hop also consumes the hop budget. Reconnect, retrying Lookup, changing settings
or a successful tool continuation cannot reset counters. Normal non-retry tool
continuations are not counted as fallback attempts. If a provider/native layer
cannot expose/count its retries, automatic integration stays unavailable; do not
multiply an outer budget by hidden inner retry defaults. No classifier-model
call or extra compaction request is added by P4.

Native `registerVirtualModel` routing remains disabled in the current isolated
P4 source slice. The bounded follow-up below identifies a supported same-turn
candidate for the required automatic path; it is not host resubmission. Do not
build a private router/fork to cover cases outside its proved native classifier.

### Required automatic fallback: bounded native continuation contract

Lead requested one additional source falsification pass; it stayed below six
active minutes with no test run. **A supported same-run path exists for native
classifier-eligible failures.** At the fixed Pi head:

- `agent-session.ts:1982–1987` calls `agent.prompt(messages)` once, then
  `agent.continue()` after post-run recovery; it does not append the original
  user input again. `:2062–2074` selects the native retry path.
- `:3938–3977` checks enabled/maxRetries, emits public retry events, applies
  recovery omission and waits abortably. `:1306–1338` retains raw history but
  omits the failed assistant **and any paired tool results** from projection.
  Therefore do not claim every possible effect is automatically preserved.
- `agent-loop.ts:254–264` returns on error/abort before executing that response's
  tool calls. Earlier completed tool/result pairs remain in context; supported
  continuation does not automatically rerun them. Fresh model-issued tool calls
  still require ordinary P3 tool policy; no exactly-once effect guarantee follows.
- `agent-session.ts:885–905` calls the public virtual router with retry reason,
  failed physical response and branch state, appends changed routing state before
  dispatch, and uses the returned physical model. `model-runtime.ts:1001–1070`
  exposes registration/resolution and validates physical/configured-auth targets.
- `:1244–1252` resets native retry count after each successful assistant response.
  Native maxRetries alone is **not** our cumulative per-input budget. Native
  `retry.ts:273–277` remains a text classifier with explicit nonretryable limits;
  it does not cover arbitrary cybersec/policy errors or normal refusal text.

Freeze this **next bounded fixture/adapter contract**, with implementer1 owning
P3's private hook and implementer5 owning route policy after lead allocation:

1. Before the one input dispatch, P3 freezes the original SubmissionRef,
   generation, policy digest and physical chain. Startup resolves an immutable
   map of each native provider to its exact AccountRef/canonical auth store/key.
   The first fixture uses two fake physical providers in one shared fake native
   auth directory. No live AccountRef switch, copied grant or mid-turn Configure.
   A missing account mapping refuses routing rather than infers it from a label.
2. Register one public virtual model in that worker's private ModelRuntime.
   Route registration/selection is explicit: retain a separate
   `NativeRoutingSelection {Provider, Model, PolicyDigest}` observation for the
   selected virtual model, and physical dispatch observations for actual calls.
   Do not falsely report the selected virtual ID as the physical provider/model,
   or overwrite requested primary settings. Production Configure/view wiring
   for this extra observation is a named P3 integration dependency.
3. The asynchronous public `route()` callback uses a P3-owned bound
   `PrepareNativeRetry` hook for `reason=retry`. Its request carries original
   SubmissionRef, generation, policy digest, native ordinal, failed physical
   target/failure evidence and cumulative counters; the worker cannot choose a
   different caller. Reply is `allow` with the exact next physical target and
   updated branch-state counters, `stop`, or `held`. This is a private worker
   hook, **not** a Controller Send call or another persistent submission ledger.
4. Allow only while the original receipt is durably **Accepted**, the exact
   turn/generation remains active, the native classifier initiated retry, and
   the narrower accepted failure category permits it. Retain the same receipt,
   input digest and user entry throughout. Reject partial output, a failed
   response containing tool calls/paired effects, uncertain tool state, unknown
   native history, cancellation or unavailable route/account. Previously
   completed tool results may remain as context; they are not replayed by the
   adapter. This permission is distinct from host `PlanNext`: Accepted still
   categorically forbids host input redispatch.
5. Charge the shared extra-attempt/hop budget on the exact original operation;
   retain counters in returned public virtual routing state before physical
   dispatch. Success/tool continuation must not reset them. Start with private
   `retry.provider.maxRetries=0` and explicitly bounded `retry.maxRetries`;
   `settings-manager.ts:953` and `sdk.ts:340–350` pass that provider limit into
   supported request options. OpenAI Responses uses an SDK maxRetries=0 plus
   its explicit wrapper limit (`openai-responses.ts:216–227`); each actual
   target still needs a fixture proving no hidden provider retries. Direct
   summary/compaction requests must not use the fallback policy or replenish
   its budget; stop the initial fixture on overflow/compaction instead.
6. Gate refusal issues targeted supported `session.abort()`/retry cancellation
   for that exact worker and holds uncertain effects. Public retry events and
   finalized physical assistant/history evidence feed P3 observations; they
   are not admission or tool-termination proof. P3 confirms it can target abort
   on witness/receipt-publication failure, but the hook is **not implemented**.
   Lost browser ACK alone consults the retained receipt; it does not cancel or
   replay work. Crash/restart leaves any unfinished native route held; this
   contract adds no automatic resume from reconstructed routing state.

One finite fake SDK fixture must show: one user entry and one unchanged Accepted
receipt; A overload/error → B reply via `reason=retry`; a completed fake tool
prefix executed once and retained in B's input; failure response with partial
output/tool-call content held; quota/refusal/nonretryable error performs no hop;
zero hidden transport retries; total retry/hop exhaustion across a successful
tool continuation; correct virtual-versus-physical observations; cancellation
during backoff; worker death before/after routing-state append stays held with
no replay or counter reset. Use fixed fake providers, tiny history and disabled
summary/compaction; no production account or broad test campaign.

**Current conclusion:** native same-turn fallback is the smallest supported
candidate and does not need replacement original IDs. It is source-backed,
not runtime-proven or activated. Remaining seams are P3's bound pre-retry gate,
preconfigured account map/selection projection, and the finite budget/effect
fixture. Cross-provider retry outside the native classifier remains blocked;
if the required exact error cannot enter it, a safe host child-attempt/original-ID
budget contract requires separate accepted P3 work. No hidden receipt mutation,
scheduler, monkey patch or new mechanism inventory is authorized. These gates
do not delay the independent P4 slice.

### P4-NATIVE-BRIEF: exact source continuation

2026-11-12. Architect0 accepts the independent pure compiler/decision, P3
structural types and finite owned SDK charge/witness fixture as sufficient for
lead allocation. The production writer declaration below now uses implementer1's
landed utility/ToolPolicy base and is technically accepted by architect0.
Following acceptance of the pure
compiler, the lead released P4-NATIVE-SDK to implementer5: only the new leaf
module, finite fixture and narrow provider documentation identified below.
The lead subsequently source-released P3-NATIVE-ROUTING-CORE to implementer1
(`da705a16`) after accepting workflow `6b64c744` and confirming capacity.
That allocation covers the writer and production authority declaration below;
actual adapter proofs and package activation remain separately gated. Neither
source release enables live fallback or changes host `PlanNext`.
Initial support is retained Pi conversations with an ordinary Accepted input;
utility fallback requires a separately accepted owner extension. No new ledger,
router process, timer, maintained fork or arbitrary retry mechanism is introduced.

**P4 compiler and pure decision.** Implementer5 owns new
`portal/internal/piproviders/native.go` and `native_test.go`. Export:

```go
CompileNativePolicy(Catalog, Resolved, agentbackend.ConversationRef, []piruntime.AccountBinding) (piruntime.NativeRoutingPolicy, error)
PlanNativeRetry(piruntime.NativeRoutingPolicy, piruntime.NativeRetryEvidence) (piruntime.NativeRetryDecision, error)
```

Compile requires intact complete process-local Resolve provenance, unchanged
CatalogDigest matching the actual catalog, complete existing all-chain route
validation, strict `ProjectRuntimeAccounts(full frozen Chain)` and containment
in the exact immutable P3 startup map. Reuse existing `findTarget`/`policyBytes`;
do not recreate their mapping/digest, shorten/re-Resolve a chain or deserialize
a value as if it had Resolve provenance. Persisted intent goes through ordinary
Resolve against its exact frozen catalog before compilation. Every target is
physical and has exact supported thinking; no native clamp substitutes a level.

For an explicitly requested virtual policy, the compiled wire projection uses
a detached nonnil `FallbackOn` slice, including `[]` when no categories are
enabled. Empty means no retry category can permit a hop; it does not silently
select physical mode. Missing/null is unavailable at the strict virtual boundary,
and P3 must preserve empty arrays through copies rather than normalize null.
The owning compiler supplies this projection from the unchanged resolved policy
and full chain using the existing owning digest algorithm. Never retain a digest
while changing bytes covered by its contract; prove the projection preserves
the existing hash inputs, with no new digest recipe or shortened/re-Resolved
chain. Existing data-only/P4 disabled-policy nil semantics remain unchanged.
Physical mode remains an explicit choice. Owner5 reports the separately released
P4-NATIVE-EMPTY-CATEGORIES correction source-ready, pending the lead's commit
window. The owning policyBytes already canonicalizes original nil/empty categories
to `[]`; compiled NativeRoutingPolicy JSON is outside that digest's wire coverage.
Owner-reported intact-Resolve fixtures prove detached wire `[]`, disabled/no-hop
decision and unchanged owning hash inputs. This is compiler evidence only;
commit acceptance and actual compiler/leaf/core/writer consumption proof remain
required before claiming that empty virtual case supported end to end.
Architect0 confirmed the representation semantics; no P3 null normalization,
mode inference or SDK/core edit is part of this compiler correction.

P3 owns the following structural types in additive
`portal/internal/piruntime/native_retry_types.go`; P3 never imports P4:

```go
type NativeTarget struct { Provider, AccountRef, Model, Thinking string }
type NativeRoutingPolicy struct {
    Conversation agentbackend.ConversationRef
    Settings EffectiveSettings
    CatalogDigest, PolicyDigest string
    Targets []NativeTarget
    MaxExtraAttempts, MaxHops uint32
    FallbackOn []string
}
type NativeRoutingSelection struct { Provider, Model, Thinking, PolicyDigest string }
type NativeRoutingResult struct {
    Outcome string // applied, rejected, unknown
    Revision uint64 // last positively applied routing revision
    Selection NativeRoutingSelection
}
type NativeRetryCounters struct { ChainIndex, ExtraAttempts, Hops uint32 }
type NativeRetryEvidence struct {
    Submission SubmissionRef
    Generation, PolicyDigest string
    UserEntryID, StateEntryID, FailedEntryID string
    Counters NativeRetryCounters
    Actual NativeTarget
    FailureCategory, FailureCode, FailureEvidenceRef string
    HTTPStatus int
    Accepted, NativeRetry, FailedResponseEmpty, FailedToolsAbsent bool
    PriorEffectsComplete, NoPendingEffects, LinearHistory, Cancelled bool
}
type NativeRetryDecision struct {
    Outcome, Reason string // allow, stop, held
    Target *NativeTarget   // only for allow
    Counters NativeRetryCounters
}
type NativeRetryRequest struct {
    Runtime RuntimeRef
    Handle agentbackend.ExecutionHandle
    Evidence NativeRetryEvidence
}
type NativeRetryHandler interface {
    PrepareNativeRetry(context.Context, NativeRetryRequest) (NativeRetryDecision, error)
}
```

The compiler obtains Conversation's exact native ID from the explicit trusted
composition argument after resolving the member; it is not supplied by catalog
data. Validate that ref against Resolved before producing the policy. NativeTarget
uses native provider IDs; AccountRef remains the configured canonical binding.
No provider endpoint/auth overrides appear in these types.

The booleans are P3-certified internal observations, never model/HTTP caller
assertions. P4 checks original ref/session/member, settings/policy digest, actual
physical target, counters, enabled category and bounded chain. P3 owns their
native/effect truth and rechecks current active input/generation immediately
before permission. Missing/inconsistent evidence yields held. `allow` selects
only `ChainIndex+1`, incrementing ExtraAttempts and Hops exactly once. No
same-target native retry, wraparound, route skipping or counter reset is allowed
in this first path. Exhaustion/disabled/nonretryable returns stop; effects,
identity, history or transport uncertainty returns held. P4 cannot Send, mutate
settings, append history or turn `allow` into a host input retry.

**Production writer declaration against landed base; technically accepted.**
Implementer1 supplied commit `4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`
(parent prefix `0a647bdf`), whose conversationRecord fields are
`Schema,CreationID,Conversation,HistoryRef,HistoryFile,Generation,HeldReason,
Settings,PendingSettings,Loaded,Persisted,WorkerPID,WorkerStart,InitialSettings,
OwnerKind,Utility,ToolPolicy,PendingToolPolicy`. Existing retained schema 1 bytes
remain unchanged. Retained policy schema 2 has empty/omitted OwnerKind and nil/
omitted Utility; utility schema 2 has OwnerKind `utility`, no Conversation or
HistoryRef and no policy pointers. `PendingSettings` remains the existing complete
`*EffectiveSettings`, including its null-when-absent field. Preserve all those
formats and the existing ToolPolicy/PendingToolPolicy semantics.

For retained conversations only, define schema 3 as that exact retained schema-2
shape plus required `NativeRouting` and optional `PendingNativeRouting` (omit
when nil; explicit null is invalid). No schema-3 utility record is supported.
Exact exported-Go JSON fields and in-process types are:

```go
type NativeRoutingRequest struct {
    Revision uint64 // target-new routing revision, not Settings.Revision
    Mode string // physical or virtual
    ExpectedSettings EffectiveSettings
    Policy *NativeRoutingPolicy `json:",omitempty"`
}
type NativeRoutingState struct {
    Revision uint64
    Mode string
    Settings EffectiveSettings
    Policy *NativeRoutingPolicy `json:",omitempty"`
    Selection NativeRoutingSelection
}
// conversationRecord schema 3:
NativeRouting NativeRoutingState
PendingNativeRouting *NativeRoutingRequest `json:",omitempty"`
// Optional P3 interface:
ConfigureNativeRouting(context.Context, agentbackend.ExecutionHandle,
    NativeRoutingRequest) (NativeRoutingResult, error)
type NativeRoutingInspection struct {
    Outcome string // legacy, recorded, verified, held, unavailable
    Generation string
    Settings EffectiveSettings
    State *NativeRoutingState
    Pending *NativeRoutingRequest
    Reason string // bounded nonsecret diagnostic code
}
InspectNativeRouting(context.Context, agentbackend.ExecutionHandle) (NativeRoutingInspection, error)
```

`InspectNativeRouting` uses the same optional bounded controller transport and
exact current-handle read/recovery admission. It never creates/loads a worker,
registers a router, configures, repairs or resumes. There is no existing public
projection that can substitute for it. Under P3's existing serialization, validate
owner/schema/native mapping, current generation, full Settings and saved routing
policy/selection, then copy the complete state/pending target. For schema 1/2,
`legacy` returns exact verified recorded Settings with nil State/Pending; it does
not invent a physical mode or revision 0. For valid schema 3 without live proof,
`recorded` returns the complete durable state: this permits restarted callers to
discover revision/settings/mode but is not execution admission. `verified` also
requires a matching live native selection/thinking, exact policy/map/module proof,
and no pending transaction or unresolved hold. `held` may expose positively read
State/Pending with its explicit reason, never pretend the pending target applied.
Any pending settings/tool/routing transaction or unresolved execution hold takes
precedence over legacy/recorded/verified outcomes, including on schema 1/2;
inspection reports held without clearing that state.
Malformed/missing/ambiguous records yield unavailable/error with nil State/Pending;
zero-valued Settings is not evidence. Each meaningful reply identifies the current
verified Generation. A stopped/cold runtime does not acquire execution merely to
answer inspection. Rejected/Unknown Configure results cannot substitute for this
fresh observation; callers use the returned record revision only under Configure's
independent exact-state/native admission checks.

The following cold-inspection exception is technically accepted by architect0
and recorded in canonical `design.md`. For an already admitted current supervisor
after an explicit successor, cold
recorded inspection may read a normally unloaded mapping from an older saved
generation. Verify the current control RuntimeRef/ExecutionHandle and exact
retained conversation/session/incarnation/path plus the complete strict mapping;
permit the generation mismatch only with `record.Loaded == false` and
`c.worker == nil`. Return recorded State/Settings under the **current request's**
Generation fence. That field identifies the authorized observation, not promotion
of record.Generation or proof of live native state. Do not rewrite the mapping,
create/load a worker or return verified. Pending transactions, held state or
unfinished/Unknown receipts retain held precedence. An old-generation mapping
marked loaded or with a worker is held/scope failure, never inferred unloaded.
This exception does not admit a stale control request or bypass ordinary
successor admission. Later Load rechecks the complete saved routing policy and
revision under current serialization/package/route guards before its existing
generation update/restoration. No original retry arm or permission is recovered.
Focused inspection fixtures cover old-generation unloaded/no-worker recorded
success, current response fence with unchanged saved generation, and refusal/
held precedence for loaded, worker-present, pending, Unknown or stale-caller cases.

`NativeRoutingResult.Revision` is the already-declared additive scalar on the
current Outcome/Selection type. Applied returns the positively verified applied
revision. Rejected/unknown may return only a positively known current mapping
revision, never the requested/pending revision; it does not verify live selection
or clear a hold. With no known routing state, zero is only an unavailable value,
not evidence of physical baseline 0. Restarted callers use InspectNativeRouting
to distinguish legacy, recorded, verified and held state; Configure is not a
discovery probe.

Physical mode forbids Policy; Selection is the exact Settings provider/model/
thinking/policy digest. Virtual mode requires the full compiled policy, matching
Conversation/Settings/CatalogDigest/PolicyDigest/canonical map, and exact private
virtual Selection. This changes execution selection only; physical primary
Settings and its revision, requested provider-policy document, native identity,
history and original receipt bytes stay unchanged. Physical reset restores that
current primary and disables native fallback without clearing requested policy.
The authoritative requested full frozen policy remains P4's session
`provider-policy.json` plus P2's admitted selection/provenance. P3's nil Policy in
physical mode disables its execution projection; it is not deletion, truncation
or modification of that P4/P2 policy. No policy digest is rewritten for reset.

Routing revision 0 exists solely as the positively verified physical baseline
of an explicit first schema-1/2 conversion. Before conversion, compare the current
native physical model/thinking, complete mapped Settings, account map, module,
generation and absence of pending/unknown effects; absence of routing fields
alone proves nothing. Only then may the request for revision 1 publish schema 3
with that baseline and complete pending revision-1 target, preserving every
existing field. Baseline Mode must be physical, Policy absent and Selection equal
the verified physical Settings; virtual revision 0 is invalid. A positive
pre-mutation first-request rejection may leave schema 3 with the verified physical
baseline at revision 0 and no pending target. Do not downgrade it or infer that
baseline after a partial/uncertain mutation; uncertainty retains the exact pending
target and hold. No proactive conversion or inspection-triggered conversion.

Request revisions are exact integers in `1..9007199254740991` (2^53-1), checked in
Go/JavaScript input, retained target/state reads and before native effects. Applied
state uses that range except the physical baseline 0 above. Refuse overflow or
lossy conversion; at maximum, a new increment refuses while exact verified replay
may still succeed. This bound concerns routing revisions only. A request uses
current routing revision+1; identical complete target
at the already-applied revision may replay only after native/private verification.
Stale/skipped/reused-different targets refuse. Empty/current-revision-zero
ExpectedSettings is invalid; full ExpectedSettings must equal current mapping
Settings. The routing revision is a scalar CAS in this same mapping, not another
operation ledger or input ID namespace. Missing optional implementation refuses.

Under the existing c.mu/s.member/c.save ownership, require current handle/
generation, exact frozen account pairs and module proof, idle native snapshot,
no unresolved input/descendants/callbacks, and no pending settings/tool/routing
transaction. Atomically fsync PendingNativeRouting **before** any native change.
Apply registration/model/thinking through public APIs without shared defaults;
verify exact native selection and private desired target, then atomically save
new NativeRouting and clear PendingNativeRouting in one mapping publication.
Positive pre-mutation refusal may preserve prior state/clear its exact pending
request with rejected outcome. Partial mutation/save, lost reply or missing proof
keeps prior NativeRouting plus exact pending target and Unknown hold; never replay
that pending mutation automatically or claim rollback. Existing settings and tool
policy mutations also refuse while PendingNativeRouting is present.

Ordinary Configure requires physical routing mode; an authorized explicit reset
precedes a physical settings change. Under its existing PendingSettings transaction,
successful Configure keeps schema-3 NativeRouting.Settings/physical Selection
coherent with new Settings, preserving routing Revision; the full settings
precondition prevents stale routing-request replay. Tool policy cannot change
native routing state. These interactions are part of the writer fixture, not
permission to modify another package's current source window.

Reload first validates record schema, exact compiled policy/map/module and absence
of every pending transaction. For virtual mode, register the exact saved virtual
definition before native restoration can select a fallback physical model, then
verify saved/native selection before exposing operations. Missing registration,
changed map/policy, pending target or selection mismatch holds; no automatic
physical reset, prompt or retry. Physical mode verifies its exact saved primary.
An unfinished original input remains held by existing receipt/effect rules even
when routing state itself is valid; reload never resumes it.

P2/P7 add exact `piNativeRouting:{policy:1,recordSchema:3}` to the existing runtime
contract only with implemented reader/writer/guard and passing fixtures. Existing
target preflight inventories retained schema-3 mappings even in physical mode or
with pending/held state and refuses missing/unequal support. Every retained
schema-3 mapping requires **both** exact
`piToolPolicy:{policy:1,conversationSchema:2}` and
`piNativeRouting:{policy:1,recordSchema:3}`. The former certifies B2's embedded
policy-layout-2 contract, not that an old schema-2 reader understands schema 3.
Use explicit shared retained-record schema dispatch: `1 -> legacy retained`,
`2 -> retained policy-layout 2`, `3 -> retained policy-layout 2 plus native-routing 3`;
the existing `OwnerKind=utility,Schema=2` arm remains separate and rejects routing
and policy fields. Unknown schema/owner combinations refuse. No equality check
for schema 2 may silently admit schema 3 without its new full validator.

P3 must route B2 `InspectToolPolicy`, `ApplyToolPolicy`, ordinary Load and
`VerifyCreation` through that exact dispatch in the existing conversation reader.
Schema-3 B2 inspection verifies its unchanged ToolPolicy target/ceiling/native
sets; routing verification never certifies tool enforcement. Apply retains all
B2 expected-revision/idle/ceiling/native checks and also refuses pending routing.
Load verifies both saved tool policy and routing selection before exposing their
operations; either pending/mismatched proof holds. VerifyCreation preserves exact
creation ID, original native/input/settings proof and B2 replay rules, and cannot
publish ready through an unresolved routing transaction. ToolPolicy nil remains
unavailable, including schema 3 converted from policy-less schema 1; native
routing conversion does not migrate tools, infer Default, or enable B2 Apply.
Create remains its existing schema-1/2 path and replay constraints, including the
no-replay-after-advanced-tool-policy rule; it does not manufacture schema 3 or
reset routing. The new dispatch is explicit source work, not a capability claim
about landed `4c0bd9a0` readers, which support only retained 1/2 and utility 2.

**Native package-guard injection; technically accepted by architect0.** The
actual owning `session.DecodePiWorkflowContract` consumes the whole bounded
runtime metadata and validates the six-field workflow-1/policy-layout-2 bundle.
It has no native-routing-3 contract today. Because session already imports
piruntime, P3 must not import session or independently parse piToolPolicy/
piNativeRouting subobjects. Do not relocate the shared codec for this package.
Freeze this smallest optional P3-owned consumer:

```go
type NativeRoutingPackageGuard func(context.Context, string /* exact app store root */) error
// Manager Config, no serialized field:
NativeRoutingPackageGuard NativeRoutingPackageGuard

func SuperviseWithNativeRoutingGuard(ctx context.Context,
    path, instance, request, digest string, guard NativeRoutingPackageGuard) error
```

Retain the existing five-argument `Supervise` as a wrapper using nil guard;
both exports delegate to the same existing supervisor implementation. Store
the injected function in the private supervisor field
`nativeRoutingPackageGuard`, outside runtimeConfig/launch/handshake formats.
Manager uses its Config function; the supervisor independently invokes its own
in-process function, never a boolean or callback result supplied on the wire.
The existing generic Config.validatePackage hook is not this proof and is not
a fallback. Nil, cancellation, error or unsupported metadata is unavailable.

For each dependent schema-3 first conversion/write, routing Configure or virtual
restore/effect admission, capture the exact verified runtime/launch AppStorePath
and invoke the owning guard before c.mu, receipt or attachment locks. Recheck
the captured runtime/request/generation/app-root under the ordinary operation
lock before pending publication, worker creation/restoration or native mutation.
Supervisor's root is its validated launch.AppStorePath whose workspace-portal
executable identity Supervise already proves; Manager derives it from that exact
verified runtime's stored launch, never a caller path or moving profile. Existing
worker metadata independently binds PiPackage/module/account checks. An operation
cannot reuse another runtime/root's successful guard or treat injection presence
as success. Physical reset needs this package guard for its schema-3 write, but
still needs no route/failure authority. Apply the same requirement to B2/settings
mutations that write schema 3. No guard invocation causes a native action.

Pure strict schema decoding and recorded inspection remain available without
the guard, within their existing read-only authority; they neither convert nor
advertise verified execution. Absence of the production guard keeps dependent
writer/native paths unavailable even if fake transaction tests pass. Existing
schema-1/2 and utility-2 operations retain their current guards and formats.

The sufficient independent decoder-only brief is recorded in canonical
`design.md` (architect0 report `a5d8ba8e-7ac5-42a7-8cea-c5d94f7806dc`); lead
release remains required. Its exact new files are
`session/pi_native_routing_contract.go` and `_test.go`, with no existing workflow
file/test, record codec, scanner, Ruby, P3, consumer or metadata edits. It adds
`session.DecodePiNativeRoutingContract(data []byte) (PiNativeRoutingContract,error)`
with return-only `PiNativeRoutingContract{Workflow PiWorkflowContract; Policy int;
RecordSchema int}`. It first requires the complete
owning DecodePiWorkflowContract result, then strictly validates exact
`piNativeRouting:{policy:1,recordSchema:3}` from that same bounded whole metadata
using the existing owning duplicate/encoding/null/integer handling. It returns
that workflow contract plus native-routing contract as detached data. There is
no P3 or command-local parallel JSON parser. Positive native3 inventory remains
separate and waits for owner1's accepted UnmarshalJSON,
validateRetainedNativeRouting and validateConversationRecord checkpoint; the
existing inventory export whitelist stays at retained1/2. The later guard
completion must deliver all-cold/pending/held native3 inventory and predecessor
refusal proofs. Decoder support alone does not authorize writer enablement.

Only after that separate guard package is accepted, central composition can
provide `verifyPiNativeRoutingPackage(ctx, appStorePath) error` in
`cmd/workspace-portal` package main: bounded read of that immutable root's
`share/workspace-portal/runtime-contract.json`, then the owning complete decoder
and existing exact package identity checks. Pass this same helper through optional
`web.Config.PiNativeRoutingPackageGuard` (type `piruntime.NativeRoutingPackageGuard`)
to `piManagerConfiguration` and Manager Config; web cannot invoke main's private
helper directly. The same main-package helper feeds the actual command consumer in
`portal/cmd/workspace-portal/pi_runtime.go`:
`piruntime.SuperviseWithNativeRoutingGuard(ctx,path,instance,request,digest,verifyPiNativeRoutingPackage)`.
Keep existing CLI arguments unchanged. The command currently calls the nil-guard
five-argument Supervise, so no production injection exists yet. Both actual
consumers must be wired in owner2's later window before enablement. The helper has
no permissive fallback, generic true return or capability-presence shortcut.

Owner1 owns only the P3 type/Config/private-field/wrapper and call sites within
the released core, with explicitly fake guards in existing supervisor fixtures.
Owner3's owning decoder/inventory amendment and owner2's central Manager/command
composition need separate lead release and their existing file windows; owner1
must not edit their source or publish metadata. P7 producer/activation remains
separate. No current file needs a shared edit: future changes to
session/pi_workflow_contract.go and cmd/workspace-portal/pi_runtime.go are
coordinated with those owners before release. Focused fixtures prove nil/error
refusal before any schema-3 write/effect, exact app-root forwarding/recheck,
unchanged schema1/2/utility2 behavior and native-free recorded inspection.
Production guard acceptance later uses the owning whole-map/cold/predecessor
fixtures, not a fake callback assertion.

**N2 Manager classification fence: technically accepted and source-released
to owner1 under lead `06a4c0aa`.** Architect0 accepted the exact amendment in canonical
[design.md](design.md) at the N2 Configure/Apply
classification-fence paragraph (technical report `9bb0ffab`). Lead expanded the
same N1/N2 native-fix package from frozen primary d3 to include the exact private
frame/supervisor scope below. R4 remains parked; this receipt changes allocation
status only, with no change to accepted semantics or compatibility.

Owner1 confirmed no exclusion spans Manager's owning full/path-strict mapping
read through m.call's Inspect wait and the supervisor mutation. A request can
classify legacy1/2, skip its Manager guard, then arrive after another Manager
converts the same mapping to3. Supervisor's own guard/checkRecord cannot bind
the first Manager's earlier observation. Preserve the existing helper's runtime,
Start, generation, app-root and fresh mapping checks, and add this exact fence:

- Only the existing retained Configure conversationRequest and ApplyToolPolicy
  toolPolicyRequest gain optional private `ExpectedRecordSchema`. Omission means
  legacy-only1/2; a present value must be integer3 exactly. Use the owning strict
  decoder with presence-aware scalar handling: reject explicit null,0,1,2, other
  numbers, fractions, strings, wrong casing and duplicates. The Manager sets3
  only after classifying3 and completing its own local package guard; legacy
  payloads omit the field and retain their bytes/shape. No permission or guard
  result is transmitted.
- Supervisor independently runs its own guard outside locks and retains
  nativePackageForRecord/checkRecord. Under c.mu, before any pending/write,
  worker call or effect, require omitted expectation with actual1/2, or3 with
  actual3. A mismatch uses existing conflict/rejected refusal without automatic
  retry or repair. Old callers cannot mutate3; old callers on1/2 remain supported.
  A predecessor that rejects the new3 field already lacks schema3 support.
- Exact released owner1 source window: native_routing.go helper, controller.go
  Configure dispatch, conversation.go private request/configure check,
  tool_policy.go private request/Apply path, supervisor.go forwarding, and
  existing focused native/codec tests. Other inspection/read/interrupt/unload
  operations and utility2 remain unchanged. No public API, stored schema,
  generic control envelope, new operation, lock or ledger is added.

Finite acceptance uses existing Manager/Unix/fake-worker fixtures: stable3 with
nil/error Manager guard and accepting supervisor; independent supervisor refusal;
both guards accepted; strict optional-field cases; legacy1/2 payload and utility
compatibility; and the actual two-Manager race. Pause legacy A after its final
read, let B convert the same mapping to3 while Runtime/Start/settings/policy stay
unchanged, then resume A Configure or Apply: both must refuse with no additional
write or worker effect. No SDK run or new harness. Sequential guard fixtures alone
do not establish this fence. Owner1 completes N1/N2 source, quick checks and
commits before the same reviewer0 checks the affected lane/new private contract;
unchanged original review conclusions remain. Substantive deviations return to
lead. This planning receipt makes no source/test completion claim by architect1.
Completed schema1/2 review remains independent.

Keep the recognized
schema-4 creation fence while dependent mappings remain; prove actual older
reader/target refusal before enabling this writer. No H0 field, new scanner/store
or inferred metadata support. P2 supplies admitted compiled policy; source work
does not expand the frozen account map or accept untrusted model selectors.

Required narrow writer fixtures cover old retained1/2 and utility2 byte/decoder
compatibility, schema3 field/owner rejection, first conversion, exact replay/CAS,
virtual enable and explicit physical reset on the same native history, no policy
rewrite, mutual pending exclusion, partial mutation/lost ACK hold, plain Configure
coherence after reset, and reload with missing registration/map change/pending
target. Also cover read-only inspection after caller restart, recorded versus
live-verified proof, nil legacy state with no inferred revision 0, positive
first-request rejection retaining physical-0, virtual-0/unsafe integers/overflow
refusal, B2 Inspect/Apply/Load/VerifyCreation schema dispatch and nil-policy
unavailability. Add both-capability target guards/actual older-reader refusal;
no production account or
new input dispatch is needed. Architect0 technically accepted this exact completed
declaration against `4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2` and recorded it in
`design.md`. Cold-state, predecessor-package, native retry and effect proofs remain
required before live writer enablement; acceptance makes no implementation or
capability claim. Lead allocation `da705a16` now releases its owner1 source window.
Independent compiler/decision and finite SDK charge proof remain unchanged.

Register the private virtual model through public ModelRuntime using provider
`dev-workspace-router`, ID `fallback-<PolicyDigest>`, and exactly the selected
primary thinking level. These reserved IDs must not collide with a physical
catalog model. Use supported `setModel(...,{persist:false})` and private settings
publication; expose the virtual selection separately from requested/effective
physical primary settings and actual physical dispatch. Same-policy replay is
idempotent only after native/private agreement. Unknown partial selection/save
holds. Restoring physical-only operation requires ordinary authorized idle
configuration; missing virtual registration on reload must hold, never accept
Pi's automatic last-physical-model fallback as the requested policy. No prompt,
new input ID or shared/global defaults are part of selection.

P3 captures exact SubmissionRef and immutable compiled policy before the single
ordinary prompt. For `reason=user`, initialize state once for that exact new
input, after its durable Accepted witness; prepared/dispatching waits within the
existing bounded deadline without holding witness/message/store locks. Any
second user reason for the same input refuses unless the state and native request
prove it is the same still-unissued primary. `continuation` stays on the recorded
physical target with unchanged counters. `direct` and context overflow/compaction
stop this first path; no classifier-model/summary request is added.

For `reason=retry`, require the native classifier actually entered retry and a
persisted physical failed assistant response associated with the current input.
Register a distinct private `native_retry` request/reply discriminant on the
existing worker pipe/control attachment. It reuses B1's bounded correlation,
cancellation and attachment checks, but is **not** HostCall, an SDK tool, a fake
toolCallID, or another Controller.Send. P3 enriches the trusted request from its
activeRef and worker mapping, verifies the original host receipt is still
Accepted, proves history/effects, then calls the injected pure P4 decider.
No receipt mutex/worker scanner/message lock is held while awaiting the callback.
Absent handler/attachment, timeout or stale generation holds and cancels only
this exact native retry path; no replacement input is sent. Reply validation
binds the original request/counters/target; model-supplied permission is invalid.

**Cumulative charge in public branch history.** The lead-released P4-NATIVE-SDK
leaf module in `pi-runtime/src/native-retry.mjs` is implementer5-owned; P3 owns its
eventual worker/transport registration and trusted admission adapter. The module
injects the actual SDK, ModelRuntime, SessionManager, frozen policy/exact subject
and generation, trusted PrepareNativeRetry and existing syncHistoryPrefix.
At this boundary policy/decision values retain P3's exported-Go JSON field names
from `native_retry_types.go`, without case aliases or a second wire format.
Public SDK results remain `{model,thinkingLevel}`; the branch state below uses
its explicit lower-camel projection. A fixture-injected acceptance/effect witness
is labeled fake SDK admission, never production receipt proof. The sole persisted counters are the supported
virtual-model branch state, not a host sidecar. Exact state keys are:

```text
schema:1, input:{operationId,action,digest}, nativeSessionId, userEntryId,
policyDigest, settingsRevision, chainIndex, extraAttempts, hops,
lastFailureEntryId
```

The initial state has counters zero and empty lastFailureEntryId. All fields
except counters/index/lastFailureEntryId are immutable for that original input.
Generation is deliberately absent; current generation remains an execution
fence, not a new budget namespace. Each retry compares `request.state` against
the latest exact matching entry on independently reopened native branch history,
the original user-entry witness and active policy. Require linear ancestry,
monotone counters/index, `hops=chainIndex=extraAttempts` for this first next-hop
implementation, values within the original maxima, and no already-charged same
failed entry. Earlier input state cannot initialize a retry for this input.

After allow, charge **before returning a physical target**: call public
`SessionManager.appendCustomEntry(VIRTUAL_MODEL_STATE_ENTRY,
{provider,modelId,state})`, using the exported constant and new exact state.
Reopen the existing mapped native history with public APIs, compare the entire
entry/parent/state and native ID, and use P3's existing `syncHistoryPrefix` file
and directory synchronization. Only then return `{model,thinkingLevel}` from
route(), omitting `state`. Pi's public branch reader supplies the new state on
the next callback; omitting returned state prevents Pi from appending it twice.
Use this same path for initial zero counters after the real user witness.
No raw JSONL/private method or synthetic input is used. Charge/write/read/sync
failure holds; do not return a target. Crash after charge but before dispatch
conservatively consumes the allowance and holds; it never refunds/resumes/replays.

Pinned evidence: `virtual-models.ts` exports the entry type and branch reader;
`index.ts:410` exports the constant; `session-manager.ts:1308` exposes public
append; `agent-session.ts:885–905` appends returned state before dispatch.
The public before-provider-request extension runner catches handler exceptions
(`extensions/runner.ts:1379–1401`), so it is explicitly **not** the charge guard.
Implementer1 confirms compatibility with current history sync and linear-entry
rules; omitted-state/no-duplicate attribution remains a required finite fixture.

**Failure/effect and hidden-retry boundary.** Native retry eligibility is only
one gate: its text classifier alone does not certify a safe category. Initial
allowlist is exact adapter-evidenced `rate_limit_exceeded/429` or `overloaded/503`
plus an enabled policy category, and the actual physical provider must have
verified failure-source and retry-disable support. Raw status alone, regex,
quota/billing/auth/storage/policy/refusal/context errors, missing failed physical
response or a route exception do not permit a hop. Keep unsupported routes
unavailable; this does not start a new classifier/provider research project.

Reject any emitted partial text/thinking, failed-response tool call, paired tool
result, uncertain/pending tool/callback/resource effect, cancellation, or changed
history. Earlier completed tool/result pairs may remain only with exact positive
completion/lineage proof and unchanged projection; never replay them. A later
fresh model tool call is still an ordinary tool effect, not exactly-once proof.
Actual stream observations, not only the final normalized response, establish
whether output was partial. Set provider/transport retry limits to zero and
finite native maxRetries from the original budget. Native counters reset after
success, so the branch counters above are authoritative across successful tool
continuations. A target with hidden/unobservable retries cannot activate this
path; no multiplication of nested budgets is allowed. Original receipt, user
entry, digest and settings revision are unchanged throughout.

**Smallest release/check sequence.** Implementer5 owns pure compiler/decision
tests on the P3-owned types and, under the lead's separate P4-NATIVE-SDK release,
the new `pi-runtime/src/native-retry.mjs`, finite
`test/pi_runtime/native-retry.mjs` fixture and assigned documentation. Implementer1
owns additive `piruntime/native_retry{,_types,_test}.go` and existing worker/
transport/config registration under P3-NATIVE-ROUTING-CORE (`da705a16`).
P4-NATIVE-SDK is accepted independently; its leaf/pure compiler stay owner5-owned
and untouched unless an exact disjoint correction is released. P2/P7
registration/projection comes after those source fixtures; no arbitrary runtime
manifest edit is owned by P4. The accepted P4 pure/compiler work is its prerequisite,
and existing source boundaries remain unchanged. Owner1 starts with codecs,
transaction/expiry cases and compilation, then one finite actual original-input/
charge fixture. Central owner2 and app.js owner4 execute disjoint source.

Use the pinned SDK and at most three physical targets across two fake provider
implementations, tiny owned history, fake canonical auth, finite deterministic
scripts and disabled summary/compaction. A successful run must prove one user
entry and the same Accepted receipt/digest, A error → B response via native
continue, one public state entry per charge, exact selected/physical views,
provider calls counted with zero hidden retries, and no second prompt. A completed
tool prefix executes once and appears unchanged in B's context. Then B success/
tool continuation followed by failure with C available and max extra/hops=1 must
stop before C: success cannot reset the original budget. Separate bounded cases
cover partial output, failed tool content/paired effects, unsupported code/refusal,
cancellation/backoff, wrong state/receipt/generation, and worker death immediately
before/after charge: zero unsafe hop, held original operation, no restart replay.

Run the smallest pure Go fixture first in D's Nix shell, then this one finite
SDK script under the existing test conventions. Record exact pinned source,
request/response counts, user/receipt/state identities and the first refusal.
Stop on any native reappend, swallowed-gate effect, hidden retry, counter reset,
history mismatch or inability to attribute a failure; hold activation and report
that exact missing proof rather than adding another engine. Long/uncertain checks
need the ordinary fresh watcher when actually allocated. No test or native call
was run for this brief; live provider availability remains separate.

### Production native retry authority adapter: source declaration

2026-11-12, design only; technically accepted by architect0, including the
conditional expiry contract, and recorded in canonical `design.md` (lead report
`c0a2847b`). The accepted SDK leaf is `aec5bea24c6a1bf18dd5c7941617286c869e4c7d`.
Its 19-case fixture proves the public SDK charge/continuation behavior under
**fake host admission/effect/failure certificates**. It supplies none of the
production authorities below. Lead allocation `da705a16` subsequently released
owner1's P3 core source against this declaration; it does not supply the absent
physical-route/domain completion adapters or activate metadata. Independent
P2/P6 and other already released packages are not held by this work.

**Original input and deadline.** Add the following P3-owned, memory-only input
projection, retaining the exported-Go spelling inside the private payload:

```go
type NativeRetryInput struct {
    Submission SubmissionRef
    Generation, PolicyDigest string
    SettingsRevision uint64
    StartedUnixMS, DeadlineUnixMS int64
}
```

The trusted portal composition supplies `NativeRetryWindowMillis` through the
optional native authority on the existing attached control connection. Zero or
missing means unavailable; enabled values are integers `1..3600000`. This is a
runtime execution bound, not a new user policy field or a different retry/hop
budget. Freeze it once for the original input. The only initializer is the
existing `receiptEngine.sendOwned` **first dispatch closure**, after its durable
dispatching write and before `worker.Call("send", ...)`. Supervisor time supplies
start and absolute Unix-millisecond deadline, checked for safe-integer overflow.
The full retained SubmissionRef comes from `ref.retained`, never from model
arguments or a worker-generated ID. Freeze current generation, complete compiled
policy/settings, account map, worker identity and attachment identity with it.
Utility owners cannot enter this arm.

For enabled retained routing only, extend the existing private send body with
`nativeRetry: NativeRetryInput`; preserve its existing `message` and
`inputOperationID` and require the latter to equal Submission.OperationID.
Disabled/legacy sends retain their current payload. Worker validation requires
exact runtime/handle/policy/ref/settings agreement before `beginInput`. Extend
JS activeInput with this frozen projection while retaining `operationID` and
`witness` for B1. Pass the leaf its exact existing
`beginInput({Submission,Generation,deadline:DeadlineUnixMS,admit})` shape.

Supervisor owns a separate active native-run arm under `activeMu`, with the
frozen input, captured worker/attachment, monotonic expiry/cancel context and
active/finished/held state. `c.activeRef` is not that arm: it retains the last
callback input after the native prompt ends. Matching worker settlement ends the
arm only after the exact prompt settles and no callbacks/effects remain
unresolved. The private `native_retry_settled` event carries the frozen Input
and final LeafEntryID from that prompt's completion handler; it grants no
external-effect proof by itself. A stale settlement cannot end another input.
Duplicate Send/Lookup
returns the existing receipt before the dispatch closure and never creates,
renews or replaces the arm. Reattachment cannot adopt an old arm. A later
first-dispatch closure and worker beginInput must refuse to replace an active,
held or unsettled arm, including one with an outstanding expiry request. Reuse
requires exact original settlement and positive authority/effect completion;
an idle snapshot, cleared JS activeInput or surviving Accepted receipt alone
cannot release that exclusion.

The supervisor's monotonic timer covers the **entire original run**, including
admission, backoff, stream and tool continuations. The leaf's absolute deadline
also bounds every certificate, charge and route return; backward wall-clock
movement cannot extend the supervisor lifetime. Expiry/cancel/disconnect targets
only the captured worker/input and calls its bounded hold/abort path, cancels
pending native certificates, and records the existing worker hold if completion
or effects are uncertain. Abort/SDK idle alone does not certify descendants or
external effects settled. An already Accepted receipt remains Accepted; outcome
uncertainty belongs to the run/hold, not a rewritten admission receipt. Send ACK
context, B1's 30-second callback timeout and a fresh retry timestamp are never
sources of this deadline. Lost active state, process restart or successor loses
retry permission permanently for that original input: read/reconcile remains
possible, continuation/replay does not. No deadline/arm is added to receipt
schema 1, utility schema 2, the receipt digest or a new on-disk store. Existing
strict receipt bytes remain unchanged.

**Conditional expiry/abort.** Owner1's existing worker abort/hold requests are
generic; they are not safe substitutes for input-bound expiry. Add the optional
private worker operation `native_retry_expire`, owned by P3 in worker/protocol/
session source, using the existing bounded request envelope and identity:

```go
type NativeRetryExpiry struct {
    Input NativeRetryInput
    Reason string // deadline, cancel, attachment_lost, authority_lost
}
type NativeRetryExpiryResult struct {
    Outcome string // no_effect or held
    Matched, Idle bool
}
```

Before enqueue, supervisor checks the captured Input, arm, worker, attachment
identity and current generation. Attachment loss means that exact captured
attachment closed, not that a replacement attachment owns the arm. The worker
then checks its envelope identity/current generation and synchronously compares
the **entire** Input with its current activeInput.nativeRetry before its first
await or any hold/abort/certificate mutation. Stale, missing or mismatched input
returns `{Outcome:"no_effect",Matched:false,Idle:false}` and changes nothing.
This proves only that no matching abort occurred, never original settlement or
effect completion. It must never fall back to generic abort/hold.

On a match, synchronously mark that original arm and worker held, cancel only
its native certificates and prevent successor admission, then invoke the
existing hold/abort path on the captured session. Return
`{Outcome:"held",Matched:true,Idle:<observed SDK idle>}`; idle still proves no
external-effect/descendant settlement. Failure/lost reply after a possible
matching abort keeps the original arm held and cannot trigger another worker's
abort or a fresh input. P3 reconciles only that exact conditional request. The
supervisor ignores stale replies for another arm. Capability negotiation for
native retry includes this operation; unsupported peers cannot activate routing.
This adds no socket, timer service, receipt or source allocation.

**Bound proof ports.** P3 owns the following optional consumer types; P4 supplies
only the existing pure decider. Extend the existing host callback attachment
handler through an optional `NativeRetryAuthority` interface, without changing
HostCall/tool semantics or adding a connection/listener:

```go
type NativePrefixBinding struct {
    Runtime RuntimeRef
    Handle agentbackend.ExecutionHandle
    Input NativeRetryInput
    UserEntryID, LeafEntryID, BranchSHA256 string
}
type NativeEffectRequest struct {
    Binding NativePrefixBinding
    Branch json.RawMessage
}
type NativeEffectProof struct {
    Binding NativePrefixBinding
    PriorEffectsComplete, NoPendingEffects bool
}
type NativeRouteProof struct {
    Target NativeTarget
    AppStorePath, PiPackage, AdapterID, EvidenceRef string
    Verified, StructuredFailure, ProviderRetriesDisabled, TransportRetriesDisabled bool
}
type NativeFailureRequest struct {
    Binding NativePrefixBinding
    Target NativeTarget
    Entry json.RawMessage
}
type NativeFailureProof struct {
    Binding NativePrefixBinding
    Target NativeTarget
    FailedEntryID, FailureCategory, FailureCode, FailureEvidenceRef string
    HTTPStatus int
}
type NativeRetryAuthority interface {
    NativeRetryWindowMillis() int64
    VerifyNativeRoutes(context.Context, RuntimeRef, agentbackend.ExecutionHandle,
        NativeRoutingPolicy) ([]NativeRouteProof, error)
    CertifyNativeRetryEffects(context.Context, NativeEffectRequest) (NativeEffectProof, error)
    CertifyNativeRetryFailure(context.Context, NativeFailureRequest) (NativeFailureProof, error)
    NativeRetryHandler
}
```

These are trusted host composition ports, not HTTP/model assertions. Branch is
the exact bounded UTF-8 JSON array produced from the independently reopened
linear public branch; BranchSHA256 hashes those exact transmitted bytes (no
second canonical serializer). P3 validates its original user/entry/parent chain
and complete current worker prefix, and validates each echoed Binding/Target.
Oversized, changed, missing or non-linear history holds; do not truncate it to
claim completeness. Failure Entry must be the exact failed entry in that branch.
No argument/error bodies or credentials are persisted as diagnostic evidence.

**Native SDK recovery omission; technically accepted for the finite
current-original core boundary only.** Architect0 records acceptance in canonical
design.md:2149 (lead reports `62e45ab9` and `688e05d9`), with the B1/production
limit below retained. Owner1 confirmed the private nativeRetryPrefix receiver
fits the current core window without a public type or file-ownership collision. The
current core's blanket native-prefix rejection of context_edit blocks the
pinned SDK's own omission of an empty failed assistant. Owner1 confirms the
actual source is `_handlePostAgentRun`: it takes and clears `_lastAssistantMessage`,
returns for abort/missing message, and calls `_prepareRetry` only for a retryable
message. `_prepareRetry` emits its sole `auto_retry_start` before
`_omitRecoveryAttempt`, without an intervening await. Omission uses public
appendContextEdit(targetId,null), then emits generic entry_appended. Public
message_end occurs before appendMessage, so its callback cannot assume that the
failed entry is already persisted. These are source facts, not an existing
provenance certificate; entry_appended alone has several other emitters.

Permit the following exception only in the NEW native retry prefix reader;
ordinary B1 linearEntries and owner5's SDK leaf stay unchanged:

1. The exact app/Pi/native-module proof must cover the actual worker construction,
   trusted listener set and this observation code. Production runWorker has no
   caller options; its loader disables external extensions/skills/templates/themes,
   installs only the owned linear/ToolPolicy extension and binds no caller
   extensions. Compaction/cache warming are disabled; admitted factories/listeners
   cannot mutate history, emit SDK events or introduce reentrant history writes.
   An unproved construction or extra history-capable listener makes this exception
   unavailable. Fixture injection proves only that explicitly tested construction.
2. Capture the live assistant object and immutable content/stream observations
   at message_end under the exact active original input. At auto_retry_start,
   associate that object with exactly one already persisted current failed
   assistant after the original user, by complete public message equality and
   captured stream identity. Duplicate/ambiguous association refuses. Require an
   empty error with no text/thinking/tool output, including earlier streamed output
   later removed, and no associated tool result. Earlier completed tool prefixes
   remain intact. Event errorMessage/attempt fields confer no provider-failure,
   effect, retry-budget or route authority.
3. Synchronously capture the complete raw public prefix and leaf, then arm a
   one-use observation token bound to that input/worker/message/target. Schedule
   its invalidation at the first microtask; do not await or call foreign code
   while arming/consuming it. Only the immediately following matching append may
   consume it: one exact context_edit entry with explicit replacement:null,
   targetId equal to that failed entry, parentId equal to the captured leaf, a
   fresh unique ID, and full manager history equal to the captured prefix plus
   precisely that entry. Check the exact supported public entry fields, including
   timestamp. Another append, unmatched/duplicate/reentrant event, missing edit,
   expired token or changed input invalidates permission and holds the original.
   No shape-only persisted edit can create a token. The trusted synchronous SDK
   emit-to-append sequence and closed construction supply provenance together.
4. Keep only the consumed omission tuples in the current memory-only original
   arm, bounded by the existing complete-prefix/frame limits. Each prefix read
   still independently reopens the public session and compares every raw entry,
   ID/parent and leaf with memory; preserve Branch bytes and their existing hash.
   Every context_edit must correspond exactly once to a consumed tuple in raw
   append order. Targets must be distinct empty failed assistants of this original
   input. Nonnull/missing replacement, user/prior-input edits, toolResult/custom
   targets, paired results, branch summaries and unobserved edits hold. Clear the
   tuples on original retirement, worker/attachment loss or restart; never rebuild
   them from disk. Historical omissions without this live original witness remain
   unavailable, including on a later original input even if the earlier input
   positively settled in this process. No prior-input witness cache is retained.
   P3 neither appends edits nor restores omitted context.

The smallest receiver extension is PRIVATE to the existing correlated
native_retry_prefix worker request/reply. Retain its exact Binding and Branch,
and add an explicit nonnull RecoveryOmissions array whose strict elements are
`{EditEntryID, FailedEntryID, ParentEntryID}` (exported-Go casing). Use [] when
there are no edits. This is a worker attestation of the consumed live tokens,
bound by the existing entire original Input/Runtime/Handle/user/leaf/BranchSHA256
and exact worker identity; it is not model or host-authority input. Supervisor
independently validates that binding, full raw history/hash, original Accepted
witness, each strict null edit/target/parent and the exact bijection with the
array. Keep this typed observation alongside the prefix through native validation
and recheck it in the fresh same-worker prefix observation before charge. A copy
from another worker/input, missing array or changed observation refuses. Structural
validation alone cannot substitute for the proved worker observer/source.

Strip RecoveryOmissions when projecting the unchanged NativeEffectRequest to
the existing effects frame/authority and SDK leaf; no exported authority type,
SDK wire shape, fifth purpose, receipt/record schema or persistent ledger changes.
The full raw Branch still includes the omitted failed message and edit. Existing
failure provenance, positive prior-effect completion, current route proof,
activity/deadline and cumulative-charge gates remain independent and mandatory.
Known retryable text or an SDK omission never grants a route.

**Known consumer limit, not production readiness.** Owner1 confirms unchanged B1
HostBridge.verify/inspectOrigin and InspectNativeOrigin read the entire raw
history through linearEntries. After any such omission they still refuse that
history, including after an otherwise successful explicit physical reset.
Ordinary physical model execution is independent; B1 callback/origin admission
on that edited history is not proved available. The finite first-original
read/tool case does not exercise B1. This clause grants no post-hop B1 or
next-input retry readiness and supplies no history repair. Any production
requirement for those consumers needs a separately accepted owning solution;
do not broaden B1 or retain cross-input provenance within this correction.

Owner1's existing native host-bridge/receiver/test window owns the correction
after canonical acceptance; no B1 or owner5 file allocation is implied. Smallest
cases: actual pinned empty-error event sequence retains one original user and
earlier completed tool; arbitrary identical-shape edit without token, append after
a microtask, intervening/duplicate append, ambiguous message, old input/worker,
missing/null/extra/mismatched tuples, nonnull replacement and partial/tool/result
targets all hold. Confirm raw reopen/hash equality and that unmodified B1 still
rejects context_edit. Reuse the existing finite component case after focused
receiver checks; its fake route/effect authority remains explicit. No check or
production activation is claimed by this declaration.

**Pre-enable route proof transport.** Technically accepted by architect0 and
recorded in canonical `design.md`; this fits the released native core without
additional allocation. Actual route evidence and activation gates remain required.
VerifyNativeRoutes runs before an original
input exists, on Manager's live locally attached authority; it is not a fifth
native_retry purpose. Manager retains the negotiated NativeRetryAuthority and
exact attachment identity only while that AttachHost connection is alive. Add
one private, transient projection (exported field spelling on the private wire):

```go
type nativeRouteAdmission struct {
    AttachmentID string
    RoutingRevision uint64
    Policy NativeRoutingPolicy
    Routes []NativeRouteProof
}
```

The existing private ConfigureNativeRouting body carries its public `Request`
plus `RouteAdmission *nativeRouteAdmission`; Runtime/Handle remain bound by the
existing control request. For virtual mode, Manager captures the current
authority/attachment and a deep copy of the full requested policy, releases its
lock, calls VerifyNativeRoutes outside c.mu/receipt/attachment locks, and then
checks that the same attachment is still live before sending. Supervisor checks
that exact current attachment under its ordinary serialization;
admission.RoutingRevision equals Request.Revision and admission.Policy
must equal the entire requested policy, not just its digest. Require exactly one
proof per ordered target, no missing/duplicate/extra route, and the original
target/account plus actual immutable AppStorePath/PiPackage/adapter identity,
current settings/policy/generation and retry-disable/failure-source requirements.
Recheck attachment liveness before pending publication/native mutation; loss
after effects begin follows pending/Unknown, never optimistic rollback. Proofs
are not written to mapping, receipt, package metadata or a separate store.

Physical reset omits RouteAdmission and rejects a supplied one; disabling
fallback does not require an unavailable routing authority or route proof.
All ordinary idle/hold/pending/current-settings guards still apply. An exact
virtual Configure replay requires fresh live route admission too.

Cold virtual Load uses the same Manager helper against the positively recorded
saved policy obtained through the existing optional InspectNativeRouting read;
RouteAdmission.RoutingRevision is that recorded state revision, and the private
Load body gains optional RouteAdmission. Inspection does not load,
register or mutate. Supervisor compares the full saved state/policy/revision
under its load serialization before creating/restoring the worker; missing,
stale or changed admission holds before virtual restoration. Physical/legacy
Load omits that arm and retains existing behavior. Pending/held saved state
cannot use this preflight to resume. The new strict body arms are sent only to
the exact native-routing-capable package; old peer behavior stays unchanged.
Read-only inspection without live authority may report recorded state, never
verified execution permission. Fresh input/each final retry still revalidates
its live authority and route source; Configure/Load admission is not a permanent
certificate or permission to invent an original NativeRetryInput.

This is owner1's bounded private Manager/control transport seam within the
released native core. It changes neither the public Configure/Load APIs nor the
four input-bound purposes below. Focused fakes must cover stale attachment during
preflight, changed policy/settings before configure/load, absent/duplicate route
proof, and physical reset without authority. No real-route proof is supplied by
this declaration; exact adapter evidence remains mandatory.

**Attachment/version ordering; technically accepted by architect0.** Initial
AttachHost precedes Create so that worker tool factories are available. After
both independent Manager/supervisor package guards pass, the optional attachment
advertisement `nativeRetry:{schema:1,windowMillis:N}` is negotiation intent only;
it requires no existing worker and grants no writer or execution permission.
Use that same attachment after Create; no B1-only attachment/reconnect cycle.
Absent guard or authority omits native negotiation and preserves B1 behavior.

Before Configure's first conversion, pending/routing-state publication or native
selection effect, query the exact actual worker's read-only `version` operation
and require `nativeRetry:1`. That capability includes the conditional-expiry
command and strict native request arms; it does not certify route/effect proof.
The same version operation may run after init only after ordinary exact worker
identity validation, without an SDK call, input, setting or tool mutation.
Recheck exact worker identity/generation after the version reply before those
changes. Missing/unequal/malformed version or replaced process/generation refuses.
Advertisement, package metadata and another worker's reply are
not substitutes.

For cold Load, keep the existing conservative load-intent bookkeeping before
spawn (`Loaded=true`, current Generation, zero PID/start), under the current
package guard and ordinary load checks. This required recovery write changes
no routing policy/revision/selection and grants no native permission. The newly
spawned exact process must answer pre-init version before session initialization,
history restoration or virtual registration. Missing capability stops before
init and retains the existing failed/uncertain-load hold; do not roll back the
ownership prewrite or automatically launch a replacement. Do not reorder spawn
ahead of that existing recovery write just to obtain a version reply. Successful
version still requires all saved-policy, route, account, pending/hold and native
restoration checks before exposing operations. Schema1/2 and utility2 creation
retain their existing ordering; no native-routing capability is inferred for them.
Focused fakes cover attach-before-Create, stale post-init worker identity, cold
pre-init refusal with no init/history/tool/model effects beyond owned spawn/version,
unchanged routing state and preserved load hold.

Unknown capability/arm refuses before enabling virtual execution. Extend the
existing bounded worker/control framing with a **distinct** `native_retry`
request/result arm and purpose `admit|effects|failure|retry`; bind original input,
current runtime/generation, attachment, correlation and deadline. Reuse B1's
correlation/cancellation mechanism, not its Tool/HostCall fields or timeout.
Each purpose carries its corresponding typed request/reply (admit uses
NativeRetryInput; retry uses the existing NativeRetryRequest). The private
host-reply route-proof wrappers below are stripped before delivery to the leaf.
Strict one-of decoding rejects mixed host-tool/native-retry bodies. Old peers
never receive these arms. No second ledger or retry service is introduced.

**Fresh admit/retry route replies; technically accepted by architect0.** Keep
VerifyNativeRoutes on the captured Manager-local authority, with no fifth
purpose. For each original admit and final retry, Manager's internal P3 handler
reads the exact original receipt and full saved/frozen policy, verifies their
agreement with the request, and calls VerifyNativeRoutes outside receipt,
conversation and attachment locks. Do not reuse Configure/Load proofs as this
fresh call's result. Send the newly collected typed proofs to the supervisor in
the existing correlated host native_retry result, using these exact private
purpose-specific body projections (exported-Go field spelling):

```text
admit: {Admission: {Submission, Generation, Accepted, Witness},
        Routes: []NativeRouteProof}
retry: {Decision: NativeRetryDecision, Routes: []NativeRouteProof}
```

Admission is the already-fixed strict admission projection; Witness retains
its existing lower-camel fields. The implementation uses typed private reply
structs, not an untyped metadata map. Mixed purposes, extra wrapper fields, null
Admission/Decision wrappers or a missing/null Routes array refuse. Nested result
fields retain their existing null semantics. Successful admit and Decision.Outcome=allow
require the complete ordered proof array for the full unchanged chain, just as
Configure/Load does; partial proofs cannot grant permission. An unsuccessful
admit uses the existing bounded error/refusal path without a successful payload.
A nonallow stop/held Decision may carry explicit `Routes:[]`, with null Target
and unchanged counters; it grants no routing permission. Transport/error or
proof uncertainty remains held rather than fabricating a stop/allow result.

Supervisor independently checks the current correlated original request,
captured attachment, active arm/worker/generation/deadline, durable Accepted
receipt, full policy/settings/canonical map, and each exact target/app/Pi/adapter/
retry-disable/source proof. The envelope supplies binding to this original
request, so no new public method, proof ID, cache or ledger is required. Recheck
the activity revision and those identities after asynchronous proof collection
and immediately before returning permission. The old configured module proof
or a trusted Manager boolean alone cannot replace these fresh typed checks.
P3 strips Routes and the private Admission/Decision wrapper and forwards only
the existing exact admit result or NativeRetryDecision to the strict SDK leaf.
Effect/failure reply shapes and the leaf remain unchanged. Focused receiver
fixtures cover missing/partial/reordered/wrong-module route proofs, stale
attachment/input/generation after collection, and a valid wrapper producing
exactly the old leaf projection; no new harness or source allocation is implied.

For `admit`, the supervisor waits within the original lifetime for the existing
receipt reader to prove **durable Accepted**, exact original Ref/settings/input,
current saved generation and native witness. It must return the native witness
to the ordinary Send ACK path so that the receipt engine can publish Accepted;
waiting for that publication inside the witness/receipt lock would deadlock.
Use the existing out-of-scanner callback handling and lock-free wait, then
revalidate active arm/worker/attachment immediately before permission. The leaf
admission callback must not acquire `c.mu`: Send holds it through ACK. Capture
the checked identity/settings under that lock at dispatch into the `activeMu`
protected arm; relevant later mutations must invalidate that arm.
The leaf
gets exactly `{Submission,Generation,Accepted,Witness}` with its existing
lower-camel witness fields. NotSubmitted/Unknown, missing receipt, mismatched
witness or lost authority cannot become Accepted from a native user entry.

For `effects`, construct the complete tool prefix from the original user through
the captured leaf: every assistant tool-call identity/name/arguments must have
one exact attributable result, public start/end observation and an authoritative
completion source. Include calls in the failed response when refusing it;
empty text/final success must not erase prior partial output or failed tools.
For host callbacks, verify existing domain receipts by the B1 immutable
input/assistant-anchor/toolCallID/action/arguments binding. A returned JSON body,
empty pending map or tool_execution_end event alone is insufficient. For local
tools, use their actual owned execution/exit/completion evidence; untracked bash
children, background work, external operations without a completion verifier or
unknown result association hold this retry path. Never infer exactly-once side
effects from a matching transcript.

Combine that positive prefix proof with current refusal inputs: callbackCount,
callbackUnknown, hostBridge.pending, tool-policy activeCalls, original receipt
holds and exact child/resource records. Running/unknown/unattributed resources
cannot be certified clear; an unprovable association conservatively holds.
The empty-prefix case still needs a complete verified inventory of the enabled
tool/callback/resource surfaces and no in-flight work; empty counters alone do
not suffice. Existing domain owners implement their read-only verifier adapters;
P3 aggregates them, with no generic effect framework/registry. Unsupported tools
may remain usable for ordinary execution, but cannot acquire fallback proof.

The final `PrepareNativeRetry` gate independently rechecks Accepted, live arm,
current generation, policy/settings/account map, complete unchanged prefix,
route/failure certificates and no pending effects before invoking PlanNativeRetry.
The worker serializes route/charge with its original turn; hold permission across
neither an awaited handler nor a receipt/scanner lock. Any effect/attachment/run
change invalidates the certificate and cancels this permission. Revalidate before
return; the leaf independently compares the entire branch again before charge.
Use an in-memory activity revision on the active arm, incremented for relevant
tool/callback/resource starts, completions and uncertainty; capture/recheck it
around asynchronous proof collection. It detects concurrent change, never proves
completion or replaces domain evidence, and is not persisted as another ledger.
Completed earlier tools remain in context and are never rerun. Project only the
two exact boolean fields into certifyEffects' return; additional host binding
fields are not passed through to the strict SDK leaf.

**Physical routes and conservative results.** VerifyNativeRoutes must cover the
entire frozen chain and actual canonical account map against the exact selected
application/Pi package and adapter code. A positive proof requires both disabled
provider/transport retries and a known structured failure source correlated to
the actual physical request/response and failed entry. Code/module evidence and
actual request options must agree. Global maxRetries=0, model existence,
api!=pi-virtual, catalog availability or a nonempty evidence string alone prove
none of this. CertifyNativeRetryFailure consumes that route-bound adapter source;
it cannot parse arbitrary error text or manufacture a provenance reference.
The SDK leaf receives only its four existing failure fields. Allowed pairs
remain enabled rate_limit/rate_limit_exceeded/429 or overload/overloaded/503;
quota/auth/storage/policy/context/transport ambiguity and partial/paired effects
never qualify. Positive nonretryable/disabled/exhausted is stop; missing,
unsupported, stale or uncertain proof is held/unavailable. No host redispatch,
new input ID, budget reset, refund or automatic recovery follows either outcome.
**No real physical route has this proof in aec5bea**; each remains unavailable
for automatic fallback until its narrow adapter evidence exists. Ordinary
verified physical-provider execution remains independent.

**Ownership and smallest checks.** Under lead source allocation `da705a16`, owner1 owns
`piruntime/native_retry{,_types,_test}.go`, conversation/worker/callback transport
and session/protocol registration, plus the schema-3 writer window already
accepted. Owner5 retains the accepted SDK leaf and provider pure compiler;
any required leaf correction needs an explicit disjoint allocation. Existing
host domain handlers own their completion adapters; central composition and
P2/P7 capability guards retain their assigned owners. This records the lead's
core source allocation, not an adapter allocation or a claim those adapters exist.
If a later P2 schema-3 guard concretely needs an inventory/decoder export,
owner1 and owner2 coordinate the smallest P3-owned strict observational reader;
any consequential contract amendment returns to the lead. No parallel parser
or additional source allocation is implied.

The smallest new P3 fake test must show the original dispatch closure freezes
one full ref/deadline and duplicates/lost ACK cannot rearm it; admission waits
without blocking native witness/Accepted publication. Add bounded cases for
mismatched ref/settings/generation, settled/restarted/expired arm, wall-clock
rollback, expiry during an already dispatched stream, disconnection and stale
settlement; no extra prompt/provider route or receipt mutation is allowed.
Inject a delayed stale/duplicate expiry after old-input settlement and a
positively admitted successor (independently testing the worker fence):
the worker must return no_effect without touching the successor. Race matching
expiry with new admission: setting held before the first await must exclude the
new input. Missing expiry ACK leaves the original arm held, never replaced.
Effect fixtures require one positively completed tool/callback prefix plus
negative missing/duplicate/unmatched/partial/tool/background/resource/Unknown
proofs. Route fixtures bind the exact frozen target/code/request and reject
hidden retries or unsupported failure provenance. Finally bridge the accepted
finite SDK fixture to the **actual P3 persisted receipt and authority adapter**,
retaining one user/ref/digest and cumulative charge. Reuse its SDK-only evidence;
do not rerun an unchanged broad batch. Begin with focused Nix Go fakes; the
finite cross-process check follows in its separately released owner window,
with a fresh watcher if its duration is uncertain. First unsafe allowance,
renewed deadline, unmatched proof or unproved route stops activation and reports
the exact missing proof. No implementation/check was run for this declaration.

## Ownership, acceptance and remaining gates

| Source owner after lead allocation | Deliverable / dependency / checks |
| --- | --- |
| implementer5 | New `portal/internal/piproviders/` types/catalog/policy/store/resolver/Apply/planner and focused tests; new `docs/pi-providers.md`. Source release uses fake Configurer and trusted fake catalog; no P3 core or worker entrypoint edits. |
| implementer1 / P3 | Existing EffectiveSettings/Configure implementation, private settings and worker account/provider injection, native receipt/dispatch evidence. P4 supplies requirements and fixture inputs; any later `pi-runtime/src/providers/` implementation needs an explicit disjoint ownership window. |
| implementer2 / central integration | Resolver/admission, provider controls/view projection and calls into P4/P3. Existing Codex branches remain unchanged. No Pi public operation advertised until real support/admission is present. |
| P7 owner | Catalog/config composition and check/doc-index wiring, without machine credential paths in package manifests. Existing flake/Go/vendor ownership retained. |

Quick fake tests cover inherited default/override/clear, incarnation mismatch,
unrelated-member digest stability, CAS conflict, malformed/unknown storage,
missing/duplicate route/account, unsupported thinking/Daybreak, budget bounds
and cycles. Fake Configure proves one call, stale/same revision semantics,
busy/held/refused/partial outcomes and no false rollback. Planner tests prove
Accepted/Unknown/effects/text refusal never select executable replay; only exact
NotSubmitted/no-effect evidence yields a non-executing candidate. Views distinguish
requested/effective/actual and omit private config/auth references.
Pair/map fixtures cover empty-current/revision-zero Apply refusal, unchanged pair,
changing exactly one component refusal, validated two-component switch, missing
old/new frozen-map pair, noninitial eligible provider inclusion, unrelated
unverified route exclusion, and unchanged all-chain policy refusal/digests.

Run focused `go test -mod=readonly ./internal/piproviders` from D `portal/` in
its Nix environment, with P3 contract tests when that dependency changes. Later
fake SDK tests, in the P3 owner's window, prove `setModel(...,{persist:false})`,
member-local thinking, configured auth-directory locks/replacement and unchanged
history/global settings. Real adapter/installed tests follow committed-deliverable
review and use the monitoring skill when long/uncertain. No live account/model
check, deployment, merge or lifecycle action is implied.

**Remaining exact gates:** P3 actual Configure/settings publication and startup
account mapping; package/runtime config injection for each supported provider;
route-specific account/model availability (Daybreak stays unverified/unavailable);
and proved execution of the separately accepted fallback input/effect/cumulative
native-budget contract. Its bounded source-backed fixture candidate is not
activation proof. Pure
policy/settings coordination does not wait for those unrelated live proofs.
Retain old policy/receipt readers on compatible forward updates; malformed or
unsupported Pi state refuses, never falls through to Codex or resets defaults.

## Evidence inspected

Reused [main plan](implementation-plan.md), [P3 current brief](design.md),
[provider evidence](provider-fallback-evidence.md) and
[shared-auth evidence](authentication-evidence.md). Focused source checks at
Pi `a22b888a58fe55b668cc45b80749ec88d4eb4ddc`:
`agent-session.ts:2657` checks auth/appends model change and persists global
defaults only when requested, without a busy guard; `model-runtime.ts:218`
accepts explicit auth/models paths and gates network catalog refresh;
`docs/virtual-models.md:63–108` distinguishes physical routing/branch state;
`ai/src/utils/retry.ts` establishes text-based native retry limits, not safe
host admission proof. D base `6587c4c1cedabee95bcc52f4667e7d33e3a82859`
`codexproviders/catalog.go` and `web/provider_models.go` are Codex-specific and
remain untouched. P3 types were read from its in-progress same-session source,
then confirmed directly with implementer1; no committed-P3 verification claim.
