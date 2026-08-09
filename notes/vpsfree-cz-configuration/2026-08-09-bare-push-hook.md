# Push configuration branches from a worktree

Related initiative:
`work/2026-08-09-supervisor-exceptions/`

## Symptom

Running `git push` from the canonical bare
`repos/vpsfree-cz-configuration.git` clone failed in `hooks/pre-push` with:

```text
No such file or directory @ rb_sysopen - .overcommit.yml
```

## Cause

The installed pre-push hook resolves `.overcommit.yml` relative to the current
working directory. A bare clone has repository metadata but no checked-out
configuration file for the hook to read.

## Fix and verification

Create or retain a clean worktree for the branch and run the push through the
repository development shell:

```sh
nix develop -c git push --set-upstream origin BRANCH
```

This preserves the normal pre-push hook. It successfully pushed the retained
configuration feature branch at `8888cc735`; the short-lived worktree and its
generated shell caches were then removed.
