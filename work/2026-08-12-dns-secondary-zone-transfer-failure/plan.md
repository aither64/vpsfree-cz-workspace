# 2026-08-12-dns-secondary-zone-transfer-failure

## Goal

Prevent BIND's successful `Transfer status: up to date` result from being
recorded as a failed secondary DNS transfer, remove existing synthetic failure
rows, repair current transfer state, and merge the exact production
configuration pin into the default branches.

## Affected repositories

- `vpsadmin`
  - `libnodectld` parses BIND journal messages into normalized transfer events.
  - the API supervisor persists those events and updates the latest transfer
    state.
  - the WebUI displays every persisted transfer-log row.
- `vpsfree-cz-configuration`
  - pin `vpsadminServices` to the exact merged vpsAdmin revision for review,
    build validation, and later ordered deployment.

## Approach

- Ignore `Transfer status: up to date` in `libnodectld`, like the already
  ignored `Transfer status: success`, because BIND follows it with the richer
  completion event.
- Keep the supervisor free of compatibility filtering. The rollout updates
  nodectld on all DNS nodes and drains queued events before the API cleanup.
- Add a data migration that deletes precisely identified synthetic failures
  and repairs every `last_transfer_*` field when a deleted row is current.
- Leave the configuration monitoring rule unchanged: it reads
  `last_transfer_status`, which the migration and future completion events
  repair.
- Pin the exact vpsAdmin head through confctl on a separate
  `vpsfree-cz-configuration` feature branch, then fast-forward both default
  branches after validation.

## Compatibility and deployment

- The event protocol and database schema shape remain unchanged.
- Deploy the new nodectld revision to every DNS node first and allow transfer
  events produced by older nodectld versions to drain from the queue. Then
  deploy the new supervisor revision to every API host before running the
  cleanup migration. The supervisor and migration serialize writes on each
  DNS-server-zone row, so the migration can run online without replacing a
  newer completion.
- The cleanup migration is irreversible because synthetic history cannot be
  reconstructed. Rollback can still load the unchanged schema, but rolling
  back the nodectld parser change can recreate false rows.
- The monitoring rule becomes healthy on its next 30-minute evaluation after
  `last_transfer_status` is repaired; monitoring history is preserved.
- Merge both repositories by fast-forward after validation. Do not deploy,
  run the cleanup migration, or otherwise change production state.

## Testing plan

- Add parser coverage for the exact prefixed status, case-insensitive matching,
  real failures, and the following zero-byte/one-record success completion.
- Keep supervisor coverage for serialized transfer-state persistence.
- Add migration coverage for deletion, same-second replacement, older failure
  replacement, empty state, and near-matching rows that must remain.
- Extend `dns/secondary-transfer-errors` with the observed pair and assert that
  only the completion produces a stored success.
- Run focused specs and lint, mandatory standalone review, the DNS integration
  test, and confctl builds for all vpsAdmin services plus ns3 and ns4.

## Follow-up BIND transfer-log audit (2026-08-13)

### Goal

Check the complete BIND 9.20 transfer and refresh message flow against the
merged parser before treating its events as reliable user-facing health.

### Approach

- Audit the exact deployed BIND 9.20.26 source and its system tests, with a
  comparison against the supported 9.18 branch where message semantics differ.
- Enumerate transfer-engine, transfer-manager, refresh, and post-load messages,
  including retry, fallback, cancellation, and local failure paths.
- Run representative full message sequences through the feature-branch parser,
  rather than evaluating isolated regex examples only.
- Classify messages by provenance and finality: accepted zone state, remote
  primary attempt, local DNS-server fault, or infrastructure lifecycle event.
- Record findings and recommend a follow-up design. This phase is read-only;
  parser changes require a separate implementation decision.

### Compatibility and deployment consequences

- BIND 9.18 and 9.20 share the central hazards: completion accounting is
  unconditional and IXFR failures can be followed by AXFR. BIND 9.20 adds a
  transfer-context pointer and reports shutdown as `shutting down`; BIND 9.18
  can report `operation canceled` and rewrite it as `IXFR failed`.
- A safe follow-up must not require atomic upgrades merely to understand the
  log vocabulary. Unknown or uncorrelated attempt messages should be retained
  as internal diagnostics, not promoted to user failures.
- Existing BIND statistics already publish loaded, serial, refresh, and expiry
  state. User notification should be gated by accepted/served zone health or
  staleness, so retries across primaries and deployments cannot create alerts.

### Verification plan

- Reproduce a failed transfer with nonzero accounting, IXFR fallback,
  cancellation, a nonfatal MX/SRV warning, and a local cache-file load error.
- Verify upstream control flow for equal-serial refresh, per-primary fallback,
  post-transfer SOA/NS validation, and accepted `transferred serial` logging.
- Document parser coverage gaps and the minimum safe remediation separately
  from the recommended health-oriented design.
