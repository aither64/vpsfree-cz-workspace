# Final workspace runtime pin handoff

Workspace head `2c5f6cdb59995700bc33026c7c1e27e71b4d893a`, tree `1c0c706d7dbacff04e6521bddbbfdbbecda99587` is committed,
clean and unpublished. It selects final published runtime
`3d76f527a6b88e9d32c202f729a1a0d673b341f2` and passes the single final matching
check against configuration `46e281115294e5d45286b60c8ff862ac287d862b`. All effects are reconciled,
no operation is running, and the workspace Git lane is returned. Same-reviewer
final whole-history/pin conclusion remains pending; this is not publication,
default integration or deployment authorization.

Owner: retained implementer1 Sol/xhigh/workspace_write; bound session matched,
both DEV_SESSION markers absent. Settings/access unchanged. No workspace push,
application/system build, CI wait/polling, claim, integration, activation or
session lifecycle action occurred.

## Complete series and consolidation

Fresh origin/master stays `6383e8848c92c06a9d817f8109853b5b61305c89`; shared
master/review base stays `ef09cf555332afebafb276e3ae54cc1f5ea6012c`. Both remain
ancestors of the feature. No rebase or shared master/index mutation was needed.
Complete own series:

1. `c474bcc55b04459dd936d2e4d8bea358b2b84184` — reviewed instructions, unchanged.
2. `2c5f6cdb59995700bc33026c7c1e27e71b4d893a` — one final generated runtime selection.

Overall4files25insertions/6deletions; pin alone only `flake.nix` and `flake.lock`,
5insertions/5deletions. Normal Nix-shell/tempfile amend preserved hook policy;
no hook framework or active hook files are declared and none were bypassed.
The direct nested URL was updated and lock generated with
`nix flake update vpsfree-dev-workspace/dev-workspace`.

The same logical update stream was replaced/consolidated, not accumulated:
old312 pin `25282ddfcade59a8bd904f3638a7c45b3d117d30` and e29 pin
`00381d14448206aa4fe93cc71f310ef4e925603b` are outside final ancestry and
retained at explicit `...-workspace-pin-312` / `...-workspace-pin-e29d4d83`
recovery refs. Full [312 receipt](workspace-pin-312-handoff.md) and
[e29 receipt](workspace-pin-e29-handoff.md), JSON/graphs/metadata/matching passes
remain unchanged and historical. Range-diff keeps instructions `=` and shows only
runtime selection replacement. No migration/release/deployed-state boundary
requires intermediate pins; no DB migrations or new behavior exists here.

Earlier instruction rebase
`6383e8848c92c06a9d817f8109853b5b61305c89..1a22338c7317b639e70372626b3f20528d641619`
→ `ef09cf555332afebafb276e3ae54cc1f5ea6012c..c474bcc55b04459dd936d2e4d8bea358b2b84184`
was patch-equivalent; the historical portal base remains intact.

## Exact sources and graph

Strict comparison to ORIGINAL c474/c218 baseline proves35nodes total, all34other
nodes unchanged, all input/follows paths and extension identity preserved. Only
runtime locked revision/NAR/time and original revision changed. No top-level
runtime input, extension lock edit, deduplication or sibling change.

- Runtime source: `/nix/store/qkv85x0hzq5kiv93s97wwqmdjsz7ndmz-source`.
- Runtime NAR: `sha256-nW2yN5CRj/4hlx1PvK0vCUn7Tkejc8ZiEKqfPO0ygU0=`.
- Runtime tree: `b9f7154cabbd95624dc447d87b855f2b01b33247`.
- Preserved extension: `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`.
- Extension NAR: `sha256-5tnBT6j5LzwkYTffhWQ7mWpDkWMisxbCpFpbtDOjBlc=`.
- Workspace source: `/nix/store/sb7hqr1dbsvl21s7y75ib2xb2ql4dak6-source`.
- Workspace source NAR: `sha256-OSBbXmWPFYYooseDUKMJa3yml11JP2z9d5w8j40Ob44=`.
- Workspace lock SHA256: `55cdebcc65c10f7333baa6f52af5385a560d995ca9388fb3001a86ca110885c4`.
- Workspace flake.nix SHA256: `f37bb31583021f97db0081f1abe807fce5a90ad6d4d88ec253fee15378af346b`.

Exact-commit metadata revision and flake/lock bytes match committed source.
Whole-range whitespace, exact parent/two-commit series/recovery refs and clean
index/worktree assertions passed. Runtime source/derivation/browser proof is in
[final runtime handoff](runtime-browser-final-handoff.md); no redundant suite ran.

## Final matching snapshot

One `nix develop --no-update-lock-file -c bin/check-dev-workspace-deployment`
invocation passed exit0 using these exact absolute roots:

- Workspace: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/workspace`.
- Configuration: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration`.

Both exact heads, lock hashes and clean statuses were verified before/after;
actual complete runtime locked identities/NARs compare equal. The checker
verified canonical portal identity and final3d76 selection. Nix emits its known
sparse-worktree dirty warning despite clean tracked bytes/status; explicit
commit metadata and pre/post hash proofs bind the actual checked source.
Old312/e29 matching results remain historical and do not substitute for this check.

Configuration head `46e281115294e5d45286b60c8ff862ac287d862b`, tree `c6230cc4950d12b357b8d53edb2b193e5b45a514`, base/parent
`c040c14cdbacc07998700b524996a89306188d7f`. Lock SHA256 `d8e4594f17393579f1b45b5fd4d53e2e7b0197d891a5becdfbe00c36e8e8d9dd`.
Source `/nix/store/dpyg2zil17nxlqhq7vwyhd12n9dd8wdg-source`, NAR
`sha256-bLYbZWfn5aI6COW2CesJVQn+Dw7pch3pCNnVzIIG9RY=`. A's proof covers the complete64node
graph, preserved mappings/edges/follows, one final generated confctl commit and
older pins retained outside final ancestry. Both final checkouts/indexes are clean.

## Review packet and next action

- [Complete final source/graph/check receipt](workspace-pin-3d76-receipt.json)
- [Original-baseline graph proof](workspace-pin-3d76-graph-proof.json)
- [Full composed graph](workspace-pin-3d76-full-graph.json)
- [Complete own diff](workspace-pin-3d76-base-to-head.diff)
- [Old/new range-diff](workspace-pin-3d76-range-diff.txt)
- [Exact source metadata](workspace-pin-3d76-metadata.json)
- [Matching-check receipt/exact command](workspace-pin-3d76-deployment-contract-receipt.json)
- [Matching-check output](workspace-pin-3d76-deployment-contract.log)
- [Configuration graph/history proof](config-pin-3d76f527/graph-and-history-proof.json)
- [Final runtime series/reuse/publication](runtime-browser-final-handoff.md)

Lead owns fresh runtime CI41518664500 monitoring and the retained reviewer's
final whole-history/pin conclusion across runtime, workspace and configuration.
Mechanical content needs no standalone content review. Workspace remains
unpublished; B is source/Git idle pending a later assignment.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
