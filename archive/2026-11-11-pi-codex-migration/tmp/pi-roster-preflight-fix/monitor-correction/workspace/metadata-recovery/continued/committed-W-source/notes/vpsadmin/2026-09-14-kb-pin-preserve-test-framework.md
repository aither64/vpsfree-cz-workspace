# Preserve the KB test-framework pin during API input updates

Initiative: `work/2026-09-13-auth-email/`.

`nix flake update vpsadmin` in `vpsfree-kb-contracts` also replaced its nested
vpsAdminOS pin and Nixpkgs inputs with the older revisions from vpsAdmin's own
lock. This was unintended: the contract repository had separately pinned
vpsAdminOS 6bdf458fd9105379860234ff33d352e55844f08f for classified retry support
(commit 34d1a14), while the API repository still selected 8e44a512.

After the normal exact API update, restore that deliberate nested pin through
Nix, without editing the lockfile manually:

```sh
nix flake update vpsadmin/vpsadminos --override-input vpsadmin/vpsadminos \
  github:vpsfreecz/vpsadminos/6bdf458fd9105379860234ff33d352e55844f08f
```

The final lock diff changed only the intended vpsAdmin node; vpsAdminOS and its
Nixpkgs graph matched the predecessor exactly. Confirm the currently intended
framework revision from repository history before reusing this command.
