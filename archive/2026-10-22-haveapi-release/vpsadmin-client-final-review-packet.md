# Downstream regenerated client final review packet

Lead assigns the retained independent reviewer. This packet is the complete
committed deliverable for `vpsfreecz/vpsadmin-rust-client`, Cargo package
`vpsadmin-client`; it does not claim completed final review or long verification.

## Identity and complete range

- Session: `2026-10-22-haveapi-release`; [plan](plan.md), [state](state.md).
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-22-haveapi-release/vpsadmin-rust-client`.
- Branch: `2026-10-22-haveapi-release-regenerate-vpsadmin-client`.
- Fresh remote main/base: `945af6a97717a7a6373507bbc9592d5cd53727c2`, tree
  `c993cef64194e86bac41c073409d345846eecf8a`.
- Final head: `ff876abe17e3301da62c1b6afbda055ec89db9d2`, tree
  `322fa86ba290b5936a327c21371c94f96f86b249`.
- Exact range: `945af6a97717a7a6373507bbc9592d5cd53727c2..ff876abe17e3301da62c1b6afbda055ec89db9d2`.
- Final full-index binary diff SHA-256:
  `257bf696adbde5d00d51f0eb47edc7e5ecc5e625f9334ee8c9b751fc2c4a0b98`.

Complete two-commit series:

| Commit | Purpose | Exact paths |
| --- | --- | --- |
| `8eaaf241992ec7dd9f5771abbd9e0565fa6da681` | `generator: pin fixed HaveAPI and isolate native setup` | `docs/development.md`, `flake.nix`, `schema/provenance.json` |
| `ff876abe17e3301da62c1b6afbda055ec89db9d2` | `generated: refresh client with scoped naming allowances` | Fifty generator-owned paths in the path map: 48 nested resource modules, common module index, ownership manifest |

[Full history](vpsadmin-client-final-history.txt),
[final diff](vpsadmin-client-final.diff),
[series and exact commit trees/messages](vpsadmin-client-final-series.json),
[53-path base/final blob and SHA map](vpsadmin-client-final-path-map.json), and
[complete 710-file base/final inventory](vpsadmin-client-final-all-710-files.json)
cover the whole branch. All changes are modifications; no files were added or
deleted. The registered comparison captures this exact base/head.

## Requested outcome and design

User requested “okay, regenerate the client.” The
[architect-owned design](vpsadmin-client-regeneration-design.md) binds the saved
API 7.0 snapshot to the reviewed fixed HaveAPI generator. Scope is downstream
development work; no default integration, schema recapture, crate version change,
tag, registry action or publication is authorized.

The source owner regenerated through `tools/regenerate`; generated files were
not hand edited. One final provenance pin selects HaveAPI
`090a188cb4ef3477324718627f4ae3415d1c0975`, tree
`e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`, generator version 0.30.0. The source
digest is `ee40aeee00e25aac87d007c241b29b519c7c22ccf3c027c1372e867809312892`;
the Ruby lock digest is
`7f51e5ea00157f4d215355acec5d95c2a8bcbb7d4600c5b34f5e1a338acbc1e4`.
Only these four generator provenance facts changed.

The downstream shell adds libffi for Fiddle's native extension. The guide
documents a dedicated frozen Ruby 3.3 bundle under ignored `target/`, avoiding
HaveAPI's Ruby 3.4 native gems and writable configuration. Nixpkgs/flake lock,
formatter 1.9.0, edition 2024, MSRV 1.95, Cargo manifests/lock and crate version
0.1.0 are retained. Fiddle/libffi are generator tooling, not Rust runtime
dependencies.

## Accepted generated delta and compatibility

The manifest covers 686 output files; all hashes verify. Exactly 49 Rust files
change: 48 nested resource modules and the common module index. They add 96
precise rationale comments and 96 scoped naming attributes. The fiftieth
generated path is the ownership manifest.

There is one explicit accepted normalization exception in the common index:
the unique `authentication__token__token` module declaration moves from
declaration 3 to declaration 152. The other 151 declarations retain their order;
removing only this unique declaration from the normalized files yields equal
bytes. This is bounded in the design; neither sorting nor another normalization
exception is allowed. The existing formatter/template boundary is a plausible
mechanism, not independently proven formatter internals. The original strict
comparison failure and exact diff remain in the owner/crosscheck evidence.

Independent owner1 comparison confirms 524 action files, 104 ordinary resource
modules, API constants and eight copied runtime files are raw-byte equal.
Schema snapshot, inventory, capture/profile/coverage, public names/routes/types,
Cargo/config/lock inputs and handwritten Rust/tests/examples are unchanged.
Runtime digest remains
`9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739`.
No database, persisted-state, wire/auth, deployment or node coordination change
is intended. Old/new client versions coexist with API 7.0; rollback selects the
prior source/pin/output without state conversion.

## History and stream conclusions to review independently

The [stream inventory](vpsadmin-client-final-streams.json) has one final generator
pin/prerequisite/docs update and one cumulative generated-output update.
No intermediate pin, obsolete approach, fixup, repeated dependency update or
superseded generated stream remains. The two purposes follow the repository's
generated ownership boundary. Their temporary provenance/output mismatch is
not a supported release or intermediate readiness checkpoint; the pair is the
final deliverable. The authored pin, libffi prerequisite and setup instructions
support the same exact generation input and are kept together for that reason.

[Migration inventory](vpsadmin-client-final-no-migrations.json): **no migrations**.
The saved API snapshot/inventory are unchanged. Existing generated API modules
with `migration_plan` in their names are client bindings, not database migrations.
There are no new migration versions with merge/release/deployment/external-use
lineage to preserve.

## Evidence and documentation

- [Owner execution receipt](vpsadmin-client-regeneration-receipt.md): isolated
  frozen setup exit 0/61s; actual regeneration, read-only regeneration check,
  provenance check, shell syntax and formatting all exit 0. Exact tools include
  Ruby 3.3.10, Cargo 1.98.0, rustc 1.98.1 and rustfmt 1.9.0. Nondefault Fiddle
  1.1.8 loads from this downstream worktree's bundle.
- [Independent surface/input receipt](vpsadmin-client-regeneration-surface-check.md)
  and [machine evidence](vpsadmin-client-regeneration-surface-check.json): final
  pass with the sole explicitly accepted ordering exception; no unexpected
  finding. This crosscheck supports, and does not replace, final review.
- [Exact frozen candidate hashes](vpsadmin-client-candidate-sha256.txt) all equal
  committed blobs. Changed-53 path-NUL-bytes-NUL digest:
  `3063e0b310f21e58b681c435422ab831058fb3e2e0732083f7517ad59b2827b0`.
  All-710 digest:
  `9a6931548e219289f867282dc81b2193ef6c3b65e53fa7ae189ca71e35341822`.
- [Input graph](vpsadmin-client-final-input-graph.json) binds exact downstream
  source, schema/provenance, helpers/config/locks/guide and generated manifest
  to 13 provider source files, eight runtime files and Ruby lock at exact 090a.
  This is a source-input inventory, not a compiler derivation reuse certificate.
- Changed lasting documentation: `docs/development.md`, linked from README.
  The lead approved its final SHA
  `8f2fa9c9435197e1fce31d1af0c8873633eedd17d64c431bccb93c802510a746`.
  It describes native setup and formatter ownership; temporary review and
  execution status stays in session receipts.
- [Commit receipt](vpsadmin-client-final-receipt.json): both commits used the
  pinned downstream Nix environment, exact-path staging and temporary message
  files. No hook framework exists; no hook installation or bypass occurred.
  Message subjects are at most 60 characters, bodies at most 72. The expected
  Nix dirty-source warning during the candidate commit entry is recorded.

## Review assignment and remaining gates

Suggested risk: **medium**, a bounded compatible generator-input/native setup
and generated-source change. Suggested lanes: general; architecture/repetition;
scope/proportionality; risk/compatibility for the cross-project generator and
generated public surface. All four references were read for packet preparation.
The lead retains assignment and classification authority. Fresh roster identifies
eligible retained `reviewer0`, thread `01a16406-faaa-7cd0-bde3-c20802c18a72`,
`gpt-6.1-sol`/xhigh/read_only/ready; no settings override or reviewer assignment
was made by implementer0.

Review the entire range independently, including the split, single update
streams, exact ordering exception, native dependency scope, provenance integrity
and explicit no-migrations conclusion. Earlier HaveAPI review does not certify
this downstream branch.

Long final-head Cargo default/blocking, independent Rust 1.95, docs, naming-lint
and package checks remain pending review under the architect's exact commands.
No production request or new live disposable server campaign is required by
this regeneration; ignored mutation acceptance tests remain unselected. No
compilation, packaging, push or CI success is claimed for this new head yet.
The source and runtime input equality proofs preserve quick-check applicability;
no source edits or repeated quick campaigns occurred during commits.

Source/index are clean, ignored `target/` is preserved/untracked, remote main
remains the base and the downstream feature is unpushed. HaveAPI source/refs,
official/development artifacts and caches remain unchanged. No owned command
remains active; source/Git/index ownership is yielded to the lead for review.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
