# 2026-08-09-supervisor-exceptions

## Repositories

- `vpsadmin`: production revision
  `c0d87bebf36c6d29b7861990890e8c650fa1afca`; inspected from canonical bare
  repository `repos/vpsadmin.git`. Implementation branch
  `2026-08-09-supervisor-exceptions` is based on upstream `master` at
  `63c2c44f6` and checked out at
  `worktrees/2026-08-09-supervisor-exceptions/vpsadmin`.
- `vpsfree-cz-configuration`: production inventory revision
  `2051708717b170afd34820817945bf858f93bb19`; canonical bare repository
  `repos/vpsfree-cz-configuration.git`; temporary read-only worktree branch
  `2026-08-09-supervisor-exceptions`.

## Status

Root-cause investigation and implementation are complete. Two vpsadmin
commits have passed focused verification and mandatory standalone review.
The branch is pushed, all targeted workflows are green, and the multi-hour
full integration run remains active on GitHub. No production or configuration
changes have been made.

## Implementation decisions

- Configure Bunny's public `Channel#on_uncaught_exception` hook from a shared
  supervisor channel factory, preserving the existing queue and acknowledgement
  behavior.
- Log consumer identity plus `Exception#full_message` with complete backtrace
  and causes. Do not log payloads.
- Change only OOM task UID columns to unsigned 32-bit integers. Do not widen
  unrelated task counters or redesign delivery/idempotency in this initiative.
- Keep unrecoverable historical partial OOM reports unchanged.
- Use two vpsadmin commits: general supervisor logging, then OOM schema and
  diagnostic changes.

## Commits

- `b1490c201`: `api: log full supervisor consumer exceptions`
- `95f8d9ca7`: `api: accept unsigned OOM task UIDs`

## Commands run

- Verified the active development-session slug.
- Fetched `vpsadmin` and `vpsadminos` upstream refs.
- Traced supervisor OOM consumer, OOM parser/exporter, schema, nodectld RPC
  client, supervisor RPC handler, and network-accounting initialization.
- Fetched production configuration and resolved pinned source revisions from
  `flake.lock`.
- Created a temporary `vpsfree-cz-configuration` worktree to use its pinned
  confctl environment. Its post-checkout hook could not load ambient gems;
  subsequent confctl commands ran in `nix develop`.
- Attempted read-only production access through confctl and direct SSH.
  Confctl returned the known empty failed-command result; direct SSH confirmed
  that this unattended shell has neither trusted Node host keys nor an
  authorized production admin key.
- Used the narrowly scoped, read-only vpsAdmin security-evidence token to
  confirm Node inventory and current status without exposing the credential.
- Inspected Bunny 2.24.0 queue subscription, automatic acknowledgement,
  consumer work-pool, and synchronous reply-queue subscription behavior.
- Inspected commit `15e630312` (`libnodectld: retry RPC read requests`) and
  the deployed retry implementation.
- Installed and signed the repository's Overcommit hooks in the root Nix
  development shell. Both commits passed all pre-commit hooks: Nixfmt,
  MigrationSpecs, VpsadminWebuiI18n, RuboCop, and VpsadminApiI18n.
- Ran the new migration against a schema-loaded scratch MariaDB database. It
  changed both UID columns in one bulk `change_table` operation.
- Ran the migration spec independently: 4 examples, 0 failures.
- Ran focused supervisor specs for shared exception logging and OOM reports:
  14 examples, 0 failures.
- Ran focused RuboCop on all changed Ruby code/specs: 4 files, no offenses.
- Ran `git diff --check` and migration-spec coverage validation: passed.
- An initial API-shell command incorrectly changed into `api/` even though the
  shell hook already does so; no tests ran. Existing note
  `notes/vpsadmin/2026-07-20-api-devshell-working-directory.md` documents it.
- A combined migration/ordinary RSpec process failed because migration specs
  switch Active Record to their minimal scratch database before the global
  seed hook. Both suites passed when run separately, as already documented in
  `notes/vpsadmin/2026-07-25-migration-spec-database-isolation.md`.
- A schema dump reordered unrelated foreign-key-dependent tables. The noise
  was removed; `schema.rb` contains only the version and two intended unsigned
  UID changes.
- Mandatory standalone change review was performed from fresh context after
  both commits and focused verification. Verdict: approved for broader tests,
  with no blocking, important, or advisory findings.
- Reviewer residual risks: pause all OOM writers/pruning during migration and
  rollback to avoid check-then-ALTER races; restart supervisors afterward;
  live RabbitMQ delivery and production-sized ALTER timing remain deployment
  checks rather than code blockers.
- Ran all core supervisor specs locally with plugins disabled: 108 examples,
  0 failures.
- Pushed branch `2026-08-09-supervisor-exceptions` to the SSH `origin` at
  `95f8d9ca7cb31e284d19ac7bc6d310a25a7071dc`.
- GitHub Actions completed successfully for API Migration Specs, RuboCop,
  i18n health, libnodectld Specs, and API Specs (topic parallel). The API
  workflow completed 27 jobs with zero failures.
- Full `tag=ci` integration run
  `https://github.com/vpsfreecz/vpsadmin/actions/runs/31314460784` remains in
  progress. A migration path intentionally selects the full matrix; recent
  successful runs take roughly 3--6 hours, so it remains active for GitHub to
  complete rather than blocking this implementation handoff.

## Results

- The OOM consumer failure is a schema signedness bug in
  `oom_report_tasks.host_uid`. The kernel reports task UIDs in the host's
  initial user namespace as unsigned 32-bit values, but `host_uid` is persisted
  as a signed 32-bit Active Record `integer`. Active Model correctly rejects
  values above 2,147,483,647 before SQL is issued.
- The exact values identify the field without needing the missing payload. All
  observed numbers are in user-namespace block 32,772 with base
  2,147,745,792 (`2^31 + 4 * 65,536`). Subtracting that base yields plausible
  in-container UIDs between 11,138 and 27,875. The vpsAdmin allocator creates
  65,536-ID blocks across the entire unsigned 32-bit UID space, so this is a
  legitimate configured mapping that a signed column cannot represent.
- Each failing message has already incremented the OOM aggregate and rule hit
  counters and created the parent OOM report, usages, and stats before the
  bulk task insert raises. There is no encompassing transaction, so those
  partial writes remain. `handle_abuser` is not reached for that report.
- The OOM queue uses Bunny automatic acknowledgement. A handler exception does
  not requeue the message; repeated journal lines are new OOM reports, not one
  poison message being redelivered.
- The backuper2 startup did retry successfully. Attempt 1 waited 65 seconds
  (the code checks `> 60` in five-second waits), timed out at 08:51:51, slept
  five seconds, then attempt 2 returned an empty interface list in roughly
  18 ms at 08:51:56. This is the intended behavior added by `15e630312`: read
  RPCs have up to 30 attempts, while write RPCs would not be retried.
- The source and supplied client journal cannot distinguish whether attempt
  1's request or response was lost, or whether supervisor handling was delayed
  beyond the hard timeout. The supervisor has no per-request success/timing
  log, and the client replaces the correlation ID on retry, so a late first
  reply is silently ignored. The original retry commit explicitly records the
  same failure mode as intermittent and its underlying reason as unclear.
- The two incidents are independent in code. Supervisor uses a separate Bunny
  channel and one-thread work pool per consumer class; the OOM failures are on
  channel 8, while Node RPC has its own channel. An OOM handler exception is
  caught by Bunny's OOM-channel worker loop and cannot block the RPC channel.
- Every supervisor-created Bunny channel now has one shared uncaught-exception
  handler that logs the consumer plus Ruby's complete exception, backtrace,
  and cause chain without logging payloads.
- OOM task `host_uid` and `vps_uid` now use unsigned 32-bit columns. The
  migration rejects negative predecessor data and refuses a rollback that
  would truncate newly stored high UIDs.
- OOM task range failures now report the parent report/VPS, task count, and a
  bounded list of exact task fields and values. The original
  `ActiveModel::RangeError` remains the exception cause, including if
  diagnostic formatting itself fails.

## Open questions

- Which VPS/processes on node5 use user-namespace block 32,772? This is useful
  incident context but not needed to establish the schema root cause. It can
  only be recovered from node5's kernel OOM task lines, the live namespace-map
  inventory, or richer consumer logging; current failed task batches were not
  persisted.
- The exact transport/server-side reason for backuper2 attempt 1 requires
  RabbitMQ connection/queue evidence and api1 supervisor correlation around
  08:50:46--08:51:56. Current code emits neither request receipt nor response
  publication timing, so the supplied logs cannot resolve it retrospectively.

## Cleanup

Removed the temporary configuration worktree and its generated `.bin/` and
`.bundle/` Nix-shell caches. Retained branch
`2026-08-09-supervisor-exceptions` per workspace policy.
