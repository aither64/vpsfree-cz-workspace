# New worktree checkout can fail after creation when hooks lack local gems

`dev-session worktree add` returned exit78 because the shared Overcommit
postcheckout hook could not find Gemfile.lock dependencies in the ambient shell.
The command had already created the correct branch/worktree and registered the
project in portal.yml. Inspect those effects before retrying; do not recreate or
reset the branch and do not bypass hooks.

In the already-created worktree, enter the pinned environment with `nix develop`.
Its confctl shell bootstraps ignored .gems/.bundle state. Verified with
`bundle check`, Ruby3.4.9, `bundle exec overcommit --version` (0.73.0), and tool
lookup for nixfmt/confctl, all exit0. Existing shared hooks were already installed.
Future commits still require their ordinary hooks.

Evidence: work/2026-10-21-aitherdev-observability-access/environment-check.log.
