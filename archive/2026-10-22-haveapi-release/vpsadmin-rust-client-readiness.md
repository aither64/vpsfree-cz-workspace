# vpsAdmin Rust crate: release preparation receipt

Read-only source and registry/setup investigation on 2026-10-22 by architect0.
This receipt prepares a later release; no token was read, no secret configured,
no tag pushed and no workflow dispatched. No downstream worktree or branch was
created, and no other session's records/worktree were accessed.

## Conclusion

The existing source already implements the required first-publication and OIDC
flows. No new application code is indicated by this audit. The repository is
**`vpsfreecz/vpsadmin-rust-client`**, but the actual crates.io package is
**`vpsadmin-client` 0.1.0**, imported as `vpsadmin_client`. Do not rename it or
publish under the repository basename by assumption.

Exact current main CI is green, including packaging, both transport modes, MSRV
and regeneration. Release prerequisites remain: explicit publication direction;
final-review evidence for the exact source; protected GitHub `release`
environment; owner/account and bootstrap-token readiness; and an authorized
`v0.1.0` tag. No version tag or GitHub Release currently exists. This is prepared
source with remaining operator/review prerequisites, not an approved release.

## Source and instructions

- Canonical SSH repository:
  `git@github.com:vpsfreecz/vpsadmin-rust-client.git`.
- Default branch confirmed by both GitHub repository metadata and live SSH refs:
  `main`, at `945af6a97717a7a6373507bbc9592d5cd53727c2`.
- The canonical bare clone's local `main` remains old
  `b67a3ba5eef89b2bd6533050aa8769aaa0574114` and has no `origin/main` ref. Audit
  reads used the exact live object already present in the bare store. Do not
  start release work from the stale local branch or reuse another session's
  registered worktree.
- Read `AGENTS.md`, `README.md`, `docs/development.md`, both workflow files,
  package/toolchain metadata, provenance and regeneration/check helpers from
  exact current main.
- Local instructions require the pinned Nix shell; generated
  `src/generated/**` is generator-owned and must never be hand-edited. Fix
  HaveAPI then regenerate using the retained schema and exact formatter.
  Handwritten and generated changes remain separate commits. There is no hook
  framework. Crate SemVer is independent from target API 7.0.
- Workflow files already exist on the default branch and are reported active:
  `.github/workflows/ci.yml` (`Rust client`, ID 389779539) and
  `.github/workflows/release.yml` (`Publish crate`, ID 392586616).

## Complete relevant input graph

| Input | Exact source / contract |
| --- | --- |
| Crate source | `945af6a97717a7a6373507bbc9592d5cd53727c2`, `vpsadmin-client` 0.1.0 |
| Saved API | `schema/api-7.0.json`, protocol 2.0, explicit API 7.0, public unauthenticated capture at `2026-10-19T16:54:51.865940+00:00` from `https://api.vpsfree.cz/v7.0/` |
| Schema digest | `70f89335e15263fd7177f29a00fab04b5ff1923c6922dfd318b07c3ae922fb8d` |
| Coverage | 152 resources, 524 actions (519 API + 5 authentication), 8720 parameters; plugin completeness unknown |
| HaveAPI generator revision | `68cc80b012b7a6b9bcdf35c008c338cbc3f4c000`, version 0.29.0; live retained public ref `2026-10-18-rust-client-generator-reviewed-68cc` |
| Generator source digest | `b2f1408d9a53eda4bdf33054f4293e5e1ae712d69c66863e6c0ee71902bcfc13` |
| Generator Ruby lock digest | `7ab15ed0bf0ded01fbb03f2f8e6b4ad73ef2806b1ee9199acea8a5269080b2f1` |
| Copied runtime digest | `9c50b8167a8b82118ba42372633e3b004276ba49fbdfed75d4979a913feea739` |
| Toolchain input | nixpkgs `fe13242281a67641c0102cdb1087f0ebe586c7df`, NAR `sha256-zp8ToDMnqZcu4o4IH9pdwXFXGp7yLm/M0dEnNWnyd7I=` |
| Recorded compiler tools | rustc 1.98.1, cargo 1.98.0; exact `rustfmt 1.9.0`; edition 2024; MSRV 1.95 |
| Runtime dependencies | reqwest 0.13.5 with JSON/rustls and optional blocking; serde 1, serde_json 1, url 2.5; exact resolution/checksums in committed Cargo.lock |
| Generation options | `generator.toml` matches provenance: package/version, MIT, edition/MSRV and formatter |

A quick independent Git-blob inspection reproduced schema, generator, Ruby-lock
and runtime digests above; checked all **686** generated file SHA-256 entries;
and proved all **8** runtime files byte-equal to the retained HaveAPI source.
No compiler, server or registry mutation was used for this check.

`git diff` between retained generator `68cc80b...` and HaveAPI's current upstream
`a32b15e379f44fc6dae4b15ef4ec17a142e5f465` is empty for generator lib/templates,
runtime source and Ruby lock. Only component docs/specs differ. The crate has
ordinary registry Rust dependencies, no HaveAPI crate/path/Git dependency.
It therefore need not wait for HaveAPI 0.30 publication. Keep truthful existing
provenance rather than relabeling it as 0.30. A deliberate later generator
refresh requires regeneration/provenance review; it is not necessary merely to
publish this initial package.

## Verification and history evidence

Current exact-head runs:

- [39739951412](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/39739951412):
  completed successfully at `945af6a...`.
- [39600821857](https://github.com/vpsfreecz/vpsadmin-rust-client/actions/runs/39600821857):
  also completed successfully at the same head.

Checks API confirms green `client (async)`, `client (blocking)`, `msrv` and
`regeneration` jobs. Current workflow tests all targets in both modes, builds
documentation and runs `cargo package --locked`, tests both modes under Rust
1.95.0 and performs deterministic regeneration with the exact saved HaveAPI
revision. Job-step evidence for the latest run confirms its package/doc and
generation steps succeeded. The legacy commit-status endpoint reports zero
statuses/pending; actual Check Runs and Actions evidence are authoritative here.
An initial `actions/runs?head_sha=...` query unexpectedly returned an empty list;
the complete run listing plus per-commit Check Runs corrected that incomplete
observation. No rerun was dispatched.

No independent final review receipt is present in the inspected source/history.
A ref named `2026-10-18-rust-client-generator-reviewed-091bd70` is not review
proof. Its commit `091bd70954d270f3e575a71a8a5a1884eed2eccd` is **not an ancestor**
of current main. Its final-tree delta to current main is only
`docs/development.md` (two changed lines) and `schema/provenance.json` (one changed
line), but this audit does not certify reviewed equivalence or migration/history
approval. No other session's private review records were read. Before claiming
the crate independently reviewed, obtain legitimate exact-head/whole-history
review or supported reviewed-equivalence evidence; if unavailable, commission a
current independent review. This audit itself neither triggers publication nor
substitutes for that review.

The visible base-to-head history contains four commits after empty base
`b67a3ba...`: handwritten package, generated public API client, README refinement,
and guarded manual publication workflow. There are no database migrations.
History assessment belongs in the applicable review packet, not a claim inferred
from commit/ref names.

## First-publication setup and commands

Implementer1's [registry evidence](registry-readiness.md) checked actual
`https://crates.io/api/v1/crates/vpsadmin-client` at 14:55:09 UTC and observed
404. That does not reserve the name or establish account ownership.

GitHub API currently lists **zero environments** for this repository; direct
`release` environment and its secrets endpoints return 404. Therefore the
required protected environment has not been prepared. No token/secret value
was read. Account verified email, API-token owner/scope/expiry, intended initial
crate ownership and ability to create `vpsadmin-client` remain unobserved.

Before a later explicitly approved bootstrap:

1. Complete the required review/verification evidence for the selected source.
2. Have the owner prepare GitHub environment **`release`** with required
   reviewers and intended version-tag restrictions. The workflow names this
   environment but does not itself prove protection exists.
3. Confirm the crates.io account's verified email and least-privilege token
   capability for the initial publication. Configure that token as environment
   secret **`CARGO_PUBLISH_BOOTSTRAP_TOKEN`** through the authorized secret path;
   never put it on a command line, in a receipt, or in a Git object.
4. After explicit release authorization and a fresh remote/source check, create
   the reviewed version tag **`v0.1.0`**. Preserve that tag after publication.
5. Dispatch the existing guarded workflow explicitly in bootstrap mode:

   ```sh
   gh workflow run release.yml --repo vpsfreecz/vpsadmin-rust-client \
     --ref v0.1.0 -f authentication=bootstrap
   ```

This command is recorded, **not executed**. Tag publication/dispatch and account
configuration remain separate external mutations requiring release direction.
The workflow validates repository/package/tag, checks the remote tag's commit,
reuses `ci.yml` as a verification gate, then waits for the protected environment.
It rejects bootstrap unless the token exists and the actual crate lookup returns
404. It prepares Nix tools before exposing credentials and supplies the token
only to `nix develop --command cargo publish --locked`. No local `cargo login`
is needed. The workflow does not automatically create a GitHub Release.

After a confirmed first upload, the crate owner can register this exact
**crates.io trusted-publisher tuple**:

| Field | Value |
| --- | --- |
| Crate | `vpsadmin-client` |
| GitHub owner | `vpsfreecz` |
| Repository | `vpsadmin-rust-client` |
| Workflow filename | `release.yml` |
| Environment | `release` |

Subsequent approved versions use `authentication=oidc` (the default),
`id-token: write` and the existing official crates.io authentication action.
OIDC failure never falls back to the bootstrap token. After first-publication
verification, follow the repository's documented token revocation/environment
secret removal and configure the OIDC binding; none of those actions was taken.

## Recovery and compatibility

No server deployment, database migration or node coordination is needed.
Async/blocking crate versions can coexist while API 7.0 remains available.
The captured public surface is not proof of complete privileged/plugin coverage.
Generated public interface/MSRV changes need deliberate crate versioning.

If upload status is uncertain, inspect actual registry version/checksum state
before retrying. The first bootstrap path intentionally refuses once the crate
exists; do not try to overwrite an accepted version. Preserve exact tag and
source. A new version or owner-authorized recovery may be needed. Package dry
runs/CI prove compilation and packaging, not account authentication or upload.
Consumer rollback pins an older crate/lockfile and cannot reverse server actions.
