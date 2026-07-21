# Node Software Revision Links State

## Status

- Initiative: `2026-07-21-node-software-revision-links`.
- Status: complete. Reviewed heads were fast-forwarded to all affected default
  branches and pushed.
- Production diagnosis: current Node evidence contains exact, current,
  error-free vpsAdminOS, vpsAdmin, nixpkgs and system-configuration revisions.
  The failure is isolated to generated WebUI repository-link configuration.

## Worktrees and bases

- `vpsadmin`
  - base: current `origin/master` at
    `b3ec1a757c51b639b6442cd2552401688061b3e3`;
  - worktree: `worktrees/2026-07-21-node-software-revision-links/vpsadmin`.
- `vpsfree-cz-configuration`
  - base: current `origin/master` at
    `a2482851753e4e23dec488a34ee3a318e6cb1db5`;
  - worktree:
    `worktrees/2026-07-21-node-software-revision-links/vpsfree-cz-configuration`.
- `vpsadmin-kb-captures`
  - base: current `origin/master` at
    `8f5395f3890792bb9dc7ceb1c379cbef481e26f5`;
  - worktree:
    `worktrees/2026-07-21-node-software-revision-links/vpsadmin-kb-captures`.

All branches are `2026-07-21-node-software-revision-links`; remotes use SSH.

## Findings

- The Nix module option used one attrset-valued `default` for the three
  standard repositories.
- Production explicitly defines only the nested
  `softwareRevisionLinks.system_configuration` key. This explicit option
  definition takes precedence over the whole option default, so the evaluated
  map contains only `system_configuration`.
- PHP correctly receives exact database revisions but renders `unavailable`
  when the component is absent from `SOFTWARE_REVISION_LINKS`.

## Command notes

- Ambient `git worktree add` triggered installed Overcommit post-checkout
  hooks without their bundled gems. The worktrees and branches were created
  successfully. Use each repository's Nix shell for hook-triggering Git
  operations, as documented in
  `notes/vpsfree-cz-configuration/2026-06-13-overcommit-hooks-need-nix-develop.md`.
- The first three `confctl inputs channel set` attempts used an incorrectly
  expanded SHA derived from the short commit ID. GitHub returned 404 for that
  nonexistent revision; no lock file or commit changed. The commands were
  rerun with the exact `git rev-parse HEAD` value
  `f82b24144219e1c23df3255188a92c810078a5a6` and succeeded.

## Feature heads

- `vpsadmin`: `88f03da4455f4d709ca64785b1db14db834f323a`
  (`webui: preserve standard software revision links`).
- `vpsfree-cz-configuration`:
  `d2bc1e4cf88cea61ad157724718ea82f0fa9ad08`, with generated channel commits
  for services, staging and production.
- `vpsadmin-kb-captures`:
  `6d10db326ff3fdfc7361d3510fdc9ba32500aea0`, pin-only contract update.
- All three feature branches are pushed to origin.

The branches were rebased onto current defaults before review. The two
unmerged rounds of configuration and KB vpsAdmin pins were folded into one
final generated update per channel and one final KB pin commit. Superseded
GitHub Actions for the old vpsAdmin head were cancelled; no stale run remains
queued or in progress.

## Verification log

- Focused vpsAdmin check
  `nix build .#checks.x86_64-linux.webui-software-revision-links --no-link`
  passed. It evaluates the enabled NixOS module with an added
  `system_configuration` link and requires all four repository mappings.
- Direct module evaluation returned the expected `nixpkgs`, `vpsadmin`,
  `vpsadminos` and `system_configuration` keys.
- `git diff --check` passed and both changed Nix files pass Nixfmt.
- The complete vpsAdmin pre-commit hook selection for the Nix changes passed:
  migration-spec guard, API and WebUI i18n health, and Nixfmt.
- `nix flake check` cannot reach the new check because the existing
  `overlays.list` output is a list rather than an overlay function. The same
  failure reproduces unchanged at base `1bb84ae9`; the focused check passed.
  Durable details are recorded in
  `notes/vpsadmin/2026-07-21-flake-check-overlay-list.md`.
- Running Overcommit through `bundle exec` polluted the API hook's Bundler
  environment. After preparing the API gem environment, invoking `overcommit`
  directly from the root Nix shell ran the required hooks successfully.
- The vpsFree.cz configuration flake check passed.
- A full build of `cz.vpsfree/vpsadmin/int.webui1` at the pinned feature head
  passed. Its generated `/etc/vpsadmin/config.php` contains commit prefixes for
  `nixpkgs`, `vpsadmin`, `vpsadminos` and `system_configuration`.
- All three configuration channels resolve vpsAdmin to exact revision
  `88f03da4455f4d709ca64785b1db14db834f323a`.
- KB `bin/check` passed: 39 controls, 29 paths, 32 capture concepts, 65
  bindings, 9 exceptions, 59 inventory concepts and 118 PNG variants.
- KB `nix flake check` passed. Only the four exact pin files changed; no
  screenshot or documentation content changed.
- After rebasing, the focused vpsAdmin check, configuration flake check,
  complete `int.webui1` build/generated-PHP inspection, KB contract check and
  KB flake check were rerun successfully at the final feature heads.
- GitHub Actions at vpsAdmin head `88f03da4`: API migration specs, RuboCop,
  WebUI PHPUnit, i18n health, client specs and libnodectld specs are green; API
  topic specs and integration CI are still running. Configuration and KB have
  no branch workflows.

## Mandatory review

- Standalone reviewer: `/root/software_revision_links_review`.
- Final result: no Blocking, Important or Advisory findings.
- Confirmed clean fast-forwardable histories, logical commit splits, exact
  cross-repository pins, correct per-key `mkDefault` semantics, canonical enum
  compatibility and absence of schema/protocol/backfill or KB content impact.
- Residual gaps: broad API/CI workflows were still running; aggregate vpsAdmin
  flake check remains blocked by the verified pre-existing `overlays.list`
  output; repository review cannot prove the production rollout premise or
  live-browser result. The documented production safety gate and post-deploy
  browser inspection remain operator steps.

## Default-branch integration and cleanup

- Fresh detached integration worktrees were created from the fetched remote
  default branches. Each merge used `git merge --ff-only` and was pushed in
  dependency order.
- Confirmed remote default refs:
  - vpsAdmin `master`:
    `88f03da4455f4d709ca64785b1db14db834f323a`;
  - vpsFree.cz configuration `master`:
    `d2bc1e4cf88cea61ad157724718ea82f0fa9ad08`;
  - vpsAdmin KB captures `master`:
    `6d10db326ff3fdfc7361d3510fdc9ba32500aea0`.
- Feature branches remain available on origin. Temporary integration and both
  superseded/current initiative project worktrees were removed.
- Development cluster `2026-07-20-node-evidence-compat-cleanup` completed a
  graceful stop and its GC root was removed.
- Master-head GitHub runs for RuboCop, WebUI PHPUnit, i18n health and client
  specs are green. API topic specs and integration CI are still running and
  were left untouched, as requested.
