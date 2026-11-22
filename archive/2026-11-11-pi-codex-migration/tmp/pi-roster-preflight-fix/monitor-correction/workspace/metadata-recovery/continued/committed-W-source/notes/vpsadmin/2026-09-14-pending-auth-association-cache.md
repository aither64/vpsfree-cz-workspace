# Reload pending authentication before invalidating it

Initiative: `work/2026-09-13-auth-email/`.

The API engine CI topic found that a password-recovery security change could
leave a pending `AuthToken` alive. An earlier invalidation had loaded
`User.auth_tokens` as empty; a later token created through another object was
absent from that cached collection. Calling `destroy_all` on the association
then skipped it. Reload the association before destroying its pending tokens.

The password-recovery model regression reproduces the sequence. The combined
recovery, email challenge, and rate-limit suite passed 62 examples after the
fix. Preserve completed sessions separately from pending authentication when
checking password changes that do not request signing out other devices.

The same CI run exposed shared-budget specs assuming an empty rate-limit table.
Independent-connection examples can retain rows outside RSpec's transaction.
Isolate the table for those examples before asserting global counts or `.sole`;
explicitly clean independently committed rows in their owning test's ensure.
