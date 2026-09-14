# General review: email refinement follow-up

Reviewed vpsAdmin commits `95a67e55e9695b5a7f56b491af186840c389f444`
and `d6f51b6e8ad9d78c68e6d0f0ce5276ca610e7bf8` against base
`cf2c8734c9091327cbc9157d43915695e9750bc5`, and production-template commit
`97ac666a390fc028c5b610b48c9963adb9e0b4ef` against base
`06f03bad4294b6f28ca9478e907f43967ebeb7d0`.

## Findings

### Important: reverse DNS runs under the account lock before send limits reject the request

Commit `95a67e55e9695b5a7f56b491af186840c389f444` adds the synchronous
`get_ptr(client_ip_addr)` call inside `user.with_lock` and before
`EmailLoginRateLimit.with_limits` in
`api/lib/vpsadmin/api/email_login.rb:75-88`. A request that is already over its
account or IP send budget therefore still performs network I/O while holding
the user's database row lock. The three-pending-challenge cap does not fully
bound this path: an OAuth client that has the password and its own challenge
token/browser binding can cancel the pending challenge through
`api/lib/vpsadmin/api/authentication/oauth2_config.rb:165-175`, then repeat the
credentials request. A slow or failing PTR lookup can consequently delay
security-setting changes and other operations that lock the same user even
though no further verification mail is allowed. This matters particularly
because the feature's threat model includes an actor who knows the password.

Avoid holding the user row lock across PTR resolution and avoid resolving on
requests that an inexpensive preliminary check can already identify as rate
limited. Keep the existing locked rate-limit check authoritative before
creating the challenge, so moving or splitting the lookup does not weaken the
shared budgets. Add a focused example proving that a rejected send does not
invoke the resolver, or record an explicit decision accepting this residual
account-level availability risk.

## Other review results

No other general-lane findings. The three commits have distinct logical
purposes and clean messages. The stored service, request time, readable device,
client address and PTR are used consistently across resends; old template
variables remain available; HTML dynamic values are escaped; built-in and
production prose differ only in the expected sender/team identity; and the
notification suppression is limited to persisted `email` evidence after the
existing authorization checks. Focused tests cover normal and forced-reset
completion, password/device and MFA notice retention, initiating-request
metadata, unknown-agent escaping, missing PTR, and the browser mail count.

Residual test gap: the reverse-DNS lock/rate-limit ordering described above is
not exercised by the focused suite. I did not run long integration tests as
requested.
