# Completed HaveAPI downstream release

HaveAPI 0.32.2 is consumed by vpsAdmin and merged. All three clients were
regenerated. Only TypeScript produced code changes, so it received the minor
0.3.0 release. The final configuration vpsadmin channel update is merged.
No production machine was deployed. The session remains open.

| Repository | Remote default / exact final feature head | Outcome |
| --- | --- | --- |
| vpsadmin | master / 5586ea8ab7dbf7e116083b0ea1819ea4d17f66a5 | Five HaveAPI gems and exporter pins coherently updated to 0.32.2 |
| vpsadmin-go-client | master / 134a9e69f9aa6ddec5c94b53744865c6f81ecdd0 | 682 generated files unchanged; no commit or release |
| vpsadmin-rust-client | main / 3ec8c045dcefcca85b60ffccd38259cda29eeb60 | 686 generated source hashes unchanged; reviewed provenance refresh merged, no crate release |
| vpsadmin-typescript-client | main / d354491537f8b654b4d2c33a705cad84474f95d6 | v0.3.0 tag and npm package published |
| vpsfree-cz-configuration | master / 0d71dd289feeb1ea2686f9c7cf0f93728baf9bd2 | Only vpsadminServices selects the verified vpsAdmin head |

Fresh explicit fetch/SSH reads prove all five exact final feature heads equal
remote defaults, are ancestors of fresh tracking refs and have clean worktrees.
All four short merge claims are released and verified. Feature refs/worktrees
and exact generator source inputs remain; disposable detached merge targets
were removed only after integration/ownership proof. No session lifecycle action.

## Verification and reviews

- vpsAdmin: 28 focused examples, tooling syntax/style, gem-byte/Nix hash checks
  and required hooks passed. Required local services-up passed all 34 checks,
  including packaged documentation and generated client examples.
- Go: two fresh generations and actual-tree generation match all 682 existing
  files; formatting and compilation passed. Zero-range comparison is unsupported
  by the portal and was recorded honestly.
- Rust: deterministic generation, provenance/lock identity, formatting and ten
  refusal tests passed. No new compile/MSRV claim for unchanged code.
- TypeScript: deterministic/source-refusal, 13 tests/build, strict typechecks
  and packed actual-runtime consumer passed; exact-head CI validation also passed.
- Configuration: all 64 lock nodes compared, only the intended three locked
  fields changed. Evaluation covers 109 entries and all 17 intended consumers.
- Retained independent reviewer0, Sol/xhigh, found no findings in A/C/D/E;
  complete history/repeated-stream and explicit no-migrations conclusions retained.
  Broad long vpsAdmin CI was not awaited, as requested.

## Publication identity

TypeScript original tag workflow 41538988296 attempt 1 and immutable artifact
13184014717 succeeded. Annotated tag object
5a51d6b108da9e57b10494bdf089b61a270b167b peels to the exact integrated head.
The npm 0.3.0 tarball is byte-identical to the approved original artifact:
SHA256 57236647f4065a0ffeaabb0f5f6c64370a5ca4e7e530876b0d562c69651ce610.
The owner and lead independently verified registry integrity/downloaded bytes.
Exact peer runtime remains haveapi-client 0.32.0, as required by this generator.
[Publication receipt](typescript-release.md) retains integrity, signed-payload
binding and initial processing/visibility observations; no retry or rebuild.

## Evidence and remaining work

[State](state.md), [design](design.md), [vpsAdmin](vpsadmin-package.md),
[Go](go-package.md), [Rust](rust-package.md), [TypeScript](typescript-package.md),
[configuration](configuration-package.md), [services-up closure receipt](services-up-receipt.md),
[reviews A](review-a-result.md), [C](review-c-result.md), [D](review-d-result.md)
and [E](review-e-result.md).

No remaining implementation, required check, review, integration, publication,
approval or resource-release task. No known blocker. No machine deployment or
live production activation is claimed.

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-haveapi-vpsadmin-release/
