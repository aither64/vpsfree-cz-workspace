# aitherdev workspace cutover

`bin/aitherdev-workspace-cutover` is the fail-closed operator procedure for the
one-time workspace namespace deployment. It deliberately stops every managed
session and creates fresh tmux and Codex client processes. It does not preserve
running processes, panes or tmux identities. Eight currently running Codex
sessions resume their already recorded conversations, one currently running
shell-only session remains shell-only, and the stale authority for the archived
session is stopped and not recreated. Active tracking without a runtime
authority remains dormant.

Before `prepare`, fetch the feature refs, fast-forward the registered workspace
root to the reviewed workspace head, and create the immutable compatibility
worktree at commit `120de27e384987e042c1b9424da20418cd0d56fe`:

```sh
git worktree add --detach \
  worktrees/2026-09-09-workspace-components/workspace-compat \
  120de27e384987e042c1b9424da20418cd0d56fe
```

Run the phases in order:

```sh
bin/aitherdev-workspace-cutover prepare REVIEWED_WORKSPACE_COMMIT
bin/aitherdev-workspace-cutover forward
bin/aitherdev-workspace-cutover accept
```

Pass the full exact workspace commit accepted by the final review to
`prepare`. The script records it in the cutover state and rechecks the same
commit and package-relevant working tree immediately before activation.

`prepare` is the first mutating phase. Before any mutation it verifies the exact
ten-authority and three-cluster inventories and proves the active/archived and
Codex/shell-only classification described above, including the one dormant
active tracking set. It then closes an independent systemd admission gate,
records credential and TLS state, resets the clusters,
stops every audited authority and service, selects the compatibility package,
preserves the stray test recovery tree, masks certificate renewal, and runs
both migration preflights.

`forward` repeats all stopped-state and migration gates, performs both
journaled state migrations, builds and switches the aitherdev configuration,
selects the final registered-root package, and starts fresh processes for the
nine active sessions. The archived authority remains retired and dormant
tracking remains dormant. The router stays behind
the systemd admission gate and certificate renewal remains masked.

`accept` verifies the final package, exact conversation identities, authority
and process environments, extension commands, credential/TLS inventory and an
authenticated HTTPS request. It opens the router only after the local checks;
a failed TLS or authenticated request closes admission again.

This is a forward-only site procedure. `prepare` and `forward` accept their own
recorded in-progress stage, so after a failure, leave the router closed, fix the
concrete problem in place and repeat that same phase. Cluster resets, authority
stops, package selection, migration journals and session starts are handled
idempotently. The script does not provide an automated rollback path.

The state file is
`~/.local/state/aitherdev-workspace-cutover-20260911.json`. Keep it and both
migration journals until the deployment is accepted. The preserved test
recovery tree remains at
`~/.local/state/dev-workspaces-test-recovery-20260911`; it is not live state
and must not be deleted as part of this deployment.
