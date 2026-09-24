# 2026-09-23-storage-redesign

## Goal and scope

Improve vpsAdmin storage reliability by representing actual ZFS dataset,
branch, snapshot and clone dependencies, then allow deletion and rotation only
when physical state permits it. Preserve and migrate the existing estate of
approximately 20,000 snapshots. Add safe user deletion of snapshots with
backup copies. Investigate a bounded daily-backup dispatcher that avoids
locking all datasets hours before their transfers run.

This conversation is bound to this session. The older
`2026-06-08-vpsadmin-storage-redesign` session named in the request was not
accessed; any unpublished findings there need to be supplied separately.

## Affected projects and readers

- `vpsadmin`: primary owner. API schema/models, transaction chains, scheduler,
  nodectld integration, WebUI eligibility feedback, storage tests and docs.
- `vpsadminos`: reference for generic ZFS behavior and integration tests.
  No vpsAdminOS code change is proposed. If one becomes necessary, provide a
  general-purpose primitive, with its own compatibility plan.
- `vpsfree-maintenance-tasks`: owns the first, read-only inventory scripts
  that an operator can run against production DB and on `backuper2.prg`.
- Operators need read-only audit, migration and recovery instructions. Future
  developers need graph invariants and the boundary between logical snapshots
  and physical ZFS occurrences in vpsAdmin storage docs. Members need clear
  deletion eligibility text in API/WebUI documentation once implemented.

The source review and detailed rationale are in [investigation.md](investigation.md).

## Proposed phases

1. Extend the existing read-only topology fixture and add a bounded node
   inventory of exact physical objects, GUIDs, origin/clone edges, holds and
   operation state. Audit real pools without writes; classify mismatches.
2. Add a shadow physical-object/edge model with durable per-dataset
   reconciliation status. Backfill it in resumable batches, then perform a
   fenced final scan for each dataset. Keep ambiguous datasets quarantined.
3. Replace reference-count-only deletion ordering with graph-aware, guarded
   nonrecursive operations. Make pending complex-topology integration
   contracts pass. Journal partial progress.
4. Reuse the existing authorized snapshot DELETE API for eligible snapshots
   on validated datasets, checking every physical occurrence and replication
   base under the same lock. Return specific blockers and add UI feedback.
5. Separately introduce durable due backup runs and a bounded per-node
   dispatcher, preserving nodectld send/receive queue reservations. This is
   feasible but larger, so it need not delay the topology repair.

These remain proposals, not approved rollout steps. The read-only inventory
slice below is implemented; no live data has been changed in this session.

## Current implementation slice: offline inventory

The dated standalone task in `vpsfree-maintenance-tasks` has separate
read-only DB and ZFS collectors and an offline comparator. The DB collector
uses vpsAdmin API models for application rows and a read-only consistent
database transaction. The operator will
run the collectors using production DB access and on `backuper2.prg`; this
session will not connect to production. The DB collector must retain every
confirmation state and relevant dataset locks. The ZFS collector must scan
only explicit backup roots, capture exact paths and dependency properties,
and mark a scan that changed during collection. Capture metadata records both
observation windows. Outputs are private, complete-only artifacts; raw files
must not be committed. Comparison reports exact mismatch classes and
volatility evidence without claiming deletion safety or modifying either
system. Offline fixture tests and source review are complete; live behavior
and scan cost await the operator capture.

## Decisions for a future implementation

- Use additive shadow schema before replacing any legacy metadata. This
  supports observation and comparison without a destructive migration.
- Treat ZFS state as the authority for whether a physical snapshot can be
  destroyed; treat DB rows as intent and user-visible catalog. A mismatch
  blocks new deletion until reconciled.
- Make logical snapshot deletion all-or-nothing across pool and branch copies.
  Preserve an explicit pending result on partial failure; do not cascade to
  dependent datasets or silently defer physical deletion.
- Preserve a confirmed common send base for each active backup by default.
  A deliberate full reseed, if desired, should be a separate operator flow.
- Keep scheduler dispatch distinct from node queue reservation: admission
  limits outstanding chains, while nodectld limits running transfers.

## Compatibility and deployment

- Persisted state: additive tables and dual maintenance of legacy tables
  during transition. Backfill is a restartable operation, not part of a long
  schema migration transaction. No automatic destructive repair.
- Database: create indexes for bounded per-dataset and per-pool graph queries;
  benchmark and rehearse against a representative copy. Old binaries ignore
  new tables. Old writers invalidate shadow validation.
- API, clients, CLI and Terraform: retain existing endpoints and request
  shapes. Successful deletion of snapshots with backups is a behavior change;
  surface precise denial reasons without changing unrelated clients.
- Node protocol: add capability-advertised inventory and a new guarded
  destroy transaction; do not extend the old transaction and assume older
  nodectld will enforce the guard. Roll node support out before API use.
- vpsAdminOS configuration: no option or on-disk format change is currently
  proposed, so no coordinated all-node OS update is expected.
- Mixed versions: observation-only phases are safe with old APIs/nodes.
  Enable graph-based deletion only when every possible storage writer and
  relevant node supports the guard, or route through a single upgraded
  writer. Keep disabled for unknown or unvalidated DIPs.
- Rollback: disable new deletion and drain guarded chains first. Legacy
  records must remain coherent with completed deletes. On re-upgrade,
  reconcile DIPs touched by old writers again. Test old software reading
  state created by the new software before claiming rollback support.
- Scheduler cutover: persist due rows first, then switch off per-action cron
  only after old schedulers and queued chains drain. Deduplicate the cutover
  day and restore old tasks before scheduler rollback.

## Verification plan

Audit all managed pools read-only, count each mismatch class, and assess scan
latency at the reported scale. Unit-test graph matching and deletion
eligibility on synthetic and sanitized real fixtures. Make repeated rollback
and complex rotation integration contracts pass, including duplicate snapshot
names, promotion, external clones, holds, interrupted transfers and payload
integrity. Rehearse migration, mixed-version behavior and software rollback on
a representative database copy. Test dispatcher admission, fairness, restart,
duplicate schedulers, missed daily snapshots and fatal-chain handling in a
two-node setup. Use mandatory review after implementation commits and quick
checks, before long integration tests.
