# Per-member providers and bounded fallback evidence

Package I, implementer5, 2026-11-11. Source-only investigation for architect0;
no application edits, installation, credentials, model calls, deployment or
lifecycle actions. This is the first assigned/executing package. Session binding
and both environment values match; same-session roster confirms implementer5 and
architect0 with workspace-write access. Lead owns acceptance and plan/state;
architect0 owns design synthesis. Read alongside [Pi evidence](pi-capabilities-evidence.md),
[current host evidence](current-runtime-evidence.md) and [design](design.md).

## Decisive result

Pi supports separate provider/model selections per AgentSession and same-history
switches. It also has a **native virtual-model routing extension point** that can
select another physical provider on an automatic retry. It does not supply the
requested cybersec classifier or an operator-configured ordered failover policy.
In particular, a route callback receiving `reason: "retry"` does **not** mean
every content/provider failure initiates a retry. The actual reported error and
the user's subscription/Daybreak entitlement remain unverified.

The requested product shape is feasible as host policy: inherited session
default plus explicit member override, each resolving to a primary and ordered
fallback provider/account/model chain. A member's switch must stay local to that
member; it must not mutate a shared pool or global default. All providers remain
in the same development-session cgroup/namespace. Provider choice changes the
network destination/account and available model capabilities, not tool authority.

## Native capabilities and their limits

All Pi links bind **a22b888a58fe55b668cc45b80749ec88d4eb4ddc** (main, not a claim
that all behavior ships in v1.5.2). Official pinned SDK implementation/docs and
the existing host provider guide are the evidence; no ecosystem survey ran.

| Boundary | Source-supported fact | Host implication |
| --- | --- | --- |
| Per-session model | SDK options accept `model`, `thinkingLevel`, `modelRuntime`, `sessionManager` and `settingsManager`. Defaults create a ModelRuntime using agentDir auth/models files. [SDK source][sdk] | Model/history selection is per AgentSession. Authentication isolation is a separate explicit choice: default sessions may share the same auth file. |
| Change selection | `setModel` checks configured auth, updates that agent's model, appends `model_change`, and adjusts thinking. Global defaults change only with `persist: true`. It has no busy-state guard. [setModel][setmodel] | Use session-local mutation; serialize managed switches against member dispatch. Changing selection does not cancel an already-issued provider request or tool. |
| Native routing | Virtual models run `route` before each request; receive user/continuation/retry/direct reason, previous physical model, failed response when present, and branch state. Targets must be physical catalog models with configured auth; virtual-to-virtual targets are rejected. [Routing docs][routing], [resolver][resolve] | A host-authored callback can express bounded fallback. This is native routing machinery with custom policy, not a built-in general failover service. |
| Persistence | Selected virtual model and level are transcript entries; each assistant message names dispatched physical provider/model/effort. Returned JSON routing state persists on the branch before dispatch, survives compaction, and follows forks. `direct` requests have no retained router state. [Routing docs][routing], [request projection][projection] | Useful attribution and switch-state building blocks. They do not prove atomic host input admission, switch completion, or exactly-once external effects. Missing virtual registration on resume can fall back to the last physical model; validate host policy before dispatch. |
| Existing host | Current dev-workspace provider schema selects a provider for the entire development session, including retained members, with workspace inheritance. Trusted catalog IDs map endpoints/token files; target catalog is preflighted. [Host guide][host] | Member override/fallback is a new explicit host contract, not current behavior. Keep trusted endpoint/catalog/account mapping and old operation recovery. |

## Retry initiation and error classification

`_handlePostAgentRun()` calls `_prepareRetry()` only when `_isRetryableError()`
accepts the response. Context overflow takes a separate compaction path; other
errors go through `isRetryableAssistantError()`, which requires
`stopReason === "error"`, an `errorMessage`, a matching transient-error regex,
and no matching nonretryable quota/billing pattern. Settings must enable retry
and leave budget. Retries use bounded exponential backoff. [Post-run gate][postrun],
[classifier and budget][retry].

Therefore a cybersec/content error reaches `route(reason: "retry")` **only if
the actual normalized error passes that gate**, or a separate supported host
continuation path is deliberately designed. A router alone cannot initiate the
retry. There is no verified general native cybersec failover trigger here.

| Observed category | Evidence / consequence for the requested policy |
| --- | --- |
| Transport, overload, transient provider response | Built-in error-text classifier recognizes many such errors. A bounded native retry can call the custom router with the failed response. Preserve original provider/category and attempts. |
| Auth, token refresh, unavailable model, subscription quota | Distinct causes; do not label them cybersec errors. `ModelsError` distinguishes auth versus OAuth refresh; quota/billing patterns may explicitly suppress retry. Auth checks show configuration, not successful entitlement. [Auth resolution][authresolve], [retry][retry] |
| Structured content/policy error | OpenAI `response.failed` code/message and incomplete reason are normalized into an error string; `rawStopReason` retains status. Generic AssistantMessage has no mandatory typed cybersec-error field. Adapter response/stream hooks can observe supported raw events, but a classifier is outside this package. [Normalization][normalization], [message/hooks types][types] |
| Model text refusal | OpenAI `response.refusal.delta` becomes ordinary `text_delta`. Plain assistant refusal text is not a failed transport request and does not by itself trigger native retry. [Normalization][normalization] |
| Unclear or conflicting signal | Preserve an unknown classification and stop/escalate under host policy. A regex match on flattened text is not proof of a provider's policy category. Do not invent success or silently treat any refusal as a transport failure. |

This is backend capability assessment, not implementation of ways around
provider policy. An exact nonsecret provider error code/shape and the intended
provider/account/model matrix are later acceptance inputs.

## Credential/account isolation

`AuthStorage` is a map keyed by **provider ID**, not member or account ID. It can
use separate paths or a supplied CredentialStore through ModelRuntime. File
writes use a shared lock; OAuth refresh rechecks the latest value under that
store's lock and persists a rotated credential before release. Cancellation
after refresh starts cannot discard the rotated token. Stored auth owns the
provider; refresh failure does not silently select an environment credential.
[Store][store], [refresh/auth resolution][authresolve], [runtime construction][runtime].

Sharing the same authoritative store/key for the same account supports coordinated
refresh among sessions. It also intentionally shares login/logout/account state;
it is not credential isolation. Two different accounts under the same provider
ID cannot occupy one ordinary auth-file slot. They need explicit account-bound
store views or separate stores/runtimes. UI aliases do not create account slots.
Copying one OAuth credential into independently refreshed alias keys/files is
not proven safe: refresh-token rotation can make the copies stale even though
individual file writes are locked. Keep one refresh authority per actual account;
validate any alias mapping and auth handler rather than copying tokens.

Separate AgentSessions can use separate ModelRuntime instances or scoped views
over a shared account service. Sharing a mutable ModelRuntime also shares its
registered providers/catalog/routing definitions; do not implement a member
switch by changing a shared provider's endpoint or auth. None of these logical
separations supplies an OS security boundary inside the shared cgroup/namespace.

OpenAI's native `openai` factory offers API-key and ChatGPT OAuth paths; the
separate `openai-codex` factory offers subscription OAuth. This proves mechanisms,
not access for the user's account or Daybreak. [Factories][openai], [Codex factory][codex].
“Snajpa codex-lb” and “Daybreak is subscription-only” remain user-provided labels
and availability statements, without verified canonical provider/model IDs here.
Represent role intent (tools, context, input, reasoning and task capability)
separately from a concrete provider/account/model binding. A subscription-only
model should be offered only on the verified subscription binding; do not claim
the same model exists through every provider or silently choose an equivalent.

## Switch boundary, history and effects

For explicit selection changes, use a settled member boundary and freeze new host
dispatch while deciding/applying the switch. `agent_end` can precede retry,
compaction and queued continuation. `agent_settled` is closer to final idle;
neither proves completion of an external tool or delivery receipt. Native queues
can drain before settlement; host coordination must preserve their order and
accepted identities rather than clear and recreate them. SDK queues are not a
proven durable submission store. [Settlement][settlement], [post-run][postrun].

Native retry routing operates at the next model-request boundary, after the
previous request failed; it need not rebuild the conversation. Keep partial
output and its failed-attempt attribution visible. Pi's model projection skips
error/aborted assistant messages, drops other-model reasoning/signatures,
normalizes tool IDs and retains usable text/tool history. Unsupported images
become placeholders; orphaned tool calls can get synthetic **error** results
`No result provided`. These are context adaptation, not proof that a tool failed
without side effects. [Projection transforms][transforms].

Preserve completed tool results and uncertain effects across fallback. Never
replay a tool merely because the next provider did not see a complete reply.
Reconcile interrupted effects using the original operation identity; do not
resubmit an accepted user prompt as a new input or announce completion from a
model answer alone. Cross-model continuity does not preserve hidden reasoning
or prompt cache, and thinking is clamped to the target's supported levels.

Proposed host receipt: bind session/member incarnation, input and switch IDs,
policy revision and ordered-chain position, old/new provider/account reference,
canonical model and requested/effective thinking, observed error category/code
with uncertainty, transcript cursor and effect-reconciliation state, attempt
counts, and prepared/applied/verified/failed/unknown outcome. Store no secrets or
raw sensitive error bodies. Native model/state entries aid reconciliation but
are not an atomic host switch receipt. Preserve existing durable-admission
blockers identified in design.md; this evidence does not resolve them.

Use one finite policy budget across provider transport retries, agent retries
and fallback hops: otherwise multiplied retries increase latency/cost and can
repeatedly expose the history to providers. No chain cycles or recursive virtual
targets; any classifier/summary model request also consumes cost and needs an
explicit direct-request policy. Keep the actually used provider/model and reason
visible. These bounds follow concrete runtime behavior, not a new approval gate.

## Evidence and handoff

Investigation began 22:43 UTC and stayed within the assigned six-active-minute
cap. Fresh official pinned source copies: `/tmp/pi-provider-evidence-2026-11-11-implementer5`
(disposable). Checks were source/path/link and owned diff checks only; no runtime
acceptance or entitlement was tested. Only this artifact changed; no commits,
branches, migrations or application edits. Routine evidence does not trigger
automatic independent change review. Next dependency: architect0 synthesis and
lead acceptance; any implementation/prototype needs a separate assignment.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

[sdk]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/sdk.ts#L48
[setmodel]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2657
[routing]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/docs/virtual-models.md
[resolve]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/model-runtime.ts#L1032
[projection]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L850
[postrun]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L2061
[retry]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/utils/retry.ts
[normalization]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/api/openai-responses-shared.ts#L717
[types]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/types.ts#L224
[store]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/auth-storage.ts
[authresolve]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/auth/resolve.ts#L106
[runtime]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/model-runtime.ts#L219
[openai]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/openai.ts
[codex]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/providers/openai-codex.ts
[settlement]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/coding-agent/src/core/agent-session.ts#L1141
[transforms]: https://github.com/earendil-works/pi/blob/a22b888a58fe55b668cc45b80749ec88d4eb4ddc/packages/ai/src/api/transform-messages.ts#L103
[host]: https://github.com/aither64/dev-workspace/blob/6587c4c1cedabee95bcc52f4667e7d33e3a82859/docs/codex-providers.md
