# Preserve an ahead local master during release integration

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

After fetching `origin/master`, the canonical bare repository's local
`master` was at an unrelated unpushed commit while `origin/master` remained
behind it. A release worktree created from local `master` would therefore
include another session's change.

## Cause

Local branches in the shared canonical bare repository can outlive or be
advanced by other development sessions independently of their upstream
tracking refs.

## Safe workflow

Inspect both refs before creating the target worktree. If local `master`
differs from `origin/master`, leave it untouched and create a clean detached
worktree from the fetched remote ref:

```sh
git worktree add --detach TARGET origin/master
```

Fast-forward the detached worktree to the reviewed feature head, validate it,
and push explicitly as `HEAD:refs/heads/master` with a lease for the fetched
upstream commit.
