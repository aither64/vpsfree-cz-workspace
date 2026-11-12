# HaveAPI 0.32.2 consumption and client releases

Design owner: architect0. Implementation and release coordination: retained lead
and implementers. This is the implementation brief, not an execution receipt.
The design is sufficient to release packages A–D below; upstream publication
gates dependency resolution. Rust reuses its existing reproducible tooling.

## Scope and source identities

Consume published HaveAPI 0.32.2 in vpsAdmin, integrate verified changes without
waiting for its long CI, regenerate the Go/Rust/TypeScript clients, and make a
new minor release only for clients whose generated code changes. Finally update
and integrate the configuration's `vpsadmin` channel. No deployment, server data
mutation, first-party vpsAdmin gem publication or session lifecycle action is
part of this work.

Fetched baselines on 2026-11-02 (refresh before integration):

| Repository | Target | Observed base | Package |
| --- | --- | --- | --- |
| `vpsadmin` | `master` | `1d4869b6e81dd60916ecb96688ca14a192000b1f` | A |
| `vpsadmin-go-client` | `master` | `134a9e69f9aa6ddec5c94b53744865c6f81ecdd0` | B |
| `vpsadmin-rust-client` | `main` | `1ab58627a225589fefc983829de5c4cfee770b3b` | C |
| `vpsadmin-typescript-client` | `main` | `e5786f69b7c223c3bb5b1de99b7f97186eec368a` | D |
| `vpsfree-cz-configuration` | `master` | `c040c14cdbacc07998700b524996a89306188d7f` | E |

Rust baseline reconciliation: implementer2's fresh fetch, reported through the
lead, established current `main` at `1ab58627a225589fefc983829de5c4cfee770b3b`.
The initially observed `80be1c1a90b7009f8ddecf6a7fe042b506de8b42` remains the
genuine creation base; it is not replaced in historical provenance. Upstream
commits `1559e448` and `1ab58627` already provide the retained generator lock,
frozen isolated CI, source/lock/shared-schema/runtime refusals and refusal tests.

The canonical SSH organization is `vpsfreecz` for all five repositories.
HaveAPI is a read-only source input owned by its publisher: annotated tag
`v0.32.2`, tag object `7f8f656ca7655bafaf2cf5e7095573806085a442`, peeled
commit `1ef9b204ba45bb261d3334be5c555cc1856b713b`. These identities were verified
against the fetched canonical clone. Do not substitute newer HaveAPI master.
The lead reported publication run `41529223599`; registry publication was still
pending at design time. Lead obtains the publication receipt through approved
lead communication; implementers never inspect the publisher's session files.

All source-generator invocations use this exact released source. vpsAdmin
consumes the published gems. Existing Rust/TypeScript regeneration wrappers
require source checkouts, so a pinned release checkout is the established path,
not a reason to use development master. Record installed/resolved gem identities
and source digests. Separate HaveAPI tooling checkouts under this initiative
(for example `haveapi-go-tools`, `haveapi-rust-tools`, `haveapi-ts-tools`) prevent
shared Gemfile.lock, native-gem and Bundler-configuration races. Use independent
gem homes and bundle paths. The lead owns registration/source-input treatment;
no HaveAPI feature changes or default-branch integration are intended.

## Common interfaces and invariants

- API 7.0 and HaveAPI protocol 2.0 remain selected. Client package SemVer is
  independent of API version. No database/schema migration, on-disk format,
  node protocol or NixOS option change is intended.
- Generated trees belong to HaveAPI. Do not patch generated Go/Rust/TypeScript
  source by hand. A generator defect returns to the lead and publisher; it does
  not authorize a new local generator fork.
- Preserve each client's capture profile: Go and Rust describe a public API
  surface; TypeScript requires vpsAdmin's declared full-fixture source export.
  Do not silently substitute the full fixture for a public capture, or a live
  permission-filtered description for the TypeScript fixture.
- Snapshots are inputs, not authorization. Server permission checks remain
  authoritative. No credentials, tokens or raw authenticated captures are saved.
- Compare code before version bumps. A manifest/source-digest/provenance-only
  difference does not trigger the user's conditional minor release. Record a
  no-code result; do not manufacture a release through metadata churn.
- Preserve output omission/nullability, request input selection, explicit API
  routes, existing authentication and timeout semantics. Review removed public
  fields/actions and changed input requirements as consumer compatibility changes.
- TS output from HaveAPI 0.32.2 supports exactly npm `haveapi-client@0.32.0`.
  Existing SDK releases retain their old runtime pairs; the new generated SDK
  updates its exact peer and development dependencies together.
- No Terraform/provider or other downstream client update is in scope. Flag
  breaking generated Go changes for the lead rather than expanding into those
  repositories. Minor releases during 0.x may contain source compatibility changes.

## Package A: vpsAdmin dependency and exporter update

Owner: implementer0 (lead assigned). Ready for preparation now; resolve and
verify published dependencies only after the registry gate.

Files:

- `api/Gemfile`: raise all five HaveAPI declarations to `~> 0.32.2`:
  `haveapi`, `haveapi-client`, `haveapi-go-client`, `haveapi-rust-client`,
  `haveapi-typescript-client`.
- Generated `packages/api/{Gemfile,Gemfile.lock,gemset.nix}` and HaveAPI-client
  locks/gemsets in `packages/client` and `packages/download-mounter`.
  Their source constraints `~> 0.32.0` already admit the patch; do not change
  unrelated dependencies or first-party component versions without cause.
- `tools/api-schema-export/Gemfile`, `tools/api-schema-export/runner.rb`, and
  `docs/api-schema-export.md`: replace the exact exporter 0.32.1 coupling with
  0.32.2, retaining its intentional declaration check and runtime refusal.
  The ignored tooling lock must resolve the same 0.32.2 server.

Use root `nix develop .#vpsadmin` and the existing narrow tasks:

```sh
bundle exec rake vpsadmin:gems:api
bundle exec rake vpsadmin:gems:client
bundle exec rake vpsadmin:gems:download_mounter
```

These tasks remove the respective package lock before resolving. Inspect all
resulting version changes; do not silently accept broad unrelated updates.
Keep one final logical HaveAPI update stream. Do not run unrelated source-gem
tasks, create build IDs or upload first-party gems.

Quick acceptance: required hooks; `git diff --check`; all five API gems and the
client/download-mounter consumers resolve 0.32.2 with valid generated Nix hashes;
Ruby syntax/style for touched tooling; database-free exporter safety/snapshot
specs using the documented `--options /dev/null` invocation. In the prepared API
shell, run the focused documentation-client spec and API boot/version smoke
specs, recording the actual loaded HaveAPI versions. The documentation spec
already checks generator/server version equality. Use a watcher if setup or
test duration is uncertain rather than calling these known quick by assumption.

Longer verification: repository instructions require
`./test-runner.sh test services-up` after HaveAPI package updates, because it
checks documentation content through the packaged API. Lead schedules this
focused local gate after final review with the monitoring skill, without waiting
for the broad long GitHub CI suite. Stop an unexpected kernel build and diagnose
cache/input identity. Do not waive the focused packaged-content check merely
because unit specs pass. No full fleet build or deployment is needed.

Bounded runner setup (source inspection only): launch from the final committed
vpsAdmin worktree with `./test-runner.sh test --jobs 1 --state-dir
/tmp/hvrel-services-up-HEAD services-up`, replacing `HEAD` with its short SHA and
using a fresh, session-recorded directory. The wrapper executes `nix run
.#test-runner`; no Ruby dev shell, NIX_PATH, sibling OS checkout, cluster or bridge
setup is needed. It uses the committed vpsAdminOS input (currently
`8e44a5124439b1f3048ffc56b1717614a5360358`) and builds
`.#tests.x86_64-linux.services-up`, a JSON configuration whose referenced store
paths build the packaged service closure and disk image. It then boots one NixOS
VM with 8192 MiB RAM, 8 vCPUs and user/socket networking, including its mailer
container. Require working `/dev/kvm`, sufficient host memory and `/dev/shm`
capacity, disk space and ordinary Nix daemon access. Host Nix configuration
already includes `cache.vpsadminos.org` and `cache.nixos.org` with their keys.
Have the watcher inspect this single output's `nix build --dry-run` plan before
the test; stop for any unexpected local kernel build and escalate the derivation
and cache/input mismatch, rather than updating pins or compiling a kernel.
Budget roughly 15–30 minutes with usable caches (planning estimate, not a measured
runtime); cold gem/package/image builds may take longer and require reassessment
at the next progress checkpoint. Keep the default 900-second command timeout;
it is not a whole-run deadline. Success requires the native test result, including
the five shared-doc routes and generated Go/Rust/TS example assertions through
the packaged API, not just a successful Nix build. Retain stdout, native results,
the per-test `config.json` under `os-test-services-up-*`, final source/input
identities and its service toplevel/kernel/disk store paths. Do not select broad
CI tags, add overrides, or run a second preparatory build unnecessarily.

After committed-source quick checks and final review, export from the exact
intended final vpsAdmin head in a clean session-owned checkout. The exporter
requires clean committed source and records its HEAD, not remote ancestry, so
both exports may run while post-review `services-up` verification proceeds:

```sh
tools/export-api-schema --prepare
tools/export-api-schema --api-version 7.0 --output /tmp/UNIQUE-vpsadmin-schema
```

Use a fresh destination and the exporter-prescribed clean environment. Keep
`schema.json`, `provenance.json` and `tooling.Gemfile.lock` together. Repeat the
export using a fresh temporary DB and compare canonical schema bytes. Provenance
must identify that exact reviewed vpsAdmin source, 0.32.2 tooling, API/protocol
versions, fixture inputs and all six bundled plugins. This output unblocks D's
preparation, checks, commits and review before A integration. Before D integration
or publication, prove the exported source SHA equals A's final integrated feature
head and retain fresh remote `master` ancestry evidence for that head. If A is
rebased or its source head otherwise changes, repeat both exports at the new
reviewed final head and refresh D's provenance/input hashes and generated output
as needed, even if canonical schema bytes remain unchanged. Apply the normal
affected-check/review rules to D's resulting changes; stale provenance cannot
be accepted merely because the schema is equivalent.

## Package B: generated Go client

Independent of A's source/export and Rust/TypeScript files: its inputs are the
explicit public production API 7.0 capture and released HaveAPI 0.32.2 generator.
Generation, quick checks, commits and review can proceed while A is underway.
Keep integration and publication after A's master integration. Current release is v0.1.0;
the next minor is v0.2.0 if a fresh tag/registry check confirms no intervening
release and the generated `.go` code changes.

Use the released Go generator's saved-schema workflow, an explicit API 7.0
public capture, and the repository's `nix-shell` formatter/compiler. Capture
once with `fetch https://api.vpsfree.cz/v7.0/ --api-version 7.0 --profile public`;
retain the sanitized snapshot and source/lock evidence under this session.
No production mutation or authentication is needed. Generate from that saved
schema into `client/` using `--package client` without `--module`; otherwise
the generator also rewrites `go.mod`. Preserve the declared module path and
Go version. The legacy unversioned URL command is documented locally but the
released saved-schema command removes default-version ambiguity.

Owned changes: generated `client/**`, plus a concise CHANGELOG/README update
only when the release needs new capture/compatibility facts. Go generation does
not remove stale files; compare generated filenames against a fresh temporary
generation and remove only proven obsolete generated paths. Keep handwritten
files and package metadata intact. Repeated generation must be byte-identical.

Acceptance: inspect complete code diff and API removals, `gofmt -l client`,
`go test ./...` (or documented `CGO_ENABLED=0` fallback), unchanged import path,
no new module dependency, and final history review. There are no existing Go
test files; this is principally a compile smoke check. Do not create mirror tests
for a mechanical generated refresh.

Go publication is a SemVer Git tag on the integrated commit, pushed over SSH.
After the approved merge, publish an annotated `v0.2.0` tag if still the next
minor, verify the remote peeled commit, and verify the module version using
`go list -m -json github.com/vpsfreecz/vpsadmin-go-client@v0.2.0` from an isolated
consumer/module cache. Record tag and module evidence. There is no npm/Cargo
publication step or need to invent a release framework.

## Package C: generated Rust client and reproducible tool inputs

Independent of A's source/export: its inputs are the retained public schema,
released HaveAPI 0.32.2 generator and retained dependency lock. Generation, quick
checks, commits and review can proceed alongside A and B. Keep integration and
publication after A's master integration. Retain saved
`schema/api-7.0.json`, its public capture profile and inventory unless an explicit
public recapture is needed and its changes are separately explained. Updating
the generator alone is sufficient to measure generated code changes. Never
replace it with the TS full-fixture snapshot.

Owned paths: `src/generated/**`, `schema/provenance.json`,
`schema/generator.Gemfile.lock` as needed, `generator.toml`, `Cargo.toml`,
crate-version entry in `Cargo.lock`, and `CHANGELOG.md`. Reuse the existing
tooling/docs/CI contract described below. Current crate `vpsadmin-client` is 0.1.0;
conditional next minor is 0.2.0. Keep config, manifest and provenance options
consistent; do not bump before establishing actual generated code changes.

Use existing `tools/regenerate` with `HAVEAPI_SOURCE` at released 0.32.2,
the client's Ruby 3.3 environment and exactly `rustfmt 1.9.0`. Preserve Rust 1.95
MSRV and edition 2024. The runtime is copied into the crate; no new runtime
package or HaveAPI Git/path dependency is permitted.

Reconciled design revision, directed by the lead: HaveAPI 0.32.2 intentionally
omits library Gemfile.lock files, but Rust output hashes the local generator
lock. Current Rust `main` already retains `schema/generator.Gemfile.lock` and
implements frozen isolated installation and source, lock, shared-schema and
runtime identity checks. Reuse that established workflow and its refusal tests;
refresh only the recorded generator/dependency inputs needed for 0.32.2.
Do not add a second lock, duplicate setup, or a new tooling/CI adaptation.
Do not resolve a fresh mutable lock during `--check`. Preserve existing
refusals and the client toolchain pins. Any newly required handwritten change
returns to the lead and receives the applicable final independent review.

Quick checks: `bash -n tools/regenerate`, `cargo fmt --all -- --check`,
`tools/check-provenance`, deterministic `tools/regenerate --check`, source/runtime
digests and retained Ruby lock equality, plus the existing refusal tests. Verify
a fresh tooling checkout can reproduce the committed tree using the retained
lock. No CI YAML change is planned.

Longer checks after final review, in the pinned Nix shell:

```sh
cargo test --locked --all-targets
cargo test --locked --all-targets --features blocking
cargo doc --locked --all-features --no-deps
cargo package --locked
cargo package --list --locked
```

Also retain MSRV 1.95 evidence, provided by the existing release CI matrix or
local check. The optional state-mutating real-server acceptance must target only
the documented disposable loopback fixture if required by the final runtime diff;
it is never pointed at production. Source/schema inspection determines whether
that extra gate is necessary.

Publication: after reviewed integration and matching `v0.2.0` tag, run existing
`gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client --ref v0.2.0
-f authentication=oidc`. The workflow's normal CI matrix, tag recheck, protected
`release` environment and crates.io trusted publisher remain mandatory.
Bootstrap mode is only for a proven absent crate, not an authentication fallback.
Verify published `vpsadmin-client` version and downloaded crate/checksum against
the tagged package. Record workflow run and registry evidence.

## Package D: generated TypeScript client

Depends on the repeated full-fixture export from A's clean, committed, reviewed
intended final head. Generation, checks, commits and review may proceed before
A integration. D integration/publication remains gated on A integration and
exact exported-head equality under package A's reconciliation rule. Prepare the
exact source checkout and pinned npm tools independently. There is no AGENTS.md on the inspected `main`;
README, `docs/development.md` and `docs/releasing.md` own the established workflow.

Owned paths: saved `schema/{schema.json,provenance.json,tooling.Gemfile.lock}`,
`tools/generator.json`, `src/generated/**`, `package.json`, `package-lock.json`,
CHANGELOG and necessary compatibility prose/tests. Preserve handwritten
`src/index.ts` unless new generator types require a bounded adapter adjustment.
Current package is 0.2.0; conditional next minor is 0.3.0 after a fresh version
check. Both exact npm dependencies on `haveapi-client` move from 0.30.2 to 0.32.0.

Update generator revision, generator/source/version digests, shared schema
identity and tooling hashes using their actual inputs. Refresh package-lock
before its recorded digest; do not hard-code the old runtime pairing or edit a
generated manifest manually. Use the existing command:

```sh
./tools/regenerate --haveapi-source /path/to/exact-0.32.2-checkout
./tools/regenerate --haveapi-source /path/to/exact-0.32.2-checkout --check
```

Retain Node 24.21.0, npm 11.19.0, Ruby 3.4.11, TS 6.0.3 and Prettier 3.9.10.
Generation does not install tools. Review expected new root/action `describe`,
help selectors and placeholders, typed metadata/receipts, metadata namespace
behavior, and pre-dispatch `ClientInputError` (`TypeError` subtype). Do not
reclassify transport errors as proven local failures. Compare fixture coverage
against baseline (151 application resources/519 actions plus separate auth
resource/5 actions); explain changes rather than changing counts to silence checks.

Checks: deterministic generation and existing shared-source refusal tests;
`npm run build`, `npm run typecheck`, `npm run typecheck:consumer`, `npm test`,
`npm run test:package`. Pin install with `npm ci --ignore-scripts --no-audit
--no-fund`. Use existing tests for executor calls, request shapes and invalid
input types; add focused cases only for exposed new behavior where existing
coverage is insufficient. Archive consumer verification must use the new exact
runtime pairing. Generated output volume is expected, not handwritten scope growth.

Publication: integrate into `main`, then push matching `v0.3.0` tag. Existing
tag-triggered `release.yml` builds and validates one immutable tarball and receipt,
then publishes that exact artifact through the protected environment and npm
OIDC when `NPM_RELEASE_ENABLED=true`. A manual workflow dispatch is build-only.
Do not replace this with local repacking or change publisher settings implicitly.
Verify `npm view vpsadmin-typescript-client@0.3.0 version dist.integrity --json
--registry https://registry.npmjs.org` against the retained artifact receipt.

## Package E: configuration channel

Depends on A integration and completion of all applicable client releases.
Only the `vpsadmin` channel's role `vpsadmin` is requested. `flake.nix` maps it to
`vpsadminServices`; `vpsadminStaging` and `vpsadminProduction` belong to other
channels and must not be updated incidentally.

From a fresh/rebased own configuration worktree, enter `nix develop` and run
`confctl inputs channel update --commit vpsadmin`. Keep confctl's generated
changelog and commit message. Do not edit flake.lock manually. Compare semantic
lock graph before/after, confirm `vpsadminServices` resolves the approved integrated
vpsAdmin revision (or a later verified descendant, reported to the lead), preserve
sibling inputs/follows and explain expected transitive changes. Inspect the
channel inventory and evaluate affected configuration using existing confctl
commands and hooks. No machine build/deploy or resource reservation is implied
by this channel-only update. Consolidate repeated candidate pins into one update.

## Review, integration, release and recovery

The lead owns approved default-branch integration. The user's instruction covers
the named targets, including Rust/TypeScript `main`, as confirmed by the lead.
Read selected-package coordination guidance before integration. Feature work,
hooks, review and tests need no repository claim. Acquire one only for the final
fresh target check, fast-forward merge/hooks, SSH push and remote ancestry proof;
release before CI or evidence updates. Keep exact final heads and full base/head
history, including the explicit no-migrations conclusion and any consolidation.

After the published HaveAPI receipt, A preparation/verification and B/C
generation, quick checks, commits and review can run independently. B's public
production capture and C's retained public schema do not consume A's source or
export; A integration does not deploy a changed production description. Keep
external delivery ordered: A master integration → client integration and
conditional minor publications → E updated/checked/integrated. D generation
requires the repeated full-fixture export from A's clean, committed, reviewed
intended final head, but can precede A integration. D integration/publication
requires that exact exported head to be the final integrated A feature head;
any head change requires fresh export/provenance reconciliation. Client
repositories use separate tooling checkouts; avoid concurrent edits/Git
operations within one repository. No long vpsAdmin CI wait; registry release
workflows retain their own mandatory verification and approval gates. Use
monitoring utilities for uncertain/long verification and release waits.

Mechanical dependency/generated changes may qualify for the review skill's
content exemption; the exporter changes are substantive. Rust reuses the
already-integrated tooling contract rather than creating a new adaptation.
The lead applies mandatory-change-review to committed final deliverables after
quick checks, preserving complete branch-history and migration assessment.

Recovery preserves immutable releases. Before retrying uncertain publication,
query the registry and original run. Never move a published tag or overwrite a
version. TS retries only the failed publish job with its original immutable
tarball/receipt, never a tag rebuild. Keep old client/runtime pairs pin-able;
client rollback cannot undo submitted server actions. Before integration, return
to the prior committed generated tree and matching schema/tool inputs if generation
fails. Rust uses atomic replacement; Go formatting failure can leave output
written; TS interruption can leave a mixed tree. Reconcile before retrying.

Configuration rollback is a future reviewed channel pin/revert; no activation
occurred here. vpsAdmin rollback restores prior dependency metadata and exporter
pins together. No new database state prevents loading the prior version. This
change does not require coordinated node updates or any machine reservation.

## Remaining evidence, not open design choices

- Publisher's confirmed registry availability and artifact/version receipt.
- Actual regenerated diffs decide which clients receive minor releases.
- Fresh upstream tags/default heads decide the final version numbers and ranges.
- Publication environment approval/registry state is checked when each release
  is concrete; no workflow bypass or new publishing mechanism is designed.
- Exact command results, source/input digests, final heads, run IDs, package
  checksums and any skipped long CI belong in existing session state/receipts.
  No application edits, commits, builds, tests or publication were performed by
  this design investigation.
