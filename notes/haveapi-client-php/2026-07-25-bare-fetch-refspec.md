# Refresh remote-tracking refs in the PHP client bare clone

Initiative:
`work/2026-07-24-vpsfreectl-snapshot-download-fix/`

## Symptom

After the remote `master` branch was advanced to HaveAPI PHP client 0.29.6,
both of these commands left the canonical bare clone's `origin/master` at the
older 0.29.5 commit:

```sh
git --git-dir=repos/haveapi-client-php.git fetch origin master --tags
git --git-dir=repos/haveapi-client-php.git fetch origin
```

`git ls-remote` and the public tag correctly showed the new commit.

## Cause

Unlike the other canonical bare repositories, this clone has no
`remote.origin.fetch` refspec. Fetching an explicitly named branch updates
`FETCH_HEAD`, but does not create or advance `refs/remotes/origin/master`.
A plain fetch only follows the remote HEAD in this configuration.

## Workaround

Fetch the exact remote-tracking destination when a current
`origin/master` is required:

```sh
git --git-dir=repos/haveapi-client-php.git fetch origin \
  +refs/heads/master:refs/remotes/origin/master
```

After this command, `origin/master` advanced from the 0.29.5 commit
`03201f5` to the published 0.29.6 commit `27da693`, and all completed
initiative branches and release worktrees passed ancestry checks against it.
