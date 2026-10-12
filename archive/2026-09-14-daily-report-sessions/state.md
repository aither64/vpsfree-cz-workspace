---
lifecycle: complete
---

# Daily report sessions and authentication actions

## Current status

All three repositories are fast-forward merged and pushed to their remote
master branches at the exact reviewed heads below. All 27 API topic CI jobs
passed. The final integration checkout also passed all 19 report specs; the
template flake check and configuration metadata/pin checks passed there.
Previous delivered-mail integration and both API host builds remain valid at
these identical heads. The broader VM suite and newly triggered master CI are
still running or queued, with no observed failure; see merge-ci-results.json.

Removed all three temporary integration worktrees using non-force git worktree
remove, plus 13 verified disposable cache/test/profile paths. Kept canonical
feature worktrees, feature branches, built configuration generations and review
evidence. Canonical project worktrees are clean; the configuration's retained
.confctl build state is ignored. No deployment, migration, archive, deletion,
retirement or other session lifecycle action occurred. Leave the session open.

Ownership was verified with matching dev-session current and DEV_SESSION_SLUG.
Initial tracking commit: db4b167. Today's consolidated tracking checkpoint was
already committed as ab55309 before the follow-up; later routine tracking
updates remain in the working tree under workspace policy. Unrelated shared
workspace changes were preserved.

## Repositories and revisions

All branches: 2026-09-14-daily-report-sessions. Registered worktrees:
/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/PROJECT.
All origins use SSH. Final comparisons captured for all three repositories.

| Project | Pre-merge default head | Merged default/feature head |
| --- | --- | --- |
| vpsadmin | 5ac49802f892da6fd37a88c8349b9cc7ea826538 | 014fbc78422f3660b295add7a50f35cc7acdf0c8 |
| vpsfree-notification-templates | f944ba03eba5d0d6b58b7eb856f251d1c96f2c11 | 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333 |
| vpsfree-cz-configuration | 249bed1ee28e69a907edd09ea97a1144dbcdefeb | 3f213d5ebf922ab5522690ab28b3fdfa9b3bed1d |

API baseline f7996f5d and follow-up 014fbc784 are separate functional commits.
API rebased cleanly onto upstream scheduled gem/WebUI dependency commits;
range-diff proved both feature commits unchanged. Previous published API head
9456fae6 was replaced with an explicit lease. Template baseline 08402ffd and
follow-up 6ebfb6f11 are additive commits. Fresh fetches before source pushes and
pins matched the recorded bases; source heads were checked with git ls-remote.

Configuration was regenerated through confctl as one final commit per input:
6e0021ac (API) and 3f213d5e (templates). Rebase the clean configuration feature
to its original base with no replay, then regenerate both pins to consolidate
repeated updates; do not hand-edit the lock. The previous published head
50361357 was replaced with an explicit lease. Generated messages are unchanged.
Only vpsadminServices and vpsfreeNotificationTemplates changed; template
vpsadmin still follows vpsadminServices. Other inputs remain unchanged.

## Implemented behavior and decisions

- Eager aggregate queries report created/active sessions by Basic/token/OAuth2,
  distinct users, overlapping permanent/admin subsets, password-change sources,
  processed recovery requests and account outcomes, and known-account failures.
- Permanent credentials are already included in active totals. Basic sessions
  are immediately closed request records. Active includes usable access or
  OAuth2 refresh credentials and applicable account restrictions. Auth behavior
  and the public open-session filter are unchanged.
- Recovery completion takes precedence over invalidation. The applicable stage
  deadline determines expiry, including before cleanup. Pending, no-MFA and
  unavailable outcomes stay separate. Request/account counts differ in scope.
- Follow-up adds events arrays under password_changes and failed_logins, with
  timestamp to seconds, login/ID, source or mechanism/reason, and recorded client
  IP. Same [from,to) window; ascending time/ID order; repeated rows preserved;
  no cap by user decision. No inferred IP, DNS/PTR, or user agent lookup.
- User.unscoped batch lookups retain hidden users. Missing users show plain IDs;
  missing IPs show an em dash. Existing users link to their admin page in HTML.
  All new HTML dynamic data/attributes are escaped. Empty or missing events
  hide details, preserving aggregate-only and older missing-section payloads.
- Both actual templates and MailTemplate metadata expose the four aggregate
  Hash keys. Four supporting indexes, migration rollback spec, core schema,
  report specs, delivered-mail assertions and CI mapping are included. No new
  migration/logging/public endpoint/auth changes were added by the follow-up.

## Verification

Follow-up source heads above:

- Actual-database report specs rendering both actual text/HTML templates:
  19 examples, zero failures after rebase (actions-final-specs.log). Coverage:
  aggregates, boundaries/ties, repeated actions, hidden/missing users, absent
  client IP without API-IP fallback, hostile HTML data/links, empty events,
  aggregate-only payloads, and fully older payloads. API shell command:
  bundle exec rspec spec/models/transaction_chains/mail/daily_report_spec.rb
  with VPSADMIN_TEST_DAILY_REPORT_HTML pointing to the organization worktree
  and VPSADMIN_TEST_DAILY_REPORT_PREVIEWS pointing to this tracking directory.
- RuboCop and Nixfmt passed (actions-quick-checks.log). All commit hooks passed.
- Template nix flake check passed (actions-template-check.log). Chromium preview
  inspected; all generated previews and test report data are synthetic.
- ./test-runner.sh ls --filter 'tag=ci && tag=alerts' passed and includes the
  daily-report delivery scenario (actions-test-list.log).
- Delivered-mail integration passed, runner exit 0, 752.47s including build,
  startup and teardown; delivery example took 97.02s:
  ./test-runner.sh test --state-dir /tmp/dr-actions.4WED53 --status-interval 30
  alerts/lifetime-and-daily-report. Log: actions-integration.log. Fixtures assert
  one password change and failed login including user and both recorded IPs.
  Extracted actual mail: actions-delivered-report.txt. Normal test teardown
  completed. No kernel source compilation occurred.
- confctl build --yes 'cz.vpsfree/vpsadmin/int.api*' passed for API1 and API2,
  generation 2026-09-14--15-35-07. Exact toplevels and source revisions are in
  actions-build-results.json. Log: actions-config-build.log. No activation.

Retained baseline evidence: migration up/down 1 example passed
(migration-specs.log), selector 16 tests/55 assertions passed (quick-checks.log),
synthetic EXPLAIN over 5,000 history rows selects all four indexes
(query-plans.log), original 17 report specs passed, original delivery integration
passed in 674.25s (integration.log, delivered-report.txt), and both original API
builds passed (build-results.json). Index implementation is unchanged.

## Mandatory review

High risk for additive live-table indexes and cross-project report/rollout
compatibility. All reviewers used fresh gpt-5.6-sol/xhigh contexts. Follow-up
functional lanes General, Architecture, Scope, Risk; final generated-pin lanes
General and Risk. Exact ranges/criteria are in actions-review-packet.md and
actions-pins-review-packet.md. Findings and decisions:
actions-review-reconciliation.md and actions-review-*.md/actions-pins-*.md.

No Blocking/Important findings or new Advisories. Prior accepted Advisories for
report-owned active-session/recovery projections and auth-type catalogs remain;
sharing those policies would require unrelated auth/cleanup changes. Preserve
explicit comments and fixed-cutoff fixtures; revisit when domain rules change.
The original review's missing MailTemplate metadata was fixed before baseline
validation. No follow-up review remediation or rerun was needed.

Residuals: separate eager queries can observe concurrent changes and temporary
count/detail disagreement. This is generation-time reporting, not historical
reconstruction. Exhaustive rows increase memory/mail size with action volume;
known-account failure volume can be attacker-driven. No production-volume or
live index-build benchmark was run. Login labels reflect retained user rows.

## CI

Current API head 014fbc784:

- API topic specs: 34849117395, passed, all 27 jobs.
- VM suite: 34849117643, in progress.
- API migration: 34849117485, passed.
- RuboCop: 34849117365, passed.
- i18n: 34849117492, passed.
- libnodectld: 34849117432, passed.
- WebUI PHPUnit: 34849117728, passed.
- Template head 6ebfb6f11 Check: 34849022483, passed.

Superseded old-head VM run34840185855 completed cancelled after the new push;
no current-head or other-branch run was cancelled. Baseline API run34840185846
had all 27 jobs pass. Snapshot files: actions-api-ci.json,
actions-api-spec-ci.json, actions-vm-ci.json, actions-template-ci.json.
Configuration lockfile changes do not trigger a workflow. Inspect remaining
runs before any later integration decision and investigate failures.

## Rollout and environment

Production database autoSetup is false. A later approved rollout must explicitly
run vpsadmin-api-migrate-db.service from the new package once, monitoring metadata
locks/I/O. Old code can retain added indexes; rollback can leave them installed.
API1 owns report scheduling and managed templates; API2 consumes the generator.
No public resource, client/CLI, Terraform, protocol or node upgrade is required.
Recreate pins/repeat affected checks if source heads change before integration.

Use the API Nix shell for specs (it automatically changes to api/) and the root
Nix shell for Overcommit/RuboCop. Avoid concurrent root/API shell bundle setup.
An ambient-shell API push failed on an Overcommit signature before remote
mutation; verified unchanged hooks, signed within the root Nix shell, and pushed
successfully from the same shell. Use explicit leases for rewritten feature
heads. Keep integration-state paths short to fit Unix socket limits.

Durable notes: notes/vpsadmin/2026-09-14-push-hook-signature-nix-shell.md,
2026-09-14-report-schema-dump-order.md,
2026-09-14-daily-report-authentication-projections.md.
Source worktrees are clean. Generated .bin/, .bundle/ and gem caches were
removed. Textual test/review evidence and .confctl generations remain; raw
VM state directories and the temporary Chromium profile were removed. Do not archive,
delete, stop, retire, or perform other session lifecycle cleanup without an
explicit user request for that exact action.

## Portal

https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-14-daily-report-sessions/


Current CI snapshot: 2026-09-14T13:44:21.381404+00:00 (actions-ci-results.json).
21 API jobs passed; 5 remain running: API specs (full) - users-auth, API specs (full) - dns, API specs (full) - platform, API specs (core) - platform, API specs (full) - vps.
Both mail jobs are green. The broad VM run remains in progress. No current-head
CI failure has been reported. Baseline platform jobs took about 36/41 minutes;
these broader checks can outlast feature-specific validation. Check their final
results before a later merge decision. All requested source/config changes,
focused verification, delivery integration, builds and reviews are complete.
That pre-merge snapshot is superseded by the integration result below.


## Authorized integration and cleanup

The user requested merging into the default branches and cleaning up. Proceed
with fast-forward integration of all three exact reviewed heads, sources first
and configuration afterward. No deployment/migration is requested. Session
archival/deletion/retirement is not explicitly requested; leave the session and
feature branches open. Remove temporary integration worktrees and disposable
test/build leftovers while retaining review evidence.

Fresh upstream fetches still match all three recorded bases. All 27 current API
CI jobs completed successfully (run34849117395); the broad VM suite
run34849117643 is still running without a final result. The user requested merge
after the previous handoff disclosed ongoing broader CI. All feature-specific
checks, delivered-mail integration and both API builds already passed. No code
or pin changes are needed, so the completed exact-head reviews remain valid.
Temporary detached worktrees will be created under worktrees/2026-09-14-daily-
report-sessions/integration/ for fast-forward merge, checks and normal pushes.


## Completed integration

All three remote defaults and retained local/remote feature refs were verified
at the exact final heads in the table. See integration-results.json for the
pre-merge bases, final heads and cleanup inventory. The comparison captures
were refreshed before the merges; do not replace them with an empty comparison
to the now-integrated master heads.

Temporary target checkouts performed git merge --ff-only followed by normal
pushes to master. Sources were pushed before configuration. No rebase, new
code, changed pin or new review was required. From those checkouts:

- API report RSpec: 19 examples, 0 failures, 28.23s plus 14.22s load
  (merge-report-specs.log).
- Organization template nix flake check: passed (merge-template-check.log).
- Configuration nix flake metadata --no-write-lock-file and exact-pin/follows
  assertions: passed (merge-config-metadata.json).

Initial checkout-hook errors occurred after the temporary checkouts were
successfully created: API signature validation and configuration missing gems.
Verified their clean expected heads and unchanged hook files, then continued
from each repository's Nix shell. No hooks were bypassed. The reusable note
notes/vpsadmin/2026-09-14-push-hook-signature-nix-shell.md covers this case.

All feature-head API CI jobs passed. Master pushes triggered new same-head CI;
the template master check, API migration and lint passed in the final snapshot,
while other master jobs and the feature-head broad VM suite continue. No
current-head or unrelated-branch workflows were cancelled. A later deployment
still needs its own authorization and explicit migration step.
