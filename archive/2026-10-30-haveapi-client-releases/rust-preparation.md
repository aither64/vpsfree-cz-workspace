# Rust SDK preparation

Owner: implementer2. **No Rust release:** all 686 generated Rust/runtime files
equal main and the published 0.1.0 archive, with no additions or removals.
Version remains 0.1.0. The substantive tooling/provenance package is committed
and published at `1ab58627a225589fefc983829de5c4cfee770b3b`. Reviewer0 completed
independent final review with no findings, including skip/history/no-migrations
conclusions. Exact-head CI and package-list verification passed; final source
rebind/check passed. The lead requested integration preparation only from this
member; the detached target is prepared for the lead-owned merge critical
section. No Rust version change, tag or registry write is planned.
No integration, tag, publication or publisher reconfiguration is authorized.

## Authoritative baseline, 2026-10-30

- Verified `dev-session current` and both session environment values match
  `2026-10-30-haveapi-client-releases` in this workspace. Retained implementer2
  has workspace-write access.
- Canonical remote: `git@github.com:vpsfreecz/vpsadmin-rust-client.git`.
  Fetch and SSH `ls-remote --symref` identify default `main` at
  `80be1c1a90b7009f8ddecf6a7fe042b506de8b42`.
- Registered branch `2026-10-30-haveapi-client-releases` and worktree
  `worktrees/2026-10-30-haveapi-client-releases/vpsadmin-rust-client`, created
  from that exact default head. The repository declares no commit hook framework.
- Remote annotated `v0.1.0` object
  `77b40d42f1f4a882f1454d6f39c977f66d67ad1f` peels to
  `b6f84679d33ff041388535dcf4dc060aeb0d1b9d`. It is outside main's ancestry;
  their common base is `ff876abe17e3301da62c1b6afbda055ec89db9d2`.
- Initial workspace plan/state were committed at
  `3f077df285ba0a6bbc78a88cab68037b10e5fcaf` before project work.

## Published package and recovery lineage

The read-only crates.io API lists one version, `vpsadmin-client 0.1.0`, published
2026-10-24T21:21:08Z, not yanked. Candidate 0.2.0 is not presently published;
version availability must be rechecked before eventual publication. The original
178,978-byte archive downloaded from crates.io has SHA-256
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`, matching
registry metadata. Its `.cargo_vcs_info.json` binds the peeled v0.1.0 commit.

The archive contains 697 files, including 687 generated entries (the generated
ownership manifest plus 686 Rust files). Every tracked package member matches
the release tag. Cargo additionally supplies its normalized `Cargo.toml`,
original manifest, VCS record and a resolved library lock. That lock's SHA-256 is
`e75582cba0ade6552f3dfacce0689d0ed2f0cb149591282503ca0da5dfdae323`.

Successful original publication run
[40133192469](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/40133192469)
retains actual publication artifact `12575966992`,
`crate-publish-40133192469-1`. Independently downloading it confirms the same
archive SHA-256. Its receipt records native exit 0, passed archive validation,
the exact tag source and lock above, and candidate/publication archive equality.
It retains Cargo 1.98.0 revision `797e8a9bc` and rustc 1.98.1 identities. Related
retained artifacts are candidate `12575917042`, verified package `12576221369`
and lock `12575219359`. Preserve the tag and its native-archive helper/recovery
contract; do not retag, rebuild or replace this published archive.

All generated Rust and copied runtime bytes in the published archive equal
current main. Main differs in generated ownership metadata, README, changelog
and Cargo.lock. Main's tracked lock SHA-256 is
`3829163d476910f929d26554ec306a463fdbec370e806df40e30d5c9561e409c`;
it has 159 package versions, as does the published lock, with 17 version
differences. These are existing baseline differences, not generated changes
qualifying for another release.

The smallest new candidate lineage is current main, preserving its tracked
Cargo.lock policy and checking generation against both main and the published
archive. The lead accepted this baseline. Do not import the divergent release
branch's older local-only lock policy or introduce a release framework.

## Read-only publisher preflight

GitHub's `release` environment exists, requires reviewer `aither64`, and allows
custom `v*` tag deployments. Current main has a guarded manual OIDC/bootstrap
workflow with direct `cargo publish --locked`; it differs from v0.1.0's retained
native-archive workflow. The prior successful first publication used bootstrap
and crates.io reports no trusted-publisher identity for that historical upload.
The current trusted-publisher binding and credential revocation cannot be
established from that historical record; owner evidence remains a publication
prerequisite. No settings or workflows were changed.

## Inputs, checks and next step

Final HaveAPI candidate: `0e7166a0f8f15827bfac051666a53bf449e999ec`.
Original capture/preparation candidate:
`f0465630595b4fd120561337b3d1d7fa96cbe221`.
Read-only inspection verified clean final source and prepared Rust lock SHA-256
`86c1d8b1846dee4046e59518585a6ab0a52b6c66f1394729ab767c0411dd942c`.
Those exact lock bytes are retained in `schema/generator.Gemfile.lock`.
An independent SDK-owned source copy under Rust `target/haveapi-generator`
uses that exact commit and lock; the owner's HaveAPI checkout and refs were
untouched. A fresh pinned Luna/low watcher installed its frozen bundle with
Bundler 4.0.23 on Ruby 3.3 in 41 seconds and verified source/lock identities
before and after. Log: `rust-preflight/frozen-bundle.log`.

Loaded gem-spec paths resolve to the SDK-owned source copy. Effective generator
source SHA-256 is
`923716b5f3eaca6352d82c8cbd8c194c9a8e4a7a743cf0cb8ce7c491dd08ddce`;
shared schema `haveapi-client 0.32.0` source SHA-256 is
`e12f7989a028bb529f4a78a510af8e09411bbeb5eec9c782feb1fbf20862533c`.
Copied runtime SHA-256 remains
`9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.

The final candidate's exact diff from f046 adds only `ruby-version: '3.2'` to
two HaveAPI CI workflows. Independent inspection confirms the two lines and
unchanged generator/shared/runtime inputs. The owner's
`haveapi-logs/candidate-identities{,-ci-fix}.json` receipts bind identical
effective identities and all ten lock digests. The SDK-owned source copy was
advanced to 0e7166 without re-resolution or dependency reinstallation. Only
`generator.revision` changed in Rust provenance; original capture source f046
remains truthful. Exact-final `tools/regenerate --check`, provenance and
before/after lock comparisons passed. Log:
`rust-preflight/final-source-rebind.log`.

The bounded source/lock/CI/docs adaptation is committed without Rust source or
version edits. Official latest-action queries on 2026-10-30 confirm checkout
v7.0.1 and install-nix-action v31.11.3; CI uses those versions. Regeneration
will verify the source revision, clean generator/shared sources, both lock
copies, loaded-source identities and runtime before invoking generation.

Keep the crate/generator version at 0.1.0 during the first regeneration. Preserve
API 7.0, profile `public-live-api-7.0`, edition 2024, MSRV 1.95 and exact
`rustfmt 1.9.0`. Freeze the actual HaveAPI Ruby lock and source/runtime identities;
the new HaveAPI component lock is a prepared ignored input, not a committed file.

The lead accepted the 2026-10-30 public capture at 11:20:08–11:20:12Z from the
f046 candidate. Its exact 3,649,376 snapshot bytes equal the existing Rust
snapshot; inventory remains 151 application resources/519 actions plus one
authentication resource/five actions. Capture provenance records its original
source, Ruby 3.4.11/Bundler 4.0.23 and Go capture lock
`bb4b5eab29bef661b4b3b5cd64a26852eee795105d0a1d872a37623ffb70450d`.
The historical raw-response hash was removed rather than relabeled as a fresh
capture hash. The new capture did not retain raw HTTP bytes.

Regeneration at unchanged version 0.1.0 passes deterministic `--check`.
There are 687 generated entries including the ownership marker. Compared with
both current main and the actual published archive: no additions/removals,
all 686 Rust files byte-identical, and every generated owned-file hash identical.
Only generator version, source digest and Ruby-lock digest changed in the
ownership marker. Schema bytes, runtime bytes, Cargo dependencies, Cargo.lock,
MSRV, formatter and crate/generator options remain unchanged. The lead accepted
the skip, now independently verified by reviewer0 with no findings.

Lead-owned final development-doc/changelog prose has been applied. The full
preparation example uses a fail-fast subshell, and its refusal paths were tested
before dependency installation. No database migrations or persisted state
changes are involved.

Quick checks passed: formatting, shell/Python syntax, provenance, deterministic
generation and 10 source/lock/shared-schema/runtime refusal tests. The refusal
tests run in disposable source/client copies and assert unchanged output/locks.
Final quick log: `rust-preflight/final-quick.log` (10 tests, 7.810 seconds).
Actionlint and documented shell syntax passed with a fresh policy watcher;
log `rust-preflight/workflow-lint.log`. The actual documented preparation refuses
wrong revision, symlink lock and conflicting lock before dependency installation;
logs `rust-preflight/documented-preparation.log` and
`rust-preflight/final-doc-provenance.log`. Earlier generation log:
`rust-preflight/regeneration-quick.log`.

Complete final local series:

- Base `80be1c1a90b7009f8ddecf6a7fe042b506de8b42`, refreshed origin/main.
- `1559e448e2b7c7f4311030aa8c0b2dce6a6e424d`: handwritten tooling, exact
  dependency lock, tests, CI and docs.
- `1ab58627a225589fefc983829de5c4cfee770b3b`: refreshed capture/generator
  provenance and generated ownership metadata.

The clean final diff contains 9 files, +485/−38, including 204 lock
lines and 107 focused-test lines. The generated/handwritten split follows the
repository's ownership rule. No obsolete approach or repeated update stream
exists. The superseded unpushed metadata commit
`63c1607bd25bdd8c53d33eb6ae9d3648c4685026` was replaced by the final metadata
commit; range-diff proves only `generator.revision` changed. This source-pin
stream has one final selected update. The original release tag/recovery lineage
remains outside this series.
Explicit migration conclusion: **no migrations**, introduced, merged, deployed
or externally consumed by this package.

Longer checks passed after the committed final deliverable, quick checks and
independent final review: default/blocking all-target tests, all-feature docs,
locked package/list and MSRV 1.95. The existing CI matrix provided compilation
coverage; only the missing package-list metadata gate ran locally. No real-server
acceptance is justified by a behavior change.

## Final review packet

Requested result: prepare the Rust SDK from the frozen HaveAPI 0.32.0 source
and accepted public API 7.0 snapshot; release only for meaningful generated
API/runtime changes. Acceptance is deterministic generation at unchanged version,
complete file/removal comparison to main and the actual last published archive,
reproducible frozen dependency installation, and refusal before output mutation
for wrong source/lock inputs. The evidence above supports a no-release outcome;
the independent reviewer must assess it.

Scope is only `vpsadmin-rust-client`, branch
`2026-10-30-haveapi-client-releases`, worktree
`worktrees/2026-10-30-haveapi-client-releases/vpsadmin-rust-client`, target `main`.
The shared [plan](plan.md), architect-owned [design](design.md), and lead-owned
[state](state.md) bound the package. The complete base/head/series and publication
lineage are above. Inspect the full diff with
`git diff 80be1c1a90b7009f8ddecf6a7fe042b506de8b42 1ab58627a225589fefc983829de5c4cfee770b3b`.
No project changes remain uncommitted. Both feature commits are published on
the dated branch; neither is released, deployed or used by an external package
consumer.

The intended two-commit split separates the handwritten source/lock/CI/docs
adaptation and its tests from schema/generator provenance plus generated
ownership metadata, following repository instructions. There are no fixup
commits, obsolete implementations, transitional migrations or repeated pin
updates in the final branch. Review must explicitly conclude on the whole
history, input-stream consolidation and **no migrations**.

Suggested risk classification: medium, for bounded development tooling and
cross-project generator compatibility; no runtime/public API/persisted-state
change. Suggested lanes: general, architecture/repetition, scope/proportionality,
and risk/compatibility for the frozen Ruby/source contract. The lead owns actual
reviewer selection/assignment; retained reviewer0 settings are
`gpt-6.1-sol`/xhigh and must be checked live before assignment.

HaveAPI owns generated code and the common schema/runtime. Rust owns its
recorded snapshot, source/lock selection, preparation and regeneration wrapper.
The actual consumers are the wrapper/CI importing the exact generator and
shared schema, plus the crate's copied runtime. Source guards use the exact
pinned generator's digest implementation and public shared-schema identity;
future source refreshes must update/check this adapter deliberately. Crate
consumers need none of these Ruby development tools. `Cargo.toml` package
inclusions are unchanged; the new dependency lock/tooling/docs are not added
to the crate's packaged file set.

Non-goals: new release machinery, runtime changes, Cargo dependency/lock
changes, different capture profiles, default integration, registry settings,
tags or publication. Preserve v0.1.0 recovery separately; do not rebase onto its
divergent source or import its local-only Cargo lock policy. No coordinated
deployment is needed; existing consumers stay on 0.1.0. Final HaveAPI source/
artifact correspondence and publication remain lead-owned gates, although this
Rust package currently has no publication candidate.

Documentation: existing README still links the owning development guide.
`docs/development.md` explains frozen preparation, input refusal and verification;
`CHANGELOG.md` describes the unreleased tooling/provenance update and no-release
decision. The lead directly supplied the final prose. Historical source/archive
and individual preparation evidence belong in this session record.

After review, the existing CI matrix is the preferred longer batch, including
Rust 1.95. Its equivalent locked commands in the pinned SDK shell are:

```sh
cargo test --locked --all-targets
cargo test --locked --all-targets --features blocking
cargo doc --locked --all-features --no-deps
cargo package --locked
cargo package --list --locked
```

The CI MSRV job installs `rustup toolchain install 1.95.0 --profile minimal`
and runs both all-target test commands via
`nix develop --command "$rustup_bin" run 1.95.0 cargo test ...` with the same
tracked Cargo.lock. These longer checks passed after independent final review.

## Post-review verification

[Reviewer0's final report](rust-final-review-result.md) covers exact head
`1ab58627a225589fefc983829de5c4cfee770b3b`: no findings, all 686 generated Rust
files equal main and the original published crate, sound full history/input
stream consolidation, and no migrations. The lead accepted no crate release
and authorized feature publication/CI only.

Pushed the exact dated branch over canonical SSH; fresh remote proof confirms
feature `1ab58627a225589fefc983829de5c4cfee770b3b` and unchanged default `main`
`80be1c1a90b7009f8ddecf6a7fe042b506de8b42`. Original v0.1.0 tag object/peeled
commit remain unchanged. The native comparison was captured for exact base
80be1c1 → head 1ab5862. No repository claim or default/tag/registry writes ran.

Exact-head [Rust client CI 41051018591](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/41051018591)
passed, monitored by a fresh pinned Luna/low verification utility. Its related
batch ran only the missing local
`nix develop --command cargo package --list --locked` metadata gate and
before/after lock comparisons; the full compile/doc/package/MSRV matrix used
existing CI. No duplicate local compilation or rerun was launched.

| Job | Job ID | Result |
| --- | --- | --- |
| client (async) | 124046786003 | formatting/provenance and locked all-target tests passed |
| client (blocking) | 124046786371 | formatting/provenance, locked blocking all-target tests, all-feature docs and package build/verification passed |
| msrv | 124046785856 | Rust 1.95.0, locked all-target tests in both feature modes passed |
| regeneration | 124046786121 | exact source checkout, frozen Ruby installation, 10 refusal tests, lock equality and deterministic generation passed |

GitHub's job window was 2026-10-30 11:50:58Z–11:55:03Z. The logs confirm
`rustc 1.95.0`, 10 refusal tests in 3.186 seconds, and native Cargo packaging
of 697 files followed by package verification. Real-server tests remained
intentionally ignored. GitHub reports zero uploaded artifacts; this workflow
does not retain its `.crate` archive. This is successful package verification,
not a publication/archive identity claim.

The missing local package-list check also passed. Its 697 unique paths exactly
match the published 0.1.0 archive's member set: no additions/removals, all eight
copied runtime files, generated ownership manifest and Cargo.lock included;
schema/tooling/local bundles excluded. Package-list SHA-256:
`6f600f81737dd3b28b86912b1eecbeb0cec2e210da4064a958810db5e29e84d6`.
Both locks remained identical before/after the metadata check and at the final
clean-worktree check: Cargo.lock
`3829163d476910f929d26554ec306a463fdbec370e806df40e30d5c9561e409c`,
generator lock
`86c1d8b1846dee4046e59518585a6ab0a52b6c66f1394729ab767c0411dd942c`.
CI used that tracked Cargo.lock via every required `--locked` command.

Final fresh SSH remote proof again confirms feature 1ab5862, default 80be1c1
and original v0.1.0 annotated/peeled refs unchanged. The worktree is clean and
the final base-to-head whitespace check passes. Native comparison capture is
still bound to exact base 80be1c1/head 1ab5862; no source changed after review.
No operations remain running.

Raw result files under `rust-preflight/`: `ci-run-result.json`,
`ci-artifacts.json`, `package-list.txt`, `package-inclusion.json`, lock receipts,
`final-ci-watch.log` and `ci-full.log`. CI result JSON SHA-256 is
`222118f9e7dcf766597460bbd446d866283e59da7848ed2b4d9ad46f86a8205e`;
full CI log SHA-256 is
`e8a649465c63f39145c794f9e568cc057e5d975621091b010f814542d493d4bf`.
This Markdown preserves the compact conclusions if raw artifacts are removed
under a future explicitly authorized session lifecycle action.

## Merge-target preparation and Git handoff

Read the complete workspace Git/coordination procedures and selected-package
`workspace-host coordination guide`. Selected runtime:
`/nix/store/d97nazmvhm2a2m3jn8ichid4ksannliq-dev-workspace-0.2.0`,
coordination catalog
`f0188e28ef09cea1410c21f723a77ad2bc1e133d6f6e258af26eed0e058bfce7`.
Preparation took no repository claim.

Fresh SSH fetch and remote proof confirm default main remains
`80be1c1a90b7009f8ddecf6a7fe042b506de8b42` and published feature remains
`1ab58627a225589fefc983829de5c4cfee770b3b`. The complete two-commit series and
9-file +485/−38 diff match the final independent review. Main is an ancestor of
the feature; whitespace passes. Cargo manifests/lock, generator options, Nix
inputs, snapshot/inventory and every generated Rust file remain identical to
base. No obsolete input updates or migrations were introduced.

Created only the requested fresh temporary detached target:
`worktrees/2026-10-30-haveapi-client-releases/vpsadmin-rust-client-merge-target`.
It is clean and remains at exact base 80be1c1; the feature checkout remains
clean at exact reviewed head 1ab5862. Original v0.1.0 tag object/peeled refs and
feature refs are unchanged. No merge or default push has run.

Actual target hook configuration: no `core.hooksPath` override; default hook
directory `repos/vpsadmin-rust-client.git/hooks` has no active executable hooks.
No hook framework is declared/present. `merge.verifySignatures` and
`commit.gpgSign` have no configured override. No installation, trust adjustment
or hook bypass is needed. `nix develop` realized the unchanged target environment
and read Git/Cargo/rustfmt versions without compiling or repeating tests.
Raw preparation/config/environment evidence is in
`rust-preflight/merge-target-preparation.json` and
`rust-preflight/merge-target-environment.log`.

Git ownership is handed to the lead after these checks. The lead owns the
individual claim, fresh feature/target/cleanliness check, ordinary fast-forward
merge, SSH push, remote proof and prompt claim release. Implementer2 will make
no further repository/ref mutations unless assigned a repair. Native comparison
already captures exact base 80be1c1/head 1ab5862. No cleanup or session lifecycle
action was performed.

Baseline environment preflight passed at
`80be1c1a90b7009f8ddecf6a7fe042b506de8b42` in 36 seconds through a fresh
`gpt-6-luna`/low verification watcher from pinned catalog
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`.
It ran `nix develop` with compiler/tool version reads,
`cargo fmt --all -- --check`, `bash -n tools/regenerate` and
`tools/check-provenance`. Tool versions: rustc 1.98.1, Cargo 1.98.0,
rustfmt 1.9.0, Ruby 3.3.10, Python 3.14.7. These checks cover the untouched
baseline only. Log: `rust-preflight/environment.log`.

Raw downloaded archives and receipts remain ignored under `rust-preflight/`.
This compact record preserves their source/checksum conclusions for review.
