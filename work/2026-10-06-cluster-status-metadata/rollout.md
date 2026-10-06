# Deployment record

Status: aitherdev system deployment passed. Application activation is prepared
and blocked by three additional unfinished archives awaiting user direction.

The user authorized aitherdev deployment and integration of the three affected
master branches after verification. The runtime is e3315a483f3d3536d492ecbe40f2655449cf630f;
configuration 165e465ae5be6ad1706e0528d537011616d20efb and workspace
ef529ec8bfb85e8c2d939ef69bdac2204fefdfc7 select that exact runtime. The workspace
head is a patch-equivalent rebase of checked a296f66f onto current shared master;
its package output is identical and its inherited instruction check passed.

Before deployment, aitherdev's system generation is
/nix/store/98s4gm1ifnvljbap8hgd6vvg7bb885an-nixos-system-aitherdev-26.05.20261004.0d9e9b8.
The selected application profile is
/nix/store/h73nvgmdlwq2ccsnr2499qdlxnj9qrdx-dev-workspace-0.2.0.
The active portal unit is workspace-portal@vpsfree-cz.service.
The cluster's runner and retained disk identities are recorded without
credentials in cluster-before.json. No guest or cluster mutation is needed.

Prepared host deployment uses confctl's exact
cz.vpsfree/machines/aitherdev selector, dry activation first, then switch, from
the checked configuration feature worktree. Prepared application activation uses
the stable workspace-host switch command from the checked workspace feature
worktree. Both scripts enforce source heads and clean tracked trees; the
application script also enforces the previous profile identity. They have been
syntax checked. Host deployment was executed; application activation has not run.

Original activation blockers were recovered after the user authorized their
existing archive operations. An ordinary
retry hit administration names Git had reused for two fix-owned worktrees;
the owned clean worktrees were temporarily removed around the normal archive
retry, then restored at unchanged heads. Recovery exited 0 and both lifecycle
receipts cleared. Three additional unfinished archives now block activation,
listed in state.md; their recovery direction is pending. Preserve their receipts
and the supported profile preflight. Supported recovery is the ordinary archive retry; application
recovery remains forward-only through the stable package-transition commands.

Host deployment completed with exit 0 in 109 seconds. Confctl dry activation and
switch selected built generation 2026-10-06--20-46-15. Both system/firewall health
checks passed. New system store path:
/nix/store/4q2w8x1h0aavywk3qc031wnzr466zd9m-nixos-system-aitherdev-26.05.20261006.b253099.
Named user unit dev-cluster-status-host-deploy.service reports Result=success,
ExecMainStatus=0, active/exited, MainPID=0. Full output is host-deploy.log.

Live acceptance still requires the existing storage cluster card to
show ready/running with services, no status-decode error, and preserved runner
and disk identities. Retain the same feature branches after fast-forward merges.
