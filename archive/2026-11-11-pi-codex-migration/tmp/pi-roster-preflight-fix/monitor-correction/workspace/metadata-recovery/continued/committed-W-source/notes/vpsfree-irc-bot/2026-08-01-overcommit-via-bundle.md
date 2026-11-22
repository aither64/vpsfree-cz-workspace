# Run vpsfree-irc-bot Overcommit Through Bundler

Related initiative: `work/2026-06-15-vpsadmin-events/`.

In a fresh `vpsfree-irc-bot` worktree, this command can install the bundle but
then fail with `exec: overcommit: not found`:

```sh
nix develop --command overcommit --sign
```

The development shell installs Overcommit in the repository bundle without
putting its executable directly on `PATH`. Run hook setup and checks through
Bundler instead:

```sh
nix develop --command bundle exec overcommit --sign
nix develop --command bundle exec overcommit --run
```

Both commands completed successfully in the initiative worktree.
