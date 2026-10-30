---
lifecycle: active
---

# 2026-10-30-oomd-abuse-policy

## Status

- Phase: implementation authorized; preparing contract brief and feature worktrees. No deployment or integration authorization.
- Architect0 owns code/log investigation and the design brief; lead owns scope, acceptance and user communication.

## Phase checklist

- [x] Verify session identity and retained roster/access.
- [x] Investigate current incident flow and central log evidence (architect0).
- [x] Deliver calibrated policy and technical proposal (architect0; inspected/presented by lead).
- [x] Settle product choices with user: original5/10 and gentle actionable emails; user explicitly authorized implementation.
- [ ] Finalize bounded implementation contracts (architect0).
- [ ] Implementation and quick checks (implementer0 backend; implementer1 legacy UI; implementer2 new UI; implementer3 templates).
- [ ] Independent final review (reviewer0), then integration/browser checks.
- [ ] Deployment and usability verification (future, separately authorized).

## Next actions

- Commit initial substantive tracking, prepare feature worktrees and finalize architect brief. Backend/API is the dependency for both UI packages and template variable contract.
- Before implementation settle delayed-event eligibility and ownership-transfer treatment, using the smallest compatible contracts. Do not expand this proposal into a queue/protocol redesign.

## Documentation

- [Plan](plan.md), architect-owned [design proposal](design.md), and [log evidence](evidence.md).
- Project documentation deferred until policy acceptance and implementation.

## Repositories

- No feature branches or worktrees registered. Implementation scope: vpsadmin backend/legacy UI, separate vpsadmin-webui, and vpsfree-notification-templates. vpsadminos/configuration inspected read-only. Existing origin snapshots were used; see design for exact revisions, not deployment proof.

## Commands run

- `dev-session current`: exact expected slug; environment identity agrees.
- `dev-session team list 2026-10-30-oomd-abuse-policy --as-is`: retained delegated_4 roster, architect0 ready with workspace_write access.
- Assigned complete read-only investigation/design package to architect0 via `dev-session team assign --message-stdin`.
- `dev-session url ... --as-is`: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/

## Results

- User explicitly authorized implementation: "anyway you can proceed with implementation of your plan". Scope includes backend/API, legacy UI, separate React UI and cs/en notification templates. Retained members are ready/workspace_write. Architect assigned contract finalization; implementers will own complete execution packages. No merge or deployment approval inferred.

## Implementation backlog

| Owner | Package | Dependencies | Acceptance evidence |
| --- | --- | --- | --- |
| architect0 | Final brief/API and email contracts, delayed-event and transfer semantics | Selected5/10 policy | Durable brief before application edits; bounded compatible decisions |
| implementer0 | vpsadmin backend/API/ingestion/chains/schema/docs | Architect brief, initial tracking commit | Dedup/rolling boundaries/cooldown/exemption/permissions/failure specs and hooks; committed feature head |
| implementer1 | Legacy PHP UI/locale changes | Stable API/settings contract | Count/status/override views and admin/member checks; serialize vpsadmin Git with backend owner |
| implementer2 | vpsadmin-webui API/views/locales/docs | Stable API/settings contract | Type/unit checks, required PR, member/admin UI coverage; committed feature head |
| implementer3 | Notification templates cs/en/rendering | Stable mail variables; lead-approved prose | Required memory/config/shared-impact guidance and KB links; effective limits; rendered checks and commit |
| reviewer0 | Independent final review across complete committed series | All deliverables committed; quick checks pass | General/architecture/scope/risk lanes, explicit whole-history/migration conclusion |

- Latest user wording refinements recorded: say "you can increase your VPS's memory" instead of requesting expansion; omit the word "policy" in the email and say the VPS "will be stopped automatically". Lead applied user-facing writing guidance to the replacement sentences. Thresholds remain5/10; no implementation or deployment changes.

- Additional user email requirement: explain that this resource abuse affects other VPS on the same node and may disrupt their services. Lead incorporating the shared impact into the gentle memory/configuration guidance.
- Architect restored current5/10 limits in design/evidence; lead inspected. Membership expansion links verified read-only in both languages: https://kb.vpsfree.org/information/membership_fees#what_the_membership_fee_is_composed_of and https://kb.vpsfree.cz/informace/platby . Reciprocal marker confirms pairing; existing incidents#oomd guidance also supports shared-node impact and worker-count tuning. No KB writes. Lead prepared English action-required example under vpsfree-user-facing-writing, mentioning shared-node impact, checking worker count/memory, and expansion if workload requires it. Actual templates will supply effective limits and incident links; bilingual repository implementation remains future work.

- Latest user decision supersedes the threshold recalibration below: "no, let's keep the original thresholds for now." Current limits are5/7d warning10/30d stop, with rolling-count recovery below10. User directs gentle email advice about more memory or configuration changes, particularly excessive web-server worker counts, with a relevant membership-expansion KB link. Architect assigned compact design/evidence restoration and read-only link verification; lead owns prose. No application implementation authorized by this clarification alone.

- User identified VPS28376's recent problems as an expected policy case. Lead acknowledged final top-five table omitted joint-sixth VPS28376 and original5/10 would not reliably act: it has5/9 weekly/monthly candidates, or4/8 excluding unresolved attempt. Revised proposed defaults3/7d warning and8/30d stop capture it under either count. At original cutoff, saved candidate distribution has8/21 weekly VPS at3 and7/48 monthly VPS at8; denominators are eventing VPS only, not fleet prevalence. Architect agreed and updated design/evidence from existing data; lead inspected the revised policy and table. No new live queries or implementation. Earlier5/10 analysis below is retained as superseded candidate evidence. Existing counts alone never trigger a retroactive stop; a qualifying new incident is required.

- Central read-only SSH works (`log.int.prg.vpsfree.cz`). Targeted daemon action/failure/coverage scan for 2026-09-29 through 2026-10-30 finished exit 0 in approximately 2.5 minutes, reading 5.0 GB logical (~1 GB allocated), avoiding the approximately 195 GB full node logs. No full node-log scan launched. Exact rolling counts, coverage qualification and candidate shares pending architect analysis.
- Source distinction: killer hit/miss diagnostics are not incidents; restart/stop records are attempts; `osctl_oomd` broadcast follows successful command return. Existing incident `detected_at` retains original integer-second event time; current ingestion lacks an event key/deduplication. No DB access used.
- Canonical notification remote confirmed as `vpsfree-notification-templates`; project-map mail name is a stale alias. Architect inspects existing origin refs without fetch/Git mutation and will record revision limitations.
- Recovery alternatives narrowed: prefer simple rolling-30-day threshold gating for v1; explicit quiet-period latch remains an alternative, not a settled requirement.
- At fixed cutoff 2026-10-30 14:30 UTC: trailing 30d has 164 attempted actions minus 6 explicit failures = 158 inferred successful restarts across 48 VPS. Trailing 7d has 51 inferred successes across 21 VPS. Zero stop attempts/broadcast errors observed. Coverage: 12 daemon-source hosts on every one of 32 sampled dates, with gaps still possible; not DB-confirmed incident counts or fleet prevalence.
- Candidate defaults: 5/rolling7d warning (4/21 eventing VPS at cutoff, 7/48 reached within some observed 7d window); 10/rolling30d stop (5/48 at cutoff). Alternative monthly thresholds 8/12/15 cover 7/3/1 eventing VPS. 26/48 had one incident, another 12 had 2–3.
- Numeric defaults are provisional, pending selective node confirmations and shadow-mode calibration in future rollout. No tests, review, deployment or live policy actions run.
- Selective confirmation complete: node23 Oct30 has 8 attempted restarts, 7 nodectld confirmations and one unresolved attempt (VPS28376). Confirmed completion delays 26–560 seconds reinforce use of source occurrence time. Excluding the unresolved attempt reduces candidate total 158→157, weekly threshold crossings at cutoff 4→3, and leaves monthly-10 candidate set at 5 VPS. Treat totals as proxies, not proven DB incidents. All live queries have ended.
- Architect delivered design/evidence; lead inspected the complete records and checked top candidate counts against distribution.json. Monthly top five: 27741=19, 28655=14, 4135=12, 27837=11, 29528=10. No owner identities queried.
- Proposed repeat-stop semantics: new incident required, rolling30d threshold gating, >=24h since completed policy stop, no timer stop, manual start allowed. Admin exemption disables policy stops while retaining warnings/counts. Observation-first rollout; no retroactive mass stop. Standard stop chain disables autostart.
- Implementation boundaries: backend/API/ingestion/chains first; legacy/new UIs after API contract; localized templates after mail-variable contract. No synchronized node update required for v1.
- No application checks or independent final change review run: this deliverable is routine investigation/planning. Implementation will require quick checks, committed-deliverable review, then longer integration/browser checks. No deployment/usability claim made.

## Open questions

- User acceptance of defaults/policy and activation timing; inferred counts need shadow reconciliation against live incident ingestion.
- Bounded implementation decisions: stale-event action eligibility and ownership-transfer counter treatment; preserve incident audit history and permissions.

## Cleanup

- None. Session remains open and active.
