# 2026-07-10-dev-session-shell

## Goal

Keep the left `dev-session` tmux pane alive as a usable shell after Codex exits,
so Codex can be updated and restarted without recreating the pane or session.

## Affected repositories

- vpsFree.cz development workspace repository

## Approach

- Create the left pane with tmux's normal login shell rather than using Codex
  as the pane command.
- Start the configured Codex command by sending it to that shell.
- Document the shell lifecycle and cover it with a real tmux regression test.

## Compatibility and deployment

- This changes only newly created local development sessions. Existing tmux
  sessions continue with their current pane processes until recreated.
- `--no-codex` remains a plain shell, and `VPSFREE_DEV_SESSION_CODEX` remains a
  shell command, including support for arguments and shell syntax.
- No persisted formats, APIs, schemas, deployed services, or cross-project
  version ordering are affected. Rollback restores the former pane lifecycle.

## Testing plan

- Run the complete Ruby test suite in `test/dev_session_test.rb`.
- Exercise a real isolated tmux server where a short-lived configured Codex
  command exits, then run another command in the same pane and confirm the
  session remains alive.
