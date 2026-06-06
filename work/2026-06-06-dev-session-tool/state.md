# Implement dev-session tmux workflow

## Repositories

- coordination workspace repository
  - path: `/home/aither/workspace/ai/vpsfree.cz`
  - branch: `master`

## Status

- Implemented and locally verified.

## Commands run

- `git diff -- AGENTS.md`
- `git status --short --branch`
- `find . -maxdepth 2 -type d -name bin -o -name docs -o -name test -o -name tests`
- `sed -n '1,260p' AGENTS.md`
- `chmod +x bin/dev-session`
- `ruby -c bin/dev-session`
- `ruby -c test/dev_session_test.rb`
- `ruby test/dev_session_test.rb`
- `ruby test/dev_session_test.rb -n test_tmux_start_and_sync_manage_only_worktree_windows`
- `env VPSFREE_DEV_SESSION_SLUG=2026-06-06-demo bin/dev-session current`
- `env -u TMUX VPSFREE_DEV_SESSION_SLUG=2026-06-06-demo bin/dev-session current`
- `env VPSFREE_DEV_SESSION_SLUG=2026-06-06-demo bin/dev-session --tmux-socket dev-session-none current`
- temporary Ruby/tmux debug snippets to inspect managed window options
- `git diff --check`
- `bin/dev-session --help`
- `ruby test/dev_session_test.rb -n test_list_output_uses_aligned_columns_for_long_slugs`
- `bin/dev-session list | head -20`
- `bin/dev-session list service-health-checks`
- `ruby test/dev_session_test.rb -n '/start_slug_resolution|start_new/'`
- `ruby test/dev_session_test.rb -n test_tmux_start_and_sync_manage_only_worktree_windows`

## Results

- Added initial `bin/dev-session` Ruby implementation.
- `ruby -c bin/dev-session` passed.
- Added `docs/dev-sessions.md`, `test/dev_session_test.rb`, and an
  `AGENTS.md` pointer.
- Fixed two issues found by tests:
  - stripped `git rev-parse --git-common-dir` output before using it as
    `--git-dir`;
  - changed tmux format strings to emit real tab separators.
- Final verification:
  - `ruby -c bin/dev-session`: passed.
  - `ruby -c test/dev_session_test.rb`: passed.
  - `ruby test/dev_session_test.rb`: 6 runs, 39 assertions, 0 failures,
    0 errors, 0 skips.
  - `git diff --check`: passed.
  - `bin/dev-session --help`: printed expected usage and exited successfully.
- Follow-up: changed `list` output from tab-separated fields to dynamically
  padded columns with a header. Added a regression test for long slugs.
- Follow-up verification:
  - `ruby test/dev_session_test.rb -n test_list_output_uses_aligned_columns_for_long_slugs`:
    1 run, 9 assertions, 0 failures.
  - `ruby test/dev_session_test.rb`: 7 runs, 48 assertions, 0 failures,
    0 errors, 0 skips.
  - `bin/dev-session list | head -20`: printed aligned columns.
- Follow-up: added `bin/dev-session remove <slug>` cleanup command.
  - Default behavior kills a managed tmux session, removes clean git worktrees
    under `worktrees/<slug>/`, and keeps `work/<slug>` notes.
  - `--force` allows dirty worktree removal.
  - `--all` also removes `work/<slug>`.
  - Unmanaged same-name tmux sessions fail before cleanup.
- Follow-up verification:
  - `ruby -c bin/dev-session`: passed.
  - `ruby -c test/dev_session_test.rb`: passed.
  - `ruby test/dev_session_test.rb`: 13 runs, 86 assertions, 0 failures,
    0 errors, 0 skips.
  - `git diff --check`: passed.
  - `bin/dev-session --help`: printed the `remove` usage.
- Follow-up: fixed `start <name>` slug resolution.
  - `start` now resumes a unique existing matching slug before creating
    today's slug.
  - `start --new <name>` forces today's slug.
  - `--new` and `--as-is` are mutually exclusive.
  - `--new` rejects dated slugs.
- Follow-up verification:
  - `ruby test/dev_session_test.rb -n '/start_slug_resolution|start_new/'`:
    7 runs, 13 assertions, 0 failures.
  - `ruby -c bin/dev-session`: passed.
  - `ruby -c test/dev_session_test.rb`: passed.
  - `ruby test/dev_session_test.rb`: 20 runs, 99 assertions, 0 failures,
    0 errors, 0 skips.
  - `git diff --check`: passed.
  - `bin/dev-session --help`: printed the `--new` usage.
  - `bin/dev-session list service-health-checks`: resolved
    `2026-06-05-service-health-checks`.
- Follow-up: changed the initial `dev` window left pane to start Codex from
  the workspace repository root instead of `work/<slug>`. The right top pane
  remains `work/<slug>` and the right bottom pane remains `worktrees/<slug>`.
- Follow-up verification:
  - `ruby test/dev_session_test.rb -n test_tmux_start_and_sync_manage_only_worktree_windows`:
    1 run, 17 assertions, 0 failures.
  - `ruby -c bin/dev-session`: passed.
  - `ruby -c test/dev_session_test.rb`: passed.
  - `ruby test/dev_session_test.rb`: 20 runs, 101 assertions, 0 failures,
    0 errors, 0 skips.
  - `git diff --check`: passed.
- Follow-up: added active session discovery for Codex/dev-session reuse.
  - Added `bin/dev-session current`, resolving the active slug from
    `VPSFREE_DEV_SESSION_SLUG`, the current managed tmux session, or cwd under
    `work/<slug>` / `worktrees/<slug>`.
  - Managed tmux sessions, panes, and synced worktree windows now receive
    `VPSFREE_DEV_SESSION_SLUG`, `VPSFREE_DEV_SESSION_WORKSPACE`,
    `VPSFREE_DEV_SESSION_WORK_DIR`, and `VPSFREE_DEV_SESSION_WORKTREES_DIR`.
  - Updated `AGENTS.md` to require checking `bin/dev-session current` before
    creating a new initiative slug.
  - Updated `docs/dev-sessions.md` with `current` and the exported
    environment.
- Follow-up verification:
  - `ruby -c bin/dev-session`: passed.
  - `ruby -c test/dev_session_test.rb`: passed.
  - `ruby test/dev_session_test.rb`: 26 runs, 128 assertions, 0 failures,
    0 errors, 0 skips.
  - `git diff --check`: passed.
  - `bin/dev-session --help`: includes `current`.
  - `bin/dev-session current`: printed active tmux slug
    `2026-06-06-os-install-tests` in the current shell.
  - Direct env-only probe with a mismatched slug failed as designed because
    tmux reported `2026-06-06-os-install-tests`; retrying with isolated tmux
    socket printed `2026-06-06-demo`.

## Open questions

- None.

## Cleanup

- No cleanup needed yet.
