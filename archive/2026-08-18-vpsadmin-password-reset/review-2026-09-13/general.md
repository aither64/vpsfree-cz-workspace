# General review

Reviewer: fresh gpt-5.6-sol / xhigh, General lane. I reviewed the complete
committed series and final behavior in all four repositories directly. I did
not launch nested agents or run integration tests.

## Findings

### Blocking

No findings.

### Important

1. **HTTP Basic transparent hash upgrades lose the required client audit
   snapshot.** Commit `6a1cf297f1b81a945043fde70570a09db807284e`
   made `Operations::Authentication::Password` capture request metadata for a
   sessionless rehash, but the Basic provider still calls it without `request:`
   at `vpsadmin/api/lib/vpsadmin/api/authentication/basic.rb:7-11`. On an
   account whose password matches an old crypto provider, the rehash at
   `vpsadmin/api/lib/vpsadmin/api/operations/authentication/password.rb:56-71`
   therefore sees both `UserSession.current == nil` and `request == nil` and
   creates an `other` password-change row with no session, IP, PTR, or user
   agent. The closed Basic session is created only afterward at
   `basic.rb:38-42`. This is a real request-backed change, while the final plan
   permits empty snapshots only for maintenance changes with neither a session
   nor request. Token and OAuth password entry both pass the request. Pass the
   Basic request to `Password.run` and add a provider-level regression that
   forces an old hash and checks the persisted client snapshot. If the desired
   audit model also links the subsequently created Basic session, carry the
   recorded row to `NewBasicLogin` as the required-reset paths do; the request
   snapshot is the minimum required fix.

   The coordinator's isolated characterization reproduced this exact boundary:
   the rehash audit row had null IP, PTR, and user agent while the Basic session
   created from the same request had the expected client IP.

2. **Recovery passkey start writes an unbounded public User-Agent into a
   255-character column, then misclassifies the database failure as a proof
   error.** Commit `2639ac721e4366e62744a608b4c0ffe86a8720a5`
   stores `@request.user_agent.to_s` as `client_version` at
   `vpsadmin/api/lib/vpsadmin/api/authentication/password_recovery.rb:488-501`;
   the existing schema limits that field to 255 characters at
   `vpsadmin/api/db/migrate/20250213133759_add_webauthn.rb:16-27`.
   Commit `a636ece734ca98428e9e6ffbe0ed2b6f8501160c` describes the retained raw
   browser value as bounded but does not add a bound. A valid recovery flow
   with a passkey and a User-Agent longer than 255 ASCII characters fails while
   creating the challenge. The method-wide `rescue StandardError` at
   `password_recovery.rb:290-292` then returns the ordinary 422
   `passkey_start_failed` response, concealing this persistence error; it also
   conceals unrelated database failures from the whole eligibility/locking/
   challenge transaction. This contradicts the final decision to normalize
   only WebAuthn parser/verifier failures without hiding database failures.
   Bound and normalize `client_version` to its schema limit, narrow the rescue
   to expected WebAuthn option-generation errors, and add route regressions for
   a long User-Agent and a persistence exception.

   The coordinator's isolated route probe reproduced
   `ActiveRecord::ValueTooLong` for a 256-character User-Agent and the resulting
   HTTP 422; the short-User-Agent control returned HTTP 200.

3. **The unmerged commit series still records superseded schemas and
   same-series repair commits instead of introducing the final behavior
   directly.** `api/db/migrate/20260818120000_add_password_recovery.rb` is
   introduced by `6f45ee44c50bd92389513c6366dd7793729bd1e3`, then rewritten by
   `89eb40b45b3818991dc6ac0c106cad72bd61b8bd` to remove the superseded
   request-recipient digest and add the final submission ledger, by
   `ed4a646040840b71ee690e1d46c5dac5fd6bb9c8` for the interactive-client
   column, and by `2639ac721e4366e62744a608b4c0ffe86a8720a5` for factor
   snapshots. Likewise,
   `api/db/migrate/20260821210000_add_password_change_logs.rb` is introduced by
   `bd32e162892bd04665177731744115bcab6c403e` and rewritten by
   `6a1cf297f1b81a945043fde70570a09db807284e` for the final client and OAuth
   linkage. Two direct repair commits remain as well:
   `1fae19609a819aed3806ae7ffd124dc43087daab` adds the one CI selector entry
   omitted by `bd32e1628`, and
   `f15d19547ed299339e1809409be5322a154c563e` fixes the sessionless admin
   dereference introduced by the password-history WebUI sequence ending in
   `44c6144e8d2fe7109a524a7c6405eed941914c1e`. The current tree is coherent,
   but these commits preserve unreleased intermediate designs and make the
   migration-owning and WebUI commits misleading as independently reviewable
   units, contrary to the General lane's explicit final-schema and clean-series
   rules. Put each migration's final definition in its introducing commit,
   fold `1fae19609` into `bd32e1628`, and fold the `f15d19547` null-session fix
   and regression into `44c6144e8`. The later functional commits can remain
   separate without their migration hunks. Recreate the exact KB and
   configuration pin commits after the rewritten vpsAdmin head is stable.

### Advisory

1. **The retained password-history KB publication candidates describe an
   obsolete sessionless required-reset behavior.** The English candidate at
   `work/2026-08-18-vpsadmin-password-reset/kb-candidates-history/en/manuals/vps/users.txt:92-93`
   and Czech candidate at
   `work/2026-08-18-vpsadmin-password-reset/kb-candidates-history/cs/navody/vps/uzivatele.txt:91-92`
   both say that required password changes have no initiating session. In the
   final code, token completion passes the password-change row into
   `NewTokenLogin` at `vpsadmin/api/lib/vpsadmin/api/authentication/token_config.rb:169-184`,
   and OAuth completion carries it into the authorization at
   `vpsadmin/api/lib/vpsadmin/api/authentication/oauth2_config.rb:749-769` for
   attachment during session creation. The production runbook correctly
   describes both links at
   `vpsfree-cz-configuration/docs/operations/vpsadmin-password-recovery-deployment.md:383-387`.
   These candidates and their release manifests are retained untracked
   workspace publication artifacts; KB publication is explicitly separate, so
   this does not block merging the four reviewed branches. It does block using
   those manifests for a later wiki promotion. Correct both candidate
   sentences and regenerate their checksums/manifests before staging or
   publication.

## Coverage and residual gaps

I inspected the exact ranges from the packet:

- `vpsadmin` `61d2ef6e712345200daddff3abcb4697c028d176..a2e6d8037c737c61c15bfd845c1b3c57d894f310`
- `vpsfree-mail-templates` `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676..f944ba03eba5d0d6b58b7eb856f251d1c96f2c11`
- `vpsfree-kb-contracts` `81d6d7dfe530884aff3e1d2634e02e4b12fe28e8..6d8ab17db3ce8ffc41216feeb90bff8468b4d39d`
- `vpsfree-cz-configuration` `b4e120294696578c3871124259f266205bad4393..8928b2aba9230202e805aa5489dc9f7369650ac7`

The review covered authentication and recovery state transitions, queue and
retention behavior, migrations, detailed audit authorization and WebUI
consumption, built-in and external mail contracts, Nix service/proxy/monitoring
consumers, rollout and rollback ordering, downstream pins, tests, and full
commit messages/diffs. I independently traced the initially suspected final
lifecycle race and found no defect: `NewBasicLogin` and `NewTokenLogin` lock and
reload the user, then call `Operations::User::Login`, whose first action is the
lifecycle-aware `Operations::User::CheckLogin` check.

I manually enumerated the new reader instructions that perform WebUI actions.
The metrics setup instructions in both languages use
`member.metrics-access-tokens.open`; the password-history instruction in each
language uses `member.password-changes.open`. The latter path is registered at
`vpsfree-kb-contracts/contract/navigation.yml:530-534`, and both page counts are
declared at `contract/kb-annotations.yml:180-183,364-367`. I found no missing
semantic navigation binding.

Per the packet, I did not run tests or mutate the projects or development
cluster. The coordinator ran the isolated characterization probes cited above
without touching the development cluster. The available current-head evidence
is strong: the CI selector passes
16 tests / 55 assertions, the external-template checker passes 71 templates /
349 files, all current-head workflows are green, and the full integration log
reports 118 successful tests. Those suites do not exercise the Basic-provider
rehash metadata boundary or an oversized recovery WebAuthn User-Agent. The
earlier one-off metrics-token HTTP 500 still lacks a root cause, although it did
not recur in focused checks or the identical full order.
