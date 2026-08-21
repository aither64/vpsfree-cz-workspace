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
- `vpsfree-cz-configuration`
  - branch: `2026-08-18-vpsadmin-password-reset`
  - worktree: `worktrees/2026-08-18-vpsadmin-password-reset/vpsfree-cz-configuration`
  - base at creation: `50e8f42020ffa2351e4ff14c06d864cf99241fb6`

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

## OAuth completion and deployment handoff follow-up (2026-08-20)

- User acceptance showed that the standalone completion page looked like a
  login form with missing fields and that its full-width sign-in link
  overflowed. The accepted replacement starts the saved OAuth client again and
  shows a Bootstrap success alert above the normal credential fields.
- A successful recovery now sets a host-only, HttpOnly, SameSite=Lax completion
  marker for 15 minutes and redirects to the saved client's validated
  authorization start URI. The OAuth authorization page accepts it only for
  the same client, clears invalid or expired markers, consumes a matching
  marker, bypasses SSO once, and shows `Password changed.` or `Heslo změněno.`
  with the credential form. A marker for another client is left for that
  client and has no authentication effect.
- Clients without an authorization start URI retain a minimal internal
  confirmation page with the same short message and no action button. The
  request and sent pages center their `Back to sign in` links.
- Focused API verification passes with 57 route/OAuth examples, followed by 37
  OAuth examples after adding the invalid-marker regression. API i18n update
  and health, focused RuboCop, ERB compilation, JavaScript syntax, Nix format,
  `git diff --check`, and all active vpsAdmin hooks pass.
- The completion follow-up is committed and pushed as vpsAdmin
  `8d61b33fda41169faf2c985c38fd85c9a506c3ca`. The former standalone
  completion commit and its replacement were consolidated so the unmerged
  history presents only the final OAuth-login alert design. Superseded CI runs
  for `eba275914` and `15e58aefd` were cancelled; exact-head workflows are
  running.
- The KB contract is mechanically repinned at all six revision sites in
  commit `fcfe56f6da459d1ef8826bd8fe52b671347b0cdf`. Its complete local check passes
  with 42 controls, 34 paths, 35 capture concepts, 90 bindings, four managed
  pages, 12 runtime tests, 21 executable samples, and all 120 PNGs. No managed
  page or screenshot changed.
- A dedicated `vpsfree-cz-configuration` worktree was created. The worktree
  post-checkout hook initially reported missing ambient Bundler gems, the
  already-documented linked-worktree behavior; the worktree itself was created
  cleanly and all commits ran through the repository Nix shell with active
  hooks.
- Generated configuration commit `ec2b42f4` pins only the `vpsadmin` services
  channel (`vpsadminServices`) to exact revision `8d61b33fd`. Manual commit
  `957fa346` adds the release-specific deployment runbook and MkDocs navigation.
  The configuration history was rebuilt from its base so the generated pin
  message contains the complete final vpsAdmin changelog. Both commits are
  pushed on the initiative branch.
- The runbook records the exact authorization start URI for WebUI, Czech and
  English DokuWiki, and Discourse; the schema-first API/frontend rollout; the
  reviewed production mail-template revision; enablement, verification, and
  rollback. It does not instruct the operator to update the channel. A strict
  MkDocs build passes.
- The required fresh standalone mandatory review is the next gate before the
  long WebUI integration test, configuration builds, and bridge-cluster update.

## Final release review and handoff (2026-08-21)

- All affected repositories are committed, clean, pushed over SSH, and match
  their remote feature branches at these exact revisions:
  - `vpsadmin`:
    `cdbe04cca72acfaacccca81e7b95dd55c01b4a9e`
  - `vpsfree-mail-templates`:
    `2f6c657321e43d39fa1d464bff78048bb5279573`
  - `vpsfree-kb-contracts`:
    `cd1936b157aa200af6bfc48021b7edad1a7b8cbc`
  - `vpsfree-cz-configuration`:
    `178e3981f1be3425ae57b77fd7a1e720691a2d90`
- The final standalone mandatory review first found that the production auth
  route targeted the API machines instead of the actual `prg/proxy` frontend,
  that the rollout installed the feature-independent password-change template
  after starting upgraded APIs, and that security notices accepted a spoofable
  `Client-IP`. All three findings were fixed. A correction pass reported no
  remaining Blocking or Important issue. Its final Advisory about the missing
  `ip_address` mail-template registry variable was also fixed and verified by
  the same reviewer. The only unchanged Advisory is the pre-existing manual
  synchronization between the two custom-route coverage inventories.
- The final vpsAdmin trust-boundary commit uses proxy-controlled `X-Real-IP`
  with Rack's address as fallback for password-change notices and recovery
  WebAuthn challenges. The production templates render that explicit address,
  and `MailTemplate.register :user_password_changed` declares it. Focused
  regression specs, RuboCop, ERB compilation, and all Overcommit hooks pass.
- The production configuration branch contains three focused commits: the
  exact generated `vpsadminServices` pin, the auth-proxy recovery route, and
  the deployment runbook. The runbook installs templates before upgraded API
  code, deploys both API nodes plus `cz.vpsfree/containers/prg/proxy`, verifies
  the disabled route, lists the exact WebUI/DokuWiki/Discourse authorization
  start URIs, and records rollback. Strict MkDocs validation passes.
- `nix develop -c bin/check` passes at the final KB pin with 42 controls, 34
  paths, 35 capture concepts, 90 bindings, four pages, 12 runtime tests, 21
  executable samples, and all 120 PNGs. Exact-head GitHub Actions are green for
  both KB workflows and for vpsAdmin RuboCop, i18n health, and all API topic
  jobs.
- The final exact-head `./test-runner.sh test 'webui#auth'` passes. The browser
  example completed in 337.88 seconds, the script in 783.87 seconds, and the
  full three-machine test in 1,031.13 seconds with one of one tests successful.
- Final production configuration builds pass independently for
  `cz.vpsfree/vpsadmin/int.api1`, `cz.vpsfree/vpsadmin/int.api2`, and
  `cz.vpsfree/containers/prg/proxy`. No production machine was deployed.
- Updating the existing development service VM initially returned exit 4
  because the configuration worktree had been added after QEMU started: the
  new generation expected a `config` virtiofs mount that the running VM could
  not acquire. The runner was stopped gracefully and restarted with the same
  preserved state, single topology, and bridge network. The new QEMU command
  includes the `config` device, `/mnt/configuration` is mounted, and no systemd
  unit is failed. The documented node `osctld` readiness race was resolved with
  a scoped node update and `devcluster refresh`.
- The running bridge cluster reports ready at exact clean vpsAdmin revision
  `cdbe04cca` (`revisionDirty: false`). API, nginx, WebUI, Mailpit, and the
  password-recovery worker are active. The public form returns HTTP 200 with
  the logo and centered OAuth restart link; WebUI's start URI returns HTTP 302
  to a fresh OAuth authorization.
- The live acceptance fixture is ready without consuming a recovery request:
  `test-user1` and `test-user2` share
  `shared-password-recovery@example.test`; only `test-user1` has account MFA
  enabled and an enabled, confirmed `Acceptance TOTP` device with deterministic
  secret `JBSWY3DPEHPK3PXP`. The unfinished recovery queue is empty and the
  feature flag is enabled.
- Broad exact-head vpsAdmin CI run `32421058486` remains normally in progress
  in its multi-hour integration step. There is no runner-shutdown signal or
  failed attempt to investigate. Superseded in-progress run `32419516057` was
  cancelled; all other current-head workflows have completed successfully.

## Cleanup

- Leave the dev cluster running for user acceptance.
- Remove worktrees only after the feature is merged or abandoned.

## OAuth client completion follow-up (2026-08-21)

- The user approved an explicit per-client completion mode. Discourse must show
  the password-change confirmation before its CSRF-protected Continue page, and
  the later vpsAdmin credentials form must not repeat the confirmation. WebUI
  and both DokuWiki clients keep the current immediate authorization restart.
- Verified the active session slug and clean, remote-matching starting heads:
  vpsAdmin `cdbe04cca`, mail templates `2f6c6573`, KB contracts `cd1936b1`, and
  production configuration `178e3981`. All remotes use SSH, and fetched
  `origin/master` has not advanced beyond any feature branch base.
- Re-read the repository rules and the complete English and Czech user-facing
  writing guidance. Implementation is in progress; production remains
  untouched.
- vpsAdmin now has an additive
  `authorization_start_requires_user_action` OAuth-client setting, defaulting
  to false. Successful recovery always creates the existing client-bound
  completion marker. Clients with the setting enabled first render a localized
  confirmation and continuation button; a second HttpOnly marker bound to the
  same recovery suppresses the alert when authorization later opens. SSO is
  still bypassed once and the normal credential form is always shown.
- The test WebUI client enables the interactive mode so the browser integration
  test and bridge development cluster can exercise the Discourse-style flow.
  Production WebUI and DokuWiki will keep the false default; only Discourse is
  to enable the setting.
- Quick verification on the final source passes: the migration spec has two
  examples, the focused OAuth-client/recovery/OAuth configuration suite has 88
  examples, API i18n health and focused RuboCop pass, both Ruby files and the
  ERB template compile, the Playwright file passes Node syntax checking, the
  Nix seed is formatted, and `git diff --check` is clean. The first application
  suite attempt was incorrectly combined with the migration spec and produced
  the repository's documented database-switch failures; they were rerun in
  separate processes as required.
- The first vpsAdmin commit invocation was attempted outside the Nix shell and
  was rejected by the active hooks because their tools were unavailable. No
  commit was created. The commit was rerun inside `nix develop`; every
  pre-commit and commit-message hook passed. The exact pushed vpsAdmin head is
  `cb3775345e92fc6ced1798a7141b523455fe936d`.
- The KB contract was mechanically repinned to `cb3775345` at all six revision
  sites. `nix flake update vpsadmin` regenerated the lock metadata, and
  `nix develop -c bin/check` passes with 42 controls, 34 paths, 35 capture
  concepts, 90 bindings, four pages, 12 runtime tests, 21 executable samples,
  and all 120 PNGs. The existing unmerged pin commit was amended and pushed as
  `8c77d895dd97cbf0ea734cca6f78f887486c4da0`; no managed page or screenshot
  changed.
- The production configuration branch was rebuilt from its base so it retains
  one generated `confctl inputs channel set --commit vpsadmin vpsadmin`
  commit, now pinning `vpsadminServices` to `cb3775345` with the complete
  feature changelog. The auth-proxy commit remains separate. The amended
  runbook commit records the new per-client boolean, leaves it false for WebUI
  and both DokuWiki clients, enables it only for Discourse, and documents both
  acceptance paths. Strict MkDocs and the active Nixfmt hook pass. The exact
  pushed configuration head is
  `c220e42a0edc4a43dbc6a7a3b7b4e769c084094e`.
- The temporary detached configuration worktree used to generate the clean pin
  from the branch base was removed. Its `.bin`, `.bundle`, and MkDocs `site`
  outputs were transient and were deleted after verification.
- All four affected worktrees are clean and match their remote feature refs.
  Exact heads are vpsAdmin `cb3775345`, mail templates `2f6c6573`, KB contracts
  `8c77d895`, and production configuration `c220e42a`. GitHub Actions on the
  new vpsAdmin and KB heads are running; there are no superseded queued or
  in-progress runs to cancel, and the configuration repository has no branch
  runs.
- The required fresh standalone mandatory review covered all four exact pushed
  ranges and reported no Blocking or Important finding. It independently ran
  the focused OAuth-client/recovery/OAuth configuration suite with 88 examples
  and no failures, verified clean worktrees and exact downstream pins, and
  accepted the latest schema/producer/consumer/UI/test commit as one coherent
  completion protocol. The only Advisory is the pre-existing manual
  synchronization between `custom_routes_coverage_spec.rb` and
  `covered_custom_routes.yml`; all current recovery routes are present and
  request-tested, so it does not block this feature. Residual validation gaps
  are the now-ungated browser integration/bridge deployment and the absence of
  a real Discourse harness for its own CSRF Continue page.
- The final exact-head `./test-runner.sh test 'webui#auth'` passes. The changed
  Playwright authentication example completed in 316.44 seconds, the script in
  754.84 seconds, and the full three-machine test in 1,080.91 seconds with one
  of one tests successful.
- Production configuration builds pass independently for
  `cz.vpsfree/vpsadmin/int.api1`, `cz.vpsfree/vpsadmin/int.api2`, and
  `cz.vpsfree/containers/prg/proxy`. The first `int.api1` invocation reached a
  confirmation prompt in a noninteractive shell and exited before building;
  rerunning with `confctl build -y` succeeded. No production machine was
  deployed.
- The initiative's old disposable bridge-cluster state was reset because the
  unreleased migration was amended. The existing runner did not exit within
  the 120-second grace period, so `devcluster reset` killed it and removed only
  this initiative's VM/database state, sockets, and GC root. A fresh
  single-topology bridge cluster was built from clean vpsAdmin `cb3775345`.
- Fresh startup hit the documented `node1` readiness race: the services seed
  completed just before `/run/osctl/osctld.sock` was republished. The runner
  and VMs remained healthy; once the socket existed, an idempotent
  `devcluster refresh` completed successfully. The cluster reports running and
  ready, with no failed boot or kernel page fault observed.
- Live bridge checks confirm `vpsadmin-api`,
  `vpsadmin-password-recovery`, and nginx are active; the public recovery form
  returns HTTP 200 with the logo; and the WebUI sign-in entry returns HTTP 302
  to a fresh OAuth authorization. The active API unit references exact revision
  `cb3775345e92fc6ced1798a7141b523455fe936d`.
- The fresh acceptance fixture is ready without consuming a request:
  `test-user1` and `test-user2` share
  `shared-password-recovery@example.test`; only `test-user1` has account MFA
  enabled and an enabled, confirmed `Acceptance TOTP` device with deterministic
  secret `JBSWY3DPEHPK3PXP`; the test WebUI client has interactive completion
  enabled; and the unfinished submission queue is empty. The temporary fixture
  script was removed after its assertions passed.
- Exact-head GitHub Actions are green for vpsAdmin API migration specs,
  RuboCop, i18n health, libnodectld, and all API topic jobs, and for both KB
  workflows. Broad vpsAdmin CI run `32461418440` remains normally in progress
  in its multi-hour `Run tests` step; setup and selection steps succeeded and
  there is no runner-death signal. All four worktrees remain clean and match
  their pushed feature refs.

## Metrics and acceptance follow-up (2026-08-21)

- The user approved durable internal recovery/password-change metrics, a
  warning-email alert for the 100-row unfinished queue limit, member-owned
  password/MFA gauges, method-specific MFA instructions, a labelled read-only
  login field, and direct development WebUI completion behavior.
- The active session slug is verified. Clean SSH-backed starting heads are
  vpsAdmin `cb3775345`, mail templates `2f6c6573`, KB contracts `8c77d895`,
  and production configuration `c220e42a`; every feature branch contains the
  current `origin/master` as its base.
- The global exporter already runs only with default API rake tasks every two
  minutes and publishes through node_exporter. The user metrics endpoint has a
  versioned, token-prefixed registry. Password writes converge on
  `User#set_password`, with account creation excluded by the update callback.
- The existing MFA controller already supplies the effective method set on the
  initial page and failed-TOTP retry. The template alone uses generic copy.
- `password_recovery_submissions.user_agent` is cleared after processing and
  retained for at most one day; matched request records are deleted after 30
  days. The permanent deduplicated `user_agents` table has no orphan cleanup,
  so recovery metadata remains a bounded raw snapshot by design.
- The complete user-facing writing guidance and WebUI documentation workflow
  have been read. Mail templates are outside this follow-up. Production
  deployment and KB publication remain prohibited without separate approval.
- vpsAdmin implements fixed-name aggregate event rows for recovery admission,
  queue-capacity transitions, and committed password changes. The base exporter
  emits all planned counters, timestamps, queue gauges, and fixed label values;
  account-owned metrics tokens now expose password generation, forced-reset
  state, account MFA enablement, and enabled TOTP/passkey counts as additive
  metrics contract version 1.1.
- Password changes are classified at `User#set_password` as authenticated,
  forced reset, recovery, administrator, or other. The after-update event write
  shares the password transaction, excludes account creation, and rolls back
  with a failed password update. Queue counters are recorded under the existing
  global admission lock, and the durable capacity event is written exactly when
  the unfinished queue reaches 100.
- The recovery password form now labels an escaped read-only login value while
  retaining autofocus on the new password. Verification guidance is selected
  from the effective method set for TOTP-only, passkey-only, and combined
  accounts in English and Czech, including a failed-TOTP retry. Anonymous
  recovery user agents remain bounded raw snapshots; they are not inserted into
  the permanent `user_agents` dictionary, and this retention distinction is
  documented and tested.
- The development WebUI client now uses direct completion like production
  WebUI and DokuWiki. The browser example expects a fresh OAuth credentials
  form with the successful password-change alert and consumed completion
  markers; the Discourse-style intermediate confirmation remains covered by
  the route suite.
- Quick vpsAdmin verification passes: the new migration up/down spec has two
  examples; the combined event, queue, global exporter, account metrics,
  forced-reset, and recovery-route suite has 55 examples; the broader user
  write/recovery/reset suite ran 76 examples with only its existing pending
  soft-delete case; API i18n update and health, focused RuboCop, Node syntax,
  Nix formatting, and `git diff --check` pass. Initial failures were confined to
  a migration helper's two-argument API, an unavailable `Time.zone` in a test,
  and Czech expectations that had not set `Accept-Language`; each was corrected
  and rerun successfully.
- The exact pushed vpsAdmin head is
  `6eee15df1b68091836bfd3d55100fba38da85d92`. The follow-up is split into
  `d400b9a34` for security metrics, `f983f5a48` for recovery form behavior, and
  `6eee15df1` for the direct WebUI acceptance fixture. Active Overcommit hooks
  passed on all three commits. Superseded broad CI run `32461418440` for the old
  branch head was cancelled after inspecting the run list; exact-head workflows
  are in progress, with migration specs, RuboCop, i18n, and libnodectld already
  green.
- The production configuration adds warning-only alert
  `VpsAdminPasswordRecoveryQueueFull`, with a 15-minute repeat interval and no
  `for`, when the current queue is at its limit or the durable capacity event is
  less than ten minutes old. The runbook now covers the third additive
  migration, both monitoring builds/deployments, exporter checks, and alert-rule
  verification.
- The configuration branch was rebuilt from base `50e8f420` so it retains one
  generated `confctl inputs channel set --commit` pin with the complete
  changelog. Its exact pushed head is
  `eedad5b8e95b6d9c01390c3c8c3325ed0f7949c7`; the generated pin is
  `742dcc5f` and resolves `vpsadminServices` to exact vpsAdmin
  `6eee15df1b68091836bfd3d55100fba38da85d92`. Nixfmt and strict MkDocs pass.
  The detached pin-rebuild worktree and generated `.bin`, `.bundle`, and `site`
  outputs were removed.
- A fresh production KB snapshot contains 114 Czech and 77 English pages. The
  bilingual metrics candidates document all four account security metric
  families and metrics version 1.1, and convert the Czech article to informal
  singular address. Both carry the shared `<page>manuals:vps:metrics</page>`
  language-pair tag exactly once. The all-page annotation checker passes with
  90 bindings and nine exceptions.
- The fresh snapshot also confirmed five previously inventoried Czech pages no
  longer exist and that four published Guix paragraphs moved by one position.
  These independent production-inventory updates are isolated in KB contract
  commit `0257db3`; the exact vpsAdmin mechanical pin is commit `870e3e7`.
  `nix develop -c bin/check` passes at the pushed KB head
  `0257db337c9c1dc7fb35ab27d43326ace827479c` with all 120 PNGs and all contract
  tests.
- Schema-5 manifests are prepared from one bilingual changes file. The Czech
  metrics page is staged with summary `Doplnění metrik zabezpečení účtu a
  neformálního oslovení`; the English page is staged with summary `Document
  account security metrics and clarify metrics setup`. Both staging releases
  verify and interlink at their real page IDs. The staging container remains
  running for review; no production KB write was made.

## Metrics mandatory-review follow-up (2026-08-21)

- The fresh mandatory reviewer identified broad follow-up commits, a stale
  runbook revision, a queue-capacity race between worker completion and
  admission, and exporters that could query the new schema during migration.
  The history was rebuilt into focused commits, every queue transition now
  uses the shared global queue lock, and the runbook masks the base exporter
  timer and service while migrations run.
- Follow-up review then found that daily retention cleanup could delete a
  pending submission outside the queue lock and that the authentication-token
  cleanup timer also queries the recovery tables. Pending retention deletion
  now holds the queue lock and row locks; finished ledgers remain independently
  removable. A deterministic two-connection regression proves cleanup blocks
  behind admission. The focused submission/authentication suite passes with
  20 examples, and all vpsAdmin pre-commit hooks pass.
- The exact pushed vpsAdmin head is
  `e9356b1947648c226e94e34535f8ec42f4e99fdf`. Superseded in-progress CI runs
  for `ee17077e4` were cancelled after the new head was pushed.
- The KB contract is mechanically repinned at all six revision sites. Its
  exact pushed head is `d6dc4d61aff851165621ffecae8807bfb2701e20`;
  `nix develop -c bin/check` passes with all contract tests and 120 PNGs. The
  superseded managed-page runtime run for `5eba9a7` was cancelled.
- The production configuration was rebuilt from base `50e8f420` so the input
  pin remains an unmodified generated `confctl inputs channel set --commit`
  commit. The runbook now pins `e9356b194`, masks and unmasks both
  `vpsadmin-api-auth-tokens` and base-exporter timer/service units around the
  migration, and starts and verifies both timers afterward. Its exact pushed
  head is `5fbfb40612401572a23b13184d15887b9b03ec1f`. The active Nixfmt hooks and
  `nix shell nixpkgs#mkdocs --command mkdocs build --strict` pass. A first
  attempt through the repository dev shell failed because that shell does not
  provide MkDocs; the explicit Nix package command is the working invocation.
- The same standalone reviewer is being asked to verify these exact final
  heads and confirm that every prior Blocking or Important item is resolved
  before long integration tests begin.
- The standalone reviewer completed the exact-head follow-up with no Blocking,
  Important, or Advisory findings. All earlier findings are resolved, including
  strict commit splitting, queue-lock ordering for every pending-state
  transition, dry-run cleanup behavior, exact downstream pins, and migration
  masking for both schema-dependent timers and services. The reviewer found no
  production lock-order inversion and approved proceeding with long
  integration verification. Remaining gaps are the planned exact-head WebUI
  suite, five production configuration builds, bridge-cluster refresh, and
  live exporter/alert checks; real Discourse behavior remains covered only at
  route level.
- The final exact-head `./test-runner.sh test 'webui#auth'` integration passes.
  The Playwright example completed in 329.77 seconds, the script in 793.82
  seconds, and the full three-machine test in 1,037.47 seconds with one of one
  tests successful.
- All five release configurations build successfully with `confctl build -y`:
  `cz.vpsfree/vpsadmin/int.api1`, `cz.vpsfree/vpsadmin/int.api2`,
  `cz.vpsfree/containers/prg/proxy`, `cz.vpsfree/containers/prg/int.mon1`, and
  `cz.vpsfree/containers/prg/int.mon2`. Prometheus rule checking is part of the
  monitoring builds. No production machine was deployed.
- The old disposable bridge cluster was reset because it ran the prior feature
  revision. Its runner again exceeded the 120-second graceful-stop timeout, so
  the wrapper killed only this initiative's runner and removed only its GC root,
  VM, and database state. A fresh single-topology bridge cluster was built from
  exact clean vpsAdmin `e9356b194`.
- Fresh bootstrap hit the documented `node1` readiness race after the seed
  completed but before `/run/osctl/osctld.sock` was republished. The VMs and
  services remained healthy; the socket appeared, a scoped `devcluster update
  ... node1` succeeded, and `devcluster refresh` completed cleanly. The cluster
  reports running and ready on the bridge network with no failed units or
  observed kernel page fault.
- Live API and password-recovery worker `ExecStart` paths contain exact
  `e9356b194`. The recovery form returns HTTP 200 with the configured logo, the
  WebUI authorization start returns HTTP 302 to a fresh OAuth request, and API,
  worker, nginx, and the exporter timer are active.
- The shared-email acceptance fixture is restored without consuming a recovery
  request. `test-user1` and `test-user2` use
  `shared-password-recovery@example.test`; only `test-user1` has account MFA
  enabled and an enabled, confirmed `Acceptance TOTP` device with deterministic
  secret `JBSWY3DPEHPK3PXP`. WebUI direct completion and recovery are enabled,
  and the unfinished submission queue is empty.
- A live base-exporter run completed successfully and deployed metrics to
  `/run/metrics/vpsadmin-base.prom`. It contains every fixed password-recovery
  admission result, unfinished depth `0`, queue limit `100`, capacity event,
  and every fixed password-change source counter/timestamp.
- Exact-head vpsAdmin RuboCop, i18n, and API topic workflows are green. Both
  exact-head KB workflows are green. The broad vpsAdmin CI workflow remains
  normally in progress; no runner-shutdown or failure signal is present.
- A follow-up is in progress to add password visibility controls to the
  recovery password form. The OAuth forced-password-change form already reveals
  both new-password fields together; it needs regression coverage but no
  functional change. The planned recovery control is self-contained, accessible
  from a keyboard, bilingual for assistive technology, masked by default, and
  does not change schema or API behavior.
- The recovery visibility follow-up is committed in vpsAdmin as `2c446a17f` on
  `2026-08-18-vpsadmin-password-reset`. Both fields remain masked by default;
  either keyboard-accessible eye button reveals or masks them together and
  updates the localized assistive label. The existing forced-reset toggle is
  unchanged and now has explicit regression assertions.
- Focused recovery and OAuth specs pass with 65 examples. API i18n update and
  health, focused RuboCop, Node syntax, Nixfmt, and diff checks pass. The first
  commit attempt was stopped because the ambient shell lacked the hook tools;
  the commit was rerun from the full repository Nix shell and every declared
  pre-commit hook passed. The long WebUI integration test is pending the
  mandatory fresh-agent review.

## Password visibility completion (2026-08-21)

- The standalone mandatory reviewer initially raised one accessibility
  Advisory: a changing Show/Hide accessible label should not also use the ARIA
  toggle-button `aria-pressed` state. The recovery controls now keep the
  changing bilingual labels, remove `aria-pressed`, and use `data-visible` only
  for visual state. The same reviewer rechecked exact base `e9356b194` and
  exact head `00674913d` and reported no Blocking, Important, or Advisory
  findings. The one-commit split remains appropriate.
- The final exact pushed vpsAdmin head is
  `00674913d112dd6a4ad3ae87a749f8da383e3aab`. Either eye button reveals or
  masks both recovery password fields together; fields start masked; labels
  are `Show passwords` / `Hide passwords` and `Zobrazit hesla` / `Skrýt hesla`.
  The existing OAuth forced-password-change form remains unchanged and has
  explicit regression coverage for its synchronized visibility controls.
- Focused recovery and OAuth specs pass with 65 examples before the review
  fix, and the directly affected post-fix example passes independently. The
  final amended commit ran every declared pre-commit hook successfully in the
  full Nix shell: migration specs, Nixfmt, WebUI i18n, RuboCop, and API i18n.
  Node syntax, diff checks, and commit-message formatting also pass.
- The exact-head `./test-runner.sh test 'webui#auth'` integration passes. The
  changed Playwright browser example completed in 319.6 seconds, the script in
  661.23 seconds, and the full three-machine test in 890.18 seconds with one of
  one tests successful. It verifies masked initial state, synchronized field
  types and assistive labels, both toggle controls, and the existing forced
  reset behavior. No kernel page fault was observed.
- The KB feature history was rebuilt from `c1d0aca` so it contains one exact
  mechanical pin commit followed by the independent production-navigation
  inventory refresh. All six pin sites resolve vpsAdmin `00674913d`; the exact
  pushed KB head is `9298febb013b0b06d3e47a66c7c5a6e054b66fe5`.
  `nix develop -c bin/check` passes with all contract tests and all 120 PNGs.
  The recovery visibility control is not a managed KB screenshot concept, so
  no page or screenshot content changed.
- The production configuration history was rebuilt from `50e8f420` so it
  retains one unmodified generated `confctl inputs channel set --commit` pin.
  Generated pin commit `0b7dba68` and the runbook both use exact vpsAdmin
  `00674913d`; the exact pushed configuration head is
  `5012ebb631f9bfb947f674a8bef6daeae0cb7419`. Nixfmt and strict MkDocs pass.
  All five release configurations build successfully with
  `confctl build -y`: both API machines, the auth proxy, and both monitoring
  containers. No production machine was deployed.
- The first configuration push was stopped by its pre-push hook because the
  ambient shell lacked the locked Ruby gems. Rerunning the exact push through
  `nix develop` let the declared hook execute and the guarded force-with-lease
  push succeeded. Generated `.bin`, `.bundle`, and `site` outputs and both
  detached pin-rebuild worktrees were removed.
- The existing ready bridge cluster was updated in place with
  `devcluster update ... services`; its database was not reset. The old
  stateless console router did not finish Puma's graceful shutdown, so systemd
  used the unit's configured five-minute stop timeout and continued activation.
  An independent read-only investigation matched this to Puma shutdown-pipe
  race `puma/puma#3677`, fixed upstream by pull request `#3940` and merge commit
  `515987476202e0bd6faf5f14ba9838fdf088b5d5`. Deployed Puma 8.0.2 predates the
  fix. The old PID received no dynamic console requests, so neither vpsAdmin's
  router/Bunny connection nor systemd caused this incident. The recommended
  follow-up is an exact upstream backport in the shared Puma derivation plus
  Puma's concurrency tests and a service stop/start smoke test. The evidence,
  temporary workaround, production exposure, and proposed coverage are in
  `notes/vpsadmin/2026-08-21-devcluster-console-router-stop.md`.
- The bridge cluster is again running and ready with zero failed services.
  API, password-recovery worker, and console-router `ExecStart` paths all
  contain exact revision `00674913d`. The public auth recovery form returns
  HTTP 200 and its deployed stylesheet contains the new password-visibility
  controls. The shared-email/TOTP acceptance state was preserved.
- Exact-head vpsAdmin RuboCop and i18n workflows and both KB workflows are
  green. API topic specs and broad vpsAdmin CI are still in progress. Obsolete
  broad CI run `32480959677` for vpsAdmin `e9356b194` was cancelled; no
  current-head run was cancelled.
