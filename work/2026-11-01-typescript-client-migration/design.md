# Full generated-client migration: implementation brief

2026-11-01, architect-owned. The user has authorized implementation without a
plan-approval wait, including SDK improvements **through its generator**.
[assessment.md](assessment.md) preserves the original evidence; its partial
adoption end state is superseded. This brief permits full replacement of the
custom vpsAdmin operation layer, not changes to backend product behavior.

## Sources and target

Starting refs: WebUI `f2765d3fd778927f4cda3563f66615bfcf72b7cf`; SDK
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`; HaveAPI
`209a7ac0c2fe6cd1b78735f50b5e60d979309543` (0.32.0); vpsAdmin
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. Use the registered worktrees under
`worktrees/2026-11-01-typescript-client-migration/`. The WebUI feature branch is
`dev/typescript-client-migration`; other repository branches use the dated slug.
Fetch and reassess upstream changes at phase boundaries.

Final dependency direction:

`UI/view models → domain workflows → generated SDK → WebUI policy executor → HaveAPI HTTP runtime`

Every vpsAdmin operation, including anonymous reads and live description probes,
must use generated SDK facilities. Remove `haveApiCall`, `CallOpts`, historical
single-namespace guessing and duplicate handwritten wire DTOs. Temporary wrappers
are allowed during conversion only. No permanent generic CRUD escape, second
endpoint registry or local protocol decoder. The one executor may import the
HaveAPI runtime and its request/error types; domain callers may not bypass SDK.
BFF/session/OAuth exchanges and browser navigation to download URLs remain their
own protocols. View models, input drafts, domain policy and boundary validation
are legitimate handwritten code, not duplicate wire schemas.

## Generator contract: first execution package

**implementer0 owns this package now.** Modify HaveAPI's
`clients/typescript/lib/haveapi/typescript_client/{ir,emitter,generator}.rb` and
related generator source only as needed, plus `clients/typescript/spec/`, its
README and affected development guidance. Read repository procedures and review
the hook configuration/custom hooks before normal signing; do not bypass hooks.
Do not hand-edit generated SDK files or add handwritten SDK behavior to fill gaps.

Keep existing generated action invocation syntax and `RequestExecutor` intact.
Generate these additive public facilities and validate them with small generic
fixtures before SDK consumers begin:

1. **Live descriptions.** Generate `api.describe(options?)` for the version-root
   OPTIONS document and `api.node.update.describe({ path: { node_id }, ... })`
   for a concrete action, using that action's recorded help route/method and path
   encoder. The latter is an illustrative concrete accessor; all actions receive
   the same facility. Options carry headers, signal and timeout, not arbitrary
   HTTP paths. Return the standard receipt with a description data type grounded
   in the HaveAPI protocol. Preserve authorization-filtered absence and errors;
   static action presence never means permission. No SDK auth cache or automatic
   capability inference. Check naming/collision rules in the IR. If attaching
   `describe` to the callable cannot fit existing collision guarantees, report
   the smallest alternative to architect/lead before changing this public shape.
   For old snapshots without `help`, the sole fallback is the already validated,
   normalized schema action route plus its validated `?method=`. Explicit invalid
   help rejects generation; never guess a live route or retry an alternative URL.
2. **Pre-dispatch input errors.** Export a generated `ClientInputError` extending
   `TypeError`, with readonly `code = 'HAVEAPI_CLIENT_INPUT_ERROR'` and
   `phase = 'pre-dispatch'`.
   Existing generated local input/path/JSON validation raises this error. Never
   wrap executor/transport errors as local input failures, and do not attach
   secret input values. Consumers can avoid treating these as uncertain writes.
3. **Metadata typing.** Export a generated `ActionResult<TData, TMeta>` retaining
   `data`, `meta`, `envelope`, `httpStatus`; type `meta` as the action's emitted
   GlobalOutput plus extensible unknown keys. Preserve optional/null metadata and
   raw receipt. This improves declarations, not runtime payload validation.
   Empty-known-metadata types must still allow unknown extension keys; intersecting
   `Record<string, never>` with an unknown-key record does not do this. Keep empty
   action data strict independently of metadata extensibility.
4. **Current runtime.** Align generated support contracts/tests with HaveAPI JS
   0.32.0. Keep safe integers, omitted versus null/false/zero, custom JSON/query
   limits, exact namespaces and single-send behavior. No session renewal, retries,
   pagination or automatic completion is added to the generated layer.
5. **Configured metadata namespace.** Generate optional
   `createClient({ execute, metaNamespace })`; omission uses the snapshot namespace.
   One effective wire namespace drives global metadata, object-input encoding,
   RequestSpec and description calls. Generated schema-named object-input keys
   stay canonical, with wire-key conversion inside the generator-owned runtime.
   Preserve typed canonical object-list metadata in returned data when a wire
   override is used; normalize only declared metadata positions, never arbitrary
   Custom content, and retain the untouched envelope. A smaller equally coherent
   interface can be proposed before freeze. Reject invalid/colliding overrides
   before dispatch. Default/custom namespace fixtures must cover object metadata
   as well as global metadata; a RequestSpec-only override is insufficient.

Acceptance: generic emitted-source/negative type fixtures and request spies prove
root/action OPTIONS method/path/mount semantics, malformed/denied descriptions,
metadata receipt preservation, compatible ordinary calls, and the local-error
versus executor-error distinction. Source-generation unit/strict compilation
checks precede a committed package review and longer actual-runtime integration.
Report settled exports with examples and exact generator head to implementer1,
architect and lead. Any further generator feature needs a demonstrated consumer
gap and design reconciliation, not a speculative framework.

## SDK/schema package: independent work available now

**implementer1 owns this package.** In the clean committed vpsAdmin worktree,
prepare and run the existing controlled full-fixture exporter per
`docs/api-schema-export.md`. It uses an owned disposable MariaDB database and
all six plugins, never a deployed API/DB. Compare with the recorded old source
`bcfa95eb136c50d25024f53a6b1af557d1173d56`; retain real source, schema, plugin,
fixture and tooling provenance. This capture/preparation can overlap generator
work. Backend behavior is out of scope; surface any exporter defect before edits.

After implementer0's contract/head is stable, own SDK `schema/`,
`tools/generator.json`, necessary regeneration/toolchain support records,
`package.json`, lock, generated tree/manifest, consumer tests and SDK docs.
Regenerate from the exact current HaveAPI source plus this initiative's generator
changes; align the runtime peer to the tested 0.32.0, not the old 0.30.2. Preserve
strict generation provenance rather than weakening checks to accept new inputs.
Do not edit generated files. Fix missing reusable client behavior in package 0.

Acceptance: reviewed full profile/schema delta; deterministic regeneration/check;
strict SDK consumer cases including the new facilities and real WebUI call
shapes. Build and pack once into an immutable candidate tarball, record commit,
generator/schema inputs, SHA256 and npm SHA512 integrity; verify that exact archive
using existing `tools/check-package.mjs --archive`. WebUI pilot installs that
archive in its verification context, not a mutable checkout/symlink.

## WebUI foundation and pilot

**implementer2 owns the shared boundary.** It waits for the generated contract;
read-only preparation can overlap. Extract the current application request policy
at the complete `RequestSpec → Promise<RequestResult<unknown>>` seam. Preserve
all spec fields, especially output namespace, headers, signal and timeout, and
the entire raw receipt. Do not route generated calls through current `CallOpts`.
Keep serialization and envelope decoding solely in HaveAPI. Generated descriptions
supply legacy runtime-header discovery and action capability inputs without
reintroducing a custom operation registry.

WebUI retains per-request auth/language, public isolation, impersonation, BFF
renewal, expiry notifications, error presentation, capability cache scope,
ambiguous-write reconciliation, polling and pagination. Validated OAuth 401 can
renew/retry reads and OPTIONS only; never automatically replay writes. Preserve
contradictory HTTP/envelope evidence and explicit local validation classification.
Preserve configured/mounted version URLs. Pass the configured/discovered metadata
namespace through the generated client option, include it in client cache identity
and recreate bindings when it changes. WebUI must not remap wire metadata. Bootstrap
description discovery must not recurse through an authenticated executor waiting
for that same discovery. Description types remain conservative/extensible; WebUI
capability guards must fail closed on malformed/missing fields.

Pilot with implementer3's first VPS list and asynchronous mutation, and
implementer4/6's first live capability probe. The domain file stays with its owner;
implementer2 owns shared fixes. Demonstrate output narrowing, includes/count,
action receipt/completion, synchronous mutation exceptions, failed capability
lookups and permission/field absence before releasing broad domain edits. Inputs
use generated types; outputs are narrowed into UI models where stronger fields
are required. Do not paper over discrepancies with broad casts or fabricated IDs.

## Complete file partition and staged parallelism

The following assigns all 64 current production files in `src/lib/api` exactly
once. Each group also owns its same-stem tests and direct domain consumer fixes,
with the lead assigning any cross-domain consumer file to one owner before edits.
New upstream files receive an owner during the next inventory delta. More owners
does not remove dependencies: activate packages 0/1 first, then 2 plus the small
pilot slices, then the five domain batches once the shared contract is proven.

| Owner | Package / exact API files (basename without `.ts`) |
| --- | --- |
| implementer0 | HaveAPI generator, generic fixtures/support docs as above; generator follow-up fixes remain here. |
| implementer1 | vpsAdmin export input and SDK regeneration/package/consumer tests/docs as above; no WebUI package lock edits. |
| implementer2 | Shared WebUI: `actionStates`, `app`, `appTypes`, `ascendingIdCollection`, `haveapi`, `haveapiRequestClient`, `public`; new SDK binding/policy/error helpers; root package/lock and package dependency hashes; common auth import adjustments, shared test setup, API inventory, requirements/API contracts/work log. |
| implementer3 | VPS/storage: `vps`, `vpsAccess`, `vpsFeatures`, `vpsMaintenance`, `vpsMounts`, `vpsUserData`, `datasets`, `exports`, `migrations`, `osTemplates`. |
| implementer4 | Network/DNS: `dns`, `dnsResolvers`, `dnsSecretScrubber`, `dnsTransfers`, `dnsTsigKeys`, `ipAddresses`, `locationNetworks`, `networkInterfaces`, `networking`, `networks`. |
| implementer5 | Users/settings: `users`, `userTypes`, `userAccounts`, `userDossier`, `userEnvironmentConfigs`, `userLookups`, `userMail`, `userNamespaces`, `webuiUserSettings`, `languages`. |
| implementer6 | Infrastructure/operations: `audit`, `cluster`, `clusterResources`, `clusterResourcePackages`, `clusterSearch`, `infra`, `lifetimes`, `monitoring`, `nodeCreateReconciliation`, `nodeHistory`, `nodes`, `oom`, `securityAdvisories`, `securityAdvisoryRelations`, `securityAdvisoryUpdates`, `systemConfig`, `transactions`. |
| implementer7 | Finance/content: `finance`, `helpBoxes`, `incidents`, `mailTemplateCreateReconciliation`, `mailer`, `newslog`, `outageScopePaging`, `outages`, `payments`, `requests`. |

Domain acceptance: generated operations for every call; generated input/wire
types replace duplicates; explicit domain models/guards remain; metadata, public
scope, raw-envelope consumers, includes, nullable associations, capability checks,
cursor budgets/partial results and mutation recovery retain behavior. Snapshot
download records use SDK; safe URL handling and browser downloads remain WebUI.
Each owner supplies focused checks and documentation facts to implementer2, who
alone edits shared product docs/barrels/types. Architect resolves consequential
deviations through lead; implementers own implementation and dependent fixes.

Source-backed migration corrections and their visible effects are settled in
[contract-dispositions.md](contract-dispositions.md). They do not delay the
generator/SDK/shared pilot. Domain source work still starts only on the lead's
phase release. In particular, static generated input types intersect live
capabilities; live metadata cannot authorize a cast around the saved contract.
Advisory revision checks cover parent edits/publish **and existing child writes**.

## Completion, verification and upstream changes

1. After domain conversion, implementer2 deletes the transitional generic call
   layer and moves only real application policy into clearly named modules.
   Search current HEAD across production sources, not just the original 53
   call-bearing files, for direct HTTP/runtime operation calls, handmade endpoint
   descriptors, `haveApiCall`, `CallOpts`, unwrap helpers and duplicate wire DTOs.
   All vpsAdmin paths must end at SDK, including calls added upstream meanwhile.
2. Use pinned Nix environments and existing commands. Quick typechecks, scoped
   generator/consumer/adapter tests, required hooks and documentation audits run
   per package. Check null/absence/false/zero, negative input types, descriptions,
   error/renewal paths, actual-package XHR decoding, receipt preservation, paging
   and representative association shapes. No substitute endpoint audit framework.
3. When intended substantive changes are committed and quick checks pass, run
   mandatory final independent review. Retained `reviewer0` is **Astra/xhigh**;
   recheck live roster and preserve its settings. Packet covers every repository's
   complete final base-to-head history/diff, generated-input lineage, dependency
   consolidation and explicit migration conclusion (no migrations expected).
   Applicable lanes: general, architecture, scope, risk/compatibility. Resolve
   Blocking/Important findings under the skill before long integration tests.
4. Then run longer actual-runtime/packaged consumer, full required WebUI build,
   regression and browser tests and a bounded isolated API member/admin contract
   check. Measure bundle effect; mocks alone do not prove backend compatibility.
   Fresh utility watchers launch/monitor long or uncertain checks per monitor
   skill. Schema capture is necessary input generation, not a substitute for
   integration evidence; its disposable database ownership must be preserved.
5. Lead serializes Git/index operations per repository and all shared-file edits.
   Pause writers and commit owned paths before rebases; preserve other work.
   At foundation, pilot, domain-batch and final-review boundaries, fetch defaults,
   inspect upstream deltas and rebase when permitted. Retest changed contracts and
   repeat inventory after each refresh. Do not rewrite published WebUI history
   without the required explicit direction; route that case through lead. Record
   old/new ranges and patch equivalence; substantive conflict resolutions need
   affected checks/review. Domain owners resolve their conflicts. Independent
   feature work needs no repository merge claim.

## Publication, compatibility, recovery and limits

Use the immutable SDK tarball for development/consumer verification. Do not
commit a machine-local tarball path or silently publish to make a lock resolve.
Prepare a reviewed SDK release and exact consumer pin. Registry publication,
release tags, default-branch integration and deployment need their respective
explicit authorization; none is granted by implementation. The existing release
workflow publishes the same approved archive and checks registry integrity.
Once authorized/published, implementer2 commits the exact SDK version and lock
integrity and reruns package/consumer checks; readiness must distinguish verified
implementation from a distributable final dependency lock. Keep release-candidate
and tarball evidence until that dependency is resolved. No new release framework.

No DB migrations, API product behavior changes, daemon/CLI/Terraform contract
changes or coordinated node update are inherent. Supported API revision/plugin
combinations remain explicit; a full-fixture snapshot is not live permission.
Capability checks must keep old/new API combinations safe. Do not automatically
select a new API default version. No session/settings storage changes are needed.
Rollback restores matching old frontend/dependency artifacts; accepted server
mutations continue and need existing reconciliation. Generator and SDK rollbacks
restore matching schema/provenance/source/manifest, not an edited generated tree.

Effort remains provisional: approximately 3–5 engineer-days for generator/SDK
foundation plus pilot, and 15–30 total for migration/verification, revised after
the pilot. Eight owners enable parallel domain work, not an eightfold elapsed-time
reduction. Scope gaps requiring backend behavior changes go to lead; client
capabilities are fixed in the generator. The lead maintains plan/state and user
communication. This brief is ready to release the first two execution packages.
