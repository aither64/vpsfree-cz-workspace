# Full generated-client migration: implementation brief

2026-11-01, architect-owned. The user has authorized implementation without a
plan-approval wait, including generated client improvements **through its generator**.
[assessment.md](assessment.md) preserves the original evidence; its partial
adoption end state is superseded. This brief permits full replacement of the
custom vpsAdmin operation layer, not changes to backend product behavior.

## Sources and target

Starting refs: WebUI `f2765d3fd778927f4cda3563f66615bfcf72b7cf`; generated client
`e5786f69b7c223c3bb5b1de99b7f97186eec368a`; HaveAPI
`209a7ac0c2fe6cd1b78735f50b5e60d979309543` (0.32.0); vpsAdmin
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. Use the registered worktrees under
`worktrees/2026-11-01-typescript-client-migration/`. The WebUI feature branch is
`dev/typescript-client-migration`; other repository branches use the dated slug.
Fetch and reassess upstream changes at phase boundaries.

Final dependency direction:

`UI/view models → domain workflows → generated client → WebUI policy executor → HaveAPI HTTP runtime`

Every vpsAdmin operation, including anonymous reads and live description probes,
must use generated client facilities. Remove `haveApiCall`, `CallOpts`, historical
single-namespace guessing and duplicate handwritten wire DTOs. Temporary wrappers
are allowed during conversion only. No permanent generic CRUD escape, second
endpoint registry or local protocol decoder. The one executor may import the
HaveAPI runtime and its request/error types; domain callers may not bypass the
generated client.
BFF/session/OAuth exchanges and browser navigation to download URLs remain their
own protocols. View models, input drafts, domain policy and boundary validation
are legitimate handwritten code, not duplicate wire schemas.

## Generator contract: first execution package

**implementer0 owns this package now.** Modify HaveAPI's
`clients/typescript/lib/haveapi/typescript_client/{ir,emitter,generator}.rb` and
related generator source only as needed, plus `clients/typescript/spec/`, its
README and affected development guidance. Read repository procedures and review
the hook configuration/custom hooks before normal signing; do not bypass hooks.
Do not hand-edit generated client files or add handwritten client behavior to
fill gaps.

Keep existing generated action invocation syntax and `RequestExecutor` intact.
Generate these additive public facilities and validate them with small generic
fixtures before generated client consumers begin:

1. **Live descriptions.** Generate `api.describe(options?)` for the version-root
   OPTIONS document and `api.node.update.describe({ path: { node_id }, ... })`
   for a concrete action, using that action's recorded help route/method and path
   encoder. The latter is an illustrative concrete accessor; all actions receive
   the same facility. Options carry headers, signal and timeout, not arbitrary
   HTTP paths. Return the standard receipt with a description data type grounded
   in the HaveAPI protocol. Preserve authorization-filtered absence and errors;
   static action presence never means permission. No generated client auth cache or automatic
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

## Generated client/schema package: independent work available now

**implementer1 owns this package.** In the clean committed vpsAdmin worktree,
prepare and run the existing controlled full-fixture exporter per
`docs/api-schema-export.md`. It uses an owned disposable MariaDB database and
all six plugins, never a deployed API/DB. Compare with the recorded old source
`bcfa95eb136c50d25024f53a6b1af557d1173d56`; retain real source, schema, plugin,
fixture and tooling provenance. This capture/preparation can overlap generator
work. Backend behavior is out of scope; surface any exporter defect before edits.

After implementer0's contract/head is stable, own the generated client’s `schema/`,
`tools/generator.json`, necessary regeneration/toolchain support records,
`package.json`, lock, generated tree/manifest, consumer tests and generated client docs.
Regenerate from the exact current HaveAPI source plus this initiative's generator
changes; align the runtime peer to the tested 0.32.0, not the old 0.30.2. Preserve
strict generation provenance rather than weakening checks to accept new inputs.
Do not edit generated files. Fix missing reusable client behavior in package 0.

Acceptance: reviewed full profile/schema delta; deterministic regeneration/check;
strict generated client consumer cases including the new facilities and real WebUI call
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

Pilot empty-output framing is confirmed: VPS Start succeeds with
`{status:true,response:{vps:{},_meta:{action_state_id:…}}}`. At vpsAdmin
`610a96f8`, `vps.rb:590–614` calls `ok!`; HaveAPI `172c752e`
`servers/ruby/lib/haveapi/action.rb:592–594` defaults its return to `{}`,
inherits the base `output {}` declaration (`:68–81`, `:520`), and wraps the
empty object plus blocking metadata (`:501–508`). `params.rb:105,112–123`
selects object layout and singular `vps` namespace. No explicit action output
block does not mean an absent output descriptor. The generated namespace is
correct; correct pilot fixtures, not the generator or executor. Actual-runtime
checks must distinguish a valid empty `vps` plus receipt, empty `vps` missing
the receipt, and invalid metadata-only output missing `vps`.

Pilot VPS output contract: use one generated-backed `Vps` domain view shared by
existing list consumers, with validated positive safe-integer top-level `id`.
Preserve nullable/absent hostname and scalars from generated output; existing
labels already fall back to `#id`, so hostname is not a universal required field.
User/node/location associations are partial generated-derived views, never full
User/Node instances. In particular, a valid id/login user reference need not have
`level`. Missing/null reference fields remain valid; malformed present shapes
produce a visible boundary error rather than silently dropping associations or
rows. Validate the exact owner/location identity when a particular action needs
it, and fail that action closed if unavailable. Narrow only consumed included
fields and retain the original receipt. Use type-only imports; no second mapping
framework or new runtime dependencies between API domain modules.

For this pilot, implementer3 additionally owns essential VPS view changes in
`src/pages/app/vps/vpsListSemantics.ts`, `src/components/ui/VpsLookupInput.tsx`,
`src/lib/search/userGlobalSearch.ts`,
`src/pages/app/networking/AssignIpAddressModal.tsx` and
`src/pages/app/networking/IpAddressAssignmentModel.ts`, plus their tests. This
ownership covers VPS typing/narrowing only; other domain operation behavior stays
with its owner. Notify i4 before overlapping later networking edits. Prefer
adapting null at an existing helper's call boundary when null and absence both
mean unknown; never coerce unknown booleans to false. Report concrete remaining
compile dependencies before expanding the pilot to additional files.

The first typecheck identified a bounded additional VPS propagation set, granted
by lead: `VpsControlCenterCards`, `VpsOverviewPrimitives`, `VpsOverviewPage`,
`VpsReinstallCard`, `VpsResourceDiskCard`, and `VpsStoragePage` under
`src/pages/app/vps/`. Implementer3 also owns narrow helper corrections/tests in
`VpsOverviewModel` and `VpsStorageModel`: ID readers accept partial id-bearing
views and validate identity; owner labels remain unavailable when both label/ID
are absent; the root-dataset fallback accepts partial/unknown input through its
existing guards. Full fetched dataset/action contracts stay strict. Preserve the
existing hostname fallback and unavailable owner semantics. This extends only
pilot model propagation, not other domain operations or a shared mapping layer.

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
| implementer1 | vpsAdmin export input and generated client regeneration/package/consumer tests/docs as above; no WebUI package lock edits. |
| implementer2 | Shared WebUI: `actionStates`, `app`, `appTypes`, `ascendingIdCollection`, `haveapi`, `haveapiRequestClient`, `public`; new generated client binding/policy/error helpers; root package/lock and package dependency hashes; common auth import adjustments, shared test setup, API inventory, requirements/API contracts/work log. |
| implementer3 | VPS/storage: `vps`, `vpsAccess`, `vpsFeatures`, `vpsMaintenance`, `vpsMounts`, `vpsUserData`, `datasets`, `exports`, `migrations`, `osTemplates`. |
| implementer4 | Network/DNS: `dns`, `dnsResolvers`, `dnsSecretScrubber`, `dnsTransfers`, `dnsTsigKeys`, `ipAddresses`, `locationNetworks`, `networkInterfaces`, `networking`, `networks`. |
| implementer5 | Users/settings: `users`, `userTypes`, `userAccounts`, `userDossier`, `userEnvironmentConfigs`, `userLookups`, `userMail`, `userNamespaces`, `webuiUserSettings`, `languages`. |
| implementer6 | Infrastructure/operations: `audit`, `cluster`, `clusterResources`, `clusterResourcePackages`, `clusterSearch`, `infra`, `lifetimes`, `monitoring`, `nodeCreateReconciliation`, `nodeHistory`, `nodes`, `oom`, `securityAdvisories`, `securityAdvisoryRelations`, `securityAdvisoryUpdates`, `systemConfig`, `transactions`. |
| implementer7 | Finance/content: `finance`, `helpBoxes`, `incidents`, `mailTemplateCreateReconciliation`, `mailer`, `newslog`, `outageScopePaging`, `outages`, `payments`, `requests`. |

Domain acceptance: generated operations for every call; generated input/wire
types replace duplicates; explicit domain models/guards remain; metadata, public
scope, raw-envelope consumers, includes, nullable associations, capability checks,
cursor budgets/partial results and mutation recovery retain behavior. Snapshot
download records use the generated client; safe URL handling and browser downloads remain WebUI.
Each owner supplies focused checks and documentation facts to implementer2, who
alone edits shared product docs/barrels/types. Architect resolves consequential
deviations through lead; implementers own implementation and dependent fixes.

Source-backed migration corrections and their visible effects are settled in
[contract-dispositions.md](contract-dispositions.md). They do not delay the
generator, generated client or shared pilot. Domain source work still starts only
on the lead's phase release. In particular, static generated input types intersect live
capabilities; live metadata cannot authorize a cast around the saved contract.
Advisory revision checks cover parent edits/publish **and existing child writes**.

## Completion, verification and upstream changes

### Approved isolated API contract check

Lead accepted the necessary test-only extension after confirming that existing
Generated client archive checks use canned HTTP responses and the exporter stops after schema
capture. Implementer0 owns WebUI
`scripts/integration/vpsadmin-sdk-contract.{mjs,rb}` and small safety checks;
implementer2 owns shared documentation. Do not change application code or frozen
HaveAPI/generated client sources. Prepare source and quick checks now; launch no real database
or server matrix until these files are committed and final WebUI review passes.

Use the session's clean vpsAdmin checkout at
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. Exact reusable inputs there:

- `tools/api-schema-export/safety.rb`: check inherited connection/Bundler/plugin
  overrides and local configuration before loading Bundler or connecting.
- `tools/export-api-schema`, `tools/api-schema-export/cli.rb`: existing preload
  refusal, isolated bundle setup and test/all-plugin environment sequence. Reuse
  these rules without extending the exporter CLI. Verify the clean committed
  vpsAdmin source separately, as the export Runner normally supplies that check.
- `tools/api-schema-export/{Gemfile,Gemfile.lock,bootstrap.rb}`: existing prepared
  HaveAPI 0.32.0 bundle and `Bootstrap.new(root:).load`, which returns the real API.
  The lock already supplies Puma, Rackup and MariaDB bindings. No new dependencies.
- `tools/test_db.rb:364–383`: `TestDb.auto_start!` allocates a temporary database
  and free local port and registers its own stop/prune on process exit. Let this
  owner retain cleanup; do not use the shared/manual database path.
- `api/spec/support/{db_setup,spec_plugins,spec_seed}.rb`: Bootstrap loads the
  actual schema, six plugin migrations and fixtures. It does not load
  `spec_helper.rb` or its request/model/network stubs.
- `api/config.ru`: production Rack target is `VpsAdmin::API.default.app`.
  Serve the returned real app on loopback only, with an allocated port and
  explicit versioned base. An ordinary Rack map can cover a non-root mount.

`SpecSeed.admin`, `.user`, `.other_user`, `.node`, `.os_template` and `.language`
provide synthetic fixture records; basic auth is enabled for seeded users.
Do not print fixture passwords/tokens. Seed three explicit template combinations
using real models (enabled/supported, disabled, unsupported) rather than assuming
the base template's flags. No VPS fixture or worker is required. Pass readiness,
synthetic IDs and credentials only through private ephemeral process state/IPC;
reports retain nonsecret identity and assertion results. Use separate anonymous,
member and admin HaveAPI 0.32.0 runtimes and ordinary public generated client imports from the
already verified immutable installed candidate. Verify its archive/package
identity; do not rebuild/repack, create a second transport or substitute replies.

Bound the actual HTTP matrix to approximately 20–30 calls:

1. Anonymous/member/admin root descriptions and user-current identity/rejection;
   concrete seeded Node Update description and member authorization restriction.
2. Template Index role filtering: admin flags, member enabled-only/omitted flag,
   anonymous enabled-and-supported restriction with both flags omitted.
3. User Index limit/count metadata; an ID predicate assertion may check returned
   IDs exceed from_id, but must not claim lossless or universal cursor ordering.
4. Member setting Set/Show/Index/Delete with false, zero and nested null in a
   Custom object, real persistence, current-user isolation and canonical empty
   delete namespace. Use allowed `ui` namespace and a synthetic key.
5. Invalid setting namespace and unauthenticated setting access: actual backend
   validation/auth errors, full receipt/error distinction, no automatic replay.

Relevant source contracts: `plugins/webui/api/{resources,models}/webui_user_setting.rb`
supports DB-only writes and rejects namespaces outside forms/tips/ui;
`plugins/requests/api/resources/override.rb` supplies anonymous template rules.
Basic authentication uses real login/session code; loopback request addresses
must remain loopback, with no forwarded production identity. Stop on unexpected
network/service work rather than adding authentication or network stubs.

Quick checks cover syntax, argument/environment refusal and child ownership
without booting DB/API. The final-review packet includes this glue. After review,
a fresh verification utility runs one bounded matrix, with a planning limit of
10 minutes for preparation/bootstrap and 5 minutes once ready. Stop at the first
contract mismatch, unsafe source/config refusal, unexpected external dependency
or kernel/VM build; diagnose only that boundary. Parent shutdown must precede
owned database cleanup, including interruption/failure. Record exact API revision,
tooling lock, six-plugin profile, generated client archive/runtime identity and assertion count.

Passing proves real mounted API authorization, descriptions, namespaces,
metadata and DB mutations. It does not prove deployed behavior, OAuth/BFF/browser
flows or asynchronous VPS worker completion. Those boundaries retain their
separate existing evidence; no synthetic chain transition is live completion.

### Delivery sequence

1. After domain conversion, implementer2 deletes the transitional generic call
   layer and moves only real application policy into clearly named modules.
   Search current HEAD across production sources, not just the original 53
   call-bearing files, for direct HTTP/runtime operation calls, handmade endpoint
   descriptors, `haveApiCall`, `CallOpts`, unwrap helpers and duplicate wire DTOs.
   All vpsAdmin paths must end at the generated client, including calls added upstream meanwhile.
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

The [optional development addendum](#optional-local-client-development-and-terminology)
below sets the current merge policy: committed merged code must use an actually
released client. The archive mechanism in this section remains the current
unpublished feature-branch input, not the permanent developer override interface.

The user chose **"Keep the SDK unpublished for now"**, then explicitly requested
temporary support for unpublished generated client candidates so implementation can be refined
without releasing versions. The selected path is one tracked, repository-relative
npm archive in WebUI, consumed through an ordinary `file:` dependency. Generated
client default integration, release tags and publication remain unauthorized. This replaces the
earlier release-only distribution prerequisite; no further user decision is needed
to implement the temporary support.

Use the existing verified generated client candidate without rebuilding or repacking it:

| Input | Exact identity |
| --- | --- |
| Generated client source | `99ee06654ef956a09b52749f4cd02d1435362087` |
| npm package | `vpsadmin-typescript-client`, version `0.3.0`, unpublished |
| WebUI archive | `vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz` |
| Manifest dependency | `file:vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz` |
| Archive bytes | 337414 |
| Archive SHA256 | `f3bb42d0392fb738f5c70fe1415cc8742ab943a31c2ed2a85af5ccbd385d831f` |
| npm integrity | `sha512-6Q74ddIgGzeav9mvPubc33g5Sd+Ni7ZOLtKnNVzP/sW1Cxmw59nLiib50H27HBYc0UgoVfjlxuqH0WmX7hR3jw==` |
| HaveAPI generator | `eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b` |
| Generator source SHA256 | `ea539499207e09c7e1835733115aeca73db3175963b817c95a621baf45da330b` |
| Schema SHA256 | `476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794` |
| Runtime | Existing exact registry `haveapi-client` 0.32.0 and its locked transport |

The source archive and receipt are retained under this session's
`artifacts/package-s/candidate-99ee066/`. Renaming the copied archive does not change
its bytes. A compact `packages/vpsadmin-typescript-client-provenance.json` records
the package/version, relative archive, source repository/full revision, hashes,
generator/schema identity and exact runtime dependency. Keep detailed inventories
in the archive's existing schema/provenance/generator records and the generated client receipt;
do not duplicate the full generated inventory. The existing generated client
`node tools/check-package.mjs --archive FILE` owns archive contents, ESM/type and
HaveAPI consumer verification. Its successful evidence for these exact bytes is
reusable; WebUI does not gain a second packer or archive decoder.

Implementer2 owns this entire WebUI package: the archive and compact provenance,
root `package.json`/npm-generated `package-lock.json`, the existing
`scripts/check-package-source.mjs` and its focused tests, `packages/frontend.nix`,
and affected `docs/design/PACKAGING.md`, `HAVEAPI_CLIENT.md`, requirements/work log.
Implementer1 supplies the already verified candidate/receipt and owns any future
generated client regeneration; no immediate generated client, generator, backend or BFF source change is
needed. Preserve existing HaveAPI/XHR provenance checks. Extend the source checker
only to require the named regular archive, verify its digest/integrity and compare
the manifest, canonical lock and compact provenance. Use the existing symlink/path
refusals. Do not implement a generic dependency validator or reread archive content
already bound by its verified digest. `nix/source.nix` already retains `vendor/`;
no filter change is needed. Repository rules forbid loose generated output, not
this explicitly authorized, reviewed dependency input. Only compiled frontend
assets enter the installed public root; the archive/provenance must not be served.

The pinned Nix prefetcher needs a small adapter in the existing frontend package.
Reconcile this package against upstream WebUI
`63d484fc070dbee633d32624de545e834d483701` after implementer5 returns the shared Git
turn. Its source filter and buildNpmPackage structure retain this design; its
frontend dependency hash and root dependency lock have advanced. Generate the new
lock/hash from that rebased graph, preserving the upstream dependency changes.
Source inspection of nixpkgs `prefetch-npm-deps/src/parse/{lock,mod}.rs` and
`util.rs` shows that it treats `file:` URLs as ordinary download URLs and does not
resolve a repository-relative tarball. Preserve `buildNpmPackage` and
`fetchNpmDeps`: in the latter's standard preBuild/postBuild hooks, save the original
lock, omit **only** `packages["node_modules/vpsadmin-typescript-client"]` from the
temporary lock passed to the remote prefetcher, then restore the original lock
into the dependency-cache output. Validate source/provenance before this projection.
No second lock is committed. All other locked dependencies are fetched unchanged;
the cache's final `package-lock.json` must be byte-identical to the committed lock.
The frontend npm hook also needs the local-archive cache-map extension described
below. It retains its lock comparison and offline `npm ci`, which reads the local
archive and verifies the canonical lock's integrity. Use the
existing `makeCacheWritable` option for npm caching that local archive. Keep this
adapter local to the one frontend derivation, using existing Nix tools, with no
new pipeline, runtime download or publication service. Recompute the frontend
dependency-cache hash with this derivation's normal fixed-output hash workflow;
plain `prefetch-npm-deps package-lock.json` is no longer the correct root hash
command while this temporary pin is present. BFF lock/hash handling is unchanged.

The first full package check at WebUI
`1ab9853312a95b5448e99fd6f83f846453de17a5` exposed a second phase of the pinned
prefetcher that the initial design missed. The dependency-cache hash and exact
canonical lock comparison passed, then `npmConfigHook` called `--map-cache` and
`--fixup-lockfile`. Rust `src/main.rs:249–253` requires a map hash for every
non-Git package with `resolved` and `integrity`, including the restored local generated client
entry. `--map-cache` only inventories the prefetched registry cache, so the generated client
entry is absent and the fixer panics with `dependency should have a hash` before
npm installation. This is not a corrupted lock or a failed archive check. Exact
failure evidence is in [webui-nix-packages-result.md](webui-nix-packages-result.md)
and its log; the failing frontend derivation is
`/nix/store/faxyv39ik06gwgdjp6843zi7aglakmhi-vpsadmin-webui-frontend-1.0.0.drv`.
The inspected installed hook is
`/nix/store/sip9p1dkwr7y1b8lkzbcrjnwj8yfslsf-npm-config-hook/nix-support/setup-hook`.

Correct this through the existing `buildNpmPackage.npmConfigHook` interface and
`pkgs.npmHooks.override`, scoped to this frontend. Override that hook's
`prefetch-npm-deps` dependency with a small `writeShellScriptBin` adapter. Delegate
every invocation to the exact pinned upstream binary, preserving arguments and
failures. Only after a successful `--map-cache`, invoke the existing source checker
in an explicit cache-map mode to add the one local generated client entry to `CACHE_MAP_PATH`.
The ordinary hook then calls the unchanged upstream `--fixup-lockfile`; do not
catch its panic, skip it, patch its Rust, or copy/reimplement the npm hook.

The checker reuses its existing manifest/lock/provenance and regular-file checks,
computes the archive SHA512 from the actual bytes, and requires it to match the
canonical lock and receipt. Add precisely that lock entry's original `resolved`
string and verified SRI to the transient JSON map. Preserve every remote entry;
reject a conflicting existing generated client map value, and leave both map and lock unchanged
on validation failure. An already matching generated client entry is harmless. This map
extension describes checked source bytes that npm can read locally; it does not
claim the archive was downloaded into the remote cache. No map is committed and
no cache-index format is written. The canonical lock's generated client integrity remains
present throughout. The fetch projection/cache restoration, archive, root lock,
runtime, npm semantics and BFF hook remain unchanged.

Implementer2 owns only `packages/frontend.nix`, the existing
`scripts/check-package-source.mjs` and its tests, plus relevant packaging docs and
work-log correction. Export the already computed generated client identity from its check
internally rather than duplicating the hash/provenance rules. Quick coverage must
prove successful map extension preserves remote entries and the lock's exact
bytes, rejects tampered/missing archives and conflicting map values, and passes
the actual pinned `--fixup-lockfile` on a disposable copy without changing the
canonical lock. Also inspect/evaluate the selected hook to establish that the
frontend uses the adapter and BFF still uses upstream. This requires no dependency
install, generated client regeneration, archive/lock change or application JavaScript change.
The existing dependency-cache output is expected to remain byte-identical;
re-evaluate the exact derivation/input evidence and retain its hash only if that
holds. Report an unexpected cache or lock change before expanding the fix.

Commit the bounded fix after quick checks, then obtain affected packaging review
under the existing final-review workflow before the fresh watcher reruns the
failed package graph. Keep ordinary npm/browser success distinct from Nix package
success. The lead may run the prepared Vite browser batch independently because
its inputs are unchanged; preserve root/BFF node_modules and application inputs.
Serialize the Nix build watcher after that batch under the lead's one-watcher
limit. Any proposal to change the archive, canonical lock or application behavior
returns to the lead before edits. The architect diagnosis ran no build, install,
server, DB operation or retry. This narrow adapter is sufficient as a design;
actual package success remains to be demonstrated, with no alternative packaging
system added speculatively.

An immutable Git/source pin remains a larger alternative: the generated client exports ignored
`dist`, has build/prepack but no prepare hook, and npm's Git packing path runs
prepare rather than prepack. The current Git package therefore lacks exported
build files without a packaging change. Avoid adding that lifecycle or changing
the Nix dependency system for temporary support. The selected cost is about 337 KB
of binary Git history per retained candidate; keep only the current candidate in
the source tree and preserve exact review evidence. No absolute local paths,
expiring artifact URLs, mutable branch pins, invented registry integrity or old
generated client fallback are acceptable.

For an update, change client behavior in the HaveAPI generator, regenerate through
the generated client's sole tool, and complete its existing build/pack/check workflow. Copy the
verified archive with a new revision-qualified filename; never replace different
bytes under an existing candidate identity. Update the compact receipt and use
the pinned npm to generate the root manifest/lock, then update the frontend cache
hash. Do not edit generated code or the lock manually. A candidate may retain its
unpublished package version: full source revision, filename and integrity identify
the bytes. Remove the superseded archive from the current tree in the same change.

Acceptance is a clean checkout installing the named package from these exact bytes
with no generated client registry fetch or source build. Quick checks cover source-checker
success and meaningful missing/tampered/mismatched archive or lock failures,
documentation audit, clean-install ESM/type resolution and the affected generated client policy
consumer checks. Coordinate clean installs with the lead so active shared
`node_modules` is not replaced. Dependency-cache hash preparation is a necessary
packaging-input step; record its actual command/output. After all intended source
and metadata are committed and quick checks pass, include this support in final
WebUI review. Then run the existing frontend build and Nix source/package-content
checks on that exact head through the normal watcher workflow. They must prove
offline installation, retained archive source, matching provenance and absence of
the archive from public output. Stop on a concrete failure and repair the owning
boundary; do not broaden into another packaging system. No install/build/test or
server was run during this design investigation; package readiness remains
conditional on this implementation and its actual checks.

Returning to the registry requires a separately authorized, actually published
generated client artifact. Replace the file spec with its exact released version/integrity,
remove the temporary archive/provenance checks, Nix prefetch projection and
frontend cache-map adapter, and
regenerate the npm lock/cache hash with affected checks. Do not assume future
published bytes. Rollback restores a matching WebUI source/archive/lock/hash set;
an older frontend remains paired with its old dependency. No server state or
storage format changes result from this distribution choice.

No DB migrations, API product behavior changes, daemon/CLI/Terraform contract
changes or coordinated node update are inherent. Supported API revision/plugin
combinations remain explicit; a full-fixture snapshot is not live permission.
Capability checks must keep old/new API combinations safe. Do not automatically
select a new API default version. No session/settings storage changes are needed.
Rollback restores matching old frontend/dependency artifacts; accepted server
mutations continue and need existing reconciliation. Generator and generated client rollbacks
restore matching schema/provenance/source/manifest, not an edited generated tree.

Effort remains provisional: approximately 3–5 engineer-days for generator/generated client
foundation plus pilot, and 15–30 total for migration/verification, revised after
the pilot. Eight owners enable parallel domain work, not an eightfold elapsed-time
reduction. Scope gaps requiring backend behavior changes go to lead; client
capabilities are fixed in the generator. The lead maintains plan/state and user
communication. This brief is ready to release the first two execution packages.

### Upstream API 0.32.1 disposition

Read-only comparison of API `610a96f8ce523afbcd3e4374a70047dbe3264b0d` to
`097226b22edf8b59f80b5dfaa55265e9d0cac633` found ten changed dependency, exporter,
documentation and example-configuration files. No application resources,
authorization implementation, models or migrations change. The new API bundle
and controlled exporter select Ruby HaveAPI 0.32.1; this does not select the WebUI's
separate npm runtime or regenerate its generated client.

The local HaveAPI release-source comparison `v0.32.0` (`0e7166a0f8f15827bfac051666a53bf449e999ec`)
to `v0.32.1` (`9efeadf91d894e01d1d4f4a3e3fc64c6309785c7`) shows the only server
behavior change in `documentation_oauth.rb`: an optional static
`switch_user_revoke_params` hash is validated, copied and added only to a validated
documentation Switch user revoke request. The API example supplies `close_sso=1`
and recommends a dedicated documentation client with SSO enabled. Ordinary
documentation sign-out, API authentication, JSON/OPTIONS descriptions, resource
validation and response/global metadata framing retain their source behavior.
JavaScript client changes are version identifiers only; protocol 2.0 remains.
The documentation cookie does not authenticate API/OPTIONS requests. No generated
operation, executor, capability or WebUI auth change is justified by this diff.

There is a real configuration compatibility boundary: the new documentation hook
option requires the matching server release; loading it with HaveAPI 0.32.0 is
rejected at startup. Upgrade/rollback must pair that optional API configuration
with its bundle. New exporter guards also deliberately require 0.32.1, so the old
isolated tooling must not be relabeled as a capture of the newer source. These
are API operator/tooling boundaries, not reasons to alter the accepted generated client.

Retain unpublished generated client `99ee06654ef956a09b52749f4cd02d1435362087`, its archive/schema,
generator identity and npm HaveAPI 0.32.0. The successful 23-call isolated matrix
and cleanup evidence remain explicitly bound to API610a96/HaveAPI0.32.0; neither
they nor this source comparison certify a run against API097226/HaveAPI0.32.1 or
identify deployed software. No consumer contract gap was found requiring another
check for the frozen-input migration claim. If a later release targets API097226,
use the existing bounded isolated matrix with that source's declared tooling and
the same consumer bytes to establish its runtime claim; no new harness or
automatic schema/archive/runtime repin is warranted. This disposition performed
no fetch, code edit, install, test, build, database or deployment operation.

### Broader CI browser repair after the published migration

Run41366168907/attempt1 at published WebUI
`14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab` has real assertion failures before all
three jobs reach their native 40-minute timeout. Use W's
[completed diagnosis](w-final-ci-diagnosis.md),
`ci-41366168907-diagnosis/test-failure-summary.json` and the already verified
trace archives as the evidence authority. The 32/35/42 project-specific failure
headings span 30 spec paths; they are neither terminal suite totals nor 109
independent bugs. Preserve earlier core-CI/A124/B8/API23/Nix/review receipts for
their exact inputs and scope. They do not certify the larger cancelled matrix.

There is no demonstrated common default response defect to normalize away.
`e2e/fixtures/haveapi.ts` correctly wraps explicit handler results as supplied,
preserves explicit envelopes/HTTP errors and supplies minimal root description,
current-user and empty background-action defaults. Most observed candidates are
explicit leaf handlers, which a default change would not repair. Adding resource
namespaces, roles, localized text or coercions automatically would conceal the
tested contract and could turn intentional malformed responses into successes.
Keep that helper's semantics, fallback behavior and explicit malformed paths.
Use small canonical responses directly in the owning specs; no generated mock
registry, output decoder or shared compatibility framework.

Proven boundaries supporting immediate bounded packages are:

- W's original-attempt traces in all projects prove news rows lack `message`.
  `admin_dashboard.spec.ts` must supply the server-localized message for its
  actual cs/en scenario while retaining the translation fields needed by the
  editor. `narrowPublicNewsLog` remains strict. This first i7 package is independent.
- Explicit successful DELETE/maintenance handlers return `{}`, null or only
  metadata where generated operations require the resource namespace, including
  `dns_resolver`, `user_cluster_resource_package`, `environment`, `location`,
  `node`, `pool` and `vps`. Correct the successful fixture branch and preserve the
  existing rejection, uncertain-outcome, duplicate-submit and recovery branches.
  An empty declared object is `{resource:{}}`; add only metadata actually needed
  by the action and never invent an asynchronous receipt for a synchronous action.
- Lookup fixtures in mobile owner selection, resource-package filtering and
  network NOC provide full User.Index rows without `level`; account readers
  require the real account identity/role fields. Synthetic member fixtures may
  explicitly declare their member level; the router must not infer it. Pool
  fixtures use scalar `node:5` although the reader requires an included reference.
  Check that concrete response against the frozen schema/source before correction.
- Payment instruction fixtures put `instructions` outside `user`, income fixtures
  use `payment_stats` instead of `payment_stat`, and export/DNS/user-data fixtures
  return unnamespaced objects/arrays. These are explicit handler corrections.
  Transaction fixture `input`/`output` are objects despite declared string fields;
  preserve the intended displayed JSON content in the server's string form.
- The mail-log retained diff shows identical query pairs in a different order.
  Assert the exact pairs as an order-independent multiset, retaining duplicate,
  unexpected-key, cursor and lookahead checks. Do not change generated encoding.
  The user-reminder diff expects forbidden `remind_after_date:null`; retain the
  accepted expiration-date setter clear and its unchanged-other-fields assertion.
  User-status success scenarios use numeric booleans; distinguish them from
  intentional malformed cases before changing a fixture.

The table assigns every observed path once. Paths are relative to `e2e/specs/`;
ownership covers bounded fixture/assertion corrections after the lead grants
source work. Owners may immediately perform read-only original-trace/source
diagnosis. Unknown cases remain unknown until that evidence is inspected; this
table does not declare all failures fixture-only.

| Package / owner | Exact spec files | Boundary and dependencies |
| --- | --- | --- |
| C3 / implementer3 | `admin/os_templates_responsive_actions.spec.ts`; `app/backup_center.spec.ts`; `app/blocking_action_progress_modal.spec.ts`; `app/export_hosts_responsive_actions.spec.ts`; `app/mobile_lookup_popover.spec.ts`; `app/mobile_touch_interactions.spec.ts`; `app/mobile_workflows.spec.ts`; `app/profile_user_data.spec.ts` | VPS/storage/export namespaces and receipts; explicit User.Index fixtures; remaining restore/migration/touch behavior from retained traces. Consult i5 for user DTO facts and W for action receipt facts; those owners do not edit these specs. |
| C4 / implementer4 | `admin/cluster_dns_resolvers_smoke.spec.ts`; `admin/cluster_dns_tools_smoke.spec.ts`; `admin/ip_address_detail_page.spec.ts`; `app/admin_network_live_noc.spec.ts`; `app/incident_create_context.spec.ts` | DNS/IP success namespaces and scoped DNS record creation; explicit NOC user fixture. The observed incident-context failure is the DNS case; preserve unrelated cases in that mixed spec. |
| C5 / implementer5 | `admin/user_detail_page.spec.ts`; `admin/user_packages_bulk_remove.spec.ts`; `admin/user_payments_smoke.spec.ts`; `admin/user_security_delete_failures.spec.ts`; `admin/user_security_status_badges.spec.ts` | Reminder clear contract, delete namespace, canonical booleans; user-payment fixture uses i7's established instruction namespace. i5 remains sole editor of user payments spec/page; i7 supplies contract facts only. |
| C6 / implementer6 | `admin/cluster_resource_maintenance.spec.ts`; `admin/cluster_resource_packages_filter_contract.spec.ts`; `admin/cluster_summary_maintenance_smoke.spec.ts`; `admin/node_detail_control_center.spec.ts`; `admin/node_pool_maintenance.spec.ts`; `app/action_state_transactions_responsive.spec.ts` | Maintenance response/route/OPTIONS evidence, pool references, lookup user and transaction wire fields. W owns action-state production code; C6 owns the mixed transaction fixture, requesting W diagnosis only if a real shared defect remains. |
| C7 / implementer7 | `admin/admin_dashboard.spec.ts`; `admin/mailer_log_smoke.spec.ts`; `admin/requests_operations_smoke.spec.ts`; `app/admin_income_forecast.spec.ts`; `app/payment_qr_images.spec.ts` | Known localized-news correction first; exact query pairs; payment namespaces. Inspect three request failures for eligible-template/profile fixtures and actual preflight behavior. Do not assume their timeouts are caused only by namespace framing. |
| CW / implementer2 | `app/centered_dialogs.spec.ts`; shared E2E type-coverage inventory/config and final technical docs/work-log | Five observed routes need individual diagnosis. The broad `fallbackResponse:[]` is invalid for namespaced reads; use only the explicit route responses needed by the scenario. User-data filters no longer expose the former advanced dialog, while environment/location/network/system-config still contain controls. Verify actual trace/locale/selector before changing those expectations. Preserve coverage of the current supported controls; no skip or product-control reintroduction. |

CW alone edits `scripts/fixtures/e2e-type-coverage.json`, `tsconfig.e2e.json` and
shared fixture/docs files if required. Each leaf owner supplies its final changed
file list and zero-diagnostic typing fixes; CW adopts edited deferred specs under
the existing coverage policy rather than merely refreshing hashes to conceal
errors. Keep malformed fixture values explicitly intentional instead of casting
them into generated success DTOs. Prefer generated output types for canonical
fixture rows when that catches the actual regression. No new blanket E2E typing
campaign, product source change, runtime shim, generated client repack or pin update is included.
Any valid API payload rejected by the product, or changed user-visible behavior,
returns to the lead before edits with its actual boundary evidence.

For each causal cluster, inspect one original failing trace plus the implicated
handler/reader and compare other owned occurrences before applying the same fix.
Record the exact request/response or assertion mismatch, test intent, and whether
the proposed change is fixture, assertion or product. Preserve explicit malformed
responses, server rejections, partial success, ambiguous mutation/no-replay,
identity/permission restrictions, exact write counts and frozen review values.
Only observed failures and proven repeated local causes in the owned specs are
in scope. No other artifact retrieval or whole-suite source audit is needed.

Owner trace confirmations refine the initial candidates without changing product
scope. C7 confirms that request cases309/1271 never submit because template5 lacks
the admin-visible `enabled`/`supported` flags; case611 supplies no required lookup
handlers and receives `{}`. Supply the explicitly eligible scenario's canonical
template/location/node responses, preserving preflight rejection and no-replay
assertions. The QR case fails at `response.instructions` before QR interaction;
its correction is `response.user.instructions`. C4 confirms successful retry
responses lack the DNS/HostIP resource namespace, NOC's synthetic member lacks
`level`, and DNS context has both an unnamespaced Show and a scalar included
`dns_zone` in Create output. Correct only those fixtures; the request still sends
the numeric zone ID and exactly one write. C5 confirms the package-delete empty
response causes an uncertain stop before the next selected row, and account-status
success scenarios supply numeric instead of boolean flags. It also identifies a
later assertion in the same payment case that expects the already unsupported
populated `paid_until` clear: assert the approved visible refusal and no dispatch,
not a new clear behavior. Its reminder mock must emulate the actual expiration
setter clearing the reminder. These are original-trace/source findings, not new
test-pass claims. Full User reads require id/login/level; included user references
remain partial and must not gain an artificial level requirement.
C6 confirms those environment/user/pool/transaction boundary failures in original
Chromium traces. Its node fixture is rejected before capability probing because
`maintenance_lock:false` is not the declared string value (`'no'` for this
scenario). Cluster summary instead has log/source evidence: the bare full-stats
response prevents the first Lock control from loading. No original summary trace
was found in the retained artifact indices; retain that evidence limitation and
verify the namespace correction in the focused run rather than claiming a trace.

After source release, quick checks are changed-spec strict typing via the existing
E2E coverage mechanism and applicable scoped lint/docs checks; shared helper tests
are needed only if a concrete shared change becomes necessary. The lead batches
browser checks through the existing watcher after the committed batch's affected
review. For the coherent six-package head4279c238/tree
`d37a454e`, use the lead's prepared native Playwright1.61 `--test-list`: it maps
the 109 original headings to 100 exact case/project pairs (32 Chromium and
68 mobile Chrome), projecting original WebKit cases onto the existing mobile
context and deduplicating nine overlaps. The former user-data Advanced title maps
explicitly to its retained supported-editor case. The lead reports list-only
preflight selected exactly100 cases/30 specs with no errors; this is selection
evidence, not browser execution.

Run the two Chromium news-shortcut cases first. If they pass on unchanged inputs,
run the remaining98 selected cases once, retaining mobile news and all observed
locale/recovery variants. This covers the representative and remaining cases
together; no extra intermediate representative batch is required. Preserve the
native relative file/title list, `--workers=2 --retries=0 --max-failures=1` and
900-second global timeout for the remaining batch. Mobile `.tap` cases use the
existing mobile Chrome project. On failure, stop and diagnose the retained trace;
retries or larger budgets are not evidence of correction. These diagnostic lists
do not change the committed CI selection or certify unrun cases. If source changes
after the first gate, reconcile affected inputs before reusing that result.

Keep the available local pairing Playwright npm1.61.0/Nix Chromium1228. Many WebKit
failures stop at the same protocol/fixture boundary before any engine-specific
interaction, so retained traces and focused Chromium can establish that correction
without installing another engine. Actual WebKit touch/layout acceptance remains
the existing CI project. If a remaining failure requires local WebKit, i7 may
answer only the read-only environment question: whether the exact installed
Playwright version already has its matching WebKit executable/dependencies in an
approved environment. No downloads, host changes, alternate browser or harness.

Keep the reviewed published14cfd ref and its evidence. Use normal logical fix
commits for settled owner packages; serialize shared edits/Git through the lead.
Assess one final consolidation after the batch settles, retaining the old/new
range and actual delta; do not rewrite after every finding. Perform affected
independent review and final-head reconciliation before one normal CI run with
the unchanged three-project selection/40-minute limit. Full success requires
completed reports for that head, not absence of early annotations. A further
timeout after actual failures are resolved requires its own measured disposition.
The architect made only this design update and read-only inspections; no source,
Git mutation, checks, installs, browser, server or database action was performed.

## Optional local client development and terminology

2026-11-02, separate milestone after the migration and local verification. The
user wants optional unreleased/local-checkout consumption while merged code uses
released `vpsadmin-typescript-client`, and requests “generated TypeScript client
for the vpsAdmin API” or “generated client” in place of the introduced shorthand.
Lead accepted the workflow below. This brief grants no registry publication,
release tag, default-branch integration or deployment. Its source baseline is
WebUI `d3d5efbef53af8eb1caec025737dc47ecbc67e96`, HaveAPI
`eea3ae5e82c3db23d5f5bc9f1a5e7784117c4e1b`, and client
`99ee06654ef956a09b52749f4cd02d1435362087`. Existing receipts and pending CI remain
evidence for their original inputs; none verifies this new milestone.

### Optional workflow and committed default

Document ordinary npm commands in WebUI's existing `HAVEAPI_CLIENT.md`, with a
short packaging cross-reference. No installer, npm script, Vite alias, symlink,
environment-switch framework, Git prepare hook or second lockfile is needed.

1. In the chosen client checkout's pinned `nix develop`, use its existing
   `npm ci --ignore-scripts --no-audit --no-fund`, then `npm run build` and
   `npm pack --ignore-scripts --pack-destination /path/to/private-output`.
   The explicit successful build must precede packing with scripts disabled.
   Use the exact resulting filename, not a wildcard, and record the checkout
   revision/dirty status and archive digest when sharing verification results.
   Keep local output outside WebUI's source tree. A previously built, checked
   exact archive can be used directly without rebuilding it.
2. In WebUI's pinned development shell, start with `npm ci`, then install the
   chosen archive with `npm install --no-save --package-lock=false --ignore-scripts
   /absolute/path/to/the-exact-archive.tgz`. This is a temporary `node_modules`
   override; do not edit the committed manifest, lock, vendor archive or provenance.
   `package-lock=false` ignores the lock during this install, so other temporary
   dependencies can also change. Verify the selected client entrypoint and the
   actual HaveAPI peer version; do not force incompatible peers or claim the
   whole installed tree still equals the canonical lock.
3. Run ordinary typechecking and focused consumer checks against that installation.
   Restart Vite using `npm run dev -- --force` so dependency prebundling does not
   retain the previous archive. Rebuild, pack and reinstall after client changes;
   this is an explicit snapshot workflow, not live source watching.
4. To leave the override, use `npm ci` and restart Vite with `--force` again.
   Confirm manifest/lock/vendor/provenance are unchanged and the installed client
   resolves to the committed input. No `npm uninstall` or global-link cleanup is
   part of this workflow. Coordinate installs with other local runners because
   they replace the application's temporary dependency tree.

Package inspection and i1's independent read-only confirmation establish that
exports point to ignored `dist/index.js` and `dist/index.d.ts`, the package is
ESM/ES2022, prepack builds, and there is no prepare/install hook. A source folder
or `npm link` adds unnecessary symlink, peer-resolution and Vite-cache behavior;
the packed archive follows the same public package exports as a release. These
commands have not yet been exercised for the new optional workflow.

Building compiles checked-in generated source; it does not regenerate or certify
its provenance. Actual generated behavior changes still start in HaveAPI and use
the client's sole regeneration command. That command checks the exact recorded
HaveAPI HEAD before source digests; equal source at another revision is not a
bypass. Preserve schema, runtime, generator and generated-file ownership rules.

The committed registry dependency is a **pre-merge prerequisite**, separate from
implementing this optional workflow. No compatible published version has been
selected by this investigation. Keep the existing exact unpublished99ee archive
until an actually available compatible release is selected under the ordinary
dependency-update process. Do not invent a version or infer publication consent.
The temporary Nix projection/cache-map adapter remains necessary for the current
committed `file:` dependency. Optional local npm development does not use it and
does not justify a permanent optional Nix archive mode. At registry transition,
remove that adapter and archive-specific checks/input, generate the ordinary
registry lock/integrity and frontend cache hash, and run affected package checks.
The documented local override remains usable afterward.

Nix builds use the committed source/lock/archive; `nix/source.nix` excludes
`node_modules` and `.vite`. They do not verify a developer's no-save override.
The isolated API runner is outside this override workflow; use it only with its
separately verified archive and receipt under the existing runner procedure.
Its explicit receipt, archive digest and selected installed-file comparisons do
not establish universal package provenance for an arbitrary override. An npm/Vite
build with local dependencies is development
evidence, not a reproducible release artifact. There is no API, database, storage,
daemon or persisted-format change. Recovery is `npm ci` plus the Vite cache restart;
official package rollback still restores the matching committed dependency set.

### Exact wording boundary and package identities

The inventory compares only additions in HaveAPI `391b0190..eea3ae5e`, client
`e5786f69..99ee0665`, and WebUI `63d484fc..d3d5efbe`, plus those feature messages.
Keep unrelated upstream prose/history, machine identifiers and all verbatim
review reports, original commands, artifact paths, quoted user instructions and
receipts intact. This is not a repository/package rename or a generated-code edit.

HaveAPI has one introduced prose occurrence in `clients/typescript/README.md`;
the client has one in `README.md`'s live-description paragraph. Neither feature
commit message contains the shorthand. Use ordinary documentation follow-up
commits for these two corrections; do not rewrite those existing feature commits
or repin the generator merely because documentation advanced. HaveAPI's generator
digest enumerates bin/lib/template/Gemfile/gemspec/Rakefile, not README. The
recorded exact generator revision remains eea3ae5e and remains an ancestor of the
documentation follow-up; regeneration must still use that exact checkout.

The client's README **is included** in the frozen337414-byte archive. Its
`docs/development.md` and build/regeneration scripts are not included. A newly
packed README correction therefore changes archive bytes and integrity even if
all `dist` files are equal. The smallest disposition for this milestone is to
correct the current source README and retain99ee unchanged as the explicitly
earlier selected artifact. Do not relabel it as the later documentation commit
or rewrite its internal prose. Defer a new artifact to the separately necessary
dependency/release selection; this avoids an otherwise unnecessary intermediate
candidate and Nix pin cycle. The final selected release must contain the corrected
README. This preserves historical artifacts rather than asserting they contain
the new wording.

If a separately approved candidate update is needed before that release, use the
existing build/pack/archive checker once: record the new client revision, compare
actual `dist` and generated-source/manifest bytes, keep unchanged generator/schema
identities truthful, and record fresh archive digests. WebUI must then update its
revision-qualified filename, provenance, npm-generated manifest/lock/integrity and
affected Nix cache evidence together. Do not synthesize new integrity from code
equality. An actual generator reword/rewritten revision would additionally require
a deliberate client generator-pin update and exact-revision regeneration check;
the manifest stores source digest, not Git HEAD, so it need not change when those
inputs are unchanged. Neither cascade is required by the chosen follow-up-only
documentation scope.

The final exact WebUI inventory is **nine affected messages, not ten** (correcting
the preliminary checkpoint): `b46c3d1e`, `8d54820f`, `28556527`, `7a382aed`,
`a42ff72e`, `083da898`, `55f0e1ac`, `14cfdcb6`, and `dba717ba`. They contain fifteen
occurrences in subjects/bodies. Change the wording only. Rewriting these ancestors
changes subsequent WebUI commit IDs, including messages that need no edit; it
does not change any client/generator/archive input by itself.

### Owners, files and serialized delivery

Lead accepted this brief and released the complete packages below. The two README
follow-ups can proceed independently. WebUI has a strict sequence: implementer5
alone owns the message-only history turn, then returns that turn with its proof
to lead. Implementer2 may touch WebUI only after lead accepts the proof and the
turn return. The existing d3d5efbe CI watch continues for its original scope.

| Owner | Exact boundary |
| --- | --- |
| implementer0 | HaveAPI `clients/typescript/README.md`: introduced sentence only; normal documentation follow-up, unchanged generator source/version/message/pin. |
| implementer1 | Client `README.md`: introduced live-description sentence only; normal documentation follow-up, no generated files, package metadata, archive or provenance change. |
| implementer2 | WebUI optional procedure plus introduced wording in `docs/design/{API_CONTRACTS,ARCHITECTURE,HAVEAPI_CLIENT,PACKAGING,REQUIREMENTS}.md` and `docs/work-log/2026-11-01-typescript-client-migration.md`; diagnostics/test descriptions in `scripts/check-package-source.{mjs,test.mjs}`, `scripts/integration/vpsadmin-sdk-contract.{mjs,rb}`, `src/lib/api/{sdk.test,sdk.wire.test,systemConfig.test,vps.receipts.test}.ts`, and `src/pages/app/admin/nodes/NodeLifecycleModel.test.ts`. Update directly paired diagnostic assertions only where required. No guard or behavior change. |
| implementer5 | Sole WebUI message-only history turn: nine message corrections and descendant reconstruction, retained original refs and exact old/new proof; report turn return to lead before implementer2 edits. |
| Lead | Accept history proof and release the WebUI source turn; own PR wording and current plan/state/backlog/portal terminology. Preserve original evidence. |
| architect0 | Reconcile author narration in this design and `contract-dispositions.md`; retain exact quotations, historical commands/paths/identifiers, original reports and receipt facts. |

Keep existing filenames/imports such as `sdk.ts`, integration script paths and
cache-map flags unchanged. They are internal identifiers; renaming them would
expand the task into import/inventory churn without improving the requested
human-facing explanation. New prose uses “generated client”; code/error strings
and synthetic fixture labels in the listed additions receive the same correction.
Do not introduce a broad replacement across upstream files or archived evidence.

For WebUI, first retain the published d3d5efbe ref and complete base/head series.
Perform one message-only reconstruction with original authors and author/committer
dates retained, recording old/new commit mapping. Verify every mapped tree/patch,
unchanged base, final tree equality, and only the selected message wording changes
apart from unavoidable commit parent/identity/signature metadata. Use required
hooks; no hook bypass. Implementer5's short acceptance packet to lead must identify
the retained original base/head, new head, mapping, equal trees/patches and
preserved authors/dates, with any exception stated explicitly. It must also state
that the Git turn has returned. After lead accepts that packet, implementer2 adds
the separate logical documentation/wording source commit. This makes the
history-only change and real source delta independently
reviewable. Avoid repeated per-message rewrites or folding unrelated repairs into
this step. Any later publication uses the lead's normal protected feature push
and exact-head CI rules; this brief does not perform it.

Quick acceptance is the bounded added-line/message inventory, documentation/link
audit, lint for changed scripts/tests and their focused existing checks, unchanged
dependency/generated identities, and exact history/tree mapping. No full browser
or real API campaign is justified by prose and diagnostic-label changes. After
committed affected review, exercise one isolated optional install/restore cycle
using the existing immutable archive or an authorized built candidate, ordinary
WebUI typecheck/focused binding tests, Vite forced dependency resolution, and
manifest/lock/peer/restoration evidence. Use the existing monitor workflow for
long commands, with no new harness. Any later new archive or registry transition
requires the existing exact-archive consumer check and affected npm/Nix package
acceptance. Preserve old Nix and API/browser receipts for their actual inputs;
new head/provenance claims require the normal final-head reconciliation.

This investigation used source/docs/history reads and i1's read-only package
confirmation. It ran no builds, tests, installs, regeneration, packing, browser,
API/DB action, fetch or history mutation. Application changes remain lead-released.

## Second browser-CI repair: 27 additional observed spec paths

2026-11-02. This is a separate acceptance milestone after the first browser repair
and optional-client/terminology work. Use i0's
[completed second-run diagnosis](w-ci-second-diagnosis.md) and
`ci-41450042371-diagnosis/test-failure-summary.json`, not another download or
inventory. Run41450042371/attempt1 tested exactly WebUI
`d3d5efbef53af8eb1caec025737dc47ecbc67e96`. All three authoritative annotations
report the native40-minute timeout. Before cancellation there were103 observed
failure headings (32 Chromium,30 mobile Chrome,41 mobile WebKit),70 identities
ignoring project, across27 paths. All27 paths are outside the earlier30-path
inventory/local100-case mapping. These are not terminal totals; absence of an
old failure from the new stream does not certify its pass. Selection/progress
differences mean WebKit-only observations are not evidence of engine defects.

The optional workflow has its own completed review and narrow A1 prose correction.
Its isolated override/restore cycle against WebUI8d0bb48a and client e166 passed
in236.009 seconds; see the
[lead acceptance](local-client-cycle-lead-acceptance.json). The subsequent27-spec
repair and two metadata files are committed, with scoped checks and combined
strict coverage134/148 passing. The A1-only fold3df72b3 and five equal-patch
replays produced the reviewed repair head
`96d9c996f3556a8e5d4322e79c11b0657564d33d`, tree
`1b6d0639818b12ba496c304f78d4d900ce6836a5`. All16 mapped predecessors are untouched
and old refs remain retained; see the
[final inventory](webui-second-ci-final-inventory.json) and
[fold proof](webui-second-ci-fold-lead-proof.json). That affected review completed
with zero Blocking, Important or Advisory findings. The two subsequent advisory
fixture models, committed in129bf840 and3ca34e34, also passed their final affected
reviews with zero findings; see the
[creation-fixture review](webui-second-ci-advisory-followup-review-result.md) and
[node-workflow review](webui-second-ci-node-workflow-review-result.md).

The local220-case selection is now accepted:164 actual passes at3ca34e34 plus56
passes with proved unchanged inputs cover the original220 unique cases across
27 specs (110 Chromium and110 mobile Chrome). All12 advisory cases passed fresh.
The [aggregate](second-ci-browser-aggregate.json) and
[lead acceptance](second-ci-browser-lead-acceptance.json) preserve exact case/input
coverage. All three runs' native effects are resolved; the unrelated older Bash
process was left untouched. This is not a global process-absence claim.

The factual work-log-only commit
`9d9617c048dded592b6362e3370d92cfca2793cb` is now published on the feature branch;
PR126 wording was verified by lead, main63d484fc remains unchanged, and Git turns
are returned. All five literal9d Nix outputs passed in66.766 seconds. The
[Nix lead acceptance](webui-second-ci-final-nix-lead-acceptance.json) records both
schema1 metadata files at exact clean9d and the complete graph of1801 derivations,
9049 edges,281 source inputs and25 protected inputs. This does not infer equality
with earlier derivations or a shell-free BFF closure.

At the lead's supplied checkpoint, CI41480946099/attempt1 at exact9d has all three
jobs successful. Native Playwright41480945591/attempt1 remains active under its
single watcher, with the existing three projects and40-minute limits unchanged.
Broader native browser acceptance remains pending. The user keeps the release
transition pending; no merge, publication or deployment authority is inferred.
The corrected optional-runner wording above follows the reviewer: its existing
receipt/archive/selected-file checks are not universal package provenance.

### Evidence and settled repair boundaries

i0 alone retrieved and digest-verified the mobile Chrome archive and, for seven
paths without Chrome traces, the one mobile WebKit archive. Both local ZIPs and
member indices are in the evidence directory. Owners read selected original
nested trace ZIPs in memory. No per-owner download, whole-archive extraction or
new Chromium retrieval is needed for the currently identified contracts.

Confidence labels below distinguish original trace plus source proof from
source/native-log proof and pending diagnosis. They do not substitute for browser
acceptance after changes. Every original negative, authorization, uncertainty,
no-replay, exact mutation-count, cursor, secret and viewport assertion remains.

- **Trace + source, Dataset Show.** Architect independently read the original
  mobile Chrome `app-dataset_downloads_keys-fa24e-*` trace. HTTP200 returns
  `response:{id:10,...}` without `dataset`; generated Show requires `dataset` and
  the HaveAPI decoder rejects before the view guard. The page shows “Failed to
  load dataset” and sends no snapshot-download request. Correct the explicit
  successful Show fixture, not the decoder or pagination. i3's original snapshot
  export trace `6c5fe` proves the same earlier failure before any picker request.
- **Trace + source, accepted deletes/mutations.** i3's snapshot-delete `49e5f`
  carries only action metadata instead of `snapshot:{}` plus that existing
  metadata. i4's relation/TSIG originals `5265c`/`313f3`, i5's known-device/metrics/
  namespace originals `c5c1e`/`ea9c6`/`b0ac4`/`c9573`, and i6's monitoring/advisory
  originals `78a8f`/`1c1c4`/`85e0e` fail at their declared output namespaces after
  the expected rejection. Correct only successful replies to their actual
  resource names. Preserve metadata already supplied for asynchronous actions;
  invent none for synchronous actions. A success `{ok:true}`, null or metadata
  alone is not a canonical empty resource response.
- **Trace + source, DNS read/association fixtures.** i4's originals `1f735`,
  `e1dd8`, `3b223` show raw zone Show responses preventing capabilities/logs/records
  from loading. Use `dns_zone` framing and actual partial `{id:10}` references
  where output currently supplies scalar10. Numeric input zone IDs stay unchanged;
  shared guards and transport stay strict.
- **Trace + source, full account and negative URI reachability.** i5's mail
  `a5b54` reaches successful User.Update but lacks the required login/level; return
  the same explicit synthetic member identity as its GET fixture. Partial included
  users do not acquire role requirements. TOTP `51c2e` lacks `totp_device` framing,
  so the intended unsafe-URI assertion never runs. Wrap the existing device,
  preserving the literal unsafe URI and zero clickable links.
- **Source/native-log only for now.** i3 found bare export Show/meta-only accepted
  delete replies, and storage-section scalar `dns_resolver:'inherit'` plus bare
  Dataset Show. Their failing headings exist but original trace members are absent
  from the retained smaller archive. Exact generated descriptors/readers and the
  leaf handler can justify an unambiguous canonical fixture correction with this
  weaker claim; do not call it trace-proven. If source cannot distinguish a
  fixture defect from valid-output rejection, stop that specific case for lead.
- **Trace + source, WebKit confirmations now complete.** i3's preference originals
  `82789`/`72545` require `vps:{}` alongside the existing asynchronous receipt or
  by itself for the synchronous boolean update. Keep their distinct completion
  and read-back policies. Console original `3bf36` requires `console_token`
  framing; console-page `b4b18` instead first fails on the fixture's primitive
  `dns_resolver:'inherit'`, which must use the supported null inherited value.
  Rescue original `29201` never reaches boot because exact template Show5 falls
  through to `{}`: provide the canonical selected template before exercising the
  unchanged boot uncertainty/receipt negatives. Empty VPS action data is `{}`,
  not null; an intentionally missing receipt remains missing after framing is
  corrected. i4's DNS-shortcut original `2deaa` proves accepted resolver-only
  PUT plus action801 lacks `vps:{}` despite successful server read-back. The same
  leaf helper covers its four role/locale variants; do not change the payload.
  i6's transaction originals `382c7`/`5fbbd` return object-valued `output` where
  API610, client99ee and the reader require string|null. Serialize those explicit
  success/error objects with JSON.stringify, retaining existing input strings,
  contents and display/search/pin/copy assertions. These originals demonstrate
  fixture failures before the affected behavior, not engine/layout defects.

### Complete disjoint packages

All paths below are relative to `e2e/specs/app/` and end in `.spec.ts`. The owners
completed these packages under lead's serialized source/Git grants at their saved
settings. The table retains the accepted ownership and repair boundaries.

| Owner | Exact spec stems | Scope and dependencies |
| --- | --- | --- |
| implementer3 (11) | `dataset_download_delete_confirm`; `dataset_downloads_keyset_pagination`; `dataset_snapshots_keyset_pagination`; `export_delete_failures`; `snapshot_delete_availability`; `snapshot_export_shortcut`; `storage_sections_contract`; `vps_admin_modifications`; `vps_console_controls`; `vps_console_page`; `vps_console_viewport` | Dataset/snapshot/export positive framing and partial references; preserve supported filter/cursor/download tests. Console/preference/rescue first boundaries now confirmed by WebKit originals above. Keep source/log limitations for export/storage explicit. No production VPS/storage edits. |
| implementer4 (7) | `dns_record_type_capabilities`; `dns_relation_delete_failures`; `dns_tsig_keys`; `dns_zone_delete`; `dns_zone_logs_keyset_pagination`; `dns_zone_records_live_contract`; `vps_dns_shortcut` | All seven have settled positive-framing/reference corrections; preserve capabilities, managed records, paging, rejection and scope. DNS shortcut belongs to i4 alone despite its VPS location; original WebKit trace confirms the missing VPS namespace. Consult i3 only for concrete VPS contract facts. |
| implementer5 (5) | `known_devices_keyset_pagination`; `profile_mail_settings_failure`; `profile_metrics_tokens`; `profile_mfa_recovery`; `profile_user_namespaces` | All five have original mobile Chrome proof. Correct known_device/metrics_access_token/entry/user_namespace_map successful framing, explicit full member identity and TOTP framing. Preserve uncalled route-change stubs and every intended malformed/security scenario. |
| implementer6 (4) | `monitoring_event_action_feedback`; `security_advisories_admin`; `transactions_readability`; `transactions_table_followup` | All four settled: monitored_event, security_advisory and outage_security_advisory empty resource success; transaction output objects serialized as their declared strings. No new revision precondition or receipt. Preserve advisory concurrency/locales and transaction display/search intent. |
| implementer2 (shared metadata only) | `scripts/fixtures/e2e-type-coverage.json`, `tsconfig.e2e.json`, necessary existing technical work-log/inventory records | Sole edited-whole-file adoption owner after leaf files settle. Owners fix diagnostics in their leaf files; adopt edited deferred files under existing strict options. No baseline/hash refresh to conceal errors, shared mock rewrite or new typing campaign. |

No common mock normalization is warranted by the proven failures: explicit leaf
handlers supply the wrong successful framing. Keep `installHaveApiMock`, generated
client/runtime/archive/schema and production guards unchanged. Do not add fields
to every row, fabricate completion receipts, coerce null/absence or introduce a
second DTO mapping layer. Keep the existing intentional malformed fixtures at
their intended failure boundary. A valid API response rejected by production or
any material visible behavior change returns to lead with exact evidence first.

### Acceptance, delivery and stopping condition

Owners supplied exact changed paths, causal trace/source references, confidence
limits and passing focused strict leaf typing/lint using existing tooling. Prefer generated
types for canonical fixture rows where they catch the actual mismatch; do not cast
malformed fixtures into success types. W completed whole-file adoption; combined
strict coverage and scoped checks passed before the serialized commits and
completed affected reviews. The final inventory and fold proof above preserve the
published d3d5 range, optional-workflow evidence and consolidated series.

After committed review, the existing native Playwright selection covered all
applicable existing cases in these27 touched specs, including their negative and
later workflow steps, rather than only the103 first-failure headings. Lead's
ordinary list-only preflight recorded exact case/project selection and excluded
unsupported desktop `.tap` combinations; the execution and continuation evidence
is linked above. Retain the
available npm Playwright1.61.0/Nix Chromium1228 pairing. Desktop behavior uses
Chromium; touch/320px behavior uses the existing mobile Chrome context. Project
original WebKit-only cases onto that context only with an explicit mapping; real
WebKit acceptance remains its native CI project. No engine installation is part
of this repair. If a remaining engine-specific question requires local WebKit,
i7 may answer only whether the exact matching executable/dependencies already
exist in an approved environment.

Use the existing watcher/driver, two workers, zero retries and stop on the first
failure, retaining the existing900-second bounded diagnostic cap. Selection may
be split once by existing desktop/mobile context if native enumeration requires
it; do not repeat representative cases in another pre-gate. This broader touched-
spec selection tests later steps hidden by the initial failures and reduces blind
full-CI retries without auditing unrelated specs or changing CI selection/caps.
If it cannot finish within the bound, record completed/unrun scope and assess the
measured remainder; do not automatically increase caps. On failure, inspect its
first actual boundary and fix only the owning cause before resuming affected
acceptance. Do not rerun the full1482 selected CI cases as local diagnosis.

Scoped local acceptance has passed; the active exact-final-head browser CI must
still establish the larger selection and native WebKit claim. Timeout alone does not justify skips,
retries, cap growth or an unseen-pass claim. New failures outside this bounded
scope require concrete triage, not a whole-fixture hardening project. No backend,
database, runtime/package, release, deployment or persisted-format change is
proposed. Rollback is the matching ordinary feature source; no state recovery
operation is introduced. Architect work here is design/evidence only: no browser,
build, install, API/DB, source/Git mutation or CI action was launched.

### Final native CI: expiration/reactivation observation

At published9d9617c, run41480945591/attempt1 is terminal failure: mobile WebKit
job125398757644 failed after35m21s, and the Chromium/mobile Chrome native
conclusions are cancelled. No cancellation actor is inferred. The raw UTC span
16:23:16..17:04:40 is41m24s; preserve the original watcher report but do not adopt
its inconsistent elapsed-time statement. Seven WebKit annotations are not seven
independent causes or a full-run tally; i0 owns the native case inventory.
The initial assigned diagnosis is only
`app/vps_expiration_reactivation.spec.ts:69`, where the shared `save()` assertion
finds `lifetimes.admin.modal` still visible. The populated local combined log
`webui-second-ci-final-ci/run-41480945591.log` identifies the caller as line88 in
both cs/en cases: the reminder-setting save immediately after Start, the second
helper invocation. Initial reactivation save74 completed; reminder-clear91 and
expiration-clear96 were not reached. The earlier empty per-job log was not the
populated evidence source.

The original retry0 cs/en WebKit traces now prove the cause. Each records one
successful reactivation PUT, then one Start POST with HTTP200
`{status:true,response:{_meta:{action_state_id:702}}}`. Generated Start requires
`vps:{}` alongside that metadata. There is no action702 read and no second PUT.
English snapshots show “Missing response namespace”; both locales then show
`LocalLockPersistenceError` with the previous-operation-uncertain message in the
lifetime modal. The uncertainty guard correctly blocks the subsequent write.
This proves a successful-fixture framing defect, not an engine, production-lock
or timing defect. The earlier Update fixture already supplies `vps` and action701.

The watcher has exited. i0 owns the observed-case inventory and retained archive
custody; architect does not duplicate inventory or download. Original lifetime
trace/context paths and hashes are linked in the
[third-run inventory](webui-third-ci-observed-inventory.md). The accepted minimal
i3 repair is the same leaf's explicit
successful Start response `{vps:{},_meta:{action_state_id:702}}`, preserving cs/en, exact state/date
payloads, one Start, reminder-clear-through-expiration and explicit-null-reminder
rejection. No speculative wait, sleep, timeout change or unlock bypass is needed.
Source grants remain lead-owned. Scoped strict/lint and narrow affected review precede the focused
existing scenario checks; no blind retry, timeout increase, skip or normalization.
Prior220 local acceptance and literal9d Nix evidence retain their recorded scope.

### Third-CI packages: exact observed scope

Lead accepted i0's [native inventory](webui-third-ci-observed-inventory.md) and
[case/member selection](webui-third-ci-observed-selection.json):52 project-specific
failure headings,36 identities ignoring engine,11 paths, all outside the prior
30/27-path repairs and local220 identities. WebKit has actual terminal totals of
7 failed,2 skipped,267 passed; Chrome jobs have incomplete totals and cancelled
conclusions. No available job-cap annotation establishes their cancellation cause.
Retain that distinction and raw41m24s span; do not infer missing passes or an actor.

Only the lifetime cause above is established at this design checkpoint. The other
ten paths are diagnosis-first packages, not declared fixture defects. Every owner
uses the original failing case's retained evidence and directly implicated
reader/generated contract before changing its leaf. One original per actual cause
cluster plus source comparison can establish repeated same-leaf occurrences; do
not audit unrelated specs or assume all occurrences share the first cause.

Lead has released i0 alone to acquire/index the accepted mobile Chrome196MB and
Chromium313MB artifacts, mapping19 additional mobile Chrome and10 Chromium original
retry0 traces/error contexts. The verified57MB WebKit report already contains its
seven originals; the duplicate74MB WebKit archive remains held. Owners consume
i0's local selected-member map, not their own downloads or inventories. Exact
Chrome-only/mobile-only title gaps are explicit in that selection: in particular,
task-drawer originals require Chromium, while the VPS tabs failure is mobile
Chrome only. Do not substitute a similarly named case or another engine as its
original evidence. Missing members remain a stated limitation routed through lead
and i0; no automatic additional acquisition.

The following are complete nonoverlapping packages for lead release. All leaf
paths are under `e2e/specs/app/` and end in `.spec.ts`. Source baseline is frozen
published9d9617c; runtime0.32.0, generated client99ee and API610 contracts remain.

| Owner | Exact spec stems | Diagnosis and allowed correction boundary |
| --- | --- | --- |
| implementer3 (7) | `user_data_editor_accessibility`; `vps_access_page`; `vps_create_admin_flow`; `vps_create_failures`; `vps_detail_tabs_matrix`; `vps_expiration_reactivation`; `vps_initialization_templates` | Apply the proven lifetime success framing correction. Diagnose the other six paths from their actual selected originals before correcting explicit fixtures or obsolete assertions against the accepted product contract. Preserve keyboard/accessibility, access-token/security, create-failure/uncertain-write, role/template eligibility, tabs and initialization intent. No product control or eligibility change. |
| implementer6 (3) | `tasks_drawer_focus_trap`; `transaction_chain_detail_page`; `transaction_detail_page` | Diagnose actual drawer/chain/detail first boundaries; do not infer focus or layout defects from missing content. Preserve keyboard focus/escape/return, transaction scope, search, secret handling, errors and later navigation assertions. W may supply shared action-state facts; i6 alone edits these leaves. |
| implementer4 (1) | `vps_network_editor_feedback` | Use the retained WebKit original to diagnose feedback/recovery boundary, preserving exact network payload, dirty-form, rejection, context, retry/count and uncertainty intent. No shared VPS/network behavior change. |
| implementer2 (conditional aggregate only) | `scripts/fixtures/e2e-type-coverage.json`, `tsconfig.e2e.json`, existing factual work-log as required | If an edited leaf is deferred, adopt its whole file under existing strict options; each leaf owner fixes its diagnostics. Already adopted files need no new metadata. W alone makes the minimal aggregate adoption change, with no baseline/hash-only refresh, compiler weakening or new coverage mechanism. |

Owner packages include direct same-case diagnosis, evidence-grounded canonical
fixture/assertion corrections, scoped lint and strict whole-file typing, stable
path/hash reports and lead-serialized commits. Preserve meaningful negative,
later-case, count, no-replay, role, nullable, completion and secret assertions.
Malformed tests remain malformed at their intended boundary. Fixing a successful
fixture must not invent server values, receipts or authorization, coerce unknowns,
or spread request-only inputs into output. A valid API reply rejected by production,
engine/environment defect, production/shared helper/guard change, harness/config
change or dependency/provenance/pin proposal returns to lead before edits. No
normalizer, broad mock rewrite, timeout increase, skip or blind rerun is authorized.

After packages and any actual W adoption dependency settle, run the existing
combined strict/quick checks, coherent commits and affected review. Then use the
ordinary native local selection for applicable existing cases in these11 touched
specs, retaining both locales/roles and negative/later steps without repeating
unaffected prior220 passes. Lead preflights exact native case/project identities;
retain two workers, zero retries, max-failures1 and the existing900-second bounded
diagnostic cap. Original WebKit behavior needs its native acceptance; any local
mobile Chrome projection is explicitly limited. No engine install/new harness.
Stop at a real failure, diagnose its retained first boundary and resume affected,
interrupted and unrun identities only. Larger final-head CI acceptance remains
separate from this diagnostic selection. Prior source/review/Nix/browser receipts
remain bound to their actual inputs; no new pass, release, merge, deployment or
lifecycle claim follows from this brief. The user keeps release transition pending.

#### Transaction fixtures: member and administrator case mapping

i6 inspected all15 selected originals for its three leaves; the accepted first
boundaries are missing singular Show namespaces, wrong Index collection framing,
and object transaction input/output rejected by the declared string contract.
The [retained member map](webui-third-ci-evidence/member-map.json) now supplies
the completed local evidence selection. The following is a same-package assertion
disposition, not evidence of a production, focus or engine defect.

API610 Transaction Index/Show exclude `user`, `type`, `urgent`, `priority`,
`input` and `output` for nonadmins. The frozen generated output also has no
transaction `progress`, `details`, `stdout`, `stderr` or `result` fields.
Keep member fixtures restricted and preserve privileged diagnostic coverage in
existing admin cases. Canonical diagnostic content is a JSON string in `output`;
the current reader displays it in Output without parsing it into a separate
`.detail.error` card. This does not authorize a production parser change.

| Existing leaf/cases | Exact role and assertion disposition |
| --- | --- |
| `transaction_detail_page`: member detail, reload, locale labels | Remain real members. Keep known fields, state/duration, node and chain context, no-admin-link, reload and viewport assertions. Check no backend payload values or restricted raw keys. The payload shell and Input/Output headings still exist, so do not assert that the entire card is absent. Remove phantom transaction progress40. |
| Same leaf: existing admin detail and admin email cases | Move the member fixture's worker/priority, error/command/stdout/stderr, long-token/raw and filled-payload geometry assertions into the existing admin detail case. Keep diagnostic strings inside canonical output and check error visibility there. Preserve the existing admin email HTML, copy, keyboard and overflow assertions. |
| `transaction_chain_detail_page`: main member list, failed polling, reload | Remain real members with restricted transaction rows. Preserve concerns, invalid-reference and no-admin-link negatives, row tones, expansion/collapse, pin, geometry and polling counts. Expanded member rows show known metadata and no backend payload. Move rich702 input/error/stderr/rollback assertions to the existing admin-route case at its narrow viewport. |
| Same leaf: done-chain narrow-desktop and running-chain/current-step | These two layout cases use an explicit admin identity in the existing `/app` My view, with that role clear in their names/comments. Keep prepare/booted/creating-veth payload assertions in place using canonical strings, without adding cases or navigation. Preserve actual chain100% and1/3 ·33%, current step902, expansion and viewport checks. Chain progress is valid and distinct from phantom per-transaction progress. |
| `tasks_drawer_focus_trap`: member cases and existing admin cases | Keep member focus/nonmodal/narrow-card/status and action79 inspection cases as members; retain the already-admin identity/search case and captured scope. Member transaction9001 retains its long name, links, card/toggle geometry and collapse, with no privileged payload. The existing admin881/882 case retains rich dataset/error diagnostics, matching its actual VPS44 identity; carry the equivalent dataset/readability and `dataset_created` assertion there. Preserve zfs/stderr text and put the former chain failure text inside transaction882 output. Assert chain880's declared failed state rather than the unsupported `tasks.chain.failure.880` summary. Keep admin navigation/reload and nonmodal assertions. |

Use declared partial relations (`depends_on`, node `name`, VPS `hostname`), not
numeric arrays or invented labels. TransactionChain has neither `error` nor
`action_state`; do not fabricate those fields to retain an unsupported summary.
Direct same-fixture source inspection also shows that ActionState Index/Show have
neither `result` nor `transaction_chain`. For member action79, use its canonical
ID/label/status/current/total fields: the existing task-link reader derives chain79
from the action's ID and state fields. Its backend-details panel falls back to the
canonical raw state, so assert that real context instead of invented `result.vps_id`.
This later setup correction is source-backed, not a newly claimed trace root.

i6 alone implements these three leaves under the lead's existing release. No
shared role filter, mock normalizer, production guard/parser/link change or new
test framework follows. Existing whole-file strict/lint, conditional W adoption,
serialized commits, affected review and bounded native acceptance remain the
checks; no additional verification campaign is introduced. Member fixtures model
the API's restricted output, not a claim that the UI filters an unauthorized reply.
Prior220 acceptance, exact Nix evidence, recovery and release boundaries remain.

#### Local WebKit setup boundary and bounded continuation

At final2ad8f71759d048685f793a36b097e4d2e7cfdffc, the reviewed third-CI
source is frozen. The [single native126 attempt](third-ci-touched-native-result.md)
exited1 after101.261s: no passes, one WebKit lifetime(cs) setup timeout, one
interrupted WebKit initialization case and124 unrun. The earlier command-file
handoff correction was setup-only, not another browser attempt. i0's
[native outcome selection](third-ci-touched-outcome-selection.json) joins all126
identities to the final preflight and establishes that all118 Chromium/mobile
Chrome cases have no execution result. Its sole report-level error is the native
maximum-failures stop, not evidence of an additional independent fault.

The exact failed lifetime trace's `test.trace` records successful browser launch
(about962ms) and context creation (about55ms), followed by the builtin `page`
fixture waiting in `browserContext.newPage` until the90000ms setup timeout.
`0-trace.trace` has only context options, `newPage`, then pageClosed/page events;
it contains no completed page call, navigation or application action.
`0-trace.network` is empty, and the error context has no application snapshot.
This establishes the failure before the test body: its bootstrap init script,
mock installation, navigation and lifetime assertions did not run. The source
imports native Playwright `test`; the shared bootstrap is a function called
inside the body, not a replacement page fixture. The existing mobile-WebKit
project uses the ordinary iPhone13 device context; the wrapper passed the
installed1.61.0 CLI and retained browser-store environment without a WebKit
workaround. No application/shared-fixture failure is demonstrated here.

Confidence is high in that setup boundary, not in a particular underlying
platform cause. The pageClosed event does not by itself prove a crash, missing
dependency, browser-version mismatch or permanent engine failure. There is no
evidence warranting a source change, timeout increase or local platform repair.
For this acceptance batch, local WebKit did not supply a usable page; leave its
original evidence intact and require native CI acceptance for its eight cases.
Prior CI successfully starting WebKit does not certify this final source.

Recommend lead release one continuation using i0's exact118 still-unrun IDs
(59 Chromium,59 mobile Chrome) through the existing runner and observer, with
the same source, ordinary configuration, two workers, zero retries,
max-failures1 and900-second cap. No new tests, helper, engine install, shell/cache
repair or browser probe is needed. Preserve all eight WebKit identities as
pending (one setup timeout, one interrupted, six unrun) under the unchanged
native final-head CI gate; successful118 would establish only118 local passes,
never aggregate126 acceptance or engine equivalence. Lead owns execution and
effect reconciliation; architect launched no check. The accepted
[effects receipt](third-ci-touched-effects.json) remains the authority for the
terminal operation's process/port absence and preserved unrelated old Bash;
it was not independently reprobed. Prior220/Nix scopes and release-pending
boundaries remain unchanged.

### Fourth-CI disposition: observed VPS cases

Frozen source is20aa0e9ea7568747f048242077f0cf15a325d990,
tree4a4c7fb8a83d287fd25026909d998373b277b2d4. Core41508552632/attempt1
passed all three jobs. Smoke41508552554/attempt1 is terminal: native WebKit
reports274 passed/2 skipped, while both Chrome jobs are cancelled with incomplete
case totals. Both40-minute caps are now directly established: the parent retained
the Chromium check-run annotation after the original watcher's missing/404
response, as recorded in the [final CI proof](webui-third-ci-final-ci-lead-result.json).
Preserve the original report's provenance limitation; do not infer a human
cancellation actor. Preserve the [original watcher report](webui-third-ci-final-ci-watcher-result.md)
and terminal raws under `webui-third-ci-final-ci/`.

i0's [final inventory](webui-fourth-ci-observed-inventory.md) and
[selected originals](webui-fourth-ci-observed-selection.json) establish20 failure
headings,10 per Chrome project,16 distinct titles and six paths. All are outside
the prior30/27/11-path repairs and local220/118 identities. This is newly observed
scope, not a later failure of a previously accepted local case. The structured
selection SHA256 is54a2893ca4bdc576484336cd5d601e4a8fbf12f1ae0032b8cd3f41786712770b;
it retains every observation and maps10 mobile-Chrome plus6 Chromium retry0
originals without inventing unavailable historical test IDs. All acquisition
is complete; no further download is needed for these cases.

The small native WebKit report now supplies the previously missing individual
proof: all eight touched identities passed on20aa, retry0 with no errors. Keep
that actual CI evidence distinct from the earlier failed local page setup and
the accepted118 local Chrome cases at2ad8. The two other explicit WebKit skips
remain recorded; dot-only output alone was not used to infer this result.
Previous220 and final Nix proofs retain their exact recorded scopes.

Architect read all16 mapped originals in memory and compared their directly
consumed contracts. The established first boundaries are:

- Eleven lifecycle/maintenance/power originals return HTTP200 namespaced VPS data
  with `dns_resolver:'inherit'`; the pages stop before any mutation. English
  contexts show Failed to load VPS, with the equivalent localized failure in
  the Czech migration case. Selected99ee declares a nullable partial relation;
  `vps.ts` rejects the primitive at its relation guard. Use explicit `null` for
  these no-resolver fixtures. No timing, geometry or permission defect is proven.
- Both list-retry originals preserve the initial409, then return200 with only
  action901/902 metadata. The confirmation displays Missing response namespace.
  Add `vps:{}` beside the existing receipt; retain the rejection and two writes.
- The disk-first original (`...workspace-adeca...`) reaches Update datasets/10,
  which returns200 metadata-only action901; Missing response namespace leaves
  the confirmation open. Supply the canonical `dataset` frame with that receipt.
- Both private-IP originals reach the correct availability query and display the
  two addresses, but each row omits `network_interface`. Selecting82 produces
  IP address is missing and no POST. `ipRouteAssignIntent` requires the known
  unassigned baseline `network_interface:null`; absence is deliberately unknown.
  Add that explicit null to both synthetic available rows. Keep the location11,
  private_access, usable_for=vps query and existing assign response/receipt.
  This preserves the guard rather than inferring unassigned state from omission.

Later same-leaf lifecycle/power action replies also omit `vps`; these are
source-backed follow-on corrections, not executed-mutation claims from originals
that stopped at GET. Likewise the disk test's deliberately missing-receipt branch
needs a canonical `dataset` frame while retaining the absent receipt, so its
intended uncertainty assertion is reached. No valid-contract rejection by
production has been established. Generated/API contracts remain99ee/610.

The following nonoverlapping packages have stable diagnosis boundaries and await
lead source release. All specs are under `e2e/specs/app/`; owners use the linked
originals and direct contracts for exact local corrections and later steps.

| Owner | Exact spec filenames | Preserved intent and boundary |
| --- | --- | --- |
| i3 | `vps_lifecycle_tab_actions.spec.ts`, `vps_list_action_failure_feedback.spec.ts`, `vps_maintenance_mobile.spec.ts`, `vps_power_stop_confirm.spec.ts` | Correct the three no-resolver fixtures and explicit action success namespaces, including directly implicated later same-scenario setup. Preserve member/admin separation, explicit override/confirmation, rejection then retry, receipts and missing-receipt uncertainty, exact payload/count, task navigation, delayed readback and mobile geometry. |
| i4 | `vps_private_ip_availability.spec.ts` | Explicitly model both available IPs as unassigned with `network_interface:null`; preserve shared-staging private IPv4 availability, both roles, location/role/usable-for query contract, exact interface payload and availability-error/no-submit negative. No new preflight, role conversion or lock change. |
| i6 | `vps_resource_workspace.spec.ts` | Correct dataset success framing and the separate missing-receipt test frame; preserve independent disk/VPS drafts and writes, override opt-in, used-space/fresh-read/activity guards, missing-receipt/no-replay and admin/member visibility. |
| W, conditional aggregate | `scripts/fixtures/e2e-type-coverage.json`, `tsconfig.e2e.json`, existing factual worklog | Lifecycle and private-IP leaves are already adopted. If edited, the other four deferred leaves require whole-file strict adoption; owners resolve diagnostics, W alone updates aggregate membership. No hash-only refresh or compiler weakening. |

Complete repeated proven framing corrections in the owning existing local mock
and same-action branches rather than leaving an immediately hidden later failure.
Use generated-derived local response types where useful. This does not justify
a cross-spec helper, normalization framework, broader fixture audit, new role
coercion or widened supported API. A valid reply rejected by a shared reader,
or a need for production/client/harness/pin changes, returns to lead before edits.
Required evidence acquisition remains i0-only under exact parent release.

Acceptance retains the existing sequence: bounded diagnosis, stable source
package and conditional strict adoption, scoped lint/whole-file strict, serialized
commits, affected review, then existing native cases from the touched six leaves
with all negative/later steps intact. Lead preflights exact project identities
and bounds the diagnostic batch with two workers, zero retries, max-failures1
and900 seconds; no speculative cap increase or duplicate prior118/220 campaign.
Stop at a real boundary and resume affected/interrupted/unrun cases after its
disposition. CI gates stay unchanged; neither cancelled Chrome totals nor a
successful WebKit aggregate imply overall acceptance. Source remains frozen;
architect edits only this design record. No deployment, state/schema, recovery,
dependency or release transition is proposed; the user's release remains pending.

#### Fourth-CI local gate: exact Start request assertion

The [single136-case attempt](fourth-ci-touched-native-result.md) at
b1b37ccf5dc5d000baed3d77d49fab6f5b84b663 exited1 after35.091s with6 passes,
one failed assertion, one interruption and128 unrun. Its retry0 power-start
trace (`browser-fourth-ci-touched/results/app-vps_power_stop_confirm-7f907-s-the-returned-action-state-chromium/trace.zip`)
records one POST `/vpses/123/start` with the exact body `{"vps":{}}`, a200 fixture
response with canonical `vps:{}` and action776, then a GET of action776. The
failure is the equality assertion at `vps_power_stop_confirm.spec.ts:97`, which
expects `{}`. Later task assertions were not accepted by this failed run.

The selected99ee Start descriptor declares `inputNamespace:"vps"` with no input
fields. Its generated executor preserves that namespace even without `params`;
HaveAPI0.32 `prepare()` serializes non-GET input as
`{[inputNamespace]: params || {}}`. The retained API610 schema likewise declares
Start's empty input under `vps`; Stop/Restart use the same namespace with optional
boolean `force`. Backend Start has no action input fields, while Stop/Restart
default force to false. Ruby's ordinary parameter-layout handling accepts an
omitted empty namespace too, so this is not a claim that the former `{}` body was
an invalid API request. It is an obsolete exact-wire assertion for the selected
generated-client serializer, not a product/client defect.

Minimal remediation: i3 changes only that Start expectation to
`toEqual({ vps: {} })` in the power leaf. Retain deep equality (including absence
of extra keys), all endpoint/role/confirmation/task776 assertions and every other
case. Existing Stop/Restart `toEqual({ vps: { force: true } })` assertions already
match the declared contract and remain unchanged. No fixture, serializer, API,
timing or receipt change is needed. No wider assertion search is authorized.

After lead release, use the owning leaf's existing quick checks and direct narrow
review disposition. Retain original b1b/review/source/run refs and fold this
one-line correction into the unpublished owning C3 commit, replaying C6/W with
unchanged patches; published20aa and prior commits remain untouched. Lead owns
serialized Git and equivalence proof. i0 owns the exact continuation selection:
cover the failed, interrupted and unrun identities plus any affected case;
preserve the six actual passes only within their proven unchanged scope. Native
limits and final acceptance gates stay unchanged. The parent's
[effect proof](fourth-ci-touched-effects.json) covers the recorded root identity,
operation-era CWD and port absence, not uncaptured descendant tuples or cleanup
of an unrelated old Bash. Architect performed only source/evidence reads and
this record update; no checks, browser, source/Git or lifecycle action.

#### Fourth-CI continuation: rescue template preflight

The [native130 continuation](fourth-ci-touched-continuation-native-result.md)
at be42b595a2a1746c55842cbfc0a6786d015fead6 exited1 after119.295s:
14 passed, one failed, two interrupted and113 unrun. The assigned retry0
`...vps_lifecycle_tab_acti-71d52--legacy-rescue-boot-payload-chromium/trace.zip`
under `browser-fourth-ci-touched-continuation/results/` proves the first failure
before any boot POST. The list returns canonical enabled templates6/7; after
selecting7 and confirming, GET `/os_templates/7` returns HTTP200
`{status:true,response:{}}`. Both the rescue form and confirmation show
Missing response namespace. The selected descriptor requires `os_template`, and
HaveAPI0.32's response decoder throws before template eligibility or boot dispatch.
The existing leaf mock provides the Index but no Show handler, so its ordinary
empty fallback produced this malformed response.

This is an incomplete preflight fixture, not rejection of a supported legacy boot
input. `VpsLifecyclePage` fetches the selected template before `vpsBoot`; the
selected99ee/API610 Boot input explicitly supports numeric `os_template` and
string `mount_root_dataset`. The model's `/mnt/rescue-root` value is valid under
that contract, and disabling the mount omits the optional string. No capability
change, field rename, coercion or assertion relaxation is needed. The existing
canonical boot success frame and receipt501 remain untouched. API610 template
Show permits `enabled` for both admin and authenticated nonadmin callers.

Smallest coherent i3 package, pending lead release: edit only
`e2e/specs/app/vps_lifecycle_tab_actions.spec.ts` to give its existing
`installLifecycleMock` explicit canonical Show replies for the known templates7
and6, matching the existing Index records (same IDs/labels, enabled:true and
hypervisor_type). Template7 is original-trace-proven; template6 is the directly
related source-backed no-mount rescue variant using this same helper. No arbitrary
ID fallback or new shared mock is allowed. Preserve the exact legacy boot payload
expectation, member/admin paths, no-mount omission, confirmation, receipts,
rejection and count assertions. This small setup completion also supplies the
same declared template lookups to existing helper consumers; it does not claim
their later outcomes have executed or passed.

Use existing scoped whole-leaf strict/lint checks and narrow committed review
before another native continuation. i0 owns exact failed/interrupted/unrun and
affected-case selection plus pass-retention dependencies; do not repeat unrelated
proved cases or infer acceptance for unrun cases. Native caps/retries/workers and
source/provenance boundaries stay unchanged. HaveAPI f29c integration is separate
from WebUI's selected99ee/0.32 contracts; no new generator/runtime adoption follows.
The parent owns effect proof for the21 captured identities and port5187; architect
did not re-probe them or launch checks, edits to project source, Git or lifecycle
operations. The session remains open.

### Residual support-shell failure at published24ae

This bounded follow-up starts from published WebUI
`24ae8a8f681ed8d4df7e147d5179116113869628`, tree
`a94cdf5276cdd8702e4f0a4438abaf73d3a155d4`. Core CI 41538869664 passed all
three jobs, including 2227 tests and strict 140/142. Smoke 41538869566/attempt 1
completed: mobile Chrome 574 passed, WebKit 274 passed, and Chromium 631 passed
with one failed support scenario (retry 0/1/2). No job was cancelled. Preserve
the prior 136-case acceptance 41dfdf35 and literal 24ae Nix/input proof e8d489f0
for their actual revisions and scopes; neither certifies this repair.

i0's [original evidence receipt](webui-ci-41538869566-evidence.json)
(SHA256 44d79a18a7d8d6afa893f6050bf0d9dadbf21550827501ebcc373db21ca80a5a)
binds test ID `06642105c069c2ad87ba-7542188c51652155248b` to
`e2e/specs/app/vps_support_permissions.spec.ts:32`, assertion 102.
Architect read only its original retry 0 trace/context in memory. The trace
SHA256 is `c8ef7bfd9418662b7e9f06e778578e838db3e3c97e382a9df4c2acc9afdbff17`;
its embedded leaf SHA256 `1d54f0d7d24590f6bdbe168fd2df8b23288156370ba43afa4c22e9eab41f32cb`
matches the retained source. Network lines 455/459 return HTTP 200 with a valid
`response.vps` frame but `dns_resolver:"inherit"`. Trace line 204 records
`Invalid VPS response` on `/admin/vps/123`; the context shows Failed to load VPS.
The recorded API requests are GETs. This establishes the first boundary, not
the later tab outcomes, which this attempt never reached.

The selected 99ee Show declaration requires a nullable partial DNS-resolver
relation, consistent with the API resource declaration. `vps.ts:66–71,117–118`
rejects the string; `fetchVps` wraps that failure as invalid output and
`VpsLayout` renders its error state before the overview assertion. This is a
malformed positive fixture with high confidence, not evidence of a permissions,
browser or timing defect. The accepted smallest correction is the local
`supportVps.dns_resolver` value from `"inherit"` to `null`. No reader, generated
client, HaveAPI 0.32 runtime, selected API contract or shared mock changes follow.

Lead-approved package ownership is **W/implementer2 alone**, pending source
release. Its exact files are the support leaf, `tsconfig.e2e.json`,
`scripts/fixtures/e2e-type-coverage.json`, and the existing
`docs/work-log/2026-11-01-typescript-client-migration.md`. Adopt the entire edited
leaf into strict coverage and remove only its deferred entry; do not refresh
the deferred hash, loosen compiler options or add allowances. Keep the fixture
change to the one literal unless actual whole-file diagnostics require a
separately explained local typing correction. Escalate any consequential
contract or assertion change. i3 receives no source grant for this package.

Preserve support identity 21/level 21, foreign owner 77, the admin route, all
positive rendered-data assertions, all hidden/disabled mutation assertions,
the direct migration denial with zero node queries, and the final empty
mutation-request list with its existing settings-only exception. Keep every
tab, viewport branch and count. An error page cannot satisfy the intended
read-only shell coverage. Later fixture failures remain unproven and do not
authorize a general audit or speculative edits.

W's quick acceptance is scoped lint/diff plus zero diagnostics for the whole
leaf and the existing combined strict/coverage gate after metadata adoption.
The concise work-log update records actual 24ae failure evidence, the correction,
actual quick results and review/native checks still pending at commit time.
Use **one ordinary focused new commit after 24ae**; preserve all 35 published
commits and their proofs. No fold or rewrite is allowed. Independent affected
review follows the committed quick pass. The parent then releases a fresh Luna
watcher for the minimum failing Chromium leaf selection, deriving actual case
membership/count before launch. Keep existing native timeouts, retries 0 and
maxfail 1; run the complete scenario through the final no-mutations assertion.
Do not expand mobile selection or rerun the accepted 136-case gate. Any later
failure returns with its original evidence before another remedy. Final native,
review, Nix and CI outcomes belong in existing session/PR records, without a
new factual work-log append/rebuild cycle.

This package changes test data, direct strict-coverage metadata and its factual
work-log entry: no runtime/API behavior, persistent state, schema, deployment order or rollback
format changes. Ordinary reversal of the new commit restores the test state;
retained original evidence remains intact. No new checks, source/Git mutations
or lifecycle actions were performed by architect. Release remains pending and
the session stays open.

## Released client transition and session preview

Current result: the released-client development preview is running and accepted
within the source/toolchain/provenance limits in the acceptance checkpoint below.
The following brief retains the transition's original implementation boundaries.

The user now authorizes using the released generated client and starting this
session's vpsAdmin development cluster to view the new UI. This supersedes the
earlier registry/preview hold, without authorizing default-branch integration,
production deployment, publication, data reset or session lifecycle changes.
The starting WebUI is published `b5c12bcd8afa67103ae05bd3fc993ad4fe14f256`, tree
`5c5446624525afdf1fa1fcddeffb37fd051cb4ad`. Preserve its 36-commit series,
including the protected 35-commit prefix. Its six CI jobs passed (632 Chromium,
574 mobile Chrome, 274 WebKit plus two skips, 2227 unit tests, strict141/141);
Nix/input proof44b0d6e0 remains evidence for that exact pre-transition head.

i1's release investigation establishes published `vpsadmin-typescript-client@0.3.0`
at the canonical npm registry URL. Its 337128-byte tarball has SHA256
`57236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610` and integrity
`sha512-jZKO+c9azQqwXYLMp+yCl54pqhjyGDVr6rxOzq2rjusEBQ8Xm5dCdc8a2iHV5buUq8hc6835tmF5wjlP8/HJ/A==`.
All 1352 distributed JavaScript/declaration files are byte-identical to the
accepted99ee candidate; all 1360 archive entry paths agree. The six changed
entries are README/package metadata and generator/schema provenance records.
The exact runtime peer remains `haveapi-client@0.32.0`; ESM/ES2022 exports and
API7/protocol2 schema SHA256`476f0086726a443a6ef8ad9a9d499bd3feff6eb6c5b0b652dcc999192d638794`
are unchanged. The published generator is `1ef9b204ba45bb261d3334be5c555cc1856b713b`
with generator/Ruby version0.32.2 and API capture
`5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5`. Do not mislabel those source identities
as oldeea3/f29c or interpret the generator version as the npm runtime version.
This proves generated-program equivalence, not source-revision equality or a
new live API compatibility run. i1's [release proof](artifacts/package-s/published-client-proof-2026-11-03/release-proof-receipt.json)
also verifies all 675 generated ownership hashes. Public tag `v0.3.0` selects
client source `d354491537f8b654b4d2c33a705cad84474f95d6`; npm-reported provenance
binds that source/tag and archive digest to release run41538988296/attempt1.
Those reported bindings were inspected, without independent Sigstore signature
verification. A missing GitHub Release page does not negate the verified npm
release/tag. Exact version0.3.0 is selected, never a mutable dist-tag.

W/implementer2 owns one complete ordinary follow-up commit after lead release:

| Files | Bounded change |
| --- | --- |
| `package.json`, `package-lock.json` | Select exact registry version0.3.0 with npm-generated canonical URL/integrity. Preserve HaveAPI0.32.0, its locked transport and unrelated entries. |
| `packages/frontend.nix` | Restore ordinary `buildNpmPackage` dependency fetching; remove the custom `npmDeps` projection, cache-map wrapper/hook override and archive-only writable cache setting; refresh only the frontend hash. |
| `scripts/check-package-source.mjs`, its `.test.mjs` | Remove unpublished-client/archive/cache-map logic, fixtures and negatives. Preserve existing HaveAPI/XHR provenance, required-source, private-path and symlink protections. No replacement registry-checking framework. |
| `vendor/vpsadmin-typescript-client-0.3.0-99ee06654ef9.tgz`, `packages/vpsadmin-typescript-client-provenance.json` | Remove obsolete committed candidate inputs and required-path references. Original receipts and published history remain available. |
| `docs/design/HAVEAPI_CLIENT.md`, `docs/design/PACKAGING.md`, `docs/work-log/2026-11-01-typescript-client-migration.md` | Document the actual release, equivalence limits and normal registry install/hash procedure before review. Retain the standard optional local `npm pack`/no-save override and restoration workflow, removing its references to deleted canonical inputs. |

Do not change production readers, roles, wire policy, generated files, shared
fixtures, BFF dependencies, flake/API/localization pins or the isolated API runner.
No permanent archive mode or switch is retained. Useful historical work-log
evidence stays historical; current packaging instructions must describe the
registry dependency. Keep the existing guide links valid without expanding the
documentation scope.

In the pinned Node/npm shell, W uses ordinary `npm install --package-lock-only
--ignore-scripts --save-exact vpsadmin-typescript-client@0.3.0`, inspects the
bounded lock delta, then coordinates `npm ci` so no live runner's dependency tree
is replaced. Verify the installed public exports, declarations and exact runtime
peer against i1's release receipt. Use `prefetch-npm-deps package-lock.json` for
the frontend hash; leave the BFF lock/hash alone. The former temporary file-lock
projection and fake-hash archive workflow are no longer needed. Hash acquisition
is a dependency-input preparation step, not final package acceptance.

Quick acceptance covers the changed source-checker tests, existing generated
client policy/wire tests, application/tooling/E2E strict checks including coverage,
affected documentation audit and scoped format/lint/Nix syntax. Preserve zero
diagnostics and all existing negative/security assertions. Commit all source,
hash and documentation changes before independent affected review. Then a fresh
Luna watcher runs the existing five final-head frontend/BFF/provenance/source/
package checks, retaining both schema1 metadata files, exact source/input graph
and actual artifact paths. Do not reuse old derivation evidence merely because
the installed generated program is equal. No new VM/platform campaign is needed.

Byte-identical generated programs make a repeated full browser matrix or isolated
API database run unnecessary for this distribution-only change. Existing tests
exercise the newly installed registry bytes; actual preview checks establish the
new serving configuration. Any installation, policy or packaging difference
returns to its exact boundary before changing scope. Final feature CI can run
normally, but a three-project CI wait is not a prerequisite to the requested
development preview after scoped checks, committed review and final packaging.

i6's [completed preview preparation](devcluster-preview-preparation.md) records
the exact owned state, source selection, standard launch, private access guidance
and safe health/login acceptance. Parent retains launch ownership under a fresh
watcher; no start has occurred during preparation. Its standard status reports this session stopped,
with no applied topology/network/ready/result/runner/disks. Preparation's standard
`urls` command initialized config/socket records; lead accepted that benign own
initialization under the start request. Earlier config existence was unmeasured,
so do not claim a measured before/after reset. Current config enables newWebui,
uses `newadmin.aitherdev.int.vpsfree.cz`, services address172.16.106.53 and bridge
`br0`/gateway172.16.106.1. i6 confirmed bridge/KVM/helper prerequisites; no local
fallback is justified. The standard first start after final package acceptance is:

```sh
vpsadmin-devcluster start 2026-11-01-typescript-client-migration --topology single --network bridge
```

Preserve the standard occupied-address refusal; do not use `--force` to bypass
another cluster. The expected preview URL is
`https://newadmin.aitherdev.int.vpsfree.cz/`, conditional on actual boot, development
network/DNS and CA trust. The preparation record describes private seeded-account
access and the ordinary OAuth bootstrap; no manual database or secret setup is
needed. Report the URL as usable only after the native ready/activation and
health/login evidence exists.

The installed provider automatically selects this session's WebUI worktree as
`vpsadminWebui` through a `path:` override; frontend and BFF share that input.
Its separate revision/dirty/sourceKind labels in result-config/status establish
selected-source information, not package metadata or activation. WebUI package
build-info derives from `self.rev`/`self.dirtyRev`; a path input without Git
metadata honestly records `unknown`, `dirty:true`, `source:unavailable`. Do not
replace that value with provider labels or claim final-head metadata without
actual evidence. Compare the final five-check package metadata/store roots with
the cluster's selected packages and booted frontend build-info/BFF package;
record any derivation difference and its input/source proof separately. The
[installed provider guide](/nix/store/9019d7wm0c40q59vrnlf1clwp7q00xrd-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md)
also distinguishes selected result-config from successful guest activation.
No provider or provenance implementation change is part of this transition.
This is a packaged preview, not a Vite mount. `--existing` would boot an applied old payload and is not a way to
adopt new worktree changes; any later authorized replacement uses the documented
`update <slug> services` path. The actual initial backend source stays this
session's clean API610a96 checkout. No session vpsAdminOS worktree exists, so the
provider's canonical local source selection must be recorded by i6 as resolved,
without fetching or silently upgrading it. Retain native ownership and operation
handles; unexpected local kernel builds require the existing verification
procedure's stop-and-investigate disposition, not a platform-workaround project.
Use the reviewed final WebUI source/artifacts, not the already-green archive
baseline or a floating default branch. Preserve existing cluster data and backend
source; no implicit API repin, new migration changes or reset. Normal fresh-cluster
bootstrap uses the selected backend's existing procedure. The historical second
isolated-API cleanup remains externally unconfirmed and outside this package;
do not treat preview preparation as permission to signal or clean that operation.
If its actual effects conflict with the documented cluster, return the exact
conflict to lead before mutation.

Preview acceptance must identify the exact session-owned cluster, network and
backend source, final WebUI commit/artifact and released client, then verify the
documented UI entry and authentication path and provide its URL/access guidance.
Keep credentials out of records. This is development preview evidence, not
production deployment or live certification of every API action. Recovery uses
ordinary source/dependency reversal with a matching lock/hash/artifact set;
no persistent-format or database change is introduced by this transition.
Do not reset data, stop/delete/archive the session or alter another session.
Architect performs design-only work; source, checks, Git and cluster turns stay
with their assigned owners and parent coordination.

### Accepted development preview

The [preview acceptance record](devcluster-preview-acceptance.md) and
[sanitized bindings](devcluster-preview-acceptance.json)
(SHA256`3251548e1c2ded848c13ba943c0ec01119d514b6d3ab2ae9cf64edda4a3d6f26`)
record the parent-accepted result: standard single/bridge start exited0 after
1168.008s; the exact session is running/ready with no pending applied operation
and boot proof for services, node1 and both DNS guests. The UI is usable at
`https://newadmin.aitherdev.int.vpsfree.cz/` with development network/DNS and CA
trust. Private seeded account fields remain in the session portal. CA-validated
health/config/deep-route requests and ordinary Administrator OAuth login/BFF
session succeeded; served HTML, entry JavaScript and metadata match the active
frontend. This is bounded development access acceptance, not full API certification.

The actual frontend/BFF source matches all 2574 included entries and modes at
`4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e`, with only an additional empty vendor
directory. The ordinary registry0.3.0 cache derivation path/hash matches the
retained package proof, paired with HaveAPI0.32.0; the cache archive itself is no
longer resident, so the receipt distinguishes retained byte verification from
current derivation binding. Backend API610 remains; all 2367 OS source entries
and modes match local staging`5918f94e5e4eef3733b60aca4e03c1a6c0d43748` without fetch.

The running provider selected Node24.22.1/Python3.13.17; the independent Git
five-package acceptance used Node24.21.0/Python3.13.15. Active package metadata
honestly remains unknown/dirty/unavailable. Preserve that distinction: old Git
outputs were absent, the single authorized reconstruction did not match retained
NAR hashes, and the reference watcher refused before execution. No artifact
equivalence or new reference result is claimed. Parent accepted the documented
preview boundary without provider repair, repin or another build campaign.
Exact active systems/store roots and authentication evidence remain in the linked
record rather than duplicated here. No owned check remains running; the cluster
and session stay open. Historical API2 uncertainty remains untouched.

## New client release, current-main adaptation and conditional integration

The user's new direction authorizes adopting the peer's completed client release,
rebasing the published WebUI feature onto current main, adapting or reworking our
migration around upstream changes, and merging WebUI into main once final review
and tests pass. The explicit clarification includes old request usage introduced
elsewhere on main. This is authorization for substantive in-scope conflict
resolution and migration work, not only patch-equivalent replay; routine remedies
within these boundaries need no repeated user confirmation. Configuration channel
preparation is also requested, but configuration-default integration, production
deployment and preview update/stop/reset are not granted. Only the lead communicates
with the peer session; nobody here accesses its files, worktree or team.

### Evidence and release dependencies

i5's [preparation receipt](webui-rebase-preparation-receipt.json) and
[inventory](webui-rebase-preparation-inventory.json) bind old base
`63d484fc070dbee633d32624de545e834d483701`, published feature
`4ed519b69c422ea6b4fd0bd7bf490a20fcd6983e` (37 commits), and freshly fetched main
`1c8478bceb3943645ec06ccde895ee4b0985873f`. Main adds one commit, Guard advisory
corrections and lifecycle actions, touching 50 paths. The 26 overlaps include
21 aggregate textual conflicts; the exported-blob simulation is neither a
performed rebase nor proof of a combined tree. Its five textually clean overlaps
and new nonconflicting production files still require semantic adaptation.
i5 returned its Git turn with source/index/HEAD unchanged. Preserve original
PR126 and fetch records; its API-reported old base is not fresh main evidence.

W's completed [caller/semantic map](w-040-migration-boundaries.md)
(SHA256`9826bda8b71740f460962c6dec51577592016a598e9e80c57d3098f827dc2b38`)
and [raw source inventory](w-040-main-request-diagnosis.json) establish 56 main
production files with old helper/type/projection symbols and 133 old-module
imports, versus zero on feature4ed. Main changes 19 production and eight test
source files; 15 source paths require semantic combination. The deterministic
per-path projection leaves two new old-module dependants without conflicts.
These are source inventory findings, not an actual combined-tree pass. The map's
eight production boundary paths and complete exceptions list are part of W's
implementation scope; final whole-tree closure remains required after rebase.

i1 has now retained canonical public metadata and one verified `0.4.0` tarball
in the [acquisition receipt](artifacts/package-s/published-client-proof-0.4.0-2026-11-03/acquisition-receipt.json).
It is 338234 bytes, SHA256`3a6f2a2a6f4eaeb31f490035b312e9b5403cf21589d649dc1fd31d60b64e1906`,
with npm integrity
`sha512-xvTQ9z/vheBmzBxuaJ50x8YsOa8ywZdFvLH6MXy/KNNgJ9tes4v3RfhhuxIHm6MaZDeTv+NYIN22sFXLCh3Oig==`.
The completed [release proof](artifacts/package-s/published-client-proof-0.4.0-2026-11-03/release-proof-receipt.json)
(SHA256`cf45d568e9c2560915b9c4dbe95359e9313cb1aae2122d5bfa1b2badee6a9952`)
binds public tagv0.4.0/object296d286401ec2b456919c406f9fd90461529119d to
client source `c53cb4dabb0b3aac8d05834478872d2cfa698fa7`, API capture
`942c6eaed41331f823d8e0f670ed239e2b308440`, generator 1ef9 and runtime 0.32.0.
Unlike the preceding registry transition, this release adds actual contracts:
advisory Retract/Delete and optional non-null `expected_state` on parent Update,
CVE Create/Update/Delete and nested node-status Create/Update/Delete. Do not carry
forward the old 0.3 byte-equivalence conclusion or install a guessed unpublished
version. i1 verified public source package/generator/provenance bytes against
the archive and matched npm-reported SLSA subject/source/tag and invocation
41670211965/attempt1; independent Sigstore cryptographic verification was not
performed. The schema is
`d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26`, with all six
plugins, 151 resources and 521 actions. The recorded outage_reports source digest
also changes without further schema changes. The package's own recorded lock
digest changes; its full development lock graph was not audited and is not the
WebUI runtime dependency graph. These limits remain explicit. The public release
dependency is satisfied. The [actual archived contract findings](artifacts/package-s/published-client-proof-0.4.0-2026-11-03/contract-quick-findings.json)
confirm exactly nine schema additions, no existing contract changes/removals,
and unchanged shared runtime/public-root bytes. The seven changed existing
actions add only `expected_state?: string | undefined` with non-null String
descriptors; the declaration is not a literal union. Application capability checks
must still enforce the actual draft/published/retracted choices. Retract is POST,
Delete is DELETE with the destroy alias; both use `security_advisory` input/output
namespaces, method-qualified descriptions, required revision and optional non-null
state. Delete's output is an empty framed object; neither action is blocking, so
do not invent an asynchronous receipt requirement. These are static archive facts,
not installed-client or live-backend acceptance. Any mismatch returns to lead, not a handwritten
generated-file patch or an alternate local archive.

These guarded operations require backend
`8225229aa0e3306f8b1723c5583969a33c64571c` or independently established equivalent
capabilities; API 7 alone is insufficient. i7 proved that minimum is a literal
ancestor of the configuration's API 942c pin and compared eight relevant backend
blobs unchanged. That is source compatibility, not live deployment proof. The
running preview remains API 610 and lacks these operations; it cannot certify
them and must not be repinned or updated as part of this milestone.

### Complete W execution package

W/implementer2 is the single application owner after lead release. It owns the
ordinary rebase, semantic migration, dependency/lock/frontend hash, affected
production/tests/docs, strict adoption metadata, quick checks and coherent commits.
The exact conflict/overlap set is in i5's inventory. Scope additionally includes
new `src/lib/api/securityAdvisoryMutations.ts`,
`useSecurityAdvisoryCorrections.ts`, `useSecurityAdvisoryNodeSnapshot.ts` and every
other actual legacy caller found in W's whole-tree inventory. There are no parallel
application writers. Architecture decisions below apply to clean merges too:

- Search all new-main and final combined production sources for `haveApiCall`,
  `CallOpts`, unwrap helpers, imported aliases/re-exports, wrapper call chains,
  direct fetch/XHR/AsyncClient operations and handmade vpsAdmin paths/descriptors.
  Trace each vpsAdmin call and capability query to the generated operation/root
  or action description. A text search alone is not the semantic conclusion.
  Record resolved call sites and the precise separate BFF/session/OAuth/external
  download exceptions. The single existing HaveAPI executor remains infrastructure;
  do not restore the generic endpoint wrapper, add another transport/registry or
  introduce an audit framework. Repeat the inventory after rebase/release changes
  and any later upstream refresh.
- Replace the new manual root/action OPTIONS and path/method structures with
  generated `describe` bindings, preserving authenticated scope, live credentials,
  metadata projection and effective object authorization. Preserve fresh
  authenticated root discovery rather than substituting an anonymous/cached
  capability description. Reuse
  `apiErrors.getMetaActionStateId` for new hook imports from deleted `haveapi`.
  Retract/Delete use their actual released generated operations. Generated types
  and namespaces replace handwritten wire declarations without broad casts or
  loosening response guards.
- Preserve upstream parent revision plus expected-state preconditions, publish
  draft checks, parent snapshots bracketing child reads, rendered-vs-fresh node
  snapshot comparison, serial CVE additions before removals and revision advancement.
  Keep localized node notes, non-retargetable CVE updates, user confirmations,
  authorization and all receipt/uncertainty/no-replay behavior. This is advisory
  lifecycle work; i5 found no new shared lifetimes API/component changes.
  Main's parent editor supports draft/published/retracted, announcements stay
  published-only, and explicit publish stays draft-only. Preserve empty CVE lists
  for existing-advisory editing, unchanged timestamp precision, localized
  null/absence and created-draft recovery without duplicate creation. Do not
  restore feature4ed's older draft-only editor policy during migration.
- Draft synchronization must gate **all six** child mutation actions: CVE and
  nested node-status Create/Update/Delete. It sends `expected_state:'draft'` and
  the frozen `expected_content_revision`, retaining the upstream capability and
  parameter checks. Generated methods do not implement this application policy.
  Preserve parent mutation checks and object-specific Retract/Delete OPTIONS.
  Older backends missing an action or required guarded parameters must disable or
  deny before any write; never omit guards as a compatibility fallback or refetch
  a newer stamp to turn a rejected draft into an automatic retry.
  Validate integer revision/string state parameters and the selected state's
  actual allowed choices, preserving upstream array and labeled-object choice
  representations. Missing/malformed descriptions fail closed. Correction flows
  retain their captured applicable state; draft-specific policy must not coerce
  an upstream published/retracted correction into a draft write.
- Adapt meaningful unit/wire/browser fixtures to the real released declarations
  while retaining upstream assertions, counts, roles, stale-state/revision and
  missing-capability negatives. Adopt each edited deferred leaf as a whole under
  existing strict options; no deferred-hash refresh or compiler allowance.
  Reconcile current API/workflow/domain/requirements docs and generated inventory
  with the actual combined tree. Preserve upstream localized behavior and consult
  its localization procedure for catalog edits; do not add incidental UI redesign.

Publication and public artifact proof are now complete. After receiving its
Git/source turn, W can perform the ordinary rebase, semantic adaptation and exact
registry0.4 adoption using the verified artifact/contracts. Installation, focused
checks, final registry lock/hash and combined-tree acceptance remain unperformed
by this investigation; publication alone does not satisfy them. W sends the completed source/caller/conflict map
and remaining concrete contract gaps before acceptance; it does not broaden into
backend, provider, generated-source or unrelated fixture work.

### History, verification and merge acceptance

The user-authorized rewrite now permits consolidating obsolete input history.
Before rewriting, preserve exact 4ed and required earlier source refs/receipts,
including the running preview's actual source graph and package/metadata limits.
i5 identifies one input stream in 8b648c8 (runtime dependency), 167f8531 (temporary
archive) and 4ed519b6 (registry 0.3), now followed by the final verified release.
Consolidate superseded archive/pin/hash updates into coherent final adoption;
retain the shared-policy work in 8b648 and other independent domain commits with
their authorship. Do not force an arbitrary squash of coherent stages. Any retained
intermediate update needs a concrete supported consumer/state boundary, not only
past publication/review. Old exact refs preserve recovery independently of whether
those commits remain in the rebased series. Record old/new ranges, range-diff and
semantic conflict dispositions; changed behavior is not patch equivalence.
Neither inspected WebUI range changes DB schema/migrations; final review must
confirm the complete migration inventory rather than infer other-repository state.

Use the pinned toolchain and ordinary npm exact-version lock generation/install,
then ordinary frontend `prefetch-npm-deps` hash preparation. Preserve unrelated
locks, BFF dependencies and API/localization/OS pins unless an actual upstream
change already owns them. Quick verification covers full production/tooling/E2E
strict+coverage, scoped lint/format, relevant documentation/inventory audits and
focused actual-library tests for capability/parameter gating, frozen state/revision,
parent/child namespaces, stale-read/write rejection, partial failure, async receipts,
no automatic write replay and the BFF/public/auth boundaries. Check old-backend
missing-action and missing-guard-parameter cases explicitly with zero writes.

After all intended changes and quick results are committed, the retained independent
reviewer receives the entire current-main-to-final series/diff, old deployed 4ed
lineage, input-stream dispositions, whole-source migration inventory and substantive
upstream resolutions. Use the applicable general/architecture/scope/risk lanes;
prior review does not certify this combined behavior. Resolve findings before
long checks. Parent then releases fresh Luna watchers for the existing complete
core CI (quick/test/build/script-browser jobs), all three native PR-smoke projects
and the final standalone Nix five-package set. Keep native caps/retries/selections
unchanged, inspect actual failures before any repeat, and report true totals/skips
instead of importing old counts. A focused affected native selection may precede
full CI when useful, but it does not replace the user's final all-tests condition.
No extra nightly/full-matrix campaign is added merely because main advanced.

Root the standalone final Nix outputs under ordinary unique session-owned result
links while CI and comparisons wait. Bind final commit, source/input graphs,
frontend/BFF store paths and truthful matching metadata; do not leave needed
outputs unrooted or infer reuse from trees alone. The live 4ed preview's Node 24.22
path-input artifacts and unknown metadata remain separate and unchanged. Do not
rerun or repair the historical isolated API test against an incompatible old
backend to certify the new guarded operations.

Parent owns final publication with an exact old-head lease, PR126 update and
conditional WebUI/main integration. Before integration, refresh the target and
inspect any further upstream delta and legacy callers; resolve changed contracts
outside the short merge claim and apply affected review/check requirements.
Once final conditions hold, use the required fast-forward-only merge/SSH push
and remote proof, releasing the repository claim before CI/records. No further
confirmation is needed for the already authorized in-scope adaptation/merge.
An unsupported new product/API requirement still returns to lead for disposition.

### Separate configuration feature

i7 owns the later configuration-only package. It has no registered session
worktree yet; create one through the ordinary workflow from freshly fetched
configuration main and record that actual base. Cached master c4107822 is
preparation evidence, not a substitute for that fresh check. Channel/role
`vpsadmin-webui` selects `vpsadminWebui`; preserve its site nixpkgs 718f follows and
API 942c/vpsadminServices follows. After the approved WebUI revision is actually
on remote main, use the documented command:

```sh
nix develop --command confctl inputs channel update --commit vpsadmin-webui vpsadmin-webui
```

The single logical update changes only `flake.lock`, with its native useful
changelog, identity and declared hooks. Verify the selected WebUI revision equals
the approved merged head and that other input/follows semantics are unchanged;
stop on newly floated unrelated main changes. Do not hand-edit the lock or select
a feature pin as a substitute. i7's quick semantic/path checks and the targeted
composed host build for `cz.vpsfree/vpsadmin/int.vpsadmin-webui1` establish this
configuration candidate separately from standalone WebUI packaging. A fresh
watcher handles that build if released. Publish the feature preparation; do not
merge configuration main or activate production without separate authorization.

Recovery preserves the running preview and exact 4ed refs, restores coherent
source/dependency/lock/hash sets by ordinary Git operations, and does not reset
cluster data or change BFF sessions/credentials. No DB migration is proposed.
The caller/semantic map and public release proof are settled, and i5's Git turn
has returned. Lead can release W's complete rebase/adaptation/registry adoption
package. The next observable result is W's rebased semantic/caller disposition followed by the installed,
verified release's focused checks. Final source release and operation turns
remain parent-owned.

## Broad-CI repair: explicit bulk advisory-note changes

This bounded REQ-055 design covers the note-loss defect at merged WebUI
`670cf286daf9bddb65594035507ca112a9e6d397`. It does not repeat i2's 12-spec,
33-case diagnosis or i5's separate workflow package. User-authorized broad-CI
repair includes this product correction. Preserve merged history and deliver
ordinary follow-up commits; source/Git turns and final acceptance remain with lead.
Architect inspection confirmed session/environment binding and roster61's retained
Astra/xhigh/design/workspace_write settings. Only this design record changed.

### Evidence and contract

The inspected `SecurityAdvisoryNodeForm.tsx` and `SecurityAdvisoryNodesPanel.tsx`
bytes match literal670 blobs `2add57fbec234129698e3ce2cbfc60d6d580fb92` and
`44a07b951d882a0981f55e09fd57fdcf0a1697a0`. Bulk opens with blank localized notes
and `original:null`; the payload helper converts each blank to `null`. Single-node
editing already compares each note with its original value and omits unchanged
languages. The installed generated 0.4 Create/Update inputs accept optional
`cs_note`/`en_note` as `string | null | undefined`; the adapter forwards supplied
parameters directly. Omission preserves an existing note; null clears it.

Evidence correction: the fixture in
`e2e/specs/app/security_advisories_admin.spec.ts:230` **does honor null updates**.
In i2's retained [retry0 evidence](w-670-broad-trace-evidence.json), the admin
management case's bulk PUTs to assessments501/502 send both notes as null and
receive null notes. They follow the successful individual edit that set501's
English note. Trace SHA256 is
`8f0b56d7621ab64fea0e09da3ed49f849a961e6b3102042e8eb9d4da63b6da16`.
The earlier claim that the fixture ignored null is withdrawn. The first failing
exact-body assertion also lacks the required `expected_state`; its later
note-preservation assertion is valid and must remain. This is source plus modeled
wire evidence, not a claim about an observed production write. Confidence in the
form defect is high; no backend/client repair is indicated.

### Selected behavior and state

Use the existing Checkbox and Textarea components. In the **bulk form only**,
each displayed language gets an initially unchecked note-update checkbox beside
its existing textarea. Disable that textarea while unchecked. Keep language
association visible and in the accessible name; focusing a control does not
select it. The existing single-node editor keeps its current presentation and
original-value comparison.

| Bulk language choice | Submitted property | Effect |
| --- | --- | --- |
| Unchecked, including default blank or a retained draft | Absent | Preserve that language on an existing assessment |
| Checked, nonblank after trimming | Trimmed string | Replace that language's note |
| Checked, blank or whitespace only | `null` | Explicitly clear that language's note |

Represent this with one bulk-only optional note-selection map in the existing
form values. An absent map retains ordinary-editor behavior; a present map requires
an explicit true entry before serializing a language. Initialize the map empty on
every successful `openBulk`, together with the existing blank note values. Validate
supported language codes before bulk omission, so opt-out cannot bypass the
existing unsupported-language refusal. Do not infer intent from focus, text
emptiness or a fabricated original assessment. Do not introduce a shared dirty-form
framework or a second wire-payload implementation.

Unchecking cancels that language's write while retaining its visible, disabled
draft until the modal closes. Rechecking uses that draft. Cancel/reopen starts with
blank notes and no selections; cancelling only the existing confirmation retains
the current form choices. The same selection rules apply when bulk creates a
missing assessment: omitted notes use the API's existing creation behavior,
without inventing a prior value. Keep the existing one-time payload capture in
`runBulk`; changing a control must not alter an in-flight batch or enable replay.

All other semantics remain: active-node targeting, missing-row creation, node IDs,
state/timestamp validation and precision, captured state/revision and snapshots,
effective capabilities, sequential revision advancement, confirmation/counts,
partial results, input retention and mandatory review after failure. Preserve
the all-six-action draft-sync gates and older-backend denial. No note normalization
belongs in the adapter, and no casts, guard weakening or coverage allowances are
part of this repair.

### Implementation and documentation boundary

Implementer2 owns this complete narrow package after lead releases its source turn:

- `src/pages/app/admin/security/SecurityAdvisoryNodeForm.tsx` and
  `SecurityAdvisoryNodesPanel.tsx`: bulk selection, controls and payload omission.
- `src/i18n/locales/{en,cs}/admin/security_advisories.ts`: two corresponding keys
  under the existing `admin.security_advisories.nodes.bulk` hierarchy for label
  and adjacent help. Use the approved wording in
  [the copy record](webui-broad-bulk-notes-copy-approved.json), including
  `Update {language} note` / `Změnit poznámku ({language})`; pass visible EN/CS
  codes consistently to both label and textarea. Explain unchecked preservation
  and checked-empty clearing next to each choice. Existing component label and
  description support is sufficient; no shared-control change is needed.
- Existing `SecurityAdvisoryNodesPanel.test.ts` and
  `SecurityAdvisoryNodesPanel.review.test.tsx`: payload and actual rendered-panel
  regressions. Reuse the existing snapshot test as single-editor coverage.
- `e2e/specs/app/security_advisories_admin.spec.ts`: retain exact request assertions,
  add the required captured expected-state values, and preserve both later note
  assertions and every subsequent publish/update/outage/negative assertion.
  Keep the fixture's real null-clearing behavior. This leaf already appears in
  `tsconfig.e2e.json`; no new strict-adoption metadata is needed for this package.
- Clarify REQ-055 and the existing localized-note paragraph in
  `docs/design/WORKFLOWS.md`; record the reason and actual quick results in the
  existing migration work-log entry, with review/native results still pending
  at commit time. Do not add a new documentation subsystem or regenerate API
  inventory when no route/adapter changes.

The main-agent wording pass is accepted after reading the vpsFree writing skill,
both Humanizers and the actual resolved terminology source
`/nix/store/030czw9xwvihmw4l24p97d5r2xxd71vi-source` at own locked API
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`. Guide/procedure SHA256 values match
`cb5296bc95a82823edae81041d40993cf0b65110b05ce3513031acdd2544780e` /
`c73e5709ed1ec65574af390b1072cd41124c41c34fa430e434623720ada9b47e`.
Lead's effective-site942c comparison proves identical guide blobs, not identical
API versions. The proposed copy needs no rewrite.

Local KB impact is confined to administrator advisory Nodes/bulk-note instructions
and screenshots; routes/navigation, roles and public note visibility do not change.
External page/concept mapping and currency are not established here. The workspace
procedure points to `vpsfree-kb-contracts/docs/webui-change-workflow.md`, whereas
the locked API guide retains the older `vpsadmin-kb-captures` name. No canonical
mapping was supplied within this read-only package; lead owns that bounded
read-only reconciliation. Do not claim external docs are unaffected or open a KB
write/publication campaign. Show actual implemented desktop/mobile cs/en captures
from synthetic fixtures after committed review, labeled with tested revision and
fixture scope; no live API or preview change is required.

### Acceptance, compatibility and recovery

Active tests must prove both note keys are absent for untouched bulk and focus
alone; selected text is trimmed; selected blank/whitespace clears only its language;
EN and CS are independent and can both be selected. Exercise unchecked-after-edit,
cancel/reopen, existing-row Update and missing-row Create through rendered controls.
Keep exact guards and mutation counts, and the stopped/read-back-failed batch's
no-replay assertion. Preserve ordinary-editor unchanged/set/clear behavior and
unsupported-language refusal. The existing browser case must again retain distinct
stored notes after a state-only bulk action; passing only the first repaired
assertion is insufficient.

Use the pinned environment for focused Vitest helper/rendered/snapshot tests and
the existing `ci:quick` gate (including strict source/tooling/E2E, localization,
documentation and quality checks). Commit all intended changes before independent
affected review. Parent then selects the actual affected advisory native cases
and implemented desktop/mobile captures, deriving membership before launch.
Fold these into the already authorized broad-CI repair verification rather than
creating a second 33-case campaign. The final broad workflow must pass in its real
configured projects; preserve actual counts, skips and earlier failed evidence.
Fresh Luna watchers own long checks, with unchanged retry/cap rules. Architect
ran no checks or native operations.

This is an application-only correction using the existing generated-client0.4 /
HaveAPI0.32 patch contract and A040 backend minimum. It changes no schema, persisted
format, package/runtime/API pin, CLI, daemon or site configuration. Compatible
guard-capable backends need no coordinated upgrade for this fix; older-backend
refusal remains. The running4ed/API610 preview remains unchanged and cannot certify
these guarded writes. Software reversal is an ordinary new source revert, but
reverting restores the accidental-clear risk and cannot recover already cleared
notes. Recovery of persisted content needs known prior content and an explicit
guarded correction or existing backup; never reconstruct it by automatic replay.

The product choice is settled; lead retains scope/source release and the external
KB mapping disposition. The next result is i2's implementation with active focused
regressions and quick results, followed by committed review and native evidence.
