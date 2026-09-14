# General review

Reviewed the complete committed ranges:

- `vpsadmin` `791ab3aa89e2f613979da6090b89785c78245db5..3c24a6aadacb054732a2a22214c98e3edb03ef5c`
- `vpsfree-notification-templates` `f944ba03eba5d0d6b58b7eb856f251d1c96f2c11..06f03bad4294b6f28ca9478e907f43967ebeb7d0`

The review covers the full commit series and final trees against the acceptance contract in `review-packet.md` and `plan.md`. Downstream KB pinning and release preparation are outside this review.

## Findings

### Blocking

1. **SSO evidence bypasses the final usable-device check after revocation or expiry.** In `api/lib/vpsadmin/api/authentication/oauth2_config.rb:1002-1006`, an SSO authorization without email proof is assigned `EmailLogin.proof(..., 'sso')`, without the device identity. `api/lib/vpsadmin/api/email_login.rb:57-68` correctly recomputes whether email verification is currently required, but line 66 then accepts `sso` evidence unconditionally whenever it is required. Consequently, an opted-in user can start SSO with a valid known-device cookie, receive an authorization code, have that device revoked or expire before token exchange, and still receive a session at `oauth2_config.rb:238-250`; the exchange recheck sees that the device is no longer usable but treats the stored `sso` method as sufficient authority. This violates the required usable known-device proof and the revocation-race recheck. Record the actual device proof, including `device_id`, for successful SSO and subject it to the same final `known_device?` check as password login. Add successful SSO and revoke/expire-before-exchange regressions. Commit: `2b5ba9d46`.

2. **The API feature commit bundles an independent CI discovery-policy change.** Commit `2b5ba9d46` changes `.github/workflows/api-specs.yml:117` from the existing recursive `spec/lib/**/*_spec.rb` platform pattern to an allowlist of five namespaces. The new email-login specs were already covered by the recursive pattern, and neither the commit message nor the review packet explains why changing repository-wide future spec discovery is indivisible from email authentication. This can exclude a future `spec/lib` namespace until the allowlist is updated and is independently reviewable CI maintenance. Restore the existing recursive pattern or move the change to a dedicated commit with its own rationale and validation.

### Important

3. **The committed browser regression cannot retain the new challenge cookie.** `tests/playwright/webui/specs/auth.spec.cjs:18,456-507` runs the fresh browser on the HTTP WebUI/auth setup, while `api/lib/vpsadmin/api/authentication/oauth2_config.rb:639-641` deliberately marks `vpsadmin_email_login` as `Secure`. The committed test environment also has `forceSSL = false` and an HTTP trusted auth origin (`tests/configs/nixos/vpsadmin-services.nix:609-624,329-335`). Chromium discards that cookie on the HTTP auth origin. The initial credential response can display the email-code form, but the resend/verify POST has no browser binding and expires the flow instead of exercising cooldown, wrong-code, and completion behavior. Configure test-only HTTPS for the auth origin and make this scenario use it, while retaining the production `Secure` policy.

4. **The shared rate-limit contract and its concurrency behavior lack focused coverage.** `api/models/email_login_rate_limit.rb:5-23` implements the account 5/15-minute and 20/day send buckets, account 10/15-minute failure bucket, IP 60-send and 100-failure buckets, fixed UTC windows, row creation, locking, and consumption. The relevant tests cover only the per-challenge three-send budget (`api/spec/lib/vpsadmin/api/email_login_spec.rb:97-107`), the account ten-guess limit (`:116-123`), and concurrent single-use challenge consumption (`api/spec/models/operations/authentication/email_login_concurrency_spec.rb:5-38`). There is no focused assertion for either account send bucket, either IP bucket, UTC-window rollover, or concurrent shared-bucket consumption from independent connections. An off-by-one, wrong scope/key, rollover error, or lost update in these security controls would pass the current suite. Add boundary and rollover examples for every configured budget plus an independent-connection regression that consumes the same shared bucket.

### Advisory

None.

## Other observations

The two feature commits otherwise form a sensible API-then-WebUI series, and their subjects satisfy the repository commit format. The additive schema, default-off rollout, authentication-generation checks, fixed challenge expiry, resend rotation, pending limit, Basic/token handling, preference authorization, bilingual UI/catalog changes, and built-in templates align with the stated behavior in the paths inspected. The production English and Czech template changes preserve the expected variables and 30-minute wording; I found no production-template-specific issue.

Quick unit, lint, template, selector, and migration results recorded in the packet are appropriate pre-review evidence. Long browser/integration execution remains deferred by design. The plan asks for Czech and English browser coverage, while the committed end-to-end scenario selects only English; the generated Czech catalog and bilingual template checks reduce that residual localization risk but do not exercise the Czech browser flow.
