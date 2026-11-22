# Complete dev-cluster user seeds before applying services

The development-cluster provider requires `namespace.blockStart` and
`namespace.blockCount` for every configured seed user, including administrators.
Adding only login, password, full name, email and level causes the ordinary
seed to fail with `KeyError: key not found: "namespace"`. The user may already
have been saved before that error. Check the complete configured-user contract
and verify that the chosen namespace blocks are available; the upsert helper
does not allocate a safe unused range automatically.

In the October 1 storage trial, schema load, singleton bootstrap and migrations
had succeeded before this seed failure. The initialized marker was intact.
Correcting the private user configuration and applying the supported
`vpsadmin-devcluster update <owned-slug> services` recovered successfully and
refreshed the nodes. Existing initialization skipped schema reload and the
generic initial seed; the separate repeatable development seed completed the
partial upsert. Do not remove the initialized marker, reset the database or
replay the generic initial seed to hide this error.

Inspect public provider templates when diagnosing helpers. Generated seed files
also contain private configuration; reading past a helper into their embedded
JSON can expose credentials. Keep guest journals private and report only
redacted exceptions. Check `Result` and `ExecMainStatus` for seed oneshots:
inactive after a successful run is expected.

Executed evidence and exact sources: [storage rollout](../../work/2026-09-23-storage-redesign/rebase-devcluster-20261001.md).
