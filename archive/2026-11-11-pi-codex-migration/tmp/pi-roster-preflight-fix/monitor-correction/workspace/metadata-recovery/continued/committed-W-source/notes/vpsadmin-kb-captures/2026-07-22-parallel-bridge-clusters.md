# Parallel screenshot and development clusters

Related initiative: `work/2026-06-15-vpsadmin-events/`

## Symptom

Starting the capture repository's cluster with the same initiative slug while
the coordination workspace cluster was running failed because the default
services address (`172.16.106.53`) already responded. Reusing only different
addresses under the same slug would also reuse the generated socket directory.

## Cause

Each repository stores local cluster state independently, but the generated VM
name is derived from the cluster slug and the default bridge addresses are
shared. The socket directory in `/tmp` is derived only from the slug, so
independent repository state directories do not make identical slugs or
addresses safe to run concurrently.

## Workaround

Use a capture-specific cluster identity, such as
`FEATURE-SLUG-captures`, and assign checked-free addresses in that cluster's
ignored `.devcluster/clusters/CLUSTER/config.json`. Keep bridge networking;
do not use `--force` against a responding services address.

The first node SSH after readiness can race the vpsAdminOS bridge network. If
the start wrapper exits with `No route to host` but cluster status is ready,
confirm that the configured node address becomes reachable and use
`bin/devcluster update CLUSTER services`. Updating services reruns the seeded
pool and node-runtime refresh after the network is online.
