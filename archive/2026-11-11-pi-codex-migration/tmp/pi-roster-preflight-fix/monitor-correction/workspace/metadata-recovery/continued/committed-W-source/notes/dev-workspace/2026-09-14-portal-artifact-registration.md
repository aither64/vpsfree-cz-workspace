# Register investigation artifacts through portal.yml

In `work/2026-09-14-restore-into-vps`, `dev-session artifact --help` failed with
`unknown command: artifact`. The stable CLI has no artifact subcommand.

Add useful files beneath the active session's tracking directory and register
them in its `portal.yml` under `artifacts`, with `label` and relative `path`.
Do not invoke lifecycle helpers to prepare a handoff.

Verified in `portal/internal/session/manifest.go` in the canonical dev-workspace
repository: artifact entries require those fields and reject unknown keys.
