# Reset a capture devcluster after changing its source closure

## Symptom

After restarting one capture-cluster slug with a corrected vpsAdminOS closure,
fixture setup timed out waiting for a VPS to become `Running`. `osctl` showed a
running container on the node, but the services database had no matching VPS
row.

## Cause

`bin/devcluster stop` preserves writable VM state. Reusing the slug across the
source-closure change left node storage from the earlier run out of sync with
the newly provisioned services state.

## Workaround

Stop the initiative-owned cluster, run `bin/devcluster reset <slug>`, and start
it again. Before recapturing, verify that the services database and node
container list agree. Do not reset another session's cluster.

## Verification

After the reset, both sides started empty. Fixture VPS `1` then appeared in the
database and on node 1, reached the running state, and all four focused capture
runs completed successfully.

Related initiative: `work/2026-09-03-webui-vps-ipv6/`.
