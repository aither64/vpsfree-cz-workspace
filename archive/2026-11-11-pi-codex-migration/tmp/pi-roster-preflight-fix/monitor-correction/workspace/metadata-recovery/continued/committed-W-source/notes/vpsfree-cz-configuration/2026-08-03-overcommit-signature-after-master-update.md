# Refresh Overcommit signature after updating the worktree base

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`

## Symptom

`confctl inputs channel update --commit vpsadmin` updated `flake.lock`, but its
commit failed with `Signature of configuration file has changed!` even though
the shared Overcommit hooks were installed.

## Cause

The bare repository's installed hook signature predated the current
`.overcommit.yml` on `origin/master`. A newly created worktree can therefore
have active hook scripts but still reject the first commit after its base is
updated.

## Fix

Review the checked-in hook configuration, then run the following from the
repository's Nix shell:

```sh
overcommit --sign
overcommit --run
```

For a failed generated channel commit, restore only the generated lock change
and rerun the original `confctl ... --commit` command. This lets `confctl`
recreate both the lock update and its generated commit message; do not replace
it with a hand-written dependency commit.

## Verification

Both `Nixfmt` and `RuboCop` passed, and the retried command created the expected
one-file channel commit.
