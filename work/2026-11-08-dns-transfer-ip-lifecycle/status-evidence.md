# DNS transfer status and monitoring evidence

Owner: implementer1. Investigation only, 2026-11-08. No application edits,
commits, tests, production queries or mutations. Lead owns acceptance and the
session tracking records; architect0 owns the combined recommendations.

## Result and confidence

The recorded November 6 failures are real failed contacts with individual
primaries, not proof that the loaded zone was unusable. The application projects
the latest recognized attempt onto `DnsServerZone.last_transfer_*`. Independent
BIND statistics can keep reporting a loaded zone and the same serial without
changing that projection. The site monitor then treats a latest failure against
a still-configured user primary as an ongoing condition and repeats alerts.

A recognized later successful completion or up-to-date NOTIFY clears the latest
failure. The supplied November 8 completion from `37.205.11.85` is from peer ns4;
it can clear ns3's transfer state without proving that either user primary has
recovered. Equal serials alone establish neither current upstream reachability
nor a successful refresh after the failure.

The source explains a stale-classification mechanism, but does not establish
that silent successful SOA refresh occurred in this incident. LOGS found no
recognized recovery event between the failures and manual retransfer. Deployed
application/configuration revisions, incident-time primary associations, BIND
statistics samples and monitoring event history were not queried in this package.
In particular, the inspected monitor suppresses failures against removed user
primaries: persistent alerts cannot be attributed to a removed address without
evidence that the association remained or was restored, or different deployed
monitoring code.

## Source identity and method

Read-only canonical bare-ref inspection, using `git --git-dir=... show`, `grep`,
`ls-tree`, `log` and `diff`; no other session's worktree was accessed or fetch run.
These are locally available remote-tracking revisions, not freshly verified
remote heads and not evidence of deployed versions:

| Repository | Fixed source revision |
| --- | --- |
| vpsadmin | `e5e39bf380ebbb469d201f92d62434cd6ebca230` (`origin/master`) |
| vpsfree-cz-configuration | `5941cdb3dda259e91c6a988a7dbf08c84700b326` (`origin/master`) |

The bare local master refs differed (`b4ef8535a629ee8c9cd753afecdb05e0895d0eea`
and `86e19685313270d88e4db30038c056ce4b807abd`, respectively). References below
use the fixed revisions above. Repository AGENTS.md and applicable workspace
procedures were read. Session identity and both environment markers matched
`2026-11-08-dns-transfer-ip-lifecycle`; saved roster verified implementer1 and
assigned peers with their retained addresses and settings.

## BIND log → event → persisted projection

All paths in this section belong to vpsadmin at the fixed source revision.

| Decision | Source and lines | Consequence |
| --- | --- | --- |
| Recognize success | `libnodectld/lib/nodectld/dns_transfer_log.rb:145–172` | Nonempty completion, including same-serial completion, and `notify ... zone is up to date` become success. NOTIFY success has no serial. |
| Ignore intermediate success statuses | Same file `:175–184` | `Transfer status: success` and `up to date` produce no event. Other statuses become failures. |
| Recognize contact failures | Same file `:187–196` | Both `transfer ... failed ...` and `refresh: failure trying primary ...` independently become failed events for that address. No all-primary exhaustion test. |
| Exclude empty completion | Same file `:148–153`; `api/lib/vpsadmin/supervisor/node/dns_transfer_log.rb:95–102` | Zero messages/records/bytes/serial is not a recovery; node and API both filter it. |
| Limit ingestion to managed zones | Node parser `:80–98` | Checks zone presence in DnsConfig, not current primary membership or configuration generation. Publishes raw message, cursor, timestamp and key, then saves cursor. |
| Resume journal | Same file `:60–77,112–126` | Persistent cursor; without one, starts at `-n 0`, so old journal history is not backfilled automatically. |
| Persist event and latest result | API supervisor `:27–76` | Resolve zone by name and node, lock server-zone, insert event once by event key, then update latest projection. Strictly older timestamps do not replace latest; equal timestamps do. Success clears reason fields. |
| Preserve history | `api/models/dns_server_zone.rb:7–13`; `api/models/dns_server_zone_transfer_log.rb:1–7` | Last-result pointer and failure/success history are distinct records. Success does not erase old failures. |

Duplicate delivery of the same journal entry is suppressed by SHA256(cursor)
(`libnodectld/.../dns_transfer_log.rb:265–279`), lookup by event key (API
supervisor `:54–59`) and the unique database index
(`api/db/migrate/20260509120000_add_dns_server_zone_transfer_logs.rb:27`). Two
different BIND messages for one attempt have different cursors and remain two
rows. LOGS correlated the duplicate IPv6 UI rows to the same BIND handle's
`failed to connect` and `Transfer status` messages, not duplicate raw input.
Journal microseconds are truncated to whole seconds (node parser `:129–133`),
so within a second arrival order determines the latest projection; this is not
established as the incident's stale-state cause.

Existing regression coverage, inspected but not run:

- `libnodectld/spec/nodectld/dns_transfer_log_spec.rb:66–122`: up-to-date NOTIFY,
  empty completion exclusion, ignored up-to-date statuses, and success for
  `0 messages, 1 records, ... serial 2026080601`.
- `api/spec/supervisor/node/dns_transfer_log_spec.rb:92–101,127–211`: delivery
  deduplication, later success/NOTIFY clears reason, empty completion does not.
- `tests/suite/dns/secondary-transfer-errors.nix:140–175`: injected NOTIFY and
  up-to-date-status-plus-completion recovery; this is not a reproduction of a
  silent real SOA refresh.

Commit `35a7a9bf64f7f6c010066a23043118ed86bb3a63` explicitly records that BIND
emits `Transfer status: up to date` before successful completion. Ignoring this
status fixed synthetic unknown failures; its cleanup migration
`20260812120000_remove_up_to_date_dns_transfer_failures.rb:16–26,51–82` removes
only that synthetic shape and repairs latest pointers. The incident's genuine
`connection_failed`/`host unreachable` events do not match that cleanup.
Commit `6761aa11bb111c8df7185d8446b8b71cc8bfffe0` added NOTIFY recovery for an
unchanged primary serial; that coverage already exists in inspected source.

## Independent zone statistics, configuration and UI

`libnodectld/lib/nodectld/dns_status.rb:36–69,73–88,104–108,117–128` fetches BIND
statistics XML, iterates `statistics/views/view/zones/zone`, reads serial, loaded,
expires and refresh, and parses timestamps. It does not run `rndc zonestatus`.
Defaults are `http://localhost:8053/xml/v3`, every 60 seconds
(`libnodectld/lib/nodectld/config.rb:270–280`). The API stores these fields and
`last_check_at` only (`api/lib/vpsadmin/supervisor/node/dns_status.rb:33–46`),
without changing transfer history or latest transfer state.

These fields have no origin address, explicit successful-contact flag or
previous-sample comparison in the inspected implementation. `last_check_at`
proves collection from local BIND, not contact with a primary. Same serial or
loaded-at does not establish recovery. No exact BIND timer implementation or
reproduction was inspected here, so a numeric predicate based on advancing
expires is **not established**. Advancing next-refresh must not be treated as
success merely because it moves; it may be scheduling/retry state. Even a
validated successful refresh could be from peer ns4 and would not prove a user
primary reachable.

External zones include peer vpsAdmin DNS servers as effective transfer sources
(`api/models/dns_server_zone.rb:45–60`), and render them as BIND primaries
(`libnodectld/lib/nodectld/dns_config.rb:139–147`). At configuration revision
above, `cluster/cz.vpsfree/containers/ns4/module.nix:18` assigns `37.205.11.85`;
ns3 has `37.205.15.45` (`ns3/module.nix:18`). Both hosts import common DNS
configuration (`ns3/config.nix:8–18`, corresponding ns4 file); common
`dns.nix:49–64` enables statistics and includes runtime-generated named.conf.

Primary add/remove persists zone sources and regenerates config
(`libnodectld/lib/nodectld/utils/dns.rb:25–66`); API transfer create/destroy
chains append global DNS reload (`api/models/transaction_chains/dns_zone_transfer/`
`create.rb:20–43`, `destroy.rb:18–41`). Reload executes `rndc reload` or a
zone-specific reload (`libnodectld/lib/nodectld/commands/dns_server/reload.rb:6–11`).
None resets transfer projection, records positive synchronization or forces
retransfer. Old queued events have no source-set generation check. Thus primary
replacement/reload alone cannot be assumed to clear an old failed attempt.

The API exposes stats and `last_transfer_*` directly
(`api/lib/vpsadmin/api/resources/dns_server_zone.rb:12–26`), masking transfer
details from non-admin users for internal zones only (`:59–64`). WebUI separates
“Zone state” from “Last transfer” (`webui/forms/dns.forms.php:268–272`), renders
stats (`:1708–1716`) and latest attempt (`:1731–1750`). Name-server summary rows
have no failure color (`:293`); only historic log rows are colored (`:476`). The
existing external-zone warning tests zero transfer records, not specifically
zero existing user primary records (`:232–235`). UI changes alone do not resolve
authoritative stale classification or monitoring.

## Monitoring trigger, persistence, close and email

At configuration revision above,
`configs/vpsadmin/api/monitoring.rb:547–593` defines
`dns_secondary_transfer_failure`:

- Query secondary server-zones of enabled external zones belonging to active
  users. Value is only `last_transfer_status.to_s`.
- Check fails exactly when that value is `failed`, last primary address is
  nonempty, and an existing user primary (`confirm_create` or `confirmed`)
  matches the failed address. It never inspects serial, loaded, expires,
  refresh, last check, reason code or age of last transfer.
- Removed primary, peer-only failed address, addressless failure, nil latest
  status and success pass. Zero user primaries also pass. No independent
  zero-user-primary monitor was found in this configuration.
- Failure period is 30 minutes, repeat interval 24 hours, cooldown one hour.
  Period is measured from monitor event creation, not from `last_transfer_at`.

Framework at vpsadmin revision:

| Behavior | Source |
| --- | --- |
| Evaluate and report one object | `plugins/monitoring/api/lib/vpsadmin/api/plugins/monitoring/monitor.rb:24–49` |
| Persistent identity | `plugins/monitoring/api/models/monitored_event.rb:12–24`: monitor name, object class and row id; here one event per DnsServerZone, not per raw log, address or zone. |
| Store observations | Same file `:65–69`; `monitored_event_log.rb:1–4`. |
| Confirm/repeat | `monitored_event.rb:85–111`: elapsed period confirms; confirmed event repeats after repeat interval; timestamps persist across task runs. |
| Clear | `:71–82`: passed while monitoring → unconfirmed, no action; passed after confirmation/ack → closed and action. Fully ignored events skip before this at `:59–63`. |
| Cooldown/ack | `:29–38,54–63,100–104`: one-hour cooldown after a closed event; acknowledge/ignore handling follows retained flags. |
| Notification | `:117`; `plugins/monitoring/api/models/transaction_chains/monitoring/alert.rb:6–9`: action invoked, alert count incremented for nonempty chain. |

`action :alert_user` maps all states in the DSL
(`plugins/monitoring/api/lib/vpsadmin/api/plugins/monitoring.rb:49–63`). Site
`monitoring.rb:70–98` sends the state-specific template, persistent event id and
incrementing alert id in Message-ID; closed mail replies to the prior confirmed
mail. Consequently two raw IPv6 failure rows do not themselves produce two
independent monitor events, although ns3 and ns4 have separate event identities.
One old failed projection can keep the same event confirmed and cause daily
repeat emails without any new failed BIND attempt.

Declared default task schedule is every ten minutes plus up to 60 seconds
randomized delay (`nixos/modules/vpsadmin/api/rake-tasks.nix:183–192`); actual
production timing/overrides were not inspected. A recognized peer success passes
at the next evaluation and can close the alert. Matching local serial by itself
never does. A removed primary also passes without a new success. Objects removed
from query scope are not reported passed; generic inactive-event closure is one
month later (`plugins/monitoring/api/tasks/monitoring.rake:8–16`).

## Minimal options and bounded checks

These are suggestions for architect/lead selection, not implemented changes.

1. Preserve historical attempt records and the meaning of `last_transfer_*`.
   Reconcile current synchronization classification with an observed successful
   freshness check after the failure, separately from intended-source
   reachability/configuration. A peer success can prove synchronization through
   that peer; it cannot certify the user primary. Avoid merely changing email
   text or hiding an old failure after an arbitrary timeout.
2. For an explicit status-only `Transfer status: up to date` outcome, emitting
   success is a small parser candidate, with outcome duplication considered.
   It is a valid no-change outcome in source history, but existing coverage
   expects a following recognized completion. This candidate does **not** solve
   a genuinely silent successful SOA refresh and is not proven relevant here.
3. For silent SOA refresh, first capture/reproduce one failure → same-serial
   recovery against the pinned BIND version using real logs and XML samples.
   Establish whether an existing positive signal can be consumed in the current
   status/event path. If expiry advancement is proven reliable, distinguish
   reload/reset effects and lack of origin attribution before using it. No
   safe numeric expires/refresh reconciliation rule can be selected from the
   evidence in this packet alone. This is the concrete remaining dependency,
   not a justification for a new monitoring subsystem.
4. Independently alert enabled external zones with zero existing **user**
   primaries (`dns_zone_transfers.primary_type`, same confirmed-state boundary).
   Effective BIND primary lists include peers and are the wrong predicate.
   Prefer one existing framework monitor identity per DnsZone to avoid duplicate
   missing-config mail per secondary; close when a valid user primary returns.
   Preserve detached-but-owned user primary records per the IP package proposal.

Small candidate regression boundaries for later authorized implementation:

- Existing node parser/supervisor specs: preserve real failures, recognized
  NOTIFY/completion recovery, empty-summary exclusion and delivery idempotence;
  status-only up-to-date if selected; several messages from one attempt.
- Existing `dns_status_spec.rb` and DNS transfer scenario: same-serial failure
  then true SOA recovery, retry-only timer movement, reload without contact,
  old/reordered samples, peer recovery vs user-primary recovery. Assert actual
  BIND observations before selecting a timer predicate.
- Site monitoring condition fixture (none currently exists under config specs):
  old failure plus verified later recovery, old failure without recovery,
  removed/readded failed primary, peer-only success/failure, no user primaries
  with fresh loaded peer-fed zone, pending-destroy primary excluded, restored
  valid primary, and disabled/internal zones excluded.
- Existing `api/spec/models/plugins/monitoring/monitored_event_spec.rb`: use
  established framework behavior to verify one event, 30-minute confirmation,
  24-hour repeat and passing close; avoid inventing notification deduplication.

No application tests were run: this package changes only investigation evidence.
No schemas, clients, feature heads, migration lineage or deployed state changed.
Future API behavior work retains the repository's generated-client assessment
requirements. The open evidence gaps belong in the combined diagnosis; do not
present equal serials, timer semantics or deployed revision parity as verified.
