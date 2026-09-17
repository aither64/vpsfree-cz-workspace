---
lifecycle: active
---

# 2026-09-17-config-shell-ignores

## Status

Implementation started after the user accepted the plan. No process session
existed; created this initiative with dev-session start --no-codex --no-attach.
The user authorized master integration, targeted generated-directory removal,
and one general review. All sessions must remain open.

## Evidence and next actions

Planning traced the files to confctl revision
7bee58a52372b95c2198ce3f2a719807a3c2c66b, nix/flake/mk-config-devshell.nix.
All seven .bin directories contain the same Bundler-generated rubocop binstub;
all .bundle directories contain only config with BUNDLE_PATH and BUNDLE_BIN
pointing to their worktree. The one .rubocop_cache contains five empty JSON
arrays under RuboCop's cache-key directories. No tracked files or symlinks were
found in these directories. The proposed rules explain all untracked files.

Next: create the registered worktree, add ignore rules, verify/hooks/commit,
review once, fast-forward master, then revalidate and clean exact allowlist.

## Repositories and documentation

- vpsfree-cz-configuration: branch 2026-09-17-config-shell-ignores, planned
  worktree worktrees/2026-09-17-config-shell-ignores/vpsfree-cz-configuration.
- Root .gitignore comment owns the lasting rationale; a workspace note will
  preserve the diagnosis and recovery lesson.
- Portal: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-17-config-shell-ignores/

## Operational notes

Noninteractive dev-session start without a goal file was refused before
creation. --no-codex creates tracking and a portal session without starting a
duplicate conversation. Shared master has many unrelated dirty records; stage
only this initiative's paths. Root repository declares no hook framework.
