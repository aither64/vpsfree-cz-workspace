# Rust 0.2.0 release verification

Published `vpsadmin-client` **0.2.0** is available and unyanked. Its canonical
crate checksum and embedded VCS revision match the reviewed, integrated source
and the locally verified package byte for byte.

## Publication and source

Lead reported terminal success for native OIDC publication
[run 41670222864](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/41670222864)
at `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`: token and publish steps
succeeded, bootstrap skipped. No release artifact was attached to that workflow;
public registry evidence below establishes the distributed package identity.

Fresh read-only SSH `ls-remote` confirmed:

- `refs/heads/main`: `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`.
- `refs/tags/v0.2.0`: annotated tag object
  `6891c260c5d39bbefa41665b0f7161ccd996bf04`.
- Peeled tag: `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`.

Review and prepublication checks:
[rust-review-result.md](rust-review-result.md),
[rust-long-checks-result.md](rust-long-checks-result.md).

## Canonical registry proof

Metadata: <https://crates.io/api/v1/crates/vpsadmin-client/0.2.0>.
Package page: <https://crates.io/crates/vpsadmin-client/0.2.0>.
Canonical archive:
<https://static.crates.io/crates/vpsadmin-client/vpsadmin-client-0.2.0.crate>.

- Version: `0.2.0`; `yanked: false`; Rust minimum `1.95`.
- Registry creation: `2026-11-03T16:10:27.705963Z`.
- Registry and downloaded SHA-256:
  `88e0ab97be87b3b3c832dacb751b9fbeee35185eda5804db0d89ee2ad43d9b2d`.
- Downloaded size: 180,913 bytes; SHA matches both registry and retained local
  prepublication archive. Complete archives compare byte for byte.
- Embedded `.cargo_vcs_info.json` has `git.sha1`
  `49e45527a5683ffe4c03d1b46a74ac137ffa2f9f`, empty `path_in_vcs`, no dirty
  marker. Embedded Cargo manifest is version 0.2.0; generated advisory delete
  and retract modules are present.

The byte identity ties the registry artifact to the package already verified by
the accepted local batch and exact-head CI. The source tree retains the accepted
API fixture schema/provenance and pinned generator identities documented in
[rust-review-packet.md](rust-review-packet.md).

Raw supporting files are disposable under `rust-registry/`: metadata.json,
vpsadmin-client-0.2.0.crate and cargo-vcs-info.json. This Markdown receipt retains
the useful source/artifact evidence. Reads ran once, with bounded HTTP requests
and a small archive; no rebuild, test, authentication change, retry or source edit.

## Limits and handoff

This verifies published package/source identity, not production API deployment,
live permissions or advisory state-conflict behavior. Opt-in fixture acceptance
remains unrun under the lead's recorded gate decision. The new optional Input
fields and exhaustive-struct-literal compatibility consequence are documented
in the published changelog; builders may omit the guard.

Rust Phase 1 release package is complete. No operation or verification utility
remains running. Phase 2 edits, session lifecycle actions and cleanup are not
part of this verification.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-03-vpsadmin-client-sync/)
