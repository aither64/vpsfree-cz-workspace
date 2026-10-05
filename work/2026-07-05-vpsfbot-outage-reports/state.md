---
lifecycle: active
---
# 2026-07-05-vpsfbot-outage-reports

## Repositories
- vpsfree-irc-bot
  - branch: `2026-07-05-vpsfbot-outage-reports`
  - worktree:
    `worktrees/2026-07-05-vpsfbot-outage-reports/vpsfree-irc-bot`
  - base: `origin/master` at `48b06b9`
- vpsadmin
  - inspected read-only through `repos/vpsadmin.git` at `origin/master`
- vpsfree-cz-configuration
  - branch: `2026-07-05-vpsfbot-outage-reports`
  - worktree:
    `worktrees/2026-07-05-vpsfbot-outage-reports/vpsfree-cz-configuration`
  - base: `origin/master` at `37a0a91e`

## Status
- Bot fix implemented and committed on the feature branch.
- Quick local verification passed:
  - `nix develop -c bash -lc 'bundle exec rspec'`
  - `nix develop -c bash -lc 'bundle exec rubocop'`
- Mandatory standalone review passed with no findings.
- Bot feature branch pushed and GitHub Actions passed.
- `vpsfree-irc-bot` was fast-forward merged and pushed to `master`.
- `vpsfree-cz-configuration` package pin was updated, verified, fast-forward
  merged, and pushed to `master`.
- Temporary worktrees were removed. Branches were kept locally and remotely.
- Work is complete.
- The production state shown by the user contains only outage 1426 with
  begins_at `1783379700`, duration `45`, impact `system_restart`, summary
  `Kernel upgrade`, and four node entities.

## Commands run
- `bin/dev-session current`
- `bin/dev-session worktree add 2026-07-05-vpsfbot-outage-reports vpsfree-irc-bot --as-is --branch 2026-07-05-vpsfbot-outage-reports`
- `git status --short --branch`
- `git log --oneline -5 --decorate`
- `rg -n "outage|planned_outage|outages.yml|begins_at|duration|impact|handlers"`
- `sed -n '1,360p' lib/vpsfree-irc-bot/outage_reports.rb`
- `git --git-dir=repos/vpsadmin.git show origin/master:AGENTS.md`
- `git --git-dir=repos/vpsadmin.git show origin/master:plugins/outage_reports/api/resources/outage.rb`
- `git --git-dir=repos/vpsadmin.git show origin/master:plugins/outage_reports/api/resources/outage_update.rb`
- `curl` checks against outage pages 1426, 1427, and 1428 on
  `https://vpsadmin.vpsfree.cz/`
- `curl`/`jq` checks against `https://api.vpsfree.cz/v7.0/outages` and
  `https://api.vpsfree.cz/v7.0/outage_updates`
- `nix develop -c bash -lc 'bundle exec overcommit --version'`
- `nix develop -c bash -lc 'bundle exec overcommit --install && bundle exec overcommit --sign'`
- `nix develop -c bash -lc 'bundle exec rspec'`
- `nix develop -c bash -lc 'bundle exec rubocop'`
- `git commit -F <tmpfile>`
- `nix develop -c bash -lc 'git push -u origin 2026-07-05-vpsfbot-outage-reports'`
- `gh run list --repo vpsfreecz/vpsfree-irc-bot --branch 2026-07-05-vpsfbot-outage-reports --limit 10`
- `git --git-dir=repos/vpsfree-irc-bot.git worktree add -B merge/2026-07-05-vpsfbot-outage-reports-vpsfree-irc-bot worktrees/2026-07-05-vpsfbot-outage-reports/merge/vpsfree-irc-bot origin/master`
- `nix develop -c bash -lc 'git merge --ff-only 2026-07-05-vpsfbot-outage-reports'`
- `nix develop -c bash -lc 'git push origin HEAD:master'`
- `gh run list --repo vpsfreecz/vpsfree-irc-bot --branch master --limit 6`
- `nix store prefetch-file --unpack --json https://github.com/vpsfreecz/vpsfree-irc-bot/archive/565c4b4e99c7b6b6daf8b0a9768b9b3796611247.tar.gz`
- `bin/dev-session worktree add 2026-07-05-vpsfbot-outage-reports vpsfree-cz-configuration --as-is --branch 2026-07-05-vpsfbot-outage-reports`
- `nix develop -c bash -lc 'bundle exec overcommit --install && bundle exec overcommit --sign'`
- `nix develop -c bash -lc 'nixfmt packages/vpsfree-irc-bot/default.nix && git diff -- packages/vpsfree-irc-bot/default.nix'`
- `nix develop -c bash -lc 'confctl build "cz.vpsfree/containers/int.vpsfbot"'`
- `nix develop -c bash -lc 'confctl build -y "cz.vpsfree/containers/int.vpsfbot"'`
- `nix develop -c bash -lc 'git push -u origin 2026-07-05-vpsfbot-outage-reports'`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree add -B merge/2026-07-05-vpsfbot-outage-reports-config worktrees/2026-07-05-vpsfbot-outage-reports/merge/vpsfree-cz-configuration origin/master`
- `nix develop -c bash -lc 'git merge --ff-only 2026-07-05-vpsfbot-outage-reports && git push origin HEAD:master'`
- `git --git-dir=repos/vpsfree-irc-bot.git worktree remove worktrees/2026-07-05-vpsfbot-outage-reports/vpsfree-irc-bot`
- `git --git-dir=repos/vpsfree-irc-bot.git worktree remove worktrees/2026-07-05-vpsfbot-outage-reports/merge/vpsfree-irc-bot`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-07-05-vpsfbot-outage-reports/vpsfree-cz-configuration`
- `git --git-dir=repos/vpsfree-cz-configuration.git worktree remove worktrees/2026-07-05-vpsfbot-outage-reports/merge/vpsfree-cz-configuration`

## Results
- Active initiative: `2026-07-05-vpsfbot-outage-reports`.
- Worktree was created from `origin/master`.
- Worktree creation exited non-zero because the repository hook wrapper found
  Overcommit hooks installed but the ambient shell lacks the `overcommit` gem.
  Git still created the branch and checkout. Hook setup must be resolved before
  committing any code changes.
- No repository-local `AGENTS.md` is present in `vpsfree-irc-bot`.
- Bot startup (`post_api_setup`) sets `@since = Time.now`, then refreshes all
  currently announced outages into `outages.yml` without announcing them.
- Periodic polling uses `api.outage.list(state: :announced, since: @since)`.
  In vpsAdmin, `Outage.list(since:)` filters `outages.created_at > since`,
  not announcement time.
- Periodic polling also fetches `api.outage_update.list(since: @since)`, but
  `report_update` returns immediately when `update.state == 'announced'`.
  Therefore staged outages created before `@since` but announced after `@since`
  are skipped: they are too old for `Outage.list(since:)`, and their announce
  updates are ignored.
- Public outage pages show announce updates:
  - 1426: `2026-07-05 18:18:38 CEST` / `2026-07-05T16:18:38Z`
  - 1427: `2026-07-05 18:20:01 CEST` / `2026-07-05T16:20:01Z`
  - 1428: `2026-07-05 18:20:50 CEST` / `2026-07-05T16:20:50Z`
- API checks show:
  - `outages` with `outage[since]=2026-07-05T16:18:00Z` returns 1426-1428.
  - `outages` with `outage[since]=2026-07-05T16:18:30Z` returns none of
    1426-1428, so all three outage rows were created before 16:18:30Z.
  - `outage_updates` with `outage_update[since]=2026-07-05T16:19:00Z`
    returns announce updates for 1427 and 1428.
  - `outages` with `outage[recent_since]=2026-07-05T16:19:00Z` returns
    1426-1428.
- Most likely sequence, corrected after user confirmed the bot did not restart:
  1. All three outages were staged/created before `2026-07-05T16:18:30Z`.
  2. Outage 1426 was announced at `16:18:38Z`.
  3. A regular bot poll ran after 1426 was announced but before 1427 was
     announced. Because the bot's previous `@since` was still older than the
     staged outage rows, `Outage.list(state: :announced, since: @since)`
     returned 1426, but not 1427/1428 because they were still staged.
  4. The bot stored and announced 1426, then advanced `@since` to the poll
     completion time because it saw an outage/update.
  5. Outages 1427 and 1428 were announced at `16:20:01Z` and `16:20:50Z`.
  6. On later polls, 1427/1428 did not match `Outage.list(since: @since)`
     because their outage rows were older than `@since`; their
     `OutageUpdate` rows did match but were ignored as `state == announced`.
  7. The state file therefore remained with only 1426.
- Implemented fix in `lib/vpsfree-irc-bot/outage_reports.rb`:
  `report_update` now treats an `announced` outage update as a new outage
  announcement when the outage ID is not already in `@store`; if it is already
  present, the update is skipped to avoid duplicate reports.
- Added regression coverage to `tests/suite/vpsadmin-events.nix` for two
  staged outages announced after creation, where the first announcement can
  advance the bot's `@since` cursor before the second is announced.
- Overcommit hooks were installed and signed inside `nix develop`.
- Commit attempt from the ambient shell failed because the `overcommit` gem was
  not available there. The commit was retried from `nix develop`, where hooks
  ran successfully.
- Bot feature commit:
  `565c4b4e99c7b6b6daf8b0a9768b9b3796611247`
  (`outage_reports: report staged outage announcements`).
- Quick verification results:
  - RSpec: 49 examples, 0 failures.
  - RuboCop: 61 files inspected, no offenses detected.
  - Commit hooks: pre-commit RuboCop passed; commit-msg hooks passed with
    Overcommit text-width warnings at 72 characters. Commit-message lines are
    still within the workspace 80-character rule.
- Mandatory standalone review result:
  - Reviewer: `019f333c-b3ab-7e33-997f-0851b0aa5223`.
  - Findings: no Blocking, Important, or Advisory findings.
  - The reviewer confirmed that the commit is focused, matches the requested
    staged outage announcement fix, and leaves the later configuration pin as
    a separate mechanical change.
  - Residual risks noted: integration tests still need to validate the real
    HaveAPI client shape for `meta: { includes: 'outage' }`; a broader
    pre-existing polling race remains where setting `@since` to local
    `Time.now` after a non-empty poll can skip events created during an
    in-flight poll. That broader cursor design is not changed in this branch.
- Pushed bot feature branch:
  `origin/2026-07-05-vpsfbot-outage-reports`.
- GitHub Actions on the pushed bot branch:
  - RSpec run `28748458431`: success, 59s.
  - Integration Tests run `28748458435`: success, 6m23s.
- Bot merge worktree:
  `worktrees/2026-07-05-vpsfbot-outage-reports/merge/vpsfree-irc-bot`.
- Fast-forward merge pushed `565c4b4e99c7b6b6daf8b0a9768b9b3796611247`
  to `origin/master`.
- Master push triggered GitHub Actions:
  - RSpec run `28748739038`: success, 1m0s.
  - Integration Tests run `28748739043`: success, 4m21s.
- `vpsfree-cz-configuration` package update:
  - Previous bot rev:
    `48b06b915451a8babfea4c0dabf63b11019a1715`.
  - New bot rev:
    `565c4b4e99c7b6b6daf8b0a9768b9b3796611247`.
  - New source hash:
    `sha256-zsorssmHS/WUM/6ZUc5BSJyF+SYBSjh63wKmlTnhKMs=`.
  - Config commit:
    `c40fc4df82df78735cd6a19bb84c95223b20257e`
    (`packages: update vpsfree-irc-bot`).
  - Config package pin review was skipped as a mechanical deployment pin to
    the already reviewed and CI-verified bot commit; no additional code or
    design change was introduced in the configuration repository.
- `confctl build "cz.vpsfree/containers/int.vpsfbot"` without `-y` prompted
  for confirmation and failed with EOF in the non-interactive shell.
- `confctl build -y "cz.vpsfree/containers/int.vpsfbot"` succeeded and built
  generation `2026-07-05--19-23-40`.
- Config repository has no push-triggered workflow for this branch; its only
  workflow is the scheduled daily update.
- Config fast-forward merge pushed
  `c40fc4df82df78735cd6a19bb84c95223b20257e` to `origin/master`.
- The latest bot `master` push workflows also passed:
  - RSpec run `28748739038`: success, 1m0s.
  - Integration Tests run `28748739043`: success, 4m21s.
- `gh run list` also showed older scheduled Daily update failures on
  `vpsfree-irc-bot` `master`; they predate this push and were not rerun or
  used as verification for this change.
- Removed all initiative worktrees under
  `worktrees/2026-07-05-vpsfbot-outage-reports/`. The initiative notes remain
  under `work/2026-07-05-vpsfbot-outage-reports/`.
- Follow-up cleanup pass ran `git worktree prune --verbose` for
  `vpsfree-irc-bot` and `vpsfree-cz-configuration`. No initiative worktree
  directories or transient cache directories remain.

## Open questions
- None.

## Cleanup
- Done. Worktrees were removed; feature branches were kept.
- Follow-up cleanup done. Branch refs were kept per workspace policy.
