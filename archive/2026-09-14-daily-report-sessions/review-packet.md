# Daily report session and password activity: functional review

## Requested outcome and accepted scope

Implement the plan in `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-daily-report-sessions/plan.md`: rolling 24-hour session counts
(total and Basic/token/OAuth2 splits, distinct users, active credential state),
permanent/admin-created active subsets, password change sources, recovery
outcomes, and recorded failures grouped by mechanism/reason. Render both the
vpsAdmin text and vpsFree HTML reports with additive payloads and old-generator
guards. Migration adds four query indexes. Keep auth behavior unchanged.

User selected validated feature branches, no merges or deployment. Session
slug: `2026-09-14-daily-report-sessions`. Coordination root: `/home/aither/workspace/ai/vpsfree.cz`.

## Committed functional changes

- vpsAdmin worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/vpsadmin`
  Base: 791ab3aa89e2f613979da6090b89785c78245db5
  Head: 8769884ae69b03c22d8532fd09acf6de85542015
- Templates worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/vpsfree-notification-templates`
  Base: f944ba03eba5d0d6b58b7eb856f251d1c96f2c11
  Head: 4dc2706df6332d235cad18c1202602004b75d63c
- Configuration worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/vpsfree-cz-configuration`
  Base/current head: 249bed1ee28e69a907edd09ea97a1144dbcdefeb

Each functional repository has one commit for this report feature. The API
commit includes aggregation, its supporting query indexes/schema/migration spec,
the built-in template, report specs, selector mapping, and delivery assertions.
They implement and validate the same behavior. The organization template
commit is independently reviewable as a consumer of the new aggregate payload.

## Configuration phase after functional review

Configuration pin commits require pushed revisions accessible to Nix. They
will follow this review and receive their own final pin/compatibility check.
Use `confctl inputs channel set --commit vpsadmin vpsadmin REV` and
`confctl inputs channel set --commit vpsfree-notification-templates
vpsfree-notification-templates REV`. Only vpsadminServices and
vpsfreeNotificationTemplates should change; the template's vpsadmin input
already follows vpsadminServices. Build both `cz.vpsfree/vpsadmin/int.api*`
configurations without deployment. API1 schedules the daily report and manages
the organization templates.

## Verification already performed

- Initial daily report smoke: 5 examples passed.
- Aggregation and both-template rendering, including populated/empty/old
  payloads and HTML escaping: 17 examples passed (`render-specs.log`).
- Migration up/down: 1 example passed (`migration-specs.log`).
- Ruby lint: 5 changed Ruby files passed (`final-lint.log`).
- CI selector: 16 tests / 55 assertions passed (`quick-checks.log`).
- Notification templates: `nix flake check` passed.
- Core-only ActiveRecord schema dump: only version + four indexes after
  preserving preexisting declaration order.
- Final rendering rerun follows a grammatical label adjustment.
- Long integration tests have not been started. Existing daily-report delivery
  test assertions were extended. API migration paths already select full CI.

## Risk and compatibility

Risk: high because of additive indexes on live persisted tables and a
cross-project report payload/configuration update. No new authentication
policy, credential storage, public API resource, protocol, node behavior,
or coordinated node upgrade. Old code can use the indexed schema. New
sections guard missing aggregate payloads. Migration deployment needs the
normal operator-controlled database migration step before service activation;
no live migration or deployment is authorized here. All reviewers: xhigh.

Required lanes: general, architecture, scope, and risk/compatibility.
Read the mandatory-change-review skill and your lane reference. Review the
committed series directly; do not edit files or launch nested reviewers.

## Acceptance details and explicit non-goals

- Permanent/admin counts are overlapping subsets, not additions to active.
- Basic records represent individual requests and are immediately closed.
- Active includes usable OAuth2 refresh tokens and applicable account flags.
- Requests and account recoveries have different cardinalities. Completion
  supersedes invalidation; expiry uses the applicable stage deadline, not
  cleanup time. Pending and unavailable attempts are not unfulfilled.
- Failures cover known accounts, including incomplete flows and recovery TOTP
  failures, not every rejected public request.
- No inferred successful login factors, no per-day cumulative-counter math,
  no success percentage across unrelated request/completion cohorts.
- No generalized telemetry/event framework, public endpoint, or report schedule
  change. Historical replay beyond current retained state is not promised.
- No integration of branches, live activation, or session lifecycle cleanup.

Synthetic previews: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-daily-report-sessions/daily-report.html` and `daily-report.txt`.
State: `/home/aither/workspace/ai/vpsfree.cz/work/2026-09-14-daily-report-sessions/state.md`. Report findings with severity, file/line and
commit evidence. Save your final review to the requested lane artifact.
