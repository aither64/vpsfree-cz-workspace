# Stale `origin/HEAD` after a default-branch change

Related initiative: `work/2026-08-06-node-kernel-history`

## Symptom

`git symbolic-ref refs/remotes/origin/HEAD` reported
`origin/2026-07-10-kb-czech-fixes`, although GitHub's current default branch
was `master`. Trusting the symbolic ref would have fast-forwarded an obsolete
target through many unrelated commits.

## Cause

The bare repository's locally cached remote HEAD was not refreshed after the
GitHub default branch changed.

## Workaround

Before merging into a repository's default branch, query GitHub directly:

```sh
gh api repos/vpsfreecz/vpsadmin-kb-captures --jq .default_branch
```

If needed, refresh the cached symbolic ref separately with `git remote
set-head origin --auto`; do not infer the merge target from a stale local
symbolic ref.

## Verification

The REST API returned `master`. `origin/master` was the feature branch's
immediate parent, so the intended integration was a one-commit fast-forward.
