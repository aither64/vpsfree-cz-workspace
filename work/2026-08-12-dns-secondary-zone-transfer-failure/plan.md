# 2026-08-12 DNS secondary transfer monitoring

## Goal

Report two separate facts without implying that every secondary naturally
transfers from every configured primary:

- whether each managed secondary currently has the zone loaded and is serving
  it; and
- whether every configured user primary is presently able to serve a valid,
  authenticated transfer to every managed secondary.

Retain BIND's real transfer diagnostics, including rejected transfers, invalid
zone contents and malformed transfer responses. Replace sparse passive
observation as the M:N coverage mechanism with bounded active probes.

## Affected repositories

- `vpsadmin`: BIND log parsing, node configuration and probe worker, event
  protocol, schema/state model, supervisor, API, WebUI, migrations and tests.
- `vpsfree-cz-configuration`: zone-level production monitor and exact vpsAdmin
  feature pin. Production returns to the single stock `pkgs.bind` package.
- `vpsfree-mail-templates`: zone-level confirmed and closed alert templates.
- `vpsfree-kb-contracts`: exact feature pin, navigation/capture contract and
  Czech/English candidate documentation.
- workspace coordination repository: durable plan/state and complete-page KB
  release candidates, plus a disposable-dev-cluster import adjustment so the
  final notification-template input can be deployed for WebUI review.

## Collection design

### Passive BIND diagnostics

- Keep the correlated parser for complete BIND transfer attempts.
- `Transfer completed` is accounting, never success. An accepted
  `transferred serial` is a real transfer success.
- Preserve actionable TSIG/ACL, network, protocol and invalid-zone failures.
- Suppress transient IXFR-to-AXFR fallback, lifecycle/cancellation noise,
  harmless MX/SRV warnings and local secondary cache-load errors from user
  health while retaining appropriate admin diagnostics.
- Mark configured user primaries distinctly from vpsAdmin secondary peers.
  Peer success never clears a user's primary-path failure.
- Retain new-envelope BIND diagnostics without a user-primary association for
  administrators, including managed peer and internal-zone activity; these
  rows never enter user-visible primary readiness.
- The already-deployed correction for `Transfer status: up to date` remains in
  the production baseline. The new feature does not reimplement compatibility
  for the pre-fix event format.

### Active M:N probe

- Probe every current `(managed secondary, configured user primary)` path.
  Never probe vpsAdmin peer secondaries as user primaries.
- Carry stable `dns_server_zone_id`, `dns_zone_transfer_id` and an opaque
  configuration generation in node configuration and every event. The API
  consumer accepts an event only when all three still identify the current,
  enabled external-zone path.
- Snapshot path IDs and generation when a passive BIND transfer starts. On
  journal replay, associate a transfer only when its first entry is strictly
  newer than the current tracking boundary. Configuration changes while a
  transfer is running therefore cannot apply its terminal result to a new path.
- Use the secondary's real transfer source address and the configured TSIG key.
  First read the primary's SOA, then issue a TCP IXFR query at that primary
  serial, signed with the configured TSIG when present. BIND checks transfer
  ACL/TSIG before returning the current SOA, so this is a cheap positive check
  of direct transfer readiness.
- Run healthy paths hourly with deterministic staggering. Retry failed
  access/network paths every five minutes. Retry invalid-zone, protocol and
  stale results hourly so a large or hostile zone cannot force a full download
  every five minutes. Bound probe concurrency and add timeouts so one primary
  cannot monopolize the node worker.
- Escalate to a temporary full AXFR only when there is no local serial, IXFR is
  unsupported/inconclusive, or a prior content/protocol failure needs positive
  recovery evidence. Validate downloaded data with `named-checkzone` before
  reporting success. Never publish zone contents or TSIG secrets.
- Default full-transfer safeguards are two concurrent AXFRs, 256 MiB per
  response and ten minutes. A local safeguard hit is inconclusive/admin-only,
  not evidence that the user's server is broken.
- A cheap IXFR success clears access/network failures. Invalid-zone/content or
  protocol failures clear only after BIND accepts a real transfer or a complete
  probe AXFR validates successfully.
- If a reachable, valid primary's SOA serial remains behind the secondary,
  classify it as `stale`. This affects primary readiness, not secondary serving
  status.
- Emit routine positive observations as state watermarks without permanent log
  growth. Persist probe history on failure/reason transitions and recovery;
  persist every meaningful real BIND transfer outcome.

### Unprivileged probe execution follow-up

- Keep scheduling, live `DnsConfig` lookup, the durable full-AXFR latch and
  RabbitMQ publication in nodectld, but move all `dig`, AXFR download and
  `named-checkzone` processing into a one-shot `vpsadmin-dns-transfer-probe`
  worker.
- Start each worker as a hardened transient systemd service with a private
  dynamic user. Pass exactly one immutable path description through stdin and
  accept only one bounded, schema-validated JSON result on stdout. The worker
  receives no RabbitMQ/database credentials and never gets to choose path IDs,
  generations or event keys.
- Give the worker a private temporary directory, no capabilities, no privilege
  escalation, a read-only/protected filesystem view, inaccessible BIND and
  nodectld state paths, restricted namespaces/address families, resource
  limits and network access only to the selected primary. Never put TSIG
  secrets or user-controlled names in argv, environment, unit names or journal
  metadata.
- The selected primary IP address is the deliberate metadata exception:
  `systemd-run` must receive it in `IPAddressAllow` to install the per-unit
  network allowlist. It is public path configuration, not a secret. The zone
  name, source address, TSIG and query remain confined to the bounded stdin job
  and private worker files; the transient unit name is an opaque digest/random
  value.
- Recompute the current M:N path set continuously. Schedule a new zone/primary
  path with deterministic jitter of at most 60 seconds. Remove pending work and
  cancel a running unit when a primary or zone disappears. Drop cancelled or
  obsolete results, while the API's existing ID/generation/boundary checks
  remain a second line of defence.
- Preserve the full-AXFR latch across a generation change for an unchanged
  zone/primary identity and prune it when that path is actually removed.
- Keep the combined transfer log and its existing daily 365-day retention.
  Probe rows remain transition-oriented: first failure, changed reason/class,
  alert-eligibility milestone, recovery and a later post-recovery failure.
  Identical retries and routine healthy observations do not create rows.
- Treat the worker job/result JSON as an internal contract of one nodectld
  package revision, not as another service protocol. Deploy the nodectld
  scheduler, worker executable and NixOS unit settings together on each DNS
  node. The follow-up does not change the RabbitMQ event envelope, database
  schema or on-disk AXFR latch format.
- Transient workers are tied to `nodectld.service`, have no durable state and
  are stopped with the parent service. Rolling back the whole nodectld package
  therefore cannot leave an old worker processing a new scheduler job.

## API and state model

- Maintain current path state per `(DnsServerZone, DnsZoneTransfer)` with
  source (`bind`, `ixfr_probe`, `axfr_probe`), status/reason, serials, first and
  latest failure times, last check, last success and ordering watermark.
- Process events idempotently and conservatively under the server-zone lock.
  Positive observations win timestamp ties, and old generations or events at
  the configuration boundary second are rejected.
- Explicit access, TSIG, protocol, invalid-zone and stale failures become
  alertable after continuous evidence for 30 minutes. Network failures require
  observations spanning 24 hours. A gap beyond the expected retry cadence
  resets continuity, preventing rolling node restarts from manufacturing a
  long outage.
- Keep one sticky monitoring incident per DNS zone. Delay opening until any
  path is eligible, keep an open incident until every current path has
  recovered, and suppress repeat mail while only young/noneligible failures
  remain.
- Expose a user-authorized path resource plus per-primary aggregate fields:
  `transfer_check_status`, `last_transfer_check_at`, and total/success/failed/
  pending secondary counts. The UI can fetch failed/pending path details for a
  selected primary without exposing other users' zones or TSIG material.
- Expose a derived per-secondary `zone_status`: `serving`, `expired`,
  `not_loaded` or `unknown`, based on BIND status serial/load/expiry/check data.
  Call this status “Serving”; do not claim freshness beyond the evidence.

## Database reset and compatibility

- Rewrite the unmerged `20260813120000` migration. It deletes every existing
  DNS transfer-log row, clears all `DnsServerZone.last_transfer_*` pointers and
  starts all new primary-path state as unknown. This is an intentional,
  irreversible history reset requested by the operator; no old rows are
  imported or reclassified.
- Remove the unmerged custom BIND package, both 9.18/9.20 patches and production
  package override. There is one supported stock BIND from pinned nixpkgs.
- Do not retain runtime branches for old nodectld or old supervisor payloads.
  Upgrade is a coordinated hard protocol boundary.
- Keep `dns_server_zone_transfer_logs.attempt_kind` nullable only at the
  database-schema level so the old supervisor can write after the documented
  full rollback. The new model/API require it, and the re-upgrade reset deletes
  any rollback-era nil rows before new services resume.
- Keep small guarded operational reset tasks for supported rollback and later
  re-upgrade. They reset probe generations/path state and the monitor's object
  history; they are not mixed-version compatibility code.
- The development cluster is disposable and may be reset rather than migrated
  from the earlier prototype schema.

## WebUI, mail and documentation

- “Name servers” shows resulting service state per managed secondary: server
  address/name, serving status, serial, loaded/last-check/expiry information and
  an activity-log link. Remove the duplicate direct-transfer aggregate from
  this table.
- “Primary servers” shows each configured primary's transfer readiness. Use a
  vertical/stacked layout so address, TSIG and check summary do not overflow.
  Show aggregate counts; expand/list individual secondary paths only when they
  are failed or pending.
- Label transfer-log entries by evidence source: real BIND transfer, IXFR
  readiness probe or AXFR validation.
- Make links readable in every globally styled failed/error table row, not
  only the DNS transfer table. Preserve the red row background and use a dark,
  underlined link color with explicit visited, hover and keyboard-focus states.
- Alert mail lists actionable primary/secondary paths and explains that the
  zone may still be served through another path. Advice covers reachability,
  transfer ACLs, TSIG and zone validity. Closed mail is sent only after all
  current failures recover.
- Rebuild the complete Czech/English KB candidates and review manifests through
  the canonical WebUI documentation workflow. Production wiki publication is
  separately approval-gated and is not part of implementation.

## Deployment and rollback

### Upgrade

1. Pause the DNS transfer monitor and drain already-enqueued alert/mail work.
2. Stop DNS-zone/API configuration writers. With old nodectld still running,
   drain its DNS transaction queue. Make the new release code available only
   for this schema-independent check, without starting new services, and run
   `bundle exec rake vpsadmin:dns:verify_configuration_drained`. Resolve
   failed/staged work and require a zero boundary before continuing.
3. Stop old nodectld producers on every DNS server. Drain `dns_transfer_logs`
   with old supervisors, then stop every consumer and monitoring-event writer.
4. Deploy the database/application/configuration/templates and run migrations.
   With DNS-zone writers and transfer consumers still stopped, run
   `CONFIRM=1 bundle exec rake vpsadmin:dns:reset_primary_transfer_tracking`.
   This deletes all old transfer history again, establishes fresh probe
   generations and queues complete configuration refreshes for every existing
   server-zone. Verify the queued refresh count before continuing.
5. Deploy/start new nodectld with stock BIND on all DNS servers. Let it consume
   every queued full configuration refresh; verify persisted zone JSON contains
   server-zone/transfer IDs, primary kinds, generation and probe source
   addresses. New-format events may queue.
6. Start only new supervisors, drain and inspect classified events, then resume
   API writes and monitoring.

There is no supported mixed old/new producer or consumer interval.

### Rollback and re-upgrade

- Use the same producer/queue/consumer barrier in reverse. First stop new
  DNS-zone writers. While the complete new nodectld fleet is still running,
  run `bundle exec rake vpsadmin:dns:verify_primary_transfer_configuration_drained`
  and require zero pending/in-flight new-format server-zone updates. A failed
  or partial upgrade must first restore enough new nodectld service to drain
  those transactions; rollback is blocked rather than delivering them to old
  nodectld. Then stop new nodectld producers on every DNS server, drain
  `dns_transfer_logs` with the new consumers, and stop every new consumer and
  monitoring-event writer. While the new API code is still installed, run
  `CONFIRM=1 REFRESH_CONFIGURATION=0 bundle exec rake
  vpsadmin:dns:reset_primary_transfer_tracking`, then run
  `CONFIRM=1 bundle exec rake
  'vpsadmin:monitoring:reset_dns_secondary_transfer_failure[DnsZone]'`.
  The rollback reset therefore does not enqueue new-format configuration
  refreshes for the old nodectld. Stop BIND on every DNS server, then
  deliberately advance `/var/lib/nodectld/dns-transfer-log.cursor`
  to the current `bind.service` journal tail. This accepts skipping already
  drained trailing diagnostics and prevents the old parser from replaying a
  cursor withheld behind an unresolved new-parser attempt. Extract only the
  opaque cursor value and install it atomically as root on these NixOS nodes:

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

  Verify that `journalctl --after-cursor="$(cat
  /var/lib/nodectld/dns-transfer-log.cursor)" -u bind.service -n 1` is empty.
  Restore templates/configuration/API as a coordinated set, then start old
  consumers before old BIND/nodectld producers. Let the old application issue
  its own compatible configuration refreshes after it is live.
- Before a later re-upgrade, stop old DNS-zone writers while old nodectld stays
  running. Drain its DNS transaction queue and run the new release's
  schema-independent `bundle exec rake
  vpsadmin:dns:verify_configuration_drained` gate. Only then stop old
  nodectld, drain `dns_transfer_logs` with old consumers and stop those
  consumers. Deploy/migrate the new API, configuration and templates while
  everything remains stopped. Run `CONFIRM=1 bundle exec rake
  vpsadmin:dns:reset_primary_transfer_tracking` with configuration refreshes
  enabled, then run `CONFIRM=1 bundle exec rake
  'vpsadmin:monitoring:reset_dns_secondary_transfer_failure[DnsServerZone]'`
  for incidents recreated by the old monitor. Start new nodectld producers,
  drain their events with only new consumers, then resume writers and
  monitoring.
- Deleted transfer and incident history is not recoverable through rollback.
- Event ordering compares node and API timestamps. Healthy NTP on DNS and API
  hosts is an operational prerequisite.

## Implementation sequence

1. Rebase all unmerged feature branches on current defaults and rewrite the
   vpsAdmin series into focused parser, probe, state/API, monitoring, WebUI and
   integration-test commits. Remove the custom-BIND commit entirely.
2. Rewrite monitoring/configuration, mail templates and KB contracts against
   the final vpsAdmin head. Update configuration pins only through `confctl`.
3. Run focused specs, lint, formatters, schema/API i18n generation and hooks.
   Commit and push all intended changes.
4. Run the mandatory fresh-context change review. Resolve or explicitly discuss
   every Blocking/Important finding before long validation.
5. Run the real-BIND M:N scenario with at least two primaries and two managed
   secondaries, Playwright WebUI coverage, exact-pinned configuration builds,
   mail rendering and KB contract validation.
6. Reset and redeploy the dedicated development cluster with review fixtures.

The unprivileged-worker follow-up is added as its own functional commit after
the original probe implementation. The global WebUI contrast fix is a separate
commit. The generated configuration and documentation pins are rewritten so
each downstream repository retains a single exact feature-pin update.

## Required test coverage

- Probe unit tests: cadence/jitter/retry, exact source binding, TSIG secret
  hygiene, classifications, IXFR and full-AXFR paths, size/time/concurrency
  limits and temporary-file cleanup.
- Worker/runner tests: stdin/stdout schema, transient-unit hardening, dynamic
  UID, secret-free process metadata, output bounds, cancellation, malformed
  output and local launch/resource failures.
- Runtime churn: create/delete zones and add/remove primaries while nodectld is
  running, verify new paths are scheduled within 60 seconds, and prove an
  in-flight old-generation result cannot update or recreate path state.
- Parser tests: complete BIND attempt sequences, completion-after-failure,
  IXFR fallback, lifecycle/local/warning noise, peer isolation and all retained
  actionable failures.
- State/API tests: precedence and recovery rules, out-of-order/idempotent
  delivery, generation boundaries, continuity gaps/reboots, alert delays,
  authorization, aggregate/detail shape, bounded log volume and reset tasks.
- Real BIND: two primaries/two secondaries, probe coverage of all paths, ACL
  omissions on one secondary, prolonged outage, invalid-zone diagnostics,
  full-AXFR recovery and secondary peer distribution while direct probes fail.
  Exact TSIG and stale-serial classifications are covered in the probe suite.
- UI/mail/docs: vertical primary layout, secondary serving state, bilingual
  templates, global failed-row link contrast, Playwright behavior and full KB
  contract/candidate verification.
