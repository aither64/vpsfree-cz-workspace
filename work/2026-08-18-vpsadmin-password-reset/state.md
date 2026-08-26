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
- Password-change client auditing started at clean, pushed heads vpsAdmin
  `5a61d5698deff70fea385bb620c6bb24b9a88597`, KB contracts
  `39f2b827cf2c91a03e276bd95e04ed7c7f243aac`, production configuration
  `304799867315efa42ad9367cca3e62fd0c77d41e`, and mail templates
  `a71b329b91acb38d24e19d8dda9512537253e901`. The mail templates are not
  expected to change.
- Accepted follow-up decisions: snapshot IP, server-resolved PTR, and normalized
  user agent on every detailed event; attach required-reset sessions only when
  real token or OAuth session creation succeeds; and render client metadata in
  a wrapping full-width detail row rather than new horizontal table columns.
- Password-change history follow-up started at vpsAdmin
  `00674913d112dd6a4ad3ae87a749f8da383e3aab`, KB contracts
  `9298febb013b0b06d3e47a66c7c5a6e054b66fe5`, and production configuration
  `5012ebb631f9bfb947f674a8bef6daeae0cb7419`; all three feature worktrees were
  clean and matched their SSH upstream branches before editing.
- Decisions for the follow-up: keep global counters, store a nullable exact
  user-session relation, allow owners and administrators to read history,
  prune detailed rows at hard deletion, leave the worker unchanged, and retain
  the existing rolling production deployment with its short measurable audit
  gap.
- The ambient-shell Overcommit version check failed because the required bundle
  is available only inside the repository Nix shell. The existing durable
  Overcommit/Nix-shell note applies; hooks will be verified and run from
  `nix develop .#vpsadmin` before committing.
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
  upstream backport was considered, but the operator chose to tolerate the
  intermittent forced shutdowns and wait for a Puma release containing the
  merged fix. That future dependency update should carry Puma's concurrency
  tests and a service stop/start smoke test. The evidence, operational
  decision, production exposure, and proposed coverage are in
  `notes/vpsadmin/2026-08-21-devcluster-console-router-stop.md`.
- The bridge cluster is again running and ready with zero failed services.
  API, password-recovery worker, and console-router `ExecStart` paths all
  contain exact revision `00674913d`. The public auth recovery form returns
  HTTP 200 and its deployed stylesheet contains the new password-visibility
  controls. The shared-email/TOTP acceptance state was preserved.
- Exact-head vpsAdmin API topic specs, RuboCop, and i18n workflows and both KB
  workflows are green. Broad vpsAdmin CI remains normally in its multi-hour
  `Run tests` step; setup, selection, and preview succeeded, and there is no
  runner-loss signal. Obsolete broad CI run `32480959677` for vpsAdmin
  `e9356b194` was cancelled; no current-head run was cancelled.

## Password change history follow-up (2026-08-21)

- Work started from clean pushed vpsAdmin `00674913d`, KB contracts
  `9298febb0`, and production configuration `5012ebb63` on the existing
  initiative branches and worktrees.
- The API follow-up adds an unbackfilled `password_change_logs` table. Each
  persisted password update records the target user, source, timestamp, and
  exact initiating user session when one exists. Recovery and required-reset
  changes deliberately have a null session. Existing global event counters
  remain unchanged and detailed rows are pruned when the target user is hard
  deleted.
- The read-only API lets members list and show only their own history and lets
  administrators list, show, and filter all history. Members receive the exact
  numeric session ID but not the related session object, so an administrator's
  session metadata is not exposed. The additive API surface is not yet added
  to `vpsadmin-go-client`; existing clients ignore it.
- The WebUI adds a localized `Password changes` profile-sidebar entry and a
  paginated history table with change time, localized source, and session.
  Administrators can follow every session link; members can follow only their
  own sessions, while administrator-session IDs remain plain text.
- Focused ordinary API regression coverage passes with 42 examples, including
  authenticated, administrator, recovery, required-reset, authorization,
  pagination, rollback, and hard-delete behavior. The migration spec passes
  independently with 2 examples. It must not be combined in the same RSpec
  process with ordinary specs because the migration helper intentionally
  switches Active Record to `vpsadmin_test_migration`.
- API i18n health and focused RuboCop pass. WebUI gettext health passes with
  only the two pre-existing embedded-URL warnings, focused PHPUnit passes with
  5 tests and 13 assertions, and PHP CS Fixer reports no changed files.
- The implementation is committed as two independently reversible vpsAdmin
  commits: API/schema/audit behavior `1b180f23f` followed by localized WebUI
  presentation `23cb768cf`. Every declared pre-commit and commit-message hook
  passed for both final commits. The worktree is clean.
- The KB contract history was rebuilt from `c1d0aca` so it still has one exact
  mechanical pin commit. All six pin sites use vpsAdmin `23cb768cf`; semantic
  control `member.password-changes` and path
  `member.password-changes.open` describe the localized profile navigation.
  The exact clean, pushed KB head is `9bfd65f48`. Full `nix develop -c
  bin/check` passes with 43 controls, 35 paths, 92 KB bindings, and all 120
  existing PNGs. A new screenshot was deliberately omitted because the audit
  table is simple and the documentation can identify it deterministically by
  its semantic path.
- Fresh production sources for `navody:vps:uzivatele` and
  `manuals:vps:users` were fetched read-only into `kb-sources-history`.
  Bilingual candidates in `kb-candidates-history` add a concise password
  change history section with the semantic navigation tag. The standalone
  reviewer verified that tag against the exact semantic contract. Running the
  all-page annotation checker on this history-only candidate reports unrelated
  metrics-page inventory drift because the contract already describes the
  separately staged metrics candidate while this source remains the production
  baseline; the earlier complete metrics candidate passed that all-page check.
  Checksummed schema-5 staging manifests are
  `kb-release-history-cs.yml` and `kb-release-history-en.yml`; no production
  KB write has been made.
- The production configuration history was rebuilt from `50e8f420` so it
  retains one unmodified generated `confctl inputs channel set --commit` pin.
  Generated commit `df1c1bcd` pins `vpsadminServices` to exact vpsAdmin
  `23cb768cf`. Runbook commit `8f9c6ee4` adds the fourth migration, both WebUI
  hosts, the accepted brief mixed-version audit gap, owner/admin privacy
  checks, and detailed-history rollback behavior. Strict MkDocs, diff checks,
  and every declared hook pass. The exact clean, pushed configuration head is
  `8f9c6ee491689c535d7a58f420a67085e8dcd676`.
- The first exact-head API topic workflow `32519458283` failed only its endpoint
  coverage shard because `password_change_log#index` and
  `password_change_log#show` were missing from `covered_endpoints.yml`. The
  failed job log was inspected at `/tmp/vpsadmin-coverage-job-96888291709.log`;
  the precise missing scopes were added before rerunning CI. The superseded
  long CI run `32519458340` was cancelled after the corrected force-push.
- The mandatory reviewer also reproduced a session-attribution defect in
  transparent old-password-hash upgrades: their direct password update logged
  source `other` without the current session. Password updates with no explicit
  audit context now use `UserSession.current`, while an explicit nil context
  remains authoritative for recovery and required-reset flows. The API exposes
  a derived, read-only ownership flag so members can link any initiating session
  belonging to their account without inferring authorization from the source
  label; administrator session details remain hidden.
- Remediation coverage includes the endpoint registry, model ownership cases,
  transparent-rehash session attribution, owner serialization, WebUI source
  independence, and a Playwright assertion that both signed-in changes appear
  as the two newest matching rows with authorized session links. The assertion
  deliberately avoids total row counts so it remains repeatable with the
  append-only, paginated history in the preserved development database.
  Focused API specs pass with 22 examples;
  RuboCop, API i18n health, focused PHPUnit (2 tests, 9 assertions), PHP CS
  Fixer, JavaScript syntax, diff checks, and every declared commit hook pass.
  The same standalone reviewer rechecked exact pushed vpsAdmin `23cb768cf`, KB
  `9bfd65f48`, and configuration `8f9c6ee49` after the repeatability correction
  and reported no Blocking, Important, or Advisory findings. An independent
  malicious-include proof also confirmed that members retain the numeric
  administrator-session ID and false ownership flag without receiving the
  protected session relation (23 focused examples, no failures). The reviewer
  approved proceeding with long integration testing.
- The exact-head `./test-runner.sh test 'webui#users-self-service'` integration
  passes. Its Playwright example completed in 421.52 seconds, the selected
  script in 906.25 seconds, and the complete three-machine test in 1,168.85
  seconds with one of one tests successful. This exercises the password-change
  history page twice against the live API and verifies both newest signed-in
  rows link to their initiating sessions.
- All seven production release configurations build successfully and no
  production machine was deployed: both API hosts, both WebUI hosts, the auth
  proxy, and both monitoring hosts. The monitoring builds include Prometheus
  rule validation. Strict MkDocs also passes, and generated `.bin`, `.bundle`,
  and `site` residue was removed after the checks.
- The existing single-topology bridge cluster was updated in place to exact
  vpsAdmin `23cb768cf`; its database and acceptance fixtures were preserved.
  The shared vpsAdminOS staging input advanced to `5d74cb39c` during closure
  evaluation, so the update rebuilt the affected OS services as well. The
  service switch completed without the tolerated Puma shutdown race, the
  wrapper refreshed the node runtime, and the cluster reports running and
  ready with no failed units.
- The live API, password-recovery worker, and console-router `ExecStart` paths
  all contain exact revision `23cb768cf`, and their services plus the base
  exporter timer are active. Schema migration `20260821210000` is the current
  maximum; the preserved database contains the new audit table and four detail
  rows. A member API request returns only its two rows with the ownership flag
  and no serialized session relation.
- A fresh live base-exporter run reports ten monotonic `other` password-change
  events while only four detailed rows remain, confirming that the retained
  aggregate counter is independent of detailed-log retention. All fixed source
  labels remain exported for both the counter and last-change timestamp.
- Both history manifests were staged and verified at their real Czech and
  English page IDs. Verification exposes the localized summaries and revision
  histories at the two review wikis. The staging container remains running;
  no production KB write was made.
- Exact-head KB `Check` and `Managed page runtime`, vpsAdmin WebUI PHPUnit, and
  vpsAdmin i18n workflows are green. Exact-head broad CI run `32525960380`
  remains normally active in its `Run tests` step with setup, selection, and
  preview green; no runner-loss signal is present.

## Expired recovery page follow-up (2026-08-22)

- Work starts from clean pushed vpsAdmin `23cb768cf`, KB contracts
  `9bfd65f48`, and production configuration `8f9c6ee49` in the existing
  initiative worktrees. The environment and `bin/dev-session current` both
  identify `2026-08-18-vpsadmin-password-reset`.
- A password form left open until the cookies expire submits without the CSRF
  cookie. `PasswordRecovery#verify_csrf!` handles that before recovery-session
  lookup and calls Sinatra `halt` with a string, which explains the observed
  plain-text response. Ordinary invalid-session paths already use the branded
  HTML template but do not offer recovery actions.
- The accepted behavior is a branded failure page with a primary request-new-
  link action and an optional configured OAuth sign-in link. Public client and
  locale context will survive the flow; stored OAuth client configuration stays
  authoritative and no arbitrary redirect URL will be accepted.
- Upstream fetches completed over SSH. vpsAdmin and KB are based on current
  `origin/master`; production configuration is 12 upstream commits behind and
  will be rebased before its exact channel pin is updated.
- vpsAdmin commit `5ce685e75` renders every browser-facing invalid recovery
  state inside the branded card. It keeps the recovery token in the fragment,
  preserves the public OAuth client ID and locale, and resolves continuation
  links only from stored client configuration. WebAuthn CSRF failures remain
  structured JSON responses.
- The initial route-focused checks passed. Focused RuboCop, API i18n health,
  Ruby/ERB syntax, Playwright JavaScript syntax, and diff checks pass. Browser
  coverage now clears the form cookies before submission and verifies the
  branded failure, exact restart URL, configured WebUI sign-in URL, logo, and
  retained locale. Every declared vpsAdmin commit hook passed and exact pushed
  head is `5ce685e75dc0b30be49366b4e559bad3fd1fdfd3`.
- The KB contract has no managed control or screenshot for the OAuth recovery
  page, so only its six exact vpsAdmin revision sites changed. Full
  `nix develop -c bin/check` passes with 43 controls, 35 paths, 92 bindings,
  four pages, 12 runtime tests, 21 executable samples, and all 120 PNGs. Exact
  clean pushed KB head is `c1a12b72f0718d9ff9b1b51a0e0f86b0c68e6896`.
- The configuration branch was rebased onto current `origin/master` before the
  service pin was regenerated. The first rebase attempt could not run the
  updated hook bundle because upstream added `rubyzip`; installing the locked
  bundle inside `nix develop` restored the declared hooks. Generated commit
  force-with-lease push succeeded and generated `.bin`/`.bundle` residue was
  removed.
- The fresh mandatory review found that pre-lookup CSRF failures could use a
  conflicting known client and locale from the query even when the submitted
  email token or flow cookie identified a persisted recovery. It also required
  consolidation of the two superseding configuration pin commits and asked for
  rendered Czech/link-level browser coverage.
- CSRF failure handling now performs only a non-mutating recovery lookup from
  the submitted email token or flow cookie, uses its stored client and locale
  when identifiable, and still falls back to the validated query context when
  all cookies are gone. Regressions use two real clients with conflicting
  parameters for both email-token exchange and an established recovery
  session. A Czech Playwright case now follows an invalid fragment token to the
  branded failure page and checks both recovery actions. Focused route/model
  specs pass with 34 examples; focused RuboCop, Ruby syntax, Node syntax, diff
  checks, and every declared commit hook pass.
- Configuration history was rebuilt from current `origin/master` with one
  unmodified generated `confctl` input commit, `ac550b89`, directly from
  `b3d63c00` to exact vpsAdmin `5ce685e75`. The final revision checks were
  folded into the password-history runbook commit instead of retained as a
  fixup. Exact clean pushed configuration head is
  `9709165ea9269a9436f4d7d6d82bd550ec894cad`.
- The exact-head recheck found one remaining presentation edge: invalidated
  email tokens still identify their persisted request, but the context lookup
  used the active-only exchange scope. Presentation now uses an including-
  inactive digest lookup while a separate active lookup and locked usability
  check continue to authorize exchange. A conflicting-client Czech regression
  verifies the invalidated row is not mutated and the original actions remain.
- The same standalone reviewer rechecked exact pushed vpsAdmin `5ce685e75`, KB
  `c1a12b72`, and configuration `9709165e` and reported no Blocking,
  Important, or Advisory findings. The application commit, mechanical KB pin,
  single generated configuration pin, and four hand-written configuration and
  runbook commits are focused; the reviewer approved proceeding to the planned
  integration, build, strict-documentation, and bridge-cluster gates.
- Strict MkDocs passes. All seven affected production configurations build
  successfully without deployment: both API hosts, both WebUI hosts, the auth
  proxy, and both monitoring hosts. The monitoring builds validate the
  Prometheus configuration and rules. Generated `.bin`, `.bundle`, and `site`
  outputs were removed after verification.
- Exact-head `./test-runner.sh test 'webui#auth'` passes. The Playwright
  example succeeded in 337.81 seconds, the selected script in 669.65 seconds,
  and the complete three-machine test in 928.41 seconds with one of one tests
  successful. It exercises the stale-form recovery failure and the new Czech
  invalid-link browser path against the live auth frontend.
- The existing single-topology bridge development cluster was updated in place
  to exact vpsAdmin `5ce685e75`; the database and acceptance fixtures were
  preserved. Its shared vpsAdminOS staging input advanced to `3bf14ec67` while
  evaluating the updated closure. The switch completed without the tolerated
  Puma console-router shutdown race, and the cluster reports running and ready
  with no failed units.
- The live API, password-recovery worker, and console-router services are all
  active, and each `ExecStart` path contains exact vpsAdmin revision
  `5ce685e75`. A direct stale-form submission through the live auth frontend
  returns HTTP 400 with the logo, explanatory recovery-session error, primary
  `Request a new link` action, centered configured WebUI sign-in link,
  `Cache-Control: no-store`, and the restrictive recovery-page CSP. The cluster
  remains running for user acceptance testing.
- Exact-head KB `Check` and `Managed page runtime`, vpsAdmin RuboCop, and
  vpsAdmin i18n workflows are green. The exact-head broad vpsAdmin CI and API
  topic workflows remain normally in progress after the dev-cluster acceptance
  gate passed; superseded runs were cancelled after each force-push.

## Default OAuth client follow-up (2026-08-23)

- User acceptance found that a queryless recovery submission reaches the
  **Check your email** page without a sign-in link. The template already shows
  the link when an OAuth client is known; live database evidence shows the
  latest direct submission had `oauth2_client_id = NULL`.
- The accepted design adds a general `Oauth2Client#is_default` role instead of
  a password-recovery-specific system setting. Password recovery uses the
  default WebUI client only when no persisted or explicit valid client exists,
  and stores it as the context for the complete flow.
- The live `test-user1` account has an enabled and confirmed `Acceptance TOTP`
  device, but the last service update reran the generic seed and reset
  `enable_multi_factor_auth` to false. The acceptance step will restore only
  that development account flag after deploying the corrected revision.
- vpsAdmin commit `fdaf8c41a` adds nullable `oauth2_clients.is_default` with a
  unique index and an atomic API switch. Explicit and persisted OAuth clients
  remain authoritative; a valid default is used only when neither exists and
  is stored on new queryless recovery submissions. The default must have a
  safe authorization start URI, can be cleared, and serializes as false while
  stored as NULL when unselected.
- Focused recovery and OAuth-client specs pass with 62 and 29 examples. The
  migration spec passes independently with two examples. Focused RuboCop, API
  i18n health, Nixfmt, JavaScript syntax, diff checks, and every declared
  vpsAdmin commit hook pass. The exact clean pushed vpsAdmin head is
  `fdaf8c41a8b1f626098c2979884982aff073ae7e`.
- The KB contract is mechanically repinned at all six revision sites. Its full
  `bin/check` suite passes with 43 controls, 35 paths, 92 bindings, and all 120
  PNGs. No managed page, semantic control, or screenshot changed. The exact
  clean pushed KB head is `08201ee082f4cb4b3d4b9f93fb907191ab84b8f9`.
- The production configuration history was rebuilt on current `origin/master`
  `1adf7d860` so it contains one generated `confctl` input commit, followed by
  the independent proxy, monitoring, and consolidated runbook commits. It pins
  `vpsadminServices` to exact `fdaf8c41a`, lists all five migrations, and marks
  only the production WebUI OAuth client as default. The active Nixfmt hook and
  strict MkDocs pass. The exact clean pushed configuration head is
  `10a27311167e3063c59a8b82a90a27ded2b20976`; no production host was deployed.
- The shared development seed remains backward compatible with older vpsAdmin
  revisions and now marks WebUI as default whenever the new model API is
  available. Its Nix formatting check passes. Deployment to the preserved
  bridge cluster and restoration of the `test-user1` MFA flag remain pending
  until the mandatory review completes.

### Mandatory review corrections

- The standalone reviewer found that OAuth client updates loaded the target
  before entering the default-switch transaction. A stale target could clear a
  newer default or remove the start URI from a client that had meanwhile
  become default. The corrected model locks all OAuth clients in ID order,
  reloads the target, applies the explicit update, validates the current state,
  and then switches the default. Clearing the former default now also updates
  its exposed `updated_at` timestamp.
- Deterministic regressions cover both reproduced stale schedules and an
  explicit stale `is_default: false` update. The complete OAuth client resource
  spec passes with 32 examples and focused RuboCop is clean. All vpsAdmin
  pre-commit and commit-message hooks ran; the corrected pushed vpsAdmin head
  is `8ba310cbbc9af272f1c258ac0f68c5d6f844bfac`.
- The reviewer also found that an older model can see the retained
  `is_default` column without supporting atomic switching. Shared development
  seed commit `2875597ab28a78609d0a6c94c64baf9ac9d15fa2` now assigns the flag only
  when `save_with_default!` is available. Its Nix formatting check passes.
- The failed prior-head API topic-coverage log was inspected before accepting
  a replacement run. It showed that the earlier password history resource
  spec was never assigned to a topic. Focused vpsAdmin commit `8ba310cbb` maps
  it to `users-auth`; the remaining superseded prior-head CI run was cancelled.
- The KB contract is repinned at all six sites to exact vpsAdmin `8ba310cbb`.
  Its full check still passes with 43 controls, 35 paths, 92 bindings, and all
  120 PNGs. The corrected clean pushed KB head is
  `20b8d77a8c0af3e8f5a09720945861d81f9e26d1`.
- The production configuration series was rebuilt on `origin/master`
  `1adf7d860` so it again contains one generated `confctl` pin followed by the
  focused proxy, monitoring, and runbook commits. The lock and both runbook
  checks use exact vpsAdmin `8ba310cbb`; the corrected clean pushed head is
  `cd3130e3b4abd6adbb9f7b6846288dc21cd2a874`. No production host was deployed.
- The same standalone reviewer rechecked the corrected exact heads and reported
  no remaining Blocking, Important, or Advisory findings. The reviewer also
  independently reran the 32-example OAuth client spec and reconstructed the
  topic mapping: all 399 non-migration API specs map exactly once, with the
  password history spec only in `users-auth`. The reviewer accepted every
  corrected commit boundary and exact downstream pin. Long integration tests,
  production configuration builds, and development-cluster deployment can now
  proceed.

### Final integration and development deployment

- Exact-head `./test-runner.sh test 'webui#auth'` passes. The Playwright
  example completed in 365.65 seconds, the selected script in 729.53 seconds,
  and the complete three-machine test in 995.29 seconds with one of one tests
  successful.
- All seven affected production configurations build successfully without
  deployment: both API hosts, both WebUI hosts, the auth proxy, and both
  Prometheus hosts. The monitoring builds validate the generated Prometheus
  rules and configuration. The first non-interactive batch stopped before any
  build because confirmation was not enabled; rerunning the same serial batch
  with `confctl build --yes` passed. Generated `.bin` and `.bundle` residue was
  removed.
- Current-head vpsAdmin API topic workflow `32635630952` passes, including
  exact topic coverage and the `users-auth` shard. Both current-head KB
  workflows pass. All active superseded vpsAdmin runs were cancelled after
  their replacement heads were pushed; the prior topic-coverage failure was
  inspected and fixed rather than rerun unchanged.
- The existing single-topology bridge development cluster was updated in place
  to exact vpsAdmin `8ba310cbb`; its database and acceptance fixtures were
  preserved. Closure evaluation advanced the shared vpsAdminOS staging input
  to `80a0017d7`. The switch completed without the tolerated Puma console-router
  stop race, and the cluster reports running and ready with no failed units.
- Live API, password-recovery worker, and console-router `ExecStart` paths all
  contain exact vpsAdmin revision `8ba310cbb` and the three services are active.
  Migration `20260823100000` is the current maximum.
- The development WebUI client `vpsadmin-webui-test` is the sole default and
  retains start URI
  `https://webui.aitherdev.int.vpsfree.cz/?page=login&action=login`.
  `test-user1.enable_multi_factor_auth` was restored to true; its `Acceptance
  TOTP` device ID 1 remains enabled and confirmed.
- A live queryless recovery GET returns HTTP 200. A submission for a unique
  unknown address returns HTTP 303 to `/oauth2/password-reset/sent` with
  `client_id=vpsadmin-webui-test`; the rendered page contains **Check your
  email** and the configured WebUI **Back to sign in** link. Following that
  link reaches a fresh OAuth authorization for `vpsadmin-webui-test`.
- The bridge development cluster remains running for user acceptance. No
  production host was deployed and no production KB page was published.

## Password reset and history UI follow-up (2026-08-23)

- User acceptance requested labelled forced-reset fields with a read-only
  login, administrator attribution in password-change history, a five-second
  idle worker poll, and consistent Czech use of `Login` for the account
  identifier. The accepted follow-up also makes the development seed skip an
  unchanged password and cleans only the seed-generated development audit rows.
- The existing initiative and project worktrees were verified clean before
  editing. vpsAdmin starts at exact pushed revision `8ba310cbb`, production mail
  templates at `2f6c657`, KB contracts at `20b8d77`, and production
  configuration at `cd3130e`. The preserved bridge cluster is running exact
  vpsAdmin `8ba310cbb`; production deployment and KB publication remain out of
  scope.
- vpsAdmin now has four focused local commits: `026869a8e` labels the trusted
  OAuth forced-reset fields, `b8b5923c5` attributes administrator password
  changes, `ab2880105` changes only the idle worker poll to five seconds, and
  `e67572ca2` corrects Czech `Login` terminology and embedded templates. Every
  commit passed the installed Overcommit pre-commit and commit-message hooks
  from the root Nix development shell.
- Production mail-template commit `c21e186` applies the same Czech `Login`
  label without changing either automated-mail footer. Shared workspace commit
  `fa7a295` makes unchanged development passwords a seed no-op. Neither change
  affects production state on its own.
- Focused API verification passes with 102 examples and no failures across the
  OAuth form, password-change resource, worker, recovery routes, and embedded
  templates. Focused RuboCop is clean. Full WebUI PHPUnit passes with 86 tests
  and 364 assertions; gettext health, PHP CS Fixer, JavaScript syntax, Nix
  parsing/formatting, and all 16 CI-selection tests pass.
- The first commit attempt was correctly rejected because Overcommit was run
  outside the root Nix shell and could not find its declared tools. Repeating
  it through `nix develop` ran every mandatory hook successfully. A separate
  reusable note records the unrelated `tools/test-db status` NameError seen
  after the automated test database had stopped.

### Password reset UI follow-up mandatory review

- A fresh standalone reviewer found no behavioral, security, compatibility,
  deployment, or user-facing-copy defects in the exact pushed vpsAdmin, mail
  template, or development-seed revisions. The reviewer independently reran
  the three highest-risk API specs: 56 examples passed with no failures.
- The reviewer classified shared-workspace commit `6a85deb` as a commit-split
  failure because it combined this initiative's plan/state update with an
  unrelated reusable test-database troubleshooting note. This finding is
  accepted rather than rewritten: the commit is already published on the
  shared `master`, whose history must remain linear and must not be rewritten
  out from under concurrent sessions. The note is a valid durable workspace
  lesson and neither part changes product behavior, so deleting and re-adding
  it would add churn without repairing the published boundary.
- Future unrelated reusable lessons will be committed separately from
  initiative tracking, even when the lesson is discovered during that
  initiative. This dedicated follow-up records the review disposition before
  downstream repins, integration tests, and development deployment proceed.

### Password reset UI follow-up integration and deployment

- The KB contract is pinned at all six revision sites to exact vpsAdmin
  `e67572ca27952f977603f570ca23961bd3bc9ebf`. Its complete `bin/check` suite
  passes with 43 controls, 35 paths, 92 bindings, and all 120 PNGs. No managed
  page, semantic control, or screenshot changed. The clean pushed KB head is
  `6ca3a0698bebed1042ebd15039626ea158deb6e8`; no KB page was published.
- The production configuration input was updated with `confctl` to exact
  vpsAdmin `e67572ca`; the deployment runbook now names that revision and
  exact mail-template revision `c21e186c72299db573c3ed16e0bc33df3c460731`.
  Nixfmt hooks and strict MkDocs pass. The clean pushed configuration head is
  `c7346294e5f8ed425c4c359ce8d33b53898faa49`.
- Two incorrect `confctl inputs channel set` invocations used the flake input
  name where the channel/role mapping was required and made no changes. The
  corrected mapping is `vpsadmin vpsadmin`; a separate reusable note records
  the discovery. An ambient-shell push was also rejected by the repository
  hook because its pinned gems were absent; the same push passed from the Nix
  development shell. Generated `.bin`, `.bundle`, and `site` outputs were
  removed after verification.
- All seven affected production configurations build successfully without
  deployment: both API hosts, both WebUI hosts, the auth proxy, and both
  Prometheus hosts. No production host was switched or otherwise changed.
- The existing bridge-network single-topology development cluster was updated
  in place to exact vpsAdmin `e67572ca`; its database and acceptance fixtures
  were preserved. The cluster reports running and ready with no failed units.
  API, password-recovery worker, and console-router services are active, and
  all three `ExecStart` paths contain the exact deployed revision.
- The switch-time seed reset `test-user1` once because earlier acceptance had
  changed its password away from the configured development value. This
  correctly incremented authentication generation from 12 to 13 and created
  seed audit row 16. Two subsequent explicit seed runs left both test-user
  password digests, authentication generations, session counts, and audit
  counts unchanged, proving the new matching-password path is a no-op.
- Exact pre-delete inspection identified seed-generated audit rows 1 through
  12 and 16: all had source `other`, no initiating session, and belonged to
  the two development users. Those 13 rows were deleted from the development
  database. Real acceptance rows 13 through 15 remain: recovery, signed-in,
  and forced reset. The deletion is recoverable only from a database backup.
- `test-user1.enable_multi_factor_auth` was restored to true only after its
  `Acceptance TOTP` device ID 1 was confirmed enabled and confirmed. The
  development cluster remains available for user acceptance.
- All three exact-head long browser gates pass:
  `webui#auth` completed in 1002.58 seconds, `webui#users-admin` in 964.09
  seconds, and `webui#users-self-service` in 1027.83 seconds. They cover the
  labelled forced-reset form, administrator attribution link, and member
  history/privacy behavior respectively.
- Exact-head API topic, RuboCop, WebUI PHPUnit, and i18n GitHub workflows pass.
  The broad CI workflow remains in progress at this checkpoint; it will be
  monitored to completion, and any runner loss will be inspected before a
  replacement run is accepted.

## Administrator recovery restriction and history fix (2026-08-23)

- User acceptance found an administrator history failure at
  `?page=adminm&action=password_changes&id=2` and requested that self-service
  recovery be unavailable to administrator accounts while still sending an
  explanatory recovery email.
- Live WebUI logs reproduce the failure at `webui/forms/users.forms.php:374`:
  a recovery row with no initiating session causes HaveAPI PHP to call
  `user_session#show` without path arguments and throw `UnresolvedArguments`.
  The API response and authorization are not the cause.
- Repository inspection confirms that API role `user` covers levels 1 through 20,
  `support` covers levels 21 through 89, and `admin` covers levels 90 and above.
  The accepted policy permits only role `user` and treats both privileged roles
  as administrator accounts in recovery mail.
- The four project worktrees are clean at the start of this follow-up:
  vpsAdmin `e67572ca27952f977603f570ca23961bd3bc9ebf`, production mail templates
  `c21e186c72299db573c3ed16e0bc33df3c460731`, KB contracts
  `6ca3a0698bebed1042ebd15039626ea158deb6e8`, and production configuration
  `c7346294e5f8ed425c4c359ce8d33b53898faa49`.
- No product repository, production host, or KB page has been changed at this
  checkpoint. The existing bridge cluster remains the only deployment target.

### Administrator recovery implementation and quick verification

- The WebUI failure was caused by resolving `user_session#show` for recovery
  and forced-reset audit rows whose optional `user_session_id` is null. Commit
  `3622dffde302a874d146fe5abfa35ea4804aeede` guards the relation lookup and
  adds an administrator browser fixture for a sessionless row.
- Commit `0057e59f4a839c5a83f138ee6ffb97e2dc231ece` permits recovery only for API
  role `user`. Roles `support` and `admin` still receive the grouped security
  mail, but their entry has no token and directs them to another administrator.
  The existing persisted `unavailable` outcome is retained; the distinct mail
  branch is transient, so this follow-up adds no migration or API/client
  contract change.
- Recovery eligibility is checked when the email token is exchanged and again
  under the user lock before the final password write. Crossing between an
  ordinary and privileged role invalidates active recoveries; tests also cover
  tokens manufactured by an older process and a role change after the password
  form was opened.
- Embedded and production templates use the same English and Czech
  administrator guidance. The exact standard automated-mail footer remains
  unchanged. Production template commit
  `a71b329b91acb38d24e19d8dda9512537253e901` is clean and pushed.
- vpsAdmin was rebased onto current `origin/master` and force-pushed with lease.
  Its exact clean pushed head is `0057e59f4a839c5a83f138ee6ffb97e2dc231ece`.
  The installed hooks pass migration specs, Nixfmt, WebUI/API i18n checks,
  PHP CS Fixer, and RuboCop.
- Focused recovery, route, policy, model, and template specs pass with 64
  examples and no failures. Full WebUI PHPUnit passes with 86 tests and 365
  assertions. All four production ERB variants compile, and diff/footer checks
  pass.
- The KB contract is pinned at all six sites to exact vpsAdmin `0057e59f4`.
  Its full `bin/check` passes with 43 controls, 35 paths, 92 bindings, and all
  120 PNGs. No managed page, semantic control, or screenshot changed. Exact
  clean pushed KB head: `908cd0dabf141c529fabbc8b5ea02a9f1fefa962`.
- Production configuration was rebased onto current `origin/master`. Generated
  `confctl` commit `9860559e` pins `vpsadminServices` to exact `0057e59f4`;
  commit `b7214ab53dc6bfca60d95a84aa6064313ab21039` updates the runbook with the
  member-only policy, privileged-account acceptance checks, and exact template
  revision. Nixfmt hooks and strict MkDocs pass. The exact clean head is pushed;
  no production host was deployed.
- Long browser integration tests, production configuration builds, mandatory
  review, CI completion, and bridge-cluster deployment remain pending.

### Administrator recovery mandatory review

- The exact-head standalone review found no Blocking or Important issue and
  cleared the implementation for long integration and development-only
  deployment.
- One tracking advisory corrected the ordinary-member range from "below 21" to
  levels 1 through 20. Levels below 1 have no API role and remain ineligible.
- One commit-quality advisory noted that already-published shared-workspace
  commit `f7c7b3e` contains a 137-character body line. Shared `master` must not
  be rewritten, so the exception is recorded here; all product commits and
  other hand-written reviewed messages comply with the 80-character rule.
- The reviewer independently passed all 64 focused API examples, both WebUI
  history regressions with 14 assertions, rendered all four production
  administrator mail variants without reset links, verified every exact remote
  head and downstream pin, and accepted the commit boundaries.
- Residual gates are the planned browser/vpsAdminOS integrations, seven
  production configuration builds, current-head CI completion, and bridge
  development-cluster update. The Playwright sessionless-row assertion checks
  the row and absence of links but not the literal `---`; the pending browser
  gate exercises the real client rendering.

### Administrator recovery integration follow-up

- The first post-review `webui#users-admin` run failed after 708.88 seconds
  while creating its browser fixtures. Artifact
  `/tmp/os-test-runner/os-test-webui-fd1a3b33` records a Ruby `NameError`:
  the two password-recovery fixtures referenced the ordinary `user` before
  `ensure_webui_user` created it. This is an integration-fixture regression in
  the administrator-recovery commit, not a runner or product-runtime failure.
- The correction moves those recovery fixtures immediately after the ordinary
  browser user is created. It retains an ordinary recovery subject while
  preserving the later token output consumed by the authentication browser
  tests. The failed run will not be accepted as validation; the affected
  browser gates will be rerun at the corrected exact head.
- Repository hooks passed when the amend was rerun inside the full Nix
  development shell. The corrected exact clean vpsAdmin head is
  `5a61d5698deff70fea385bb620c6bb24b9a88597` and is pushed.
- The KB contract is mechanically repinned at all six sites to that revision.
  `bin/check` again passes with 43 controls, 35 paths, 92 bindings, and all 120
  PNGs. Its corrected exact clean pushed head is
  `39f2b827cf2c91a03e276bd95e04ed7c7f243aac`.
- Production configuration was regenerated through `confctl`. Its rewritten
  feature history retains one generated pin commit, `8399af33`, followed by
  one runbook commit, instead of recording superseding pins for the same
  integration correction. The lock and both runbook literals use exact
  vpsAdmin `5a61d5698`; exact clean pushed configuration head is
  `304799867315efa42ad9367cca3e62fd0c77d41e`. No host was deployed.
- The same standalone mandatory reviewer is rechecking only this correction
  and the new exact downstream heads before the browser gates resume.
- The exact-head correction recheck passed with no Blocking, Important, or new
  Advisory finding. The reviewer confirmed the vpsAdmin delta is only the
  intact fixture relocation, all product/runtime files are unchanged, all six
  KB pins match, the configuration series is exactly one generated pin plus
  one runbook commit, and every worktree/SSH branch tip is clean and exact.
  The long browser gates are cleared to resume.
- Corrected-head `webui#users-admin` passes: its Playwright example completed
  in 388.22 seconds, its script in 829.74 seconds, and the full VM test in
  1088.12 seconds. This covers the real sessionless history rendering that had
  failed during user acceptance.
- Corrected-head `webui#auth` also passes: its Playwright example completed in
  363.55 seconds, its script in 755.10 seconds, and the full VM test in 857.37
  seconds. This revalidates recovery and OAuth completion using the relocated
  ordinary-user fixtures.
- All seven production configurations in the runbook build successfully, with
  no deployment: `int.api1`, `int.api2`, `int.webui1`, `int.webui2`,
  `prg/proxy`, `prg/int.mon1`, and `prg/int.mon2`. The builds include exact
  vpsAdmin `5a61d5698`, the recovery worker unit, frontend route, and checked
  Prometheus configuration/rules.
- The existing single-topology bridge cluster was updated in place from the
  exact corrected vpsAdmin worktree; its persistent database was preserved.
  The cluster reports ready, has no failed units, and the API, password
  recovery worker, WebUI container, and mailer are active. No production host
  or KB page was changed.
- A live Playwright smoke signs in as the development administrator and opens
  the exact reported URL, `?page=adminm&action=password_changes&id=2`. It sees
  `Password changes for test-user1`, renders the history table, and finds no
  server error. The first smoke attempt stopped at Chromium's private-CA error;
  explicit `ignoreHTTPSErrors` resolved that test-environment issue. The next
  attempt reached the WebUI but used an incorrect visibility assertion for the
  intentionally hidden account-menu logout form; matching the repository's
  value assertion resolved that test-only error. The final run passed in 25.0
  seconds, and its temporary spec/artifacts were removed.
- A live recovery submission for `test-admin` produced exactly one Mailpit
  message. Its plain and HTML bodies contain the administrator guidance and
  standard automated-mail footer, and neither contains a recovery URL or HTML
  link. The email remains in development Mailpit for user inspection; local
  CSRF/cookie/form artifacts were removed.
- Exact corrected-head GitHub workflows for API topic specs, RuboCop, API/WebUI
  i18n, and the KB contract check are green. Superseded broad vpsAdmin run
  `32654022527` was cancelled after the amend. Current broad vpsAdmin run
  `32656237937` and KB managed-runtime run `32656346842` remain alive in their
  test steps with no reported failure; runner deployment may extend or
  interrupt them, so any eventual failed result requires log inspection before
  a rerun is accepted.
- Final handoff audit confirms all four project worktrees are clean and every
  local feature head equals its SSH upstream: vpsAdmin `5a61d5698`, mail
  templates `a71b329b`, KB contracts `39f2b827`, and configuration `30479986`.
  All immutable KB/configuration/runbook references resolve to the exact
  vpsAdmin and mail-template revisions listed above.

### Password change client audit follow-up

- Work started from the clean pushed project heads vpsAdmin `5a61d5698`, mail
  templates `a71b329b`, KB contracts `39f2b827`, and production configuration
  `30479986`. No mail-template change is currently required.
- The unreleased password-change migration now stores a nullable client IP,
  server-resolved PTR, and normalized user-agent reference. Pending OAuth
  authorizations can carry one password-change log until code exchange.
- Signed-in and administrator changes snapshot the exact initiating session.
  Recovery and required-reset writes snapshot the final browser request from
  proxy-controlled `X-Real-IP` or the connection address. Transparent hash
  upgrades use the current session when present and otherwise snapshot their
  request. Maintenance writes without either context remain nullable.
- Required token resets attach their new session in the same savepoint as
  session creation. Required OAuth resets remain sessionless until code
  exchange, then attach within the exchange savepoint. Focused regressions
  prove that wrong-user attachment failures roll back session creation and
  preserve OAuth authorization codes.
- The API exposes the three nullable snapshot fields to the existing
  owner/administrator history endpoint. WebUI keeps its compact primary
  columns and adds a full-width detail row with vertically listed IP address,
  PTR, and user agent. The table uses fixed layout and anywhere wrapping; the
  browser fixture contains a 300-character unbroken user-agent segment.
- API and WebUI catalogs were regenerated. The new Czech labels are
  `IP adresa`, `PTR IP adresy`, and `User agent`; API metadata uses
  `IP adresa klienta`. WebUI locale health, Node syntax checks, the focused
  PHPUnit regression (2 tests, 19 assertions), Nixfmt, PHP CS Fixer, and
  focused RuboCop (22 files) pass.
- The migration up/down spec passes independently with two examples. A mixed
  migration/application RSpec invocation was discarded because the migration
  harness switches Active Record to its isolated database, as documented in
  the existing workspace notes. The complete focused ordinary API rerun passes
  with 121 examples and no failures.
- vpsAdmin commit `4afc559b4` contains the API/schema/session-linking unit and
  commit `df4216aee` contains the independently reviewable WebUI/layout unit.
  Both commits ran all installed Overcommit hooks successfully. A serialized
  final PHPUnit rerun passes with 2 tests and 20 assertions; an earlier parallel
  Nix-shell startup was discarded after hitting the already-documented shared
  Bundler extraction race.
- The exactly-one fresh standalone mandatory review is now running against
  base `5a61d5698` and head `22eadb340`. Long browser/vpsAdminOS integration,
  downstream pins, configuration documentation, and development deployment
  remain gated on that result.
- The full configured WebUI PHPUnit suite passes from `webui/` with 86 tests
  and 371 assertions. A root-directory invocation was discarded because it
  bypassed `webui/phpunit.xml.dist` and loaded duplicate regression helpers.
- Mandatory review found a rolling-upgrade gap when an old API process exchanges
  a new authorization: it would create the correct session without attaching
  the password-change row. The existing five-minute authentication task now
  reconciles those rows with the same locked, same-user, idempotent attachment.
  New processes attach immediately after opening the OAuth session, before
  publishing it as the thread-local current session.
- The review also found that a superseded unsaved password assignment retained
  its earlier explicit client snapshot. Password-change context assignment now
  clears all three client fields first, with a replacement-to-null regression.
- Account owners retain client details for their own and sessionless events,
  while another user's initiating-session details are returned as null. This
  keeps administrator workstation IP, PTR, and user agent private from the
  affected member; administrators continue to see every stored snapshot.
- Schema-first rolling deployment remains API-compatible, but an old process
  cannot populate the newly added client fields and some sessionless metadata
  cannot be reconstructed. The production runbook must minimize and explicitly
  describe this transient audit-detail gap. New-authorize/old-code-exchange is
  separately repairable and converges through authentication maintenance.
- Corrected focused API verification passes with 74 examples and no failures;
  the standalone reviewer independently passes 71 examples. Focused RuboCop
  reports no offenses in ten files, and both rewritten vpsAdmin commits pass
  every installed Overcommit hook. The exact clean pushed vpsAdmin head is
  `df4216aeeafc4893e3167f71f840345e3f37b31f`.
- KB contract history was reduced to the inventory update, navigation change,
  and one final pin. All six source references resolve to the exact vpsAdmin
  head; `nix develop -c bin/check` passes. The clean pushed KB head is
  `60cc9fb6e2016ec1de99231e77d4b4ea1a55df6b`.
- Production configuration history was reduced to the frontend, monitoring,
  final runbook, and one generated `confctl` input commit. The runbook records
  the mixed-version metadata gap and reconciliation procedure, and the exact
  channel pin is `df4216aee`. Overcommit and strict MkDocs pass. The clean
  pushed configuration head is
  `c7a1978c96daacc9b98936b74e23e2914f511155`.
- Ambient configuration rebase/push attempts were rejected by Overcommit
  because the pinned bundle is only present in `nix develop`; the identical
  guarded operations succeeded inside that shell. Generated `.bin` and
  `.bundle` files and the MkDocs `site/` output were removed after validation.
- The mandatory reviewer cleared its original three findings on the corrected
  vpsAdmin head and is completing the exact KB/configuration pin, runbook, and
  commit-series review before long integration starts.
- Current-head CI started after the force-push. Migration, WebUI PHPUnit,
  RuboCop, i18n, and libnodectld workflows are already green; API topics and
  broad CI remain active or queued. Superseded broad run `32656237937` at
  vpsAdmin `5a61d5698` was cancelled, while current-head jobs were left intact.
- Mandatory review completed on exact ranges vpsAdmin `5a61d5698..df4216aee`,
  KB contracts `c1d0aca2b..60cc9fb6e`, and configuration
  `7cd45c867..c7a1978c9`. It reported no Blocking, Important, or Advisory
  findings. The reviewer confirmed the commit splits, authorization and
  redaction boundary, atomic session attachment, mixed-version reconciliation,
  migration/rollback contract, wrapping layout, exact downstream pins, and
  runbook. Long Playwright/vpsAdminOS and development-cluster acceptance are
  now unblocked.
- `./test-runner.sh list` was a discarded discovery attempt: this runner has no
  `list` command. The exact RSpec-style script selectors were confirmed from
  the test suite sources instead.
- The long `webui#users-self-service` vpsAdminOS test passes: its Playwright
  example completed successfully in 481.05 seconds and the complete test
  returned exit status 0 after 1,190.84 seconds. The long `webui#users-admin`
  test is running next, serialized to avoid VM and shared-memory contention.
- The old bridge development cluster was stopped before the remaining VM tests
  because it consumed enough `/dev/shm` for the runner to warn that its 24 GiB
  request exceeded the safe limit. Shutdown reached the known Puma stop timeout
  and the cluster runner killed it; status is now stopped and shared-memory
  availability rose from 25 GiB to 44 GiB. Its disposable state will be reset
  before the final deployment as already required by the rewritten migration.
- The long `webui#users-admin` vpsAdminOS test also passes: its Playwright
  example completed successfully in 510.72 seconds and the complete test
  returned exit status 0 after 1,400.2 seconds. Services-guest teardown consumed
  the expected remainder of the known Puma stop timeout, but did not affect the
  result. The serialized `webui#auth` test is running last.
- Exact-head API topic CI completed successfully, including the `users-auth`
  shard and the topic-coverage gate. Current-head broad VM CI is still queued
  for a runner; all current-head quick workflows remain green.
- The final long `webui#auth` vpsAdminOS test passes: its Playwright example
  completed successfully in 445.42 seconds and the complete test returned exit
  status 0 after 1,083.22 seconds. All three serialized browser/vpsAdminOS
  suites selected for this follow-up are green.
- The stopped bridge cluster was reset successfully, removing all disposable
  database and VM state. A fresh single-node bridge deployment is now building
  from exact vpsAdmin head `df4216aee`.
- The fresh bridge deployment built exact clean vpsAdmin `df4216aee` and all
  four guests. Its first node boot reached the known pre-kernel/stale-readiness
  failure and the post-start refresh returned `No route to host`; the failed
  attempt was stopped without resetting the newly seeded disks. The preserved
  retry booted node1, but its first refresh raced osctld group initialization.
  Once `/default` existed, the documented idempotent refresh succeeded. The
  cluster now reports running, bridge, and `ready: yes` with no failed units.
- Live build info reports exact revision
  `df4216aeeafc4893e3167f71f840345e3f37b31f` with `revisionDirty: false`.
  API, password-recovery worker, console router, supervisor, nginx, the
  five-minute authentication timer, and the base Prometheus timer are active.
- Development-only acceptance state was restored through the application
  models: password recovery is enabled and `test-user1` has one enabled,
  confirmed `Acceptance TOTP` using deterministic secret
  `JBSWY3DPEHPK3PXP`; `test-user2` and `test-admin` have no MFA. Both temporary
  scripts were removed immediately after their assertions passed.
- The queryless public recovery form returns HTTP 200 with no-store/security
  headers, the configured logo, labelled login-or-primary-email field, and a
  default-client sign-in link to WebUI's OAuth start. That WebUI URI returns a
  fresh OAuth authorization redirect. The neutral sent page contains the
  requested wording, logo, and sign-in link.
- One live `test-user1` submission returned the neutral HTTP 303. The worker
  completed it on attempt 1, the unfinished queue returned to zero, and the
  resulting recovery remains unconsumed and incomplete. Mailpit message
  `4Kqxuv0yfNhkUerYwuX1XN` is the newest message for manual acceptance. It is
  multipart, contains reset links in both text and HTML, uses the canonical
  automated-mail footer, and contains neither recovery-code nor used-once
  wording.
- A live base-exporter run records one accepted recovery submission, zero
  pending submissions, queue limit 100, zero capacity events, and all five
  fixed password-change source counter/timestamp series. The live schema has
  nullable `user_session_id`, `client_ip_addr`, `client_ip_ptr`, and
  `user_agent_id` on password-change logs and the nullable OAuth authorization
  handoff column.
- Exact-head vpsAdmin API topics and every quick workflow are green; broad CI
  has started on a redeployed runner. Exact-head KB `Check` is green and
  managed-page runtime is queued.
- Build-only production configuration validation passes for all seven affected
  systems: `int.api1`, `int.api2`, `int.webui1`, `int.webui2`, `prg/proxy`,
  `prg/int.mon1`, and `prg/int.mon2`. No production generation was deployed.
  The development shell's transient `.bin/rubocop` and `.bundle/config` files
  were removed afterward, leaving the configuration worktree clean.
- The migration matches the CI selector's full rule, so broad vpsAdmin run
  `32667575449` is executing all 130 `tag=ci` integration scripts on
  `gh-runner2`; its test step remains live without a failure signal. It was not
  restarted or disturbed. Exact-head KB managed-page runtime run `32667741305`
  remains queued for a self-hosted runner, while its `Check` workflow is green.
- Three independent security/architecture reviews completed against exact
  vpsAdmin head `df4216aee`. They found no cross-user recovery, administrator
  recovery, recovery/API/OAuth token confusion, open redirect, completion-cookie
  authentication, or stale-password token-issuance path. Email tokens are
  256-bit random values stored as digests, expire after one hour, and are
  exchanged once for a distinct 15-minute digested browser-session token.
- The reviews independently confirmed one factor-revocation race. Recovery
  TOTP and WebAuthn select an enabled factor without locking and revalidating
  the factor before committing `mfa_verified_at`; a concurrent disable or hard
  delete can therefore finish first while the stale proof is still accepted.
  Real-MariaDB proofs cover recovery TOTP disable/delete, recovery WebAuthn
  disable, an end-to-end password replacement, and the same pre-existing race
  in ordinary TOTP. Exploitation requires the emailed recovery session, valid
  factor proof, and a narrow race, but production enablement should wait for a
  shared ordinary/recovery TOTP/WebAuthn locking fix.
- Keep the separate browser recovery routes and authority state machines:
  recovery uses an HttpOnly flow cookie plus CSRF and never creates a user
  session or OAuth authorization, while normal MFA uses generation-bound
  `AuthToken` capabilities. Extract only the common factor verification,
  replay/counter update, and locked enabled-state revalidation. Factor
  management and both verification paths should use one user-first lock order.
  Do not reuse the existing WebAuthn challenge helper unchanged because it
  prefers caller-controlled `Client-IP`; recovery correctly trusts
  proxy-controlled `X-Real-IP` with the Rack peer as fallback.
- Advisory hardening: replace or cap outstanding two-minute WebAuthn challenges
  per recovery and add failed-finish observability/backoff. A valid recovery
  session can currently create them without a per-flow cap, although the
  five-minute cleanup bounds retention and no service degradation was shown.
  Also define and test behavior when an OAuth client referenced by an active
  recovery is deleted; the current nullification falls back to the default
  client but loses completion-marker client binding and one-time SSO
  suppression.
- Independent focused suites passed with 126 normal authentication/recovery
  examples, the route/architecture review passed 102 plus 24 examples, and the
  vulnerability proofs passed independently. The primary agent reproduced the
  MariaDB TOTP disable/delete proof (2 examples) and TOTP/WebAuthn scheduling
  proof (2 examples). All exact-head GitHub workflows are now green, including
  broad CI, API topic/migration specs, WebUI PHPUnit, RuboCop, i18n, and
  libnodectld. No existing feature source was changed; review artifacts are
  confined to untracked `vulnerabilities/` paths pending remediation.

### MFA revocation and recovery-state hardening

- Implementation started from exact clean pushed vpsAdmin head
  `df4216aeeafc4893e3167f71f840345e3f37b31f`. The unreleased recovery
  migration now records the exact verified TOTP device or passkey using two
  nullable indexed identifiers.
- Shared TOTP and WebAuthn factor operations now lock and revalidate the latest
  enabled factor state while the caller holds the user and authority locks.
  Ordinary and recovery authority transitions remain separate operations.
  Supported TOTP/passkey disable and delete operations use the same user-first
  lock order and invalidate only recoveries verified with the affected factor.
- Whole-account MFA disable invalidates all active recoveries and pending MFA
  tokens. The TOTP fallback-code path disables its factor internally and keeps
  the current recovery usable while invalidating other active recoveries that
  were verified by the same device.
- Recovery passkey begin replaces the preceding recovery challenge, a
  recognized finish consumes its challenge even on failed proof, and ordinary
  WebAuthn challenges are not touched. No retry-counter schema was added.
- OAuth-client deletion invalidates active associated recoveries before the
  request association is nullified. The worker locks and revalidates a selected
  client while creating recovery state, which closes the concurrent
  create-after-invalidation window. Completed recoveries can fall through only
  the current default OAuth client for the existing completion alert.
- Deterministic independent-connection MariaDB regressions pass for six
  TOTP/passkey schedules: verification-first blocks factor revocation until
  commit, exact recovery revocation then wins, and revocation-first prevents
  ordinary and recovery MFA. A second deterministic client-lock schedule proves
  deletion waits for recovery creation and then invalidates the new flow; a
  deleted-client regression proves stale workers cannot create orphaned state.
- The complete recovery-route suite passes with 38 examples. The affected
  model/resource suite passes with 141 examples, the migration suite with two,
  the maintained MFA concurrency suite with six, the TOTP fallback suite with
  six, and the request-creation suite with nine. Focused RuboCop passes on all
  38 hand-written MFA files and all eight OAuth lifecycle files. An earlier
  198-example pass had two ordinary WebAuthn lookup-rescue failures; the rescue
  placement was corrected and its four exact regressions then passed.
- All temporary `vulnerabilities/` proof artifacts were removed after their
  evidence was represented in maintained product specs. vpsAdmin commits
  `2d2cd1f67d603b2a54c9e340718d21d4a901b3fc`,
  `fe5bbbd3fb2cde9ed8cf8ffa05399c7812f08165`,
  `4a105768331823205e8452e346ed2e0c1a397480`, and
  `7ccaf19bbea35d32b345267c8240da99e3906ea1` separate factor lifecycle,
  trusted WebAuthn metadata, bounded recovery challenges, and OAuth-client
  lifecycle behavior. Every commit passed all installed Overcommit hooks
  inside `nix develop .#vpsadmin`.
- A first ambient-shell commit attempt was correctly rejected because RuboCop,
  gettext, and MariaDB were absent. No hook was bypassed; the repository's
  existing `notes/vpsadmin/2026-08-18-overcommit-nix-shell.md` procedure was
  used for both successful commits.
- Mandatory fresh-agent review, downstream repins, CI, long integration, and
  the bridge-cluster reset/deploy remain pending. Production deployment and KB
  publication remain operator-only.
- Upstream fetch found seven new vpsAdmin master commits. The entire feature
  branch was rebased onto exact master `661896d007313dedc91066f55c72410ef893d10f`;
  the only conflicts were schema-version lines, resolved by retaining master's
  later `2026_08_23_170000` version while preserving every feature column.
  KB contracts and production configuration also have upstream changes and
  will be rebased before their final mechanical repins.
- A post-rebase 195-example security/resource run passed 194 examples and
  exposed one order-dependent passkey setup failure. The new committed
  no-transaction OAuth deletion race had persisted a per-spec `core.api_url`
  override, while WebAuthn allowed origins are configured once at suite start.
  Removing the unnecessary override fixed the reproducing combined order; 47
  request-and-route examples then passed at the original seed. No rerun was
  accepted without first identifying this cause.
- Mandatory review of rebased head `9db2b8086` requested three Blocking fixes:
  ordinary TOTP fallback did not invalidate recoveries tied to its disabled
  factor; client deletion before worker pickup degraded queued work into a
  queryless recovery; and WebAuthn RuntimeError paths rolled back recognized
  challenge consumption. It also found that both lock tests inferred blocking
  from a timed thread join without proving the competing query was scheduled.
- Ordinary and recovery TOTP now prelock all active TOTP-verified recoveries
  before factor verification. Ordinary fallback invalidates every recovery
  tied to the device, while recovery fallback preserves only its current flow.
  Queued OAuth work is locked, scrubbed, and finished during client deletion;
  enqueue revalidates the client under the queue lock and the worker rechecks a
  locked unfinished submission before client lookup. WebAuthn parser and proof
  RuntimeErrors are narrowly normalized to the handled assertion-error path,
  so recognized challenge destruction commits.
- The concurrency regressions now publish the competing MariaDB connection ID
  and wait until its blocking SQL is visible in
  `information_schema.PROCESSLIST`; they no longer depend on a 250 ms scheduling
  guess. A new no-transaction malformed-assertion regression proves the exact
  challenge is consumed across a real commit boundary.
- Corrected focused verification passes: 30 MFA/concurrency/request/TOTP
  examples before the malformed correction, the exact malformed WebAuthn
  example, 50 OAuth-client/submission/worker examples, and 57 recovery-route
  plus ordinary WebAuthn examples. Targeted RuboCop passes on all eleven
  changed hand-written files, and every amended commit passes all installed
  hooks.
- The corrected clean vpsAdmin head is
  `459232faa1c8843f56f51ac4b2c16b248bef8bc5`, with focused commits
  `0d6463109`, `9efa4f850`, `763f084cb`, and `459232faa`. The same mandatory
  reviewer is checking the exact rewritten tree and closure of all findings;
  downstream repins, CI, long integration, and bridge deployment remain
  blocked on that follow-up verdict.
- Mandatory follow-up review of `459232faa` confirmed two remaining Blocking
  paths. Recovery TOTP locked the current recovery before older verified rows,
  while OAuth deletion locked all linked recoveries by ID; a deterministic
  MariaDB schedule reproduced the resulting lock inversion. The WebAuthn gem
  also raises `JSON::ParserError` and `NoMethodError` for other malformed client
  data, outside the earlier `RuntimeError` normalization, so those failures
  still rolled back recognized challenge deletion. The reviewer also noted a
  loose SQL match and incomplete persistent-fixture cleanup in the OAuth race
  test.
- TOTP verification now locks the current recovery and all active
  TOTP-verified recoveries in one ID-ordered query, then operates on the locked
  current instance. A maintained two-thread regression pauses before that
  query, lets OAuth deletion complete, and proves verification returns a clean
  rejection rather than deadlocking. The WebAuthn boundary now normalizes
  `StandardError` only around the gem parser and verifier calls; database lookup
  and counter updates remain outside. Its real-transaction regression covers a
  wrong assertion type, invalid JSON, and valid JSON missing its challenge, and
  proves each recognized challenge deletion commits.
- The OAuth race harness now requires both the `oauth2_clients` table and the
  `FOR UPDATE` clause in observed SQL, restores the two values changed by its
  no-transaction setup, and removes its recovery, mail transaction, factor,
  user, and client fixtures. Focused verification passes 22 combined
  TOTP/WebAuthn/concurrency examples, eight revised WebAuthn/concurrency
  examples, the corrected OAuth race, and targeted RuboCop on all seven files.
  Both fixup commits passed every installed hook before autosquash.
- The exact clean corrected vpsAdmin head is now
  `75ea67f886ff5deb4e9c70066599212522c8dba7`; its final hardening commits are
  `0d6463109`, `9efa4f850`, `974f049e5`, and `75ea67f88`. The same reviewer is
  performing the required exact-head closure check. The KB contract and
  production configuration branches have been rebased onto their current
  masters but remain intentionally pinned to the preceding feature revision
  until this review clears and the final vpsAdmin revision is pushed.
- The mandatory reviewer cleared exact vpsAdmin head `75ea67f886` against
  merge base `661896d007` with no Blocking, Important, or Advisory findings.
  Its independent focused MFA/concurrency/OAuth run passed 23 examples, and
  the same-process request/recovery-route run passed 48. The review confirmed
  that the ID-ordered recovery lock closes the TOTP/OAuth deadlock and that
  recognized malformed WebAuthn attempts consume their challenge across a
  real transaction boundary.
- The rebased KB contract is clean and pushed at
  `01b100037407cc682c4093047146e5ab223cc613`. All capture, navigation, page,
  workflow-action, and Nix inputs use exact vpsAdmin `75ea67f886` and its
  inherited vpsAdminOS `8e44a51244`. `nix develop -c bin/check` passes; the
  initial run correctly rejected the stale page-runtime action revision before
  it was updated.
- The rebased production configuration is clean and pushed at
  `52ed765062f6c2033f3fa49f0414b8a668f4fd92`. Its runbook records the MFA
  snapshots, hardening acceptance checks, no-sixth-migration fact, and both
  API/worker rollout requirement. `confctl inputs channel set --commit` created
  the sole final `vpsadminServices` pin at exact `75ea67f886`; no lock file was
  edited manually.
- All seven production configurations named by the runbook build successfully:
  `int.api1`, `int.api2`, `int.webui1`, `int.webui2`, `prg/proxy`,
  `prg/int.mon1`, and `prg/int.mon2`. The first scripted attempt stopped at
  the expected interactive confirmation; the actual validation used
  `confctl build --yes` and completed every system.

### Final hardening closure

- The final fixture/history corrections keep every commit independently
  runnable: the completed-recovery browser case runs before delayed tests with
  the production completion lifetime, only the active password-form fixture
  receives a one-hour test lifetime, and exact verified-factor IDs appear in
  the same commit as their schema.
- The last order-dependent API failure was traced to the non-transactional
  OAuth deletion schedule retaining `SpecSeed.node` state. Its teardown now
  restores the seed node and complete current-status row. The exact full API
  engine run passed 912 examples with zero failures and three pending; the
  reproducing 21-example polluting order also passes.
- The final clean, pushed vpsAdmin head is
  `8d55a0a4871a52c7dc3f90c5449b32149328fc24`. The mandatory fresh-context
  reviewer found no Blocking, Important, or Advisory issue and cleared this
  exact head for integration and downstream pins. Its independent focused
  suite passed three examples; targeted RuboCop, JavaScript syntax, and Nix
  parsing also pass.
- Every GitHub check at the final vpsAdmin head is green: broad CI, API topic
  and migration specs, WebUI PHPUnit, RuboCop, i18n health, and libnodectld.
  The full `webui#auth` VM/browser scenario passed in 1,198.07 seconds,
  including the real password-recovery completion path.
- The clean, pushed KB contract head is
  `6096a76caf9ad6825218eeaa8ce5f1f8fb54e672`. All six contract and Nix pin
  sites use exact vpsAdmin `8d55a0a487`; `nix develop -c bin/check` passes.
  Both the `Check` and managed-page runtime workflows are green.
- The clean, pushed production-configuration head is
  `35e43276f2b2a2af7e3235fa51a7c2306bf136bb`. Its sole generated
  `vpsadminServices` update and runbook use exact vpsAdmin `8d55a0a487`.
  `confctl build --yes` passes for both API servers, both WebUI servers, the
  auth proxy, and both monitoring servers.
- The final `webui#users-self-service` VM/browser test passes: its Playwright
  example completed in 436.74 seconds and the complete test in 1,086.04
  seconds. The final `webui#users-admin` test also passes: its Playwright
  example completed in 459.12 seconds and the complete test in 1,074.12
  seconds. The suites were serialized to stay within `/dev/shm` limits.
- The preceding bridge cluster was reset, including its disposable database
  and VM state. The fresh single-node bridge deployment built exact clean
  vpsAdmin `8d55a0a487` and reports `ready: yes`; API, recovery worker, console
  router, supervisor, nginx, osctld, and nodectld are active with no failed
  systemd units. Build info reports `revisionDirty: false`.
- First boot encountered the documented osctld socket readiness race after
  successful service seeding. Once osctld and nodectld were running, the
  documented idempotent node refresh completed successfully without resetting
  the seeded disks.
- Development-only acceptance state is restored without consuming a recovery
  request: password recovery is enabled, the unfinished queue is empty,
  `test-user1` and `test-user2` share
  `shared-password-recovery@example.test`, and only `test-user1` has effective
  MFA with a confirmed, enabled `Acceptance TOTP` device using deterministic
  secret `JBSWY3DPEHPK3PXP`. `test-user2` and `test-admin` have no factors.
  The WebUI OAuth client is the default direct-continuation client. The public
  recovery form returns HTTP 200 with its logo, labelled identifier field, and
  working OAuth-start sign-in link. The temporary fixture scripts were removed.

### Pending lifecycle authentication and recovery prefill

- A final independent security review identified the pre-existing interval in
  which a user with a newly requested destructive lifecycle state could still
  authenticate or complete recovery before the transaction chain materialized
  the state. The accepted compatibility decision blocks new authentication,
  refresh, required-reset, and recovery authorities while leaving already-issued
  sessions resumable until the chain closes them.
- Fetched vpsAdmin upstream and rebased the feature branch onto exact master
  `80e27053c8e6578251fca69a55981037ad2a6193`. The rebase completed without
  source conflicts; downstream exact pins remain intentionally unchanged until
  the follow-up is reviewed.
- Added one shared user lifecycle predicate based on both the materialized state
  and newest requested `ObjectState`, neutral denial for OAuth/login, and locked
  rechecks before ordinary token authentication and required password reset.
  Added recovery policy, route, Basic/token, OAuth authorization/code/refresh,
  and existing-session compatibility regressions. The first focused run passed
  172 examples with zero failures; the session/OAuth/submission follow-up passed
  69 examples with zero failures.
- Added recovery-link prefill from the retained OAuth login value. The value is
  URL-encoded and bounded by the recovery identifier limit; blank and oversized
  values are omitted and the password is never copied. The browser regression
  continues from an invalid-password response and checks the prefilled recovery
  field. Targeted RuboCop passes on all 19 changed Ruby files and JavaScript
  syntax passes with Node.
- The first mandatory review found one Blocking TOCTOU race: final
  authentication checks held the `users` row, but lifecycle publication used
  only the separate `resource_locks` table, so a destructive `ObjectState`
  could still commit after the check and before authority publication. It found
  no Important or Advisory issue and accepted the prefill and intended split.
- User lifecycle publication now holds the same database user-row lock as
  authentication authority creation, including direct recorded state changes.
  A deterministic two-connection MariaDB regression pauses after the effective
  lifecycle query, schedules a real soft-delete request, proves its `FOR UPDATE`
  is blocked, and then proves token publication linearizes before deletion.
  The exact race spec passes 12 examples with zero failures. User creation,
  resource writes, and every user transition suite pass 58 examples with zero
  failures; targeted RuboCop reports no offenses.
- The lock correction was autosquashed into the lifecycle security commit so
  exact commits `150537ff1e0275f4d07a3cf40cee15e86d658c24` and
  `257a5a0ae81b29a5c080d6666e71ff9fef58876e` kept the lifecycle change and
  recovery-prefill convenience separate. Every installed Overcommit hook
  passed for each staged change in `nix develop .#vpsadmin`; no hook was
  bypassed.
- The reviewer's closure pass found a second Blocking lifecycle path: inherited
  expiration and reminder writers appended a newer `active` state log while a
  destructive transition was queued, masking that transition from the shared
  authentication predicate. User lifecycle metadata changes now take the same
  user-row lock and reject any pending materialized/requested state mismatch;
  the regression proves neither metadata writer can supersede the destructive
  log.
- The same pass found an Important test-isolation issue in the deterministic
  authentication/lifecycle race. It now runs the real mail-backed queued chain,
  retains the returned chain, and explicitly removes its mail, confirmations,
  transactions, resource lock, concerns, and chain before deleting the user.
  The first focused run exposed the missing live mail-node fixture; adding the
  standard current-node-status fixture made the production-real path pass.
- Exact-head verification passes the two lifecycle metadata examples and the
  real two-connection issuance race (three examples, zero failures). Targeted
  RuboCop reports no offenses, and every installed Overcommit pre-commit and
  commit-message hook passed.
- Exact-head closure cleared the production lifecycle guard and transaction
  graph cleanup, but found one Important test-isolation leak: the mail-node
  setup mutated `SpecSeed.node` and left its `NodeCurrentStatus`. The race spec
  now snapshots and exactly restores both records, matching the established
  non-transactional recovery-race pattern. Its isolated metadata also skips the
  ordinary spec setup, which otherwise persisted a password change for the
  shared seed user outside RSpec's transaction.
- A 187-example exploratory combined run started before the isolated-setup
  correction and failed two later user-write examples because that shared seed
  mutation persisted. The diagnosed four-example order now passes the real
  issuance race, the reviewer's supervisor status regression, missing-login
  validation, and signed-in password change with zero failures. The corrected
  clean commits are `085f0c7fc891370ecb305b60307cea5f544feb20` and
  `99f46e0238bfbc3a7bccb5eec7d6657ba57f3cda`; the same reviewer is performing
  final closure before downstream repins and long integration.
- The exact-head CI API shard then exposed a lifecycle-lock regression in the
  payments transaction chain: ActiveRecord's `with_lock` reload discarded an
  unsaved `UserAccount#paid_until` extension held by the caller. The corrected
  lifecycle wrapper locks a separate `User` instance, refreshes only the three
  lifecycle attributes on the caller, and preserves its association cache. It
  uses the unscoped user relation so administrator transitions away from
  `hard_delete` remain supported. The exact payment regression and all four
  hard-delete transition examples pass.
- The final reviewer found that an MFA token issued before a destructive state
  request could still consume a TOTP factor or complete WebAuthn before the
  later authorization/password boundary rejected it. Ordinary TOTP, WebAuthn
  begin/finish, and fulfilled WebAuthn OAuth conversion now recheck the shared
  lifecycle predicate while holding the user lock. Rejected continuations do
  not consume the factor, challenge, or MFA token.
- The complete affected MariaDB batch passes 144 examples with zero failures,
  covering ordinary TOTP/WebAuthn, OAuth, password issuance, user lifecycle
  writes, and the payments chain. Targeted RuboCop passes eight changed files,
  and every installed Overcommit pre-commit and commit-message hook passed.
  The corrected clean commits are
  `4f20f4d730cd92ee3caa06cdb3b20324e05c8a6b` and
  `18cac37ed004e4fd960b723297566e9ca1328d91`; fresh exact-head mandatory
  review is pending before any downstream repin or deployment.
- The reviewer required positive focused coverage for the rewritten fulfilled
  WebAuthn OAuth path because the browser suite does not exercise passkey
  sign-in. Those examples exposed a real block-value handoff regression that
  made both successful branches call the `reset_password` method without its
  arguments. The corrected code explicitly carries the locked password-reset
  value out of the block. Focused examples now prove both authorization-code
  issuance and conversion to an unfulfilled required-reset token, alongside
  the rejected destructive-state case.
- The completed authority inventory found two other new-credential paths:
  administrator-created detached API token sessions and metrics bearer tokens.
  Both now lock the target user and recheck the effective lifecycle predicate
  before creating any owner or token row. Operation and authenticated API
  regressions return controlled resource-locked failures and prove that no
  credential is issued. Existing API/OAuth sessions and ordinary operations
  performed through them remain deliberately usable until the lifecycle chain
  closes those sessions.
- The final focused closure batch passes nine examples with zero failures,
  targeted RuboCop passes 13 files, all installed Overcommit hooks pass, and
  the worktree is clean. Rewritten exact commits are
  `4a1dd1661048125c32b4adef72f85f4d650b06a6` and
  `e57fb02e184450b6ad94d4cc1e00772392d90ef2`; exact-head mandatory review is
  pending before long integration, force-push, repins, and deployment.
