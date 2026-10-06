# 2026-07-07-secondary-dns-transfer-check

## Goal

Investigate and fix misleading DNS secondary transfer logs where nodectld
records a successful transfer for BIND timeout attempts that end with
`Transfer completed: 0 messages, 0 records, ... (serial 0)`.

## Affected repositories

- `vpsadmin`
  - `libnodectld` parses BIND journal messages and publishes DNS transfer
    events.
  - `api`/supervisor stores those events and updates `DnsServerZone`
    latest-transfer fields.
  - Existing integration coverage is in
    `tests/suite/dns/secondary-transfer-errors.nix`.

## Approach

- Confirm the parser behavior against the BIND log sequence from ns3.
- Prefer fixing `libnodectld` to avoid publishing imaginary success events
  from failed BIND transfer summaries.
- Add an API supervisor-side guard for the same empty completion event so a
  central API update protects against older nodectld instances during a rolling
  deployment.
- Remove already persisted bogus success logs with a data migration, repairing
  `DnsServerZone` latest-transfer fields to the newest remaining log.
- Add unit coverage for the observed zero-message/zero-record timeout
  completion line.
- Consider whether integration coverage should include the full BIND timeout
  sequence: `failed to connect`, `Transfer status: timed out`, and final
  zero-record `Transfer completed`.

## Compatibility and deployment

- Event schema should remain unchanged for supervisor/API/WebUI compatibility.
- New nodectld/libnodectld must be safe with existing supervisors: the fix
  should only suppress a bogus success event.
- Rolling upgrades are acceptable: updated nodectld/libnodectld stops emitting
  bogus success logs, and updated API/supervisor drops the same event if an
  older node publishes it before every node is upgraded.
- Existing persisted bogus successful logs are corrected by a data migration.
  The migration is irreversible because deleted synthetic rows cannot be
  reconstructed, but the deleted rows are derived from failed transfer attempts
  and latest-transfer state is restored from remaining logs.

## Testing plan

- Reproduce current parser behavior for the observed BIND timeout completion
  line.
- Run focused `libnodectld` specs after any parser change.
- Run migration specs and supervisor specs for data cleanup and rolling-upgrade
  ingestion behavior.
- If the change expands integration coverage, run
  `./test-runner.sh test dns/secondary-transfer-errors`.
