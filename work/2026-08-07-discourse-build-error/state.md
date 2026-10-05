---
lifecycle: active
---
# 2026-08-07-discourse-build-error

## Repositories

- `vpsfree-cz-configuration`
  - Worktree:
    `worktrees/2026-08-07-discourse-build-error/vpsfree-cz-configuration`
  - Branch: `2026-08-07-discourse-build-error`
  - Base: `origin/master` at `1d6ef004`

## Status

- Root cause confirmed and the obsolete local override removed.
- Fix committed as `338db498` (`packages: use upstream discourse ICU fix`).
- Mandatory standalone review completed with no findings.
- Full targeted build was stopped at the user's request; completed
  verification was accepted as sufficient for integration.
- Fast-forwarded the fix into `master` and pushed both `master` and the retained
  feature branch to origin.
- Previous initiative `2026-07-04-discourse-update` added that override because
  the then-current nixpkgs Discourse package incorrectly combined ICU 76 with
  Node/libv8 built for ICU 78.

## Commands run

- `bin/dev-session current`
- `git --git-dir=repos/vpsfree-cz-configuration.git fetch origin --prune`
- `bin/dev-session worktree add 2026-08-07-discourse-build-error
  vpsfree-cz-configuration --as-is --base origin/master`
- `rg -n --hidden --glob '!flake.lock' 'discourse|icu' ...`
- Inspected the repository-local `AGENTS.md`, relevant durable hook notes, Git
  history, and the prior Discourse fix initiative.
- `nix develop -c confctl build --yes cz.vpsfree/containers/discourse`
- Queried the upstream nixpkgs history for
  `pkgs/servers/web-apps/discourse/default.nix` and inspected commit
  `8bbc131cc0b9fb402cac14737ea87a31d2d4804d`.
- `nix develop -c overcommit --run`
- `nix build --dry-run --no-link --impure --no-write-lock-file
  --no-update-lock-file
  .#confctl.build.m_cz_vpsfree_containers_discourse_c2787e8f.toplevel
  .#confctl.build.m_cz_vpsfree_containers_discourse_c2787e8f.autoRollback`
- `nix develop -c bash -lc 'git add overlays/packages.nix && git commit
  -F /tmp/vpsfree-discourse-build-fix-commit-message.txt'`
- Began `nix develop -c confctl build --yes
  cz.vpsfree/containers/discourse`, then interrupted it on user request.
- `git fetch origin --prune`
- `nix develop -c git worktree add -b
  merge/2026-08-07-discourse-build-error-config
  worktrees/2026-08-07-discourse-build-error/merge/vpsfree-cz-configuration
  origin/master`
- `nix develop -c git merge --ff-only
  2026-08-07-discourse-build-error`
- `nix develop -c overcommit --run` in the merge worktree.
- `git fetch origin master` and verified that `origin/master` still matched the
  feature commit's parent.
- `nix develop -c git push origin HEAD:master`
- `nix develop -c git push -u origin
  2026-08-07-discourse-build-error`
- Queried GitHub Actions for the pushed commit and feature branch.

## Results

- The active process is correctly bound to the initiative slug.
- The feature worktree was created at `1d6ef004`. The helper returned non-zero
  because worktree hooks could not load Bundler gems in the ambient shell, but
  the branch and worktree were created successfully. Per existing workspace
  notes, all hook-triggering Git commands will run through `nix develop`.
- The pre-fix targeted build reproduced the reported evaluation failure:
  nixpkgs' Discourse function rejects the unexpected `icu` argument and
  suggests `icu78`.
- The break was introduced when configuration commit `5b9f46f5` advanced the
  stable/production/staging nixpkgs inputs from `04607e11` to `445d861c`.
  That update included nixpkgs commit `8bbc131c`, which fixed the original ICU
  mismatch by renaming the Discourse input from `icu` to `icu78` and using it
  for `mini_racer`. The local July workaround consequently became both invalid
  and redundant.
- Removed the local `discourse = super.discourse.override { icu = ...; };`
  overlay so the fixed upstream package is used directly.
- Repository hooks passed: Nixfmt and RuboCop both reported OK.
- The post-fix dry-run evaluated both the target system and automatic rollback
  attributes successfully. It selected upstream `discourse-2026.1.4`,
  `discourse-ruby-env-2026.1.4`, and `nodejs-slim-22.23.2`; 84 local
  derivations remain for the full build.
- Commit hooks passed. The commit-message hook emitted non-failing 72-column
  warnings; every commit-message line is within the workspace's 80-column
  limit.
- Mandatory change review found no Blocking, Important, or Advisory findings.
  The reviewer confirmed that removing the override preserves Discourse 2026.1.4
  and the same derivation as an explicit `icu78 = pkgs.icu78` override. Residual
  gaps before integration were the full 84-derivation build, including
  `mini_racer` linkage/assets, and the intentionally deferred runtime smoke
  test after deployment.
- Before interruption, the full build fetched all 422 substitutes and completed
  64 of 84 local derivations. It reached the active
  `discourse-assets-2026.1.4` Ember production build without reproducing the ICU
  evaluation or Ruby environment failure. The asset derivation and final system
  closure did not finish, so this is not recorded as a successful full build.
- The user explicitly accepted the completed hook run, exact target dry-run,
  mandatory review, and partial full-build progress as sufficient and requested
  immediate merge/push/cleanup.
- The temporary merge branch fast-forwarded from `1d6ef004` to `338db498`.
  Post-merge Nixfmt and RuboCop hooks passed.
- Pushed `master` from `1d6ef004` to `338db498` over SSH. Pushed and retained
  `origin/2026-08-07-discourse-build-error` at the same commit.
- No GitHub Actions runs were created for the pushed commit or feature branch.

## Open questions

- None currently.

## Cleanup

- Direct `rm -rf` of the explicitly inspected cache directories was rejected by
  the execution environment's safety guard before anything was removed.
- Removed the temporary merge and feature worktrees with scoped
  `git worktree remove --force`; their only untracked content was generated
  `.bin`, `.bundle`, `.rubocop_cache`, and `.confctl` data.
- Pruned the worktree registry and removed the now-empty initiative worktree
  directories.
- Retained local and remote `2026-08-07-discourse-build-error` at `338db498`.
  The local temporary merge branch also remains at the same commit; no branch
  refs were deleted.
- Cleanup complete.
