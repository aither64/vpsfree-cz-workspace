# 2026-08-18-vpsadmin-password-reset

## Repositories

- `vpsadmin`
  - branch: `2026-08-18-vpsadmin-password-reset`
  - worktree: `worktrees/2026-08-18-vpsadmin-password-reset/vpsadmin`
  - base at creation: `d8ce525fa08dfbdc96348a8682d11a78649c8b2b`
- `vpsfree-mail-templates`
  - branch: `2026-08-18-vpsadmin-password-reset`
  - worktree: `worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-mail-templates`
  - base at creation: `04921d75ab5321962b207bb380deff90906bd662`
- `vpsfree-kb-contracts`
  - branch: `2026-08-18-vpsadmin-password-reset`
  - worktree: `worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-kb-contracts`
  - base at creation: `1fe36b35cebb75f8c61741da77b6861d4e0ece58`

## Status

- Feature worktrees created.
- vpsAdmin schema, recovery state machine, OAuth routes/forms, TOTP and
  WebAuthn verification, shared-address mail delivery, cleanup task, feature
  flag, localization, and focused specs are implemented.
- Czech and English production mail templates are implemented.
- Quick verification and repository hooks pass on the amended pushed heads. A
  fresh exact-head review found three blocking serialization defects in the
  preceding authentication prerequisite commit; all were fixed with dedicated
  regressions and the four-commit history was rewritten. A later exact-head
  review found two more revocation races, and the next review found a recovery
  TOTP lock inversion/factor-replay flaw; all are fixed with dedicated
  regressions. A final remediation review is running on the exact repinned
  heads. The long integration rerun remains gated on that review.
- The OAuth/WebUI integration test passed at the preceding vpsAdmin head. The
  running single-topology bridge-network development cluster still has that
  build and must be reset and redeployed because the unmerged migration was
  amended with the asynchronous submission table.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-08-18-vpsadmin-password-reset vpsadmin --as-is --branch 2026-08-18-vpsadmin-password-reset --base origin/master`
- `bin/dev-session worktree add 2026-08-18-vpsadmin-password-reset vpsfree-mail-templates --as-is --branch 2026-08-18-vpsadmin-password-reset --base origin/master`
- `bin/dev-session worktree add 2026-08-18-vpsadmin-password-reset vpsfree-kb-contracts --as-is --branch 2026-08-18-vpsadmin-password-reset --base origin/master`
- `nix develop ..#api -c bundle exec rake vpsadmin:i18n:update`
- `nix develop ..#api -c bundle exec rake vpsadmin:i18n:health`
- Focused RSpec runs for password recovery routes, operations, mail handling,
  OAuth client configuration, API serialization, route coverage, and the
  authentication cleanup task.
- `./test-runner.sh test 'webui#auth'`
- `dev-clusters/vpsadmin/bin/devcluster start
  2026-08-18-vpsadmin-password-reset --topology single --network bridge`
- `dev-clusters/vpsadmin/bin/devcluster update
  2026-08-18-vpsadmin-password-reset services`
- Focused post-review RSpec runs for the durable submission worker, uniform
  request enqueue, pending authentication-token revocation, session exception
  handling, WebAuthn input validation, locked final eligibility, and cleanup.
- `nix develop ..#api -c bundle exec rubocop`
- `nix develop -c bin/check` after repinning the KB contract to the post-review
  vpsAdmin commit.

## Results

- The active environment and dev-session slug both resolve to
  `2026-08-18-vpsadmin-password-reset`.
- All three repositories use SSH remotes and clean dedicated worktrees.
- The recovery request operation groups all accounts sharing a primary email
  into one account-neutral `MailLog`, with an independent link only for each
  eligible account and exclusive recipient handling.
- Raw email tokens appear only in the rendered mail and are stored as SHA-256
  digests in recovery rows. Email links last one hour and exchange once for a
  non-sliding 15-minute HttpOnly recovery cookie.
- Focused request-operation, TOTP, mail, resource, custom-route, and cleanup
  tests pass. OAuth route tests pass for TOTP, token reuse, generic public
  responses, session preservation/revocation, and failed passkey retry.
- Initial focused failures exposed a Ruby constant collision in the route
  controller, a mail-template registry order leak, and malformed WebAuthn
  input handling. All three were fixed and their affected suites passed.
- Successful WebAuthn recovery, normal-authentication challenge isolation,
  password-change invalidation, and recovery-challenge cleanup coverage were
  added during the security edge-case pass.
- The expanded focused suite passed with 97 examples and no failures. The
  recovery route suite later passed 10 examples including continuation after a
  recovery code disables the final TOTP device.
- The migration up/down spec and core-schema smoke spec passed with 4 examples
  and no failures. Migration and ordinary application specs must run in
  separate RSpec processes; the reusable reason is recorded in
  `notes/vpsadmin/2026-08-18-separate-migration-specs.md`.
- Full API RuboCop inspected 1,471 files; its nine reported offenses were fixed.
  Subsequent focused reruns inspected the latest changed files with no
  offenses.
- A final focused ordinary-spec run passed 45 examples, including the enabled
  and disabled OAuth forgot-password link, exact-login/shared-email grouping,
  one-time token exchange, password-change invalidation, and cleanup behavior.
- The generated English and Czech catalogs are normalized and the i18n health
  check passes. The OAuth client's authorization start URI has an explicit
  human-readable label that survives catalog generation.
- `git diff --check` passes for the vpsAdmin worktree.
- The first commit attempt from the ambient shell was rejected because the
  combined Overcommit checks could not find RuboCop, gettext, or MariaDB. The
  commit was rerun without bypassing hooks in `nix develop .#vpsadmin`; the
  reusable shell requirement is recorded in
  `notes/vpsadmin/2026-08-18-overcommit-nix-shell.md`.
- Production mail-template Ruby and ERB syntax checks pass in its Nix shell.
- The canonical WebUI documentation workflow applies because the OAuth sign-in
  page changes. The contract is pinned to the exact vpsAdmin feature commit;
  all semantic, page, test, capture, and inventory checks pass without any
  reader-visible KB or screenshot changes.
- Preceding pushed revisions after the earlier review and integration fixes:
  - `vpsadmin`: `1d62a2f2e516b0a7ed535ed0e9af00920d5ce9c4`
  - `vpsfree-mail-templates`:
    `0c4009337f3ecbde1943c7039eabcd5b20b20750`
  - `vpsfree-kb-contracts`:
    `fd70a83951b1edf3814c1c3d5751d22db9bfc8b0`
- The mandatory reviewer found that `UserSession::CloseAll` did not revoke a
  standalone SSO with a pending OAuth authorization code. The operation now
  atomically closes ordinary sessions, destroys pending codes, and closes all
  user SSO tokens. Operation and route-level regressions prove that both the
  code and SSO are unusable after a checked reset.
- The reviewer also found duplicated recovery eligibility/MFA gates. Issuance,
  link exchange, and continuation now use one
  `PasswordRecoveryPolicy`; lifecycle-only email snapshot validation remains
  in the controller. Dedicated policy specs cover confirmed TOTP, WebAuthn,
  unconfirmed TOTP, and login-policy rejection.
- The review advisory to describe the OAuth authorization start URI was also
  applied with normalized English and Czech API metadata.
- Post-review verification: 44 focused route/operation/resource examples and
  6 focused policy/session examples pass, targeted full-shell RuboCop is clean,
  i18n update/health passes, and all Overcommit hooks pass on the amended
  feature commit.
- The second standalone review found an account-enumeration timing oracle in
  synchronous request processing. The public POST now performs one uniform
  `PasswordRecoverySubmission` insert for known and unknown identifiers. A
  dedicated systemd worker claims rows with `FOR UPDATE SKIP LOCKED`, performs
  account lookup and mail work after the response, retries failures three
  times with a five-minute stale-claim interval, deletes processed rows, and
  discards queued work when the feature is disabled. Abandoned submissions are
  cleaned after one day.
- The same review found that pending `AuthToken` rows could survive a password
  change and complete an old MFA or forced-reset flow. Every persisted password
  change now destroys both token purposes and their backing tokens, whether or
  not ordinary sessions are retained. Full session revocation also destroys
  pending authentication tokens.
- `UserSession::CloseAll(except:)` now preserves OAuth authorization and SSO
  state tied to the excepted session while full recovery revocation still
  closes all such state. Non-object WebAuthn JSON returns a controlled 422, and
  final password submission reloads and locks the user before checking the
  email snapshot and login policy.
- The integration fixture now uses `auth.vpsadmin.test` as the OAuth authority,
  enables recovery for the browser suite, and follows the real forgot-password
  link through the dedicated auth nginx frontend to the recovery form.
- Post-second-review quick verification passed: 92 wider focused examples, 74
  final recovery/OAuth examples, 4 worker examples, and 2 migration up/down
  examples, all with zero failures. Full API RuboCop inspected 1,478 files
  without offenses; JavaScript syntax, Nix parsing, Nixfmt, `git diff --check`,
  and every vpsAdmin pre-commit hook pass. The KB contract passes after its
  exact revision pin was updated.
- The long `webui#auth` integration test passed: the Playwright authentication
  example completed in 306.77 seconds, the test script in 688.58 seconds, and
  the full test in 936.56 seconds.
- Browser-level dev-cluster verification found that the dedicated auth nginx
  frontend proxied only `/_auth` and `/webauthn`; the new recovery route was
  initially available only on the API hostname. The frontend now also proxies
  `/oauth2/password-reset`. Nixfmt and all vpsAdmin Overcommit hooks pass on
  the final amended commit, and the running services VM was updated to it.
- The KB contract was repinned to the final vpsAdmin head. `nix develop -c
  bin/check` passes all semantic, page, runtime-test, capture, and inventory
  checks with no reader-visible documentation or screenshot drift.
- Dev cluster `2026-08-18-vpsadmin-password-reset` is running with the `single`
  topology and bridge networking. The first start command encountered an
  `osctld` readiness race after the runner had already made the cluster ready;
  adding the four expected default-group device rules once `osctld` was ready
  and restarting `nodectld` completed node initialization. The reusable
  diagnosis is recorded in
  `notes/vpsadmin/2026-06-15-devcluster-node-osctld-race.md`.
- At the preceding deployed head, the cluster had `test-user1` (confirmed TOTP)
  and `test-user2` (no MFA) on
  the same primary email. A real public recovery submission returned the
  neutral 303 response and produced exactly one Mailpit message. The message
  lists both logins, contains one one-hour reset link for `test-user1`, and
  directs `test-user2` to support without a link. Its database request owns two
  recovery children, while the associated `MailLog.user_id` is `NULL`, proving
  the combined-mail log integration remains account-neutral.
- The advertised auth-host recovery form and unconsumed fragment-link landing
  page both return HTTP 200. The generated message is intentionally left in
  Mailpit with its token unused for user acceptance.
- Superseded vpsAdmin CI runs were cancellation-requested after the force-push.
  The superseded KB managed-page run finished successfully before its cancel
  request arrived. Fresh workflows are running against the new heads. The
  mail-template repository has no branch workflow run.
- The amended vpsAdmin history is split into authentication serialization
  (`55aeb3027`), bounded recovery queue/mail (`cbe95189f`), the MFA-protected
  OAuth flow (`a8318f7e6`), and Nix/deployment integration (`f31a7bdf4`). Every
  commit passed the repository's complete Overcommit suite in a clean detached
  commit worktree; no hook was bypassed.
- Recovery usability is rechecked after row locking so a request completed or
  invalidated concurrently cannot change the password. Password changes and
  successful password/OAuth issuance serialize on the user row through an
  authentication generation, including authorization-code and refresh-token
  exchange.
- Queue admission is bounded at 1,000 pending submissions globally and 10 per
  source address per 10 minutes. The worker stays idle before the recovery
  schema is deployed, backs off on processing errors, and reuses the durable
  request result if delivery succeeded before the submission was deleted.
- The preceding exact-head quick verification passed 210 ordinary examples
  with zero failures and one pre-existing pending example. The two migration
  specs pass separately with 4 examples and zero failures. The KB contract
  passes all semantic, page, test, capture, and inventory checks at the exact
  vpsAdmin revision. The intentionally invalid mixed migration/application
  invocation was discarded because migration specs switch to their isolated
  database; both required separate invocations passed.
- After rewriting the vpsAdmin and KB feature histories, superseded in-progress
  CI was cancellation-requested only for old heads. Current-head workflows are
  running for `f31a7bdf4` and `bc425cea`.
- The superseded KB managed-runtime failure was investigated from its uploaded
  logs rather than blindly rerun. `tests/configs/nixos/vpsadmin-services.nix`
  assigned `auth.vpsadmin.test` at normal priority, conflicting with the test
  framework's externally reachable auth domain. The fixture now uses
  `lib.mkDefault`, preserving the standalone hostname while allowing runner
  override. The focused Nix evaluation succeeds with the local vpsAdmin input,
  all vpsAdmin hooks pass on the amended deployment commit, and the repinned KB
  contract passes locally; fresh managed-runtime CI is running.
- The final exact-head mandatory review of `1d62a2f2e` found that default user
  and administrator password changes called `CloseAll` with unsaved password
  fields, which ActiveRecord refuses to lock; that persistent token and HTTP
  Basic sessions could still be published from a password generation verified
  before a concurrent recovery reset; and that an ordinary password update
  verified with the old password could overwrite a concurrent recovery reset.
  It also advised moving the `password_recoveries` association from the
  authentication prerequisite commit into the recovery-domain commit. The
  findings were accepted and led to the amended history described below.
- The review blockers are fixed on pushed vpsAdmin revision
  `f31a7bdf47eba8d46127286796ba29449a62aff3`. Token and HTTP Basic session
  creation now lock the user and compare the generation captured by password,
  TOTP, or legacy reset-token authentication immediately before publishing a
  session. Continuation option updates preserve that generation. Ordinary user
  and administrator password changes now lock first, reject a stale verified
  generation, persist the password, and only then revoke sessions, so
  `CloseAll` never locks a dirty record. Deterministic regressions cover all
  affected issuance paths, default logout behavior, and an old-password update
  racing a recovery reset.
- The retained-session behavior is explicit: leaving the recovery checkbox
  unchecked preserves existing token, OAuth authorization-code, and SSO state;
  password-backed `AuthToken` continuations are still invalidated by every
  password change. Checking it continues to revoke all session, code, SSO, and
  pending authentication state.
- The reviewer-requested association move is complete:
  `User#password_recoveries` now first appears in the recovery queue/mail
  commit with its schema and models.
- Exact amended-head verification passed 234 ordinary examples with zero
  failures and one pre-existing pending example. The two migration specs pass
  separately with 4 examples and zero failures. All active vpsAdmin hooks pass
  on every amended commit, and targeted RuboCop inspected all corrective files
  without offenses.
- The KB contract is pinned to pushed revision
  `bc425cea37e8dd5c8a97871297b03f2e06f6e1a6`, including the recalculated Nix
  source hash. `nix develop -c bin/check` passes all semantic, page, runtime,
  capture, and inventory checks at the amended vpsAdmin head.
- The next exact-head review found that `CloseAll(except:)` used SQL `NOT IN`
  semantics which skipped normal pending OAuth authorizations whose
  `user_session_id` is `NULL`, and that a stale TOTP continuation could consume
  or disable a factor after a concurrent password change invalidated its token.
  `CloseAll` now explicitly includes `NULL` authorizations, while TOTP
  continuation re-finds and validates its token and authentication generation
  under the user row lock before any factor mutation. Real pending-code and
  deterministic recovery-code race regressions cover both findings.
- The resulting pushed vpsAdmin code revision `f1e2533c4efc18b46e469f35d791a39e211fa132`
  passed 243 changed ordinary examples with zero failures and one pre-existing
  pending example, 23 focused corrective examples with zero failures, targeted
  RuboCop, and every repository hook. Its migration, RuboCop, i18n, and
  libnodectld GitHub workflows also passed before the head was superseded.
- The `f31a7bdf4` GitHub CI artifact was investigated before any rerun. All
  seven non-WebUI integration tests passed; every WebUI script failed with HTTP
  500 because HaveAPI rejected the separate `auth.vpsadmin.test` authorization
  URL. The PHP/nginx log identified the exact protocol error, and the test
  WebUI fixture was missing that origin from `api.oauth2TrustedOrigins`.
  Production and dev-cluster WebUI configuration already trust their auth
  origins. The deployment commit now configures the test fixture as well.
- Current clean, pushed, remote-matching heads are:
  - `vpsadmin`: `aff18a72805a5f517407a92871fc7b1d6ef579bd`
  - `vpsfree-mail-templates`:
    `0c4009337f3ecbde1943c7039eabcd5b20b20750`
  - `vpsfree-kb-contracts`:
    `9902e2500f10b4af92bdde331aa94fa14d54d609`
- The only change from verified code head `f1e2533c4` to `aff18a728` is the
  one-line trusted-origin integration fixture. The amended deployment commit
  passed all Overcommit hooks in `nix develop .#vpsadmin`; no hook was bypassed.
  Superseded in-progress workflows were cancelled only after the replacement
  push.
- Both migration up/down specs were rerun at exact head `aff18a728` in the API
  Nix shell and passed with 4 examples and zero failures.
- Every KB pin and both lock-file revision fields now reference exact vpsAdmin
  revision `aff18a72805a5f517407a92871fc7b1d6ef579bd`, with a recalculated source
  hash. `nix develop -c bin/check` passes syntax, semantic/page/capture
  validation, all four unit suites, and the complete 120-image inventory at
  KB revision `9902e2500`.
- The final `aff18a728` review found two Important rollout/concurrency issues
  and one route-coverage advisory. A negative ActiveRecord table-existence
  result could be cached forever by a worker started before the migration, and
  recovery completion acquired its recovery and user locks in the opposite
  order from ordinary password changes. The worker now uses a connection-level
  uncached existence query, rechecks false results until the schema appears,
  and memoizes only a successful result. Link exchange and final password
  submission now acquire the user row before the recovery row. Regressions
  cover a same-process absent-to-present schema transition and the actual SQL
  `FOR UPDATE` order. The clientless completion redirect is also followed and
  asserted behaviorally.
- The corrected vpsAdmin history is clean, pushed, and split into four
  functional commits at `c93b03bf77b28865d823a67a0dd314333bea4c0e`.
  All hooks passed before the two corrections were autosquashed into their
  queue and OAuth-flow commits; no hook was bypassed. Exact-head verification
  passed 245 changed ordinary examples with zero failures and one pre-existing
  pending lifecycle example, 23 focused route/worker examples with zero
  failures, 4 migration examples with zero failures, targeted RuboCop, and
  `git diff --check`.
- The exact vpsAdmin revision is pinned at every KB contract and Nix lock site.
  The clean, pushed KB head is
  `3a254ad9f5ad0ab8b5822092a6bb59cb7ba8ecc0`; `nix develop -c bin/check`
  passes all semantic, managed-page, executable-sample, unit, capture, and
  120-image inventory checks. The mail-template head remains clean and pushed
  at `0c4009337f3ecbde1943c7039eabcd5b20b20750`.
- A new standalone mandatory review is running against only these exact three
  pushed heads. Long integration and the clean dev-cluster reset/redeployment
  remain gated on its result. Current-head GitHub Actions are running; RuboCop,
  migration, i18n, and libnodectld jobs have already passed.
- That review confirmed a Blocking MariaDB deadlock and factor-replay window in
  recovery TOTP. The operation held a recovery row and then updated the user
  failed-login counter, opposite to the User-then-Recovery order used by every
  password change. It also lacked the User lock that serializes normal TOTP, so
  two recoveries could inspect the same factor state. Recovery TOTP now locks
  User then Recovery before all valid/invalid factor work. A real SQL-order
  regression and a second-recovery TOTP replay regression cover the invariant;
  the focused operation/route suites and full changed suite pass.
- The same review had no Important findings. Its initially reported systemd
  lifecycle concern was retracted after checking `Requires=` stop/restart
  propagation; the temporary redundant `PartOf` and restart-test fixup was
  dropped completely. The review advisories led to canonical Czech
  `Přezdívka` terminology in the form and both mail-template copies, the exact
  full review bases above, and explicit compatibility documentation for the
  additive OAuth client URI and nullable MailLog user API fields. Existing
  clients remain compatible, while the generated Go client cannot yet manage
  the new URI and is intentionally not regenerated in this initiative.
- Final clean, pushed, remote-matching candidate heads are:
  - `vpsadmin`: `1c83542ae9cbedb28c3b543438e2eb3d92eecc89`
  - `vpsfree-mail-templates`:
    `e328f1c058e378a60ce80316c5f62f7d2300b16f`
  - `vpsfree-kb-contracts`:
    `a4269b23858781bf15f3b6e483752f14232e025c`
- Exact final-head quick verification passed 247 changed ordinary examples
  with zero failures and one pre-existing pending lifecycle example, both
  migration specs with 4 examples and zero failures, i18n normalization and
  health, focused RuboCop, all repository hooks, production ERB compilation,
  and `git diff --check`. The final KB head pins vpsAdmin `1c83542ae` at every
  contract/lock site with a recalculated source hash; its full `bin/check`
  passes the semantic, page, executable-sample, unit, capture, and 120-image
  inventory checks.
- The final fresh mandatory review independently verified the exact clean,
  pushed heads and complete three-repository ranges. It reported no Blocking,
  Important, or Advisory findings and approved proceeding with the long
  integration test and scoped development deployment. The remaining validation
  gap is intentionally the exact-head `webui#auth` run and clean dev-cluster
  acceptance check.
- The exact-head `./test-runner.sh test 'webui#auth'` integration passed. Its
  Playwright authentication example completed in 301.53 seconds, the test
  script in 641.14 seconds, and the full isolated test in 876.25 seconds with
  1 of 1 tests successful.
- The exact `1c83542ae` GitHub full-CI failure was investigated from uploaded
  artifact `vpsadmin-test-logs-32206386955`. All but one of 117 tests passed.
  The sole failure was `webui#users-self-service`: the application correctly
  redirected passkey registration to `auth.vpsadmin.test`, while the older
  Playwright assertion still expected `api.vpsadmin.test`. The assertion now
  follows the reviewed authentication-frontend routing. The exact formerly
  failing `./test-runner.sh test 'webui#users-self-service'` run passes, with
  Playwright completing in 396.13 seconds, the script in 869.94 seconds, and
  the full test in 1113.54 seconds with 1 of 1 tests successful.
- The integration assertion was autosquashed into the deployment commit after
  the complete Overcommit suite passed inside `nix develop .#vpsadmin`; no
  hook was bypassed. An initial ambient-shell commit attempt was correctly
  rejected because Nixfmt, gettext, and MariaDB were unavailable, matching the
  existing repository note.
- Final clean, pushed, remote-matching candidate heads are now:
  - `vpsadmin`: `b64f3b96522eaff317f96e26b935a5382060a214`
  - `vpsfree-mail-templates`:
    `e328f1c058e378a60ce80316c5f62f7d2300b16f`
  - `vpsfree-kb-contracts`:
    `2f000f2c1e177930667173a7ed06ffbf9d5ca3f9`
- Every KB contract and Nix lock pin now references exact vpsAdmin revision
  `b64f3b965`, with a recalculated source hash. The full
  `nix develop -c bin/check` passes all syntax, semantic, page, executable
  sample, unit, capture, and 120-image inventory checks at that pin.
- The development cluster was reset and rebuilt from scratch on bridge
  networking. Its initial launch encountered the documented late-osctld socket
  race; after both daemons became active, the recorded `devcluster update ...
  node1` workaround completed successfully. The cluster reports ready and the
  API, nginx, and password-recovery worker are active.
- The disposable shared-email fixture was applied through the deployed
  `db:seed:file` task after a direct Ruby runner correctly failed before any
  mutation because it does not preload ActiveRecord. A real public submission
  returned the neutral HTTP 303 and drained the queue to exactly one Mailpit
  message. Its request owns two recoveries: `test-user1` has one unconsumed,
  unexpired link, while `test-user2` has the support-only outcome. The grouped
  MailLog has `user_id = NULL`; the fragmentless landing page returns HTTP 200.
- Fresh GitHub workflows are running against `b64f3b965` and `2f000f2c1`; no
  superseded old-head workflows remained queued or running. A final fresh
  mandatory review of the one-line CI correction and complete exact heads is
  also running before the final cluster update and handoff.
- The final post-CI-correction mandatory review completed against the exact
  clean, pushed heads. It reported no Blocking, Important, or Advisory
  findings. It independently confirmed that the only post-review runtime-tree
  change is the corrected WebAuthn frontend assertion, that all six KB pins
  reference `b64f3b965`, and that the complete recovery security and
  concurrency design remains sound. Current-head GitHub CI remains the only
  residual validation in progress.
- The running bridge-network development cluster was updated in place to exact
  reviewed vpsAdmin revision `b64f3b965`; `/etc/vpsadmin/build-info.json`
  reports that revision and the API, nginx, and password-recovery worker are
  active. The public auth-host recovery form returns HTTP 200.
- The service switch reapplied the normal built-in dev seed, which deliberately
  restored the default fixture users and invalidated the earlier recovery.
  The initiative's shared-email/MFA fixture was therefore reapplied through the
  deployed `db:seed:file` task. A fresh real public submission returned the
  neutral HTTP 303 and produced one new `[vpsFree.cz] Password recovery`
  message in Mailpit (alongside an unrelated daily report generated at service
  startup). Its latest grouped request has two children, one recoverable link
  for `test-user1`, one support-only outcome for `test-user2`, and a nullable
  grouped `MailLog.user_id`. The token is unconsumed, uninvalidated, and valid
  until `2026-08-19 10:07:12 UTC`; the message is intentionally left untouched
  for user acceptance.
- Exact-head KB GitHub Actions are green: `Check` passed and the managed-page
  runtime completed successfully in 39 minutes 18 seconds.
- The exact-head API topic workflow encountered an external package-mirror
  failure before Ruby or any affected spec ran. Multiple independent
  `ubuntu-latest` jobs reached their 45-minute timeout inside `apt-get update`:
  logs show repeated failures against `azure.archive.ubuntu.com`, a fallback
  to `archive.ubuntu.com`, and then no package-index progress until GitHub
  cancelled the step. Seven matrix jobs that reached their package mirror
  normally completed successfully. The full integration workflow is
  unaffected and still running. Wait for the topic workflow to finish, then
  rerun its failed jobs only after retaining this root-cause evidence.
- After the cancelled first attempt closed, only its affected jobs were
  rerun. Every rerun job cleared package installation, executed RSpec, and the
  exact-head API topic workflow completed successfully on attempt 2 with all
  27 jobs green. This confirms the recorded first-attempt failure was external
  to the feature. The exact-head full integration workflow remains the sole
  GitHub Actions job in progress.
- The exact-head full integration attempt was interrupted by the operator's
  planned runner deployment at `2026-08-19 11:31:56 UTC`. The retained job log
  explicitly says the runner received a shutdown signal; immediately before
  it, the suite reported 95 expected successes, zero expected or unexpected
  failures, three running, and 19 remaining. Both `webui#users-self-service`
  and `webui#auth` had passed in this attempt. GitHub skipped artifact upload
  and result evaluation because the runner stopped. The exact same run was
  restarted as attempt 2 after the new runner came online and was picked up
  immediately.
- Full integration attempt 2 completed 114 of 117 tests successfully. Its
  uploaded artifact was inspected before another rerun. `vps/create` and
  `vps/clone-same-node` failed during Nix evaluation because the runner store
  no longer contained the MariaDB 11.4.12 derivation. `vps/replace-remote`
  failed 8.5 guest-seconds into boot with a Linux 6.18.43 write-protection
  page fault in `__execmem_cache_free`; it never reached API readiness or a
  scenario assertion. These failures are unrelated to the feature.
- At the user's request, a fresh independent agent investigated the kernel
  failure. The trace matches Linux's executable-memory cache race under
  parallel module loading, fixed upstream by commit `1871d548fc4f`
  (`mm/execmem: make the populate and alloc atomic`). A durable workspace note
  records the evidence, safe mitigation, proposed vpsAdminOS kernel backport,
  and verification plan at
  `notes/vpsadmin/2026-08-19-linux-execmem-ci-kernel-page-fault.md`. No
  vpsAdminOS or kernel change was made in this password-recovery initiative.
- The authorized attempt-3 rerun then completed successfully. All 117 selected
  integration tests passed, with zero unexpected failures or successes, in
  21,367.76 seconds. Exact-head GitHub Actions are therefore green for the
  vpsAdmin API topic matrix, full integration suite, i18n workflow, KB checks,
  and managed-page runtime.
- A final shared-email recovery submission returned the neutral HTTP 303 at
  `2026-08-19 22:08 UTC` and produced Mailpit message
  `1UPqQ0KBwrJcr1HrziKHsj`. Database request 3 has exactly two children:
  `test-user1` is recoverable with an unconsumed, uninvalidated, uncompleted
  email token, while `test-user2` has the `no_mfa` support-only outcome and no
  token. The grouped MailLog has `user_id = NULL`. At verification the link
  had 3,457 seconds of its one-hour lifetime remaining; it was not opened or
  consumed and is left in the newest Mailpit message for user acceptance.

## Open questions

- None. Product and security choices are recorded in `plan.md`.

## Cleanup

- Leave the dev cluster running for user acceptance.
- Remove worktrees only after the feature is merged or abandoned.
