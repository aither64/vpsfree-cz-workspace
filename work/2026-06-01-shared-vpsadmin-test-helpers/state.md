---
lifecycle: active
---
# shared vpsAdmin test helpers state

## Current status

Worktrees are prepared and the proposed cross-repository design is ready for
review. No repository code has been changed.

## Initiative

- Slug: `2026-06-01-shared-vpsadmin-test-helpers`
- Tracking directory:
  `/home/aither/workspace/ai/vpsfree.cz/work/2026-06-01-shared-vpsadmin-test-helpers`

## Repositories and worktrees

### vpsadminos

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadminos.git`
- Branch:
  `2026-06-01-shared-vpsadmin-test-helpers`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsadminos`
- Base:
  `origin/staging` at `6dc4209c4`
- Status:
  clean

### vpsadmin

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsadmin.git`
- Branch:
  `2026-06-01-shared-vpsadmin-test-helpers`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsadmin`
- Base:
  `origin/master` at `21a1d0b11`
- Status:
  clean

### terraform-provider-vpsadmin

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/terraform-provider-vpsadmin.git`
- Branch:
  `2026-06-01-shared-vpsadmin-test-helpers`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers/terraform-provider-vpsadmin`
- Base:
  `origin/master` at `6984147`
- Status:
  clean

### vpsfree-irc-bot

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-irc-bot.git`
- Branch:
  `2026-06-01-shared-vpsadmin-test-helpers`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsfree-irc-bot`
- Base:
  `origin/master` at `6db629e`
- Status:
  clean

### vpsf-status

- Bare repository:
  `/home/aither/workspace/ai/vpsfree.cz/repos/vpsf-status.git`
- Branch:
  `2026-06-01-shared-vpsadmin-test-helpers`
- Worktree:
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsf-status`
- Base:
  `origin/master` at `c6fab24`
- Status:
  clean

The existing vpsf-status integration-test worktree remains separate at:

`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsf-status-integration-tests/vpsf-status`

It has staged WIP integration-test changes and was used as reference only.

The existing vpsfree-irc-bot integration-test worktree remains separate at:

`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-06-01-vpsfree-irc-bot-integration-tests/vpsfree-irc-bot`

It has WIP changes from another Codex instance and was used as read-only
reference.

## Commands run

Fetched current refs:

```sh
git fetch --prune origin
```

Run in:

- `repos/vpsadmin.git`
- `repos/vpsadminos.git`
- `repos/terraform-provider-vpsadmin.git`
- `repos/vpsfree-irc-bot.git`
- `repos/vpsf-status.git`

Created tracking directories:

```sh
mkdir -p work/2026-06-01-shared-vpsadmin-test-helpers \
  worktrees/2026-06-01-shared-vpsadmin-test-helpers
```

Created worktrees:

```sh
git worktree add -b 2026-06-01-shared-vpsadmin-test-helpers \
  ../../worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsadminos \
  origin/staging

git worktree add -b 2026-06-01-shared-vpsadmin-test-helpers \
  ../../worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsadmin \
  origin/master

git worktree add -b 2026-06-01-shared-vpsadmin-test-helpers \
  ../../worktrees/2026-06-01-shared-vpsadmin-test-helpers/terraform-provider-vpsadmin \
  origin/master

git worktree add -b 2026-06-01-shared-vpsadmin-test-helpers \
  ../../worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsfree-irc-bot \
  origin/master

git worktree add -b 2026-06-01-shared-vpsadmin-test-helpers \
  ../../worktrees/2026-06-01-shared-vpsadmin-test-helpers/vpsf-status \
  origin/master
```

The first terraform-provider worktree add failed because the bare clone had no
local heads and `HEAD` pointed at `refs/remotes/origin/master`. The bare clone
was normalized with:

```sh
git update-ref refs/heads/master refs/remotes/origin/master
git symbolic-ref HEAD refs/heads/master
```

The vpsadmin worktree add printed an Overcommit signature warning from checkout
hooks, but the worktree was created and is clean.

## Inspection notes

- vpsAdminOS test-runner currently only loads local
  `tests/runner/extensions/*.rb` from the current working directory.
- vpsAdmin has the broadest `VpsadminServicesMachine` helper in
  `tests/runner/extensions/vpsadmin_services.rb`.
- terraform-provider-vpsadmin has a smaller copied helper with `vpsadminctl`,
  `api_ruby`, MariaDB helpers, chain waiting, and transaction key unlock.
- vpsf-status currently has a minimal copied helper in its separate
  integration-test WIP branch.
- vpsfree-irc-bot WIP currently embeds vpsAdmin API helper methods in
  `tests/runner/extensions/irc_bot.rb` alongside IRC-specific helper code.

## Cleanup notes

- No code has been edited in the prepared worktrees.
- Remove these worktrees after the proposal is implemented, merged, or
  abandoned.
