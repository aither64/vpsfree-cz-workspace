# Run vpsAdmin hooks without leaking the root bundle

Related initiative: `work/2026-09-23-storage-redesign`.

In the repository's root Nix shell, `bundle exec git commit` passes the root
Bundler context to Overcommit's API i18n hook. That hook starts the API bundle,
which then fails to find root-only gems even though both bundles are installed.
Overriding `GEM_PATH` with only a private test cache also hides Overcommit from
the hook's Ruby process.

Run the normal hooks with `nix develop .#vpsadmin -c git commit -F <message-file>`
from the repository root. Keep the root shell's `GEM_HOME`, `GEM_PATH` and
`BUNDLE_GEMFILE` environment intact. This ran all pre-commit hooks, including
the API i18n health check, and committed `58eb29a8f` successfully. The API
locale files still had to be normalized with their catalog renderer before the
hook would pass; an environment change does not replace that check.
