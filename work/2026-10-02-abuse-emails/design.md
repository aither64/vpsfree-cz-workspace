# Abuse email parsing: design and verification brief

## Scope and evidence

Proposal based on all nine originals and local canonical configuration HEAD
`b6e650ad902482b4c4e66b5a89a4275bed92419e`. vpsAdmin interfaces were inspected
read-only at `9fc0648accd414246d6422e67106ae7217486020`. These are inspected
snapshots, not verified production revisions. No application edits, incidents,
commits, deployments or mailbox operations were performed.

Implement only in `vpsfree-cz-configuration`, retaining the existing
`parse -> Array<IncidentReport>` interface. Create one incident per incoming
report/source, using its latest relevant event. The three Burina reports remain
separate despite overlapping history. Exclude framework redesign, cross-message
deduplication, historical replay and vpsAdmin core/schema changes.

Original uploads and identifying bulk evidence stay outside version control.
Tests use synthetic equivalents; this brief retains only structural findings
and ticket references. The architect owns design; implementers own application
edits; the lead accepts material deviations and maintains tracking records.

## Routing and timestamp matrix

Expected times assume valid historical assignments and the privacy checks below.
UTC conversions were checked; application tests were inspected, not executed.

| Ticket | Format and current behavior | Proposed handling | Expected UTC `detected_at` |
| --- | --- | --- | --- |
| #95347 | Blocklist.de XARF 0.2 `report.txt`; unidentified | Extend structured-text XARF routing; complete RFC 2822 `Date`; log attachment has only a heading | `2026-09-28T08:41:50Z` |
| #95348 | Provider.tools inline `X-XARF: PLAIN`; unidentified | Narrow inline profile; choose summary `Last seen`, retain `Date` as generation metadata | `2026-09-28T08:44:40.114Z` |
| #95350 | Burina Fail2Ban SSH syslog; routed but returns no incident | Parse source-bound syslog with year inference and explicit `+0200` | `2026-09-28T09:23:02Z` |
| #95351 | LRob/Shieldlist JSON XARF 4.2.0; unidentified | Dedicated provider adapter using existing decoder; JSON `timestamp` | `2026-09-28T09:29:00Z` |
| #95353 | CEDO Fail2Ban XARF 0.2 attachments; unidentified | Same structured-text extension as #95347; RFC 2822 `Date` | `2026-09-28T09:36:08Z` |
| #95355 | Second Burina syslog report; routed but returns no incident | Same syslog extension, maximum event time | `2026-09-28T10:32:52Z` |
| #95356 | Cisilino bilingual UTC range; unidentified | Narrow prose adapter, labeled source and UTC `Last seen` | `2026-09-28T10:38:19Z` |
| #95360 | Third Burina syslog report; routed but returns no incident | Same syslog extension, maximum event time | `2026-09-28T11:46:46Z` |
| #95361 | Custom Visuals prose and wrapped SSH record; unidentified | Narrow adapter; full log timestamp with explicit `-05:00` | `2026-09-28T11:57:11.439254Z` |

Three messages match a parser; six miss routing. None currently reaches incident
construction on the inspected code paths. Fail2Ban's `abuse .* from` body regex
misses the exact `abuse from` wording. The subject fallback then calls
`parse_access_log_time(fallback: false)`, which accepts Apache timestamps but
not these syslog records. The legacy handler still marks the message processed.

LRob's JSON meets the existing `XArfDecoder` core shape, including a valid UUID v4.
The gaps are originator admission, absent feedback MIME part and unsupported
provider/type dispatch. Do not render login attacks as Abusix spam.

## Implementation boundaries and routing

Paths below are relative to `configs/vpsadmin/api/` unless stated otherwise.

- `incident_reports.rb`: register narrow provider adapters before generic XARF.
- `abuse_notice_parser/x_arf.rb`: preserve the old ISO-subject path; add
  `match_message?` profiles for Blocklist.de/CEDO structured attachments and
  Provider.tools inline fields. Parse selected sections, not flattened mail.
- `abuse_notice_parser/fail2ban.rb`: support the exact observed prose and SSH
  syslog timestamps; preserve original Fail2Ban and Apache paths.
- New `abuse_notice_parser/{lrob,cisilino,custom_visuals}.rb`: small adapters.
  LRob uses `XArfDecoder`; leave Abusix/Netcraft `XArfJson` admission and stable
  Netcraft duplicate subjects unchanged. Decoder expansion is unnecessary.
- `utils.rb`: only small helpers needed for strict times, section selection,
  content limits and assignment interval coverage; avoid unrelated refactoring.
- Add focused specs under repository `spec/configs/vpsadmin/api/`, synthetic
  fixtures under `spec/fixtures/emails/`, and supported behavior to API `README.md`.

New profiles check exact `X-RT-Originator` addresses: `abuse-team@blocklist.de`,
`www-root@cedo.com`, `noreply@provider.tools`, `abusereport@lrob.net`,
`notifiche@cisilino.com`, `abuse@customvisuals.com`. Preserve existing Burina
routing policy. `CHECK_SENDER` may bypass identity checks for diagnostics;
required structure/source/time validation remains. RT originator selects a
provider within trusted ingestion; it does not prove an allegation is true.

Blocklist.de/CEDO require one recognized `report.txt` block with unique required
keys (`Source-Type`, `Source`, `Date`, `Version`, category/type). Allow leading
`---`, optional fields and descriptive `Port: ssh`; do not evaluate YAML.
Provider.tools requires its inline marker, source/type and coherent summary.
LRob requires one `application/json` attachment named `xarf.json`, matching
sender/reporter identity and `connection/login_attack`. Its missing feedback MIME
part is accepted only in this adapter. Validate contact metadata in the bounded
JSON object; the decoder result currently preserves only sender domain.

Keep report/evidence MIME boundaries. Reject competing blocks, duplicate required
keys and malformed structured data; do not fall back to prose guesses. Do not
extract report fields from forwarded messages, arbitrary logs, HTML or headers.
These nine messages need only their observed top-level MIME layouts.

## Source, time and evidence rules

Validate one host IP with `IPAddr`, reject prefixes/hostnames, and normalize it.
Use structured source fields or the adapter's explicit attacking-source phrase.
Corroborate subject/body claims; contradictions require manual review. Victim
addresses, masked targets, routing hops and URLs never trigger ownership lookup.

- XARF text: complete RFC 2822 numeric-offset or existing ISO `Date` fields.
  Blocklist.de has no actual raw log lines; structured evidence is sufficient.
- Provider.tools: `Last seen` is the event; `Date` is generation time. Require
  valid first/last ordering. Missing/invalid event time requires manual review.
- Burina: maximum source-specific syslog time, using the numeric timezone note.
  Infer the year against message date in that offset, considering adjacent years.
  Proposed conservative bound: require a unique past candidate within 31 days;
  reject future/older/ambiguous records. The lead should accept this bound before
  implementation. Do not use current year, process timezone or delivery time
  as a substitute for an event timestamp.
- LRob: JSON `timestamp`; validate any retained first/last range. Decode MIME
  Base64 and evidence Base64 separately; retain only supported textual evidence.
- Cisilino: explicit UTC first/last; bilingual repetition describes one report.
- Custom Visuals: join the wrapped last record and use its full timestamp;
  prose last time must agree to the second. Parse first time with explicit
  `-05:00`. Do not infer a fixed offset merely from `America/Chicago`/`CDT`.

Retain fractions for attribution and rendered evidence. Verify persisted
precision during integration against the existing `detected_at` column; do not
introduce a schema migration for fractional timestamps.

## Ownership and privacy invariants

Use `find_ip_address_assignment(source, time: detected_at)` and existing incident
fields. Never substitute the present owner or infer ownership from email names.
The helper uses inclusive assignment intervals and highest-ID boundary ties.
A latest-event lookup alone does not prove ownership of historical evidence.

For dated logs, select the latest event's assignment and retain only records
within its interval that resolve to that assignment, including boundary checks.
Recompute displayed ranges/counts from retained records; omit original aggregate
claims. Diagnose omitted historical records for manual handling without creating
extra historical incidents. For aggregate reports, require the selected
assignment's continuous interval to cover first..last and consistent endpoint
lookups. Same user/VPS at both ends is insufficient across A/B/A reassignments.
Reject uncertain aggregate ownership. This includes Provider.tools, Cisilino
and Custom Visuals when retaining their reported totals/ranges.

Generate a summary plus validated evidence. Full originals remain in RT; never
forward historical activity across ownership boundaries. Describe reported
attempts/listings without asserting compromise or successful login. State when
raw logs are absent. Include provider, source, event time, relevant service/range
and available report ID. Final visible prose goes through the lead's writing
workflow. Do not fetch links or execute content from reports.

Keep subjects <=255 characters and text <=65,535 bytes, compatible with utf8mb3;
reuse XARF's 1 MiB JSON/decoded-evidence bounds. Reject oversize/unsupported data
before persistence. Diagnostics identify ticket/provider/field/reason without
bulk evidence. Preserve legacy processed semantics; malformed new profiles may
remain unprocessed. `processed?` never guarantees an incident or full coverage.
Dry runs must not save, notify or change mailbox contents.

## Compatibility, deployment and recovery

No migrations, persisted-format, API/client/CLI/Terraform, daemon protocol or
Nix module-option changes; no coordinated node update. Old code reads new
incidents. Mixed versions differ only in recognized formats. Keep legacy fixture
behavior, sender rules and duplicate-key subjects stable.

API configuration comes from `cluster/cz.vpsfree/vpsadmin/common/api.nix`;
inspected default rake tasks are enabled on `int.api1`. A future rollout verifies
the actual mail-task owner, builds/deploys its configuration and confirms reload.
Deployment and replay are not authorized by this investigation. Rollback restores
old parsing but does not remove incidents or retract notifications.

vpsAdmin fetches/deletes messages before handling them with `EXECUTE=yes`.
Unprocessed/rejected mail is not retained for automatic retry. Preserve RT
originals; inspect existing incidents before replaying only missing reports.
No cross-message deduplication is added. Persistence/notification failures can
be partial and require inspection before retry.

## Acceptance and verification

Quick implementation checks in the configuration Ruby 3.4 Nix shell:
`nix develop -c bundle exec rake spec` and targeted `bundle exec rubocop`.
Use synthetic RT/MIME fixtures without original IPs, hosts, private IDs, log
usernames or tokenized URLs. Preserve necessary provider-routing identity fields.

Acceptance must cover all nine handler routes and UTC times; one incident per
report/source; source rather than victim lookup; legacy regressions; sender
mismatch; duplicate/conflicting blocks; malformed structured data without fallback;
RFC/ISO offsets/fractions; both Base64 layers; quoted-printable; timezone-independent
results; maximum log time; December/January and leap-day handling; missing offsets;
empty/summary-only evidence; wrapped records; dry-run no-save and content limits.

Extend the assignment test stub with intervals: different owners, same user/new
assignment, A/B/A history, open end, exact boundaries and missing owner. Assert
historical evidence exclusion and aggregate rejection. The current IP-only stub
cannot establish these guarantees. Assert no unrelated source or log leaks.

After commits and quick checks, the lead runs mandatory independent review of
the complete branch/history with an explicit no-migrations conclusion. Only then
run longer checks through the required watcher: targeted API configuration build
and disposable real-database handler validation with notifications disabled,
including assignment intervals and stored timestamp precision. No node/VM/kernel
suite is justified for this parser-only change. Later original-message dry runs
must remain private and omit `EXECUTE=yes`; production creation is separate work.
