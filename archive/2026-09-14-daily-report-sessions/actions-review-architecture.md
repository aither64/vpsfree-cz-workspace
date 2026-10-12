# Architecture and repetition review

Reviewed the exact committed functional series for:

- `vpsadmin`
  `5ac49802f892da6fd37a88c8349b9cc7ea826538..014fbc78422f3660b295add7a50f35cc7acdf0c8`
  (`f7996f5df` baseline, `014fbc784` individual-action follow-up);
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..6ebfb6f11c1ba00ae9dc7868ac0b3c42d30e5333`
  (`08402ffd` baseline, `6ebfb6f1` individual-action follow-up).

The current configuration range
`249bed1ee28e69a907edd09ea97a1144dbcdefeb..5036135728832d5c375705e3b69949c33460ff7e`
still pins the baseline source heads and is deliberately deferred from this
functional review until the final source heads are pushed and repinned. The
rebased vpsAdmin baseline is patch-identical to the previously reviewed
`9456fae6f` commit according to `git range-diff`.

No Blocking or Important findings. No new Advisory finding was introduced by
the individual-action follow-up.

## Accepted residual advisories from the baseline

### 1. Usable-session policy remains a report-owned projection

Commit `f7996f5df` implements active-session eligibility in
`api/lib/vpsadmin/api/daily_report_authentication.rb:54-81`. It necessarily
repeats rules also represented in the token/OAuth2 resume operations and the
OAuth2 refresh-token lookup: account-state eligibility, lockout and password
reset, mechanism enable flags, permanent-token representation, access-token
expiry, and the refresh-token fallback. A future authentication-policy change
could update the runtime owner without updating the report and silently skew
the active snapshot.

This is the previously reconciled Advisory. The projection currently matches
the inspected runtime owners at the reviewed revision, has an explicit parity
comment and focused boundary coverage, and a structural extraction would
require changing security-sensitive authentication callers outside this
report feature. Keep the recorded follow-up to revisit a domain-owned,
time-parameterized eligibility relation when those rules next change.

### 2. Recovery deadline selection remains a report-owned historical view

Commit `f7996f5df` derives the email/session deadline and terminal
classification in
`api/lib/vpsadmin/api/daily_report_authentication.rb:91-123`. The same stage
choice also appears in `PasswordRecovery#email_token_usable?`,
`#session_usable?`, and the expiry cleanup task. A future recovery stage or
deadline change could leave the report's historical CASE expression stale.

This is also the previously reconciled Advisory. The report needs a fixed
historical cutoff and completion precedence that the live predicates do not
provide, and the reviewed tests cover the relevant boundaries. A shared
relation should be designed with the live and historical consumers together
when the recovery state machine changes; no current-scope remediation is
required.

### 3. Authentication-type catalogs are still independently declared

The report's known zero-row catalog and active-mechanism conditional live in
`api/lib/vpsadmin/api/daily_report_authentication.rb:4,33-40,63-66`, while the
UserSession resource independently declares `basic`, `token`, and `oauth2` in
`api/lib/vpsadmin/api/resources/user_session.rb:10`. Adding a stored mechanism
would automatically produce a raw created row, but its active classification
and public choices would still need coordinated edits. This remains the prior
Advisory: give the finite machine-level type catalog one domain owner when a
new mechanism is introduced, and require provider coverage for its active
strategy. The English label maps should stay in their presentation consumers;
both safely fall back for an unknown stored value.

## Follow-up architecture assessment

The API remains the owner of the cross-project payload. Commit `014fbc784`
adds both action collections through one `event_details` boundary
(`api/lib/vpsadmin/api/daily_report_authentication.rb:84-88,127-145`). That
helper owns the half-open report relation supplied by its caller, stable
`created_at, id` ordering, projected row fields, and unscoped batch identity
resolution. Both the built-in text template and external HTML template only
render the resulting hashes. There is no repeated query, lookup, sorting, or
missing-user policy in a consumer.

The two action families reuse the helper without forcing unlike source and
failure semantics into a catalog. Presentation repetition is proportionate:
password-source labels remain local to each format, detailed failure columns
differ from password-change columns, and the HTML-only `action_user` helper
centralizes linked/missing user rendering at
`templates/daily_report/email/en.html.erb:99-106`. Extracting the small row
layouts across the independent repositories would obscure format ownership
without removing a behavioral rule.

Compatibility is localized and bidirectional. Old templates ignore the new
`events` members; both new templates test `events&.any?` and therefore accept
the prior aggregate-only payload. The external template's vpsAdmin flake input
is made to follow `vpsadminServices` by
`vpsfree-cz-configuration/flake.nix:31-34`, and API1 consumes both that template
package and the API package. API2 consumes the same API package but does not
schedule or install the external template. Searches of current repository
refs found no additional consumer of the four authentication payload sections;
the KB capture repositories refer only to the `daily_report` template identity,
not this payload contract.

Provider and representative-consumer coverage is present in
`api/spec/models/transaction_chains/mail/daily_report_spec.rb:276-475`, which
uses the actual text template and the companion HTML template, and in the
delivered-mail scenario at
`tests/suite/alerts/lifetime-and-daily-report.nix:70-112`. Post-rebase focused
verification completed with 19 examples and 0 failures. RuboCop, Nixfmt, the
template flake check, and commit hooks are recorded as passing in the packet.

## Residual limits and pending validation

- Unbounded eager action arrays can make unusually active reports large; the
  absence of a row cap is an explicit user decision for this report.
- Aggregate and detail queries are intentionally independent and may observe
  concurrent writes differently. The report is a generation-time operational
  summary rather than a transactional historical reconstruction.
- Final configuration pins, long delivered-mail integration, and both API host
  builds remain pending by plan. Their absence is not an architecture defect in
  these committed functional heads.
