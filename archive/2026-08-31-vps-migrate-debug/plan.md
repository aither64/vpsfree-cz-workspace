# 2026-08-31-vps-migrate-debug

## Goal

Prevent VPS replacement from corrupting shared daily-backup group-snapshot
actions, reconcile the existing corruption generically during the vpsAdmin
database migration, and update the production configuration's `vpsadmin`
channel to the repaired vpsAdmin revision.

The reconciliation is limited to existing `daily_backup` assignments. It must
not enable the plan for any additional VPS or dataset and must not contain
vpsFree.cz-specific record IDs.

## Affected repositories

- `vpsadmin`: fix group-snapshot reassignment, add an idempotent data migration,
  and add focused regression coverage.
- `vpsfree-cz-configuration`: pin the exact repaired vpsAdmin revision in the
  `vpsadmin` channel.
- Top-level coordination workspace: initiative plan and state.

`vpsfree-maintenance-tasks` is not affected because the repair can derive all
targets from core model relationships and the stable `daily_backup` plan name.

## Approach

1. Change backup-preserving VPS replacement to move only the replaced
   dataset's `GroupSnapshot` membership. Do not relabel a shared source action
   or destroy the destination action and its unrelated memberships.
2. Reuse or create the destination pool's group-snapshot action and 01:00
   repeatable task while holding the destination pool row lock. Only move a
   membership when its plan is available in the destination environment;
   otherwise remove it with the unavailable plan. Remove source actions only
   when no membership will remain.
3. Add a transaction-wrapped, idempotent migration which finds
   `daily_backup` by name and derives expected memberships from existing
   `DatasetInPoolPlan` rows.
4. For every represented pool, require at most one existing correctly labelled
   group action, create it if absent, move mismatched memberships, create
   missing memberships, and remove duplicates, memberships without an
   assignment, and newly orphaned actions.
5. Abort without partial writes when the existing state is ambiguous, and
   assert that every existing assignment has exactly one pool-matched
   membership before committing. The reverse migration is a no-op.
6. Refine `RecordNotFound` diagnostics using HaveAPI's existing
   `exec_exception` context. Log class, message, and backtrace for non-Show
   actions outside the test environment; suppress expected Show misses and
   all operational diagnostics during RSpec. Keep the existing 404 response
   mapping unchanged and avoid a HaveAPI release.
7. Commit and push vpsAdmin, run the mandatory fresh-context review, then use
   `confctl inputs channel set --commit vpsadmin vpsadmin <revision>` and push
   the configuration branch.

## Compatibility and deployment

There is no schema, API, generated-client, node protocol, or on-disk format
change. The data migration repairs core relational invariants and can run on
any vpsAdmin installation without deployment-specific IDs. Existing plan
assignments and backup actions are preserved.

Old API instances can read the repaired rows, but their VPS replacement code
can recreate the corruption. Avoid replacements and dataset-plan edits during
the rollout and update every API instance before the 01:00 group snapshot.
Rollback can read repaired data, but would reintroduce the code defect; the
data repair is intentionally not reversed.

The scheduler on api1 must restart or refresh after migration so newly created
repeatable tasks are loaded before the scheduled run.

## Testing plan

- Replacement-chain specs with unrelated memberships on both source and
  destination pools, plus destination-action creation and orphan cleanup.
- Migration specs for mixed pools, missing memberships, task creation,
  duplicate memberships, ambiguity rollback, idempotency, and preservation of
  datasets without an assignment.
- Focused RSpec, migration-spec coverage, RuboCop, and CI-selection checks.
- Logging regressions for a non-Show failure in production and test
  environments, plus a Show miss in a production environment.
- Mandatory standalone change review after commit and quick verification.
- Post-deployment SQL verification must show no missing or pool-mismatched
  daily-backup memberships and no mixed-pool group actions.
