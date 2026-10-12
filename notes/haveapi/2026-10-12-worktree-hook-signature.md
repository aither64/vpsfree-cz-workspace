# A failed checkout hook can leave a usable worktree

`dev-session worktree add` created the HaveAPI branch and checkout, then
reported failure because Overcommit rejected a changed configuration signature.
Inspect the owned checkout and hook configuration instead of trying to recreate
or remove the branch. The ambient shell may lack Overcommit even when Git hooks
invoke it through a wrapper.

After reviewing `.overcommit.yml` and its custom hooks, install/sign the hooks
with `bundle exec overcommit --install` and `bundle exec overcommit --sign` in
the repository Nix shell, then retry the ordinary registration command.
This session's retry succeeded and subsequent required hooks passed.

A later pre-rebase hook similarly refused a command run outside the repository
Nix shell. Normal signing and rebase within that shell succeeded; no hook bypass
was needed. Keep hook-managed Git commands in the declared toolchain.

Related session: `work/2026-10-11-diagnose-vpsadmin-api-exception/`.
