# Run confctl Git hooks in the development shell

## Symptom

`git push` from the ambient shell rejected a clean, hook-verified branch with
`Signature of configuration file has changed`, even after running
`overcommit --sign` in `nix develop`.

## Cause

The installed Git hook has an `env ruby` shebang. The ambient system Ruby
loaded Overcommit 0.71.0, while confctl's development shell and bundle use
Overcommit 0.68.0. The two versions calculate different configuration
signatures, so signing with the repository version and executing the hook with
the ambient version still fails.

## Workaround and verification

Sign and run the Git operation through the repository development shell:

```sh
nix develop -c bundle exec overcommit --sign
nix develop -c git push ...
```

The pre-push hook then loads the same Overcommit version used to create the
signature. This successfully pushed the final branch for initiative
`work/2026-06-15-vpsadmin-events` without bypassing hooks.
