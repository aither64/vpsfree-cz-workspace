# Downstream regeneration final review packet

Status: completed committed deliverable, quick checks and independent surface
comparison passed. Exact source/index clean; all 53 candidate hashes retained.
Ready for mandatory final review before long compilation/package checks.

## Requested outcome and authority

User: “okay, regenerate the client”, following the completed HaveAPI fixes.
Regenerate `vpsfreecz/vpsadmin-rust-client` (Cargo `vpsadmin-client`0.1.0) with exact
reviewed/verified HaveAPI090a, retaining saved API7.0 and existing package/config/
Cargo/toolchain inputs. Development branch only. No schema fetch, default merge,
version bump, tag, registry/credential change or crates.io publication is approved.
No new HaveAPI release is needed; the generated runtime is embedded.

Session `2026-10-22-haveapi-release`, workspace `/home/aither/workspace/ai/vpsfree.cz`.
Worktree `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client`.
Branch `2026-10-22-haveapi-release-regenerate-vpsadmin-client`.
Exact base `945af6a97717a7a6373507bbc9592d5cd53727c2`, tree
`c993cef64194e86bac41c073409d345846eecf8a` from fresh SSH defaultmain.
Final head `ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree
`322fa86ba290b5936a327c21371c94f96f86b249`.

Complete series:

```text
8eaaf241992ec7dd9f5771abbd9e0565fa6da681 generator: pin fixed HaveAPI and isolate native setup
ff876abe17e3301da62c1b6afbda055ec89db9d2 generated: refresh client with scoped naming allowances
```

Inspect full final diff directly with `git diff --binary --full-index
945af6a97717a7a6373507bbc9592d5cd53727c2 ff876abe17e3301da62c1b6afbda055ec89db9d2`.
[Commit result](vpsadmin-client-commits-20261023T183942Z/commit-result.json)
binds exact 3/50-path boundaries, all 53/710 file hashes, clean tracked/index and
hook absence. Supplemental export records will follow without source changes.
No obsolete intermediate refresh, migration or repeated input update in this pair.

Read [design](vpsadmin-client-regeneration-design.md), [state](state.md),
[preparation](vpsadmin-client-preparation.md), [implementation receipt](vpsadmin-client-regeneration-receipt.md),
[independent surface check](vpsadmin-client-regeneration-surface-check.md) and its
[full JSON inventory](vpsadmin-client-regeneration-surface-check.json).
Read downstream AGENTS/README/docs/development fully and applicable workspace
procedures. No hook framework is declared; no hook bypass occurred.

## Review selection and risk

Independent retained reviewer0, gpt-6.1-sol/xhigh/read_only, thread
01a16406-faaa-7cd0-bde3-c20802c18a72, project01a16406-fa76-7532-9ee4-a890352500df.
Verify live saved identity before assignment, no overrides/fallback/nested agents.
Apply mandatory-change-review with general, architecture/repetition,
scope/proportionality and risk/compatibility lanes. Overall riskhigh because this
refresh pins a cross-project generated public Rust contract and native setup,
even though preserved public behavior is expected and registry writes are excluded.
Earlier HaveAPI review certifies its input only; it does not replace this review.

## Intended final history and boundaries

Two commits required by downstream AGENTS:

1. Three authored files: exact generator provenance pin/version/source and
   Ruby-lock digest, libffi-only Nix build prerequisite, scoped development guide
   for an isolated frozen Ruby3.3 bundle and exact downstream formatter.
2. Fifty actual generator outputs only:48 nested resource modules, common module
   index and ownership manifest. No handwritten generated corrections.

One final generator pin stream and one generated output stream, no intermediate
pins/fixups/obsolete algorithms. The temporary provenance/generated mismatch
between commits is a reviewable source/output boundary, never a release state.
Complete deliverable is the pair. Explicit no migrations: saved schema/capture
bytes unchanged, no database/persisted-format/protocol/public-name conversion.
No migration merged/released/deployed/externally consumed in this new branch.

## Exact inputs and compatibility

HaveAPI pin090a188cb4ef3477324718627f4ae3415d1c0975, source digest
ee40aeee00e25aac87d007c241b29b519c7c22ccf3c027c1372e867809312892,
Ruby-lock7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4.
Its source/tree/published branch are preserved. The old68cc→090a generator/IR/
naming algorithms and all eight runtime files are unchanged; new docs adapter is
included in source digest but not loaded by offline generator. Version0.30 and
explicit Fiddle dependency are true provenance changes, not a patch-equivalence
claim for the whole generator source.

Retain API7.0 schema70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d,
inventory563b3472fe0ab03f9c8b0ecc4a5623a883efe43103060e3c6484c13bdbd474a1,
152resources/524actions/8720parameters. Unchanged public-only/plugin-unknown
coverage, capture time/profile/diagnostics, Cargo files/version0.1.0/MSRV1.95,
generator.toml/rustfmt.toml and flake.lock. Downstream nixpkgsfe1324 and exact
rustfmt1.9.0 remain. Runtime digest9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739.
Libffi/Fiddle/Ruby bundle are generation tools, not Cargo runtime dependencies.
No server deployment or state conversion; old/new clients coexist against API7.0.

Independent candidate crosscheck:53 modified tracked files, no added/deleted;
686 owned-file hashes verify (687 including manifest). Exactly49 Rust files gain
96 scoped attributes with96 exact rationale comments.48 nested bodies equal after
removing only those pairs;524actionfiles,104ordinary modules,constants and8runtime
files equal without normalization. All public names/routes/types/signatures/bodies
remain. Changed53 path-NUL-bytes-NUL digest3063e0b310f21e58b681c435422ab831058fb3e2e0732083f7517ad59b2827b0;
all710candidatefiles9a6931548e219289f867282dc81b2193ef6c3b65e53fa7ae189ca71e35341822;
manifest07b37518b47fc0037abe2a38aa2eac8446b717c67274d53501e2c8924b13308f.

One explicit accepted ordering exception, independently inspect it:
`src/generated/resources/mod.rs` declares the same152unique modules, but the
unique `authentication__token__token` declaration moves from declaration3 to152
(physical4→249; normalized line153). Remove only that unique declaration from
both normalized sides: all other151 declarations/order/bytes equal. No generic
sorting or broader normalization. Unchanged IR appends auth resources, and the
new attribute/comment boundaries are consistent with rustfmt grouping; actual
formatter internals are not claimed proved. Plain out-of-line modules have no
macro_use/executable registration. Original strict comparison failure remains
recorded, not hidden or labeled an exact whole-file match. Lead accepted the
precise exception; source remains actual deterministic generator output.

Consumers to inspect from current manifests/imports: handwritten src/lib reexports,
async/blocking clients/tests/examples, regeneration/provenance helpers and CI's
exactSHA HaveAPI checkout, package/docs consumers. No new workflow is needed.

## Verification and documentation

Owner setup: one fresh pinned Luna/low utility, normal downstream Nix, own ignored
target paths, frozen lock and isolated Ruby3.3 native gems. Exit0/61s,
Ruby3.3.10/Cargo1.98.0/rustc1.98.1/rustfmt1.9.0; nondefaultFiddle1.1.8 active.
HaveAPI tracked source/lock unchanged. See [setup result](vpsadmin-client-setup-result.json).
Owner quicks exit0: bashsyntax, bundlecheck, actual tools/regenerate, --check,
all687before/afterhashes, tools/check-provenance, cargo fmt and whitespace.
Independent read-only crosscheck reproduced source/runtime/Ruby-lock digests
from canonical blobs and checked all baseline/candidate hashes/public invariants.
No compiler/network/schema/registry probe in those checks.

Lasting guidance in docs/development.md explains Fiddle/libffi, frozen isolated
bundle and pinned formatter. Main-agent prose pass complete, hash8f2fa9c9435197e1fce31d1af0c8873633eedd17d64c431bccb93c802510a746.
Project docs describe repeatable operation; exact decisions/runs remain in session
records. No new changelog/version/release instruction was added.

Remaining gates AFTER final review: lockeddefault/blocking all-target tests,
Rustdocs, naming lint with dev and explicitRust1.95, package list/archive,
deterministic generation/provenance on committed head, package inspection, feature
push/exactheadCI. No live vpsAdmin mutation acceptance is needed: schema/runtime
unchanged; ignored real-server tests remain unselected. No long checks yet.
Return concrete findings by severity/lane/file/commit and explicit history,
stream/consolidation/migration/publiccompatibility conclusions plus residualgaps.
Remain read-only except assigned report; no nested reviewers/compiler/build/
listener/install/API/registry/Git/source mutation.

## Supplemental command-free exports

[Final owner packet](vpsadmin-client-final-review-packet.md),
[receipt](vpsadmin-client-final-receipt.md), [series](vpsadmin-client-final-series.json),
[path map](vpsadmin-client-final-path-map.json), [710-file inventory](vpsadmin-client-final-all-710-files.json),
[source input graph](vpsadmin-client-final-input-graph.json),
[streams](vpsadmin-client-final-streams.json),
[no migrations](vpsadmin-client-final-no-migrations.json),
[full diff](vpsadmin-client-final.diff). Full-index binary diff SHA-256:
`257bf696adbde5d00d51f0eb47edc7e5ecc5e625f9334ee8c9b751fc2c4a0b98`.
All owners command-free, exact candidate hashes retained and comparison captured.
The owner packet's suggested medium risk does not change lead's high/all-four-lane
classification. Preservation proof distinguishes untouched shared local HaveAPI
master7835acaf from remote masterb64; no previous local hash/ancestry is invented.
