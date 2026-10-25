# HaveAPI 0.30 release preparation

**SDK registry-read stop, 2026-10-24:** the user explicitly authorized the
one-time `v0.1.0` movement to reviewed/tested b6f84679; that authority stands.
The attempted launcher stopped before any tag/ref/dispatch change on a public
API HTTP 403. The [bounded registry observation](sdk-registry403-resolution-design.md)
records the one permitted sparse-index GET: HTTP 404, but cached with Age 1798.
It does not establish fresh origin absence or explain the 403. Recommend one
lead-routed crate-name API read matching the unchanged workflow bootstrap
predicate before replacing the stopped launcher's guard. No source, registry,
tag, dispatch, credential or default-branch action occurred in this investigation.

**SDK archive recovery design, 2026-10-24:** release attempt
`40123807556/1` failed after a successful credential-free native dry run because
the workflow expected `cargo package`'s archive path after `cargo publish`.
The [focused Cargo archive/recovery brief](vpsadmin-sdk-cargo-archive-recovery-design.md)
records exact Cargo 1.98 source evidence and the proposed narrow owner3 helper,
tests, affected review and one actual native dry-run validation. Native upload
was skipped; neither candidate nor actual-publish artifacts exist for that
attempt. Preserve tag `v0.1.0` and all original evidence. No rerun, tag movement,
version change, SDK main integration or publication-recovery exception is
authorized by this design; lead routes the concrete recovery choice after the
fix is reviewable. No change to generated Rust, schema, dependencies or MSRV.

**Current SDK scope, 2026-10-24:** the user authorized regenerating and releasing
`vpsadmin-client`, provisionally version 0.1.0, with released HaveAPI 0.30.1.
The [SDK execution brief](vpsadmin-client-0.1.0-release-design.md) preserves the
saved API 7.0 snapshot, applies the library-lock policy, and binds regeneration
to the original released generator and Ruby lock. Owner3 owns SDK source/Git
after lead routing; architect0 owns this design. A reviewed immutable feature
tag can use the existing manual publication workflow: **SDK main integration is
not authorized by this release request**. Registry ownership/bootstrap credentials
and release-environment protection remain prerequisites to establish. Preserve
all HaveAPI artifacts/refs; no deployment or lifecycle action. The earlier
[empty Actions step display finding](release-0-30-1-publication-step-metadata.md)
is independent of successful HaveAPI publication and destination verification.

**Current authorization, 2026-10-24:** the user directed continuing 0.30.1,
backporting the actual library-lockfile removal and releasing it. Removal,
HaveAPI master integration, supported-branch backport, tag and publication are
now authorized, superseding the earlier holds below. Lead accepted the complete
[lockfile removal brief](library-lockfile-policy.md) at SHA-256
`95d290d686ab217c6905dbb677e2c1672584cbd92cec80feb4e4631cf17a36b6` for implementation;
no additional design gate applies. Owner0 owns the shared removal worktree from
master7ac, Git and shared release files; owner1 owns Python, owner2 JS and owner3
Rust in disjoint paths. Retain real native local resolutions, all nine actual
release lock records and tools-only original-artifact verification. Preserve
source91 and all original artifacts. Required review/checks and protected release
approval remain; no deployment or lifecycle action is authorized.

**Release-test prerequisite proposal, 2026-10-24:**
[Owning TypeScript prerequisite](release-0-30-1-release-test-compiler-prerequisite.md)
defines one offline JS-only `npm ci` using an opaque copy of the qualified
same-session cache, all 214 applicable locked packages and native integrity
checks. Owner1 owns setup after acceptance; owner0 then reruns only the failed
maintained `make release-test`. Preserve the successful release-check, exact
19-path metadata state, locks and all 47 retained dist outputs. No product
changes, scripts/build campaign, network fallback or publication is proposed.

**Metadata recovery design, 2026-10-24:**
[Native uv recovery](release-0-30-1-uv-recovery-design.md) preserves the stopped
twelve-path 0.30.1 state and original failure. Owner1 prepares native shadow
metadata/cache proof with all 26 external lock records unchanged; owner0 resumes
the maintained target offline only after acceptance and a new attempt grant.
No dependency/Python-range/backend/Makefile change or publication is proposed.

**Current authorization, 2026-10-24:** the user directed merging completed fixes
and dependency/profile changes into HaveAPI `master`, then backporting to
`haveapi-0.30` and preparing 0.30.1 with a refreshed CHANGELOG date. The exact
owner sequence, retained six backports, version boundary and final verification
gates are in [integration/backport/release preparation](integration-backport-release-preparation.md).
Complete profile implementation, committed review and affected longer checks
before integration. This supersedes the integration/preparation holds below;
tags, publication, registry/PHP mirror writes and deployment remain unapproved.
Downstream ff876abe is already integrated; no additional repository work is implied.

The accepted [0.30.1 version-sensitive verification facts](release-version-sensitive-verification.md)
define the minimum real Rust/Go subset, 18-path version boundary and owning lock
rebinding. Preserve successful pre-version model/compiler evidence under exact
input proof; do not relax or rerun the fixed-4dc0 model comparator unchanged after
versioning. This adds no product-source changes or publication authority.

**Accepted verification addition, 2026-10-24:**
[Real Rust profile mount acceptance](client-example-profiles-rust-mount-brief.md)
requires a session-only probe with the actual server and optional Rust gem under
one qualified combined bundle. It adds no product paths to the 27-path packet.
Include the pending gate in final review, execute after review and before
integration, and repeat the matching-version subset on actual 0.30.1 preparation.
Owner1 owns dependency qualification; owner3 owns probe authoring after lead's
grant. No setup precedes owner0's final committed yield.

**Proposed simplification, 2026-10-24:**
[Client example profile simplification](client-example-profile-simplification-design.md)
responds to the user's request for less configuration: default generator version
to HaveAPI, make SDK versions optional with package-manager resolution at user
installation, derive the current schema after mount, and accept inline Rust
crate identity with optional pinned Git source. Existing file forms remain
optional exact-SDK overrides. Lead acceptance of the exact brief precedes
application edits in the isolated profiles worktree; the architect changes only
design records. vpsAdmin changes, release and default integration stay held. The previous
configuration investigation below records the current behavior.

**Additional investigation, 2026-10-23:**
[vpsAdmin Go/Rust example configuration](vpsadmin-client-examples-configuration-design.md)
shows the existing startup profile API, actual SDK names/TOML and source
evidence. This is explanation/design only: the API's HaveAPI upgrade, Go saved
input/version gap and Rust's unpublished-crate dependency hint are explicit
prerequisites. No vpsAdmin patch, SDK regeneration, publication or deployment
is authorized. Dependency verification and the release hold below are unchanged.

**Current user hold, 2026-10-23:** do not publish HaveAPI0.30.1. The user
requested our own dependency refresh after Dependabot PR3 and prohibited
accepting that PR. [Dependency-refresh addendum](dependency-refresh-addendum.md)
records current official versions, compatibility reasons, frozen patch state,
separate worktree ownership and new review/check gates. Successful master/main
integrations remain intact; their approval does not automatically authorize the
expanded dependency change or resume publication.

Current authorization, 2026-10-23: the user approved **HaveAPI 0.30.1
publication**, first merging the reviewed HaveAPI fixes into `master`, and
separately merging regenerated `vpsadmin-rust-client` into `main`. The exact
scope, source/backport/version ownership, compatibility, verification and
immutable-artifact recovery contract is
[release-0.30.1-plan.md](release-0.30.1-plan.md). This supersedes the older
development-only holds below for those specific actions. No Rust crate
publication/version change, live schema refresh or credential/setup change is
authorized. Architect owns design records; owner0 owns Git/mechanical metadata,
lead owns final prose/review/coordination, owner2 publication/recovery preparation
and owner1 independent original-artifact destination checks.

Downstream regeneration authorized 2026-10-23: see
[vpsadmin-client-regeneration-design.md](vpsadmin-client-regeneration-design.md)
for the saved API7.0 `vpsadmin-client` refresh using exact reviewed HaveAPI 090a.
Its original implementation used a separate development branch with unchanged
crate version/schema. The new authorization above permits main integration only;
the crate remains unpublished.

Current follow-up design (2026-10-22):
[release-followups-design.md](release-followups-design.md) defines bounded
registry-confirmation, JavaScript build/dependency/module-cycle and Rust
generator warning fixes on the separate `haveapi-followups` development
worktree. Published 0.30.0 source/tag/artifacts stay immutable; its original
development-only scope is superseded only by the 0.30.1 authorization above.
The older preparation
and examples sections below retain their historical scope; the follow-up brief
owns the new implementation boundaries and verification gates.

Status: implementation brief, 2026-10-22. Architect owns design; the lead owns
scope decisions, user-facing release prose and execution assignments. Registry
evidence is in [registry-readiness.md](registry-readiness.md).

The user approved the generated server client examples implementation, including
File system example removal. The accepted design is in
[api-doc-client-examples-plan.md](api-doc-client-examples-plan.md), with the frozen
implementation interfaces in [api-doc-contract.md](api-doc-contract.md).
Implementer0 owns shared server/context/profile/registry/templates/UI/highlighter
and Git; implementer1 owns JS/TS/Python plus callback typed lookup; implementer2
owns Go; implementer3 owns Rust. Missing Go/Rust profiles hide those languages
from the overview and all tabs; configured-invalid profiles fail startup. Rust
generator configuration uses its existing TOML format. Full saved SDK schemas
stay inside optional generator adapters and authorized live help bounds output.
The previous release baseline `08345b2` was reviewed and verified; new examples
require their own complete quick checks, committed final review and longer
verification. Preserve final release commit message exactly `Version 0.30.0`.
No publication or default-branch integration is authorized.

### Mounted URL acceptance correction

Installed rendered examples exposed duplicate mount joining in JS and Python
after baseline `27b4f8f895a4e5401357a402187c2a4590699aec` passed earlier core/CI
checks. The bounded corrective contract is
[api-doc-mounted-url-contract.md](api-doc-mounted-url-contract.md).
Server descriptors already contain actual origin-root paths; do not rewrite
server routes or fixtures. Implementer1 owns JS descriptor-vs-raw URL resolution
and diagnostics, implementer2 owns Python descriptor binding, and implementer0
owns shared Git plus the independent PHP launcher cleanup fix. Keep public raw
JS requests/discovery API-relative, origin restrictions and version selection
unchanged. Commit and quick-check the complete correction, run the same reviewer
on affected behavior/history, then retry real installed mounted acceptance.
No generator features, protocol/state migrations or publication are added.

### Python initial-login example correction

At reviewed head `ee150c8515aae399dc14e0fe9daefeb95a8bb17e`, installed wheel
acceptance found the Python renderer omitted advertised required token lifetime.
The runtime correctly rejected it before transport. The bounded correction is
[api-doc-python-login-contract.md](api-doc-python-login-contract.md): implementer1
owns Python required-field rendering and explicit fixture environment input;
validators/defaults/schema, JS behavior and continuation ownership stay unchanged.
Both Python variants need actual-schema/native-builder positive and missing-field
negative regressions, then committed affected-lane final review before installed
acceptance retry. No Python runtime expansion or fixture simplification is needed.

## Scope and baseline

Prepare HaveAPI **0.30.0**, without publishing packages, tags, official release
branches or GitHub releases and without integrating defaults. Use the registered
initiative branch `2026-10-22-haveapi-release`, based on live upstream master
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. It contains the rewritten JS clients,
Python client and Rust generator. Latest supported maintenance release is
`v0.29.12`, commit `355c2990a4bfd3940d3234cb2077ad0127f43551`; development VERSION
was still 0.29.0. Do not use that old development version as the changelog's
comparison baseline.

The eventual official minor-release branch is `haveapi-0.30`, with annotated
tag `v0.30.0`. Creating/pushing those refs belongs to the later explicitly
authorized release operation. Source preparation stays on the initiative branch;
integration into HaveAPI master requires separate explicit approval.

The user additionally identified the `vpsadmin-rust-client` repository. Its
actual Cargo package is **`vpsadmin-client` 0.1.0**, import `vpsadmin_client`.
Its source/release audit is a separate package, recorded in
[vpsadmin-rust-client-readiness.md](vpsadmin-rust-client-readiness.md). It has its
own release workflow and no runtime/package dependency on publishing HaveAPI
0.30 first. The crates.io credential must remain unread and unused during
preparation.

## Package interfaces and invariants

| Destination | Package | 0.30 contract |
| --- | --- | --- |
| RubyGems | `haveapi-client` | Shared version; publish before dependent gems |
| RubyGems | `haveapi` | Depends on `haveapi-client ~> 0.30.0` |
| RubyGems | `haveapi-go-client` | Same client dependency |
| RubyGems | `haveapi-rust-client` | New maintained release artifact; same dependency |
| npm | `haveapi-client` | One package: callback/async clients and declarations |
| PyPI | `haveapi-client` | First wheel/sdist release; import `haveapi_client` |
| Composer/Packagist | `haveapi/client` | Existing `vpsfreecz/haveapi-client-php` mirror |

All these packages use 0.30.0. The Rust runtime harness remains private:
`haveapi-runtime-tests`, version 0.1.0, `publish = false`. Runtime source is
embedded in the generator gem and copied into generated clients. Do not publish
or version-bump that harness as a HaveAPI package. A generated consuming Rust
crate has its own version and publication process.

`HaveAPI::Release::GEMS` in `utils/release/artifacts.rb` is the single maintained
gem catalog and publication order. Append `haveapi-rust-client` after the existing
gems, preserving `haveapi-client` first. Existing `Publisher` methods already
iterate this catalog for preflight, push and completion; add code only for an
identified missing behavior.

Preserve exact source/version/checksum manifests, same-run artifact reuse,
preflight-before-registry-write behavior, no rebuilding after approval and
conflict refusal. Rust artifacts must participate in the same checks, draft
assets and retry behavior. Retain relevant Rust generator dependency lock and
Rust tool versions in build provenance. Build/inspect the generator gem with its
templates, executable, dependency lock, documentation and embedded runtime source;
exclude private Cargo harness and acceptance fixtures.

## Independent implementation packages

### Package 0 — implementer0: versions, build and artifact contract

Exclusive application files: `Makefile`, `flake.nix` if needed for root release
tools, `utils/release/build.sh`, `utils/release/artifacts.rb`, existing
`utils/release/spec/release_spec.rb`, and version metadata/locks changed by
`make version VERSION=0.30.0`. This includes Rust generator version/gemspec and
tracked `clients/rust/Gemfile.lock` local versions/dependency requirements.
Do not alter unrelated lock resolutions. Fix the version target to keep that
tracked Rust lock coherent for future releases. No private runtime version bump.

Add Rust generator dependency preparation, build/copy and metadata inspection to
the broad release path. Root release verification must cover generator unit
tests, runtime feature tests and generated-client protocol acceptance; retain the
lightweight `test-rust-unit` versus longer `test-rust` split. Ensure the root Nix
release environment supplies the required compiler/formatter/native build tools,
and respect the component bundle/server bundle isolation already implemented.
Use existing component-specific invocations where that avoids duplicated setup.

Add meaningful regression tests: omitted/wrong Rust version or dependency must
fail metadata checks; missing or corrupt gem runtime/template contents must fail
artifact inspection; manifest includes the fourth gem and required provenance.
Packaged-generator smoke coverage must run from an isolated installed/extracted
artifact with no checkout source fallback, generate a saved fixture and confirm
the copied runtime. A dedicated new smoke helper/spec is permitted under
`utils/release/`; coordinate any new CLI entrypoint with package 1 first.

Acceptance: all maintained versions/dependencies/locks agree; four gems are built
and inspected; generated package works outside the checkout; broad release checks
exercise Rust; no crates.io operation or runtime dependency is introduced.

### Package 1 — implementer1: publication contract and release procedure

Exclusive files: NEW `utils/release/spec/publish_spec.rb`,
`doc/agent-instructions/releases.md`, `doc/agent-instructions/development.md`,
`clients/rust/docs/releasing.md`.
Use the generic catalog interface from package 0; do not edit its existing
`release_spec.rb`. `utils/release/publish.rb` needs no change unless tests expose a
concrete missing behavior. Own `.github/workflows/release.yml` only if a real
coverage/trigger gap needs a change; first coordinate with lead and verify every
imported action's current official upstream version if editing workflows.

Tests must independently prove that all four gems are preflighted; a conflicting
Rust gem prevents registry writes; missing gems publish client-first; matching
existing gems are skipped on retry; an unconfirmed Rust gem prevents GitHub
release completion. Use mocked registry/command boundaries, no external writes.

Update repeatable release documentation to include the fourth gem, pending
RubyGems/PyPI publisher setup, first-publication ordering, retained artifact
recovery and the fact that Rust runtime is embedded. Remove the obsolete claim
that broad release automation excludes Rust. Link to component packaging and
compatibility constraints. Registry-readiness evidence supplies exact current
registry prerequisites. Leave user-facing documentation edits uncommitted for the
lead's required prose pass, then commit during the serialized Git turn.

Acceptance: existing general publication logic handles the new gem with explicit
regression coverage; docs match actual workflow/artifacts; no unnecessary new
registry credentials, release workflows or publisher environments are introduced.

### Lead-owned prose and coordination

`CHANGELOG.md` and final release prose belong to the lead. Implementers provide
technical bullets and wait for the lead's prose pass before committing those
changes. Serialize Git/index/hook operations in the shared initiative worktree.
Implementer0 currently owns setup/hooks and metadata; architect has no active
setup command and made no hook-signature mutations. Worktree-add had created the
branch, checkout and portal registration before its post-checkout signature
failure; preserve those effects instead of recreating the branch blindly.

### Package 0b — preserve already released server example behavior

Lead accepted this prerequisite after comparison with `v0.29.12`. Implementer0
owns it after its release-tooling source commit, with serialized Git operations.
Keep these three provenance-bearing changes independently reviewable, in order:

| Released commit | Change and exact file boundary |
| --- | --- |
| `9b53aa87aec7a8d9c61eee2716e5520b3ecf743c` | Validate structured examples: `servers/ruby/lib/haveapi/{action,example,example_list,server}.rb`, `servers/ruby/spec/documentation/examples_spec.rb` |
| `fda2e33d32c249310812730b6b3096b99778918d` | Native syntax checks and renderer fixes: `servers/ruby/lib/haveapi/client_examples/{http,js_client}.rb`, `servers/ruby/spec/client_examples/syntax_spec.rb`, `flake.nix` |
| `f82ca890683d518496fdb57dc1c040589a0d585b` | Recursive/escaped PHP literals: `servers/ruby/lib/haveapi/client_examples/php_client.rb`, same `syntax_spec.rb` |

All three are present in the released maintenance ancestry and absent as
patch-equivalent changes from initial upstream master: `git log --left-right
--cherry-pick v0.29.12...origin/master` retains them on the maintenance side;
direct source diff confirms the missing behavior. The original upstream-source
provenance in their messages is respectively `7273615b3cdb67ba97fd0f6d3b8967e7c8ac7c2f`,
`508d60d2833799de41107f01f9a74010d7715a3f`, and
`d2549fb33204c3b5184c992a2ac03bc4b4e4393e`.

Prefer ordinary `git cherry-pick -x` when the owned checkout/index is ready.
Do not stash/reset the whole shared worktree or disturb lead CHANGELOG,
implementer1 docs/specs or pending metadata. If necessary, wait for their
serialized commits or apply only the recorded owned-file patches and make
equivalent separate commits containing the source SHA. `flake.nix` overlaps
package 0: retain its new root release tools and preserve this released patch's
Node/PHP additions to the server component shell. Patch 3 depends on the syntax
spec introduced by patch 2. No blind overwrite of the final flake is permitted.

These are already released behavior, not unconsumed obsolete changes to squash
away. No database migrations are involved. Verify the resulting server example
files against the released tree, allowing only independently reviewed new
changes. Focused checks: Ruby syntax/style; after `make doc`, server RSpec
`spec/documentation/examples_spec.rb` and
`spec/client_examples/syntax_spec.rb` in the declared shell with Node/PHP.
Use the watcher if setup/spec duration is uncertain. Final full server suite
follows committed-deliverable review. Add no new release highlight claiming
these old fixes are new; the release gate requires their preservation.

## Registry bootstrap and release ordering

Existing workflow: `.github/workflows/release.yml`. Trusted publisher tuple for
all HaveAPI registries: GitHub owner **vpsfreecz**, repository **haveapi**, workflow
filename **release.yml**, environment **release**. RubyGems needs this for all
four gems; the new gem can use a pending publisher. PyPI needs project
`haveapi-client` configured through a pending publisher if still uncreated.
Public 404 responses do not prove name ownership or reserve names.

Keep the protected `release` environment with required reviewers, tag restriction
`v*`, the `HAVEAPI_RELEASE_ENABLED=true` setup gate and existing PHP environment
secret `HAVEAPI_PHP_DEPLOY_KEY`. Registry account configuration is not established
by source inspection. Use implementer1's evidence for npm's current setup expiry
and direct-publish requirements. New publisher setup is an operator prerequisite,
not authorized by this preparation.

After future release approval: install final workflow/source on master and the
supported release branch, push annotated tag, build/test/retain all artifacts,
inspect and approve protected publish job. Preflight all registry hashes/PHP
mirror before writes. Existing flow uploads missing Python files, then publishes
Ruby client before dependent server/Go/Rust gems, npm and PHP mirror; GitHub
Release becomes public only after every destination is confirmed.

For downstream repository `vpsadmin-rust-client`, registry audit rechecked the
actual package **`vpsadmin-client`**, returning 404 at 14:55:09 UTC. Current
crates.io requires a token-based first publication before configuring OIDC for
an owned crate. Its tuple is owner `vpsfreecz`, repository
`vpsadmin-rust-client`, workflow `release.yml`, environment `release`; first
upload uses environment secret `CARGO_PUBLISH_BOOTSTRAP_TOKEN` in explicit
bootstrap mode. Token use is needed only for that later specifically authorized
bootstrap, never for HaveAPI's embedded runtime. The downstream readiness receipt
records source/CI/setup limits; the workflow is not dispatched during preparation.

## Compatibility, deployment and recovery

No database migration, service protocol version change, on-disk state conversion,
configuration pin change or production deployment is planned. Existing server
and clients keep HaveAPI protocol 2. Mixed-version support is preserved within
each existing component's documented protocol support; do not infer that a new
client implements every legacy convenience method.

JS remains one npm package and UMD browser bundle. `Client` and `CallbackClient`
are the same constructor/prototype/static helpers; callback callers keep their
existing entrypoint. `AsyncClient` is a separate opt-in Promise interface with
its own discovery/binding/authentication contracts. TypeScript declarations ship
in the package. Existing client-name/package imports remain valid.

Python is a new package requiring Python 3.11+, with synchronous and asynchronous
clients, dynamic API discovery, authentication continuation, paging and operation
tracking. Compatibility workarounds are explicit documented choices; do not
claim blanket equivalence with the Ruby client.

Rust generator requires Ruby >=3.2; generated clients use Rust >=1.95, edition
2024 and the recorded exact formatter, default async reqwest with optional
blocking support. Generated clients are self-contained and select an explicit
API version/schema snapshot. Runtime fixes require regeneration and release of
each consuming crate. Blocking clients must be constructed, used and dropped
outside an async runtime thread or within the documented owned blocking task.

Rollback selects earlier package versions; it cannot undo server actions already
executed. Registry publication is non-atomic: preserve accepted versions, tags,
draft assets and original manifest. Retry only exact retained bytes; conflicting
hashes stop. If source changes or original artifacts are lost, use a newly
authorized patch version. No tag movement/deletion or package replacement.

## Verification gates

Before final independent review: complete intended changes, run known quick
checks in the declared Nix environments, commit with Overcommit hooks enabled,
then give the reviewer the entire base-to-head series, diff and explicit
no-migrations conclusion. Review is required before long build/integration work.

Quick checks after dependencies are prepared:

- Root shell: `make release-check`; `bundle exec rspec utils/release/spec` and
  `python utils/release/spec/python_artifacts_test.py` (together `make release-test`).
- Rust component shell: `bundle exec rspec spec/unit` and focused launcher
  contracts documented in `clients/rust/spec/integration/README.md`; these do not
  start servers or Cargo. Run required Ruby style and hooks on changed files.
- Static workflow syntax/contract checks only if workflow changes; inspect version
  diff and locks. If a proposed quick command has uncertain duration, delegate it
  through the verification watcher rather than starting an unbounded local run.

After committed-deliverable review, use a fresh watcher for dependency setup,
`make release`, full `make test`, Rust runtime both-feature tests/Clippy and
generated-client acceptance, installed-artifact smoke checks, npm package-name
strict TypeScript smoke, Python installed wheel/sdist smoke and final manifest
verification. Release build needs clean tracked source and an empty `dist`.
Confirm packaging/MSRV with existing supported checks; do not silently expand
this release into a real-vpsAdmin database campaign or downstream deployment.
No `publish` helper, tag push, registry upload or default integration is a test.
