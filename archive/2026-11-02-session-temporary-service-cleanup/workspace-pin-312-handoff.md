# Workspace runtime pin snapshot — held after CI failure

Owner: implementer1, retained Sol/xhigh/workspace_write. Bound session identity
matches; both DEV_SESSION markers are absent. Settings/access are unchanged.

The workspace pin commit completed before lead reported runtime CI failure.
**This unpublished pin is stale and held; it is not final readiness evidence.**
A owns runtime diagnosis/fixes. B will replace/consolidate the one runtime pin
stream only after a corrected published runtime is assigned. No publication,
application/source build, deployment, claim, integration or session lifecycle
action occurred. No operation remains running. Workspace Git lane is returned.

## Exact Git effects

- Review base/shared master: `ef09cf555332afebafb276e3ae54cc1f5ea6012c`.
- Fetched origin/master: `6383e8848c92c06a9d817f8109853b5b61305c89`.
  It remains an ancestor of shared master and feature. No rebase was needed;
  shared master/index were not mutated.
- Instructions: `c474bcc55b04459dd936d2e4d8bea358b2b84184`.
- Pin/head: `25282ddfcade59a8bd904f3638a7c45b3d117d30`.
- Tree: `05470f4d5306042360abc96f15d474e6289ce5d9`.
- Complete own series: instructions, then one mechanical selection update.
  Four files, 25 insertions/6 deletions overall; pin alone changes `flake.nix`
  and `flake.lock`, 5 insertions/5 deletions.
- Feature index/worktree clean. Normal Nix-shell commit used a temporary message
  file. No declared hook framework or active hook files exist; none were bypassed.

The reviewed instruction patch is unchanged. Its earlier range
`6383e8848c92c06a9d817f8109853b5b61305c89..1a22338c7317b639e70372626b3f20528d641619`
was rebased to
`ef09cf555332afebafb276e3ae54cc1f5ea6012c..c474bcc55b04459dd936d2e4d8bea358b2b84184`
with exact patch equivalence. Historical portal base remains unchanged.
No migrations or intermediate pin commits exist. This pin has not been published,
deployed or externally consumed. Preserve this range and graph when replacing it.

## Input graph and provenance

The direct nested `vpsfree-dev-workspace/dev-workspace` input changed from
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79` to published runtime
`312d2e2a8994c136f96938d2f2a71ae8e2f16f33`, generated with
`nix flake update vpsfree-dev-workspace/dev-workspace`. Of 35 nodes, all 34 other
nodes and all input/follows paths are unchanged. Only runtime locked revision,
NAR/time and original revision changed. No top-level input, extension lock change
or deduplication was introduced.

- Runtime NAR: `sha256-rGcsolzKwEqs7T09CF7QLU4hOvGD7JSI4nj+eeJOMmk=`.
- Preserved extension: `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`.
- Extension NAR: `sha256-5tnBT6j5LzwkYTffhWQ7mWpDkWMisxbCpFpbtDOjBlc=`.
- Lock SHA256: `1a3cdba00b3f3755a0f0416924e60773cc37885db1a86fb220f47bae892f82bc`.
- flake.nix SHA256: `7febe9071ab7e4ebdc9f3594f605b05e41e0d67c28316bd9397ccf045b62ce60`.
- Exact committed workspace NAR: `sha256-s/MCP2U7X5lmfKJm2FBefNeFW6Z5K9PEXz1JD3Kp4Gk=`.
- Exact source: `/nix/store/ci4450sb8ckp2kbyfasfjbm4p24l1m0k-source`.

Unqualified sparse-worktree metadata reported a dirty revision despite clean
Git status/index/diff. The already-started explicit exact-commit metadata export
completed successfully and matches committed flake/lock bytes. Both exports are
retained; no source adjustment was made.

## Old-snapshot cross-lock evidence

The single agreed checker passed, exit 0, in the repository Nix environment:

```sh
nix develop --no-update-lock-file -c bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration
```

It verified canonical portal identity and matching exact runtime312d selection.
This result applies only to that old snapshot and must be repeated after both
corrected final pins exist.

Configuration snapshot: head `7b6d1a12571507eebf59de75806cd922b666788c`,
tree `b02408d963244d87ba13e2a71236489f32305d21`, base
`c040c14cdbacc07998700b524996a89306188d7f`, lock SHA256
`142d0f3401f9dbfac425c960421003169a54264d042e0f0b46e6d06fd3c10db9`.
Its 64-node graph preserves other nodes and all input/follows edges; its runtime
revision/NAR matches this workspace snapshot. Both checkouts/indexes were clean.

Whole-range whitespace and committed pin-byte checks passed. Nix prepared its
shell environment; no application build or long test was launched. Final reviewer
whole-pin/history conclusion waits for corrected source and both final pins.

## Retained evidence and next action

- [Machine-readable receipt](workspace-final-pin-receipt.json)
- [Graph comparison](workspace-pin-semantic-check.json)
- [Full graph](workspace-final-pin-input-graph.json)
- [Complete own diff](workspace-final-base-to-head.diff)
- [Cross-lock output](workspace-config-deployment-contract.log)
- [Exact commit metadata](workspace-final-pin-exact-commit-metadata.json)
- [Configuration graph proof](config-pin-graph-proof.json)

B is source/Git idle. Await corrected published runtime assignment, then replace
the stale pin, consolidate one mechanical stream and repeat matching verification.
Do not publish until the retained reviewer's final graph/history conclusion.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
