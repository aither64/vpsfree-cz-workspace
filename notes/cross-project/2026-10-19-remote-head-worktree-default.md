# Check a bare repository's remote HEAD before worktree registration

`dev-session worktree add` selected `origin/master` for vpsadmin-webui even
though upstream uses `main`, because the canonical bare clone had no symbolic
`refs/remotes/origin/HEAD`. The default attempt failed with an ambiguous
`origin/master`; supplying `--base origin/main` created the checkout but still
recorded `default_branch: master` in the portal registration.

Before first registration, verify the authoritative default branch and run
`git --git-dir=repos/PROJECT.git remote set-head origin -a` if the local remote
HEAD is missing. Fetch its remote-tracking branch, then register using the
repository's required feature branch name and base. The set-head command
corrected the remote HEAD to `main` in this case.

Existing portal registrations retain their default branch through ordinary
sync/re-add. Correcting the remote HEAD does not repair those records. Do not
invent an `origin/master`, edit retained branch history, or hand-edit the portal
to conceal the mismatch. Record the actual target and resolve the registration
through supported metadata maintenance before eventual integration/completion.

Related initiative: `work/2026-10-19-haveapi-async-client/`.
