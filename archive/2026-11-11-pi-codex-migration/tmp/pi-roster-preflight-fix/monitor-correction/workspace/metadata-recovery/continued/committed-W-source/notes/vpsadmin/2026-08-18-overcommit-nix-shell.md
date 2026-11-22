# Run vpsAdmin Overcommit hooks in the full development shell

## Symptom

Committing from the ambient workspace shell made the vpsAdmin pre-commit hook
report missing `rubocop`, `msgattrib`, and `mariadb`, even though focused checks
had passed in the API development shell.

## Cause

Overcommit executes all repository checks, including API and WebUI i18n hooks.
The ambient shell does not provide the combined Ruby, gettext, PHP, and database
tooling those hooks require.

## Workaround

Run the commit itself from the repository root in the full shell:

```sh
nix develop .#vpsadmin -c git commit -F COMMIT_MESSAGE_FILE
```

Do not bypass the hooks. The full shell lets the normal Overcommit entrypoint
run every declared check.

## Verification

The password-recovery initiative reran the unchanged staged commit this way so
all declared hooks could execute with their required tools.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`
