# Storage reliability investigation (proposal)

This is a source review, not a production inventory. The reported scale of
approximately 20,000 snapshots is a planning input; no live dataset or
snapshot was changed. Source inspected: canonical `vpsadmin` head
`9fc0648accd4` and `vpsadminos` head `2166e5934fe1` on 2026-09-24.
The older session named in the request was
not accessed because this conversation is bound to `2026-09-23-storage-redesign`.

## Evidence and failure mechanism

- The backup layout uses trees and branches. After a clone and promotion, ZFS
  can move snapshot ownership between branch datasets. The existing
  `doc/storage/branching.mdwn` explains the intended dependency order.
- `snapshot_in_pools` stores one row per logical snapshot and pool; branch
  occurrences are separate `snapshot_in_pool_in_branches` rows with a
  parent-entry pointer. `reference_count` is stored on the shared pool row.
  This is not a full inventory of physical ZFS snapshot objects or their
  current origin/clone edges. See `api/db/schema.rb` and the original storage
  migration `api/db/migrate/20140927161700_add_storage.rb`.
- `TransactionChains::DatasetTree::Destroy` orders rows by
  `reference_count, snapshot_in_pools.id`; rotation skips entries with a
  positive `reference_count`. Both rely on database metadata to predict ZFS
  deletion eligibility. `tests/suite/storage/repeated-rollback-branching.nix`
  and `complex-rotation-order-pending.nix` explicitly retain pending
  contracts for dependency failures after complex branching.
- The repository already has a read-only topology fixture tool that captures
  DB rows plus ZFS `origin` and `clones` (`api/bin/storage-topology-fixture`).
  Its leaf diagnostic compares snapshot *names*, so it is useful for a small
  case but cannot prove physical-object identity when a name occurs in more
  than one branch.
- The snapshot DELETE API exists, including user authorization, but refuses
  every snapshot on a dataset that has a backup pool, even if the particular
  snapshot has no dependants. See `api/lib/vpsadmin/api/resources/dataset.rb`
  and `api/models/transaction_chains/snapshot/destroy.rb`.
- OpenZFS exposes snapshot `guid`, filesystem `origin`, snapshot `clones`,
  `userrefs`, and `defer_destroy`. A snapshot with clones or holds cannot be
  deleted normally; clone promotion reverses origin ownership. See
  [ZFS properties](https://openzfs.github.io/openzfs-docs/man/master/7/zfsprops.7.html),
  [destroy](https://openzfs.github.io/openzfs-docs/man/v2.3/8/zfs-destroy.8.html),
  and [promote](https://openzfs.github.io/openzfs-docs/man/master/8/zfs-promote.8.html).
- The normal node storage-status stream reports usage properties for primary
  and hypervisor pools, not backup snapshot topology. It cannot serve as the
  new inventory (`libnodectld/lib/nodectld/storage_status.rb`).

## Recommended sequence

### 1. Inventory and classify, without deleting

Add a read-only node inventory operation scoped to a managed pool/dataset. It
should return exact ZFS object paths, type, GUID, origin, clone relationships,
holds/userrefs, deferred-destroy state, and an observation time or generation.
Keep it paged or bounded
so a pool with many snapshots does not create a huge RPC message. Compare each
physical object and edge with the current DB model. Classify missing objects,
unmanaged objects, path/ownership changes, and ambiguous logical mappings.
Expose counts and a small redacted diagnostic, not raw production paths in
routine logs. The existing fixture format can seed tests, but needs exact
path/GUID comparisons before it becomes a migration authority.

Build the inventory on a replica or a small sample first, then run a complete
read-only audit. Inventory must cover every backup pool and any clone located
outside the immediate dataset subtree; otherwise a proposed deletion could
miss a dependant. Do not infer safety from `reference_count == 0` alone.

### 2. Add a physical topology model and migrate in batches

Prefer additive tables that describe physical ZFS snapshot occurrences,
branch datasets and explicit clone-origin edges, while retaining logical
`Snapshot`, `SnapshotInPool`, tree and branch records for old API/transaction
compatibility. Link a logical snapshot to *each* physical occurrence. Keep
the observed ZFS identity and path distinct: the path can change after
promotion. A received snapshot may share a GUID with its source, so scope
identity by pool and lineage, and verify that assumption on real inventory.
Treat a duplicate or uncertain match as an exception to review, not a reason
to rewrite live metadata automatically. Derive legacy reference counts from
the verified graph while old code still needs them; never trust them alone.

Backfill by dataset/pool in small, resumable batches. Bulk-read ZFS and DB,
write a versioned observation and validate one-to-one/known many-to-one
matches and inverse clone edges. Use a short per-dataset mutation fence for
the final stable scan; replay or invalidate observations if a supported ZFS
operation happened meanwhile. Keep a migration cursor and mismatch count.
At 20,000 snapshots, benchmark scan time, query plans and index sizes on a
representative copy before choosing batch size. Avoid one ZFS subprocess or
SQL query per snapshot. A dry run must report every unresolved mapping. No
destructive repair should be automatic.

### 3. Make every destructive operation graph-aware

Calculate deletion order from actual origin/clone edges and current holds,
then revalidate exact path, GUID and current dependencies on the responsible
node immediately before each physical destroy. Delete only leaves, and remove
their DB rows only after success. The current node destroy transaction does
not carry this guard; give the guarded operation a new capability-gated
transaction type so old nodes cannot silently ignore the new requirements.
Fail closed on stale/missing inventory or an unrecognized dependant. Avoid
`zfs destroy -R` and deferred deletion: they can remove other objects or
leave a snapshot visibly pending while DB state says it is gone. On a partial
failure, retain enough operation progress to reconcile and retry without
guessing. Make the two pending integration contracts pass and add a case where
the same snapshot name appears in several branches.

### 4. Allow safe user snapshot deletion

Use the existing authorized snapshot DELETE action, but compute eligibility
for *all* physical copies of that logical snapshot. Require no clone or hold,
no mount/export/in-progress download or active transfer use, a valid inventory,
and a continuing confirmed common snapshot for each active backup if deleting
the chosen one would break incremental send. Respect retention policy. A
completed download file does not by itself need its source snapshot. Return a specific
reason when ineligible. Under the storage lock, recheck eligibility when the
transaction executes; UI hints are advisory. Start with a feature flag and
validated datasets, then expand. Treat deletion of a logical snapshot as
all-or-nothing across its physical occurrences; retain an explicit pending
state if a later copy cannot be removed and require reconciliation before
retry. This should follow topology reconciliation,
because removing the blanket backup check before that would trust the broken
dependency representation.

## Compatibility and rollout constraints

- Deploy additive schema and read-only node inventory first. Old nodes must
  continue to work; mark their topology unknown and keep new destructive
  behavior disabled for them. Roll out node support before the API uses it.
- During backfill and shadow comparison, keep existing transaction formats and
  legacy tables intact. A mixed API fleet must not make contradictory delete
  decisions. Gate topology-based deletes until all relevant API/scheduler/node
  components use the new checks, or route them to a single upgraded writer.
- Software rollback is safe during observation-only phases because legacy
  tables remain authoritative. After enabling topology-based deletes, either
  dual-write legacy metadata correctly or disable those deletes before a
  rollback. Disable guarded deletion and drain its chains before downgrade;
  old writers invalidate shadow coverage, so re-upgrade needs a fresh
  reconciliation. Test rollback against state actually created by the new
  version.
- Do not rewrite old migrations merely to reset disposable development DBs.
  Production backfill is a separate, restartable operation with an audit
  report and operator decision for anomalies.

## Verification before production mutation

Use synthetic and sanitized real topology fixtures; exercise repeated
rollback, tree switches, clone promotion, duplicate names, interrupted send,
holds, and external clones. Test both graph calculation and complete VM
operations, including payload integrity after backup and restore. Perform a
read-only full audit, inspect mismatches, and rehearse the migration on a
representative database copy. Define acceptable mismatch count (ideally zero
for automatically migrated datasets), batch latency, rollback steps, and the
operator handling for quarantined datasets before enabling deletion.

## Open questions

- How many of the approximately 20,000 snapshots are physical copies across
  pools/branches, and what fraction have DB/ZFS mismatches?
- Are all relevant clones inside managed pool subtrees? If not, the node
  inventory must query dependencies across the pool.
- Which snapshots are intentionally held, mounted, exported, or used as
  incremental send bases, and how should those reasons appear to users?
- Is a new tree after loss of the only common send base acceptable as a
  deliberate operator action, or should user deletion always preserve one?

## Backup scheduling: a second phase

The current pool-wide group snapshot runs at 01:00 and per-dataset backup
tasks at 01:05 (`api/config/dataset_plans.rb`,
`api/lib/vpsadmin/api/dataset_plans.rb`). The scheduler enqueues every task
matching the minute. Its single worker builds chains one by one, but the
chains then execute asynchronously; each `Dataset::Backup` locks both source
and destination DIPs until transfer and rotation finish. The transfer already
uses nodectld `zfs_send`/`zfs_recv` queues and queue reservations, so queue
capacity limits running transfers but not the number of locked queued chains.
The scheduler has no durable daily due/retry row. A group snapshot can skip a
locked DIP, and a backup lock error is logged without a same-day retry.

Recommended separate scheduler change: persist one due backup run per action
and local scheduled date, with a unique key, snapshot-readiness state, chain
ID, terminal result and retry information. Let the daily schedule create due
rows in batches; a dispatcher admits only a configured small number of
outstanding chains per source and destination node, including queued and
rollbacking chains. Admit a new run as a prior one finishes. Use a short DB
transaction with deterministic node/admission-row locking to serialize
dispatchers, and create the chain and save its ID atomically. Keep nodectld's
queue reservations as the execution limit. Do not wait for a queue slot while
holding a DB transaction. Fair selection should let an idle node proceed when
another is saturated.

Reconcile chain state on each dispatcher tick. A pre-enqueue lock/port
conflict leaves the due row pending for bounded retry. A fatal chain needs
operator attention because locks can be retained; never blindly create a
replacement. A completed no-new-data backup should be an explicit successful
result. Ensure each due run has a confirmed source snapshot, or retry the
group-snapshot members skipped because of locks, so bounded dispatch does not
trade lock duration for silently missed daily backups. Preserve manual
`Dataset::Backup` calls and account for their contention when sizing limits.

This is feasible without a vpsAdminOS change, but it is a larger scheduler
change than the topology audit. Implement after, or in parallel only with a
separate rollout and tests. Additive run tables can be deployed first. Switch
from old per-action cron tasks only after old scheduler instances and queued
daily chains have drained; explicitly deduplicate the cutover day. Restore
legacy tasks before a rollback and drain new managed chains. Verify restart,
duplicate scheduler instances, lock/fatal failures, node capacities, missed
group snapshots and data integrity in two-node integration tests.
