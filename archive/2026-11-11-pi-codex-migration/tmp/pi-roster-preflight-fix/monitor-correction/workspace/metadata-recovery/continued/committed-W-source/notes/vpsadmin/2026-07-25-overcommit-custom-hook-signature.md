# vpsAdmin custom Overcommit hook signature

## Symptom

An otherwise valid commit stops before running checks and reports that
`VpsadminApiI18n` in `.git-hooks/pre_commit/vpsadmin_api_i18n.rb` was added or
changed.

## Cause

Overcommit requires each worktree/user environment to trust the repository's
custom hook implementation before executing it. Installing the shared Git
hooks does not necessarily establish that plugin signature.

## Fix

Inspect the referenced repository hook. Because the calculated signature can
change when the Nix development closure changes, sign and run the hooks in the
same shell invocation:

```sh
nix develop --command bash -c \
  'overcommit --sign pre-commit && overcommit --run'
```

Then retry the original commit without bypassing hooks. Its commit-time hooks
must still run normally, including `VpsadminApiI18n`.

## Verification

During `work/2026-07-24-ct-start-hang`, a signature created in an earlier Nix
shell was rejected after the shell closure changed. Signing and running in one
invocation passed Nixfmt, migration specs, WebUI i18n, API i18n, PHP CS Fixer,
and the remaining pre-commit checks.
