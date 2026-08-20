# Dev cluster virtiofs worktree added after startup

Related initiative: `work/2026-08-18-vpsadmin-password-reset`.

Command:

```sh
dev-clusters/vpsadmin/bin/devcluster update <slug> services
```

Symptom:

An in-place service update switched the application successfully but exited 4
because `mnt-configuration.mount` failed. The mount source was the virtiofs tag
`config`, while the running QEMU process had no corresponding
`services-fs-config` device.

Cause:

The `vpsfree-cz-configuration` worktree was added to the initiative after the
cluster runner started. Dev-cluster evaluation discovers optional worktrees and
adds a virtiofs device for each one. A NixOS generation can add the mount unit,
but an already-running QEMU process cannot gain the corresponding virtual
device.

Fix:

Restart the runner with its existing state rather than resetting it:

```sh
dev-clusters/vpsadmin/bin/devcluster stop <slug>
dev-clusters/vpsadmin/bin/devcluster start <slug> \
  --topology single --network bridge
```

The state disks remain in the cluster directory. If startup then encounters
the independently documented node `osctld` readiness race, wait for `osctld`
and run the scoped node update followed by `devcluster refresh`.

Verification:

The restarted QEMU command contained `services-fs-config`,
`findmnt /mnt/configuration` reported `config` with type `virtiofs`, all
application services were active, and `systemctl --failed` was empty.
