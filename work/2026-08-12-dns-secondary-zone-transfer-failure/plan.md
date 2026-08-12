# 2026-08-12-dns-secondary-zone-transfer-failure

## Goal

Prevent BIND's successful `Transfer status: up to date` result from being
recorded as a failed secondary DNS transfer, remove existing synthetic failure
rows, repair current transfer state, and prepare the exact production
configuration pin on unmerged feature branches.

## Affected repositories

- `vpsadmin`
  - `libnodectld` parses BIND journal messages into normalized transfer events.
  - the API supervisor persists those events and updates the latest transfer
    state.
  - the WebUI displays every persisted transfer-log row.
- `vpsfree-cz-configuration`
  - pin `vpsadminServices` to the exact unmerged vpsAdmin feature revision for
    review and build validation.

## Approach

- Ignore `Transfer status: up to date` in `libnodectld`, like the already
  ignored `Transfer status: success`, because BIND follows it with the richer
  completion event.
- Add a supervisor-side compatibility filter for older nodectld versions. Mark
  it with a searchable TODO explaining that it can be removed only after all
  DNS nodes are updated and old queued events are drained.
- Add a data migration that deletes precisely identified synthetic failures
  and repairs every `last_transfer_*` field when a deleted row is current.
- Leave the configuration monitoring rule unchanged: it reads
  `last_transfer_status`, which the migration and future completion events
  repair.
- Pin the exact vpsAdmin feature head through confctl on a separate
  `vpsfree-cz-configuration` feature branch.

## Compatibility and deployment

- The event protocol and database schema shape remain unchanged.
- Mixed-version event handling is safe in either direction: new nodectld
  suppresses the event for an old supervisor, while the new supervisor drops
  it from an old nodectld.
- Deploy the guarded API supervisor revision to every API host before running
  the cleanup migration. The new supervisor and migration serialize writes on
  each DNS-server-zone row, so the migration can run online without replacing
  a newer completion. After migration, roll out ns3/ns4; the API guard remains
  until every DNS node is updated and older queued events have drained.
- The cleanup migration is irreversible because synthetic history cannot be
  reconstructed. Rollback can still load the unchanged schema, but rolling
  back both guards can recreate false rows.
- The monitoring rule becomes healthy on its next 30-minute evaluation after
  `last_transfer_status` is repaired; monitoring history is preserved.
- Stop with pushed feature branches. Do not merge, deploy, or change
  production state.

## Testing plan

- Add parser coverage for the exact prefixed status, case-insensitive matching,
  real failures, and the following zero-byte/one-record success completion.
- Add supervisor coverage for the older-node compatibility filter and nearby
  legitimate unknown failures.
- Add migration coverage for deletion, same-second replacement, older failure
  replacement, empty state, and near-matching rows that must remain.
- Extend `dns/secondary-transfer-errors` with the observed pair and assert that
  only the completion produces a stored success.
- Run focused specs and lint, mandatory standalone review, the DNS integration
  test, and confctl builds for all vpsAdmin services plus ns3 and ns4.
