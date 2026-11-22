# Worktree checkout hook requires the locked bundle

## Symptom

`dev-session worktree add` created the `security-advisories` worktree and
branch, but Git returned exit 78 from the checkout hook because locked RuboCop
and parser gems were unavailable.

## Cause and workaround

The shared repository hooks invoke Overcommit while a new worktree has not yet
installed its worktree-local bundle. Enter the new worktree with `nix develop`
so its shell hook installs the locked gems, then install and sign Overcommit
before the first commit. Verify the branch and worktree after the initial
nonzero result instead of rerunning worktree creation blindly.

## Verification

For initiative
`work/2026-08-07-security-advisories-6-12-95-2`, the intended branch and
worktree were present at base commit `5d4138a` despite the exit status.
