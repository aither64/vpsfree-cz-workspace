# Restart a capture VM after changing its pinned source

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

After `bin/devcluster update SLUG services`, the nested WebUI container returned
404 and `/mnt/vpsadmin` in the services VM was empty. Nginx reported that
`/run/vpsadmin-live-webui/public/index.php` did not exist.

## Cause

The running QEMU process kept its original virtiofs export. Rebuilding and
switching the services configuration moved the cluster GC root to the new exact
vpsAdmin pin. Once the old source store path disappeared, the existing
virtiofs export had an empty backing directory. A NixOS switch cannot retarget
the already-running QEMU virtiofs process.

## Fix and verification

Stop and start the disposable capture cluster after changing an exact pinned
source. The restarted QEMU process exports the new store path. Verify the
mounted WebUI `public/index.php`, an HTTP 200 response, and affected services
before running captures.
