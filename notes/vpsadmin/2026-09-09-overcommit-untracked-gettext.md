# Untracked PHP files affect gettext checks during split commits

When splitting API and WebUI commits, Overcommit temporarily stashes tracked
unstaged WebUI/catalog changes but leaves untracked PHP files in place.
The gettext hook scans those files and reports a stale catalog for the otherwise
consistent API-only commit.

Temporarily move the untracked feature PHP files outside the checkout, commit the
API with all hooks enabled, then restore them in an ensure/finally block and
commit the WebUI with its generated catalogs. Do not bypass the gettext hook or
regenerate unrelated intermediate catalogs.

Observed in work/2026-09-09-ip-release-mechanism/. Both split commits subsequently passed all hooks.
