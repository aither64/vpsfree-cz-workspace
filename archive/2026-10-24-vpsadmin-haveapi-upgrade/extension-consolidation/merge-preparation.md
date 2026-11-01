# Prepared extension master integration — lead execution only

The single final review alias remains `vpsfree-dev-workspace-services-os`, exact checked/published **e4e7e95ed39bf514b33f8f8ae61ba9868de060ae/treec4bc21bdf5274f9159866b2b22a10818ec3bc41b**. Default/master remains **767dfd587e346168e1443e65ccdb67ce748f3fe3** in the latest independent canonical SSH observation. No target movement or rebase occurred.

E0 prepared a clean detached scratch target at:

`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-merge-target-e4e7`

HEAD is exactly767, detached, with the canonical bare common Git directory `repos/vpsfree-dev-workspace.git`. This checkout is integration machinery only; it is not another review candidate. All old feature worktrees/refs/private inputs and roots remain intact. No claim, merge or default push has been performed by E0.

[Preparation bindings](merge-preparation.json), [actual0/0 acceptance](acceptance.json), [complete source/output/root/effects receipt](postreview-receipt.json), [publication proof](publication.json), [accepted review](review-acceptance.md), [full history and final diff](review-packet.md).

The four-commit reviewed series retains literal deployedd632→bd66, then original-author bootproofa781 and writinge4e7. Exact mapping, fixture conflict resolution and whole-history/NO MIGRATIONS are accepted by reviewer0 native01a192e4-d4d4-72e2-bd44-f548a632bd28 all4/HIGH. Original51233 passed fullflake0 (56/833 commands once) then full ordinary installedchecker0 (config-export/12refusals/allphases/bothrunners). CI [Check41226322173](https://github.com/vpsfreecz/dev-workspace/actions/runs/41226322173) was observed in_progress at exacte4e7; no CI success is claimed.

## Prepared environment and ordinary hooks

Target AGENTS was read. There is no declared hook framework, core.hooksPath or active nonsample hook. No hook configuration or trust was changed. The ordinary declared environment was prepared successfully with Git2.54.0 at `/nix/store/5vpcfsdx1lcnlb2y4k7xyc74shp5qwbh-git-2.54.0/bin/git`, retained under `/tmp/e0os-e4e7-final-4841_p4d/merge-shell`.

Enter the existing cached declared shell **before** requesting the repository claim; keep all following critical commands in that shell:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-24-vpsadmin-haveapi-upgrade/vpsfree-dev-workspace-merge-target-e4e7
nix develop --profile /tmp/e0os-e4e7-final-4841_p4d/merge-shell .#checks.x86_64-linux.tests -c bash
```

No tests need repeating because source/input identities are unchanged. No build/profile/cluster/machine operation is part of this merge.

## Short repository claim and merge sequence

Lead already owns integration approval and performs this sequence. The prepared [schema1 request](merge-claim-request.json) selects only the registered extension alias/canonical repository; it has no machine resource. Its fresh request ID is `dd73610d-694e-4d80-a77d-cf69a5d75d03`. E0 has **not** submitted it. If lead uses another request, use a fresh UUID.

Acquire and inspect authoritative status, proceeding only when that exact claim is held:

```sh
dev-session coordination acquire 2026-10-24-vpsadmin-haveapi-upgrade --as-is --request /home/aither/workspace/ai/vpsfree.cz/work/2026-10-24-vpsadmin-haveapi-upgrade/extension-consolidation/merge-claim-request.json --json
dev-session coordination claim-status 2026-10-24-vpsadmin-haveapi-upgrade --as-is --id dd73610d-694e-4d80-a77d-cf69a5d75d03 --json
```

Within the held claim, freshly verify current feature/head, clean detached target, exact ancestry and canonical remote default/feature. Expected outputs are featuree4e7 and master767. A changed target requires stopping/releasing and reconciling outside the claim; do not silently merge a different range.

```sh
git rev-parse HEAD
git status --porcelain=v1
git symbolic-ref -q HEAD
git rev-parse refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os
git merge-base --is-ancestor 767dfd587e346168e1443e65ccdb67ce748f3fe3 e4e7e95ed39bf514b33f8f8ae61ba9868de060ae
git ls-remote --symref git@github.com:vpsfreecz/dev-workspace.git HEAD refs/heads/master refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os
```

`symbolic-ref` must exit1 with no output because the target is detached. After guard inspection, ordinary fast-forward merge and nonforce SSH publication:

```sh
git merge --ff-only e4e7e95ed39bf514b33f8f8ae61ba9868de060ae
git rev-parse HEAD
git status --porcelain=v1
git push git@github.com:vpsfreecz/dev-workspace.git HEAD:refs/heads/master
git ls-remote --symref git@github.com:vpsfreecz/dev-workspace.git HEAD refs/heads/master refs/heads/2026-10-24-vpsadmin-haveapi-upgrade-services-os
```

Expected final HEAD/master/feature are exacte4e7; the target remains clean. Inspect normal merge/hook output before pushing; Git success can conceal a post-merge hook error. A push uncertainty requires exact remote effect reconciliation under the same original claim, never an unguarded retry.

Once the approved merge/push/readback effects are known safe, promptly release this exact repository claim and verify released state **before** CI, records or any other work:

```sh
dev-session coordination release 2026-10-24-vpsadmin-haveapi-upgrade --as-is --id dd73610d-694e-4d80-a77d-cf69a5d75d03 --json
dev-session coordination claim-status 2026-10-24-vpsadmin-haveapi-upgrade --as-is --id dd73610d-694e-4d80-a77d-cf69a5d75d03 --json
```

This independent extension scratch merge needs no shared-workspace tracking lock. The later shared workspace/master integration has its own mandatory claim-then-nonblocking-tracking-lock procedure. No machine claim is acquired or released here. The scratch worktree and all roots remain preserved; preparation/handoff does not authorize cleanup or session lifecycle action.

[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-vpsadmin-haveapi-upgrade/)
