# Rebase onto an explicit fetched default branch

In the configuration bare clone, `git fetch origin` populated FETCH_HEAD with
multiple branches. `git rebase FETCH_HEAD` chose a historical nondefault branch
and attempted to replay thousands of commits. Hooks stopped the first commit
because the historical tree had no .overcommit.yml.

Run `git rebase --abort`, verify the feature head is restored, then fetch the
exact target: `git fetch origin refs/heads/master:refs/remotes/origin/master`.
Rebase onto `refs/remotes/origin/master`, never the ambiguous FETCH_HEAD from a
multi-ref fetch. Aborting restored the exact committed feature with only its
existing untracked bundle caches. No unrelated worktree or branch was changed.

Related initiative: work/2026-09-16-portal-upload-recovery/.
