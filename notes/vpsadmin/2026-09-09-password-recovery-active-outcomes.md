# PasswordRecovery.active includes informational outcomes

A live recovery probe after completing one account from a shared-address mail
found `PasswordRecovery.active.count == 1`, even though the completed account
had no remaining recovery authority.

The scope filters only completion and invalidation timestamps. The request
operation also persists `no_mfa` outcomes for accounts mentioned in the grouped
mail; these have neither email nor session tokens. Both usability predicates
require the `recoverable` outcome.

To check for outstanding authority, inspect `active.recoverable` and the token
usability predicates. Check informational rows separately for their expected
outcome and absent token digests; do not delete them merely to make a global
active-row count zero. Inspect token presence as booleans without logging the
values.

Verified against vpsAdmin `9f30c1fe0`: the completed MFA account had no active
recovery, the non-MFA account retained one tokenless informational row, and the
submission queue was empty. Related initiative:
`work/2026-08-18-vpsadmin-password-reset/`.
