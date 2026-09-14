# Architecture and repetition review

Reviewed committed ranges:

- `vpsadmin` `cf2c8734c9091327cbc9157d43915695e9750bc5..d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8`
- `vpsfree-notification-templates` `06f03bad4294b6f28ca9478e907f43967ebeb7d0..97ac666a390fc028c5b610b48c9963adb9e0b4ef`

No Blocking findings.

## Important

### 1. Reverse DNS is performed while holding the account row lock, before rate-limit rejection

`vpsadmin` commit `95a67e55e9`,
`api/lib/vpsadmin/api/email_login.rb:75-88`, enters `user.with_lock` and then
calls `get_ptr` before consulting `EmailLoginRateLimit`. The resolver helper
performs a synchronous `Resolv#getname` and has no application-level time bound
(`api/lib/vpsadmin/api/operations/utils/dns.rb:5-8`). The rate limiter is
explicitly called under the same user lock and only obtains its bucket locks
after the lookup (`api/models/email_login_rate_limit.rb:3,16-23`).

A slow or unavailable resolver can therefore keep the user row locked for the
lookup timeout. Concurrent password/MFA login completion, device updates,
password or authentication-setting changes, and pending-authentication
invalidation for that account then wait behind unrelated presentation metadata.
Requests that have already exhausted a shared send budget still perform the
lookup while holding the row lock before they are rejected, so the rate limit
does not bound this lock-hold cost. A client with the correct password can keep
repeating that path even after the mail budget is exhausted.

Capture the initiating request address and resolve its PTR before entering
`user.with_lock`, then pass that immutable snapshot into the locked token
creation path. Keep the authentication-generation, account policy, pending
challenge count, budget locks, token creation, and delivery transaction inside
their current serialized boundary. This preserves the required initiating-login
snapshot without placing network I/O inside the account transaction.

## Residual risks and validation gaps

- The built-in and production verification templates intentionally remain
  separate provider/default and deployment-override implementations. Their
  variable references and visible plain-text/HTML content match at the reviewed
  heads, with only the expected branding and sender metadata differing. The
  synthetic parity check is an initiative artifact rather than a permanent
  cross-repository CI contract, so future mail-contract changes must continue to
  inventory and validate the production template consumer explicitly.
- `EmailLogin` owns production of the persisted `email` proof, and
  `NewOAuth2Login` consumes it only after the existing code-exchange authority
  check. Password/device and MFA evidence still take the notification branch,
  while device trust is updated after session creation. No conflicting proof
  producer or second unknown-device-notice path was found.
- The revised API continues to supply the old `user_agent` variable alongside
  the new flat mail variables, so old text templates remain compatible. The new
  production templates require the revised API producer; the documented
  API-workers-before-template deployment order remains necessary.
- Focused and synthetic checks reported in the packet were inspected. This lane
  did not run the long browser integration test.
