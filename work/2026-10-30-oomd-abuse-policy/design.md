# OOM daemon abuse policy — proposal

Status: proposal only, 2026-10-30. No application edits, commits or deployment.
Architect investigation for the lead; the user has selected the original thresholds.
See [log evidence](evidence.md) for the measurements and their limits.

## Recommended policy

Current user decision: "no, let's keep the original thresholds for now."
Use **5/7-day warning and 10/30-day stop**. The alternative 3/8 was declined
for now; VPS 28376 intentionally remains below the monthly stop limit in this sample.

| Rule | Proposed default | Semantics |
| --- | --- | --- |
| Action-required warning | 5 incidents in rolling 7 days | Send when a new incident makes the count meet/exceed the limit. |
| Policy stop and email | 10 incidents in rolling 30 days | Stop on a new incident while the count meets/exceeds the limit. |
| Further stops | At most once per rolling 24 hours | Allow manual restart; only another new incident can trigger another stop. |
| Recovery | Rolling 30-day count falls below 10 | Normal threshold rules resume automatically; retain history and cooldown. |

Count unique successful `osctl_oomd` stop/restart events collected by vpsAdmin,
using their original occurrence time (`detected_at`), not receipt time. Do not
count hit/miss samples, failed attempts, ordinary OOM reports, manual incident
reports or this policy's own stops. A successful restart followed shortly by
another successful restart is two incidents; transport duplicates are one.
Use UTC durations `(now - period, now]`: 7/30 days are not calendar weeks/months;
24 hours is not a midnight reset and is unaffected by daylight saving changes.

A warning may recur on a new incident while above its threshold, at most once
per 7 days. Falling below the threshold re-arms it without bypassing that
cooldown. A stop notification supersedes a warning due on the same incident.
The 24-hour stop cap includes the first policy stop. A pending/uncertain stop
prevents another action. Incidents during cooldown remain counted but do not
schedule a stop for later. UI wording must say when a **new incident** can next
cause a stop. Manual start, reboot and migration do not reset these counters.

Prefer this rolling-count recovery over a separate quiet-period restriction:
it has one visible threshold and no additional probation state. With no new
incidents the VPS necessarily recovers within 30 days. The tradeoff is that one
new incident can push 9 back to 10; this is predictable and still subject to
the cooldown. A quiet-period latch would need another reset/re-entry rule to
avoid immediately re-entering restriction from the same historical events.

No implicit per-VPS grace period is proposed: 10 incidents can cause a stop
even without a previously delivered weekly warning, including slow recurring
abuse or a burst. Make that explicit in policy communication. Roll out with
observation/warnings first, then enable enforcement deliberately; enabling a
setting or expiring a timer alone must never stop a VPS.

## Evidence and limits

At 2026-10-30 14:30 UTC, the trailing month contains 164 logged action attempts,
6 explicit failures, and 158 remaining candidate successes across 48 VPS.
The last 7 days contain 51 candidates across 21 VPS. These are log-derived
proxies, not an audited count of database incidents. A targeted sample confirms
7 of 8 candidates; removing the unconfirmed one changes 158 to 157. Under the
selected 5/10 limits, weekly warning candidates change from four to three;
the five monthly stop candidates are unchanged.

| VPS ID | Last 7 days | Last 30 days |
| --- | ---: | ---: |
| 27741 | 5 | 19 |
| 28655 | 5 | 14 |
| 4135 | 6 | 12 |
| 27837 | 3 | 11 |
| 29528 | 4 | 10 |
| 28376 | 5 (4 excluding unconfirmed) | 9 (8 excluding unconfirmed) |
| 29988 | 0 | 9 |

The initial table omitted VPS 28376, joint sixth by monthly count. Under 5/10
it does not meet the stop limit, and its warning depends on the unresolved
action. This limitation is now explicit and accepted by the user's decision to
retain the original thresholds. It does not establish API ingestion of every event.

The selected 10/month threshold covers 5/48 observed eventing VPS (10.4%);
5/week covers 4/21 (19.0%; 3/21 excluding the unresolved action). Seven of the
48 reached five in some observed rolling week. Twenty-six had only one monthly
candidate and another twelve had two or three. These shares do not describe the
whole fleet. Reconcile shadow decisions against deduplicated incidents before enforcement.

Historical alternative, declined for now: 3/8 covers 8/21 weekly (38.1%) and
7/48 monthly (14.6%), unchanged by excluding the unresolved action. It includes
VPS 28376 and VPS 29988, whose monthly count is nine but weekly count is zero.
No separate burst rule is proposed. Existing history alone never triggers a stop.

## Admin controls, API and both WebUIs

Store global defaults and nullable per-VPS overrides for the two count limits;
`null` means inherit, not zero. Show explicit and effective values separately,
with an admin-only reset-to-default action. Validate positive limits and keep
the monthly threshold at least the weekly threshold. Record actor/time/reason
for changes. A per-VPS enforcement exemption disables **vpsAdmin policy stops**
while retaining collection, counts, warnings and visibility. It does not disable
the host's protective OOM daemon. Recheck exemption before dispatching a stop.

Provide one server-calculated summary API for both UIs: 7/30-day counts, effective
limits, exemption, last incident/warning/policy stop, pending/failed action and
next-incident stop eligibility. Restrict reads to the VPS owner/admin and writes
to admins. Include a batch/list form so neither UI counts paginated incidents.
Show counts/limits and policy status on VPS detail; add a compact list indicator
and an admin overview/filter for approaching/exceeded limits and exemptions.
Link the incident history. Show pending, completed and failed stops distinctly.

## Implementation shape and invariants

Keep policy in vpsAdmin; the existing node event protocol is sufficient for v1.
Add source identity/provenance to collected OOM incidents and a database unique
key over existing `(node, VPS, type, occurrence-second, action)` fields. Do not
deduplicate by text or merge nearby distinct events. Integer-second collisions
are a documented protocol limitation; the observed minimum interval was 19.4s.
Use a VPS-scoped database lock and a durable policy action record, linked to
existing transaction chains, so ingestion/retries/concurrent workers cannot
create duplicate decisions. Count events by occurrence time; do not replay old
incidents into multiple daily stops. A delayed event predating the previous
policy stop cannot trigger a further stop. Historical backfill is display-only.

Reuse `TransactionChains::Vps::Stop` for VPS locking, node dispatch and disabling
autostart. A failed or uncertain chain retains its action identity for retry or
operator reconciliation; it must not look like a successful stop. A completed
stop starts the cooldown. Send the stop email after confirmed success, with
email retry independent of stopping: mail failure must not restart the VPS or
repeat its stop. Reuse existing mail transactions and stable message identity;
SMTP delivery cannot honestly promise exactly once. Retry pending decisions
after resource contention, rechecking applicability, ownership and exemption.

Future implementation must settle two bounded edge contracts before coding:
how stale a newly received event may be before it becomes visibility-only, and
whether ownership transfer resets enforcement history for the new owner. Keep
the audit history either way; never send old-owner data to the new owner.

## Future packages, compatibility and checks

1. **vpsAdmin backend**: supervisor OOM ingestion; incident provenance/index;
   policy state/action persistence; evaluator/task; summary/admin API; stop/mail
   chains and built-in fallback templates. Own the API contract and shared tests.
2. **Legacy UI in vpsAdmin**: VPS detail/list, incidents overview, admin override
   forms and gettext catalogs. Depends on the backend summary/settings contract.
3. **vpsadmin-webui**: API adapters, VPS detail/list/incident views and cs/en
   catalogs. Independent of legacy UI once the API is fixed; repository PR rules
   apply. Cover existing requirement REQ-051 and document the new policy view.
4. **vpsfree-notification-templates**: warning and stopped templates, cs/en
   subjects/text (HTML if used), reusing one stopped template for initial/repeat
   stops. Include counts, limits, recent incidents, required action, restart and
   recovery rules, links and support. Depends on the backend variable contract.

Email content requirements from the user: gently explain that this resource
pressure affects other VPS on the same node and may disrupt their services.
Offer both corrective paths: the VPS may need more memory, or service configuration
may need adjustment; too many worker processes, such as web-server workers, are
a common example. Link the verified resource-expansion sections:
[Czech](https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek)
and [English](https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of).
Lead owns final email wording under the writing skill; this is a content brief.

The user's template repository name is correct: both local bare clone names
resolve to `git@github.com:vpsfreecz/vpsfree-notification-templates.git` at
`2cfd218`; the project-map mail name is an older alias. Templates are declarative
build inputs under `templates/`, not uploaded using the historical mail tool.

Use additive nullable schema/API changes; old nodes and clients continue working.
Deploy migrations/backend/templates with enforcement disabled, then compatible
UIs, verify shadow counts/mail paths, and enable only after policy acceptance.
No coordinated update of all vpsAdminOS nodes is required. Rollback disables
policy dispatch and reconciles pending chains before reverting backend code;
retain additive tables/history. Disabling the feature does not undo actual stops.
Configuration pin/deployment work is later scope, not authorized by this proposal.

Quick checks: boundary/dedup/concurrency specs; 4→5 and 9→10; warning recurrence;
new incidents before/after 24h; count expiry; manual restart/migration; exemption
and ownership permissions; delayed events; resource-lock/stop/mail failures;
template rendering; legacy PHP lint and React type/unit checks. Longer checks:
isolated services/node integration with real stop/start and daemon event delivery,
retry/recovery behavior, and member/admin browser flows in both languages/UIs.
Run repository-required hooks, independent final review after implementation,
then longer integration checks. Apply the external KB impact workflow for visible
UI changes. This proposal/investigation does not itself trigger final review.

## Source pointers

Inspected local remote-tracking snapshots without fetch or worktree mutation:
vpsAdmin `ac10a62f1`, vpsAdminOS staging `a5ad64f81`, new WebUI `40653dff`,
configuration `fcc7fc97`, templates `2cfd218`; these are not deployment proof.

- vpsAdminOS `osctl-oomd/lib/osctl/oomd/killer.rb`: hit decay, restart/stop resets,
  action logged before execution, event broadcast only after successful action.
- vpsAdmin `libnodectld/lib/nodectld/ct_monitor.rb`: original timestamp forwarding;
  `api/lib/vpsadmin/supervisor/node/vps_events.rb`: current incident creation/mail,
  node/VPS check and lack of dedup; `api/models/incident_report.rb` and
  `api/lib/vpsadmin/api/resources/incident_report.rb`: existing model/authorization.
- vpsAdmin `api/models/transaction_chains/vps/stop.rb`,
  `api/models/transaction_chains/incident_report/{new,send,utils}.rb`,
  `api/models/transactions/mail/send.rb`, `docs/transactions.md`: reusable chains.
- Legacy `webui/pages/page_incidents.php`; new UI `src/lib/api/incidents.ts`,
  `src/pages/app/incidents/`, `src/pages/app/vps/`, `docs/design/REQUIREMENTS.md`.

Lead owns plan/state and user response. Session remains open:
<https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/>.
