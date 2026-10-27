# Concrete TypeScript clients: investigation and proposal

## Accepted performance comparison follow-up — 2026-10-27

The user authorized implementation: performance tests must not fail merely
because a response differs between revisions. This simplified brief supersedes
the earlier proposed shared semantic validator, format 3, fixture tightening and
acknowledgement mechanism. Those additions are outside this task. Preserve all
existing timing and allocation limits selected by the user.

### Behavior and evidence contract

- Cross-revision response differences never cause failure, skipped comparison
  or a budget waiver. Replace the comparator's single response reference with
  references keyed by the **actual verified source SHA** of each observation.
  Both columns of baseline/self pairs belong to the baseline revision. Retain
  existing canonical response-distribution/occurrence-total stability checks
  only within each revision. Do not add a single-raw-body requirement or stricter
  serialization determinism; existing JSON map-order tolerance stays intact.
- Preserve current live functional/status/header/index checks, per-operation
  query/authorization/execution counters, proof lifetime, raw/canonical integrity
  checks, source/dependency/fixture provenance and replay validation. No expanded
  response-contract framework, fixture inventory, media-type field or validator
  extraction. Replay's existing limits remain documented honestly.
- Add per-case raw and canonical response-change diagnostics, baseline/candidate
  bytes per request, and absolute/percentage byte delta. Use occurrence-weighted
  values from the actual baseline/candidate pairs; self-pairs measure noise and
  do not bias the size comparison. Reports contain summaries, not raw bodies.
  Equal byte length does not establish correctness, and output growth neither
  fails by itself nor discounts measured time or allocations.
- Keep samples format **2**. New reports add `comparison` metadata containing
  `policy: per-revision-response-stability-v1`, `comparator_sha256` (the actual
  loaded `performance_compare.rb` bytes), and `samples_sha256` (the exact
  consumed `samples.json` bytes). Existing `budget_sha256` binds the budget.
  Preserve the original measurement `harness_sha256` from samples, including
  error reports after samples load. If measurement identity is unavailable,
  omit it rather than substitute current fixture/harness identity. A clean Git
  checkout is not required to identify a local test comparator by file digest.
- Existing wall/CPU thresholds, agreement/noise/adequacy rules, allocation
  budgets/fixed ceilings, watchdogs, batch/warmup/order policy, reference,
  genuine event pair and benchmark runtime/dependencies remain unchanged.
  Retain existing normalization behavior; add no response exceptions or automatic
  baseline/budget updates. Inconclusive timing remains visibly inconclusive.
- `endpoints.rb` saves complete samples before comparison. After final committed
  review, replay the retained actual master-failure `40529570313` samples with
  their matching budgets into a **new** report directory. Its original run and
  report remain failed historical evidence. Bind the new report to its new
  comparator/policy and original measurements; do not call it a new measurement
  or retroactively green CI. Missing/invalid retained samples are an evidence
  blocker, not permission to fabricate a pass. No new benchmark campaign is
  required solely to classify complete retained measurements under this policy.

### Ownership, files and acceptance

Implementer0 owns the entire bounded HaveAPI change: comparator and focused
specs/sample helpers under `servers/ruby/{benchmarks,spec/performance}`, minimal
`endpoints.rb` report attribution, `doc/performance.md` and
`doc/agent-instructions/development.md`. Update driver/workflow summary only as
needed to expose response changes beside performance results. Lead owns final
prose. No fixture expansion, Makefile/budget/reference/event/runtime change or
new configuration mechanism. Architect edits only this design file.

Quick acceptance covers differing stable revisions classified normally; changed
responses plus known timing/allocation regression still failing; within-revision
variation failing, including the second self-pair column; retained malformed
body/hash/count/counter/provenance rejection; additive diagnostic arithmetic;
actual comparator/input hashes and correct measurement identity on success and
error. Existing focused tests remain the correctness authority. Run declared
checks and normal hooks, commit, then obtain reviewer0's final general,
architecture and scope/policy review of the complete new range. The retained
sample replay follows review. No example execution, API call or benchmark run
is authorized by this brief for architect.

Create one new performance commit after the fresh HaveAPI master. The previous
five commits are already merged and must not be amended or rewritten. Retain
original review ranges and failed/new report identities. The earlier “merge it
all” approval preceded this material policy scope and does **not** authorize its
default integration; publish the feature only unless new approval is obtained.
This changes benchmark classification/reporting, not application API, schema,
persisted state or package behavior. No migration, generator/downstream repin,
release, deployment or session lifecycle action; rollback selects the previous
comparator without overwriting evidence. Lead owns plan/state/portal and final
publication/integration decisions.

## Approved five-repository integration — 2026-10-27

User approval, “all right, let's merge it all”, covers these five targets.
This appendix supersedes earlier statements that default integration lacks
approval; release, deployment and session lifecycle permissions are unchanged.
Lead owns the approval record and final integration gate. Recorded candidates:

| Repository / target | Exact reviewed candidate | Preparation owner |
| --- | --- | --- |
| HaveAPI / master | `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875` | implementer0 |
| vpsAdmin / master | `7456c7eaae11cee0c76a984b1386a94656510f88` | implementer1 |
| vpsadmin-go-client / master | `73f164dd5eeebfc494705ae27981d30872fa88c3` | implementer2 |
| vpsadmin-rust-client / main | `80be1c1a90b7009f8ddecf6a7fe042b506de8b42` | implementer2 |
| vpsadmin-typescript-client / main | `149c72f11acef67224a47ed77711a3abb805fbd4` | implementer3 |

Merge HaveAPI and the vpsAdmin exporter before the TypeScript SDK, which records
both producer identities. Those two producers are independently integrable:
the exporter retains its separate released HaveAPI 0.30.2 tooling and does not
require a new HaveAPI release. Go/Rust changes are documentation-only and can
integrate independently. A simple sequence is HaveAPI, vpsAdmin, Go, Rust, TS;
all target/hook preparation can proceed in parallel under the named owners.
The SDK's exact generator pin is `18b45aed`; retain that identity if no rewrite
is required. No registry publication, version bump, tag, trust activation,
production deployment, API action or session close is part of integration.

Existing review coverage is cumulative: [unified review](unified-generator-review.md)
covers the common capture/generators and optional server example profile;
[release disposition](release-review-disposition.md) closes the release findings
and binds the narrow final HaveAPI correction plus mechanical downstream repin;
[exporter disposition](postreview-disposition.md) binds the unchanged exporter,
its reviewed rebase and authentic capture; [final README review](vps-readme-member-focus-review.md)
binds the exact Go/Rust/TS heads and unchanged compiled fences/source. Complete
HaveAPI/exporter/Go/Rust/TS histories contain 5/1/1/1/3 coherent commits, no obsolete
approaches or repeated pin streams, and no new/transitional migrations. Existing
runtime/API/schema and persistent-state compatibility remain unchanged; there
is no coordinated production upgrade or data rollback requirement.

Reuse those conclusions only while fresh owner evidence confirms exact heads,
reviewed ranges, clean preparation and unchanged relevant inputs. Previous
checks/CI retain their recorded scope; they do not prove a changed head or a new
push pair. Lead assesses the actual integrated-head/default CI after claim
release. Do not launch a new source investigation or check campaign merely for
an unchanged fast-forward.

Stop on unexpected upstream drift, non-fast-forward target, dirty/uncertain
state, hook failure or an input/review identity mismatch. Reconcile outside the
merge claim. A clean patch-equivalent rebase may retain the five-target approval
only with old/new immutable ranges, range-diff/equivalence proof, applicable
checks and review-policy acceptance. A HaveAPI rewrite blocks SDK integration
until its exact-source pin/provenance/digest/manifest closure is reconciled by
its owner; unchanged source bytes can preserve content digests, not commit IDs.
Never relabel the saved schema's actual acquisition revision. Changed exporter
capture inputs need a separate affected assessment before any export or package
refresh. Material conflict resolutions, behavior/scope changes or target changes
require affected final review and renewed approval through lead.

Owners prepare unlocked; the merge executor acquires one repository only for
fresh target/feature/cleanliness checks, fast-forward plus normal hooks, ordinary
non-force SSH push and remote proof, then releases before CI or records. Preserve
feature refs, original reviews and exact old/new lineage. Partial integration
requires reporting the actual completed refs and remaining dependency gate;
never rewrite an integrated default to undo progress. Architect edits only this
appendix and performs no claims, merges, pushes, source changes, tests or CI.

## Accepted README lifecycle appendix — 2026-10-27

The user authorized implementation of the settled lifecycle examples. Extend
only the existing `README.md` in `vpsadmin-go-client` (implementer0),
`vpsadmin-rust-client` (implementer1), and `vpsadmin-typescript-client`
(implementer3). Lead owns final user-facing prose. Preserve the earlier design;
this appendix extends the preceding README work without changing SDK behavior.

### Narrative and example contract

- Keep the standalone, read-only existing-token connect/list-first-50 program.
  Follow it with location/template discovery, **one** of minimal/configured
  creation, completion guidance, inspection/hostname-only rename of the returned
  VPS ID, independent power alternatives, and deletion last. Integrate these as
  one lifecycle narrative. Action snippets reuse `api` and explicitly declared,
  caller-selected catalogue IDs; no selection framework or extra CLI parsing.
- Ordinary-member minimal creation supplies `hostname`, `location` and
  `os_template`. The server uses the current member as owner and selects a
  compatible node/pool. Do not hardcode deployment IDs or include admin-only
  node/user/pool inputs. Default `start=true` means creation starts the VPS.
- The configured creation is an alternative to the minimal call, adding
  `cpu=2`, `memory=2048` MiB (2 GiB), `diskspace=10240` MiB (10 GiB),
  `ipv4=1`, `ipv6=1`. CPU denotes capacity, not pinned/dedicated cores. Leave
  private IPv4 at its default zero and omit swap. Environment bounds, steps,
  quota and availability apply; these values are examples, not live defaults.
- IP values count allocations, which can be individual addresses or routed
  prefixes; they neither select exact addresses nor promise a prefix size.
  IPv6 allocation requires a location with IPv6 support. Minimal creation uses
  environment sizing and default one IPv4/one IPv6 allocation where supported.
- A receipt is not completed background work. Briefly require checking actual
  successful completion before dependent actions; an unfinished/timed-out wait
  is not success. Do not introduce a polling framework or pass generated TS raw
  receipts to `AsyncClient.waitForCompletion`. Validate absent/null output and
  the returned VPS ID before reusing it throughout later snippets.
- Show start, stop and restart as separate choices, not a sequential script;
  start applies to a stopped VPS, and default stop/restart are graceful.
  Member deletion uses the default soft/scheduled behavior. Explain that the
  request does not immediately erase disk data; omit `lazy=false` and admin
  inputs. Examples are documentation, not authorization to execute VPS actions.

### Confirmed SDK calls

| SDK | Catalogue discovery | Create inputs and lifecycle calls |
| --- | --- | --- |
| Go | `Location.Index.Prepare()` / `NewInput().SetHasHypervisor(true)`; `OsTemplate.Index.Prepare()` / `NewInput().SetLocation(locationID)`; then `Call()` | `Vps.Create.Prepare()` / `NewInput()` with `SetHostname`, `SetLocation`, `SetOsTemplate`; configured adds `SetCpu`, `SetMemory`, `SetDiskspace`, `SetIpv4`, `SetIpv6`. Power/delete use `Vps.{Start,Stop,Restart,Delete}.Prepare()`, `SetPathParamInt("vps_id", vpsID)`, `Call()`. Use actual generated argument types; no assumed Go `int64`. |
| Rust | `location().index().has_hypervisor(true).send().await?`; `os_template().index().location(location_id).send().await?` | `vps().create().hostname(...).location(...).os_template(...)`; configured adds `.cpu(2).memory(2048).diskspace(10240).ipv4(1).ipv6(1)`; finish `.send().await?`. Power/delete use `vps().{start,stop,restart,delete}(vps_id).send().await?`. |
| TypeScript | `location.index({params:{has_hypervisor:true}})`; `os_template.index({params:{location:locationId}})` | `vps.create({params:{hostname,location,os_template,...}})`; configured numeric keys as above. Power/delete use `vps.{start,stop,restart,delete}({path:{vps_id:vpsId}})`. Await calls and preserve existing error/optional-output handling. |

Keep existing authentication: Go/Rust use unversioned bases; TypeScript uses
the versioned base and public `runtime.authenticate('token', {token})`.
Catalogue results guide caller selection; do not blindly choose the first row.
Source basis: vpsAdmin `api/lib/vpsadmin/api/resources/{vps,location,os_template}.rb`,
`api/models/transaction_chains/{vps/create,vps/soft_delete,ip/allocate}.rb`,
`api/models/cluster_resource_use.rb`, and node `commands/vps/resources.rb` /
`utils/zfs.rb` establish defaults, member behavior, units and allocation semantics.

### Verification, history and compatibility

Each owner compiles the exact final fences against the actual SDK in disposable
consumers, using small typed wrappers only for snippets with declared context.
Compile only: no example execution, API call, actual VPS mutation, regeneration,
schema capture, full suite, release, registry operation or deployment. Preserve
the standalone quickstart and check the lifecycle narrative/links directly.
Use normal owning documentation amendments and hooks, then independent final
general documentation/history review of the complete final ranges. Lead retains
old/new immutable reviewed ranges and coordinates explicit-lease feature
publication. No default integration is authorized. No source, schema, runtime,
package metadata, pin or workflow changes; no migration, deployment ordering or
state-recovery effect. Reverting the documentation is sufficient rollback.
Architect changes only this design file; lead owns plan/state/portal updates.

## Authorized release-workflow preparation — 2026-10-26

Prepare publishing support, **do not make a release**. Inspected HaveAPI
`e6d4f797fc92090fff265585196970e6b017003f` and generated SDK
`50a9602cbc30ca0c18ace092ad9750439e9cf82a`. Keep the identities
`haveapi-typescript-client` (Ruby generator gem) and `vpsadmin-typescript-client`
(npm SDK). This supersedes the earlier exclusion of the generator from registry
release artifacts. No version bump, tag, release, registry upload/settings,
default-branch integration or deployment is authorized. No runtime, generated
API, schema or capture changes. Use the existing release machinery and small
repository-specific checks, not a new release framework.

### Package A — HaveAPI, implementer0

- Own `utils/release/{artifacts.rb,build.sh,typescript_smoke.rb,spec/*}`, necessary
  existing CLI/publisher glue, `.github/workflows/release.yml`, `Makefile`,
  `clients/typescript/haveapi-typescript-client.gemspec`, its README and
  `doc/agent-instructions/{development,releases}.md`. Existing publisher and
  recovery behavior should work through the registry list; avoid a second TS
  publication path. No performance files or root-flake changes.
- Append the TS gem to `Release::GEMS`; publish the shared Ruby client first,
  then dependent gems. Include TS in exact artifact inventory, all-registry
  preflight, hashes, retained assets, conflict/matching-version checks and final
  confirmation. Keep shared `VERSION`, the existing `~> VERSION` Ruby-client
  requirement and current Ruby >=3.2 floor. The Ruby-client gem must contain the
  shared `haveapi/schema` implementation. Future coordinated version preparation
  must release that implementation with the generator; an older same-range gem
  does not acquire the new capability merely because it satisfies the range.
- Retain the prepared, ignored `clients/typescript/Gemfile.lock` in the existing
  release manifest (ten locks total). Validate its generator/shared-client
  identity and dependency; update `make version`'s local-lock handling if needed.
  Do not track a library lock or require a local bundle when verifying retained
  artifacts in the tools-only publishing job. Source-only `check-clean` stays
  usable before dependency preparation.
- The current gemspec omits `Gemfile`, `Rakefile` and its own gemspec, although
  `Generator.source_files` hashes them. Package those three files along with
  executable, all Ruby code/templates, README and existing MIT license. Inspect
  their exact bytes and executable declaration; reject missing/extra/corrupt
  release content. Do not change the source-digest definition to hide omissions.
- Add one extracted-gem smoke using the retained TS AND Ruby-client gems in a
  disposable directory. Clear ambient Ruby/Bundler load-path overrides, prove
  loaded generator/shared files and versions belong to those artifacts, compare
  their source identity with the candidate, run the packaged executable's saved
  fixture generation and `--check`, and exercise emitted modules in a strict
  consumer. Use the existing compiler tooling and actual supported published JS
  runtime `haveapi-client@0.30.2`; any consumer dependency preparation happens
  before protected publication. Source VERSION `0.30.0` is not that runtime.
  Do not load generator/schema code from the checkout as a packaging fallback.
- Existing build-only/tag/release-branch/environment gates remain. Add TS and
  shared-schema paths to release-validation triggers; retain normal tests and
  build-before-approval, upload-by-original-artifact behavior. Update docs from
  four to five gems and remove claims that TS is excluded/source-only. Keep
  source instructions valid and describe packaged use as available once released,
  without inventing a first released version.

### Package B — generated npm SDK, implementer3

- Own `.github/workflows/release.yml`, `tools/check-package.mjs`, a compact
  release preflight/receipt helper under `tools/` with focused tests under
  `test/`, package scripts/metadata and `docs/releasing.md` linked from README.
  Later own the exact producer pin/identity and ordinary regeneration. Keep
  `private: true`, version `0.0.0` and license undecided. Do not silently assign
  MIT because the generator uses MIT. Preserve existing npm/repository name,
  ESM exports, runtime peer `0.30.2`, saved schema/provenance and lock graph.
- One conventional workflow: build/validate on branch pushes, PRs, manual
  build-only dispatch and `v*` tags. GitHub-hosted runner, pinned Nix shell,
  `npm ci --ignore-scripts`, existing type/consumer/unit checks and archive check.
  Obtain the exact recorded public HaveAPI revision in a separate checkout;
  explicitly pass it to offline `tools/regenerate --check`. Acquisition belongs
  to workflow setup; the regeneration driver still never fetches or discovers
  sources. The existing Nix Node/npm versions satisfy trusted-publish minimums;
  no setup-node action, new dependency framework or toolchain bump is needed.
- Build once, pack with scripts disabled after the build, then validate that
  exact tarball. Add an existing-archive mode to `check-package.mjs`, preserving
  its normal local mode, full module inventory, extracted strict declarations
  and executor checks. Retain the tarball and small JSON receipt binding
  package/version, source commit, tag if present, filename and archive hash/SRI.
  Use the immutable Actions artifact ID between jobs. Publish must neither
  rebuild nor repack; run no dependency installation/package scripts after
  acquiring publishing authority.
- Publishing runs only for a pushed tag in
  `vpsfreecz/vpsadmin-typescript-client`, after successful validation, with
  `environment: release` and job-only `id-token: write`. Leave repository
  activation variable `NPM_RELEASE_ENABLED` unset; tag preflight fails clearly
  unless it is `true`. Require a tag `vX.Y.Z` exactly matching a non-placeholder
  stable package version, matching package-lock identity, a commit on `main`,
  `private` removed/false, chosen license metadata plus license file, canonical
  publishing repository and expected package identity. Ordinary build-only
  validation must still pass with today's private/unlicensed `0.0.0`.
- Setup docs require `release` environment reviewers and tag restrictions,
  exact npm publisher fields and deliberate activation only when prerequisites
  are complete. Preserve the archive's verified name/version/hash before
  `npm publish <retained.tgz> --ignore-scripts --access public` to the explicit
  npm registry. No `NODE_AUTH_TOKEN`, npm token, token fallback or login step.
  Registry publication is not exercised by this initiative. No GitHub Release
  automation, dist-tag-management subsystem or reusable release framework.
- Minimal recovery: retain the approved original artifact; retry only the
  failed publish job after reconciling registry identity/integrity. Never
  overwrite an existing artifact on rerun, reupload blindly, replace a version,
  move its tag, or automatically rebuild an expired/missing accepted archive.
  Describe uncertainty and manual diagnosis; do not implement generalized
  cross-run recovery orchestration.

### Registry setup facts and action pins

Official documentation checked 2026-10-26:

- [RubyGems trusted publishing](https://guides.rubygems.org/trusted-publishing/)
  supports a pending publisher for a new gem. Configure gem
  `haveapi-typescript-client`, owner `vpsfreecz`, repository `haveapi`, workflow
  `release.yml`, environment `release`; reusable-workflow repository fields stay
  blank. First successful upload creates the gem and converts its publisher.
  This is setup documentation, not an instruction to perform the setup now.
- [npm trust prerequisites](https://docs.npmjs.com/cli/v11/commands/npm-trust/)
  require an existing package. No documented pending-new-package equivalent was
  found. First npm publication/bootstrap and ownership must therefore be
  resolved separately by the maintainer before enabling this workflow; do not
  claim OIDC can bootstrap the nonexistent SDK or add a credential workaround.
- [npm trusted publishing](https://docs.npmjs.com/trusted-publishers/) requires
  npm >=11.5.1/Node >=22.14, hosted runners, matching repository metadata and
  exact publisher fields. For the SDK use owner `vpsfreecz`, repository
  `vpsadmin-typescript-client`, workflow `release.yml`, environment `release` and
  direct-publish permission. A new trust configuration expires without a first
  publication within two days, so configure it near an authorized release.
  Public-package/public-repository OIDC publication supplies provenance.

Latest official upstream release/tag commit pairs were checked via GitHub's
release and Git-ref APIs. Pin these immutable commits in edited workflows:

| Action | Release | Commit |
| --- | --- | --- |
| actions/checkout | v7.0.1 | `3d3c42e5aac5ba805825da76410c181273ba90b1` |
| actions/upload-artifact | v7.0.2 | `cf430e030ddbb5b0abf93d22962f4752f3646cd9` |
| actions/download-artifact | v8.0.2 | `9000827ccba6bdab643e8b6fd33ac0654aef8333` |
| cachix/install-nix-action | 31.11.3 | `75c75c31ebece974e48ebc36b4ad125bd97bd97b` |
| rubygems/configure-rubygems-credentials | v2.1.0 | `dc5a8d8553e6ee01fc26761a49e99e733d17954a` |
| pypa/gh-action-pypi-publish | v1.14.3 | `7245906fb61fa33a13554f9d5fb856fe61758086` |

All except Nix already match HaveAPI's workflow. Nix 31.11.3 is the compatible
installer patch from 2.35.3 to 2.35.4 with certificate fixes; its composite Linux
action inputs are unchanged. The SDK needs only the first four actions. This
does not authorize unrelated workflow/action churn.

### Dependencies, checks and compatibility

Both packages can begin independently in their own repositories. HaveAPI Git,
index and normal-hook windows remain serialized through lead. Package A's
gemspec change changes the generator source digest, so package B's final pin,
shared identity and ownership manifest refresh waits for the final committed
producer. Re-run ordinary offline generation/check; emitted API files and
coverage should stay identical. No vpsAdmin export or database repetition.

Quick checks: release inventory/lock/version/packaged-file tests and focused
Ruby lint; SDK preflight negative fixtures (private, placeholder/mismatched
version/tag, missing license, wrong identity/hash), workflow syntax/permissions,
existing strict type tests and build-only check behavior. No real registry
mutation in tests. Use the existing Nix shells. After all substantive changes
are committed and quick checks pass, obtain mandatory affected final review of
complete branch history, publication gates, artifacts and docs. Then perform
bounded build-only retained-gem/extracted-generator and exact npm archive
consumer checks, plus existing published-0.30.2 loopback acceptance as affected.
Long/uncertain runs go through the assigned watcher. Earlier runtime/schema
results remain evidence for their actual revisions, not release-workflow proof.

Keep HaveAPI release enablement one reviewable logical commit after generator
and generated-docs behavior. Consolidate follow-up release fixes and repeated
SDK pins; the downstream initial commit remains its owning package history
unless lead establishes a real consumed boundary. No migrations, runtime
deployment ordering or on-disk format change. Existing released artifacts and
old tagged workflows keep their own recovery rules; never reinterpret old
four-gem manifests with new five-gem code. Before any future publication select
an authorized new version/release branch; current source `0.30.0` is not release
readiness. License, first npm bootstrap/ownership and external trusted-publisher
setup are explicit pending prerequisites, not implementation blockers.

Performance coordination (lead accepted): retain the already reviewed generic
SDK-version overview in `e6d4f797`; the paused conditional-copy repair is dropped.
The prior exact pair failed solely on an intentional 12-byte HTML prose change;
it made no timing-pass claim. Optional TS dependency/profile/tab contracts stay
unchanged. Assess the next genuine push pair normally. Do not alter baseline,
refs, comparator, budgets or substitute a representative-ancestor pass. Owner1
owns that evidence; release owners do not duplicate its investigation.

## Authorized unified capture and generated TypeScript examples — 2026-10-26

The user authorized implementation of the accepted plan. All three generators
must document and implement `fetch -> offline generate`; there is no `describe`
command. Add generated TypeScript examples to Ruby-server documentation alongside
existing Go/Rust profiles, keeping dynamic TypeScript examples separate. This
section supersedes earlier stdlib-only-distribution and TS-no-fetch assumptions.
The resource/action module layout and generated client/executor API stay intact.
Design evidence: HaveAPI `fae5508aca9def6b1388d298aab898b0b9ce832c`, generated client
`7bc0f83be9dfee42bd09e2228d799a464eef7ff2`. Source generator VERSION is `0.30.0`;
supported published JavaScript runtime remains exactly `0.30.2`.

### Shared schema, capture and CLI contracts

- One implementation in the existing Ruby-client package:
  `clients/ruby/lib/haveapi/schema.rb` and `schema/{snapshot,capture,fetch_command}.rb`,
  namespace `HaveAPI::Schema`, with its own `Error`. No new gem/framework.
  Loading `haveapi/schema` for offline snapshot/digest operations uses stdlib only,
  compatible with the Ruby client's >=3.0 floor. HTTP/client dependencies load
  lazily when capture runs. Do not require the full dynamic Ruby client during
  offline snapshot loading.
- `Schema::Snapshot` owns `load`, `validate`, `canonical`, `sha256`, `sanitize`,
  `from_description`, `from_envelope`, version/endpoint/path validation. Preserve
  format 1's exact seven keys, canonical sorted UTF-8 JSON/two spaces/final LF,
  meaningful array order, mounted APIs and explicit numeric API version.
  Capture sanitizes structural prose/protected defaults, preserving real
  Custom/default/choice keys; loading validates without rewriting saved data.
  Use the reviewed TS contextual endpoint checks on capture AND load. Existing
  reviewed Rust/TS snapshots must retain their bytes/hashes. Authentication
  discovery remains in snapshots; each generator keeps its own emission policy.
- Existing Rust/TS `Snapshot` constants remain thin compatibility facades,
  including existing helpers and native error types; delegate rather than copy.
  Rust's `fetch`/`from_envelope` entrypoints remain callable. Generator-specific
  types/layouts/naming/ownership validation stays outside the common core.
- Shared `Capture.fetch(url:, api_version:, profile:, basic_user: nil,
  basic_password: nil, token: nil, diagnostics: [])` returns a validated snapshot.
  `FetchCommand.run(argv, out:, err:, command_name:)` owns common option parsing,
  environment-secret resolution and saving, returning CLI status. All three
  language CLIs delegate their `fetch` subcommand to this same implementation.
  Reject bad arguments before network/output mutation. Preserve old output on
  failure; save validated canonical bytes by atomic file replacement, rejecting
  symlink destinations. Require the output parent to exist (README creates it).
- Common command: `haveapi-LANGUAGE-client fetch URL --api-version VERSION
  --profile LABEL --output FILE`. URL must already end in the selected
  `/vVERSION/`, including any mount prefix; do not select a server default.
  Public capture is default. Auth choices are mutually exclusive:
  `--basic-user USER --basic-password-env ENV_NAME`, or `--token-env ENV_NAME`.
  Missing/invalid credentials fail before dispatch. Environment variable names,
  not secret values, appear in argv. Profile is a nonsecret coverage label,
  never an authentication mechanism or completeness claim.
- Reuse the existing RestClient OPTIONS transport and Ruby token-header policy:
  TLS verification, no redirects, 10-second connection/30-second read timeout,
  JSON accept, no retries. Public/Basic requests target the exact version URL;
  Basic uses HTTP Basic credentials. Token capture first obtains anonymous
  discovery at that SAME mounted version endpoint, requires the advertised
  HaveAPI token provider and valid header, then repeats OPTIONS there using the
  supplied existing token. No guessed header, API-root traversal, query token,
  token login/acquisition/renewal, OAuth or custom auth framework. Missing token
  discovery is a clear failure. Require successful HTTP and `status: true`,
  protocol major 2 and coherent version/mount before saving. Save only the final
  authorized description, not a merge of anonymous/authenticated surfaces.
  Never add request credentials/headers to snapshot/provenance; diagnostics
  must not expose secrets, response bodies, credential URLs or raw exceptions.
- Common generation: `generate --schema FILE --api-version VERSION --output DIR`.
  Rust retains `--config`; Go retains `--module`/`--package`; Rust/TS retain
  their `--check`. No new Go ownership/check subsystem is required. New Go mode
  validates the common snapshot, converts its description to the existing
  symbol-key contract and calls `Generator.from_description`, `generate`,
  `go_fmt`; no discovery or generated API/runtime change. Retain Go's old
  positional URL/destination invocation, optional `--version` server-default
  behavior and raw `--basic-password` only in that legacy mode. Do not weaken
  old authentication or silently reinterpret its arguments.

### Distribution, source identity and downstream loading

Go/Rust already depend on Ruby `haveapi-client`. TS adds that gem dependency and
an explicit `gem 'haveapi-client', path: '../ruby'` component Gemfile entry.
No fifth published gem: TS remains source/local-gem distributed. Use the existing
version convention without inventing a release; registry consumers need a release
actually containing the shared API, with its minimum dependency floor set through
normal release preparation. A version range alone does not prove this unreleased
API exists; fail clearly on missing capability, never fall back to another source.
Retain Go/Rust/TS Ruby floors; the shared code must run on Ruby >=3.0.

Generic source instructions from the HaveAPI root use the component bundle:
`BUNDLE_GEMFILE="$PWD/clients/typescript/Gemfile" bundle install`, then the same
prefix with `bundle exec ruby clients/typescript/bin/haveapi-typescript-client
fetch ...` or `generate ...`; use the analogous Go/Rust paths. The root Gemfile
contains development tools only and cannot substitute for this dependency setup.
Fetch needs the prepared HTTP dependencies; offline generation never installs or
contacts anything. Document setup honestly rather than claiming a standalone
dependency-free packaged CLI.

Expose `Schema.source_identity` with stable package name, actual Ruby-client
VERSION and shared-source SHA256. Hash shared entrypoint/files and the version
file under stable logical relative names, excluding checkout paths/timestamps.
TS/Rust generator source digests must bind that identity in addition to their own
sources, so moving snapshot code cannot make changes invisible. Keep Rust's
existing dependency-lock provenance; it does not replace proof of loaded code.

For the exact-source downstream TS driver, deliberately pass both verified
`clients/ruby/lib` and `clients/typescript/lib` via `ruby -I` for digest AND
generation. Assert the loaded shared source belongs to that exact checkout;
expand dirty/untracked input checks to shared schema files and version identity.
This explicit source selection preserves stdlib-only offline regeneration without
adding a Ruby bundle to the client's Nix environment. It is not an implicit
fallback. Update driver/tool hashes, source pin/digest and owned manifest together;
this is substantive tooling work, not a pin-only edit. Existing schema/provenance
and exporter lock remain unchanged; no vpsAdmin export or DB repeat.

### Generated TypeScript documentation contract

- Minimal profile: `typescript: {package_name: 'widget-client', package_version:
  optional, snapshot_path: optional, generator_version: optional}`. Validate
  ordinary scoped/unscoped npm names and optional concrete SemVer; no registry,
  Git/path source, custom factory or package-resolution subsystem. Omitted package
  version means package-manager selection, not verified availability. Do not
  advertise the private unpublished vpsAdmin package as installable from npm.
  Its root already exports canonical `createClient`; no custom factory is needed.
- Server renderer ID `typescript-generated`, label `TypeScript (generated)`,
  syntax `:typescript`; existing dynamic TS callback/async IDs are unchanged.
  Optional generator loads only for configured profiles. Missing dependency,
  bad fields/snapshot/version or incompatible adapter fails startup with current
  atomic profile-finalization behavior, not a partially usable mount.
- Generator owns `HaveAPI::TypeScriptClient::Documentation` in `documentation.rb`:
  `from_description(description:, api_version:, protocol_version:, mount_path:,
  package_name:, package_version: nil)`, `from_snapshot(snapshot:, package_name:,
  package_version: nil)`, `resolve(resource_path:, action_name:)`,
  `render(kind:, context:, mode: :async, auth_method: nil, auth_description: nil)`.
  Return existing `{status: :code, code:}` or `{status: :limitation, reason:}`.
  Build frozen full IR/alias indexes using existing Snapshot/IR/Naming, no second
  allocator, emitter call or server-gem dependency. Profile initialization uses
  complete post-mount structural schema or the exact saved SDK snapshot.
- Preserve the server's private `StructuralSchema.copy` boundary: it strips ALL
  defaults, prose and examples, unlike portable capture. Do not replace it with
  common capture sanitization. Shared adapters are frozen. HTML requests read
  only their authorized Context/sample, using private IR solely for canonical
  name/contract lookup; no files, capture, generation, compiler or network there.
- Require the action to exist in authorized help and the saved SDK. Compare
  version, mount-normalized route/method, auth/blocking, IO layout/namespace/format,
  metadata namespace, and every used parameter's type/requiredness/nullability/
  association. Require inputs/metadata required by BOTH contracts; do not fill
  hidden defaults. Missing/stale/unrepresentable samples produce limitations
  without exposing private names or fields. Unrelated live additions need not
  invalidate an otherwise compatible saved action.
- Complete snippets import public `AsyncClient` and configured-package
  `createClient`; bind `new AsyncClient(context.version_url)` to
  `createClient({execute: spec => runtime.request(spec)})`. No constructor version
  option, added transport or runtime change. Public snippets need no setup.
  Protected snippets use existing runtime authentication for advertised Basic
  or existing HaveAPI token only; compare saved/live provider/header and use
  environment credentials. No login/renewal/OAuth extension. Mounted/version-root
  authentication routing must pass the real 0.30.2 acceptance.
- Map sample path order and input wire names through IR placeholders/emitted
  names; retain output wire names and canonical alias resolution. Use existing
  sample DSL and generated `{path,params,meta}` shape, without inventing a new
  metadata format. Missing required metadata is a limitation. Preserve omission,
  null/false/zero/empty; reject unsafe IDs, invalid JSON, list input and structured
  Custom query values. Access only authorized sample output fields with optional/
  null/unknown guards. Show preserved data/meta/envelope/httpStatus and rejected
  errors; no casts to fabricated DTOs, automatic retry or completion claim.
  Raw receipts never enter `waitForCompletion`.

### Independent implementation packages

1. **Owner0 — shared core/capture:** new `clients/ruby/lib/haveapi/schema*`, new
   focused `clients/ruby/spec/schema_*_spec.rb` and dedicated fixture helpers.
   Reuse existing auth header policy; any necessary tiny Ruby auth helper change
   stays here. Own shared API/source-identity contract and focused tests, not
   generator wrappers, root build files or server profiles.
2. **Owner1 — generator integration and generic guides:** Go/Rust/TS CLI/bin,
   Snapshot wrappers, component Gemfiles/gemspecs, TS/Rust digest methods and
   focused CLI/snapshot/digest specs. Sole owner of root `Makefile`, any root
   dependency/test registration, `utils/release` package-smoke adjustments,
   `doc/agent-instructions/development.md`, three generator READMEs and root
   README. The root README distinguishes `clients/js` dynamic JS/TS discovery
   runtime from `clients/typescript` concrete saved-schema generator. Generic
   guides include capture/auth/save/generate with example.test/widgets; service
   instructions belong in vpsadmin-client repositories. No release-list expansion.
3. **Owner2 — TS documentation adapter:** new
   `clients/typescript/lib/haveapi/typescript_client/documentation.rb`, new
   `spec/unit/documentation*_spec.rb`, `spec/documentation/**` fixtures/harness,
   and `clients/typescript/docs/documentation.md`. Own actual rendered-snippet
   compile/runtime acceptance, reusing generated fixtures/public runtime. Do not
   edit owner1's generic README/wrapper/spec_helper or server bridge.
4. **Owner3 — server bridge, then downstream:**
   `servers/ruby/lib/haveapi/documentation_clients.rb`, new
   `client_examples/ts_generated_client.rb`, focused server profile/HTML specs,
   server-only support helpers and `doc/client-examples.md`. After producer
   commits, own generated-client `tools/regenerate`, source pin/tool hashes,
   regeneration, dependent checks and service README. Server settings need the
   new optional generator before use; normal servers gain no mandatory generator.

Shared-file rule: owner1 alone edits existing component `spec_helper.rb`, Rakefiles,
root Makefile/build registration and dependency manifests; owner3 owns existing
server spec helpers/manifests. Owners2/0 add scoped helpers and request shared
registration through those owners. Nonoverlapping edits may proceed concurrently;
overlaps and all Git/index/normal-hook windows are serialized, and other writers
pause for hook isolation. Lead assigns execution/commit windows. Adapter/server
work can proceed against these interfaces while owner0/1 complete shared capture.

### Acceptance, review and recovery

Quick checks: common CLI option/auth parity and failure-before-write; format-1
golden bytes from existing TS/Rust snapshots plus generic mounted fixture; private
default sanitization/data-key preservation and secret-safe diagnostics; bounded
OPTIONS/auth request selection, no redirects or token actions; offline generation
without network. Go old/new same-description generated output and aliases/auth
must agree. Test exact shared-source identity, source/extracted-package loading,
dirty shared-input refusal and unchanged existing generated contracts.

Adapter/server quick checks cover optional dependency isolation, unknown/missing
profile/snapshot/version, atomic mount failure, hidden actions/fields/defaults/
samples, stale saved SDK and untouched dynamic tabs. Compile ACTUAL rendered
complete snippets against the ACTUAL generated generic fixture with TS6,
NodeNext/ES2022 strict/exactOptionalPropertyTypes/noUncheckedIndexedAccess/
verbatimModuleSyntax. Use targeted lint, ordinary hooks and existing focused
component commands; owner1 registers only the necessary checks.

Construct final generated downstream package, committed inputs and passing quick
checks before mandatory final affected review of complete history (no migrations).
Then run bounded local public-runtime 0.30.2 capture/snippet wire acceptance at
root and mounted URLs: public/Basic/existing-token, aliases/nested IDs, metadata,
success/error/null/filtered output. Run extracted generator and generated-client
archive consumers to prove shared dependency and module completeness. No production
calls, broad benchmark campaign or DB/export repeat; existing performance evidence
retains its old source scope, and lead handles required new-head CI.

Rollback restores matching generator/shared library/downstream pin+manifest pair;
no persisted state or runtime wire change. Remove new TS profile settings before
rolling back to an older server; old profiles/dynamic clients remain supported.
Feature branches only. No releases, default merges, npm publication, deployment
or lifecycle action is authorized by this brief. Architect edits design only.

## Authorized module layout change — 2026-10-26

Implement the user's requested resource/action file split in the generator, then
regenerate the client. This supersedes the three-file emission layout, not its
API or executor contract. Inspected sources: HaveAPI
`dcbd537f325ce4b8a8d0afb1a398763260806c87`, client
`33bc6f9e1daa08539f3f3aeec5a4b542e2c5f49d`. vpsAdmin and its saved schema,
provenance and exporter lock are unchanged; no schema export or DB repeat.

### Settled files and dependency direction

- Keep `index.ts`, `api.ts`, `runtime.ts`; add `types.ts`. `api.ts` contains only
  API/schema constants, top-level resource imports, `createClient` composition
  and type re-exports. It must contain no action DTOs, descriptors or nested
  resource implementations. `index.ts` retains its existing public surface.
  `types.ts` explicitly re-exports every existing resource/action type from its
  owning module; it contains no declarations, descriptors or runtime exports.
- Each resource owns `resources/<accessor>/resource.ts`; nested resources own
  `resources/<parent>/resources/<child>/resource.ts`, recursively. Each canonical
  action owns its resource's `actions/<accessor>.ts`, e.g.
  `resources/network/actions/index.ts`. Fixed `resources`/`actions` directories
  separate schema namespaces; there is no action barrel named `index.ts`.
- Use existing ASCII `accessor_name` spellings for path segments, preserving
  case; do not derive paths from URLs or public PascalCase export names. Validate
  all planned paths before adding them to the output map: safe relative paths,
  no traversal/backslash/control characters, no file/directory conflicts, and
  no duplicates after ASCII case folding. Fail with both original schema paths
  on collisions; never overwrite, silently suffix, or modify public names.
  Derive paths during emission from the frozen resource tree; no new IR fields
  or parser naming rules are needed. Aliases receive no additional modules.
- An action module owns its unchanged Path/Input/Output/GlobalInput/GlobalOutput/
  ObjectInput/ObjectOutput/Options exports, one private request descriptor and
  an internal exported binder `createAction(execute)`. Preserve optional/default
  arguments and the exact method return type. A resource module owns its existing
  Resource interface and internal exported `createResource(execute)` factory;
  it composes immediate children and canonical action binders, including aliases.
  Descriptor/operation coverage stays one per canonical action, with every alias
  still callable. Internal factories are not re-exported by public barrels.
- Use explicit static relative `.js` specifiers for ESM/NodeNext and `import type`
  for types. Runtime dependency direction is api -> resource -> child resource /
  action -> shared runtime. No action/resource imports from api/index/types, no
  dynamic imports or discovery, and no runtime cycles. The type-only barrel
  re-exports explicit public symbols, avoiding duplicate factory exports.
  Keep current root and `generated/api.js` public type/value imports working.
  The client package currently exports only `.`; do not add package subpaths.
  New individual module paths are generated organization, not a new stable
  package export promise. Document browsing them without changing root examples.

`Emitter.new(ir, {runtime_import: 'haveapi-client'}).files` remains a pure sorted
UTF-8/LF map; templates load outside emission and frozen IR stays untouched.
Keep `runtime.ts` behavior unchanged. Version-relative paths, integer/input/query
validation, metadata, receipts/errors, one-send behavior, authentication exclusion
and coverage remain intact. Generated bytes and source digest necessarily change;
schema bytes and declared operations do not. Current 151 resources/519 canonical
actions imply 151 resource modules and 519 action modules plus four root files.

### Execution ownership and dependencies

1. **Implementer2, complete emitter package:** own
   `clients/typescript/lib/haveapi/typescript_client/emitter.rb`, existing/new
   `template/*.ts.erb`, `spec/unit/emitter_spec.rb`, `spec/typescript/*` and
   `clients/typescript/README.md`. Add resource/action/type-barrel templates,
   path planning and diagnostics; replace recursive monolithic emission.
   Update fixture writers to create parent directories and TypeScript includes
   to cover `**/*.ts` (both unit consumer and postreview `wire.rb` currently
   assume flat files). Preserve compile-negative cases and executor assertions.
   The existing gemspec/source-digest recursive globs already cover new templates.
2. **Implementer0, bounded output regression package:** own only
   `spec/unit/generator_spec.rb` initially. Existing `generator.rb` already
   creates nested parents, compares recursive trees and removes stale files/empty
   directories. Add meaningful nested-output/check-mode/stale-directory and
   foreign-file/symlink protection coverage, including flat-to-modular migration.
   No parser/IR/naming change is planned. Report an actual orchestration defect
   through lead before expanding source scope. Independent nonoverlapping HaveAPI
   file edits may proceed in parallel; overlapping edits and all Git/index/normal
   hook windows are serialized, with every other writer paused during hook isolation.
3. **Implementer3, dependent generated-package package:** after the final producer
   commit, update exact source revision/content digest and affected tooling hashes
   in `tools/generator.json`, regenerate all `src/generated/**` and its manifest
   through `tools/regenerate`, and update `tools/check-package.mjs`, relevant
   `test/consumer/*` and README. Retain handwritten `src/index.ts` API. Existing
   `tsconfig.json` already includes `src/**/*.ts`, build clears old `dist`, and
   archive allowlist accepts nested `dist` paths; change them only for an actual
   gap. Extend archive completeness checks from manifest-owned `.ts` files to
   expected nested `.js`/`.d.ts` artifacts; retain the restrictive allowlist and
   exact runtime dependency. No manual generated-source edits or schema relabeling.

### Acceptance and verification

Quick checks: normal hooks/focused Ruby lint and `make test-typescript`; deterministic
sorted emission twice with no I/O/IR mutation; nested resources, canonical actions
and aliases, normalized/path case collisions with useful diagnostics; strict
NodeNext/ES2022 consumers with `exactOptionalPropertyTypes`,
`noUncheckedIndexedAccess` and `verbatimModuleSyntax`. Check root and legacy api
imports plus representative individual action/resource modules; internal binders
must not leak into root exports. Existing runtime spy must prove unchanged exact
requests and receipts. Test recursive owned-tree hashes, no-write stale checks,
removed nested outputs/directories and refusal to touch foreign files/symlinks.

Construct the full downstream deliverable before final review: exact generator
pin, ordinary generation followed by `--check`, build/typecheck and existing
local executor consumer. Check complete resource/action module counts, all public
symbols, routes and aliases against the unchanged IR/schema; no skipped operations.
New files must be in the owned manifest, imports must resolve, and api.ts must
remain composition/re-exports only. Record source/output digests at final heads.

After all intended changes are committed and quick checks pass, lead requests a
new mandatory final affected review of emitter/layout, output ownership changes,
full generated package and complete branch history (no migrations). Preserve prior
review evidence for its scope; this substantive output change is not a mechanical
rebase. Postreview, run the existing published HaveAPI 0.30.2 local wire check and
extracted npm-archive ESM/strict-declaration/runtime consumer with the new module
tree, using normal monitoring for long/uncertain checks. Existing performance
success remains evidence for its old range; lead handles required new-head CI.
No performance framework/workflow, environment, runtime or release changes.

Compatibility/recovery: client call sites and root type names need no migration;
only generated implementation paths expand. Source consumers regenerate the whole
owned directory with its matching manifest/pin. Recover interruption using the
existing restore-committed-tree procedure, never by editing the marker. Reverting
the generator/package pair restores the old layout without server or data changes.
WebUI edits remain deferred; feature publication only, with no default integration,
npm publication, deployment or lifecycle authorization.

## Baseline refresh acceptance — 029f79b, 2026-10-26

Decision: recommend rebasing the two reviewed commits in
`cb43ae2367b12e22e602d69312bfd1f7331b4995..9b9e8549ff0593bf184fc42194b153138831be1d`
onto fetched HaveAPI master `029f79b31cec93167f07e43e571c36b5f42d5b80`.
Bounded inspection found no changed-path intersection with the feature patch.
The baseline adds Ruff parity and frozen performance tooling; `flake.lock`,
runtime pins and generator paths are unchanged. Root `flake.nix` changes only
by the Ruff parity check. Preserve all merged baseline behavior. This is a
rebase recommendation, not integration approval or a review of that framework.

The shell-removal decision below remains valid, but its whole-flake performance
guard explanation is historical. At the new baseline, the workflow and
`utils/performance_ci.rb` use the tracked benchmark Gemfile/lock/shell under
`servers/ruby/benchmarks/` for a frozen environment shared by both source roots.
Root contributor flake files remain provenance, outside dependency equality;
runtime dependency/activation checks and timing budgets remain enforced. See
HaveAPI `doc/performance.md` at `029f79b`. Old environment evidence cannot certify
this changed benchmark input graph.

Owner0 acceptance and minimum verification:

- Rebase only from a clean owned worktree. Record the exact old/new base/head
  ranges and a one-to-one patch-equivalent `git range-diff`; retain the two
  logical commits and no-migrations conclusion. Preserve generator subtree
  content/source digest and generated bytes. Stop and report a substantive
  conflict, changed public contract/output, dependency declaration/lock change,
  or need to alter upstream benchmark policy.
- Run ordinary hooks and the existing focused generator/emitter checks at the
  new head, including strict emitted-source compilation. Keep prior evidence
  attached to its actual inputs. Reconcile the downstream exact generator
  revision/provenance through its existing workflow; unchanged generator
  content needs no vpsAdmin schema re-export. Reuse independent review only
  under the existing patch-equivalence/narrow-fix policy; no new review lane is
  introduced by this assessment.
- Reconcile the remote before feature publication and use an explicit lease
  against published `73115aa5e66c5bebdc3150fff27e6054ff0c4271`; if it moved, stop.
  The merged quick-push resolver compares that exact nonzero event-before SHA
  with the new event-after head, even when they are nonancestors. It does not
  substitute master, merge-base or local `9b9e8549`. The workflow fetches exact
  objects and passes verified push-pair evidence to the runner; a manually
  supplied nonancestor pair is not equivalent.
- Obtain fresh exact-head CI, including performance and release/Ruff checks.
  The direct before/after tree diff includes the merged performance changes,
  so a relevant measurement is expected. Retain preparation failure receipts
  and distinguish measured pass, timing-inconclusive and failure. Lead owns
  monitoring and cancellation of superseded runs for this feature branch.
  No extra manual benchmark campaign is required absent a concrete gap.

No generator, executor, schema or runtime interface changes; no baseline edits,
new environment, version/release expansion, deployment or lifecycle action.
This assessment performed source inspection and documentation only.

## CI preparation repair — existing root development shell

Decision: remove the new `client-typescript` devShell and use the established
root `nix develop` environment for this source-distributed generator. This
supersedes the dedicated-shell part of the implementation brief below. Owner0
reported performance run `40330638675` at candidate `73115aa5` stopped during
dependency preparation, before benchmarking: the only changed guarded input
was the added shell in root `flake.nix`. Bounded inspection confirms
`utils/performance_ci.rb:154,260–268` hashes that whole file and refuses mismatched
dependency manifests. Preserve this check, its budgets, workflows and baselines.

Owner0's exact fix scope:

- Remove only `devShells.*.client-typescript` from HaveAPI `flake.nix` (currently
  lines 196–203), restoring this feature's flake change to the target bytes.
- In `clients/typescript/README.md`, replace `nix develop .#client-typescript`
  with root `nix develop`; remove the component-shell preparation/test paragraph.
  Retain root `make test-typescript`, focused lint and existing JS compiler setup.
- In `doc/agent-instructions/development.md`, remove the component from the shell
  list and state that root Ruby development dependencies and Node supply its
  checks. No Makefile, component Gemfile, runtime, generator, schema or version
  change; no standalone Nix environment or publication expansion.

Evidence: root `flake.nix:82–123` already provides Ruby 3.4, Node 24 and normal
root bundle preparation; root Gemfile supplies RSpec/RuboCop. Makefile:56–58
already runs `test-typescript` from that root bundle. Generator CLI runtime is
stdlib-only. No additional environment is needed for the existing contract.

Acceptance: ordinary hooks; scoped documentation-reference/whitespace checks;
confirm root `flake.nix` is byte-identical to the actual comparison target and
the guarded dependency manifest has no other feature delta. Run the existing
focused `make test-typescript` in the root shell once if needed to establish the
documented command at the corrected head; retain existing strict emitted-source
evidence unless affected inputs changed. Lead uses normal verification monitoring
for any long check and the next exact-head CI run. No new test mirrors this edit,
and this decision itself runs no builds or CI. Preserve the failed preparation
receipt; it is neither a timing regression nor a benchmark pass.

Public API, IR, executor and generated bytes/source-content digest are unchanged
(the digest excludes root flake and these docs). The removed development-shell
selector is unreleased feature tooling. Review scope is development-environment
and documentation reconciliation under the mandatory review skill's narrow-fix
rules, not a repeated runtime/security/schema design review. Final source-head
and any downstream exact generator revision pins must still be reconciled by
their owners; no re-export is justified. The separate Ruff failure remains with
owner0 and is outside this decision.

## Authorized implementation brief — 2026-10-26

This section supersedes conflicting proposal details below. Implement now in own
feature worktrees from HaveAPI `ec84ec874eb209ab59848873998456293ddf3c52`,
vpsAdmin `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5`, and the empty new client
repository. WebUI edits wait for its upgrade integration. No releases, default
merges, deployment or other-session source access. Lead assigns edits and Git
windows; architect owns contract changes.

### Shared schema and generator contracts (settled)

- Generator location `clients/typescript`, Ruby namespace
  `HaveAPI::TypeScriptClient`, executable `bin/haveapi-typescript-client`.
  Source-distributed gemspec/CLI at shared HaveAPI VERSION; no fifth published gem
  or registry release-pipeline change. Add focused Nix/Make/version registration.
- Saved JSON envelope has exactly `schema_format: 1`, `api_version: "7.0"`,
  `protocol_version: "2.x"` (actual exported value), `source_url`, `profile`,
  `mount_path`, `description`. This intentionally matches Rust's structural
  envelope without depending on the Rust gem. Export uses synthetic
  `https://schema.invalid/v7.0/`, mount `/`, profile `vpsadmin-full-fixture`.
  This URL is provenance, never contacted. Record `acquisition: mounted-source`
  in separate provenance. Validate explicit version, description help/routes,
  protocol major, endpoints and shape. Context-aware sanitization strips prose,
  examples and protected defaults, preserving real field/choice/Custom keys.
- Canonical output sorts object keys recursively, preserves arrays, uses UTF-8,
  two-space JSON indentation and one terminal newline. SHA256 binds exact bytes.
  No credentials, generated users/tokens or DB connection strings in artifacts.
- CLI: `haveapi-typescript-client generate --schema FILE --api-version 7.0
  --output DIR [--check]`. DIR is exclusively `src/generated`. No network,
  package manifest generation or source mutation outside DIR. Validate completely
  before writing; refuse foreign nonempty/symlink outputs; owned hash manifest,
  stale owned-file removal and no-write check mode. Determinism excludes absolute
  checkout paths/timestamps. Generator identity includes source-content digest.
- IR is deeply frozen Ruby hashes/arrays with symbol keys and string wire values.
  Root: `api_version`, `schema_sha256`, `metadata_namespace`, `resources`, `actions`.
  Resource: `schema_path` (wire segment array), `export_name`, `accessor_name`,
  `children`, `actions`. Root actions is a flattened sorted index of the same
  action records. Action: `schema_path` (resource+canonical action), `export_name`,
  `accessor_name`, `aliases`, `method`, `path_template`, `placeholders` (ordered
  original names), `auth`, `blocking`, `input`, `output`, `global_input`,
  `global_output`, `object_input`, `object_output`. Absent IO is nil. IO:
  `layout`, `namespace` (string/false), `parameters`. Parameter: `wire_name`,
  `emitted_name`, `kind` (original type string), `required`, `nullable`,
  `protected`, `association` (nil or `resource_path`, `value_id`, `value_label`),
  `validators`. Path template is normalized to version-relative form once.
- Parser owns naming and collision validation. Preserve safe wire snake_case
  accessors; normalize invalid identifier characters deterministically; encode
  nested export boundaries unambiguously. Reject collisions with both original
  schema paths, including action/resource aliases and reserved helpers, `then`,
  `constructor`, `prototype`, `__proto__`. Never silently suffix/drop entries.
- Emitter seam: `Emitter.new(ir, config).files` returns sorted relative path to
  UTF-8 LF content map; no I/O/process/network. Config currently has only
  `runtime_import: 'haveapi-client'`. Emit `index.ts` reexporting generated public
  API; owner0 installs/checks these outputs. Owner0 and owner2 must coordinate any
  field additions through this contract, without editing each other's files.

Contract clarification during implementation: generate all supported application
operations under `description.resources`. Framework authentication resources under
`description.authentication.*.resources` remain owned by HaveAPI authentication
and are deliberately not generated. Retain and validate them in the snapshot and
list their separate resource/action counts and exclusion reason in the generated
inventory/manifest and package docs. Their unversioned `/_auth/...` routes cannot
use this version-root executor. This is an explicit scope boundary, not an
unsupported-operation omission; complete application API coverage remains required.
Any non-versioned path under application resources is a diagnostic/blocker to
report with its exact schema path, not a reason to silently exclude it. No `../`
workaround, extra auth stack or executor path-mode extension is authorized.

Emitted files are `index.ts`, `api.ts`, `runtime.ts`. Reserve the complete global
public symbol set: resource suffix `Resource`; action suffixes `Path`, `Input`,
`Output`, `GlobalInput`, `GlobalOutput`, `ObjectInput`, `ObjectOutput`, `Options`;
helpers/constants `RequestExecutor`, `ClientOptions`, `JsonValue`, `API_VERSION`,
`SCHEMA_SHA256`, and internal `RequestOptions`/`executeAction` where they share a
scope. Aliases remain original wire strings in IR; the emitter uses the parser's
pure `Naming.identifier` function to obtain their checked accessor names. Parser
collision checks use that same function, retain canonical action identity and
reject ambiguous normalized aliases. No added IR field is needed.
Per-object input metadata belongs under the configured metadata namespace in
`params`; global input metadata uses `RequestSpec.meta`. Diagnose a collision with
a real parameter name rather than overwrite it. No object-list input is implied.

### Emitted TypeScript/executor contract (settled)

Public named `RequestSpec` and `RequestResult` imports are verified in published
HaveAPI 0.30.2 (source tag `321ce8256ad4704efaed04f4f2aa1ea4c2a3b4b8`).
`RequestExecutor = (spec: RequestSpec) => Promise<RequestResult<unknown>>`.
`createClient({execute})` exposes named resources/actions; one options object per
call: `{path?: {...}, params?: {...}, meta?: {...}, headers?, signal?, timeoutMs?}`.
Require path/params/options when their members are required; no arguments for
operations with no required inputs. Return `Promise<RequestResult<Output>>`;
narrow only data at one documented boundary and preserve the other receipt fields.

Strip captured mount and `/vVERSION` by validated segments, never guessing.
The executor must already target `https://host/mount/v7.0`; constructor
`{version:'7.0'}` does not version raw AsyncClient.request. Adapter is simply
`spec => runtime.request(spec)`, preserving `this`. Explicitly forward input,
output and metadata namespaces. No discovery/auth/HTTP/decoder/retry/completion
implementation; raw receipts cannot be passed to AsyncClient.waitForCompletion.

Generate per-action inputs, filters and global metadata, not inferred universal
models. String/Text/Datetime use string, Boolean boolean, Integer/Float number,
Resource input scalar integer ID; numeric integers/path IDs must be safe integers
(path strings permitted and encoded). Omit undefined, preserve explicit nullable
null/false/zero/empty. Output fields conservatively optional and nullable;
object/hash outputs are DTOs and list outputs arrays. Resource outputs are partial
association records, Custom output unknown, object metadata retained. JSON-body
Custom input supports recursive JSON; query Custom input is scalar only because
0.30.2 cannot encode structured query values safely. Reject composite query
values locally. Do not manufacture runtime response validation from types.
Reject unsupported input lists/custom IO formats, unsafe paths, unknown types or
namespace forms with precise diagnostics; no silent partial generation. Actual
full-schema unsupported inventory is owned remediation before declaring success.

### Independent edit packages and acceptance

1. **Owner0, HaveAPI parser/orchestrator:** `clients/typescript` snapshot, naming,
   IR, CLI, generator/output ownership, version, bin/Gemfile/gemspec/Rakefile/README,
   parser/CLI/safety fixtures and unit specs; shared Nix/Make/version/docs
   registration. Does not edit emitter/templates/emitter consumer tests.
2. **Owner2, HaveAPI emitter:** `lib/haveapi/typescript_client/emitter.rb`,
   `template/*.ts.erb`, `spec/unit/emitter_spec.rb`, `spec/typescript/**`.
   Own emitted executor/path/type semantics and strict compile/runtime-spy checks.
   No existing `clients/js` runtime changes. Same-worktree edits disjoint; lead
   serializes all Git/index operations with owner0.
3. **Owner1, vpsAdmin exporter:** `tools/export-api-schema`,
   `tools/api-schema-export/{Gemfile,runner.rb,bootstrap.rb,safety.rb,safety_spec.rb}`
   plus fixture/provenance helpers there and `docs/api-schema-export.md`/index.
   Follow narrow real bootstrap precedent `api/lib/vpsadmin/api/i18n/catalog.rb`
   rather than spec_helper/support globs: isolated DB/schema, real API load,
   language/system-config/cluster-resource fixture, mount, actual plugin migrations
   and SpecSeed bootstrap. No runtime/model/schema stubs or production data.
   Reject inherited DATABASE_URL/local DB/api/hooks/Bundler overrides before load;
   use existing TestDb isolated auto-start, no global DB framework rewrite.
   Tool Gemfile evaluates base API Gemfile with original filename and exactly one
   asserted HaveAPI constraint replacement to `=0.30.2`; separate BUNDLE_PATH and
   effective lock. Do not modify API/package runtime pins. Lock is ignored tool
   input, exact bytes/hash retained with export evidence. Explicit all-plugin mode
   with sorted IDs/version/source/migration inventory; reject unexpected plugin
   directory overrides. Export mounted server with user:nil, endpoint:false,
   doc:true, locale en. Provenance binds source, real gem/tool versions, schema,
   fixture/config/lock hashes and counts; no volatile runtime IDs/DB secrets.
4. **Owner3, generated client:** whole new repository outside generated ownership.
   ESM `vpsadmin-typescript-client`, development version 0.0.0, exact 0.30.2
   peer+dev dependency, handwritten entry/adapter outside `src/generated`.
   ESM ES2022 output/declarations, pinned Nix/Node developer tools and TS6.0.3;
   no public Node24 engine restriction. Commit canonical schema/provenance and
   emitted source, not dist. Commit the new repository's npm tooling lock for
   repeatable developer/consumer checks as accepted by lead; HaveAPI's own
   library-lock exclusion remains confined to the HaveAPI repository.
   Offline tools/regenerate requires explicit exact local generator source,
   verifies its identity and supports --check. Export createVpsAdminClient as the
   package-facing wrapper of generated createClient; no fake generated placeholders.
   Package/build/export/declaration and extracted npm-pack consumer checks; no
   initial workflow or publishing setup required. Full generation depends on 1–3.

### Check order and completion

Each owner first runs DB-free safety/parser/emitter/type checks and normal hooks.
One controlled real export and full client generation are implementation/build
work needed to construct the deliverable: after safety checks, use the required
fresh watcher for uncertain-duration DB/tool work. Reconcile every unsupported
construct against the complete schema; do not substitute a subset or omit fields.
Commit complete generator/exporter/client outputs and pass quick checks, then
mandatory independent final review. Afterwards run bounded independent fresh-DB
repeat determinism and real AsyncClient wire/packaged consumer integration through
a watcher; check mount/version paths, namespace/meta, filtered/nullable responses,
errors/cancellation and no write replay. Scope regressions to owned functionality,
with new fixes committed/reviewed as required. No WebUI suite or deployment now.
Acceptance requires complete declared fixture/plugin API coverage and reproducible
output; runtime object-specific authorization/prepare behavior is not schema
completeness. No DB migrations/persisted-state changes; rollback is tooling/client
source selection, not reversal of accepted server writes. Keep feature branches
published, session open and integration approval separate.

Status: proposal, not an implementation or verified deployment. The user selected
one API version deployed with WebUI. Architect0 investigated HaveAPI JS/TS;
implementer0 supplied Go/Rust evidence and implementer1 supplied WebUI/vpsAdmin
evidence. Inspection used canonical bare repositories read-only, without fetching,
tests or live API calls. Cached refs do not establish current remote/deployed state.

## Recommendation

Support a HaveAPI TypeScript generator and a separate generated
`vpsadmin-typescript-client` package. Generate named async operations, per-action
inputs/outputs and metadata from a recorded schema for the API version used by
that WebUI release. This gives autocomplete and compile-time checks for operation
names, arguments, filters and result fields. Generate a small facade with an
injected request executor; keep HTTP, authentication and error handling in the
consumer's established runtime. For WebUI, adapt its existing `haveApiCall` and
retain its domain wrappers. An adapter for HaveAPI's `AsyncClient` can serve other
consumers later. A second standalone HTTP/authentication implementation is not
needed, and switching WebUI to the npm transport is not a prerequisite.

Keep the generic dynamic HaveAPI client for API exploration and arbitrary servers.
Declarations alone would improve autocomplete, but attaching a complete static
interface to permission-filtered dynamic properties can promise methods absent
at runtime. A generated facade offers stable names and one explicit execution
boundary. Its methods still can fail because of permissions or schema drift.

## Evidence and inspected revisions

| Repository | Explicit cached default revision |
| --- | --- |
| HaveAPI (`origin/master`) | `ec84ec874eb209ab59848873998456293ddf3c52` |
| vpsAdmin (`origin/master`) | `b82eeca50cd4dd7bd76728685c7de8aad66e7ba5` |
| vpsadmin-webui (`origin/main`) | `5a2d2bdc3ad7a827038f877d75959916528db844` |
| vpsadmin-go-client (`origin/master`) | `1d9240f3d27b5831baf3694baab5fe06294875d8` |
| vpsadmin-rust-client (`origin/main`) | `ff876abe17e3301da62c1b6afbda055ec89db9d2` |

Paths and line numbers below refer to these revisions, not bare local `HEAD`.

- **There is one JS/TS runtime.** HaveAPI `clients/js/package.json` and
  `clients/js/README.md` describe the TypeScript-authored npm package. Runtime dot
  properties already exist in `clients/js/src/haveapi/async/client.ts:101` and
  `async/resource_model.ts:253`. Generic declarations (`resource_model.ts:11`)
  cannot infer endpoint names fetched later. Callback `findResource`/`findAction`
  also safely resolve names that collide with JavaScript helpers
  (`clients/js/src/haveapi/client.ts:192`).
- **WebUI already has typed adapters and its own transport.** Its
  `tsconfig.json:3` enables strict checking; `src/lib/api/haveapi.ts:83` defines
  request options and `:405` implements `haveApiCall<T>`. `networks.ts:37` is a
  small adapter candidate; `vps.ts:194` translates UI options to wire filters,
  includes and pagination. These wrappers contain product behavior worth keeping.
- **Transport replacement would carry material migration risk.** WebUI
  `haveapi.ts:175` preserves omitted/null query semantics, `:369` selects language
  and authentication headers, and `:471` permits OAuth recovery replay only for
  GET/OPTIONS. `:270` and `haveapiEnvelope.ts:5` preserve uncertain-write receipts.
  Errors, metadata, cancellation, reconciliation and explicit write resubmission
  must survive the generated adapter unchanged.
- **Complete source-derived schema has a precedent, but export needs preparation.**
  HaveAPI `servers/ruby/lib/haveapi/documentation_clients.rb:62` builds Go/Rust
  naming adapters from the mounted DSL using a context with no user and no
  endpoint authorization; `documentation_schema.rb:5` strips structural copies.
  This private documentation machinery is not a supported export CLI.
  vpsAdmin `api/lib/vpsadmin/api.rb:325` loads configured plugins before mount;
  `cluster_resources.rb:463` reads database rows to define fields. A reproducible
  exporter must load the intended plugins and controlled schema fixture data,
  recording their provenance. Static Ruby source scraping is insufficient.
- **Permissions and response filtering remain runtime facts.** HaveAPI
  `servers/ruby/lib/haveapi/action.rb:213` filters descriptions;
  `authorization.rb:111` filters actual output. vpsAdmin
  `api/lib/vpsadmin/api/resources/network.rb:41` restricts fields/rows and
  `resources/vps.rb:117` limits member visibility. WebUI `networks.ts:72` and
  `nodes.ts:312` use OPTIONS to gate writes. A generated method's existence is
  not permission evidence.
- **Types do not validate responses.** HaveAPI `async/request.ts:103` and
  `async/resource_model.ts:224` cast payloads to caller-selected types. Server
  `parameters/typed.rb:132` can return null regardless of input nullability;
  filtered fields can be absent. Generate conservative action-specific output
  shapes, not a fully required universal resource model. WebUI's existing output
  shape checks remain necessary.
- **Borrow Rust's generation discipline.** HaveAPI
  `clients/rust/lib/haveapi/rust_client/snapshot.rb:7` records API/protocol/profile
  identity and canonical schema; `generator.rb:56` records input/output hashes
  and `:126` stages owned output with check mode. The Rust consumer retains
  `schema/provenance.json` and offline `tools/regenerate`. Go's
  `clients/go/lib/haveapi/go_client/generator.rb:37` normally describes a live
  API, while `:22` offers supplied-description generation. Prefer saved inputs;
  do not copy Go's silent unsupported-parameter omission
  (`input_output.rb:37`) or full-Show association assumptions
  (`parameters/resource.rb:24`).

## Proposed interface and initial slice

Illustrative syntax only; this package and interface do not exist yet:

```ts
import { createVpsAdminClient } from 'vpsadmin-typescript-client';

// Adapter retains haveApiCall's errors, receipts and auth/retry behavior.
const api = createVpsAdminClient({ execute: webUiHaveApiExecutor });
const result = await api.network.index({
  params: { limit: 50 },
  signal,
});
const networks = result.data; // Generated conservative NetworkIndexOutput
```

The generated package fixes API version 7.0 for this example, based on inspected
vpsAdmin `api/lib/vpsadmin/api.rb:2` and WebUI `src/app/config.ts:126`.
The executor contract carries method, version-relative path, namespaces,
parameters, metadata and cancellation, returning the existing data/meta/envelope
receipt. It must not accidentally duplicate the configured `/v7.0` prefix.
`fetchNetworks` remains a UI adapter; its operation serialization and handwritten
wire types can be replaced incrementally. No frontend language conversion or
BFF rewrite is involved.

Proposed independent implementation boundaries, for later lead assignment:

1. **Schema export and provenance:** HaveAPI exporter plus a vpsAdmin-owned
   controlled loading fixture; record API/protocol versions, source revisions,
   plugins, schema-defining data and digest. Establish completeness before claiming
   a full vpsAdmin client. This is the explicit prerequisite.
2. **Generator and executor contract:** a new HaveAPI generator directory, with
   deterministic fixtures, operation/type emission, collision diagnostics and
   owned-output check mode. Can develop against fixtures independently of export.
3. **Generated package:** proposed `vpsadmin-typescript-client` repository/package,
   consuming the accepted schema and generator; publish declarations and JS with
   provenance. Depends on the first two boundaries.
4. **WebUI pilot:** `src/lib/api` executor adapter and `networks.ts` read path,
   depending on the package contract. Retain runtime OPTIONS checks and domain
   semantics. Expand to writes and other domains only after the pilot is accepted.

## Invariants, compatibility and recovery

- Separate API version, HaveAPI protocol version, generator version and npm
  package version. Pin the generated package/schema with WebUI's release inputs.
  Do not silently select the server's default API version. One deployment pair is
  the primary target; arbitrary independently upgraded servers are out of scope.
- Generate per-action filters, required inputs and pagination from their actual
  input declarations. An output field is not automatically a list filter.
  Preserve omission versus explicit null, false, zero and empty string; distinguish
  ordinary input/output from global/object metadata.
- Use optional and, where necessary, nullable outputs; resource associations are
  partial references, not guaranteed full objects. Datetime wire values remain
  strings; unspecified Custom values remain `unknown`/JSON. Do not infer closed
  output enums, required fields or integer precision guarantees that the schema
  cannot support. JavaScript safe-integer handling needs an explicit policy before
  claiming lossless 64-bit support.
- Preserve canonical names and deterministic collision handling for helpers,
  aliases and names such as `then`. Reject unsupported schema constructs clearly
  rather than silently dropping operations or parameters.
- Runtime OPTIONS and server authorization remain authoritative. Generated full
  schema is never installed as a user's permission set. Runtime validation and
  schema drift can still reject statically valid calls. Existing HaveAPI async
  validation silently drops unknown inputs (`async/authentication.ts:25`), so any
  later adapter for that runtime must deliberately preserve or improve this
  behavior rather than assume TypeScript prevents stale inputs.
- Preserve WebUI authentication, impersonation, localization, envelope errors,
  metadata, AbortSignal, blocking-action receipts and uncertain-write handling.
  No automatic retry of writes, implicit association fetch or eager pagination.
- Prefer release-time schema drift checks and a tested API/WebUI pair. Roll out
  compatible API changes before the UI consumes them; require explicit ordering
  for incompatible changes. Browser tabs can retain an old bundle during rollout,
  so same-release deployment does not eliminate mixed-version operation.
- This proposal changes no database schema, persisted format, node protocol,
  CLI, Terraform contract or host configuration. Client rollback restores the
  previous WebUI/package pair; reverting UI code cannot undo accepted API writes.
  Schema fixture/export changes must not mutate production data. No deployment or
  publication is authorized by this investigation.

## Acceptance and verification brief

No checks were run: the deliverable is a source-backed recommendation. Future
implementation acceptance is a deterministic generated package whose network
pilot removes handwritten operation/wire typing while retaining WebUI behavior.
Autocomplete and compile-time rejection must work without `any` casts in callers;
permission failures and incomplete responses must still be handled at runtime.

Quick checks should cover deterministic regeneration, wrong operation/argument
compile failures, optional/null semantics, collisions, Custom/association shapes,
and adapter preservation of request and receipt fields. Use HaveAPI's component
Nix environment and established JS/type checks when changing its runtime; WebUI
has an existing `typecheck` script. Check schema coverage and input provenance,
not just successful compilation. Exact commands for the new generator/package
remain to be designed.

After implementation and required independent final review, longer checks should
exercise the pilot against a controlled matching API: authenticated member/admin
descriptions, denied writes, filtered fields, null clearing, cancellation, blocking
receipts and OAuth expiry without write replay. Include a bundled browser smoke
check with WebUI's TypeScript/Vite configuration and an old UI/new API rollout
case. Use the required verification watcher for long/uncertain checks. Actual
export completeness, package publication, deployed-version compatibility and
browser behavior are unverified; they are not blockers to this recommendation.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-typescript-client-generation/>

## Follow-up: use the HaveAPI 0.30.2 adoption as the baseline

Retain the work in `2026-10-24-vpsadmin-haveapi-upgrade`. Its recorded Package C
replaces WebUI's custom transport with npm `AsyncClient`, while retaining
`haveApiCall`, domain wrappers, BFF session policy, per-request credentials/locale,
public/authenticated isolation, error/receipt semantics and protection against
automatic write replay. Package C3 pins 0.30.2 without another adapter rewrite
([upgrade design](../2026-10-24-vpsadmin-haveapi-upgrade/design.md), lines 466–487
and 777–795). The proposed call chain becomes generated operations → WebUI
`haveApiCall` adapter → existing `haveapiRequestClient` → HaveAPI `AsyncClient`.
Do not restore a custom HTTP transport, duplicate decoding or call setup/authenticate
merely to reconstruct WebUI's existing policy on its already-versioned API base.

Our earlier WebUI evidence describes cached base `5a2d2bdc...`, not that upgrade.
Its current [state](../2026-10-24-vpsadmin-haveapi-upgrade/state.md), lines 50–66,
records WebUI candidate `f10d3d48c4f21cc39187c3667ffffd9952404c11` and vpsAdmin
candidate `70a2ed54b98d0c2f359a9cc4484452a257a9807b`. Use the upgrade's accepted
final successor as the WebUI implementation baseline once available through its
normal publication/integration process. Generator/schema work can proceed
independently; serialize subsequent WebUI adapter/package edits after adoption.
No work is transferred from that session by this assessment.

The user reports creating `vpsfreecz/vpsadmin-typescript-client`; the repository
is therefore the intended existing destination, while its contents and package
publication remain unverified. The schema-export prerequisite and generation
proposal are otherwise unchanged. This correction relies only on the explicitly
requested read of that session's plan/state/design/handoff, not its source or
worktrees. The dated handoff still describes 0.30.1 and is superseded by current
state: reviewed 0.30.2 work is not yet merged, legacy verification/cluster work
remains, and browser results retain two accepted preexisting mobile failures.
No implementation, fetch, test, deployment or integration was performed here.

## Appendix: authorized generated-client README follow-up — 2026-10-27

The user authorized implementation of the accepted documentation plan. Improve
the Go, Rust and TypeScript vpsAdmin client READMEs with the same useful VPS
workflow, preserving each SDK's actual interfaces. Accepted source investigation:
Go cached `origin/master` `1d9240f3d27b5831baf3694baab5fe06294875d8`, Rust cached
`origin/main` `ff876abe17e3301da62c1b6afbda055ec89db9d2`, TypeScript
`2dab582881c4af8d8b3f932d9f2308e133d8d925`. This appendix records the settled
brief; it does not authorize further source investigation or generated changes.

### Common flow and exact example contracts

Use this sequence: introduction, installation, complete read-only usage example,
inspect/rename examples, authentication, responses/errors/timeouts, then
development/regeneration. The complete example authenticates with an existing
HaveAPI token, lists the first 50 visible VPSes and prints ID, hostname and
running state. Obtain the token from the environment/caller, reject an empty
value and never print it. Describe this as one page, not all visible VPSes.
Separate examples inspect VPS `123`, then intentionally rename only its
`hostname` to `new-hostname`. Do not put the mutation in the read-only quickstart.

- Go uses the unversioned base `client.New("https://api.vpsfree.cz")`,
  `SetExistingTokenAuth(token)` and an explicit request timeout. List with
  `api.Vps.Index.Prepare()`, `NewInput().SetLimit(50)`, then `Call()`; check `err`
  first and response `Status` before reading `Output`. Fields are `Id`,
  `Hostname`, `IsRunning`. Inspect through `api.Vps.Show.Prepare()` and
  `SetPathParamInt("vps_id", 123)`. Rename through `api.Vps.Update.Prepare()`,
  that same path setter and `NewInput().SetHostname("new-hostname")`, then
  `Call()` with both error checks. Setter selection sends only hostname; avoid
  direct struct initialization that sends unset fields. Go scalar outputs do
  not distinguish omitted values from zero values.
- Rust uses `Client::builder("https://api.vpsfree.cz").token(token).build()?`.
  List with `api.vps().index().limit(50).send().await?`, inspect with
  `api.vps().show(123).send().await?`, rename with
  `api.vps().update(123).hostname("new-hostname").send().await?`. Read `output`
  and handle `Option` fields honestly, including an unknown running state.
  Retain the crate/MSRV/Tokio instructions. Include a short blocking VPS read
  using `blocking::Client` and `.send()?`, with the feature enabled and its
  lifecycle outside an async runtime.
- TypeScript uses `new AsyncClient("https://api.vpsfree.cz/v7.0")`, then
  `await runtime.authenticate('token', {token})`, then
  `createVpsAdminClient({execute: createHaveApiExecutor(runtime)})`. Do not set
  a separate constructor version, add `setup()`, or handcraft authentication
  headers. Version-root OPTIONS with `?describe=default` retains that route's
  version; existing reviewed root/mounted wire acceptance covers this setup.
  List with `api.vps.index({params: {limit: 50}})`, inspect with
  `api.vps.show({path: {vps_id: 123}})`, rename with
  `api.vps.update({path: {vps_id: 123}, params: {hostname: 'new-hostname'}})`.
  Read `data`; preserve absent/null output handling and request `timeoutMs`
  examples. Keep the mounted/versioned-base explanation in the usage section.

Explain each language's errors and selected-input behavior without pretending
the SDKs are identical. Mention existing `from_id` pagination setters without
adding an iterator. Successful submission can start background work; timeouts
do not prove a write failed. Do not add automatic retry/completion code or pass
TypeScript raw receipts to `AsyncClient.waitForCompletion`. Preserve supported
authentication alternatives and the distinction between Rust's public snapshot
and TypeScript's complete declared fixture capture.

### Ownership, acceptance and verification

- Implementer0 owns only `vpsadmin-go-client/README.md`: apply the common flow
  and replace broken `response`/`resp`, inverted token-login error handling and
  invalid token assertion/printing examples with correct supported usage.
- Implementer1 owns only `vpsadmin-rust-client/README.md`: apply the common
  flow, retain the short blocking example and replace obsolete feature-branch
  links with current source links.
- Implementer3 owns `vpsadmin-typescript-client/README.md` and new
  `docs/development.md`: remove the opening exact-runtime requirement and
  private `0.0.0`/unpublished sentences; explain truthful local-tarball
  installation without claiming registry availability. Move detailed tooling,
  verification, schema/provenance and regeneration instructions into the new
  development document, preserving working commands and release-doc links.
- Lead owns the final direct prose pass. Independent repository edits may run
  concurrently; normal Git/index/hook windows remain serialized per repository.

Acceptance is accurate, similarly ordered documentation and compilable exact
final code fences. In disposable consumers, compile Go snippets, Rust async and
blocking snippets, and TypeScript snippets with the existing strict settings,
using local SDKs and each repository's declared environment. Do not execute
examples or contact an API. Keep verification bounded to these snippets and
links; no permanent harness, full suites, regeneration or new package checks.
Run normal hooks and commit intended documentation, then obtain independent
final documentation and complete-history review. No long integration batch is
needed for unchanged runtime/generated inputs.

Compatibility and recovery are documentation-only: no migration, persisted
format, API/runtime, generated source, schema, package metadata, dependency pin
or release change. No version/tag/registry action, default-branch integration,
deployment or lifecycle action is authorized. Existing release prerequisites
remain in their owning documentation and metadata. Architect changes only this
appendix; lead retains plan/state/portal ownership.
