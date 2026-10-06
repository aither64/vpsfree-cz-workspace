# 2026-08-23-vpsadmin-supervisor-issue

## Goal

Fix the API OOM-report range failures, make OOM persistence atomic, prevent
nodectld publishers from racing RabbitMQ channel recovery, and make the
transaction-poll watchdog deterministic and diagnosable.

The completed vpsAdmin feature revision will be pinned in the `vpsadmin`,
`staging`, and `production` vpsAdmin channels in
`vpsfree-cz-configuration`. No deployment, activation, production migration,
service restart, or merge is authorized.

## Affected repositories

- `vpsadmin`
  - branch: `2026-08-23-vpsadmin-supervisor-issue`
  - worktree: `worktrees/2026-08-23-vpsadmin-supervisor-issue/vpsadmin`
- `vpsfree-cz-configuration`
  - branch: `2026-08-23-vpsadmin-supervisor-issue`
  - worktree:
    `worktrees/2026-08-23-vpsadmin-supervisor-issue/vpsfree-cz-configuration`

## Implementation

### OOM persistence

- Change kernel memory counters `total_vm`, `rss`, `rss_anon`, `rss_file`,
  `rss_shmem`, `pgtables_bytes`, and `swapents` to unsigned bigints.
- Preserve PID/TGID, UID and OOM-score types.
- Reject negative predecessor data on upgrade and reject a lossy downgrade
  after values exceed the old signed 32-bit range.
- Persist the report, child rows and related counters in one transaction while
  retaining range diagnostics.
- Leave existing partial reports unchanged and keep API values as integers.

### RabbitMQ recovery

- Track connection recovery until Bunny's completion callback.
- Prevent publishes from racing recovery start.
- Block `publish_wait` until channels are recovered and make `publish_drop`
  return false while recovery is active.
- Preserve the existing timed-out-channel cleanup and generation barrier.

### Transaction watchdog

- Keep the watchdog scoped to transaction-poll-loop liveness. Do not inspect
  transaction rows, age, dependencies or eligibility.
- Use a database-free local health command and monotonic timestamps.
- Warn at 600 seconds, capture the transaction-loop backtrace once at 810
  seconds and restart at 900 seconds since the last successful poll.
- Bound local health/debug RPCs to 10 seconds, keep the 60-second TERM grace
  and SIGKILL fallback, and reset inherited signal handlers in forked children.
- Treat process restart as the hard boundary instead of attempting to cancel a
  Connector/C call inside Ruby.

### Configuration channels

- After the final vpsAdmin revision is rebased and pushed, run:

  `confctl inputs channel set --commit 'vpsadmin,staging,production' vpsadmin <rev>`

- Keep the generated commit message and changelog unchanged.
- Verify only `vpsadminServices`, `vpsadminStaging`, and
  `vpsadminProduction` change and all resolve to the exact feature revision.
- Rebase onto current configuration `master` immediately before generating the
  pin so newer channel and dependency updates are preserved.

## Compatibility and deployment

- Widened columns accept old and new writers. Application rollback remains
  compatible with the widened schema; the schema must not be narrowed after a
  large value is stored.
- API supervisor processes already running when the migration is applied may
  retain the old signed type in ActiveRecord's schema cache. Operators must
  restart them after migration before they can accept the widened range; an
  old application started against the widened schema remains compatible.
- NodeBunny and watchdog changes are local to each daemon and support mixed
  node versions.
- The configuration pin prepares future operator deployment only. This
  initiative must not run `confctl deploy`, dry activation, production
  migrations or service control commands.

## Testing and review

- Add migration, supervisor/API, NodeBunny and watchdog unit coverage.
- Run targeted RSpec, migration coverage, RuboCop, CI-selection validation and
  mandatory Overcommit hooks in the component Nix shells.
- Commit intended changes and quick verification, then run the mandatory
  fresh-context change review before long integration tests.
- Apply and revalidate significant review findings. The user-requested second
  review must independently check the final commit series and current upstream
  bases before the configuration pin is finalized.
- Run `services-up` and `cluster/1-node`, push over SSH and monitor GitHub
  Actions to completion.
- Build/evaluate only the affected configuration scopes. Do not deploy or
  activate them.
