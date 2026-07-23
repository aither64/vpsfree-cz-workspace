# Reset stale screenshot node state after a failed seed

Related initiative: `work/2026-06-15-vpsadmin-events`

## Symptom

After resetting and restarting a screenshot devcluster whose services seed had
failed, the database setup failed while creating the documentation VPS because
`/tank/ct/1/private` already existed on a node.

## Cause

The services database had been reset, but a node VM from the earlier partial
run still retained its container dataset. The fresh database therefore reused
container ID 1 while the node still had storage for that ID.

## Recovery

Stop and reset the disposable capture cluster as a whole before restarting it;
do not retry only the services database. When another bridge cluster is active,
restore checked-free, capture-specific bridge addresses in the ignored cluster
configuration before starting. A first-node network race can still leave the
cluster marked ready after `No route to host`; confirm node reachability and
run:

```sh
bin/devcluster update CLUSTER services
```

This reruns the seed and refreshes node pool runtime after networking is up.

## Verification

The rebuilt screenshot cluster completed database setup, seeded both nodes, and
captured the Czech and English notification scenarios twice with an identical
complete binary diff hash.
