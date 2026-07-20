# Fresh vpsAdmin worktrees need both hook dependency sets

Initiative: `work/2026-07-20-kernel-boot-evidence-history`

## Symptom

A commit in a freshly created vpsAdmin rewrite worktree could not run the
declared Overcommit checks because repository-local API or root gems were not
installed. The source changes and index were preserved; no commit was created
and no hook was bypassed.

## Cause

The API and repository hook dependencies are installed into worktree-local
`.gems` directories. A new worktree does not inherit those generated files
from another initiative worktree.

## Fix

Initialize the API dependency set with:

```shell
nix develop .#api -c true
```

Then run the commit itself through the root development shell:

```shell
nix develop -c git commit -F /tmp/commit-message
```

The root shell installs its own hook bundle when necessary. After both sets
were present, MigrationSpecs, Nixfmt, API/WebUI i18n and RuboCop hooks passed.
