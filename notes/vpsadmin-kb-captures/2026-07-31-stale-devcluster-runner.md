# Restart a stale screenshot devcluster with `--force`

## Symptom

`bin/devcluster status SLUG` reported a stopped screenshot cluster while the
same initiative's old QEMU runner still answered at its bridge address. A
normal start could therefore reuse process state that was not represented by
the status file.

## Cause

The prior capture runner survived after its recorded cluster state became
stale. The runner paths, process arguments, and bridge address all belonged to
the same verified development-session slug; this was not another session's
cluster.

## Fix

From the capture repository's Nix shell, rebuild and restart that exact slug:

```sh
bin/devcluster start SLUG --topology screenshots --force
```

Do not use `--force` until the active `VPSFREE_DEV_SESSION_SLUG`, process paths,
and cluster paths all prove that the runner belongs to the current session.

## Verification

The forced start rebuilt the capture environment against the newly pinned
vpsAdmin revision and returned all WebUI/API endpoints ready. Observed for
`work/2026-06-15-vpsadmin-events`.
