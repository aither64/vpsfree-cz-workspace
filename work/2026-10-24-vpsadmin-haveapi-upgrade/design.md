# HaveAPI 0.30.1 adoption design

Design owner: architect0. Status: all four packages ready for lead assignment;
SDK compatibility is an explicit package B acceptance gate. Initial tracking
commit: `b6001eb8`. No project source changes or external writes were made by the
architect. The lead owns assignment, shared Git serialization, final prose,
review and publication.

Current target: released **HaveAPI 0.30.2**, per the
[2026-10-26 addendum](#2026-10-26-addendum-released-haveapi-0302).
The [2026-10-25 registry addendum](#2026-10-25-addendum-rust-registry-adoption)
supersedes the original Rust Git-source recommendations in packages B/D.
Decision B1 remains historical design evidence; its performance remedy is now
owned by the user in another session and R1 remains an external readiness gate.

## Scope and boundaries

Adopt released HaveAPI 0.30.1 throughout `vpsadmin`, take over only the final
production async-client change from the authorized old WebUI session into a new
session-owned branch, expose Go/Rust API documentation examples, and prepare
bilingual `manuals:vps:api` client documentation. No deployment, default-branch
integration, old-session mutations or production KB publication is authorized
by this design.

Use a new `vpsadmin` worktree/dated branch from fresh remote master. The React
WebUI is a separate `vpsfreecz/vpsadmin-webui` repository and needs its own
registration, worktree and `dev/<short-name>` branch; it is not the legacy PHP
`vpsadmin/webui` directory. The lead sets up these worktrees.

## Package A: vpsAdmin released dependencies

Suggested owner: implementer0. This package is independent of WebUI and KB work.
Read repository `AGENTS.md`, `docs/README.md`, development/testing procedures,
and `skills/vpsadmin-update-haveapi/SKILL.md` before edits. The skill's script is
stale: it invokes `tools/bundix_all.sh`, absent from inspected master, and its
root discovery also requires that absent file even with `--skip-bundix`.
The lead accepted direct updates of the four declarations plus current
`tasks/gem_updates.rb` rake tasks under the testing procedure. Use current
scoped tasks, not an invented compatibility script.
Report this documented deviation in the implementation receipt.

Own these files:

- Ruby source requirements: `api/Gemfile`, `client/vpsadmin-client.gemspec`,
  `download_mounter/Gemfile`, `plugins/outage_reports/utils/Gemfile`.
- Generated `packages/{api,client,download-mounter}/{Gemfile,Gemfile.lock,gemset.nix}`
  where present and affected. Preserve legitimate source-gem metadata handling.
- PHP dependency: `webui/composer.json`, `webui/composer.lock`, and any package
  integrity metadata actually derived from that lock.
- Both checked-in JavaScript distributions:
  `webui/public/js/haveapi-client.js` and
  `console_router/public/haveapi-client.js`.

Change source Ruby requirements to the repository's `~> 0.30.1` convention,
and prove every generated HaveAPI runtime resolution is exactly `0.30.1`.
Package A also owns adding `haveapi-go-client` and `haveapi-rust-client` runtime
requirements to `api/Gemfile` at `~> 0.30.1` for package B; their exact resolved
version must also be 0.30.1. Both generator gems are published. They are optional
HaveAPI components and are not brought in by the server gem alone.
Use scoped rake metadata tasks for API/client/download-mounter and inspect all
other components for missed consumers. The task deletes/re-resolves its lock;
enumerate resulting transitive changes and avoid unrelated package refreshes.
Do not create build IDs or publish first-party gems.

Update PHP to exact `haveapi/client` `0.30.1` and regenerate Composer lock using
the component Nix environment. Packagist confirms this release exists; its source
commit is `195f1a4db7699dc4187463dab0f0e029df375e6c` in
`vpsfreecz/haveapi-client-php` (PHP >=8.0). No PHP source fork is needed.

Replace both browser distributions with the same published npm 0.30.1
`dist/haveapi-client.js`, verifying the registry integrity before extraction.
Do not hand-edit generated JavaScript or switch the legacy consumers to the
async API. Preserve `HaveAPI.Client` callback compatibility; inspect console and
PHP usages and run focused regressions. Inventory all tracked HaveAPI references
to establish that no old runtime bundle or dependency remains.

Registry observations on 2026-10-24:

| Artifact | Published identity/provenance |
| --- | --- |
| Ruby server | `haveapi` 0.30.1; SHA256 `309b94465461b0ac1bd2019e63f601e287a027dfcb668ceb54b9f6799ab5b00f` |
| Ruby client | `haveapi-client` 0.30.1; SHA256 `4759bb0003649a8ebcf5f88c05a33b3491db296a984a9b8d3408a205bc8e5cf1` |
| PHP | `haveapi/client` 0.30.1; source above |
| JS/TS | npm `haveapi-client` 0.30.1; repository directory `clients/js`; registry integrity `sha512-n4RMhSbaJZLRm9390wz+M1759h06sEOfh3XVG3t/wGrE0mr97uf+ozERXdJfGXGqxdxelkk765vidheYwUJBWw==` |
| Python | PyPI `haveapi-client` 0.30.1, Python >=3.11; wheel SHA256 `3d44949f4d545c07ea54fbb35229e74a084d5324da89866e6d4d7a91b95eb0c0` |

The npm metadata has no gitHead; use published attestation/tag and file matching
for source proof, never infer source solely from the package version. npm locks
must retain exact transitive `xmlhttprequest` resolution despite upstream's
`latest` requirement.

Acceptance and quick checks:

- All intended Ruby, Composer and browser artifacts resolve to 0.30.1 and have
  recorded provenance; no unrelated source/framework upgrade.
- Lock/gemset consistency, syntax/format and `git diff --check`; scoped lint;
  minimal Ruby require/version and PHP client load checks in their Nix shells.
- Published browser UMD export still provides callback `HaveAPI.Client`; both
  vendored outputs are byte-identical to the verified released distribution.
- Source, generated metadata and exact files appear in the review inventory.

Longer checks after committed-deliverable independent review: required
`./test-runner.sh test services-up` (packaged shared documentation), console
router smoke and relevant PHP WebUI authentication/console browser coverage;
API full/core specs and affected package builds/CI as selected by repository
rules. A fresh policy watcher owns long/uncertain commands. Stop unexpected
local kernel builds. These are planned checks, not executed evidence.

### Package A native dependency addendum: Fiddle/libffi

The first API dependency setup failed because `haveapi-rust-client` 0.30.1 now
requires the native `fiddle` 1.1.8 gem. Its extension found neither pkg-config
metadata for libffi nor `ffi.h`/`ffi/ffi.h` in the API shell; its gem ships no
fallback libffi source. This is a development dependency declaration gap, not a
reason to bypass the gem or change the generator version.

Minimal permanent correction owned by implementer0:

- Add `libffi` and `pkg-config` to the `api = mkRubyBundlerShell` package list
  in `flake.nix`. A short comment may connect them to the Rust documentation
  generator's Fiddle dependency. Preserve shared shell behavior, Ruby version,
  existing compiler purity setting and unrelated shell packages.
- No change to `packages/api/common.nix`, API package wrapper files, overlays,
  gemConfig or flake.lock is currently needed. Pinned Nixpkgs already supplies
  `defaultGemConfig.fiddle.buildInputs = [ libffi ]`. Evaluating the actual
  vpsadmin API environment confirmed `ruby3.4-fiddle-1.1.8` with build inputs
  `ruby-3.4.9` and `libffi-3.8.0`. Fiddle's extension supports direct header/library
  detection when pkg-config is absent, so the packaged gem is already provisioned.
- Also declare `libffi-dev` and `pkg-config` in the existing pre-Bundler apt
  dependency lists of both full/core jobs in `.github/workflows/api-specs.yml`
  and the conditional dependency step in `.github/workflows/api-migration-specs.yml`.
  These jobs install the same API bundle outside Nix. Explicit requirements
  avoid depending on incidental runner-image contents. Preserve conditions,
  topic manifests and aggregate behavior; do not update unrelated action refs
  as part of this dependency correction. Check imported action versions as
  required by the workspace verification procedure before workflow edits.

The root shell already has libffi and its own Gemfile does not use the Rust
generator. Client and console-router Ruby bundles do not gain Fiddle. Do not
broaden the change to every shell or add temporary `LD_LIBRARY_PATH`, vendored
libffi, a host package install or a compiler-flag workaround.

Evidence read on 2026-10-24: locked Nixpkgs source
`/nix/store/5b2ic4sxjc2lzgxk4hninyw22r5gv5qr-source`, gem configuration
`pkgs/development/ruby-modules/gem-config/default.nix`, and the actual failed
API `api/.gems/ruby/3.4.0/extensions/x86_64-linux/3.4.0/fiddle-1.1.8/mkmf.log`.
The architect evaluated package inputs only; no build was launched.

Checks: format the changed Nix file, validate workflow YAML and shell fragments,
then enter the normal corrected `.#api` shell through a fresh watcher. Require
successful bundle setup, `pkg-config --modversion libffi`, `require 'fiddle'`
and a real `require 'haveapi/rust_client/documentation'` reporting generator
0.30.1. Retain the failed setup result and the successful correction evidence.
After committed review, verify the actual packaged API Ruby environment can load
Fiddle and both generators, and run services-up as already planned. Only if the
package build demonstrates a missing input should a package override be added,
after referring the evidence through the lead. The system libffi dependency
enters the immutable Nix closure; no deployed host prerequisite, persistent
format change or coordinated node update is introduced.

## Package B: Go and Rust documentation profiles

Suggested owner: implementer2. Ready to start; final execution needs package A's
new API bundle. Share the vpsAdmin worktree only with disjoint edits and lead
serialization of Git operations. Package A alone edits Gemfiles/locks/gemsets.
Own `api/lib/vpsadmin/api.rb`, a small profile helper if useful, focused API
documentation specs, developer documentation linked from `docs/README.md`, and
`tests/suite/services-up.nix` documentation assertions. Prefer a focused spec
under `api/spec/lib/` so the existing platform-config CI topic selects it; if
using a different new location, update the precise topic selector as required.

Read HaveAPI release `v0.30.1` guides `doc/client-examples.md`,
`clients/go/docs/documentation.md`, `clients/rust/docs/documentation.md` and
implementation `servers/ruby/lib/haveapi/documentation_clients.rb`. The release
already implements Go and async/blocking Rust renderers. Configure the existing
profile API before mounting, next to `use_version`/`action_state` setup:

```ruby
api.documentation_clients('7.0',
  go: {
    import_path: 'github.com/vpsfreecz/vpsadmin-go-client/client'
  },
  rust: {
    crate_name: 'vpsadmin-client',
    source: {
      git: 'https://github.com/vpsfreecz/vpsadmin-rust-client',
      rev: 'ff876abe17e3301da62c1b6afbda055ec89db9d2'
    }
  }
)
```

Omit optional SDK version fields unless compatibility evidence establishes a
reason to pin them. Go emits its normal `@latest` selection; current public
master and proxy identify `1d9240f3d27b5831baf3694baab5fe06294875d8`, pseudo-version
`v0.0.0-20260604065514-1d9240f3d27b`. Rust emits Git+full-rev because the crate is
not published. Do not set Rust crate version to 0.30.1 or a literal `latest`.
The generator version defaults to `HaveAPI::VERSION` and fails startup unless
the matching generator gem is actually installed. Register only API 7.0; avoid
pretending the SDK targets other versions.

Automatic profiles capture the full mounted structural model once, after auth
and post-mount routes. Request-local authorized descriptions control displayed
samples. No request may fetch a schema, run a compiler/generator, read secrets,
or relax authorization. New Python/JS/TS variants need no profile configuration.
Do not add an alternative renderer or copy upstream adapter logic into vpsAdmin.

SDK compatibility gate: the package identity alone does not establish that the
published SDK matches current vpsAdmin. Compare rendered imports, action/member
names, path types, setter signatures and response fields with the exact external
Go SDK and Rust source. Rust's saved `schema/api-7.0.json` is an authenticated=false
public 2026-10-19 capture (524 total actions) generated by HaveAPI 0.30.0. Current
generator naming must be checked against that retained generated surface. At
minimum compile emitted initialization, auth and representative public,
authenticated, nested and nullable/optional-output action examples. Check all
renderable current action samples for missing/mismatched SDK symbols, not just
the easy public-statistics example. An earlier local Go origin/master is stale;
use the fresh remote/proxy revision above when validating.

If this audit finds a stale SDK, stop the readiness claim and refer the evidence
through the lead. Preferred bounded remedy is the upstream saved-model override,
so unsupported/stale action samples show an honest limitation. Rust can load the
exact source-repository snapshot through `snapshot_path`, with inline crate/Git
identity. Keep an immutable sanitized copy and provenance under `api/` (not
`api/config`, which packaging replaces with a `/run` symlink), use an absolute
path derived from `__dir__`, and verify its checksum and source revision. The
inspected Rust snapshot is 3,649,376 bytes; do not silently introduce it or invent
a smaller incomplete schema. Go lacks a retained source schema in its public
repository; do not mislabel today's schema as its historic generation input.
Regenerating external SDKs expands the repository scope and needs a lead decision.

Acceptance/quick checks:

- Configured real vpsAdmin API mounts with both 0.30.1 generators. Go and both
  Rust tabs appear in version overview, initialization/auth and applicable action
  examples; nonconfigured versions stay hidden.
- Rust dependency hints use exact public Git source; output never contains a
  fictitious crates.io install/version. Go import path matches the real SDK.
- Existing API startup, language handling and access control remain intact;
  anonymous/member/admin documentation does not disclose hidden samples, fields
  or the private structural model. Assert representative regression cases at
  the vpsAdmin integration seam, not a duplicate upstream test suite.
- Focused spec, scoped lint/syntax, diff whitespace and topic coverage if changed.
  Inspect actual rendered code; no tests that merely assert configuration text.

Longer checks after final review: compile emitted programs against pinned SDKs
in disposable consumers; run read-only fixture operations to verify URL/version,
auth and errors; required services-up through the packaged API proves optional
gems and documentation files survive Nix packaging. Watchers own uncertain
compile/integration runs. Persist source and dependency identities, results and
limits. No SDK release, production request mutation or deployment is authorized.

Keep lasting profile configuration, expected SDK alignment, install identities,
failure-at-startup behavior and rollback coupling in a short owning API doc.
Rollback removes/restores both inline profile registration and generator gems
with the corresponding HaveAPI server; an older server cannot read new inline
profile configuration. Mixed API workers may show different tabs without any
wire-protocol or persisted-state change.

## Compatibility and recovery

### Decision B1: full-page documentation rendering cost

Status: measured regression; no implementation or dependency-version exception
authorized. Package B cannot be called ready for use on the present performance
evidence. Other package deliverables remain independent. The lead owns the
scope/version decision; architect recommendation is an upstream correction,
followed by explicit selection of its adoption path.

Evidence: the owner-run instrumented real API request, after mount and before
CGI decoding or RSpec matchers, took 102.375670 s wall / 102.274825 s process CPU
for administrator `GET /v7.0/`. It made 639 `Context#with` calls taking 88.757291 s
and 294 renderer calls taking 16.075294 s. These timers overlap and must not be
added. A subsequent captured request took 49.716002 s wall / 49.667719 s CPU,
with 484 context calls / 42.536361 s and 224 renderer calls / 6.041193 s.
The timings file itself has no role field; the owner identifies the first as
administrator and must bind later roles from ordered request evidence. Receipts:
`package-b/rendered-instrumented/timings.jsonl`, `package-b/instrumented.log`,
and instrumentation in `package-b/audit_rendered_spec.rb`. The first focused
run was interrupted after three examples; its zero failures are not a complete
suite result. The active watcher owns remaining capture; no duplicate run is
required for this design decision.

Root cost identified in released sources:

- `servers/ruby/lib/haveapi/documentation_context.rb`: `with` invokes the public
  constructor, which recursively copies/freezes the entire authorized API
  description even when changing only a profile or sample. The description is
  already an owned immutable copy in the parent context.
- `servers/ruby/lib/haveapi/server.rb`: each renderer availability check derives
  a context, and selected renderers derive another. Each example panel repeats
  this. Go/Rust bridge renderers derive a sample context again.
- `clients/rust/lib/haveapi/rust_client/documentation.rb`: authentication,
  authorized-action lookup and credentials selection normalize the entire
  authorized description to string keys to use a small selected subtree.
  This causes further repeated full-schema traversal in both Rust modes.

No supported 0.30.1 configuration remedy preserves the requested behavior.
The profile keys select package identity/version/source and automatic versus
saved SDK shape; none changes request-context copying or normalization.
Saved `description_path`/`snapshot_path` profiles do not fix this cost. Removing
Go/Rust profiles removes requested tabs and leaves the shared context issue in
other clients. Changing locale, worker count or timeouts does not remove the CPU
cost. Filtering examples, custom renderers, partial pages, monkeypatches and
response caches are behavior/source changes, not supported tuning. In particular,
shared HTML/context caching must not be introduced because user authorization,
locale and visible samples vary by request.

Proposed minimal fix, owned by **HaveAPI**, not copied into vpsAdmin:

1. Make deriving an immutable documentation context reuse unchanged fields that
   the parent context already owns and has deep-frozen. Deep-copy/normalize
   caller-supplied changed fields just as the public constructor does today.
   Preserve current reader names, keyword interface, unknown-key errors,
   version/URL/action-name/resource-path normalization, nil/default behavior,
   immutable result, and unchanged parent context. Public construction must
   still detach caller-owned data without freezing it. Do not trust arbitrary
   frozen inputs: a shallow-frozen hash can still contain mutable children.
   There must be no process/global/user-shared snapshot cache.
2. In the Rust documentation adapter, locate the authorized authentication or
   action subtree using bounded hash/path lookup before normalizing it. Preserve
   support for symbol-keyed server descriptions and string-keyed standalone
   contexts, and existing normalization/duplicate-key semantics. Continue to
   verify against the authorized description; do not blindly substitute
   `context.action`, which a standalone caller can supply independently.
   Keep every route/type/input/output/auth compatibility check and limitation.
3. Keep server templates, renderer selection, registry, protocol, sample text,
   source highlighting and client runtime behavior unchanged. Removing redundant
   bridge derivations or adding request memoization is unnecessary once context
   derivation is cheap; omit it unless later measurements justify separate work.

Expected independent file boundaries: server context source and
`servers/ruby/spec/client_examples/context_spec.rb`; Rust adapter source and
`clients/rust/spec/unit/documentation_spec.rb` (plus minimal fixture coverage);
the owning guide `doc/client-examples.md` may explain immutable derivation if
useful. No generated SDK regeneration, protocol/schema/database migration,
frontend bundle change or vpsAdmin rendering implementation is needed for this
correction. Add a separate session-owned HaveAPI worktree/registration only
after the lead authorizes that implementation scope. Preserve existing release
branch/tag identities. Relevant repository instructions and
`doc/agent-instructions/{development,releases}.md` have been inspected for this
proposal; implementers must read current worktree instructions before action.

Adoption options and truthful version reporting:

| Option | Exact released 0.30.1? | Consequence and authority |
| --- | --- | --- |
| Retain unmodified published artifacts | Yes | All requested example semantics remain, but measured full-page response cost is a known blocker to readiness. Continuing to deploy/use with that limitation requires an explicit informed scope decision; no claim of a performance fix. |
| Upstream development patch on 0.30.1, selected by exact SHA/patch digest | No: base version is 0.30.1, bytes differ | Honest identity is “HaveAPI 0.30.1 + documentation performance patch at SHA”, even if VERSION reports 0.30.1. Requires explicit permission to use patched dependencies. Never call it the exact published artifact or replace the registry's existing version. |
| Correct upstream and publish the next supported patch release | No: selected release version changes | Preferred durable route when authorized. Follow the supported release branch/backport procedure and shared component release process. Release publication and adoption of the changed requested version need explicit direction. Do not invent an already available release or reuse/move v0.30.1. |

For an explicitly authorized development-patch option, source/provenance must be
concrete across both normal Bundler development and Nix package builds: exact
upstream source/patch, base published gem hashes, generator/server versions,
artifact build inputs and retained unpatched recovery. Only the server and Rust
generator code require changes; untouched client artifacts can remain published
0.30.1 if that mixed-source graph is explicitly selected and verified. Do not
hide a development override in a local `.bundle` configuration, mutate installed
gems, use an unpinned Git branch or silently supply patched code only to tests.
The exact dependency mechanism is a follow-up implementation brief after the
lead/user selects the option; no application dependency change is approved here.

Acceptance for an authorized fix:

- Public-context input mutation and shallow-frozen nested-input regressions
  prove isolation. Derived contexts preserve values, normalization and error
  contracts, cannot mutate parents, and share only safely owned immutable data.
  Separate requests/users/locales retain distinct authorized snapshots.
- All affected renderer/profile/auth-filtering unit specs pass. Rust adapter
  output and limitation results are equal for symbol/string descriptions,
  missing/hidden actions, nested actions, basic/token/OAuth2 authentication,
  and ordinary/nullable/zero/false fields in async and blocking modes.
- Compare complete emitted programs and limitation records with the retained
  0.30.1 role-specific capture, plus representative HTML panels. No loss of
  samples, visibility checks or supported languages is acceptable.
- Quick tests and committed source precede independent final review; only then
  run full documentation/package checks and real vpsAdmin full-page timings
  through a fresh watcher. Measure the same user/locale/plugin/API shapes with
  matching tool/dependency identity, and report uninstrumented wall/CPU/body
  size plus low-overhead aggregated counters separately.
- Performance must no longer scale as whole-description copies per renderer
  panel or full-schema Rust normalization per action. An initial practical
  target is warm supported pages within 5 seconds on the same host; this is a
  proposed acceptance target, not an already verified result or fixed production
  SLA. If it is missed, inspect residual cost before approving adoption. Keep
  complexity and functional regressions deterministic; avoid flaky wall-clock
  assertions in ordinary unit specs.

Rollback restores the exact prior unpatched source and dependency graph
together. No persisted data changes; rollback reintroduces the measured latency.
Retain original registry artifacts, tags and receipts throughout. Existing SDK
coverage/naming and emitted-program compilation remain separate package B gates;
this performance decision neither proves them nor authorizes adding SDK repos.

No database migration or persisted-state format is intended. API 7.0 and existing
authentication/authorization contracts remain intact. Separate legacy callback
JS and new async WebUI consumers coexist. New API documentation profiles are
additive and may not change resource routing or authorization. Source inspection
of HaveAPI `v0.29.12..v0.30.1` shows Ruby client runtime changes only its version
constant; protocol remains 2.0. Server changes center on documentation rendering
and mount-time profile initialization, including startup failure behavior.
PHP `v0.29.6..v0.30.1` changes only `Client.php` under `clients/php/src`; the
0.29.12-to-0.30.1 hunk is its version constant. The new JS exports retain
`Client` and add alias `CallbackClient` alongside `AsyncClient`; compatibility
of consumers is still verified through their actual tests, not inferred from
those exports alone.

Dependency-only rollback restores the previous source and lock/generated bundle
set together; it does not reverse schema or user data. No coordinated node/OS
update is planned. Record any discovered incompatible protocol, schema or
deployment requirement and refer it through the lead before implementation.

## Shared WebUI and KB constraints

The lead accepted a new WebUI branch from fresh main with only the reconciled
final production delta from `8772bab21cd8739bf4672cdf4976aea2a6e59de3`, preserving
original authorship/source mapping. The old `dev/haveapi-async-client` refs,
worktree and records remain untouched. Do not replay its obsolete pilot series.
Replace its local 0.29.0 tarball with published npm 0.30.1 and retain policy and
session isolation behavior.

The lead owns final bilingual KB prose. Local technical sources, candidates and
schema-5 release manifests can be prepared independently. Staging is currently
owned by `2026-09-13-auth-email` with a pending release (lead's status evidence).
Do not reset, release or write that staging instance. Production publication
requires approval of the exact staged manifest; staging availability is an
external blocker, not permission to take it over.

The initial boundaries above do not prohibit the specifically requested reuse
of PR74; the exact published-history rewrite approval gate in package C controls
that later operation. No default integration, deployment or lifecycle action is
implied by branch publication or a finished handoff.

## Package C: React WebUI takeover and published async client

Suggested owner: implementer1. Ready for implementation in the lead-created
worktree `worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-webui`, branch
`dev/vpsadmin-haveapi-upgrade`, base `5a2d2bdc3ad7a827038f877d75959916528db844`.
The actual default is **main**. Read the current worktree AGENTS, design index,
API contracts, relevant requirements and latest work-log entries. Current
AGENTS requires the contributor's own identity, not the historical fixed
maintainer identity in the old worktree.

Source lineage and reconstruction:

- Old feature base `7860521f30826c3886c89c35e8ab6f4e082e0a4b`.
- Published PR74 head `5dd2333b9af230d4a81c8f772cbbb08d39b14913` on
  `dev/haveapi-async-client`; PR base is main. PR74 is the matching existing PR:
  https://github.com/vpsfreecz/vpsadmin-webui/pull/74 .
- Authorized final local production source
  `8772bab21cd8739bf4672cdf4976aea2a6e59de3`. Its four-commit history includes
  an obsolete pilot and later replacement. Reuse its final production content,
  not that whole sequence. Preserve original authorship of carried work and
  record exact old/new range and source mapping.
- Prior read-only preview under old session
  `webui-replacement/owner1/consolidation-preview/` is reference material only.
  It used older base `b9f47f06`; it is not a patch certified for today's main.
- At inspected new base, seven changed paths overlap: `WORK_LOG.md`,
  `docs/design/API_CONTRACTS.md`, `docs/design/REQUIREMENTS.md`,
  `scripts/fixtures/e2e-type-coverage.json`,
  `scripts/fixtures/structural-debt-ledger.json`, `src/lib/api/nodes.test.ts`,
  and `tsconfig.e2e.json`. Union current product work, current tests and source
  coverage; do not overwrite any with the old branch. Recompute overlap after
  any base change.

Own the entire React repo package: production request adapter, fixture/test
migration, npm/Nix dependency and provenance, affected design docs/work log.
Primary files are `src/lib/api/{haveapi,haveapiRequestClient,public}.ts`, removal
of redundant `haveapiEnvelope.ts`, `src/lib/errorMapping.ts`, migrated
`src/lib/api/*.test.ts`, `src/test/haveapiXhr.ts`, `vitest.setup.ts`, affected
E2E fixture/spec/coverage files, root npm manifest/lock, `packages/frontend.nix`,
package-source checks and `docs/design/*`. BFF application code is outside scope
unless a concrete regression is referred to the lead.

Runtime invariants:

- Actual npm `AsyncClient` is the normal authenticated, public and description
  request path. The library owns transport, serialization and wire decoding.
- WebUI retains BFF OAuth/session policy, per-request credentials and locale,
  one bounded refresh path, request abort/timeout semantics and existing domain
  result/error shape. No automatic mutation retry or invented operation success.
- Public and authenticated instances remain isolated by scope and resolved base
  URL; do not call setup/authenticate against WebUI's already-versioned runtime
  base merely to recreate its existing policy layer.
- Preserve real `AsyncError` classification (API vs protocol vs transport vs
  timeout/abort), structured error details and response/meta data. Do not add a
  second generic decoder or fallback custom transport.
- No pilot route, opt-in runtime toggle or duplicate implementation remains.

Use exact root dependency `haveapi-client: "0.30.1"` from npm; regenerate the
lock using pinned Node/npm and preserve unrelated entries. Its SLSA provenance
binds `refs/tags/v0.30.1` to HaveAPI commit
`1c3c98f0d77e0b23c8da1a8937f25c5799864a3b`, release workflow run `40114719358`.
The earlier npm integrity is the artifact identity. Remove the superseded vendor
tarball, its source overrides and obsolete archive-only checks/documentation.
Use the repository's normal registry package build path, refreshing its npm hash
if applicable. Either existing standard `buildNpmPackage` npmDepsHash or standard
`importNpmLock` without a local override is acceptable when aligned with current
main; do not invent a custom fetcher or filtered lock. Keep meaningful package
source/provenance/security checks. Reconcile both 0.30.1 exports and declarations
against the copied adapter, including `AsyncError` and `RequestSpec`.

Prepare one logical final dependency update and one production adaptation commit
if useful; do not commit then remove the pilot or intermediate vendor pin. The
lead owns final user-facing prose review. Update current contracts and one dated
takeover work-log entry; distinguish historical evidence from new checks.

Quick acceptance: actual installed package/declarations typecheck; focused
adapter/auth renewal/public isolation/protocol-error/abort regressions; migrated
domain tests; package-source tests; scoped lint, design audit and regenerated
inventory/structural/E2E coverage as required. Fixtures use the real installed
library with controlled XHR, not mocked adapter answers. Main's new node tests
and current typed E2E scope must survive reconciliation.

After commits and independent final review: full unit suite, normal production
build, Nix frontend/package/source checks and ordinary browser workflows for
public overview, authenticated home, refresh/session expiry, failure handling
and relevant VPS action state. Use desktop/mobile browsers where these workflows
already support them. Retain actual provenance and separate fixture coverage
from live API/OAuth proof. No deployment is authorized.

PR publication constraint: fully prepare, review and publish the new owned
branch first. GitHub cannot change PR74's head ref to the new branch. Reuse by
updating its existing remote head requires a concrete exact-range publication
plan. Current AGENTS requires exact published-commit rewrite authorization;
the lead requires that final approval before any force push. Record both old
published `7860521..5dd2333` and old local `7860521..8772bab` ranges, new base/head,
content migration and absence of deployed/schema boundaries. If authorization
is obtained, use an explicit fresh exact lease for the old remote head and verify
both own branch and PR head equal the final head. Leave old local branch,
worktree, old records, unrelated refs and PR63 untouched. Track our owned branch
against its own remote ref and main target; PR74 is a second publication alias,
not a reassignment of the old session's local registration.

## Package D: KB technical evidence and guarded release preparation

Suggested owner: implementer3 for mechanics; lead owns final Czech/English prose.
Ready to begin independently. Read KB/writing procedures and tool help; use the
existing `kb-original/{cs,en}` copies and production read-only revision checks.
Do not copy credentials. Own session-local source snapshot, technical fact
sheet, validation commands/results and candidate/manifest mechanics, not product
repository changes or final prose rewriting.

Identify exact Czech and English page IDs from originals, retaining reciprocal
`<page>` mapping derived from English `manuals:vps:api`. Check whether either page
is already managed by `vpsfree-kb-contracts`; do not register a new contract repo
or add managed markers simply to edit this article. Produce a concise technical
fact sheet with canonical installation/import examples, supported runtimes,
sync/async distinctions, authentication and links:

- Python: PyPI `haveapi-client==0.30.1`, Python >=3.11; verify public import and
  sync/async calls from the actual released package/source.
- TypeScript: npm `haveapi-client@0.30.1`, bundled declarations, actual
  `AsyncClient` API; no separate invented TypeScript package.
- Rust: source repo `vpsfreecz/vpsadmin-rust-client`, crate `vpsadmin-client`,
  Rust >=1.95, async and optional blocking client. crates.io returns 404 for
  this crate as of investigation; use HTTPS Git plus full public revision
  `ff876abe17e3301da62c1b6afbda055ec89db9d2`, not a registry installation.
  SDK version 0.1.0 and API 7.0 are independent of HaveAPI generator 0.30.1.
- Preserve existing correct Go/Ruby/PHP/CLI information unless the requested
  new state requires a correction. Do not document prior incorrect guesses.

Validate examples with released dependencies or exact SDK source in isolated
temporary consumers; no real credentials or member mutations. Distinguish
syntax/type checks, fixture behavior and any public read-only smoke explicitly.
Send facts and verified snippets to the lead for the final prose pass.

Prepare complete-page candidates and checksummed schema-5 manifests through
`kb-contract-fetch/build/manifest` and one bilingual `release-changes.yml`, with
informative Czech noun-phrase and English summaries. The workspace's current
schema-5 requirement overrides the older schema-4 prose still present in the
contract workflow. Preserve the fetched source revision/content guards.
If the page is unmanaged, follow installed tools' ordinary page-candidate route;
do not forge managed provenance or claim a code revision without a real file.

Staging remains blocked by another session's pending release. Local preparation
can finish while blocked. The lead must claim staging legitimately when it is
available, stage the exact candidates at real IDs, verify rendered content and
both translation links, expose exact summaries/revision-history links, then seek
production approval for those concrete manifests. Do not publish production or
mutate the existing staging owner's state. Recovery before publication is local
candidate revision; after any separately approved publication, rollback uses
captured original page content through the same guarded release workflow.

## 2026-10-25 addendum: Rust registry adoption

User direction: remove the Rust Git source pin now that the SDK is published.
Keep the original Git observations, receipts and old source revision as history.
This revision changes current installation guidance only. The user owns the
HaveAPI performance fix in another session: do not investigate, patch or select
a provider successor here. Blocking R1 remains open until that successor is
explicitly adopted and verified with the authorization/locale/input-ownership
acceptance already recorded in B1. This change does not remediate R1.

### Release identity and compatibility

Read-only verification on 2026-10-25 found the sole crates.io release
`vpsadmin-client` **0.1.0**, non-yanked, published
`2026-10-24T21:21:08.329377Z`. Its 178,978-byte archive has SHA256
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`, matching the
registry metadata. The archive's `.cargo_vcs_info.json` names root-path source
commit `b6f84679d33ff041388535dcf4dc060aeb0d1b9d` in
`https://github.com/vpsfreecz/vpsadmin-rust-client`. The original Cargo manifest
matches both that locally available commit and previous pin
`ff876abe17e3301da62c1b6afbda055ec89db9d2` byte for byte.

All packaged Rust source and examples are byte-identical to the previous pin:
690 packaged files match; differing files are README, CHANGELOG, Cargo.lock,
Cargo-normalized manifest and generator provenance, plus Cargo packaging
metadata. The provenance now reports generator 0.30.1; runtime and schema hashes
are unchanged. API target **7.0**, edition **2024**, declared Rust minimum
**1.95**, `default = []`, and `blocking = ["reqwest/blocking"]` are unchanged.
Async imports `vpsadmin_client::Client`; blocking imports
`vpsadmin_client::blocking::Client` and retains its synchronous-runtime boundary.
Reqwest/Serde/serde_json/url requirements are unchanged; Tokio remains a consumer
dependency for the async examples. No new SDK source/API compatibility audit is
needed solely for this source substitution.

The packaged Cargo lock is not byte-identical to the former Git lock: both have
159 packages, with 17 package-version replacements. Do not claim identical
resolved dependency graphs or transfer an old compilation result to this new
lock. Library consumers resolve with their own manifest/lock; these lock changes
do not alter the verified SDK public-source identity. No fresh compilation or
full-page request is required for this mechanical profile revision. Existing
sample/coverage verification and its limitations remain valid only to their
recorded scope. Evidence: `package-b/rust-crates-2026-10-25/{crates-io.json,
comparison.json,release-comparison.json,vpsadmin-client-0.1.0.crate}`.

### Package B2: implementer2, ready bounded brief

Starting vpsAdmin head supplied by lead: `21872fe6`. Change only:

- `api/lib/vpsadmin/api.rb`: remove the Rust `source` hash; retain
  `rust: { crate_name: 'vpsadmin-client' }`. Keep Go, API 7.0 selection and
  generator requirements unchanged. Do not add `crate_version`.
- `api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`: change old Git
  installation expectations to registry async/blocking commands, reject the old
  Git URL/revision in those initialization panels, and preserve authorization,
  locale and action examples. Add a small separately selectable check using the
  actual mounted Rust profile and upstream init renderer, with a minimal
  in-memory documentation context; no HTTP full-version render is needed for
  this check. Do not replace existing full-page coverage with the small check.
- `tests/suite/services-up.nix`: expect registry installation hints in place of
  the Git URL/revision and inverted cargo-add rejection. Retain existing tabs,
  action examples and package integration assertions.
- `docs/api-client-examples.md`: describe the published registry SDK and Cargo
  selection semantics; remove the current claim that it is unpublished and the
  source-pin installation guidance. Retain performance/authorization facts and
  the distinct SDK/API/generator identities. No docs index change is needed.

Exact HaveAPI **0.30.1** contract, confirmed in released
`documentation_clients.rb`, Rust `model.rb`, `documentation.rb` and
`clients/rust/docs/documentation.md`:

- Supported Rust keys are `crate_name`, `crate_version`, `source`,
  `snapshot_path`, `generator_config_path`, `generator_version`.
- Omitted/nil `source` and omitted/nil `crate_version` render
  `// cargo add vpsadmin-client` for async and
  `// cargo add vpsadmin-client --features blocking` for blocking. There is no
  emitted SDK version or server-side registry resolution. Cargo selects a
  compatible release under its resolver, manifest, toolchain and lockfile.
- An optional three-part `crate_version: '0.1.0'` instead emits a Cargo.toml
  requirement `version = "0.1.0"`; this is Cargo's compatible requirement,
  not exact `=0.1.0`. Literal `latest`, `0.1` and `=0.1.0` are not accepted by
  the HaveAPI profile validator. Omitting it follows the existing design's
  default-version policy and avoids introducing an arbitrary new pin.
- `generator_version` defaults to `HaveAPI::VERSION` and must match the loaded
  generator. It is independent of SDK 0.1.0 and API 7.0; leave it unchanged.

Quick acceptance: run only the existing mount check and new bounded init-render
check in the repository API shell, scoped Ruby lint/syntax, Nix syntax/evaluation
appropriate to the edited assertion, and diff whitespace. Both upstream Rust
renderer modes must produce the exact cargo-add hints and unchanged imports/
execution modes, with no Git source or fabricated version. Prefer actual
`HaveAPI::ClientExamples::RustAsyncClient`/`RustBlockingClient` initialization
rendering with the mounted profile; direct public adapter `render(kind: :init,
context:, mode:)` is also an actual renderer seam. Use short failures, never a
diff of the whole page. Do not run the slow full HTML example or services VM for
this mechanical revision. Long integration remains deferred by R1 and final
review order; the original full-page/service gates remain part of overall
acceptance after the external remedy is adopted.

### Package D and recovery

Lead owns final bilingual KB prose; implementer3 owns source guards, fact-sheet
refresh, candidate checks and regenerated manifests. Use the released README's
`vpsadmin-client = "0.1"` and blocking
`vpsadmin-client = { version = "0.1", features = ["blocking"] }`. These are
compatible 0.1-series requirements; do not call them exact pins. Plain
`cargo add vpsadmin-client` agrees with API renderer output. A command using
`@0.1.0` is also a version requirement, not an exact lock, but is unnecessary
for the selected default guidance. Preserve API 7.0, Rust >=1.95, Tokio async
setup, blocking runtime caveat and existing authentication examples. Link the
crate registry/reference and repository as appropriate; remove Git-source
installation only from current supported guidance. Preserve original sources,
historical checksums and Git evidence. Recheck source-revision guards and rebuild
candidate/manifests under ordinary ownership rules; no staging takeover or
production write is authorized by this addendum.

No server wire contract, persistent state, database migration, node coordination,
generated SDK content or runtime dependency of vpsAdmin changes. Mixed workers
may temporarily show Git versus registry install hints. Rollback restores this
small configuration/docs/assertion delta together; it does not undo consumer
Cargo changes. Consumer rollback uses the consumer's retained manifest/lock.
Neither this revision nor its quick checks clear R1 or authorize integration,
publication, deployment or session lifecycle changes.

## 2026-10-26 addendum: released HaveAPI 0.30.2

User direction supersedes the original exact 0.30.1 target with released
**0.30.2**. Packages A3 and C3 below are ready for independent implementation;
their dependency refresh need not wait for the separate R1 acceptance analysis.
Starting heads supplied by lead: vpsAdmin `57a53e700`, React WebUI `014f7b9c`,
KB tracking `df1944a2`. Preserve all prior observations and review receipts.
No provider fix, merge, push, deployment or lifecycle action belongs to this
architect assignment. Lead controls source ownership, review and publication.

### Release identity

All requested artifacts were found and downloaded on 2026-10-26. Ruby gems,
npm and Python archive bytes match registry-provided digests. PHP has no registry
dist checksum; its downloaded archive hash below is an observation, bound to
the exact source ref. Canonical HaveAPI annotated tag object
`8c24a7c89ee13936da6f81908c1da84f1d8eda9b` peels to
`321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`, confirmed by remote read-only lookup.

| Released artifact | SHA256 of downloaded artifact |
| --- | --- |
| Ruby `haveapi` 0.30.2 | `bc90fba07462088ee9982fe4f0ae910028000fa5123554034a74aeddbd6b1815` |
| Ruby `haveapi-client` 0.30.2 | `d0cea63d1f0c64406aacfcfdb555fe928b70b21411014a131fae3072541dddc7` |
| Ruby `haveapi-go-client` 0.30.2 | `17c57891f934cc259a6a6d5342b12c54995eb0fa799ef07a70be72f0df5ef083` |
| Ruby `haveapi-rust-client` 0.30.2 | `ae4b54e62d057443dff7a7e60187eaa7dcb301260bba15450b11d6f734e58948` |
| npm `haveapi-client` 0.30.2 tarball | `e6fc12590ebabd05b09d579cfcd62344bf60dfa0b3b05b3c75d7015e2bd5cbfa` |
| PyPI `haveapi-client` 0.30.2 wheel | `4332346ea2923edd2764107e900f87b3fba780c287869432ab1cfdd265646d50` |
| PyPI `haveapi-client` 0.30.2 sdist | `f4484155f2a4558e9ef6a0a5be515809a7c32fe9ababa4af3cf9f8e71dd351cc` |
| Packagist `haveapi/client` 0.30.2 GitHub zip | `fcf2453bbfa1dd8ebe8861124151100cf422e355a9319eea84f7fb9f3a3864b2` |

PHP source is `a02dd2506209f54ea782fbd949243207bf9f93bc` in
`vpsfreecz/haveapi-client-php`; its remote annotated v0.30.2 tag peels to that
commit. npm integrity is
`sha512-o2geRdCaZe9gH93GPLMdGCxeIflyuERt3dN0oErVe3xzdLfPV2A+UwDI62LbUSOEzd2XgMZLCa/BbmhwZBQ/6Q==`.
Its published SLSA statement binds the matching SHA512 to canonical source
`321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`, `refs/tags/v0.30.2`,
`.github/workflows/release.yml`, run `40238928168`, attempt 1. There is no npm
`gitHead`. Evidence lives in `release-0.30.2/`, including
`artifact-summary.json` and `npm-provenance-statement.json`.

Source diff v0.30.1..v0.30.2: Ruby client, Go generator, JS/PHP clients and
Python change version declarations only; protocol remains 2.0. Server context
derivation and Rust documentation lookup contain the functional performance
changes, with additional regression/benchmark/CI tooling. No generated Rust
SDK release is implied. Existing crates.io `vpsadmin-client` 0.1-series guidance,
crate-name-only profile and independent API 7.0 target remain unchanged.

### Package A3: vpsAdmin dependency refresh, implementer0

Keep original package A boundaries and accepted scoped generation procedure.
Own source HaveAPI requirements in `api/Gemfile`,
`client/vpsadmin-client.gemspec`, `download_mounter/Gemfile`,
`plugins/outage_reports/utils/Gemfile`; generated API/client/download-mounter
Gemfiles, locks and gemsets; legacy PHP Composer manifest/lock; both checked-in
browser distributions under `webui/public/js/` and `console_router/public/`.
Retain the Fiddle/libffi/pkg-config support. Use `~> 0.30.2` declarations where
the project follows that convention, with **exact 0.30.2** resolved for every
HaveAPI server/client and both Go/Rust generator gems. PHP source declaration
and resolution are 0.30.2. Replace both browser files with verified npm 0.30.2
`dist/haveapi-client.js`; do not hand-edit generated bundles. Preserve unrelated
dependency resolutions and report unavoidable transitive changes.

Quick checks: lock/gemset agreement and registry digests, all HaveAPI consumers
inventoried, loaded Ruby/generator versions and source paths, PHP client load,
callback exports/bundle equality, scoped syntax/lint and whitespace. No full
documentation GET or long VM/build run before final independent review. Package
B owner retains API profile/spec/docs files; A3 must not revert the registry
profile or change SDK/API identities. Lead serializes Git in the shared worktree.

### Package C3: React npm/provenance refresh, implementer1

Own root `package.json`, `package-lock.json`, `packages/frontend.nix`,
`packages/haveapi-client-provenance.json`, current
`docs/design/{HAVEAPI_CLIENT,PACKAGING}.md` and the appropriate dated work-log
entry/index. Set exact root `haveapi-client: "0.30.2"`; regenerate the lock and
frontend dependency hash in the pinned Node/npm shell. Preserve the BFF lock,
unrelated entries, exact XMLHttpRequest transport pin, existing takeover source
mapping and R2 contradictory-receipt correction. Refresh provenance to the
artifact/source identities above. Source-check scripts are already data-driven;
edit only if an actual remaining version-bound assertion requires it. No adapter
rewrite, transport fallback, auth change, pilot return or vendor tarball.

Quick checks: installed declarations/typecheck; existing focused actual-package
adapter/public-isolation/auth-renewal/error/abort and R2 mutation-guard fixtures;
package-source check/tests, scoped lint, docs audit and whitespace. Record npm
source-file matching and preserve historical 0.30.1 receipts as history. Full
unit/build/Nix/browser checks follow committed-deliverable review under existing
package C acceptance. No WebUI deployment or PR-head rewrite is authorized here.

### Package D3: KB versions and guarded mechanics

Lead owns final bilingual prose; implementer3 owns source guards, fact sheet,
current candidates/manifests and focused validation. Update current Python/npm
HaveAPI examples to published 0.30.2, retaining Python >=3.11 and actual exports.
Do not invent `vpsadmin-client` 0.30.2: Rust remains ordinary version `"0.1"`
with optional blocking feature, Rust >=1.95 and API 7.0. Keep all historic
0.30.1/Git evidence. Recheck production source revisions read-only and rebuild
checksummed candidates/manifests; staging requires legitimate availability and
production writes require exact staged approval. Refresh only affected snippet
dependency evidence; pure version-only client source differences do not justify
an unrelated SDK rebuild or real-member mutation.

### Review, compatibility and R1 gates

Before review, consolidate each superseded dependency-pin stream into the final
0.30.2 update, with generated metadata and current docs aligned. Preserve exact
old/new base/head ranges, original authorship/takeover map, diff/range mapping and
the explicit no-migration conclusion. Do not rewrite protected published WebUI
commits without their exact approval; lead resolves any such boundary. Earlier
review remains evidence for unchanged code, not approval of new source identity.

R1 remains **open**. Adoption of the version number alone does not prove the
actual consumer loads the released fix, improves request cost, or preserves
authorization/locale and immutable ownership. After committed quick checks and
independent review, a fresh watcher runs the real mounted vpsAdmin API tests and
same admin/member/anonymous `GET /v7.0/` instrumentation, preserving the old
50–139-second inputs/evidence. Bind each timing explicitly to role/locale,
plugin/API shape, final consumer head, effective lock, loaded gem source/hash,
mount completion and toolchain. Measure GET before CGI/matchers, wall/CPU/body
size and existing context/renderer counters; distinguish overlapping counters.
Keep an uninstrumented warm request measurement separate. Require every role
and authorization/locale regression to finish, not a partial zero-failure run.
The earlier same-host warm-page target of <=5 seconds is the proposed practical
acceptance threshold, not a release claim. A miss or unexplained output change
returns to lead for diagnosis/design; do not cache privileged HTML or suppress
examples to pass. Ownership/source compatibility detail follows below.
Required packaged `services-up`, affected
full/core API checks, compilation gaps and WebUI long checks remain separate
gates; upstream benchmarks cannot replace consumer proof.

No database/persisted-format/wire-protocol change is identified. Mixed 0.30.1/
0.30.2 clients remain compatible; server plus optional generator bundle must
move together because default generator-version validation remains enforced.
Roll back complete source/lock/generated-bundle sets and paired WebUI artifacts;
retain BFF session data. Rolling API dependencies back reintroduces known R1
cost. No coordinated node update or deployment is needed to implement this
feature change. Integration, deployment and KB promotion remain separate acts.

### Released fix/source assessment and package B3 follow-through

Artifact-to-tag comparison is complete for runtime source. The release gems
match 204 server files, 65 Ruby-client files, 55 Go-generator files and 28
Rust-generator files at canonical source `321ce8256`. All 53 npm packed files,
36 PHP split-repository files and all 18 Python wheel `.py` files match their
canonical component paths. Server packaging additionally copies six matching
root `doc/` files and includes generated `doc/json-schema.html`; that generated
HTML was not certified byte-for-byte against a rebuild. Rust's gem includes its
prepared generator-provenance `Gemfile.lock`, intentionally required by its
gemspec and not tracked in source. Python sdist retains an identical
`pyproject.toml.orig`; its rewritten manifest differs only in formatting.
These packaging exceptions are not runtime source mismatches. Raw comparisons
are `release-0.30.2/source-file-comparison.json` and
`release-0.30.2/packaging-exceptions.json`. npm attestation source/digest fields
were inspected and archive bytes matched; no independent Sigstore signature
verification was executed by the architect.

The released source meets the proposed B1 design boundary on inspection:

- Exact base-class `Context#with` duplicates the frozen context shell, reuses
  unchanged already-owned fields and normalizes/copies every explicitly supplied
  replacement. Public construction still detaches Hash/Array/String contents,
  including mutable children of shallow-frozen inputs. Explicitly passing an
  existing owned container still copies it. Returned contexts remain frozen;
  nil/default normalization, unknown-key errors and parent/sibling isolation are
  preserved. Subclasses retain the constructor path and its side effects.
  Profiles and arbitrary non-container objects keep their existing reference
  semantics; do not claim a new arbitrary-object deep-freezing guarantee.
- Rust uses shallow normalized member maps on the selected path, then normalizes
  only the selected action/provider or credential header. It preserves
  last-inserted symbol/string collision semantics, route/type/input/output checks,
  provider equality, basic/token/OAuth2 preference and both execution modes.
  Missing or malformed selected action/provider shapes fail as limitations.
  It still derives authorization from the request's description, not an
  independent supplied action or a privileged private SDK model.
- There is no response cache, cross-user cache or adapter authorization-decision
  cache. Public profile keys, registry installation defaults, API routes, wire
  protocol, generated runtime and SDK schema remain unchanged. Templates and
  renderer selection are unchanged. Supplying a large resource subtree still
  copies that subtree, and shallow maps still traverse ancestor siblings; the
  change does not promise constant cost for all API shapes.

Upstream source includes context regression tests for each changed/unchanged
field, shallow-frozen mutable children, explicit nil, nested mutations, subclasses
and unknown keys; allocation tests distinguish independent requests from derived
contexts. Rust tests cover both modes, mixed keys/collisions, provider/header
changes, hidden samples, mutable standalone contexts and malformed selections.
Deterministic work-count tests forbid traversal of unrelated descendants.
These tests were inspected, not executed here; no other session's worktree,
records or refs were changed or needed for this assessment.

**B3 owner: implementer2, after A3 supplies the effective 0.30.2 bundle.** Own
`docs/api-client-examples.md` and any narrowly necessary consumer spec update;
do not overlap A3 lock/artifact files. Replace the current present-tense
0.30.1 cost paragraph with the supported 0.30.2 ownership/authorization contract.
Retain the costly baseline as session evidence, not as a statement that the new
version still has the exact diagnosed fault. Do not claim actual latency until
measured. Existing profile configuration, registry hints, API7 target and
SDK compatibility limits stay unchanged. Existing `:documentation_profile`
checks can verify mount and real init-render behavior before review. Add no
consumer copy of upstream renderer code, cache or broad upstream test suite.

Before long measurements, prove from the consumer environment that the loaded
server context and Rust adapter files match the released source, not an old
installed gem, local path override or patched file. Retain absolute source
locations, loaded versions, SHA256s, effective lock and Nix input identities.
A bounded installed-code check may establish changed-input detachment and
unchanged-description identity without rendering the full API. Preserve any
failure for review rather than substituting a successful source-tree check.

For post-review measurement, copy the retained instrumentation to a new evidence
path; never overwrite `package-b/audit_rendered_spec.rb` or its baseline outputs.
Preserve its GET-before-CGI timing boundary and wrapping behavior, and add
explicit role/locale plus body-size/status fields. `prepend` instrumentation
does not subclass the context, so it retains the optimized exact-class path.
Warm-up must not precompute/cache privileged pages. Repeat the ordered
admin/English, member/Czech and anonymous/English requests with the same full
API/plugin fixture, then a warm uninstrumented request for each role. Preserve
private test-only credentials without printing them. Verify restricted fields,
samples and admin actions remain absent for the member, locale rendering has no
missing translations, and subsequent users cannot inherit earlier context data.

Baseline receipts contain three GETs of 102.376, 49.716 and 139.036 seconds;
the timing rows themselves lack role labels, while render receipts identify
admin/user/anonymous in the corresponding ordered spec. Baseline render inventory
is 174 panels, 168 emitted programs, six limitations. Compare new results by
role/client/kind/resource/action/sample identity, allowing only explained
intentional deltas such as the separately approved Git-to-registry dependency
comments. Do not silently normalize away source/body differences or infer role
from elapsed time. Keep basic/token/OAuth2 output and async/blocking semantics,
hidden-data checks and full pass/fail receipts. Existing uncompiled SDK-sample
gaps are still separate; do not call static symbol checks compilation proof.

R1 may be closed only when independent review accepts the source/ownership
change and the actual 0.30.2 consumer completes these timing and isolation checks
with material reduction and no required semantics lost. If measured cost remains
unacceptable, keep R1 open and refer it to lead/user; this assignment does not
authorize repairing or benchmarking a new upstream implementation.

### 2026-10-26 SDK acceptance decision: representative compilation

Bounded supplement to `package-b/b3/postreview/plan.md`, for implementer2 only
after quiet timing completes and the lead releases a verification utility slot.
This decision was prepared by static inspection only: no API request, compiler,
build, provider edit or new application test was run or added. The lead accepts
the session-only harness/sample preparation before execution; any application,
SDK or provider source change remains a separate lead decision.

The original 17 action-example identities are all top-level resources; the
saved emitted programs contain no nested resource call or explicit nullable
input setter. `DnsResolver.Index` exercises optional associated output, not
nullable input. The original all-program symbol audit remains useful but is
explicitly not compilation. Choose the smallest representative complete-program
set rather than compiling duplicate role variants or rebuilding an SDK:

| Actual current page output to compile unchanged | Go | Rust async | Rust blocking |
| --- | --- | --- | --- |
| Initialization | 1 | 1 | 1 |
| Basic and OAuth2 authentication | 2 | 2 | 2 |
| Existing-token authentication | limitation | 1 | 1 |
| `Cluster.PublicStats` public action | 1 | 1 | 1 |
| `Location.Update` path arguments and several input setters | 1 | 1 | 1 |
| `DnsResolver.Index` optional associated output | 1 | 1 | 1 |
| **Total actual programs** | **6** | **7** | **7** |

Take these **20 exact complete programs** from the successful current 0.30.2
capture, selecting the admin rows for a stable bounded inventory and retaining
their role/panel coordinates, sample identity and SHA256. Other roles remain
covered by full-page authorization/output-equivalence checks, not falsely by
this compile selection. Do not combine auth builders with other programs,
replace generated calls, reformat sources or copy earlier Git-install variants.
Keep the six known Go limitation records (token authentication and Vps.Index
for each captured role) and their reasons. Do not manufacture token code or
treat a limitation as a passing compiler case. All remaining published programs
retain their static-audit/equivalence status; do not report all 168 as compiled.

Use one disposable Go consumer with exact module
`github.com/vpsfreecz/vpsadmin-go-client` version
`v0.0.0-20260604065514-1d9240f3d27b`, source
`1d9240f3d27b5831baf3694baab5fe06294875d8`. Each emitted main has its own
`cmd/<identity>/main.go`; a single `go build -buildvcs=false ./cmd/...` can share
the generated-library cache. Retain the resolved module metadata and sums,
including its source identity. Do not use floating `@latest` to resolve this
verification consumer merely because the displayed installation comment does.

Use one disposable Rust consumer with registry `vpsadmin-client = "=0.1.0"`
solely for repeatable verification; verify archive SHA256
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`.
Do not change normal API/KB version selection. Add Tokio macros/rt-multi-thread
and serde_json, retain the freshly resolved consumer Cargo.lock and toolchain.
Each complete source is a separate bin. Define consumer feature
`blocking = ["vpsadmin-client/blocking"]`, with blocking bins requiring that
feature; build async bins with default features first and blocking bins with
the feature enabled. This avoids masking an async dependency on the optional
blocking API. Use `cargo build --locked --bins`, then the blocking-feature
build, rather than executing programs. A single pinned supported compiler
(>=Rust1.95) suffices for this consumer-signature gate; do not claim a second
MSRV matrix. Retain exact compiler/Nix identities; Go's shell follows its selected
nixpkgs, while Rust has a locked flake. Watchers own uncertain compile batches.

**Separate synthetic fixture coverage: two samples, six programs.** Static
inspection found these routes/setters in both exact SDKs and the current API:

| Case | Real authorized action and structured sample |
| --- | --- |
| Nested path | `Dataset.Snapshot.Show`, resource path `['dataset', 'snapshot']`, action `show`; `path_params: [101, 202]`, `request: {}`, `response: { id: 202 }`, `status: true` |
| Nullable input | `DnsRecord.Update`, resource path `['dns_record']`, action `update`; `path_params: [101]`, `request: { ttl: nil }`, `response: {}`, `status: true` |

These are fictitious IDs and response samples, never executed. After the timing
window, load the already reviewed API/bundle once through its normal fixture
harness, obtain the real **member-authorized** API7 description and mounted
Go/Rust profiles, and select the resource/action from that description. The
context must retain that real description, selected resource/action, real base/
version URL, path and profile; only its structured sample is synthetic. Invoke
the actual upstream Go/Rust async/Rust blocking renderer, not handwritten SDK
calls or an independently rebuilt adapter/model. Do not alter the API example
DSL, schema, private profile model or authorization to obtain output. Retain
the selected authorized contract, sanitized input sample, returned status/reason
and exact source bytes. Obtain no full HTML page just for these two samples.

Expected nested output uses the real Dataset.Snapshot resource chain/two path
arguments in Go and `dataset__snapshot(...).show(...)` in Rust. Verify the SDK
route is `/v7.0/datasets/{dataset_id}/snapshots/{snapshot_id}`. Expected nullable
output selects `SetTtlNil(true)` in Go and `.ttl_null()` in both Rust modes,
without adding other setters. Go must not turn null into zero; Rust must not
omit the input. Both SDKs expose these setters in the inspected source. Compile
the six exact returned programs in the same consumers, identified separately
from the 20 published-page cases. This is renderer/SDK compatibility coverage,
not evidence those synthetic examples appeared on the published page, nor proof
of actual wire serialization or successful server execution.

If the actual authorized description or renderer yields a limitation, preserve
it and report the specific uncovered case; do not patch a schema, broaden roles,
choose a different SDK, or quietly omit it. If compilation fails, retain the
original bytes and diagnostics and refer the naming/type/source mismatch to
lead. Acceptance is 20 published plus six supplemental complete programs built
against the exact sources, with all limitations and uncompiled scope explicit.
No SDK regeneration, real API mutation, fixture endpoint execution, exhaustive
provider matrix or public-contract expansion belongs to this gate. It does not
independently close R1 or replace the lead's source/performance acceptance.

## 2026-10-26 package E: development cluster for both interfaces

User explicitly requested starting this exact session's vpsAdmin development
cluster **after current work/verification**, to test legacy PHP and new React
interfaces. Lead releases startup after the outstanding A/C checks and source/
performance acceptance; this is not production deployment, default integration,
cluster reset, or session lifecycle approval. Implementer3 owns bounded
preparation and runtime verification. Lead owns the final start authorization
within that sequence and resource allocation. No project-code change is expected.

### Observed state and mandatory boundaries

Session/current and both environment variables match
`2026-10-24-vpsadmin-haveapi-upgrade` under
`/home/aither/workspace/ai/vpsfree.cz`. Selected runtime is
`/nix/store/fqajxhsmaqg44pl8x2xshgn8q0bl7wr2-dev-workspace-0.2.0`; installed
provider is
`/nix/store/wahwpzf7gz4hfzpaijd4nih6fqgz0flr-vpsfree-dev-workspace-tools-0.1.0`.
The architect read workspace deployment/lifecycle/coordination guidance, the
installed `workspace-host coordination guide`, provider README and native
selection/ownership paths, and WebUI package/module contracts.
Implementer3 rereads current instructions before action; a changed selected
runtime requires rechecking its contract. Current provider schema is 1,
transition policy 3.

Native inspection reports stopped, ready=false, no topology/network selected,
no result GC root. Only `config.json` and `socket-dir` exist in
`.dev-clusters/vpsadmin/clusters/<slug>/`; no runner, disks, applied selection or
WebUI credential bundle has been prepared. **Inspection side effect:** installed
`config`/`urls` commands initialize the native per-session config/socket stub;
these files were materialized during inspection at 10:28. They are retained
intact. No start, reset, reservation, VM deployment, source edit or private-helper
invocation occurred. Treat config/URL commands as preparation, not pure reads.
Raw native status/URLs include fixture passwords: redact secret fields in logs
and reports rather than persisting their complete stdout in tracking.

The socket identity is `/tmp/vpsfree-devcluster-02da06564216`. Revalidate it
through native commands and the complete workspace/slug/runner tuple before
future action; never infer ownership from a dated pathname or adopt foreign
state. Preserve lifecycle/package generation fencing and all native refusals.
No claim or host policy change is needed merely to inspect or build feature
sources. Do not invent a machine alias/reservation for a VM; if coordination
requires an actual shared physical-host mutation, refer it to lead separately.

### Source selection and compatibility preflight

Only these two own worktrees exist, clean at inspection:

- `vpsadmin`: `70a2ed54b98d0c2f359a9cc4484452a257a9807b`.
- `vpsadmin-webui`: `f10d3d48c4f21cc39187c3667ffffd9952404c11`.

The native launcher automatically selects both by exact session path, overriding
its packaged API and WebUI defaults. Require WebUI source kind `worktree`, full
revision f10d3d48..., dirty=false, and API 70a2ed54b... in evaluated/built/runtime
proof; do not accept the provider's older fallback WebUI revision. There is no
session HaveAPI checkout, so the cluster must use the reviewed 0.30.2 gem/bundle
graph. No SDK regeneration or dependency refresh belongs to E.

**Material input distinction:** absent a session vpsAdminOS worktree, the native
provider selects canonical bare `refs/remotes/origin/staging`, observed
`d9be8c4bada590c0405df85444600d40e6f3caa6`, and overrides both `vpsadminos` and
`vpsadmin/vpsadminos`. This differs from vpsAdmin's own locked
`8e44a5124439b1f3048ffc56b1717614a5360358`. Provider nixpkgs follows that OS
input, and WebUI nixpkgs/API inputs follow provider nixpkgs/our API. Thus
standalone WebUI package checks at its own nixpkgs do not by themselves prove
this cluster build. No new OS/provider repository scope is assumed. Lead must
accept the concrete native effective graph before startup; if the OS source
needs pinning, an owned worktree, or a provider change, refer that bounded decision
instead of mutating the canonical ref or silently selecting a different version.
Recheck exact refs/graph when building; preserve a receipt if upstream advances.

The selected OS must provide per-disk `preserve`, rootDisk descriptors,
`overlays.all` and `vpsadminosRubyGemConfig`. Inspect kernel derivation/cache
availability before a long run where possible. An unexpected local kernel
build stops the owned operation for investigation under the normal verification
rule; do not solve it by dropping tests or changing host/package policy.

### Supported topology, routing and OAuth

Use native `single` topology and **bridge** network. It supplies services and
node1, plus the already configured DNS primary/secondary pair. Services and
node1 each allocate 8 GiB/four vCPUs; DNS guests each allocate 1 GiB/one vCPU.
Plan for 18 GiB guest memory plus host/build overhead, not the earlier 16 GiB
test watcher cap. Lead assigns an adequate bounded memory/CPU budget and avoids
overlapping heavy builds; a CPU quota may cap scheduling without changing guest
contracts. Do not silently disable DNS or lower guest memory to fit a cap.

Observed preflight: br0 is up, `/dev/kvm` is accessible, the setuid bridge helper
is executable for the current user and `/etc/qemu/bridge.conf` permits br0.
Both interface names resolve to services `172.16.106.53`. A single ICMP probe
received no reply; this is not proof that the shared address is free. Only one
VPN-visible cluster may use these fixed addresses at once. Before start, the
lead/owner checks active provider/host ownership and process/address evidence
read-only, without accessing another session's mutable records. If occupied or
ambiguous, wait/refer; never stop the foreign cluster or use `--force`.
React requires bridge networking in this provider, so local mode is not an
equivalent fallback for the requested two-interface test.

Existing `newWebui.enable=true`, all plugins and distinct domains are sufficient:

- PHP: `https://webui.aitherdev.int.vpsfree.cz/`.
- React: `https://newadmin.aitherdev.int.vpsfree.cz/`.
- API: `https://api.aitherdev.int.vpsfree.cz/`, version 7.0.
- OAuth provider: `https://auth.aitherdev.int.vpsfree.cz/`; callback
  `https://newadmin.aitherdev.int.vpsfree.cz/oauth/callback`.

These are intended URLs, not yet a live-access claim. The services TLS frontend
routes React to its separate `newadmin` container nginx at loopback 18082 and
OAuth BFF at loopback 3001. The provider imports the selected WebUI NixOS module,
passes its matching frontend/BFF pair, config/session endpoints, exact API/OAuth
URLs, OAuth header and console origins. TLS to the auth service trusts the
cluster CA, including BFF `NODE_EXTRA_CA_CERTS`. Native OAuth seed creates a
separate nondefault WebUI client; PHP's default client/service is preserved.
No hand-written redirect URI, proxy, OAuth secret or host DNS change is needed.

Native first build generates the private `webui-credentials/` bundle (client
ID/secret/session secret) and mounts it at runtime, outside Nix source/store.
Keep it across starts/updates. BFF sessions persist separately at
`/var/lib/vpsadmin-webui/sessions`; incomplete/foreign secret or state ownership
must fail, not rotate or repair automatically. Legacy PHP serves the selected
worktree through its live symlink tree with packaged Composer dependencies;
React is immutable built output and needs a services update after source changes.

### Implementer3 execution package and gates

Own only session-local `work/<slug>/devcluster/` preparation/proof and native
state under `.dev-clusters/vpsadmin/clusters/<slug>/` after lead release. Shared
workspace config, provider sources, production configuration, foreign clusters,
canonical refs and application files are outside this package. Lead owns main
state/portal updates; never edit raw ownership/applied envelopes or private
lifecycle helpers. Expected implementation is an exact command/preflight receipt
and access handoff, not a source patch.

1. Prepare a compact receipt with selected runtime/provider paths, verified heads
   and clean status, configuration digest and nonsecret options, complete effective
   input graph/derivations, native stopped/no-pending state, bridge/access/collision
   observations, resource budget and remaining-check clearance. Preserve existing
   application verification and GC-root recovery evidence.
2. After lead release, use the public initial start command:
   `vpsadmin-devcluster start 2026-10-24-vpsadmin-haveapi-upgrade --topology single --network bridge`.
   Do not use `--existing` for this config-only stub, `--force`, maintenance or
   reset. There is no public build-only subcommand: native start builds then boots
   with ownership checks. Do not source/invoke private `build_config` to bypass
   preparation. Lead launches the activation operation or explicitly assigns its
   execution; a fresh utility monitors its exact process/log under the monitoring
   skill, without diagnosing, retrying or independently activating it. Preserve
   the chosen resource caps and native detached runner identity beyond startup.
3. Require actual command success, full boot/seed/refresh completion and native
   ready state. Record `result-config` path/digest, machine toplevels, selected
   source labels, applied-envelope proof and per-guest current-system/closure
   identity. A selected build or ready file alone does not prove activation.
   Inspect API/server/client/generator runtime 0.30.2, PHP installed package,
   both frontend/BFF full build-info heads and dirty=false.
4. Verify TLS with the cluster CA, native URL routing, public React overview,
   anonymous `/config.json` and `/session.json`, legacy login page, BFF/service
   health and API response. Complete one test-member login/logout through each
   interface using the existing seeded account and actual cluster OAuth provider;
   confirm API7 resource reads, language switching and PHP/React coexistence.
   Tokens, cookies, passwords and secret files never enter logs/screenshots.
   Browser fixture passes alone do not prove this real attachment. Do not create
   a VPS or execute unrelated mutations merely to claim login readiness.
5. Handoff both live URLs and access prerequisites: internal/VPN DNS reachability,
   cluster CA trust/fingerprint and seeded account names. Direct the user to the
   portal's native secret fields/local native account output for passwords; keep
   credentials out of committed tracking. Leave the ready cluster available for
   the requested manual testing. Do not stop, reset, archive, delete or schedule
   cleanup because the handoff is complete.

### Roots, interruption and recovery

The native provider roots `result-config` while in use and registers indirect
host roots for boot/copy payloads (kernel/initrd/toplevel, QEMU/virtiofs, image/
squashfs and store-backed shares/helpers). JSON alone is not a transitive Nix
root. Applied/maintenance config and payload roots survive interruption and
ordinary stop; guest boot proof includes exact current-system, closure validity
and guest GC roots. Existing retained disks need no source-image rebuild, while
fresh creation requires its image. Record native `gcroots <slug>` plus exact
selected payload/root evidence; do not run cleanup or host GC. The source
worktrees and private runtime credentials are external to those store roots and
must remain available for this cluster.

On failure, inspect the exact owned command, runner PID/socket and pending/applied
selection before any retry. A build can publish `result-config` before a root
registration failure; retain that identity and rerun only the supported native
operation after reconciliation. No success claim from build selection alone.
Do not reset disks, rotate credentials, replace the applied envelope or invoke
maintenance recovery without positive residency evidence and a new lead brief.
Native stop, if later explicitly requested for this cluster, preserves disks,
credentials and sessions; reset is a separate destructive decision. Preserve
original source/lock/runtime receipts for a compatible supported services update
or rollback. Cluster launch does not authorize physical-host deployment or
default-branch integration, and physical-machine claim rules remain separate.

## 2026-10-26 C mobile transaction expansion: controlled base comparison

This is a bounded verification investigation owned by implementer1, with design
and disposition routed through architect0/lead. No application, fixture, dependency,
ref or cluster change is authorized by this brief. The user-requested cluster
remains package E/implementer3; existing R1/R2 acceptance evidence is unchanged.
Session/current and both environment values were reverified; the live roster
retains implementer1 ready with workspace-write access and its saved settings.

### Observed boundary and limits

The current exact WebUI head `f10d3d48c4f21cc39187c3667ffffd9952404c11` has
60/62 passing cases in the fresh rooted full run: desktop 31/31, mobile 29/31.
Both failures are the user/admin cases in
`e2e/specs/app/action_state_detail_page.spec.ts:60`, at the normal click on
`action_state.detail.tx.toggle.7001` at line 129. Original command, JSON and
artifacts remain under `package-c/0.30.2/browser-full-rooted-*`; do not overwrite
them or turn the result into a pass by combining separate runs.

Read-only trace inspection independently confirms Playwright 1.61.0, Pixel 5
393 x 727, scale 2.75, mobile/touch true, en-US/light and a visible, enabled,
stable expand button. After automatic scrolling, the progress-bar div,
CardBody `p-4`, or outer `space-y-6` intercepts its pointer events until the
90-second timeout. The user screenshot shows horizontally displaced content
and a wide blank region. This identifies hit testing/overflow as the first
observed failing boundary, not its exact cause. The transaction data and target
already exist; no transport/auth/response error is established by these failures.

Against exact base `5a2d2bdc3ad7a827038f877d75959916528db844`, the spec,
ActionStateTransactionsTable, ActionStateDetailPage, Table, Card, Playwright
configuration/wrappers and flake.nix/flake.lock are byte-identical. The table has
an overflow-x-auto wrapper, minWidth=lg, and a last-column expand button. All
existing package-lock entries are unchanged; only the root dependency addition,
haveapi-client 0.30.2 and xmlhttprequest 1.8.0 are new. The HaveAPI fixture DID
change: a baseline run must use its own original fixtures and custom client.
Source equality does not itself prove a preexisting failure.

### Minimal execution package

Own only a new `package-c/0.30.2/mobile-base-comparison/` directory for source
archives, runner scripts, logs and artifacts. Do not checkout/reset the current
worktree, borrow an old session, edit tracked files, share writable node_modules,
replace roots or rebuild/recover the FHS runtime. No production API is involved.
Read current workspace verification/Git procedures, local AGENTS and verification
guide, and the monitor skill before execution. Lead reports C capacity available
for a later bounded parent fallback; confirm its execution release, preserve A's
active watcher, and use the explicitly authorized parent fallback only while that
utility remains unavailable, with bounded output/progress.

1. Export the COMPLETE base Git tree with `git archive` at the full base SHA
   into a new session-owned `base-source/` directory (no new Git worktree/ref).
   Record commit/tree, archive SHA-256 and a tracked-source manifest. Include
   original app, CSS, fixture imports, config and lockfiles. Do not overlay the
   current fixture or client. Verify source bytes before/after execution.
2. Use an independent `npm ci` against that base lock under the SAME locked Nix
   Node 24.21.0/npm 11.19.0 environment. Use an explicit flake path/reference:
   this Gitless archive lives beneath workspace Git, so implicit flake discovery
   must not select the coordination repository. Base/current flake bytes are
   identical; the existing exact pinned development environment can be reused
   with the working directory explicitly set to base-source. Enter that environment
   before installing dependencies rather than importing node_modules into Nix.
   No npm install/update, browser install, lock refresh, dependency upgrade or BFF
   build is needed. Verify the installed lock graph, Playwright version and app
   resolution paths point to this base archive.
3. Reuse the registered `fhs-gc-root/bin/package-c-playwright-fhs` and current
   185-path rooted closure from the successful launch of the full run. Require
   current rootfs NAR `sha256-Faq97Z93sfvQBWCNJ/EX5jic/sqAG5EaMPXqyh3CjhQ=`,
   Chromium SHA-256 `670ba079b75107746ba41abad131180a31a7c7219aa1bd4061fb471f4535d541`
   and ffmpeg SHA-256 `460d44f3416005662f528d4b92e7b94ace924e8a0288106d3803b73c56eaadc8`.
   Keep browser revisions Chromium 1228/ffmpeg 1011 and the existing roots.
   Recheck port 52847 is free; use the same loopback URL and CI/env exclusions
   from `browser-full-rooted-command.sh`. Keep the assigned CPUs 60-63, nice 5,
   Nix cores 2 and resource envelope unless lead coordinates a different budget.
4. List selection first, then launch exactly these two mobile cases once:

   ```sh
   node scripts/playwright.mjs test \
     e2e/specs/app/action_state_detail_page.spec.ts \
     --project=mobile-chrome \
     --grep 'shows related transactions and expandable payloads for (user|admin)$' \
     --workers=2 --retries=0 --reporter=list,json
   ```

   Add separate absolute JSON/output destinations under this comparison and
   retain ordinary failed traces/screenshots/video. Preserve the original
   90-second timeout and device/context options. The initial command is the
   base app plus base fixtures; it is not the current app loading base data.
   A title list must contain exactly user and admin, with no skips/extra cases.
   No force click, tap substitution, evaluated click, extra scroll, selector
   replacement, retries, sleeps, timeout increase or UI mechanism change.
5. Retain exit/status/duration, both failure boundaries or successful expansion
   assertions, request/console error summaries, trace hashes, environment/source
   manifests and before/after runtime closure proof. Reconcile only the owned
   runner/Vite/browser processes and free port; keep roots and evidence intact.
   These are synthetic browser checks, not live cluster or physical-device proof.

### Decision after evidence

- If BOTH base cases reproduce the same line-129 hit-test/scroll interception
  after transaction data loads under the verified identical runtime, classify
  this specific failure as reproducible before the HaveAPI upgrade. Recommend
  lead disposition as a documented preexisting mobile layout residual, with a
  separate narrowly scoped fix if desired. Keep 60/62 as the current full-run
  result; do not claim a clean browser gate or automatically approve release.
- If base passes, fails earlier, or differs by role/signature, the result is
  inconclusive for a preexisting layout defect. Return artifacts to lead before
  broader work. The next bounded candidate would be the same two-case selection
  against an exact current-source archive with its own lock/fixtures and fresh
  cache, to distinguish full-suite/order effects from an upgrade boundary. A
  source/fixture delta or diagnostic instrumentation requires a new brief.
- Do not infer a successful retry resolves the failure. Compare rendered text,
  table/scroll dimensions and actual hit-test blockers only after the baseline
  result; investigate transport differences only if the captured data/request
  boundary supplies evidence. No speculative layout patch is part of this package.

There are no schema, persistent-state, service-protocol, dependency or deployment
changes and no rollback action. This experiment cannot authorize merging,
production rollout or cluster startup. Lead owns final acceptance and any scope
decision; package E may continue preparation independently.

### Completed base comparison and architect disposition

Inspected implementer1's `package-c/0.30.2/mobile-base-comparison/receipt.md`,
`base-current-trace-comparison.json`, `reconciliation.json` and
`artifacts-sha256.json`. The complete base tree
`cc70705158813536e017afa99de593aa8fd97172` at 5a2d2bdc... used its original
2364 tracked files, fixtures and independent 407-entry npm install. Both cases
failed at the same line-129 normal click (base 0/2, exit 1, 194.004 seconds).
Both roles loaded transaction 7001 and had equal base/current device/context,
layout-snapshot viewport, unique click coordinates, scroll geometry and
progress-bar/CardBody/space-y-6 interceptor sets. Relevant API fixture reads
returned 200. Source, browser binaries, all 185 runtime paths and roots stayed
unchanged; owned processes and port were reconciled.

This is sufficient evidence that these TWO specific mobile expansion failures
are reproducible before the HaveAPI upgrade under the same selected browser
runtime. Recommend carrying them as an explicitly documented preexisting
mobile interaction residual, outside this upgrade's implementation scope, and
allowing HaveAPI-scope acceptance and the requested development-cluster testing
once lead accepts that residual and all other gates pass. Do not silently add
a layout feature/fix or run more comparison cases to make this batch green.
Desktop transaction expansion passed in the current full run; mobile users may
be unable to expand these inline transaction payloads in the tested conditions.

The current full browser result remains **60/62**, with these two failures;
the suite is not a clean pass. This comparison neither identifies the exact CSS
or browser hit-testing mechanism nor proves behavior on physical devices or the
live cluster. It does not exclude other upgrade regressions. Keep the failed
tests and all original evidence. A later fix needs a separate scoped decision,
with normal interaction tests and independent review; no force click or test
weakening is acceptable. Lead owns the actual residual/acceptance disposition;
this recommendation supplies no merge, production or startup authorization.

### E clarification: foreign physical-host hold and native QEMU startup

Rechecked exact session/environment and read the currently selected
`workspace-host coordination guide`, workspace deployment/coordination
procedures, installed catalog, cluster dispatch and provider start/ownership
code. Runtime is now
`/nix/store/fa7zlb2z311w9p8y9wygaqxpmq086s9b-dev-workspace-0.2.0`, provider
`/nix/store/7vrkd2yg349dsqq3hwmwpmcw86nrvq6s-vpsfree-dev-workspace-tools-0.1.0`.
Use implementer3's `devcluster/preflight.md` and additive `runtime-refresh/`
receipts for this generation; earlier runtime paths remain historical evidence.

A fresh public `dev-session coordination status` for this session shows no own
claims, reservations or jobs, and one foreign held `vpsfree:aitherdev`
reservation. No foreign mutable state was opened and no reservation was changed.
The catalog identifies that machine with confctl selector
`cz.vpsfree/machines/aitherdev` and also selects it as `profileMachine`.

The selected coordination contract reserves physical machines **for deployment**;
it explicitly requires a machine claim for `workspace-host switch` profile
activation. It does not grant a host-wide exclusion on ordinary feature builds,
tests or session-owned QEMU execution. Installed cluster dispatch
(`libexec/.workspace-host-wrapped`, `dispatch_cluster`) uses the current-generation
shared transition lock and selected registered provider. The provider's ordinary
`start_cluster`/`devcluster_with_lifecycle_lock` checks active session, native
state/socket/runner identity, pending lifecycle/maintenance state and per-cluster
locking, then builds and starts the selected guest runner. This path neither
switches the host system/profile nor acquires a physical-machine deployment claim.
Using the already installed bridge helper for the cluster's ephemeral networking
does not install or change that host policy.

**Recommendation: the reported foreign physical-host hold is not by itself an
ownership blocker for package E's ordinary authorized native start.** Do not
request/transfer/release that foreign reservation or invent a machine claim for
the guests. No actual ownership conflict was established by this assessment.
This conclusion follows both the policy's deployment scope and the native
operation contract; absence of a tool guard alone would not waive a policy.

Native refusals and operational checks remain binding: recheck current generation,
session tuple/pending state, selected sources/graph, accepted 32 GiB/12 CPU
resource budget, and absence of another active fixed-address cluster immediately
before lead-released start. The physical-host hold is not a development-IP lease
or proof of exclusive address availability. A real conflicting guest/address,
unsafe native ownership, unfinished operation or incompatible package transition
is a blocker. If starting required a host configuration/bridge-policy change,
workspace profile switch or host service deployment, that would be a different
operation requiring its own authorization and machine ownership; the present
package requires none. No startup, claim, deployment, runtime test or host-policy
mutation was performed by this assessment.

## 2026-10-26 A publication after upstream dependency advance

Read the publication stop receipts under `package-a-0.30.2/publication/`, current
repository instructions and verification procedures, and the complete Git diff
and ancestry of observed master advance
`b82eeca50cd4dd7bd76728685c7de8aad66e7ba5..898e2881e8230d24fb06baee1c58737ae55e0009`.
The inspected target is a linear two-commit successor; the exact verified
feature remains clean at `70a2ed54b98d0c2f359a9cc4484452a257a9807b`, with its two
reviewed commits above b82eeca50.... No fetch, ref/source mutation, merge trial,
test/build, claim or push was performed by this investigation.

### Actual upstream delta and consumer boundary

The FULL target delta is four generated files, 12 insertions/12 deletions:

| Commit | Files | Exact change |
| --- | --- | --- |
| `abc478cf7625676f8595e61a34d01f5532f69d3f` | `packages/api/Gemfile.lock`, `packages/api/gemset.nix` | Faraday 2.15.0 to 2.15.1; Nix gem hash changes from `1zsz6ghll6hqsrnbfxagvln58nw4zvyfjygnnjhi7nby33qfzq1v` to `13r8mjqk8slscc8rxfhfrqglks131sb78ay4dklcafd7xm6ia247`. |
| `898e2881e8230d24fb06baee1c58737ae55e0009` | `webui/composer.lock`, `webui/php-packages.nix` | Guzzle 7.16.0 to 7.16.1; Git/dist ref `ffb62ec787050ae4fa9449cdd6b80335db69bda2` to `81755d989b3007ca7f88a069857553cd08e7dc2e`, matching Nix zip URL/hash and Composer support/time metadata. |

All four paths overlap the feature inventory, but the feature edits the separate
HaveAPI dependency entries and additions. Upstream does not change HaveAPI,
dependency requirements, application source, API schemas, database migrations,
CI/spec selection, Nix flake inputs, options, seeds, daemon protocols or state
formats. Upstream retains Ruby HaveAPI 0.29.12 and PHP 0.29.6, so it does not
already incorporate this upgrade. File overlap is real; whole-file ours/theirs
resolution would lose either the new upstream dependency or the HaveAPI update.
Textual reconciliation appears bounded to preserving both sets of entries; no
automatic merge/conflict-free claim has been tested.

Faraday is used transitively by `rack-oauth2` and `json-jwt`; Guzzle by
`league/oauth2-client`, which PHP HaveAPI uses. Their HTTP/auth consumers make
these actual package-closure changes, not runtime-equivalent metadata. Their
requirements remain satisfied. This investigation has not audited either new
dependency's upstream source/release rationale and does not label the changes
security fixes, harmless, or behaviorally equivalent merely from patch versions.
No application-level migration or required coordinated rollout is introduced by
the repository delta; a later refreshed closure still needs affected verification.

### Recommended immediate disposition

**Publish the unchanged reviewed 70a2ed54b... to this session's own feature
branch; defer rebase until integration preparation.** This is the shortest valid
path and preserves the exact PHP-test, package/runtime and package-E source
bindings. Fresh target inspection is complete; the workspace rule requires
rebasing before push *when appropriate*, not replacing a verified feature
baseline for every independent publication. Neither new upstream commit is a
prerequisite of the requested HaveAPI 0.30.2 behavior, and publishing the feature
does not revert master or change any running consumer.

Lead may release implementer2's stopped publication with the explicit changed-
target disposition. Use a normal SSH push with declared pre-push hooks to
`refs/heads/2026-10-24-vpsadmin-haveapi-upgrade`, currently reported absent;
recheck exact local head/cleanliness/lock hashes, remote own-ref state and default
identity first. If a remote feature ref unexpectedly exists or inputs change,
reconcile rather than force/rewrite. Capture remote exact-head proof and ordinary
CI evidence within the existing publication brief. No merge claim or default
push is involved. Preserve ignored `api/Gemfile.lock` and ongoing verification.

Record original review base b82eeca50..., feature head 70a2ed54b..., observed
target 898e2881..., and **published for review/testing; integration refresh
pending**. This is not a declaration that the branch can fast-forward current
master or is merge-ready. No integration approval exists. Existing exact-70a
checks and E preparations remain valid for their original inputs, without a
new full verification run merely for publication. Newly triggered CI can
resolve its ignored development lock separately: retain its effective lock
hash/versions, and do not relabel differing resolution as the prior local run.

### Deferred refresh package, if integration is later requested

Implementer0 owns dependency reconciliation, coordinated with implementer2's
Git/publication ownership. First finish/reconcile exact-70a checks and any
cluster consumption; preserve old reviewed base/head and deployment receipts.
Refresh onto the freshly inspected target then, not a guessed future master.
Keep both logical feature commits/authorship and the complete final HaveAPI
0.30.2 declaration/generated-pin stream. Preserve upstream Faraday/Guzzle
entries and paired generated hashes; no unrelated dependency update, SDK
regeneration, provider change or schema edit belongs to this refresh. Do not
hand-refresh only a constraint or select one whole lockfile side. Use the owning
generation procedure if reconciliation requires regeneration, with exact locks
and bounded semantic-diff review.

Quick acceptance: full old/new base-to-head diff and range-diff/patch mapping;
same intended 25-path feature scope; lock-to-gemset/Composer-to-Nix consistency;
HaveAPI server/client/generators/PHP remain exact 0.30.2; upstream pins retained;
Composer validity, focused dependency loading/checks and declared hooks. Record
no migrations in both ranges, plus any actual use/deployment of the old head.
Independent review applies the appropriate mechanical/equivalence policy and
must explicitly assess final whole-branch history/migration lineage; changed
runtime inputs do not inherit a blanket exact-head test pass.

After committed quick checks/review, affected longer verification is the new
packaged API/services-up closure and auth consumers, plus legacy PHP package
regression/browser login/API interactions with its new Guzzle graph. Use actual
effective locks in full/core auth-spec runs where Faraday is loaded. A complete
unrelated API/browser campaign or repeating all 26 emitted SDK compilations is
not required solely by this four-file advance; broaden only for new differences,
failures or reviewer findings. These are future check boundaries, not commands
released now. If a live E cluster later selects the refreshed head, rebuild and
verify its affected services/runtime before claiming that successor deployed;
retaining the original exact-70a cluster for user testing is a separate valid
state. Preserve compatible old closure/inputs for recovery rather than swapping
locks in place, and retain old/new lineage instead of calling a rebased
nonancestor commit literally merged.

## 2026-10-26 E guest-proof defect and isolated A integration refresh

### E: observed defect, current safety evidence and acceptance boundary

This assessment used E3's saved `devcluster/runtime-verification/guest-residency.json`
and `guest-residency-diagnostic.json`, activation result, and exact installed
source. No guest polling, source/ref edit, root write, native recovery, build,
test, stop or reset was performed. Current runtime is
`/nix/store/w6j9bzbv7m04h7snndb5bs9jj39jd2kc-dev-workspace-0.2.0`; selected
provider is `/nix/store/q19s1vj5yn00jq46n4gs7g10z5f76y68-vpsfree-dev-workspace-tools-0.1.0`.
Within its `share/vpsfree-dev-workspace/dev-clusters/vpsadmin/` directory,
`bin/devcluster` SHA-256 is
`8fc86cd540785130f5fc61810a67e7f837dbbd7ebba8e8b196172777679f887b`, and
`lib/maintenance.rb` SHA-256 is
`8f205b0c64ca4fb5d0b46203fb126cfac8668c08aad219416f9c1875b92b6ef4`.

The installed `prove_full_applied_boot` (line 1714) feeds sorted machine names
to a `while read` loop through stdin. Its `prove_machine_selection` calls SSH
without `-n`, StdinNull or stdin redirection (line 1711); the selected ssh_opts
also supplies none. SSH can consume the remaining machine-name input. The loop
has no independent coverage/count check before `applied-finish-boot`.
`maintenance.rb:542` then assigns `prior_boot` provenance to every configured
machine and clears pending, trusting the caller's full-proof statement. This is
a concrete all-guest proof defect. The exact syscall/input consumption was not
traced, but it explains the observed first-sorted `dns-primary` root only;
the code permits incomplete guest checks to produce a complete envelope.

E3 independently checked all four selected guests. Every `/run/current-system`
matches its selected toplevel and each queried closure is valid. Saved Nix root
queries show `/nix/var/nix/profiles/system-1-link` referencing that exact system
on **all four**, plus current/booted-system roots. The provider-specific
`vpsadmin-devcluster-applied-<slug>-<machine>` root exists only on dns-primary;
diagnostics confirm its absence on dns-secondary, node1 and services. These
observations and the original native exit 0/pending=null claim must coexist in
the record; do not repair history or describe the native certificate as complete.

**Recommendation: these independent per-guest closure and standard retained
system-root proofs support qualified acceptance of the CURRENT running cluster
for the user's manual UI testing**, once E3's separate real login/access checks
are satisfied. Missing provider-specific roots do not mean these same closures
are currently unrooted: the recorded system-profile roots retain them and their
transitive store dependencies. No immediate missing-closure/GC exposure has been
demonstrated. Leave the running cluster and live testing intact. This conclusion
is limited to the exact observed systems and roots, not arbitrary future profile
pruning, updates, stopped-disk recovery or cold restart.

The residual is a provider residency/recovery guarantee defect: the envelope can
overstate proof and relies on roots it did not actually establish for three
guests. It is not evidence of a HaveAPI source/API/auth regression. It should
not block HaveAPI merge correctness absent a concrete consumer delta; preserve
it as a separate E limitation rather than expanding this upgrade into a provider
project. Do not use native ready/pending=null alone for later recovery decisions,
delete/prune roots or profiles, or stop/reset the cluster to demonstrate recovery.
Host payload roots and guest roots remain distinct obligations.

### Minimum remedy proposal, not assigned execution

No repair is required merely to continue qualified current manual testing.
The installed public CLI has no proof-only all-guest command. `update all` would
rebuild/copy/activate services and is disproportionate for a missing-root proof;
stop/start would disrupt testing and still use the defective loop.

If lead separately assigns restoring the intended additional retention, the
smallest supported access path is the public `vpsadmin-devcluster ssh` command,
one explicit guest at a time: first revalidate exact session/runner/selected
system and closure, then add ONLY the exact expected provider root to that
already resident toplevel using Nix's normal root registration (substitution
disabled), and verify its symlink and `nix-store --query --roots` registration.
Bind four explicit results to the saved selection; refuse a mismatching existing
root/system, never retarget it. This is a proposed guest mutation requiring a
separate lead brief, not an operation authorized or performed here. Record it as
supplemental independently verified retention; do not rewrite the applied
envelope or pretend the original full-boot claim was sound. A symlink alone is
not registration proof. No provider/private lifecycle helper is needed for this
bounded operational mitigation.

A durable source fix belongs to a separately assigned bounded package in
`vpsfree-dev-workspace`, not vpsadmin/HaveAPI: isolate this noninteractive proof
SSH from stdin and make full-machine coverage explicit before finish. Test the
actual shell orchestration with a fake SSH that deliberately drains stdin,
multiple sorted guests and first/middle/last failure; every guest must be visited
exactly once and no incomplete/failed set may finish/clear pending. Do not change
generic interactive ssh behavior, applied schema or unrelated maintenance flows.
Provider publication/profile deployment and live reproof remain separate future
decisions; none is needed to claim the existing independent current-state proof.

### A: prepare a successor without changing the live 70a checkout

The prior four-file Faraday/Guzzle refresh analysis remains authoritative.
Merge-readiness preparation can proceed independently of E; user asking about
readiness supplies no default-branch integration approval. Preserve the live
`worktrees/<slug>/vpsadmin` path, checked-out feature ref, exact
`70a2ed54b98d0c2f359a9cc4484452a257a9807b` tree and ignored effective lock/config
bytes. PHP serves that worktree live, and the provider automatically selects its
name: even a harmless rebase there would change the user's active source/input
binding. Do not reset, switch, regenerate dependencies in, or repoint that path.

After lead dispatch, prepare a SECOND linked checkout from the same canonical
`repos/vpsadmin.git`, e.g. `worktrees/<slug>/vpsadmin-refresh`, on a distinct
session-owned successor branch `2026-10-24-vpsadmin-haveapi-upgrade-refresh`.
Lead records the same-repository temporary worktree/branch and explicit comparison
without changing the existing native `vpsadmin` registration or inventing another
canonical clone. Keep the original local/published feature ref and live worktree.
Use ordinary feature-work Git operations, without a repository merge claim.

At the freshly verified target (currently
`898e2881e8230d24fb06baee1c58737ae55e0009`), replay the two reviewed logical
commits in order (`44393c352fbd5e9247850ed8490f369999553d62`, then 70a2ed54b...),
preserving authorship and their intended division. This produces a successor
range without rewriting the active/published source. Keep new upstream Faraday
2.15.1/Guzzle 7.16.1 entries and all HaveAPI 0.30.2 declarations/generated pins;
resolve only bounded overlapping generated-file entries, never whole-file sides.
Record exact old/new base/head ranges, semantic lock delta, range-diff and patch
mapping, complete history and no-migration conclusion. If target advances again,
inspect the additional delta before assuming this package still applies.

Dependency setup, ignored generated locks, `.bundle`/`.gems`, Composer vendor,
test databases, build outputs and GC roots must belong to the new checkout or
its new receipt directory. Do not symlink mutable caches/config into the live
checkout or copy private/ignored live configuration. Keep independent disposable
test state and existing resource caps; shared read-only immutable store outputs
may be reused only with exact input proof. Do not call native cluster start/update
from the refresh package or substitute its worktree for E.

Use the prior quick/review/affected-longer-check package: semantic lock/generated
consistency, exact HaveAPI pins, focused loading/hooks; committed final-range
review/equivalence assessment; affected packaged services/auth and PHP regressions
with actual effective dependency evidence. Do not repeat unrelated full campaigns
or emitted-SDK compilation absent new changes/failures. Preserve original tests
and live-cluster receipts as exact-70a evidence rather than relabeling them as
successor results. Final CI is still a separate pending gate, not a failure.

Lead decides the final registered/published successor after review/checks; preserve
the old ref/worktree while it is live, and do not rewrite its published head as
part of preparation. Before future integration, register/capture the exact final
comparison through supported tooling while retaining the active cluster's old
source mapping. No stop, guest update, production deployment, default merge or
old-ref deletion follows automatically from preparing or approving the successor.

## 2026-10-26 F: fix provider SSH stdin and full-guest certification

User's direct “so fix it” authorizes a durable source fix in
`vpsfree-dev-workspace`. It does not authorize integration, host deployment,
workspace package selection, current guest-root repair, applied-envelope edits,
stop/reset or update-all. Implementer1 is the intended source owner, ready with
saved workspace-write access; lead supplies worktree/execution release. Architect
has made no source/ref changes or run tests/builds. The live 70a/f10 cluster and
the preceding isolated A-refresh design remain unchanged.

### Current source and minimum file boundary

Read canonical repository AGENTS/README, provider contract, existing command-test
seams and flake check definitions. Read-only SSH `ls-remote --symref` confirms
canonical `git@github.com:vpsfreecz/dev-workspace.git` master at
`767dfd587e346168e1443e65ccdb67ce748f3fe3`, matching locally available origin/master.
All 33 tracked `dev-clusters/` files were compared against installed q19s1vj:
30 are byte-identical and three differ only in substituted shebangs. There is
no upstream source fix to adopt. Nine additional installed files are accounted
for by `nix/organization-tools.nix`: runtime contract, two site default configs
and six copied shared assets. No site defaults or secrets need copying into
the source change. This comparison covers the full native provider source tree,
not a claim that the generic runtime or whole package input graph is identical.

Prepare only our own `worktrees/<slug>/vpsfree-dev-workspace` feature worktree,
from the rechecked canonical master, through lead-coordinated normal registration.
No foreign worktree/ref or installed store path is an edit target. Expected files:

- `dev-clusters/vpsadmin/bin/devcluster`: `prove_machine_selection` and
  `prove_full_applied_boot` only, plus a tightly local helper if needed.
- `test/devcluster_commands_test.rb`: extend existing fake-command/SSH and
  selection-proof harness; it already drives the real public launcher against
  disposable workspace/state and records applied state and proof events.
- `dev-clusters/vpsadmin/README.md`: short full-boot-proof/failure-semantics update
  in the existing retained-boot section. No site names or this session's paths.

No new public command/framework, dependency/flake pin, CI workflow, generic
interactive ssh behavior, vpsAdminOS provider, runtime lifecycle, applied schema
or transition-policy change is expected. `lib/maintenance.rb` is a compatibility
reference, not an expected edit: it can retain the trusted internal finish
interface when the shell establishes complete success first. Refer any required
boundary expansion to lead before editing it.

### Required behavior and invariants

1. The noninteractive guest selection-proof SSH must not read the caller's stdin.
   Use `ssh -n` or explicit `/dev/null` redirection at this proof call. Do not
   change `ssh_cmd`/global options, because other commands intentionally stream
   scripts/input or support an interactive shell.
2. Enumerate the expected machine set from the selected immutable config with
   explicit producer-status checks. Iterate without exposing its enumeration
   stream to child commands (e.g. an array or dedicated read descriptor).
   Record a guest as proved only after its current-system/closure/init/root
   command succeeds. Before `applied-finish-boot`, explicitly require successful
   coverage of the COMPLETE expected machine set, with no missing or duplicate
   guest. A count alone based on an already truncated enumeration is insufficient.
3. Failed enumeration, incomplete coverage or any guest proof failure returns
   nonzero and never calls finish. Keep the native pending record, earlier roots,
   previous provenance and owned runner state under their existing rules; do not
   roll back/stop guests, manufacture missing proofs, or clear pending to recover.
4. Preserve root paths, bounded SSH timeout, exact toplevel/closure checks, guest
   init requirement, host roots, refresh-before-certification ordering and native
   ownership/lifecycle locks. Fresh and copied-config boot share the corrected
   function; per-target update still verifies/promotes only its selected target.
   Existing schema 1/policy 3 and on-disk formats stay unchanged.

### Meaningful focused regression package

Use existing `DevclusterCommandsTest` fixtures, never the registered live cluster.
Add four distinct configured guests (dns-primary, dns-secondary, node1, services)
and assert identities/operations, not merely a success count. The fake selection-
proof SSH should attempt to drain inherited stdin as real SSH does; when `-n`
is selected it must model its null input. If redirection is selected it should
observe EOF. Keep other fake SSH paths' stdin behavior intact. Exercise the
actual shell loop and public start boundary, not a copied implementation.

- Regression success: with a draining SSH, each of the four intended guests
  reaches real fixture selection-proof exactly once; verify per-guest query,
  validity and root operations, all four final provenance keys, and pending=nil
  only after the last success. Demonstrate this catches the predecessor defect.
- Failure: inject a middle guest failure (closure/query or root command), require
  nonzero status, later guests unproved, boot pending retained and no fabricated
  complete provenance. Parameterizing first/last failures is cheap if the same
  harness supports it; no broad matrix is required.
- Incomplete coverage: drive a deliberately truncated/skipped enumeration via the
  existing command-stub seam while the authoritative config still contains four
  guests; require refusal before finish. Also cover a failed enumeration producer
  if its exit could otherwise be masked by array/process substitution. These
  cases must exercise the coverage guard independently of the SSH isolation fix.
- Keep existing per-target update closure/root refusal and successful promotion,
  retained-boot layout and maintenance state tests passing. Do not replace actual
  proof behavior with unconditional success just to add a loop-count assertion.

All fixture paths, sockets, state and subprocesses are disposable and isolated.
No live Nix GC, guest SSH, profile/root mutation or selected package change is
part of verification. Source preparation does not retroactively repair the
running cluster's certificate; the preceding qualified-current-testing conclusion
and independent four-guest evidence remain intact.

### Checks, review, compatibility and delivery

Use the repository's locked Nix inputs/tool environment and `testEnvironment`
contract from flake.nix for focused Ruby commands; do not add a new development
shell or dependency to solve ambient-tool absence. Quick checks: launcher shell
syntax, focused `ruby test/devcluster_commands_test.rb`, relevant existing
`devcluster_maintenance_test.rb` and `devcluster_store_roots_test.rb` assertions,
diff/format consistency and discovered declared hooks. No tracked hook framework
was found in the inspected root inventory; owner must still check actual worktree
hook configuration and preserve required hooks. Read commits procedure, verify
identity and commit via a message file. Keep source/tests/docs one functional
fix, with original failure and limitations in session evidence.

Commit all intended changes and pass focused checks, then lead commissions
mandatory independent final review of exact complete branch/history and the
failure/pending-state boundary. Only after review run repository-required
`nix flake check --print-build-logs`, using a fresh permitted watcher for long or
uncertain verification, and the existing installed `nix run .#devcluster-check`
package/runner smoke when assessing installed packaging. That smoke uses temporary
configuration, not VMs. Do not launch the live cluster or host-migration VM.
Additional disposable boot integration is needed only if focused evidence/review
finds an uncovered path; a new full VM framework is outside this fix.

Acceptance: every configured guest is actually proved exactly once before a
complete envelope is published; missing/failed proof leaves the original pending
operation; stdin is isolated without breaking script/interactive commands; locks,
formats, pins, rollback and recovery contracts unchanged; quick checks, committed
independent review and affected package checks pass. Publish only the authorized
feature branch under normal rules, not a default merge or package deployment.
There is no data/schema migration or new state. Reverting source restores the
known bug, so rollback is not a validation strategy; preserve prior evidence and
do not use a predecessor package to evade refusal. Selecting a fixed installed
package and deciding how to reconcile existing certificates remain separate
explicit operations, never automatic consequences of this source fix.
