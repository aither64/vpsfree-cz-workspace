# Dev cluster requires the vpsAdminOS flake revision

Related initiative: `work/2026-06-15-vpsadmin-events/`

## Symptom

Starting the vpsAdmin dev cluster failed during Nix evaluation with:

```text
The option system.vpsadminos.revisionDirty does not exist.
```

The initiative's `vpsadminos` worktree was a clean detached checkout at an old,
unrelated feature revision. The dev-cluster flake overrides both its direct
`vpsadminos` input and vpsAdmin's nested `vpsadminos` input with that worktree,
so the stale checkout replaced the compatible revision from vpsAdmin's lock
file.

## Fix

Inspect the revision pinned by the vpsAdmin worktree and switch the clean
detached vpsAdminOS worktree to that exact commit before starting the cluster:

```sh
git -C worktrees/<slug>/vpsadminos switch --detach <pinned-revision>
dev-clusters/vpsadmin/bin/devcluster start <slug> \
  --topology single --network bridge
```

For this initiative, the compatible revision was
`736f689391bc3f920e808eb574662ed6a9e6c955`.

## Verification

Nix evaluation and the full cluster build completed. The cluster reached
`ready: yes` on the bridge network, all notification services were active, and
`nodectld` was running on `node1`.
