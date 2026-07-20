# Populate API gems before running all vpsAdmin hooks

## Symptom

In a fresh vpsAdmin integration worktree, `nix develop .#vpsadmin -c overcommit
--run` passed migration selection and root/WebUI checks but
`VpsadminApiI18n` failed to load `activerecord`.

## Cause

The root development shell installs the root hook bundle in `.gems`. The custom
API i18n hook changes into `api/` and explicitly uses `BUNDLE_PATH=.gems`, so a
new worktree also needs the component-specific `api/.gems` bundle.

## Fix

Populate the API environment once, then rerun the complete root hook suite:

```sh
nix develop .#api -c bundle check
nix develop .#vpsadmin -c overcommit --run
```

The second command then passes `VpsadminApiI18n` and all other hooks. Do not
bypass the failed hook.

Related initiative:
`work/2026-07-20-kernel-boot-evidence-history/`.
