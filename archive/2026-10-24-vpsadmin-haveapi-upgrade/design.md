# HaveAPI adoption design — current release 0.31.1

New authorized patch milestone: [0.31.2 adoption](#2026-10-28-authorized-0312-patch-adoption)
is in preparation. The 0.31.1 deployment described below remains the running
baseline until the new committed sources, review and affected checks pass.

Design owner: architect0. Current status, 2026-10-28: released **HaveAPI 0.31.1**
is adopted, reviewed and checked; the authorized disposable cluster redeployment
is accepted for qualified manual use, and both final KB articles are staged.
The lead owns final acceptance, tracking and publication. Initial tracking commit:
`b6001eb8`. See [current state and access details](state.md) and the
[0.31.1 adoption section](#2026-10-27-authorized-0311-adoption-gates).

API documentation now includes Go, Rust and generated TypeScript profiles.
The generated `vpsadmin-typescript-client` SDK remains **0.1.1**, paired with
its supported **haveapi-client 0.30.2** runtime; generic application clients use
0.31.1. Rust uses the published registry client, without the historical Git pin.
[Release facts](package-0.31.1/release-facts.md) bind these distinct identities.

The released TypeScript remedy and actual consumer measurements close A31-R1:
qualified anonymous rendering measured 4.775s wall/4.772s CPU versus the retained
0.31.0 observation of 15.231s/15.218s. This is measured consumer evidence, not an
identical-condition benchmark claim; see the [accepted R1 proof](package-0.31.1/vpsadmin/R1-qualified-anonymous/receipt.md).
The former external-remedy gate is no longer open.

The subsequent user-reported Go token-auth documentation warning has a separate
[read-only diagnosis](go-auth-investigation.md): the upstream Go adapter rejects
equivalent String/Symbol query-parameter metadata. The SDK supports token auth;
no remediation or deployment change is included in that investigation.

E4's native packages are independently bound to exact reviewed React head e468
through the [complete source/input/output proof](package-c/0.31.1/native-provenance/receipt.md).
Actual application flows and documentation checks passed and were accepted;
the manual-use conditions are satisfied. Embedded native revision metadata
remains unavailable, so the clean-release metadata gate is not claimed. The
installed provider still lacks F's certificate fix: independent four-guest
system/closure/root proof supports present use, not a complete retained-boot
certificate or guaranteed future cold recovery. Default-branch integration and
production KB publication remain separately unauthorized.

The original scope and dated sections below are preserved as historical design
and decision evidence. This current summary and linked state supersede their
earlier version targets, readiness gates and operational status.

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

## 2026-10-27: HaveAPI 0.31.0 and generated TypeScript examples

This is a new user milestone replacing the pending 0.30 upgrade stream.
Packages A4+B4 and C4 below are ready for implementation by their assigned
owners. F remains a separate completed source fix. Preserve the original LIVE
70a/f10 worktrees, refs, ignored configuration/locks and running cluster, and
published vpsAdmin successor `2c6542941fde72c0ea7bb2991274981e98c5781c`.
Use isolated 0.31 successor worktrees; no live update, package switch, default
integration, protected PR74 rewrite or KB production write is authorized.

### Released contract and scope decision

HaveAPI tag `v0.31.0` peels to
`c9124da141adc258fbbaf67d4ec19ee3f8580849`. All five Ruby packages (`haveapi`,
`haveapi-client`, `haveapi-go-client`, `haveapi-rust-client`, new
`haveapi-typescript-client`) and generic npm/PHP/Python clients are published at
0.31.0. Implementer2 supplies compact registry/artifact receipts. Source inspection
confirms `servers/ruby` means the HaveAPI framework: its released
`TsGeneratedClient` already supplies `typescript-generated` panels. Therefore
configure the vpsAdmin consumer; no HaveAPI source change or new release is needed.

Register alongside existing API 7.0 Go/Rust profiles:
`typescript: { package_name: 'vpsadmin-typescript-client' }`.
Allowed additional keys are `package_version` (concrete SemVer), `snapshot_path`
(absolute saved snapshot), and `generator_version`. Omit these by default:
SDK version is selected by the user's package manager, the mounted structural
model supplies names, and generator version defaults to exact server version.
Registration loads `haveapi/typescript_client/documentation`; the matching gem
must be in the API bundle. Models remain private, built at mount, and samples
come from the current user's authorized description. No schema fetch, SDK
generation, compiler or registry call belongs in a documentation request.

The published generated SDK is **0.1.1**, API 7.0/protocol 2.0, source
`60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`, tarball SHA256
`9d262825d1dffb695eaace8029e3e7eb03a44338131602822907632945f566e8`.
It is ESM/ES2022 and re-exports `createClient`, as required by the renderer;
its documented convenience exports are `createVpsAdminClient` and
`createHaveApiExecutor`. It was generated with recorded 0.30.0-era sources,
not 0.31.0. The SDK's exact peer is `haveapi-client@0.30.2`; HaveAPI 0.31.0's
released TypeScript renderer explicitly emits that runtime version and offers
no runtime-version override. Lead accepts this supported pairing. All actual
vpsAdmin/React HaveAPI dependencies become 0.31.0; generated-SDK example
consumers use 0.30.2. Do not force incompatible peers, patch the renderer,
change the SDK or claim every example dependency is 0.31.0.

The generated SDK exposes vpsAdmin-specific resource/action/input/result types
from a saved API schema. Generic `haveapi-client` callback and async clients
discover resources dynamically; their TypeScript declarations describe that
generic API. Generated calls still delegate transport/authentication to the
generic async runtime. Use a versioned runtime base ending `/v7.0`, without
adding its constructor version option, for generated raw requests. Authentication
and server authorization remain the runtime/server's responsibility.

### A4+B4: one vpsAdmin execution owner, implementer0

Use new `vpsadmin-031` linked checkout/branch; retain 2c as the exact reconstruction
input. Fresh read-only remote master is `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7`:
since reviewed base 898e it adds `f3794d5fa` PHP dependency updates and `08c3bd7e3`
controlled schema-export tooling/docs. Recheck before setup and inspect this
small advance; preserve those upstream changes, do not execute/export schemas or
port tooling into this task. Reconstruct the two logical feature commits on the
fresh target: consolidated A dependency update directly to 0.31.0, then B Go/Rust/
generated-TypeScript documentation configuration. Preserve authorship and old/new
base/head mappings; no intermediate 0.30 pin commits in the new series. Protected
live/published original refs stay unchanged. Lead coordinates registration/push.

A files: `api/Gemfile`, `client/vpsadmin-client.gemspec`,
`download_mounter/Gemfile`, `plugins/outage_reports/utils/Gemfile`, generated
`packages/{api,client,download-mounter}/{Gemfile,Gemfile.lock,gemset.nix}` where
present, `webui/{composer.json,composer.lock,php-packages.nix}`, and both existing
`webui/public/js/haveapi-client.js` / `console_router/public/haveapi-client.js`.
Use the existing declaration convention `~> 0.31.0` plus exact generated 0.31.0
resolutions, PHP exact 0.31.0, and verified npm release bytes for both bundles.
Add `haveapi-typescript-client` beside Go/Rust in source/generated API Gemfiles.
Its only declared runtime dependency is Ruby `haveapi-client ~> 0.31.0`;
Go/Rust now require the same shared schema library. Keep libffi/pkg-config support
and unrelated upstream pins; use existing scoped metadata generation, not a new
generator/update framework. Report unavoidable transitive changes.

B files: `api/lib/vpsadmin/api.rb`, existing
`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`,
`docs/{README,api-client-examples}.md`, and `tests/suite/services-up.nix`.
Extend existing profile membership, generator version and initialization checks
to TypeScript; preserve Go/Rust and existing dynamic JS/TS panels. Keep API 6.0
unconfigured. Assert `createClient`, correct package/runtime/base URL and emitted
action calls; keep bounded string diagnostics. Extend existing member/anonymous
visibility and locale assertions to generated panels, with no private schema
diagnostics or privileged sample leakage. Update docs to distinguish generated
from dynamic TypeScript and explain the separate supported SDK/runtime pairing.
The existing spec remains in platform-config; no new CI partition is needed.

Quick batch: syntax/lint/hooks, exact dependency/metadata agreement and artifact
hashes, loaded server/client/all three generator identities, PHP load and equal
legacy bundles, focused `:documentation_profile` examples in core/full modes.
Add one small actual-renderer generated TypeScript initialization/action seam
using the mounted profile and authorized fixture description, not a second full
page campaign. Capture a few complete emitted programs (init, supported auth,
public action, one nested/path or nullable input if emitted) and compile against
the published SDK 0.1.1 + its supported npm runtime, strict NodeNext/ES2022.
Use existing sample-capture mechanisms. Do not replace programs with hand-written
equivalents or regenerate the SDK. If a real sample mismatches, report it before
adding snapshot overrides or upstream work.

After commits and independent final review, run the affected existing full/core
documentation spec and `services-up` with all three generators packaged. Reuse
the established admin/member/anonymous GET timing seam once against final 0.31
inputs to catch a TypeScript rendering regression; retain prior R1 evidence and
do not reopen its closed fix or invent new instrumentation. Authorization/locale
and completed role coverage must pass. Measure actual request cost before large
string diagnostics; an unexplained return to the previous tens-of-seconds cost
is a defect to report. Run affected API/auth/client/PHP checks required by the
final dependency delta and existing CI. No blanket 26-program SDK recompilation,
provider tests or new exhaustive browser/performance campaign is justified.

### C4: independent React successor, implementer1

Create a distinct session-owned `dev/` branch/worktree from preserved f10 content
on fresh main (currently still `5a2d2bdc3ad7a827038f877d75959916528db844`).
Consolidate the npm update stream directly to 0.31.0 while carrying the reviewed
adapter/takeover authorship and source mapping. Do not edit or repoint live f10,
the old pilot, PR74 head or unrelated refs. Keep protected publication decisions
with lead; final source review uses complete successor history and diff.

Own only root `package.json`, `package-lock.json`, `packages/frontend.nix`,
`packages/haveapi-client-provenance.json`, current HaveAPI/packaging design docs
and the dated work-log entry/index. Exact dependency `haveapi-client: "0.31.0"`;
regenerate lock/hash with pinned tooling, retaining unrelated/BFF/XHR versions.
The released JS source delta from 0.30.2 is the Client.Version constant; imports,
AsyncClient transport/auth and declaration source are unchanged. Verify release
artifact/provenance separately, without assuming identical build bytes.
No generated vpsAdmin SDK adoption or adapter rewrite belongs to React.

Quick batch: registry/package source checks, typecheck, focused actual-package
transport/public isolation/auth/error/abort tests, scoped lint/docs audit and
hooks. After committed independent review: required unit/build/Nix package
checks and a bounded existing authentication/browser smoke if packaging inputs
affect it. Preserve the proven two preexisting mobile expansion failures; no
layout fix or automatic repeat of all 62 browser cases. Stop when the changed
dependency and carried adapter are verified under the repository's required checks.

### D4, compatibility and stopping condition

Lead owns final EN/CS KB prose: replace current generic npm/Python 0.30.2 references
with 0.31.0, add the generated TypeScript SDK link and a short distinction above,
and document its actual 0.1.1/0.30.2 supported install pair if giving an install
command. Rust remains crates.io `vpsadmin-client` version `0.1`; no SDK 0.31 claim.
Keep original source/history and use existing guarded candidate/manifest tools;
foreign staging and exact production approval boundaries remain. No new evidence
framework or compiler suite is needed for this small addition.

No database migration, persisted application format, node protocol or service
ordering change is introduced. Shared schema validation now rejects unsafe
nested saved endpoint metadata, but this consumer uses mounted profiles; no
stored snapshot migration is assigned. Ship server, generator gems and profile
configuration together; rollback that complete set, with matching generated
metadata/assets. Mixed workers may expose different documentation tabs while
wire API/authorization stays unchanged. Source diff retains the 0.30.2 context
and Rust rendering fixes; the newly added TypeScript adapter still needs its
bounded consumer check. This is not permission to modify the live cluster.

Delivery stops at committed, independently reviewed successors with exact
dependency/generated-SDK checks and affected required verification, plus reviewed
KB candidates. Report actual remaining approvals/CI conclusions. No unrelated
SDK regeneration, HaveAPI/provider redesign, live deployment or default merge.

### A4 fresh-base compatibility amendment: schema-export tooling

Lead accepts this necessary bounded addition. Actual upstream 08c3 introduces a
tooling Gemfile that requires the API's exact declaration text `~> 0.29.9`, then
substitutes `= 0.30.2`; its runner rejects any loaded server except 0.30.2.
Leaving these files unchanged would break the upstream tool after our API bump.
This supersedes the earlier no-tooling-edit assumption, not its no-export rule.

Implementer0 additionally owns `tools/api-schema-export/{Gemfile,runner.rb,cli.rb}`
and `docs/api-schema-export.md`. Preserve the existing checked substitution:
expect exactly one `gem 'haveapi', '~> 0.31.0'`, replace it with exact `= 0.31.0`
for the separate tooling bundle, and update the runner's exact loaded-version
guard/error and CLI help. Docs should say the isolated bundle pins the same
release used by the API; preserve its separate local lock/store and all existing
environment, clean-checkout, destination, plugin, fixture and provenance rules.
Do not broaden accepted versions, remove the guard or rewrite bootstrap/snapshot
logic. This is a few version/reference edits, not a generator/tooling project.

Checks: syntax/scoped lint; evaluate the real tooling Gemfile through existing
Bundler DSL under the prepared repository environment and confirm server exact
0.31.0 plus all profile generator dependencies without launching the exporter.
Run existing database-free `safety_spec.rb` and `snapshot_spec.rb` with the docs'
explicit `--options /dev/null` and isolated API bundle. Existing B mount checks
cover the shared API/profile load. No actual export, temporary-database campaign,
SDK regeneration or new regression framework is required for literal version
refreshes. If installed bundle/source cannot meet the guard, report the mismatch.
Fresh-base PHP delta f379 changes only PHPUnit 13.4.3 to 13.4.5 and its metadata;
retain it. It does not add another deployed Guzzle update.

Public release identity and inspected SDK exports are summarized in
[the compact fact receipt](package-0.31/release-client-facts.md). Its hashes match
registry metadata where supplied; it does not claim signature verification or
complete source/archive equality. Owners' package/source checks retain those
distinct limits.

## 2026-10-27 E4: authorized development redeploy and KB staging

User now requests redeployment after the source work and permits resetting this
session's disposable cluster. Lead accepts **reset/recreate**, because the native
source selection and live PHP mount prevent a safe alias-only services update.
This authorization does not select a new workspace/provider package, integrate
defaults, change the physical host, stop/archive the session, or touch another
session. Implementer3 owns bounded preparation and the released Git moves; lead
owns native reset/start and ordinary tracking registration edits. No mutation
was performed by this investigation.

Current public wrapper selects runtime
`/nix/store/46rpb1jcjaclc01vrj0r9m8v0xvp8341-dev-workspace-0.2.0` and provider
`/nix/store/cscrk1qkydsvzlkxjv272nq7xq25bg30-vpsfree-dev-workspace-tools-0.1.0`.
Its installed native README, source, contract and selected coordination guide
were read. Cluster schema 1 / transition policy 3 remain. Recheck this selection
before action; old w6/q19 launch receipts do not identify today's commands.
The installed proof SSH still reads caller stdin and full-boot enumeration uses
a here-string. F is not installed. Native exit0/applied completeness alone is
therefore insufficient; do not claim this redeploy fixes the certificate bug.

### Source binding and exact gates

The provider selects literal `worktrees/<slug>/vpsadmin` and
`worktrees/<slug>/vpsadmin-webui`; it ignores registration aliases and overwrites
source environment variables. There is no public alias selector, move/rebind or
native build-only/prepare command. `dev-session worktree add` refuses a different
branch for an existing registration. Symlinks are rejected by normal registration.
PHP is served through a virtiofs-backed source directory. Replacing its host
directory while QEMU remains active cannot prove that the guest leaves the old
directory inode. Reset first avoids that ambiguity and makes both source mounts
fresh without changing provider code.

Before disruption, A and C must each have their exact final 0.31 head committed,
quick checks passed, independent final history/source review accepted, and
affected required package/postreview checks complete. D's local candidates must
be final/reviewed before staging. Bind these final heads, effective dependency
locks and built artifacts; never infer them from a mutable branch name. Retain
old 70a/f10/2c refs and previous runtime evidence. Recheck selected generation,
own native pending/runner tuple, native OS `origin/staging` and complete effective
input graph, source cleanliness, bridge/KVM, actual capacity and kernel cache
availability. Do not run new guest probes before the execution release.

Native OS selection overrides both `vpsadminos` and `vpsadmin/vpsadminos`; its
nixpkgs also supplies the React build graph. Compare with source-check graphs
and report material differences. Finish already required application/package
builds before reset. No optional prebuild framework is needed. Native `start`
prepares credentials and builds final `cluster-config`/runner before boot; record
those final outputs and graph when available. There is no separate public native
prepare stage to invent or a reason to invoke private `build_config`.

### Bounded ordered execution package

1. E3 prepares four Git moves and a before/after inventory, without executing them.
   Coordinate with A/C owners so no checkout command/process is still writing.
   Preserve exact branches/heads/common Git directories and the existing ignored
   locks/private configuration. Save the current editable cluster `config.json`
   privately outside the reset tree, mode0600 in an owned mode0700 directory;
   retain a digest/compact old source/selection receipt, never secret contents in
   Git or output. No broad copy of private runtime journals is required.
2. After source gates and fresh native ownership/pending checks, lead runs public
   `vpsadmin-devcluster reset 2026-10-24-vpsadmin-haveapi-upgrade`. The native reset
   owns stopping the exact runner and removing its cluster state/disks/socket.
   Require actual completion and no remaining owned VM/socket processes before
   any path moves. A refusal or uncertain result returns to reconciliation, not
   a forced cleanup or new command around the native checks.
3. After lead's reset-complete release, E3 uses ordinary `git worktree move`
   (from the respective canonical bare clone) in this order per repository:

   | Existing basename | New basename |
   | --- | --- |
   | `vpsadmin` | `vpsadmin-live030` |
   | `vpsadmin-031` | `vpsadmin` |
   | `vpsadmin-webui` | `vpsadmin-webui-live030` |
   | `vpsadmin-webui-031` | `vpsadmin-webui` |

   All paths remain in this exact session's worktree group. No branch change,
   ref rewrite, deletion, symlink or source checkout/reset occurs. Stop after a
   failed move and reconcile actual Git paths before retry. Lead renames only
   these four ordinary `portal.yml` registration `name` values, carrying each
   whole entry (project/branch/default/initial base/comparison) with its worktree.
   Preserve the refresh/F and all other entries. Public `dev-session sync
   <slug> --as-is` validates the resulting attached-worktree identities. Check
   that canonical paths now contain exact final031 heads and retained paths
   contain old70a/f10 with original ignored/private bytes. The permitted ordinary
   tracking change is not a private runtime-state override.
4. Initialize the same session through public `vpsadmin-devcluster config <slug>`
   with secret-bearing output suppressed. Restore only the saved **documented
   editable config.json** at that initialized owned location, preserving mode and
   validating its digest. Do not restore applied envelopes, sockets, journals,
   disks or credential directories. Reset intentionally creates fresh disposable
   application/BFF state; native start generates its new credential bundle.
   Preserve workspace CA/SSH state; no certificate import/rotation is requested.
5. Lead launches public `vpsadmin-devcluster start <slug> --topology single
   --network bridge` under the existing bounded execution approach, nominal
   32GiB/12CPU and requested Nix max-jobs1/cores2. Detached runner/QEMUs must retain
   limits after the command exits; account for the global Nix daemon separately.
   Do not overlap another heavy batch or launch another cluster. A fresh permitted
   watcher observes this exact parent-owned command/log; it does not launch,
   retry or diagnose reset/start. If utility capacity is busy, use the documented
   visible parent fallback. Unexpected actual local kernel compilation stops the
   owned build for the existing cache-policy investigation. No `--force`, local
   network fallback, maintenance mode or host/profile change is part of E4.

### Runtime acceptance and recovery

Require successful native build/boot/seed/refresh, ready state and exact selected
source labels. Save compact source/input graph and four selected toplevels plus
normal host GC-root proof; do not rely on JSON as a root. Then use four separate
public `vpsadmin-devcluster ssh <slug> MACHINE -n -- ...` reads, one for each
dns-primary/dns-secondary/node1/services, to check selected current-system,
closure validity and existing standard/profile/provider root registrations.
Do not put SSH inside an input-fed names loop. No manual root creation or
applied-envelope rewrite is authorized. If the old provider again leaves three
extra roots absent, record that certificate/recovery limitation explicitly;
independent valid closures plus retained system roots can support current manual
testing as previously accepted, but cannot certify the native full-boot record.
Missing real system/residency/retention proof is a runtime blocker to report.

Check actual packaged HaveAPI 0.31.0 and generator identities, matching final
React frontend/BFF build-info, legacy PHP from the new canonical checkout, TLS
through the cluster CA and one real seeded-member login/read/logout through
each UI. Confirm generated TypeScript documentation alongside retained Go/Rust
panels. Use existing bounded access checks, not a broad browser/SDK campaign.
Keep passwords/tokens/cookies out of logs and screenshots. Handoff both actual
URLs, internal DNS/VPN and CA requirements, and private credential access.
Leave the cluster running and session open.

An interrupted operation retains its native pending state and selected roots;
inspect that exact outcome before retry. Source/config rollback requires the
same supported Git mapping and public native operations, not copying old proof
records. Recreated disks deliberately have no retained-data rollback obligation;
old source refs and previous verification remain intact. New package generation,
ownership or layout refusals are blockers, not permission to bypass checks.
The selected physical-host coordination policy reserves host deployment/profile
changes, not ordinary session QEMU execution. No host mutation is needed here;
do not take over a foreign host reservation. A real address/runner conflict still
blocks startup.

### KB staging ownership boundary

Public `kb-stage status` still reports owner `2026-09-13-auth-email`, container up
and a pending EN release. Public help exposes start/stop/status/reset/release,
with no queue or transfer command. Our user's request authorizes showing this
session's final articles in staging once legitimately available; it does not
authorize discarding another session's review bundle or releasing its claim.
Lead reports the blocker; no foreign records, messages or mutations are assigned.
The existing owner must settle/discard its own pending bundle and release staging,
or the user must supply separately scoped direction for that ownership issue.
Do not poll indefinitely or invent a staging queue.

Once availability is confirmed, E3/D owner uses existing public `kb-stage start`,
then `kb-release stage --manifest FILE --yes` and `kb-release verify --manifest
FILE` for the final EN/CS manifests after fresh production-source guards. Present
both real staging page URLs and verified localized revision-history links. No
production promotion, staging reset or post-handoff release is implied.

## 2026-10-27: bounded A31-R1 measurement and C4 expiry decision

This addendum releases design preparation only; execution remains with A0/C1
under the lead's existing check/utility allocation. Exact session identity was
reconfirmed from tracking CWD; both session environment variables are absent
and the trusted binding matches. No application/provider source, refs, live
cluster or staging change is part of this design step.

**A31-R1 (A0): measure the real page before broader suites.** At committed
vpsAdmin `d258591f81e49365b02206dd184296f5f5e7d045`, reuse the existing B3
mounted full-plugin RSpec/disposable-database setup and unwrapped warm-GET seam
in `package-b/b3/postreview/capture.rb`. Do not execute that historical harness
unchanged: its head, role order, versions and sample extraction identify 70a.
A short session-only adaptation is sufficient; no new framework or application
spec change. Bind the actual current full-mode lock and loaded HaveAPI/generator
versions/source paths, retain response status/bytes and time `GET /v7.0/` using
monotonic wall and process CPU immediately around the real request, before CGI
or matcher work. First request: anonymous/en. If it again consumes tens of
seconds of CPU, record the result and stop the broader batch for lead disposition;
there is no value in repeating the expensive member/admin requests to establish
that public-page regression. An interrupted request is incomplete lower-bound
evidence, never a pass. If no gross regression appears, run the existing member/cs
and admin/en requests and bounded role/locale/isolation assertions. No new numeric
SLA, repeated warm campaign or speculative deadline is introduced. Retain the
0.30.2 reference of approximately 4.23s anonymous, 2.53s member and 4.94s admin
unwrapped requests with its original conditions; it is context, not a new gate.

Read-only source at HaveAPI v0.31.0 (`c9124da...`) confirms repeated recursive
`normalize(context.description)` in TypeScript `Documentation#authentication`,
`#action_authentication`, `#authorized_action` and `#compatible_action!`. The
last is invoked for both authorized/live and current actions. Tiny init/action
checks cannot establish full-page cost. If measurement confirms the regression,
the minimum proposed remedy belongs to upstream
`clients/typescript/lib/haveapi/typescript_client/documentation.rb` and its
existing documentation tests: shallow string-key selection along the resource
path, selected action/alias/provider and metadata, recursively normalize only
selected values. Follow the existing Rust adapter's last-insertion key semantics;
retain ambiguous-alias rejection, request-local authorization/locale, detached
frozen model ownership and unchanged limitation/error behavior. Test mixed
symbol/string keys, selected aliases and rejection, nontraversal of unrelated
subtrees, frozen inputs and different request contexts. No shared privileged
rendered cache, consumer monkeypatch or copied renderer. A patched generator is
not an unmodified published 0.31.0 artifact: any upstream source/new-release or
dependency exception needs lead/user disposition before implementation. No
migration, deployment or recovery contract changes are proposed here.

**C4 (C1): one controlled desktop comparison, not a browser campaign.** The
ordinary preview seam exists (`npm run preview -- --host 127.0.0.1 --port PORT
--strictPort`, `E2E_BASE_URL`, with `E2E_START_SERVER` unset). It is **not eligible
for the already built normal frontend with this unchanged fixture**: normal
`npm run build` compiles `VITE_RUNTIME_MODE=bff`; required BFF bootstrap validates
HTTPS and fetches `/config.json` and `/session.json`. The fixture only injects
`window.vpsAdmin` legacy configuration and intercepts `/api`, while ordinary
Vite development defaults to legacy. Serving that BFF artifact would test a
missing bootstrap rather than the reported expiry behavior. The existing
`build:legacy` could make a separate artifact, but doing so is an additional
build and is not proof of the already built BFF artifact; it is not the selected
shortcut. No fixture, proxy, runtime-mode override or bootstrap weakening.

Use only `e2e/specs/app/session_expiry_redirect.spec.ts`, project `chromium`,
zero retries, unchanged 15s URL/30s overview assertions and normal notice check.
Compare exact f10d3d48c4f21cc39187c3667ffffd9952404c11 against current
baf00acc31d34ab37720643c5833b4476a341f3b using the same retained FHS/browser,
CPU60-63/nice5, fresh owned Vite server/free port for each side, identical normal
development mode and selected fixture. C1 owns one isolated scratch source at
f10 with its original lock/fixtures; preserve the live checkout, refs and source.
Reuse existing verified runtime/dependency material only if its actual input
identity matches, otherwise ordinary isolated installation; no broad baseline
archive campaign or full-suite rerun. Record both outcomes and the 401 → public
navigation → Overview mount/URL cleanup → notice boundary from existing artifacts.
The user contract is expired authenticated state leaving the app and reaching a
usable public overview with the fresh notice. A trace showing a prompt 401 and
redirect alone does not prove completion; a green artifact must exercise all
unchanged assertions. If both fail similarly, classify only this fixture/runtime
limitation, not all browser behavior; if both pass, record paired passes and the
original cold-server failure without claiming its exact cause; if current alone
fails, retain the unresolved upgrade boundary. Stop after the pair and report to
lead; no timeout increase, force-click, layout fix or blind retry. Mocked browser
proof does not replace later actual TLS/BFF login checks for the authorized
cluster redeployment. Old 60/62 mobile-expansion disposition remains separate.

## 2026-10-27: A31-R1 upstream source fix (implementer2 ready)

The qualified anonymous GET at consumer d258 measured 15.23135s wall/15.21839s
CPU, HTTP 200 and about 2.8 MB, with no Authorization, empty Cookie and nil
user/session before and after; full English help/panels were verified. This
supports the Important performance finding. Anonymous help intentionally lists
all actions: only authenticated-member help is permission-filtered. A0 owns the
separate mistaken anonymous test assertion correction. C4's paired f10/baf expiry
case passed on both sides under the same cold runtime and assertions; lead
accepted that bounded evidence, without converting the earlier six-case run to
6/6 or claiming a proven preexisting cause. No more C work is required here.

**Source and ownership.** Implementer2 owns exactly
`clients/typescript/lib/haveapi/typescript_client/documentation.rb` and
`clients/typescript/spec/unit/documentation_spec.rb` in a new ordinary
session-owned `haveapi` worktree, branch
`2026-10-24-vpsadmin-haveapi-upgrade-typescript-docs`. Use fresh canonical master
`4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c` as the source baseline (SSH remote
and remote HEAD verified). Both files are byte-identical to released v0.31.0
`c9124da141adc258fbbaf67d4ec19ee3f8580849`, also current `haveapi-0.31`.
Read current local AGENTS and development/release procedures; ordinary public
worktree registration preserves other sessions' refs/checkouts. Recheck base on
creation; report substantive intervening changes. No release branch mutation,
version bump, tag, registry publication, default merge, generated artifact or
consumer dependency edit. A later authorized patch release belongs on the
supported release branch with `cherry-pick -x` per HaveAPI's release procedure;
that later operation is not included in this source package.

**Implementation.** Adopt the released Rust adapter's small `normalized_members`
pattern (stringify one map level, last-inserted colliding key wins). Select the
resource path and selected action before recursive normalization. Keep exact
canonical-name precedence and alias fallback: inspect sibling alias metadata
shallowly, normalize alias values as needed, reject ambiguous aliases, and
normalize only the selected action. Authentication selection visits only the
authentication map and selected provider, preserving Basic/token preference,
header matching and explicit-description checks. Metadata compatibility selects
only `meta.namespace`; existing selected `context.action`/sample normalization
and validation stay. Never recursively normalize the complete request description
in a render path. Keep mount-time snapshot detachment/freezing unchanged; no
cross-request memo/cache, broad new helper abstraction, consumer patch or copied
renderer. A short nearby comment explains shallow lookup/key-collision semantics;
no separate documentation expansion is needed for unchanged public behavior.

**Acceptance and checks.** Extend the existing spec/fixtures locally in the same
spec file with a small deterministic unrelated-subtree traversal regression
that fails before the fix; exercise selected example and auth paths without
wall-clock thresholds or an oversized synthetic tree. Reuse existing fixture
helpers to prove string/symbol/mixed keys and last-insertion collision order,
canonical/unique/ambiguous aliases, Basic/token/header rejection, frozen caller
input/model nonmutation and sequential distinct authorized contexts without
retained decisions. Preserve current exact program/result/limitation contracts
and anonymous-versus-member semantics; the adapter consumes the description
provided by the server and does not invent a new visibility policy. Existing
specs already cover sample validation, stale contracts and protected fields;
extend them proportionately rather than duplicating an exhaustive matrix.

Quick check from the normal root Nix shell: existing `make test-typescript`
command narrowed to `bundle exec ruby -Iclients/ruby/lib
-Iclients/typescript/lib -S rspec
clients/typescript/spec/unit/documentation_spec.rb`, plus scoped RuboCop and
mandatory Overcommit hooks. Keep prepared library locks untracked. Commit one
focused source/regression change, then independent final review of the exact
base/head and two-file diff (no migrations). After review, run the existing full
`make test-typescript` and `make test-documentation-generated` with ordinary
prepared JS/server dependencies and `make doc` prerequisite; these exercise
compiled emitted programs and mounted profile/server integration. Use the
required watcher for uncertain/long checks; stop on relevant failure, do not add
a new performance runner, full release build or unrelated all-language campaign.
Publish the reviewed feature branch normally after the required checks; return
its patch/quick/long evidence to lead for user review and release disposition.

**Consumer and recovery boundary.** Published vpsAdmin 0.31 dependencies remain
unchanged except A0's known test correction. A source fix with the same VERSION
is not the published artifact. After explicit adoption of a released successor
or separately approved dependency source, A0 repeats the same qualified full
consumer GET first, retaining original role/locale/input conditions and comparing
measured CPU/wall/response semantics; then member/cs and admin/en plus existing
visibility/isolation checks. R1 closes only on actual adopted-source and measured
consumer proof. Source fix alone is not that proof. No protocol, schema, SDK
package identity/runtime pair, persistence or cluster change is proposed;
rollback of a later release is ordinary dependency reversion, with no data
migration. Current live cluster and E4 reset gates remain unchanged.

## 2026-10-27: authorized 0.31.1 adoption gates

The user directs watching for 0.31.1 about every ten minutes and upgrading when
available; no repeated approval is needed on availability. E2's read-only watcher
owns registry and public KB-staging status checks. Architect/implementers do not
add polling. The preceding upstream-source package is superseded by the user's
external ownership: retain its exported partial patch/evidence, but perform no
further upstream source, test, review, release or foreign-session work here.

**Availability/source gate (E2 facts, architect assessment).** Once available,
retain exact public identities/digests for the five Ruby 0.31.1 gems, generic npm
package/browser bundle, Python wheel/sdist and PHP mirror tag/Packagist commit.
Distinguish registry-published integrity from locally computed hashes. Bind the
release tag/source and compare 0.31.0 to that released source, especially the
TypeScript Documentation selection/normalization fix, key/alias/auth semantics,
request-local ownership and unchanged profile contract. Verify artifacts actually
contain the remedy; a new version alone does not close A31-R1. Inspect only the
relevant released SDK/runtime requirements: retain generated SDK0.1.1 with its
0.30.2 runtime unless the new renderer/SDK's published contract supports a changed
pair. Never infer an SDK0.31.1 release or force all SDK runtimes to the application
version. Do not read the user's other-session records for this assessment.

**Independent consumer packages.** A0 owns the existing vpsAdmin dependency and
profile stream: exact runtime0.31.1 declarations plus generated Ruby/Nix locks,
PHP Composer lock, legacy JS source/provenance, schema-exporter declaration and
exact-version guard/help/docs, and version assertions. Keep the corrected
anonymous full-help expectation and authenticated-member visibility checks.
C1 owns React's npm manifest/lock, vendored released source/provenance and affected
Nix/package metadata/docs. Use ordinary session-owned successors/history
consolidation to replace the pending0.31.0 pin stream with final0.31.1; preserve
published C31baf and all old LIVE70a/f10/2c refs and checkouts. Keep the carried
adapter/profile change coherent and record old/new range equivalence. No PR74
rewrite, default merge or live-source switch during preparation. Do not append
multiple obsolete dependency commits just to retain earlier test provenance.
Lead owns the small EN/CS KB version/pair wording update; E3 owns existing checks
and final manifests. Reuse prior prose/snippet evidence for genuinely unchanged
content, refresh guards against final candidates, and stage only after public
status proves this session can ordinarily acquire staging. User's planned release
of staging is not evidence that foreign ownership has already ended.

**Verification and stopping condition.** Owners compare the actual released diff
and select affected checks, preserving prior exact-input evidence for unchanged
code. Quick generated-pin/provenance checks, exporter guards and relevant focused
profile/adapter tests precede commits; obtain the necessary final affected review
and whole-history/no-migration conclusion before longer checks. No automatic
repeat of full browser/SDK campaigns. For A31-R1, first repeat the same qualified
anonymous full-plugin GET after actual0.31.1 loading: explicit no auth, nil
user/session, expected all-action English help, save body before assertions and
measure wall/processCPU before CGI/matchers. Compare with qualified0.31.0
15.23135s/15.21839s and the retained0.30.2 conditions; report any condition/response
change. If severe cost persists, stop broader suites and return the concrete
release defect to lead. If remedied, complete existing member/cs and admin/en
visibility, locale and isolation checks, then only affected packaged/services
and consumer acceptance checks. R1 closes on measured adopted artifact plus
preserved semantics, not the tag or unrelated unit passes. Any material new
release behavior changes this brief through lead; no consumer workaround.

No migrations or persistent-format change is expected; verify this against the
release diff. Ordinary dependency reversion retains the previous software/data
contract, while E4's explicitly authorized devcluster reset discards disposable
cluster data. After final source/review/check gates, lead/E3 execute the already
accepted E4 supported reset/rebind/start and access checks against final0.31.1
sources, and show both reviewed KB staging pages once available. Existing native
ownership/generation/provider-certificate limits and rollback preparation stay;
no provider install, release publication, production KB write or default merge is
added. Adoption source work is ready at the availability gate; operational
activation remains behind its established verification gates.

E4 source-binding amendment for 0.31.1: after final reviewed/checked successor
heads and lead's completed public reset, retain the original canonical `vpsadmin`
and `vpsadmin-webui` at their previously planned `*-live030` names. Move the
new 0.31.1 successors into the vacated canonical names; do **not** move the
retained `vpsadmin-031`/`vpsadmin-webui-031` checkouts or rewrite their refs.
The intended new registration basenames are `vpsadmin-0311` and
`vpsadmin-webui-0311`; they were not yet present in `portal.yml` at this design
check, so E3 must substitute the actual final registered aliases/paths in its
existing four-move receipt and verify exact final heads before execution. Lead
renames only the four involved whole registration entries and public-syncs;
031 entries, historical bases and all unrelated registrations remain intact.
All reset-completion, private editable-config restoration, native start/build,
capacity, four-guest proof and access checks from E4 remain unchanged. No move,
manifest edit, probe or activation is performed by this amendment.

KB staging is already owned by this session with reviewed 0019 / generic0.31.0
pages verified. Its staging review remains valid for those exact pages. After
E2 confirms the 0.31.1 source/runtime facts, lead updates only current generic
version references and any genuinely changed pairing guidance; E3 refreshes
source guards/manifests and restages/verifies the revised pair through the same
public workflow. This does not authorize production publication.

0.31.1 first artifact facts (E2 report; compact receipt follows in
`package-0.31.1/release-facts.md`): tag source is
`d49cfa3f3b8ee42f6cd8a6b7de8b7d551215cd42` (unsigned). Downloaded TypeScript gem
matches registry SHA256
`597a6fe9f7d95f4e40cb6a4795352e5798082d3df65944f19ea060841742bb02`;
its Documentation source matches the tag with SHA256
`57a9d866a548c86c06c7351bff70b8b8afa18b8c281407053586639ed0b6fd53`.
E2 proves the runtime change identical to the retained patch implementation;
architect inspected that patch: shallow selections preserve canonical-before-alias
lookup, unique-alias rejection, Basic/token preference/header checks and
last-insertion mixed-key normalization, with no request cache/model mutation.
The other reported release changes are performance tests/tooling and synchronized
versions, not server HTML rendering source. This supports the existing narrow
A/C verification mapping; it is not a consumer timing pass or release-test claim.
Published SDK remains0.1.1 and both its peer requirement and the packaged0.31.1
guide/renderer retain runtime0.30.2, `createClient`, versioned API base and the
same profile keys. Keep SDK/renderer examples and KB pairing unchanged; only
generic application versions become0.31.1. No additional design or source scope
is needed. A0 proceeds with adopted-source timing/role checks after required
quick/final-review gates; C1 retains focused artifact/provenance and affected
adapter checks, with unchanged browser/BFF evidence reusable for its exact scope.

C0.31.1 baseline decision (lead accepted): use fresh WebUI main
`9113caa0915b2908373ecd616f8f752e779ed4c9`, retaining published baf/LIVE f10.
The recorded 119-path upstream delta includes body-parser1.20.9, qs6.16.1 and
its independent BFF Nix hash, plus integrated product/fixture changes. The
canonical selected-release receipt records those upstream PRs as approved and
deployed; they are baseline content, not this session's new feature scope.
Preserve them while carrying only the existing two logical HaveAPI upgrade/
adapter streams with final0.31.1 pins. The empty successor's historical initial
registration base5a stays truthful; record911 separately as the final review
base, with old5a..baf to new911..head mapping and any conflict resolutions.

C1 owns the seven overlaps: retain both work-log histories and requirements;
PACKAGING must combine the final root npm hash with upstream BFF hash; merge
strict E2E coverage/tsconfig additions and structural-debt removals without
restoring obsolete allowances; preserve the new datasets regression while
adapting its fixture to the carried client. The actual new dataset wire contract
is `dataset[dataset]`, `to_depth:0`, and role `backup`; preserve upstream nullable
network ownership types and HaveApiError/localized snapshot rejection handling.
These are focused compatibility checks, not grounds to reimplement upstream UI.

Retain unchanged adapter/npm runtime source equivalence only for its verified
scope (0311 published JS is version-only, declarations unchanged). Old BFF lock,
full frontend tree and broad browser proof do not establish911 successor identity.
Run ordinary quick/audit/type coverage plus affected adapter/dataset/error tests;
new BFF lock requires its normal installation, audit and BFF checks. After final
committed affected review, use normal required test/build/package provenance
checks against the combined head and bounded auth/expiry acceptance. Do not
repeat upstream's entire product/browser campaign or claim prior60/62 or paired
expiry results as a new full-browser pass. Report a concrete merge/test conflict
through lead; no additional design gate is imposed. E2's completed
`package-0.31.1/release-facts.md` satisfies the release-source fact gate; installed
consumer timing/semantics remain the R1 closure gate.

## 2026-10-28: E4 proposed native graph disposition

Recommend accepting E3's exact proposed graph for the already authorized new
disposable cluster, subject to the existing A services/final-writer handoff and
execution preflights. No additional compatibility blocker was found. This is a
graph/source assessment, not a build, guest-proof or deployment result.

Read-only retained Git inspection shows OS staging
`d9be8c4bada590c0405df85444600d40e6f3caa6` →
`f4e55a13d7d2f5c1b61737f0300ec8a535ef02f1` is exactly one commit changing only
`flake.lock`: stable nixpkgs `1f607aa79...` → `718f670e8...`. No OSVM runner,
module, application, protocol, seed or migration source changes occur in that
OS range. The status commits were unavailable in the canonical local Git
object database; no fetch was attempted. Both exact status source trees were
already cached locally, identified by E3's recorded NARs at
`/nix/store/glbypzg1ixw5wm6q2wf0k2shkxcyw1bd-source` (0210b055) and
`/nix/store/8z9sv8rm8pkpnxsgm1589lsb99j709ld-source` (e4881a93).
Their only file-content difference is the same stable-nixpkgs lock update;
status application/config/module source is unchanged. Native vpsfStatus follows
its root nixpkgs/vpsadmin/vpsadminos inputs, so its own lock does not introduce
an additional independent dependency selection in this composed graph. Its
source revision/package identity still changes; no binary equality is claimed.

The seven changed node keys comprise the two final0311 source paths, both OS
nodes, their two stable-nixpkgs nodes and the status source. E3 records complete
20-node graph digest `d6f76d362cbfe695550a19674150ebab6c9d3d5bcfd44728fddf2faaba562f84`.
Selected runtime pq2jwj/provider vh650 retains contract `9c8e9e5c...`, schema1/
policy3. This graph uses a newer stable package set, so ordinary native public
start must build/validate its complete final canonical-path graph; C's standalone
package outputs are not interchangeable proof. Fresh reset avoids loading old
application/database/BFF disk state through this package update. No retained-disk
migration or mixed-OS fleet rollout is proposed. Restore only the accepted
editable configuration, with native fresh credential/state creation as designed.

Retain E3's existing local/cache evidence for the actual two6.12.113 kernels;
stop and investigate unexpected kernel compilation under the normal policy.
No extra OS/status campaign, host package switch or manual pin is required.
Final source/ignored-byte handoff, post-reset address ownership, immediate host
capacity and canonical-source checks remain unchanged. F is still absent in the
selected provider: independent four-guest exact system/valid closure/standard
and provider-root observations remain required, with the known certificate
limitation reported honestly. Native build/runtime failure returns to ordinary
owned-operation reconciliation; this assessment does not bypass a refusal or
authorize provider repair, defaults integration or physical-host deployment.

## 2026-10-28: E4 embedded WebUI metadata versus exact source proof

The running native frontend5y1v/BFFnb19 metadata says `unknown`, `dirty:true`,
`source:unavailable`, while native labels name clean e468. Labels alone cannot
prove package identity. The existing packaging contract intentionally emits
this conservative metadata when its flake input lacks `self.rev`; the native
provider's path input is the reported cause. No metadata file should be patched,
no clean revision fabricated and no provider correction/rebuild is required
solely to improve this display.

Accept independent exact-source provenance for this **development testing
cluster**, once C1 completes the existing evidence chain: actual services
selection/closure and nginx/BFF runtime package paths → actual package outputs
and their recorded derivations → complete cleaned source/build inputs → reviewed
e468 tree and expected locks/dependency artifacts. E3's saved native-input and
6749-derivation graph records already identify frontend drv8n5b99 and BFFdrvq8r7d
with the same `/nix/store/6p46phpszswrwq6029rmj1gyyi7ynm44-source` (BFF `/bff`)
as C1's reviewed/rooted e468 Git-filtered source. C1 owns the final NAR/content/
mode/symlink and complete relevant input binding, reusing those records; E3 owns
actual runtime linkage/access facts. This does not require standalone/native
output equality: their nixpkgs/build graphs differ. It requires identity of the
actual native outputs, their own complete inputs and exact reviewed application
source, including absence of extra retained build inputs.

If that chain is complete and the existing actual application-flow checks pass,
report the cluster usable at independently proven e468, with missing embedded
revision metadata as an explicit limitation. Do not call the normal **clean
release metadata** gate passed: PACKAGING.md requires matching full commit IDs
and false dirty flags for that claim. Existing standalone package proof retains
its actual scope. No new product/source fix is necessary for qualified manual
use. An unproved edge blocks only the unsupported exact-head claim until the
owner resolves that concrete edge; it does not justify an automatic rebuild or
new provider project. Any later durable provenance improvement needs a separate
lead-owned scope decision through the existing Git-backed packaging/input seam.
The running cluster, provider, roots, package outputs and default branches stay
unchanged during this assessment; no new probes or repeated checks are assigned.

C1's completed `package-c/0.31.1/native-provenance/receipt.md` now satisfies the
independent source/output gate above: all2,438 retained files/90,121,622 bytes
and executable bits match e468 with no extra files/symlinks; both actual native
derivations use that exact reviewed6p46 source. Their complete relevant edges
match E3's6749 graph and actual services44b2 closure/nginx root/BFF ExecStart.
Locks, npm FOD hashes, Node inputs and installed BFF dependencies are bound.
Absent build-only cache outputs are disclosed; retained constrained derivations
and actual installed-output proof suffice here without a cache-restore claim.
Architect accepts this as exact e468 provenance under ordinary Nix build/store
trust. No provenance blocker or corrective rebuild remains for manual dev use;
E3's actual TLS/login/application checks remain separate. Embedded metadata is
still unavailable and the normal clean-release metadata gate remains unmet.

## 2026-10-28: authorized 0.31.2 patch adoption

**Ready bounded source package.** The user requests the released Go-auth fix and
0.31.2 upgrade; prior authorization to redeploy this session's development
cluster, including reset, persists. E2's [release facts](package-0.31.2/release-facts.md)
bind released source `819bba5110e089465535ecd71ca2eb37a7d39caa` and actual
registry artifacts. The release changes Go documentation transport-name
comparison plus focused regressions and coordinated versions. Valid String/Symbol
names compare by their string value; equal nil/false/numeric names now correctly
reject. This tightens invalid descriptors without changing the valid token wire
contract. Other server/HTML/locale/auth-policy implementations are unchanged;
generic JS changes its version constant, with all 46 declaration files unchanged.
The TypeScript renderer fix remains unchanged. Keep generated TS SDK **0.1.1**
with runtime **0.30.2**, Rust **0.1.0**/normal `0.1` guidance and the existing Go
import/profile. Do not invent matching SDK version numbers.

**Source/history boundary.** A0 and C1 prepare separate registered
`vpsadmin-0312` and `vpsadmin-webui-0312` worktrees/branches; do not edit the
canonical running `9697bf28c3171d4ee3e0980160be60764ae2c4aa` or
`e468ca48406bde1bd99cc42a05e1832fb42162f4` checkouts. Consolidate the dependency
stream to final 0.31.2 and carry the reviewed profile/adapter stream as the second
logical commit, preserving original authorship and recording old/new ranges.
Retain all published 0.31.1, older LIVE/0.31, PR74 and default refs; no rewrite or
default integration. Preserve old private config and ignored locks.
The accepted bases are vpsAdmin `08c3bd7e3cb4dc324a0381df6a1eec190daab1a7`
and WebUI `9113caa0915b2908373ecd616f8f752e779ed4c9`, carrying the exact reviewed
9697/e468 content except the bounded patch changes. Lead explicitly accepted
continuing that reviewed/deployed range: WebUI main `40653dff...` adds 73 product
paths and is excluded. Fresh upstream observations do not silently expand this
patch milestone or establish current-default merge readiness.

| Owner | Files and change boundary | Quick acceptance |
| --- | --- | --- |
| A0 | Existing HaveAPI declarations in `api/Gemfile`, `client/vpsadmin-client.gemspec`, `download_mounter/Gemfile`, `plugins/outage_reports/utils/Gemfile`; `packages/{api,client,download-mounter}` generated declarations/locks/gemsets; `webui/composer.{json,lock}` and `php-packages.nix`; both legacy bundles at `webui/public/js/haveapi-client.js` and `console_router/public/haveapi-client.js`; exporter `tools/api-schema-export/{Gemfile,cli.rb,runner.rb}` and current docs/spec/services version references | All five API gems and other HaveAPI consumers resolve exactly 0.31.2; release bundle/PHP provenance matches E2; no unrelated dependency churn; retain native prerequisites/Faraday/Guzzle resolutions and existing exporter disposable version/guard checks. Preserve profile and anonymous/member semantics. |
| C1 | `package.json`, `package-lock.json`, `packages/frontend.nix`, `packages/haveapi-client-provenance.json`, applicable current packaging/client docs and dated work log | Exact npm 0.31.2 integrity/source proof; pinned-source checker and its tests, typecheck and focused existing HaveAPI adapter tests; unchanged app/BFF/fixture implementation compared with e468, except necessary version assertions. Preserve locked Node/BFF/security baseline. |
| Lead/E3 | Lead changes only the three generic installation-version references per EN/CS article plus summary; E3 refreshes existing guards/manifests and staging | SDK pairing and prose otherwise unchanged; existing candidate/snippet checks with actual final digests; public staging ownership must still be ours before restaging. No production publication. |

Owners use their repository guidance/hooks and normal generation commands.
Regenerate runtime pins, not constraints alone. No actual schema export or SDK
regeneration, dependency modernization, auth-request experiment, upstream
HaveAPI edit or provider installation is included.

**Affected verification.** Commit all intended changes and pass quick checks,
then obtain the narrow independent final/whole-history review of new ranges,
release/source mapping, generated pins and no-migration conclusion. Earlier
reviews and successful full campaigns remain evidence for their exact old inputs;
they are not relabelled as new-head passes. After review, build the affected API,
legacy PHP and React package outputs using their normal retained commands; run
the existing affected services/package acceptance and scoped React tests/build
required by local guidance. Reuse unchanged BFF/browser/SDK evidence only with
the applicable exact source/dependency proof. No automatic full/core matrix,
62-browser/26-SDK campaign or six-hour CI wait; a concrete new failure or changed
input determines any additional check through lead.

Go fix acceptance is one actual rendered token panel under the mounted consumer
and adopted installed 0.31.2 artifact: save the public HTML before assertions;
require `auth-token-go` code containing `SetExistingTokenAuth` and the expected
environment placeholder, no former mismatch limitation, unchanged advertised
header/query names, and retained Basic/OAuth2/init panels. Use the existing
public-page extraction seam; it needs no token acquisition or authenticated Go
request. The unrelated VPS-index response-field limitation remains separately
recorded. Existing focused generator tests may be inspected as release evidence;
do not launch upstream tests or recreate its suite here.

**Deployment selection: reuse the accepted reset/rebind route.** Current public
wrappers still select runtime `pq2jwjcv4hbyiwzcam50x6j9fv008qiq` and provider
`vh650zaiazv3n8z12yf12pfbc951xwb9`; execution must recheck them. Installed native
instructions support `update <slug> services` for changes within the selected
canonical worktree. They do not select successor aliases or remount PHP's source
directory. Moving an isolated successor over a running virtiofs mount is unsafe.
An in-place Git branch switch would preserve the root inode but change live PHP
source before its matching vendor closure activation and would need a different
checkout/config preservation procedure. It is not part of this brief. Since reset
is already authorized and the existing route preserves whole predecessor
checkouts, use that route rather than adding another binding mechanism.

E3 prepares only the established E4 operations and before/after invariants.
After final committed source/review/affected-check gates, recheck native ownership,
pending state, bridge, capacity, complete proposed inputs and kernel cache. Keep
the editable config privately with original secret bytes/modes. Lead performs
public reset for this exact slug and proves it complete. Only then E3 performs
ordinary Git worktree moves `vpsadmin` -> `vpsadmin-live0311`,
`vpsadmin-0312` -> `vpsadmin`, and the corresponding WebUI moves to
`vpsadmin-webui-live0311`/`vpsadmin-webui`. Retain old `*-live030` and all other
entries. Lead carries whole ordinary registration entries with their new names,
then public sync verifies exact branches/heads. No symlinks, private overrides,
ref rewrites or lifecycle closure. Public config initialization followed by
restoration of documented editable config precedes lead's public bridge start.
Use the existing resource limits (Nix jobs1/cores2; runner 32GiB/12CPU) and watcher
ownership, subject to actual capacity. Native start builds the final canonical
graph normally; do not invent a prepare/private build command or output-equivalence
claim for different native inputs.

Acceptance retains the E4 contract: exact built source/locks/packages and actual
services paths, independent four-guest current-system/closure/retained-root proof,
strict-CA login/read/logout through both UIs, the Go token panel above, and both
reviewed KB staging pages. F remains uninstalled: no complete provider boot
certificate or future cold-recovery claim. Native React metadata may remain
unknown; the established complete filtered-source/derivation/service chain can
prove exact source instead. Reuse the existing proof method, not a new framework.
Leave the accepted cluster running and provide both URLs.

**Compatibility/recovery and stop condition.** E2 found no schema, node protocol,
persistent format or auth policy change. Mixed 0.31.1/0.31.2 transports remain
compatible; retain old deployment/source evidence. Reset discards only this
authorized disposable cluster's data. An uncertain reset/start/update must be
reconciled through its original public operation before any path change/retry;
do not restore old applied envelopes or manufacture roots. If artifact mismatch,
new semantic delta, real package/check failure or ownership refusal appears,
report that specific blocker rather than expanding scope. This milestone ends
with verified 0.31.2 consumer/token documentation, both usable dev UIs and staged
articles. Default integration, production KB release, upstream fixes and session
closure remain outside authorization.

## 2026-10-28: E5 selected-runtime and status-input disposition

E3's [generation inputs](devcluster/e5-preflight-0312/generation-inputs.json)
identify a newly selected runtime/provider, without a switch by this team:

- Runtime `/nix/store/pjmi2cz75r9cwynh4lin706jdzlp4xb9-dev-workspace-0.2.0`.
- Provider `/nix/store/kbppyqvzbizqvdi7d8ws07j006mdz8q0-vpsfree-dev-workspace-tools-0.1.0`.
- Coordination catalog SHA256
  `9936fc4d7605c6a2790167473cfa75a688682b77d57d5cd48b59b7ad2947783e`.

Architect's read-only installed-byte comparison found the runtime host executable
identical to pq2 (`ac32c4608ea599dc8de9c15f7c7817b11d04b457fecfd1105d01c1c3e388b399`);
its wrapper changes only its own store path. Coordination/claim/repository-claim/
integration contracts and both coordination guides are byte-identical. The
coordination catalog differs only in the confctl adapter's vh650→kbppy wrapper
path; resource mappings and policies are unchanged. The integration catalog has
the analogous recipe-path change. Team catalog/package metadata changed, which
does not replace this session's retained roster/settings.

All installed native provider payload files are unchanged; its launcher wrapper
changes only the self path, preserving tools and default config. Cluster contract
`9c8e9e5c371eda46ccb49eaf275ee4996d2ddce3930c9047da39ccd195f67183`
still has schema1/policy3. Native script SHA256 remains
`8fc86cd540785130f5fc61810a67e7f837dbbd7ebba8e8b196172777679f887b`.
F remains absent. Accept E5 driver constant rebinding to these selected identities;
invoke current public wrappers so generation checks run normally. Do not reuse a
superseded prepared invocation, edit native state, weaken refusals or change
ownership/recovery rules. Reset/start and independent four-guest/root/provenance
acceptance remain exactly as designed. This input acceptance is not deployment
release before the remaining A/C gates.

The [proposed graph delta](devcluster/e5-preflight-0312/proposed-graph-delta.json)
also updates vpsfStatus from `e4881a932ad20bab141e3203afb985e96a51b1da` to
`5723f8a40d458a847d4efc4f6b30d98f22a6bca5`, besides the two 0.31.2 application
paths; OS f4e55a13, nixpkgs/follows and the other 17 nodes remain unchanged.
Canonical local Git lacks these status commit objects, so no commit-history
conclusion is claimed. Exact already-retained source trees were located locally:

| Revision | Retained source | NAR hash |
| --- | --- | --- |
| e4881a93 | `/nix/store/8z9sv8rm8pkpnxsgm1589lsb99j709ld-source` | `sha256-HavQ0U+sHtEzNr5jC+ShSyIxUzFlRBhX4xYoEs96EG4=` |
| 5723f8a4 | `/nix/store/fhjlb8yd2qv4chkcyhs6df9xd45z6b2z-source` | `sha256-OP5Uztub5U+uyyR5nF4cf+uelPLhRur9y+cy7Oc1Q2M=` |

Nix's cached revision/tree/NAR records and registered store hashes bind those
sources to the retained locked inputs; fresh read-only `nix hash path` confirms
their exact NARs. All 90 files, types and executable bits were compared. Only
`go.mod`, `go.sum` and `nix/package.nix` differ: go-i18n/v2 2.6.1→2.7.0,
indirect x/net 0.61.0→0.62.0, vpsadmin-go-client 1d9240f→73f164dd, and the
normal vendor hash `sha256-3Xjm…`→`sha256-f6Xzt…`. The Go SDK change is the
already-proven README-only revision. Status application/handler/template/config/
schema code and flake lock are unchanged. The optional local-SDK vendor-hash arm
is unchanged and no local SDK source is selected by this deployment.

Accept this bounded dependency refresh for the new disposable cluster; no
compatibility blocker was found. The localization/network dependencies really
change, so no binary or dependency-semantic equivalence is claimed. The normal
native build must verify its vendor hash and retain the package's ordinary Go
checks. Include status health/render in the existing poststart smoke, with EN/CS
on its existing locale route where applicable. No independent status campaign,
new package worktree, input override or provider project is needed. Final native
source/artifact identities still come from the actual canonical-path build;
proposed alias NARs are provisional until final writers finish. No network fetch,
native/status/guest probe, build, source/ref or cluster mutation was performed
by architect0 for this assessment.

## 2026-10-28: authorized development HaveAPI documentation deployment

The 2026-10-29 M8 amendment below selects the next development candidate after
the retained d67 operation's safe boundary. The d67 pin and checks in this
section remain their exact historical evidence; they are not M8 results.

**Current development pin and boundary.** Peer final handoff `60f51b8c` releases
HaveAPI `d67bebcb37f2d4558a97caa208465147da19dbef`, tree
`cd91bf06fd14d297aaa2470844f679f0998d85f9`, based on
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`, for consumer packaging and HTTPS
validation. Architect confirmed that exact tree and the remaining M6 interface
from already-present canonical objects; A0 owns fetch/remote readback and package
selection. No further deployment confirmation is needed. This is a development
candidate, not full producer release/CI/performance readiness: installed-snippet,
generated-wire/MSRV and direct f6-to-final performance gates remain producer-owned
and running at handoff. They do not block stable consumer packaging or authorize
a duplicate campaign. Final consumer quick checks, committed affected review,
package/services checks and actual HTTPS acceptance still precede use.

Earlier reference and sequencing, retained for lineage:
`35c1fb964735639c0873aacf078e18569f05f9bc` (tree
`756b61de87833d8ded478b5d7785618671b4ddcb`, base
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`) is a contract reference, **not the
selected pin**. Peer message `752ae063-1840-4dd3-b635-ec4c3407ecf9` supersedes
the earlier test-only successor: milestone6 now changes documentation auth/UI.
The final source/contract gate is now satisfied by d67 above; bind its full
SHA/tree, published branch readback and final supplied evidence. Do not fetch a moving branch
as the deployment identity. No peer worktree, upstream source change, release,
default integration, production KB publication or lifecycle action is included.

The inspected final contracts are
[`doc/documentation-oauth.md`](https://github.com/vpsfreecz/haveapi/blob/d67bebcb37f2d4558a97caa208465147da19dbef/doc/documentation-oauth.md)
and [`doc/documentation-ui.md`](https://github.com/vpsfreecz/haveapi/blob/d67bebcb37f2d4558a97caa208465147da19dbef/doc/documentation-ui.md).
Milestone6 requires OAuth-only HTML documentation while ordinary API/OPTIONS
Basic/token behavior stays unchanged, slashless version-root normalization,
README at `/doc`, visible selector values, dotted sidebar identity, and a combined
theme/account menu without wider sidebar. Peer message
`7f5332c3-44a8-4690-b7f2-bef2f0167aa1` settled the behavior below, now confirmed
in final d67. **35c's Basic-first HTML acceptance is superseded.** A0 may select
the exact released development pin under lead release. Activation waits for the
consumer gates, not another source-contract brief. No source was selected or
deployed from35c.
All five gems deliberately declare 0.31.0. Comparing released 0.31.2 to f6
shows version/release-policy changes, with the Go transport-name fix and TS
selected-subtree normalization unchanged. The feature adds simple/thorough
examples and changes HTML navigation; preserve those intentional changes.
Check the final successor's actual source, not numerical version ordering.
Keep released PHP/legacy JS/React dependencies, React `2e32c814...`, SDKs, and
generated TS SDK0.1.1/runtime0.30.2 unchanged. No schema export or SDK regeneration.

**A0: one isolated consumer package, based on deployed API
`8102179cf7f7e9bb534965c8acb3e02ef723045f`.** Preserve all published refs,
old checkouts, private configuration, ignored locks and rooted E5 closures.
Prepare an ordinary new owned successor; consolidate this development-source
stream without rewriting the published 0.31.2 boundary. Files:

- `api/Gemfile`, generated `packages/api/Gemfile`, effective lock and
  `packages/api/gemset.nix`: one canonical Git source at the full final revision,
  explicitly selecting `haveapi`, `haveapi-client`, `haveapi-go-client`,
  `haveapi-rust-client`, `haveapi-typescript-client` from their five sibling
  gemspecs. Use normal Bundler/bundix Git source hashes and nested gemspec
  discovery; all five must resolve to the same revision and source hash.
  Do not retain a competing RubyGems selection of any of these five.
- `packages/api/common.nix` and, if useful, one small adjacent HaveAPI gemConfig
  file: retain the Git-source install convention and add the server preparation
  hook that runs repository-root `make doc` before server packaging/install.
  `Makefile:doc` calls `utils/copydoc.sh`, requiring make, shell and Ruby/ERB;
  it generates `servers/ruby/doc/json-schema.html` and copies shared Markdown
  and PNG files. Preserve the whole source until nested gemspec evaluation and
  the existing `git ls-files` packaging step have completed. A raw source mount,
  version range or successful require does not prove packaged docs. Include a
  bounded actual server-gem build/extraction check from this prepared source;
  do not publish archives or require byte equality with the peer's archive.
- `api/spec/lib/vpsadmin/api/documentation_clients_spec.rb` and
  `tests/suite/services-up.nix`: adapt existing full-overview assumptions to
  the final supplied routes (35c reference: `/v7.0/`, `?page=authentication`,
  `?page=resources`, and `?resource=cluster` or `?resource=node`). Preserve actual generator, token-auth, locale and
  anonymous-all/member-filtered assertions; do not weaken them to page200.
- `tests/configs/nixos/vpsadmin-services.nix`: the smallest test/development
  proxy configuration needed for trusted origin and query-free OAuth logging.
  Existing nginx frontend logs and HAProxy `option httplog` can record callback
  queries. Use ordinary nginx/HAProxy configuration to omit query/credential
  data (or disable the relevant request log), without a new proxy framework.
  If the shared module must expose a narrow option, keep changes confined to
  `nixos/modules/vpsadmin/{frontend,haproxy}.nix` and explain that necessity.
- Update `docs/api-client-examples.md` with the supported development-source
  package/config contract. The schema exporter deliberately requires released
  0.31.2 and will fail closed on this branch; leave that guard intact and record
  its temporary unavailability. It is not a deployment prerequisite.

Use the existing per-API gem task, not an all-package dependency refresh.
Preserve unrelated dependency versions and native prerequisites. No new HaveAPI
flake input, overlay framework, provider edit or client implementation is needed.
If the conventional Git installation cannot retain the generated docs, report
the concrete packaging failure before selecting a different packaging approach.

**Before-mount configuration and dedicated client (E3, with A0's public sample).**
Current consumer `api/lib/vpsadmin.rb:45` loads `config/api.rb`;
`api/lib/vpsadmin/api.rb:335` calls `VpsAdmin::API.configure` before mount at339.
Use this existing hook, not an authentication-chain patch. Set
`api.documentation_name = URI.parse(SysConfig.get(:core, :api_url)).host`:
the known display label is `api.aitherdev.int.vpsfree.cz`. It is display-only.
HaveAPI reads OAuth endpoints from default-version provider metadata at mount;
vpsAdmin's authority is actual `core.auth_url || core.api_url`. Record the
nonsecret resolved authorize/token/revoke URLs; do not assume an OIDC issuer
or add `/v7.0/` to `/_auth/oauth2/{authorize,token,revoke}`.

E3 provisions through the normal admin-authorized `Oauth2Client::Create` /
`Update` resource (`api/lib/vpsadmin/api/resources/oauth2_client.rb:82,115`),
using the API client's discovered route and existing strict-CA mechanism.
Use a session-specific name and fresh confidential client credentials;
`is_default:false`, `access_token_lifetime:'fixed'`,
`access_token_seconds:3600`, `issue_refresh_token:false`,
`allow_single_sign_on:false`, exact redirect
`https://api.aitherdev.int.vpsfree.cz/_documentation/oauth/callback`.
Request scope `['all']` in documentation configuration; it is not a new client
schema field. Do not reuse BFF/PHP credentials or alter their clients or the
user's whole-account SSO flag. Save the returned ID and nonsecret ownership
facts privately; repeat preparation reads that exact owned client and updates
only intended fields, refusing a conflicting identity rather than adopting it.
Never use raw DB writes, the React-specific seed or private provider helpers.

Deliver credentials and a stable random **at least64-byte** session key through
ordinary public services SSH with protected stdin/file transfer and atomic
file placement. Use existing persistent API state/config regular files, with
API-readable restrictive owner/mode, outside Git and the Nix store.
`nixos/modules/vpsadmin/api-app.nix:setup` preserves regular private config files
while rebuilding configuration symlinks. Keep a private host rollback copy;
do not print payloads, include secrets in argv, trace commands or save raw auth
responses/HARs. A small `config/api.rb` loads the private values and calls
`documentation_oauth` with the exact redirect, scope, lifetime3600 and initially
`switch_user:false`. Missing optional config leaves OAuth disabled; malformed
present config fails rather than silently replacing secrets. No secret goes
into `config.json` that Nix serializes, writeText, source snapshots or receipts.

Check provider SSO-off and fresh editable username/password entry first;
only then enable `switch_user:true` through the same private config and ordinary
API restart/update. Existing known-device state can still affect MFA. No
`prompt`/`select_account` parameter is supplied. Under settled M6, valid docs
cookieB alone selects the HTML identity; Basic/Bearer/custom/queryA credentials,
including malformed ones, neither override it nor repair an absent/invalid
cookie. The latter is anonymous. Original request headers/params still reach
provider policy unchanged; no bearer injection or consumer header-stripping is
needed. Ordinary API/JSON/OPTIONS/provider endpoint authentication is unchanged.
Docs logout/switch retains origin, CSRF and capability checks; explicit API
credentials do not govern that operation.

**Activation choice and current runtime.** E3 reports selected runtime
`/nix/store/mw2fa43yyjar8hcl5h2zckrjg79rl915-dev-workspace-0.2.0` and provider
`/nix/store/n16b9dxgp5fx3g5xjfvpp00acaybsyzn-vpsfree-dev-workspace-tools-0.1.0`;
architect verified public wrapper/catalog selection and byte-identical public
coordination/native guides against those read above. This is no claim that all
runtime/provider implementations equal E5. E3 owns the bounded current-contract,
generation and input preflight; historical pjmi/kbppy receipts stay historical.
Reuse E3's completed operational preparation at
[devcluster/e4-preparation.md](devcluster/e4-preparation.md), section at line404
(reported SHA256 `f98d968f25e08c70235990094d1320bed1edfde388ce88436c0cd20f83366930`);
no duplicate live preflight/observation is requested by this design.

Prefer parent-owned public `vpsadmin-devcluster update <slug> services` after
all source gates. The provider selects the canonical `vpsadmin` pathname, so a
successor alias alone is insufficient. A0/E3 prepare an ordinary Git branch
transfer/checkout and normal portal registration that retain the canonical root
inode, the old8102 ref and an owned rollback checkout. Before that operation,
prove all live PHP/templates/static files and their dependency inputs byte-equal
to8102, no mounted path move, and no uncommitted/private file loss; transfer only
the reviewed exact final source and its resolved locks. All source development
stays in the isolated successor until this activation boundary. React canonical
2e32 and its registration remain unchanged. If ordinary registration/checkout
cannot establish these invariants, use the already-authorized reset/rebind route
with retained `vpsadmin-live0312`, then a new single/bridge start; do not invent
symlinks, path overrides or private state edits. Reset is fallback, not required.

Parent owns activation and original pending-target recovery. Recheck compatibility,
capacity/cache and complete proposed input graph; preserve the established
resource caps. Public update builds/copies/activates/restarts/refreshes and proves
the services target. Candidate labels alone never establish activation. No reset
to bypass pending/refusal state. Provider F and embedded native metadata limits
remain; no provider fix/install is included. Reuse independent exact-source,
derivation/closure/residency/root proofs, preserving all four guests' evidence.
C1 is needed only if actual native React inputs change or proof needs a bounded
refresh; no React implementation or automatic frontend campaign.

**Checks and acceptance.** A0's quick gate is resolved five-gem source identity,
generated-doc/content completeness, focused mounted documentation/profile specs
in full/core modes, syntax/lint/hooks and final narrow diff/history review.
Test new configuration loading with absent/valid/malformed disposable input;
do not use registered-cluster secrets as fixtures. After all intended changes
are committed and independent review accepts, build the API package and run the
required existing `services-up` check with its updated navigation assertions.
Reuse peer final browser/generator/performance evidence for its exact source;
do not relabel it as our consumer pass or repeat a compiler/fullmatrix campaign.

E3 then uses existing strict-CA curl and isolated NSS Chromium/member harnesses:

1. Bind the final HaveAPI Git SHA/tree/hash through Bundler/bundix, prepared
   server gem/docs/assets, five loaded gem paths and bytes, API package,
   services derivation/closure and actual running services. Version0.31.0 alone
   is insufficient. Preserve Go token code and the supported TS runtime text.
2. Verify trusted HTTPS scheme/host through the actual proxy, normal CA trust
   in browser and Ruby, no callback query/token/credential retention in logging,
   and same-origin token/revoke concurrency. Existing test services have two
   Puma workers/eight maximum threads and native CA trust; check final effective
   values instead of assuming them from defaults.
3. Exercise login→callback→clean documentation URL, account identity and
   authorized resource/search navigation, revoke/sign-out, expiry→public view
   and re-login, plus SSO-off editable account entry and Switch user. Bound
   expiry with a temporary short lifetime for this owned client/config, restore
   final3600 and verify that final selection; no hour-long wait is necessary.
4. Exercise valid cookieB with valid/malformed Basic, Bearer, custom header or
   queryA: documentation GET/HEAD index/version/search remains B. With no valid
   cookie, each is anonymous; no OAuth configuration yields anonymous docs and
   themes-only controls. Reuse focused peer cases and add only the bounded
   mounted-consumer cases needed to prove this seam. Verify unchanged ordinary
   API/JSON/OPTIONS/provider credential/conflict behavior and that a docs cookie
   does not become API credentials. Verify nil authentication clears prior
   request-local user/session state through the existing hook.
   Preserve final failed/cancelled callback semantics using peer tests plus the
   bounded real flow, without reproducing the upstream security matrix.
5. Check final overview/authentication/resource/internal-doc assets. Exact known
   slashless version GET/HEAD roots return308 preserving raw query; actions,
   unknown versions, OPTIONS and mutations do not acquire that redirect.
   `/doc`, `/doc/index`, `/doc/index.md` and `/doc/readme` serve the actual packaged
   README with neutral/no-auth/no-store shell; guides never obtain identity.
   Legacy `_login`/`_logout` GETs are inert303 default-overview redirects with no
   challenge or session clearing. Check one narrow viewport with visible selector
   values, dotted identity and the combined menu without a wider sidebar; retain
   strict-CA PHP+React login/read/logout smoke. Return the
   existing documentation/API and both UI URLs when usable.

No database migration, node/message protocol or persistent API format change is
introduced. The dedicated OAuth client uses existing schema; new encrypted docs
cookies are optional and expire/are ignored by old code. For rollback, first
remove/disable new documentation configuration, restore protected predecessor
config and exact8102 package/source via the same supported public update route
(or accepted reset/rebind fallback), retaining2e32. Revoke the owned docs session
through ordinary OAuth; client removal is not an automatic rollback side effect.
Do not restore private applied envelopes or manufacture roots. Retain old/new
source/closure receipts and report unresolved effects before retrying.

Stopping condition: final peer source is ready, consumer package/review/checks
pass, actual source/assets and HTTPS documentation authentication are proven,
and both existing UIs remain usable. No genuine user choice is currently needed.
This section is the implementation brief, not a claim that packaging, client
creation, checks or activation have run. Lead reports all nine exact0.31.2 CI
workflows passed and E2's monitors ended; this design does not query or restart
that work.

### M6 standard-provider compatibility disposition

Read-only assessment at canonical vpsAdmin
`8102179cf7f7e9bb534965c8acb3e02ef723045f`: **no consumer OAuth adapter is
indicated by the settled contract**. `api/lib/vpsadmin/api.rb:348–352` installs
`HaveAPI::Authentication::OAuth2.with_config(Authentication::OAuth2Config)`.
`OAuth2Config` subclasses the framework's Config (`authentication/oauth2_config.rb:7`),
not its Provider. At inspected HaveAPI35c, `authentication/oauth2.rb:5–6` delegates
to `Provider.with_config`; `authentication/oauth2/provider.rb:62–78` constructs
the standard Provider and injects that Config. Therefore the final standard
Provider's new `authenticate_access_token(request, token)` will be available to
vpsAdmin directly. The custom-provider requirement does not require vpsAdmin to
add a parallel implementation or override its ordinary credential chain.

The existing policy entry is
`api/lib/vpsadmin/api/authentication/oauth2_config.rb:412–416`,
`find_user_by_access_token(request, token)`. It invokes
`Operations::UserSession::ResumeOAuth2.run` and rejects missing users or disabled
OAuth2 auth. `operations/user_session/resume_oauth2.rb:8–23` requires an open
OAuth2 session, matching valid token, active/suspended account, no lockout and no
password-reset requirement. Lines25–46 retain normal activity accounting,
conditional renewal and `User.current`/`UserSession.current` installation. The
dedicated fixed-lifetime client does not enter renewable-auto branches. Scope
filtering remains the existing `api.rb:177–220` pre-authorization hook, using
that current session, followed by the ordinary resource/action role checks.
Do not substitute a raw token/user lookup or bypass these side effects.

**Final d67 source confirmation: no consumer adapter required.** Paths below
are relative to `servers/ruby/lib/haveapi/` at the immutable final revision:

- `authentication/oauth2/provider.rb:138–141` delegates the original request
  and separate cookie token directly to `config.find_user_by_access_token`,
  rescuing `HaveAPI::AuthenticationError` to nil. Ordinary `authenticate` at
  115–135 retains request credential extraction and TokenConflict handling;
  only the existing final callback is factored through that method. Other
  unexpected exceptions are not silently converted to successful auth.
- `authentication/chain.rb:51–62` selects only `@instances[version]` providers
  named `oauth2` that implement the explicit-token method; unsupported versions
  or custom providers yield nil, without invoking Basic/Token fallback. Its
  existing normal `authenticate` at38–48 is unchanged.
- `documentation_oauth.rb:133–148` checks origin/method and valid session cookie,
  then passes `handler.request` unchanged plus its token to that chain. Missing
  cookies yield nil; rejected cookie tokens clear the session cookie. There is
  no bearer-header injection or API credential selection on this path.
- `documentation_helpers.rb:44–49` resets handler identity, performs the docs
  lookup, then calls `post_authenticated` and locale resolution for every normal
  user **or nil** result. The unconfigured fallback at186–187 returns nil.
  vpsAdmin `api.rb:117–126` therefore clears thread-local user/session on nil and
  sets PaperTrail identity. This is not an ensure-handler for arbitrary raised
  exceptions. `server.rb:88–103,517–518` retains explicit negotiated language
  when supplied and restores request locale afterward; do not assert that
  cookieB overrides an explicit language header.
- Version rendering (`documentation_helpers.rb:56–66`) authenticates before
  describing and before search-index/conditional handling. Index handling
  (`server.rb:531–559`) uses the per-version documentation method. Ordinary
  root/version OPTIONS (`562–598,691–700`), actions (`786–797`) and action
  OPTIONS (`856–869`) retain their normal authentication paths. Provider routes
  (`authentication/oauth2/provider.rb:85–112`) retain their endpoint handlers.
- Legacy GET routes (`server.rb:635–640`, with Sinatra's HEAD handling) are
  inert303 fixed-default-overview redirects. Exact known slashless version
  GET/HEAD roots (`667–679`) preserve the raw query in308; control bytes reject.
  README aliases (`601–607,619–620`) and guide rendering call
  `shared_documentation_helpers.rb:7–14,32–44`, which uses packaged content and
  a neutral/no-auth/private-no-store shell.

This closes the bounded source-interface question, not consumer runtime proof.
Keep the existing bounded mounted/HTTPS assertions, including repeated worker
user→nil cleanup, cookieB/headerA separation and API/OPTIONS independence.

Stable preparation is reported committed at A0 `4a7924c16f48132a4017b9104ba321245c07d765`;
its nine-file public package/config/proxy/doc preparation is separate from final
source selection and acceptance. E3's existing operational preparation remains
the execution input. Peer auth120/core51/search55/assets results overlap and are
reported upstream evidence only; no local checks or verification totals are
claimed here. The supplied final five-commit lineage is4363d111/260e3ea8/
222812c0/07c0d0a6/d67bebcb. Lead accepted the producer's reviewed predecessor
range and subsequent folded CSS/test changes with focused/equivalence evidence;
architect did not perform a broad re-review. Producer five-gem HTTP/15-profile/
four-width browser results remain supplied evidence. A0's final consumer
packaging/quick/commit, reviewer0's affected review, and bounded postreview
services/HTTPS/source-to-runtime acceptance remain. No additional adapter,
framework, upstream test or provider work is indicated; deployment authorization
persists.

### Bounded VPS Index example correction

At both8102179 and preparation4a7924c, the identical
`api/lib/vpsadmin/api/resources/vps.rb:137–139` sample has
`user: { id: 1, name: 'somebody' }`. The declared owner reference at14–15 uses
User with `value_label: :login`; `api/models/vps.rb:16` is `belongs_to :user`.
User Show (`resources/user.rb:241–244`) includes `:all`→`:common`→`:writable`,
which declares `login` and `full_name` at10–11, not `name`. Smallest correction:
change only that sample key to `login: 'somebody'`, retaining its value and id.
This changes documentation/example metadata (including descriptions that carry
examples), not live VPS/User response fields, schema, authorization or migrations.

A0 may include this at the next safe source boundary before final review.
Use the existing mounted-profile seam in
`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb` for one focused Go
VPS Index example regression: render the actual declared sample through the
configured automatic profile and require code rather than the unknown-field
fallback. Do not relax schema checking or copy a corrected synthetic sample
into the test. A further limitation, if observed, needs its own concrete
diagnosis; this static assessment does not claim a successful renderer run.
No generator audit, SDK regeneration or M7 navigation dependency is added.

### Ready packaging amendment: nested Git gem discovery

A0 owns this narrow correction before final commit/review. The selected nixpkgs
source `/nix/store/5b2ic4sxjc2lzgxk4hninyw22r5gv5qr-source` has no supported
glob argument in `pkgs/development/ruby-modules/gem/nix-bundle-install.rb`:
lines42–55 build only name/version/uri/ref; lines115–121 construct the Git source
and install its selected spec. `buildFlags` are extension arguments. Adding
`glob` to bundix metadata alone cannot reach that constructor. Bundler2.7.2 at
`/nix/store/k8gfb9iip51zm4sy50b0s8yqgrsfr0hz-bundler-2.7.2`, under
`lib/ruby/gems/3.4.0/gems/bundler-2.7.2/lib/bundler/source/`, reads
`options["glob"]` in `git.rb:15`; `path.rb:14` defaults to
`{,*,*/*}.gemspec`, missing all five two-directory-deep HaveAPI gemspecs.
`path.rb:185–201` can synthesize a fake gemspec, so exit0 alone is insufficient.
This is installed-package correctness, not an upstream or runtime auth change.

**Implementation boundary:** `packages/api/common.nix` plus a small adjacent
`packages/api/haveapi-git-gemspec-glob.rb`. Use the existing per-gem `gemConfig`
extension point (`bundled-common/functions.nix:83–84`) and the normal
`buildRubyGem` preInstall/postInstall hooks (`gem/default.nix:208–239`). Apply
only to Git-source `haveapi`, `haveapi-client`, `haveapi-go-client`,
`haveapi-rust-client`, and `haveapi-typescript-client` in this API bundle.
Preserve other gem configuration and existing hooks. In preInstall, retain the
prior RUBYOPT set/unset state and value, then add an absolute `-r` for the small
Ruby file. Restore RUBYOPT before the inherited postInstall hook; never emit
this preload into runtime wrappers, binstubs or setup hooks. On install failure
the isolated builder fails; no alternative installation or source is selected.

The Ruby file loads Bundler and prepends only `Bundler::Source::Git#initialize`.
For those exact five names, and only when no explicit `"glob"` key exists, pass
a copied options hash with `"glob" => "**/*.gemspec"` to `super`. Otherwise pass
the original options unchanged. Leave Path sources, constants, GitProxy,
fetch/copy/install logic and unrelated gem names unchanged. This small build-time
compatibility shim fills the missing installer option; it is not a copied
installer, global nixpkgs/Bundler patch or new packaging framework. Keep the
standard installPhase. Keep server-only `make doc` in preBuild before Nix's
`git add .`, all five original nested gemspecs, and the single d67 whole-source
revision/hash. No root gemspec wrappers, source-subdirectory overrides,
repackaging, overlay, dependency refresh or HaveAPI source edit is needed.

**Quick gate, A0:** syntax/format checks plus one bounded disposable smoke using
the actual selected `nix-bundle-install.rb` path and Bundler2.7.2 above, not a
reimplementation. Exercise the preload with a two-directory-deep gemspec and
require its real installed gem metadata/library path. Check that all five names
receive recursive discovery, an explicit glob survives, unrelated Git/Path
behavior is unchanged, and the hook restores initially unset and existing
RUBYOPT. A concise existing-style standalone check/receipt is sufficient; no
new framework or repeated full/core documentation tests. Bind the selected
installer path and Ruby/Bundler identity in the evidence. A0 may use the already
prepared exact source for the smoke if smaller than a fixture.

**After committed quick checks and affected independent review:** build the
normal final API package with this gemConfig and run the already-required
services-up package/docs check. Inspect all five actual Nix outputs' real
nested gemspec paths, names/versions/require paths and shared d67 source identity;
reject placeholder metadata. Through the packaged Ruby environment, verify the
five actual loaded library paths and the server's generated JSON schema,
shared guides/README/CSS/JS against the retained prepared-source receipt. Keep
the prior raw-archive/full8/core8 successes for their actual scope; they do not
substitute for this Nix install proof. No new compiler/performance/browser
campaign. The amendment changes build discovery only: no schema, migration,
API/SDK contract, activation ownership or rollback8102/2e32 change. Architect
performed static inspection only; A0's real Nix install remains unverified.

### DEV-R1: bypass Varnish on the documentation API route

Lead accepted this bounded review remediation against frozen consumer
`c413b07cf8120eb6159b4249b150a6aff99ecaed`. At
`tests/configs/nixos/vpsadmin-services.nix:664–668`, the API frontend still sends
all traffic to `/run/varnish/vpsadmin-varnish.sock`. The VCL in
`nixos/modules/vpsadmin/varnish.nix:89–98` returns pass for non-metrics requests;
this changes cache handling, not Varnish shared-memory logging. Request/backend
URLs and headers, and backend/client response headers, can therefore retain
callback code/state, credentials, cookies and response Location/Set-Cookie.
The nginx/HAProxy log controls do not cover that intermediate process. This is
static source evidence; no live disclosure or log inspection is claimed.

**A0 fix after lead release and completion of the frozen review:** change only
the API frontend backend address in that test/development configuration to
`unix:/run/haproxy/vpsadmin-api.sock`, with a short comment explaining the VSL
boundary. This uses the existing `vpsadmin.frontend` backend interface and the
same direct route already used by `auth.test` at671–674. Bypass Varnish for the
whole API virtual host, not just the callback: documentation cookies also travel
to version/index/search pages. Neither request nor response values then enter
Varnish through this public API route. Preserve trusted proxy headers, nginx
API/auth query-free access logging and disabled error logging, and HAProxy's
API `no log`. Preserve PHP/React/auth routes and all normal API authentication,
authorization and request/response handling.

Update the existing proxy paragraph in `docs/api-client-examples.md` to explain
the direct route and its constraint. Do not alter the shared Varnish/frontend
modules, service enablement or provider. The selected nixpkgs Varnish module
does expose `services.varnish.extraCommandLine` (line185), but an instance-wide
log-mask policy is unnecessary here; partial URL/header masks also require more
coverage than removing this already-pass-through hop. Deliberate compatibility
cost: `/metrics?…` on the test/development API no longer gets the VCL's 60-second
cache (`varnish.nix:100–111`); it reaches the same API backend directly. This
does not change reusable production cache defaults or PHP/React routing.

**Focused quick acceptance, A0:** extend the existing configuration-evaluation
check using the actual final services configuration and imported frontend and
HAProxy modules, without copying their rendering logic. Require the generated
nginx `api_test` upstream to contain only the direct HAProxy socket, the API `/`
location to select that upstream, and no Varnish hop in any API/auth proxy path.
Check the generated API HAProxy frontend still has `no log` and selects the
same API backend; retain the nginx safe-log/trusted-header assertions. Compare
the PHP/React-related route values with c413 for no change. This is one bounded
generated-configuration check plus normal formatting/hooks, not another auth
or browser campaign. The normal postreview API/services gate remains required.

**Later actual acceptance, E3:** in the existing HTTPS documentation OAuth
batch, bind the running nginx and HAProxy configurations to the final selected
closure and confirm the direct route, including any native overrides. During
the bounded callback/login/logout flow, verify that request query/header and
response cookie/Location values are absent from nginx logs, HAProxy journal and
VSL. Use non-secret unique markers for deliberate negative probes and compare
real sensitive values privately; retain only redacted results/counts, never a
raw credential-bearing VSL dump. Bind absence evidence to an active observation
window and the actual route/configuration; a missing log reader is not a pass.
Reuse the existing PHP/React smoke and report the metrics-cache tradeoff rather
than claiming cache equivalence. No extra live probing is released by this brief.

The correction stays within the reviewed proxy/logging boundary and two already
changed files. After A0's normal fix commit and focused checks, lead can apply
the review's narrow-fix acceptance policy to DEV-R1; no new all-lane campaign is
indicated. A changed module interface or broader routing policy would require
fresh affected-lane review. No migration or persisted format changes. Retain
8102/React2e32/config/closure rollback; do not restore the credential-logging
Varnish route while development documentation OAuth remains enabled. Keep the
route on rollback, or retire that OAuth exposure with its matching old API
configuration first. Activation stays parent-owned. Current kdqm runtime and
catalog89a06 are guide observations only, not provider equivalence or deployment
proof. Architect changed this design only and ran no builds/tests/live queries.

### Postreview capacity disposition: retain the existing wait

For accepted consumer `cba626581a698256e873319983ac51312f40398c`, retain A0's
single utility87249/thread01a18450-3f01-7312-aa91-6e32c10ea10f and its current
80GiB disk gate. This is a recommendation to lead, not a command release.
The supplied receipt has80,531,492,864 available bytes (about75GiB), below
85,899,345,920 bytes; the gap is about5GiB. Memory/shared-memory/CPU checks pass.
Swap0 is recorded information and is not a new acceptance condition.

`package-haveapi-development/vpsadmin/postreview/run.py:capacity` checks
`statvfs('/tmp').f_bavail` before source archiving/rooting/build/probes and again
before the services runner. The same literal80GiB appears in the retained
`package-a-integration-refresh/postreview/{services,api-auth,php-auth}/executed-harness.py`.
It is therefore a conservative inherited admission envelope, not a measured
minimum, allocated VM disk size, native runner requirement or reserved space.
It protects starting headroom for the batch's temporary files/build preparation
and VM writes. It does not itself prove Nix-store filesystem capacity, enforce
a runtime disk quota or continuously stop builds at a reserve threshold.

The current batch serializes the normal API build and installed-five-gem/docs
proof before services preparation/start, with Nix jobs1/cores2. Current
`tests/suite/services-up.nix` defines one services machine; retained0312
`postreview/services/test-config.json` records8GiB RAM/8CPUs, no additional
disks and8192MiB native memory/shm requirements. The existing runner retains
16GiB memory/shm caps and8CPUs. These bound concurrency and guest memory, not
peak host disk use. Five whole-source Git gem installations and generated docs
are new compared with released0312 package outputs; cached historical results
cannot establish their final build-scratch/closure peak.

Retained `initial-capacity.json`→`services-capacity.json` host-free-space pairs
show107.52→102.80GiB for integration-refresh,91.92→87.67GiB for0311 and
83.92→80.02GiB for0312. Their differences (4.73/4.25/3.90GiB) are **not** owned
usage or high-water measurements: concurrent host activity and temporary build
peaks are unaccounted for. The0312 services success proves that run with its
recorded admission checks, not a lower safe minimum. No retained receipt gives
an exact-current-workload peak plus an explicit reserve. Selecting75/64GiB or
splitting off the package under a smaller arbitrary threshold would therefore
be an unsupported policy change, not an evidence-based correction.

Shortest supported path: let the original interruptible admission wait continue
until the accepted gate passes. Do not change its executing script, add another
watcher, manufacture a timeout/failure, retry the batch, or perform cleanup/GC,
root deletion or another session's intervention. Existing kernel-build and
source/test-identity escalation, ordinary command-failure/no-retry handling and
effect reconciliation remain unchanged. If lead later chooses cancellation or
receives concrete capacity evidence for a different envelope, A0 must first
stop/reconcile this exact wait and prove it cannot launch a child before one
fresh successor is released; no hot threshold edit. This assessment inspected
own static scripts/configs/receipts only and releases no capacity probe, source
edit, build, lifecycle or infrastructure action.

### Maintenance alias: single-origin OAuth acceptance boundary

E3's selected kdqm/ih7 provider evidence in `devcluster/e4-preparation.md:497`
identifies a separate `frontend.api.maintenance` route through Varnish
(`test.nix:1541–1545`, default host `api-tmp.aitherdev.int.vpsfree.cz`). The
main consumer API route from acceptedcba survives the provider import/domain
override. Do not describe all aliases as bypassing VSL. No provider equivalence
or deployed configuration proof follows from unchanged guide bytes.

No further consumer correction is required for the specified documentation
OAuth flow, **provided the following single-origin boundary is verified before
enablement**. In exact HaveAPId67 `servers/ruby/lib/haveapi/documentation_oauth.rb`,
lines96–97 derive one origin from the configured callback;124–126 bind encrypted
pending/session purposes to client, callback and mount. Controls151–158, login
redirect parameter174–175 and return URLs305–312 use that fixed origin, never the
request's alias. Cookies350–358 and387–389 are Secure/HttpOnly/mount-scoped with
no Domain attribute, hence browser host-only. Authentication136 and260–265,
login167, callback186 and logout216 reject the other origin. Those checks are
identity controls, **not proxy-log redaction**. The provider verifies the
registered client redirect at `authentication/oauth2/provider.rb:171–176`.
vpsAdmin `authentication/oauth2_config.rb:419–420` obtains provider base URL from
actual `core.auth_url || core.api_url`; docs OAuth mount118–123 uses its metadata.

E3's existing final acceptance must bind the protected redirect configuration
and ordinary client registration to exactly
`https://api.aitherdev.int.vpsfree.cz/_documentation/oauth/callback`; the actual
authorize/token/revoke endpoints must use the intended primary API/auth origin,
with credential-bearing paths going directly to HAProxy. Verify effective
nginx virtual-host/upstream selection for those hosts, including native
overrides, and no redirect/rewrite through the maintenance alias. Privately
verify actual pending/session Set-Cookie attributes have no Domain and that
the existing login/callback/logout/revoke browser/server request chain never
uses the alias. Even entry from anonymous alias documentation must lead to the
absolute primary login URL, not establish an alias session. Retain the existing
bounded request-and-response logging window; no new alias probe is released.

The supported browser flow therefore does not send primary documentation
cookies to the alias, register its callback there, or send provider credentials
there. This does not protect manually copied Cookie/Authorization headers or
callback URLs sent to the alias: Varnish may log them before origin rejection.
Do not send such values during testing or claim alias log safety. If actual
configuration instead needs credential-bearing alias traffic, stop OAuth
enablement and return the concrete delta for a consumer routing decision;
do not broaden callback registration or rely on origin rejection. That is an
activation prerequisite, not a new source/package gate while it remains absent.
Frozen cba and main-route DEV-R1 acceptance remain unchanged. The capacity
disposition above also remains unchanged: sole utility87249 at its original
80GiB admission wait, no threshold edit, duplicate watcher or cleanup release.

### Actual Git-output collision: align preparation and remove staging indexes

This supersedes the server-only preparation requirement above. Accepted consumer
`cba626581a698256e873319983ac51312f40398c` selected exact HaveAPId67/treecd91,
source `/nix/store/aqv56rhl85ivbgfn340cqf7wakzbfv7w-haveapi-d67bebc` (hash0a2y).
The later postreview-continuation utility81160 ended1 after111.89s: all five Git
gem outputs built, but rubyEnv `qis6j1j0k7zfqdlzrik7gjgbxza98adj` failed255
merging the shared repository cache index. The API wrapper/probe did not run,
API_PACKAGE_PROOF_PASS was not reached, and services never started. A0 reconciled
owned effects and retained source/lock equality and roots. The earlier capacity
wait is historical, not an active operation inferred by this design. Preserve
the original failure in `package-haveapi-development/vpsadmin/postreview-continuation/`:
`built-five-gems.json`, `collision-differences.json`, `failed-env.log` and
`reconciliation.json`.

**Cause from actual output/source evidence.** The selected nixpkgs
`gem/nix-bundle-install.rb` copies prepared `.git` into the per-output Bundler
cache and the whole repository into its common `bundler/gems/haveapi-d67bebcb37f2`
path. Bundler2.7.2 `Source::Git#checkout` then serializes every recursively selected
gemspec in that checkout, not just the installed gem. A0's server/client diff
has only two differing Git indexes and `servers/ruby/haveapi.gemspec`; the server
additionally contains nine generated shared doc files, while the Ruby client
has its own `bin/haveapi-cli`. The serialized server spec's file list differs
by exactly those nine docs. Server-only `make doc` therefore makes overlapping
repository content inconsistent. The actual v2 indexes each have858 entries;
their first `.editorconfig` entries have the same OID/mode/path but different
ctime values1793225803.784662933 and1793225785.242547978. These are concrete
build stat differences, not different pinned source revisions. The selected
`buildenv/builder.pl:111–126,200–206` accepts collisions only when content and
permissions match; ignoring collisions could choose stale server metadata.

**A0 implementation, after lead accepts this brief:** change only the existing
HaveAPI gemConfig in `packages/api/common.nix`, with a concise rationale comment.
Run the existing root `make doc` preBuild for **all five** Git gems before the
normal `git add .` and installer serialization. Keep the normal installer,
recursive discovery shim, one immutable whole source/hash and all inherited
hooks. In the existing postInstall, after installation/metadata emission and
RUBYOPT restoration, remove only these two staging files in that gem's own output:

- `<install-path>/.git/index`, obtaining install-path from the installer's
  `$out/nix-support/gem-meta/install-path`;
- `$GEM_HOME/cache/bundler/git/haveapi-<URI-hash>/index`, the one matching
  HaveAPI cache entry under this output (current hash suffixa36ce581219fc007495b4ac8c77a2a87b7c3fb6d).

Use exact output-scoped paths/a narrowly matched single cache entry; check the
expected path shape/count and fail on an unexpected layout. Do not delete an
entire `.git`, cache directory, source tree, metadata, gemspec, executable or
asset, and do not touch the fetched source or retained failed outputs. Keep
objects/HEAD/other Git metadata and per-gem `nix-support` intact. Preserve prior
RUBYOPT states and inherited postInstall execution. No ignoreCollisions, source
slicing, shared-closure redesign, installer copy, new helper framework, pin or
lock change is needed. Reconsider only if the actual new output exposes another
specific conflict; do not preemptively broaden the removal.

**Why these indexes are build-only here.** The installed five gemspecs inspected
in both retained outputs are already serialized Ruby specifications, with no
`git ls-files` evaluation. Bundler's `Git#specs` loads these from the installed
checkout; normal runtime leaves Git operations disabled. `Git#git_proxy` passes
the lock's full `revision` into GitProxy, whose `revision` returns that value;
`installed_to?` checks populated checkout directories. None of these runtime
steps consumes the staging index. The index is needed earlier for source
gemspec evaluation, which is why removal must follow normal installation and
serialization. This does not promise that a read-only installed output is a
development checkout for restaging/repackaging or mutable bundle updates.

**Quick checks and review:** A0 uses normal Nix formatting/parse/hooks and a
bounded evaluation of the actual five gem derivation hooks: all five now prepare
docs, only the five Git outputs receive the two-file removal, and existing
RUBYOPT restoration/discovery remains unchanged. Against the retained real
outputs, confirm the chosen two paths exist and the removal scope cannot include
libraries/specs/cache contents. If checking index-free spec loading quickly,
use disposable copies of those real installed specs/output paths, never mutate
store outputs; do not start a new fixture framework or repeat mounted full/core.
Do not claim these quick checks establish new-output equality. Commit normally
and give the same independent reviewer the packaging delta and failed-output
evidence before a long build. This new preparation/installed-metadata policy
needs affected general, architecture/scope and package runtime/rollback review;
reuse unrelated OAuth/proxy review. It is not merely confirmation of DEV-R1.

**Postreview next milestone:** one normal final API build with strict default
buildEnv collision checking. Compare the actual five shared checkout/cache
trees' overlapping files and permissions; require identical serialized specs
and generated docs, absence of only the two indexes, preservation of CLI/bin
and per-gem metadata, and the same d67 source in all derivations. Then the actual
API wrapped Ruby must pass existing five-gem source/load/docs/assets and Bundler
activation proof from its frozen lock without fetching or restaging. Retain
new derivation/input/output roots and the failed originals. Only after that
API_PACKAGE_PROOF_PASS proceed to the existing services-up gate on the same
final package. No additional compiler/performance/browser campaign. This is
packaging only: no API/schema/migration/auth changes, no deployment yet, and
released8102/React2e32/config/refs/closure rollback remains unchanged. Architect
performed only static source/retained-output inspection and this design edit;
no implementation, build, test, retry or cleanup was launched.

### 2026-10-29: M8 successor adoption and one final development deployment

**Ready bounded brief.** Under the existing user deployment authorization,
select published HaveAPI `e5ea07028e48a6936b947c172fa89eca15e3a416`, tree
`543cd44c4a1863489ae2289d2a8769a60e7c1b85`, from canonical SSH
`git@github.com:vpsfreecz/haveapi.git`, branch
`2026-10-27-api-documentation-redesign`. Architect inspected already-local exact
objects; A0 owns normal remote identity verification before selection. Commits
9e1d86f1/15455a58/e5ea0702 share basef6e5 with d67: this is a substantive
replacement, not descendant or equivalent source. Supplied full-base change is
142paths; actual d67→M8 diff is78paths/+2986/-703. Keep exact d67 recovery ref
`recovery/2026-10-27-api-documentation-redesign-external-d67-20261028t204550z`
and consumer3ae74281/tree3c047743 receipts/refs/roots. Do not activate d67 first.

A0 reports the d67 operation reconciled: actual API dm232/artifact binding and
five-gem/docs/runtime proof passed;29 services assertions passed, stale root
assertion30 was interrupted and four later assertions did not run. These remain
partial d67 results, not a full services pass. The sole pending source edit is
the lead-authorized root oracle correction; do not repeat the d67 batch.

**Contract and boundaries confirmed from M8 source.** OAuth session/config,
auth Chain/Provider, Ruby client/schema, Context/profile/structural schema and
search-index implementation, five gemspecs/VERSION, Makefile/copydoc and Nix
inputs are unchanged from d67. All five gems remain0.31.0; version equality is
not source equality. No adapter, migration, credential provisioning change or
dependency upgrade is indicated. Retain reviewed all-five make-doc preparation,
recursive discovery, two-index removal and RUBYOPT restoration unchanged.
Keep SDK0.1.1/runtime0.30.2, PHP/React/legacyJS/CLI and exporter unchanged.

Changed documentation includes navigation/permalinks, per-group detail choices,
copy controls, literal example credentials, error-handling forms and validator
display. The new optional renderer query preserves old/custom adapter behavior;
we have no consumer custom adapter to add. M8's `documentation-ui.md` defines
singleton selector behavior, no-JS section links and stable legacy fragments.
Its `views/index.erb:1–9` is byte-identical to d67: `<h1>API versions</h1>` plus
version help links. A0's retained-body oracle `<a href="/v7.0/">Version 7.0</a>`
matches this consumer mount; retain that correction. Do not change the product
to satisfy the obsolete `API description` assertion.

**A0 source package, after lead release:** update `api/Gemfile`, generated
`packages/api/Gemfile`, packaged/effective ignored lock and `packages/api/gemset.nix`
to one exact M8 revision and newly computed common source hash for all five.
Preserve all unrelated dependency entries. Update only affected assertions in
`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb` and the root assertion
in `tests/suite/services-up.nix`. Concrete intentional changes: Go emits
`SetExistingTokenAuth("example-token")`; TS uses literal credentials and
`api.cluster.public_stats()` rather than bracket accessors, and no longer embeds
the runtime-version comment. Check actual code/limitation status and profile
contract, not obsolete wording; keep SDK pairing verification in package metadata
or its owning documentation. Preserve Go Symbol/String transport regression,
real VPS sample, member/admin visibility, locale, cookieB/headerA separation,
OPTIONS independence and user→nil cleanup. Add only a compact mounted assertion
for real M8 section/permalink and per-example detail metadata if existing checks
do not cover that consumer integration. No schema relaxation or generated SDK work.

Before consolidation preserve exact3ae. Consolidate unpublished d67→M8 pins into
one final development-source update atop the supported published8102179 stream;
carry the final configuration/proxy/index-collision fixes without reintroducing
intermediate failures. Preserve old refs and document old/new ranges; do not
rewrite a published ref if publication occurred unexpectedly—use a distinct
successor under lead disposition. A0 owns all source/Git/history work. Reviewer
receives the complete final series and no-migration conclusion. No new upstream
fix/ref/registration, default integration or production release is authorized.

**Verification order and reuse.** Quick: exact-five source/hash/lock checks,
existing focused mounted documentation spec in full/core modes, the root-oracle
check, syntax/format and normal hooks. Update expectations only for documented
M8 behavior. Retain unchanged packaging/proxy review evidence; changed renderer
and dependency behavior requires same-reviewer affected consumer/history review
after final commits/quick checks, before long verification. Review the pin,
assertion changes, content/privacy and source/package binding; do not duplicate
the producer's four-lane upstream review or reopen unchanged auth/provider work.

Postreview, one normal final API/package→services batch must prove all five
actual M8 derivations/serialized specs/shared checkout contents, strict
collision-free buildEnv, frozen Bundler/load paths and generated docs/assets.
Bind the final tracked consumer source, complete inputs, actual package and
services closure. Old d67 output hashes cannot satisfy changed source/assets;
reuse only exact unchanged dependency/config evidence. Run services-up through
all assertions at the final M8 consumer head, including the corrected version
index. Preserve both partial d67 evidence and new results without adding counts.
No extra raw-archive/compiler/browser matrix is required merely to repeat an
already-covered boundary.

**E3 and parent deployment package:** after final review/package/services and
no-writer handoff, use the previously accepted supported canonical binding and
public services-update/recovery procedure, subject to actual selected guide and
effective-config checks. Parent owns activation. E3 provisions the dedicated
client/private configuration normally and performs the existing strict-CA OAuth,
worker cleanup, primary-origin/host-only-cookie/no-maintenance-alias and
request/response-log acceptance. Retain rollback8102/React2e32/private config and
rooted closures; remove the optional docs configuration before released rollback.
M8 uses the same docs-cookie format/key purposes as d67, so no state migration or
key rotation is implied. C1 has no source task; actual changed native React
output identity, if encountered, uses the existing bounded provenance procedure.

Bind the actual served M8 CSS/JS to these source-confirmed SHA256 values:
CSS `7c4ba9357a31cdfa988cd6df599d748856db5b847f64ccac24562bcc4bf0b5e4`,
JS `ff3530e27fe60eeadacc7d9d12ce05e81d29e00bdf55954cb2fa4171b5e1f8ab`.
Extend the existing browser smoke with one real resource navigation/search and
permalink/copy/detail-selector/theme sequence; verify displayed and copied code
agree and use public placeholders. Check the existing narrow viewport without
creating a full layout matrix. Reuse normal PHP/React smoke, and observe ordinary
page responsiveness during these requests; a concrete serious regression blocks
use and returns to lead, without inventing benchmark thresholds/retry loops.

**Producer evidence versus gates.** Handoff reports reviewed source/history,
packaged/mounted10, HTTP all-five/15profiles, native768 and affected390 passes;
these are supplied evidence, not our runs. Remaining1024/1440/no-JS, installed
npm/wheel36-program matrices, Go/TS wire, Rust dev/MSRV, all-client/scaling/direct-f6
performance and exact-final CI remain producer-owned and unclaimed. They are
not blanket prerequisites for this authorized development trial with unchanged
client packages; do not launch replacements. Our exact package/services and
bounded HTTPS behavior/asset/auth checks are prerequisites. Any concrete
producer Important/Blocking finding affecting this source/use must be resolved
or explicitly dispositioned before activation. Do not call this release-ready
or claim all generated programs/performance/layouts verified. Existing provider-F
and embedded-metadata qualifications remain. Production-specific notes belong
in vpsfree-cz-configuration after ordinary scoped own-repo preparation; generic
contracts remain with their owners. No production write or new repository work
is released here. Architect performed source/design inspection only.

### 2026-10-29: final M8 pin 511 and bounded verification reuse

This amendment supersedes only the e5ea selection above. Select final published
HaveAPI `5114746f3a9f87e91c704147c0d99dd4f0d32f02`, tree
`5b9c52d0f0d81957bbca227d254e2e5b09b53373`, on the same canonical SSH feature
branch. Architect compared the already-local exact e5ea and 511 trees: both
contain 908 entries, with 900 identical mode/type/object entries and no added or
deleted paths. The eight modified paths (+71/-56) are:

- `.github/workflows/clients-rust.yml` and `Makefile`;
- `clients/rust/docs/development.md` and `clients/rust/spec/integration/README.md`;
- `clients/rust/spec/integration/fixture_actions_spec.rb` and
  `clients/rust/spec/unit/documentation_harness_spec.rb`;
- `servers/ruby/spec/client_examples/dynamic_mounted_paths_spec.rb` and
  `servers/ruby/spec/documentation/reference_headings_spec.rb`.

They relocate/wire the existing Rust fixture test, explain its setup, and align
two server test expectations with existing behavior. Runtime, emission,
fixtures, assets, OAuth/provider/config/cookies, all five gemspecs/VERSION,
dependencies and flake inputs are unchanged. The `make doc` target and copydoc
implementation are unchanged; the Makefile delta adds only the Rust test command.
The CSS/JS hashes above still apply. This is an exact bounded source comparison,
not a claim that the whole trees, packages or derivations are equal.

**A0 package after lead release:** change only the five shared revision pins and
normal source hash in `api/Gemfile`, generated `packages/api/Gemfile`,
`packages/api/Gemfile.lock`, `packages/api/gemset.nix` and the effective ignored
API lock. All five version-0.31.0 gems must resolve to this one immutable source;
retain the other 117 gem entries. Keep assertions, documentation, auth/proxy
configuration, packaging hooks and SDK0.1.1/runtime0.30.2 unchanged. Preserve
all-five make-doc preparation, recursive discovery, exact two-index removal,
whole checkout/cache, and RUBYOPT restoration. No adapter, migration, protocol,
node ordering or persistent-state change is introduced by this refresh.

All five normal Git installations contain the whole repository. The new source
hash/revision therefore changes their derivations, checkout paths and Git
metadata, followed by rubyEnv/API/services inputs. Serialized nested gemspec
contents may remain equal, but their paths and provenance change; inspect the
actual outputs rather than assuming equality or difference. Producer source
SHA256 is not a substitute for the normal Nix source hash.

**Checks and review:** quick checks cover exact source/tree/hash/lock agreement,
the intended metadata-only consumer diff, syntax/format and normal hooks.
Retain the successful mounted full/core behavioral evidence for its actual
tested revision and unchanged runtime/test inputs; this delta alone does not
justify repeating that whole batch or the producer's matrices. Final installation
still needs the actual load proof below. Consolidate the unpublished development
pin stream above supported published8102179, preserving tested2a4/e5ea and d67
refs, roots and receipts. Give the retained independent reviewer the complete
final range, consolidation/no-migration inventory and this exact eight-path
comparison for the requested affected package/history conclusion. Reuse the
unaffected product/auth/proxy review; no automatic four-lane upstream re-review.
A0/lead separately own master08c3→4cb disposition; this brief authorizes no rebase
or additional product scope.

**Required final outputs:** build the normal final API and prove all five actual
Git outputs, shared-tree byte/mode/link agreement, nested specs, retained Git
objects/CLI, designated index absence, generated docs/assets and frozen Bundler
activation/load paths. Account for normal shebang substitutions as in the
existing actual-package probe. Record the exact final source, locks, derivations,
outputs, complete inputs and roots. Then run all 34 services assertions on that
final package/closure and reconcile effects. Repository
`docs/agent-instructions/testing.md` explicitly requires services-up after
HaveAPI dependency updates; workspace verification and review-reuse policy
requires exact derivation/input identities, not tree similarity. Those identities
change here, so the prior 34 passes cannot satisfy final services acceptance.
Reuse unchanged dependency outputs only where their exact derivation/input
identities match; no new equivalence framework is needed.

The successful e5ea boundary remains consumer
`2a4a7bc9f0cf4c625aadb7cfded50dff0890ef68`, full lock `ff66923a…`, API
`r865c2ri1ji4fy1sc0n5s12lvim2aqaz`, services system `p2fvyxbhbcl9ilcxjk653l254xf3l5ry`.
Its actual package and 34/34 results remain in
[postreview-services](package-m8/vpsadmin/postreview-services/reconciliation.json),
[paths](package-m8/vpsadmin/postreview-services/paths.json) and
[five-output proof](package-m8/vpsadmin/postreview-services/actual-five-output-boundary.json).
Do not relabel them as 511 results. Preserve released API8102/React2e32 rollback
configuration/closures and the existing optional-docs-config rollback procedure.

**Deployment and producer limits:** parent activation and E3's existing exact
source/served-asset, strict-CA OAuth, host-only cookie, primary-origin/no-alias,
request/response-log and same-worker cleanup acceptance remain required. Current
runtime/provider selection needs E3's own fresh binding; historical E5 identities
and F/embedded-metadata qualifications remain scoped. No additional user approval
is needed for the already-authorized ready development deployment.
Producer reports final affected review without findings, hooks/server6,
Rust161+2/package10 and final all-five/15-profile HTTP evidence. Wire/MSRV,
direct-f6 performance, supplemental/full CI and remaining package limits stay
producer-owned and unclaimed; earlier installed matrices remain a06b artifacts.
They do not add blanket gates to this bounded development trial. A concrete
Important/Blocking finding affecting this use does require lead disposition
before activation. No full-release claim or parallel producer campaign follows.
Architect performed read-only source/design work and this record update only.

### 2026-10-29: final 59d/511 disk admission disposition

Historical pre-build assessment; superseded for the now-prepared native-only
continuation by the concrete disk budget below. Do not retain its 80 GiB gate
for that continuation.

Retain the original interruptible wait owned by A0, driver95502 at
`/tmp/hf51.cb_x2jy1`. No revised threshold is justified by the retained evidence.
The supplied available-space receipt is 80,838,090,752 bytes (75.28634 GiB);
the existing 80 GiB gate is 85,899,345,920 bytes, a gap of 5,061,255,168 bytes
(4.71366 GiB). These are arithmetic on the lead's receipt, not a fresh poll.

**Origin and authority:** `package-m8-final/vpsadmin/postreview/run.py:53–62`
implements the same `statvfs('/tmp').f_bavail * f_frsize >= 80 * 1024**3`
predicate used by the retained h312 development driver and earlier
`package-a-integration-refresh/postreview/services/executed-harness.py:51–56`.
It is an inherited, accepted batch admission envelope. No inspected workspace
verification/documentation or repository testing requirement declares 80 GiB,
and no original measured sizing calculation is retained in these records.
It is neither a native VM requirement nor a reservation, quota or runtime
low-space stop. The final driver checks it before evaluation/build and again
before services, retaining Nix jobs1/cores2 and one VM with 16 GiB memory/shm
caps and eight CPUs. Swap remains informational.

**New evidence from successful e5ea:** its stored initial/services snapshots
are 93,840,453,632 and 89,250,918,400 bytes, a decrease of 4,589,535,232 bytes
(4.27434 GiB), not attributed usage or a peak. Retained NAR sizes total
238,665,448 bytes for the API closure and 3,146,807,832 bytes for the services
closure; the five HaveAPI outputs total 50,692,024 bytes. The package log lists
11 builds/three substitutions; services preparation lists 107 builds/15
substitutions. These quantify that old run's outputs/work, not final511's
remaining builds, temporary peaks, physical allocation or concurrent demand.
The actual test config declares one 8192 MiB/eight-CPU VM, no additional disks,
and a root disk image; it declares no host-disk budget. Absence of additional
disks does not bound root-image or writable-state usage. Sources are the retained
`package-m8/vpsadmin/postreview{,-services}` capacity receipts, build logs,
`api-closure.json`, `services-system-closure.json` and `test-config.json`.

A lower admission would need a bounded package/build-scratch plus native
root-image/writable-state peak, filesystem applicability for `/tmp` and Nix
store, and explicit allowance for other admitted work. Output sizes and free
space snapshots supply none of those bounds; final511 has not yet evaluated
its remaining build set. No measurement campaign is proposed. The shortest
currently supported continuation is the original wait until its accepted gate
passes. Lead's own-root inspection found only 1,196,032 bytes of compact
records and no VM scratch candidate; no cleanup or GC follows.

If lead later supplies a defensible revised envelope, A0 must retire/reconcile
this exact wait before changing the temporary driver's `capacity` seam and
launching one successor; never edit a running guard or overlap drivers. Preserve
original wait/status, prove no child/effect uncertainty, and retain source/lock,
kernel escalation, no-retry and final package/all34 acceptance contracts.
Architect performed static own-record/source inspection only: no live resource
read, operation change, build, cleanup or new watcher. This is planning evidence,
not a source deliverable or automatic independent-review trigger.

### 2026-10-29: prepared native-only continuation — 16 GiB admission

**Correction:** 80 GiB is unjustified for this remaining test. API/package proof
and services preparation have passed at59d/511; they must not be repeated.
A0's07:47 receipt `package-m8-final/vpsadmin/postreview/current-capacity-facts.json`
binds prepared config `1wdyzxxizl1zsndh69vkap4frnwybfz3`, one VM/no extra disks,
RAW root image5,662,310,400 bytes (5.2734375 GiB; allocated3,724,611,584),
and `/tmp`, state parent and Nix store on the same ext4 device64769.
It reports84,804,399,104 bytes free, no native state, and original PID705876
with no children. Architect used that receipt, not a duplicate live query.

**Exact remaining allocation:** selected runner
`/nix/store/sv2fvmc7s3zli33adkpg58vym1pw1hn2-test-runner/bin/test-runner`
loads osvm from `/nix/store/if3m22r33wplikchlhhp8bsc28il488f-osvm`.
Its `lib/osvm/nixos_machine.rb:50–68` removes any old destination and calls
`FileUtils.cp` directly to `services-root.img`; QEMU uses that writable RAW
file (`:33–38`). Selected Ruby FileUtils `copy_file` opens the destination
with `wb` and `IO.copy_stream` (`fileutils.rb:2279–2283`): no second temporary
image, overlay or conversion. Budget a fully allocated copy regardless of sparse
copy behavior. The source image already occupies the store/free-space baseline.
Base `Machine#prepare_disks` (`machine.rb:799–805`) only handles configured
extra disks, of which there are none. Startup makes shared push/pull directories
(`shared_dir.rb:33–36`), sockets and logs; it does not duplicate the closure.
The8 GiB VM memory backend is `/dev/shm` (`machine.rb:573–585`), covered by the
separate existing memory/shm checks, not another8 GiB ext4 file.

**Recommended lead disposition:** use16 GiB =17,179,869,184 available bytes
for this native-only admission. Arithmetic: one full image5,662,310,400 plus
10 GiB =10,737,418,240 conservative concurrent-work/log/metadata allowance totals
16,399,728,640; rounding adds780,140,544 bytes. Even at that minimum, the full
copy leaves11,517,558,784 bytes (10.7265625 GiB). At the supplied free-space
snapshot it leaves79,142,088,704 bytes. This is a practical remaining-work budget,
not a reservation or guarantee against unrelated writers. Do not charge already
realized build outputs again. Preserve jobs1,8CPU and16 GiB memory/shm admission.

A0 owns the lead-released continuation: retire/reconcile only original idle
95502/PID705876 and prove it cannot launch a child, preserve its original status,
then run one successor containing only unperformed native services, final graphs,
effects and separately released publication. The temporary continuation's
`capacity('services')` is the only admission seam to change; no product/runner
source change. Bind exactly the prepared config/API; any unexpected missing
output/build or identity change returns to lead rather than expanding this budget.
The sole watcher may observe free space at its normal progress cadence; below
2 GiB =2,147,483,648 bytes, report promptly for supported owned-test cancellation
under the lead's release. Any ENOSPC/copy/I/O/test failure remains a real nonzero
incomplete result: preserve evidence and partial effects, reconcile, and do not
retry automatically. No separate disk watcher, cleanup or new resource framework.
All34 assertions and final closure/source/effects proof remain required; prior
package/preparation passes are retained. This supersedes the earlier conservative
wait recommendation only at this measured post-build boundary. No runtime action
or threshold edit was performed by architect.

### 2026-10-29: deployed511 Switch user failure and optional trial scope

Provisional diagnosis, superseded by the definitive Origin/referrer-policy
disposition below. Parser and expiry hypotheses are ruled out; disabling Switch
user does not resolve the shared ordinary sign-out failure.

E3 retained a Switch user POST403 on actual consumer59d/HaveAPI511; the later
browser wait for a form timed out. Classify this as an HTTP rejection with a
secondary harness timeout, not a backend timeout. The exact response reason is
not yet retained, so no upstream defect or root cause is established. E3 alone
owns the nonsensitive Rack parsing probe, normal-form reason capture and client
lifetime restoration15→3600; architect inspected static exact511/59d only.

**Exact rejection branches:** `servers/ruby/lib/haveapi/documentation_oauth.rb`
first checks configured HTTPS request origin (`require_origin`,264–265; failure
400), then `switch_user_request?` (319–335;403 **Invalid documentation switch
request**), then session/HTTP_ORIGIN/CSRF (`logout`,218–221;403 **Invalid
documentation sign-out request**). Switch rejection occurs before cookie reads,
clearing or revocation. The switch validator requires the capability, exactly
one scalar `switch_user=1` across query/form and URL-encoded media type. It reads
raw body pairs from `rack.request.form_vars`. Actual deployed dependency source
Rack3.2.7 `lib/rack/request.rb:499–550` normally populates that field for
URL-encoded parsing, but cached form pairs/hash can bypass the population path.
That is a candidate interface issue, not proof that it happened here.

The temporary15-second provider lifetime is another concrete distinction:
callback203–208 caps the cookie expiry at the smaller provider/config lifetime;
`read_cookie`361–384 rejects expired/invalid sessions, then logout returns the
sign-out403. A stale form/session during short-expiry testing is expected refusal,
not a parser defect. E3's nonsecret response text and fresh-session timing must
distinguish these cases. Do not log cookie, CSRF, token or private config values.

**Supported bounded configuration:** `doc/documentation-oauth.md:42–47` and
initializer91–94 explicitly make `switch_user:false` the default supported
capability. Controls151–162 hide only Switch user. The template
`views/version_sidebar/authentication_control.erb:7–16` retains ordinary Sign out
without a switch field; validator326 returns false for that ordinary request.
Thus a development trial with switching disabled is valid if normal sign-out,
revocation, expiry, re-login and the other accepted OAuth/isolation/logging
conditions actually pass. Readers can Sign out, then Sign in through fresh
editable credentials on the dedicated SSO-off client. Keep the observed switch
failure visible in the receipt; do not count it as passed or promise the control.

Mandatory retained behavior is documented in `documentation-oauth.md:95–110,
123–143`: ordinary logout validates origin/CSRF, clears authenticated and pending
cookies, revokes the token and returns303; expiry/revocation yields anonymous
docs; re-login works; cookie/API identity separation remains. A revoke failure
may truthfully return502 after local clearing, but that documented failure mode
does not satisfy successful-revocation acceptance. Disabling optional switching
cannot waive broken logout, revoke, expiry, account entry or session cleanup.

If E3 proves valid normal switch input is rejected because the raw form cache is
missing, the smallest fix belongs to producer HaveAPI's
`DocumentationOAuth#switch_user_request?`, with its existing
`servers/ruby/spec/documentation/oauth_spec.rb` coverage. Use the supported
Rack parsed-pair interface or bounded body handling preserving duplicate,
query-plus-body, nested/multipart, capability/origin/CSRF rejection before effects;
do not weaken to collapsed-params equality or change consumer/provider policy.
The focused regression must submit a normal URL-encoded form through the actual
supported Rack/Sinatra parser, including its normal cached-parameter path, and
retain existing malformed/default-off/no-effect cases. If evidence instead shows
expired session or wrong Origin/CSRF, correct only the owning harness/config
cause and verify its existing assertion; no upstream code change is inferred.
Any producer fix requires a separately bound source handoff; current package,
34 assertions and deployed proof remain59d/511. No repin/build/runtime/config
action or independent new campaign is released by this disposition.

### 2026-10-29: confirmed browser Origin/referrer-policy sign-out defect

E3's `devcluster/m8-runtime/switch-diagnostic-03/switch-diagnostic.json` records
normal Chromium form POST403 with literal **Invalid documentation sign-out
request**, Origin `null`, cookie present, matching43-character CSRF, exactly one
scalar `switch_user=1` and no switch-parser failure. The same cookie rendered
test-user1 immediately beforehand; `existing-cookie-expiry.json` binds expiry
10:21:57.514770UTC after the09:41:53 capture. It predates the15s fixture.
The nonsensitive Rack probe populated raw form_vars/pairs/hash. Parser and
expiry explanations are therefore ruled out. Client3 is restored3600; stable
key/config preserved; all E3 operations ended.

**Root cause/owner:** HaveAPI511 sets `Referrer-Policy: no-referrer` on the
authenticated HTML document via `DocumentationOAuth#authenticate:135` and
`#protect_response:268–269`. Browser navigation form POSTs under this policy
can serialize Origin as `null`; this is the observed normal Chromium request.
The same source's `#logout:220–221` requires the exact configured origin and
correctly rejects null before clearing/revoking. The response policy and normal
form/CSRF contract are incompatible. This is a producer HaveAPI browser-integration
defect, not a backend timeout, wrong user/client, consumer auth adapter or
permission failure. The later harness form wait is secondary.

Static selected deployment configuration corroborates ownership: appliedxlwlsjk's
nginx unit selects `/nix/store/x9l3x82jdimfxx41r4sq0ili8iapsi1y-nginx.conf`;
primary API location118–134 passes Host/trusted scheme/host to direct HAProxy and
does not override Origin or Referrer-Policy. Selected
`/nix/store/408dqs000a40ylg1hv7vs06r64ksn0av-haproxy.conf:33–41` routes that socket
to the API with no header rewriting. No live request/query was duplicated.

**Smallest owning correction:** producer adjusts the referrer policy of rendered
documentation pages so normal same-origin POSTs retain their real Origin while
no path/query/credential-bearing URL is disclosed. A narrowly applied
`strict-origin` page policy is a conventional candidate: only the origin can be
sent, not page path/query. Keep `no-referrer` on callback/login/logout/error
responses and preserve private/no-store. This intentionally permits public-origin
referrer disclosure and needs owning documentation/test review; do not replace
it casually with a policy that forwards the full same-origin URL. The boundary is
`documentation_oauth.rb`, its existing `oauth_spec.rb` and the affected statement
in `doc/documentation-oauth.md:119–121`. Producer owns the implementation and
focused source regression; E3 owns the real-browser proof after the corrected
deployment. Retain strict exact-Origin, session and CSRF checks:
never accept null Origin, forge it at the proxy, or weaken duplicate/form guards.

Focused acceptance must include real browser ordinary Sign out and Switch user
through generated forms without injected Origin or JavaScript-dependent repair,
successful revoke/local cookie clearing and correct redirect/new login behavior,
plus preserved foreign/null/missing Origin and wrong-CSRF rejection. Confirm no
credential-bearing referrer from callback/error paths. Existing unit-only form
requests cannot establish the browser's Origin generation. No broad new audit or
matrix is required; producer provides checked affected-reviewed immutable source
before any consumer repin, and E3 resumes the existing bounded acceptance then.

**Usability disposition:** `switch_user:false` remains a supported optional
capability, but cannot close this defect: ordinary Sign out shares `#logout:220`
and the same page policy. Authenticated docs trial acceptance remains blocked;
do not claim logout/revoke/switch/expiry/relogin/exact-worker/final-session-cleanup
PASS. Preserve PHP/React login/read/logout passes and all59d/511 package/34/native
deployment evidence at their actual scope. Existing sessions are not claimed
revoked. No automatic reconfiguration, repin, build or activation follows this
design amendment; producer correction and lead handoff remain the next steps.

### 2026-10-29: sign-out correction — prepared consumer successor package

**Adoption prerequisite:** producer supplies the final published immutable
revision/tree on canonical SSH, bounded511→successor diff, focused source/spec
and strict-guard quick evidence, and completed affected security/history review.
These suffice to begin consumer adoption; the changed real-browser Origin and
sign-out behavior is mandatory final acceptance by E3 after the refreshed
deployment, not a pre-pin gate. Producer message90e9a548 reports provisional
sidecar6f7aa/treee526 onfb07 with OAuth80/0, two-file lint and hooks passed;
consolidation/independent affected review are pending, so this is not the final
target. A0 verifies the final handoff against the preceding root-cause brief;
no moving branch pin or speculative build. A materially broader delta returns
to lead. Unrelated producer release/compiler/performance campaigns remain their
own scope. No duplicate producer browser campaign or additional approval gate
is introduced; existing user deployment authorization remains sufficient.

**A0 owns one complete package:** after that handoff and lead release, update
only the five common HaveAPI pins/new normal source hash, `api/Gemfile`, generated
`packages/api/Gemfile`, effective and packaged locks, and `packages/api/gemset.nix`.
Retain all117 unrelated gem entries, SDK0.1.1/runtime0.30.2, consumer assertions,
hooks/make-doc/recursive discovery/two-index handling and proxy/private-config
interfaces. Current consumer mounted spec and `docs/api-client-examples.md` do
not assert `no-referrer`, so no consumer expectation edit is presently needed.
If the exact producer contract contradicts an existing assertion, report that
concrete delta rather than weaken it. No upstream edit, auth adapter, Origin
rewrite, PHP/React/exporter change or new provider mechanism.

Quick verification binds five source identities/hash/locks and unchanged117,
normal generation/syntax/hooks, then the existing focused mounted documentation
spec in its required full/core modes against the new installed bundle. Reuse
producer's focused source/spec/guard evidence at its actual scope; neither those
checks nor local mounted specs replace E3's postdeployment real-browser normal
form, Origin, revoke and session acceptance. Preserve deployed59d/511,
tested2a4/e5ea and d67 recovery refs/roots/receipts. Consolidate the same development
update stream according to the Git procedure while preserving published-ref and
supported8102 boundaries; an exact deployed recovery ref remains even if the
feature series is consolidated. Supply the complete final range, old/new diff
and no-migration inventory to the retained reviewer after commits/quick checks.
This upstream runtime-policy change requires the narrow affected consumer
compatibility/package/history conclusion; reuse unaffected product/proxy review.
No blanket mechanical-equivalence exemption for changed auth-page behavior.

**Postreview verification:** normal builds of changed outputs are expected.
Prove all five actual successor Git outputs/source/tree/hash, complete shared
checkout/specs/docs/assets, frozen Bundler/load paths and actual API closure with
the existing package proof. Then run one services-up/all34 batch and reconcile
effects on the exact final source/API/config. Repository testing.md explicitly
requires this after HaveAPI dependency updates; old59d/511 results stay valid
only for their actual outputs. Reuse unchanged dependencies by exact derivation
and input identity. Do not repeat the producer matrices, old package probes or
unaffected application suites, and do not invent a new equivalence framework.

Capacity is scoped to the remaining phase. There is no blanket80 GiB gate and
no prohibition on the ordinary builds this new source requires. For package/
services preparation, use current remaining-build/substitution facts and the
retained small-output measurements, with practical scratch/reserve headroom;
unexpected kernels follow the existing escalation rule. Once outputs are
realized, the measured one-VM raw-copy budget applies:16 GiB admission if the
same5,662,310,400-byte image/no-extra-disk geometry remains; if it changes, recompute
one full writable image plus10 GiB margin, rounded up. The existing sole watcher
owns normal progress/low-space observation, no auto retry or new resource system.

**E3/parent activation:** after source/review/package/services/no-writer handoff,
perform only the existing canonical-inode/PHP/private-file-preserving source
binding and supported public services update. E3 binds the selected runtime,
exact prepared inputs and original pending-target recovery; parent activates.
Preserve current dedicated client3/fixed3600/no-refresh/SSO-off, stable shared
key, callback and private config; no credential rotation or recreation is implied.
Bind applied/running generation, new native five-gem/API/assets/closure and
rollback59d/511 (which retains the known logout defect), plus released8102/React2e32
and its optional-config removal procedure. No default integration is authorized.

**Remaining acceptance, E3:** normal browser Sign out and Switch user with
real Origin/no injected header, token revocation and local/pending cookie clearing;
fresh login/callback and editable account entry; short fixed expiry→anonymous→
re-login with client restored3600; exact same-worker/thread cleanup evidence and
final owned docs-session cleanup. Observe policy on the rendered page and
sensitive auth/callback/error responses plus the existing redacted log window.
Preserve rejection of foreign/null/missing Origin and wrong CSRF through producer
focused evidence and the consumer's normal form path. Bind assertions to the new
actual deployed output; no synthetic relabel of59d/511. Existing PHP/React and
mixed-identity/OPTIONS passes may be retained where their application/config/
auth inputs are unchanged; the new correction needs targeted form/session proof,
not another full UI campaign. Missing any mandatory logout/revoke/expiry/relogin/
cleanup result keeps docs OAuth usability incomplete. This preparation releases
no edit, fetch, build or activation before the concrete handoff.

### 2026-10-29 resume: selected runtime d0wi/provider r2vd update compatibility

Bounded installed-source comparison for the resumed90e2/HaveAPI2f6 rollout
found no relevant compatibility blocker. Selected runtime is
`/nix/store/d0wikyzpr7qk1w2c2zbqgj97qz1m58qn-dev-workspace-0.2.0`, with reported
guide catalog `af53ccceb927a13cce1bed4ef27a6b236a2b24067b6ac481c4876a5d09d27c07`.
Its actual `share/dev-workspace/extensions.json` selects provider
`/nix/store/r2vdj3ib32pryx8n0cb1104adw5c4xn1-vpsfree-dev-workspace-tools-0.1.0`.
Previous actual update used runtime7wqvb8/provider2flmy0/catalog4fe07; those
identities remain historical evidence, not current command bindings.

Compared with2flmy0, selected provider's native `vpsadmin/bin/devcluster`,
README, shared runner, runner library/Nix, maintenance library, test.nix, flake
and defaults are byte-identical. Shared `dev-clusters/lib/runtime.sh` and
`runtime-contract.json` are also identical. Native command SHA256 remains
`8fc86cd540785130f5fc61810a67e7f837dbbd7ebba8e8b196172777679f887b`;
README SHA256 `2364880b7e8e2a416c69f84324404f6b1a658dc1fd03ddcfc2e5eb2236e11357`.
The provider wrapper changes only its own exec store path; its tools and default
configuration store paths are unchanged. This is bounded interface/source reuse,
not a whole-package or future output-equivalence claim.

Generic runtime `coordination.md`, coordination contract and
`share/workspace-portal/runtime-contract.json` are identical. The latter's hash
is `f06f639a247b584a652777543c27284b1939bc8179ecfbbc1fe3299f4090b8a2`:
cluster schema1/policy3, authority policy1 and8 MiB tracking bound remain.
The actual `.workspace-host-wrapped` methods `dispatch_cluster`, `system_env!`,
`with_current_generation_lock` and cluster-helper compatibility check are exact.
Inspected host changes concern per-workspace Codex home/SQLite/log/skill paths
and their session/coordinator environment, not cluster command execution.
Public wrappers bind the new runtime/catalog paths; no package switch is needed.

Reuse the ordinary parent command `vpsadmin-devcluster update <slug> services`
and existing output protection/32 GiB memory/12CPU/zero-swap/Nix jobs1 cores2
containment. Native update1433–1486 still records pending before copy, activates,
restarts API, refreshes nodes, proves current system/closure/root, then promotes
only the services descriptor. Other guests retain their selection. Original
same-target pending recovery/refusals and generation/ownership checks persist;
no reset to bypass refusal or assumption that candidate equals running state.
Rebind only any explicit runtime/provider identity checks in the prepared parent
invocation, retaining the existing command and protection semantics.

`system_env!` still uses `Open3.capture3` then writes stdout/stderr after exit.
Keep stdout discarded and stderr private0600 with only sanitized/allowlisted
events exposed; buffered quiet output is not proof of a stall. Public SSH still
does not pass arbitrary stdin through that capture call. Preserve the previously
accepted ordinary OpenSSH route for protected file delivery with the exact
owned key/address/host-key policy; do not repeat a transfer probe or repair the
provider. No new secret delivery is implied by this runtime change.

E3 alone supplies fresh cluster tuple/pending/config/source/inode/private-file
guards at the binding boundary; this comparison does not replace them. A0's
standalone native34 test continues unaffected. Prior provider-F and embedded
metadata qualifications remain; no new provider installation, graph sweep,
cluster query, native operation or runtime mutation was performed. Architect
updated this design only; lead may reuse the existing preparation.

### 2026-10-29: minimum installed-code same-thread cleanup proof

Accept E3's controlled Rack sequence against the actual installed90e2/HaveAPI2f6
package/config as the intended same-worker/thread user→nil invariant proof,
combined with independent guest/applied xqd5/API0k8v/wrapperwjn2 binding and the
separate actual HTTPS/browser acceptance. It is not attribution to a live Puma
worker. Two workers/1–8 threads and HTTP keepalive do not establish that identity;
forcing worker selection or adding production instrumentation is unnecessary.
Earlier shorthand does not require a stronger live-worker attribution gate.

Source basis: consumer `api/lib/vpsadmin/api.rb:117–126` clears `User.current`
and `UserSession.current` on nil and always sets `PaperTrail.request.whodunnit`.
HaveAPI2f6 `documentation_helpers.rb:44–49` invokes that hook for every normal
user/nil documentation lookup; `server.rb:132–149` invokes it on ordinary auth,
including the version OPTIONS path. Existing consumer mounted spec217–243 tests
these transitions. This proof covers successful requests, not arbitrary-exception
ensure cleanup or all concurrent interleavings.

**E3 minimum sequence:** load one actual installed application with its normal
deployed configuration and frozen bundle; execute synchronously in one owned
Ruby PID, thread and fiber, recording those identities before/after each call.
Use fresh Rack request environments and the exact configured HTTPS host/scheme,
real version7.0 routes and normal request stack, consuming/closing each response.
Do not reuse a Sinatra request object, stub authentication, invoke hooks directly
or manually clear thread state between requests.

1. GET `/v7.0/` with the existing valid owned docs cookieB:200, rendered identityB;
   require `User.current` isB, nonnil OAuth2 `UserSession.current` belongs toB,
   and `PaperTrail.request.whodunnit.to_s` equalsB's ID. This must be nonvacuous.
2. GET the same documentation without cookie or API credentials:200, anonymous
   account controls, and all three state values nil immediately after the call.
3. Repeat the authenticated GET with cookieB and require the same nonnil state.
4. OPTIONS `/v7.0/` with cookieB but no Authorization/custom/query credentials:
   normal200 JSON description and all three state values nil. The intervening
   authenticated GET makes this an independent dirty→nil transition rather than
   merely observing state already cleared by step2. Cookie-only OPTIONS must not
   authenticate through the documentation mechanism.

Private cookie arrives only over the already accepted protected stdin route;
no token/cookie/CSRF/config content in argv, output or records. Record only
request classes, status, same-identity booleans and state assertion results.
Do not dump Rack environment, raw responses or exceptions with credentials.
No client/session creation, raw database helper, server instrumentation,
source edit, authentication bypass or worker-count change is needed.

**Side-effect precision:** GET/OPTIONS are the nonmutating request methods, but
the normal `ResumeOAuth2` operation (`operations/user_session/resume_oauth2.rb:25–32`)
increments request_count and updates session/user last_request_at. Do not call
this literally database-read-only or suppress those normal authentication effects.
The fixed-lifetime client avoids renewable-auto token extension. This stays
within ordinary authorized acceptance; final docs-session logout/revocation and
fixture restoration remain E3's existing separate cleanup responsibility.
An expired/invalid first cookie makes this proof incomplete, not a cleanup pass.

A passing controlled sequence satisfies the invariant with this explicit scope;
actual HTTPS Origin/forms/revoke/expiry/relogin/log-window proofs remain separate
mandatory acceptance. Preserve exact package/source/config identity and existing
failure evidence. E3 may run the bounded method after normal HTTP acceptance
under lead release; architect ran no dynamic probe or guest/API request.

### 2026-10-29: example-style successor — bounded consumer adoption

**Source and decision:** canonical SSH readback confirms
`refs/heads/2026-10-27-api-documentation-redesign-example-style` at
`1b264e25a73a0ab9bca5f847bd52254f74e0931c`, tree
`dcdba06a92fe0d8a577f4cffe46ea69fc8d73a40`, direct parent deployed
`2f6c18a80f3a5f8ce46449ff81183b100b60f34c`. Objects were already local; no fetch
was needed. The original redesign branch correctly remains2f6. Exact diff is
11 modified paths/+212/-106: Go and typed-TypeScript documentation renderers,
server PHP/Python/Ruby example adapters, and six associated specs. PHP uses
single quotes for ordinary literals, consistent four-space indentation and clean
assembly separators; control-containing literals use escaped double quotes to
preserve their bytes. Ruby uses single-quoted authored credentials and clean
separators; Python adjusts import/top-level spacing; Go uses tabs and import
group separation; typed TypeScript spaces imports/objects and uses double-quoted
module/auth literals. Calls, values and client interfaces are preserved. Producer
round-trip/gofmt/typed-compilation coverage supports those formatting changes;
reported150/fullTS63/11CI passes remain supplied evidence, not our executions.

The exact diff excludes OAuth, provider/config, routes, dependencies, inputs,
gemspecs, versions and migrations. Independently compared Git objects are equal
for `documentation_oauth.rb` (e28bc7ef), `documentation_helpers.rb` (d93c03bd),
the authentication tree (33ffc6cd), server (37071e53), public CSS/JS tree
(7650d3fe), both documentation guides, all five gemspecs, VERSION and flake.lock.
All five gems remain0.31.0. No auth adapter, SDK change, schema/node migration,
credential operation or new runtime mechanism is required. Standing local
deployment authorization recorded in plan.md applies; no new permission gate.

**A0 source/quick package:** create the new own isolated
`worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsadmin-haveapi-style` worktree
and `2026-10-24-vpsadmin-haveapi-upgrade-docs-style` branch from reviewed90e2.
Preserve both canonical90e2 and isolated59d rollback. Update only the five common
immutable Git pins/normal source hash in `api/Gemfile`, generated
`packages/api/Gemfile`, `packages/api/Gemfile.lock`, `packages/api/gemset.nix`
and the effective ignored API lock, plus these two necessary assertions in
`api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`:

- line106: `import {createClient} from "vpsadmin-typescript-client";` becomes
  `import { createClient } from "vpsadmin-typescript-client";`.
- line151: `runtime.authenticate('token', {token: "example-token"})` becomes
  `runtime.authenticate("token", { token: "example-token" })`.

The remaining mounted assertions, services-up literals and owning consumer
documentation are compatible; no other consumer mismatch was found in those
files. Retain all117 unrelated gem entries, SDK0.1.1/runtime0.30.2, PHP/React/
exporter, proxy route/log protection, private inputs, hooks, all-five make-doc,
recursive gemspec discovery, two-index handling and RUBYOPT restoration.
Use normal scoped metadata generation/lock reconciliation, syntax/format/hooks
and the existing mounted documentation spec in full/core modes (eight examples
each). No new fixture framework or producer compiler/performance campaign.

Consolidate only the new branch's same-development update above supported8102:
retain the current split between development packaging and consumer behavior/
assertions, folding the latest pin into the former and these expectations into
the latter. Retain released0312 package/profile commits32608935/8102179 and
all published90e2/docs-signout,59d/511,8102 and earlier recovery refs/roots.
Do not append another superseded pin or rewrite those published refs. No default
rebase merely to publish. Give retained reviewer0 the committed/quick-passed
complete final range, narrow90e2 delta, old/new history comparison and explicit
**NO MIGRATIONS** for affected packaging/consumer/history review; reuse unchanged
auth/proxy review. Lead owns review acceptance and subsequent execution release.

**Actual package and native gate:** all five whole-Git outputs acquire new
revision/store identities even where libraries are unchanged. Run the existing
actual five-output/API/shared-docs/assets/load-path/frozen-Bundler proof on final
source, then ONE complete34-assertion services-up run required by repository
`docs/agent-instructions/testing.md`. Old90e2 outputs/34 passes stay historical;
reuse unchanged dependencies only by actual derivation/input identity. Normal
builds are expected. Apply phase-correct capacity: after preparation, retain
16GiB native disk admission for the unchanged one-image geometry, recomputing
only if geometry changes; no80GiB or blanket no-new-build guard. Use the existing
sole watcher, failure/effects reconciliation and unexpected-kernel procedure.

**E3/parent deployment and acceptance:** after source/review/package/services/
publication/no-writer handoff, use existing canonical-inode/PHP/private-file
preserving transfer and ordinary public services update, retaining pending-target
recovery. Client3/fixed3600/no-refresh/SSO-off, stable shared key, callback and
private config stay unchanged. Bind actual applied/running source, all five gems,
API output/closure and served assets to the final consumer/1b source. Through
existing strict-CA served-panel mechanisms check representative PHP Simple and
With-error-handling quotes/indentation/blank lines, and affected Ruby, Python
sync/async, Go and typed-TypeScript output. Use existing initialization/auth/public
action pages and synthetic example values; no credentials in receipts. This is
the focused changed-output check, not a new all-profile/compiler/browser matrix.

Reuse completed90e2/2f6 real OAuth/form/revoke/expiry/relogin/same-thread/privacy,
PHP and React acceptance after E3 confirms the unchanged corresponding deployed
config/application inputs. Exact OAuth/source equality supports that reuse;
style alone requires no repeated TTL/session/mixed-identity campaign. Existing
provider-F/embedded-metadata qualifications remain. Rollback is preserved working
90e2/2f6 with its matching config/direct route;59d/511 retains its known old signout
defect and released8102 retains its optional-config removal requirement. No
production/default/release/lifecycle action follows. Architect inspected source
only and releases HaveAPI Git ownership with this brief; no build, source edit,
runtime probe or activation was performed.

### 2026-10-29: KB installation versions and obsolete header warning

**Scope/owners:** user requests removing avoidable client-version literals and
a durable general documentation rule. Lead owns the bilingual existing API
candidates and localized change summaries; E1 owns the minimal rule in
`docs/agent-instructions/documentation.md`, with at most a pointer from the KB
procedure, not a duplicated policy. E3 owns existing guarded changeset/staging
mechanics. Architect records source findings only. No product correction, new
client release, live API/auth/browser check or deployment is required.

**User-Agent evidence:** vpsAdmin commit
`c3543c5c82c155d31e165f7c3c1172c610fcd433` (2026-05-29, “api: allow sessions
without User-Agent”) identifies the historical bug: absent User-Agent left the
default session label nil, violating the non-null label column. Current
`api/lib/vpsadmin/api/operations/user_session/utils.rb:17,35–39` normalizes it
with `request.user_agent.to_s` and uses that string for metadata/default label.
The path is unchanged from pre-initiative08c3 through retained0.31.2 consumer8102
to deployedstyleaae; this is not a development-documentation-only repair.
`api/models/user_agent.rb:9–14` has no nonempty validation, and schema1931–1935
requires non-null agent/hash, not a nonempty agent. Retained8102 regressions
`api/spec/lib/vpsadmin/api/authentication/basic_spec.rb:101`,
`oauth2_config_spec.rb:797`, and `token_config_spec.rb:147` each cover both nil
and empty User-Agent and assert empty metadata/label after successful login.
These are inspected existing tests, not new executions or a production probe.
Remove the Czech HTTP500/nonempty-UA workaround rather than implying arbitrary
500 errors have this cause or replacing it with another warning.

**Accept/Content-Type evidence:** in released HaveAPI0.31.2,
`servers/ruby/lib/haveapi/output_formatter.rb:15–31` selects the first formatter
when Accept is absent; JSON is the built-in formatter
(`output_formatters/json.rb:5`), and `output_formatters/base.rb:14–17` accepts
matching wildcards. Explicit `Accept: application/json` is useful for ordinary
API calls, not a universal required header. `server.rb:106–120` returns406 for
unsupported Accept and400 for malformed Accept. `server.rb:762–776,969–976`
requires a JSON media type for a nonempty action body on methods other than
GET/HEAD/OPTIONS; it accepts application/json or a +json type, and rejects
missing/wrong media type with415. Bodyless GET/OPTIONS do not need Content-Type;
ordinary JSON action bodies must parse as objects. Provider/form and HTML docs
routes have their own contracts, so do not generalize the action rule to every
URL. Existing `servers/ruby/spec/server/integration_spec.rb:86–148` covers
unsupported/malformed Accept, invalid/nonobject JSON and wrong Content-Type.
The exact setup_formatter, mount_action and json_content_type? method bodies
are unchanged at deployedHaveAPI1b (lines111/807/1027). Keep the existing protocol
link and remove the speculative header sentence; no new warning is needed.
Source evidence does not assert the current production deployment revision.

**Installation decisions:** remove generic PHP/Python/npm client pins and the
versioned PyPI URL. Use `composer require haveapi/client`,
`python -m pip install haveapi-client`, `npm install haveapi-client`, and the
unversioned project page. For the generated SDK use only
`npm install vpsadmin-typescript-client`: the retained actual published package
declares a nonoptional exact haveapi-client peer, and its packaged README:31
explicitly documents normal npm peer installation. Evidence:
`package-0.31/kb/sdk-consumer/node_modules/vpsadmin-typescript-client/package.json`
and README, plus registry metadata in
`package-0.31/kb/vpsadmin-typescript-client-0.1.1-npm.json`. The verified pair
remains SDK0.1.1/runtime0.30.2 in our evidence; it need not be copied into the KB.
Explain that npm selects the runtime required by the SDK. Do not recommend
installing both unqualified latest packages or force/legacy-peer bypass; an
existing incompatible runtime must be reconciled with the SDK's declared peer.
This describes normal current npm dependency resolution, not a claim that all
future latest pairs are compatible or a fresh unpinned installation test.

For Rust replace handwritten version constraints with `cargo add vpsadmin-client`
and the optional `cargo add vpsadmin-client --features blocking`. Link maintained
Python/Rust requirements instead of copying their version floors. Preserve API7
call/URL values and unrelated command output/examples; this earlier disposition
is superseded for optional API selectors by the 2026-10-30 correction below.
Machine significance alone does not establish necessity. No broad historical
KB refresh.

The general rule should prefer version-independent prose/install commands and
maintained requirement sources, retaining versions only for a clear compatibility,
migration, reproducibility or protocol reason, or an owned update workflow.
Removing a number must preserve dependency constraints and must not imply latest
compatibility. Record a necessary exception's rationale or maintenance owner.
This belongs in the routed general documentation procedure because the user's
rule extends beyond KB pages.

**Bounded validation:** lead/E1 preserve bilingual page IDs/tags/links and all
unrelated examples, inspect only changed commands/claims and rule scope, apply
the existing writing/hooks/review requirements, and hand the exact candidate
bytes/summaries to E3 for existing guarded stage/verify/render checks. Reuse the
retained source, regression and package metadata evidence at its actual scope;
no new dependency/compiler/auth matrix is needed for these prose corrections.
Existing pending changesets and production pages remain protected; production
promotion still needs approval of the exact staged changes. No new permission
gate is added to preparing the requested candidates. Architect's binding and
saved Astra/xhigh/workspace_write settings were verified; only this design was
edited, with no product/live action or test run.

### 2026-10-30: released HaveAPI 0.32.0 — A0 consumer package

User requests the released version in vpsAdmin and preparation of the production
channel/deployment instructions, with the documentation OAuth client created
before deployment. Standing dev-cluster deployment authorization remains;
production activation, client creation, secrets access and default integration
are not authorized. Identity/roster reconfirmed; architect retains Astra/xhigh/
workspace_write. A0 may execute this complete isolated consumer package under
lead release independently of E1's configuration preparation below.

**Verified release:** canonical SSH annotated tag `v0.32.0` is
`e78e4b398819a82961cabb7c7ceea59c773c6a64`, peeled commit
`0e7166a0f8f15827bfac051666a53bf449e999ec`, tree
`a87c3b7d186b015c720210eb3dc765af6e186170`. One ordinary tag fetch completed;
HaveAPI ownership is released to A0. Exact deployed1b→release is17 commits,
153 paths/+10500/-5734, mostly formatting/tooling. Runtime changes include
RubyCLI/curl shell escaping, inert displayed response/password transcripts,
Ruby CLI help escaping and release metadata. Included commitsddf836fb,
a3f522e5, aee093cd and c79645e0 cover the reported argument and subsequent
transcript issues. Their presence is source evidence, not a claim of a completed
new security audit or of safety in the still-deployed1b. No peer reply/audit wait
is added to adopting this independently verified release.

TypeScript generation now requires Prettier3.9.10 and includes formatter
provenance. It runs inside `Generator#generate`; mounted documentation profiles
do not generate clients or require Prettier. The actual documentation renderer,
OAuth module/helpers/auth tree/server, public assets and OAuth guide are exact
1b bytes. There is no auth/provider/schema/protocol/node migration. PHP changes
are source formatting/trailing argument commas and version metadata; required
PHP8 compatibility is retained. JS authored source was reformatted; release-built
output is distinct from the repository's checked-in dist and must be taken from
the actual package, not reconstructed by changing a version string.

All five downloaded gems match RubyGems SHA256, and all232 packaged lib/bin files
match the tag (server135/Ruby49/Go26/Rust10/TS12). Server includes11 doc files;
the exact public assets and the TS formatter JSON are packaged. Archive hashes:

| Package0.32.0 | SHA256 |
| --- | --- |
| haveapi | `5e5566972ef1c7725df5f8647f3b9bb53fad9572fd8b9b14446dbe767c169027` |
| haveapi-client | `c5ce21e3e5167ff1021b0719d82674d6e91abb7e78cd560b4c0b8a11db3e9613` |
| haveapi-go-client | `1296e3a3f15cb5a1fe3a1ca4d87f2d24d0ca81eab15ce271c8bb8ac09f2192c2` |
| haveapi-rust-client | `a54e08a3027c8df46614af401563279827fe3daa7177655a45664615b06697d1` |
| haveapi-typescript-client | `3b774cb6dac62a6b1236a7375f2f956f30bf71bfde25a214495bf75ec52c2e10` |

npm0.32.0 integrity matches the actual tarball, SHA256
`144cf17ada3b4578c8a3d81c87d183c94bd72d98e83934475c019b8bfd8b2efc`;
37/47 dist files differ from committed dist, so no tag-dist byte-equivalence
claim. Packagist0.32.0 selects PHP mirror
`d0d51d09ada7beb863d2cd726ca446504312579a`; all20 source files match the tag.
Observed PHP archive SHA256 is
`8755f44669e6963faa2e6973b959c397433e1252bfe737366ba0bc871482c4bb`;
Packagist supplies no checksum. Fresh SDK metadata says TypeScript0.2.0 latest
still requires exact runtime0.30.2. Do not update the independently verified
SDK0.1.1/runtime0.30.2 pair or separate React2e32 merely to match HaveAPI0.32.

**Source/history:** use a new isolated `vpsadmin-haveapi-032` worktree/dated
feature branch; never edit the mounted canonicalaae to prepare the package.
Fresh observed vpsAdmin default is
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`. Its08c3→ac10 range has four normal
dependency-refresh commits,16 metadata/lock files/+55/-116, with no application,
schema, migration or API change. A0 owns normal fresh fetch and final baseline
verification. Carry reviewed08c3..aae feature content onto ac10, preserving
those newer default dependency records, then consolidate the final branch into
the released dependency update and its owning profiles/config/docs/tests change.
Do not carry obsolete Git pins or Git-only installer machinery into the final
released stream. Preserve publishedaae/1b,90e2/2f6,59d/511,8102 and earlier refs,
roots and receipts independently; do not rewrite any published rollback ref.
Record exact old/new base/head ranges and range-diff; the0.32 adoption is a
substantive successor, not whole-tree equivalence. If default advances beyond
this bounded delta, assess the actual new change without automatic scope growth.
No repository claim is needed and no default merge is authorized.

**A0 owned files:** replace API five-sibling Git block with ordinary released
RubyGems constraints selecting0.32.0 together; regenerate scoped packaged
Gemfiles/locks/gemsets and effective locks normally. Remove the now-unused
`packages/api/haveapi-git-gemspec-glob.rb` and Git-only preBuild/preInstall/
postInstall machinery in `packages/api/common.nix`; retain ordinary default
gemConfig behavior. Published gems already contain generated docs: do not run
source make-doc inside a registry gem, use a raw source mount, or repackage it.
Update `client/vpsadmin-client.gemspec`, `download_mounter/Gemfile`,
`plugins/outage_reports/utils/Gemfile` and affected generated client/download
package metadata. Refresh `webui/composer.json`, lock and `php-packages.nix`
through their normal scoped tooling; replace BOTH
`console_router/public/haveapi-client.js` and `webui/public/js/haveapi-client.js`
with `package/dist/haveapi-client.js` from the same verified
`https://registry.npmjs.org/haveapi-client/-/haveapi-client-0.32.0.tgz` archive
(SHA256 above). The second bundle is actively loaded by
`webui/template/template.html:42`; leaving it at0.31.2 would leave an effective
consumer behind. Bind both tracked/package/served bundle bytes to that archive
and confirm their0.32.0 runtime identity through the existing PHP/browser and
console checks. No additional browser matrix or SDK/React update is implied.
Preserve unrelated baseline dependencies.

Bring the isolated exporter back to a coherent released boundary: update its
exact Gemfile substitution/runner guard/CLI text and `docs/api-schema-export.md`
to0.32.0, retain all environment/clean-source/fixture refusals. The carried
tracked `api/config/api.rb.example` needs one exact allowance in
`tools/api-schema-export/safety.rb`'s `Safety::CONFIG_FILES`: add only the literal
`api.rb.example`, with the existing regular-file requirement and symlink refusal
before allowlist handling. No `.example` wildcard or live `api.rb` allowance.
This is nonexecuted sample data: `api/lib/vpsadmin/api.rb:363` loads exact
`config/#{name}.rb` paths, not example suffixes. Extend the existing
`safety_spec.rb` positive sentinel case with this file (`raise "must not execute"`),
retaining the no-API/ActiveRecord-load assertion; extend existing negative cases
for a symlinked `api.rb.example`, private `documentation-oauth.json` and
`documentation-session.key`, while preserving live `api.rb`, `database.yml`,
hooks, environment, clean-checkout and isolated-fixture refusals. This is a
bounded exporter compatibility correction for a tracked inert sample, owned by
A0 and included in its affected quick checks/final consumer review, not permission
to load deployment configuration. Existing14 exporter/16 shell checks are prior
evidence; the amended cases still require A0's normal quick run. Update
`docs/api-client-examples.md` to describe normal released gem packaging and
remove the superseded development-only override/rejection explanation. Keep
before-mount/private-input/proxy/runtime compatibility guidance. Existing mounted
assertions change only for a demonstrated released contract difference. No SDK
regeneration, external SDK package change, runtime framework or migration.

**Quick/review/actual checks:** normal generation and focused metadata equality,
syntax/format/hooks; existing mounted full/core eight-example spec and exporter
safety/snapshot checks. Bind the packaged shell corrections with one bounded
local argv-only check for CLI/curl request values and whole commented response
transcripts, plus the Ruby CLI help formatter; reuse existing producer tests/
methods, no network target or broad audit. Preserve known failing evidence if
an actual release mismatch appears. Commit complete intended changes and give
retained reviewer0 the affected package/client/security compatibility lanes and
whole-history **NO MIGRATIONS** conclusion before longer checks.

After review prove all five actual registry gem/spec/load/doc/assets outputs,
frozen API bundle and closure; actual CLI/download-mounter and PHP packages,
vendored JS archive identity; run ONE repository-required all34 services-up.
Exporter real fixture export is an affected functional check after restoring
its release guard, not an SDK generation/performance campaign. Reuse exact
unchanged derivations/input evidence only; no relabel of Git-source outputs.
Ordinary builds are allowed; native-only16GiB admission applies after preparation
when measured geometry is unchanged. No80GiB guard or duplicated watcher.

**E3/parent dev boundary:** retain existing inode-preserving source transfer,
private configuration/client3/key, pending-target recovery and public services
update. Intentionally changed dependency artifacts are not covered by the old
blanket PHP-byte equality. Retained providerd50 `nix/test.nix:1731,1753,1814–1835`
selects mounted authored PHP source but explicitly links
`${config.vpsadmin.webui.package}/vendor`; it skips mounted `vendor`. Build the
new lock-derived noDev PHP package and prove the active vendor resolves to it,
with HaveAPI0.32.0 loaded. No canonical ignored-vendor refresh is needed for
that path. E3's current4x provider comparison confirms these relevant bytes equal
d50. The separate1465+ regular-vendor merge belongs to the vpsFree website
(`/mnt/web`, `vpsfree-web-live-root`), not containers.webui; it is not a reason
to modify canonical PHP vendor. Prove actual applied selection after update;
never silently retain old effective PHP or overwrite config/secrets.

Final dev acceptance binds applied/running API/all-five/CLI/PHP/console outputs
and served docs to the exact final source. Check representative served CLI/curl
escaping and inert response text through existing strict-CA page capture, with
argv-only local inspection if executing copied text (no real API command).
Repeat bounded PHP login/read/logout because its dependency changes. Reuse prior
OAuth/thread/privacy and unchanged React acceptance only after actual relevant
code/config/dependency equality; packaging or default dependency differences
that affect auth need targeted validation, not presumed equality or an automatic
full TTL/mixed-identity campaign. Existing provider-F/embedded metadata limits
remain. Currentaae rollback contains the reported shell weaknesses; retain it
honestly as recovery, not security clearance. Production work remains preparation.

### 2026-10-30: E1 production channel and documentation-OAuth preparation

E1 owns a new same-session `vpsfree-cz-configuration` worktree/feature branch,
fresh canonical fetch and its source changes. Architect inspected already-local
`fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627`, matching fresh SSH master; the older
bare HEAD86e differs in lock inputs but the relevant hook/frontend/channel
definitions are equal. Do not base preparation solely on86e. This package may
start independently; its exact channel pin waits for A0's final reviewed and
published consumer. No production client/secret/runtime access or activation.

**Files and channel:** `flake.nix:106–108` defines channel `vpsadmin`, role
`vpsadmin`, input `vpsadminServices`, currently
`4a21dd25b23de9832166def98526f410416b651e`. In the normal configuration shell
use `confctl inputs channel set --commit vpsadmin vpsadmin FULL_FINAL_CONSUMER_SHA`
for the published unmerged feature. A later normal default update uses
`confctl inputs channel update --commit vpsadmin vpsadmin`; do not use it now
to select an unrelated default without the consumer change. Preserve generated
changelog and all other input pins/follows. `vpsadminWebui` and notification
templates follow this services input; inspect their affected module composition,
without changing their own revisions. `vpsadminProduction`/`vpsadminStaging`
node channels remain untouched. Existing source4a21 supports the ordinary
OAuth2-client create/update fields required below. No core schema or core/plugin
migration path changes were found in4a21→ac10; final channel inventory must also
include A0's complete exact head. This source observation is not a live database
or production-generation assertion.

Implement the optional before-mount configuration in
`configs/vpsadmin/api/api.rb`, preserving its existing ExceptionMailer in the
same configure block. Use the released configuration contract already described
in the consumer sample: label from `core.api_url` host, optional JSON,
scope `['all']`, session lifetime3600, stable session key and initially
`switch_user:false`. Missing JSON means anonymous usable documentation;
present invalid JSON/key/fields must fail clearly without printing values or
chained secret-bearing exceptions. Resolve adjacent runtime files through
`File.join(VpsAdmin::API.root, 'config', ...)`, not the source hook's `__dir__`:
the configuration hook is symlinked from the store. The application root's
config link selects that service's persistent configuration directory. API and
supervisor share the authored configDirectory; only API instances receive the
private docs files, so other consumers retain the absent-file path. Do not
grant supervisor or unrelated services access to the docs key.

Use existing regular persistent files
`/var/lib/vpsadmin/api/config/documentation-oauth.json` and
`documentation-session.key` on both `int.api1` and `int.api2` (confirm effective
stateDirectory/user/group from generated configuration). The ordinary module
links `/run/vpsadmin/api/config` there, removes old symlinks during setup, and
preserves unrelated regular files; no secret may be added to configDirectory
or any Nix-store expression. Directory0750 and files0600 owned by the effective
API service account/group permit reads without public access. Existing owned
paths must be checked before replacement; copy prepared secret files atomically
through the operator's normal protected route. Do not create a new provisioning
helper, rotate existing credentials, or print secrets in argv/receipts.

**Credential-bearing route prerequisite:**
`cluster/cz.vpsfree/vpsadmin/common/frontend.nix` is imported by
`cluster/cz.vpsfree/containers/prg/proxy/config.nix:114`; proxy.prg terminates
TLS using forceSSL/ACME. API and auth production/maintenance currently point
through Varnish. Set these four existing frontend backends to the existing
`unix:/run/haproxy/vpsadmin-api.sock`, retaining API production's
`ipv4.ddns.vpsfree.cz`/`ipv6.ddns.vpsfree.cz` aliases, maintenance behavior,
HAProxy's existing Unix/*:5000 binds and api1/api2:9292 backends. This deliberately
removes the60-second API metrics Varnish cache on these routes. Shared Varnish,
PHP/React/console/download routing and private credentials stay unchanged.

Use ordinary existing nginx virtualHost/location overrides for API/auth only:
trusted Host/scheme/port/client-address headers derived at the TLS edge,
discarding alternate client forwarding headers; access format omits query,
headers and bodies; API/auth error logging disabled because it can include raw
requests. Cover their HTTP→HTTPS redirects and maintenance locations as well as
successful TLS proxy responses. Existing `vpsadmin.haproxy.api.prod.logRequests
= false` suppresses credential-bearing request logging. No global logging or
provider change. Exact canonical callback/host-only cookie rules restrict docs
OAuth to the primary origin, but that is not a substitute for protecting values
before they reach application checks; all four API/auth routes bypass VSL.
E1 must inspect generated configuration to verify effective overriding directives
and trust boundaries rather than claim copied dev configuration is proof.

**HTTP redirect appendix (2026-10-30):** selected nixpkgsStable
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source/nixos/modules/services/web-servers/nginx/default.nix:460–473`
generates `forceSSL`'s HTTP server without vhost `extraConfig` or configured
locations; those appear only in the main server at509. TLS-only safe logging
therefore leaves callback queries exposed in inherited HTTP redirect logs.
Use the existing virtualHost interface in this same configuration frontend file:

- For the four API/auth TLS virtualHosts, set `forceSSL = lib.mkForce false`
  and `onlySSL = true`; preserve their names, aliases, existing ACME certificate
  ownership and all proxy/maintenance locations. Apply scoped safe access logs
  and `error_log /dev/null crit;` to each. Replace the original unsafe
  `extraConfig` access-log directive rather than append a second one; retain
  `error_page 503 @maintenance;` when replacing that fragment.
- Add four uniquely keyed HTTP-only virtualHosts with explicit `serverName`
  equal to each corresponding TLS domain: `api.vpsfree.cz`,
  `api-admin.vpsfree.cz`, `auth.vpsfree.cz`, `auth-admin.vpsfree.cz`. Copy their
  aliases, including both DDNS aliases for the primary API. Keep the same
  HTTP listening addresses/port; set no SSL mode (`forceSSL`, `onlySSL`,
  `addSSL` all false). Set `enableACME = false`, `useACMEHost` to the existing
  corresponding TLS certificate name, and `acmeRoot` to that TLS vhost's value.
  This reuses its certificate/challenge configuration without a second issuer
  or certificate identity. The module's `hasSSL` at335–336 depends on SSL modes,
  not `useACMEHost`; its431–455 code still emits the ACME challenge location.
- In each HTTP vhost, set `locations."/".return` to the original redirect code
  and target (`301 https://$host$request_uri` with current defaults), and put
  the same safe access-log policy and `/dev/null` error log in its `extraConfig`.
  Keep the redirect inside location `/`, not at server level, so the generated
  `^~ /.well-known/acme-challenge/` location retains its HTTP-01 behavior.
  Preserve path/query on the redirect wire; exclude them as required from logs
  (no query, headers, bodies or response Location). No global logging change.

E1's focused generated-effective-config check must show exactly one HTTP redirect
and one TLS server for each of these four domain/alias sets, no leftover automatic
unprotected redirect, unchanged listening/redirect/ACME SANs+webroot, safe logging
in both servers and inherited ACME/maintenance locations, and all four TLS routes
using direct HAProxy with existing maintenance behavior. Check absence of unsafe
duplicate access logs/header captures and effective HAProxy request logging off;
ordinary nginx syntax validation follows normal scoped config preparation.
This is part of the existing affected proxy/security review and targeted proxy
configuration validation, not an upstream module patch or new review campaign.
Later authorized production acceptance includes benign HTTP query/redirect and
ACME-path checks plus existing TLS callback/request+response log-window checks;
no production request is authorized now. Reverting to automatic forceSSL while
docs OAuth remains enabled would reopen the logging gap: preserve this routing/
logging protection on application rollback. PHP/React/console/download vhosts,
shared Varnish and their global settings remain unchanged. No schema or client
contract change; E1 owns implementation after lead release.

**Operator sequence, documented before deployment:** add reusable
`docs/operations/vpsadmin-documentation-oauth.md`, link from `mkdocs.yml` and
the existing API config README. Keep exact execution receipts in this session,
not a configuration-repository release-report directory.

1. Verify the current API's ordinary admin `Oauth2Client Create/Update` interface
   (POST `/v7.0/oauth2_clients`, PUT `/v7.0/oauth2_clients/ID`) and real provider
   metadata from `core.auth_url || core.api_url`. Existing4a21 source already
   supports this; no docs-capable deployment is needed to register the client.
   Do not assume the metadata origin is api.vpsfree.cz or copy the dev client3.
2. Operator creates a dedicated confidential client using a generated client ID
   and secret, nondefault (`is_default:false`), exact redirect
   `https://api.vpsfree.cz/_documentation/oauth/callback`, fixed3600-second
   access tokens, `issue_refresh_token:false`, `allow_single_sign_on:false`.
   Request scope `all` in the docs configuration; the client-create resource
   has no scope field. Retain the generated secret privately: ordinary Show
   does not return it. Never reuse PHP/React credentials, use raw DB writes or
   change the default client. Reuse an existing dedicated client only after
   checking its exact settings; do not silently recreate/rotate it.
3. Prepare identical client JSON and one stable, cryptographically random key
   of at least64 bytes for both API hosts/all workers. Verify service-readable
   ownership/modes and exact callback/provider HTTPS/CA trust without exposing
   values. These are operator-supplied production inputs, not the dev fixture.
   Keep switch_user disabled until fresh authorization for this client actually
   offers editable credentials; SSO-off is necessary but no prompt/select_account
   parameter is invented. Preserve adequate API concurrency for token/revoke.
4. Build/review the matching channel, optional hook and proxy preparation before
   later authorized activation. Activate credential-safe proxy routing/logging
   before exposing docs OAuth on either API host; then deploy the matching API
   package/hook with prepared files. Client registration precedes this deployment.
   Rolling APIs may temporarily differ in docs presentation; use the same client
   and key on both, and verify final package/config on both before acceptance.
5. In the later authorized production acceptance, confirm applied identity,
   anonymous docs and no-secret startup/log behavior, then bounded real HTTPS
   login/callback/signout/revoke and expiry/relogin plus account-entry/Switch
   only if enabled. Existing dev passes do not certify production provider,
   trust, routing or credentials. This plan authorizes no such production action.

**Checks and recovery:** quick Ruby syntax/normal hooks and a focused optional
hook fixture (missing files, valid synthetic config, malformed/missing-key
failure, ExceptionMailer retained) plus Nix formatting/generated input diff.
After committed quick pass, retained independent affected config/security/docs/
history review; then targeted ordinary configuration builds/evaluation for
proxy.prg/api1/api2 and followed service composition, including generated
nginx/HAProxy/header/log and service permissions/source selection. No broad
fleet build or production dry-activate. Preserve old exact channel/config/system
identities for later rollback. Revert the bundle and authored hook together if
the old server lacks documentation keys; keep direct protected routing while
docs OAuth is enabled. Preserve client/key/files on software rollback; disabling
the optional client by removing its JSON from the service path makes docs
anonymous but does not revoke already-issued tokens. Any revocation is a separate
ordinary operator action. No database rollback or coordinated node upgrade is
introduced by this release. E1 owns concrete checked source; lead owns any later
production release decision. No additional user decision is needed for preparation.

### 2026-10-30: optional API versions in KB and shared writing guidance

Separate documentation milestone; completed0.32 code/review/package work proceeds
unchanged. Identity and same-session roster reconfirmed; architect retains
Astra/xhigh/workspace_write. Current CS/EN candidates match accepted hashes
`c7b1f412783a2ce0dfe5fe863bf1dc16bb1368bdf2590bfa14905931723aff5e` /
`d6ca6635aaa3ca0c5b9fb42b753fbd49b4fd9a7a3613a4fccd3053759f9a572a`.
Lead owns bilingual edits and natural wording; E3 owns append-only logical
staging after final review, without resetting/replaying earlier revisions.
No installation, upstream fetch, product change or live-client campaign is
needed for this source-backed correction.

**Concrete client decisions:** inspected accepted HaveAPI release0e7166a0
and retained published SDK/archive contracts, not a claim about live deployment.

| Current KB example/client | Required change and source basis |
| --- | --- |
| PHP (CS666/EN613) | Use `new \HaveAPI\Client('https://api.vpsfree.cz')`. `clients/php/src/Client.php:44–52,551–563` defaults version to null and requests OPTIONS with `describe=default`; authentication calls setup at148. Remove the second `'7.0'` argument. |
| Python (CS696/EN642) | Drop `version="7.0"`, retain URL and TokenAuth. Sync/async constructors default to None (`client.py:35–46`, `async_client.py:35–46`); shared `_resources/state.py:170–181` sends OPTIONS to the root with `describe=default`. Existing context-manager/lazy connection handles discovery; no new explicit init is needed. |
| Dynamic JS/TS (CS724/EN670) | Use `new AsyncClient("https://api.vpsfree.cz")`. `clients/js/src/haveapi/async/client.ts:48–59,118–130` defaults absent version to null and discovers `/?describe=default`; existing authenticate loads the description. Callback Client/CallbackClient also defaults to null (`client.ts:183–184,527`). No new init step. |
| Ruby library / vpsfreectl | Existing `VpsFree::Client.new` and CLI already omit the selector. vpsfree-client56357098 `lib/vpsfree/client.rb:6–8` passes root URL/options through; `lib/vpsfree/cli.rb` supplies root URL. HaveAPI `client/client.rb:20–23,142` and `client/communicator.rb:91–92` select `describe=default` when no version is supplied. Keep executable examples and optional CLI-help option names. |
| Generated Go | Keep `client.New("https://api.vpsfree.cz")`; remove prose's numeric API version and say action paths already include their schema's version prefix. Canonical134a9e69 `client/client.go:232` accepts root; `client/resource_vps_action_index.go:366` carries the versioned wire path. This is generated-schema selection, not dynamic default discovery. |
| Generated Rust | Current KB only installs/names clients; remove numeric API support prose and link maintained client compatibility guidance. Retained verified crate in `package-b/rust-crates-2026-10-25/README.md:21–31` requires root base URL and documents async/blocking clients. Keep existing examples/options; do not add a versioned constructor URL. |
| Generated vpsAdmin TS | Remove numeric support prose but explain generated resource/action methods and parameter/result types from a saved vpsAdmin schema. Keep sdk-only npm install and its declared runtime pairing. The retained SDK's `dist/index.js:3–8` forwards generated requests unchanged; VPS index descriptor is `/vpses`, relative to the supplied base. Its README:57,74–77 explicitly requires the schema-matching versioned base, including any mount prefix. Unlike the dynamic example, deleting that prefix would rely on an unverified default/schema match. Current KB has no executable SDK initialization, so explain the requirement without a number and link the SDK README; do not add a pinned example merely to illustrate the exception. |

Versionless dynamic discovery selects the server's configured default, not
necessarily the newest version and not a promise that an application remains
compatible with all future schemas. The server's OPTIONS default contract is
`servers/ruby/lib/haveapi/server.rb:583–605`. Generated SDK types remain tied to
their saved schema even when a constructor takes an origin-only URL. Do not
strip version prefixes from their generated wire paths or treat an arbitrary
root path as equivalent. No current KB numeric API literal needs retention:
replace the obsolete `/v6.0/#auth` documentation links (both line44) with the
stable API root, without promising a root `#auth` anchor. Remove “main client”
in both overview and installation prose. Use “Dynamic” / “Dynamický” for the
HaveAPI JS/TS label; if section headings change, update their local TOC anchors.
Explain that the dynamic client discovers names/parameters at runtime, while
the generated vpsAdmin client adds schema-specific methods and editor/compiler
types over the HaveAPI transport; neither bypasses server permission checks.

**One policy owner, revised by direct user choice:** authoritative organization
guidance belongs to `vpsfreecz/dev-workspace` (local `vpsfree-dev-workspace`),
not a second vpsAdmin/workspace policy. Canonical local default inspected:
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. E2 owns a small docs-only change to
`skills/vpsfree-user-facing-writing/SKILL.md`: in its factual workflow, prefer
versionless prose, install commands, links and examples whenever the actual
client/protocol permits; inspect defaults before removing a selector. Retain
exact values for a demonstrated compatibility/protocol, migration/recovery or
reproducibility requirement, with its reason or maintained owning reference.
Being a URL/argument or other machine-significant value is not itself a reason.
Reconcile the skill's protected-content paragraph so copy-edit preservation
does not exempt optional versions during requested factual changes. Do not
duplicate this rule in another new procedure or alter generic runtime skills.

The existing workspace knowledge-base procedure already applies this skill to
KB and vpsAdmin documentation; its installed catalog also supplies it to this
workspace. Thus no separate vpsAdmin policy branch, runtime package switch or
0.32 repin/rebuild is needed. For standalone-repository discoverability, the
only useful extra pointer would be one link from vpsAdmin `docs/README.md`'s
existing Writing documentation section to the authoritative skill; no copied
policy text or new routing framework is required. E1 can later adapt the existing
workspace documentation-version-policy feature to a pointer at that same skill,
retaining its KB pointer and published old0c2c9f18 recovery ref/history. This
changes ownership/location, not the user's accepted rule; no default integration
is authorized. Serialize those Git writes outside E1's configuration work and
coordinate any vpsAdmin pointer/doc edit with A0 through lead; leave A0's exact
reviewed consumer untouched.

Bounded source-doc observation on vpsAdmin defaultac10: `docs/api-schema-export.md:30`
has optional `--api-version 7.0`; `tools/api-schema-export/cli.rb:8,18` already
defaults to and only permits that value. The command can omit the selector.
The page's description of its fixed exported schema and synthetic provenance URL
serves a concrete reproducibility contract and must remain accurate. This is a
one-line future docs correction, not permission to modify exporter code or
rewrite A0's completed branch; no wider documentation cleanup was identified as
necessary for this milestone.

**Acceptance:** inspect only changed example/label/link bytes against these
contracts and preserve bilingual IDs/tags, token handling and install pairing.
Lead applies the existing writing skill before final KB review; E3 regenerates
and stages one new logical revision with updated anchors and localized summaries.
E2 runs normal docs/hooks/link checks and obtains required independent final
docs/history review for its committed extension change. No runtime/schema/input
change or migration; no package/native/browser/client matrix is warranted by
these instructions. Workspace/vpsAdmin pointer follow-ups remain docs-only and
must not delay the accepted0.32 package/services/deployment gates. The shared
source policy can be read directly now; installation is not an adoption gate.

**Remaining CLI literals (same KB correction):** remove the copied Ruby minimum
from both introductions and retain Ruby/header/ncurses prerequisites. Point to
`https://rubygems.org/gems/vpsfree-client` for published package/dependency
requirements, not to its README as a supposed Ruby-floor source: canonical
vpsfree-client56357098 README has installation guidance but no Ruby minimum,
and its gemspec delegates to vpsadmin-client. The inspected vpsAdmin defaultac10
and HaveAPI0.32 client gemspecs both declare Ruby >=3.0; this demonstrates why
the article's >=2.7 is not a durable current requirement, without asserting the
exact released transitive resolution or replacing it with another copied floor.
The package target follows its actual gem name; no registry/live probe was run.

Replace the hardcoded user/version PATH example with
`export PATH="$PATH:$(ruby -r rubygems -e 'puts Gem.bindir')"`.
In the selected Ruby3.4.9 source, `rubygems/commands/environment_command.rb:128`
prints `EXECUTABLE DIRECTORY: #{Gem.bindir}` exactly; `rubygems.rb:347–350`
selects the current Gem.dir's bin directory (or Ruby's default bindir).
Thus this discovers exactly the preceding `gem env` field for the same Ruby
environment. Do not describe it as discovery of every installation: installer
`installer.rb:673–678` can instead use an explicit install/bin directory or a
user-install home. Such custom destinations retain their own install instructions;
no new CLI/configuration workflow is needed here. The command was inspected,
not executed. Change only the Czech link label `Ubuntu 20.04` to `Ubuntu`, keeping
`navody:vps:api:ubuntu`: this is the platform-navigation label, not a claim that
the linked instructions support every Ubuntu release. Leave any version-specific
scope of that separate page to its own text; no unrelated page inspection/change.

### 2026-10-30: vpsFree.cz operator commands for documentation OAuth

Independent docs-only follow-up to configurationd0024528e93da895deeb4b7efc2b68c1461c94ec.
Identity/roster40 and retained Astra/xhigh/workspace_write verified. E1 edits only
`docs/operations/vpsadmin-documentation-oauth.md`; lead owns its final contextual
writing pass. Existing code/pin/three-target build evidence remains bound to
d002. Do not change the running dev update, configuration inputs, hook or product.
These are documented operator actions, not authorization to create production
clients, generate real credentials here, or access production.

**Inspected contracts:** vpsfree-client56357098 `bin/vpsfreectl` runs the
VpsFree CLI subclass; `lib/vpsfree/cli.rb` supplies `https://api.vpsfree.cz` and
vpsAdmin's subclass retains HaveAPI action parsing. Released HaveAPI0.32 source
0e7166a0 `clients/ruby/lib/haveapi/cli/cli.rb:169–188,333–350,381–385,698–710`
uses `oauth2_client create --` followed by action options. `utils.rb:5–16`
dasherizes field names and defines Boolean `--[no-]FIELD`; false therefore means
`--no-is-default`, `--no-issue-refresh-token`, `--no-allow-single-sign-on`,
not a textual `false` following a flag. `@PATH` is supported for action values:
File.read supplies its exact bytes, including any newline. `@@` escapes literal
@, and `--raw-values` disables file loading; explicitly select `--no-raw-values`.
There is no JSON-body/stdin-import option in this CLI. Bare string options prompt
through HighLine, but `client_secret` is not marked protected in this resource,
so do not rely on that prompt hiding its input. Use a protected file instead.
Token authentication can prompt for administrator credentials/challenges
(`authentication/token.rb:48–76`); keep passwords/tokens out of argv, use normal
saved credentials or interactive authentication, and select header transport.
Explicit `--api` precedes `--auth` because auth-option parsing connects immediately.
No optional API version is needed.

Existing production-capable4a21 and ac10 resource
`api/lib/vpsadmin/api/resources/oauth2_client.rb:6–35,82–107` requires name,
client_id, client_secret and redirect_uri; administrator-only Create hashes the
supplied secret through `Oauth2Client#set_secret` (BCrypt), and Create/Show omit
it from output. Use a32-random-byte hex client secret (64 ASCII bytes, avoiding
BCrypt's72-byte input boundary), distinct random client identifier, and a separate
session key. No `scope` or `client_type` Create field exists. Default schema
seconds900/SSOtrue must be overridden explicitly; fixed3600/no-refresh/nondefault
settings are explicit even when matching a default. Client creation is supported
before the documentation deployment.

**Copyable skeleton for E1's owning guide:** first inspect/reuse any existing
dedicated production client and protected files. Run the following generation
block only for first registration in a private, unrecorded operator terminal,
outside the repository. It intentionally prints the secret-bearing JSON as the
user requested; do not paste it into tickets, shared transcripts or Git. The
fresh0700 directory and077 umask protect regular files; mkdir must refuse an
existing path, including symlinks, so rerunning never rotates/overwrites a key.

```bash
(
  set -eu
  umask 077
  mkdir -- "$HOME/vpsadmin-documentation-oauth"
  cd -- "$HOME/vpsadmin-documentation-oauth"
  ruby -rsecurerandom -rjson <<'RUBY'
settings = {
  'client_id' => SecureRandom.hex(16),
  'client_secret' => SecureRandom.hex(32),
  'redirect_uri' => 'https://api.vpsfree.cz/_documentation/oauth/callback',
  'switch_user' => false
}
File.write('client-id', settings.fetch('client_id'))
File.write('client-secret', settings.fetch('client_secret'))
json = JSON.pretty_generate(settings) + "\n"
File.write('documentation-oauth.json', json)
File.binwrite('documentation-session.key', SecureRandom.random_bytes(64))
puts json
RUBY
)
```

Then register the client once with ordinary administrator authentication. Only
file paths/nonsecret settings appear in argv; neither shell interpolation nor
the CLI response is used to reconstruct the secret. The two credential files
have no trailing newline. Keep them and JSON together for reconciliation.

```bash
vpsfreectl --api https://api.vpsfree.cz --auth token \
  --token-via header --no-raw-values oauth2_client create -- \
  --name 'vpsFree.cz API documentation' \
  --client-id "@$HOME/vpsadmin-documentation-oauth/client-id" \
  --client-secret "@$HOME/vpsadmin-documentation-oauth/client-secret" \
  --redirect-uri https://api.vpsfree.cz/_documentation/oauth/callback \
  --no-is-default --access-token-lifetime fixed --access-token-seconds 3600 \
  --no-issue-refresh-token --no-allow-single-sign-on
```

Retain the returned numeric resource ID privately with the operator record;
verify ordinary `oauth2_client show ID` settings before deployment. On any
uncertain Create result, reconcile ordinary list/show against the retained
client_id before retrying; do not generate another identity or rotate the secret.
Existing clients use the ordinary Update action only for an intentional settings
correction, omitting client-secret to retain its hash. For later upgrades skip
both generation and Create; reuse original JSON/key and verify settings.
An existing/partial local directory is a reason to inspect/resume, not remove
it or bypass mkdir refusal. `cat "$HOME/vpsadmin-documentation-oauth/documentation-oauth.json"`
can intentionally reprint the retained JSON in that same private terminal;
the raw session key stays in its file.

d002 `configs/vpsadmin/api/api.rb` takes exactly client_id/client_secret/
redirect_uri/switch_user from JSON; it reads session_secret as raw File.binread
bytes and fixes scope['all']/session_lifetime3600 in the hook. The generated64
random bytes satisfy HaveAPI `documentation_oauth.rb:73–75`'s64..4096-byte
contract. Do not hex/base64-decode the file on one host or generate per-host keys.
Install the SAME JSON and key through the existing protected/atomic operator
route on int.api1 and int.api2, regular0600 files owned by effective
vpsadmin-api:vpsadmin-api under the existing0750 persistent config directory.
Do not install client-id/client-secret helper files into the API config tree.
Preserve existing ExceptionMailer, missing-JSON anonymous behavior, provider
origin from core.auth_url||core.api_url, exact callback, initial switchfalse,
proxy-first ordering, CA/concurrency/logging acceptance and software rollback.
No production provisioning command is executed by this documentation package.

**Proportional checks/history:** E1 verifies the literal blocks offline with
fixed synthetic RNG values and an action/communicator stub, no network/help
invocation. Reuse actual released CLI option/file parsing; assert false Boolean
values, exact field names/3600/callback, @file read without newline, preserved
stdin for auth and absence of secret bytes in argv. Parse generated synthetic
JSON, check client files agree and raw key length64; repeat generation against
the existing fixture directory to prove refusal and unchanged bytes. Syntax/
normal hooks plus narrow independent docs/security/history review after commit.
These checks validate the few documented commands, not a provisioning framework
or real authentication campaign. Consolidate into the existing functional guide
stream while preserving publishedd002 and its exact source/build receipts;
no channel/lock edit, new three-system build or reopened A0 review is implied.
Record the new docs head separately; do not relabel d002 runtime proof.

### 2026-10-30: default-aware documentation specs, isolated from update3922

Source inspected: final vpsAdmin
`33d6c7723b392c828de2165854d106d9528f9305` against base
`ac10a62f1cb0fc890378ae83cdf18dd0e29f049a`; canonical33d6 remains untouched
while parent owns update3922. Identity/roster40 and Astra/xhigh/workspace_write
reconfirmed. This is a test-maintenance follow-up, not a runtime API-version
change. Lead releases one implementer into a new isolated worktree/branch after
coordinating its Git boundary; no current source/ref/lock transfer until the
parent has reconciled the original operation. Preserve33d6 and all recovery
refs/receipts. No wholesale historical-test replacement.

**Answer to the user:** default-aware smoke and rendering tests will need fewer
edits when the default API changes. They must still detect missing documentation
profiles and schema mismatches. Choosing the default route does not prove that
an older generated SDK supports a new schema; that compatibility decision remains
explicit.

**Established seam:** mounted `app.settings.api_server.default_version` and
`server.version_prefix(version)` are the actual runtime contract (HaveAPI0.32
`server.rb:474–484,550,1003–1005`). The existing
`api/spec/support/version_helpers.rb` is NOT a default selector:
`api_version` returns `api_versions.first`, and `vpath` also performs an
OPTIONS request that changes request/header state. Do not use it as an alias
for the default or broaden this task into changing all its callers. Add only
local lets beside the existing server let in the new documentation spec:
`default_api_version = server.default_version` and
`default_api_path = server.version_prefix(default_api_version)`.
No new shared helper framework is needed.

**Two-file implementation boundary:**

- `api/spec/lib/vpsadmin/api/documentation_clients_spec.rb`: rendering checks
  at44–47,74–84,97–101,120–126 select profiles/contexts using the mounted default
  rather than duplicated7.0 literals. Form canonical version URLs from the
  base origin and `default_api_path`, keeping real version prefixes in emitted
  generated-SDK initialization. In the TypeScript example at94, request
  `OPTIONS /?describe=default` and JSON Accept; construct its canonical
  version URL explicitly instead of reusing `last_request.url`, which now
  contains the discovery query. Assert emitted initialization uses that canonical
  version URL, not the discovery URL. Missing default profiles must fail, not skip.
- The same file's HTML helper at14–20 can exercise the actual default route:
  `GET /` with exactly one selector, `resource` when supplied, otherwise
  `page: page || 'overview'`. Bare GET / is the version index, not an overview;
  do not simply delete /v7.0. HaveAPI `documentation_helpers.rb:77–100` permits
  at most one page/resource selector; `server.rb:553–555` renders the default
  version for it. Keep HTML/locale/HTTPS and all identity/privacy assertions.
  BOTH ordinary OPTIONS identity-separation requests at231/234 must retain the
  versioned endpoint, using `default_api_path` derived from the mounted default.
  Keep cookie/header, request order and User/UserSession/PaperTrail assertions
  unchanged, without inserting discovery calls between them. Root discovery is
  reserved for the isolated TypeScript/default-payload and native index checks.
- The slashless redirect check at169–171 remains a versioned-route test, but
  derive its slashless path and expected Location from `default_api_path`;
  preserve the exact raw query `page=resources&q=a%2Bb` and308 assertion.
  The legacy-login destination at177 likewise expects `default_api_path`.
- `tests/suite/services-up.nix:137,164–166`: use root URLs with
  `?page=overview`, `?page=authentication`, `?resource=cluster` for generated
  examples. Keep every existing content/absence assertion. Preserve the root
  index assertion and its real version-link check by obtaining the declared
  default once in that existing example from OPTIONS
  `/?describe=versions` (JSON Accept), then comparing the rendered anchor with
  that response's default and confirming it belongs to its versions list.
  Do not reduce this to the title alone or infer the default from first link.
  Use the existing runner's Ruby JSON support (explicit require if necessary);
  no new endpoint/helper/fixture campaign.

**Deliberately explicit cases:** retain one focused profile-registration
assertion at35–40 for7.0 profiles and6.0 absence. This matches
`api/lib/vpsadmin/api.rb:46–55`, which intentionally binds the three generated
SDK profiles to that schema. Neither this registration nor
`HaveAPI.implicit_version = '7.0'` at3 is an optional test selector. Do not
replace it with automatic default registration, which would silently bless
SDK/schema compatibility. Keep an explicit unknown-version negative route
(current99.0 at172); establish that it is not mounted before asserting406 and
no Location. That synthetic unsupported identifier is the point of the test,
not an instruction to target a current API version.

Exporter fixtures are outside this correction. `tools/api-schema-export/cli.rb:8,20`
deliberately defaults to and restricts exported schema7.0; runner30–31/48 records
that selected identity. `snapshot_spec.rb:9–14,32,48,54–57,74–75` supplies a fixed
schema fixture, checks matching source URL, rejects6.0 mismatch and unsupported
protocol3.0. Those literals prove provenance/negative protocol behavior; changing
them to the current application default would couple a database-free schema
contract test to unrelated runtime state. Safety specs have no API selector
change. No exporter, schema, generated SDK, profile registration, CI partitions,
package dependency or migration change is proposed.

**Verification/history:** one complete isolated test-only commit; syntax/format/
normal hooks and existing documentation_clients_spec full+core runs, retaining
all eight behavioral examples per mode and failures. Check that root overview
is selected explicitly, default discovery returns the proper description, emitted
SDK URL remains canonical, and redirect raw-query/unknown-version behavior plus
identity separation are still asserted. No tests should claim arbitrary-version
SDK compatibility. Independent affected test-correctness/history review after
quick pass, then ONE affected services-up run for the changed native assertions
under the normal watcher/resource procedure. Do not rerun exporter fixtures,
browser/provider/OAuth matrices or all package proofs for unchanged inputs.
Normal required Nix preparation may occur for the changed test; reuse previous
package/VM results only with actual unchanged derivation/input evidence, without
relabeling old service passes. No dev/prod redeployment is required solely by
test changes. Any later consolidation/source transfer is the parent's decision
after3922 reconciliation and preserves the original exact deployed lineage.

**Quick-check correction accepted by lead6c7aab88:** A0's initial full8 run
reported6pass/2fail; retain that evidence. Literal `/?describe=default` fixes the
TypeScript discovery request/assertion. Root OPTIONS calls
`authenticated_versions -> do_authenticate` without `post_authenticated`, whereas
versioned OPTIONS calls `authenticated?(version) -> post_authenticated`, including
vpsAdmin's identity cleanup. Deriving the existing versioned path removes the
optional7.0 literal without changing what the identity test exercises. No
objection to this scope reduction; no runtime change or weaker assertion follows.

### 2026-10-30: bounded OAuth logging coverage, shared server and four clients

Read-only source assessment requested by the user; no fix, new gate or backlog
expansion. Compared configuration base `fcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627`
with proposed `249f2eb5896b0a2697ed94e44657294847b3e606`. Their vpsAdmin service
sources are respectively `4a21dd25b23de9832166def98526f410416b651e` and
`33d6c7723b392c828de2165854d106d9528f9305`; React remains
`606a02c19f328c69298dd30780c805211fb5cb27`. Pinned nixpkgsStable
`718f670e845328e9c2cecdd832835712b2cbd065` was inspected at local
`/nix/store/z40fynbhnw0d06q05mw2mznn49h1y9pk-source`. These are selected-source
facts, not a statement about currently installed production or actual log contents.

**Both ends matter:** the provider handles authorization/token requests; the
client callback receives code/state in its request query. Protecting the shared
API/auth proxies benefits every OAuth client using those routes, but cannot
change logs on another callback origin. Documentation is special here only
because its callback `https://api.vpsfree.cz/_documentation/oauth/callback` is on
the API origin covered by the same change.

| Surface and configured route | BaseFCC coverage / remaining exposure in configuration | Proposed249f effect |
| --- | --- | --- |
| Shared server: `api.vpsfree.cz`, `api-admin.vpsfree.cz`, `auth.vpsfree.cz`, `auth-admin.vpsfree.cz` | Ordinary nginx request logs and HAProxy httplog retain request targets; API/auth traverses Varnish. `return(pass)` disables caching, not VSL URL/header records. No universal application-log redaction established. | HTTP redirects and TLS use query-free method/path/status access format and suppressed scoped error output; API HAProxy logging disabled; all four route directly to that HAProxy socket, bypassing Varnish. Helps all clients' server-side traffic, not just docs. |
| Legacy PHP: `vpsadmin.vpsfree.cz/?page=login&action=callback`; maintenance frontend `vpsadmin-admin.vpsfree.cz` uses same backend | Edge nginx -> webui HAProxy -> backend nginx/PHP. No equivalent callback suppression found; ordinary request logs retain query. PHP error logging/captured stderr enabled. Callback catch itself displays a generic error; broader app/private policy is not certified. Registered redirect URI not inspected. | Callback path/logging unchanged; only its separate shared-server requests benefit. |
| React: `newadmin.vpsfree.cz/oauth/callback` | Already explicit protection: edge access off; `/oauth` and `/oauth/` error output suppressed; HTTP redirect access/error off. Internal nginx likewise suppresses OAuth access/error output. BFF callback catch logs only a fixed failure category and integer status. | Unchanged existing client protection, plus shared-server benefit. This is bounded normal-callback coverage, not proof about every dependency/pre-routing error. |
| KB: `kb.vpsfree.cz`, `kb.vpsfree.org`; DokuWiki oauth/oauthgeneric | Edge nginx explicitly uses combined logs; both KB vhosts and automatic HTTP redirects have no callback override. Internal DokuWiki nginx/PHP has no callback-specific log suppression in the selected module. Exact plugin callback path/application filtering unknown because the pinned plugin sources are absent locally. | Client routes/logging unchanged; shared-server benefit only. Ordinary edge query logging is established independently of the unknown plugin path. |
| Discourse: `discourse.vpsfree.cz`; configured OAuth2 basic provider | Selected module serves nginx -> Unicorn, with forceSSL and ordinary default request/error logging; no dynamic callback-specific exclusion in inspected config/module. Exact callback path and Rails/plugin filters unknown because the pinned application source is absent locally. | Client routes/logging unchanged; shared-server benefit only. No claim that an application filter also protects nginx. |

**Source anchors:** configuration `cluster/cz.vpsfree/vpsadmin/common/frontend.nix`
at249f:66–153,187–196,258–290,320–346 defines scope, logs and sockets;
vpsAdmin4a21 `nixos/modules/vpsadmin/frontend.nix:241,287`,
`haproxy.nix:187–193`, `varnish.nix:89–98` establish old proxy behavior;
33d6 `haproxy.nix:44,104–126` supplies per-instance `no log`.
PHP4a21 `webui/lib/login.lib.php:278–280`, `webui/pages/page_login.php:41–55`,
`nixos/modules/vpsadmin/webui.nix:216–228,257–285` establish callback/error/backend
handling (these paths unchanged at33d6). Configuration
`cluster/cz.vpsfree/containers/prg/proxy/config.nix:101–105,138–165,258–267`
contrasts React/KB edge policy; React606 `nixos/modules/webui.nix:100,137,164–169,572–575`
and `bff/server.js:284–290,334–385` establish exact callback and categorical errors.
KB config `cluster/cz.vpsfree/containers/int.kb/config.nix:220–231,258–277,337–340`
selects the providers/webserver; pinned nixpkgs `nixos/modules/services/web-apps/dokuwiki.nix:551–602`
defines PHP routing. Discourse config `cluster/cz.vpsfree/containers/discourse/config.nix:30–36,85–98`
selects host/provider; pinned `nixos/modules/services/web-apps/discourse.nix:881–932`
defines its ordinary dynamic route. None of these four client route policies is
changed by the proposed API/auth protection.

**Limits:** combined request logs contain the request target/query and selected
headers such as Referer/User-Agent, not automatically Cookie/Authorization or
body; HAProxy httplog alone likewise does not establish arbitrary header capture.
Varnish VSL can record request/response headers. Scoped nginx protection does not
cover errors before vhost/location selection or certify application logs. No
production logs, private configuration, registered client records or credentials
were read; no actual disclosure/exploitation is asserted. No tests, builds,
evaluation, fetches, live requests or source changes were performed for this
check. Existing delivery/rollback work and backlog remain unchanged.

### 2026-10-30: plan for the remaining OAuth clients

The user's subsequent request authorizes planning protection for PHP, both KB
sites and Discourse, with React unchanged. The focused implementation/deployment
plan is [oauth-client-log-protection-plan.md](oauth-client-log-protection-plan.md).
Exact pinned KB/Discourse sources were obtained and hash-verified for read-only
inspection; application logging requires more than proxy controls. The plan
identifies scoped proxy packages, concrete application sinks, bounded remaining
implementation preflights and later review/acceptance. The subsequent user
“proceed with implementation” releases E1/P1, E2/P2 and E3/P3 under the plan's
disjoint paths and one-worktree/E1-only Git contract. P2 owns PHP/FPM duplicate
error preflight; P3 owns earliest Discourse initialization/patch preflight.
Production access, real acceptance, deployment and integration remain unapproved;
this adds no gate to original3922 or the published a089 test work.

E1's concrete PHP callback gate subsequently releases minimal P0 in the same
plan: A0 owns only page_login.php plus its focused regression, isolated from
published a089. Put setup/provider lookup inside the callback try and catch
Throwable with a fixed diagnostic; preserve auth/session/redirect behavior.
Product quick checks and affected independent review/publication precede E1's
single final services-channel selection; config's final review/targeted installed
checks bind the resulting new output. No dependency refresh or native34 solely
for this PHP boundary change.

Postreview execution is now split in the existing plan's “Postreview execution
split (E1/E2/E3)” section: E1 owns six exact systems/config/output graph receipts,
E2 installed KB FPM/syslog/FastCGI plus minimal P0 transport proof, E3 actual
Rails/OmniAuth boot and logger sinks against private disposable state. Launches
wait final committed-source review. Scratch-only fixture work, exact output
handoffs, visible owner fallback for unavailable watcher840 and bounded milestone/
failure contracts are specified there; no duplicate quick campaign or live action.

### 2026-10-30: PHP-only scope and installed configuration corrections

The user canceled KB and Discourse OAuth changes. Their unshipped design/evidence
is historical, with no remaining diagnosis, rebuild or acceptance gate. Earlier
API/auth protection stays; React stays unchanged. The existing
[plan's current PHP-only boundary](oauth-client-log-protection-plan.md#current-php-only-correction-and-execution-boundary)
now owns the reduced package and exact two-file correction: common/webui.nix
forces the existing WebUI pool `error_log` option to PHP's `syslog` destination;
common/frontend.nix merges Basic auth into the generated dev vhost instead of
replacing its protection. Installed7fdb's missing native diagnostics and duplicate
unsafe dev servers are real configuration failures, not accepted runtime proof.

E1 owns source/history reduction and fixes only after the lead's safe-batch
release, preserving P075c and recovery refs. Fresh affected final review precedes
proxy + three WebUI system builds/effective-config proof; E2 owns only the minimal
installed P0 transport sequence proving useful diagnostics and sentinel absence.
No P0 dependency/source change, canceled-app checks, native34, live action or
production/default integration is added. Lead owns the reduced operator prose
and current status reconciliation. Original3922 and frozen prior refs stay intact.

### 2026-10-30: authorized disposable test-data cleanup

The user explicitly requests removal of unused temporary/test data to recover
disk space. This authorizes bounded file cleanup, not session lifecycle changes,
integration, deployment or stopping active operations. Session binding and roster40
reverified; architect0 retains Astra/xhigh/workspace_write. E1 owns candidates
under `/tmp` and `/var/tmp`; E2 owns raw generated artifacts under this session's
`work/2026-10-24-vpsadmin-haveapi-upgrade/` only. Neither owner follows a symlink
into the other's scope. Architect owns this brief and no deletions.

**Always preserve:** original updater3922 and all of
`/tmp/vpsadmin-release032-update-b6mfombs`; frozen33d6 source and its inputs;
all live `.dev-clusters` disks, sockets, shares, mounts and private state;
unfinished/uncertain operation inputs and recovery copies; accepted build outputs
and every Nix store path/GC-root link (including roots nested in scratch trees);
registered worktrees, Git objects/refs/indexes; compact Markdown/JSON receipts,
source/input/output identities, failed-attempt summaries and review/publication
proofs. Keep retained rollback/source/config/key material and current fixture
inputs needed for unfinished acceptance. Cancellation of KB/Discourse does not
alone prove that their daemon/build effects ended; use existing reconciliation.
No new diagnosis/tests of those canceled applications or update3922 are needed.

**Eligible classes:** completed, effects-reconciled native-test VM scratch disks;
stopped isolated fixture database/cache/session/browser profiles; duplicate
extracted source/archive or generated SDK/assets/transcript payloads no longer
needed to reproduce an unresolved failure or bind a pending acceptance. Eligibility
requires a session receipt, saved command or native record naming the exact path
and proving its purpose/owner; filename/date/Unix UID alone is insufficient.
Keep the compact evidence and final actual acceptance/publication records even
when redundant bulky payloads can go. Do not delete tracked files or the only
remaining recovery/input copy. A directory containing roots or retained evidence
must be handled by selecting disposable children, never by deleting its parent.

For each worthwhile candidate, confirm recorded completion/reconciliation and
no present writer, process/open-file or mount reference using checks limited to
that candidate and its recorded operation. Match saved process identities rather
than assuming a PID still names the same process. Recheck immediately before
removal, without stopping anything to make it eligible. Do not follow symlinks,
cross mount boundaries or use broad deletion globs; operate on explicit verified
paths. An inaccessible check relevant to the recorded owner/reference chain,
uncertain owner/use, active reference, mount or recovery dependency means retain
and report. Unrelated inaccessible process interfaces are not such a gap: this
does not require reading every machine process or proving a global negative.
No foreign-session scan,
global daemon/worker scan, elevation, root removal, Nix GC/store deletion,
coordination GC, lifecycle helper, reset/stash or archive/delete/stop is in scope.

**Bounded clarification after E1's preflight:** a completed isolated compiler
cache or redundant read-only source extraction is eligible on exact recorded
ownership and ordinary operation completion (including any recorded child/
detached-work reconciliation), stable owned path/inode, no recorded reuse or
pending/recovery dependency, and candidate-specific mount/reference checks.
Check any recorded still-live owner/handle or known consumer with normal access;
retain if that specific use cannot be resolved. A synchronous compile's final
successful exit and no later recorded reuse do not require a fresh global
`/proc` scan. Do not generalize this to VM disks, daemon state or shared caches,
whose existing owner/effects contracts still apply.

Concrete candidate `/tmp/vpsadmin-haveapi-upgrade-kb-checks/rust-consumer/target`
is named by `package-d/rust-shell-status.json` and `rust-rerun-command.sh`;
`rust-final-status.json` records exit0 after129s, ending2026-10-24T19:55:32Z.
E1's `disk-cleanup-20261030/tmp/rust-target-preflight.json` records no visible
candidate references, nested mounts, loop backing, symlinks or special files.
Its2475 inaccessible interfaces among811 other same-UID process checks are not
evidence of use of this cache. Subject to no known later reuse/pending dependency
and the exact-path/inode recheck, removal of this `target` alone is supported;
preserve source/manifest, receipts, roots and updater inputs. Parent accepts this
clarification before E1 applies it; no further machine-wide process scan is
needed. Report allocation by a consistent method: the retained preflight sums
209,711,104 bytes, while E1's reported allocated size is198,250,496 bytes; reconcile
accounting on that exact candidate without treating either as reclaimed yet.

The bounded extension through this session's21 registered worktree locations
found no additional image/large-file cleanup candidate: each root is below409MB
allocated, with no image file of at least1MiB apparent size or regular file of
at least64MiB allocated in the checked same-filesystem, non-symlink traversal.
Recorded test scratch remains in already-assigned temporary locations or
protected store/live-cluster paths. No additional worktree deletion is proposed.

Record a compact candidate/removal list with ownership receipt, disposition and
allocated bytes (`du -sx --block-size=1 -- <path>` or summed file `st_blocks*512`,
not apparent sparse-image size). Record filesystem free bytes before and after
with `df -B1` for the relevant filesystem. After removal verify only the exact
selected paths are absent and preserved evidence/root siblings remain. Report
allocated bytes removed separately from the observed free-space change: active
work, sparse files and hardlinks can make them differ. Stop a removal batch on
an ownership/reference/path discrepancy; retain uncertain candidates. No tests,
builds, new review campaign or per-file user approval are required for clearly
owned unused data within this brief. Lead retains original update/recovery and
status ownership; the session stays open.

### 2026-10-30: update3922 kernel diagnosis and recovery boundary

Fresh21:00UTC diagnosis verified the original driver3867340 → wrapper3867343 →
provider3867347 → Nix3871312 start identities. The Nix client was waiting on
daemon socket844432974↔844432118, not copying or activating a guest. Root SSH
through configured `root@172.16.106.40` with normal strict host-key checking
matched local hostname/boot ID; local sudo refusal was not an access limit.
Exact peer844432118 belonged to worker3871330, which was actively building
`/nix/store/md61flvfj3zp6k2a06kk5w3n2wbllm9h-linux-6.12.113.drv` through
builder18853/make44068/44071/2473823 and changing linker/pahole descendants.
The build used `make -j2`; an attributed106s interval added about990MB of writes.
The client cgroup had no OOM/resource-limit failure; filesystem availability was
68.4GB. Ordinary wrapper `Open3.capture3` hid provider build messages until exit.
This was an unexpected active local kernel build, not a demonstrated deadlock.

Lead/E0 owned the subsequent exact-client SIGINT and reconciliation: original3922
exited1 at21:08:22.937908UTC after18,809.732s; E0 reports the exact owned chain
gone, global daemon alive, locks released and no guest activation. Architect sent
no signal and did not duplicate those effect checks. Preserve the original
private attempt and raw diagnostic evidence at
`/tmp/architect0-update3922-diagnosis-l87ow37p` (0700/0600). Buffered355856-byte
stderr now records the kernel build and interruption; initial cache-miss reason
was not retained. No secrets/environment dumps were published.

**Why this dependency entered a services update.** The installed4x0 helper builds
the full `#cluster-config` before selecting the services target. Actual original
lock warnings identify OS `05201326975fc19d20a545c52f651cce0420dbc9`, tree
`54d79140bf9ead87293c3250e0837af52c853d02`, with nixpkgs
`6f06d204d8f2d8761d9da78778745974a3216381`
(`sha256-loLMnbbS4KhmG2ln9EY6f0YMNCA273Yx02oWYQ9IMeE=`), and unstable
`31ecbaca1bdefa45dffc409f0250bd8039ea0010`. Canonical staging later advanced4dfed;
do not relabel that as the original input. The full config derivation40pl79gq
references node1 and final kernelavd0kbbv; md61 is the base kernel needed by
zfs-builtin5jz7i6c2 before that final kernel. OS052 normally selects Linux6.12.113
source1dfea587. This differs from the isolated33d6 verification input graph;
there is no intentional HaveAPI/kernel-source change in consumer33d6.

**Cache facts and limit.** The configured trusted vpsAdminOS cache currently
returns200 for exact base outputs6fknvi25/8jpmywdp and final outputs
`/nix/store/b043pwyanxjfz22hbiibv5wipqqcl932-linux-6.12.113` and
`/nix/store/5kahy705jlci2fhhwmjr3hjn1cad8264-linux-6.12.113-dev`.
Base metadata was also read through ordinary Nix cache `path-info`, matching
md61 and the configured signer. Intermediate zfs-builtin output9dbnighk returns404;
substituting final kernel outputs need not rebuild that build-time dependency.
System substituters include cache.vpsadminos.org/cache.nixos.org, with fallback
enabled and the vpsAdminOS signing key trusted. No cache/trust/download error is
in the flushed update log. Exact historical cache decision rows/timestamps are
absent; present availability does not prove availability at15:54, nor establish
whether the original miss was publication timing or a transient failure.

**Do not blindly retry the original selection.** Retained6dsi config
`/nix/store/isj7505havzk1s606p10akz4d7lcxnj1-os-test-vpsadmin-devcluster-2026-10-24-vpsadmin-haveapi-upgrade.json`
mounts OS source `/nix/store/gdvfz3vl6fzcvb634aijn860lqha20q1-source` for all guests.
Original3922 candidate40pl instead mounts kw0iifzv (OS052). The installed
`maintenance.rb:855–880` preserves sharedFileSystems in its exact layout check,
so this candidate would be refused before pending/copy even if its build finished.
The public helper (`bin/devcluster:682–706,733–760`) has no OS revision flag or
environment selector: it uses a literal own `vpsadminos` worktree or mutable
canonical origin/staging and overwrites source environment values. Adding an
exact052 worktree is supported selection but changes the mount path again; it
does not fix this recovery. Do not rewrite shared refs, substitute a private
helper, waive layout, reset guests or silently advance OS inputs.

Safest recovery keeps consumer33d6, applied6dsi/private/auth state and the retained
OS source/mount. An owning supported selector correction or another explicitly
validated public mechanism is needed to bind that retained input; current
installed interface does not provide it. Lead owns that bounded recovery decision
and any implementation release. Once selection is settled, normal signed
substitution-only preparation (`max-jobs=0`, no remote builders, fail if missing)
can fetch the exact selected kernel outputs before the single public services
update. Current cache200 evidence is preparation, not realization or proof that a
different future graph is covered. Native layout/pending guards and actual final
output acceptance remain required. No retry/build/eval/realization, source change,
root release/GC, cluster lifecycle action or integration was done by architect.

### 2026-10-30: services-only applied OS selection correction (E0)

**Superseded by the user's 2026-10-31 selection correction below.** The prepared
acc4958/consumer132/package61v must not be activated: retaining the applied OS as
the build input no longer matches the requested policy. Preserve their evidence.

**Scope and base.** Correct the extension provider's ordinary `update <slug>
services` selection before its candidate build. Keep consumer33d6 and the applied
OS content/mount; do not upgrade OS inputs or change logging. E0 owns one isolated
`vpsfree-dev-workspace-services-os` worktree/feature branch from selected
`767dfd587e346168e1443e65ccdb67ce748f3fe3`. Installed4x0's `bin/devcluster` and
`lib/maintenance.rb` match that commit excluding packaging shebangs. Preserve the
existing ab9346b boot-proof branch/worktree and the writing-policy worktree.
No generic-runtime change, source33d6 edit, public flag or state-schema change.

**Authoritative selection.** Add a small read-only maintenance projection,
`applied-os-source`, using existing `applied_record` validation under the ordinary
cluster operation lock. Require a proven services descriptor in its provenance;
all recorded machines must have the same `sharedFileSystems.vpsadminos` string.
Return that exact existing immutable store source directory, with `flake.nix`
and `flake.lock` present. Reuse existing store-path validation. No Git lookup,
mutable worktree/ref fallback, inferred residency, new journal or state write.
The retained source is
`/nix/store/gdvfz3vl6fzcvb634aijn860lqha20q1-source`, proven by config
`/nix/store/isj7505havzk1s606p10akz4d7lcxnj1-os-test-vpsadmin-devcluster-2026-10-24-vpsadmin-haveapi-upgrade.json`
(SHA256 `0d77159082ce08d893578badf91484a8d04466ab8105a35b8e2488ae03dedfc2`).
Its locked root nixpkgs is718f670e845328e9c2cecdd832835712b2cbd065.
The OS Git revision is not established by these retained records: exact immutable
content/path is authoritative; do not substitute original3922's different052013.

**Pending and missing state.** Accept no pending operation, or exactly pending
`operation=update, targets=[services]`. A same-target retry selects the prior
`configuration` descriptor, never the pending candidate; existing layout checks
still validate the new candidate. Reject another target, boot/copy pending state,
absent services proof, missing/mixed/non-store source or unreadable applied
selection before build/copy/pending writes. Explain that services update requires
a known retained immutable OS source and that the operator must resolve retained
selection through the existing recovery workflow; never recommend reset as an
automatic remedy. Do not require complete provenance for unrelated guests:
partial legacy records with proven services and matching mounts remain usable.
An unproved legacy services selection now fails deliberately rather than choosing
today's OS. `retained_config!` is unsuitable because it forbids pending retries.

**Helper interface and compatibility.** Call the projection only for ordinary
target exactly `services`, before credential preparation and the candidate build.
Thread its result through optional internal arguments to
`build_config_with_credentials`/`build_config`. Both input overrides (`vpsadminos`
and `vpsadmin/vpsadminos`) become `path:<retained-source>`; export that identical
path as `VPSADMIN_DEVCLUSTER_VPSADMINOS_SOURCE`. Skip worktree Git metadata lookup
in this branch: revision is empty/unknown and dirty is0, using the existing flake
null-revision behavior. Do not invent a SHA or generalize `source_revision`.
Generated candidate node revision labels may therefore be unknown; services
promotion must continue to retain untouched node descriptors and provenance.
Start, default/all, node/storage targets and maintenance `services --copy-only`
keep their existing input/recovery behavior. Preserve strict `machine_layout`,
generation/ownership/locks, roots, private source mounts, credentials/session
values, candidate failure handling, copy/activation/proof and promotion ordering.

**Owning files and acceptance.** E0 edits only
`dev-clusters/vpsadmin/{bin/devcluster,lib/maintenance.rb,README.md}` and
`test/{devcluster_commands_test.rb,devcluster_maintenance_test.rb}` unless a
concrete dependency is reported. Extend the existing stubbed command harness and
applied fixtures: moving staging or adding a different optional OS worktree must
not change either override or the source mount for services; no Git command may
target the retained store directory. Test missing/invalid/mixed source and
unproven services refusal before build/copy/state/credential changes; same-target
retry uses old applied source, conflicting pending state refuses. Preserve
credential-byte/mode and lock-release assertions, failed-build behavior, strict
mount-mismatch rejection, other-target/default/start/copy-only behavior, and
untouched node provenance. Prepare valid applied fixtures explicitly where old
services tests had no envelope; do not weaken their original assertions.

Run the two focused Ruby suites in the declared development environment, syntax
and normal hooks, then commit the focused final history. Mandatory independent
affected-source and complete-history review precedes normal
`nix flake check --print-build-logs` and `nix run .#devcluster-check`; the latter
checks installed flakes/runners without VM closures/start. No host-migration VM,
whole-cluster/kernel build, provider/browser campaign or real cluster retry is
needed to prove this selector. Stop unexpected kernel realization. No migrations
or on-disk format changes are expected; old packages can still read the state.

**Consumption boundary.** Publish the reviewed extension feature normally;
prepare its exact consuming-workspace input/package through the existing
`lib.mkPackage`/workspace pin flow, preserving the selected generic runtime and
unrelated inputs/siteConfig. Source preparation does not install it. Explicit
approval is still required before normal workspace package activation, with
existing generation/schema/coordination and rollback checks. Never replace an
installed helper or invoke modified private helpers against the live cluster.
After approved activation, separately prepare the selected graph with local and
remote builders disabled, then use the ordinary public services update under
lead ownership. Cache availability and successful selector tests alone do not
prove that final graph or authorize retry. This brief ran no tests/builds/eval,
network queries, runtime changes or product edits.

### 2026-10-30: consuming workspace package preparation for services OS fix (E1)

**Historical baseline:** the 2026-10-31 refresh below supersedes this section's
0548/4155/profile214 baseline and choice of configuration checkout. Its two-file
extension update, verification and unapproved activation boundaries still apply.

**Selected baseline, read-only proof.** User profile
`/home/aither/.local/state/dev-workspaces/profile` selects `profile-214-link` →
`/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`
(deriver `gia18wgbmc0ssxr81qykk076rmh0kl6d-dev-workspace-0.2.0.drv`).
Its generic source `/nix/store/1jliyjqz4abknq16kwp8afw6m5k3yqqi-source` has NAR
`sha256-hxhPj+obva7nETfnBTNZlmup+qqHERnZHI7zUdLcwkw=`, matching locked runtime
`4155d0099d03028b43d5f08d225a88156cb4155a`. Installed extension4x0 uses source
`/nix/store/lfmiclfqmpw7bs99lil6x5f83ba1j070-source`, NAR
`sha256-om/+qNfQw6y74gjdzXfVG5AbHOQGysMefFZiqR92KP4=`, matching767dfd5.
Installed package's workspace source reference is
`/nix/store/37drc0djnn5gk8k7jm5i3r8y77l5v218-source`; no Git head is inferred
for that immutable snapshot. Local master and local origin/master observed at
`0548c2fbb6e7fa70bc99f0fb5511dae99f38410b` have identical flake.lock,
registration, site/team/coordination/integration/cluster configuration and
update-codex skill to that snapshot. The sole flake.nix difference is an added
storage-retention check, not changed package composition. No baseline blocker.

**Isolation and exact pin.** After E0's final provider commit, independent review
and publication, E1 owns a new registered workspace feature worktree
`worktrees/<slug>/workspace-services-os`, branch
`2026-10-24-vpsadmin-haveapi-upgrade-workspace-services-os`, from the fresh verified
workspace default (currently0548). Follow normal workspace worktree/hook rules;
leave shared master and our existing workspace policy branch eeec0c4 untouched.
Do not include extension boot-proof ab9346b or writing-policy d4355518. If the
fresh default changes installed runtime/site composition, report that delta
before selecting it; do not turn this repair into an unrelated package upgrade.

Edit only the extension URL in `flake.nix` to
`github:vpsfreecz/dev-workspace/<exact-reviewed-published-E0-SHA>`, then run
`nix flake update vpsfree-dev-workspace` in the isolated worktree. Generate
`flake.lock` normally; never edit it manually. Preserve the explicit nested
`inputs.dev-workspace.url` selecting4155, root nixpkgs follows, extension child
inputs and every unrelated locked identity/follows path. Compare semantic paths,
not generated node names. The intended delta is only the extension's source
revision/NAR/metadata and corresponding original URL. Do not update the nested
runtime or extension's own lock.

`config/coordination.nix` already maps the extension to workspace input
`[vpsfree-dev-workspace]`. However, `config/integration.nix`'s existing
`refreshes.workspace` recipe targets repository `dev-workspace` and nested input
`[vpsfree-dev-workspace, dev-workspace]`; invoking it would refresh the wrong
component. Use the ordinary two-file pin update above, with no recipe/config
redesign. `lib.mkPackage` remains the sole composed package constructor and
`packages.x86_64-linux.default` the output. Both our configuration worktrees lock
`devWorkspace` to4155, so this extension-only repair needs no configuration pin
or system deployment.

**Verification and reviewable candidate.** Capture exact old/new workspace
base/head, extension review/publication identity, complete semantic lock graph,
unchanged runtime/source hashes and siteConfig. Run existing deployment-contract
Ruby tests and normal hooks, commit the two-file update, and assess final history
and mechanical-pin review reuse with the E0 review; a composition deviation needs
affected review before longer checks. Run normal workspace `nix flake check
--print-build-logs`, then `nix build --no-link --print-out-paths .#default` and
`bin/check-dev-workspace-deployment --workspace-root <candidate> --configuration-root
<our-configuration-worktree>` against the exact locks. Do not repeat E0's source
suite or build cluster/host VM closures. Stop unexpected local kernel work.

Bind the resulting package/store derivation and its installed provider source
to the final published E0 commit (account for packaging substitutions), unchanged
generic runtime, site/provider catalog and generation/schema/recovery contracts.
Normal selected `workspace-host prepare --source <candidate> --json` can then
perform supported compatibility preparation and retain a candidate artifact/root;
it builds/checks and records preparation but does not select the profile. Keep
its exact source identity, predecessor profile token and candidate package in
our receipt. It is a later E1 preparation action, not executed by this design.

**Activation boundary.** Present the built/reviewed exact candidate to the user
before requesting activation approval. No claim is needed for feature source,
checks, publication or preparation. Approved activation later uses normal
`workspace-host switch --source <candidate>` under the configured
`vpsfree:aitherdev` machine claim and exact session environment; current-generation
admission and compatibility checks remain authoritative. Preserve predecessor
and original recovery evidence; profile recovery is forward-only, not an
automatic rollback. Approval to switch does not authorize default integration or
a private helper/live patch. Lead separately owns the eventual public services
retry. This task performed only source/metadata reads and local content hashing;
no build/eval/network/source pin/claim/profile/cluster mutation occurred.

### 2026-10-31: final consumer refresh for selected profile216 (E1)

This supersedes the earlier0548/4155/profile214 and9e/f05/profile215 consumer
baselines. Use the existing registered `workspace-services-os` alias/worktree;
its layout was subsequently released by lead and it now exists. Preserve the
separate eeec policy registration and both frozen4155 configuration branches.
Do not recreate a second workspace registration or duplicate policy obligations.

**Fresh baseline and installed binding.** E1 owns the completed SSH/default/profile
guards in `updater-services-os/consumer/same-selector/baseline-stop.json` and
`baseline-drift.diff`; architect did not repeat them. Workspace default is
`4737ef1449278f2b8d9b8398178008cfe401fb3c`; published consumer remains
`13232fe8f4371bc79546195424a85fd2a030b87a`, with old preparation preserved.
Profile216 selects `/nix/store/sj07yk7l85j01h2z2qr3nqi2rdljnlds-dev-workspace-0.2.0`,
deriver `/nix/store/g5gnkhlclyyn2wbzl9rxc9cq6bashgy9-dev-workspace-0.2.0.drv`,
catalog `sha256:9b9773cf14a3c4b7439c88427529ea181824658abc7721bd557bbd454981893e`.
Its derivation binds generic source
`/nix/store/rl8c57hw2xd7pnvi99rd5ipn768k75m0-source`, measured NAR
`sha256-qxtRcCtVsav41/23Wu8P4ZWvOGWs5FqvPxbmbFengcY=`, and workspace source
`/nix/store/w9ln2a2slq14a3mlvpx90cyxld1gjmfc-source`.
Both installed snapshot and4737 lock generic
`6f54d0c7fdb974705c120b3c1ef5372f5897d544`, codex-web
`d3a29bee90ef00a08816920408c596152339a637`, and extension767dfd5. Installed
extension tools are `/nix/store/6hapsj44krhczcyijm3kmqz0z8yfdj7f-vpsfree-dev-workspace-tools-0.1.0`.
Bounded composition files match the installed snapshot; site, registration, team,
coordination, integration and cluster configs remain unchanged. This is a changed
runtime revision already selected outside this session, not merely metadata drift;
preserving it does not require a new audit of unrelated runtime behavior.

**Source/history disposition.** Reconstruct the uninstalled consumer on4737 with
one final extension pin767 → reviewed/published corrected provider
`3fdecfbbdd93f92754a0384d0134958c260cf619`, plus one separate existing instruction
repair. Preserve published132 and old preparation/recovery refs before ordinary
feature-history refresh. Keep the nested generic6f54 URL, codex-webd3a and every
unrelated semantic locked input/follows unchanged. Edit the extension URL and
regenerate with `nix flake update vpsfree-dev-workspace`; do not invoke the generic
runtime refresh recipe or restoref05/4155. E0 owns remaining provider checks.

The independent repair is NOT upstream:4737 AGENTS.md and
`test/agent_instructions_test.rb` are byte-identical to original9e (16875-byte
AGENTS, original locale-dependent reads). Carry132's reviewed repair once,
unchanged: its two concise paragraphs and explicit UTF-8 reads remain needed.
Record patch equivalence and retain the unchanged assertions/cap; do not duplicate
it, drop it as upstream, or rewrite policy. The deployment checker and its tests
are unchanged. Final history should contain the current pin and that repair only,
without obsoleteacc pins or unrelated boot-proof/writing-policy content.

**Configuration and compatibility.** Bounded local canonical configuration ref
is `e34f08314b6db1ac38facc2386b79111daee864f`; `devWorkspace` already locks6f54
with the same NAR, and aitherdev site bytes equal our prior reference. No channel
update, new configuration branch or host-system rollout is required. E1 should
export unmodified canonical `flake.lock` and
`cluster/cz.vpsfree/machines/aitherdev/dev-workspace-site.nix` at that exact commit
into the owned source-reference directory, bind commit/blob hashes, and run the
unchanged deployment checker against the final consumer and this reference.
This proves source contract equality, not the host's deployed configuration SHA.

Generic6f54 versus prior installedf05 has byte-identical `nix/host-module.nix`,
`nix/host-paths.nix`, claim/repository-claim/coordination/integration contract JSON,
and `portal/internal/session/runtime-contract.json`; installed coordination and
recovery guides are byte-identical too. No host compatibility change is introduced
by the extension-only candidate. Preserve these identities and the current
profile token in the candidate receipt; normal selected package preparation must
still check actual generation/state compatibility. Do not infer it from hashes
alone or read other sessions' private state manually.

**Acceptance and authority.** E1 may resume the narrow consumer source package on
this baseline. Retain prior results only with exact unchanged source/input/derivation
scope; current final source/history needs the affected review/equivalence decision,
normal quick hooks/checks, package verification and exact provider/source graph
binding. No duplicate E0 source-test campaign. Use selected sj07 for ordinary
preparation and later activation; stale132/61v preparation cannot be reused for
the corrected candidate. Recheck generation/default at the normal final boundary.
The user now explicitly authorizes corrected workspace application deployment on
aitherdev once done: do not request that approval again. Normal machine ownership,
compatibility and source-bound switch verification remain required. Default
integration, host-system rollout, reboot, export-layout transition and cluster
retry remain outside this preparation disposition. This design refresh performed
only source/metadata reads and hashing plus this section edit; no source/ref,
build/eval/prepare/claim/profile/cluster/storage/lifecycle mutation.

### 2026-10-31: second workspace checkout constraint (consumer layout correction)

E1's public add failed before creating a path/ref; retain its recorded effects.
The earlier `workspace --name workspace-services-os` instruction was incorrect.
Installed f05 `libexec/dev-session:2717` requires project workspace to use name
workspace; its existing registration at2746 requires the same branch. The
published `docs/dev-sessions.md:1037` likewise reserves that single name. Manual
Git creation does not solve registration: `validate_worktree_path!` at7086
requires a non-workspace alias to belong to a canonical bare repository, while
the shared workspace common Git directory is non-bare and outside repos/.
No second-workspace registration entry point was found in this bounded pass.

Keep policy branch eeec0c4, its checkout and registration unchanged. A separate
canonical bare clone of the SAME workspace remote could technically use the
ordinary independent-project add/capture machinery, with a distinct registered
alias and fully tracked branch obligation. It is not an independent repository,
however: `docs/agent-instructions/git.md` explicitly says the top-level workspace
workflow is complete and the bare-repository rules apply only to independent
project repositories. Therefore it is not presently a compliant workaround.

Under the combined constraints there is no supported layout for this second
independent consumer branch. Lead must resolve that exact layout-policy conflict
before E1 edits source; do not patch runtime, alter a registry, rewrite policy,
create a new session or leave an unregistered branch. The smallest potential
exception is a declared additional canonical bare clone of
`git@github.com:aither64/vpsfree-cz-workspace.git`, public registration under a
unique non-workspace project/name, and normal feature worktree/branch from9e.
If explicitly authorized as a layout exception, retain BOTH registered final
heads/obligations; integration would still go through the shared workspace master
and its normal approval/claim/tracking-lock workflow, never the alias default.
Do not execute that option on this design note alone. Provider checks and all
baseline/activation constraints remain independent and unchanged. Architect made
no repository, registry, worktree or runtime mutation.

### 2026-10-31: consumer baseline instruction-check repair (E1)

The failed67c check inherited two independent defects, established by E1's
`updater-services-os/consumer/verification/attempt-1/first-failure.json`:
AGENTS.md is16875 bytes against the existing16384 cap; locale-dependent text
reads raise US-ASCII errors. Base9e, head67c and failed immutable source agree.
Repair only `AGENTS.md` and `test/agent_instructions_test.rb` in the existing
consumer worktree, in a separate coherent commit after the mechanical pin.
No provider/runtime/config input or policy changes.

**Exact small prose reduction.** Replace the paragraph beginning `Repository
claims cover approved shared merges only` through `recovery contracts.` with:

```text
Follow the mandatory Git procedure for repository claims; only approved merges
need them. For machine reservations and automatic release, follow
[machine retention](docs/coordination.md#machine-retention), preserving existing
recovery contracts.
```

Replace only the prose under `Rule Precedence` with:

```text
This AGENTS.md governs workspace orchestration, tracking, worktrees, SSH remotes,
cross-project planning and compatibility. Repository-local AGENTS.md controls
its repository's structure, style, commands, generated files, releases, hooks,
branches, PRs, commits and tools. Follow local content rules while preserving
workspace tracking, compatibility and SSH remotes. Derive commands from that
repository's instructions, manifests and CI; never apply another repository's
rules or commands.
```

In-memory byte calculation against actual67c gives16356 bytes (519 saved), below
the unchanged cap. No file was edited or test run for that calculation. The Git
procedure's mandatory opening paragraphs already retain preparation without
claims, exact approved critical section, hooks/SSH push/remote proof, release
before CI/records/cleanup, intervention and uncertain-effect reconciliation.
Its route covers every affected activity. The machine link and original recovery
obligation stay explicit. The second replacement retains workspace/local scope
and conflict precedence; concrete manifests are examples, not separate policy.
All team settings, approval gates, lifecycle rules, compatibility requirements,
review timing and mandatory routing remain untouched. No procedure move needed.

**Encoding boundary.** Add `encoding: 'UTF-8'` to the remaining `File.read` calls
in this test file, matching its existing routed-reader test. Keep `File.binread`
for byte counting and retain every assertion/regular expression and the16384 cap.
Do not change process-wide default encoding, Nix locale, production readers or
test structure. This is deterministic decoding of known UTF-8 guidance.

**Checks and history.** E1 checks the exact two-paragraph diff against the mapping
above, unchanged routes/assertions/cap and bytesize, then runs only the focused
`test/agent_instructions_test.rb` in the declared environment with
`LC_ALL=C LANG=C ruby -EUS-ASCII test/agent_instructions_test.rb`; normal hooks
still apply. That reproduces the failing default text encoding while exercising
all original assertions. Commit separately from67c; final complete consumer
history/diff receives affected independent review before resumed long package
checks/build/publication/preparation. Keep failed evidence. Reuse passing checks
only for exact unchanged source/input/derivation scope: changed workspace source
means no blanket reuse of prior workspace results; unchanged provider/generic
derivations retain their actual evidence. E0 alone owns the disappearing-output
retention issue. No duplicate generic campaign, GC/storage inquiry, activation,
claim, integration or cluster action is part of this repair.

### 2026-10-31: same OS selector for creation and updates (superseding design)

The user requests the same selection rules and notes that intentional OS updates
can be desirable. Supersede acc4958's services-only applied-input pin; prepared
consumer132/package61v remains uninstalled and held. Preserve all original refs,
checks and recovery evidence. Consumer33d6 and reconciled3922 remain unchanged.
This section is a recommendation for lead disposition, not authorization to
implement a new restart/migration mechanism or activate the prepared package.

**Selection and effects are separate.** Keep `vpsadminos_input` unchanged for
creation and every ordinary update: literal own `worktrees/<slug>/vpsadminos`
checkout when present, otherwise canonical locally fetched origin/staging,
resolved at the operation's Nix build. No implicit fetch or fallback to old OS.
Both input overrides use that selection. Selected checkout HEAD/dirty or resolved
flake revision describe build content, not the source export mounted in guests.

`services` copies/switches the NixOS services system built with selected OS inputs
and their nixpkgs; it does not switch a vpsAdminOS node. Its existing API restart
and node seed/pool/nodectld refresh remain explicit effects. `node1`, `node2` and
`storage1` switch only that selected vpsAdminOS guest. `all` iterates configured
services, nodes/storage and DNS targets sequentially, preserving pending/provenance
per target. These existing switches update userspace/system selection; they do
not replace a running kernel. The applied direct-boot kernel/initrd/squashfs can
be used by a later supported cold start. No reboot or broader target is implied
by a services request or by the user's comment that OS upgrades can be useful.

**Actual source-share constraint.** Provider `nix/test.nix:991–1020` separately
uses `vpsadminosSourcePath` for virtiofs and `vpsadminos` for imports/build inputs.
The bounded source reads found no provider service using `/mnt/vpsadminos` as its
live executable tree; it is the guest-visible development source export.
OSVM `machine.rb:168–180,877–896` captures the host paths and starts virtiofsd with
`--shared-dir` at boot. The runner reads configuration once (`shared/devcluster_runner.rb:161–197`).
Ordinary update copies a system and invokes its switch command; it cannot move
the live export. `maintenance.rb:855–880` correctly keeps all shared filesystems,
host qemu/virtiofsd, disks, network, resources and boot options in exact layout.
Thus newly selected052/kw0 versus retainedgdvf is a real mismatch, even if every
kernel output is cached. Cache metadata resolves neither this mismatch nor target
authorization. Merely choosing `all`, stopping/starting, or editing provenance
does not supply a supported source-share transition: retained cold start checks
layout and boots the applied selection.

**Recommended smallest coherent repair.** Keep the current selector, and separate
the candidate's build sources from the already-running VM environment. A validated
read-only applied update context supplies retained boot metadata, not an OS input.
Preserve the exact existing vpsadminos export path (including a mutable own
checkout if that was booted) and host `qemu`/`virtiofsd` paths; never copy new
contents over an immutable source or claim that its Git revision changed. Select
guest package inputs and revision metadata normally. State plainly in the command
output/README that a different selected build source leaves `/mnt/vpsadminos` at
its boot source; this preserves OS upgrades without silently mislabelling the
export. Other shared mounts and credential paths remain exact.

Build an update configuration from the existing lazy `clusterConfig.config`
interface (`tests/make-test.nix` returns `{ config; json; }`), rather than realizing
the full new `clusterConfig.json`. Validate requested topology/layout independently
before projecting payloads: preserve only the named boot-host paths/export above,
then compare every other existing non-update layout field exactly. A change in
CPU, disk, network, another mount, boot mode or kernel options must still refuse;
do not blindly merge the whole old layout over requested changes. Keep
`compatible_configuration!`/`machine_layout` unchanged as the final guard.

For a single target, carry untouched applied guest descriptors exactly and use
only that target's new permitted system/boot payload fields. Preserve its old
NixOS source `rootDisk.image` because the existing disk is reused. For `all`, use
new payloads for the actual existing target set, preserving staged per-target
promotion. This avoids realizing an unrelated node kernel for services-only work;
selected services kernels/closures can still be genuine dependencies and remain
subject to the unexpected-local-kernel stop rule. No promise of cache success.

Apply the same boot-metadata distinction to retained-start compatibility so a
later cold start does not fail solely because the source selector or host QEMU
package moved. Fresh creation remains unchanged. Retained start boots proven
applied payloads, not arbitrary newly selected systems; it does not retarget the
export. Pending same-target retries use old applied VM metadata and a normally
selected new candidate; other pending operations still refuse. Missing/unknown
applied VM context cannot be guessed from result-config or today's inputs.
Preserve existing partial-provenance semantics where sufficient actual descriptors
exist; do not manufacture proof for untouched guests. No state-schema migration.

**Execution boundary if accepted.** One extension package: `bin/devcluster`,
`lib/maintenance.rb`, `flake.nix`, provider README and existing command,
maintenance and Nix-smoke tests; `nix/test.nix` only if the existing source-path
argument needs wiring. No generic runtime, OSVM or vpsAdmin33d6 changes. Retain
acc4958 as historical evidence and form a clean corrected feature from selected767
without importing unrelated boot-proof/writing-policy work. Refresh the consumer
pin once the corrected provider passes quick checks, committed-source/history
review and normal affected package checks; previous semantics tests are not proof
for this changed design.

Focused regressions must prove creation/services/node/all use the same selected
OS after staging or own checkout changes; build revision stays selected while
source export/host tools stay retained; requested layout mutations still refuse;
services never forces an unrelated node payload (use a lazy throwing fixture),
never activates another system, and keeps existing refresh ordering. Cover exact
untouched descriptors, credentials, same-target retry/conflicting pending state,
failed build before copy, incremental all promotion, and retained cold-start
selection. Nix checks inspect the selected graph without realizing VM closures;
long installed/disposable acceptance follows final review, not a new full provider
or browser campaign. The implementation must report a concrete interface gap
instead of growing a generic update/observability framework.

**Alternative/product boundary.** If the user also requires `/mnt/vpsadminos` to
expose the newly selected immutable source, this recommendation intentionally
does not provide that. Actual retargeting requires stopping the owning virtiofs/QEMU
processes and a supported change to retained boot-layout evidence. The current
public update/start contract has no such transition. That is a separately scoped
restart/layout capability and needs an explicit decision before design or action;
neither guard weakening, private patch nor reset is a remedy. Intentional guest
OS updates with unchanged VM layout remain supported by the recommended ordinary
target path. No source edits, build/eval/network/live query, activation, claim,
retry or lifecycle action occurred during this reassessment.

**Target-context proof clarification (E0 question).** Require existing validated
provenance for each requested update target before preserving its boot metadata:
a single target requires its own proof; `all` requires every target it will switch.
Use existing accepted provenance kinds and `applied_record` validation, without
a new boot-proof schema or a `prior_boot`-only restriction. Any other proven guest
is insufficient to prove this target. Untouched, unproved descriptors may remain
in a partial envelope and are carried exactly without gaining provenance; their
presence must not block a proven services/node target. Pending same-target retry
still needs that target's previous applied proof; an initial pending candidate
with no prior proof cannot supply the retained context.

This intentionally refuses a first update of an unproved legacy target, including
an absent envelope or `empty_applied` descriptor. Existing legacy target-updatable
wording therefore needs this narrow qualification: retaining actual host/export
metadata cannot infer it from a candidate. Lead accepted this narrow compatibility
consequence in disposition49fe390e to E0; no additional user gate is required.
Do not claim all old partial-update paths remain supported.
Use the existing explicit residency-recovery contract when suitable evidence
exists, never another guest's proof, reset or a new recovery mechanism. Tests must
distinguish proven target with unproved peers (allowed), unproved target with a
proven peer (refused before build), all with missing target proof (refused), and
same-target retry with/without prior proof. This does not affect this cluster's
already proven selected targets.



### 2026-10-31: retained-start refusal from a newly detected configuration export

Original public `start --existing`17669 failed before guest launch with the
retained topology/layout refusal (exit1/58.549714s). Installed profile217/ns0,
consumer35510cb, providerd632caf/toolsac34, frozen vpsAdmin33d6 and normally
selected local OS628b4a7 remain the diagnosis inputs. E3 owns effects evidence:
stopped/not-ready, pending null, four retained proofs/payloads, disks and runner
log unchanged; no successful boot or promotion. Preserve the original private
attempt `/tmp/vpsadmin-retained-start-3w1y0qdk` and E3's receipt.

**Exact cause.** The offline lazy `make-test.config` layout comparison succeeded
in115.754s with IFD disabled, zero local build jobs and no builders. After applying
only the accepted qemu/virtiofsd/vpsadminos-share preservation, exactly four fields
differ: `machines.{services,node1,dns-primary,dns-secondary}.sharedFileSystems.config`.
Each was absent and is now the literal own
`worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-cz-configuration` path.
Every other nonpayload field matches, including kernel arguments, resources,
disks, networks, other mounts and top-level metadata. Selected OS is
628b4a7c43b51d11ed8726188497a09f64814833 with nixpkgs
6f06d204d8f2d8761d9da78778745974a3216381. No inference about when or who created
that checkout is needed.

Installed `bin/devcluster:693,838,784` detects the optional literal configuration
checkout and passes `VPSADMIN_DEVCLUSTER_CONFIG_SOURCE`; `nix/test.nix:998–1000`
adds the virtiofs export and1030–1035 declares `/mnt/configuration` in guests.
`configSourcePath` has no other use there. This is a real automatically requested
new export, not equivalent representation, OS-default drift or an omission from
the accepted OS-specific projection. The strict guard correctly rejects it.
The earlier full-JSON evaluation exited1/137.177s because IFD was disabled for
`vpsadmin-source-33d6…`; that was a diagnostic expression boundary, not the product
failure. The narrower expression removed payloads before serialization; its one
root-node metadata correction and both results remain private under
`/tmp/architect0-retained-start-layout-3o2vdde9` (0700, files0600), including
`effective-inputs.json`, `layout-only.nix`, `layout-only.json`, `layout-diff.json`
and command/result receipts. No realization, source/lock write or cluster action
was performed by this diagnosis.

E3's config.json timestamp is separate: `ensure_cluster_config` always merges
packaged defaults beneath saved settings using jq and replaces that file
(`bin/devcluster:146–171`), before the later failed layout check. Without a saved
preimage, do not claim unchanged bytes or attribute a particular value change.
The differing export is derived from checkout presence, not from config.json.

**Accepted minimal disposition.** Lead explicitly accepted the narrow product
consequence and authorized E0 implementation after this brief. No additional
user decision gate applies to this correction. There is no installed public option to suppress this auto-detected export.
`--copied-config` requires the separate maintenance hold/copy contract; it is not
a general retained-start workaround. Preserve both registered configuration
worktrees, paths, refs and private files. Do not move them, override the helper's
environment, fabricate a maintenance hold or amend applied evidence.

Treat this automatically detected configuration share as creation-time convenience:
in `build_config`, when a validated nonempty retained context has no `config`
export in any machine descriptor, leave automatic `config_source_path` empty
before `nix_common_env`. Use the existing validated context passed by maintenance;
empty/null context retains fresh-creation behavior, and malformed context must
fail rather than being treated as an absent export. Fresh creation continues
detecting the checkout normally.
When a retained config export exists, keep current selection and exact comparison;
missing, changed or inconsistent exports must still refuse. Do not silently
preserve or strip arbitrary requested mounts, add `config` to projection exceptions,
or alter `compatible_configuration!`. Existing `nix/test.nix` then consistently
omits both host export and guest mount for the absent-share case. All ordinary OS
selection rules, target effects, proof/pending rules and other layout checks stay
unchanged. This is a narrow additional policy decision: adding a configuration
worktree alone does not attach it to a retained cluster. An intentional attachment
remains a separately scoped layout transition; this package does not provide one.

**Owning implementation package (E0).** Extension only:
`dev-clusters/vpsadmin/bin/devcluster`, its README,
`test/devcluster_commands_test.rb`, and `test/devcluster_nix_smoke.rb` as needed
for the existing regression fixtures. No state schema, maintenance recovery,
OSVM, vpsAdmin33d6, configuration repository or generic runtime change.
Cover fresh creation with the checkout (export included); retained boot/services/
node/all and same-target retry with the newly present checkout (auto export stays
absent); already exported matching path (unchanged); missing/retargeted/mixed
retained config exports (refuse); and direct candidate additions/removals of config
or another mount (strict projection still refuses). Check the existing Nix fixture
omits both export and guest mount when the resolved source path is empty, preserves
all other layout fields and does not force unrelated payloads. Quick focused checks
and normal hooks precede committed-source/history review; then use normal affected
package checks and the already established consumer pin/application deployment
path. E0 owns provider source/tests/technical docs; parent owns the prose pass,
review and application activation coordination. Lead owns any later actual
retained-start/update. This brief itself launches no retry, activation or broader
export transition. Original failures and scoped evidence remain preserved.


**Installed-check coverage clarification (b918 follow-up).** The new config-export
Nix assertions currently run only in `--projection-only`, which exits before the
normal five-argument packaged checker. Raw quick success does not prove installed
coverage. Repair only `test/devcluster_nix_smoke.rb`: share the existing assertion
expression/runner and invoke it once from normal packaged vpsAdmin checking as
well. Parameterize the provider and fixed fixture inputs; packaged mode must use
its supplied PACKAGE's `flake.nix`, `nix/test.nix` and installed default config,
plus the existing fixed vpsAdmin/OS inputs (normal OS-selected nixpkgs). Raw mode
keeps its fixture-default copy. No developer-source fallback, duplicated assertion
body, new public option, product/guard change or expanded scenario campaign.
Keep explicit successful config-export/guest-mount and strict refusal output in
the final installed receipt. Focused quick checks and a coherent test-only commit
precede affected final review; run the actual final packaged checker afterward.
Earlier raw evidence remains scoped to raw source. E0 owns this repair; parent
owns review and final package verification/release scheduling.


### 2026-10-31: current services update5781 is building application dependencies

User requested fresh diagnosis of the silent services update begun13:13:30UTC.
Normal root SSH to172.16.106.40 matched the local hostname/boot ID. Revalidated
original Nix740180/start5442124, FD3 socket16228792 and reciprocal16230880;
that peer belongs to daemon worker740200/start5442131. No client pipe was read,
no signal or new Nix evaluation/build was issued, and parent retains original5781.

The worker advanced from console-router-env to React frontend and then Go
`/nix/store/mk599vhadmcvxdw8xdddvlway02x9y34-vpsf-status-a5be7b9.drv`
(output89px5a06zjbv835f0sy02p1s9wpgnia1). A53.21s observation crossed completion
of frontendx4xlbpd1pb190fv06p82ds5miawx8mik (its log reports18.73s frontend build,
then install/fixup) and creation of the Go compiler subtree. This proves progress,
not a static lock/download wait. Original NIX_CONFIG explicitly selects
`max-jobs=1`, `cores=2`; the attributable builder also has NIX_BUILD_CORES2.
Worker-held roots reference700 derivations with logs modified since operation
start, including113 Ruby-named and258 systemd-unit derivations. This describes
recent dependency build-log activity, not exclusive authorship of every log.
The only two Linux-named logs assemble/shrink existing modules; neither compiles
a kernel. Filesystem available space was138.9GB; E0's existing scope receipt shows
zero OOM events. The buffered wrapper hides ongoing build output until exit.

Current evidence supports letting this exact advancing operation finish, not a
source fix, daemon action or blind retry. No completion estimate or historical
cache-miss explanation is established. Restarting solely to raise concurrency
would abandon the current unfinished build and repeat evaluation. Parent owns
any subsequent user-directed interruption and effects reconciliation. Diagnosis
has ended without a watcher or lifecycle/cluster mutation. Private0700/0600
receipts, exact process/log evidence and sanitized summary remain under
`/tmp/architect0-update5781-diagnosis-8vqmw63t`; original attempt and all inputs
remain untouched. This finding does not assert eventual update success.


### 2026-10-31: end-user KB client examples and supported highlighting

Lead owns the CS/EN rewrite from `kb-restructure/end-user-examples/{cs,en}-before.txt`.
Use one existing-token example per client: literal `TOKEN`, first page of up to10
visible VPSes, ID and hostname output. These are placeholders, not real secrets.
Remove environment-variable setup and OAuth/authentication matrices from these
examples. Retain unversioned install commands and useful client links; no optional
API selector or generated-client implementation explanation. Do not claim these
list all pages. Generated TS alone requires the inspected schema's `/v7.0` base;
Go/Rust embed that prefix, while dynamic clients discover the server default.

Source facts: own HaveAPI7230373933180e0fe2a69623d2290b099018abea,
`clients/php/README.md:59–137`, `src/Client/Resource.php:127`, Python
`clients/python/README.md:25–42,109–128` and `_resources/__init__.py:137–140`;
JS `doc-async-client.md:79–87`, `doc-async-resources.md:3–25`,
`src/haveapi/async/resource_model.ts:11–13,295,442–469`. Dynamic action `value`
is a resource list; `response.data` is the plain payload. The array check below
allows the same JS syntax to remain valid TypeScript without casts/generics.
Generated Go canonical134a9e69 README:18–64 documents the complete request and
both error checks; `client/resource_vps_action_index.go` contains its versioned
path. Retained published SDK0.1.1 README:33–77, `dist/index.js:3–8` and
`dist/generated/resources/vps/actions/index.js:2` prove the adapter, required
base prefix, `index` call and `page.data`. This is the already-inspected SDK
package, not a fresh claim about registry latest. Retained Rust crate0.1.0,
Gitb6f84679d33ff041388535dcf4dc060aeb0d1b9d, README:21–56,106–125 and
`src/generated/resources/vps/{mod.rs:101,index.rs:119–121,198,331}` prove
blocking call, root URL, index/limit and optional output fields; runtime
`client.rs:73,175,265` proves token/build/send. No fetch or execution was needed.

Minimal source-backed sample bodies for lead adaptation follow. Keep each complete
program and its install prerequisite; localize any added prose/comments, not code
identifiers. Rust uses the already documented blocking feature to avoid adding a
Tokio setup example; Option debug output is deliberate, not an assumed always-set
ID/hostname. The generated TS sample is ESM JavaScript-compatible syntax.

```php
<?php
require __DIR__ . '/vendor/autoload.php';

$api = new \HaveAPI\Client('https://api.vpsfree.cz');
$api->authenticate('token', ['token' => 'TOKEN']);
foreach ($api->vps->list(['limit' => 10]) as $vps) {
    echo $vps->id . ': ' . $vps->hostname . PHP_EOL;
}
```

```python
from haveapi_client import Client, TokenAuth

with Client("https://api.vpsfree.cz", auth=TokenAuth("TOKEN")) as api:
    result = api.vps.list(limit=10)
    for vps in result.data:
        print(vps["id"], vps["hostname"])
```

```javascript
import { AsyncClient } from "haveapi-client";

async function main() {
  const api = new AsyncClient("https://api.vpsfree.cz");
  await api.authenticate("token", { token: "TOKEN" });
  const result = await api.resource("vps").action("list")({
    params: { limit: 10 },
  });
  const vpses = result.response.data;
  if (Array.isArray(vpses)) {
    for (const vps of vpses) console.log(vps.id, vps.hostname);
  }
}

main().catch(console.error);
```

```go
package main

import (
    "fmt"
    "log"
    "github.com/vpsfreecz/vpsadmin-go-client/client"
)

func main() {
    api := client.New("https://api.vpsfree.cz")
    api.SetExistingTokenAuth("TOKEN")
    action := api.Vps.Index.Prepare()
    action.NewInput().SetLimit(10)
    response, err := action.Call()
    if err != nil { log.Fatal(err) }
    if !response.Status { log.Fatalf("%s: %v", response.Message, response.Errors) }
    for _, vps := range response.Output {
        fmt.Println(vps.Id, vps.Hostname)
    }
}
```

```javascript
import { AsyncClient } from "haveapi-client";
import { createHaveApiExecutor, createVpsAdminClient } from "vpsadmin-typescript-client";

async function main() {
  const runtime = new AsyncClient("https://api.vpsfree.cz/v7.0");
  await runtime.authenticate("token", { token: "TOKEN" });
  const api = createVpsAdminClient({ execute: createHaveApiExecutor(runtime) });
  const page = await api.vps.index({ params: { limit: 10 } });
  for (const vps of page.data) console.log(vps.id, vps.hostname);
}

main().catch(console.error);
```

```rust
use vpsadmin_client::blocking::Client;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api = Client::builder("https://api.vpsfree.cz")
        .token("TOKEN")
        .build()?;
    let response = api.vps().index().limit(10).send()?;
    for vps in response.output {
        println!("{:?} {:?}", vps.id, vps.hostname);
    }
    Ok(())
}
```

**Highlighting is source-confirmed.** Installed host container declaration
`/etc/nixos-containers/kb-staging.conf` selects systemlg3a8dvm; its nginx unit
selects configzn81lq4a with CS docrootsp7zrg7 and EN8ignwv6. Both are DokuWiki
2026-07-14c "Mort" and bundle GeSHi1.0.9.1
(`vendor/geshi/geshi/src/geshi.php:43`). The language directory has
`javascript.php`, `php.php`, `python.php`, `go.php`, `rust.php`, but no
`typescript.php` or `ts.php`. DokuWiki `inc/parser/xhtml.php:656–711` delegates
code blocks to GeSHi. Use `<code javascript>` for these JS-compatible examples;
keep the client headings accurate. This changes documentation only, not the
highlighter or host. Installed selection/source was read; no staging request,
render, browser or runtime test was performed by the architect.

**Minimal acceptance for the documentation owners:** compare final CS/EN call
bodies for equivalent URL/auth/action/limit/output semantics; preserve page IDs,
translation markers and TOC anchors. Confirm six complete examples, literal TOKEN,
no environment reads or OAuth discussion, no optional version selector, and only
the required generated-TS base prefix. Match the Rust blocking install feature
and Node ESM prerequisite to the samples. Reuse existing snippet/source checks;
if code checking is performed later, use syntax/type checks or fixed offline
fixtures only, never these placeholders against a real API. After the ordinary
final content review and released staging, inspect the existing rendered preview
for supported code classes and highlighting, plus normal links/revision summaries.
No package installation, application change, new client matrix, production write
or highlighter campaign belongs to this brief. Current staged06 snapshots remain
unchanged until lead-owned rewrite and the normal additive release workflow.


### 2026-10-31: acquire tokens in KB examples (successor to staged07)

User now requests username/password token acquisition plus a commented existing-
token alternative. Lead owns bilingual member wording. Preserve staged07 commit
`a1b404fab578b71454f11760e6d0a8097b0e179f`, CS revision1793457686/hashdccf9649…,
EN1793457690/hash3d25d3de… and all review/render receipts. Change only authentication
imports/setup in the seven client examples, including the same Ruby auth replacement
in its two older backup scripts. Keep staged07 listing/output code, backup logic,
install/run prerequisites, links and supported JavaScript code tags unchanged.
The Ruby listing's existing page/list semantics need no incidental change.

All seven support token acquisition; none needs Basic auth substituted. Use literal
USERNAME/PASSWORD, and the commented TOKEN alternative below. An alternative
replaces the whole active acquisition/check block, not an extra call after login;
lead must make that clear with one short localized comment/instruction. Do not print
new tokens. No environment-variable handling, OAuth matrix or client product change.

**Required facts.** HaveAPI token request requires `lifetime`; interval defaults to
300 seconds (`servers/ruby/lib/haveapi/authentication/token/provider.rb:224–233`).
PHP/JS/Go supply `renewable_auto`; Ruby passes its supplied lifetime, Python forwards
request input, and Rust's generated schema marks lifetime required. Supply
`renewable_auto` explicitly only where the client requires it; no optional interval
argument is needed. This is a renewable token, not a permanent credential. Password
login requires token authentication enabled on the account. Minimal examples assume
password completes login; TOTP/password-reset accounts need the supported challenge
continuation or an already acquired token. Never recommend disabling MFA. Ruby/PHP/
JS/Go refuse an unhandled challenge; Python/Rust must check completion explicitly.
A continuation token is not an authenticated API token.

Source basis is retained HaveAPI7230373933180e0fe2a69623d2290b099018abea:
Ruby `clients/ruby/lib/haveapi/client/authentication/token.rb:10–24,77–126` and
`client/client.rb:68`; PHP `clients/php/src/Client/Authentication/Token.php:50–66,
156–170,184–199,226–244`; Python `client.py:75–80,123–149` and
`_auth/__init__.py:101–116` (public exports in `__init__.py`), docs/reference.md:101–119;
JS `src/haveapi/async/authentication.ts:104–141`.
Generated SDK's retained runtime0.30.2 bundle has the same default/token/challenge
flow at `package-0.31/kb/sdk-consumer/node_modules/haveapi-client/dist/haveapi-client.js:3154–3223`.
Go canonical134a9e69 `client/auth_token.go:40–98,101–194` provides
`SetNewTokenAuth`, its options/defaults and the existing-token setter.
Rust retained crate0.1.0/Gitb6f84679 has no one-call login/set-token helper, but has
`src/generated/resources/authentication__token__token/{mod.rs:16–35,request.rs:42–67,
79–116,138–157}`; `Output.token_step()` validates token/completion and returns
`TokenStep::Complete` or a challenge. Runtime `auth.rs:38–52` exports that enum
and `SecretString.expose_secret`; `client.rs:73,175,265` supports a new blocking
client using the obtained token. vpsAdmin33d6 `authentication/token_config.rb:24,
29–75` establishes enable-token-auth and TOTP/reset-password prerequisites.
These are source facts, not newly executed API/client checks.

**Exact changed auth snippets.** Comments below are semantic placeholders for
lead localization. Keep the following existing listing code directly after each
block. Existing-token alternatives replace the indicated login block in full.

Ruby: replace the authentication line in all three occurrences with:

```ruby
api.authenticate(:token, user: 'USERNAME', password: 'PASSWORD', lifetime: 'renewable_auto')
# api.authenticate(:token, token: 'TOKEN')
```

PHP:

```php
$api = new \HaveAPI\Client('https://api.vpsfree.cz');
$api->authenticate('token', ['user' => 'USERNAME', 'password' => 'PASSWORD']);
// $api->authenticate('token', ['token' => 'TOKEN']);
```

Python: replace the import and constructor/auth setup; existing listing remains
inside the same `with` block. The commented setter replaces both login and its
completion check, preserving the constructor/context.

```python
from haveapi_client import Authenticated, Client, TokenAuth

with Client("https://api.vpsfree.cz") as api:
    login = api.begin_token_login({
        "user": "USERNAME",
        "password": "PASSWORD",
        "lifetime": "renewable_auto",
    })
    if not isinstance(login, Authenticated):
        raise RuntimeError("Additional authentication is required")
    # api.set_auth(TokenAuth("TOKEN"))
```

Dynamic JS: inside existing async main, replace only the token call:

```javascript
const api = new AsyncClient("https://api.vpsfree.cz");
await api.authenticate("token", { user: "USERNAME", password: "PASSWORD" });
// await api.authenticate("token", { token: "TOKEN" });
```

Go: keep current imports/main/list call and both existing list error checks.
The alternative replaces the entire `if err := …` block.

```go
api := client.New("https://api.vpsfree.cz")
if err := api.SetNewTokenAuth(&client.TokenAuthOptions{
    User: "USERNAME", Password: "PASSWORD",
}); err != nil {
    log.Fatal(err)
}
// api.SetExistingTokenAuth("TOKEN")
```

Generated vpsAdmin TS: keep the required saved-schema base and adapter setup;
the auth call is the same runtime operation, not a new SDK method:

```javascript
const runtime = new AsyncClient("https://api.vpsfree.cz/v7.0");
await runtime.authenticate("token", { user: "USERNAME", password: "PASSWORD" });
// await runtime.authenticate("token", { token: "TOKEN" });
const api = createVpsAdminClient({ execute: createHaveApiExecutor(runtime) });
```

Rust blocking: add `TokenStep` to the import. Replace the initial client builder
with the acquisition block below; keep existing `fn main() -> Result<…>` and
VPS listing/output/Ok logic. The alternative replaces the whole login/client-
construction block. The `let … else` handles challenge and unknown enum variants
without installing an intermediate token. No invented mutating setter is used.

```rust
use vpsadmin_client::{blocking::Client, TokenStep};

let login = Client::builder("https://api.vpsfree.cz").build()?;
let response = login.authentication__token__token().request()
    .user("USERNAME")
    .password("PASSWORD")
    .lifetime("renewable_auto")
    .send()?;
let TokenStep::Complete { token } = response.output.token_step()? else {
    return Err("Additional authentication is required".into());
};
let api = Client::builder("https://api.vpsfree.cz")
    .token(token.expose_secret())
    .build()?;
// let api = Client::builder("https://api.vpsfree.cz").token("TOKEN").build()?;
```

Minimal doc checks remain scoped to exact staged07-to-successor auth-only changes:
seven patterns/nine occurrences (Ruby3), both username/password and commented
existing-token forms, correct imports/error/completion handling, unchanged list
and backup bodies, localized comments/messages, and unchanged JS highlighting.
Any later authorized syntax/type checks are offline only; do not execute login
or backups. Normal final content review and additive staging preserve07 and
preceding revisions. This architect pass only read retained source and appended
this brief; no fetch/install/build/API/login/staging/browser or product mutation.


### 2026-10-31: consolidate to five active review candidates

This supersedes the eight-candidate presentation in merge-readiness.md. The user
requests consolidation of this session's sibling features into one active review
branch/worktree per repository, refreshed against current upstream. It authorizes
feature preparation, not default integration, deployment, lifecycle or checkout
cleanup. Old published/deployed refs, immutable packages/roots, private files,
source-share paths and original receipts remain recovery evidence. No migration
is introduced by consolidation; preserve upstream migration history without
rewriting it. All owners retain their roster40 Sol/xhigh/workspace_write settings.
Architect source/design inspection is complete; implementers own the operations.

| Owner | Final existing review alias | Inputs and established baseline | Release/dependency |
| --- | --- | --- | --- |
| E0 | vpsfree-dev-workspace-services-os | Fresh master767dfd587e346168e1443e65ccdb67ce748f3fe3; updaterbd66db1e738b0021a2ec55c4bcbf92ad33b8eb30, bootab9346b0c4b942fccd0da6af760401fad3a55bd1, writingd4355518d945ef2e7d5fc2fdb45d6eab8226fa4c | READY for the complete extension package below. |
| E1 | vpsfree-cz-configuration-oauth-clients | Fresh mastere34f08314b6db1ac38facc2386b79111daee864f; old reviewed basefcc7fc97be79df92ed39b4a7bfcc8ba21dc6c627 through60af1a1f0930c731d6f0bbabd0a0cb3ed21b550a | READY; E2 final published75c dependency is satisfied. |
| E2 | vpsadmin-oauth-client-logs | Fresh masterac10a62f1cb0fc890378ae83cdf18dd0e29f049a through75c691b17c48115f929b57ef55f78935be006ea6, four commits | No-op reconciliation accepted by lead: exact source/base unchanged; no rebase/retest/review churn. |
| E1 | workspace-services-os | Publishedf1d53cb659fa914fcfd27a39a53ccecc88439615 based on4737ef1449278f2b8d9b8398178008cfe401fb3c, plus pointereeec0c40d66a6db374dc0e6e60151666d1a9ec49 based on1c7f990d9ccd61c510c22da18f4771cdaaef640b | Preparation independent; final pin waits reviewed/published E0 combined head. Use current shared workspace master as base, preserving its later tracking commits. |
| E3 | vpsadmin-webui-031 (conditional) | Source range9113caa0915b2908373ecd616f8f752e779ed4c9..2e32c814d3af70ac39257f2542075bd580ee38d4; fresh main40653dffed4561dd6086716fd506a7223d3631d7; existing aliasbaf00acc31d34ab37720643c5833b4476a341f3b | Checkout mutation HELD only for exact PID952323 path obligation; see React boundary below. Canonical2e32 remains frozen. |

**E0: extension, released now.** Fresh default remains767, so retain the deployed
linear d632→bd66 prefix in the existing services-os branch. Apply the focused
ab934 boot-proof commit atopbd66, then the disjoint d435 writing-skill commit.
Final expected series is d632/bd66/replayed-boot/replayed-writing: four coherent
behavior commits, no merge commit, obsolete applied-OS-pin approach or repeated
input update. Preserve original authorship and full functional rationale. Retain
exact original refs before any rewrite; a normal append should need no force.
The old boot-proof and writing checkouts become recovery-only, not cleanup targets.

Owning union is the existing seven updater paths (provider README, bin/devcluster,
flake.nix, lib/maintenance.rb, command/maintenance/Nix-smoke tests) plus
skills/vpsfree-user-facing-writing/SKILL.md. The boot helper hunks are disjoint
from the updater: retain ssh -n only for the noninteractive selection proof,
checked full-machine array/set enumeration, exact once-per-configured-guest
coverage, and finish-boot only after every proof succeeds. Missing/duplicate/
failed enumeration and middle proof failure must leave boot pending. Interactive
SSH and streaming behavior stay unchanged.

Retain bd66's ordinary creation/update source selector, target-scoped validated
context, same-target pending retry, strict topology/layout refusal, old boot
host tools and OS share, requested-target-only payload changes, and exact
unselected peers. Retain automatic absent-config-export suppression ONLY when
validated retained descriptors all lack it; fresh creation detects it normally,
existing/mixed/removal/retargeted exports remain under exact guards. No schema,
private helper, public flag, OS export transition or live certificate repair.
The writing change remains the exact ten-line policy addition, without merging
workspace prose into the extension.

Reconcile shared command-test stubs by preserving BOTH sets of event/argument
handling, especially maintenance build-context and applied-finish-boot, jq
machine enumeration, guest proof events and stdin-drain instrumentation. Do not
replace one branch's fixture with the other or weaken assertions. Quick checks:
focused existing boot-proof/updater interaction command cases, the maintenance
Ruby suite, writing-skill checks used by the original d435 packet, shell/Ruby
syntax and owning hooks. Prove boot coverage
failure cases still run alongside services/all/retained-boot projection,
partial-target proof, pending retry, absent-config-export and strict-refusal
cases. A focused interaction case is warranted only if existing cases do not
exercise retained boot context followed by full guest proof. Keep config-export
assertions wired into the actual packaged checker, not merely projection-only.
After commit/quick, obtain final affected HIGH review including combined history;
then run the full command suite once through the normal full flake check,
followed by the full normal installed devcluster-check. These checks
use disposable fixtures and build/load runners; no live guests or new migration
VM. Prior separate branch passes are context, not proof of this combined tree.

**E1: configuration, released now.** Own baseline/input receipts prove e34,
60af and frozen249f. Rebase/reconstruct only the four logical FCC..60af changes
onto fresh e34, preserving upstream6f54 devWorkspace and every unrelated input.
Keep API/auth/docs configuration and operator guide, PHP-only frontend/backend/
HAProxy policy, native syslog destination and literal dev Basic-auth merge.
Canceled KB/Discourse sources must remain absent. Do not restore the old4155
runtime lock or reintroduce249f's obsolete33d6 services pin.

The services input remains exact E2 published75c. If the lock must be generated,
use existing `confctl inputs channel set --commit vpsadmin vpsadmin 75c691b17c48115f929b57ef55f78935be006ea6`;
retain its generated message and one final services update in the branch. Never
hand-edit the lock or change unrelated channels. Input semantic-path comparison
must distinguish fresh upstream changes from this feature's sole services pin.
Keep frozen canonical configuration249f, both registered paths, ignored/private
state and recovery refs intact; no current exported path is moved or removed.
Quick: declared hooks/Nix formatting/parsing, existing bounded nginx fixture,
source/guide/pin/cancellation preservation. Review the final range and real
conflict resolutions before longer work. Required final verification is the
existing affected proxy+webui1+webui2+webui-dev build/generated/syntax boundary;
reuse prior results only where exact derivation/input identities prove scope.
Installed P0 transport may reuse the recorded five-case pass only with equal
actual binary/ini/pool/page/vendor inputs; otherwise repeat that bounded check.
No real login, production access, canceled component build or deployment.

**E2 and React.** E2's fresh default/feature proof leaves75c unchanged and already
cumulative of33d6 and a089; bind its existing final review/check/publication and
hand the exact head to E1. Preserve canonical live33d6 and all recovery aliases.

For E3, retain canonical vpsadmin-webui2e32/inode51692404 as lead directs. Use
existing vpsadmin-webui-031 only after the exact952323 Bash cwd reference is
classified by E3/lead. Its structured safe-alias proof currently says false;
the earlier no-process prose is superseded. A proved idle owned shell with no
children, open target file or operation can be classified as incidental cwd
without stopping it; an active writer/consumer or unresolved owner blocks
mutation of that path. Do not infer permission to signal it. Preserve oldbaf
ref and the19972 private/ignored entries; no rename/deletion/private replacement.
Lead owns any necessary supported registration change. If this exact obligation
cannot be resolved, report it; do not invent an unregistered checkout.

Once path use is settled, replay only the two reviewed911..2e32 commits onto
fresh main40653, retaining upstream behavior and authorship. Preserve production
HaveAPI adapter/error/mutation no-replay/uncertain-result protections and exact
released dependency intent, without downgrading newer upstream dependencies or
copying historical docs over newer content. Material semantic conflicts go to
lead; ordinary textual reconciliation is implementation work. Preserve PR74
alias5dd, PR63 and old live refs; this task does not authorize rewriting that
separately protected published PR range. Publish the consolidated owned feature
normally; any PR74 disposition must be explicit, not an accidental force push.
Quick: normal ci:quick/typecheck, focused existing actual-library adapter/auth/
mutation tests, source/provenance guard and affected docs audits. After final
review, normal unit/build and affected frontend/BFF/provenance/source/package
Nix outputs; repeat browser/BFF checks only for affected behavior or unresolved
prior gates, retaining their original limits. No live login/deployment campaign.

**E1: workspace dependent package.** Reuse workspace-services-os; old workspace
pointer checkout becomes recovery-only. Fresh remote019ea536593cbf27abde9ec157a24ce126fbb655
has the same bounded composition as4737; its alias clone lacks a fetch refspec,
so localmaster9e is not a fresh target. Base final feature on the current shared
workspace master (latest retained5b894bd6fcaef2ff4a0aa743afba3e5f840c289a), which
preserves later own KB/tracking commits and contains fresh remote019. Do not
reset shared master or replay unrelated tracking as feature commits.

Carry eeec's two procedure pointers once, the independent f1d instruction-budget/
UTF-8 repair once if not already present by exact/equivalent upstream proof, and
ONE extension pin selecting E0's final reviewed/published combined SHA. Regenerate
flake.lock with `nix flake update vpsfree-dev-workspace` after changing its exact
URL; do not invoke the generic-runtime refresh recipe. Preserve explicit nested
generic6f54, codexd3a, site/team/coordination/integration/cluster contracts and
all unrelated semantic inputs/follows. If fresh composition moved again, report
that exact compatibility boundary; no implicit downgrade/adoption. Keep existing
16384-byte budget, assertions, approval rules and saved team settings. No new
policy edits. Final feature has logical pointer, repair (if needed), and one pin
commits, with oldf1d/eeec/deployedbd66 refs and package roots preserved.

Quick checks cover existing instruction/deployment-contract tests, pointer
resolution, byte budget/UTF-8 and hooks. Final review/equivalence must bind both
old reviewed ranges, final full series, new extension and every substantive
resolution. After review, normal workspace flake check/default package build and
source deployment checker against the exact fresh matching configuration source
contract. That checker is source compatibility evidence, not deployed host Git
proof. Bind actual packaged extension/helper/skill and unchanged generic/runtime
contracts. Do not repeat E0's suite, build cluster kernels, prepare/switch profile
or alter host configuration under this consolidation assignment.

**Common completion/reuse boundary.** Inventory each fresh default-to-final series,
full diff and original-to-successor mapping. No feature merge commits or obsolete
pin streams; retain functional commits and deployed behavior with exact recovery
refs. “NO MIGRATIONS” applies to owned delta, not an assertion that upstream has
none. Review reuse follows mandatory-change-review: certified reconstruction can
cover a mechanical refresh, but substantive baseline/conflict/combined behavior
requires affected independent review after commit/quick and before long checks.
Never relabel old source/output/live proofs as a new head. Use normal declared
shells/hooks; no inherited one-job/two-core limit merely from earlier diagnostics.
Lead schedules appropriate verification watchers/resource admission. Preserve
failed evidence, currently selected profile218 and live services/private state.

Final handoff is five clean published review candidates, one designated alias
per repository, exact fresh bases/heads, complete history/migration conclusions,
check/equivalence scope and dependent pins. Extension precedes workspace, and
vpsAdmin precedes configuration; React is independent after its path disposition.
No new user gate is needed for these feature preparations. Default merges,
production/profile deployment and physical recovery-worktree cleanup remain
separate from this package. Lead owns state, final prose/review scheduling and
registration disposition; architect changed only this design appendix.


**React path/dependency clarification, accepted E3 exact evidence.** E3's corrected
safe-alias-shell-reference.json identifies952323 as sleeping Bash under tmux2451,
PTY323, with no children and no direct source argv. Together with the structured
absence of applied exports/optional selector/config references, this is an
incidental cwd/path-presence obligation, not an active build or served consumer.
Preserve its directory inode/path/terminal; do not signal the shell. E3 may now
perform the described tracked-source consolidation in vpsadmin-webui-031, while
canonical2e32 and its path remain frozen. Preserve the oldbaf commit under an
explicit recovery ref before any branch rewrite and retain the exact private
inventory; no whole-directory reset/clean/stash or overwrite of ignored files.

Normal npm ci must NOT replace the retained alias node_modules/private contents.
Use an owned disposable Gitless export of the exact candidate tracked tree for
normal dependency installation and verification, with exact tree/modes/links and
locks recorded. This is a test-source copy, not another review branch/worktree;
exclude all credentials/private files and keep original copies untouched. Use
the repository's normal Nix/source-provenance inputs, never fabricate a clean
Git identity. Ordinary hooks remain enabled; run required hook tools through
the declared environment without bypass or copying test artifacts into the
retained checkout. Bound results to the exact committed source and installed
lock/input identities; no live source retargeting follows from tests.

PR74 at5dd remains protected historical publication, separate from the new
current-main candidate. Prepare the final review branch in the reused alias,
retain original author/history mapping, and report the concrete normal
publication/registration mapping to lead before any protected PR rewrite. This
is not a reason to hold local consolidation/checks or to create a duplicate PR.
Lead owns that publication disposition; no blanket force push/default/merge
authority is inferred.

## Finish plan: workspace first, product defaults and React 0.32 (2026-10-31)

This supersedes final-readiness claims for product75c, configuration4ea and
React02e under the user's corrected requirements. It is a plan, not release of
new source work. Lead holds those three packages until plan review/direction.
The already-authorized E0 tooling checks and dependent E1 workspace package
continue. [Compact ordered plan](finish-plan.md) is the lead's user-review handoff.

### Five packages and order

| Order / owner | Existing active review alias → integration target | Remaining result |
| --- | --- | --- |
| 1 / E0 | `vpsfree-dev-workspace-services-os` → `vpsfreecz/dev-workspace:master` | Finish existing full flake, full installed checker and publication of reviewed `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae` (or properly reviewed successor). Preserve literal deployed bd66 prefix, boot-proof and writing union. No new security work is added to this running package. |
| 2 / E1 | `workspace-services-os` → `aither64/vpsfree-cz-workspace:master` | Finish one final published E0 pin atop existing pointer/repair head `551c2870ecd3f225403c10e45c1332301c6a8127`; preserve shared-master tracking and selected generic6f54/codexd3a composition. Complete review/check/package binding, then integrate after extension. |
| 3 / E2 | `vpsadmin-oauth-client-logs` → `vpsfreecz/vpsadmin:master` | Extend current `75c691b17c48115f929b57ef55f78935be006ea6` with product-owned secure nginx/FPM/HAProxy defaults and their tests/docs. Preserve released HaveAPI0.32 and PHP callback containment. |
| 4 / E1 | `vpsfree-cz-configuration-oauth-clients` → `vpsfreecz/vpsfree-cz-configuration:master` | Replace site copies with product defaults and one final generated product pin, starting from `4eaed0ea87cb14411d84630237af2473c87d92e9`. Depends on E2 final published source. Keep topology/operator settings and unrelated upstream inputs. |
| 3, independent of E2 / E3 | `vpsadmin-webui-031` → `vpsfreecz/vpsadmin-webui:main` | Adopt actual published JS HaveAPI0.32.0 from current `02e58932cef3b667ff68401ff93e4e43bc2a3ce5`, retaining the production adapter and current upstream behavior. |

Only the two workspace default integrations have the user's named direction.
After their checks/review, integrate extension first and workspace second, then
deploy/verify the final workspace profile and release aitherdev as below.
Application corrections follow; their default merges and production deployments
remain separate decisions. There is one active review alias per repository;
historical refs/checkouts/private paths remain recovery material, not extra
merge steps or cleanup targets.

### Exact aitherdev release dependency

Selected `workspace-host coordination guide` identifies package
`/nix/store/413w4bai6br4c2vq08gx9diq55iasvqk-dev-workspace-0.2.0`, catalog
`sha256:ede4b6852f771c40e32a7f13d95c2d851486a2b3fbdb2835a1157b1c55a2b09f`.
Its machine-retention rule requires verified effects plus complete integrated
deployed lineage; a substantive nonancestor successor needs a new verified
deployment. It does not permit calling a superset patch-equivalent.

[Profile218 receipt](updater-services-os/consumer/config-export/activation/receipt.json)
binds consumer `f1d53cb659fa914fcfd27a39a53ccecc88439615`, provider
`bd66db1e738b0021a2ec55c4bcbf92ad33b8eb30`, the413w package, completed switch88943,
verified application health and exact claim
`d0061f09-dbfd-4531-b10f-862e7354a78f`. Its recorded request covers
`machine:vpsfree:aitherdev`, specifically workspace application activation.
[Complete input binding](updater-services-os/consumer/config-export/verification/attempt-1/source-input-binding.json)
identifies workspace source `/nix/store/2iiw1d4yypnq0phqqhjbr074wb5b0z03-source`,
121 semantic input paths and unchanged generic
`6f54d0c7fdb974705c120b3c1ef5372f5897d544` / codex-web
`d3a29bee90ef00a08816920408c596152339a637`.

E0's final reviewed series literally contains bd66. The refreshed workspace
consumer does not literally contain f1d; its final provider pin adds boot-proof
behavior and writing policy. The instruction repair's proven replay is not
whole-consumer equivalence. Therefore the minimal valid path is integration of
both final workspace heads, ordinary final-package prepare/switch under the
existing held machine claim, and new verification of that exact profile's
application health, contracts and preserved session/cluster state. Keep413w and
all prior source/input/recovery receipts; recovery remains the supported forward
package procedure, not an assumed old-profile rollback.

The recorded profile graph uses existing published product defaults (including
devcluster-vpsadmin5c76 and devcluster-webui534c), not the pending75c/4ea/02e
application candidates. The separately selected guest sources and simulated
guest operations do not turn those candidates into dependencies of this
physical-host application reservation. No recorded host-system/config rollout
under this claim requires application integration before workspace release.
This does not certify application features as merged or erase guest obligations.

At execution, retain the exact final source/input graph and reviewed old/new
history mapping; prove fresh remote-default ancestry for all deployed feature
dependencies. Use one short repository merge claim at a time; shared workspace
integration also takes the nonwaiting tracking lock. Reconcile all original
operations, inspect authoritative status for this exact machine claim, verify
the final deployment and integrated lineage, then release and verify released
state. No separate UI-acceptance wait follows satisfied policy. A later deployment
needs fresh machine ownership. None of this authorizes session cleanup, stop,
archive, guest changes or a host-system rollout.

### Secure defaults: ownership, compatibility and package boundary

The user's objection is supported by source. At75c, product
`nixos/modules/vpsadmin/frontend.nix` emits ordinary access logs, `webui.nix`
sets FPM `error_log` to `stderr`, and `haproxy.nix` defaults `logRequests` true.
The site branch supplies query-free nginx logs, scoped request-error suppression,
Referrer-Policy, syslog and HAProxy logging overrides in
`configs/nginx/oauth-client-logs.nix` and `common/{frontend,webui}.nix`.
History packaged this as site deployment preparation and then PHP protection;
it supplies no evidence that site-only ownership was a deliberate product
requirement. The earlier boundary was incomplete for ordinary deployments.

E2 owns reusable policy in those existing product modules: query/header-free
access records retaining method/path/status/timings; suppression of raw request
errors only on sensitive API/auth/PHP virtual hosts; PHP Referrer-Policy;
working native FPM syslog with existing fixed application diagnostics; and
safe API/PHP HAProxy request-log defaults using the existing `logRequests`
option. Keep console and unrelated nginx hosts unchanged. Move the existing
API/auth edge header normalization into the owning frontend where appropriate;
an upstream trusted proxy remains an explicit topology choice. Preserve auth,
sessions, OAuth callback containment, maintenance, allowed PHP entrypoints and
Basic-auth behavior. No database/protocol migration or broad logging framework.

TLS is a necessary acceptance boundary, not a reason to delay this plan:
selected nixpkgs nginx `default.nix:460–471` generates a forceSSL redirect server
without the vhost's extraConfig (`:509`). Merely adding protected TLS-vhost logs
would leave HTTP callbacks exposed. Move the existing protected explicit
redirect composition into the product owner, covering HTTP, HTTPS, HTTP→HTTPS,
aliases/listeners, ACME challenges, redirect code and exact wire query, addSSL,
maintenance and additive Basic auth. The exact Nix expression / any narrowly
necessary product TLS option remains a bounded E2 design detail before edits;
do not silently discard existing per-vhost overrides, cause recursive option
evaluation, globally suppress unrelated nginx diagnostics, or claim success
while the generated redirect is unprotected. Route a real compatibility change
to lead rather than expanding this into a proxy framework.

E1 then deletes redundant site log/header/FPM/HAProxy overrides and explicit
redirect implementations after their replacement is verified. Retain concrete
domains/certificates/listeners/backends/firewall, direct HAProxy routing around
Varnish, private credentials/docs-client setup, trusted origins and additive dev
Basic auth. Site docs describe deployment/topology and link the product contract.
Do not delete a protection before the final product pin provides it. Generate
that sole pin with the existing confctl channel, preserving unrelated inputs.

Product `tests/configs/nixos/vpsadmin-services.nix` must exercise the defaults,
not mask them with duplicate log overrides. Reuse/adapt the existing nginx/PHP
fixtures rather than add a harness. Explicit Varnish/custom-proxy routing remains
an operator boundary: product nginx cannot redact an intermediary's journal.
The dev provider's temporary API hostname explicitly routes through Varnish
(`dev-clusters/vpsadmin/nix/test.nix:1544`); this plan does not relabel that route
as protected or change the already-running tooling package. Any later dev privacy
acceptance must account for its exact topology. Pre-vhost parser errors and
uncontrolled external proxies are also outside a per-vhost guarantee.

Quick checks cover module formatting/hooks, plain/default and TLS generated
config fixtures, all owned PHP/backend/edge/redirect cases, absence of synthetic
code/state/token/header sentinels from native logs, useful safe diagnostics and
unchanged redirect/auth results. Commit, then affected independent review of the
whole final branch/history; afterward run the owning bounded service/PHP tests
and the site's four affected proxy/webui builds/generated syntax checks. Reuse
only exact unaffected derivation/input proofs. No real login or production test
is implied. A later authorized rollout protects edge before backend; rollback
must retain protective configuration rather than revert to raw logging.

### React: released JavaScript 0.32.0, not a Ruby-version inference

The prior dependency commit intentionally adopted0.31.2. The subsequent0.32
scope explicitly held React unchanged (release brief above, around4358); current
main consolidation replayed that dependency unchanged. No source evidence shows
a technical requirement to remain on0.31.2. Published npm0.32.0 is already proven:
`https://registry.npmjs.org/haveapi-client/-/haveapi-client-0.32.0.tgz`, retained
archive SHA256 `144cf17ada3b4578c8a3d81c87d183c94bd72d98e83934475c019b8bfd8b2efc`,
matching registry integrity, release tag peeled to
`0e7166a0f8f15827bfac051666a53bf449e999ec`. This is JavaScript artifact evidence,
independent of RubyGems. Its built dist is not identical to checked-in tag dist.

E3 changes exact root package/version and lock resolution/integrity,
`packages/haveapi-client-provenance.json`, and the normally computed
`packages/frontend.nix` npmDepsHash; update owning dependency docs/work log and
source checks where version-bound. Preserve xmlhttprequest1.8.0 and all unrelated
lock entries. Inspect the published RequestSpec/AsyncClient/AsyncError surfaces
used by `src/lib/api/haveapiRequestClient.ts`; retain the adapter unless actual
0.32 package compatibility requires a small change. Formatting/release-only
authored-source history is not runtime equivalence proof. Bind provenance to
the actual archive/release source; parsed attestation metadata alone is not
signature verification. No SDK/client-generator or unrelated dependency upgrade.

Quick: source/provenance guard, typecheck and existing actual-library adapter,
auth, timeout/abort, error/result and mutation-no-replay tests. Commit and obtain
affected final review; then normal unit/build and affected frontend/BFF/source/
package/provenance Nix checks once. Preserve existing private node_modules by
using the approved exact tracked-source test export. Consolidate0.31.2→0.32 into
one final dependency stream, keep adapter authorship and recovery refs, and
preserve protected PR74/63. Product33d6's API protocol is unchanged by this npm
adoption; compatibility still needs the actual-package checks above.

### Review and authorization boundary

Lead presents this plan now. New E2/E1-security/E3 source work waits plan
direction; their earlier passes remain evidence only for old source/scope.
Existing E0/E1-workspace checks are not restarted or blocked by this planning.
Each final branch needs clean published head, whole-history/migration conclusion,
quick→affected-review→required-final-check sequence and fresh target proof before
integration. Application targets remain awaiting explicit integration direction.
Keep canonical live33d6/config249f/React2e32 and all source/export/private paths,
deployed roots and failure receipts intact. No KB/Discourse work, new audit,
profile action, merge, PR rewrite or lifecycle operation was performed here.

## Product nginx implementation boundary (2026-10-31)

User has directed implementation of the finish plan. Workspace integrations,
final profile verification and aitherdev release retain first integration
priority. E2 owns product code/tests/technical docs; E1 owns the dependent site
simplification and final product pin. E3's npm0.32 package is independent.
This section settles the normal TLS composition; it adds no public TLS option.

**Composition.** Use one small product-private module shared by frontend and
PHP backend (for example `nixos/modules/vpsadmin/nginx-privacy.nix`, imported
once through the normal module list). Add an `apply` function to the existing
`services.nginx.virtualHosts` option. Selected nixpkgs declares this option at
`nginx/default.nix:1280` without its own apply function. The function receives
the fully merged/defaulted host values, so it can see a user's per-host
forceSSL override without recursively reading the value it changes.

Select only enabled product frontend API/auth/PHP host names and the enabled
PHP backend domain. Other hosts, console/download frontends and all host keys
stay untouched. For a selected host whose merged `forceSSL` is true, preserve
its record and explicit listen list, replace only `forceSSL = false` and
`addSSL = true`, and prepend the HTTP-only redirect below to its protected
`extraConfig`. Reject the originally invalid combinations with addSSL,
onlySSL or rejectSSL before transforming them; do not hide existing nginx
validation errors. Hosts with forceSSL false retain their existing HTTP,
addSSL, onlySSL or rejectSSL behavior and receive no redirect transformation.

The intended nginx expression is a server-rewrite return, before custom server
rewrite text and before location/auth processing:

```nginx
set $vpsadmin_redirect_scheme $scheme;
# Emit this exemption only when nginx emits its HTTP ACME challenge location.
if ($uri ~ ^/\.well-known/acme-challenge/) {
    set $vpsadmin_redirect_scheme "";
}
if ($vpsadmin_redirect_scheme = http) {
    return REDIRECT_CODE https://$host$request_uri;
}
```

Substitute the existing merged numeric redirectCode, not a fixed301. The ACME
condition must match the selected nginx generator exactly: enableACME or
useACMEHost, with the selected certificate's dnsProvider null. Resolve the
certificate name from useACMEHost, otherwise serverName, otherwise the original
host key. Preserve the ordinary generated ACME location, acmeRoot/fallback,
certificate ownership and challenge auth exemption; do not duplicate them or
create another certificate. Without that location, omit the exemption. Use the
normalized URI for this prefix comparison, and the untouched request_uri for
the redirect destination. The rewrite contains only set/return, not proxy or
location reconstruction.

For normal dual-listener forceSSL hosts this keeps the same host key, aliases,
listener order/default-server identity, certificate settings and service
locations. HTTP returns before Basic auth or maintenance; HTTPS reaches the
original auth/maintenance/service configuration. Existing global frontend
forceSSL and direct per-vhost overrides both continue to select this behavior.
The effective generated record uses addSSL plus the protected redirect instead
of nginx's implicit unprotected server; document that representation change.
No synthetic host names, host relocation, global error-log suppression,
nixpkgs-module replacement, new public flags or generic proxy abstraction.

**Compatibility limits must be explicit.** Literal listen entries, including
one-sided lists, are retained and remain accepted. The old generator split
forceSSL's effective listeners into two servers; an empty half could cause
nginx to add an implicit default listener. The single-host form does not add
that accidental listener. This edge difference must be recorded and exercised,
not described as complete byte/behavior equivalence or hidden by refusing the
typed listen option. The inspected current site uses ordinary dual defaults /
listenAddresses, while dev uses addSSL without forceSSL; neither requires that
fallback. If a real owned consumer depends on the implicit empty-half listener,
route that concrete dependency to lead before changing its behavior.

Raw custom server-level rewrite directives can affect an exempt HTTP ACME
request in a shared server, and custom response headers can also apply to HTTP
redirects. This is a limit of arbitrary imperative nginx text, distinct from
the documented typed SSL/listener/ACME/auth options. Do not build a parser or
silently rewrite/reject such text. The current owning product/site policy has
no such server-level routing requirement. Cover the actual snippets in the
fixture; report a concrete conflicting custom snippet rather than expanding
the implementation. Explicit user overrides that re-enable sensitive logging
remain operator policy, not a secure-default guarantee.

**E2 file/test boundary.** Keep the finish-plan controls in frontend.nix,
webui.nix and haproxy.nix, with only the shared private module and its normal
module-list entry added for this composition. Keep per-product access files
and useful query-free method/path/status/timing fields, scoped request-error
suppression, fixed PHP diagnostics/native syslog, Referrer-Policy and safe
API/PHP HAProxy defaults. Preserve existing application75c code and dependencies.
Remove masking log overrides from tests/configs/nixos/vpsadmin-services.nix so
ordinary default-module evaluation is the subject of the tests.

Place the reused standalone nginx fixture and a small module-generated config
fixture under `tests/oauth-client-log-protection/`; adapt the site's existing
seven-case fixture instead of adding a harness. Test generated product config,
not a handwritten approximation of the proposed rewrite. Preserve/adapt the
existing installed PHP/P0 fixture at its owning boundary. Document the reusable
contract in product docs and link it from docs/README.md; lead owns final prose.

Quick checks before commit/review: hooks/format and focused config evaluation;
no TLS, addSSL, onlySSL, per-host forceSSL overriding the global setting, and
forceSSL with default/custom/explicit IPv4+IPv6 listeners and nondefault ports.
Include one-sided explicit lists with the documented fallback difference,
invalid SSL-mode combinations, aliases/default host identity, static certs,
ACME own/shared certs and DNS/HTTP challenge modes. Native nginx fixture must
prove exact redirect code/encoded query, ACME precedence, Basic-auth HTTPS
challenge, maintenance behavior, safe access diagnostics, synthetic secret
absence from access/error logs, and an unrelated host left unchanged. Verify
PHP standalone backend and API/auth/PHP frontends, not only the site instance.

After committed quick-pass source, affected independent review covers the
complete final history, TLS representation and limits. Then run the existing
bounded native PHP/P0 and affected services tests plus final package checks.
Do not repeat the old broad HaveAPI campaign. Long VM checks use the normal
watcher and unexpected-kernel rule. Prior results may be reused only for exact
unaffected source/input/derivation scope. No real login/deployment is implied.

**E1 consumption.** After E2's reviewed/published final source, remove the site
nginx logging fragment and duplicate PHP/API/auth explicit redirect machinery,
log-format/header/FPM and HAProxy-default overrides. Keep the original product
frontend.forceSSL setting and all domain/alias/listener/certificate/ACME choices;
keep additive dev basicAuthFile, topology/direct-HAProxy route, private inputs
and trusted-origin settings. Retain genuinely site-owned edge trust decisions.
Generate one final vpsadmin channel pin normally. Quick generated-config and
native fixture comparison must bind actual site behavior to the product cases;
then affected review and the existing four-target build/generated/syntax scope.
Do not remove protection with an old product pin. Old4ea/75c refs and frozen
live33d6/config249f remain intact; no production deployment/default merge follows
from this source assignment.

## Site publication refresh onto 2e1d9e95 (2026-10-31)

**Disposition: preserve upstream c218 and mechanically refresh the same site
candidate; no workspace upgrade or deployment is required.** The completed
workspace integrations/deployment and aitherdev release at18:26:52 stay closed.
This is E1 source/verification/publication preparation in the existing
`vpsfree-cz-configuration-oauth-clients` alias, after lead release; A0 made no
Git/source/runtime mutation. Exact session/absent environment pair and saved
roster40 Astra/xhigh/workspace_write were revalidated.

[Publication guard](product-secure-defaults/site/postreview/publication-master-drift.json)
proved canonical master advanced solely from
`e34f08314b6db1ac38facc2386b79111daee864f` to
`2e1d9e957a5c11fda47bdea8f12dffbafa8064ee`: only devWorkspace's locked revision,
NAR and time changed, from6f54 to
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. Original57755 stopped before any
push; clean final `196174e3866c8acd2bf1df0eaad1be119afb6351`, remote4ea and all
old refs/evidence remain valid for their recorded scope.

Canonical immutable runtime history has one6f54..c218 commit, “codex: retire
redundant generation roots through coordination collection”. It changes three
libexec files to stop adding redundant historical Codex roots and handle those
roots in ordinary collection, plus docs/tests (10 paths, +290/-36). This is
substantive runtime behavior, not metadata-only runtime equivalence. However,
flake/lock, Nix host module and package definitions are unchanged. No assessment
of another session or execution of this behavior is part of this disposition.

Canonical configuration consumption is narrow: flake.nix maps the dev-workspace
channel to devWorkspace; only `cluster/cz.vpsfree/machines/aitherdev/module.nix`
selects that channel, and its config.nix imports the host module/Codex package.
The four owned targets—proxy, webui1, webui2 and webui-dev—select nixos-stable,
os-staging and vpsadmin, not dev-workspace. Their service configuration/product
inputs are unchanged by this upstream commit. Whole system identities can still
change with source provenance: the retained proxy derivation graph contains
`etc-confctl-configuration-info.json` referring to196. Do not infer whole-output
equality from the unchanged site policy or from this static dependency finding.

**E1 implementation.** Preserve196 under a recovery ref, then replay exactly the
three e34..196 logical commits onto2e1: generated45cb services pin821f04ad, product
policy consumption15e40e85 and operator docs196174e3. Preserve authorship/messages,
the accepted SITE-R1 deletion, frozen249f and all4ea/60af/b56/private/live paths.
No new behavior, intermediate product pin, migration or merge commit. Keep the
entire fresh upstream devWorkspace locked node byte-exact and all other lock
nodes unchanged except the existing owned vpsadminServices45cb delta. Normal Git
replay of the generated pin is sufficient when clean. If lock conflict requires
regeneration, use the existing `confctl inputs channel set --commit vpsadmin
vpsadmin 45cb49e2ef5e9f570d8cc7d7629d014345fea223` workflow and retain one logical
generated pin commit; never hand-edit/downgrade devWorkspace or update its channel.

**Review/equivalence.** Before longer checks, bind e34..196 and2e1..newfinal with
ordered stable patch IDs/range-diff, complete series/diff and NO MIGRATIONS.
Independently reconstruct all non-lock entries/modes and the expected entire
lock (old reviewed final plus exactly upstream's devWorkspace change). Normal
hooks/format/whitespace and this bounded preservation proof are the affected
quick checks. Lead may certify mechanical review reuse from accepted immutable
b56 all4/HIGH plus exact SITE-R1 step9 only after this proof. Source conflicts,
additional semantic deltas or a changed consumed module require affected review;
the upstream runtime commit itself is not to be re-audited by this site package.

**Verification comparison, then only necessary realization.** E1 compares the
new four-target derivations and complete relevant input edges to
[the checked196 receipt](product-secure-defaults/site/postreview/checked-receipt.md),
`generated-package-binding.json` and the four retained input graphs. Record the
new source/head/lock and actual target outputs without relabeling old results.
If a complete target drv/output/input identity is equal and its retained output
is available, its existing build result may be reused. If only configuration
revision/input-description metadata and dependent etc/system wrappers changed,
show that bounded changed derivation frontier and realize the changed final
target roots through the normal affected confctl build; do not rerun unrelated
runtime suites. A changed root alone does not invalidate unchanged service tests.

Reuse native syntax only with equal actual nginx/HAProxy binary derivations,
generated configuration bytes/paths and fixture inputs. Reuse the site PHP
five-case proof only with equal PHP/FPM/nginx binaries, effective ini/pool,
installed45cb page+vendor inputs and exact fixture/adaptations; use
`actual-P0-inputs.json`, php-attempt-1 receipts and generated binding.
Production identity does not certify the mutable dev application or a live login.
If any of these inputs changes, repeat only its affected syntax/PHP check and
review any real configuration behavior change. No blanket four-host service
retest, product CI wait, kernel build, aitherdev build or generic-runtime suite.

After accepted review/equivalence and required final artifact checks, normal
feature publication may proceed with a fresh canonical target/own-ref guard,
preserved recovery refs, exact lease where already required, and remote readback.
Another target move returns to its actual bounded delta; do not publish stale
or silently restore6f54. No default merge or machine claim is needed for feature
publication. The workspace/config runtime-match checker concerns a later
workspace/host deployment, not these four site targets: do not fix the new
source pin by changing installed composition, reacquiring aitherdev or reopening
its completed release. Application integration/deployment authority is unchanged.

## Preserve Varnish caching: corrected requirement (2026-10-31)

User explicitly wants Varnish kept in its original position and excludes its
shared-memory logging from this task. This supersedes DEV-R1's bypass, the
four-route site bypass and the corresponding mandatory-bypass prose. HaveAPI
and OAuth do not require cache removal. The bypass was our privacy design
choice; previous acceptance does not establish the user's intended cache policy.

**Evidence and impact.** Product45cb's unchanged varnish.nix:87–103 returns pass
for non-`^/metrics\?` requests on its configured API hosts and assigns matching
metrics responses a60-second TTL. Builtin Varnish policy still excludes cookies,
Authorization, unsuitable methods/responses and keys by host plus full URL.
This is a real metrics cache, not proof that all traffic was uncached; unmatched
hosts/aliases fall through builtin policy. Bypass loses cache reuse/backend-load
reduction, cached response age and Varnish diagnostics; no workload measurement
quantifies that cost. API metrics itself authenticates `access_token` from query
(`api/lib/vpsadmin/api.rb:62–67`). Do not strip that query or alter the cache key.

Final site6d frontend.nix:218/225/234/241 changed API/API-admin/auth/auth-admin
backends to HAProxy; its Varnish service remains enabled at180–197. Product test
API route changed at tests/configs/nixos/vpsadmin-services.nix:614–620; auth.test
already used HAProxy and must remain so. The extension's temporary API route
already uses Varnish; no extension/workspace change is needed.

VSL is a FIFO shared-memory buffer, not automatically a persistent access log.
Selected Varnish8.0.2's manual describes `-n` as its shared-memory/runtime directory
and `vsl_space` as the VSM FIFO. Exact built proxy unit selects
`-n /var/run/varnishd -F`, `RuntimeDirectory=varnishd`, without a request collector.
Its generated tmpfiles var.conf:12 declares `/var/run -> ../run`; normal NixOS
`/run` is runtime tmpfs. This is source/config evidence, not a live mount audit.
No varnishlog/varnishncsa collector is declared in canonical config6d or the
selected nixpkgs service; the exporter reads varnishstat counters. Foreground
daemon diagnostics may reach the journal, but VSL URL/header records are not
automatically copied there. Persistent sensitive Varnish request logs have NOT
been established. Ordinary diagnostics are not a claim that every possible
error is secret-free. No live/private log hunt is required by the clarified scope.

Varnish supports daemon `vsl_mask` through services.varnish.extraCommandLine;
consumer-side filters alone would not prevent VSL creation. That is an available
alternative if an operator later requires it, with loss of request diagnostics,
not work to implement here. Metrics-only routing would also add unnecessary
classification and would still carry the metrics query token. Restore the
original route instead, preserving all existing persistent-log protections.

### E2: product correction and one focused cache proof

Own existing vpsadmin-oauth-client-logs. In
`tests/configs/nixos/vpsadmin-services.nix`, restore only api.test's original
`unix:/run/varnish/vpsadmin-varnish.sock` backend and remove the bypass comment.
Keep auth.test direct, all trusted forwarding headers and nginx/HAProxy/PHP
protections, service settings, application code and dependency locks unchanged.
Keep reusable varnish.nix VCL/cache semantics unchanged. Correct
`docs/api-client-examples.md` and `docs/http-log-protection.md`: ordinary Varnish
topology is supported; distinguish runtime VSL from a separately enabled
persistent collector. Remove bypass/keep-bypass-on-rollback requirements and
claims of intentionally losing metrics caching. Lead owns final prose.

Use existing `tests/oauth-client-log-protection/` fixture inputs and the locked
native Varnish/varnishtest tooling for ONE focused test, not a new runner or VM
matrix. Export the actual product-generated VCL as an extra fixture value and
use a small ordinary VTC/native case with synthetic upstream responses. Prove
two identical eligible metrics requests cause one backend fetch then a cache
HIT, with the configured60s TTL (e.g. native insertion TTL evidence; no60s sleep).
A different token/query must remain a distinct cache key. A normal nonmetrics
OAuth/auth request remains pass-through, preserving method/query/body as
applicable, Cookie/Authorization and response Location/Set-Cookie/status values;
do not redact/change these wire values. Keep actual persistent nginx/HAProxy/PHP
logs protected while allowing synthetic VSL. Retain default cache eligibility;
the fixture must not force-cache cookie/auth responses to manufacture a hit.
Reuse existing native nginx fixture plumbing and disposable endpoints; no live
API/login, VSL suppression, new daemon policy or performance campaign.

Quick: hooks/format, actual generated API upstream/VCL identity, focused native
cache/pass-through case, and corrected doc references. Unchanged24-case nginx
and PHP/P0 passes remain scoped to their original exact binaries/config/inputs;
do not rerun them merely because docs changed. Commit complete correction, then
lead schedules affected independent HIGH review under mandatory-change-review,
covering cache/privacy boundary, actual routing/test and full final history. Use
all4/HIGH if required by that workflow; previous all4 review remains evidence
for unchanged implementation, not approval of the new topology. After accepted
review run the existing affected services-up scenario once through restored
ordinary nginx→Varnish→HAProxy route and applicable normal package checks. Reuse
unchanged package outputs by actual derivation/input identity. No broad client,
PHP browser or generic-workspace campaign. Existing CI41229546687 remains E2-owned;
do not cancel/rerun it now. At later authorized publication apply the normal
superseded-own-head workflow rule and retain its actual result/scope.

Preserve published45cb, live33d6 and their full recovery lineages before rewrite.
Consolidate the restored test-route/prose into the logical originating API/docs
commit and current default-protection documentation; retain the released0.32,
selector, PHP containment and default-protection functional commits/authorship.
The new cache fixture belongs with the owning protection/regression commit.
Do not leave an obsolete bypass-add/remove pair in the final ready series or
rewrite any default branch. Record old/new ranges and material equivalence limits:
this changed topology is substantive, not a claim of literal ancestry or complete
patch equivalence to deployed33d6. Lead/reviewer assess the whole cleaned series.
After review/check/publication E2 hands E1 one exact final product SHA.

### E1: restore site topology and consume the final product once

Own existing vpsfree-cz-configuration-oauth-clients; preserve current6d recovery,
upstream2e1/c218 and all prior frozen/private refs/paths. In
`cluster/cz.vpsfree/vpsadmin/common/frontend.nix` restore the four API/auth
production/maintenance backend addresses to the original Varnish socket. Do
not change Varnish VCL, HAProxy bindings/backends, aliases, host/forwarding trust,
TLS/ACME, Basic auth, private settings or PHP/React/console/download routes.
Correct only the obsolete bypass/cache-loss passages in
`docs/operations/vpsadmin-documentation-oauth.md` and
`docs/operations/oauth-client-log-protection.md`; retain deployment ordering for
edge/backend persistent-log controls. No claim that the running site was changed.

Topology/docs preparation can begin independently; final input generation waits
E2's reviewed/checked/published SHA. Use ordinary confctl for one final services
pin, preserving upstream c218 and all unrelated inputs. Consolidate into the
existing three logical pin/site/docs commits, with no obsolete routing reversal
or repeated pin stream; preserve6d/4ea/196 and earlier recovery refs. Quick checks
prove exact four restored upstreams plus unchanged sensitive-host logging,
trust/TLS/aliases/Basic-auth configuration and normal hooks. Obtain affected HIGH
review with complete old/new range/history and NO MIGRATIONS before longer checks.

Then bind the four affected target systems and generated configs to the final
source/input graph. Realize changed roots through normal four-target confctl
builds; retain exact unchanged outputs where justified. Repeat proxy nginx
syntax for the changed upstream and VCL syntax using selected native8.0.2.
Do not duplicate E2's cache semantics test if actual Varnish binary/VCL behavior
is the same; compare generated site host/backend definitions and unchanged
cache predicates/TTL separately. Site PHP5 and other syntax proofs may be reused
only with equal actual binary derivations, effective ini/pool, relevant generated
config, installed page/vendor bytes and fixture inputs. Product source-revision
metadata may change wrappers; trace that difference rather than treating path
churn as either behavior equality or a reason to repeat all tests. Any real
changed runtime input gets only its affected check. No current dev mutable-source
login certification, production access or actual cache flush/restart.

This is the complete narrow correction package, not merge/deployment authority.
React and the completed workspace integration/deployment/reservation release
remain unchanged. No claims, lifecycle or cleanup. Architect changed only this
design appendix and performed no source edit, test, eval/build or live action.

## API foundation CI failure: database semantics and cleanup (2026-10-31)

Exact published product `7219ab22a49f666077056fc2f093424547294aeb` remains
blocked on original API Specs run `41245794195`, attempt 1. This diagnosis does
not invalidate the independent reviews or relabel their local checks; neither
does it declare the product/site ready. Evidence below is under
`varnish-cache-preservation/product/postreview/`. No architect reproduction ran.

**Established failure chain.** The retained foundation result ZIPs contain
1,432 examples per mode: full seed 53137 has 29 failures/3 pending, core seed
25558 has 28 failures/52 pending. Exactly 27 failing example IDs are common:
seven IP-ownership, six IP-assignment, five MFA-factor, four IP-release, four
cluster-resource and one concurrent mail-template reconciliation example.
The extra two full/one core failures are later duplicate source-marker inserts.
Core IP-ownership fails before mail reconciliation: this is not one mail
failure contaminating every domain. Coverage correctly fails because its two
matrices failed, while its manifests cover 416/416 files in both modes
(`ci-41245794195-failed-steps.txt:18692–18696`); it is not a partition omission.

The primary database symptom is `Record has changed since last read` on current
locking reads after another connection commits. For example,
`api/spec/models/cluster_resource_adjustment_concurrency_spec.rb:47–74` holds an
old transaction snapshot, commits a competing adjustment, then expects
`api/lib/vpsadmin/api/cluster_resources.rb:291–311` to lock/read the current
budget/usage. The IP-release SAVEPOINT failures retain this earlier error in
their exception causes (failed log lines 6790, 6857, 6924, 6988). They are
transaction-unwinding fallout, not evidence that all nested transactions need
rewriting. Mail marker creation first races on its unique key, then fails on
the locking read (`api/lib/vpsadmin/api/mail_templates.rb:140–158`). Its spec's
ensure joins workers before `cleanup.call` (`mail_templates_spec.rb:467–470`);
a failed thread's join rethrows and skips committed-fixture cleanup. The later
duplicate marker errors are consistent with that concrete cleanup defect.

**Execution and source boundary.** Each topic/mode has one randomized RSpec
process and its own temporary MariaDB server/data directory/free TCP port
(`.github/workflows/api-specs.yml:204–271,348–413`,
`tools/test_db.rb:347–365`). Intentional test threads share that job's database
through separate ActiveRecord connections; the matrix does not share a DB.
Ordinary examples use an outer rollback, while these tests also commit worker
fixtures; cluster-resource examples explicitly use `:no_transaction`
(`api/spec/spec_helper.rb:15–28`). Changing matrix parallelism is not a remedy.

E2's targeted original setup retrieval, `ci-foundation-setup-facts.json` and
the linked setup excerpts/printed locks, proves both jobs used Ubuntu 26.04
image `20261025.179.1`, apt MariaDB `1:11.8.6-5ubuntu0.1`, Ruby 3.4.12,
ActiveRecord 8.1.4/mysql2 0.5.7 and all five HaveAPI gems 0.32.0. Shared gem
versions match between modes; full adds four plugin gems. Printed-lock hashes
are hashes of retained printed text, not substitutes for the effective lock
hashes in the original RSpec environment JSON. CI resolves `api/Gemfile`, not
the Nix package lock.

All six failing spec files, their implicated locking implementations and
`tools/test_db.rb` are unchanged from base `ac10a62f`; the API workflow delta
only adds libffi-dev/pkg-config. Relative to 45cb, the Varnish correction changes
none of those files or dependencies. This establishes no new locking-code
regression from that correction, but does not certify arbitrary dependency
equivalence. CI's temporary server starts `mariadbd --no-defaults` without
explicit isolation/snapshot options (`tools/test_db.rb:136–150`). In contrast,
the product database module explicitly selects READ-COMMITTED
(`nixos/modules/vpsadmin/database.nix:102`), also present in the retained 7219
services system's `etc/my.cnf:36`. That graph uses MariaDB 11.4.12, not CI's
11.8.6 (`system-recursive-derivations.json`, `services-system-closure.json`).
Local Varnish/nginx/PHP checks do not execute these API concurrency specs;
services-up uses the packaged DB contract. Their success cannot certify this
CI database environment.

**Remaining causal proof and proposed E2 reproduction.** The leading cause is
the temporary DB's implicit snapshot/current-read semantics under MariaDB
11.8, specifically `innodb_snapshot_isolation`; the original artifacts do not
record the live variable or server SQL error number. Do not assert its value
from the version alone. No more CI retrieval is needed: the required remaining
evidence is a controlled native comparison, proposed here for lead release.
In the existing declared API shell and a disposable test DB, bind the source,
actual server/client/Ruby/gem versions, and on both worker connections record
`VERSION()`, `@@session.tx_isolation`, `@@session.innodb_snapshot_isolation`,
connection ID and the first exception's MySQL error number/SQLSTATE. Do not
record DSNs or credentials. Use the existing representative, from `api/`:

```sh
bundle exec rspec spec/models/cluster_resource_adjustment_concurrency_spec.rb:68 \
  --seed 25558 --format documentation --format json --out "$evidence/result.json"
```

Use `VPSADMIN_PLUGINS=none nix develop .#api` as documented; its shell changes
to `api/`. First retain the unmodified control, then compare the same binary,
bundle and fixture with snapshot isolation explicitly OFF versus ON, retaining
REPEATABLE-READ so the adversarial old snapshot remains real. Settings apply
only to this owned disposable server/connections, before transactions. A locally
available 11.4 binary is a mechanism control, not an exact 11.8 reproduction;
record that limit rather than installing/fetching another environment silently.
Expected discrimination: ON produces the current-read abort; OFF permits the
current value/26 assertion while ordinary snapshot reads remain old. If this
does not discriminate, stop and report the first SQL/error/config difference;
do not retry broadly or modify application transaction/retry behavior. Likewise
stop if matching required binaries would require a new environment campaign.

**Conditional smallest repair package, E2 only.** Once that control establishes
the cause, make the auto-test server's existing intended contract explicit in
`tools/test_db.rb`: REPEATABLE-READ with `innodb_snapshot_isolation=OFF`, retaining
old-snapshot/current-locking-read tests. Do not make tests green merely by
switching them all to READ-COMMITTED, deleting concurrency assertions, pinning
an older runner, rescuing arbitrary SQL errors or adding product-wide retries.
Keep the ordinary product READ-COMMITTED module unchanged. Add compact actual
DB version/isolation evidence to the existing test output/environment evidence
at its owning DB setup boundary, without a new reporting framework or secrets.
Separately fix the demonstrated mail spec ensure so all workers are accounted
for and committed fixtures are cleaned even when a join raises; preserve the
original failure instead of swallowing it. Reuse the local failure-collecting
cleanup pattern in `ip_ownership_concurrency_spec.rb:45–111`. Update only the
relevant API-testing paragraph in `docs/agent-instructions/testing.md` to state
the test versus deployed database contracts. No models, migrations, API/auth
behavior, locks, VCL, nginx/PHP protections or site topology change is proposed.

Quick scope after implementation: Ruby syntax/lint/hooks; the two-connection
discriminator and existing concurrent mail reconciliation; and one controlled
worker-error case proving cleanup runs and following marker examples do not
acquire duplicate-fixture failures. The postreview foundation topics cover all
six implicated files, so do not add a redundant six-file matrix. Do not treat a
green random rerun as diagnosis. Commit one coherent test-environment/cleanup fix, preserving
published 7219 and earlier recovery/live refs. This is an independent correction
to inherited test infrastructure, not another Varnish reversal or reason to
rewrite the five accepted product commits. Obtain affected independent HIGH
review under the retained policy, including the final whole history and explicit
NO MIGRATIONS conclusion, before the full foundation topics in both modes and
normal final-head CI. Leave the current integration run/observer with E2; no
cancellation, rerun or new observer is authorized by this design.

There is no runtime compatibility, schema or deployment requirement from the
proposed test-only repair. A new final product head still requires one final
site product-pin refresh for the consolidated candidate's exact source lineage,
not a functional database upgrade. E1 must retain c7/recovery refs, consolidate
the same final pin stream, and compare actual derivations/configs before reusing
its four-target/PHP/Varnish evidence. Test/docs-only source changes can still
alter package revision metadata/wrappers; neither whole-tree inequality nor
unchanged application bytes alone establishes reuse. Repeat only genuinely
affected checks after that binding. Until the controlled DB cause and repaired
final CI are established, product/site readiness remains qualified; no merge,
deployment, profile, claim, lifecycle or cleanup action follows from this brief.

### Control-setting correction after native 73949

The corrected row-shape control completed with all three children passing, but
its ON arm did not apply ON to the adversarial connection: `on-events.jsonl`
records changer connection 20 at snapshot 1 and old-snapshot connection 19 at
snapshot 0. Both remained REPEATABLE-READ. OFF correctly demonstrated ordinary
20 followed by current adjustment 26 after the competing commit of 22. The ON
result is an invalid contrast, not evidence against the database hypothesis.

The scratch `corrected-control/control-hook.rb:27–35,66` changes only future
`Mysql2::Client#initialize` calls. The repository's `api/.rspec` already requires
`spec_helper`, which establishes/seeds connections before the additional CLI
hook; existing pooled connections are outside that hook. Constructor-only
instrumentation also cannot enforce the setting after a session reset. The
events do not distinguish connection creation/reuse/reset history for ID 19,
so retain that limit rather than inventing a witnessed sequence.

For lead release, E2 should remove the constructor setting and set/verify the
selected GLOBAL snapshot value on this owned disposable server before spawning
each fresh RSpec child. OFF/ON also select GLOBAL REPEATABLE-READ; the initial
unmodified arm keeps actual server defaults. Do not change a live or shared DB.
All child connections then start after mode selection, including replacements.
Retain the same binary/bundle/fixture/seed and read-only fact/error observations.
Assert expected snapshot/isolation on both worker connections before accepting
an outcome; any mismatch is a failed control, not a product failure or a
nondiscriminating SQL experiment. The existing native-control stop condition and
11.4-versus-CI-11.8 limitation remain. No conditional source repair is released
by these all-green but incorrectly applied modes. Original controls and E2's
owned-server shutdown evidence remain under `postreview/database-control/`.

### Valid discriminator and repair disposition

Native 71070's `database-control/global-control/` supplies the intended
contrast on unchanged 7219, MariaDB 11.4.12 and bundle lock `f2f7c737…`.
Global facts precede each fresh child; both worker sessions report the selected
REPEATABLE-READ/snapshot setting. OFF connections 16/17 preserve ordinary read
20 after the other connection commits 22, then adjust the current row to 26
(exit 0). ON connections 22/23 preserve ordinary 20 but the current locking
read raises MySQL errno 1020/SQLSTATE HY000 on `cluster_resource_uses` (expected
exit 1). Unmodified local RR/OFF passes. The receipt records the owned server
absent; earlier invalid attempts remain separate.

This establishes the mechanism and satisfies the conditional brief for E2's
already authorized minimum test-server contract, mail cleanup and testing-doc
repair. It does not establish the historical 11.8 CI session variable or make
that failed run pass. The proposed actual DB diagnostics and final foundation
checks remain necessary. No application transaction, production DB default,
dependency, Varnish or migration change follows from this result; review,
final-head verification and exact downstream pin/reuse boundaries remain as
specified above. A0 inspected the retained events/receipt, not a live database.

## Final-head auth-smoke 500: missing exception evidence (2026-11-01)

Product `fbd0b9379839dd0e747a00b5bd63e4be98880889` / tree `700d…` and site
`5e…` remain published and preserved. API run `41252535538`, attempt 1, is
failed; this appendix does not authorize a repair, rerun or downstream repin.
Evidence is in `varnish-cache-preservation/product/postreview/database-control/final-ci/`.

**Established.** Core foundation job 124688843880, seed 16772, ran 1,432
examples with one failure/52 pending; full job 124688843783, seed 33586, ran
the same 1,432 IDs with zero failures/3 pending. All failures from the earlier
concurrency run now pass in these original CI results. Core startup explicitly
observes MariaDB 11.8.6 / REPEATABLE-READ / snapshot isolation 0. Coverage has
416/416 paths per mode and fails only because core failed. E2's
`ci-41252535538-failure-facts.json` and artifact-retention receipt bind these
facts to the original run; the 25 other topic successes do not make the run green.

The failed example is `./spec/smoke/auth_smoke_spec.rb[1:1:3]`, request at
line 39, assertion at line 42. It returns generic 500 with `errors:null` after
51.649543192 seconds. Core output lines 1838–1847 show CloseAll's four examples,
then unauthenticated smoke, normal-user smoke (both pass), then admin failure
at 23:29:40Z. This is ordering evidence, not proof that CloseAll leaked state.
The next longest core example takes about 3 seconds. A roughly 50-second wait
is consistent with a timeout but establishes neither its type nor its owner.

**Source/diagnostic boundary.** `AuthHelpers#as` sets HTTP Basic credentials and
clears them in ensure (`api/spec/support/auth_helpers.rb:4–18`). SpecSeed caches
are cleared after each example; the default example wrapper rolls back its
transaction (`support/global_reset.rb`, `spec_helper.rb:20–28`). Basic auth
calls password verification/user locking, then NewBasicLogin's user lock,
login/session writes (`api/lib/vpsadmin/api/authentication/basic.rb`,
`operations/authentication/password.rb:28–106`,
`operations/user_session/new_basic_login.rb:12–32`). `User::Current` simply
returns current_user (`resources/user.rb:201–218`). PTR lookups are already
stubbed by `support/network_stubs.rb`; there is no evidence of a DNS campaign
being needed. These implicated application/smoke/helper paths are unchanged
from base ac10. The fbd-versus-7219 change is only test-DB configuration, mail
spec cleanup and its testing documentation; no auth behavior changed there.

Selected immutable HaveAPI 0.32.0 (`52j1vdh…`, `lib/haveapi/server.rb:209–233,
808–874`) catches request exceptions and invokes `:request_exception` before
returning the generic response. That path does not itself print the original
exception. The test's singleton app (`support/app_helper.rb:9–10`) installs no
request-exception diagnostic; action/description hooks are different boundaries.
The original failure provides only the response/assertion trace, not the caught
exception or blocked SQL. E2 confirmed the complete 52-artifact inventory has
no separate application/Rack log. Further original-log retrieval is unnecessary.
The missing fact is the first exception/cause/backtrace before generic response
conversion. Application defect, fixture/order contamination and environment
failure remain unresolved; no SQL retry, timeout change or auth fix is justified.
The retained local foundation passes used full seed 53137/core seed 25558 and
MariaDB 11.4.12, so they did not reproduce this exact core order/environment
(`database-control/publication.md:17–30`). Their valid scope remains intact.

**Minimal E2 diagnosis package for lead release.** Use unchanged fbd in the
existing API native environment/disposable test database, core plugin mode and
the retained original 278-file core-foundation manifest. Replay seed 16772
once with a scratch observer on the actual mounted app's server
(`ApiAppHelper.app_instance.settings.api_server.connect_hook(:request_exception)`).
Install through a suite hook after the existing app is initialized and before
examples; verify it is attached without replacing the singleton app. Record
exception class, cause chain, backtrace, and MySQL errno/SQLSTATE if present,
plus current example ID and monotonic timestamp. Return the hook's incoming
`ret` unchanged: do not raise inside it, change the response, turn off catches,
modify authentication or relax the existing 200/status/login assertions.
Keep raw exception text private outside portal exposure; omit request bodies,
headers, credentials, SQL binds and user data from shareable evidence. No new
diagnostic framework or production logging change.

From the declared `VPSADMIN_PLUGINS=none nix develop .#api` shell (cwd `api/`),
the command shape is:

```sh
mapfile -t files < "$original_core_manifest"
bundle exec rspec "${files[@]}" --seed 16772 --fail-fast \
  --require "$private_observer" --format documentation --format json \
  --out "$evidence/result.json"
```

Bind final source, effective bundle hash/gem versions, actual server version and
isolation facts. Existing native Ruby/MariaDB differences remain explicit; do
not install another environment. Full original file selection preserves the
random-order context; do not start a separate smoke-only run or repeated seed
campaign first. Expect about 4–10 minutes using existing CI/local foundation
timings, with the existing required fresh utility monitoring for this released
batch, separate from E2's integration-CI observer. Stop at the first failure or
one completed replay. If the 500 reproduces, report the caught exception before
choosing a repair. If green or the observer misses the error, report exactly
that limit; do not treat green as resolution or automatically bisect/rerun.

**Eventual repair boundary.** No application patch is presently specified.
A proven fixture/diagnostic defect belongs in the existing owning spec/support
helper; an application/auth change requires its demonstrated exception and
separate concrete disposition. Preserve assertions, public error containment,
test isolation, the current DB contract and all original evidence. Once an
actual patch is settled: syntax/lint plus its focused discriminator/regression
are quick checks; obtain the applicable affected independent review and final
history/NO MIGRATIONS conclusion before the affected full foundation check and
normal final-head CI. Preserve fbd/site5e and recovery/live refs. Source/pin
history, downstream repin and derivation-bound reuse are assessed for that
actual patch only, not preemptively. Integration CI 41252535439 stays with E2's
observer 47627. Product/site readiness remains qualified by the unresolved 500;
no merge/deploy/claim/profile/PR/lifecycle or cleanup action follows.

### Replay disposition and minimal CI exception diagnostic

E2's single released replay 97874 completed in 607.170 seconds on unchanged fbd,
original core manifest/seed 16772: 1,432 examples, zero failures, 52 pending;
the target admin example passed in 5.866906612 seconds. Its mounted-singleton
observer was attached correctly and recorded no request exceptions or observer
errors. Sanitized `database-control/auth-smoke-replay/receipt.json`, `result.json`
and `attachment-and-environment.json` bind the inputs and owned-process absence.
Raw files remain private; A0 inspected only those sanitized records. Local
MariaDB 11.4.12/Ruby 3.4.9 differs from CI 11.8.6/3.4.12. The original 500 is
not reproduced, explained or accepted by this pass. No further local foundation
replay, seed sweep, bisect or environment installation is proposed.

**Recommended bounded E2 package, pending lead release:** add a test-only
diagnostic through the existing HaveAPI hook, not a causal/auth repair. Files:

- `api/spec/support/app_helper.rb`: when constructing its cached default server,
  attach one instance `:request_exception` hook before returning/caching the app.
  Keep the same singleton and mount behavior. Repeated `app_instance` calls must
  not add listeners. Emit one compact structured line to stderr with a fixed
  identifying prefix. Existing CI RSpec logs retain it without workflow changes.
- `api/spec/smoke/harness_spec.rb`: extend the existing harness tests with the
  focused diagnostic/containment cases below. It already belongs to foundation
  in both modes, so no topic/workflow/file-manifest change is needed.
- `docs/agent-instructions/testing.md`: one short paragraph describing the safe
  diagnostic fields and where CI retains them, with no claim that it fixes 500s.

Allow only the current scoped example ID and a bounded cause chain (at most four
entries) containing class names, a repository-relative source file and line when
available, and MySQL numeric error number/five-character SQLSTATE when available
from an actual Mysql2::Error. Pick source locations from known API code/spec
directories using backtrace location path/line, not rendered backtrace strings
or method labels; omit unknown/outside/eval locations rather than exposing their
paths. Do not serialize exception messages, inspect/to_s output, SQL statements
or binds, request/context objects, URLs, headers, bodies, credentials or model
attributes. Cause classes and safe source locations identify the failure layer;
errno distinguishes, for example, lock waiting from the prior snapshot error.
An exception without these optional fields remains a useful class-only record.
This is a small private helper in existing test support, not a public formatter,
log-sanitization framework, storage format or production logger.

The hook returns its incoming `ret` unchanged and does not raise, suppress the
original error, add a retry, change timeout/isolation/authentication or alter
status/body. Guard diagnostic failure so it cannot replace the API result; a
fixed safe failure marker may be used, never the observer error's message.
Do not change HaveAPI/Sinatra error settings. `rack.errors` or generic verbose
logging is not a smaller substitute: HaveAPI catches the request exception and
converts it without retaining that original exception there, and raw logging
would include fields excluded from this package. No workflow flag/seed pin,
new artifact or broader exception-hook coverage is needed.

**Finite acceptance:** in the existing harness, temporarily stub the ordinary
Basic-auth entry point to raise a synthetic exception with a cause, known errno
metadata and secret sentinels in messages/request data. Send the normal request
through the actual cached app and capture stderr with the established RSpec
output matcher convention. Require one parseable diagnostic with the allowed
class/cause/source/errno fields, no sentinels/raw request or SQL data, and the
same generic 500 body/status. Separately preserve a nonempty hook return hash
and prove repeated app lookup does not duplicate output; successful normal
auth emits no diagnostic and retains existing 200/status/login assertions.
Cover absent source/cause metadata and a reporter failure without extending
production behavior. No need to manufacture a real lock timeout or replay the
whole foundation suite to validate observation.

Quick scope is syntax/lint/hooks plus existing harness/auth-smoke files in full
and core modes with these deliberate diagnostic cases. After a coherent
committed test-support change, obtain the applicable affected independent review
with whole-branch history and explicit NO MIGRATIONS conclusion. Preserve fbd
and all recovery/live refs; no rewrite/pin is automatic. Postreview, one ordinary
published exact-head CI run exercises the original CI environment and supplies
the useful next observation. Do not add another locally green foundation batch;
the earlier paragraph's generic full-foundation scheduling is superseded for
this observability-only package. If a future request fails, retain the original
safe diagnostic and route its demonstrated cause before repair. If CI passes,
record that result while retaining the unexplained historical failure; do not
claim a proven causal fix. No automatic reruns/dispatches or current-run changes.

The patch has no application/schema/dependency/production logging effect. Once
its actual diff exists, compare packaged inputs/derivations and revision metadata
before deciding any final site-pin refresh or evidence reuse; no preemptive site
mutation or new deployment is justified. Site5e/productfbd readiness remains
qualified pending lead disposition and new exact-head evidence. Integration
observer 47627 keeps its existing ownership. Architect edits only this design.

## 2026-11-01: React main broad-smoke serialization assertions

**Disposition:** the two original desktop failures are stale browser-test wire
expectations exposed by the approved switch from local fetch serialization to
HaveAPI AsyncClient. Repair the two expectations, preserving the behavioral
assertions; no application, dependency, API or runner repair is supported by this
evidence. This brief awaits the lead's implementation release to E3.

Original run `41291251937`, attempt 1, head
`163ad4e09a1b77f788e65a8345d69c74c8475723`, Chromium job `124802797772`
ended 237 passed / 2 failed / 1 skipped. Preserve
[original evidence](react-032/default-ci/broad-failure-evidence.json) and
[failing-case facts](react-032/default-ci/broad-failure-facts.json), including
all configured retry traces and the unsuccessful direct job-log read. A0 read
only the six identified case traces in E3's retained private archive, emitting
allowlisted method/path/query-category/status/shape facts, never raw headers,
credentials or browser data. No tests, retrieval or reruns were performed.

| Original failure | Established explanation and source anchors |
| --- | --- |
| `e2e/specs/app/vps_list_row_click.spec.ts:245` expects `{}` | Actual DELETE `/api/v7.0/vpses/300` is `{ "vps": {} }`; initial trace's request-body resource confirms it and HTTP 200. Original log records the same shape mismatch on both retries. `src/lib/api/vps.ts:374–394` still passes namespace `vps` without member deletion options; `haveapi.ts:359–373` passes that namespace to the package. The retained actual npm 0.32 archive's `dist/haveapi-client.js:3064–3069` supplies `spec.params || {}` under a defined namespace, matching release source `0e7166a0`, `clients/js/src/haveapi/async/request.ts:132–138`. This adds no lazy/expiry/force setting. HaveAPI's object-layout normalization (`servers/ruby/lib/haveapi/params.rb:270–287` at that release) normalizes an absent optional object namespace to `{}`; this is source-level contract evidence, not live deletion proof. |
| `e2e/specs/app/profile_keys_sessions.spec.ts:156–160` waits until the 90-second test deadline | The request predicate demands `user_session%5Bauth_type%5D=token`. All three original traces instead contain literal brackets, decoding to `user_session[auth_type]=token`; each initial filtered GET and subsequent poll returned HTTP 200, envelope `status:true`, one row of category `token`. First filtered GETs occurred at 09:07:24.614Z / 09:08:57.502Z / 09:10:30.248Z. The actual package's `dist/haveapi-client.js:214–222` constructs literal namespace brackets. The existing mock at `profile_keys_sessions.spec.ts:80–84` already reads `URLSearchParams` and filters correctly. The observer fails to match an existing successful request; duration is not the cause. |

Both failing specs and domain helpers `vps.ts`/`userDossier.ts` are unchanged
between base `40653dff` and merged `163ad4e`. Base `haveapi.ts:180–209` used
`URLSearchParams`, and lines 451–461 omitted the body namespace when params were
absent. The approved adapter delegates both decisions to the actual library.
This establishes missed fixture adaptation in that transport change, without
claiming the behavior first appeared in release 0.32 rather than an earlier
library release. Prior unit/build/package passes did not execute these browser
specs. Mobile success is not counterevidence: these cases have `@smoke`, not
`@smoke-mobile`, and `scripts/e2e-harness.mjs:15–19` selects those separately.
The profile test's later rename/close assertions were not reached; their outcome
on this head remains unobserved by the failed run.

**E3 package, after lead release:**

- In the VPS spec require exact `{ vps: {} }`, retaining method/target,
  confirmation, absence of admin-only options in member deletion and
  no-row-navigation assertions.
  Keep the admin lazy/hard/retention cases unchanged. Do not accept arbitrary
  empty-looking payloads or modify the production serializer to satisfy `{}`.
- In the profile spec construct `new URL(r.url())` and match GET, exact
  `/api/v7.0/user_sessions` pathname and
  `url.searchParams.get('user_session[auth_type]') === 'token'`. Register the
  waiter before selection as now; retain row-visibility/exact-ID/rename/close
  assertions. Do not alter timeout/retry counts or weaken the auth category.
- The VPS spec is already in strict E2E coverage. The profile spec is deferred:
  adopt only that complete file in `tsconfig.e2e.json` and
  `scripts/fixtures/e2e-type-coverage.json`, removing its deferred entry rather
  than refreshing its hash. Make only necessary local fixture typing/index
  corrections with unchanged data and runtime behavior; stop for design
  disposition if this needs wider helper or product changes.
- Record the correction and evidence limits in a dated `docs/work-log/` entry
  linked from `WORK_LOG.md`; a short existing verification-guide clarification
  may explain semantic query comparison. Requirements REQ-021/046/061/064
  retain their current contracts. No inventory regeneration is needed when
  routes and adapters remain unchanged.

**Checks and stopping condition:** quick scope is the existing locked-toolchain
static/type/coverage/documentation gate and declared hooks, with focused review
of unchanged behavioral assertions. After all intended changes are committed,
obtain independent affected review including the complete follow-up range and
explicit NO MIGRATIONS conclusion. Then run both complete affected specs once
through the ordinary wrapper, Chromium, existing two-worker setting and
`--retries=0`, in the existing isolated exact-source environment; use the normal
watcher for uncertain duration. For example, select these two paths with
`E2E_START_SERVER=1 node scripts/playwright.mjs test e2e/specs/app/vps_list_row_click.spec.ts e2e/specs/app/profile_keys_sessions.spec.ts --project=chromium --workers=2 --retries=0`.
This must reach and pass the profile's remaining steps
and preserve neighboring deletion cases. Retain any new failure and stop for
its concrete evidence; no seed sweep, blind replay or general browser campaign.
Normal relevant PR CI remains required under repository policy; this brief
authorizes neither manual CI dispatch nor another run on the old head.

The correction is a new focused follow-up above merged main, never a rewrite of
`2ee0167a`/`163ad4e`. Preserve published/recovery/live refs and private alias
contents. No persisted format, migration, BFF/auth behavior, package lock,
production asset source or deployment policy changes are intended. Do not
automatically repin site configuration or rebuild unrelated packages; bind any
verification reuse to actual changed inputs and distinguish new revision
metadata from unchanged runtime source. There is no production deployment or
rollback action here. Original smoke observer 17843 and product CI ownership
remain unchanged; lead owns state, review/release and any later integration.

## 2026-11-01: Original PR smoke adds two transport-fixture corrections

**Evidence and disposition:** original main/push run `41291251986`, attempt 1,
exact merged `163ad4e`, failed in Chromium (2 failed / 605 passed) and mobile
Chrome (1 failed / 548 passed); mobile WebKit passed 249 with 2 skipped. E3
preserved [original metadata](react-032/default-ci/smoke-failure-evidence.json)
and [case facts](react-032/default-ci/smoke-failure-facts.json), including the
original configured retries. Observer 17843 is consumed; all three original
React runs are terminal. No new CI query or execution belongs to this diagnosis.
The existing seven-file correction at `a44b3ac` remains separately frozen until
the lead releases this extension; these findings must enter the final scope
before independent review, not be silently treated as fixed by section 7340.

- `e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:1220`, case at 1180,
  repeats the proven member-delete `{}` versus `{ vps: {} }` mismatch in initial
  and both retries. Apply the same exact namespaced-empty assertion as the
  list-row case. Preserve member/admin action visibility, lack of admin deletion
  options, confirmation and the final navigation assertion at 1221, which was
  not reached in the failure. No application or serializer change is justified.
- `e2e/specs/app/profile_session_transaction_filter.spec.ts:268`, case at 199,
  fails because its dispatch-location array is empty on desktop/mobile and both
  retries. Its recorder at 202–225 patches only `window.fetch`; the accepted
  adapter sends XHR. The original representative Chromium traces, initial and
  both retries, explicitly show `resource_type=xhr`, GET
  `/api/v7.0/transaction_chains`, decoded limit `51`, no session-filter key and
  HTTP 200. The preceding page-URL normalization, visible-row and actual mock
  request-count assertions at 259–263 passed. This establishes a disconnected
  test observer, not a failure to issue the request or a timeout/environment
  cause. The strict dispatch-time ordering assertion itself remains unproven by
  this run; later normalized URL/data observations cannot replace it.

Both specs and `TransactionChainSessionFilterGuard.tsx`/`TransactionChainsPage.tsx`
are byte-unchanged from `40653dff` to `163ad4e`. The guard at lines 28–37 renders
loading while replacing invalid parameters; the page wraps its content with it
at line 53. Preserve that contract. These are two further instances of missed
fixture adaptation in the same approved fetch-to-AsyncClient integration, with
one new observer mechanism to update. They are not covered by the first two-file
fix. No separate product defect is established, and no further artifact retrieval
is needed to choose the bounded correction.

**Proposed E3 extension, subject to lead release:** change only those two specs,
the existing E2E coverage/configuration and the same correction documentation.
Replace the profile case's local init-script fetch probe with native-XHR
observation: retain method/URL per XHR instance when `open` succeeds, then record
`window.location.href` synchronously immediately before forwarding the matching
native `send`. Match GET, exact API transaction-chain path, decoded page limit
51 and absent `transaction_chain[user_session]`. Forward original `this`, all
arguments, native results and exceptions; preserve async mode/headers/body and
do not issue, intercept or delay requests. A small local WeakMap plus open/send
wrappers is sufficient; no shared instrumentation framework or production hook.
Do not substitute an asynchronous Playwright request-handler/page evaluation,
an `open`-only snapshot or eventual `page.url()` for send-time ordering.

Retain positive actual-request and recorder counts and require every recorded
location to lack the invalid browser `user_session` parameter. Retain the two
other profile filter/link cases. Adopt the complete profile transaction spec
from its deferred manifest entry into `tsconfig.e2e.json`, with only necessary
local typing changes; do not refresh its deferred hash. The lifecycle spec is
already adopted. No retry/timeout/workflow/dependency/auth/backend change.

**Verification:** add static type/coverage checks for this adopted file to the
existing quick batch and reconcile the technical work-log entry. Commit the
complete correction above immutable main, then independent affected review must
cover both earlier fixes, these additions, preserved dispatch-order strength,
the complete follow-up history and NO MIGRATIONS. After review, extend the one
focused browser batch: the lifecycle member-delete case on Chromium and all
three profile transaction-filter cases on Chromium/mobile Chrome, with existing
two-worker setting and retries disabled, alongside the previously planned two
files. Use explicit file/title selection; do not run both whole PR matrices
locally. Preserve original failures; stop if the restored ordering observation
or a later assertion fails and report that concrete fact before product changes.
Normal applicable PR CI remains separate; no manual dispatch/rerun is released.
No additional unit/Nix/build/deployment or site-pin campaign follows from these
test-only changes. Runtime contracts, source/pin recovery, independent product
CI ownership and the session-open boundary remain as in the preceding section.

## 2026-11-01: Patch-release consumers and API1/API2 documentation setup

### Independent E1 operator-documentation package

This package is released independently of publication of the upcoming HaveAPI
patch. E1 owns only `docs/operations/vpsadmin-documentation-oauth.md` in
`vpsfree-cz-configuration-oauth-clients`, baseline
`64220e2877417f5a6669358b98660ae2b5649bae`. Lead owns the final prose pass before
commit. Prepare instructions, not their execution; no host access, credentials,
registration, deployment, channel update or source-hook change in this package.

Replace the existing first-setup example with these settled requirements:

- Generate once on `api1.int.vpsfree.cz` (`172.16.9.128`), through the installed
  `vpsadmin-api-shell`. From its initial packaged `api/` working directory use
  `../ruby-env-wrapped/bin/ruby -rsecurerandom -rjson`; do not assume Ruby,
  Python or OpenSSL is on root's PATH. Generate in a new
  `/var/lib/vpsadmin/api/documentation-oauth-bootstrap` directory, mode `0700`,
  with Ruby umask `0077` and refusal to overwrite an existing directory.
  Write a 64-character hex client secret, JSON and a separate 64-byte binary
  session key, without printing their contents. The secret helper has no newline.
- JSON uses literal client ID `api.vpsfree.cz`, callback
  `https://api.vpsfree.cz/_documentation/oauth/callback` and `switch_user: true`.
  Retain the same secret, JSON and binary key across both workers and upgrades;
  generation/registration is for first setup, not every update.
- From the user's local machine, prepare a private local directory and root-only
  staging on API2 (`api2.int.vpsfree.cz`, `172.16.9.129`). Copy each named JSON/key
  file with `scp -3 root@api1.int.vpsfree.cz:/var/lib/vpsadmin/api/documentation-oauth-bootstrap/FILE root@api2.int.vpsfree.cz:/root/vpsadmin-documentation-oauth/FILE`.
  This relays through the local machine, which can SSH to both hosts. Copy the
  secret helper from API1 into the private local directory for CLI registration;
  no direct API1-to-API2 SSH capability is assumed.
- Register through the local `vpsfreectl`, with its ordinary administrator
  authentication and `--api https://api.vpsfree.cz --auth token --token-via header
  --no-raw-values oauth2_client create --`. Use `--name 'vpsFree.cz API documentation'
  --client-id api.vpsfree.cz --client-secret "@$HOME/vpsadmin-documentation-oauth/client-secret"
  --redirect-uri https://api.vpsfree.cz/_documentation/oauth/callback --no-is-default
  --access-token-lifetime renewable_auto --access-token-seconds 900
  --no-issue-refresh-token --allow-single-sign-on`. Preserve the existing
  uncertain-create/list/show recovery advice; do not recreate an existing client
  or disclose the secret in arguments/output.
- Install regular JSON/key files under `/var/lib/vpsadmin/api/config`, directory
  owner/group `vpsadmin-api:vpsadmin-api`, mode `0750`; files same owner/group,
  mode `0600`. Make the key available before enabling the JSON. Retain private
  contents on upgrade. Setup preserves regular files and links runtime config;
  there is no separate `vpsadmin-api-setup.service` to run. Restart with
  `systemctl restart vpsadmin-api.service vpsadmin-password-recovery.service`;
  the companion's Requires/After ordering follows the API's own preStart setup.
- Explain the unchanged non-sliding cookie: the hook's `session_lifetime: 3600`
  is a ceiling; callback fixes expiry to the shorter token expiry, here about
  900 seconds from sign-in. API use can renew the token, but does not extend the
  documentation cookie. No refresh-token or sliding-cookie redesign.
- Replace the incorrect SSO-off/keep-switch-false advice. With the supporting
  release and consumer hook, Switch user sends `close_sso=1` on revocation,
  matching legacy PHP; ordinary logout is unchanged. State the matching-software
  prerequisite honestly while publication is pending; do not invent a released
  version or claim real-provider acceptance. Preserve callback protections,
  provider trust, ExceptionMailer, anonymous-without-JSON and sanitized failures.

Source anchors retained from product `0f450b89`: `api-runners.nix:19–33,77–81`,
`api-app.nix:108–149`, `api/default.nix:228–257,298–312` beneath
`nixos/modules/vpsadmin/`; `packages/api/common.nix:47–48`;
`api/models/oauth2_client.rb:17`; `resume_oauth2.rb:27–41` beneath
`api/lib/vpsadmin/api/operations/user_session/`. Cookie behavior is in released
HaveAPI `0e7166a0`, `servers/ruby/lib/haveapi/documentation_oauth.rb:138–143,203–208`.

Finite doc quicks: `git diff --check`; extract the final shell and Ruby blocks
to owned scratch files and run `bash -n "$QUICK_DIR/setup.sh"` and
`ruby -c "$QUICK_DIR/generate.rb"` in existing tooling. Inspect exact hosts,
paths, modes, flags, ordering and retained-file behavior against this brief.
Do not execute SSH/SCP/CLI/restart snippets. Lead prose pass, normal hooks and
final committed independent review remain required. No system build, browser,
live login or provider acceptance is part of these quick checks. No migrations.

### Release-gated E2 product and E1 consumer packages

Accepted producer interface, relayed by lead in
`026fe102-a779-412f-a08c-5f11b32d1529`, is
`documentation_oauth(..., switch_user: true, switch_user_revoke_params: { 'close_sso' => '1' })`.
The new option is a static `Hash<String,String>`, default `{}`, inert when
switching is disabled. The producer rejects overrides of `client_id`,
`client_secret`, `token` and `token_type_hint`; only a validated switch after
capability/Origin/CSRF checks adds parameters to revoke POST. Ordinary logout,
authorize/token/state/PKCE and failure semantics remain unchanged. The producer
owns that implementation and shared-SSO fixture. We consume its accepted release
evidence; do not duplicate its investigation/tests or access its session files.

As of this brief, `haveapi-0.32`/`v0.32.0` is `0e7166a0`, master `209a7ac0`,
and no patch tag has been supplied. Expected `0.32.1` is not publication proof.
Lead must supply the actual tag/commit and published gem identities/hashes before
dependency/hook implementation. E2 binds artifacts to that release and stops on
missing gems, unexpected compatibility changes or extra dependency upgrades.

| Owner / existing alias | Complete boundary | Dependency |
| --- | --- | --- |
| E2 / `vpsadmin-oauth-client-logs` at `0f450b89a5e39c203db0bbdfe0df86b386275343` | Update the five API HaveAPI dependencies in `api/Gemfile`, generated `packages/api/{Gemfile,Gemfile.lock,gemset.nix}`; keep server, Ruby client and Go/Rust/TypeScript generator versions aligned. Add the literal revoke map to `api/config/api.rb.example`, alongside the existing private switch flag. Update the hard-coded selector/exact tooling version in `tools/api-schema-export/Gemfile` to the accepted API release. Reconcile only directly affected product docs. | Actual published release and accepted interface. |
| E1 / `vpsfree-cz-configuration-oauth-clients` | Add the same literal map in `configs/vpsadmin/api/api.rb`; extend its existing `spec/configs/vpsadmin/api/documentation_oauth_spec.rb` for false/default and true forwarding, preserving all sanitization/anonymous behavior. Finish the operator doc prerequisite, then one final `vpsadmin` / `vpsadmin` channel pin. | Hook requires supporting product; final pin requires E2's reviewed, quick-checked, published exact head. |
| E3 / `vpsadmin-webui-031` at `f2765d3fd778927f4cda3563f66615bfcf72b7cf` | No current package. npm `haveapi-client@0.32.0` does not implement this Ruby documentation flow. | Open only if actual publication scope establishes a JS need; then separately bind package/lock/provenance/Nix hash. |

Use the static map in Ruby, not a new private-JSON field or provider/backend
change. Keep `settings.fetch('switch_user', false)` for existing installations;
the documented first setup explicitly supplies true. Library inactivity when
false keeps ordinary logout unchanged. No fallback that silently drops the
new option on old HaveAPI: 0.32.0 rejects unknown options. Raise the five API
minimum patch requirements to the actual compatible release and ship hook/pin
together. Rollback restores the prior hook/product pair, retaining the same
private files/key; it restores the old switch limitation. No migrations,
credential rotation, protocol/storage change, PHP dependency bump or unrelated
Ruby-client/download-mounter/outage-report package update is intended.

For E2 metadata generation, avoid the broad `rake vpsadmin:gems` task. Even
`vpsadmin:gems:api` deletes its lock before resolving (`tasks/gem_updates.rb:136–155`),
so prefer the existing writer plus targeted native lock update: from the root's
declared Ruby environment run
`ruby -rrake -r./tasks/gem_updates -e 'Vpsadmin::Gems.write_api_gemfile'`; in
`packages/api`, run `bundle lock --update haveapi haveapi-client haveapi-go-client haveapi-rust-client haveapi-typescript-client --conservative`,
then `bundix -l` and `nixfmt gemset.nix`. Preserve all unrelated locked versions;
stop and report any required expansion. `api/Gemfile.lock` is untracked, so do
not add it. The schema tooling's explicit selection must follow the new API
minimum rather than leave its old string guard broken. E2 also updates the
independent exact-version guard in `tools/api-schema-export/runner.rb:25` to
that same actually published patch; updating the Gemfile alone leaves the
runner unusable. Preserve exact equality and refusal semantics, without a
generalized compatibility layer. Align the directly matching references in
`docs/api-schema-export.md:21` and `docs/api-client-examples.md:118`; lead applies
the final prose pass before commit. These companions retain the release/tag/
five-gem evidence gate and add no schema export or database execution.

E1 uses `confctl inputs channel set --commit vpsadmin vpsadmin FINAL_PRODUCT_SHA`
for the exact published feature head, or ordinary
`confctl inputs channel update --commit vpsadmin vpsadmin` only when the selected
upstream is the intended final head. This owns `vpsadminServices`; preserve
`vpsadminWebui` and notification-template follows. Preserve independent
`devWorkspace`, nixpkgs and node staging/production channels. Do not manually
edit locks or add a React pin without an actual E3 package.

### Finite downstream quick batch and acceptance

User's **ONLY QUICK VERIFICATION** overrides product testing guidance requiring
`services-up` after HaveAPI updates and site guidance requiring affected-host
builds. Lead accepted this disposition. Neither check, full unit/API/foundation
or browser suites, Nix system builds nor extra live checks are authorized here.
No claim of equivalent VM, packaged-service or real-provider coverage follows
from the quick batch. Existing product observer 89033 remains separately owned.

Use existing declared environments and retained local tooling; do not turn
dependency preparation into a new installation/build campaign. One pass of each
applicable quick below is sufficient; repeat only an affected failed check after
repair. Stop on unexpected dependency drift or an environment requiring broad
build/setup, and report the exact blocker.

1. **E2 release identity/content/load:** bind producer publication receipt to all
   five downloaded `.gem` hashes and selected lock/gemset identities. Inspect
   their packaged documentation/templates/entry points, not just the Git tag.
   Against the actual selected API bundle, run `bundle check` and the following
   DB-free check, replacing `RELEASE_VERSION` only with the evidenced version:

   ```sh
   bundle exec ruby -rhaveapi -rhaveapi/documentation_oauth - RELEASE_VERSION <<'RUBY'
   expected = ARGV.fetch(0)
   %w[haveapi haveapi-client haveapi-go-client haveapi-rust-client haveapi-typescript-client].each do |name|
     spec = Gem::Specification.find_by_name(name)
     abort "Unexpected #{name} version" unless spec.version.to_s == expected
   end
   [false, true].each do |enabled|
     HaveAPI::DocumentationOAuth.new(
       client_id: 'synthetic-client', client_secret: 'synthetic-secret',
       redirect_uri: 'https://api.example.test/_documentation/oauth/callback',
       session_secret: 'k' * 64, scope: ['all'], session_lifetime: 3600,
       switch_user: enabled, switch_user_revoke_params: { 'close_sso' => '1' }
     )
   end
   RUBY
   ```

   This establishes actual constructor compatibility, not revoke/SSO behavior;
   the producer's accepted fixture supplies that behavior evidence. Run
   `ruby -c api/config/api.rb.example`, `ruby -c tools/api-schema-export/Gemfile`,
   `ruby -c tools/api-schema-export/runner.rb`,
   `nix-instantiate --parse packages/api/gemset.nix >/dev/null`,
   scoped `bundle exec rubocop config/api.rb.example` from the API component,
   and `git diff --check`. Inspect generated lock scope and run normal hooks.
   Confirm the schema-tool Gemfile, runner equality guard and the two owning
   documentation references select the same evidenced release. Do not run the
   exporter, database setup or a broader schema/test campaign for this companion.
2. **E1 hook:** from the configuration shell run
   `bundle exec rspec spec/configs/vpsadmin/api/documentation_oauth_spec.rb`,
   `ruby -c configs/vpsadmin/api/api.rb`,
   `bundle exec rubocop configs/vpsadmin/api/api.rb spec/configs/vpsadmin/api/documentation_oauth_spec.rb`
   and `git diff --check`. The spy proves exact hook arguments, not library
   support; bind it to E2's actual constructor check and producer behavior proof.
   Inspect `git diff -- flake.lock` semantically for one intended service revision
   and required follows, preserving unrelated nodes; use `python3 -m json.tool
   flake.lock >/dev/null` and `nix-instantiate --parse flake.nix >/dev/null` for
   syntax. No host evaluation/realization is needed for this limited claim.
3. **Docs:** use the E1 syntax/inspection batch above and lead's prose pass. No
   registration, live sign-in, new credentials or request-log inspection.

Commit all intended changes, then independent final review covers all four
applicable lanes (authentication/cross-project risk), complete new base-to-head
history, one final dependency/pin stream and explicit NO MIGRATIONS. Review is
not waived by quick-only scope. No long-check phase follows this batch; report
the omitted coverage and actual final inputs plainly. Existing merged histories,
published/recovery refs, live paths and private state remain intact. New
follow-ups target product/configuration master but this milestone does not
authorize default integration, deployment, lifecycle actions or cleanup.

## 2026-11-01: Three-step production KB preview from accepted KB08

**Scope:** show the exact proposed logical revisions before publication approval.
Lead accepted the three groups below. E1 materializes local full-page snapshots
and predecessor diffs; lead owns summary wording and user presentation. This is
regrouping of accepted text, not a new article rewrite, and needs no new commit,
review, SDK/runtime or staging campaign merely to show it. Production writes,
staging replay/reset and lifecycle actions remain unauthorized.

**Exact articles and bytes:** canonical `kb-candidates/cs/navody/vps/api.txt`
(`cz`, `navody:vps:api`) and `kb-candidates/en/manuals/vps/api.txt`
(`org`, `manuals:vps:api`) equal their `publication/08-token-request-examples`
snapshots and the accepted KB08 hashes. No media, other article or managed-page
contract edit is needed. The two candidate-index entries are ordinary updates,
without managed markers. Retain historical eight-iteration evidence separately;
it is not the proposed production sequence.

| Language | Captured production revision / SHA256 | Required final KB08 SHA256 |
| --- | --- | --- |
| CS | `1783860648` / `8ea88de825d7b3823aee1d4ff8fd2704c9eb2f431cfbb944643927eabde3fd13` | `d18fbda8e3945ce77fc809b740432b90aef1ac7d5641c7635773034b2c887904` |
| EN | `1777543182` / `8006293f735a7e6f45c04d2d59ad82a003afa4547db1ddb38f380504e1e107d3` | `5cb41ae1d666de9f6b5cb679080c3104b1a56ebd14303d96af1e99696d4e72fd` |

Use `kb-original/{cs,en}` as the captured starting bytes. The retained KB08
staging revisions are CS `1793458925`, EN `1793458929`, bound by
`kb-restructure/token-request-examples/staging/receipt.md`; these are historical
readbacks, not fresh production guards. Its review and exact R1 acceptance
remain the source-content evidence. Final bytes are 30346 CS / 28214 EN.

### Exact grouping and section boundaries

All boundaries below are unique full headings; spans include their separating
blank lines, and end immediately before the named next heading. Copy final
spans verbatim, retaining final trailing bytes. Do not reconstruct prose or code.

1. **Remove obsolete material, both languages.** Delete the obsolete
   `haveapi-fs` and `haveapi-webui` bullets from the original opening catalogue.
   Remove original `===== Souborový systém ======` through immediately before
   `===== Ukázky použití =====` (CS original lines552–626), and
   `===== File system ======` through immediately before
   `===== Usage Examples =====` (EN493–567). Keep both following backup examples.
   In CS only, remove the `**poznámka** Pokud API vpsfree vrací http kód 500`
   paragraph and surplus separating blanks before `===== Autentizace =====`;
   preserve the REST/protocol text and link. No corresponding English warning
   edit or extra no-op English revision. Summary intent: CS
   `Odstranění zastaralých klientů a poznámky o HTTP hlavičkách`; EN
   `Remove obsolete clients and the haveapi-fs guide`.
2. **Final authentication, CLI installation and Ruby examples.** Replace the
   span from top-level `===== Autentizace =====` / `===== Authentication=====`
   through the end of Updates with the corresponding final KB08 span, ending
   before `===== Klient pro Ruby =====` / `===== Ruby client =====`.
   This updates the authentication documentation link, shared token/challenge
   explanation, maintained Ruby requirements and executable-directory discovery;
   CS also removes the Ubuntu label's version, EN promotes the CLI heading.
   Existing CLI commands and scopes stay at their accepted final bytes.
   Replace the old top-level Usage Examples block with the final Ruby block,
   ending before `===== Další klienti =====` (final CS551–654) /
   `===== Other clients =====` (EN499–602). This introduces the final Ruby VPS
   example and changes both backup auth blocks directly to username/password
   with commented existing-token alternatives, preserving backup logic and
   final heading text/hierarchy. Keep the original opening catalogue, minus
   step1's deletions, until step3. Add the final English
   `<page>manuals:vps:api</page>` mapping now; retain the Czech mapping and
   maintainers footer. Summary intent: CS
   `Upřesnění autentizace, instalace CLI a příkladů pro Ruby`; EN
   `Clarify authentication, CLI installation and Ruby examples`.
3. **Final other clients and linked opening overview together.** Replace
   `===== Práce s API =====` through before `===== Autentizace =====` with
   final CS17–36; likewise `===== Working with the API =====` through before
   `===== Authentication=====` with final EN18–37. Insert the final Other
   clients block from its heading to before the existing CS maintainers footer,
   or through EOF in EN. Include all six complete installation/auth/list/run/link
   sections: PHP, Python, dynamic JS/TS, Go, generated vpsAdmin TS and Rust.
   Every new example already requests a token and includes its commented TOKEN
   alternative. Copy the accepted completion checks, localized safe diagnostics,
   generated TS `/v7.0` prefix and `javascript` tags exactly. Introduce the final
   eight overview links only here, when all their target headings exist.
   Summary intent: CS `Doplnění přehledu klientů a úplných příkladů použití`;
   EN `Add the client overview and complete usage examples`.

The final result must equal KB08 byte for byte, including existing Czech
`<maintainers hidden>` footer and the English EOF. Preserve all retained heading
anchors despite nesting changes; removed obsolete filesystem anchors are the
intentional deletion. Neither article contains `<kb-managed>` or
`<vpsadmin-nav>` markers; do not introduce either or remove any newly discovered
annotation during freshness reconciliation. Both final language markers use the
English page ID. Preserve all unrelated content. No main-client preference,
temporary token-only new example, optional-version selector or OAuth explanation
is introduced and later removed.

### E1 preview package and eventual publication boundary

Prepare one small `kb-restructure/publication-preview/` bundle: six complete
page snapshots (three steps × two languages), six predecessor unified diffs,
one content-hash chain and one compact overview linking them and final staging
previews. Keep old `publication/01..08`, canonical pages, root aggregate
manifests and staging history unchanged. Those root manifests describe a single
aggregate update and must not be presented as a three-revision release.
Do not invent future production revision IDs or executable release manifests
whose later predecessor revisions do not yet exist.

Quick acceptance is offline byte/hash/diff and markup inspection: the first
predecessors equal captured originals; each later predecessor equals the prior
snapshot; applying all diffs yields canonical KB08 exactly; only the two article
IDs change; no introduced overview anchor is unresolved at its step; final code
blocks, language tags, translation markers and footer equal the accepted pages.
Reuse retained KB08 syntax/render evidence for identical final code. Do not run
examples, install SDKs, repeat browser/runtime checks or fetch all KB articles.
Lead reads the proposed localized summaries before presentation. This preview
does not assert that the retained production/staging observations are current.

Before an actual release, perform bounded fresh page-info/source/page-info reads
for these two production and two staging pages, requiring stable revisions and
exact hashes; verify current staging owner/up/pending state and normal identity/
edit ACL. Production drift requires reconciling that concrete page and refreshing
the proposed diff for user review; never silently replace a concurrent edit.
Staging drift must be explained without reset or private-state modification.

Current selected public wrappers bind tools
`/nix/store/9019d7wm0c40q59vrnlf1clwp7q00xrd-vpsfree-dev-workspace-tools-0.1.0`.
Source `lib/kb_release.rb:128–151,438–499,526–563,616–643,881–890` confirms schema5,
unique page IDs per manifest, source revision+hash guards, exact localized
summary checks and one session-bound pending digest. There is no sequence command
or multi-revision queue. After approval of the exact immutable sequence, use
ordinary stage → verify → promote separately for each step/language, serializing
the pending manifest and completing each logical step in both languages before
the next. Bind later guards to observed production readbacks, not staging
revisions or predicted timestamps. A later staged candidate cannot satisfy an
earlier step's baseline; if needed at that later authorized phase, ordinary
public staging saves can select the approved snapshot and summary before normal
stage/verify/promote. No tool changes, staging reset/history deletion or replay
of obsolete eight-stage approaches is required. None of those writes is part of
this preview assignment; no publication, commit/review campaign or lifecycle
authority is implied.
