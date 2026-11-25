# Shared incident escalation — released implementation contract

2026-10-30. User approved “ok, agreed, reworkit”. This replaces the
[previous narrow contract](implementation-contract-before-shared.md). It is the
single current interface/behavior specification. No merge or deployment approval.
Lead's [accepted copy](mail-rework-copy.md) supplies EN/CS wording; implementers
may proceed within the file boundaries below. No arbitrary rule editor, additional
production rule, new action, transport or workflow framework is authorized.

## Registered rule and shared evaluator

Use `IncidentEscalation` for evaluation/dispatch, `VpsIncidentSummary` for batched
SQL summaries, `VpsIncidentPolicy` for per-VPS/type settings/warning state and
`VpsIncidentAction` for durable actions. Keep a small code-defined registry under
`IncidentEscalation::RULES`; no persisted editable rule definitions.

The only production entry has key/codename **`oomd`**. Its EN label is
**VPS memory-pressure incidents**; CS **Incidenty přetížení paměti VPS**.
Its qualification scope requires backend provenance `source_kind=node_vps_event`,
non-null unique `source_key`, matching source node and `source_action` in
`restart,stop`. Node ingestion proves the VPS currently belongs to that node and
retains existing successful-event semantics. The qualifying relation also requires
`codename=oomd`; a manual report with that codename alone is not qualified.
Later migration must not invalidate historical event provenance: source node is
an ingestion-time fact, not a requirement to equal the VPS's current node forever.

Each registry entry explicitly supplies its key, EN/CS label, qualifying relation,
SysConfig category and optional warning/stopped template IDs. One shared evaluator
uses the selected relation for both decisions and summaries. No hard-coded oomd
scope outside this registration/source adapter, nor counts pooled across types.
A synthetic second rule in tests proves isolation; it is not registered in production.
Future rules may explicitly qualify manual reports. No automatic enrollment by
codename and no changes to existing `OomReport`, `OomPrevention`, node `oomd`
event protocol or existing report/metrics/history codenames.

The supported arrival boundary is
`IncidentEscalation.ingest!(vps, incident_type:, attributes:, source_node: nil, now:)`.
The source-owning adapter deliberately selects a registered type and supplies
validated report attributes; ingestion persists the report and evaluates that
selected rule under VPS serialization, then reconciles/dispatches. The node-only
`record_oomd_event` adapter supplies trusted daemon provenance. A future manual
adapter must explicitly invoke this boundary; registry registration alone does
not enroll existing API/nodectl/mail arrivals. Qualification remains rule-specific,
so a synthetic manual-qualified rule needs no `source_key`. Scheduler discovery
uses registered qualification scopes plus retained action/transfer recovery needs;
it reconciles/dispatches without re-evaluating historical reports as new arrivals.
Synthetic second-rule acceptance must exercise this public arrival-to-decision-to-
dispatch path, not only call internal `decide!`.

## Schema and settings

Revise migration **20261030180000** in place as `AddIncidentEscalation`; matching
filename `20261030180000_add_incident_escalation.rb`, migration spec and core-only
schema. Owner0 reconfirmed fresh master ac10a62f and no merge/release/deployment/
external persistence; only owned disposable local/hosted specs used it. Preserved
old head 4d72e3e7 under `refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-before-shared-incident-rework`.
Reset owned disposable databases before checking revised schema. No transitional
migration or schema-existence guards; stop if provenance changes.

| Storage | Exact replacement fields |
| --- | --- |
| `vpses` shared escalation state | `incident_enforcement_enabled` boolean NOT NULL default true; `incident_accounting_since`, `incident_last_stop_at` nullable datetime; `incident_owner_transfer_chain_id` nullable bigint. |
| `vps_incident_policies` / `VpsIncidentPolicy` | `vps_id` and `incident_type` NOT NULL, unique together; nullable integer `warning_limit_override`, `stop_limit_override`; nullable datetime `last_warning_at`; timestamps. Type is registered key, max 100 characters. |
| `incident_reports` provenance/ordinary mail | Nullable `source_key` string(64), unique; `source_kind` string(32), `source_node_id` bigint, `source_action` string(16), `notification_chain_id` bigint, `notification_processed_at` datetime. Index `(vps_id,user_id,codename,detected_at)` for scoped counts. |
| `vps_incident_actions` / `VpsIncidentAction` | Retain current action columns/states, counts, owner/epoch, stop/mail chain identities and retry fields; add NOT NULL `incident_type` string(100). Unique `(incident_report_id,incident_type)`. Retain `(vps_id,state)` index. |

Replace only this feature's new `oom_*` fields/table; unrelated existing OOM fields
remain. Per-type policy rows can be created lazily under the VPS lock when settings
or warning state need persistence; absent row means inherited limits/no warning.
Reads must not create rows. Use existing audit for per-type override and shared
exemption edits; do not silently lose audit when moving overrides off VPS.

SysConfig category **`incident_policy_oomd`**: existing `mode` String default
`observe`, `warning_limit` Integer default 5, `stop_limit` Integer default 10;
admin-only. Registry chooses category; no free-form category construction from
request input. Modes stay observe/notify/enforce. Enforce permits stops, subject
to the shared VPS exemption. Validate positive effective limit pairs, stop>=warning,
including inherited/overridden combinations. Invalid stored configuration disables
that rule's dispatch and exposes a diagnostic. Settings edits alone never act.

## VPS API: exact selected-type flat contract

Use existing Index/Show/Update routes and HaveAPI envelopes; no new endpoint.
Index/Show accept **`incident_policy`**, registered key, default **`oomd`** when
omitted. Reject unknown, blank or null selectors as invalid parameters; never
silently fall back. Selection is a read filter, not a state change. No selector
or settings input on unrelated actions such as Create/Delete. Normal strict
parameter validation applies; do not make unknown selectors inert metadata.

Return this same summary on Index and Show (and existing VPS outputs already
sharing the summary definition). API labels use the request's existing locale.
`incident_policy_label` falls back to EN for unsupported locales.

| Output field | Type / scope |
| --- | --- |
| `incident_policy` | string, selected registered key (`oomd` initially) |
| `incident_policy_label` | string, localized registered display label |
| `incident_count_7d`, `incident_count_30d` | integers; selected type/current ownership epoch |
| `incident_warning_limit`, `incident_stop_limit` | integers; selected type's effective limits |
| `incident_warning_limit_override`, `incident_stop_limit_override` | nullable integers; selected type, admin-only read/write |
| `incident_enforcement_enabled` | boolean; shared VPS stop permission, owner-readable/admin-writable |
| `incident_mode` | observe/notify/enforce; selected rule |
| `incident_stop_enforced` | boolean; selected mode=enforce AND shared VPS permission |
| `incident_status` | clear/near_limit/warning/stop_threshold; selected counts/limits only |
| `incident_last_incident_at` | nullable datetime; selected qualified type/current epoch |
| `incident_last_warning_at` | nullable datetime; selected type's last durably queued warning, not delivery proof |
| `incident_last_stop_at` | nullable datetime; shared latest confirmed escalation stop |
| `incident_next_stop_allowed_at` | nullable datetime; shared last stop+24h, never scheduled stop |
| `incident_action_state` | none/pending/failed/uncertain; shared outstanding physical stop across registered types |
| `incident_action_chain_id` | nullable integer; that shared stop's existing authorized chain ID |
| `incident_accounting_since` | nullable datetime; shared ownership epoch |

Status precedence unchanged: stop_threshold if count30>=stop limit; else warning
if count7>=warning limit; else near_limit if either count>=ceil(0.8*its limit);
otherwise clear. Counts/status must never use another rule's reports or warning
state. Shared physical action/cooldown may appear regardless of selected type;
UI describes it as VPS-wide. No second stopping rule is enabled by this contract.

Index filters: `incident_policy`, `incident_status` (same enum),
`incident_enforcement_enabled` boolean. Apply existing owner scope first, selected
qualification/status/exemption filters before count/pagination; use a single UTC
now and batched SQL for all returned VPSes. Index/Show must agree. No per-row API
queries or client counting of paginated incident reports.

Update accepts the same three writable fields as above. At least one must be
present, with an **explicit valid `incident_policy`**. Selector alone is rejected
as an empty incident update; omission is rejected when incident settings are
present. Selector/settings mixed with unrelated VPS properties are rejected
before effects. Non-admin incident writes are rejected server-side. Even an
exemption-only write requires selector, but changes the **shared VPS exemption**
for every registered rule, not a per-type value. UI must state this scope.
Null resets an override; omitted fields preserve it; exemption cannot be null.
Validate final pair atomically. Settings-only success is the existing synchronous
DB acknowledgment (`state_id` absent/null); no fabricated chain receipt. Read back
selected type and exact settings after save. React's synchronous allowlist covers
only selector plus these three fields; preserve other action receipt guards.

Capability detection: a numeric `incident_count_7d` together with returned
`incident_policy` means this interface is available. Missing fields mean unavailable,
not zero. On old APIs omit new query parameters, hide controls/indicators and keep
normal VPS views. Default Index/Show allow detection without sending a selector.
After capability is known, carry selector explicitly in filters/detail refreshes;
Update always explicit. Do not retain aliases for unreleased `oom_*` feature keys.
No new arbitrary-type selection/editor/navigation is needed with one registry entry.

## Unchanged execution invariants, with explicit type isolation

- Count unique qualified EVENTS by source identity, using their occurrence
  timestamps in UTC `(now-window,now]`, 7/30 days, within current owner/epoch.
  Do not count DISTINCT timestamps: distinct source events can share a second.
  Thresholds 5 and 10. No calendar boundaries. Ordinary
  process OOM reports, manual lookalikes and escalation's own stops do not count.
- Dedup source identity before ordinary incident mail or escalation decisions.
  Retain node/VPS/type/integer-second/action hash; integer-second collisions remain
  a known protocol limit. Registry qualification/provenance is backend-only.
- A new qualified report initiates evaluation for its registered type. At 5/7d,
  warn at most once per 7d for that type. At 10/30d, stop and then email; a stop
  supersedes a warning due for the same type/trigger. No prior-warning prerequisite.
- Stop cooldown, pending/uncertain guard and exemption are shared across types
  under the VPS lock. Further stop requires a NEW occurrence at least 24h after
  confirmed stop completion. During-cooldown reports count but never schedule
  deferred stops. Manual start/migrate/reboot do not reset state. Recovery is
  selected rolling count falling below stop limit; no separate restricted latch.
- Reports >24h late are visible/countable but cannot trigger dispatch. Future
  timestamps are audit-only until valid and never replayed. Unsent decisions
  expire after 24h; settings enabling alone cannot replay existing reports.
- Successful ownership transfer resets shared epoch and ALL per-type warnings,
  invalidates old-owner actions; retain history/shared last stop. Reconcile actual
  successful Chown/chain completion; failed transfer keeps prior epoch, uncertain
  transfer blocks dispatch. Keep member history private to owner/epoch.
- Reuse existing VPS serialization/resource locks, normal Stop with rollback_stop
  false and existing scheduler. Scope warning queues/retries by type; physical
  stop exclusion is shared. A successful Stop transaction.finished_at after chain
  completion starts cooldown. Never auto-repeat an uncertain physical stop.
- Stop preparation precedes ordinary mail preparation. Ordinary mail opt-out or
  savepoint-isolated failure cannot block a stop. Stop mail waits for confirmed
  success; failed mail retries same identity independently, never repeats stop.
  Inspect actual keep_going mail transaction result, not chain completion alone.

## Templates, variables and fallback

Exactly **four templates** (two pairs), in backend registry/core EN fallbacks and
site repository `templates/<id>/meta.rb`, `email/{cs,en}.{subject,text}.erb`:

| Purpose | Warning | Stopped |
| --- | --- | --- |
| oomd specific mapping | `vps_memory_pressure_warning` | `vps_memory_pressure_stopped` |
| Generic fallback | `vps_incident_warning` | `vps_incident_stopped` |

Mail chain `TransactionChains::Vps::IncidentEscalationMail` chooses by registered
rule and action kind. Use specific ID when registered and installed; otherwise
use generic ID. Resolve before sending. Missing/disabled recipient preference,
rendering/translation/SMTP error or nil message is NOT a reason to send fallback.
Keep ordinary template language fallback (requested language then EN). Missing
both usable template definitions is a retryable configuration error. No names
constructed by interpolating report codename or request text. Nil from existing
MailTemplateDisabled handling records intentional mail suppression; no alternate
mail or retry loop. A suppressed warning finishes that decision without advancing
last queued warning time; a suppressed stopped email leaves confirmed stop intact.

All four receive exact variables: `user` (User), `vps` (Vps), `base_url` (String),
`incident_type` (registered String key), `incident_type_label` (String in the actual
rendered template language, EN on EN fallback), `incident_count_7d`,
`incident_count_30d` (Integer decision snapshots), `warning_limit`, `stop_limit`
(current effective Integers), `warning_period_days=7`, `stop_period_days=30`,
`repeat_stop_hours=24`, `incident_at` (Time), `stop_enforced` (Boolean current
selected rule mode plus shared VPS permission). Stopped adds `stopped_at` (Time
actual successful finish), `repeated_stop` (Boolean prior shared stop in current
owner epoch). Counts are selected-type decision statistics; consequences/limits
are re-read on each render/queue/retry. Stable message ID derives from action ID
(e.g. `<vps-incident-action-ID@vpsadmin>`), never type display text.

Use existing recipient language/timezone rendering and `local_time`; do not freeze
English labels in stored decisions. Registry keys are fixed safe identifiers
(`[a-z][a-z0-9_]*`), so existing codename history-link interpolation is safe;
never pass arbitrary report text as a template ID or URL key. Generic copy has no
memory/worker/membership claims. Specific site pair retains accepted shared-node
impact, remedies, CS/EN membership/KB links and current-enforcement conditional;
core EN fallbacks omit site branding/external links. Follow lead's copy file.
Existing `vps_incident_report`, `vps_oom_report`, `vps_oom_prevention` remain.

## Ownership, ordering and acceptance

Owner0 owns vpsAdmin Git, `api/` migration/schema/models/resources/locales,
node adapter/scheduler, fallback/registry/mail chain, backend docs/specs and shared
CI registration. Rename feature docs to `docs/incident-escalation.md`; rename
related new specs/runtime test IDs and update selectors/topic coverage together.
Owner1 owns only legacy `webui/`, gettext and agreed legacy browser fixture;
use incident naming for feature helpers/forms, preserve existing OOM report files.
Owner2 owns separate React VPS adapters/components/catalogs/docs/tests, preserves
latest-search fix and unrelated OOM views; no BFF transport changes. Owner3 owns
four site template dirs/render evidence and later KB pin/capture package. Lead
owns wording/plan/state. Shared Git edits/commits remain serialized by owner0/lead.

All consumers can implement this released interface now. Backend owns common
contract corrections and reports material deviations through lead. Templates have
no UI dependency. Backend API/schema/registry must be finalized before integrated
consumer checks. KB waits final published combined backend+legacy pin; keep two
previously identified bilingual list captures/semantic IDs unless diff changes
actual impact. No React KB certification or unrelated historical refresh.

Quick checks after source changes: revised migration in owned disposable DB;
existing boundaries/dedup/concurrency/stale/ownership/mail-failure specs; synthetic
second rule proving counts, warning state, limits/template selection isolation and
shared physical cooldown/pending guard/exemption; all selector rejection/permission/
null/reset/synchronous cases; Index/Show/filter-before-page parity; generic absence
fallback versus disabled/failed specific template; real EN/CS/EN-fallback timezone
renders; PHP/gettext and React types/adapter/catalog/affected browser checks;
CI topic/runtime selector coverage. Owners diagnose existing CI failures separately;
rework does not waive them. Heavy allocations stay held until lead releases capacity.

All intended changes committed + quick checks, then mandatory independent final
review of affected substantive code/schema/API and complete branch/migration history,
then long real stop/restart/mail/ownership integration and required UI/KB captures
through fresh watchers. Prior evidence covers only unchanged inputs, not new schema.
Deploy later: migration + matching templates/backend in observe mode, compatible
UIs, verify then deliberately enable. Old nodes/ordinary clients remain compatible.
Rollback disables dispatch, reconciles physical effects and retains additive audit
state; it does not undo stops. No production write, merge or deployment authorized.
