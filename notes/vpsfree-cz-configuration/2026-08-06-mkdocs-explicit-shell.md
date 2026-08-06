# Build configuration documentation with an explicit MkDocs shell

Related initiative: `work/2026-08-06-node-kernel-history`

`nix develop -c mkdocs build --strict` fails with `mkdocs: not found` because
the `vpsfree-cz-configuration` development shell contains deployment and hook
tools, but not MkDocs.

Run the documentation check without changing the repository shell:

```shell
nix shell nixpkgs#python3Packages.mkdocs -c \
  mkdocs build --strict --site-dir /tmp/PROJECT-mkdocs
```

Use a task-specific temporary output path so the check does not create an
untracked `site/` directory. This command successfully built the livepatch
history deployment runbook with strict warnings enabled.
