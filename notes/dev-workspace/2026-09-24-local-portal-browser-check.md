# Local portal browser check can fail outside the changed case

The full generic `dev-workspace` portal browser suite failed locally in its
pre-existing page-lifecycle timing case while reporting TLS handshake errors.
The cause was not established, so this is not evidence that the Team-settings
change failed. The new Team-settings regression passed when run in isolation
with the pinned Nix Playwright package and browsers. Keep the full-suite
failure visible in the initiative record and use CI plus the focused case as
separate evidence; do not silently describe the whole local suite as passed.

Observed during `work/2026-09-24-team-settings-write-access/`; that session's
state records the verification result.
