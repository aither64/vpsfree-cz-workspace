# Scope and proportionality review

Reviewed with the mandatory-change-review scope lane at `gpt-5.6-sol` / `xhigh`:

- `vpsadmin` `791ab3aa89e2f613979da6090b89785c78245db5..c3a9ab01f3fea2f28a22394353d9bbd3e87bac37`
  (`2b5ba9d46` and the amended `c3a9ab01f`)
- `vpsfree-notification-templates`
  `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..06f03bad4294b6f28ca9478e907f43967ebeb7d0`

The uncommitted SSO remediation and the separate downstream documentation phase
were excluded. I inspected both commit series, repository guidance, the review
packet, plan/state, implementation, tests, templates, rollout documentation, and
the small HTTPS browser-test correction in `c3a9ab01f`.

## Blocking

1. **An SSO proof bypasses the required current-device recheck after a device is
   revoked.** In `2b5ba9d46`,
   `api/lib/vpsadmin/api/authentication/oauth2_config.rb:1002-1006` constructs an
   `sso` proof before calling `EmailLogin.check_authority!`. That method reloads
   the device through `required?`, but
   `api/lib/vpsadmin/api/email_login.rb:65-66` accepts `sso` whenever email
   verification is now required. A request can therefore read a usable SSO and
   device cookie, lose the user lock to a concurrent `UserDevice#close`, then
   acquire the lock and mint an authorization despite the device having been
   revoked. This violates the explicit boundary that SSO retains its flow only
   with valid device proof and that revocation is rechecked under the user lock.
   The committed code needs to require the reloaded usable known device for the
   SSO path rather than treating SSO itself as replacement evidence.

## Important

None.

## Advisory

1. **MFA label-only edits invalidate unrelated pending authentication.** The
   unconditional call at
   `api/lib/vpsadmin/api/operations/authentication/mfa_factor_change.rb:23-24`
   also runs for `TotpDevice::Update` and `WebauthnCredential::Update`, including
   changes that only rename a factor. For opted-in users it advances the global
   authentication generation and destroys all auth tokens and uncompleted OAuth
   authorizations through `User#invalidate_pending_email_logins!`
   (`api/models/user.rb:289-310`). Renaming a passkey in one session can therefore
   cancel an unrelated MFA, forced-password-reset, or authorization-code flow in
   another browser even though factor authority did not change. Limit this call
   to changes that alter effective authentication authority (confirmation,
   enablement, creation, or deletion); label-only changes are outside the stated
   invalidation contract.

2. **The API-spec topic glob was expanded into a redundant closed list.** In
   `.github/workflows/api-specs.yml:115-121`, `2b5ba9d46` replaces
   `spec/lib/**/*_spec.rb` with five namespace-specific patterns. Both forms
   select the same 21 committed files, and the new email-login spec was already
   covered by the original glob. The replacement adds no feature coverage and
   makes a future `spec/lib` namespace fail topic coverage until this list is
   extended. Retaining the existing wildcard is the smaller, more durable
   change.

## Proportionality assessment and residual gaps

Apart from the findings above, the implementation is proportionate to the
accepted high-risk contract. The database-backed fixed buckets, browser and
OAuth context binding, persisted authorization proof, generation checks,
enrollment gate, bilingual built-in/production templates, and focused unit plus
browser coverage each have a current consumer or a concrete security/deployment
requirement. The commit split is coherent: API enforcement and its schema/tests
are together, profile UI and its browser scenario are separate, and production
template ownership remains in its own repository. The HTTPS test certificate is
the minimum support needed to exercise production `Secure` cookies in the
browser scenario.

Long integration/browser execution remains the principal test gap, as intended
by review ordering. The separate KB candidate/pin/release work still requires
its own committed review. No production template scope issue was found.
