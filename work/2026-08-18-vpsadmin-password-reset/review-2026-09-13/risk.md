# Risk and compatibility review

Reviewer: fresh risk-and-compatibility lane. I reviewed the complete committed
series and final behavior across all four repositories directly. I did not
launch nested agents, mutate a project or service, install dependencies, or run
integration tests.

## Findings

### Blocking

1. **Generation-less authentication tokens issued by the predecessor remain
   valid after a password change across the supported cutover.** Commit
   `2a844e772929c5098856905b1c287a2538b4ef77` makes a missing token generation
   read as `0` at
   `vpsadmin/api/models/auth_token.rb:20-25`, while its migration initializes
   every existing user to generation `0` at
   `vpsadmin/api/db/migrate/20260818115900_add_authentication_generation.rb:3-5`.
   The exact predecessor issued five-minute MFA and forced-reset `AuthToken`
   records without an `authentication_generation` option at
   `61d2ef6e712345200daddff3abcb4697c028d176:api/lib/vpsadmin/api/operations/authentication/password.rb:81-108`,
   and its password setter did not advance a generation or destroy those
   tokens at
   `61d2ef6e712345200daddff3abcb4697c028d176:api/models/user.rb:158-170`.
   The rollout added by `ad6c41ea295ee6ae45b2fd2f9c806bf74f2a1f9e`
   stops the final old writer and immediately starts the new API at
   `vpsfree-cz-configuration/docs/operations/vpsadmin-password-recovery-deployment.md:186-224`;
   it neither drains nor revokes pending legacy tokens. Its later maintenance
   step at lines 246-258 invokes code that removes only expired tokens
   (`vpsadmin/api/lib/vpsadmin/api/tasks/authentication.rb:10-24`).

   The concrete trigger is an old API issuing an MFA or reset token, followed by
   an old-writer password change and cutover before the token's five-minute
   expiry. The new generation check compares the token's synthesized `0` with
   the migrated user's `0` and accepts stale authority. A stale reset token can
   replace the intervening password; a stale MFA token can complete login. The
   coordinator's isolated test-database characterization reproduced the reset
   case: the generation-less token survived a predecessor-style password update
   and the new `ResetPassword` operation overwrote that password, while an
   equivalent token was rejected after a new-writer password change.

   Reject every token that lacks an explicit `authentication_generation` once
   the new API is active, and add a regression for a legacy `opts == nil` or
   missing-key token. An operational alternative is an explicit post-old-writer
   barrier that destroys all `AuthToken` rows and their backing tokens, verifies
   zero remain, and only then starts the first new API. That invalidates pending
   login/reset attempts while preserving established `UserSession` records.

### Important

1. **HTTP Basic transparent hash upgrades omit the request-backed audit
   snapshot.** Commit `6a1cf297f1b81a945043fde70570a09db807284e`
   made a sessionless hash upgrade use request metadata at
   `vpsadmin/api/lib/vpsadmin/api/operations/authentication/password.rb:56-71`,
   but the Basic provider still calls this operation without `request:` at
   `vpsadmin/api/lib/vpsadmin/api/authentication/basic.rb:7-11`. When Basic
   authentication matches an old password provider, `UserSession.current` and
   the operation's request are both nil, so the new immutable
   `PasswordChangeLog` row is written without session, IP, PTR, or user-agent
   attribution. The Basic session holding that data is created only afterward
   at `basic.rb:38-42`. Token and OAuth callers pass the request, so this is a
   caller-specific compatibility hole in the new audit contract. The isolated
   characterization confirmed a null audit snapshot alongside a Basic session
   containing the request's client address. Pass `request:` to `Password.run`
   and add a provider-level old-hash regression that checks the persisted
   snapshot.

2. **Passkey recovery persists an unbounded public User-Agent in a 255-character
   column and reports the database rejection as an MFA error.** Commit
   `2639ac721e4366e62744a608b4c0ffe86a8720a5` copies
   `@request.user_agent.to_s` into `WebauthnChallenge.client_version` at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.rb:488-501`.
   The existing column is limited to 255 characters at
   `vpsadmin/api/db/migrate/20250213133759_add_webauthn.rb:16-27`. A legitimate
   passkey-only recovery with a longer header therefore cannot create its
   challenge. The method-wide `rescue StandardError` at
   `password_recovery.rb:290-292` converts `ActiveRecord::ValueTooLong`, as well
   as unrelated persistence failures in the transaction, into the ordinary
   HTTP 422 passkey-start response. An isolated route characterization returned
   HTTP 200 for a short header and reproduced `ActiveRecord::ValueTooLong` plus
   HTTP 422 for 256 ASCII characters. Normalize `client_version` to the schema
   limit before persistence, narrow the rescue to expected WebAuthn option
   errors, and cover both a long header and an unexpected persistence failure.

3. **The MailLog protocol description still declares `user` non-null although
   this series starts returning null.** Commit
   `6f45ee44c50bd92389513c6366dd7793729bd1e3` makes the model association
   optional at `vpsadmin/api/models/mail_log.rb:1-4`, and recovery deliberately
   creates account-neutral mail logs without a user; the committed route test
   asserts the resulting null at
   `vpsadmin/api/spec/api/resources/mail_log_spec.rb:254-258`. The resource
   declaration at `vpsadmin/api/lib/vpsadmin/api/resources/mail_log.rb:6-23`
   still lacks `nullable: true`. HaveAPI therefore describes `user` as
   non-null in both Index and Show even though those actions serialize null.
   Schema-driven consumers receive a false contract and can generate a
   non-null representation that fails on the first recovery mail. The current
   generated Go client uses a pointer for resource outputs and therefore
   tolerates JSON null, so I found no concrete break in that consumer;
   this limits the immediate blast radius but does not repair the published
   contract. Add `nullable: true`, assert the Index/Show metadata as well as the
   payload, and regenerate or verify consumers against the corrected
   description.

### Advisory

1. **Retention cleanup can delete a submission currently held by the worker and
   make the worker escape its own recovery path.** Commit
   `eaad07112044bcac21db0a518c6000a52cd0a45a` deletes every unfinished
   submission older than one day under the queue lock at
   `vpsadmin/api/models/password_recovery_submission.rb:132-138`; it does not
   exclude a row with a recent `processing_started_at`. The worker introduced
   by `6f45ee44c50bd92389513c6366dd7793729bd1e3` releases the queue lock after
   claiming, performs the request, and only then calls `finish!` at
   `vpsadmin/api/lib/vpsadmin/api/password_recovery_worker.rb:37-56`. If an old
   backlog row is claimed while the five-minute cleanup timer runs, cleanup can
   wait for the request transaction's row lock and then delete the row before
   `finish!`. `finish!` raises `ActiveRecord::RecordNotFound`; the rescue at
   lines 57-60 calls `retry_or_finish!` on the same missing row, which raises
   again outside that rescue and terminates the loop. Systemd restarts the
   service after 30 seconds at
   `vpsadmin/nixos/modules/vpsadmin/api/default.nix:298-311`, so this is a
   self-healing availability fault rather than lost authentication authority.
   Exclude recently claimed rows from retention cleanup and make finalization
   idempotent when cleanup has already removed a row; add a cleanup-versus-
   processing concurrency regression.

## Coverage

I inspected the exact committed ranges:

- `vpsadmin`
  `61d2ef6e712345200daddff3abcb4697c028d176..a2e6d8037c737c61c15bfd845c1b3c57d894f310`
- `vpsfree-mail-templates`
  `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676..f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`
- `vpsfree-kb-contracts`
  `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8..6d8ab17db3ce8ffc41216feeb90bff8468b4d39d`
- `vpsfree-cz-configuration`
  `b4e120294696578c3871124259f266205bad4393..8928b2aba9230202e805aa5489dc9f7369650ac7`

The risk trace covered all five additive migrations and their destructive-down
boundary; old/new writer compatibility; authentication generation, MFA and
reset tokens; all session-publication paths; recovery token digestion and
expiry; CSRF/cookie and redirect behavior; factor, role, client-deletion and
lifecycle revocation; queue admission, claim, retry and retention; owner/admin
audit isolation; built-in and external mail contracts; Nix services, proxy and
monitoring; and executable rollout/rollback ordering.

The production configuration pins `vpsadminServices` exactly to
`a2e6d8037c737c61c15bfd845c1b3c57d894f310` and templates exactly to
`f944ba03eba5d0d6b58b7eb856f251d1c96f2c11` at
`vpsfree-cz-configuration/flake.lock:1194-1209,1389-1401`; the template input
follows that vpsAdmin source at `flake.nix:47-50`. The KB flake, contract,
navigation, and captures pin the same vpsAdmin head while retaining the
independent vpsAdminOS revision
`6bdf458fd9105379860234ff33d352e55844f08f`. I found no pin mismatch or node
protocol change.

## Residual gaps

Completed hard-deleted and deleted users are excluded by
`User.including_deleted`; I withdrew the initial concern that retained
hard-delete rows alone could put a nil login into shared-email sorting. Static
chain ordering leaves a very narrow unmeasured interval between the hard-delete
node that clears the login and the following node that publishes the materialized
hard-delete state. The requested hard-delete log already makes the policy deny
authority, but shared-email sorting occurs before that policy call. I found no
evidence of this interleaving in tests or runtime data and do not elevate it
above a residual concurrency gap.

No new test was run in this lane. I used the coordinator's isolated
characterizations described in the findings and the supplied verification:
the quick selector passes 16 tests / 55 assertions, the external-template check
passes 71 templates / 349 files, all current-head workflows pass, and the exact
vpsAdmin head's full integration log reports 118 successful tests. These suites
do not cover legacy generation-less tokens, Basic-provider hash-upgrade
attribution, a 256-character recovery User-Agent, MailLog metadata nullability,
or cleanup racing a claimed stale submission. The earlier one-off
metrics-token HTTP 500 remains unexplained, although it did not recur in narrow
checks or the identical full order.
