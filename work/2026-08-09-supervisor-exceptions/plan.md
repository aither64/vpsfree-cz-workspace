# 2026-08-09-supervisor-exceptions

## Goal

Fix production OOM report ingestion for valid host UIDs above the signed
32-bit limit and make uncaught vpsadmin-supervisor consumer exceptions useful
for diagnosis across all queues.

## Affected repositories

- `vpsadmin`: supervisor channel error handling, OOM task schema and ingestion,
  migration/spec coverage.
- `vpsfree-cz-configuration`: deployment pin update after the vpsadmin changes
  are merged or an exact revision is selected for rollout.

## Approach

1. Install a full-backtrace uncaught-exception handler on every Bunny channel
   created by the supervisor. Keep existing auto/manual acknowledgement
   semantics and never log message payloads.
2. Change `oom_report_tasks.host_uid` and `vps_uid` from signed to unsigned
   32-bit integers in one bulk table alteration, with data-integrity checks and
   a lossless-only rollback.
3. Add OOM-specific context for task serialization range failures while
   retaining the original exception as the cause handled by the shared logger.
4. Commit general supervisor logging and the OOM fix separately, run quick
   verification and mandatory fresh-agent review, then run broader API tests.

## Compatibility and deployment

- The nodectld JSON payload, RabbitMQ topology, public API, WebUI, and
  acknowledgement behavior remain unchanged.
- Mixed old/new application code can use unsigned UID columns. Every
  supervisor process must restart after migration to refresh Active Record's
  cached column metadata.
- Code rollback keeps the unsigned schema. Migration rollback is allowed only
  while all stored UIDs still fit signed 32-bit storage.
- Production rollout pauses all supervisor consumers and OOM pruning while the
  MariaDB table-copying type change runs. Durable quorum queues buffer reports.
- Historical partially persisted reports are retained because their auto-acked
  task payloads cannot be reconstructed safely.

## Testing plan

- Specs for shared channel creation and full exception/cause backtraces.
- Migration specs for high unsigned UIDs, nullability, negative-data rejection,
  and safe/refused rollback paths.
- OOM consumer specs for the observed production UID and contextual
  out-of-range task diagnostics.
- Targeted RSpec and RuboCop checks, migration coverage validation, mandatory
  standalone change review, relevant broader API specs, and GitHub Actions.
