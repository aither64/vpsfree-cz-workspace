# Configuration worktree hooks require the Nix shell

`git worktree add` for vpsfree-cz-configuration can create the worktree and then
exit 78 because its post-checkout Overcommit hook cannot find the declared
Ruby gems in the ambient shell. The worktree and branch already exist; inspect
them before attempting creation again.

From that worktree, run `nix develop -c true` to populate its declared `.gems`
environment, then `nix develop -c bundle exec overcommit --install` to confirm
hook installation. Use the Nix shell for subsequent commits and confctl input
updates. Both commands succeeded for
`work/2026-10-02-portal-creation-performance/`. The failed post-checkout hook
does not justify bypassing commit hooks.
