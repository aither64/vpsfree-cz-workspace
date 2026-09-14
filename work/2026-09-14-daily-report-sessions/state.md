---
lifecycle: active
---

# 2026-09-14-daily-report-sessions

## Delivery status

The approved implementation is committed and pushed in all three repositories.
Focused checks, delivered-mail integration, both API configuration builds, and
all 27 API CI jobs passed. The broader VM CI run remains queued on shared
runners at handoff; see ci-results.json for the timestamped snapshot.
No branches were merged and no live deployment or migration was performed.
Keep this session open for review and follow-up.

Ownership was verified with matching dev-session current and DEV_SESSION_SLUG.
Initial tracking commit: db4b167. This handoff is the day's consolidated tracking
checkpoint. Preserve unrelated changes in the shared workspace.

## Repositories

All branches: `2026-09-14-daily-report-sessions`. Registered worktrees live in
`worktrees/2026-09-14-daily-report-sessions/<project>`. Origins use SSH.

| Project | Base | Pushed head |
| --- | --- | --- |
| vpsadmin | 791ab3aa89e2f613979da6090b89785c78245db5 | 9456fae6f181cef2e8982eed462e873095fd49da |
| vpsfree-notification-templates | f944ba03eba5d0d6b58b7eb856f251d1c96f2c11 | 08402ffd8010384f950b1ec4a1b95de8e5410ba3 |
| vpsfree-cz-configuration | 249bed1ee28e69a907edd09ea97a1144dbcdefeb | 5036135728832d5c375705e3b69949c33460ff7e |

Fresh upstream fetches before source pushes and downstream pins showed unchanged
bases. Source heads were independently verified with git ls-remote. Captured
all three exact comparisons using dev-session worktree capture-comparison.
API and template worktrees are clean; configuration has only shell-generated
untracked .bin/ and .bundle/ directories.

## Implementation and decisions

- Eager SQL aggregation adds created/active sessions by Basic/token/OAuth2 and
  distinct users, overlapping permanent/admin subsets, password-change sources,
  processed recovery requests and account outcomes, and known-account failures.
- Active includes usable access or OAuth2 refresh credentials and applicable
  account restrictions. Basic sessions are immediately closed request records.
  Authentication behavior and the public open-session filter are unchanged.
- Recovery completion takes precedence over invalidation. The stage deadline
  determines expiry, including before cleanup. Pending, no-MFA and unavailable
  outcomes remain separate; request and account counts have different scopes.
- Both actual templates guard absent aggregate fields. HTML escapes dynamic
  labels/reasons. MailTemplate metadata documents all four new Hash keys.
- Added four indexes with migration rollback coverage, updated the core schema,
  and extended existing report specs, delivered-mail assertions and CI mapping.
- confctl generated separate commits 158516e5 (API) and 50361357 (templates),
  with automatic messages unchanged. Only vpsadminServices and
  vpsfreeNotificationTemplates moved; template vpsadmin still follows
  vpsadminServices. Other staging/production/OS/nixpkgs inputs are unchanged.

## Verification

See verification.md for the compact checklist and portal previews.

- Final report RSpec: 17 examples, 0 failures. Actual text/HTML, populated and
  empty statistics, old payloads, escaping, time boundaries and registry keys.
  API shell: bundle exec rspec
  spec/models/transaction_chains/mail/daily_report_spec.rb, with
  VPSADMIN_TEST_DAILY_REPORT_HTML pointing to the template worktree and
  VPSADMIN_TEST_DAILY_REPORT_PREVIEWS pointing to this tracking directory.
  Log: final-render-spec.log.
- Migration up/down: 1 example, 0 failures (migration-specs.log). Ruby lint,
  migration-spec coverage, and all commit hooks passed.
- CI selector: 16 tests / 55 assertions (quick-checks.log).
- Final template nix flake check passed (final-template-check.log).
- Synthetic EXPLAIN on 5,000 history rows selects all four indexes, including
  the actual active relation (query-plans.log). This is not a production
  latency or live index-build benchmark.
- Final Chromium preview inspected. All preview and delivered-report data are
  synthetic. No real member messages were sent.
- ./test-runner.sh test --state-dir /tmp/dr-test.Y0gjeo --status-interval 30
  alerts/lifetime-and-daily-report passed, runner exit 0. Script took 674.25s
  including build/startup/teardown; delivery example took 93.18s. Evidence:
  integration.log and delivered-report.txt. Normal test teardown completed.
- confctl build --yes 'cz.vpsfree/vpsadmin/int.api*' passed for both hosts.
  Generation: 2026-09-14--14-00-03; exact toplevel/input revisions captured in
  build-results.json. No kernel source compilation or activation ran.

## Mandatory review

Risk high: live-table indexes and cross-repository report compatibility.
All reviewers used gpt-5.6-sol/xhigh with fresh context. Functional lanes:
General, Architecture, Scope, Risk; downstream pin lanes: General and Risk.
Reviewed ranges, packets and evidence are in review-*.md.

No Blocking or Important findings remain. Added the missing MailTemplate
metadata identified by Risk. Architecture accepted the duplicated session and
recovery projections as Advisory after reconciliation established current
parity and that actual sharing would require auth/cleanup changes outside
scope. Auth-type catalog duplication is also Advisory. Retained explicit
comments and fixed-cutoff fixtures; revisit these projections when domain rules
change. Final metadata/comment/layout fixes passed focused checks and did not
require broad review reruns. Both final pin reviews returned no findings.

Residual limits: separate eager queries can observe concurrent state changes;
this is a generation-time snapshot, not arbitrary historical reconstruction.
Production index creation costs have not been benchmarked.

## CI and next step

- API topic specs: 34840185846, all 27 jobs passed.
- API migration: 34840185909, passed.
- RuboCop: 34840185949, passed.
- i18n: 34840185800, passed.
- libnodectld: 34840185832, passed.
- Templates Check: 34840175378, passed.
- Full VM CI: 34840185855, queued at handoff behind other initiatives.
  https://github.com/vpsfreecz/vpsadmin/actions/runs/34840185855
- Configuration: no workflow triggered by its lockfile-only branch.

Check the queued run before a later integration decision and investigate any
failure. No superseded runs were created or cancelled. The focused local
delivery test supplies feature-specific end-to-end validation while this
broader run waits for shared capacity. No merge or deployment is authorized.

## Rollout and environment notes

Production database autoSetup is false. A later approved rollout must explicitly
run vpsadmin-api-migrate-db.service from the new package once and monitor index
locks/I/O before relying on indexed performance. Old code can use the additive
indexes; rollback can leave them installed. API1 owns report scheduling and
managed templates; API2 consumes the generator. No protocol, public resource,
client/CLI, Terraform or node update is required. Recreate downstream pins and
repeat affected checks if the source heads change before integration.

Worktree checkout hooks initially reported trusted signatures/ambient gems, but
creation and registration succeeded. Inspected/signed hooks and used repository
Nix shells. API shell changes to api/; root shell supplies Overcommit. Use short
real integration-state paths to avoid Unix socket limits. Notes:
notes/vpsadmin/2026-09-14-report-schema-dump-order.md and
notes/vpsadmin/2026-09-14-daily-report-authentication-projections.md.

Transient local logs, test state and generated development-shell files remain
available. Do not archive, delete, stop or retire this session without an
explicit user request for that action.

## Portal

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-daily-report-sessions/
