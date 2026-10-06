---
lifecycle: abandoned
---
# 2026-07-04-discourse-update

## Repositories

- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-07-04-discourse-update/vpsfree-cz-configuration`
  - Branch: `2026-07-04-discourse-update`
  - Base: `origin/master` at `7343069fc473ff1b6203d18fc2f800af18626c2a`

## Status

- Investigated Discourse deployment build failure.
- Root cause: nixpkgs `pkgs.discourse` builds `mini_racer` against default
  `pkgs.icu` 76.1, while `nodejs-slim_22.libv8` references ICU 78 symbols.
  Loading `mini_racer` fails with:
  `undefined symbol: _ZN6icu_788ByteSink15GetAppendBufferEiiPciPi`.
- Applying a narrow overlay to build Discourse with `icu78`.
- Fixed locally; targeted Discourse build now succeeds.
- Committed fix as `b37bba9a` (`packages: build discourse with icu78`).
- Merged to `master` with a fast-forward and pushed to origin.
- Cleaned up feature and temporary merge worktrees.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-07-04-discourse-update
  vpsfree-cz-configuration --as-is --branch 2026-07-04-discourse-update
  --base origin/master`
- `nix develop -c confctl --help`
- `nix develop -c confctl ls | rg discourse`
- `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
- `nix log /nix/store/wczq6pcgh7bwp6kgy3259zk066cj4n8c-discourse-assets-2026.1.4.drv`
- `nix-store --read-log /nix/store/wczq6pcgh7bwp6kgy3259zk066cj4n8c-discourse-assets-2026.1.4.drv`
- `nix eval --impure --expr 'let flake = builtins.getFlake (toString ./.);
  pkgs = import flake.inputs.nixpkgsStable { system = builtins.currentSystem; };
  in { icu = pkgs.icu.version; icu76 = pkgs.icu76.version; icu78 =
  pkgs.icu78.version; nodejs22 = pkgs.nodejs-slim_22.version; }'`
- `nix eval --impure --expr 'let flake = builtins.getFlake (toString ./.);
  pkgs = import flake.inputs.nixpkgsUnstable { system = builtins.currentSystem; };
  in { discourse = pkgs.discourse.version; icu = pkgs.icu.version; icu78 =
  pkgs.icu78.version; nodejs22 = pkgs.nodejs-slim_22.version; }'`
- `nix eval --impure --expr 'let flake = builtins.getFlake
  "github:NixOS/nixpkgs/nixos-unstable"; pkgs = import flake { system =
  builtins.currentSystem; }; in { rev = flake.rev or null; discourse =
  pkgs.discourse.version; icu = pkgs.icu.version; icu78 =
  pkgs.icu78.version; nodejs22 = pkgs.nodejs-slim_22.version; }'`
- `nix develop -c overcommit --run`
- Ambient `git commit -F <tmpfile>` failed because Overcommit's bundled gems
  are provided by the Nix development shell, not the ambient shell.
- `nix develop -c bash -lc 'git add overlays/packages.nix; git commit -F
  <tmpfile>'`
- `git fetch origin --prune`
- `git worktree add -B merge/2026-07-04-discourse-update-config
  worktrees/2026-07-04-discourse-update/merge/vpsfree-cz-configuration
  origin/master`
- `git -C worktrees/2026-07-04-discourse-update/merge/vpsfree-cz-configuration
  merge --ff-only 2026-07-04-discourse-update`
- `nix develop -c overcommit --run`
- `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
- `git push origin HEAD:master`
- `git worktree remove
  worktrees/2026-07-04-discourse-update/merge/vpsfree-cz-configuration`
- `git worktree remove
  worktrees/2026-07-04-discourse-update/vpsfree-cz-configuration`
- `git worktree prune`

## Results

- `nix develop -c confctl build --yes cz.vpsfree/containers/discourse` failed
  before the fix, matching the reported deployment error.
- Full builder log showed the real exception above the trimmed stack:
  `Bundler::GemRequireError` loading `mini_racer` due to an ICU 78 symbol
  missing from the linked ICU 76 libraries.
- `ldd` confirmed `mini_racer_extension.so` was linked to
  `/nix/store/657ny...-icu4c-76.1/lib/libicui18n.so.76`.
- The current pinned `nixpkgsUnstable` input and upstream
  `github:NixOS/nixpkgs/nixos-unstable` both resolve to
  `65179426c83bb3f6bc14898b42ea1c6f01d374b0` for this check. They still have
  `discourse = 2026.1.4`, `pkgs.icu = 76.1`, `icu78 = 78.3`, and
  `nodejs-slim_22 = 22.23.1`; switching Discourse to nixos-unstable would not
  fix this failure as of 2026-07-04.
- After overriding Discourse's `icu` argument to `icu78`,
  `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
  succeeded and built generation `2026-07-04--13-05-55`.
- `nix develop -c overcommit --run` passed: `Nixfmt` OK and `RuboCop` OK.
- Commit hooks passed for `b37bba9a`; commit-msg hooks emitted non-failing
  warnings for lines longer than 72 columns. All commit message lines are
  within the workspace 80-column limit.
- Mandatory change review by standalone reviewer found no Blocking, Important,
  or Advisory findings. Residual risks: no runtime activation/smoke test has
  been run yet, and the override should be revisited after future nixpkgs bumps
  because upstream may fix or change the ICU/Node combination.
- Fast-forward merge in temporary default-branch worktree succeeded.
- Post-merge `nix develop -c overcommit --run` passed.
- Post-merge `nix develop -c confctl build --yes
  cz.vpsfree/containers/discourse` succeeded and built generation
  `2026-07-04--13-33-23`.
- Pushed `master` to origin at
  `b37bba9a0ff136fb9131887010a87378d0cbdbf9`.
- GitHub printed an unrelated Dependabot vulnerability notice for the default
  branch during push.

## Open questions

- None currently.

## Cleanup

- Removed generated `.bin/`, `.bundle/`, and `.rubocop_cache/` from the
  worktree.
- Removed generated `.confctl`, `.bin`, `.bundle`, and `.rubocop_cache`
  directories from feature and merge worktrees before removing the worktrees.
- Removed the feature worktree and temporary merge worktree. Local branch refs
  were retained per workspace policy.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
