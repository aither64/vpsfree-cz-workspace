# 2026-08-12-dns-secondary-zone-transfer-failure

## Goal

Make user-facing secondary DNS transfer reporting follow BIND's actual transfer
semantics. Track each direct path from a vpsAdmin secondary to a configured user
primary independently from whether the zone is loaded and served through a
vpsAdmin peer. Preserve recovery after rolling reboots without allowing peer
success or NOTIFY traffic to hide broken user-primary authorization.

## Affected repositories

- `vpsadmin`: small BIND 9.18/9.20 logging patches, stateful parser, event
  protocol, schema and state model, supervisor, API, WebUI, migrations, and
  tests.
- `vpsfree-mail-templates`: zone-level confirmed and closed alert templates.
- `vpsfree-cz-configuration`: patched BIND selection, zone-level production
  monitor, and exact vpsAdmin revision pin.
- `vpsfree-kb-contracts`: exact vpsAdmin pin and review of the visible Primary
  servers status change.

## Design

- Keep BIND `DnsStatus` as the source for loaded/served zone health. Add an
  internal state for every current `(secondary, configured user primary)` path.
- Parse complete BIND 9.18/9.20 attempts. Completion counters are never success;
  engine success requires an accepted `transferred serial` marker. Suppress IXFR
  fallback, lifecycle noise, harmless MX/SRV warnings, and local cache errors
  from user health.
- Classify explicit remote/configuration errors separately from network errors.
  Explicit failures become alertable after 30 minutes. A network failure is
  alertable only when failed observations on that path span at least 24 hours;
  one transient reboot-time failure cannot open an incident.
- Patch BIND's already-validated equal-serial SOA response branch to emit one
  INFO message identifying the primary, source, and serial. Treat that message,
  BIND's existing older-primary-serial message, and a same-primary current
  NOTIFY as positive reachability evidence which changes only a network failure
  to unknown. Routine positive refresh/NOTIFY observations are not persisted as
  transfer-log rows; their per-path ordering watermark is retained in state.
- Treat xfrin `Transfer status: up to date` as refresh evidence, not proof that
  AXFR is authorized: BIND also emits it for SOA-before-AXFR paths. Only an
  accepted `transferred serial` clears an explicit REFUSED, TSIG, protocol, or
  zone failure. Peer transfers and peer NOTIFY never clear user-primary state.
- Expose one aggregate `success`/`failed`/`unknown` status on each Primary
  servers row. Keep the internal matrix out of the WebUI and send one monitoring
  incident per DNS zone. Delay opening until a path is eligible, but once an
  incident is active keep it open until every current path has recovered.
  Suppress repeat mail while only younger, non-eligible failures keep it open.
- Purge unsafe legacy completion, NOTIFY, refresh, fallback, lifecycle, warning,
  and local-cache rows. Repair cached latest-transfer fields but do not seed new
  direct-path state from old history. Purge legacy server-zone monitoring
  incidents because the monitor now owns one DNS-zone object per incident.
- Do not add active probes or compatibility handling for old nodectld events.

## Network-outage decision

BIND's stock INFO log cannot distinguish a primary that stayed down from one
that recovered and answered an equal-serial SOA refresh. The user accepted a
small BIND patch instead of dropping long network-outage alerts. The patch adds
five logging lines in the existing successful branch and changes no DNS
protocol, timing, transfer, or state behavior. Separate minimal hunks cover the
9.18 and 9.20 implementations of the adjacent primary-health bookkeeping.

## Compatibility and deployment

- The node event adds attempt kind and failure classification while retaining
  the existing success/failed envelope. The new consumer intentionally does not
  accept old events without this classification.
- Patched BIND, the new nodectld parser, the new supervisor/state model, the
  zone-level monitor, and its templates are one compatibility set. Do not run
  the new monitor without positive refresh telemetry on every DNS server.
- For upgrade, first pause this monitor and drain already-enqueued old
  monitor-alert and mail transactions. Stop old API workers and other old-code
  writers which can enable a DNS zone or change its source; DNS-zone mutations
  remain unavailable through the core migration and new API activation. Stop
  old nodectld producers on every DNS server, then drain `dns_transfer_logs`
  completely with the old consumers still running. Only after the queue is
  empty, stop every old supervisor consumer for that queue. This creates an
  explicit message-format boundary: no old-format event can arrive after the
  drain. With all consumers stopped, deploy and start patched BIND and new
  nodectld on every DNS server; new-format events may safely queue. Verify the
  live `named` binaries contain `confirmed current serial` and observe the message
  from a controlled equal-serial refresh. Keep consumers stopped while the core
  and monitoring migrations, new supervisor code, templates, and configuration
  are deployed everywhere; never use a mixed-consumer cutover. Run
  `CONFIRM=1 rake vpsadmin:dns:reset_primary_transfer_tracking` once while
  writers and consumers are stopped. It repeats unsafe old-format log cleanup,
  repairs cached latest-transfer fields, establishes a fresh boundary, and
  empties path state. Verify that every enabled external zone has a non-NULL
  tracking epoch and every disabled or internal zone has NULL. Only then start
  new consumers, drain queued
  classified events, inspect fresh path state, and resume API writes and
  monitoring. The new
  consumer also checks current enabled/source state independently and fails
  closed if epoch metadata is stale.
- New path state starts unknown. Schema additions remain readable after an API
  rollback, but deleted transfer and monitoring history is irreversible.
- Rollback is also coordinated. Pause monitoring and drain its queued alert/mail
  work. Stop API workers which can acknowledge, ignore, or otherwise mutate
  monitoring events for the reset window; the reset task also locks each event
  batch transactionally. Stop new nodectld producers on every DNS server, drain
  `dns_transfer_logs` completely with new consumers, and only then stop all new
  transfer-log consumers. Stop BIND before changing its package. This prevents
  classified events from reaching the old envelope-only consumer. A stopped
  parser may retain a cursor behind an unresolved attempt, so deliberately move
  `/var/lib/nodectld/dns-transfer-log.cursor` to the current `bind.service`
  journal tail. Extract only the opaque value after `-- cursor: `; never write
  the complete human-readable `journalctl` output. With BIND and nodectld
  stopped, write it atomically with the existing cursor's ownership and mode.
  On these NixOS DNS servers nodectld runs as root and its state directory is
  `0700 root:root`, so use:

  ```sh
  cursor=$(journalctl -u bind.service -n 0 --show-cursor \
    | sed -n 's/^-- cursor: //p' | tail -n 1)
  test -n "$cursor"
  cursor_tmp=$(mktemp /var/lib/nodectld/.dns-transfer-log.cursor.XXXXXX)
  printf '%s\n' "$cursor" > "$cursor_tmp"
  chown root:root "$cursor_tmp"
  chmod 0600 "$cursor_tmp"
  mv "$cursor_tmp" /var/lib/nodectld/dns-transfer-log.cursor
  ```

  Verify that `journalctl
  --after-cursor="$(cat /var/lib/nodectld/dns-transfer-log.cursor)" -u
  bind.service -n 1` is empty. This accepts skipping the already-drained trailing
  diagnostics and prevents the old false-positive parser from replaying them.
  While the new application is still installed run
  `rake 'vpsadmin:monitoring:reset_dns_secondary_transfer_failure[DnsZone]'`.
  This repeatable, destructive task removes new monitor events and their logs.
  Restore the old templates, monitor configuration, API/core consumers, then
  start the old consumers before starting upstream BIND and old nodectld
  producers. Resume monitoring last.
  Rolling back
  patched BIND alone while the new monitor is active is unsupported because
  quiet network recovery would again be invisible.
- On a later re-upgrade, pause/drain monitoring again, stop old nodectld
  producers, drain their queue with old consumers, then stop the old consumers
  and old DNS-zone and monitoring-event writers. Deploy the new application and
  before starting new
  producers or consumers run `CONFIRM=1 rake
  vpsadmin:dns:reset_primary_transfer_tracking`. This also removes unsafe
  old-format transfer rows recreated by the old parser and repairs the cached
  latest result; only rows with NULL attempt classification are candidates.
  Before enabling the new
  zone-level monitor run
  `rake 'vpsadmin:monitoring:reset_dns_secondary_transfer_failure[DnsServerZone]'`.
  The original irreversible migration will already be recorded and therefore
  cannot remove legacy incidents recreated during the rollback. Both cleanup
  directions deliberately discard incident history and require an operator to
  confirm the reported deletion count.
- Update production configuration inputs only through `confctl`. KB production
  publication remains separately approval-gated.
- Admission and ordering compare DNS-node journal timestamps with API database
  timestamps at one-second resolution. All DNS and API hosts must keep NTP
  synchronization healthy; clock skew is an operationally monitored deployment
  assumption. The consumer deliberately rejects the entire boundary second.

## Verification

- Unit/spec coverage for full BIND 9.18/9.20 sequences, both patch variants,
  parser replay, event
  classification, state transitions, aggregation, authorization, migration
  cleanup, pruning, and bilingual mail rendering.
- Real-BIND integration coverage for peer distribution, direct-primary failure,
  a continuously down primary, recovery through the patched equal-serial
  refresh, rolling-reboot protection, same-primary network NOTIFY recovery,
  peer NOTIFY isolation, and explicit-error persistence.
- WebUI browser coverage and the canonical KB contract/capture workflow.
- Prepare guarded Czech and English KB candidates explaining direct-transfer
  status and alert delays. Production publication remains separately approved.
- Run focused lint/specs and repository hooks, commit all intended changes, then
  invoke the mandatory standalone review before long integration/configuration
  builds. Merge through fresh worktrees using fast-forward-only integration.
