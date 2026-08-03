# Reset capture state when switching network modes

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`

## Symptom

After stopping a bridge screenshot cluster and starting the same slug with
local networking, fixture preparation waited indefinitely for the preseeded
NAS dataset. The database had no `nas` row, and transaction `#1` had rolled
back because `/tank/ct/nas/private` already existed.

## Cause

The services VM database is rebuilt for the changed cluster configuration,
while the slug's node and backuper disk images persist. The fresh database
therefore tried to create a NAS dataset already present on the reused backuper
filesystem. The API rollback removed the database object but correctly left
the pre-existing filesystem untouched.

## Fix

For a disposable capture cluster, run `bin/devcluster reset SLUG` before
restarting the same slug in a different network mode. This removes only that
slug's VM state and lets the database and ZFS fixtures seed together from a
clean baseline.

## Verification

Confirm that the initial dataset-create transaction succeeds and that the
services database contains the unowned `nas` dataset before launching a
checkpoint capture.
