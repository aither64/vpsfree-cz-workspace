# Email verification for logins from unknown devices

## Goal and scope

Implement optional email verification after a correct password for accounts
without effective TOTP/passkey authentication. Users enable it in profile
settings; it defaults to off. Recognized devices keep their existing login
behavior. An account without any successful known-device login is exempt.

Implementation was authorized on 2026-09-14 after the user accepted the plan.
Production deployment and KB promotion are not part of this implementation.

Confirmed decisions: 30-minute email challenges; retained successful device
history counts after expiry/revocation; password reauthentication but no email
confirmation when enabling; normal administrator-only outgoing mail history.
Use existing bcrypt for the challenge code hash and the existing mail queue.
No new delivery service, secret provisioning, or node protocol is needed.

## Affected repositories and existing behavior

`vpsadmin` owns the API policy, storage, mail integration, Ruby OAuth2 login
page, PHP profile setting, translations, and tests. Inspected fetched
`origin/master` at `791ab3aa89e2f613979da6090b89785c78245db5` on 2026-09-14.

- `api/lib/vpsadmin/api/authentication/oauth2_config.rb` resolves the
  `vpsadmin_devices` cookie to usable device tokens. Cookies are Secure,
  HttpOnly, and SameSite=Lax; IP/user-agent metadata are not trust proofs.
- `api/models/user_device.rb` has a 90-day renewable token lifetime. Revocation
  and expiration delete the token but retain the record and its `known` flag.
- `Operations::UserSession::NewOAuth2Login` sets `known: true` after an
  authorization code exchange creates a session. Password submission and
  unfinished authorization do not make a device known.
- `Operations::Authentication::Password` is shared by OAuth2, Basic, token
  issuance, and password reauthentication. Effective MFA depends on the MFA
  switch and enabled credentials. `AuthToken` already supports staged login,
  forced password changes, and password authentication generation checks.
- `TransactionChains::PasswordRecoveryMail` already supports exclusive
  primary-email delivery. However, `MailTemplate.send_mail!` and
  `Transactions::Mail::Send` persist rendered mail bodies.
- Regular users request administrator approval to change their primary email;
  they cannot directly replace it through `User.Update`.

`vpsfree-notification-templates` owns the production English/Czech login-code
emails, as explicitly requested by the user. Keep its variable contract and
expiry wording synchronized with the built-in templates.

Check `haveapi` and `haveapi-client-php` consumer compatibility during
implementation. The inspected Ruby/JS/PHP clients support arbitrary
`next_action` callbacks; actual CLI and unattended flows still need testing.
Use `vpsfree-kb-contracts` for documentation impact, bilingual pages, and
captures. No vpsAdminOS or node authentication protocol change is proposed.

## Policy and first-device semantics

Add `users.enable_new_device_email_verification`, non-null boolean, default
false, independent of the existing MFA setting. After password/account checks:

```ruby
require_email =
  user.enable_new_device_email_verification &&
  !effective_totp_or_passkey_auth?(user) &&
  user.user_devices.where(known: true).exists? &&
  !recognized_device_for_user?(user, request_context)
```

Effective MFA means the MFA switch is enabled with at least one usable enabled
factor: confirmed TOTP or an enabled passkey. Configured but disabled MFA does
not suppress opted-in email protection. Keep the email preference while MFA is
active so it takes effect again if effective MFA is disabled or removed. Email
never satisfies a TOTP/passkey challenge or changes its existing trust periods.

Recognizing the current device requires possession of an unexpired, unrevoked
token belonging to that user with `known: true`. An IP address, user agent,
device ID, active-but-unconfirmed device row, or another user's token is not
sufficient. Trust is established only after the full login succeeds.

Confirmed interpretation: treat "already has at least one known device"
as successful login history, including retained revoked/expired known-device
records. Revoking the last device or waiting for its token to expire should
not silently disable email protection. Existing retained records support this
without a new flag. Future deletion of this history would need a durable
first-success marker. A literal active-device-only rule is possible, but would
restore password-only bootstrap after the last token expires or is revoked.

## Flow and challenge storage

1. Check the password and account/login-method eligibility before sending mail.
   Wrong passwords retain the existing neutral failure response.
2. Evaluate policy in the API with server-validated device context. Keep raw
   password verification separate from email delivery so profile password
   reauthentication cannot accidentally issue login codes.
3. If required, create a pending authentication and send a code to the primary
   email snapshot. Render a separate email-code step with a masked destination
   and resend action. Do not persist or forward the submitted password.
4. Verify and consume the challenge atomically, then continue to a forced
   password change if required or complete authorization. No OAuth2 code, SSO
   cookie, access token, or session is issued before all required steps succeed.
   Preserve the existing point at which session creation marks the device known.

Reuse `AuthToken` with an appended `email_login` purpose, preserving existing
enum values. Existing serialized options hold a bcrypt code hash, recipient
snapshot, fixed expiry, failed attempts, send/resend state, and flow binding.
Add database-backed rate-limit buckets shared by all API workers. TOTP, WebAuthn, and password-reset actions must reject this purpose.

Bind the challenge to the initiating browser and validated OAuth2 context:
client, redirect URI, requested scope, state and PKCE as applicable. The code
alone cannot resume another browser's login or change the requested authority.
Token authentication binds its own requested scope/lifetime. Use CSRF-protected
POSTs, no-store responses, and keep secrets out of URLs and referrers.

Confirmed starting limits: random six-digit code, 30-minute fixed lifetime,
five incorrect attempts, 60-second resend cooldown, and three sends per
challenge. Resend rotates the code without resetting attempts or extending
expiry. Shared per-account issuance/guess limits across challenges, plus IP
limits, prevent fresh logins from resetting the budget. Email throttling must
not deny known-device logins. Bound pending challenges without allowing every
new attempt to cancel a legitimate pending login.

Store a bcrypt hash using the existing crypto provider. Lock consumption, wrong
attempt increments, resend rotation, and send-budget reservation. At completion,
recheck password generation, email snapshot, eligibility, device revocation,
and current authentication policy. Restart if the security context changed.
Revalidate before granting authority so concurrent first-device login or a
security-setting change cannot leave an old password-only attempt exempt.

## Delivery and profile settings

Use only `User.email`, with `exclusive_recipients: true` and explicit empty
CC/BCC. Role/template recipients must never receive the code. Authentication
mail is independent of optional notifications and the new-login notification
switch. Validate a single usable primary mailbox when enabling. Do not send an initial mailbox confirmation when enabling the setting.

Use the existing mail queue and normal administrator-only mail history and
transaction inspection, retaining complete verification messages as explicitly
chosen by the user. Do not add code values to request or diagnostic logs.
Delivery delay never extends validity. Missing templates or queue failures
never permit password-only completion; failed resends preserve the old code.

Suggested profile label: "Verify new devices by email".

Suggested help: "When two-factor authentication is off, signing in from an
unknown device also requires a code sent to your primary email address. This
starts after your first successful device login. Known devices can sign in as
usual."

Show the masked address, effective status while MFA is active, and known-device
management. Preference changes require an authenticated session, owner/admin
authorization, CSRF protection, and password reauthentication; administrator
recovery overrides must be explicit and audited. Pending logins cannot change
settings. Invalidate challenges after password/email changes, account
restrictions, and relevant authentication-setting changes.

Preserve the preference through password recovery. Recovery already proves
mailbox access and returns to login; the following password login evaluates
this policy normally. Keep recovery and login credentials separate and preserve
recovery's existing MFA requirements. Lost mailbox access uses a known device,
existing trusted session, or the existing support process; no password-only
recovery shortcut is added to the challenge page.

## Other authentication paths

- OAuth2/WebUI: the Ruby API renders the new code step; PHP handles the profile
  setting and its help/status.
- New password-based token issuance: return `complete: false` and
  `next_action: email_code`; add verification/resend actions. These callers
  currently lack trusted browser-device proof, so opted-in accounts with
  successful device history need email for each fresh password login.
- HTTP Basic: reject when the email policy applies and direct the caller to
  OAuth2 or interactive token authentication. Never send a code on each Basic
  request. Leaving Basic unchanged would permit a password-only bypass.
- Existing sessions, supplied tokens, refresh tokens, and authenticated SSO
  retain their existing behavior. SSO still needs valid device proof, and an
  unfinished challenge cannot create it.
- Verify CLI callbacks, description caching, and Terraform/unattended clients.
  Consumers that cannot answer the new action must fail clearly or use an
  already provisioned token. Never fall back silently to password-only login.

## Compatibility and deployment

Use additive core migrations from the exact preceding schema: default-off user
column, rate-limit table/indices, and appended purpose. Do not add guards for
stale disposable databases. Existing device cookies, MFA settings, session
tokens, API resources, recovery state, and node formats remain compatible.

Deploy schema/templates first, then all API authentication workers. Allow opt-in and expose the profile setting only after every
password entry point enforces the policy. Old workers would ignore the setting;
mixed enforcement after opt-in is unsafe. Add a default-off enrollment availability gate controlling new opt-ins only;
already enabled accounts remain enforced regardless of this gate.

Older code may read the additive schema but cannot preserve email enforcement.
For downgrade, drain/invalidate pending challenges and explicitly accept loss
of enforcement; otherwise retain the enforcing version. Keep additive schema
for application rollback. No coordinated update of vpsAdminOS nodes is needed
for this policy. Token-login behavior can affect consumers even though no
Terraform resource schema or daemon protocol changes.

Follow `vpsfree-kb-contracts/docs/webui-change-workflow.md` for bilingual
documentation/captures and local release candidates. Production KB promotion
retains its direct-approval requirement.

## Testing plan

- Policy matrix: opt-in/out, effective/disabled MFA, confirmed/pending TOTP,
  passkeys, absent/successful device history, known/unknown/foreign token,
  expiry, revocation, and retained historical device rows.
- No mail for invalid passwords/ineligible accounts; no authenticated state
  after wrong, expired, exhausted, replayed, foreign-flow, or undelivered codes.
- Concurrency: verification, resend, attempts, first successful login,
  revocation, email/password/MFA changes, and forced password changes.
  One challenge cannot mint two independent authorizations.
- Shared rate budgets across workers and new challenges; exclusive recipient
  handling; existing admin-only mail-history access; no extra diagnostic leaks.
- Token/Basic bypass cases, client callback compatibility, unattended failure,
  SSO/refresh continuity, and password-recovery regression.
- Profile authorization/reauthentication/CSRF; browser tests for code entry,
  retry, resend, expiry, completion, known-device reuse, and Czech/English UI.
- Additive migration and rollout checks. Run quick API/PHP verification,
  commit implementation, then mandatory change review with xhigh review agents
  before long integration tests. Update spec topic coverage/CI selectors.

## Security positioning

Email verification adds a barrier when a stolen password has not also exposed
the mailbox. It remains susceptible to mailbox compromise and phishing, as
described in [OWASP's email authentication guidance](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html#email).
Keep active TOTP/passkey requirements authoritative. This feature makes no NIST
MFA assurance claim: [NIST SP 800-63B-4](https://pages.nist.gov/800-63-4/sp800-63b/authenticators/#out-of-band)
does not permit email as an out-of-band authenticator in that model.

## Locked implementation defaults

- Per challenge: 30 minutes from creation, five wrong guesses, 60-second resend
  cooldown, three total sends, at most three active challenges per account.
- Per account: five sends/15 minutes, 20 sends/day, ten wrong guesses/15 minutes.
- Per trusted source IP: 60 sends and 100 wrong guesses/15 minutes.
- Fixed UTC database-backed buckets; atomic cross-worker updates and cleanup.
- Email auth token and browser binding share the original 30-minute deadline.
  Resend changes neither that deadline nor the failure count. After email
  verification, forced password changes receive a fresh five-minute token and
  renew the browser binding so a late verification can finish the reset.
- Token actions: `email_code` with protected string `code`, and `email_resend`.
  Retain requested scope/lifetime. Basic rejects without sending mail.
- Self-service changes require current password including self-admin changes;
  another-account administrator override is explicit and audited.
- Tests cover 5/15 minutes, just before and exactly at 30 minutes, delayed
  messages, resend near expiry, and subsequent forced-reset validity.
- HaveAPI CLI already prompts for arbitrary steps. Terraform uses an existing
  supplied token. Validate these consumers without adding new protocols.

## Consumer compatibility clarification from implementation review

Terraform's provider accepts existing tokens. Its separate get-token utility
and pinned Go client only support TOTP/password reset and fail explicitly on
email_code. Members who opt in must use the Ruby HaveAPI CLI to issue tokens
for these consumers, or keep using a provisioned token. This is the explicit
unsupported-client boundary allowed above; generating and updating the Go
client/helper is separate work. Communicate this before enabling enrollment.

## Documentation delivery

Prepare and stage four public page candidates: Czech and English account
settings and API guides. The account pages cover opt-in, lifetime, known devices
and MFA precedence; the API guides cover token continuation, Basic refusal and
the supported CLI replacement for the Go helper. Preserve existing navigation
annotations and bilingual links. Pin the KB contract to the exact tested API
revision while retaining its deliberate newer vpsAdminOS test framework pin.

## Accepted email refinement follow-up

On 2026-09-14 the user approved rewriting the Czech password warning, removing
resend mechanics from both languages, matching the existing new-device mail's
service/time/device/IP/PTR layout, and adding verification-only HTML variants in
both template repositories. Suppress the new-device notification only after
successful email-code verification, including the forced-reset continuation;
password-only, TOTP and passkey notifications retain their behavior. Preserve
successful-session device trust timing and existing challenge limits.

Snapshot the initiating request's display metadata for resends. Add template
variables without removing old ones; use the existing user-agent formatter and
DNS helper. API workers must supply new variables before updated production
templates are installed; restore the earlier templates before rolling back any
API workers. Resolve PTR before taking account or budget locks, with an early
read-only budget check and the original locked budget check remaining
authoritative. This follow-up needs no schema or public auth API
change. Validate both renderings/languages, exclusive delivery, notification
suppression and the browser flow; run mandatory review before integration.
Prepare synthetic HTML previews and advance the KB contract's final API pin.
