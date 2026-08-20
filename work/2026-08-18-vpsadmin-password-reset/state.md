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

## User-acceptance follow-up (2026-08-20)

- The user requested shorter request-form copy, a revised neutral confirmation,
  no user-facing recovery-code wording, HTML mail buttons, a working OAuth
  restart behind “Back to sign in”, and the configured logo on all recovery
  states.
- Root cause of the empty WebUI content column: the OAuth client's
  `authorization_start_uri` ended at `?page=login`; WebUI only begins OAuth for
  `?page=login&action=login`. The test seed and backward-compatible shared
  dev-cluster updater are being changed to use the actual authorization entry
  point.
- The recovery page keeps its restrictive content security policy. Logo
  rendering is limited to configured absolute HTTP(S) URLs without user info or
  fragments, and only the validated origin is added to `img-src`.
- The Linux page fault remains documented but is not being patched, per the
  user's explicit decision. No kernel or vpsAdminOS files are in scope.
- The acceptance follow-up was split into focused wording, HTML-mail, logo/CSP,
  and OAuth-restart commits. Production mail wording and HTML are separate, and
  the KB history contains one final exact-pin commit. Clean pushed heads are:
  - `vpsadmin`: `60126568cd7b6cd6c806efb4ed476774e37b4c4f`
  - `vpsfree-mail-templates`:
    `e6a9d9bbe058ca9279fa825d7bbd91dae8958c8f`
  - `vpsfree-kb-contracts`:
    `20517911557ea142507f0c6e2ee33860d7f286b7`
- Focused final-tree verification passes: 34 API examples, RuboCop, API i18n
  update and health, Playwright JavaScript syntax, Nix formatting, all changed
  ERB compilation, active Overcommit hooks, and the full KB contract with its
  120-image inventory.
- The fresh standalone mandatory review found no Blocking or Important issue.
  Its one Advisory notes that custom-route coverage still synchronizes
  `custom_routes_coverage_spec.rb` with `covered_custom_routes.yml` manually.
  All twelve recovery routes are correctly covered. Consolidating that existing
  test registry is deferred because it is unrelated architecture cleanup and
  does not affect runtime behavior or this feature's coverage.
- The exact `60126568c` `./test-runner.sh test 'webui#auth'` integration passes.
  Its Playwright example completed in 351.02 seconds, the test script in 725.88
  seconds, and the full isolated test in 967.95 seconds with 1 of 1 tests
  successful. The browser assertion follows “Back to sign in” through WebUI
  and confirms that a new authorization starts on the auth frontend.
- The existing bridge-network development cluster was updated in place to
  exact clean revision `60126568c`. `/etc/vpsadmin/build-info.json` reports that
  revision with `revisionDirty: false`; `vpsadmin-api`, nginx, and
  `vpsadmin-password-recovery` are active and the cluster reports ready. The
  public recovery page returns HTTP 200, renders the configured logo, and its
  CSP permits only the validated WebUI logo origin. The live WebUI sign-in
  entry returns HTTP 302 to the OAuth authorization endpoint instead of the
  previously empty login shell.
- The shared-address fixture was reapplied after the service switch:
  `test-user1` and `test-user2` both use
  `shared-password-recovery@example.test`; only `test-user1` has effective TOTP,
  with deterministic secret `JBSWY3DPEHPK3PXP`. A real public request returned
  the neutral confirmation and produced one grouped multipart message. It has
  one plain-text link and one HTML action button for `test-user1`, a support-only
  entry for `test-user2`, and no user-facing recovery-code or single-use
  wording. A bad factor attempt returned HTTP 422 with the TOTP-only error; a
  valid TOTP reached the new-password form, whose logo and account label were
  also verified. No password was changed.
- The ten-minute recipient throttle was preserved during testing. After moving
  only the disposable request timestamp outside that window, a final public
  submission produced fresh Mailpit message `7jLZ5HzjbO8DX7YMr50lnX`. Its
  per-account reset token was not opened or consumed and is intentionally left
  as the newest message for user acceptance.
- Exact-head GitHub Actions are green for vpsAdmin RuboCop, i18n health, and all
  27 API topic jobs, and for both KB workflows (`Check` and managed-page
  runtime). The exact-head full vpsAdmin integration workflow is still running.

## Open questions

- None. Product and security choices are recorded in `plan.md`.

## Mail notification and throttling follow-up (2026-08-20)

- The user reported that the recovery message changed the established
  automated-mail notice, requested a password-changed security message, and
  found that recipient-address throttling silently suppressed a request for a
  different login sharing the same primary email.
- The accepted admission policy uses the normalized submitted value before
  account lookup: one accepted request per value per 10 minutes, plus the
  existing 10-per-source rolling limit. Either limit returns HTTP 429 and
  `Retry-After`. Queue capacity is reduced from 1,000 to 100 unfinished rows;
  capacity or persistence failures return HTTP 503.
- Finished submission ledgers will be kept for one day and excluded from queue
  capacity. The raw identifier and user agent will be cleared after terminal
  processing. The unreleased migration can be rewritten and the development
  database reset.
- Password-change notices cover recovery, authenticated self-service changes,
  and forced OAuth/token changes. They are plain text, include security details
  comparable to `user_new_login`, and are not sent for administrator changes to
  another account.
- The exact canonical automated-mail notice will be written into both
  repositories' contributor rules. The English and Czech member-facing copy is
  being edited under the workspace user-facing-writing and Humanizer guidance.
- Implementation is in progress from clean pushed heads `60126568c`
  (vpsAdmin), `e6a9d9bbe` (production mail templates), and `205179115`
  (KB contracts). The kernel investigation remains out of scope and no kernel
  or vpsAdminOS change will be made.
- The follow-up is implemented, committed, and pushed at clean exact heads:
  - `vpsadmin`: `94c521bfef8dd116a32e37f620b4b5bf0f8cbc8c`
  - `vpsfree-mail-templates`:
    `26a010e0b7316a25804a280b713b625572205f88`
  - `vpsfree-kb-contracts`:
    `c9c7b4128387f3879d864b448a441d743aa1dbc1`
- The admission ledger now hashes the normalized submitted value before any
  account lookup. It returns HTTP 429 with a computed `Retry-After` for the
  per-value or per-source window and HTTP 503 when the 100-item unfinished
  queue cannot admit work. Terminal rows are scrubbed and retained for one
  day; they enforce rolling limits without consuming queue capacity.
- The recipient-address throttle was removed. Operation coverage confirms that
  two different submitted logins sharing one primary email create two
  independent messages, while an email submission can still group all matching
  accounts in one message.
- Successful recovery, authenticated self-service, and forced OAuth/token
  password changes now enqueue the bilingual plain-text security notice.
  Administrator changes to another account do not. The canonical bilingual
  automated-mail footer is restored in both recovery message variants and its
  exact wording is recorded in both repositories' contributor rules.
- Quick verification passes: 49 queue/worker/operation/route/task examples;
  both migration examples including rollback; all 27 changed Ruby files under
  RuboCop; API locale update and health; changed ERB and Ruby syntax; and the
  two focused authenticated/admin password-change resource examples. The
  expanded 125-example notification run initially had 124 passes and one
  fixture-only failure because its deliberate concurrency wrapper lacked a
  mail server; after isolating the notification chain there, that exact failed
  example passes. The vpsAdmin Overcommit hook reran Nix formatting, migration
  specs, WebUI/API i18n checks, and RuboCop successfully at commit time.
- The mandatory-review commit-split gate was applied before review: the
  vpsAdmin follow-up is now two independently reviewable commits,
  `8f27d577a` for throttling/schema and `94c521bfe` for password-change mail.
  Production mail remains split between canonical-footer policy/content and
  the new template. Superseded in-progress CI runs for the rewritten vpsAdmin
  and KB heads were cancelled as required.
- The KB contract is mechanically pinned at all six lock/configuration sites
  to exact pushed vpsAdmin revision `94c521bfe...`. `nix develop -c bin/check`
  passes with 42 controls, 34 paths, 35 capture concepts, 90 bindings, four
  managed pages, 12 runtime tests, 21 executable samples, and all 120 PNGs.
- The required fresh standalone mandatory change review is the next gate
  before the long WebUI integration test and dev-cluster reset/deployment.
- The fresh mandatory review of exact heads `94c521bfe`, `26a010e0b`, and
  `c9c7b4128` reported one Blocking history issue, one Important worker edge
  case, and one Advisory timing issue. The vpsAdmin footer/rule restoration
  must be split from the notification commit; a worker killed after claiming
  attempt three leaves an unclaimable unfinished payload until daily cleanup;
  and admission time was captured before waiting for the serialization lock.
  All three findings are accepted for correction before integration. The same
  standalone reviewer will verify the corrected exact heads.
- All three findings are corrected and pushed. The current clean exact heads
  are `1096992e4cd6fd0c6263f58fc77ac0f3b255aa7e` for vpsAdmin,
  `26a010e0b7316a25804a280b713b625572205f88` for the production mail
  templates, and `ee6b3c079a6282e269465e49876372ec1f25851e` for the KB
  contract. The vpsAdmin history now has independent commits for throttling,
  password-change notification, and footer/rule restoration.
- Admission now measures its rolling windows after obtaining the serialization
  lock and calculates `Retry-After` against current time. Before claiming new
  work, the worker terminalizes and scrubs a stale submission whose final
  attempt was interrupted, releasing its unfinished-queue slot.
- Focused submission and worker coverage passes with 14 examples. The full
  expanded notification/password-flow batch also passes with 125 examples,
  zero failures, and one pre-existing expected pending example. Repository
  hooks pass for both reconstructed vpsAdmin commits, and the repinned full KB
  contract passes locally. Superseded running workflows for both rewritten
  branches were cancelled.
- The same standalone reviewer is verifying the corrected exact heads before
  the long OAuth/WebUI integration test and bridge dev-cluster reset.
- The same standalone reviewer completed the correction pass with no remaining
  Blocking, Important, or Advisory findings. It confirmed that all original
  findings are resolved, the three vpsAdmin follow-up commits are focused, all
  worktrees and SSH remote heads match, and all six KB pin sites resolve to
  `1096992e4cd6fd0c6263f58fc77ac0f3b255aa7e`.
- The exact `1096992e4` `./test-runner.sh test 'webui#auth'` integration passes.
  The Playwright example completed in 363.03 seconds, the script in 807.79
  seconds, and the isolated test in 1,069.82 seconds with 1 of 1 tests
  successful.
- The bridge development cluster was reset because the unreleased migration
  was rewritten. The old runner exceeded its 120-second stop grace period, so
  the reset tool killed it, removed only this initiative's GC root/state, and
  rebuilt a fresh single-node bridge cluster from clean exact revision
  `1096992e4` (`revisionDirty: false`). Initial post-seed node refresh hit the
  documented osctld-socket startup race; node1 was already healthy moments
  later, and the documented scoped `devcluster update ... node1` followed by
  `devcluster refresh` completed successfully. The cluster is ready and API,
  nginx, and `vpsadmin-password-recovery` are active.
- The shared-email acceptance fixture is restored on the fresh database:
  `test-user1` and `test-user2` use
  `shared-password-recovery@example.test`; only `test-user1` has effective
  TOTP, with secret `JBSWY3DPEHPK3PXP`.
- Live acceptance verifies that immediate `test-user2` and `test-user1`
  submissions each return the neutral HTTP 303 and produce separate messages.
  A repeated `test-user1` request returns HTTP 429, a computed `Retry-After`
  header, and the explicit English wait message. The no-MFA message contains
  support guidance but no reset action; the MFA-enabled message has plain and
  HTML actions. Both have the canonical footer and neither mentions recovery
  codes or single-use behavior.
- A complete live recovery used the deterministic TOTP, showed the logo and
  account label on the password form, reset the account to its documented
  development password, and redirected to WebUI's OAuth-start entry point. It
  produced the plain password-changed security message with time, source IP,
  user agent, support guidance, and canonical footer.
- A final unconsumed acceptance request is the newest Mailpit message,
  `5oQPUVXLrO1bJgwo7i3d4K`. Its `test-user1` recovery is unconsumed,
  incomplete, and uninvalidated; it had 3,588 seconds remaining when checked.
  Leave the bridge cluster running for user acceptance.
- Exact-head GitHub Actions are green for API topic specs, migration specs,
  RuboCop, i18n health, libnodectld specs, the KB contract, and managed-page
  runtime. The full vpsAdmin CI run `32388040775` is still in progress; the
  user warned that runner redeployment may interrupt it, so inspect evidence
  and restart it if that occurs.
- User acceptance found that the immediate post-reset OAuth redirect hides the
  successful outcome. The completion follow-up now redirects the password POST
  to the internal completion page, carries only the persisted recovery client
  and locale, shows the exact short bilingual confirmation, and offers a button
  to start a fresh OAuth authorization. It never accepts a browser-provided
  redirect target and omits the button if the saved client has no configured
  authorization start URI.
- The focused password-recovery route spec passes with 20 examples. API i18n
  update/health, RuboCop for the touched Ruby files, ERB compilation with the
  production trim mode, JavaScript syntax, and `git diff --check` pass. The
  first focused rerun exposed one old redirect expectation and the first i18n
  health run exposed the stale explicit key inventory; both test-backed issues
  were corrected before commit.
- The completion follow-up is committed and pushed as vpsAdmin
  `eba275914372bb69db0b3b84c0d9d7ecf18b240a`. The production mail-template
  head is unchanged at `26a010e0b7316a25804a280b713b625572205f88`.
- The KB branch was rebased onto current `origin/master` at `c1d0aca` and its
  repeated development pins were consolidated into one mechanical commit, as
  required for clean unmerged dependency history. Its exact pushed head is
  `60293e20efd2fdc4209dc18a2759156a1ff69537`; all six pin sites reference the
  vpsAdmin completion head. The full contract passes after the rebase with 42
  controls, 34 paths, 35 capture concepts, 90 bindings, four managed pages, 12
  runtime tests, 21 executable samples, and all 120 PNGs. No managed page or
  capture changed.
- Superseded in-progress CI for the prior vpsAdmin head and both superseded KB
  heads was cancelled. Exact-head CI has started. The fresh mandatory review
  of the two pushed completion deltas is the next gate before rerunning the
  long WebUI integration test.
- The required fresh standalone mandatory review completed for exact pushed
  vpsAdmin `eba275914` and KB `60293e2` with no Blocking, Important, or
  Advisory findings. It confirmed the persisted client/locale context, internal
  303, flow-cookie clearing, server-configured OAuth destination, exact copy,
  optional button behavior, focused commit split, unchanged mail templates,
  and all six KB pins. The reviewer independently reran the 20-example route
  spec successfully. Residual coverage is limited to the intentionally pending
  exact-head `webui#auth` integration and indirect rather than header-level
  assertion of cookie deletion; rejected recovery reuse covers the latter
  behavior.
- The exact `eba275914` `./test-runner.sh test 'webui#auth'` integration passes.
  The Playwright example completed in 327.86 seconds, the script in 703.22
  seconds, and the complete three-machine test in 937.64 seconds with 1 of 1
  tests successful.
- The existing single-node bridge development cluster was updated in place to
  exact clean revision `eba275914372bb69db0b3b84c0d9d7ecf18b240a` without a
  database reset. `devcluster refresh` completed, the cluster reports
  `running` and `ready: yes`, and `vpsadmin-api`,
  `vpsadmin-password-recovery`, nginx, WebUI, and Mailpit are all active. The
  public recovery form returns HTTP 200 with the configured logo. The live
  English and Czech completion pages show the exact requested copy and sign-in
  labels, and the WebUI sign-in entry point returns HTTP 302 to a fresh OAuth
  authorization request.
- Exact-head GitHub Actions are green for the vpsAdmin API topic specs,
  RuboCop, and i18n health, and for both KB contract workflows. Broad vpsAdmin
  CI run `32402119307` remains healthy on the current head after 54 minutes;
  no runner interruption has been reported. The immediately preceding
  successful run spent 5 hours 7 minutes in the same test step, so the current
  duration is normal and the completed handoff is not held open for that
  multi-hour remote signal.
- The in-place services update reran the declarative development seed after the
  final acceptance checks. It reset the two test users to their default email
  addresses and forced `test-user1.enable_multi_factor_auth` off while leaving
  its enabled, confirmed `Acceptance TOTP` device intact. This caused the
  user's next `test-user1` recovery to produce the support-only outcome. The
  live bridge fixture is corrected: both users again share
  `shared-password-recovery@example.test`, only `test-user1` has account MFA
  enabled, and its TOTP device remains enabled and confirmed. The one recent
  `test-user1` submission was moved outside the ten-minute development throttle
  window so the user can retry immediately; no replacement request was sent.

## Cleanup

- Leave the dev cluster running for user acceptance.
- Remove worktrees only after the feature is merged or abandoned.
