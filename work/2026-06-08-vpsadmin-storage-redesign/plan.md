# 2026-06-08-vpsadmin-storage-redesign

## Goal

Analyze and redesign vpsAdmin storage snapshot/backup topology handling so
dataset destroy, snapshot rotation, snapshot deletion, rollback, and backup
incremental send/recv remain dependency-safe and recoverable. The first
implementation step is read-only topology capture, followed by a reviewed data
model/design before mutation paths are changed.

## Affected repositories

- `vpsadmin`: API models, transaction chains, nodectld storage commands,
  web UI snapshot actions, client-facing API shape, and integration tests.

## Approach

- Read current vpsAdmin storage model, transaction chains, node-side ZFS
  commands, API resources, web UI snapshot list/delete flow, and existing
  storage topology tests.
- Identify invariants that must hold between database topology and real ZFS
  `origin`/`clones` state.
- Propose staged changes that first make state observable and reconcilable,
  then make deletion and rotation use a dependency-safe planner.
- Keep production recovery and incremental send/recv preservation as primary
  constraints.

## Recommended direction

1. Add read-only topology diagnostics. Use a DB-wide scanner to rank suspicious
   datasets first, then collect detailed DB+ZFS topology reports only for
   candidates. Treat each capture as a point-in-time sample: production will
   continue creating daily snapshots before any deployment.
2. Introduce explicit dependency records instead of relying on the overloaded
   `snapshot_in_pools.reference_count` integer for both mounted clones and
   backup branch dependencies. Do not implement schema changes until the
   proposed updated data model has been reviewed.
3. Build a deletion planner that computes a topological delete order from
   dependency edges and refuses to plan snapshots that are needed as
   incremental bases or have live external clones.
4. Make rotation, dataset destroy, and user snapshot deletion call that same
   planner and expose destroyability plus reason codes in the snapshot API.
   Every planner user must participate in the existing lock system so that
   analysis, DB edits, and queued storage transactions are consistent with
   concurrent snapshot, backup, rollback, export, snapshot-download, and
   destroy operations.
5. Enable user deletion only after diagnostics and reconciliation demonstrate
   DB and ZFS topology agree on production samples.

Hard safety constraint: never use or propose `zfs destroy -R`. Deletion must be
explicitly planned and bounded to known snapshots/filesystems.

## Current diagnostic tool

`api/bin/storage-topology-scan` performs a read-only DB-wide scan and ranks
candidate datasets using conservative heuristics: stored `reference_count`
mismatches against DB-visible clone/branch dependents, old blocked snapshots,
branch topology complexity, pending destroy rows, locks, and active snapshot
downloads.

`api/bin/storage-topology-report` emits a read-only JSON report for one dataset,
one dataset-in-pool, or all dataset IDs listed in a scan output. It captures
selected DB rows, snapshot downloads, mounts, exports, resource locks, locked
transaction chains, and ZFS filesystem/snapshot `origin` and `clones` metadata
unless `--skip-zfs` is used. Reports are point-in-time evidence only; any later
repair or deletion plan must re-read current state under locks before acting.

## Compatibility and deployment

- Must preserve old and new API clients while adding snapshot destroyability
  metadata; any new fields should be additive.
- Any schema migration must be forward-compatible while old transaction chains
  can still be in flight.
- Backup pools can have long-lived existing topology that must be reconciled
  from live ZFS state before automated deletion is trusted.
- Rollbacks must not invalidate incremental backup/send/download base
  selection.
- Production rollout should start with read-only diagnostics and dry-run
  reconciliation before applying DB repairs or enabling user deletion.

## Testing plan

- Use current API unit specs for storage transaction chains.
- Extend existing storage topology integration suites, especially repeated
  rollback branching and complex rotation pending contracts.
- Add fixture-based offline tests for production-derived topology reports.
- Add API/web UI tests for snapshot destroyability status and user deletion.
