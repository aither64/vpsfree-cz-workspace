# 2026-07-20-security-advisory-review

## Repositories

- Top-level coordination repository
  - Branch: `master`
  - Worktree: `/home/aither/workspace/ai/vpsfree.cz`
  - Scope: add `security-advisories` to `AGENTS.md`; preserve and do not commit
    unrelated existing changes.
- `security-advisories`
  - Bare clone: `repos/security-advisories.git`
  - Remote: `git@github.com:vpsfreecz/security-advisories.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/security-advisories`
  - Base: current `origin/2026-07-13-security-advisory-automation`
- `vpsadmin`
  - Bare clone: `repos/vpsadmin.git`
  - Remote: `git@github.com:vpsfreecz/vpsadmin.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/vpsadmin`
  - Base: `origin/master` at
    `1bca29dfac3dba6a82a857ffad24d42e46ae861e`
- `haveapi`
  - Bare clone: `repos/haveapi.git`
  - Remote: `git@github.com:vpsfreecz/haveapi.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree: `worktrees/2026-07-20-security-advisory-review/haveapi`
  - Base: `origin/master` at `e3749669d6034d529095ccbd3a40148fcb243a27`
- `vpsfree-cz-configuration`
  - Bare clone: `repos/vpsfree-cz-configuration.git`
  - Remote: `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`
  - Branch: `2026-07-20-security-advisory-review`
  - Worktree:
    `worktrees/2026-07-20-security-advisory-review/vpsfree-cz-configuration`
  - Base: `origin/master` at
    `36c0e9ba2f5cdca43d4d3b0541c6b6fa809f699d`

## Status

- Preparation complete: the repository is documented and the isolated
  worktree is ready.
- Investigating a production token-creation failure before accessing vpsAdmin
  data: `ActiveRecord::ValueTooLong` reports that `tokens.opts` is too long.
- Awaiting successful token creation before accessing vpsAdmin data.
- The token must remain ephemeral and must not be recorded in this file or
  repository content.
- Diagnosis, implementation, mandatory review, broader verification, and the
  requested `vpsadmin` channel pin are complete and merged to both default
  branches. The configuration change has not been deployed to production.

## Commands run

- `bin/dev-session current`
- `git status --short --branch`
- Inspected the existing `AGENTS.md` diff to identify unrelated shared changes.
- Inspected the advisory bare clone's remotes, refs, registered worktrees, and
  repository-local `AGENTS.md`.
- Queried the upstream symbolic `HEAD` and branch refs with `git ls-remote`.
- `bin/dev-session worktree add 2026-07-20-security-advisory-review
  security-advisories --as-is --branch
  2026-07-20-security-advisory-review --base
  origin/2026-07-13-security-advisory-automation`
- `git fetch origin master` in the top-level coordination repository.
- Verified advisory worktree registration, branch/ref identity, SSH remote,
  clean status, installed Overcommit hooks, and `git diff --check` results.
- Committed the scoped coordination changes with `git commit -F` and pushed
  top-level `master` over SSH.
- Fetched current vpsAdmin and HaveAPI `origin/master`, read their local
  `AGENTS.md` files, and created initiative worktrees from those refs.
- Traced the advisory client's token scope payload through HaveAPI's token
  request input and vpsAdmin's MFA continuation handling and schema.
- Measured the exact serialized continuation payload with Ruby/JSON.
- Ran a temporary, uncommitted RSpec reproduction through
  `nix develop .#api`; the temporary spec was removed after the run.
- `nix develop .#api -c bash -lc 'bundle exec rspec
  spec/lib/vpsadmin/api/authentication/token_config_spec.rb --format progress'`
- Regenerated `api/db/schema.rb` from an isolated MariaDB instance with
  `VPSADMIN_PLUGINS=none`, then verified that only the schema version and
  `auth_tokens.opts` type changed.
- Ran the new migration spec and token-configuration spec in separate RSpec
  processes after confirming that combining them leaves ordinary examples on
  the intentionally minimal migration-spec database.
- `ruby tools/check_migration_specs.rb --cached`
- `nix develop -c overcommit --run`
- `nix develop -c git commit -F /tmp/vpsadmin-token-opts-commit-message`
- `git fetch origin master`
- `git push -u origin 2026-07-20-security-advisory-review`
- `nix develop -c confctl inputs channel set --commit vpsadmin vpsadmin
  b3ec1a757c51b639b6442cd2552401688061b3e3`
- Ran 92 ordinary authentication, user-session, authentication-task, and core
  schema examples together in the normal API test database.
- `nix develop -c confctl inputs channel ls`
- `nix develop -c confctl build -y` for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`, serially to avoid ConfCtl log collisions.
- Pushed the configuration feature branch from `nix develop` so its pre-push
  Overcommit hook could load the locked gems.
- Monitored vpsAdmin branch workflows with `gh run list`, `gh run view`, and
  `gh run watch`.
- Downloaded the failed serialized workflow's test-log artifact and inspected
  the exact failing test's `test-result.txt` and `test-runner.log`.
- Fetched both default branches, rebased the configuration feature branch onto
  its advanced `origin/master`, and force-pushed only that unmerged feature
  branch with an explicit lease.
- Created fresh default-branch integration worktrees, fast-forwarded them with
  `git merge --ff-only`, and pushed `vpsadmin` followed by
  `vpsfree-cz-configuration` over SSH.
- Removed the completed implementation, investigation, and temporary merge
  worktrees; retained the clean `security-advisories` worktree for the pending
  token-based review.

## Results

- Verified active session slug: `2026-07-20-security-advisory-review`.
- The bare clone already exists and uses the required SSH origin.
- Upstream `HEAD` currently resolves to
  `origin/2026-07-13-security-advisory-automation` at
  `55e26c3ad6bc548e7b40b0cc1dddd47c41e2da11`.
- The new advisory worktree is clean on
  `2026-07-20-security-advisory-review` at that same commit.
- The repository's Overcommit hooks are installed in the canonical bare
  clone. During worktree creation, the post-checkout hook could not find the
  locked RuboCop gems in the ambient shell; `bin/dev-session` recovered and
  completed the registered, clean worktree. Future hook/test commands must run
  from the repository's `nix develop` environment.
- The top-level `master` matched `origin/master` after fetching.
- Coordination commit `eaaf844f150dc52470ab8cb9ce001fd5cdb06350` was pushed
  to `origin/master`.
- `git diff --check` passed for the advisory worktree and this initiative's
  top-level documentation.
- Repository-local rules require evidence-backed platform assessment, resolved
  evidence before a publishable draft, and prohibit advisory publication.
- `security-advisories` requests 34 action scopes. Their space-separated value
  is 924 characters; vpsAdmin serializes the MFA continuation options to 1,042
  JSON bytes. The current `auth_tokens.opts` column is `VARCHAR(255)`, and the
  exact payload first exceeds that limit at the ninth scope (269 bytes).
- vpsAdmin creates the temporary `AuthToken`, then stores `lifetime`,
  `interval`, and the split scope list in `opts` before returning the TOTP
  continuation. Strict MariaDB therefore raises `ActiveRecord::ValueTooLong`.
  Forced-password-reset token continuations use the same column and have the
  same boundary.
- Password-only token issuance bypasses `auth_tokens.opts` and writes the final
  scope to `user_sessions.scope`, which is already `TEXT`. This explains why
  short or non-MFA token creation can work.
- HaveAPI accepts the scope as an unconstrained string but does not own the
  continuation persistence. The defect is in vpsAdmin's application schema;
  no HaveAPI change is needed.
- The exact long-scope MFA reproduction passed by observing the expected
  `ActiveRecord::ValueTooLong`: 1 example, 0 failures.
- The existing vpsAdmin token-config spec passed: 6 examples, 0 failures. It
  uses only the one-word `all` scope and does not cover MFA token issuance, so
  it cannot detect this overflow.
- Recommended fix: migrate `auth_tokens.opts` to `TEXT` with a 65,535-byte
  limit, regenerate the core-only schema, and add a token-config regression
  that completes MFA with a representative long scope and verifies the final
  session scope. No advisory-client scope broadening or MFA bypass is
  appropriate.
- The documented command must retain the versioned API URL and separate option
  argument: `bin/create-token --api https://api.vpsfree.cz/v7.0 --user LOGIN`.
  The unversioned URL and the displayed `--usermyuser` typo do not cause the
  reported database exception, but would make the saved configuration invalid
  for later versioned API resource requests or be rejected by `OptionParser`,
  respectively.
- Durable diagnostic note:
  `notes/vpsadmin/2026-07-20-auth-token-opts-overflow.md`.
- The `vpsfree-cz-configuration` worktree was created from current
  `origin/master`; its post-checkout Overcommit hook lacked locked gems in the
  ambient shell, and `bin/dev-session` recovered to a registered clean
  worktree. Hook and `confctl` commands must run from `nix develop`.
- Added a reversible core migration from `VARCHAR(255)` to `TEXT`, regenerated
  the core-only schema, and added migration plus end-to-end long-scope TOTP
  token coverage.
- The migration spec passed in both directions: 2 examples, 0 failures.
- The focused token-configuration spec passed: 7 examples, 0 failures.
- Migration specs use an isolated minimal database and must not share an RSpec
  process with ordinary API specs. Durable note:
  `notes/vpsadmin/2026-07-20-migration-spec-database-isolation.md`.
- Ruby syntax checks and `git diff --check` passed for all changed vpsAdmin
  files. The cached migration inventory confirmed that the new migration has a
  matching spec.
- A full explicit Overcommit run found one correctable string-concatenation
  style issue in the new migration spec. After correction, RuboCop passed for
  all three hand-written Ruby files, and the actual commit reran every
  configured pre-commit and commit-message hook successfully.
- vpsAdmin implementation commit:
  `b3ec1a757c51b639b6442cd2552401688061b3e3` (`api: allow long MFA token
  scopes`). The feature branch was pushed over SSH so the configuration flake
  could resolve the exact revision. Current `origin/master` remained at the
  recorded base before push.
- Before the final rebase, `confctl` updated only `flake.lock`, pinning
  `vpsadminServices` from
  `1bca29dfac3dba6a82a857ffad24d42e46ae861e` to the exact vpsAdmin feature
  commit. After rebasing onto the advanced configuration default branch, the
  generated commit is `791439abcec85a6c689837cae27758f65861904e`
  (`inputs: set vpsadminServices to b3ec1a75`). Its generated message was
  retained exactly.
- The configuration worktree is clean after removing `.bin/` and `.bundle/`
  files generated by development-shell setup.
- Mandatory standalone review completed with no blocking findings. It found
  one important documentation issue: logical five-minute expiry does not
  remove an overlong row until the scheduled `vpsadmin:auth:close_expired` task
  runs. Rollback guidance now requires confirmed cleanup and a zero result from
  `SELECT COUNT(*) FROM auth_tokens WHERE OCTET_LENGTH(opts) > 255`.
- The reviewer also advised that the existing boot-evidence deployment runbook
  pins all application and Node channels to its older release revision. The
  runbook now explicitly identifies those checks as release-specific so this
  later `vpsadminServices` application update is not mistaken for a violation
  of a current global pin. The rebased configuration documentation commit is
  `a2482851753e4e23dec488a34ee3a318e6cb1db5` (`docs: mark boot evidence
  pins as release-specific`).
- Reviewer residual gaps: broader API/configuration builds were still pending,
  production MariaDB DDL locking has not been measured, and the regression uses
  a representative over-255-byte 12-scope list rather than all 34 advisory
  scopes. The representative payload directly exercises the failed boundary;
  the exact 34-scope payload was separately measured and reproduced during
  diagnosis.
- Broader related API coverage passed: 92 examples, 0 failures across
  authentication configurations, authentication operations, user-session
  operations, the expired-authentication task, and the core-schema smoke spec.
- `confctl inputs channel ls` reports channel `vpsadmin`, role `vpsadmin`, input
  `vpsadminServices` at `b3ec1a75` while staging and production Node channels
  remain unchanged at `1bca29df`.
- Configuration builds passed serially for `int.api1`, `int.api2`, `int.webui1`,
  and `int.webui2`. The first `int.api1` invocation omitted `-y` and stopped
  safely at its confirmation prompt without building; the non-interactive
  rerun and all subsequent builds succeeded.
- The rebased configuration feature branch was pushed over SSH at
  `a2482851753e4e23dec488a34ee3a318e6cb1db5`. Its exact
  `vpsadminServices` pin remained unchanged through the rebase.
- vpsAdmin GitHub Actions passed RuboCop, API migration specs, libnodectld
  specs, i18n health, and all 26 parallel API/topic jobs for
  `b3ec1a757c51b639b6442cd2552401688061b3e3`. The separate serialized `CI`
  workflow run `29781749917` completed 116 of 117 integration tests and failed
  only `client/snapshot-download`. Its downloaded artifact shows that Nix
  evaluation stopped before the test ran because the runner no longer had the
  `rabbitmq-server-4.2.5.drv` store path. This pre-test runner/store failure is
  unrelated to the authentication-token schema and regression changes, so it
  does not block integration and was not treated as evidence repaired by a
  blind rerun. Durable note:
  `notes/vpsadmin/2026-07-21-ci-missing-rabbitmq-derivation.md`. The
  configuration repository produced no branch-triggered workflow runs.
- `vpsadmin` was fast-forwarded and pushed to `master` at
  `b3ec1a757c51b639b6442cd2552401688061b3e3`.
- `vpsfree-cz-configuration` was fast-forwarded and pushed to `master` at
  `a2482851753e4e23dec488a34ee3a318e6cb1db5`, after vpsAdmin was available at
  the pinned revision.
- On the vpsAdmin default-branch push, API migration specs, RuboCop, i18n
  health, and libnodectld specs passed. API topic specs run `29810531250`
  remains in progress and serialized CI run `29810531324` remains queued; the
  same commit already passed the feature-branch API topic run. The
  configuration repository has no workflow run for its default-branch push.
- No deployment, production database migration, production API request, or
  token handling was performed.

## Open questions

- Authentication identity, permissions, and API endpoint will be verified only
  after the user supplies the token; the secret itself will not be persisted.
- The merged fix and channel update must still be deployed before the
  production token command can succeed with the long MFA scope list.

## Cleanup

- Keep the review worktree until the advisory review is finished or abandoned.
- Keep the feature branch after integration unless the user explicitly asks to
  delete it.
- Removed the `vpsadmin`, `vpsfree-cz-configuration`, and `haveapi` initiative
  worktrees plus both temporary default-branch merge worktrees. Their feature
  branch refs were retained.
- Removed transient development-shell files and the downloaded CI artifact.
- The clean `security-advisories` initiative worktree remains ready at
  `55e26c3ad6bc548e7b40b0cc1dddd47c41e2da11`.
