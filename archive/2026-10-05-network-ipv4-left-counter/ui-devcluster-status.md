# Manual interface review cluster

The session-owned development cluster is running and ready. The supported
installed vpsadmin-devcluster provider started single topology on br0 and
selected clean V5d5527 and React W e4c49 feature worktrees.

- [PHP interface](https://webui.aitherdev.int.vpsfree.cz/)
- [React interface](https://newadmin.aitherdev.int.vpsfree.cz/)
- [Workspace portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-05-network-ipv4-left-counter/): use the Development clusters panel for login details.

Both UI endpoints returned HTTP 200 with TLS verified using the cluster CA;
the PHP endpoint also passed a direct-address check. No browser login or
interactive acceptance test was performed. See ui-devcluster-verification1-status.json
and ui-devcluster-http1.json. The cluster remains running for the user's review.

First startup failed while fetching the locked frontend npm archive with an
HTTP/2 framing error. The identical supported retry completed with exit 0.
State/config/credentials were preserved, without a dependency/source override,
reset or force flag. The kernel-named modules-shrunk jobs copy/filter existing
modules and are not kernel source compilation. See ui-devcluster-start1-failure.json
and ui-devcluster-start2.exit. Complete command output remains private.

This manual UI startup does not run local CI, activate new workspace packages,
integrate feature branches, or regenerate the two pending KB screenshots.
