# Abuse email parsing: approved design and verification brief

## Scope and status

The user authorized implementation of this simpler contract on 2026-10-02:
"Implement the plan." It covers all nine supplied reports. The restrictive
implementation at `7cce4271be0bcd81a42c6784e12dff326e5d041f` is superseded;
its per-record filtering and ownership-range rules are not a supported path.
This document describes the approved replacement, not completed verification.

Keep changes within `vpsfree-cz-configuration` and its existing
`parse -> Array<IncidentReport>` interface. For each valid incoming report,
extract one reported source IP and one event instant, look up its historical
assignment once, and preserve the original subject and decoded readable content.
The three Burina reports remain separate despite overlapping evidence.

The architect owns this brief, implementers own application changes, and the
lead owns plan/state/portal records and acceptance. Original messages and bulk
identifying evidence remain outside version control; fixtures are synthetic.
No cross-message deduplication, historical replay or new provider framework.

## Required metadata and timestamps

Keep the existing narrow provider routes, originator checks and diagnostic
`CHECK_SENDER` behavior. Source comes from a recognized subject or authoritative
structured field, never from individual SSH records or an arbitrary IP scan.

| Ticket | Profile and authoritative source | Event time | Expected UTC `detected_at` |
| --- | --- | --- | --- |
| #95347 | Blocklist.de; structured `Source`, agreeing with subject | Complete structured `Date` | `2026-09-28T08:41:50Z` |
| #95348 | Provider.tools; inline `Source`, consistent with subject/summary IP | Summary `Last seen` | `2026-09-28T08:44:40.114Z` |
| #95350 | Burina; `Abuse from <IP>` subject | Maximum syslog timestamp prefix | `2026-09-28T09:23:02Z` |
| #95351 | LRob/Shieldlist; JSON `source_identifier`, agreeing with subject | JSON `timestamp` | `2026-09-28T09:29:00Z` |
| #95353 | CEDO; structured `Source`, agreeing with subject | Complete structured `Date` | `2026-09-28T09:36:08Z` |
| #95355 | Burina; recognized subject | Maximum syslog timestamp prefix | `2026-09-28T10:32:52Z` |
| #95356 | Cisilino; the two recognized subject IP slots must agree | One explicit UTC `Last seen` | `2026-09-28T10:38:19Z` |
| #95360 | Burina; recognized subject | Maximum syslog timestamp prefix | `2026-09-28T11:46:46Z` |
| #95361 | Custom Visuals; recognized subject | Precise numeric-offset prefix in designated last-log section | `2026-09-28T11:57:11.439254Z` |

Blocklist.de/CEDO retain one direct `text/plain` structured report attachment,
XARF 0.2/category/type/source-type admission and reporter identity checks.
Required source/date keys are unique. Their structured date is authoritative;
subject dates, prose and logfile times need no corroboration. Service, port,
report ID and log contents are forwarded without interpretation.

Provider.tools retains one marked inline XARF block and summary with its
source-type/category/type admission. `Last seen` is required; generation `Date`,
`First seen`, state and services are preserved without parsing or ordering.
They do not determine attribution or require generated labels.

LRob retains one direct `application/json` attachment, current XARF 4.2.0
`connection/login_attack` admission, sender/reporter identity and the existing
`XArfDecoder` required shape, UUID, source and timestamp validation. No feedback
MIME part is required. Decode textual evidence without parsing its records.
Ignore optional range extensions for extraction; do not validate prose dates.

Cisilino needs no English/Italian source sentence, translation agreement,
first-seen field, counts, services or sample grammar. Custom Visuals needs only
its subject source and one complete timestamp prefix in the unique designated
last-log section. No username, log-source, prose count, first/last prose time,
AM/PM conversion or prose timezone corroboration is needed.

### Timestamp behavior

Retain strict calendar and numeric-offset RFC/ISO parsing, including fractions.
Burina reads line-leading syslog date/time prefixes in the report's log section
and takes their maximum; the remainder of each record is opaque. A numeric
local-timezone note and message Date are required for year inference. Consider
adjacent years and require exactly one nonfuture candidate within 31 days of
message Date for each parsed prefix. Reject invalid or out-of-window timestamps;
never substitute the current year, process timezone or receipt time as an event.

Custom Visuals reads the precise date/time/offset prefix without joining or
rewriting the record's content. Keep fractional instants for attribution and
persistence. No selected timestamp may fall back to another field when invalid.
Unknown SSH wording or an address mentioned in a log cannot change the source.
A later prefix inside the reported log section can determine Burina's event time
regardless of that record's opaque message text; this is intentional.

## Content preservation, attribution and failures

Set the incident subject to the original subject after removing the RT prefix.
Preserve the decoded human-readable body after RT-wrapper removal, eligible
direct text/plain attachments and complete log text. LRob additionally appends
all supported decoded `text/plain` JSON evidence payloads, in order. Do not emit
the raw JSON envelope or Base64 data. Empty optional logs/evidence remain valid.

Reuse existing text-section helpers and `append_text_sections`; decode MIME
encodings and retain existing line-ending/outer-whitespace normalization and
exact duplicate-section avoidance. Preserve wording and internal wrapping.
Do not traverse nested/forwarded messages or emit HTML/binary attachments.
Incidental unsupported MIME parts are ignored; malformed required parts and
unsupported JSON evidence types remain rejected. No link fetching or YAML use.

Validate a single host IP with existing helpers, excluding prefixes/hostnames.
After required metadata validation, call
`find_ip_address_assignment(source, time: detected_at)` exactly once. Use the
returned assignment/user/VPS and existing incident fields. Missing ownership
means no incident; there is no fallback to the current owner. Preserve existing
inclusive interval and highest-ID boundary semantics through the API helper.

Forward full readable report content to that selected event owner. Content may
include earlier-owner activity, repeated records and other IP mentions. This is
the approved behavior: no range coverage, endpoint ownership, A/B/A, per-record
source/ownership checks, filtering, generated counts or reconstructed summaries.
A single lookup establishes event-time attribution, not ownership of every
statement or historical record in the forwarded report.

Keep required MIME/section uniqueness, provider identity, host-IP and selected
source/time validation proportional. Missing/duplicate/invalid required metadata
or conflicting required source claims fail closed with a useful diagnostic;
no alternate IP guesses or malformed-structured-report prose fallback. Unused
prose and optional range/count/sample fields are not validation inputs.
Ignored optional text fields may repeat, and optional JSON range values remain
uninterpreted, but existing rejection of duplicate JSON keys applies throughout
the document without custom exceptions for unused extensions.
`CHECK_SENDER` disables only identity checks. Keep legacy Fail2Ban handled
semantics; malformed new provider profiles remain unprocessed.

Retain 1 MiB report/JSON/decoded-evidence bounds, nonempty readable content,
subject <=255 characters, text <=65,535 bytes and utf8mb3 compatibility. Reject
unrepresentable or oversized original content rather than truncate or regenerate
it. Diagnostics identify provider/ticket/reason without bulk evidence. Dry runs
must not save incidents, send notifications or alter mailbox contents.

## Files and removal boundaries

Under `configs/vpsadmin/api/`, retain `incident_reports.rb` routing and the
existing provider classes. Simplify `x_arf.rb`, `fail2ban.rb`, `lrob.rb`,
`cisilino.rb`, `custom_visuals.rb` and `utils.rb`; leave the decoder unchanged.
Preserve original Fail2Ban/Apache, legacy XARF and all other legacy provider
behavior, including Abusix/Netcraft admission and duplicate-key subjects.

Remove `Event`, `assignment_contains?`, `notice_range_assignment`,
`notice_owned_events`, `notice_log_source`, `notice_iso_log_events`,
`notice_summary` and `notice_event_evidence`. Reduce `notice_syslog_events` to
a local Fail2Ban timestamp helper. Remove Custom Visuals `local_prose_time` and
provider range/count/translation/sample interpretation. Simplify
`notice_incident` to use the original stripped subject and supplied text.
Reuse needed metadata, bounds, date, MIME, warning and single-assignment helpers.
No abstraction replaces the removed machinery.

Update `spec/configs/vpsadmin/api/extended_abuse_notices_spec.rb`, synthetic
fixtures where needed, and `configs/vpsadmin/api/README.md`. Retain the small
interval-aware assignment stub in `spec/spec_helper.rb` for event-time tests.

## Verification and branch history

Quick checks: full `nix develop -c bundle exec rake spec`, targeted RuboCop and
mandatory repository hooks. Test all nine formats for one candidate, exact UTC
instant, original stripped subject, preserved body/text attachments/JSON textual
evidence, exactly one lookup for reported source/time, and dry-run no-save.
Retain required-metadata/MIME/JSON/Base64/storage errors and legacy regressions.

Replace evidence-exclusion, regenerated-count and range/A/B/A rejection tests
with explicit preservation and event-owner assertions. Unknown SSH message text,
username-like IPs, old records and other-IP mentions remain in output without
changing the source. Remove rejection tests for unused ranges, counts, services,
translations, samples and Custom Visuals prose offsets. Cover reversed log order,
maximum prefixes, numeric offsets, process-TZ independence, year rollover,
leap dates, the 31-day bound, fractions, missing owner, historical versus current
owner, inclusive highest-ID boundaries and oversized original subjects.

Before final review, fetch/recheck upstream and provenance. The current single
pushed feature commit is unmerged and undeployed per session records. Consolidate
its replacement into one coherent feature commit with no obsolete restrictive
approach retained in the branch history. Do not rewrite master. Provide the
retained independent reviewer the entire final base-to-head series/diff and
explicit no-migrations inventory. Review general, architecture/repetition,
scope/proportionality and risk/compatibility lanes, including the user's accepted
full-content behavior. Previous verification/review does not validate this change.

After review, use the required watcher for longer verification. Adapt the existing
isolated pinned-schema MariaDB harness to all nine private originals, dry-run
and save/reload, exact subject/text, one lookup and fractional DATETIME roundtrips.
Cross-range/A/B/A cases now succeed when the selected event has an owner and
preserve full content. Keep real historical/boundary lookup checks, disable
notifications/mailbox access and keep originals outside Git. Rebuild only the
affected API configuration at the final head; no node/kernel suite is needed.

Capture the final comparison and push the rewritten feature with an explicit
force-with-lease after checking the expected remote head. Handle applicable CI
and only superseded feature runs. Retain the branch/session. Integration,
deployment and production incident creation remain separate authorizations.

## Compatibility, deployment and recovery

No API/schema/pin, persistent-format, client/CLI/Terraform, daemon protocol or
Nix option changes; no node coordination. Old versions can read new incidents.
Mixed parser versions can differ in recognition/rendering but retain the same
incident-array contract. An authorized rollout must verify the actual API mail
worker/configuration revision and reload; recorded offline checks do not prove
production state.

With `EXECUTE=yes`, vpsAdmin fetches/deletes mail before parsing; rejected or
unprocessed messages are not automatically retained for retry. Originals remain
in RT. Inspect existing incidents and partial notification/persistence success
before replaying missing reports. Rolling back restores old parser behavior but
cannot remove existing incidents, retract notifications or restore deleted mail.
