# Devcluster Runtime Mounts

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

- Adding another host source, such as `vpsfree-mail-templates`, as a new
  virtiofs mount is awkward for an already-running OSVM/QEMU cluster.

Cause:

- The VM device topology is fixed when QEMU starts. A service switch can update
  NixOS configuration inside the guest, but it does not add a new host/guest
  virtiofs device to the running machine.

Fix/workaround:

- For seed-only assets, copy the source into the Nix closure instead of adding a
  live runtime mount.
- The devcluster now imports `vpsfree-mail-templates` from the selected
  worktree by copying it into the services system build and loading it during
  the seed service.

Verification:

- Updating the running services VM loaded 52 mail templates without adding a new
  virtiofs device.
- A daily report sent through the configured mailer was accepted by Mailpit.
