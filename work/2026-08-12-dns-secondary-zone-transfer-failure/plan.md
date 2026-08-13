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
