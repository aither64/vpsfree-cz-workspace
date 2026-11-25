> Historical contract, superseded by [shared incident escalation contract](implementation-contract.md). Retained as evidence only; do not implement these old names.

# Released OOM abuse implementation contract

2026-10-30. Implementation authorized; no merge/deployment authorization.
Applies to backend implementer0, legacy implementer1, React implementer2 and
template implementer3. Read [design](design.md) and repository instructions.
Prepared bases confirmed by lead: vpsAdmin `ac10a62f1`, React WebUI `40653dff`,
notification templates `2cfd218`. Report material deviations through lead.

## API and settings (fixed consumer contract)

Extend existing HaveAPI VPS `Index`/`Show`, `Update` and their existing HTTP
routes (`GET /vpses`, `GET /vpses/:id`, `PUT /vpses/:id`). No new endpoint or
generated-client prerequisite. Return fields below on both Index and Show;
Update accepts only the three settings fields marked writable. Native HaveAPI
request envelopes, pagination, owner authorization and resource IDs remain.

| Field | Type | Meaning |
| --- | --- | --- |
| `oom_incidents_7d` | integer | Unique qualified incidents in rolling 7 days/current ownership epoch. |
| `oom_incidents_30d` | integer | Same for rolling 30 days. |
| `oom_warning_limit` | integer | Effective warning threshold, default 5. |
| `oom_stop_limit` | integer | Effective stop threshold, default 10. |
| `oom_warning_limit_override` | nullable integer | Admin writable/readable; null inherits global default. |
| `oom_stop_limit_override` | nullable integer | Admin writable/readable; null inherits global default. |
| `oom_enforcement_enabled` | boolean | Per-VPS stop permission, default true; admin writable, owner readable. False is exemption. |
| `oom_mode` | string | `observe`, `notify`, `enforce`, effective global mode. |
| `oom_stop_enforced` | boolean | Mode=enforce AND per-VPS permission. Does not mean stop currently due. |
| `oom_status` | string | `clear`, `near_limit`, `warning`, `stop_threshold`; derived solely from counts/effective thresholds. |
| `oom_last_incident_at` | nullable datetime | Latest qualified occurrence in ownership epoch. |
| `oom_last_warning_at` | nullable datetime | Last durably queued warning in epoch; not SMTP delivery proof. |
| `oom_last_stop_at` | nullable datetime | Latest confirmed successful stop attributable to this feature. Preserved across ownership transfer. |
| `oom_next_stop_allowed_at` | nullable datetime | Last stop +24h; cooldown boundary only, never scheduled stop. Null before any stop. |
| `oom_action_state` | string | `none`, `pending`, `failed`, `uncertain`; outstanding stop action only. |
| `oom_action_chain_id` | nullable integer | Existing transaction chain ID for that outstanding stop; preserve normal chain authorization. |
| `oom_accounting_since` | nullable datetime | Ownership reset boundary; null means no ownership reset since feature activation. |

Status precedence: stop_threshold if count30>=stop limit; else warning if
count7>=warning limit; else near_limit if count7>=ceil(0.8*warning limit) OR
count30>=ceil(0.8*stop limit); otherwise clear. Exemption/mode/action state are
separate fields so counts remain visible. Index adds optional `oom_status`
(same enum) and `oom_enforcement_enabled` filters; apply existing owner scope
before filtering/counting/pagination. The existing admin VPS list with these
filters is the overview. Compute one consistent `now` per request and batch
counts/state for the returned VPSes; do not count paginated incidents in UIs.

Both raw overrides are admin-only output; owner output includes all remaining
summary fields. Support follows existing VPS authorization, with no new write
privilege. Reject non-admin writes server-side. Sending null explicitly resets
an override; omitted fields remain unchanged. Integers must be >0 and effective
stop>=warning; validate the final pair atomically. Record setting changes in the
existing VPS/object audit mechanism; no new free-text reason UI is required.

SysConfig category `oom_policy`: `mode` String default `observe`,
`warning_limit` Integer default 5, `stop_limit` Integer default 10; admin-only
settings through existing SystemConfig API/UI. Validate mode/positive values
and resulting effective threshold pairs including inherited/overridden values.
Invalid stored configuration must disable dispatch and surface a diagnostic,
not silently stop using fallback limits. Keep periods 7d/30d/24h fixed in v1.
Observe records counts only; notify sends threshold warnings without stops;
enforce sends warnings/stops, respecting exemption. Normal existing individual
incident reports remain; new threshold notifications are additive. Setting or
mode changes alone never dispatch; wait for a new qualifying incident.

Frontend compatibility: detect availability from the returned summary fields
(in particular `oom_incidents_7d`), not a version string. Missing fields mean
feature unavailable, not zero incidents. Hide new controls/indicators on older
API; keep normal VPS views working. Both UIs show limits/counts/status, cooldown
meaning, exemptions and errors. React package updates REQ-051/work log and
adapter inventory; both UI packages assess external KB impact without publishing.

## Mail contract (fixed names and variables)

Register `vps_oom_warning` and `vps_oom_stopped` in backend MailTemplate registry;
provide built-in English fallback templates. Site repository owns corresponding
`templates/<name>/meta.rb` and `email/{cs,en}.{subject,text}.erb`. No HTML needed.

Both templates receive these exact instance variables:

| Variable | Type / contract |
| --- | --- |
| `user` | User object; `login` available. |
| `vps` | VPS object; `id`, `hostname` available. |
| `base_url` | String, configured legacy WebUI base URL, matching existing templates. |
| `incident_count_7d`, `incident_count_30d` | Integers snapshotted at decision. |
| `warning_limit`, `stop_limit` | Current effective integer thresholds when rendering/queuing the mail; consequence text uses these, not stale decision values. |
| `warning_period_days`, `stop_period_days` | Integers 7 and 30. |
| `repeat_stop_hours` | Integer 24. |
| `incident_at` | Time of the incident which triggered this decision. |
| `stop_enforced` | Boolean, current actual mode/per-VPS enforcement permission when rendering/queuing the mail; re-evaluate on a render/retry, never copy a stale decision snapshot. |

Stopped template additionally receives `stopped_at` (Time, actual successful
stop transaction finish) and `repeated_stop` (Boolean, whether a previous stop
exists in the current accounting epoch). A stopped email is emitted only after
confirmed success. Warning consequence uses `stop_enforced`: only true may say
"it will be stopped". False still requests corrective action but makes no stop
promise. No `policy` wording in member email. Lead supplies final bilingual copy
and any edits to stock repeated/single-incident wording; implementers wire it.
Incident counts remain the decision snapshot; identify their period/event context
where needed rather than presenting them as a fresh count. Before each mail
render/queue attempt re-read mode, exemption and effective limits so the future
consequence is current. SMTP acceptance cannot retract already transmitted text;
do not promise post-send synchronization or duplicate mail on every setting edit.

Site templates use these literal language-specific links, not API variables:
CS `https://kb.vpsfree.cz/informace/platby#z_ceho_se_sklada_clensky_poplatek`;
EN `https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of`.
OOM help: CS `https://kb.vpsfree.cz/navody/vps/incidenty#oomd`;
EN `https://kb.vpsfree.org/manuals/vps/incidents#oomd`.
Retain existing template footer/greeting/subject-prefix conventions. More memory
and configuration/worker limits are alternatives; explain other VPS on the same
node can suffer service disruption. Do not claim every case is solved by RAM.

## Backend invariants and resolved edges

Use existing IncidentReport, VPS/SysConfig, scheduler and transaction chains;
one small persisted action model is sufficient. No general workflow framework,
new queue transport or vpsAdminOS update. Dedup unique source key before incident
creation and any existing/new incident mail chain; source key comprises node,
VPS, type, original occurrence integer-second and action. Only daemon-sourced
successful stop/restart events qualify; arbitrary admin `codename=oomd` does not.
Do not retroactively arm actions from legacy rows lacking source identity.

Windows use occurrence time, evaluated against current UTC now. New event older
than 24h at receipt is persisted/countable but cannot initiate a warning/stop.
The durable decision records trigger time and owner/epoch; retry dispatch only
while that trigger is <=24h old, still eligible, and settings/mode permit it.
Expired unsent decisions become suppressed, not future scheduled stops. Events
with future occurrence timestamps are audit-only and do not trigger/count until
their time is valid; do not rewrite source time or automatically replay them.

At successful ownership transfer, reset the accounting epoch and warning state;
retain source incidents/audit and last completed stop cooldown. Prior-owner
undispatched actions become ineligible. Use existing chown-chain confirmations
and successful chain/transaction timestamps, not model callbacks (confirmations
bypass callbacks). A transfer rollback must preserve prior epoch/state. Keep
the transfer chain identity if completion must be reconciled by the scheduler;
while completion is uncertain, do not dispatch. Events occurring before the
new epoch cannot be attributed to the new owner for counts or notifications.
Do not expose old-owner incident details via a summary/history link. Admin-only
transfer already serializes on VPS; migration/reboot/manual start do not reset.

Serialize decisions per VPS, persist action identity and chain linkage together.
A pending/uncertain stop prevents another. Existing successful stop transaction
`finished_at`, after successful completion of its chain, starts the 24h cooldown;
chain `updated_at` or mail-chain completion is not stop/delivery proof. Failures
retain identity for retries/reconciliation. Never automatically retry an uncertain
physical stop; resolve its effect before further dispatch. A new incident must
occur after the last completed stop and after cooldown expiry to cause another;
events during cooldown are counted only and never schedule a later stop.

Reuse Vps::Stop with `rollback_stop: false`; a later mail failure must not restart
the VPS. Stop and notification have independent durable progress so retrying mail
cannot repeat stop. Mail transaction is keep_going: inspect its actual result,
not merely chain done, and reuse stable message identity. Existing mail delivery
semantics apply; no exactly-once SMTP claim. ResourceLocked defers the same
decision. Recheck exemption under VPS serialization before stop-chain dispatch;
an exemption edit cannot silently promise cancellation of already executing work.

## File ownership and acceptance

- **implementer0** owns vpsAdmin repository Git; `api/` backend, migrations/core
  schema, locales, fallback templates, `nixos/modules/vpsadmin/api/rake-tasks.nix`
  if scheduling registration needs it, backend specs/integration tests,
  `docs/oom-abuse-policy.md` + index, and CI selection/topic wiring. Main edits:
  `api/lib/vpsadmin/supervisor/node/vps_events.rb`, `api/models/{vps,incident_report,sys_config,mail_template}.rb`,
  `api/lib/vpsadmin/api/resources/vps.rb`, existing incident-report task,
  `api/models/transaction_chains/vps/update.rb` for chown and new dedicated
  evaluator/action/chain files following local conventions. Avoid general node
  transport changes. Report exact additional paths before touching shared areas.
- **implementer1** owns only legacy `webui/` (especially `lib/vps.lib.php`,
  `pages/page_adminvps.php`, `forms/vps.forms.php`, incident links, gettext
  catalogs) plus a disjoint legacy browser test scenario agreed with backend.
  No `api/` edits or Git mutation concurrent with backend. Backend owns shared
  test registry/CI changes and all vpsAdmin commits unless lead sequences otherwise.
- **implementer2** owns separate `vpsadmin-webui`: VPS type/API adapters,
  detail/list/configuration/incident links, cs/en catalogs, scoped unit/browser
  tests, design/work-log/inventory. Reuse existing list/overview; no new BFF API.
- **implementer3** owns separate `vpsfree-notification-templates`, the two named
  directories and synthetic rendering/check fixtures if appropriate. Backend
  owns registry/fallback paths, preventing cross-package file overlap. Lead owns
  final human-facing email copy; use the vars above without renaming them.

Quick acceptance: 4→5 warning, 9→10 stop, recurrence after7d, expiry/recovery;
duplicate ingestion and concurrent threshold events yield one decision/chain;
old/future/delayed events, new incident after24h versus cooldown-time event;
owner change and rollback, exemption/mode switch, ResourceLocked, failed/uncertain
stop, mail failure after successful stop; owner/admin permission and explicit-null
reset, invalid defaults/override pairs; batch/list count parity without N+1;
old API gracefully lacks UI; truthful notify/exempt warnings and both languages.
Use backend focused RSpec/RuboCop, PHP lint/gettext checks, React typecheck/unit
tests, templates checker/synthetic renders under each pinned development shell.

After intended changes are committed and quick checks pass, mandatory independent
final review includes entire branch/migration history. Then long checks through
required watcher: isolated services/node integration with actual stop/manual start,
new daemon events and failed/retried mail, ownership transfer retaining VPS data,
legacy and React member/admin browser flows. No production checks/deployment.
Do not delay independent UI/template edits once this contract is read; raise
source incompatibilities promptly through lead, without inventing consumer fields.
