# TypeScript client adoption assessment

Historical assessment. The full-replacement implementation brief in
[design.md](design.md) supersedes the partial-adoption end state proposed here;
the inspected source evidence and limitations remain useful.

Assessment only, 2026-11-01. Proposed design, not authorization or evidence of
implementation. Source inspection used canonical bare repositories at these
fetched default heads; no builds, API calls, application edits or deployments ran:

| Reference | Repository / default | Revision |
| --- | --- | --- |
| W | vpsadmin-webui / main | `f2765d3fd778927f4cda3563f66615bfcf72b7cf` |
| S | vpsadmin-typescript-client / main | `e5786f69b7c223c3bb5b1de99b7f97186eec368a` |
| H | haveapi / master | `209a7ac0c2fe6cd1b78735f50b5e60d979309543` |

File/line references below use these immutable revisions. Architect owns the
recommendation; implementer0 supplied a bounded read-only WebUI inventory.

## Recommendation and actual starting point

Adopt the generated SDK incrementally for operation names, paths, inputs and wire
response types. Retain HaveAPI as HTTP/protocol runtime and retain WebUI's policy
and domain adapters. Do not replace the HTTP stack or rewrite React screens as
the initial step.

The premise needs one correction: WebUI already uses raw
`AsyncClient.request(spec)`, without `setup()` or `authenticate()`; it does not
invoke dynamically discovered resource methods. See
[W request adapter:17–38](https://github.com/vpsfreecz/vpsadmin-webui/blob/f2765d3fd778927f4cda3563f66615bfcf72b7cf/src/lib/api/haveapiRequestClient.ts#L17).
The SDK is also a facade over a request executor, with `haveapi-client` as a peer
dependency ([S entry point:1–16](https://github.com/vpsfreecz/vpsadmin-typescript-client/blob/e5786f69b7c223c3bb5b1de99b7f97186eec368a/src/index.ts#L1)).
The change replaces handwritten operation descriptions and caller-selected
`haveApiCall<T>` assertions, not the runtime package itself.

Scale at W: `src/lib/api` contains 64 production TypeScript files / 10,651 lines;
53 contain 368 lexical `haveApiCall` invocation sites. Anonymous calls are
separate. There are 260 handwritten interface/type declarations across 60 API
files, including options/helper types, not 260 endpoints. Inventory used
`git ls-tree` and `git show`, excluding tests/specs and `src/test`; these are text
counts, not AST coverage or a claim that every declaration should disappear.
There is no `src/api`, `useApiCall` or `.lookup()` call path.

## Correctness gain and its limits

Generated calls catch misspelled resources/actions, missing path arguments,
unsupported filters and wrong primitive/nullability inputs. They also construct
method/path/namespaces centrally and reject unknown inputs, unsafe integer IDs
and invalid JSON before execution (S `src/generated/runtime.ts:79–175`).
S `test/consumer/types.ts:32–49` contains negative type examples for these cases.

For example, W `src/lib/api/vps.ts:244–250` accepts arbitrary
`Record<string, unknown>` updates and asserts a returned `Vps`. S
`src/generated/resources/vps/actions/update.ts:6–37` instead declares the actual
update fields and an empty `Record<string, never>` output. A future adapter can
use `api.vps.update({ path: { vps_id }, params: typedChanges })`, preserve the
receipt, and read back state where required. Similarly `api.vps.index({ params:
{ limit, from_id }, meta: { includes: 'node,user', count: true } })` replaces the
handwritten descriptor at W `vps.ts:194–232`. Construct typed input objects at
their source; passing broad records or adding casts loses much of the benefit.

Generated types are deliberately less optimistic than current UI models. W
`vps.ts:6–47` requires `id` and `hostname` and treats `node` as a Node; S
`resources/vps/actions/index.ts:20–71` permits absent/null fields and exposes
associations as partial records with unknown values. Narrow/normalize required
fields at the adapter boundary, retain UI-specific models, and reject malformed
identity rather than inventing IDs or silently dropping rows. Do not cast every
generated result back to the existing DTO.

This is not runtime payload validation. S `runtime.ts:237–240` explicitly asserts
`response.data as T`; the runtime validates envelopes and selected namespaces,
not entity fields. Custom outputs remain `unknown`, dates remain strings, and
the compiler does not establish permission, ownership, cursor ordering, valid
state transitions or successful job completion. Existing meaningful boundary
guards and domain validation remain necessary. No new universal validation
framework is needed to start.

## Parity, confirmed adaptation work and open risks

| Area | Evidence and consequence |
| --- | --- |
| Runtime versions — confirmed blocker | W `package.json` pins HaveAPI **0.32.0**; S 0.2.0 pins exact peer/dev **0.30.2**. Verify and update SDK support toward 0.32.0, including generator support records as needed. Do not downgrade WebUI, force peer installation, or assume compatibility from similarly shaped types. S `tools/generator.json` records Ruby shared-source version 0.32.0; that is not proof of supported JavaScript runtime compatibility. |
| Results and namespaces — confirmed difference | SDK carries `data`, `meta`, `envelope`, `httpStatus` and specifies the exact output namespace. W `haveapi.ts:135–176,374–383` uses historical single-namespace projection, tolerant metadata aliases and generic casts. Preserve old projection only for old callers; generated results must not be unwrapped twice. Verify empty outputs and multi-namespace/custom replies in the pilot. |
| Metadata and completion — supported transport, retained policy | Input `count`/`includes` and object metadata are generated; GET Custom metadata accepts scalar values, so keep string includes. Response metadata is still generic `RequestResult.meta` even though standalone `GlobalOutput` types are emitted (S VPS Index:74–87,215–219). Keep count/receipt checks and W `actionStates.ts`. SDK receipts cannot enter `AsyncClient.waitForCompletion`, which requires a dynamic invocation. Preserve W `vps.ts:251–261` synchronous exceptions and required receipts for other writes. |
| Capabilities — intentionally outside SDK | Static method presence is not authorization or deployed support. Retain live OPTIONS probes: W `nodes.ts:299–329`, `networks.ts:76–90`, `ipAddresses.ts:96–104`, including input requiredness/nullability, denied/error states and scope-aware caching. SDK includes recent network `enabled` and IP `network_enabled` inputs, but this does not justify sending them to older APIs without capability checks. |
| Authentication/errors — retained WebUI responsibilities | Keep public/authenticated separation, current credentials and language, configured headers, impersonation and BFF/OAuth handling. W `haveapi.ts:387–419` renews only a validated OAuth 401 and retries GET/OPTIONS, never writes automatically. Preserve `HaveApiError`, validation details, contradictory HTTP/envelope receipts, expiry events, abort/timeout and ambiguity. SDK local validation throws `TypeError` (S runtime:46–47); W `haveapi.ts:252` considers TypeError ambiguous transport. Distinguish proven pre-dispatch validation from a possibly submitted write; never weaken transport ambiguity globally. |
| Pagination — no automatic replacement | Generated `limit`/`from_id` fields do not establish ordering or complete traversal. Retain `ascendingIdCollection.ts`, `useKeysetPagination.ts`, role-specific traversal, budgets and partial results. W `docs/design/API_CONTRACTS.md` records existing server-order limitations; migration does not resolve them. |
| Downloads/raw requests — retain small explicit boundary | Snapshot downloads are JSON records and sanitized URL links, not a binary API transport. SDK has SnapshotDownload operations and `url`/`ready` fields (S Show:8–19); preserve W `DatasetDownloadModel.ts:43,99,232` link/legacy behavior until separately reconciled. Preserve original envelopes used by W `vpsAccess.ts:33–39`. Keep raw requests for OPTIONS, configured custom routes and documented uncovered operations; BFF/session/OAuth JSON remains its own protocol. |
| Coverage/platform — unresolved pilot risk | SDK declares 151 application resources / 519 actions from API 7.0, six plugins; authentication actions are deliberately excluded (S `docs/development.md:40–45`). No whole-endpoint audit was performed. Exact consumer coverage, installed API compatibility, TS 5.9 consumer compatibility (SDK tooling uses TS 6), browser bundle cost and 0.32 runtime behavior require a pilot. Missing support is a risk, not a confirmed missing endpoint. |

## Proposed interface and invariants

Extract WebUI request policy at the complete
`RequestSpec -> Promise<RequestResult<unknown>>` boundary. The generated SDK uses
that executor; existing `haveApiCall` and public helpers remain compatibility
wrappers for unmigrated callers. Do not implement the executor by translating
through current `CallOpts`: it lacks `outputNamespace`, `headers` and
`timeoutMs` (W `haveapi.ts:86–102,358–370`). Preserve all spec fields and the raw
receipt, with explicit auth/language header ownership and the current no-auth
public policy. Keep one serialization/envelope decoder in HaveAPI.

Preserve per-request credential/language selection, immutable retry inputs,
mount plus `/v7.0` URL handling, cancellation, timeout, no automatic write replay,
receipt validation and domain read-back. Snapshot schema metadata uses `_meta`;
reconcile any configured metadata namespace deliberately rather than allowing
generated object metadata and transport namespace to diverge. Pilot against the
normal vpsAdmin configuration before claiming other configurations supported.

Keep exported domain adapter functions initially so React Query consumers and
screens do not all change together. Use generated input types and operation
outputs, then explicit normalization only where a view model needs stronger
guarantees. Avoid a second handwritten endpoint registry or permanently
duplicating every generated DTO.

## Adoption, effort and possible implementation boundaries

Judgment-based estimate for an engineer familiar with the code: **3–5 engineer
days for runtime alignment plus a useful pilot; roughly 15–30 engineer days total
for broad adoption with regression verification**. This is not a measured plan;
schema gaps or heavily assumed association shapes may increase it. A pilot
should revise the estimate before promising all 53 call-bearing modules.

| Package | Files/boundary and dependencies | Acceptance |
| --- | --- | --- |
| SDK support | SDK package/lock, compatibility fixtures and support docs; HaveAPI generator change only if demonstrated necessary | Supported 0.32 runtime installation and packaged consumer checks; no WebUI downgrade. First dependency for consumer integration. |
| Policy seam and pilot | W `haveapi.ts`, `haveapiRequestClient.ts`, new typed client binding; one VPS list and one asynchronous mutation in `vps.ts` | Same auth/error/recovery semantics; typed inputs; correct projection/meta; optional fields handled; accepted versus completed mutation remains distinct. One owner serializes shared seam changes. |
| Domain batches | Disjoint `src/lib/api` groups and their tests, e.g. networking; datasets/downloads; users/payments | Depend on accepted seam/pilot. Keep public adapter contracts where honest; narrow outputs; preserve capabilities/paging. Independent implementers can own non-overlapping groups, with shared view-model changes coordinated. |
| Completion | Remaining raw-call inventory, package/docs/work-log/inventory changes | Every retained escape hatch justified; no blanket casts hiding migration errors; consumer checks and agreed API matrix pass. |

## Verification, compatibility and maintenance

For this assessment, evidence is source inspection only. A later pilot should
run WebUI's pinned Nix environment, typecheck and focused adapter/actual-package
tests. Cover reads with count/includes, public isolation, 401 renewal, denied and
malformed replies, abort/timeout, exact namespaces, empty mutation outputs,
false/zero/null/omission, pre-send validation, action receipts and uncertain
writes. Compile negative examples for unsupported inputs. SDK checks include
`typecheck:consumer` and `test:package` using the supported runtime. Broader build,
unit/required audits and Playwright follow the repository procedure; a real
isolated API/member/admin test must establish server compatibility separately
from fixtures. Inspect bundle effects during the pilot, not by assumption.

SDK maintenance replaces repeated handwritten request contracts with a reviewed
schema-update pipeline. Its inputs are reproducible: saved full-fixture schema,
vpsAdmin source `bcfa95eb136c50d25024f53a6b1af557d1173d56`, pinned HaveAPI generator
`0e7166a0f8f15827bfac051666a53bf449e999ec`, provenance and tool locks. Use the
controlled vpsAdmin exporter and SDK offline regeneration, not a user's
permission-filtered OPTIONS response; review and release schema/runtime changes
together, then update the WebUI lock. Never hand-edit generated files. Consumers
need neither Ruby nor the generator at application runtime.

No database/schema/on-disk format, API server, CLI, Terraform, daemon protocol or
system configuration change is inherent in this proposal. Old and new WebUIs may
use the same supported API during staged adoption. New SDK fields must still be
capability-gated; API version 7.0 alone does not prove identical revision/plugin
coverage. If an endpoint requires a newer API, document that minimum and deploy
the compatible server before enabling it. No coordinated node update is needed.
Rollback restores the prior frontend artifact and matching package lock; browser
settings/session formats should remain unchanged. Accepted server mutations
continue after frontend rollback, so existing reconciliation remains necessary.

The added SDK/version pipeline is a maintenance cost, but central request
contracts and compiler-visible drift are worthwhile at this scale. Adopt it
behind the existing policy layer; measure the pilot before undertaking the full
conversion. Lead owns session state and final user-facing handoff.
