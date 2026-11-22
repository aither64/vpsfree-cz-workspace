# P6-B2 policy and Plan integration evidence

Owner implementer4. Prior P6-A accepted at
`9a4f44e9c64106bc36d65fead1be881412c778c3`; this is the separately released B2
package. Binding/current/env and live retained Sol/xhigh/workspace_write roster
verified. Required unchanged guidance and documentation skill reused; owning
repository AGENTS read. No real credentials/models, services, lifecycle,
activation, deployment or default integration.

Latest accepted source checkpoint: native P6 component fixture committed at
`94b4d58480d7545dfd8ddda02872b6e536c42f24`, parent
`4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`. Exactly three test paths/370 insertions,
unchanged tested hashes, index empty/owned paths clean, sole window closed and
fake-worker staging returned to implementer1. Receipt:
`tmp/p6-native-commit-receipt.json`. No push or central/installed readiness claim.
Lead accepted this exact checkpoint, source/check receipts and closed window.
Current capacity boundary: assigned P6 source and native component evidence are
complete at the accepted checkpoints. Full B2 remains unfinished pending P2-owned
central permission/retained-state guard/coherent observation composition and
lead-sequenced installed-flow proof. Implementer4 retains P6 technical/review
fixes and capacity for a released integration continuation; no next package is
queued. Own commands and both native fixture watchers are terminal, with no
owned index window or repository/machine claim. No new source, SDK check,
harness or lifecycle action is started by this handoff.

Current functional milestone: the joint runtime/supervisor policy source is
accepted in `4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`, including the two owned
private policy method/test files. The new focused native P6 domain fixture passes
in2.784s against that committed core plus exactly three test overlays, ready for
its later source checkpoint. Central authority/guard/observation composition and
installed proof remain required; no live capability is inferred. This supersedes
the earlier blocked private-source notes below.

The first API/native policy unit is committed at
`fa43219096e3e8b9e5002cb28efccadf73a1a2ce`, parent
`0e8c0fb5b1357a3810df9f35b1dfe040a874fa41`. The lead's sole index window is
closed. Exactly four new files and their unchanged hashes below were staged,
committed and compared with current source; index empty and owned paths clean.
Normal `git commit -F` ran in the immutable repository Nix environment. Receipt:
`tmp/p6-b2-api-commit-receipt.json`. No push, core field/supervisor integration,
dependent Plan/origin adapter or docs commit, migration or capability claim.
The complete B2 package remains executing.

The independent28file domain/manual/native-origin checkpoint is now committed
at `74c5646455e1e40f03732347c5eb567dd90d8fbc`, parent
`e4b9f861f14c5f6fa803c320e4e66e71cca866f4`. Lead accepted this exact checkpoint and
its evidence; functional/native/central gates remain separate. Exact16new/12modified paths and all
staged/committed/current hashes match `tmp/p6-b2-domain-checkpoint.json`; complete
commit receipt is `tmp/p6-b2-domain-commit-receipt.json`. Normal commit-F/Nix,
index empty, owned28 clean, window closed. Both private policy files and all
peer source are excluded/preserved. Retention-only parent advancement leaves
the checked committed exported dependencies unchanged. No rerun, push, migration
or live capability is implied; private supervisor/core/E2E integration continues.

## Executing source and settled contracts

Own new `piruntime/tool_policy.go` and tests; `src/tool-policy.mjs` and pinned SDK
tests; concrete `piplan/policy_adapter.go`, pure observation projection/tests;
owned Plan store/service/types sequencing changes and technical docs.
P3 retains every existing conversation/types/worker/protocol/supervisor/session
and schema-2 mapping decoder edit. P2 retains composition/guard/main/app; P7
metadata/packaging. No C change.

Accepted design refinements, recorded by architects in design.md and
pi-host-tools-plan.md:

- Independent tool-policy revision and expected CAS are exact integers
  1..9007199254740991. Overflow change refuses; exact max duplicate may fresh
  verify. Digest excludes revision: SHA256 of compact ordered JSON
  `["pi-tool-policy",1,Mode,Active,RegisteredCeiling]`.
- Names/lists are sorted, unique and bounded. Fixed RegisteredCeiling belongs to
  trusted bootstrap and retained policy for worker lifetime. Mode changes vary
  Active within it; no narrowing/broadening or automatic composition reload.
- Schema2 adds exactly ToolPolicy/PendingToolPolicy, no InitialToolPolicy.
  Initial complete Create is Revision1; exact retry only at unchanged revision1
  with no pending and existing native proof. Greater revision refuses Create
  replay, even a repeated digest; pending/partial setup holds without restart.
- Plan consent token is exact `pi-plan-policy-v1:mode:revision:originalDigest:defaultDigest`,
  five fields, max192 ASCII, canonical decimal and lowerhex digests. Plan targets
  next safe revision; alreadyDefault requires same revision/equal digest.
- Duplicate consent returns before live inspection. Selection/native inspection
  happen under ordinary admission outside the short store lock; atomic capture
  rechecks exact proposal/caller/CAS with invocation-local pure observations.
  No shared FileStore callback swapping. Snapshot/Lookup remain native-free.
- Optional typed immutable observation projection is display only. Full current
  handle/binding, retained policy/proof, eligibility, released domain/guard/tools
  and latest proposal/lineage must match. Missing/invalidated observation hides
  controls. Production P2/P3 refresh/invalidation wiring is REQUIRED and absent,
  not an implemented cache. No poller, TTL or Applied-boolean shortcut.

## Current quick checks

Pinned SDK package `/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2`, upstream
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`; coherent public exports only. Immutable
repository development environment uses D revision
`4f390101de7ca5047d9e41faa0b483088d591185`; tested source is the current owned
working files, not a claim that they exist in that environment commit.

Commands:

```
env PI_PROBE_PACKAGE=/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2 \
  nix develop 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace?rev=4f390101de7ca5047d9e41faa0b483088d591185' \
  --command node --test pi-runtime/src/tool-policy.test.mjs
nix develop 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace?rev=4f390101de7ca5047d9e41faa0b483088d591185' \
  --command go -C portal test -mod=readonly ./internal/piruntime -run TestToolPolicy -count=1
nix develop 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace?rev=4f390101de7ca5047d9e41faa0b483088d591185' \
  --command go -C portal test -mod=readonly ./internal/piplan -count=1
```

Go policy validators passed (0.014s). Full piplan suite passed (0.286s), including
real-inspection outside store lock, duplicate without native call, exact token,
changed composition/overflow refusal, lost Default ACK observed once, original
plan/acceptance/operation/message/receipt, terminal NotSubmitted no resend, and
pure full-proof/invalidation projection without native calls.

Native fixture validates real public SDK active/callable/registered sets and
installed `tool_call` hook, nested refusal, late/deferred tool registration,
Default fake mutator then Plan, fixed ceiling/revision/max and partial Unknown
hold. Uses fake provider and fixture tools; no paid/model service or login.
Latest native run passed 3/3 in1.81s; focused Go policy boundary cases passed
in0.012s, and current full piplan/projection suite passed. These working inputs
are not a standalone committed-build claim. Provisional source hashes follow;
final freeze waits the meaningful P3 parent as lead directed.

- `portal/internal/piruntime/tool_policy.go`: `6752778cb0880e837a7d1b52b852c2dc7b09bf70c0ff32865a1cfba688dff1de`
- `portal/internal/piruntime/tool_policy_test.go`: `e6c93271acddfb71787db3903dc26985c7617da23ca39609d82987e8b314fc7c`
- `pi-runtime/src/tool-policy.mjs`: `94e3c744bf7c5ddca02bf29ad96b0284ad324338b4927449b134729cafab8b77`
- `pi-runtime/src/tool-policy.test.mjs`: `91288386ffc385689a017c621bbc2cc53e421f7f3ac753c5447dc46f55212a35`
- `pi-runtime/src/lineage.mjs`: `f78c91e766e33cbda5432254ef80f392e3ce17241492a860f7ffe1be22ab5673`

Initial uncertain native check used fresh installed Luna/low watcher, package
`/nix/store/9hr3ppqzzwb12x51vwjasw8hq0ka7dab-dev-workspace-0.2.0`, catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`, full access.
It terminated in3s, 1/2 tests passed; log `tmp/b2-sdk-first.log`. Public SDK fixture
fixes: bindExtensions requires `{}`; explicit `tools:[]` filters custom tools too,
so use trusted name ceiling; faux provider context has system messages rather
than `context.systemPrompt`. Focused now-known-fast reruns diagnosed only those
interfaces. Production uses no private monkey patch. A transient P3 worker import
compile issue was left with its owner and later resolved. No command remains
running from those attempts.

## Dependencies, not claimed capabilities

P3 agreed `createToolPolicy(target) -> {extensionFactory,inspect(session,generation),apply(session,target,generation)}`;
worker operations are `tool_policy_inspect`/`tool_policy_apply`, full `toolPolicy`
config, exported Go proof/result field spelling. Native factory consumes P3's
`installLinearGuards`. P3 B1/tagged utility commit must first include that helper;
then the tested policy API/native unit can commit before P3 schema2 integration
uses its types. This dependency checkpoint is now committed as recorded above.

P3 checkpoint is now committed at
`2dd2af9499fa64602bfce94c20a17b6e41139eca`, parent
`563f6be3ae0498c4b4e9d5fffe0c8844f4555e75`. A clean `git archive` of the P3
checkpoint plus only the four unchanged policy files passed all five focused Go
policy/initial-replay tests in0.014s; importing the policy JS module resolved
its actual committed lineage/framing graph successfully. Snapshot:
`tmp/p6-b2-api-2dd.V3g1HR`. This establishes the narrow API unit independently
of dirty Plan/origin/peer files. Pinned SDK enforcement evidence above is reused
for unchanged policy files; no unchanged SDK test was rerun. The committed
lineage module is now `c171adbe3b5ac4568b6fcf55d1cc5d268b2949844f19210ce658e49d3baade04`;
its used `installLinearGuards` event body is unchanged. D declares no hook
framework/core.hooksPath and the canonical hook directory contains sample hooks
only; normal Git hooks remain enabled. The subsequent index grant/commit is
recorded in the current checkpoint above.

P2 confirms piToolPolicy guard/map/old-reader fixture absent from its current
package. No production policy writer/dispatch/initial policy creation is
registered. Required contract is `piToolPolicy:{policy:1,conversationSchema:2}`;
existing sole compatibility hook must inspect retained cold mappings and preserve
schema4 old-candidate fences before writer release.

Remaining execution: P3 exact owned policy field/helper integration; supervisor
pending-before-mutation/positive-durable-completion/Inspect/Load proof and failure
fixtures; real fake-SDK native supervisor-to-Plan acceptance fixture; required
P2/P3 projection invalidation composition; lead prose pass and short index windows;
committed quick checks/evidence and lead final review. No successful stub or
optional interface presence substitutes for those proofs.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-11-pi-codex-migration/>

## Released historical-origin amendment

Lead released the accepted content-aware origin addition within retained B2.
Independent source now includes strict native argument comparators, additive
question Dispatch / Plan Ports VerifyOrigin, admitted question HTTP store and
Proposal-aware Plan capture inspector. No P3 type/interface was duplicated.
Exact original duplicates return before action admission/native checks; receipt
lookup can reconcile with absent origin/effect ports. New capture/Apply/Prepare/
Send requires origin proof outside domain file locks. Pure atomic capture
rechecks immutable selected scope/content, closure/proposal, revision and CAS.

Questions compare exact order/title/options and canonical host indexes, with
only omitted options versus [] equivalent. Strict JSON rejects unknown/null/
duplicate/wrong types and escaped lone surrogates; valid surrogate pairs retain
the same exact code points. Plan requires exact saved text/digest/complete anchor.
Neither comparator claims original raw JSON byte equality or guesses input ID.

Final amended full domain suites passed (questions0.521s / Plan0.416s); focused
web origin/strict HTTP cases passed0.176s. Fixtures include outside-lock inspection,
closure/new-proposal race, missing reader for new effects, duplicate with all
reader/admission ports absent, original receipt lookup without new proof, byte/
order/index/Unicode mutations. No unchanged SDK rerun was performed for this
amendment. First four-file checkpoint remains unchanged and uncommitted awaiting
its named meaningful P3 dependency/window. All commands terminal.

The lead's writing pass on both appended technical sections is closed. No new
prose change is pending.

### Actual runtime origin adapters

Consumed implementer1's actual `piruntime.NativeOriginInspector`,
`NativeOriginRef`, `NativeOriginObservation` and Manager transport export in
working source. New `piquestions/native_origin.go` and `piplan/native_origin.go`
provide `NativeOriginVerifier{Inspector}.Verify` method values for the admitted
store, dispatch and Plan policy/service ports. No duplicate runtime interface,
active-input guess or central registration was added.

The adapters bind the exact unchanged durable conversation, saved tool call,
anchor and selection token while allowing host-resolved current generation.
They check returned handle/ref exactly, then run the strict saved-content
comparator. Missing reader is unavailable; scope/conflict errors refuse. The
saved caller remains unchanged. Host admission remains required around calls.

At working D HEAD `563f6be3ae0498c4b4e9d5fffe0c8844f4555e75`, the focused new
`go -C portal test -mod=readonly ./internal/piquestions ./internal/piplan -run TestNative -count=1`
passed in0.016s per package in the immutable Nix environment above. Fixtures cover
restart generation, wrong durable scope/native ID, forged returned generation/
anchor/token/tool-call/tool, changed/oversized content, incomplete Plan/digest,
missing reader and error propagation. Owned `git diff --check` passed. P3 source
remains uncommitted; this is working-source adapter evidence, not independent
committed buildability. First four-file policy hashes remain unchanged. No SDK
rerun, index mutation or live capability occurred; all commands terminal.

Manual mode selection had no concrete source interface in the earlier brief:
`ModeIntent` only validated a value, and existing Plan HTTP/browser ports handled
acceptance only. Architect2 confirmed this is not covered by the neutral-settings
path and is recording the smallest optional admitted mode adapter/HTTP/browser
contract for architect0 acceptance and lead source release. No provisional mode
token, central route or operation ledger was implemented. This gap does not block
the independent four-file policy checkpoint. Current D HEAD advanced to
`6d2730282d871383dfc56d05143830e29ecfe619` through the seven P2 creation/runtime
composition files; inspected inventory does not change the policy-unit inputs.

## Released manual-mode amendment source milestone

Lead released the architect0-accepted exact manual-mode brief after accepting
the four-file API checkpoint. New `piplan/mode.go` and focused tests implement
the optional ModeSetter/ModeAdapter; existing `web/pi_plan.go`, its new focused
`pi_plan_test.go`, `static/pi-plan.js` and browser fixtures add only the optional
unmounted action/hook. No synthetic Caller, proposal, acceptance token, policy
initialization, receipt/ledger or Codex-settings path was added.

Trusted Admit/Resolve/Eligible/Compose ports supply the exact current handle,
complete policy proof and host-composed target. Expected revision and digest
must match before composition; same-mode full equality is a fresh no-op. Changed
mode uses checked revision+1, the unchanged ceiling and one Apply. Any invoked
Apply error or incomplete/unknown result yields Unknown without Policy, even
when the transport's default result says rejected. A post-Apply admission error
also remains Unknown. Pre-effect scope/conflict/unavailable errors use existing
domain mapping; held remains503.

The HTTP action uses `pi-plan.mode` authorization and exact-origin/strict JSON
helpers. It returns200 applied,409 positive rejected,202 unknown; malformed
positive result is sanitized to Unknown. Missing Modes suppresses CanSelectMode
on GET without native calls. Browser selectMode captures displayed CAS once,
never changes mode optimistically or persists/replays mode requests, and blocks
with shared busy/pending-plan state. Only an explicit post-settlement no-store
refresh with a coherent enabled host observation can clear uncertainty; pushed
updates and delayed pre-request/pre-settlement GETs cannot. The production P2
invalidation/composition dependency remains required and unregistered.

At working HEAD `fa43219096e3e8b9e5002cb28efccadf73a1a2ce`, immutable Nix quick
checks passed:

- `go -C portal test -mod=readonly ./internal/piplan ./internal/web -run 'TestMode|TestPiWorkflow' -count=1`: domain0.110s, web0.144s.
- Additional missing-policy/wrong-scope/generation/callable proof fixture:
  `go -C portal test -mod=readonly ./internal/piplan -run TestModeMissing -count=1`:0.014s.
- `node --test portal/test/pi_workflows_browser_test.cjs`:7/7 in227ms, including
  existing question/Plan behavior and new delayed GET/reconnect/one-POST cases.
- Owned `git diff --check`: clean. All commands terminal; no SDK rerun or staging.

New `docs/pi-questions.md` Manual mode selection section and two new visible JS
strings were sent to lead for the required direct writing pass; those prose spans
are held until that pass closes. The manual/adapters unit has no index grant.
P3 existing fields/config/dispatch remains owner1. Its private retained seam is
confirmed, but no new-file supervisor methods will be appended until its coherent
Schema2 field-ready notice. Full B2/E2E/live guards and observation gates stay open.

## Domain checkpoint and private supervisor continuation

The lead accepted the manual writing pass, changing only exact-origin to
same-origin in that appendix and retaining both visible strings. The requested
independent source checkpoint is frozen as28paths (16new,12modified) in
`tmp/p6-b2-domain-checkpoint.json`, with exact SHA256/status inventory and parent
`1eeecfb575220d7f8d152bc42b6b9e91c77c995b`. Clean archive of that parent plus
only those paths, in `tmp/p6-b2-domain-x66eux_p`, passes selected affected Go
questions0.300s / Plan0.455s / web7.842s and7/7 browser220.6ms. Every current owned
source hash matches the tested copy. Its runtime policy file is the committed
first API version; no private supervisor bodies, schema fields or dirty peer
dependencies enter it. Index remains empty, no grant taken or SDK rerun. This
proves optional ports/adapters with default-refusing composition, not live readiness.

Separately, implementer1 released the actual coherent schema2 field seam. New
private methods are appended only in owned `piruntime/tool_policy.go`:
`s.inspectToolPolicy(ctx,handle)` and
`s.applyToolPolicy(ctx,handle,expectedRevision,target)`. P3 owns invoke/config/
Create/Load/worker integration. Worker calls use full exported proof/result and
direct target bodies. Methods compile against the actual fields; no core file
was edited or stub supplied.

Inspect is observational and never saves, loads, repairs or clears holds. Apply
requires current retained schema2 policy, fixed ceiling/exact CAS, idle native
snapshot, no active callbacks, receipts or uncertain descendants; duplicate
revalidates live proof without Apply. Pending is synced before native mutation;
Applied is synced before ACK. Native uncertainty keeps Pending and holds the
worker. Failed completion restores prior policy plus Pending, attempts its disk
fence and holds; fixture completion-write failure retains the original durable
pending record for cold refusal. No new record/schema/retry is added.

P3's source read found normal live publication must be able to inspect policy
at callbackCount1. The correction now excludes ordinary active callbacks only
from Apply; callbackUnknown remains held in Inspect. The focused regression
proves positive no-write Inspect and no-effect Apply refusal during that callback.

Latest scoped `go -C portal test -mod=readonly ./internal/piruntime -run TestSupervisorToolPolicy -count=1`
passes0.228s in the immutable environment. It covers pending-before-mutation and
durable ACK ordering, lost ACK with fresh Inspect/exact duplicate, no-write/cold
Inspect, unknown/malformed native results, failed completion and cold pending
hold, no retries, schema1/nil unavailable, idle/callback/handler/settings/child
refusals, stale/skipped CAS, changed ceiling and safe max duplicate/overflow.
Initial pure fixture used a non-UUID native ID and failed the real scope validator;
correcting the fixture to the existing UUID contract resolved it without changing
production validation. All commands terminal. These two private policy files are
explicitly excluded from the28file checkpoint and remain uncommitted pending the
joint P3 integration/native proof window.

## Actual native P6 component fixture

The joint18path core commit is accepted at `4c0bd9a0f97c15de76d45e8c5fe54a31ef7afce2`.
After its freeze closed, the new test graph adds only:

- Owned `piruntime/tool_policy_test.go`: a small test-only exported wrapper of
  existing supervisorFixture/attachFixture/waitIdle; no production API edge.
- Owned new `piruntime/p6_plan_integration_test.go`: external Go test package
  imports the actual domains without a runtime/domain import cycle.
- P3-owned `pi-runtime/test/fake-worker.mjs`: exact gated question/Plan response
  branch before its unchanged policy regression branch; staged only by an
  explicitly released owner window.

The fixture uses actual Manager/private Unix callback transport, pinned public
SDK worker, first-party question/Plan factories, historical origin reader and
tool-policy controller with the real domain stores/services. Host admission is
a fixture mutex and pure exact-scope checks; ordinary Prepare/Send/Lookup ports
bind the actual P3 digest and Manager APIs to the same original identities.
These are component fixture ports, not production portal authority/guard wiring.

It proves publication returns a pending question and exact Unicode/CRLF Plan;
normal live callbackCount1 can Inspect applied policy; an answer uses original
historical origin after the publishing turn; its lost ACK reconciles by original
receipt without resending. Plan consent is retained before one real Default
Apply; a deliberately lost mode ACK uses Inspect only. The original implementation
input then loses its ACK and recovers by Lookup only. Exact envelope data,
message/action context, native witness digest and original receipt IDs remain
bound. A scripted fake write runs only after Default; exactly three native user
inputs exist. No model service, credentials, real session mutation or new listener
was used. Existing finite test cleanup owns every fake socket/worker.

First frozen run failed in2.253s at original question Lookup because the test's
receipt helper omitted ActionContext from the existing SendInput digest. Actual
source inspection identified the mismatch; correcting only that helper and its
stored-context assertion passed the cheap compile check. Production validation
was unchanged. The first snapshot and `tmp/p6-native-first.log` are retained.

The corrected97file graph is frozen in `tmp/p6-native-second-inputs.json`, source
snapshot `tmp/p6-native-second-ajjhcjy_`: committed4c core plus exactly the three
test overlays above. Only the external test file differs from the first graph.
Latest source bytes equal the checked graph. The new focused command was:

```
env PI_PROBE_PACKAGE=/nix/store/9hf2a7rz231w2pn50s4jlmrgs4007xc5-pi-1.5.2 \
  nix develop 'git+file:///home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-11-pi-codex-migration/dev-workspace?rev=4f390101de7ca5047d9e41faa0b483088d591185' \
  --command go -C <frozen snapshot>/portal test -mod=readonly ./internal/piruntime \
  -run '^TestP6NativeQuestionAndPlanUseOriginalReceiptsAfterLostAcks$' -count=1 -v
```

PASS2.784s, watcher elapsed7s; log `tmp/p6-native-second.log`. Each uncertain
attempt used a separate fresh Luna/low watcher from installed package9hr/catalog
f2d5a890 with native utility `dw_e792014d07f1ab00a4e052aeb6fbc575674f9dbc9073f569`,
danger-full-access/never policy. Both reported terminal with no operation-owned
sessions remaining. No unchanged SDK/core suite was repeated. Current index is
empty; the later three-file test checkpoint window/staging transfer is requested.
Full B2 central/installed functional acceptance and final review remain open.

## Read-only central-composition clarification

At committed D `3872155b55688742355b8dc16b88584f4cb5a303`, bounded source
inspection for architect2 found three unresolved composition seams: the optional
PolicyObservation carries only ProposalCaller rather than the explicit observed
proposal ID/revision/text digest; no exported validated native-free immutable
Proposal selector exists for its producer; and genuine absence of plans.json
currently suppresses mode-only projection. Architect2 is recording the minimal
typed proposal tuple, LatestProposal read and valid-empty mode projection, plus
the equivalent Questions read for content-aware cached question controls. These
are proposed/released-by-lead continuations, not implemented fixes here.

Exact current handler/controller APIs and ownership were sent directly. The new
standalone UI mount still needs API and Plan-render composition; app.js currently
owns Codex-only optional questions/Plan heuristics. Its generic request helper
throws HTTP409, while mode selection needs a parsed positive rejected ModeResult
distinct from pre-effect conflict. The API shim must preserve that distinction,
forward no-store reads and keep update versus explicit-refresh sequencing. P2
retains central app/server/main/view/permission/cache hooks, P6 existing modules
retain technical ownership, and new standalone-file allocation remains with lead.
No source edits, tests, native calls or expanded inventory were performed for this
clarification; accepted source and capacity boundary remain unchanged.
