# Devcluster Seeded Pools

Related initiative: `work/2026-05-30-dev-vpsadmin-clusters`

Symptom:

- A devcluster with a database-seeded hypervisor pool could not create VPSes.
- nodectld either did not see the pool in its runtime cache or later failed
  because vpsAdmin pool working directories were missing.

Cause:

- The API seed inserts the pool directly into the database.
- That bypasses the normal pool-create transaction that would prepare node-side
  directories and refresh nodectld state.

Fix/workaround:

- After seeding a development cluster, wait until the services database exposes
  the configured pool filesystem.
- On each regular node, create the vpsAdmin pool directories, including
  `<pool>/vpsadmin/config/vps` and the hook root under the top-level pool.
- Restart nodectld so it reloads the pool state from the API.

Verification:

- `devcluster refresh <slug>` prepared node1 for filesystem `tank/ct` and
  restarted nodectld.
- A seeded-user VPS create then completed, with dataset `tank/ct/5`, generated
  config `/tank/ct/vpsadmin/config/vps/5.yml`, and hook
  `/tank/hook/ct/5/veth-up`.
