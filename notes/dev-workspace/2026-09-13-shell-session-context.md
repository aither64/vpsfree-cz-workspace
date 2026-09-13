# Starting a coordination session outside managed tmux

`dev-session start NAME --no-attach --json` requires `--goal-file` when stdin is
not interactive. When an existing conversation already owns the work, use
`--no-codex --no-attach --json` to create a shell-only session without a second
Codex writer. To run `dev-session current` from separate command processes,
provide both `DEV_SESSION_SLUG` and the matching `DEV_SESSION_WORKSPACE`.
Providing only the slug fails with "session environment is not managed by this
workspace". Both values verified the newly created session successfully.

Related initiative: work/2026-09-13-portal-file-links/.
