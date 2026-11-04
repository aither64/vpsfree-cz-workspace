# Rust Phase 1 package

## Current status

Implementation committed; quick checks and deterministic generation passed.
Independent final review passed all four lanes with no findings; see
[rust-review-result.md](rust-review-result.md). Feature branch published over SSH;
remote head verified as the exact reviewed head. Required local long checks and
exact-head CI passed; [rust-long-checks-result.md](rust-long-checks-result.md).
Integrated and published as unyanked `vpsadmin-client` 0.2.0. Canonical registry
checksum and embedded VCS source match the exact reviewed head and locally
verified archive; [rust-release.md](rust-release.md).
Head `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`, clean tree. Complete history,
compatibility, documentation and verification inventory is in
[rust-review-packet.md](rust-review-packet.md). Lead owns consolidated session
state and approval-bound integration/publication.

## Ownership and exact inputs

- Repository: vpsadmin-rust-client; target main.
- Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-rust-client`.
- Feature branch: `2026-11-03-vpsadmin-client-sync`.
- Fresh starting head: `3ec8c045dcefcca85b60ffccd38259cda29eeb60`.
- Approved API source: `942c6eaed41331f823d8e0f670ed239e2b308440`.
- Approved HaveAPI source: `1ef9b204ba45bb261d3334be5c555cc1856b713b`.
- Shared HaveAPI checkout is read-only except the source-owner-authorized ignored
  `clients/rust/Gemfile.lock`, copied from this client's retained lock:
  SHA-256 `061f5e4e0f3cb48d529a7914eb087cabda9889d4200a1af9d0d70af7908b5459`.
- Shared export owner: implementer3. Accepted directory:
  `source-inputs/api-7.0` beneath this session. [source-inputs.md](source-inputs.md)
  records accepted hashes and all-three byte-identical fresh-database repeat.

## Release state

At preparation, remote tags and crates.io showed only 0.1.0, unyanked, published October 24.
Tag `v0.1.0` object `77b40d42f1f4a882f1454d6f39c977f66d67ad1f` targets
`b6f84679d33ff041388535dcf4dc060aeb0d1b9d`.
Registry checksum:
`2099d96e698e23912879cc15a32097c920f0db96976c2bee671a5ce2239777d0`.
Released version: 0.2.0. New public Input fields affect exhaustive downstream
struct literals; builder calls can omit the optional fields. No existing actions,
fields, types or validators were removed or changed. Existing crate means manual release
workflow should use OIDC. User confirmed publisher configuration and retired
bootstrap through the lead; no registry authentication attempt is claimed here.
Lead completed approved integration and native OIDC publication; public registry
verification passed. Fresh remote main and peeled v0.2.0 both identify the exact
reviewed head. Published checksum:
`88e0ab97be87b3b3c832dacb751b9fbeee35185eda5804db0d89ee2ad43d9b2d`.

## Preparation and verification

No hook framework is declared; inspected hooks directory contains samples only.
Exact tooling batch is [rust-tooling.sh](rust-tooling.sh), shell syntax passed.
It uses the Rust client's Nix shell, Ruby3.3/Bundler4.0.23 and client-local
`target/` gem/bundle/config paths. It makes no shared root Bundler changes.

Watcher selection verified against pinned catalog `catalog_digest`
`495ef6620926420612ee4988e69d03a4e975e41734a1a5e3208db65fcd731db7`:
gpt-6-luna/low, identity
`dw_af6ea530112c2a5e816254d08d217be90f4f5c713a51db96`, operation lifetime,
single concurrent utility, full access. Lead-owned fresh batch utilities completed
Rust tooling (68s, exit0) and generation plus deterministic check (16s, exit0).
Those preparation operations finished; no duplicate setup or generation was performed.
Logs: rust-tooling.log and rust-generation.log; generation-batch-result.md.

Approved provenance change: retain exact shared schema bytes as
`schema/api-7.0.json`, raw exporter receipt as `schema/source-provenance.json`
and exporter lock as `schema/tooling.Gemfile.lock`. Replace HTTP-capture
assumptions with checks for mounted-source/full-fixture provenance, source SHA,
schema/profile, six plugins, fixture hashes and retained exporter lock. Preserve
generator/runtime/config/dependency-lock gates. Seven provenance artifact tests
pass; ten generator refusal cases pass; formatting, shell syntax and source/input
checks pass. Generated file set/hashes exactly match its ownership manifest and
the copied runtime is unchanged. No manual generated edits were made.

Lead completed writing pass in [rust-prose-draft.md](rust-prose-draft.md).
Approved wording and subsequent concrete Input compatibility note were applied.

All intended changes are committed in three logical commits: provenance tooling,
single generated/input refresh, release metadata/docs. There are no superseded
streams or migrations. Long checks are prepared in
[rust-long-checks.sh](rust-long-checks.sh), passed once in the granted serialized
Luna/low utility slot in approximately eight minutes. Feature CI/MSRV passed.
Exact-head CI run [41665561009](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/41665561009)
completed successfully: async, blocking/docs/package, MSRV1.95 and regeneration.
No operation remains running. Utility capacity released to lead immediately;
no duplicate watcher or parent polling while it ran.

Lead selected the required gates: local async/blocking all-target tests,
documentation/package and exact-head CI MSRV/regeneration. Existing opt-in
real-vpsAdmin acceptance exercises unchanged VPS/DNS/auth runtime behavior and
does not add advisory state coverage; do not prepare/run it for this package.
It remains unrun, with no live authorization/state-conflict or deployment claim.

## Next action

Rust Phase 1 update/release is verified complete. Required verification passed
with no failures, retries or optional fixture work. This owner retains follow-up
ownership; no Phase 2 edits or lifecycle action taken.

Earlier clean detached integration target was prepared at
`worktrees/2026-11-03-vpsadmin-client-sync/vpsadmin-rust-client-integration`,
fresh main `3ec8c045dcefcca85b60ffccd38259cda29eeb60`. Native Git only, no new
session registration, no hook framework, no claim or target mutation. Feature
comparison captured through dev-session with that exact base and reviewed head.
Lead subsequently completed approved integration/publication; this target
preparation paragraph records earlier work, not a current pending approval.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
