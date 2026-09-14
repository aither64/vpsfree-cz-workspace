# Keep daily-report projections aligned with authentication changes

The daily report's `VpsAdmin::API::DailyReportAuthentication` is a read-only
projection of stored session and password-recovery state. Review it when
changing token/OAuth2 authentication, account eligibility, recovery stages, or
cleanup deadlines.

The public session filter uses `closed_at IS NULL`; the report also checks
usable access/refresh credentials and account restrictions. Permanent tokens
are an overlapping subset of active sessions. Calling resume operations from
the report would mutate request counters, timestamps, authentication context,
and sometimes tokens, so it is not a suitable substitute for aggregate SQL.

Recovery reporting captures one cutoff, uses the applicable email/session
deadline, and gives completion precedence over invalidation. Cleanup can mark
an expired recovery invalidated later, and successful recovery also invalidates
records. Do not count those as another unsuccessful outcome. Live usability
predicates alone do not answer historical daily-report questions.

Review found no current mismatch. A structural shared implementation would
require changing authentication/cleanup callers, so that refactor was deferred
outside the reporting-only feature. Keep the fixed-time boundary specs and
explicit helper comments. If those domain rules gain another stage/mechanism,
design the shared time-parameterized interface and its provider tests together.

Verified by four mandatory review lanes, 17 report specs, and the delivered-mail
integration test in `work/2026-09-14-daily-report-sessions/`.
