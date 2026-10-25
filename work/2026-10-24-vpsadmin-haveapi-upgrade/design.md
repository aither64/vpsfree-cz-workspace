# HaveAPI 0.30.1 adoption design

Design owner: architect0. Status: all four packages ready for lead assignment;
SDK compatibility is an explicit package B acceptance gate. Initial tracking
commit: `b6001eb8`. No project source changes or external writes were made by the
architect. The lead owns assignment, shared Git serialization, final prose,
review and publication.

Current revision: the [2026-10-25 registry addendum](#2026-10-25-addendum-rust-registry-adoption)
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
