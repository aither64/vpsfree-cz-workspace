---
lifecycle: active
---

# 2026-11-22-vpsadminos-nixpkgs-2611

## Status — discovery and design

- [x] Verify session identity, team, repository and upstream default.
- [ ] Settle the exact 26.11 source and port procedure; register the worktree.
- [ ] Port and pass quick checks; review the complete committed branch.
- [ ] Run focused integration/CI on the feature branch and hand off. No merge or deployment approved.

| Package | Owner | Dependencies / acceptance | Status / next result |
| --- | --- | --- | --- |
| Discovery and design | `architect0` | Read-only refs, project procedure, current pins and prior ports; sufficient implementation boundaries and check commands | Assigned; next result is exact upstream target and package brief in `design.md` |

## Repositories

`vpsfreecz/vpsadminos` default `staging`, remote HEAD observed at `e9d55bada43c888ae91139d549d156a0831817de`. Planned worktree `worktrees/2026-11-22-vpsadminos-nixpkgs-2611/vpsadminos`, same branch slug.

## Results and open questions

- `dev-session current` matches trusted binding after using `$HOME/bin:$HOME/.nix-profile/bin` in PATH.
- Initial `git ls-remote` on NixOS/nixpkgs returned `nixos-unstable` but neither `nixos-26.11` nor `release-26.11`. Need to verify an appropriate ref and its actual release line, not assume unstable is 26.11.
- Repository `AGENTS.md` and `docs/os/updates.md` inspected; the latter is the installed-system update guide, not a maintainer port guide. The design owner is checking upstream docs/history.

## Next action and cleanup

Register the feature worktree and dispatch implementation on a settled brief. No build, push, activation or temporary test data yet.
