# 2026-10-30-oomd-abuse-policy

## Goal

osctld-oomd restarts/stops containers that abuse system resources. vpsadmin picks up these events and creates incident reports. i'd like to create a policy to handle frequent abusers. for example, if a vps has several oomd incidents in a week, the user is sent an "action required" email. If a vps has greater amounts of oomd incidents per month, the user is sent an email and the vps is stopped. the question is what to do then if the user starts the VPS and oomd incidents keep coming. I'd say stop the VPS after oomd incident, but once per day.

so we'll need to establish the policy and modify vpsadmin to support this. we should have some overview in vpsadmin webuis (both legacy and new) -- to see how many oomd events there were and if the vps is nearing limits. the limits could be configurable by admins per vps (with defaults) and admins should be able to disable the policy, i.e. prevent the VPS from stopping. we'll also need email templates in vpsfree-notification-templates.

suggest a solution.

## Affected repositories

- vpsadmin: incident ingestion, policy enforcement, API and legacy PHP WebUI.
- vpsadmin-webui: separate React WebUI consuming the shared summary/settings API.
- vpsfree-notification-templates: confirmed canonical remote; project map's `vpsfree-mail-templates` is a stale alias.
- vpsadminos and production configuration: read-only sources for oomd event semantics and central logging access; implementation changes only if evidence demonstrates a need.

## Approach

User authorized implementation: "anyway you can proceed with implementation of your plan". Implement the selected original5/10 thresholds and final email wording, both WebUIs and notification templates. Feature branches, checks and review are in scope; merge and deployment approval remain separate.

1. Architect investigates current event/incident flow and existing stop/email mechanisms.
2. Read central osctl-oomd logs, as explicitly authorized by the user's follow-up, to measure per-VPS rolling weekly/monthly counts, burst patterns, duplicates and coverage.
3. Propose evidence-based defaults, warning/stop/repeat-stop semantics, recovery and admin exemptions, plus matching visibility in both WebUIs.
4. Record the technical design and future execution packages in [design.md](design.md). Lead presents the proposal and unresolved product choices.

## Decisions

- Verified same-session identity: `dev-session current` and both environment markers match this initiative and workspace.
- Retain Full-team roster/settings; architect0 owns investigation/design. Implementers remain unassigned until the proposal is settled.
- Central log access is read-only. No deployment, stop commands, live configuration changes or merge is authorized by this proposal task.
- Numeric thresholds are recommendations based on the observed log distribution, subject to policy acceptance and live shadow reconciliation.
- User decision: keep original warning at 5 qualifying incidents in rolling 7 days and policy stop at 10 in rolling 30 days for now. The subsequent 3/8 recommendation was not accepted. VPS28376 remains below the monthly stop threshold in saved evidence (5/9 weekly/monthly candidates or4/8 excluding unresolved attempt). Start in observation mode and calibrate before enabling stops. Counts are inferred successful daemon actions, not a DB incident audit; see [evidence](evidence.md).
- Preferred v1 recovery proposal: repeat stops gated by rolling-30-day incident count; each needs a new incident and a rolling 24-hour policy-stop cooldown. Return to normal as count ages below threshold. No daily timer stop or independent quiet-period latch.
- Admin exemption should disable vpsAdmin policy stops while preserving counts/visibility and existing node-level oomd protection; precise warning behavior remains in proposal.
- User email direction: explain gently that the VPS may need more memory or a configuration change. Common cause: services such as a web server spawn more worker processes than available memory can support. Suggest checking/reducing worker concurrency and assessing memory needs; link the relevant membership-expansion KB article for workloads requiring more memory. Do not diagnose every incident as misconfiguration or imply expansion alone fixes it. Lead owns actual user-facing wording under vpsfree-user-facing-writing; templates use effective per-VPS limits.
- Explain the shared impact: resource pressure from this VPS affects other VPS on the same node and may disrupt their services. Connect this to the request for corrective action without blaming the member.
- User wording refinement: say members "can increase your VPS's memory" with the membership-expansion link, rather than "request" an expansion. Do not mention "policy" in the email consequence; say the VPS "will be stopped automatically" upon reaching its effective monthly limit. English draft sentences: "If your workload needs more memory, you can increase your VPS's memory through a membership expansion." and "If your VPS reaches 10 incidents within 30 days, it will be stopped automatically." Template rendering must substitute the effective per-VPS limit.
- Verified English expansion guidance: https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of (Everything About Membership Fees). Describes resource expansion with increased fees and contacting support. Use the member's language-specific KB target in templates.
- Verified Czech counterpart: https://kb.vpsfree.cz/informace/platby (Vše o členských poplatcích), resource expansion under Z čeho se skládá členský poplatek. Reciprocal page marker confirms pairing. Incident guidance also verified: https://kb.vpsfree.org/manuals/vps/incidents#oomd and https://kb.vpsfree.cz/navody/vps/incidenty#oomd support shared-node impact and tuning worker counts to available memory. No KB edits required for this proposal.

## Compatibility and deployment

Design must preserve mixed-version API/node operation, existing incident reports and ordinary user VPS starts. Assess additive persistence, deduplication and durable enforcement state, idempotent stop/email dispatch, deployment ordering, activation epoch and rollback before implementation.

## Documentation

Readers: operators and future implementers. Current [proposal](design.md) and [evidence](evidence.md) belong in this session. Accepted behavior and API/admin instructions should later live with vpsadmin; actual localized email copy belongs with its template repository. No project documentation changes in this investigation phase.

## Testing plan

This phase uses read-only source inspection and log analysis; record time coverage and counting semantics. Future implementation checks must cover rolling-window boundaries, duplicate/reordered incidents, concurrent delivery, daily stop cooldown, recovery/re-arm, overrides/exemptions, permissions and both WebUIs. Final independent change review and integration checks apply after implementation, not to routine investigation/planning alone.
