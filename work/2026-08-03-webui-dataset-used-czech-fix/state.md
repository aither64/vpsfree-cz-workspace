# 2026-08-03-webui-dataset-used-czech-fix

## Repositories

- `vpsadmin`: branch `2026-08-03-webui-dataset-used-czech-fix`, worktree
  `worktrees/2026-08-03-webui-dataset-used-czech-fix/vpsadmin`, based on
  `origin/master` at `ae5dd5e01`.
- `vpsadmin-kb-captures`: branch
  `2026-08-03-webui-dataset-used-czech-fix`, worktree
  `worktrees/2026-08-03-webui-dataset-used-czech-fix/vpsadmin-kb-captures`,
  corrected to base `origin/master` at `7248a8b` before edits.
- `vpsfree-cz-configuration`: branch
  `2026-08-03-webui-dataset-used-czech-fix`, worktree
  `worktrees/2026-08-03-webui-dataset-used-czech-fix/vpsfree-cz-configuration`,
  based on current `origin/master` at `1fb5274a`.
- Temporary vpsAdmin target worktree:
  `worktrees/2026-08-03-webui-dataset-used-czech-fix/vpsadmin-master`.

## Status

- Root cause identified and corrected in source and gettext catalogs.
- Focused regression coverage passes for English and real Czech gettext output.
- Commit `2f9546ce8` contains the intended vpsAdmin change.
- Mandatory standalone review completed with no findings; documentation
  contract revision is pinned and its lock update/check remain.

## Commands run

- `bin/dev-session current`
- `git status --short --branch` (workspace)
- inspected the initiative tracking files and canonical vpsAdmin remote
- `bin/dev-session worktree add 2026-08-03-webui-dataset-used-czech-fix
  vpsadmin --as-is`
- inspected vpsAdmin `AGENTS.md`, `doc/i18n-cs.md`, and the canonical
  `vpsadmin-kb-captures/docs/webui-change-workflow.md`
- searched all WebUI consumers and gettext messages with boundary whitespace
- `webui/lang/scripts/locales-update` (failed: ambient shell lacks gettext)
- `nix develop .#webui -c webui/lang/scripts/locales-update` (failed because
  the component shell already changes into `webui/`)
- `nix develop .#webui -c lang/scripts/locales-update`
- `nix develop .#webui -c composer install`
- `nix develop .#webui -c lang/scripts/locales-generate`
- `nix develop .#webui -c vendor/bin/phpunit
  tests/Regression/DataSizeFormattingTest.php`
- `nix develop .#webui -c lang/scripts/locales-update --check`
- `nix develop .#webui -c vendor/bin/phpunit`
- `nix develop -c bundle exec overcommit --run` (API-i18n failed because the
  fresh worktree's API bundle was not installed)
- `nix develop .#api -c bundle check` (component shell installed and verified
  the API bundle)
- `nix develop -c env -u RUBYOPT overcommit --run`
- `nix develop -c env -u RUBYOPT git commit -F <temporary-message-file>`
- `git fetch origin` and `git push -u origin
  2026-08-03-webui-dataset-used-czech-fix` (vpsAdmin)
- `bin/dev-session worktree add 2026-08-03-webui-dataset-used-czech-fix
  vpsadmin-kb-captures --as-is`
- `git merge --ff-only origin/master` (capture branch base correction)
- `nix flake update vpsadmin` (capture repository)
- `nix develop -c bin/check` (capture repository)
- `nix develop -c bin/devcluster start
  2026-08-03-webui-dataset-used-czech-fix-captures --topology screenshots`
- attempted the six affected Czech/English checkpoint captures; fixture setup
  failed while looking for the seeded `Praha` location
- inspected the isolated services database and the browser-visible WebUI data
- stopped the bridge capture cluster and started rebuilding the same isolated
  cluster with `--network local`
- `git fetch origin`, fresh `master` worktree creation, and
  `git merge --ff-only 2026-08-03-webui-dataset-used-czech-fix` (vpsAdmin)
- `nix develop .#webui -c composer install --no-interaction --no-progress`
  and focused PHPUnit from the vpsAdmin target worktree
- `git push origin master` (vpsAdmin)
- `bin/dev-session worktree add 2026-08-03-webui-dataset-used-czech-fix
  vpsfree-cz-configuration --as-is` (returned nonzero after successful
  checkout because the ambient post-checkout Overcommit hook lacked gems)
- `nix develop -c confctl inputs channel update --commit vpsadmin`
  (first attempt generated the lock update but the commit hook rejected a
  stale Overcommit signature)
- `nix develop -c overcommit --sign` and `nix develop -c overcommit --run`
  (configuration repository)
- restored only the generated `flake.lock` retry input, then reran
  `nix develop -c confctl inputs channel update --commit vpsadmin`
- `nix flake check --no-build` and `nix flake check` in the configuration
  feature worktree
- pushed the configuration feature branch, created a fresh target worktree,
  fast-forwarded `master`, reran `nix flake check`, and pushed `master`
- reset only the disposable capture slug after the mixed-state diagnosis,
  started it cleanly with local networking, and verified the NAS seed and its
  initial transactions
- regenerated `datasets/vps-dataset-list`, `vps-details/datasets`, and
  `networking/routed-addresses` in Czech and English
- `nix develop -c bin/validate --update`, `nix develop -c bin/validate`, and
  `nix develop -c bin/check` (capture repository)
- visually inspected all six selected bilingual PNGs
- stopped the capture cluster
- committed capture contract pin `baa1416` and pushed the capture feature
  branch
- `bin/kb-contract-fetch --output
  work/2026-08-03-webui-dataset-used-czech-fix/kb-sources`
- built a zero-replacement all-page candidate set and validated it with
  `tools/check-kb-annotations.rb`

## Results

- The current session slug and `VPSFREE_DEV_SESSION_SLUG` both equal
  `2026-08-03-webui-dataset-used-czech-fix`; this initiative is safe to use.
- Workspace contains unrelated concurrent changes; they will be preserved.
- Canonical vpsAdmin remote already uses the required SSH URL.
- `usedSpaceWithCompression()` embedded a trailing separator in the gettext
  msgid `uncompressed, ratio `. English used the source's trailing space, but
  Czech translated it as `nekomprimovaný, poměr` without one, producing
  `poměr1,3×`.
- Both `used` and `referenced` fields call this formatter; the ratio-first
  formatter uses a separate `uncompressed` message and had correct spacing.
- A catalog-wide audit found the same fragile leading/trailing-space pattern in
  DNS, monitoring, networking, OOM reports, VPS routes, context switching,
  password notifications, VPS creation, cgroup hints, mount removal, pool scan
  status, and authorization errors. Confirmed missing separators were possible
  at those call sites, so separators are now structural in PHP.
- The route-via default also passed a runtime-concatenated string to gettext,
  preventing the static catalog translation from matching; it is now split.
- No single-line source gettext message retains leading or trailing whitespace.
- Focused PHPUnit result: 9 tests, 31 assertions, all passing.
- Full WebUI PHPUnit result: 82 tests, 335 assertions, all passing.
- Locale update health passed with only the two existing xgettext warnings
  about embedded URLs in unrelated messages.
- All declared pre-commit hooks passed: MigrationSpecs, VpsadminApiI18n,
  VpsadminWebuiI18n, Nixfmt, PhpCsFixer, and RuboCop.
- vpsAdmin commit: `2f9546ce8` (`webui: make translated spacing explicit`).
- Mandatory standalone review result: no Blocking, Important, or Advisory
  findings. Residual gaps are browser coverage for secondary audited call sites
  and the pending KB documentation contract. The reviewer independently passed
  `git diff --check`, locale health, and the randomized focused PHPUnit test
  (9 tests, 31 assertions).
- vpsAdmin feature branch pushed to the SSH origin at `2f9546ce8`.
- A fresh target worktree fast-forwarded vpsAdmin `master` from `ae5dd5e01` to
  `2f9546ce8`. The focused target-branch test passed again (9 tests, 31
  assertions), the worktree was clean, and `master` was pushed over SSH.
- The capture repository inventories dataset screenshot concepts, including
  `datasets/vps-dataset-list` and `vps-details/datasets`; documentation impact
  must be decided by its pinned contract/capture checks.
- The capture remote's `origin/HEAD` incorrectly points to the old
  `2026-07-10-kb-czech-fixes` branch. Its new initiative branch was clean and
  the old tip was an ancestor of `origin/master`, so it was safely
  fast-forwarded before edits.
- The capture contract now pins exact vpsAdmin commit `2f9546ce8` in
  `flake.nix`, `flake.lock`, `captures.json`, and `contract/navigation.yml`.
  Updating the input also mechanically advanced the transitive vpsAdminOS and
  nixpkgs locks carried by that vpsAdmin revision.
- `bin/check` passes: contract validation covers 39 controls, 29 paths, 32
  capture concepts, and 3 selectors; annotation validation covers 65 bindings
  and 9 exceptions; tests pass with 8 runs/50 assertions and 7 runs/17
  assertions; the inventory has 59 concepts and 118 bilingual PNG variants.
- The first capture did not reach this initiative's cluster. Its isolated
  services database contained the expected production fixtures (`Praha`,
  `Brno`, and the other configured locations), while the browser showed
  `test-location` from a concurrent cluster at the fixed WebUI hostname.
  Bridge-mode browser proxying resolves that hostname instead of using the
  custom services address (`172.16.106.70`). Because bridge capture access is
  therefore unavailable without changing capture infrastructure, this
  disposable screenshot cluster is being restarted with local networking;
  the fixed local forwarding ports were checked free first.
- Reusing the bridge cluster's VM state across the first local restart caused
  the clean services database and persistent backuper filesystem to diverge.
  NAS creation transaction `#1` rolled back because
  `/tank/ct/nas/private` already existed, so the browser correctly waited for
  a NAS row which could never appear. The failed capture was interrupted and
  only the disposable `...-captures` slug was reset before a clean local
  restart.
- The configuration worktree helper hit the already-documented ambient
  Overcommit gem failure after checkout. The requested branch and worktree
  were nevertheless created successfully at current `origin/master`; its
  shared Overcommit hooks are installed, and commit work is running inside
  the repository's Nix shell.
- The first `confctl --commit` attempt correctly refused the stale Overcommit
  configuration signature. After reviewing the generated one-file lock diff,
  the current `.overcommit.yml` was signed in the Nix shell and both declared
  hooks passed. The generated update was then retried from the original lock
  so `confctl` created its own unmodified commit message.
- Configuration commit `a481a740` updates only `vpsadminServices` from
  `19e613c2` to `2f9546ce`; both the feature branch and fast-forwarded
  `master` were pushed over SSH. `nix flake check` passes from the target
  worktree. This dependency-only generated update required no additional
  mandatory change review.
- The clean capture seed created the `nas` dataset successfully and both
  initial transactions completed successfully before captures began.
- All six selected Czech/English captures completed and were visually sound.
  A first Czech dataset bitmap caught an in-flight fixture value, but the
  required deterministic recapture returned to the committed SHA-256. The
  final six PNGs are all byte-identical to the repository, so no media update
  remains.
- Final capture checks pass with the same contract/test/inventory counts as
  above. Capture commit `baa1416` changes only the exact vpsAdmin revision in
  `flake.nix`, `flake.lock`, `captures.json`, and
  `contract/navigation.yml`; the mechanical contract pin was pushed on the
  feature branch and does not require another change review.
- The production KB fetch contains 116 Czech and 70 English pages. No page
  contains the affected WebUI wording, and no selected screenshot changed.
  The immutable zero-replacement candidate build validates all 65 bindings
  and 9 exceptions and reports 0 changed pages, 0 annotations, 0 media
  objects, and 0 content replacements. Consequently there is no release
  manifest or DokuWiki write to stage; production and global KB staging were
  left untouched.
- vpsAdmin push workflows for `2f9546ce8`: WebUI PHPUnit and i18n health are
  green; the selected CI integration run is still in progress.

## Open questions

- None. Waiting only for the already-running vpsAdmin master CI integration
  workflow to finish.

## Cleanup

- Removed the vpsAdmin feature and temporary `master` worktrees after the
  successful push; retained both local and remote feature branches.
- Removed the vpsfree-cz-configuration feature and temporary `master`
  worktrees after the successful push; retained both local and remote feature
  branches.
- Stopped and reset only the disposable capture cluster, removing its VM state
  and GC root.
- Retained the clean `vpsadmin-kb-captures` feature worktree and pushed branch
  because its exact contract pin is the review artifact for the KB workflow.
