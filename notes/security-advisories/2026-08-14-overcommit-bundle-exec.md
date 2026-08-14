# Install security-advisories Overcommit through Bundler

Related initiative: `work/2026-08-14-advisories-6-12-95-5`.

Command and symptom:

```sh
nix develop --command overcommit --install
```

The development shell installed the locked bundle into the repository-local
`.gems` directory, then failed with `exec: overcommit: not found`. The freshly
installed executable was not available directly on the shell command path.

Use the locked Bundler context explicitly:

```sh
nix develop --command bundle exec overcommit --install
```

This installed the hooks successfully. Continue to invoke Overcommit checks as
`nix develop --command bundle exec overcommit --run` so the same locked bundle
is used.

The installed Git hooks also expect this environment. Ambient `git commit` and
`git push` commands failed because Bundler could not find the locked gems even
though `.gems` already contained them. Run Git itself in the development shell:

```sh
nix develop --command git commit -F <message-file>
nix develop --command git push <arguments>
```

The hooks then found the locked bundle and completed normally.
