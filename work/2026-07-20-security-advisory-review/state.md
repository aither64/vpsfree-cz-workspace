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

## Status

- Preparation complete: the repository is documented and the isolated
  worktree is ready.
- Awaiting the user's authentication token before accessing vpsAdmin data.
- The token must remain ephemeral and must not be recorded in this file or
  repository content.

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

## Open questions

- Authentication identity, permissions, and API endpoint will be verified only
  after the user supplies the token; the secret itself will not be persisted.

## Cleanup

- Keep the review worktree until the advisory review is finished or abandoned.
- Keep the feature branch after integration unless the user explicitly asks to
  delete it.
