# Implement dev-session tmux workflow

## Goal

Add workspace-local tooling that starts and maintains a tmux session for each
development initiative, with convenient windows for Codex, notes, and feature
worktrees.

## Affected repositories

- coordination workspace repository

## Approach

- Add `bin/dev-session` as a Ruby CLI using tmux and git command-line
  interfaces.
- Resolve short names to `<yyyy-mm-dd>-<name>` by default and support
  `--as-is` for literal slugs.
- Create a first tmux window with Codex on the left, a notes shell on the
  right top, and a worktree-group shell on the right bottom.
- Add explicit `sync` behavior for one managed tmux window per worktree.
- Add thin `git worktree add/remove` helpers that follow workspace paths.
- Document the workflow and add focused Ruby tests.

## Compatibility and deployment

This is local development tooling only. It changes no production code,
protocols, schemas, persisted state, generated clients, NixOS options, or
deployment order. Existing work directories and state files are preserved.

The tmux sync design tags only tool-managed sessions/windows and leaves
unmanaged windows alone, so it is safe to use in sessions that users customize.

## Testing plan

- `ruby -c bin/dev-session`
- `ruby test/dev_session_test.rb`
