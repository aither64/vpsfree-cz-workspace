# HaveAPI JavaScript Promise support: investigation and implementation proposal

Status: execution authorized by the user's **“Implement the plan.”**, 2026-10-19.
Architect: `architect0`. The lead has released the initial implementer packages.
This brief governs application work; the architect edits design only. Revised for the user's
standalone async client object: this supersedes the Async-suffixed method proposal.
The user has also selected TypeScript authoring for **both** the existing callback
Client and new AsyncClient, superseding the earlier async-only source option.
The earlier investigation performed no implementation. Execution progress and
verification results belong in state.md and implementer reports, not historical
claims in the evidence section. Current browsers and React WebUI adoption remain
requirements. Later user directions authorize HaveAPI/master, the reviewed
dev-workspace fix/master and the shared runtime update described below. WebUI
integration, npm publication, other default-branch integrations and session
lifecycle actions remain outside that authorization.

## HaveAPI master reconciliation, 2026-10-20

**Second target refresh.** The first reconciliation is reviewed at
`e16526d42949bae96bf35e8db6cd984d739dcc2a`, tree
`32b6099b5ec3e367c9ce86b81afa8c4ee74b461c`, eight commits above c182;
all six exact-head CI checks passed. Target is now
`a8ea3132e7efe601aaa8965afe648459b3dab5c5`. Claim
`1cd94ef4-e345-44cf-b351-cc54733406dc` remains held by the lead through the
remaining HaveAPI-only operation. `final-integration/incoming-drift.json` and
`incoming.diff` beneath `haveapi-merge` record four upstream commits/seven paths:
Ruby 3.4 shells, Nixpkgs refresh, Python certifi/Ruff refresh and explicit Ruby/Go
test-server BUNDLE_LOCKFILE. None overlaps c182..e165; no JS runtime changes.

After lead release, owner0 preserves published e165 under
`2026-10-19-haveapi-async-client-before-toolchain-rebase`, retains the existing
old403 preservation ref (and reachable f94), and cleanly replays the same eight
commits on fresh-confirmed a8ea. Expect no edits or conflicts; stop and report if
that expectation fails. Preserve all seven incoming blobs and the complete
reviewed feature diff/commit purposes. Record range-diff/patch IDs and independent
final-tree reconstruction. Feature publication uses only an explicit e165 lease;
master remains normal fast-forward/SSH. WebUI and its source pin stay unchanged.

Mechanical patch equivalence can retain unaffected client/history evidence, but
the installed review exception is not a blanket exemption here: Ruby selection
and test-server environment change substantive execution inputs. A schema-1
receipt/reconstructed tree alone cannot waive that boundary. Request only focused
general and risk/compatibility review of the changed toolchain/test-harness
interaction and resulting range, retaining the prior four-lane client/release
review. No broad Python/client audit or new architecture is needed. Unexpected
conflicts or fixes expand only the affected review lanes through the lead.

Minimum fresh checks in the new locked Nix shell: record Ruby/Node/npm/tsc/uv/
Python identities; run release metadata, combined release RSpec/Python artifact
tests and normal required hooks. Use a fresh utility for uncertain-duration shell
setup/checks. Confirm the real disposable version fixture still passes; do not
change actual versions or bypass Ruby ABI/tooling failures. After the focused
review, run one bounded JS build/normal pack/isolated runtime+declaration smoke
with the new tools and inventory its final-source bytes. Old403/e165 package
proof remains historical; equal source alone does not establish tool-input reuse.
Observe applicable new-head automatic CI, including changed Ruby/Go harness
coverage; prior six green checks do not certify the new head. No full local
multi-language/WebUI/browser/release campaign or new package-pin stream.
Lead's HaveAPI/master approval continues for this patch-preserving refresh;
material semantics or further target drift return to the lead before integration.

User explicitly approved HaveAPI/default integration and forbade WebUI merging.
Reviewed source is `40365b47a1a0c946367bc4596db6060853b52c0a`, tree
`3fe6010640cf64a063731fe8c49eb5819ca94b59`, eight commits above
`c58704a08451a231fdf6c6123437133422af46dc`. Owner0 fetched new master
`c1823f3d70365b0442d0e2171bdf83bd4c6dbe31` under lead-held HaveAPI claim
`1a971f9a-eb1c-4b18-ae1c-156e098d27c2`; source remains clean. Incoming is
eight Python-client/release commits over 62 paths, not merely additive guidance.
Neither tip contains the other. Evidence: `haveapi-merge/drift.json` and the
incoming/feature series and overlap diff beside it.

**Route after lead release.** Owner0 exclusively owns rebase/code/Git under
the verified repository claim. Preserve and publish the old source under
`2026-10-19-haveapi-async-client-before-master-rebase` at exact `40365b4` before
replacing its feature ref. This keeps original published
`f94e65e35166a0bf8048a27c9d57c7d36957d65b` reachable for WebUI's archive
provenance; no WebUI source/lock/archive/PR change. Rebase the existing eight
feature commits onto fresh-confirmed c182, preserving their substantive split
and authors. Retain incoming Python source, workflow, hooks and Nix additions.
No merge commit, default-history rewrite or force push to master. Own unmerged
HaveAPI feature publication may use an explicit lease against recorded old403
after review; WebUI's stricter published-history rule does not apply here.

**Five overlaps.** In Makefile keep Python check/integration, uv sync/lock and
Python release-test commands together with JS npm ci, client.ts and both npm
lock-root version updates. In artifacts.rb retain Python artifact names,
version/tool/lock provenance and Python validation in complete inspect_packages
after PHP; keep inspect_npm as the JS-only validator and retain the installed
CJS/types smoke. Preserve both sets of release specs. The disposable make-version
test must copy the incoming Python inputs and use the new shell's real uv path;
any offline/cache accommodation stays test-local, preserves Python version/lock
updating and never disables production commands or runs a real source bump.
If a meaningful fixture change is needed, owner0 reports its exact seam first.
README keeps Python's bullet plus the approved one-line JS/TS bullet. Release
guide combines both client/package descriptions, commands and PyPI recovery with
our npm lock/install/type checks. Owner1 may reconcile those two docs after lead
assignment; owner0 alone owns index/rebase continuation, including their files.

**Acceptance.** Record range-diff/patch IDs for all eight commits, explicit
resolution diff, all nonoverlap upstream blobs preserved, and exact JS subtree,
runtime/declarations, npm lock and consumer fixture equality to reviewed403.
Run focused combined release RSpec/Python artifact tests, metadata, scoped
lint/hooks and docs links in the updated repository shell; use a watcher if the
uv fixture makes duration uncertain. No full Python-client or WebUI audit or new
browser campaign. Because shared release behavior changed upstream, pure
mechanical review reuse is insufficient: reviewer0 assesses the reconciled
shared release/docs boundary and whole-series/no-migration conclusion after
quicks, reusing unaffected accepted client review. Prior exact403 CI is historical;
observe applicable automatic CI on the new head. Reuse installed-tar evidence
only with proven package bytes, smoke/compiler/dependency inputs unchanged;
otherwise repeat just that proof after review. No whole release rebuild by default.

Lead accepts equivalence and resolves any material semantic deviation before
integration; ordinary patch-preserving rebase keeps the user's repository/target
approval. Capture the final comparison, recheck target/feature refs, then perform
only normal fast-forward/SSH integration under the held claim. Further target
drift returns to bounded assessment. No version/publication/deployment/lifecycle
action is included. Reconciliation does not alter persistent state or add a
migration. This brief itself performs no rebase, ref/index or source mutation.

## README and release-check update, 2026-10-20

The user requests updating the project README for JavaScript/TypeScript usage
and checking the release process. Baseline is clean published HaveAPI
`f94e65e35166a0bf8048a27c9d57c7d36957d65b`. Append scoped changes; preserve
published history. This package does not authorize a version bump, release
branch/tag, npm publication, workflow dispatch, default merge or deployment.
WebUI `8772bab2`, its vendored f94 package and pending history decision are
independent; do not repin that dependency for documentation/release-helper edits.

**Audit and contract.** There is one npm package, `haveapi-client`, authored in
TypeScript and distributed as ordinary JavaScript plus generated declarations.
It exports callback `CallbackClient`/`Client` (same constructor) and `AsyncClient`;
both JavaScript and TypeScript users consume the same package. Existing plain
script/UMD, CommonJS, package name, main/types paths and callback behavior stay
unchanged. Gulp/tsconfig/package files already generate and pack the bundle,
declaration tree and async guides; the version source already points to client.ts.
Do not create a separate TypeScript package or change the build format.

Concrete gaps are narrower: root/client README wording underexplains this
contract; npm artifact inspection checks only identity/bundle/version; extracted
smoke uses checkout NODE_PATH and tests only Client; `make version` omits the
now-tracked npm lock's two root version fields. `release-deps` still uses install
instead of the committed JavaScript dependency lock.

**Owner0 files:** `Makefile`, `utils/release/artifacts.rb`,
`utils/release/spec/release_spec.rb` and a small release consumer fixture only
if useful. Update package-lock top-level `version` and `packages[""].version`
alongside package metadata; preserve every nested dependency/version/integrity.
Check lock identity/root versions against VERSION. Use `npm ci` for JavaScript
release dependencies. Test version updates in a disposable copy, never by
bumping the real checkout. Inspect exact main/types paths, nonempty emitted
declarations and shipped README/async guides/license in the real npm archive.
Ensure missing transitive declarations are caught, not just the entry filename.

Replace checkout-module smoke with normal installation of the retained tarball
in an isolated temporary npm consumer, scripts disabled and no NODE_PATH bridge.
Require package-name CommonJS import, CallbackClient === Client, matching legacy
version, construction of both clients and absence of a default-wrapper requirement.
Compile a consumer importing callback/async exports by package name against the
installed declarations using the existing pinned TypeScript compiler. It must
not resolve authored source or checkout declarations. No API/network-operation
suite or new browser harness is needed; npm runtime dependencies may resolve
normally for this isolated install.

**Owner1 files:** root `README.md`, `clients/js/README.md`,
`doc/agent-instructions/releases.md`. Explain one package/two APIs/two consumer
languages, link async/type usage, scope callback setup examples, and describe
gulp-before-pack plus the actual installed runtime/type smoke. Keep release
approval, shared version, artifact reuse and failure-recovery instructions.
Lead performs the prose/fact pass before commit release; owners serialize Git
and use command-scoped Jakub author/committer with normal hooks.

**Acceptance and checks.** Quick: focused release RSpec including missing/broken
package content and lock-version regressions, metadata check, Ruby/Makefile
syntax as applicable, documentation links/examples and normal lint/hooks.
Final committed review precedes a bounded fresh-watcher proof of the real
retained npm tarball's install/runtime/declaration smoke. No full Ruby/WebUI
rerun or full release build is required for this bounded change. Leave release
workflow/actions/publisher, manifest schema, immutable artifact checksums and
no-rebuild-after-approval unchanged. No runtime, schema, state or deployment
migration results; rollback is the previous tooling/docs revision.

## Production WebUI replacement: current execution brief, 2026-10-20

The user's **“well no trial, just replace the original solution in
vpsadmin-webui with the new client”** supersedes every pilot-only, unchanged-default
and publication-prerequisite boundary below. Replace the production transport;
retain domain helper signatures and application policy. PR74 stays open. No
default integration, npm release, deployment or runtime-rollout action follows
from this brief. Architect owns design; lead releases the packages below.

**Baseline and history.** Owned WebUI `vpsadmin-webui-async`, branch
`dev/haveapi-async-client`, is clean at
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Owner1's fresh SSH check found main
`b9f47f06e0877eb4a160053c413c4b87dd4a3d55`; the 20 incoming commits overlap the
pilot only in three additive documentation files, with generic transport,
bootstrap, configuration and package inputs unchanged. Prepare additive work on
the existing feature; preserve incoming consumers and all contributor history.
No rebase or published rewrite is released. Before final review, lead inventories
the complete series and proposes any necessary consolidation/rebase using exact
ranges and preserved original refs; published-history permission remains separate.
Use command-scoped Jakub Skokan <jakub.skokan@havefun.cz> author and committer.

**Post-review consolidation recipe (design only).** Reviewer0's Important
whole-history finding requires removing obsolete pilot iterations from the final
series; publication is not an exemption. The exact old range is
`7860521f30826c3886c89c35e8ab6f4e082e0a4b..8772bab21cd8739bf4672cdf4976aea2a6e59de3`,
including published `0d05a2584bf30ee4acfa1d64bf00325cdda62934` and
`5dd2333b9af230d4a81c8f772cbbb08d39b14913`. Proposed retained ref:
`dev/haveapi-async-client-before-production-consolidation` at `8772bab2`, keeping
both published commits reachable. No ref creation or rewrite is authorized here.

Prepare two final commits on fresh-confirmed main (currently `b9f47f06`):
(1) the final vendor archive/provenance, package manifest/lock, frontend Nix
dependency configuration, source checks/tests and packaging documentation;
(2) actual production adapter/public/description integration, migrated unit and
browser tests, XHR fixture/setup, error mapping, structural/type-coverage records
and current design/work-log documentation. Put the runtime-facing HAVEAPI_CLIENT
guide in (2), avoiding a commit claiming an unimplemented production default.
No pilot runner, temporary entry, opt-in API or add-then-delete pilot commit
belongs in either. Retain useful dated pilot findings as historical evidence,
with references to preserved original commits, not executable obsolete recipes.

Reconcile all six overlaps deliberately: preserve both contributors' entries in
WORK_LOG/API_CONTRACTS/REQUIREMENTS; union main's adopted E2E coverage with public
overview in `scripts/fixtures/e2e-type-coverage.json` and `tsconfig.e2e.json`,
removing only corresponding deferred entries. Preserve main's new node overview
and maintenance-capability tests in `src/lib/api/nodes.test.ts`, convert their
fetch fixture to the actual-package XHR fixture, retain GET/no-pagination and
OPTIONS method query checks, and prove abort behavior rather than fetch-init
signal identity. Preserve main's node helpers and every nonoverlapping change.

Owners may prepare a reviewable patch/content preview after lead lifts the freeze;
private index/object previews do not authorize updating refs or bypassing normal
hooks for deliverable commits. Lead requests exact published-history permission
only with the prepared old/new range, preservation ref and reconciliation diff.
Run focused nodes/API/session/public tests, E2E type coverage, docs/inventory and
package/provenance checks on the reconciled candidate; independently review its
whole series and conflict resolutions. Prefer waiting to run full app/browser/Nix
verification until that final candidate is committed and reviewed: main changes
behavior and test coverage, so a full pass on `8772` would not certify the result.
Pure dependency receipts may be reused only with identical source/lock/tool inputs.

**Runtime contract.** Import the actual npm package's named `AsyncClient` in
production. Lazily create separate authenticated and public clients per resolved
API base after existing runtime bootstrap. The configured base already includes
the API version: use setup-free `request({method:'OPTIONS', path:'/'})` for
fallback description discovery, not `setup()` adding a version. Retain supplied
window descriptions and the existing fully configured-header/metadata shortcut.
Use `request<T>` for ordinary authenticated and public calls; its validated
`data`, `meta`, `envelope`, `httpStatus` are the only wire-result boundary.

WebUI reads live runtime credentials for every dispatch; do not call library
authentication or cache tokens there. Preserve configured/described/fallback auth
headers, impersonation token header, language, abort and same-origin credentials
semantics. Public calls have separate state, Accept only, no auth/language,
description discovery or session renewal. Remove fetch transport, query/body
encoding and JSON/envelope decoding. Retain only scalar-query admission,
one-read immutable retry inputs, existing omission of params without an input
namespace, and projection of validated payloads to the public helper shape.
Projection retains configured/`_meta`/`meta` fallback, single namespace,
raw-array/null and multiple-namespace behavior without a second protocol decoder.

Keep HaveApiError/request diagnostics, HTTP200 API-rejection status convention,
session-expiry event, domain guards and action-state/ambiguous-mutation handling.
Reuse BFF renewal unchanged: qualifying OAuth HTTP401 reads retry once with fresh
auth and original inputs/language; writes may renew but never replay. Preserve
concurrent renewal and logout/identity-change guards; no retry for impersonation,
403, malformed replies or transport failures. BFF config/session and OAuth token
fetches remain outside HaveAPI. Missing success payload or invalid metadata stays
a protocol failure, distinct from valid null and authoritative API rejection.

**Provider prerequisite, owner0.** At HaveAPI
`19c20c90cc957d4225ece50a92e190855f252710`, stock validation errors are flat;
public `Action#error!` plus recursive localization can also emit nested maps.
Support nested wire errors rather than misclassifying existing WebUI rejection
cases. Keep local `ValidationErrors` flat and callback runtime/declarations
compatible. Add a recursive wire-error map with string-array leaves; use a
defaulted second Envelope type parameter for async wire errors while preserving
the callback default. AsyncError and RequestResult use that wire type. Reject
scalar/non-string leaves. Owner0 owns `clients/js/src/haveapi/{types.ts,async/}`,
entry type exports, focused bundle/declaration regressions and client docs;
change only error typing/decoding there. Test nested HTTP200/422 rejection retains
errors/envelope/receipt; malformed leaves remain protocol failures.

**Production source package, owner1.** Own `src/lib/api/haveapi.ts`,
`haveapiRequestClient.ts`, `public.ts`, removal of redundant `haveapiTransport.ts`
and `haveapiEnvelope.ts`, their tests, affected domain/browser fixtures and WebUI
design/work-log/inventory updates. Make the adapter the sole normal path; remove
its opt-in surface. Tests use the actual package with controlled XHR, not a fetch
stub masquerading as the library. Preserve all 57 domain-helper consumers.
No unrelated pages, backend or BFF changes. Owner1 owns API-contract docs;
owner0 owns package/provenance documentation, coordinating shared indexes.

**Dependency package, owner0.** Commit one normal npm-pack archive from the final
corrected, committed/published HaveAPI source as
`vendor/haveapi-client-<full-source-SHA>.tgz`. Root dependency is
`file:vendor/haveapi-client-<full-source-SHA>.tgz`; import `haveapi-client` normally.
Own vendor/provenance, root manifest/lock, frontend Nix dependency configuration,
package checks and
obsolete `scripts/haveapi-package`/runner/script-registration removal. Consolidate
useful package/type/browser cases into normal tests; no pilot app remains.
Git npm dependencies cannot select this repository's `clients/js` subdirectory;
expiring CI artifacts are unsuitable. No version bump, installer or source alias.
Document exact source/toolchain, archive SHA256/integrity and file inventory.
Regenerate in the HaveAPI Nix shell with client `npm ci`, normal gulp build and
`npm pack --json --pack-destination OUT`; bind packed files to that source, then
rename/copy the archive without modifying it. Existing 51-file archive is prior
evidence only: the error fix requires a new final archive.

Use normal pinned WebUI npm install to record the relative archive and resolved
transitive dependencies, then clean `npm ci`; preserve unrelated locked versions.
Regular vendor archives pass the current Nix source filter. The actual pinned
`prefetch-npm-deps` failed on `file:///vendor/...tgz` with `invalidformat`; normal
npm lock/install and clean `npm ci` passed, preserving all 482 previous lock
entries. Use the existing pinned Nixpkgs `importNpmLock` support below; do not
filter the lock, inject a fabricated cache/hash or change the toolchain.

**Nix correction after concrete failure.** Owner0 changes only
`packages/frontend.nix` and its package/provenance documentation. Keep
`pkgs.buildNpmPackage` and replace the frontend `npmDepsHash` with:

```nix
npmDeps = pkgs.importNpmLock {
  npmRoot = source;
  packageSourceOverrides."node_modules/haveapi-client" =
    "${source}/vendor/haveapi-client-f94e65e35166a0bf8048a27c9d57c7d36957d65b.tgz";
};
npmConfigHook = pkgs.importNpmLock.npmConfigHook;
```

This exact single-package override is supported by the helper at locked Nixpkgs
`5e2305d577ca00acbba631b05cb1094d172b29f3`,
`pkgs/build-support/node/import-npm-lock/default.nix`; the matching hook and
`doc/languages-frameworks/javascript.section.md` document the build integration.
The override points to the same committed archive consumed by npm; all remote
packages retain lock integrity hashes. The helper generates private store
metadata with resolved store paths, normalizes locked `latest` references and
installs offline with its standard hook. That hook restores the original
manifest/lock before application build. Repository manifest/lock bytes are not
rewritten, and no aggregate frontend hash is needed. Preserve frontend Node,
prePatch/source audit, preBuild/docs audit, provenance and install allowlist;
leave BFF hash/configuration, flake inputs and source filtering unchanged.
Document this frontend/BFF distinction in `docs/design/PACKAGING.md`. One quick
Nix evaluation/derivation inspection is permitted before review; the full
frontend and package-content builds remain post-review gates, not claimed passes.

**Ordering and gates.** Provider and WebUI source packages can proceed independently
at the interface above; lead serializes WebUI Git/index operations. Final archive,
lock/Nix dependency configuration and default source form one reviewed candidate,
not intermediate pins.
Quick gates: focused provider/actual-package API, renewal/public/domain tests,
declaration consumers, type/tooling/e2e checks, scoped lint/format, docs inventory
and audits, source/archive/lock integrity and normal hooks. After all intended
changes are committed, run all applicable final-review lanes with whole-history
and no-migration conclusions. One fresh watcher then runs clean npm ci, full app
tests/build, Nix frontend/source/package checks and normal app browser workflows:
public pages, authenticated home, expiry/renewal, create failures, blocking-action
progress and cancellation. No dedicated pilot entry proves production adoption.
These fixtures do not certify live OAuth or backend deployment.

No schema, stored-session format or backend wire change is required. The new
frontend remains compatible with existing services; rollback restores the prior
frontend package with its matching lock, without data migration. No live rollout
is authorized here. Completion requires every HaveAPI path using the package,
preserved request/error/session behavior, reproducible npm/Nix/CI and passing
ordinary application workflows. Packaging feasibility is a gate, not a reason
to hold independent source work or introduce a parallel transport.

## Execution addendum and interface freeze

### Shared runtime adoption after explicit user approval

The user answered **“yes”** to merging the reviewed dev-workspace fix into
master, updating the shared runtime, then completing the HaveAPI merge while
leaving WebUI open. This supersedes the preparation-only authorization below.
The lead owns approvals, queue submissions and activation; architect0 owns this
brief, implementer0 owns source/equivalence evidence, and implementer1 owns the
two pin streams. Do not change product review heads, publish npm/tag releases,
alter lifecycle state or integrate workspace/configuration defaults by inference.

**Actual source and preservation gate.** The selected package is
`/nix/store/ad0s75irvrbj6pz6qk1zf7v9sy4l1qyp-dev-workspace-0.2.0`.
Its derivation's generic source
`/nix/store/i5nqmglmzr0v80hq10cb5ibr0xrk6ccw-source` matches all 501 regular
tracked files of published `6ab3b48f57981f4358094b47cac1ba724c458396`, with no
changed/missing/extra regular files. This contains `10eccece` lifecycle-access
waiting and `6ab3b48f` archive-reservation release on top of `09a40795`.
Those deployed changes must survive adoption. Reviewed Ruby fix
`dce4784fe0069b061dd76cdf689e2099b4b0e66d` alone, based on `09a40795`, is not
a sufficient runtime candidate. The lead verified its separate approved master
merge succeeded at that exact `dce4784` head.

Default to the next published canonical runtime containing both the reviewed
fix and all selected/deployment-frontier behavior, after the existing owners'
normal integration/release. Prove ancestry or retained reviewed replacement
lineage; do not merge their unmerged features under our core-fix approval.
Recheck this condition before activation because the queued browser rollout can
advance the required source. No composite-source application edits are released
by this brief. If earlier composition becomes necessary, agree its supported
registration and lineage with the lead first.

**Worktrees and exact edit boundary.** Lead creates/registers normal canonical
names with `dev-session worktree add`, rechecking fetched bases first:

- `workspace`, dated branch `2026-10-19-haveapi-async-client`, created clean at
  fetched base `4bc49561dd48842b5b26c2e247d6d6b8c6b8a513`; path
  `worktrees/2026-10-19-haveapi-async-client/workspace`.
- `vpsfree-cz-configuration`, same dated branch, candidate base
  `a2ad6da408715de811cc6d8ea7b29ac55ea341ec`; corresponding same-session path.
  Lead reports creation pending; do not claim registration until it completes.

Use `--as-is --branch 2026-10-19-haveapi-async-client --base BASE` with those
project names. Preserve shared master and unrelated tracking. No additional
`dev-workspace-runtime` alias: ordinary worktree aliases are supported, but the
selected coordinator resolves registration **name**, not project, against its
immutable catalog, which has only `dev-workspace`. Keep the existing canonical
source registration. Worktree preparation can proceed; pin values wait for the
preservation gate above.

Implementer1 owns workspace `flake.nix` and generated `flake.lock`: change only
`inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to the exact published
runtime, then run `nix flake update vpsfree-dev-workspace/dev-workspace` in that
worktree. Preserve extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` and its
content hash, sibling input identities, follows paths, catalogs and host/site
configuration. Selected ad0's workspace source has the same agent-team,
coordination, integration and registration files as current workspace master;
its lock differs only in the generic `dev-workspace` node.

In configuration use the existing `dev-workspace` channel / `devWorkspace` role
and generated lock only. For the published integrated source, run
`confctl inputs channel update --commit dev-workspace devWorkspace` and verify
it resolves to the exact agreed revision. An explicitly agreed published feature
candidate would instead use `channel set --commit dev-workspace devWorkspace REV`.
Do not hand-edit the lock, change host module code, update another channel or
install the application through system configuration. Preserve generated commit
messages and consolidate each final pin stream before review.

**Verification and deployment order.** Quick gates are clean scoped diffs,
semantic lock/follows comparison, unchanged extension/siblings, declared hooks,
and `bin/check-dev-workspace-deployment --workspace-root ABS_WORKSPACE_FEATURE
--configuration-root ABS_CONFIG_FEATURE`. Record complete branch ranges and
no-migration conclusions; apply mandatory review to substantive changes and its
mechanical-pin exemption without waiving history/equivalence checks. Then use
fresh verification watchers for the composed package/check builds and
`confctl build cz.vpsfree/machines/aitherdev`. Reuse earlier core test results
only when their complete derivation/input identities match. Build/copy outside
claims and prepare the system from the exact final configuration commit, since
its revision is embedded in the artifact.

The installed coordination guides and configuration's aitherdev procedure
require matching system-module selection followed by user-profile activation.
Submit ordinary approved `machine_activate` (dry activation then no-reboot
switch) and dependent `profile_activate` jobs under one `vpsfree:aitherdev`
reservation. Use the actual user instruction as deployment evidence. The
foreign review reservation and already queued owner keep their order; no direct
confctl/profile switch, private helper, forced release, owner pressure or
catalog bypass. Refresh stale preparation against the actual integrated/frontier
source and selected generation before admission. Verify system and system-profile
identities, selected application package, composition, portal/router and retained
Codex/tmux continuity. Freshly prepare the authorized HaveAPI merge afterward.

**Release and recovery limits.** Workspace and configuration feature pins are
not authorized for master integration; request that specific decision only when
the concrete reviewed candidates exist. Reservation creation freezes every
current registered repository as an obligation, and normal `finish` proves each
exact head integrated. This session's intentionally open WebUI registrations
also remain obligations; their names are absent from the selected catalog.
This is a completion refusal, not an admission refusal. In selected `6ab3b48`
source, `workspace-coordination.rb:802` validates obligation registrations and
targets without looking up the catalog; `:1204` freezes all manifest entries.
Job creation and claim (`:1274-1425`) check approval, dependency, owner/machine
and queue eligibility, not the eventual integration proofs. Normal system/profile
coverage is derived from catalog-mapped deployed inputs, so unrelated unknown
WebUI registration names do not themselves stop those operations.

At `finish`, `workspace-coordination-execution.rb:617-641` requires exact
`finalHeads` for every current/frozen registration. Omitting WebUI fails with
`finalHeads differs from owned integration obligations`; including its entries
reaches `repository()` / catalog lookup and fails with
`repository is absent from coordination catalog`. Even a catalog entry would
still require the exact open feature head integrated. These are read-only source
findings; no reservation or deliberate failing admission was submitted.

`workspace-host prepare` builds and checks a candidate only. `switch` enters the
coordinated path (`workspace-host:614-617`), whose
`find_or_submit_profile` requires the existing owner reservation
(`workspace-coordination-execution.rb:18-23`). A merge-only core job or separate
profile preparation does not avoid freezing these obligations. There is no
supported normal deployment-and-release route within the current session scope
while WebUI must stay open. Continue preparation outside claims, but hold
deployment submission until the lead resolves that explicit limitation. Do not
create an indefinite machine hold merely because admission permits it, remove
registrations, invent catalog aliases or add unrelated lifecycle work.
No ledger/schema/journal/adapter contract migration is proposed. Preserve all
original attempts and receipts. Unknown system effects use original-attempt
reconciliation with both live identities; profile recovery remains forward-only
to the admitted candidate or a reviewed compatible successor. No replay,
automatic downgrade, reboot, archive or deletion is authorized.

### Coordinator hook-runtime blocker: preparation-only correction

Historical preparation scope; runtime adoption authorization is now governed by
the preceding section.

The user approved only HaveAPI integration and keeping the WebUI PR open.
HaveAPI `19c20c90cc957d4225ece50a92e190855f252710` and WebUI
`5dd2333b9af230d4a81c8f772cbbb08d39b14913` remain unchanged by this package.
Coordinator preparation failed before a snapshot/job, so no merge occurred.
See [ABI evidence](premerge/hook-runtime-diagnosis.md) and its checksummed JSON
receipt: selected runtime Ruby 3.4.9/ABI 3.4.0 was forced into HaveAPI's declared
Ruby 3.3.10/ABI 3.3.0 shell and native gem home. Reinstalling both ABIs into that
shared gem tree is unsafe and is not the proposed repair.

Read-only canonical inspection found `dev-workspace` local `master` and cached
`origin/master` both at `09a407953026514ae84be81dab9442fd74b6a362`.
`libexec/workspace-coordination-execution.rb:335-378`, especially line 355,
still passes `RbConfig.ruby` after `nix develop --command`, matching selected
package `/nix/store/i144xnc9p02svar5kz6jxjjpp6gz4cwh-dev-workspace-0.2.0`.
No existing fix was found in that cached head; this inspection did not fetch.
Lead rechecks the fetched base before releasing a new source worktree.

**Minimal change / implementer0:** replace only the child executable argument
with `'ruby'`, resolving through the entered repository shell's PATH. Keep the
shellHook, Ruby validation program, Bundler.setup/Overcommit requires, inherited
gem-variable scrubbing, allowlist, marker parsing, environment restoration,
retained roots and later hook execution unchanged. No interpreter override flag,
ABI fallback, dependency repair mode, hook bypass or private helper invocation.
Owner0 owns `libexec/workspace-coordination-execution.rb`, focused changes in
`test/workspace_coordination_test.rb`, and a short `docs/coordination.md`
clarification that validation uses the repository-selected Ruby.

Lead creates/registers the same-session worktree
`worktrees/2026-10-19-haveapi-async-client/dev-workspace`, proposed branch
`2026-10-19-haveapi-async-client`, from the confirmed canonical source.
Do not reuse another session's checkout, modify installed store files or touch
the HaveAPI/WebUI review heads. Source preparation is a separate package;
activation, new repository integration and machine ownership are not authorized.

**Meaningful regression:** strengthen the existing shell-initialization test
(`test/workspace_coordination_test.rb:51-78`) with an executable `ruby` shim on
the entered shell's PATH that records selection and delegates to real Ruby.
Invoke the actual preparation method and program in the disposable test store;
the old absolute-Ruby implementation must fail the selection assertion, while
the changed command succeeds. Retain exact allowed environment assertions,
excluded secret, inherited-variable scrubbing and original environment restore
on success/failure. Fake shells must provide a runnable Ruby; the existing
missing-Overcommit test must still fail for the missing dependency, not a missing
interpreter. Preserve the test exercising real target-checkout hooks and runtime
Git/SSH PATH composition. Do not settle for a source-string or argv-only test.

**Independent evidence / implementer1:** after lead release, verify the real
HaveAPI 19c shell selects Ruby 3.3 and its matching native extensions, with
Bundler.setup and Overcommit loading successfully. Use an owned disposable copy
of the exact committed source and isolated source-local gem home, normal shell
initialization, and the same validation program; preserve original retained
evidence/gems. Report interpreter path/version/ABI and declared environment
keys, never full environment/secrets. This verifies the real environment while
owner0's regression proves coordinator command selection. No production job,
default-branch mutation, package selection or private coordinator call is part
of this verification.

Quick checks run under dev-workspace's Nix shell: Ruby syntax and the focused
coordinator selection/dependency/environment tests, followed by normal hooks.
Commit the cohesive source/test/docs correction and perform independent final
review of this newly affected component, including whole-branch history and
explicit no-migrations conclusion. Run uncertain-duration package/coordination
suite and real-ABI checks through the verification watcher after review. The
retained team settings and single Git/generated-output owner remain in force.

**Compatibility and later rollout:** no ledger, journal, schema, request,
artifact, reservation, profile or public command contract changes. Existing
prepared artifacts and workers retain their recorded environment/generation;
new preparations use the corrected interpreter selection. Old packages can
read the same state, although they retain this preparation defect. The selected
runtime remains unchanged during preparation. A later candidate must use the
normal composed workspace nested runtime pin and matching configuration channel,
preserving extension/sibling inputs and passing deployment-composition checks.
Prepare source/review/build evidence outside claims, then present the exact
candidate, package diff and rollout/recovery scope to the user. HaveAPI merge
approval does not authorize these additional integrations or runtime activation.
The foreign `vpsfree:aitherdev` reservation must remain untouched; any later
approved system/profile rollout waits through normal coordination. No direct
activation, claim acquisition, forced release or old-store fallback is allowed.
Package selection is forward-only: recover through the supported original
attempt or reviewed successor, not by changing private state. Once a corrected
runtime is legitimately selected, freshly prepare the still-approved HaveAPI
merge with current evidence; do not reuse the failed preparation as a job.

This addendum fixes the accepted execution choices and supersedes conditional
build wording in the earlier proposal below. Current implementation bases:

- HaveAPI: `worktrees/2026-10-19-haveapi-async-client/haveapi`,
  `cb3f39f75e8a63416388d24293f936d1db97162b`.
- React pilot: `worktrees/2026-10-19-haveapi-async-client/vpsadmin-webui-async`,
  branch `dev/haveapi-async-client`, base
  `7860521f30826c3886c89c35e8ab6f4e082e0a4b`. The earlier dated-branch WebUI
  worktree is read-only and not an implementation destination.
- Baseline HaveAPI dist SHA256, captured by implementer1 before conversion:
  `3e8fcefe8edf78f6cea635c1bf4312b56c2e05355287153e142d30a9608c6436`.

**Build fixed:** keep the gulp command; run `tsc` with `target: ES5`,
`module: ESNext`, declaration emit, then Rollup named-export UMD at unchanged
`clients/js/dist/haveapi-client.js`. Preserve package main, `HaveAPI` browser
global, AMD/CommonJS shape and `Client.*` static exports; add `AsyncClient`
without a `.default` wrapper. Generated declarations go under `dist/types` with
a matching package types entry. No separate ESM runtime artifact initially;
React/Vite consumes the packed CommonJS/UMD package. No new engines restriction,
runtime polyfills or eager Promise/AbortController access during callback-only
loading, construction or requests.

AMD compatibility requires the original `define([], factory)` registration and
the factory's returned namespace object. Rollup's direct named UMD output uses
an `exports` dependency instead. Therefore generate a named-export IIFE payload
with Rollup, then compose the original UMD shell around it in the build: the
factory returns the local HaveAPI binding, CommonJS assigns `module.exports =
factory()`, and browser scripts assign `root.HaveAPI = factory()`. Final output
remains UMD; the intermediate IIFE is an intentional build detail. Do not weaken
the baseline AMD fixture or rewrite generated wrapper text with an unchecked
regex. Preserve ambient CommonJS/XHR detection if an inner export-container
parameter would shadow `exports`; keep any detection capture factory-local.

Use named-export TS modules at the existing source paths. Preserve function
constructors/prototype assignments and represent callable objects with component
interfaces plus constructable callable bridges; do not convert their behavior
to ES classes. `src/haveapi/types.ts` owns shared description, transport and
callback shapes; each component owns its public interfaces. Type-only imports
break type cycles. The export entry populates runtime `Client.*` and provider
registries in the original order after modules load.

Rollup `output.strict: false` is required for existing sloppy-mode behavior;
prevent the TS configuration from reintroducing a bundle-wide strict directive.
Preserve actual hook `.apply` receiver/argument behavior. Undeclared legacy
globals require localized, documented compatibility handling. The actual Vite
proof below supersedes bare ambient assignments for reachable global effects:
use an explicit typed host-global bridge for `Authentication`, `v1`, `v2` and
`ret`, preserving their observable values and live reads without a new
globalThis requirement. Unreachable references may use erased ambient typing.
Do not turn these into unrelated callback bug fixes. New async code is scoped
normally. Escalate broader incompatibility or disproportionate complexity.

The generated `i18n_messages.js` remains unchanged: implementer0 may provide a
typed catalog declaration and include its contents as Rollup factory-local intro,
preserving the existing catalog scope. Intermediate ES modules are build inputs,
not published runtime entries. No generator or translation changes are implied.

**Initial ownership:** implementer0 owns build/package/TS configuration, shared
types/export registration, callback client/http/hooks/authentication/exceptions/
i18n migration and generated dist. Implementer1 owns self-contained `node:test`
VM compatibility fixtures and callback action/action_state/base_resource/
resource/resource_instance/resource_instance_list/response/local_response/
parameters/validator migration, including validators. Fixture work can proceed
independently against the pinned baseline before converted modules exist. Both
read current repository guidance; only implementer0 edits build/export/shared
type files. Serialize Git operations and generated-output writes through lead.

**Shared seams:** normalize RequestSpec fields (method, API-relative path,
namespaces, params, meta, headers, signal and timeout) and snapshot per-client
request context at dispatch. The low-level transport reports HTTP status,
body and transport error without prematurely collapsing them. It must remain
usable by Client without constructing Promises; AsyncClient wraps that internal
completion boundary and applies the new rejection contract. Callback Client
keeps its existing observable outcome/timing mapping. Async RequestResult has
fixed data/meta/envelope/httpStatus fields; dynamic InvocationResult has fixed
value/response fields. Async resources invoke the normalized request seam and
return only async-owned objects. Auth state is per-client; WebUI supplies current
headers and retains its refresh/read-retry policy. No shared mutable mode flags,
credentials, prepared paths or callback-owned resource objects.

The accepted resource/core seam is `src/haveapi/async/types.ts`, owned by
implementer0. `AsyncResourceContext` supplies readonly `description`,
`metaNamespace` and `generation`, plus `request<T>(spec)`,
`validateParams(action, params?)`, `makeError(kind, message, details?)` and
`recordInvocation(value, response, action)`. Validation reuses typed coercion
and the snapshot's language context without mutating caller input; public
async methods turn its synchronous errors into Promise rejections. A resource
request checks the generation before sending; low-level client requests use
the current dispatch context. Absent/null `outputNamespace` selects the full
payload; a selected namespace must exist. RequestResult and InvocationResult
retain the fixed shapes above. Error details retain HTTP status, response,
envelope, validation errors, completion state, cause and reason when available.

Async MFA/resource snapshots use null-prototype parameter maps. The legacy
`Parameters` implementation assumes callable map-owned `hasOwnProperty`, so
implementer0 owns a narrow optional per-validation dictionary policy: async
validation supplies null-prototype allocation and safe own-key checks; the
default callback path retains plain objects and its original receiver-method
calls, including existing throws. Apply it consistently to Parameters-owned
result/error maps and ownership checks. Keep constructor arity/prototype and
legacy instance shape unchanged; no global policy, client mode flag, duplicated
validators or unrelated validator-option changes. Cover null-prototype MFA and
action input, own `hasOwnProperty`/`__proto__` parameter names, and callback
default parity. The resource-context interface is unchanged.

Implementer1 owns the resource factory and public resource type:

```ts
export function createResource(
  context: AsyncResourceContext,
  path: readonly string[],
  ids?: readonly IdArgument[]
): AsyncResource;
```

Resolve resource descriptions from the context and path. AsyncClient imports
this factory; resource modules use type-only imports for core types and invoke
the injected context, avoiding a reverse runtime dependency. Encode bound IDs
once, retain independent path/option snapshots, and associate completion data
privately with invocation wrappers. Do not eagerly allocate async-only runtime
primitives at package load.

The initial packages are released; callback parity is the gate before shared-core
extraction and async behavioral packages. The phase table below retains later
ownership. Independent final review follows committed intended changes and
quick checks, before long integration checks. This design handoff alone does not
trigger final review.

### React pilot without an npm release

Implementer1's later WebUI package adds a thin structural/injectable request-client
adapter plus one dedicated script, type consumer fixture and browser test using
existing tooling. Reuse existing auth/session/retry policy and HTTP fixtures;
do not create a parallel protocol decoder or a new harness framework. Normal
production application entry points retain their current default transport.
Do not add an unpublished npm version, absolute/local file dependency, root lock
update or Nix dependency hash. Ordinary `npm ci`, typecheck and build must still
work without the candidate HaveAPI package installed.

The HaveAPI owner builds the candidate then runs local `npm pack --ignore-scripts`
in `clients/js`, writing the tarball to an owned temporary artifact directory.
Packing does not publish and needs no version bump. The WebUI proof command is:

```sh
npm run test:haveapi-package -- --package /absolute/path/haveapi-client-0.29.0.tgz --webui-ref HEAD
```

Use the actual packed filename/version; the example does not select a release.
The dedicated script snapshots the specified committed WebUI ref into an owned
disposable directory, runs `npm ci` there, and installs the tarball there with
`npm install --ignore-scripts --no-save --package-lock=true <tarball>`. No
dependency mutation reaches the real worktree. A dedicated TS fixture imports
the package's emitted declarations and assigns AsyncClient to the adapter's
structural interface; a dedicated Vite/browser test loads its actual compiled
JS and injected adapter. Prove one read, mutation, qualifying 401 refresh/read
retry, no write replay, abort and response-first action-state receipt. Keep these
candidate-dependent fixtures outside the default application compilation/tests.

The first post-review proof demonstrated that the earlier `--package-lock=false`
command ignored the snapshot's resolver baseline and upgraded 96 installed
packages, including pinned Playwright. Its existing CLI guard correctly refused
before browsers launched. Therefore explicitly enable lockfile reading while
retaining `--no-save` and `--ignore-scripts`. Before candidate installation,
capture snapshot manifest/lock bytes and installed name/version at each existing
lock-listed package path after `npm ci`; verify those versions match the lock.
Before any candidate compilation or browser launch, require unchanged manifest
and lock bytes and unchanged presence/name/version of every baseline installed
locked package. New candidate/dependency paths are allowed; replacements are
not. Do not require platform-optional paths absent from the baseline. This is an
integrity assertion, not a dependency solver or per-tool pin workaround.

Implementer1 owns this narrow runner correction and drift/lock-change
regressions. First run the lead-authorized single fresh npm-only disposable
feasibility probe with a new watcher; no compiler/browser invocation or blind
retry of the drifted snapshot. Record the probe result before editing the runner.
The change restores isolation already required by the reviewed pilot and does
not expand its public/cross-project contract; focused inspection and quick checks
apply under review steps 9/10, with no automatic reviewer rerun. If preserving
the graph needs a new resolver or broader behavior, return to the lead. The
earlier candidate type/Vite run used drifted tools and is not final proof.

Record tarball SHA256, both source heads, Node/tool versions and results. Accept
`--haveapi-ref <full-SHA>` as pack-owner-supplied provenance, required when the
candidate package has no `gitHead`. Record whether the source reference came
from this argument or package metadata; fail clearly if both exist and disagree.
Neither source label independently proves the tarball's Git contents. The pack
owner confirms the candidate was built from the stated committed source; the
tarball hash identifies the exact artifact exercised by the proof. No adjacent
manifest or publication step is needed. Run the
long/uncertain proof via the verification watcher after committed-deliverable
review; existing quick structural/fake-client checks remain independent. This
proves real package fit, not production migration. Switching the default WebUI
transport and committing a registry dependency follows an approved published
release in a later rollout; no package publication is authorized here.

### Synthetic BFF state for the adapter fixture

The dedicated Vite fixture explicitly compiles with
`import.meta.env.VITE_RUNTIME_MODE` set to `bff`, matching the production policy
under test; verify the actual resolved fixture config rather than a copied
mock. Its four adapter scenarios start from a deliberately synthetic,
already-validated session identity, not a full application/OAuth bootstrap.
The existing window bootstrap supplies API/provider/meta configuration and a
synthetic token. The fixture uses a known 64-hex-character session key, matching
token and a fresh browser context with empty session storage.

Implementer1's fixture-only session helper calls the real
`bindBffImpersonationToSession(key, window.sessionStorage)` and then
`rememberBffSession(sameOriginSessionUrl, key, token)` on that same runtime object,
matching `src/app/runtimeBootstrap.ts:250-251`. `rememberBffSession` alone does
not establish the validated identity required by `src/app/config.ts:232-245`.
Before the first API call, assert the actual production runtime reports OAuth2
auth with the synthetic token and that both bound/remembered session identities
match the fixture key. Do not rebind during refresh or replace the runtime
object: the real refresh/session-identity checks remain under test.

No production guard, config, auth source or storage policy changes are needed.
Do not introduce a second validator/bootstrap framework or call
`loadRequiredBffRuntime` merely to run adapter tests. That would add config and
initial session HTTP requests unrelated to their contract. The fixture does not
certify config/session-response validation, OAuth login or application bootstrap;
existing production-bootstrap tests own those checks. Retain current assertions
for old/new token headers, one read refresh/retry, no write replay, changed-session
rejection, abort and response-first receipts. Commit the coherent fixture/config
and focused quick checks for direct acceptance before another browser proof.

### Real-browser UMD smoke within the packed pilot

Implementer1 owns one `scripts/haveapi-package/umd.spec.ts` in the WebUI
repository and the existing pilot's config/type/script-check updates.
Implementer0 supplies the exact minimal OPTIONS/description/action wire fixture
compatible with both clients, referencing the committed core/contract tests;
there is no additional application-source package. Replace the preliminary
Chromium-only raw-script check rather than retaining two overlapping checks.
The shared fixture is pinned to HaveAPI
`ae0fe39738c3eb10019377d0fce95dc249cdfd16`: explicit `{version: 1}` sends OPTIONS
to `/umd-api/v1/`; a `widgets.show` action at `/v1/widgets/{widget_id}` then sends
GET `/umd-api/v1/widgets/7`. Use the protocol-2.0 success envelope with description
at `response`, object payload at `response.widget` and
`response._meta.path_params: [7]`. Callback setup takes `(client, status)`;
action `onReply(client, value)` receives ResourceInstance. References are
`test/compatibility/callback.spec.cjs:64-112,128-134` and
`test/async/core.spec.cjs:27-45`, relative to `clients/js`. No authentication or
version-discovery scenario is needed for this smoke.

Run the same small scenario in named `umd-chromium`, `umd-firefox` and
`umd-webkit` projects using the WebUI's pinned Playwright 1.61.0. Keep the fuller
adapter `browser.spec.ts` on Chromium only. A fresh empty HTML page loads the
exact installed candidate `dist/haveapi-client.js` through an ordinary script
element. Serving the HTML, script bytes and synthetic API responses with
Playwright routes is sufficient; the page must not import the npm module or
pass its script through Vite transformation. Verify `window.HaveAPI.Client` and
`AsyncClient` with no default wrapper. Use real browser XHR for callback setup
and one described GET action, then async setup and the same awaited action.
Check callback arguments/undefined immediate action return, async value/meta,
request methods/paths, and absence of page errors/unexpected requests. These
are browser/transport fixture checks, not live-server certification.

The existing `npm run test:haveapi-package -- --package <absolute-tgz>
--webui-ref <committed-ref> --haveapi-ref <full-SHA>` runs the Chromium adapter
proof and all three UMD projects. Reuse its artifact/provenance record and
existing preview server; no new framework or production dependency. Apply any
Chromium executable override only to Chromium projects. Commit all fixture
code and pass quick type/config-discovery (`--list`)/runner unit checks before
final review; run browsers only afterward through the verification watcher.

Runtime availability is a separate preflight: on 2026-10-19 the default browser
cache contained Chromium/headless-shell build 1228 and ffmpeg, but no Firefox or
WebKit entries; no launch was attempted. This is cache evidence, not successful
runtime verification. Provision missing matching engines through the existing
pinned runner (`node scripts/playwright.mjs install chromium firefox webkit`)
in the documented environment before the post-review run. Record actual engine
versions/results. Missing engines or system libraries must produce an incomplete
matrix report, never an automatic skip or a three-browser success claim.

### Vite strict-context correction (awaiting lead implementation release)

The actual locked/minified proof using HaveAPI
`dc94157808966c12418b4009085fec237a869789` passed raw-script UMD in Chromium and
Firefox, but all four adapter cases failed before initialization. The emitted
`index-CrWIWntf.js:4:2456` retained `Authentication={...}` from
`src/haveapi/authentication.ts:42-44`; its ambient declaration emitted no runtime
binding. Vite had neither omitted nor mis-renamed it: a script of type module
applies strict semantics to the bundled CommonJS code despite the inner bundle
having no strict directive. Evidence is retained under
`/tmp/webui-haveapi-package-IsQ5c6/source/scripts/haveapi-package/dist/assets/`.
The later callback `v1`/`v2` and `ret` assignments have the same mechanism.

Correct the package source, not its consumer import: one small internal typed
host-global bridge explicitly reads/writes these four known properties. Preserve
the exported authentication registry object, registerProvider's live global
lookup, protocol scratch globals and defaultParams' returned/global object.
Resolve the actual host global with guarded globalThis/browser/worker/Node
fallbacks; do not require globalThis, dynamic evaluation, a new package entry or
an unminified consumer. Retain the original non-strict UMD loader shell and other
callback behavior. Do not turn the bridge into a general compatibility layer.

Implementer0 owns the package bridge and generated bundle, coordinating edits
to callback client/authentication/resource_instance files with implementer1.
Implementer1 owns any packed-consumer fixture adjustment; the named-import Vite
proof must remain minified. Quick verification includes raw UMD/AMD/CommonJS
and global-value parity, callback loading without async primitives, host fallback
without globalThis, and strict-context CommonJS-wrapped VM initialization plus
protocol/defaultParams paths. This changes the preservation mechanism assessed
by review; submit the cohesive committed fix and quick evidence for affected
general, architecture and risk/compatibility review before repeating the actual
packed browser proof. No existing green raw-script result certifies Vite fit.

## Review remediation decisions

At HaveAPI `ae0fe39738c3eb10019377d0fce95dc249cdfd16`, review found two
new-async correctness gaps during preliminary triage and a third in the final
report. The lead released bounded remediation after the complete four-lane
review: no Blocking findings; Important R1/R2/R3. Owners implement the following
seams, retain callback compatibility, and coordinate generated output/commits.

- **R1 / implementer1:** preserve AsyncResourceInstance references as leaves
  only when copying local resource attributes. Keep generic parameter/metadata
  snapshot and cycle semantics unchanged. Remove the premature `new()` and
  `submittedParams` deep copies: dynamic actions normalize Resource values
  synchronously before snapshotting the request. For a Resource-typed input,
  extract the declared `value_id` (default `id`) from an async entity or an own
  key of a plain association record; a custom key never falls back to `id`.
  Missing/invalid identifiers reject validation, not silent omission. This is
  parameter conversion, not binding inference; `path_params` remains authoritative.
  Local entity references must not survive into the dispatched scalar payload.
- **R2 / implementer0, feasibility confirmed:** keep callback coercion
  and the dictionary policy unchanged. In the async validation adapter, create
  one Parameters accumulator with empty input, coerce each own input entry in
  a separate `coerceParams` call, merge the results into its safe parameter map,
  then validate once with the complete map and accumulated type errors. Separate
  calls isolate function-scoped scratch values that legacy coercion accidentally
  reuses between fields. This reuses coercion and cross-field validators without
  duplicating their logic or introducing a compatibility mode.
  For null input descriptions and unknown schema keys, do not read ignored
  supplied values merely to create the single-entry map.
- **R3 / implementer0 receipt; implementer1 guard regressions:** construct the
  existing RequestResult diagnostic receipt immediately after top-level envelope
  validation, before metadata/payload/namespace interpretation. It retains raw
  `envelope.response` (possibly undefined), the envelope and HTTP status; `meta`
  begins empty and is populated only after validation. Attach that same receipt
  to invalid-metadata, missing-payload and missing-namespace protocol failures.
  Materialization failures already preserve it. No new public type is needed.
  An unsaved instance's existing accepted-unbound guard latches when HTTP is 2xx
  and the validated envelope says `status: true`, preventing another create on
  that instance while preserving local attributes/identity and original failure
  context. Invalid JSON/top-level envelopes have no validated success receipt;
  transport/timeout/abort, non-2xx and `status: false` remain distinct. Do not
  infer success from HTTP alone or introduce automatic retries.

Regression gates cover direct create, `new(attributes)`, set/save, loaded
association update, custom/missing/inherited identifier keys, and deferred
entity/scalar mutations after dispatch; preserve generic metadata behavior.
Exercise the actual emitted bundle, Parameters and fake XHR in addition to
resource-context unit tests. For R2 cover valid-then-invalid Integer, Float,
Boolean and Datetime fields, order/mixed/nullable cases, MFA and complete-map
cross-field validation, while callback compatibility checks retain old behavior.
For R3 use actual emitted request decoding plus save for HTTP 201 success with
missing selected namespace and missing response payload; also cover malformed
metadata. Assert retained response/envelope/status, unchanged local attributes
and binding, and exactly one POST after two save attempts. Negative controls
must not turn ambiguous transport or API failures into confirmed-create latches.

## Recommendation

Export **`HaveAPI.AsyncClient` alongside `HaveAPI.Client` from the same npm
`haveapi-client` package**. It is a standalone public client object, not a
separate npm package or a `.async` facade. Its network methods use ordinary
names and return Promises. Existing `Client` keeps its callback signatures,
return values and documented callback-free/fire-and-forget behavior.

Author both clients and their action/resource/authentication implementations in
TypeScript, compiling them to ordinary JavaScript with generated declarations.
The user's “sync client” means the existing callback-based Client: its HTTP
operations are already asynchronous. Rewriting its source language does not
convert its public API to Promises or introduce blocking network operations.

Share protocol, validation and transport machinery through composition and
small internal helpers; give the async client its own state and resource model.
Do not subclass callback resources and expose their network methods, toggle a
mutable async mode, or change existing Client instances. A separate package
would duplicate maintenance and complicate keeping protocol/security fixes
consistent. The tradeoff is maintaining two public object models in one package,
with contract tests proving their shared protocol behavior.

The separate React **vpsadmin-webui already uses its own async TypeScript/fetch
client** and has no direct or transitive npm HaveAPI dependency. This feature
does not automatically benefit that application. Making it usable there is now
an explicit design goal: add a typed low-level request API and prove a thin
WebUI adapter can replace transport/protocol duplication. Broad migration follows
that proof. Scope is HaveAPI and the **new React vpsadmin-webui only**; legacy PHP
WebUI and console integration are excluded by the user's latest direction.

## Evidence scope and exact revisions

Inspected existing canonical bare repositories using Git object reads; no other
session's checkout was used. These are cached remote-tracking heads, not claims
about the latest upstream or deployed revisions. HaveAPI local `master` differs
from the inspected remote-tracking ref.

| Repository | Inspected ref | Exact commit |
| --- | --- | --- |
| haveapi | `refs/remotes/origin/master` | `06865bb847a564fe20e59ea6d72856c2f01a82e3` |
| vpsadmin-webui | `refs/remotes/origin/main` | `7152729dcde326e00d16b5af0a46d0f60b431dbb` |

All paths and line numbers below refer to these commits. `implementer0`
independently inspected the HaveAPI callback contracts; `implementer1` traced
the WebUI dependencies. Their read-only findings inform this design.

## Proposed public contract

These methods and signatures are **proposals**, not currently available APIs:

```js
const HaveAPI = require('haveapi-client');
const api = new HaveAPI.AsyncClient('https://api.example.test');

await api.setup();
await api.authenticate('token', { token });

const { value: vps, response } = await api.vps.show(101);
console.log(vps.hostname, response.meta);

const { value: vpses } = await api.vps.list({
  params: { limit: 10 },
  meta: { count: true }
});

// The request was accepted; the server operation may still be running.
const started = await api.vps.restart(101);
const completed = await api.waitForCompletion(started, {
  timeoutMs: 120000,
  onStateChange: state => console.log(state.progress)
});
```

- `setup(): Promise<void>` validates descriptions and installs async resources.
  `authenticate(method, options): Promise<void>` supports authentication before
  setup and refreshes the authorized description before resolving. These reject
  all failures, including errors from later transport callbacks. They do not
  return the client. `availableVersions()` also returns a Promise. Constructor,
  `useDescription`, local language settings and resource selection remain
  synchronous; they perform no network I/O.
- Dynamic `api.vps.show(101, options?)` and explicit
  `api.resource('vps').action('show').invoke(101, options?)` use the same Promise
  contract. Support aliases, resource-curried IDs and an unambiguous options
  object containing `params`, `meta`, `signal` and request timeout. Resolve a
  fixed `{ value, response }` wrapper; never detect optional completion
  callbacks or introduce suffixed action aliases.
- `value` is an **async-owned** resource instance/list for object layouts, or
  plain data for other layouts. `response` is a data-only RequestResult carrying
  `data`, `meta`, `envelope` and `httpStatus`. No callback Client, provider,
  ResourceInstance, ResourceInstanceList or ActionState leaks into this API.
  Low-level `request<T>()` provides raw/unwrapped results without a second
  `directInvoke` flavor in the first release.
- AsyncResourceInstance field access and list indexing/iteration are local.
  Its bound actions return the same Promise result as root actions. `.save()`
  awaits create/update, validates the reply and updates identity, attributes and
  bound paths only after success; it returns `{ value: instance, response }`.
  A local `resource.new(attributes)` creates an unsaved async instance. Lists
  contain only async instances; any future pagination/network helper must also
  return a Promise. No automatic fetch occurs during iteration or field access.
- Server `path_params` is authoritative for returned identity; never infer a
  generic binding from `data.id`. An update may retain its existing binding when
  path metadata is omitted; explicit invalid metadata is a protocol error.
  Require new identity only where the described binding needs it, preserving
  valid singleton/idless resources. A definitely successful create missing
  required identity rejects with a protocol error retaining the successful
  response/envelope. Preserve local attributes/identity and set one small
  accepted-unbound guard so a second save cannot issue another create. Its
  message states that creation succeeded but identity is missing and the caller
  must fetch/rebind; it must not imply rollback or retry safety. Ordinary
  unbound results remain readable, while network helpers needing missing IDs
  reject until bound. This is new async behavior only, not a generalized
  recovery state machine or a callback Client change.
- Associations use explicit `await instance.loadAssociation(name, options)`
  returning `{ value, response }`; prefetched data can satisfy it without I/O.
  Here `response` is the actual load reply, or null for a prefetched cache hit;
  do not fabricate an HTTP reply for local data.
  Association property access never starts a hidden request. Failed loads reject
  without a half-resolved shell. This replaces callback `whenResolved` and avoids
  superficial wrappers around the existing save/lazy-load correctness gaps.
  Save and explicit association loading are included in first-release coverage;
  callback lazy-property semantics are not carried into AsyncClient.
- Authentication includes Basic, token and existing-token OAuth2 with independent
  async provider state. Token MFA uses an async-capable `onChallenge` function
  returning input/Promise<input>; no continuation callback is needed. Provider
  setup does not newly prove credential validity. OAuth authorization-code,
  session-refresh policy, automatic renewal and a convenience `logout()` are
  deferred; existing explicit revoke actions remain callable with Promises.
  Do not expose callback-only provider methods to fill these gaps.

### Isolation, collisions and Promise safety

AsyncClient owns credentials, language, descriptions, resource bindings and
in-flight lifecycle state. Independent async/callback clients cannot change each
other's state. Concurrent requests snapshot IDs/options/auth context at dispatch;
there is no shared mutable prepared path. Serialize setup/authentication changes
within each async instance, and publish new descriptions atomically after
validation. A late result cannot replace a newer authentication generation;
cross-generation requests retain their dispatch identity and never replay.

Lead-approved binding rule: after a successful description/authentication
generation replacement, an older bound resource/instance rejects new network
operations with a clear stale-binding error before dispatch. Already-dispatched
requests may settle using their original context but cannot republish the old
root registry. Implement this as a generation snapshot and guard; no retry
framework is needed. Low-level `request<T>()` uses current explicit dispatch
context and is not tied to a description binding. Merely changing per-request
headers/language does not replace a description generation. Callback Client
behavior is unaffected.

Fixed result wrappers retain metadata without flattening resources. Additionally
**all async-owned client/resource/list objects must be non-thenable**: reserve a
noncallable `then` on these new surfaces, and keep described `then` actions,
resources and attributes reachable through explicit `action(name)`,
`resource(name)` and `get(name)` lookup. Apply the same explicit lookup rule to
helper-name collisions and reject unsafe prototype attachments. Do not change
legacy Client's attachment rules. API-supplied properties stay nested in
response records; setup/auth resolve void. Thus neither Promise settlement nor
an accidental `await` on a local async resource can invoke a remote `then` action.

Shared internals must retain URL-origin, encoded-path, validation and language
rules. Prefer extracting pure serialization/decoding helpers and a per-instance
transport adapter; do not route AsyncClient through callback methods that lose
HTTP status/errors or throw later without a rejection channel. Preserve old
Client behavior while reusing the lower-level implementation where safe.

### Typed path-based API for the React WebUI

Add `asyncClient.request<T>(request): Promise<RequestResult<T>>` alongside the
dynamic action API in the **same package**. This is necessary because the React
WebUI already knows endpoint paths/types and should not need to download a
resource description or construct ResourceInstance objects for every adapter.
A dynamic-invocation-only wrapper would leave transport/protocol duplication or
force an unnecessarily broad application rewrite.

Proposed TypeScript-facing example:

```ts
const result = await api.request<Vps>({
  method: 'GET',
  path: '/v1/vpses/101', // Illustrative: retain the actual WebUI endpoint path.
  outputNamespace: 'vps',
  signal,
  headers: currentAuthenticationHeaders()
});
// Stable typed fields: result.data, result.meta, result.envelope, result.httpStatus.
```

`RequestSpec` explicitly carries method, API-relative path, input/output
namespace, metadata namespace, params, meta, headers and optional AbortSignal.
The client validates the URL against its configured origin, serializes query or
JSON payloads using shared HaveAPI rules, sends language/authentication headers,
parses and validates the envelope, and unwraps the selected output namespace.
The adapter supplies endpoint-specific namespace/metadata settings already
known to the WebUI; this route does not require `setup()` or an OPTIONS fetch.
Dynamic actions derive the same request information from descriptions
and share the request/decoding pipeline. Do not build a second transport.

`RequestResult<T>` has fixed own fields `data`, `meta`, `envelope` and
`httpStatus`; API-supplied properties remain nested. It exposes the raw envelope
without forcing consumers to use rich resource wrappers. The error contract
includes HTTP status independently from HaveAPI envelope status, plus structured
errors and the parsed envelope when available. Type parameters describe the
caller's expected payload; they do not replace runtime envelope validation.

Generate `.d.ts` declarations from TypeScript for **both** public surfaces,
including callback overloads, RequestSpec, RequestResult, AsyncError, dynamic
invocation results and completion options. Publish them via the package `types`
field and included package files; do not maintain duplicate handwritten full-API
declarations. Endpoint/resource schemas remain separate from declaration emit
and their generation is deferred. Check actual TypeScript/Vite consumption of the retained
UMD/CommonJS package; add an additive bundler entry only if that proof requires
it. Do not assume the existing global bundle is automatically a working Vite
dependency or introduce ESM-only packaging.

The WebUI keeps a small adapter around this API:

- Supply the current token/provider headers at each request and set the current
  language; no stale credential snapshot or persistent token storage is added.
  Document header precedence and validation. Pass the caller's AbortSignal into
  the actual transport, including already-aborted signals; remove listeners
  after completion and preserve recognizable abort errors.
- On a qualifying HTTP 401, call the existing BFF/session refresh code with its
  session-identity guard. Retry GET/OPTIONS at most once under the existing
  policy. Never automatically replay mutations. Keep refresh orchestration and
  application-specific session-expired/resubmit errors in the WebUI adapter.
- Map the library's typed error/result to the existing WebUI-facing contract
  while retaining HTTP status, errors, metadata and raw envelope. Remove old
  fetch, query/body encoding and envelope parsing for migrated calls; this
  adapter owns application policy, not another HaveAPI implementation.
- Preserve response-first mutation acceptance and action-state receipts. React
  Query and the existing UI task tracker can continue polling separately; the
  application is not required to use the library's blocking completion helper.

A bounded proof-of-fit must cover one read, one mutation, HTTP/authentication
failure with refresh, cancellation and a blocking-action receipt before broad
consumer migration. Execution is authorized within the lead's assigned packages;
the addendum fixes how to prove fit without an unpublished dependency.

### Errors and server completion

New Promise methods reject an `Error` subtype, proposed `HaveAPI.AsyncError`,
with a stable `kind` (validation, transport, protocol, authentication, API,
action-failed, timeout or aborted), `message`, and available `httpStatus`,
`response`, `envelope`, `errors`, `state` and `cause`. Unavailable fields remain absent.
Preserve the underlying response/envelope rather than throwing only a string or
boolean. Do not claim to recover server detail already lost by a boolean-only
provider callback; extend the internal completion/error channel where needed.
Do not attach credentials or authorization headers to errors.

Normalize non-success HTTP replies, HaveAPI `status: false`, invalid/missing
envelopes, invalid JSON, network errors, local validation, incompatible
descriptions and callback-time exceptions. Each operation settles exactly once.
Timeout/abort handling must use an explicit transport error path; wrapping the
current outer method in `new Promise` cannot catch a later callback's throw.
Keep legacy callback behavior and synchronous throws covered separately.

Dynamic action calls and `request()` resolve on the successful API reply, including for a
server-declared blocking action. JavaScript asynchronous I/O and a server job's
completion are separate concepts; there is no server protocol change.

`waitForCompletion(result, options)` is the separate completion API:

- Use the existing protocol condition: a blocking action description plus
  `action_state_id` metadata. For an ordinary/nonblocking reply, resolve
  `{ value, response, state: null }` immediately; otherwise use action-state
  show/poll and resolve that wrapper with a successful terminal state.
- Reject failed terminal execution even when the polling HTTP/envelope status
  succeeded. Reject polling failure, malformed/missing state and local stopping
  rather than leaving a Promise pending. Preserve the original action response
  and final/last state in completion results or errors.
- Accept a positive overall `timeoutMs` and optional abort signal; require the
  timeout in the first version so the completion wait is bounded. This differs
  from the existing per-poll server timeout. Stopping/aborting local observation
  does not cancel server execution. Remove local timers/listeners on settlement.
- Server cancellation is an explicit API call to `action_state.cancel`, only
  when supported; its response may itself describe another blocking operation.
  Expose progress/terminal states as data-only snapshots; do not return legacy
  ActionState helpers. Cancel through an async action/request and stop tracking
  through AbortSignal. Keep legacy `ActionState.stop/cancel` behavior intact.
  Do not implement
  new completion by merely wrapping the existing `onDone` callback: that callback
  does not establish terminal success and may never run after local stop.

## Implementation boundaries and phased plan

The lead has assigned the initial packages described above. Later packages use
the following independent file boundaries and are released by the lead as their
dependencies become ready.

| Phase / suggested owner | Files and responsibilities | Dependency and acceptance |
| --- | --- | --- |
| 1 / architect + lead; build owner implementer0; fixtures implementer1 | Freeze both public contracts and shared internal types; `clients/js/tsconfig*.json`, package/build scaffolding and baseline callback/consumer fixtures | Establish callback behavior and supported runtimes before source conversion; build fixtures must exercise published JS exports |
| 2A / implementer0 | Convert `src/haveapi/{client,http,hooks,authentication,exceptions,i18n}.js` and `authentication/*.js` to `.ts`; own `src/haveapi.ts` export/build integration | Preserve callback timing, provider setup/MFA/logout behavior, hook order and error delivery; own shared type definitions, serialize build/export edits |
| 2B / implementer1, parallel after type scaffold | Convert `src/haveapi/{action,action_state,base_resource,resource,resource_instance,resource_instance_list,response,local_response,parameters,validator}.js` and `validators/*.js` to `.ts`; callback overload/type fixtures | Preserve callable objects, IDs/aliases/prototypes/attributes, save/lazy behavior, validation, undefined returns and synchronous throws; no callback bug fixes mixed into conversion |
| 3 / implementer0, coordinated with implementer1 | Extract typed internal protocol/request outcome helpers from the converted modules | Only after callback parity; share validation/serialization/transport while callback facade retains its original observable mapping/timing; independent per-client state |
| 4A / implementer0 | New `src/haveapi/async/{client,request,authentication,error,completion}.ts` and core/completion tests | Use phase-3 core; Promise setup/auth/request, AbortSignal, isolated state, reply-first receipts and bounded completion wait |
| 4B / implementer1, parallel on frozen core interface | New `src/haveapi/async/{resource,resource_instance,resource_list}.ts`, unit tests, `test/helpers/adapter_async.js` and type-consumer fixtures | Async dynamic actions/save/loadAssociation; non-thenable objects and explicit collision lookup; generated declarations, no callback helper leakage |
| 5 / implementer1; serialized build owner implementer0 | README/API examples, scoped `AGENTS.md` source/build guidance; finalize package `main`/`types`/files and generated JS/declarations | Both surfaces type-check and emit; one owner regenerates bundle; verify script tags, CommonJS and TypeScript/Vite imports |
| 6 / implementer1, WebUI pilot package | Structural/injectable API adapter and focused tests; one package-proof script/type fixture/browser test and npm script entry | Use disposable packed-artifact proof; default transport/dependencies/root lock/Nix hashes unchanged; preserve local interface; no broad page rewrites |
| Release / lead + retained reviewer + watcher | Quick checks, committed-deliverable review, then shared Ruby-server contracts, browser/WebUI integration and CI; release proposal | Future workflow only; publishing requires approval; broad WebUI adoption follows successful fit evidence |

Serialize edits to shared fixtures, export/build lists and Git operations.
Keep migration, shared-core extraction and new async behavior as separate
reviewable changes. Temporary mixed JS/TS build support may bridge conversion
packages; the final authored client implementation is TypeScript. Generated
locale/catalog inputs remain generated under their own procedure, and tests or
build scripts need not be converted merely because production source is.
Keep repairs to the **old callback** save/lazy-association implementation,
a fetch rewrite, ESM-only packaging and generated endpoint schemas outside the
initial change. The new async-owned save and explicit association loader are
included and tested independently. Automatic token renewal, OAuth flow/session
management and convenience logout are explicit first-release deferrals; no
callback-only substitutes are exposed. Broad WebUI migration follows the bounded
adapter trial; WebUI usability is initial acceptance. Route material contract
changes through the lead.

## Runtime, packaging, compatibility and recovery

### Selected TypeScript authoring and migration contract

Both Client and AsyncClient, including their resource/action/authentication
implementations, are authored in TypeScript. This is the selected design scope;
execution follows the lead's assigned packages and the addendum above.

Compile `.ts` with `target: ES5`, `module: ESNext` and declaration emit, then use
Rollup named-export UMD through the retained gulp entry as fixed in the addendum.
Keep `dist/haveapi-client.js`, CommonJS/AMD/browser contracts and the Client
export; add AsyncClient alongside it. No separate ESM runtime artifact initially.
Package compiled JS and declarations together, with `main`/`types` pointing to
those artifacts. `.ts` source is never the runtime entry. Plain JS consumers
need neither a TypeScript compiler nor a source rewrite: `require('haveapi-client')`
and a browser script exposing `HaveAPI` continue to work.

TypeScript types are erased and cannot validate network data. Keep runtime
description/envelope/input validation. Source typing also cannot infer endpoint
names loaded at runtime through OPTIONS: precise resource/action typing requires
application-authored or generated schemas, or the explicitly typed `request<T>()`
surface. Both exported client APIs receive generated declarations; JavaScript
build/test artifacts do not justify a second handwritten public-API definition.

For callback conversion, preserve argument/callback shapes, return values,
synchronous local throws, hook order and fire-and-forget behavior. Never add
`async` to callback methods as a convenience: that changes throws and returns.
Keep existing exception constructors and provider failure semantics observable
through Client; new Promise error normalization belongs to AsyncClient. Known
callback save/lazy-load defects are separate fixes, not incidental conversion.

Represent callback signatures and variadic action calls with overloads and
callable interfaces in source, including optional parameters and resource-curried
IDs. Preserve function-object prototypes, exported constructor/static access,
`this` binding and attribute descriptors; a mechanical rewrite into ES classes
can change these. Keep dynamic description/payload values at explicit typed
boundaries, narrow after validation, and use localized documented casts where
the runtime callable model requires them. Do not claim that a permissive index
signature or type assertion validates arbitrary API endpoint names or data.

Generate declarations for the complete callback and async surfaces from source;
author supporting interfaces/overloads in `.ts`, not a parallel full `.d.ts` API.
Check positive and negative type-consumer fixtures for callback forms, Promise
results and unknown dynamic endpoints. Source conversion must preserve JS
runtime exports: avoid accidentally requiring `.default` after CommonJS import.

Update HaveAPI's client-specific ES5 source/build guideline deliberately to allow
TypeScript authoring and generated JS/declarations for the JavaScript client.
This scoped guideline update supersedes the earlier async-only exception; it
does not change other languages/components. Choose emitted syntax for current
supported browsers and the preserved supported Node baseline. No generated
output is edited by hand; the serialized build owner maintains compilation,
bundling and package metadata.
Verify script-tag, CommonJS and TypeScript/Vite consumers of the **published
artifacts**, not imports of uncompiled source. No build was run in this pass.

### Existing constraints and rollout

The inspected npm package is version `0.29.0`, ships only `dist`, uses a CommonJS
`main`, and produces a browser/global/AMD/CommonJS UMD bundle through gulp.
The inspected repository instructions require ES5-style source; the selected
TypeScript migration includes the scoped guideline update above. The package
declares no `engines`; CI selects `lts/*`, so there is no evidenced minimum Node version.
Keep current entry points and XHR transport for this change. Do not add ESM-only
exports, `fetch`, `Proxy` or a syntax/runtime bump as an incidental dependency.

Target current, vendor-supported browsers, as requested; do not add obsolete
browser support or Promise/AbortController polyfills. Preserve public JS entry
points while moving authoring to TypeScript and using native Promise and
AbortSignal for the new surface.
`async`/`await` syntax can appear in consuming applications and examples. Test
current supported Chromium, Firefox and WebKit-family browsers and document the
tested versions at implementation time. Preserve Node operation and CommonJS;
its exact supported minimum remains a release prerequisite rather than an
invented new requirement. Runtime modernization beyond this is separate scope.

No persisted-state, database, protocol, Ruby/PHP/Go client, CLI, Terraform,
daemon, NixOS/vpsAdminOS configuration or migration change is needed. Old/new
clients may coexist with existing servers. No coordinated node update or server
deployment ordering is required. Rollback is a dependency/bundle revert, with
the consuming application's Promise calls reverted together; no data rollback
is involved. AsyncClient's explicit resource/action/attribute lookups retain
access to names reserved by its new object model. Test these collisions without
changing legacy name attachment globally. Do not mutate a callback instance to
make it async or reuse its mutable authentication/resource state.

The existing version/release process remains authoritative; do not invent a new
release number or publish without approval. The bounded React WebUI adapter
trial depends on the new typed client, then consumer rollout may proceed
incrementally after an approved package release. The initial pilot keeps the
default transport/dependencies unchanged. For the later default switch, revert
its dependency and adapter together for rollback; no
server deployment is required. Legacy WebUI and console integration are outside
the requested scope.

## Acceptance and verification brief

The investigation established source/dependency evidence; implementation checks
below are release gates, with actual results recorded by the implementers/lead.
Use HaveAPI's declared Nix shells and repository procedures.

Quick checks after implementation:

1. Type-check both client implementations, then run configured TypeScript JS and
   declaration emit followed by bundle generation in the declared environment.
   Run this through the retained gulp entry point using the accepted Rollup build.
   Check generated output and packed files: callback and async exports must work
   through the same script-tag/CommonJS contract without `.default`, runtime TS
   loaders or missing declarations. Compare callback runtime behavior before and
   after conversion at each migration stage.
2. Run focused Mocha unit/regression files, including async error delivery with
   deferred fake XHR callbacks. Cover malformed/empty JSON, network/open/send
   failures, validation without HTTP, HTTP errors and envelope `status: false`.
3. Preserve callback argument shapes, return values, local synchronous throws,
   fire-and-forget calls, hooks, aliases, curried/nested IDs and path cleanup.
   Test Client and AsyncClient side by side without state leakage or changes to
   callback return/throw behavior. AsyncClient rejects callback invocation forms
   rather than silently exposing a mixed API.
4. Verify async-owned result/resource/list classes, metadata/count/includes,
   all output layouts and low-level results; reject during materialization.
   Concurrent calls use independent IDs/options, and setup/auth publish state
   atomically. Test described `then` resources/actions/aliases and attributes
   through explicit lookup; resolving or awaiting async-owned objects must not
   execute them. Test create/update save identity/path refresh and failure
   atomicity, omitted versus invalid update identity, singleton/idless create,
   and successful create with missing required identity (successful response
   retained, local state unchanged, second create prevented). Cover readable
   unbound results and rejected ID-dependent sends; old-generation bound sends
   reject before transport, while dispatched calls retain their snapshot.
   Test cached and uncached association loads, loading errors, and no I/O
   during property access/list iteration. No returned object exposes a
   callback-only network helper or callback-owned provider/state object.
5. Cover setup failure, unsupported provider, description refresh failure,
   Basic/token/OAuth2 setup and async MFA challenge/rejection/missing handler. Preserve
   callback-only use without introducing Promise-returning legacy methods.
6. Test reply-first blocking/nonblocking calls and completion success, failed
   terminal status, polling errors, timeout, abort/local stop and cancellation
   as a separate potentially blocking request. Check single settlement and no
   polling/listeners after settlement.
7. Compile positive/negative TypeScript consumer fixtures against generated
   declarations from the packaged artifacts for both Client and AsyncClient,
   including callback overloads, callable resources/actions and Promise results.
   Compile the actual WebUI adapter with its normal TypeScript/Vite tooling.
   Exercise path-based GET/query and mutation JSON,
   strict envelopes and missing namespaces, HTTP versus API errors, current
   token/language headers and pre-start/in-flight AbortSignal cancellation.
   Prove one 401 refresh retry for reads, no mutation replay, stable-session
   protection and response-first action-state receipt handling. Check that
   migrated calls no longer retain a second fetch/serialization/decoder path.

After committed-deliverable independent review, run the existing shared contract
suite against both CallbackAdapter and the new AsyncAdapter using the Ruby test
API, plus the full JS suite and real-browser UMD smoke coverage. Existing
`npm test` includes server-starting contract tests; it is not assumed quick.
Use a fresh verification watcher for these uncertain/long checks. Ruby test-server
dependencies require the top-level/Ruby environment in addition to the Node-only
`client-js` shell. Retain the existing path/query, OAuth2 origin and localized
typed-validation tests. This design addendum alone does not trigger review;
completed substantive implementation follows the mandatory review workflow.

## Key source references

HaveAPI, at `06865bb847a564fe20e59ea6d72856c2f01a82e3`:

- `clients/js/package.json:1-38`, `gulpfile.js:6-43`,
  `src/haveapi.js:6-38`, `.github/workflows/clients-js-tests.yml:36-51`:
  package version/entry points, UMD build, browser/Node XHR and current CI.
- `clients/js/src/haveapi/action.js:18-30,128-130,173-213,221-343`:
  callable action methods, documented callback-free operation, invocation,
  argument parsing and existing undefined returns.
- `clients/js/src/haveapi/client.js:316-335,417-468,517-570,580-715`:
  setup/authentication, error loss/callback-time exception paths, logout and
  raw/rich response mapping.
- `clients/js/src/haveapi/http.js:18-66` and
  `src/haveapi/authentication/token.js:105-145`:
  transport missing structured error delivery and MFA callback semantics.
- `clients/js/src/haveapi/client.js:77-95,476-503`,
  `src/haveapi/base_resource.js:9-13,44-64`,
  `src/haveapi/resource_instance.js:271-305`: arbitrary attached names and
  the thenable-assimilation risk.
- `clients/js/src/haveapi/resource_instance.js:28-50,103-141,173-217`:
  rich response access, save and lazy-association caveats.
- `doc/protocol.md:479-491`, `clients/js/src/haveapi/action.js:381-435`,
  `src/haveapi/action_state.js:19-28,55-90`: server blocking identification,
  polling, final-status distinction and local stop/cancel.
- `clients/js/test/helpers/adapter_callback.js:9-18,63-84,91-125` and
  `test/contract/client_contract.spec.js:25-115`: existing test-only Promise
  wrapping and shared contract coverage, not production Promise support.

React vpsadmin-webui, at `7152729dcde326e00d16b5af0a46d0f60b431dbb`:

- `AGENTS.md:3-6` identifies React/BFF ownership separately from legacy PHP.
- All four root/BFF package manifest/lock files contain no `haveapi` match;
  the inspected locks contain 483 and 90 package entries respectively. This
  supports absence of both direct and transitive npm HaveAPI dependencies.
- `src/lib/api/haveapi.ts:405-514` exports `async haveApiCall<T>` returning
  `{data,meta,envelope}`, uses native `fetch` at line 471 and throws HaveApiError.
  `src/lib/api/vps.ts:229-235,263-268` uses that local adapter.
- `src/lib/api/haveapi.ts:434-490`,
  `src/lib/auth/bffSession.ts:36-70`: language headers, AbortSignal, session-aware
  OAuth refresh, retry of reads only and deliberate non-replay of writes.
- `src/lib/api/actionStates.ts:33-56` separates polling from request completion;
  `docs/design/ARCHITECTURE.md:35-50` and `bff/README.md:13` confirm SPA direct
  HaveAPI access and an OAuth/session BFF, not a resource-client proxy.

Consequently the planned upstream-client adoption needs behavioral parity for
typed results/errors, namespaces/metadata, headers, abort, refresh/session
identity, write replay prevention and action-state tracking. The user's reuse
goal is addressed by the typed request core and bounded adapter trial above;
preserve this application-specific policy while replacing protocol duplication.

Current supported browsers are the explicit baseline; obsolete browsers are
out of scope. The exact supported Node minimum and tested browser versions must
be recorded during implementation. No other unresolved design question blocks
this proposal.
