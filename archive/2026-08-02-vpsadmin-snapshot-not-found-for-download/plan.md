# 2026-08-02-vpsadmin-snapshot-not-found-for-download

## Goal

Prevent snapshot downloads and exports from racing with queued destruction of
their physical snapshot copies. Downloads must report the existing transaction
lock as HTTP 423, source-less snapshots must return a controlled HTTP 409, and
the logical snapshot lifecycle must reflect pending destruction.

## Affected repositories

- `vpsadmin`
  - branch: `2026-08-02-vpsadmin-snapshot-not-found-for-download`
  - worktree: `worktrees/2026-08-02-vpsadmin-snapshot-not-found-for-download/vpsadmin`
- `vpsfree-cz-configuration`
  - branch: `2026-08-02-vpsadmin-snapshot-not-found-for-download`
  - worktree: `worktrees/2026-08-02-vpsadmin-snapshot-not-found-for-download/vpsfree-cz-configuration`

## Approach

- Mark the logical `Snapshot` as `confirm_destroy` when the last live
  `SnapshotInPool` is scheduled for destruction, using the existing destroy
  confirmation to delete it on success or reconfirm it on failure.
- For archive and incremental downloads, inspect existing physical-copy locks
  when no eligible source can be selected. Return the standard HTTP 423 locked
  response for queued work and a typed HTTP 409 response for an unlocked
  unavailable topology.
- Lock the source dataset-in-pool and snapshot-in-pool when a snapshot clone is
  used for an export, so export creation serializes with destruction.
- Keep pending snapshots visible through the existing Snapshot Index/Show API;
  do not add a logical Snapshot resource lock.
- After the vpsadmin commits are merged, update the production configuration's
  `vpsadmin` channel through `confctl` so deployment consumes the merged head.

## Compatibility and deployment

No schema, API input, persisted-format, or node protocol change is required.
Existing nodectld versions resolve snapshot names through the database whenever
the snapshot state is not exactly `confirmed`, so `confirm_destroy` is already
wire-compatible. Old in-flight chains are covered by inspecting their physical
SIP locks even though they did not mark the logical snapshot. During a rolling
API deployment, old workers may still return the original error until drained,
but mixed versions cannot corrupt state. Rollback needs no data conversion and
may only reintroduce the original race.

Deploy vpsadmin code before or through the configuration channel update. The
configuration change only advances a source pin and introduces no additional
schema, protocol, or persisted-state dependency. Rolling deployment and mixed
old/new API workers remain supported. Reverting the channel pin is sufficient
for rollback and does not require operator data conversion.

## Testing plan

- Run only focused local API model/resource specs for snapshot destruction,
  backup, full/incremental downloads, clone use, snapshot downloads, and
  exports, plus focused libnodectld destroy/confirmation specs.
- Run targeted RuboCop, API i18n normalization/health, and mandatory Overcommit
  hooks; do not run the complete local suite.
- After committing and quick verification, run the mandatory standalone change
  review before pushing.
- Push the feature branch and monitor all GitHub Actions jobs for the current
  head SHA. Inspect logs and artifacts before fixing or rerunning failures and
  cancel superseded runs after follow-up pushes.
- Update the `vpsadmin` channel with `confctl inputs channel update --commit`,
  inspect the generated pin/changelog, run repository-required quick checks,
  and merge the configuration update by fast-forward after its CI passes.
