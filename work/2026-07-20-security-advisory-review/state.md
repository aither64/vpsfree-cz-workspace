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

## Status

- Preparation complete: the repository is documented and the isolated
  worktree is ready.
- Investigating a production token-creation failure before accessing vpsAdmin
  data: `ActiveRecord::ValueTooLong` reports that `tokens.opts` is too long.
- Awaiting successful token creation before accessing vpsAdmin data.
- The token must remain ephemeral and must not be recorded in this file or
  repository content.
- Diagnosis complete; no source fix was implemented because the user requested
  investigation only.

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

## Open questions

- Authentication identity, permissions, and API endpoint will be verified only
  after the user supplies the token; the secret itself will not be persisted.
- Whether to implement and deploy the vpsAdmin schema migration and regression
  test before resuming token creation.

## Cleanup

- Keep the review worktree until the advisory review is finished or abandoned.
- Keep the feature branch after integration unless the user explicitly asks to
  delete it.
