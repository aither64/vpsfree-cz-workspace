# Individual authentication actions: functional review

Initiative: 2026-09-14-daily-report-sessions.
Workspace: /home/aither/workspace/ai/vpsfree.cz.
Plan/state: work/2026-09-14-daily-report-sessions/{plan,state}.md.

## Request and acceptance

The existing feature adds session counts/splits, active credential counts,
permanent and administrator-created subsets, password changes/recoveries and
recorded failed-login summaries. The user approved a follow-up listing all
password-change and failed-login actions beneath their existing summaries.
Each row includes time with seconds, login and user ID, change source or failed
mechanism/reason, and the recorded client IP. Preserve repeated actions; sort
oldest first with ID ties; impose no row limit. Missing IP uses an em dash.
Batch-resolve even default-scope-hidden users, preserving missing users by ID.
HTML links available users to their admin page and escapes dynamic data.
Add events arrays under password_changes and failed_logins. Empty or absent
events hide details, keeping existing aggregate-only payloads compatible.
No PTR/user-agent lookup, inferred IPs, extra recovery rows, new logging,
new schema changes in this follow-up, auth-policy changes, merge or deployment.

## Committed series and ownership

All worktrees: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-14-daily-report-sessions/PROJECT.
All branches: 2026-09-14-daily-report-sessions.

- vpsadmin base 5ac49802f892da6fd37a88c8349b9cc7ea826538
  baseline feature f7996f5df67d82c9627c73aae8e2b40101609570
  final head 014fbc78422f3660b295add7a50f35cc7acdf0c8
- vpsfree-notification-templates base f944ba03eba5d0d6b58b7eb856f251d1c96f2c11
  baseline feature 08402ffd8010384f950b1ec4a1b95de8e5410ba3
  final head 6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333
- vpsfree-cz-configuration base 249bed1ee28e69a907edd09ea97a1144dbcdefeb
  current baseline head 5036135728832d5c375705e3b69949c33460ff7e

The API owns data projection and the built-in text consumer. The independent
organization template consumes the same internal report vars. Daily-report
MailTemplate registration declares four Hash parameters. Configuration supplies
these through vpsadminServices and vpsfreeNotificationTemplates; templates'
vpsadmin input follows vpsadminServices. API1 schedules the report and manages
templates; API2 also consumes the API package. Discover any further relevant
consumers from code/pins.

Each source has a baseline feature commit and a follow-up commit explicitly
requested after baseline delivery. API behavior and its supporting tests and
text rendering stay together; the HTML consumer is separately reviewable.
API was rebased over upstream scheduled gem and WebUI dependency updates only;
the baseline commit was previously 9456fae6f181cef2e8982eed462e873095fd49da.
Focus on follow-up and its interaction with the full feature; inspect history.

## Configuration phase

Current configuration pins the baseline heads; final pins require accessible
pushed revisions. After functional review, push sources, regenerate exact pins
through confctl, then run final general/risk pin review before long builds.
Do not hand edit flake.lock. Preserve generated messages and all unrelated
inputs. Build both cz.vpsfree/vpsadmin/int.api* without activation.

## Quick evidence

19 actual-database report RSpec examples passed before rebase; post-rebase
result is actions-final-specs.log (check completion). Tests render both actual
templates and cover repeated rows, boundaries, tie ordering, hidden/missing
users, absent client IP without API-IP fallback, hostile HTML values and hrefs,
empty and aggregate-only and older missing-section payloads.
RuboCop and Nixfmt passed (actions-quick-checks.log); template nix flake check
passed (actions-template-check.log). Commit hooks passed. Chromium screenshot
visually inspected; previews are synthetic. The delivered-mail integration
scenario now inserts and asserts one action of each kind; no follow-up long
integration has started yet. Baseline integration/builds and all 27 API CI jobs
passed. No new files need selector/topic mapping changes.

## Risk, compatibility, and explicit decisions

High risk for full series: additive live-table indexes, authentication-derived
reporting and cross-project compatibility/deployment. All reviewers use
sol/xhigh. Lanes: general, architecture, scope, risk.
Baseline four indexes are unchanged; production autoSetup=false means a later
approved rollout must explicitly run vpsadmin-api-migrate-db.service from the
new package and monitor locks/I/O. Old code tolerates added indexes; rollback
may leave them. No public API/client/CLI, protocol, node or coordinated upgrade.
Old templates ignore additional vars; new templates guard old missing vars and
old missing events. Historical rows expose only already-recorded admin-report
data, never credentials. Report recipients/access remain unchanged.

Prior review reconciliation in review-reconciliation.md records bounded
eligibility/deadline projections as accepted Advisory: refactoring domain auth
and cleanup callers is outside this report task. Reassess concrete new defects,
but do not require unrelated auth-policy refactoring solely for sharing.
Separate queries can observe concurrent mutations: this is generation-time
reporting, not historical reconstruction. No volume cap is an explicit user
decision for these action lists. Source categories reuse summary labels.

Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and the assigned
lane reference. Review directly with fresh context; no code edits or nested
agents. Report severity, commit and file/line evidence. Save results to the
assigned tracking artifact and send a concise result to the parent.
