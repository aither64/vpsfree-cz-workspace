# vpsAdminOS feature rebases target `staging`

Related initiative: `work/2026-07-13-security-advisory-automation/`

## Symptom

Running an autosquash rebase from a merge base computed against
`origin/master` began replaying the repository from its root and queued roughly
1,800 unrelated commits.

## Cause

The vpsAdminOS upstream default branch is `staging`; `origin/master` is absent.
An empty merge-base argument made the rebase behave like a root rebase.

## Workaround

Before rebasing, identify the upstream default with
`git symbolic-ref refs/remotes/origin/HEAD` and use `origin/staging` for
vpsAdminOS. If a rebase unexpectedly starts replaying unrelated history,
interrupt it and run `git rebase --abort` before making other changes.

The feature branch was restored unchanged after aborting, then successfully
autosquashed from its merge base with `origin/staging`.
