# Preserve the KB runtime pin when updating vpsAdmin

`nix flake update vpsadmin` can replace the contract repository's already-pinned
vpsAdminOS and transitive nixpkgs revisions with vpsAdmin's own older lockfile
entries. `nix develop -c bin/check` then reports a vpsadminos revision mismatch.
For a vpsAdmin-only change, preserve the contract's existing runtime with:

```
nix flake lock --override-input vpsadmin/vpsadminos github:vpsfreecz/vpsadminos/<existing-full-revision>
```

Check that the resulting lockfile diff changes only vpsAdmin. Do not update the
page contract's expected runtime just to accept an incidental downgrade. In
`work/2026-09-14-kernel-history-fix`, preserving revision
`6bdf458fd9105379860234ff33d352e55844f08f` restored all three unrelated lock entries;
the navigation and annotation checks already passed before this correction.
