# Overcommit signature in a new confctl worktree

## Symptom

`git worktree add` created the worktree but its post-checkout hook stopped with
`Signature of configuration file has changed!`.

## Cause

Overcommit configuration signatures are worktree-local Git configuration. A
new worktree did not inherit a valid signature for the repository's current
`.overcommit.yml`.

## Fix and verification

From the new worktree, run:

```sh
nix develop --command overcommit --sign
```

The command completed successfully and updated only worktree-local Git
configuration. Run hook-bearing Git operations through the same development
shell, for example `nix develop --command git push ...`; an ambient `git push`
can invoke a different Overcommit installation and reject the just-created
signature. Do not bypass the hook. Related initiative:
`work/2026-08-03-gh-runner-gc/`.
