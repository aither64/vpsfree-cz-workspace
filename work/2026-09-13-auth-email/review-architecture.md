# Architecture and repetition review

Reviewed committed ranges:

- `vpsadmin` `791ab3aa89e2f613979da6090b89785c78245db5..3c24a6aadacb054732a2a22214c98e3edb03ef5c`
- `vpsfree-notification-templates` `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..06f03bad4294b6f28ca9478e907f43967ebeb7d0`

No Blocking findings.

## Important

### 1. The consumer inventory misses the repository's official password-based token helper

The new API deliberately returns `next_action: email_code` from password token
issuance (`vpsadmin` commit `2b5ba9d46`,
`api/lib/vpsadmin/api/authentication/token_config.rb:29-45`). The review packet
concludes that `terraform-provider-vpsadmin` only consumes a supplied token, but
that repository also builds and documents an interactive `get-token` program:

- `terraform-provider-vpsadmin` commit
  `8e205a3b4b87160a42e69de63c28653d226e65c2`, `get-token/main.go:144-159`,
  calls `SetNewTokenAuth` with a username, password, and only a TOTP callback.
- Its `get-token/go.mod:6` pins `vpsadmin-go-client` commit
  `1d9240f3d27b5831baf3694baab5fe06294875d8`.
- That generated client's `client/auth_token.go:41-49,99-167` knows only
  `reset_password` and `totp`; any `email_code` response ends with
  `Unsupported authentication action 'email_code'`.
- `get-token/README.md:1-3,28-43` presents this as the helper for obtaining the
  token required by the Terraform provider. It has no supplied-token mode that
  could serve as a fallback for its own operation.

An opted-in member with known-device history therefore cannot use the shipped
helper for its sole purpose. The failure is explicit rather than a password-only
bypass, but this is still a broken real consumer of the changed cross-project
contract. Add `vpsadmin-go-client` and `terraform-provider-vpsadmin` to the
affected consumer set, regenerate the Go client against the reviewed API, and
teach `get-token` to prompt for the email code with focused coverage. If that
work is intentionally deferred, record the incompatibility and the supported
replacement workflow before opening enrollment.

### 2. The two new public User parameters omit descriptions for non-obvious policy

`vpsadmin` commit `2b5ba9d46`,
`api/lib/vpsadmin/api/resources/user.rb:28,51`, declares
`enable_new_device_email_verification` and
`new_device_email_verification_available` with labels only. The generated
English and Czech metadata likewise has no descriptions
(`api/lib/vpsadmin/api/locales/{en,cs}.yml`, keys at approximately lines
602 and 1192).

Neither field's meaning is captured by its label. The preference applies only
without effective MFA, starts after successful device history, and remains
stored while MFA takes precedence. The availability field controls new opt-ins
but deliberately does not disable enforcement for accounts already opted in.
API-description consumers and administrators therefore cannot discover the
security and rollout semantics from the public contract and can plausibly
interpret the availability flag as an enforcement switch. Add useful source
descriptions and localized metadata for both fields.

## Advisory

### 3. WebUI recomputes the API-owned effective-MFA rule

The API now owns the authoritative predicate in
`api/models/user.rb:275-279`, including the requirement that TOTP be both
enabled and confirmed. The profile page independently derives the displayed
email-verification status from `hasTotpEnabled()` and `hasWebAuthnEnabled()`
(`webui/pages/page_adminm.php:288-289,335-337`; helpers in
`webui/lib/functions.lib.php:1679-1698`). The current factor implementations
keep these expressions equivalent, so this is not an enforcement bypass.
However, a new factor type or a change in factor usability can make WebUI say
that MFA takes precedence while the API still requires email, or say email is
active when the API suppresses it. Expose the effective status from the owning
API policy and render that value instead of repeating the factor catalog in
PHP.

### 4. Unknown challenge-flow names silently acquire token-flow semantics

`api/lib/vpsadmin/api/email_login.rb:191-196` selects OAuth policy only when
`flow == 'oauth2'` and treats every other value as token authentication. The
module's callers currently store only `oauth2` and `token`, but the serialized
context is an implicit interface with no central validation. A typo or future
third password flow can consequently check the wrong login-method flag and be
accepted as a token challenge. Validate the finite flow values explicitly (and
reject an unknown value) at the `EmailLogin` boundary.

## Residual risks and validation gaps

- The built-in and production templates currently use the same variable set
  and fixed 30-minute wording; their differences are the expected sender and
  branding overrides. The production repository's standalone flake pins
  vpsAdmin `9fc0648accd414246d6422e67106ae7217486020`, whose checker validates the
  template DSL and files rather than the new runtime variable registry. The
  deployed configuration does make the notification-template input follow
  `vpsadminServices`, so the planned integration with the feature pin remains
  the representative end-to-end check.
- The generic Ruby HaveAPI CLI and the PHP client at WebUI's actual pinned
  revision `27da6934f0497501187f77d14b566469dd4a7e14` discover arbitrary
  continuation actions from API metadata. No compatibility issue was found in
  those consumers.
- Long integration/browser tests and the separately scoped KB exact-pin work
  were intentionally not part of this lane. Changes made after the stated
  heads, including the pending HTTPS browser-fixture correction reported by the
  coordinator, were not reviewed here.
