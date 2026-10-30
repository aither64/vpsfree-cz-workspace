# HaveAPI 0.32 and conditional generated-client releases

Design brief, 2026-10-30. The user subsequently authorized implementation through
the lead. Integration and publication retain their separate approval gates.
The initial investigation used canonical bare repositories and cached
remote-default refs only; the baseline table below is historical planning
evidence, not a claim about current execution heads. The lead owns live
plan/state/portal records; architect0 owns this design.

## Scope and observed sources

Publish HaveAPI **0.32.0** before publishing any regenerated vpsAdmin client.
Prepare the three client candidates beforehand from an exact committed HaveAPI
0.32.0 candidate and refreshed existing API input profiles, so integration and
publication approvals can cover concrete reviewed results. Publish a new minor
client version when its generated source changes, including formatting changes.
Generator/package-version, provenance or other metadata-only changes do not
qualify by themselves. This corrects the earlier semantic-only interpretation;
the user's clarification and resulting decisions are recorded below.

| Repository / cached default | Observed source | Conditional release |
| --- | --- | --- |
| HaveAPI / master | `7edb003dd5d5a058b3308510bb8a5f60387ad654`, source `VERSION=0.31.0`; latest local tag `v0.31.2` peels to `819bba5110e089465535ecd71ca2eb37a7d39caa` | coordinated `0.32.0` |
| vpsAdmin / master | `bcfa95eb136c50d25024f53a6b1af557d1173d56` | schema input only; no vpsAdmin release |
| vpsadmin-go-client / master | `73f164dd5eeebfc494705ae27981d30872fa88c3`; module `github.com/vpsfreecz/vpsadmin-go-client`, Go 1.16; no cached tags or package version | determine authoritative tag history first; if genuinely untagged, propose first `v0.1.0`, not an established next minor |
| vpsadmin-rust-client / main | `80be1c1a90b7009f8ddecf6a7fe042b506de8b42`; crate `vpsadmin-client` version `0.1.0` | `0.2.0` if changed and still available |
| vpsadmin-typescript-client / main | `60a1b5d1b911c610bd993d93ae2b28d1932a0ccc`; npm `vpsadmin-typescript-client`, package/lock/tag `0.1.1` | `0.2.0` if changed and still available |
| haveapi-client-php / master | `a02dd2506209f54ea782fbd949243207bf9f93bc`; latest cached tag `v0.31.0` | automatic HaveAPI mirror/tag `v0.32.0`, subject to mirror preflight |

HaveAPI master intentionally retains patch zero while release branches carry
patch versions. Its `0.31.0` source metadata does not mean it predates all
`0.31.2` fixes. Cached PHP refs likewise do not establish whether a publication
finished. Refresh authoritative branches/tags and query exact registry versions
before execution chooses release baselines or reserves versions.

HaveAPI's release procedure includes five RubyGems packages (`haveapi`,
`haveapi-client`, `haveapi-go-client`, `haveapi-rust-client`,
`haveapi-typescript-client`), npm `haveapi-client` plus browser bundle,
PyPI `haveapi-client` wheel/sdist, and Composer `haveapi/client` through the PHP
mirror. All maintained components share 0.32.0; Elixir is excluded. There is no
separately published HaveAPI Rust runtime crate. Ruby vpsAdmin/vpsFree CLIs are
dynamic clients and are outside generated-client release scope, as are Terraform
provider updates, deployments and configuration pins.

## Input and compatibility contracts

- **Go and Rust:** capture the public, unauthenticated
  `https://api.vpsfree.cz/v7.0/` description once with explicit API version `7.0`
  and profile `public-live-api-7.0`; reuse that sanitized format-1 snapshot
  offline. Do not substitute administrator metadata or the full fixture profile.
  Record endpoint, acquisition time, protocol version, canonical schema digest,
  sanitization and inventory. If retaining a raw-response digest, label it
  separately from the canonical digest and keep raw captures outside Git.
- **TypeScript:** use the clean, committed vpsAdmin source exporter with profile
  `vpsadmin-full-fixture`, API 7.0, protocol 2, mount `/`, and all six bundled
  plugins. It uses an isolated temporary MariaDB database and synthetic source
  URL `https://schema.invalid/v7.0/`; no production API/database is contacted.
  Preserve `schema.json`, `provenance.json` and `tooling.Gemfile.lock`, binding
  exact source, fixtures, configuration, plugin inventory and tooling hashes.
- The exporter deliberately overrides HaveAPI to **0.30.2**, while the deployed
  API Gemfile remains `~> 0.29.9`. Verify the exported snapshot with the new
  generators; do not automatically upgrade either dependency. TypeScript's
  exact npm runtime peer/dev dependency remains **0.30.2**, which is also the
  published runtime used by HaveAPI's generator package smoke check. A runtime
  upgrade needs concrete compatibility evidence and a revised brief.
- Pin the exact committed HaveAPI 0.32.0 candidate, component/shared-schema and
  runtime identities, resolved Ruby locks and formatter versions. Source
  generation before publication is supported: each generator's Gemfile selects
  the sibling Ruby client by path, and TypeScript's source helper verifies loaded
  paths and shared/generator identities. No unpublished runtime dependency is
  needed by the SDKs. An executable found on PATH is insufficient provenance.
  Generation is offline and never installs tools. Bind the final released
  source and artifact evidence before SDK publication as described below.
- Existing Rust capture: 2026-10-19, 152 total resources/524 total actions,
  digest `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d`,
  generator `090a188cb4ef3477324718627f4ae3415d1c0975` / 0.30.0.
  Existing TypeScript capture: vpsAdmin
  `7456c7eaae11cee0c76a984b1386a94656510f88`, 151 application resources/519
  actions plus excluded authentication resources/actions, generator
  `18b45aeddd0c28c8ddf6c5ea81f9611d6e3a7875`. Compare refreshed inventories;
  matching action counts alone do not prove identical profiles.

No database migrations, persisted-format changes, server deployment or
coordinated node updates are planned. Schema export only exercises disposable
test state. Generated operation presence never grants permission. Existing
consumers can retain old client versions while the API continues to support
their contracts. Review removed/renamed operations, required inputs, nullability,
public type changes, copied runtime changes and MSRV before releasing; a 0.x
minor bump does not remove the need to document a breaking interface. Rolling
back a client cannot undo server actions it already submitted.

## Ordered execution packages and file boundaries

The following owner allocation follows the lead's plan; verify the live roster
and saved access again when assigning execution. No assignments here start work.

1. **Lead: establish execution and release baselines.** Obtain implementation
   direction, refresh only authorized repositories, read their current rules,
   create session worktrees, and check remote tags, registries and publisher
   configuration. Go's first tag is unresolved until this check. Rust's cached
   annotated `v0.1.0` peels to `b6f84679d33ff041388535dcf4dc060aeb0d1b9d`,
   diverging from cached main at base `ff876abe17e3301da62c1b6afbda055ec89db9d2`.
   Compare the tagged source and release workflow against main and registry
   contents; preserve the tag and its original recovery contract. Do not assume
   main is the already published baseline.
2. **implementer0: HaveAPI release preparation.** From its master-based feature
   worktree, use top-level `nix develop`, `make release-deps`, then
   `make version VERSION=0.32.0`. The Makefile owns shared versions and internal
   dependencies under `VERSION`, `servers/ruby`, `clients/{ruby,go,rust,typescript,js,php,python}`
   and the example Gemfile. Update `CHANGELOG.md` from the actual release delta;
   relevant work includes documentation/UI/OAuth documentation sessions,
   example escaping, formatting and generator/tooling changes. Preserve external
   dependency resolutions; ignored library locks and build artifacts stay
   untracked. Keep metadata separate from any necessary source fixes. Commit
   the candidate and complete quick checks before sharing its fixed identity;
   the committed-deliverable review and release verification gates remain.
3. **Lead and implementer0: freeze the preparation source.** Record the clean
   committed 0.32.0 candidate SHA and generation inputs. Make this exact source
   and its prepared lock evidence available to SDK owners without allowing them
   to edit the HaveAPI owner's checkout, resolve into its bundles or change its
   refs. SDK preparation can start before HaveAPI integration/publication and
   before the later release package checks finish. Its results remain candidates
   until source/package correspondence and all applicable checks pass. This
   removes a scheduling dependency, not a verification or approval gate.
4. **implementer1: schema inputs.** Capture Go/Rust once using the frozen
   HaveAPI candidate source and prepared component bundle:

   ```sh
   BUNDLE_GEMFILE="$PWD/clients/go/Gemfile" bundle exec ruby \
     clients/go/bin/haveapi-go-client fetch https://api.vpsfree.cz/v7.0/ \
     --api-version 7.0 --profile public-live-api-7.0 \
     --output /existing/session-candidate-directory/api-7.0.json
   ```

   Separately, from the selected clean vpsAdmin checkout:

   ```sh
   nix develop .#vpsadmin
   tools/export-api-schema --prepare
   tools/export-api-schema --api-version 7.0 --output /fresh/session-export-directory
   ```

   Respect exporter environment refusals; do not pass production connection
   settings or run it through `bundle exec`. Review candidate schema/provenance
   and an independent repeat export before handing frozen inputs to SDK owners.
   Own candidate artifacts only; SDK owners copy accepted inputs into their
   repositories. No vpsAdmin application or dependency change is expected.
5. **implementer0: Go; implementer2: Rust; implementer3: TypeScript.** These
   packages can proceed independently after steps 3–4 without waiting for
   HaveAPI publication. Hold existing client
   versions fixed while regenerating and classifying the complete diff.

   | Owner | Files and commands |
   | --- | --- |
   | Go | Generator owns `client/**`; preserve handwritten root `go.mod`, README and `shell.nix`. From prepared HaveAPI: `BUNDLE_GEMFILE="$PWD/clients/go/Gemfile" bundle exec ruby clients/go/bin/haveapi-go-client generate --schema /accepted/api-7.0.json --api-version 7.0 --output /go-worktree/client --package client`. Omit `--module` to preserve root module metadata. Generate into a fresh candidate directory and replace only generated files: Go does not remove stale output itself. Retain source/schema/command provenance in release evidence. Current client lacks emitted language support, so a real diff is plausible, not proven. |
   | Rust | Generator owns `src/generated/**`, including runtime and manifest. SDK owner controls `schema/**`, `generator.toml`, `Cargo.toml`, `Cargo.lock`, `CHANGELOG.md` and regeneration tooling. Prepare the separate Ruby bundle following `docs/development.md`, exact `rustfmt 1.9.0`, edition 2024. Point `HAVEAPI_SOURCE` at the frozen candidate source; run `tools/regenerate` then `tools/regenerate --check`. Record new generator/runtime/lock identities. Retain the handed-off generator lock as `schema/generator.Gemfile.lock` and follow the restoration contract below; 0.32 does not commit this lock in HaveAPI. |
   | TypeScript | Generator owns only `src/generated/**`. SDK owner controls `schema/**`, `tools/generator.json`, regeneration/toolchain files, package manifests and relevant docs. Compute identity with `ruby -I /exact/haveapi/clients/ruby/lib -I /exact/haveapi/clients/typescript/lib tools/generator-source.rb identity /exact/haveapi`; update source/schema/provenance/tooling hashes deliberately. Run `./tools/regenerate --haveapi-source /exact/haveapi` then the same with `--check`. New HaveAPI requires **Prettier 3.9.10**, absent from this client's current Nix/npm tools: add a pinned development-only formatter and select its local executable reproducibly, preserving existing source refusals. Keep runtime peer/dev 0.30.2; package validation also checks that exact peer. |

6. **Each SDK owner: apply the release decision.** Compare generated source,
   including copied runtime, against both current default and the last actual
   release. Use raw source differences for release eligibility: formatting-only
   source changes count. Also inspect whitespace-insensitive differences to
   assess compatibility and verify formatting did not hide literal changes.
   Explain every interface/runtime change and every removed file. If source is
   unchanged apart from version metadata, retain the package version and record
   **no release**. Tooling/provenance/metadata-only changes may still need review
   and integration but do not justify publication. If generated source changed,
   select the fresh available minor version, update release metadata
   and changelog, regenerate again if it embeds that version, then rerun affected
   checks. Rust updates Cargo package/lock identity and `generator.toml`; TS
   updates package/lock identity. Never manufacture a change by bumping first.
7. **Lead: finish candidates, review and checks, then request integration and
   publication direction.** Complete SDK candidates and skip decisions before
   asking for the corresponding approvals. Obtain explicit integration direction
   for `haveapi/master` and each changed SDK default (`vpsadmin-go-client/master`,
   Rust/TS `main`). Prepare outside claims; perform short claimed fast-forward
   integrations with hooks, SSH push and remote proof, releasing before CI or
   records. Cut `haveapi-0.32` only from integrated 0.32.0 master. With explicit
   publication authorization, push that branch and annotated `v0.32.0`; the
   protected `release` environment approves the retained artifacts. Authorization
   must explicitly cover automatic `haveapi-client-php/master` and tag updates
   as well as registries. Complete and verify HaveAPI publication and final
   source/package correspondence before publishing changed SDKs, using their
   separately authorized versions/artifacts. Preserve feature refs and keep
   this session open.

## Rust generator dependency preparation

Implementer2 owns this bounded adaptation in the Rust SDK: existing
`.github/workflows/ci.yml`, `tools/regenerate`, `tools/check-provenance`,
`docs/development.md`, and `schema/{generator.Gemfile.lock,provenance.json}`.
Current regeneration CI checks out HaveAPI at the recorded revision but runs
unfrozen `bundle install`; that no longer reproduces a removed upstream lock.
HaveAPI's Rust generator hashes `clients/rust/Gemfile.lock` into its manifest.

- Commit the exact prepared lock bytes handed off with the frozen candidate as
  `schema/generator.Gemfile.lock`. `tools/check-provenance` must hash the file and
  match the existing `generator.ruby_dependency_lock_sha256` in provenance and
  the generated manifest. A recorded digest without retained bytes is insufficient.
- In CI, restore that lock to `clients/rust/Gemfile.lock` in the job's own
  exact-revision `.haveapi-generator` checkout. Local preparation uses an SDK-owned
  exact-revision source copy with the same relative `../ruby` dependency layout.
  Never restore or resolve into the HaveAPI implementer's checkout. A missing
  lock may be copied in explicit preparation; an existing different lock must
  cause refusal, not silent replacement. Verify bytes before and after setup.
- Install the recorded graph with `BUNDLE_FROZEN=true` and dedicated SDK-owned
  Bundler/gem/config paths using the pinned Rust SDK Ruby toolchain. Use the
  recorded compatible Bundler version. Do not reuse HaveAPI's native gem builds
  from a different Ruby. This is dependency installation, not fresh resolution.
  If the handed-off lock cannot install frozen for the supported Ruby/platform,
  report that compatibility failure to the lead. Any necessary alternate graph
  must be deliberately prepared and recorded before generation, never silently
  selected by CI or `tools/regenerate`.
- Before generation, verify the recorded source revision, relevant source
  cleanliness and installed lock identity without weakening source refusals.
  `tools/regenerate` and `--check` only validate and generate; neither installs,
  resolves, copies nor rewrites locks. Preserve existing schema/runtime/formatter
  checks and generated ownership. Correct the docs' obsolete instruction to use
  an upstream committed lock; retain the same ordinary preparation commands.
- Acceptance: a fresh owned checkout can restore/install frozen and reproduce
  generation; a missing/mismatched lock or wrong source fails before output
  mutation; installation/generation preserve the retained lock hash. Run focused
  refusal checks and the existing provenance/`--check` gates. This adaptation
  does not change Cargo dependencies, Rust runtime behavior or the crate's
  packaged file list, and does not alone qualify the crate for a release.

## Candidate-to-release correspondence

Preparing SDKs from source is supported by HaveAPI's local packaging procedure:
component gems use the local Ruby client and do not require the new shared
version to exist on RubyGems. TypeScript's extracted-generator smoke explicitly
uses published npm runtime 0.30.2. Preserve these checks and input profiles.

- Record candidate SHA, effective generator/shared-schema source identities,
  copied Rust runtime digest, exact schema bytes, generator options, formatter
  identities and resolved dependency graphs. Prove the loaded sources come from
  that candidate. Preserve the original candidate and its evidence if later
  changes require another candidate; do not relabel results as final.
- Existing retained-package inspection and extracted Rust/TypeScript generator
  smoke checks remain mandatory. TypeScript's smoke compares extracted and
  checkout source identities and verifies its packaged formatter configuration.
  For Go, additionally compare the retained generator gem's executable, library
  and template inputs against the recorded candidate, together with its matching
  shared Ruby-client schema sources; the existing general gem identity/version
  check alone does not establish that correspondence. A bounded artifact
  inspection is sufficient; no new release framework is requested.
- If the release tag selects the same committed candidate and the relevant
  input identities match, existing SDK generation evidence remains applicable.
  Source and package input equivalence does not mean separate complete release
  builds are byte-identical: verify the final workflow's own manifest, locks,
  artifact hashes and package checks. Source-only tests cannot replace them.
- If integration/rebase changes the HaveAPI SHA, record old/new revisions and
  patch/input equivalence, update SDK provenance to the actual release source,
  then rerun generation/`--check` against the same frozen schemas and inspect the
  final diff. If source, formatter or dependency inputs change, regenerate and
  rerun affected checks; apply the existing independent-review rules to any
  substantive changes. Do not infer equivalence merely from a version string or
  an unchanged final-looking tree. A schema/profile change returns to the lead.
- After HaveAPI publication, verify exact registry package hashes against its
  final retained artifacts and source/tag evidence. Confirm required consumer
  installation/package checks for the published artifacts, then release only
  the SDKs already selected by generated-source change evidence. An incomplete or
  uncertain HaveAPI release blocks SDK publication while preparation can remain
  reviewable and preserved.

## Verification and acceptance

The initial planning investigation ran none of the checks below; live results
belong in the lead's state/evidence. Use repository Nix environments
and declared hooks. Commit intended changes and pass quick checks before final
independent review; use the mandatory-change-review skill and retained eligible
reviewer with saved settings. Include complete base-to-head histories, final
diffs, generated input streams, package ownership and an explicit **no migrations**
conclusion. Mechanical metadata exemptions do not waive history assessment.
This design-only sequencing reconciliation does not itself trigger review.

- **HaveAPI quick:** `ruby utils/release/cli.rb check-clean --master`, prepared
  `make release-check`, relevant hooks. **Longer release gate:** build-only
  release workflow (or equivalent documented local batch) runs dependency
  preparation, i18n health, `make release-test`, `make release`, `make test`,
  npm retained-package smoke and Python package smoke. Release building includes
  extracted Rust/TS generator package checks. Retain exact source, resolved
  locks, manifest and artifact hashes; do not duplicate equivalent successful
  batches without a changed input or unresolved failure.
- **Schema:** database-free exporter safety/snapshot specs per its guide;
  isolated full export and repeated export compare canonical schema/inventory
  and explain volatile provenance fields. Check profile, all six plugins,
  explicit version, and absence of credentials. Both Go/Rust consume identical
  accepted public snapshot bytes; TS consumes its separately accepted fixture.
- **Go:** `nix-shell`, formatting inspection and `go test ./...` (documented
  `CGO_ENABLED=0` fallback if needed). Existing tests mainly compile the package;
  inspect public API/runtime changes separately. Repeat fresh generation and
  compare inventory to catch stale files; no production mutations.
- **Rust quick:** `cargo fmt --all -- --check`, `bash -n tools/regenerate`,
  `tools/check-provenance`, deterministic `tools/regenerate --check`.
  **Longer:** `cargo test --locked --all-targets` both default and
  `--features blocking`, `cargo doc --locked --all-features --no-deps`,
  `cargo package --locked`, package list, and MSRV 1.95. Run real-server
  acceptance only when needed for changed behavior, through the existing
  disposable loopback fixture; never point mutating tests at production.
- **TypeScript:** `npm ci --ignore-scripts --no-audit --no-fund`, generation
  `--check`, `npm run build`, `npm run typecheck`, `npm run typecheck:consumer`,
  `npm test`, and package validation. If regeneration tooling changes, run
  `HAVEAPI_SOURCE=/exact/haveapi node --test test/regeneration/sources.test.mjs`.
  Verify retained tarball using `node tools/check-package.mjs --archive PATH`.
  Keep `dist/` ignored. Strict consumers must still compile against peer 0.30.2.

Delegate long/uncertain tests and CI waits to a fresh policy-selected watcher
under dev-session-monitor, with bounded batches and concrete stopping conditions.
Failures return to the owning implementer; no retry-until-green or additional
unrelated infrastructure project. Final acceptance requires reproducible
generation, reviewed semantic diffs, appropriate check evidence, explicit skip
records for unchanged clients, and exact published artifact/version verification.

## Publication, recovery and remaining gates

- **HaveAPI:** verify protected environment, `HAVEAPI_RELEASE_ENABLED`, trusted
  publishers and PHP deploy-key/mirror prerequisites before tagging. Workflow
  publishes original retained artifacts, synchronizes PHP atomically, and makes
  the GitHub Release public only when all destinations succeed. Verify package
  identities/checksums, remote branch/tag, browser bundle and asynchronous
  Packagist indexing. `make publish` is intentionally not a publishing path.
- **Go:** publish the approved SemVer Git module tag at the verified integrated
  commit. Verify remote tag and module resolution for that exact version from a
  disposable consumer. No existing release workflow or registry upload is known.
- **Rust:** after resolving historical divergence and passing CI, manually
  dispatch `gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client --ref v0.2.0 -f authentication=oidc`.
  Use actual selected version. Protected environment and an existing crate's
  trusted publisher are required; bootstrap is only for proven first publication
  and separate authorization, never an OIDC fallback. Verify crates.io metadata,
  published archive/source identity and downloaded consumer build. Preserve the
  old tag's artifact/recovery obligations independently of the new workflow.
- **TypeScript:** tag the integrated matching version on main. Automated release
  requires `NPM_RELEASE_ENABLED=true`, trusted publisher and protected `release`
  environment. Publish the original immutable tarball/receipt artifact, then
  compare npm `dist.integrity` to the receipt. This workflow creates no GitHub
  Release. If configuration is absent, prepare a validated manual-publication
  candidate under the documented procedure rather than quietly enabling it.
- **Partial or uncertain publication:** preserve tags, original artifacts,
  manifests/receipts and successful destination proofs. Reconcile public state
  before retrying. HaveAPI reruns reuse original artifacts; TS retries only the
  failed publishing job. Respect Rust's exact selected workflow contract. Never
  retag, overwrite accepted versions, blindly reupload, or rebuild an accepted
  archive. Defective published content needs a separately authorized new version;
  consumers can pin the previous release. No machine reservations are needed.

Execution gates still open: authoritative refs/registries; Go version baseline;
Rust tagged-source lineage; publisher/environment readiness; actual regenerated
diffs; final review and checks; integration and publication approvals. These are
execution prerequisites, not blockers to accepting this implementation plan.

## Execution reconciliation: CI Ruby selection and client decisions

Lead-reported evidence on 2026-10-30; exact heads, logs and review receipts remain
in the lead's state/evidence. HaveAPI's candidate identified as `f046…` passed
final review without findings. Its feature-branch RuboCop/i18n jobs then failed
before checks: `ruby/setup-ruby` inherited `.ruby-version` 3.2.0 on Ubuntu 26.04,
but the builder supplies the latest 3.2 patch, not that initial patch.

The accepted bounded fix sets explicit `ruby-version: '3.2'` in the two affected
CI workflows. It preserves the declared Ruby floor, application/runtime source,
generator inputs and dependency locks. Implementer0 owns a separate logical
compatibility commit, official-action-ref verification and quick syntax checks;
reviewer0 covers the affected lane before the next push. This changes the CI
tool selection, not the supported API or SDK runtime contract.

After the final HaveAPI SHA and input-equivalence evidence are available, SDK
owners update their exact revision provenance and repeat regeneration/`--check`
under the existing correspondence rules. Previous source checks do not imply
the failed CI jobs passed, and the final workflow/package evidence still needs
verification.

Historical decisions reported at this checkpoint: TypeScript final review had
no findings and the semantic-only gate selected no npm release; Rust's 686
generated code files were identical and selected no crate release; Go had
generated changes qualifying for its first `v0.1.0`. The TypeScript skip decision
is superseded by the user correction below. Preserve its original review and
skip records as evidence of that earlier decision; do not rewrite them.

## User correction: generated formatting changes qualify

The user asked: "how come typescript doesn't need a new release? iirc we added a
code formatter for it, didn't we?" The lead acknowledged that the original
request covered actual changes and that the semantic-only release gate was
narrower than requested. Generated-source formatting changes therefore qualify;
metadata, provenance and version-only changes still do not qualify alone.

TypeScript's formatter changed 674 generated source files, so the requested
minor release is **0.2.0**. Implementer3 owns the bounded version, changelog and
provenance/hash updates, quick checks, commit, affected review and package gate.
No additional runtime behavior or dependency change is requested: its exact
HaveAPI npm peer/dev dependency remains **0.30.2**. Rust's 686 generated
source/runtime files remain byte-identical, so **no crate release** is still
the correct decision. Go's first **v0.1.0** remains selected; the lead's concrete
compatibility assessment and inherited Custom limitation stay in the execution
evidence, without a new architect investigation.

The pending approval prompt covering HaveAPI and Go while excluding TypeScript
publication is stale and superseded. The lead reports that no approvals were
received. This correction restores the requested scope; it grants no integration
or publication authorization. Complete the corrected release candidates and
verification before presenting updated approvals for the actual repository,
target and publication set. No release is claimed to have occurred.

## Source references

Paths are relative to the named repository at the exact cached revisions above.
They can be read with `git --git-dir=repos/<name>.git show <revision>:<path>`.

- HaveAPI: `AGENTS.md`, `README.md`, `VERSION`, `CHANGELOG.md`, `Makefile`,
  `doc/agent-instructions/{releases,development}.md`, `.github/workflows/release.yml`,
  `clients/go/README.md`, and generator/runtime source comparisons.
- vpsAdmin: `AGENTS.md`, `docs/README.md`, `docs/api-schema-export.md`,
  `docs/agent-instructions/{development,testing}.md`,
  `tools/api-schema-export/Gemfile`, `api/Gemfile`, `client/README.md`.
- Go: `AGENTS.md`, `README.md`, `go.mod`, generated `client/**` and tag inventory.
- Rust: `AGENTS.md`, `docs/development.md`, `Cargo.toml`, `generator.toml`,
  `schema/{api-7.0,inventory,provenance}.json`, `tools/regenerate`, release workflows
  and default/tag ancestry; read-only implementer0 report relayed by lead.
- TypeScript: no repository AGENTS.md; `docs/{development,releasing}.md`,
  `package.json`, `tools/{generator.json,generator-source.rb,regenerate,check-package.mjs}`,
  `flake.nix`, `schema/**`; read-only implementer1 report relayed by lead.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-haveapi-client-releases/
