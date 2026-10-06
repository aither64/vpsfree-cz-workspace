# Bounded risk follow-up

Reviewed only the public `User::Create` password boundary and shared ordinary /
recovery WebAuthn metadata boundary added after the first remediation snapshot.
The exact committed heads were vpsadmin
`6c08f8aa6df5099313c7cae799ba75e004be0c34` and configuration
`00a81e8e68df0b5a4baccdc972cb4857b03a3ed5`. The final vpsadmin tree is exactly
the tested pre-autosquash tree `6e7cabba3ccf701f5bf7ad1dfd8af793fd105951`,
and the configuration pin resolves to that API head.

## Findings

### Blocking

None.

### Important

1. **The new test and deployment contract say an omitted User Create password
   is generated, but the action creates an account with password login
   disabled.** `User::Create` calls `set_password` only when the optional input
   is present at `api/lib/vpsadmin/api/resources/user.rb:140-152`. With no
   supplied password, `TransactionChains::User::Create` immediately saves the
   model (`api/models/transaction_chains/user/create.rb:6-8`) and the
   `before_validation` callback stores the literal disabled-password marker
   `!` (`api/models/user.rb:48,413-415`). No generator runs, `password_plain`
   remains nil, and the account-creation mail therefore omits a temporary
   password (`api/notification_templates/templates/user_create/email/en.text.erb:5-10`).

   The regression at `api/spec/api/resources/user_write_spec.rb:298-303`
   checks only that the database password is present, which the `!` marker
   satisfies. The deployment guide then tells provisioning operators that
   omitting the password still generates one at
   `docs/operations/vpsadmin-password-recovery-deployment.md:85-88`. An
   operator relying on that statement creates an account that cannot use
   password authentication and receives no generated secret. Preserve the
   longstanding disabled-password behavior, change the compatibility text to
   describe it, and make the regression assert the `!` marker and absence of
   plaintext rather than describing or accepting it as generation. The
   coordinator accepted this correction during the follow-up.

### Advisory

None.

## Closed findings

- The explicitly supplied User Create password now passes through
  `PasswordChanges.valid_length?` before user construction
  (`api/lib/vpsadmin/api/resources/user.rb:143-149`). The regression changes
  the shared constant, rejects one character below it without creating a user,
  and accepts the boundary value (`api/spec/api/resources/user_write_spec.rb:280-296`).
  This closes the public metadata/enforcement mismatch. Existing accounts are
  untouched; after upgrade, provisioning clients that send short initial
  passwords receive the documented field error. Rollback restores the
  predecessor's acceptance behavior without a state-format change.
- `WebauthnChallenge.normalize_client_version` now owns invalid-byte
  replacement, utf8mb3 supplementary-character replacement, and truncation to
  the live column limit (`api/models/webauthn_challenge.rb:9-14`). The only two
  application challenge writers call it: recovery at
  `api/lib/vpsadmin/api/authentication/password_recovery.rb:491-504` and the
  ordinary registration/authentication factory at
  `api/lib/vpsadmin/api/resources/webauthn.rb:13-35`. The ordinary factory also
  uses the normalized value for `UserAgent`, so raw malformed or oversized
  browser data no longer reaches either utf8mb3 insert. Recovery retains its
  deliberately generic user-agent dictionary row while storing the normalized
  browser snapshot in `client_version`.
- The route regressions cover 255 and 256 ASCII characters, 256 three-byte BMP
  characters, and a supplementary plus invalid byte for recovery and ordinary
  authentication. Ordinary registration uses the same factory and its normal
  success path remains covered. The narrow recovery `WebAuthn::Error` boundary
  and propagation of an unexpected storage failure remain intact.
- Ordinary WebAuthn examples now use the canonical generation-stamped
  `create_auth_token!` helper. Their positive flow exercises valid authority
  again, while expiry and lifecycle examples reach their intended rejection
  conditions.

## Residual gaps

- The four ordinary metadata examples are placed under the registration
  context but issue authentication-begin requests. Both actions currently use
  the exact same `create_challenge!` factory, and the ordinary registration
  success example traverses that factory, so I found no current behavior gap;
  a future split between the actions would reduce the direct boundary
  coverage.
- I relied on the supplied passing 74-example focused run, six-file RuboCop
  run, 87 configuration specs, and strict MkDocs result. I did not repeat those
  checks or run long integration, deployment, or lifecycle commands. The queue
  interleaving and rollback-consumer evidence gaps recorded in `risk.md` are
  unchanged and outside this bounded follow-up.
