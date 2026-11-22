# Explicitly base capture worktrees on `origin/master`

## Symptom

`dev-session worktree add ... vpsadmin-kb-captures` based a new initiative
branch on `origin/2026-07-10-kb-czech-fixes`, leaving it 28 commits behind the
current master branch.

## Cause

The repository's remote `HEAD` points to the old feature branch even though
`master` is the current integration branch. The session helper followed that
remote default pointer.

## Workaround

Pass `--base origin/master` when adding a new capture worktree. If an untouched
new branch was already created and its base is an ancestor of master, correct
it with:

```sh
git fetch origin
git merge --ff-only origin/master
```

## Verification

The initiative branch fast-forwarded from `4364db7` to `7248a8b`, exactly
matching `origin/master`, before any pin files were edited.

Related initiative:
`work/2026-08-03-webui-dataset-used-czech-fix/`.
