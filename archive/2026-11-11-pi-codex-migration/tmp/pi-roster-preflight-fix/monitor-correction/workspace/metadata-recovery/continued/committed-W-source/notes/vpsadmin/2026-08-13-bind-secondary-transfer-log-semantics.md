# BIND secondary transfer logs are attempt telemetry

## Symptom

A line-oriented parser can report healthy transfers as failures and failed or
rejected transfers as successes. This was found while auditing
`work/2026-08-12-dns-secondary-zone-transfer-failure` against deployed BIND
9.20.26.

## Cause

- `xfrin_destroy()` always logs `Transfer status` followed by `Transfer
  completed`. The completion line contains accounting; it is not a success
  marker and can contain records, bytes, and a serial after failure.
- `IXFR failed` normally causes an immediate AXFR retry. Shutdown, forced
  retransfer, and reconfiguration also terminate individual transfer contexts.
- Refresh errors apply to one primary. BIND can retry its transport or advance
  to another primary, whose equal-serial response has no INFO success line.
- Secondary MX/SRV targets without address records are nonfatal warnings.
  Failure to load a secondary master file concerns BIND's local cache.
- The accepted-transfer signal is `transferred serial <serial>`, emitted after
  BIND validates the transferred database's SOA and NS records.

The central behavior is present in BIND 9.18 and 9.20. BIND 9.20 adds a
transfer-context pointer, but it does not correlate IXFR-to-AXFR or
primary-to-primary fallback.

## Safe approach

Do not treat isolated transfer/refresh attempt messages as user-visible zone
health. Keep them as diagnostics. Stop using `Transfer completed` as success;
use accepted `transferred serial` and explicit up-to-date outcomes. Gate user
notification on whether BIND has a loaded, accepted zone and whether its expiry
or staleness indicates that retries across all primaries have actually failed.

## Verification

A direct parser probe reproduced a failed FORMERR sequence as two failure
events followed by false success from a nonempty completion summary. Source
control flow and upstream tests confirmed unconditional completion logging,
IXFR fallback, forced-retransfer cancellation, nonfatal secondary warnings,
post-transfer SOA/NS rejection, and the accepted-serial log boundary.
