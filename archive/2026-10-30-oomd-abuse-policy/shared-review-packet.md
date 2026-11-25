# Shared incident escalation final review packet (preparation)

Status: RELEASED for independent final source review. All intended substantive application source/docs/tests are committed and affected quick checks pass. Long runtime/build/browser checks and feature publication remain held pending this review. Prior original-range reports are retained as evidence, not certification of the shared redesign.

## Request and accepted boundary

User questioned feature-only OOM naming because individual OomReport/process-kill
reports are a separate subsystem. User then proposed generic repeated reports by
type with specific templates and approved the bounded shared-engine recommendation:
“ok, agreed, reworkit”. Authoritative current brief: [implementation-contract](implementation-contract.md),
[design](design.md), [accepted main-agent EN/CS copy](mail-rework-copy.md).
No arbitrary rule builder, second production rule, new transport/action framework,
new public endpoint, node protocol change, deployment or merge is authorized.

Expected final shape: IncidentEscalation registered-rule evaluator/arrival;
VpsIncidentSummary shared qualified SQL; VpsIncidentPolicy per-VPS/type overrides
and warning time; VpsIncidentAction durable typed actions; shared VPS stop
permission/cooldown/pending-stop guard/ownership epoch. Only production ruleoomd
qualifies trusted successful whole-VPS restart/stop; OomReport/process OOM remains.
Source-node provenance survives VPS migration. Explicit backend arrival for a
synthetic second manual-qualified rule demonstrates genuine shared behavior.

Keep5/7d warning,10/30d stop, new incident after24h physical-stop completion,
observe default, rolling-count recovery, source dedup, late-event visibility-only,
owner change accounting reset with physical cooldown/history retained. Mail optout
or savepoint failure cannot block enforcement; nil New/Create synchronous success
is supported. Isolated typed settings validate/audit atomically before effects.
Generic/specific template selection only falls back for missing template definition,
never recipient optout/render/SMTP errors; labels match actual rendering language.

## Scope, reviewer and lanes

Overall HIGH risk: changed additive schema, public API/consumers, persisted action
and ownership state, host stop behavior and extension boundary. All four lanes:
general; architecture/repetition; scope/proportionality; risk/compatibility.
Retained eligible independent reviewer0, gpt-6.1-sol/xhigh/read_only, no overrides
or nested reviewers. Verify actual live roster/identity again before assignment.
Use mandatory-change-review and all four lane references. Routine design/tracking
has no separate review gate; all substantive source/docs/tests are in final scope.

## Exact ranges and consolidation (fill only from final receipts)

| Repository | Base | Retained pre-rework head | Final head / readiness |
| --- | --- | --- | --- |
| vpsadmin | ac10a62f1cb0fc890378ae83cdf18dd0e29f049a |4d72e3e754fd47b598de1e54e05b3c5d26c62200|e9a6530b0e18f2f58b013b3a470f3d6991d79876; local checked/committed, unpublished|
| vpsadmin-webui |40653dffed4561dd6086716fd506a7223d3631d7|b67c7917e8758e707e0b88512f055eab9fbd8529|55a813b44edb915c7ed5ce68366d6d797a551606; local quickchecked/committed, unpublished|
| vpsfree-notification-templates |2cfd218d9152888feea4109f064459078ea9f76e|e8c2c3df4ae57015ff4fba3647b13aa219d0c216|bf32762126f21fb7fc825fac25b5b45d075a2681; local checked/committed, unpublished|
| vpsfree-kb-contracts |ce2c8cd9358c3636e5d39343e595df813a0b197f|1119bcdcf7db00a9bd91e84490d7a8de37c3575e|HELD, dependent later mechanical exact source pin/captures|

Source worktrees are under worktrees/2026-10-30-oomd-abuse-policy/<repo>.
Owner0 serializes all vpsadmin Git and integrates owner1's webui-only source.
Retain refs/range-diffs for original reviewed and pre-shared source. Final series
must introduce final generic design directly, not retain OOM implementation then
replace it. Keep separately justified isolated MariaDB testDb compatibility commit;
no old alias/shim needed for unreleased branch fields. No default branch changes.
Final review must inventory WHOLE base-to-head series/diff, obsolete approaches,
repeated dependency/pin/generated streams and explicit migration conclusions.

Migration20261030180000 is revised in place to AddIncidentEscalation. Owner0
reconfirmed unmerged/unreleased/undeployed/no external persistence; disposable local
and hosted spec DBs only, no runtime guest ever booted. Fresh SSH master remained
suppliedbase, old source preserved. Final schema must directly assume preceding
migration, no guards/transitional draft step; final dump core-only. Recheck final
owner receipts before reviewer certifies this. React/templates/KB have no migrations.
KB has never run/captured pinned earlier iterations; fold one final pin stream later.

## Final backend series and acceptance inspection

- Backendffbe4cc5234a294cd2ca9ffc49f492183c08ce8d.
- Legacy8a6309553d0de3ee2535ffce7af5e3960eb9caaf.
- Testenve9a6530b0e18f2f58b013b3a470f3d6991d79876.
- Full final vpsAdmin diff60files,+3480/-153. Exactly one new migration:
  api/db/migrate/20261030180000_add_incident_escalation.rb.
- Tree931bbd2c80c51c2c5db3e2eaa7bdc393e6005728 exactly equals hook-checked
  preconsolidation857b6147829261bf44f02f6efb51b684a7a687d3 retained under
  refs/review/2026-10-30-oomd-abuse-policy/vpsadmin-shared-before-consolidation.
- Owner reports rebase/hooks exited0/no rebase state; branch restored. Lead read-only
  verified full HEAD/tree/old-ref tree equality and three-commit list. Tracked/index
  clean, only excluded webui/.phpunit.cache untracked. No source/test command active.
- Fresh SSH default/mergebase remainsac10a62f; no default movement or integration.
- Backend commands/results/contracts/provenance: [shared-backend-delivery](shared-backend-delivery.md).
  Owner is appending final range/history receipts; source identity above authoritative.
- Legacy source/results/copy: [legacy-incident-rework](legacy-incident-rework.md),
  [final UI copy](legacy-incident-ui-strings.md).
- React full final packet: [react-rework-review-packet](react-rework-review-packet.md).
- Template full final packet: [template-rework-review-packet](template-rework-review-packet.md).
- Original reports: review.md,review-followup.md,testdb-review.md,kb-history-review.md.
  The old narrower design is intentionally superseded; final generic interfaces,
  qualifier/privacy/arrival scope and changed consumer contracts require real review.

## Checks and diagnostics already known (not final-gate certification)

- Core CI fixture contamination confirmed with unchanged negative3/2 and7/6
  exact-order slices, corrected only minimal owned fixture/session/config cleanup
  positive3/0 and7/0. Original assertions/order retained. Final broad exact-head
  hosted foundation acceptance still required. MariaDB11.8/OFF/RR receipts prove
  earlier independently reviewed testDb compatibility remains effective/justified.
- Legacy revised PHP120tests/832assertions +focused13/92, gettext/lint/format pass;
  exact source scope/hash in legacy-incident-rework.md. Existing pagination warning
  unrelated/unchanged, not masked.
- Templates32synthetic render cases/16first-repeat equivalences/1actual pinned
  EN-label fallback render/checker77templates383files/Nixcheck pass. All specific
  subject/body bytes unchanged from accepted original. Input renderer/checker9fc0648;
  this is NOT final backend selection/transport proof. See template-rework-review-packet.md.
- React final affected quick packet ready (react-rework-review-packet.md). Backend48app/0 +2separate migration/0 +49corrected adjacent/0 +9real site renders/0 pass; final26filelint, locale, hooks and3commit consolidation completed. Selector16/55 and13topic421fileexactonce coverage pass. Retain invalid trailing-dot launch as no-valid-result evidence, not app failures; corrected six-path native49 result separate. Native/input receipts bind final commit equivalence once source is consolidated.
- Full real-node stop/autostart/mailretry/manualstart/Chown-data-retention scenario,
  real legacy browser, updated React synthetic screenshots/full checks/hosted CI,
  final KB source+capacity+four bilingual captures+strict check remain post-sourcegate.

## Final review duties and limits

Independently inspect the exact complete final ranges, commit splits, diffstats/range-diffs/source trees, native quick outcomes and migration/core schema provenance. Verify actual API topic exact-once/runtime selector proof, provider and representative consumers, docs placement and source-specific/generic mail distinction. Explicitly conclude whole-history consolidation/obsolete approaches/repeated input streams and migration lineage (or no migrations). Source clearance only: exact-head hosted full/core CI, real guests and updated UI/KB media remain later required checks; no merge/deploy/readiness-for-use claim. Do not run tests/builds/CI or edit source/tracking; deliver report by authorized team reporting, lead preserves file.

No production inspection/activation/merge/readiness-for-use claim. Session open:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/
