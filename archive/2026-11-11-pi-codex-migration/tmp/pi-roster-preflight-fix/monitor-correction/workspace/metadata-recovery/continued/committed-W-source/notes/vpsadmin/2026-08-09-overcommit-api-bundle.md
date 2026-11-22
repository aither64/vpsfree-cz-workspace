# Prepare the API bundle before committing root-only vpsAdmin changes

Related initiative: `work/2026-08-09-test-vm-kernel-oops/`

## Symptom

The vpsAdminOS flake update was staged correctly, but the pre-commit
`VpsadminApiI18n` hook failed because the root development shell did not have
the API's Active Record bundle installed.

## Cause and workaround

The repository-level shell prepares `.gems`, while the API hook runs with
`BUNDLE_GEMFILE=api/Gemfile` and `BUNDLE_PATH=api/.gems`. Enter the API shell
once before retrying the commit:

```sh
nix develop .#api --command true
```

The API shell changes into `api/` and installs its bundle automatically; do not
append another `cd api` to its command.

## Verification

After preparing the API shell, all Nixfmt, migration, WebUI i18n, API i18n,
and commit-message hooks passed for the isolated flake lock commit.
