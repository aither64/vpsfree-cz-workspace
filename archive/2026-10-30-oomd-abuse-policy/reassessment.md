# Incident escalation reassessment

2026-10-30. Historical decision analysis: user approved the recommended predefined-rule
shared design (“ok, agreed, reworkit”). The [released contract](implementation-contract.md)
now supersedes the provisional names/options below. Arbitrary admin-created rules
were not selected. This analysis made no application, Git or runtime changes.

## Recommendation and alternatives

Prefer a **shared incident escalation evaluator with predefined rules**, initially
only the existing whole-VPS memory-pressure rule. Count per VPS and incident type;
reuse the current warning, stop, retry and ownership behavior. Rule registration
decides which reports qualify and which templates apply. Matching a free-form
codename alone must not silently authorize automatic stops.

| Option | Shape and tradeoff |
| --- | --- |
| Rename the narrow feature | Rename new `oom_*` identifiers to `memory_pressure_*`; least rework, but another incident type would duplicate or later extract its evaluator/state. |
| Shared evaluator, registered rules (recommended) | One code-defined rule registry, per-type settings/counts, shared action execution. One registered rule initially; no rule builder or new transport. Modest additional schema/API work now gives incident escalation a clear home. |
| Admin-created rules for any codename | Requires a persisted rule CRUD/configuration interface and decisions about eligible sources, duplicate identity and historical reports. A report count can be valid for one source and inflated by another. This is a separate product scope, not implied by generic evaluation. |

Future rules may legitimately count administrator-filed reports. Each rule needs
that explicit qualification contract; manual origin is not inherently invalid.
The current memory-pressure rule continues to require a trusted successful
whole-VPS stop/restart event and must exclude manual lookalikes.

## Existing facts supporting the boundary

- `IncidentReport.codename` is a nullable string, not an enum or trusted type
  registry. Admin API Create accepts it; nodectl writes it; configured mailbox
  parsers can produce reports. `user_id`, `vps_id`, `detected_at`, `filed_by_id`
  and `mailbox_id` provide existing ownership/time/origin context.
- `IncidentReport.vps_action` is an existing one-report instruction (`none`,
  `stop`, `suspend`, `disable_network`), with optional CPU limiting. It is not
  the action already taken by the daemon or an escalation-rule definition.
- Current `VpsOomPolicy` combines source ingestion with otherwise reusable
  counting, qualification, decision, stop and mail reconciliation. `VpsOomSummary`
  already shares SQL between counts, filters and pagination.
- Existing `MailTemplate` registration and incident-report scheduler/chains
  suffice. `OomReport`, its rules/tasks and `OomPrevention` are separate existing
  concepts; preserve them, existing incident codenames and node `oomd` messages.

## Small concrete shape for discussion

| Boundary | Proposed shape; names remain provisional |
| --- | --- |
| Rule definition | Small Ruby registry keyed by existing codename; first key `oomd`, display meaning “VPS memory-pressure incidents”. Entry selects qualifier, default limits and template IDs. No arbitrary expressions/actions or runtime rule builder. |
| Qualification/ingestion | Keep daemon adapter responsible for node/VPS validation and unique source identity. Generalize new IncidentReport provenance to `source_key`, `source_kind`, `source_node_id`, `source_action`; source fields are backend-written, not admin Create inputs. The first qualifier checks codename plus trusted source and successful restart/stop action. |
| Shared evaluator | `IncidentPolicy` / `VpsIncidentSummary` operate on a selected registered type. Keep the VPS lock and existing transaction chains. Durable `VpsIncidentAction` adds rule/type identity to the current action record; repeated notification and stop progress remain independent. |
| Settings/state | Per-VPS/type row (e.g. `VpsIncidentPolicy`) holds nullable limit overrides and last warning. Existing VPS ownership epoch/transfer marker remain VPS-scoped. Stop permission and confirmed physical-stop cooldown can remain VPS-scoped; see unresolved multi-rule decision below. This adds one small settings/state table to the current action table, not a generic workflow store. |
| Defaults | Existing SysConfig, scoped by registered type (e.g. category `incident_policy_oomd`), with current `mode`, `warning_limit`, `stop_limit`. No new modes or editable action vocabulary. |
| API | Keep existing VPS Index/Show/Update routes. A selected registered `incident_policy` identifies the summary/settings; rename new summary fields to `incident_*` and return the selected key. Current single-rule default can remain `oomd`; explicit selection for settings prevents ambiguity. Preserve batch counts, status/exemption filtering before pagination, owner reads/admin writes and synchronous isolated settings updates. Exact field contract follows scope acceptance. |
| UI | Existing VPS list/detail/admin controls show rule label, counts and limits. Initially one rule needs no rule editor or extra navigation. Keep incident history filtered by codename; process OOM reports retain their separate UI. A second enabled type would need a visible type selector, not pooled counts. |
| Email | Existing registry selects specific `(type, warning/stopped)` templates with generic incident-warning/stopped fallback. Suggested specific IDs: `vps_memory_pressure_warning` / `vps_memory_pressure_stopped`; generic pair: `vps_incident_warning` / `vps_incident_stopped`. Existing count/limit/consequence variables survive; generic copy needs type identity/label. Selection is an explicit registry mapping, not a template name constructed from untrusted input. |

Source-specific advice belongs in the specialized template: memory/configuration,
excess workers and membership links for this rule. Generic copy must not assume
every incident is caused by insufficient memory or harms other VPS. Lead owns
the final English/Czech wording. Existing single-incident mail remains separate;
its opt-out cannot block escalation stops or their independent mail retry.

## Preserved behavior and unresolved decisions

The first rule preserves **5/rolling 7 days**, **10/rolling 30 days**, rolling-count
recovery, and further stops only after a new event at least 24 hours after the
last confirmed successful stop. No timer-driven stops, retroactive activation or
mandatory prior warning. Keep 24-hour stale-event visibility-only dispatch,
deduplication, transfer epoch reset, old-owner suppression, exemption visibility,
pending/uncertain-stop blocking, completed-stop proof and durable mail retries.
Current integer-second source-key collision remains a producer limitation.

Counts and warning recurrence must be per type, never pooled. For multiple rules,
recommend one physical-stop cooldown/pending-stop guard and exemption per VPS
so independent types cannot multiply stops; this is a proposal requiring explicit
acceptance before a second stopping rule. Per-type override/exemption distinctions
need confirmation only if the user chooses multiple configurable rules now.

The immediate product decision is **registered predefined rules versus arbitrary
admin-created rules**. For the latter, qualification/dedup semantics and eligible
types must be settled before activation. Suspend, network disable and CPU limiting
remain existing one-report actions; adding them to escalation is deferred.
No additional arbitrary-rule UI/schema needs design before that scope answer.

## Compatibility, ownership and verification impact

Session state records migration `20261030180000` as unmerged, unreleased,
undeployed and never externally persisted; only disposable databases used it.
Therefore the implementation owner can revise this single migration/schema after
reconfirming that provenance, resetting owned disposable DBs. Do not add transition
migrations/existence guards merely to retain discarded local drafts. Public feature
branches alone are not a released API, but all current backend/UI/template consumers
must change together. If external persistence is discovered, reassess upgrade needs.

Keep the old node protocol and all existing report APIs working. Deploy schema,
matching templates/backend in observe mode, then compatible UIs. Older APIs hide
the new UI by capability detection. Rollback preserves audit/additive state and
reconciles dispatched stops; it cannot undo actual stops. No deployment authorized.

- Backend owner0: current policy/summary/action models, provenance migration/schema,
  VPS/IncidentReport/SysConfig APIs, node adapter, scheduler, mail registry/chains,
  docs, specs and CI selection. Extract qualification without broad parser rewrites.
- Legacy owner1: only `webui/` and agreed browser fixture; React owner2: existing
  VPS adapters/components, translations, REQ-051/API docs and tests. Both depend on
  the accepted exact backend contract; preserve separate OOM-report screens.
- Templates owner3: specific/generic registered template pairs and render checks;
  backend owns fallback/registry. KB package waits for final published backend pin.

Quick checks after implementation: existing behavioral specs under final names,
migration up/down, excluded manual/same-codename/process-OOM reports, source dedup,
per-type isolation with one synthetic second rule, current ownership/late-event/
mail-failure tests, API permission/filter/batch parity, template fallback and
specialized renders, PHP lint and React types/catalog/adapter checks. Moving spec
or runtime files requires CI topic/selection updates. No checks run in this design.

This is a substantive redesign if accepted: final committed changes and quick
checks require independent affected-lane review before long integration/capture
checks. Existing test results cannot certify changed schema/API. Retain the bounded
real stop/restart scenario and visible UI/KB checks, not a new broad test campaign.
Canonical KB workflow still applies to changed labels/list captures; preserve
semantic IDs and the two identified capture concepts unless actual scope changes.

Source evidence: vpsAdmin `api/models/{incident_report,vps_oom_policy,vps_oom_summary,
mail_template}.rb`, `api/lib/vpsadmin/api/{resources/incident_report,incident_reports,
tasks/incident_report}.rb`, `api/models/transaction_chains/incident_report/{new,send,
process,utils}.rb`, node `vps_events.rb`, nodectl `commands/incident_report.rb`;
React `src/lib/api/vps.ts` and `src/pages/app/vps/VpsOom*.tsx`; site template pairs
under `templates/vps_oom_{warning,stopped}/`. Inspected current owned worktrees;
no fetch, source edits, tests, builds or live queries.
