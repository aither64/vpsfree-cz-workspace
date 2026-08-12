# Prepare the API bundle before vpsAdmin Overcommit

## Symptom

`nix develop -c git commit` reached the `VpsadminApiI18n` pre-commit hook but
failed with `Bundler::GemNotFound` for ActiveRecord.

## Cause

The root development shell prepares the top-level bundle in `.gems`. The API
i18n hook changes to `api/` and needs the separate `api/.gems` bundle, which
had not yet been prepared in the new worktree.

## Fix

Prepare both shells before committing changes that run the API i18n hook:

```sh
nix develop .#api -c true
nix develop -c git commit -F /path/to/commit-message
```

## Verification

The second commit attempt passed all six pre-commit hooks after the API shell
installed its bundle. Related initiative:
`work/2026-08-09-kb-kvm-review`.
