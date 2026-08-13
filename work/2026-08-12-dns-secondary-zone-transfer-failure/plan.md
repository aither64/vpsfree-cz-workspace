# 2026-08-12-dns-secondary-zone-transfer-failure

## Goal

Make user-facing secondary DNS transfer reporting follow BIND's actual transfer
semantics. Track each direct path from a vpsAdmin secondary to a configured user
primary independently from whether the zone is loaded and served through a
vpsAdmin peer. Preserve recovery after rolling reboots without allowing peer
success or NOTIFY traffic to hide broken user-primary authorization.

## Affected repositories

- `vpsadmin`: stateful BIND parser, event protocol, schema and state model,
  supervisor, API, WebUI, migrations, and tests.
- `vpsfree-mail-templates`: zone-level confirmed and closed alert templates.
- `vpsfree-cz-configuration`: zone-level production monitor and exact vpsAdmin
  revision pin.
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
  Explicit failures become alertable after 30 minutes; network failures after
  24 hours. Same-primary accepted/up-to-date transfer clears any failure.
- Treat same-primary `notify ... zone is up to date` as recovery only for a
  network failure. Peer transfers and peer NOTIFY never clear user-primary
  state.
- Expose one aggregate `success`/`failed`/`unknown` status on each Primary
  servers row. Keep the internal matrix out of the WebUI and send one monitoring
  incident per DNS zone.
- Purge unsafe legacy completion, NOTIFY, refresh, fallback, lifecycle, warning,
  and local-cache rows. Repair cached latest-transfer fields but do not seed new
  direct-path state from old history. Purge legacy server-zone monitoring
  incidents because the monitor now owns one DNS-zone object per incident.
- Do not add active probes or compatibility handling for old nodectld events.

## Compatibility and deployment

- The node event adds attempt kind and failure classification while retaining
  the existing success/failed envelope. The new consumer intentionally does not
  accept old events without this classification.
- Deploy nodectld to every DNS server and drain queued old events first. Then
  pause monitoring during the schema/template/monitor switch, deploy the
  vpsAdmin core and monitoring-plugin migrations and services, install updated
  templates, deploy the new configuration, inspect fresh state, and resume
  monitoring.
- New path state starts unknown. Schema additions remain readable after an API
  rollback, but deleted history is irreversible. Rolling nodectld back requires
  a coordinated consumer/API rollback.
- Update production configuration inputs only through `confctl`. KB production
  publication remains separately approval-gated.

## Verification

- Unit/spec coverage for full BIND 9.18/9.20 sequences, parser replay, event
  classification, state transitions, aggregation, authorization, migration
  cleanup, pruning, and bilingual mail rendering.
- Real-BIND integration coverage for peer distribution, direct-primary failure,
  rolling-reboot recovery, same-primary network NOTIFY recovery, peer NOTIFY
  isolation, and explicit-error persistence.
- WebUI browser coverage and the canonical KB contract/capture workflow.
- Prepare guarded Czech and English KB candidates explaining direct-transfer
  status and alert delays. Production publication remains separately approved.
- Run focused lint/specs and repository hooks, commit all intended changes, then
  invoke the mandatory standalone review before long integration/configuration
  builds. Merge through fresh worktrees using fast-forward-only integration.
