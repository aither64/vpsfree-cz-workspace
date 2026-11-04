# Rust Phase 1 final review packet

Prepared for lead-coordinated independent review; no long suites started.

## Outcome and boundaries

Refresh vpsadmin-rust-client to the accepted current API source fixture, prepare
0.2.0, preserve generator ownership/provenance gates, and keep publication separate.
Phase 2 rules, other clients, WebUI WIP, source-generator edits, integrations,
tags, publication and machine deployments are outside this package.

Read this session's plan.md, design.md, source-inputs.md and rust-package.md.
Repository/worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-rust-client`.
Feature branch `2026-11-03-vpsadmin-client-sync`, target main.

## Complete range and history inventory

- Base: `3ec8c045dcefcca85b60ffccd38259cda29eeb60` (fresh upstream main at setup).
- Final head: `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`.
- Working tree clean. Feature branch is not yet pushed, avoiding automatic long
  CI suites before final review. Publish after review, then inspect exact-head CI.

Complete base-to-head series:

1. `98286609d16e17c47bd100bebe895757584634e2` — generator: bind saved schema to source export provenance.
   Narrow checker adaptation, seven negative/positive source-artifact tests and
   one invocation in the existing CI workflow.
2. `a6c00f72756246a875ae228c3de259d6dfb35f4a` — generated: refresh API 7.0 from the source fixture.
   One consolidated schema/provenance/inventory/generated stream, including the
   0.2.0 generator configuration required to produce its ownership manifest.
3. `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f` — release: prepare vpsadmin-client 0.2.0.
   Crate manifest/lock, README, crate documentation, development guide, changelog.

Inspect `git diff 3ec8c045dcefcca85b60ffccd38259cda29eeb60..49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`
and the full series. Final diff: 27 files, 2485 insertions/109 deletions; most
growth is saved schema/inventory, raw exporter receipt/lock and generated actions.
No superseded approaches or repeated generated/pin updates remain. Generator and
runtime pins did not change. Generator config and crate metadata versioning span
commits 2/3 without intermediate versions. No migrations; no migration version
was merged, released, deployed or externally consumed. The new branch itself is
not released, deployed or integrated.

Require the reviewer's explicit whole-history, update-stream consolidation and
no-migrations conclusions. Intended split keeps handwritten checks, generated
refresh and release documentation/metadata separately reviewable.

## Accepted source and dependency identities

API `942c6eaed41331f823d8e0f670ed239e2b308440`; HaveAPI generator
`1ef9b204ba45bb261d3334be5c555cc1856b713b` (0.32.2), retained unchanged.
The latter is an honest nonancestor source pin relative to HaveAPI current
master; this branch does not repair or claim that lineage. Lead owns source
dependency completion handling.

Retained byte-identical shared artifacts:

| Client file | SHA-256 |
| --- | --- |
| schema/api-7.0.json | `d6ec617653913c56e92398a6032aa350118597a0e3f45c599bc92b6071ea0a26` |
| schema/source-provenance.json | `c85815abd315f53a5ef05f324abe377760293786a13a25b7a127ec804c50e0c1` |
| schema/tooling.Gemfile.lock | `62a0e7f65e0755296ea50e3f5efa590f51e8615571a078cf45243f6ca8555f1c` |

Source exporter independently repeated all three artifacts byte for byte.
Profile vpsadmin-full-fixture, English, API7.0/protocol2.0/mount /, all six
bundled plugins. Exporter application counts are 151 resources/521 actions;
Rust inventory includes token authentication: 152 resources/526 actions,
521 application + 5 authentication actions, 8760 parameters.
Full source/plugin/fixture/gem/tooling graph remains in the raw receipt.

Rust uses Ruby3.3.10/Bundler4.0.23/rustfmt1.9.0, pinned nixpkgs
`fe13242281a67641c0102cdb1087f0ebe586c7df`. Generator lock digest
`061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459`;
generator/shared/runtime digests match the existing pin (see rust-tooling.log).
No Cargo dependency updates, MSRV change or generator/runtime source edits.

## Complete compatibility assessment

Structural schema diff is 19 entries: two new advisory actions; seven new
optional expected_state inputs; removal of five protected null defaults; three
fixture OAuth URLs; source URL/profile. No removed resources, actions, parameters,
changed existing field types or validators. The fixture OAuth URLs are not emitted
into Rust source; copied runtime and existing output models are unchanged.

Generated additions: advisory delete/destroy and retract handles, action modules,
and optional expected_state fields/setters/specs on seven existing mutations.
Existing action routes, required inputs and output types remain unchanged.
Adding fields to public Input structs breaks exhaustive downstream struct
literals. 0.2.0 and its changelog explicitly require the new field or
`..Default::default()`; existing builders may omit it.

New calls still require compatible API deployment and server authorization.
Client source availability does not prove production support. No persistent
state, schema migration or coordinated node update is introduced. Consumers can
pin the older crate; rolling back software does not undo submitted server actions.

HaveAPI owns generated code and copied runtime. The Rust crate owns its source
receipt checks, frozen inputs, packaging and public typed API. Actual in-repository
consumers are async/blocking examples and opt-in real_vpsadmin acceptance tests;
crate users are external consumers, not inspected peer worktrees.

## Quick evidence and remaining checks

- Pinned-shell cargo fmt --all -- --check: passed.
- bash -n tools/regenerate: passed; generation/tooling batch scripts also pass.
- tools/check-provenance: passed against accepted schema hash.
- python3 -B tools/test-provenance.py: 7 tests passed in 1.786s.
- python3 -B tools/test-regenerate.py: 10 tests passed in 9.508s.
- tools/regenerate followed by --check: passed, exact lead watcher batch exit0,
  16s; [generation-batch-result.md](generation-batch-result.md), rust-generation.log/status.
- Generated manifest: complete filesystem set and every hash match; runtime
  diff empty; shared triple byte-identical; complete range diff whitespace passes.
- No hook framework declared or installed; hooks directory contains samples only.
- Official action tags checked before CI edit: existing checkout v7.0.1 and
  install-nix-action v31.11.3 are latest checked versions; refs unchanged.

Quick checks ran on the final logical source before commits; subsequent changes
were the lead-approved changelog compatibility note and commit metadata only.
Setup passed once (68s) and is not repeated. No long compilation, package, MSRV,
live acceptance or feature CI result is claimed.

Prepared remaining local batch: [rust-long-checks.sh](rust-long-checks.sh),
async/blocking all-target tests, all-feature documentation, package list and
verified package build. Estimated 5–15 minutes for first compilation; stop at the
first failing command, preserve evidence, no retry loop. Unexpected kernel build
requires escalation. CI also covers exact-head Rust1.95 MSRV and regeneration.
Existing opt-in real-server acceptance needs separately prepared disposable
fixture tooling; lead selects that gate rather than claiming it ran here.

Overall risk: high, because this changes a public Rust interface and source-input
contract. Proposed lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Lead coordinates saved reviewer0 (gpt-6.1-sol/xhigh) after
its TypeScript review; no automatic review assignment made by this packet.
Relevant skill and all four lane references have been read by this packet owner.

Project docs changed: README.md, docs/development.md, src/lib.rs, CHANGELOG.md.
Lead directly applied the writing skill to prose and approved the concrete
compatibility addition. Source-fixture limitations and existing recovery/release
boundaries remain explicit. No Phase2 synchronization procedure was introduced.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
