# Use confctl build --yes in verification watchers

`confctl build <machine>` prompts Continue? [y/N]. Without a terminal/input stream,
a watcher gets end of file reached and no target build completes. The pinned
`confctl build --help` documents command option `-y, --yes`; use
`nix develop --command confctl build --yes <machine>` for an already-authorized
local build. This is build confirmation only, never deployment authorization.
Keep exact project pwd and tested HEAD guards on watcher commands.

Evidence: work/2026-10-21-aitherdev-observability-access/acceptance-verification-02.log;
subsequent host-build logs/result in that session.
