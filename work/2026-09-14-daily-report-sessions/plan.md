# Daily report: sessions and password changes

## Goal and current scope

Propose an extension to the vpsAdmin daily report covering session counts,
current sessions, password recoveries, and manual password changes. The user approved implementation, including the additional metrics and updates
to both configuration channels. Delivery ends with validated, pushed feature
branches. Do not merge or deploy.

## Affected repositories

- `vpsadmin`: collect report aggregates, extend the built-in English text
  template, and test the counts and rendering.
- `vpsfree-notification-templates`: extend the English HTML daily report used by
  vpsFree.cz. Its current template metadata labels this as an admin report.
- `vpsfree-cz-configuration`: pin both feature revisions with confctl channel
  set, commit the generated changes, and build both API configurations.

Inspected fetched `origin/master` revisions on 2026-09-14:

- vpsAdmin: `791ab3aa89e2f613979da6090b89785c78245db5`.
- Notification templates: `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`.

## Report period

Keep the existing rolling 24-hour period. Capture one UTC end time and use
`from <= event_time < to` for all new event counts. Label current-state counts
as snapshots at report generation. Display times through the existing template
timezone helpers. Changing the scheduler or converting the whole report to a
calendar-day report is a separate decision.

Counts of events during the period and current-state counts describe different
populations. A recovery started before the period can complete during it, and
an old session can still be active. Do not present new requests minus successful
recoveries as a failure count or success rate.

## Session metrics

Use a table with rows for Total, HTTP Basic, API token, and OAuth2, and columns
for Created during period and Active now. Include zero rows. The total must
include any unexpected stored auth type, shown as an additional/unknown row.

- Created during period: `UserSession.created_at` in the report window,
  including sessions closed before the report runs.
- Active now: open sessions with a valid access token or, for OAuth2, a valid
  refresh token. Include permanent tokens using their actual lifetime rules.
  Match the applicable account state, lockout, password-reset, and auth-enable
  checks. Avoid counting a session twice when both tokens are valid. This is a
  credential/session snapshot, not an assertion that a request from any IP
  would pass request-specific authorization.
- HTTP Basic creates and immediately closes a session for each authenticated
  request. Its Created count is therefore a request count, and Active now is
  zero. Explain this in the report.
- Token renewal and OAuth2 refresh update an existing session; they do not
  increment Created. Administrator-created detached tokens do create sessions.

The API and Prometheus currently define open sessions using `closed_at IS NULL`.
That alone can include expired credentials awaiting cleanup. The proposed
report must account for expiry without changing existing API filter behavior.

The recorded session `auth_type` is `basic`, `token`, or `oauth2`. It does not
record whether a successful login used password alone, TOTP, WebAuthn, or SSO.
The accepted breakdown uses these session types. Successful login factors
need a separate logging design and cannot be reconstructed reliably from
current user MFA settings.

## Password changes

Count `PasswordChangeLog.created_at` in the window, grouped by its recorded
source. Use these labels:

| Label | Source |
| --- | --- |
| Successful recoveries | `recovery` |
| Manual password changes | `authenticated` |
| Required password changes | `forced_reset` |
| Administrator password changes | `administrator` |
| Other password changes | `other` |

Include a total. These are actual recorded changes; do not use lifetime
`PasswordEventCounter` values to infer daily counts. Do not count a completed
recovery a second time by adding its recovery record to the log count.

## Recovery attempts

Separate request volume from account outcomes: one `PasswordRecoveryRequest`
can generate several `PasswordRecovery` rows for accounts sharing an email.
Label parent request counts and account recovery counts accordingly. A parent
request represents processed recovery work with a queued notification; it is
not proof of email delivery or a count of all public form submissions.

Recovery metrics:

- Processed recovery requests during the period, plus recoverable account
  attempts created during the period.
- Successful recoveries during the period from the password-change log above.
- Unfulfilled recoverable attempts: expired or invalidated during the period,
  shown separately and summed.
- Recovery unavailable at request time during the period: no MFA, and other
  unavailable accounts, shown separately. These records never had a usable
  recovery link, so exclude them from expired attempts.
- Pending recoverable attempts now: incomplete, not invalidated, and before
  the applicable deadline. Split into Awaiting email link and Recovery in
  progress.

For unfulfilled attempts, determine the applicable deadline from
`email_expires_at` until the link is consumed, then `session_expires_at`.
The effective unsuccessful end is the earlier of that deadline and
`invalidated_at`, where present. Count expiry at the deadline even when the
cleanup task has not run. Classify invalidation before the deadline separately;
a cleanup invalidation after expiry must not count the attempt again.
Completed recoveries take precedence over invalidation, because changing the
password also invalidates recovery records. Apply the report cutoff to all
timestamps and avoid reporting the same terminal attempt in two categories.

The current records do not preserve an invalidation reason. Do not infer a
specific cause such as factor removal or another password change. Pending
attempts are not unfulfilled. Recovery records are retained for 30 days, which
supports the daily report but not arbitrary historical reconstruction.

## Useful additions

Prioritize distinct users alongside Created and Active session counts. Compute
the overall distinct-user total independently; a user may appear in multiple
auth-type rows.

Include recorded failed login attempts during the period, grouped by mechanism
and reason. `UserFailedLogin` includes incomplete
MFA flows and some recovery TOTP failures. It requires a known user, so its
count does not cover every rejected login or unknown-account attempt. Keep
those qualifications in the label/help and group incomplete/expired flows
separately where the stored reason permits.

Include active permanent-token sessions and administrator-created sessions as
overlapping subsets. The active metric measures credential validity. A future
activity metric based on `last_request_at` would need to account for Basic's
immediate close and missing last-request timestamps.

Defer per-day recovery rate-limit and queue-full counts. The existing
`PasswordEventCounter` stores cumulative counts and the last event time only,
and recovery submissions have one-day retention. Accurate period counts need
retained time buckets or event records; neither subtraction of arbitrary daily
reports nor filtering the current cumulative counter by its last timestamp
provides that history.

## Implementation approach

Add a dedicated aggregation helper called by
`TransactionChains::Mail::DailyReport#vars(now)`. Return aggregate values under
additive keys such as `user_sessions`, `password_changes`, and
`password_recoveries`. Keep database queries out of the new template sections.
Use grouped SQL counts and targeted joins/EXISTS rather than loading complete
session histories. Include only aggregate values in the new report payload.

Update the built-in text report and the organization HTML report together.
Place the compact sections near the user overview. Apply the user-facing
writing skill after technical behavior is settled and before committing.

Inspect query plans before deciding on indexes. In particular, current
`user_sessions` and `password_change_logs` lack a standalone `created_at`
index. The core proposal needs no new event storage; additive indexes may be
appropriate for large tables. Re-fetch current heads before implementation.

## Compatibility and deployment

All proposed report fields are additive. Preserve existing fields and hook
arguments. Old templates should continue working with the new generator.
Guard new template sections when their payload is absent so the new external
template also renders with an older generator or after rollback.

Prefer deploying the generator before or together with the external template.
Current notification templates are a Nix build input reconciled at API startup;
there is no separate manual template-upload step. Use the reviewed revisions
when pinning them through confctl if deployment is later requested.

No new persisted data format, public resource/API contract, client/CLI or
Terraform behavior, inter-service protocol, node configuration, or vpsAdminOS
change is needed for the proposed core metrics. Nodes need no coordinated
update. Any new indexes would use additive migrations and need an assessment
of live-table locking and rollback cost. Old code can read the same data.

## Testing plan for implementation

- Fixed report-time specs covering empty datasets, all auth types, boundary
  timestamps, closed sessions created during the period, and old active
  sessions. Check totals and distinct-user counts across types.
- Active-session cases for expired access tokens before cleanup, usable OAuth2
  refresh tokens, expired refresh tokens, permanent credentials, closed
  sessions, account/auth disabling, and Basic sessions.
- Password-change source groups and recovery success counted exactly once.
- Recovery cases spanning report windows: one request for several users,
  no-MFA/unavailable accounts, pending email/session stages, consumed email
  links whose original email deadline has passed, expiration before cleanup,
  cleanup after expiration, early invalidation, and completion that also sets
  `invalidated_at`.
- Built-in text and external HTML rendering with populated and zero metrics,
  plus absent new variables for compatibility. Use synthetic data for previews.
- Run focused API RSpec/RuboCop in the repository Nix shell and the template
  repository's flake checks. If adding spec files, update API topic coverage.
- Commit intended changes, then run mandatory-change-review with xhigh review
  agents before longer integration checks. Extend the existing
  `tests/suite/alerts/lifetime-and-daily-report.nix` scenario if needed and
  follow selective CI rules. Run the focused integration test and both API configuration builds before
  handing off the validated branches.

## Accepted implementation decisions

- Include unique-user counts for both created and active sessions, failed-login
  counts by mechanism/reason with distinct users, and active permanent and
  administrator-created subsets. Subsets overlap and are already in the total.
- Include both pending recovery stages and the unfulfilled total.
- Add indexes on user_sessions.created_at, user_sessions.closed_at,
  password_change_logs.created_at, and user_failed_logins.created_at.
- Use auth types Basic/token/OAuth2; factor logging and daily rejection counters
  remain outside scope.
- Update exact pushed revisions with `confctl inputs channel set --commit
  vpsadmin vpsadmin REV` and `confctl inputs channel set --commit
  vpsfree-notification-templates vpsfree-notification-templates REV`.
- Build `cz.vpsfree/vpsadmin/int.api*`. API1 owns report scheduling and managed
  templates. Keep template input following vpsadminServices.
- Extend the existing daily-report integration test to check delivered content.
- User selected validated branches as the stopping point, with no merges or
  live deployments. Keep the session open.

## Review decisions and rollout detail

All four mandatory review lanes completed at xhigh. Keep the report's bounded
SQL projections separate from authentication and cleanup: they currently match
the relevant rules, while sharing them would require changing security-sensitive
callers outside this report feature. Comments and fixed-time tests identify the
parity requirement. Revisit domain-owned eligibility/deadline relations and the
auth-type catalog before later authentication or recovery policy changes.

Production has `vpsadmin.databaseSetup.autoSetup = false`. A later authorized
rollout must run `vpsadmin-api-migrate-db.service` once from the new package,
monitoring metadata locks and I/O during index creation, before relying on
indexed report performance. Old code remains compatible with the extra indexes;
rollback can leave them installed. No migration or activation runs in this task.
