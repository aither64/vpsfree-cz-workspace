# Noninteractive development session startup

Related initiative: work/2026-09-12-portal-review-experience/.

`dev-session start <name> --no-attach` still requires `--goal-file` when its
input is not interactive. Prepare the initial tracking commit first, then start
the exact slug with `--as-is --goal-file FILE --no-attach`.

For a coordinating process outside the helper-created terminal, `dev-session
current` requires both `DEV_SESSION_SLUG` and `DEV_SESSION_WORKSPACE` (the
canonical workspace root). Setting only the slug produces “session environment
is not managed by this workspace.” The two-variable lookup returned the newly
created slug after startup. Do not set these variables to adopt another session.
