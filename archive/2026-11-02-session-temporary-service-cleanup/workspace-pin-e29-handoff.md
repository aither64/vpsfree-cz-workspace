# Final workspace runtime pin handoff

Owner: implementer1, retained Sol/xhigh/workspace_write. Bound identity matched;
both DEV_SESSION markers were absent. Settings/access remain unchanged.

The final workspace pin is committed and clean at
`00381d14448206aa4fe93cc71f310ef4e925603b`, tree `d212ad426171d858a4d3279f69cc4943847de699`. It selects
published runtime `e29d4d83fc62e0dc929aca332f324336c9c8b034` and passes the single
final cross-lock check against configuration `abee6aec3ade96eb902132bea11d2eba2d6c8119`.
**Unpublished; awaiting the retained reviewer's final history/graph conclusion.**
No application/source build, CI observation, claim, default integration,
deployment or session lifecycle action occurred. All command effects are
reconciled, no operation is running, and the workspace Git lane is returned.

## Final series and consolidation

Fresh fetch retained origin/master `6383e8848c92c06a9d817f8109853b5b61305c89`.
Shared master/review base remains `ef09cf555332afebafb276e3ae54cc1f5ea6012c`, an
ancestor of the feature. No rebase or shared-master/index mutation was needed.
There is no published workspace feature ref. The complete own range is:

1. `c474bcc55b04459dd936d2e4d8bea358b2b84184` — reviewed instructions, unchanged.
2. `00381d14448206aa4fe93cc71f310ef4e925603b` — one final mechanical runtime selection.

Four files, 25 insertions/6 deletions overall. The pin alone changes only
`flake.nix` and `flake.lock`, 5 insertions/5 deletions. It was generated with
`nix flake update vpsfree-dev-workspace/dev-workspace`, then committed through
the normal Nix shell, temporary message file and declared hook policy. The
workspace declares no hook framework and has no active hooks; none were bypassed.

The unpublished old312 pin `25282ddfcade59a8bd904f3638a7c45b3d117d30` was replaced
by amending its logical update, rather than accumulating another pin commit.
It is absent from final ancestry and remains at
`2026-11-02-session-temporary-service-cleanup-workspace-pin-312` with the full
[old receipt](workspace-pin-312-handoff.md), [old JSON](workspace-pin-312-receipt.json),
graphs/metadata and old matching pass intact. Range-diff shows unchanged
instructions and only the runtime pin replacement. No migration or release,
deployment or externally consumed state boundary requires an intermediate pin.

The earlier instruction rebase from
`6383e8848c92c06a9d817f8109853b5b61305c89..1a22338c7317b639e70372626b3f20528d641619`
to `ef09cf555332afebafb276e3ae54cc1f5ea6012c..c474bcc55b04459dd936d2e4d8bea358b2b84184`
was exactly patch-equivalent. Historical portal registration base stays unchanged.
There are no DB migrations or new runtime/source behavior in this pin package.

## Exact sources and graph

The direct nested `vpsfree-dev-workspace/dev-workspace` URL/lock now selects
`e29d4d83fc62e0dc929aca332f324336c9c8b034` from original baseline
`c2182254d29c4175c3e9fe4267e5a92dd1da6b79`. Strict comparison to the original
c474/c218 baseline confirms all 34 other nodes (35 total), extension and every
input/follows path unchanged. Only runtime locked revision/NAR/time and original
revision changed. No top-level input, extension lock edit or deduplication.

- Runtime source: `/nix/store/snbsx4bqra8nkr8qsy6h13mydriq79sj-source`.
- Runtime NAR: `sha256-f3UjSBS9+zyEULhOdBjiBG04aDiqTKNsjzuwokIYzJ4=`.
- Runtime accepted tree: `9b93683362e149ba6f2599232bc1fbbbe4694a17`.
- Preserved extension: `e4e7e95ed39bf514b33f8f8ae61ba9868de060ae`.
- Extension NAR: `sha256-5tnBT6j5LzwkYTffhWQ7mWpDkWMisxbCpFpbtDOjBlc=`.
- Final workspace source: `/nix/store/58nj5a33lxqd75x9zlm9vh5bkf00iz3p-source`.
- Workspace source NAR: `sha256-7JlJ3kwNhgW15N179v3MbaAj2fh8s0tiChvMSaGFX7s=`.
- Workspace lock SHA256: `a75b24bfa5da6f485747dac8c5ae895dab3476846f118046118cc8f4b4f1686d`.
- Workspace flake.nix SHA256: `3de6f6368d4fc83e830db641e2314e5d6a278c76520f404e5cc1dc51a2b973e5`.

The exact-commit Nix metadata source revision and flake/lock bytes match the
final committed tree. Complete graphs, selectors, follows and locked identities
are retained below. Whole-range whitespace, exact parent/series/ref identities,
clean index/worktree and committed pin-byte assertions passed.

## Final matching check

The single final check passed exit 0, with both commit identities, clean statuses
and exact lock hashes verified before and after:

```sh
nix develop --no-update-lock-file -c bin/check-dev-workspace-deployment \
  --workspace-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/workspace \
  --configuration-root /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-02-session-temporary-service-cleanup/vpsfree-cz-configuration
```

It verifies canonical portal identity and the matching exact e29 runtime. The
actual runtime locked identity/NAR is equal in both complete locks. Nix's local
sparse-worktree dirty warning does not represent tracked changes: pre/post Git
checks are clean, lock hashes unchanged and exact committed source bytes match.
No source adjustment or application build was performed.

Configuration: head `abee6aec3ade96eb902132bea11d2eba2d6c8119`, tree
`3161a034c01880e905a58499137f0d85d3029bed`, base/parent/origin-master
`c040c14cdbacc07998700b524996a89306188d7f`. Lock SHA256:
`9fc3abbb3d728ed4ddcf0a34540f7ffa59a21e3466cf284f153ff5e8aa2f97c9`.
Source `/nix/store/323lhjf58hm1ywj00i9jpyxwg5v6d1rg-source`, NAR
`sha256-ljGS/zjifseFn51YRnnQLhqH0jGpnuSagJV11MmKodY=`. A's final proof retains
its 64-node graph, preserved other nodes/edges/follows and one generated final
commit. The old configuration312 pin is retained outside final ancestry.

The old312 matching pass remains historical evidence only; this new receipt
binds only the corrected final snapshots above. Runtime CI41509697499 remains
owned by lead's watcher and was not polled here.

## Evidence and remaining gate

- [Full final receipt and workspace graph](workspace-pin-e29-receipt.json)
- [Original-baseline graph proof](workspace-pin-e29-graph-proof.json)
- [Full composed input graph](workspace-pin-e29-full-graph.json)
- [Complete own diff](workspace-pin-e29-base-to-head.diff)
- [Old/new range-diff](workspace-pin-e29-range-diff.txt)
- [Exact workspace source metadata](workspace-pin-e29-metadata.json)
- [Generated update log](workspace-pin-e29-update.log)
- [Final matching-check receipt](workspace-pin-e29-deployment-contract-receipt.json)
- [Final matching-check output](workspace-pin-e29-deployment-contract.log)
- [A's final configuration graph/history proof](config-pin-final/graph-and-history-proof.json)
- [Old312 snapshot and provenance](workspace-pin-312-handoff.md)

The retained reviewer must conclude whole-branch history/graph correctness for
both final mechanical pin streams. Mechanical content needs no standalone
review. Lead owns that conclusion and any later publication assignment. B is
source/Git idle; no push, build, claim, integration or deployment is authorized
by this handoff.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
