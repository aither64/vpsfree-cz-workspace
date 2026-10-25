# Downstream vpsAdmin Rust client: final independent review

**No Blocking, Important or Advisory findings.** All four assigned lanes pass
for the committed regeneration pair. Cargo compilation, docs, package checks,
explicit Rust 1.95 acceptance and exact-head CI remain pending. This report
does not authorize integration, versioning or publication.

## Identity and exact reviewed range

- Session `2026-10-22-haveapi-release`, workspace
  `/home/aither/workspace/ai/vpsfree.cz`; `dev-session current` matched the
  trusted binding. Both identity environment variables were absent.
- Retained independent reviewer `reviewer0`, purpose `review`, ready in live
  roster revision 34; actual saved/assigned settings **gpt-6.1-sol / xhigh /
  read_only**. No overrides, fallback, nested agents or substantive authorship.
- Thread `01a16406-faaa-7cd0-bde3-c20802c18a72`; project
  `01a16406-fa76-7532-9ee4-a890352500df`.
- Repository `vpsfreecz/vpsadmin-rust-client`, target `main`; worktree
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client`.
- Complete range **`945af6a97717a7a6373507bbc9592d5cd53727c2` →
  `ff876abe17e3301da62c1b6afbda055ec89db9d2`**, tree
  **`322fa86ba290b5936a327c21371c94f96f86b249`**.

Applied mandatory-change-review, Shared Reviewer Instructions and full general,
architecture/repetition, scope/proportionality and risk/compatibility references.
Read the complete packet, architect brief and accepted ordering exception,
preparation/owner/independent receipts, current state, downstream AGENTS, README,
development guidance and relevant helpers/manifests/workflow consumers. Reused
unchanged applicable workspace procedures read in this context. Overall risk is
high because the generator pin and generated public contract cross repositories;
the reviewed HaveAPI input does not replace this downstream review.

## Four-lane conclusions

**General: exact saved-input regeneration and ownership are consistent.**
Authored commit `8eaaf241` modifies only `schema/provenance.json`, `flake.nix`
and `docs/development.md`. The four changed provenance leaves are generator
revision, version, source digest and Ruby-lock digest. Capture time, public
profile, schema/inventory/coverage, diagnostics, generator options, runtime and
toolchain facts remain identical. The Nix change adds only libffi. Guidance
uses an isolated Ruby 3.3 frozen bundle under ignored `target/`, separate
Bundler configuration, and the exact downstream rustfmt 1.9.0.

Generated commit `ff876abe` changes only 48 nested resource modules, the common
module index and the ownership manifest. Independently reconstructed and checked
the complete 710-file base/final Git trees and live checkout: exactly 53 modified
paths, no additions/deletions and no unexpected generated paths or symlinks.
All 686 ownership entries match their actual hashes; 687 generated files include
the manifest. Exactly 49 Rust files gain 96 exact rationale/attribute pairs.
Each of the 48 nested declaration attributes matches its corresponding Client
accessor, and all 48 nested bodies are byte-equal after removing only those pairs.
The manifest changes only generator-source/version/Ruby-lock metadata and the
49 affected owned-file hashes.

**Architecture/repetition: the provider remains the sole generator/runtime owner.**
No generated correction was handwritten or downstream naming implementation
added. Actual generator templates own the scoped attributes. Canonical HaveAPI
blob comparison from the previous pin `68cc80b0` to `090a188c` independently
confirms unchanged generator, IR, naming, snapshot, CLI and runtime algorithms.
The new documentation adapter is included in the source digest but absent from
the offline loader's require chain. Existing `tools/regenerate`, provenance
checks and CI consume the exact saved revision rather than a new floating ref.
The source/output commit boundary follows downstream AGENTS and remains one
complete deliverable; the intermediate mismatched provenance/output is not a
release checkpoint.

**Scope/proportionality: the delta matches the bounded regeneration request.**
There is one exact generator pin, one libffi prerequisite and directly related
setup guidance, followed by actual output. No schema refresh, toolchain/Cargo
upgrade, public renaming, fallback, extra compatibility layer or unrelated
handwritten crate change was introduced. Existing verification gates are
appropriate; neither additional live API probing nor a mutation fixture campaign
is needed to explain this unchanged-schema/runtime refresh.

**Risk/compatibility: public behavior and supported inputs are preserved.**
All 524 action files, 104 ordinary resource modules, generated API constants and
eight copied runtime files are byte-identical without normalization. Handwritten
exports (`src/lib.rs`), async/blocking examples and real-server test consumers
retain the same resource/action/type paths. Cargo package version 0.1.0, API 7.0,
MSRV 1.95, Cargo files, generator/formatter config and flake.lock are unchanged.
Fiddle/libffi are generation tools, not new Cargo runtime dependencies. Saved
coverage stays 152 resources, 524 actions and 8720 parameters, with the existing
public-only/plugin-unknown limits.

The common-index exception was independently verified exactly: the unique
`authentication__token__token` declaration moves from declaration 3 to 152.
All 152 declarations remain unique and identical. After removing only the new
exact comment/attribute pairs and that one declaration from both sides, the
remaining bytes and other 151 declarations' order match. No sorting or broader
normalization was used. The index contains ordinary out-of-line declarations,
with no textual macro import, execution or registration behavior; the auth
module has no textual macro scope requiring the old position. Public identity,
visibility, paths and implementations therefore remain intact. The original
strict mismatch is preserved in evidence. This review does not claim a proved
rustfmt-internal cause or an exact normalized whole-file match without the
accepted exception.

Old/new clients can coexist against the same API 7.0. No server deployment,
persistent-state conversion or coordinated update is required. Reverting the
pin/generated tree restores prior source behavior; it cannot undo server
actions previously submitted by a client.

## History, update streams and migrations

Inspected the complete two-commit series, messages, path inventories and final
diff from the verified merge base:

1. `8eaaf241992ec7dd9f5771abbd9e0565fa6da681`: three authored provenance/native/
   documentation paths.
2. `ff876abe17e3301da62c1b6afbda055ec89db9d2`: 50 generated/ownership paths only.

The split is required by downstream AGENTS and matches the accepted design.
Messages describe the result and rationale. There is no obsolete unmerged
iteration, fixup-only commit, abandoned algorithm or transitional compatibility
path. Earlier HaveAPI/released histories remain separate input provenance.

Repeated-stream conclusion: **one final generator revision/provenance update
and one final generated-output stream**, with no redundant intermediate pin or
refresh. No retained release/consumer/state-boundary exception is needed.

Migration conclusion: **no migrations**. Saved schema/capture bytes are unchanged;
there is no database, persisted-format, protocol/API-version or public-name
conversion in this pair. No migration was merged, released, deployed or
externally consumed on this new branch; no transitional lineage remains.

## Independent input evidence and remaining gates

Reviewer performed lightweight read-only canonical-blob/tree/hash comparisons,
without repeating generation or owner quick commands. Independently reproduced
the generator's sorted path-NUL-bytes-NUL rule over 13 source/template files and
eight runtime files at exact HaveAPI `090a188cb4ef3477324718627f4ae3415d1c0975`:

| Evidence | SHA-256 |
| --- | --- |
| Generator source | `ee40aeee00e25aac87d007c241b29b519c7c22ccf3c027c1372e867809312892` |
| Ruby dependency lock | `7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4` |
| Runtime | `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739` |
| Changed 53 files | `3063e0b310f21e58b681c435422ab831058fb3e2e0732083f7517ad59b2827b0` |
| Complete 710-file tree | `9a6931548e219289f867282dc81b2193ef6c3b65e53fa7ae189ca71e35341822` |
| Ownership manifest | `07b37518b47fc0037abe2a38aa2eac8446b717c67274d53501e2c8924b13308f` |

These match committed provenance/manifest and the accepted candidate receipts.
All runtime bytes also match their canonical generator sources. Whole-range
whitespace passes. The supplemental full-index binary diff independently matches
Git and SHA-256 `257bf696adbde5d00d51f0eb47edc7e5ecc5e625f9334ee8c9b751fc2c4a0b98`.
The lead's high-risk/all-four-lane classification governs over the supplemental
packet's medium suggestion; no scope, source or reviewer-setting change occurred.
Owner actual regeneration, read-only check, provenance and
formatting successes and isolated setup receipt are supporting owner evidence,
not reviewer-run execution or proof of Rust compilation.

Remaining post-review gates: committed-head deterministic regeneration and
provenance; locked default and blocking all-target tests; docs; development and
explicit independent Rust 1.95 tests/naming lint; package list/archive inspection;
development push and exact-head CI. Retain the actual input/tool/source graphs
and final `.crate` evidence. Package contents must include the copied runtime
without a HaveAPI path/Git runtime dependency. No compiler, build, install,
listener, API/registry probe or live mutation acceptance was run by the reviewer.

Final recheck confirmed exact head/tree and clean source/index. No hooks framework
is declared by the downstream repository; none was bypassed. Only this assigned
report was written. Lead owns state reconciliation and later verification.
No push, main integration, version/tag/publication, credential, deployment or
lifecycle action occurred. The session remains open.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
