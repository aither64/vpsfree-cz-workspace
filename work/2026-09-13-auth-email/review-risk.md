# Risk and compatibility review

Reviewed the committed ranges specified by the review packet:

- vpsadmin `791ab3aa89e2f613979da6090b89785c78245db5..3c24a6aadacb054732a2a22214c98e3edb03ef5c`
- vpsfree-notification-templates `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..06f03bad4294b6f28ca9478e907f43967ebeb7d0`

Later uncommitted or follow-up remediation in either worktree was excluded from
the review. No long integration test was started.

## Findings

### Blocking: SSO is accepted as independent proof of the new-device policy

At the reviewed vpsadmin head, `EmailLogin.check_authority!` accepts evidence
whose method is `sso` even when `required?` has just established that the
current device is not a usable known device
(`api/lib/vpsadmin/api/email_login.rb:57-68`). The OAuth SSO path needs only an
SSO plus any usable `UserDevice` belonging to the same user
(`api/lib/vpsadmin/api/authentication/oauth2_config.rb:122-126` and
`:951-960`). That device can still have `known: false`. `create_authorization`
then replaces the missing evidence with a standalone SSO proof and persists it
in the authorization (`api/lib/vpsadmin/api/authentication/oauth2_config.rb:1002-1007`
and `:1095-1112`). The same proof is accepted again during authorization-code
exchange (`:238-258`).

This defeats the explicit boundary that SSO retains its existing flow only with
valid device proof. A concrete first-device race is enough to reach it: two
password authorizations can bootstrap while the account has no successful
device history, producing SSO cookies and unfinished devices in both browsers.
After the first code exchange marks its device known, the second browser's
original authorization correctly fails the final device check. That browser
can nevertheless start another authorization with its SSO and still-usable
unknown-device cookie; the `sso` proof bypasses the email challenge and code
exchange succeeds. This also defeats the required recheck after concurrent
first-device completion.

Bind SSO authorization to the specific current device and store ordinary
`device` evidence with its ID. Do not exempt an `sso` method from
`check_authority!`. Add regressions for SSO on a usable known device and for an
unknown, revoked, or expired device both before authorization and at code
exchange.

### Important: account creation bypasses the enrollment gate and mailbox validation

The new preference was added to the shared `:writable` parameter set
(`api/lib/vpsadmin/api/resources/user.rb:9-30`). The administrator-only Create
action consumes that complete set and passes it directly to `User.new`
(`:124-154`). The enrollment gate and `EmailLogin.valid_email?` check exist only
in Update's `check_email_verification_enrollment!` (`:375-494`). There is no
model validation providing the same invariant.

An administrator API client can therefore create an opted-in account while the
default-off enrollment gate is closed, including with a missing, malformed, or
multi-recipient primary email. The gate can no longer guarantee that no account
is opted in while old workers are still present. Once such an account gains
successful device history, an unknown-device password login fails closed at
`EmailLogin.start` with `email_login_unavailable`, leaving the member dependent
on a known device or administrator repair.

Keep the preference out of Create so new records use the database default, or
apply the same gate and single-mailbox validation there. Add Create action
regressions covering a submitted opt-in while the gate is closed and with an
invalid primary mailbox.

### Important: disabling SSO does not invalidate an unexchanged SSO authorization

`User#authentication_settings_changing?` advances the generation and destroys
pending OAuth authorizations for password, email, MFA, token, Basic, OAuth,
lockout, and lifecycle changes, but it omits `enable_single_sign_on`
(`api/models/user.rb:289-304`). A new SSO lookup does honor that switch
(`api/lib/vpsadmin/api/authentication/oauth2_config.rb:896-905`), while an
authorization code already created through SSO is exchanged through
`get_tokens`, which rechecks OAuth/account state and the stored email/device
evidence but never rechecks whether SSO remains enabled (`:238-258` and
`:1136-1150`).

An SSO-authenticated authorization can consequently be exchanged during its
ten-minute lifetime after the user disables SSO. This conflicts with the
documented rule that login-method changes invalidate pending authentication.
It is especially relevant when disabling SSO is the response to suspected
cookie exposure. Include `enable_single_sign_on` in the authentication-setting
generation callback, preserving active sessions and refresh tokens as planned,
and test disabling SSO between authorization creation and code exchange. If an
issued OAuth code is intentionally considered completed rather than pending
authentication, record that exception explicitly in the plan and rollout
documentation.

### Advisory: an unknown challenge flow is treated as token authentication

`EmailLogin.check_user!` selects OAuth only for the literal `oauth2` flow and
treats every other value as `token` (`api/lib/vpsadmin/api/email_login.rb:191-195`).
The two current callers create only `oauth2` and `token` contexts, and both
public completion endpoints also constrain their stored context, so this does
not provide a current external bypass. It is still a fail-open authentication
dispatch boundary: a later caller, corrupted row, or migration mistake can
silently acquire token-flow eligibility instead of being rejected. Use an
exhaustive case for the two supported values and reject everything else before
creating or processing a challenge; cover this with a focused regression.

### Advisory: the shared rate limiter lacks a concurrent bucket test

The limiter creates and locks fixed-window account and source-IP rows in sorted
order (`api/models/email_login_rate_limit.rb:3-24`). The implementation appears
to serialize reservations correctly, including the unique-row insertion race.
The reviewed specs exercise limits sequentially
(`api/spec/lib/vpsadmin/api/email_login_spec.rb:97-128`), while the only
cross-connection email-login spec verifies one-time challenge consumption
(`api/spec/models/operations/authentication/email_login_concurrency_spec.rb:4-43`).
They do not exercise simultaneous first insertion or final-slot consumption by
different users sharing one IP.

Add a no-transaction, independent-connection test that releases concurrent
workers against the same source-IP bucket and proves that the limit is not
overshot. Boundary coverage should also establish fixed UTC rollover and the
separation of send and failure counters. This is Advisory because the lock
order and unique index support the intended behavior and no implementation
failure was found by inspection.

## Compatibility and data-safety assessment

Apart from the findings above, the authority checks are placed at the relevant
issuance boundaries. Password results carry an authentication generation;
email challenges bind a bcrypt code hash, recipient snapshot, flow parameters,
and browser/OAuth context; challenge processing reloads the user and token under
locks. Token and Basic issuance repeat policy checks, and OAuth code exchange
rechecks both current policy and the referenced device. Device revocation also
takes the user lock. Resend rotates the hash without extending the original
deadline or resetting guesses, and enqueue failure rolls the rotation back.

Forced password reset retains the verified email or MFA proof, changes the same
opaque continuation to `reset_password`, removes the email hash, and grants a
fresh five-minute server-side lifetime. Reset and final session creation recheck
the generation and current policy. Existing sessions, supplied tokens, refresh
tokens, and completed OAuth sessions are not invalidated by the additive
mechanism.

The database migration is additive: the user preference defaults false, the
OAuth proof column is nullable, rate buckets are new, and `email_login` is
appended to the existing `AuthToken` enum. The recorded deployment constraint
is material: old authentication workers do not enforce opted-in accounts, so
schema and effective templates must precede a coordinated API/WebUI update and
the enrollment gate must remain closed until every password entry point runs
the new code. The Create finding currently weakens that gate. Rollback can keep
the additive schema, but pending email tokens must be drained and operators
must explicitly accept that the old application loses enforcement.

The built-in and production template contracts agree on the variables and
fixed expiry/resend semantics. The login chain uses the snapshotted primary
address with `exclusive_recipients: true` and explicit empty CC/BCC. Rendered
messages and their codes remain in normal mail/transaction storage; Index and
Show access to `MailLog` remains administrator-only
(`api/lib/vpsadmin/api/resources/mail_log.rb:26-42,54-70`). This is the explicit
accepted retention decision.

The production template change is data-only and does not alter a protocol or
persisted format. The downstream KB contract pin and release preparation need
the exact final pushed API revision and correctly remain a separate phase from
this review.

## Residual risks and test gaps

- The source-IP limits assume the trusted reverse proxy overwrites
  `X-Real-IP`; both bucket selection and the member-facing login notice use that
  value. Deployment should retain that proxy boundary.
- The coordinated mixed-version rollout and documented rollback/drain procedure
  have been reasoned from the additive migration and gate. They have not yet
  been exercised on a live multi-worker deployment.
- Long OAuth/WebUI browser and integration coverage remains pending by design.
  The pending HTTPS-only test-origin correction was outside the reviewed
  commits; production cookies remain `Secure`.
