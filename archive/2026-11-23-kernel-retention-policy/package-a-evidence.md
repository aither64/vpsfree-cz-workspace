# A: kernel catalog and candidate validation

## Delivery

The original A commit below was replaced by `a1ce827b87c310254870a0537397fb07f891e63e` in the history-only dependency move. See the last section for the mapping and proof.

- Worktree `worktrees/2026-11-23-kernel-retention-policy/vpsadminos`, attached branch `2026-11-23-kernel-retention-policy`.
- One commit `726de81563317ac2e6e7b67b09e07a35d20d783d` on `b86287c105b749827cd63632ac35936533910f63`, `os: record and validate kernel catalog entry dates`. No DB/schema/API migrations or compatibility changes to deployed state. The nine introduction dates are a one-time **source catalog** backfill. No superseded intermediate A commits or unpublished migrations. No push, administrator settings, production or fleet request, integration, or local kernel compilation.
- The 15 scoped paths cover the catalog facade and nine records, the offline tool and fixtures, `.overcommit.yml`, `.github/workflows/kernel-entry-check.yml` and `docs/os/kernel-updates.md`. The established `{ lib }` catalog API and both selector names remain. D owns serialized catalog output/retention and has the exit-status-only checker interface. C owns the subsequent `.110` patch path update when it moves the patch; A left the source file at its original path.
- Documentation inventory: registration, holds and the staged check are maintainer guidance in `docs/os/kernel-updates.md`; its staging-admission section is repository administrator guidance. The concrete rollout remains pending. Keep the checker and workflow under trusted review; Actions required-check settings are not part of these changes.

## Backfill provenance

The clone is not shallow. Followed the rename from `os/packages/linux/availableKernels.nix` (`77527f4c895dfb8c7f0bd218dfc79799d6fa285b`), checked the older `kernels` bindings and current shape, and searched only ancestry of `b86287c105b7`, including per-parent merge diffs. The structural added bindings, not selector edits, tag dates, later repins or abandoned branches, supplied these commits. Each shown introduction has one parent; none of the nine appeared earlier or was removed and restored on that ancestry. Both `6.18.44` and `6.18.49` enter in the same commit.

| Key | Introducing OS commit | Committer `%ct` | UTC `dateAdded` |
| --- | --- | ---: | --- |
| 6.12.48 | `71ae15a1444516a45a6ef13fed366075daf47cd3` | 1758399094 | 2025-09-20 |
| 6.12.95 | `849282e6be436743a47fb0e592041e6fba9ad41f` | 1783331081 | 2026-07-06 |
| 6.12.109 | `69299d992725fd5f39968280fb80aee103f7d38e` | 1788890553 | 2026-09-08 |
| 6.12.110 | `4c8cbf296d16f4b25aba50789b1d3337dece3a08` | 1791852655 | 2026-10-13 |
| 6.12.113 | `eb5c39c0789401117c48cd124e47b7a401fb91b6` | 1792261993 | 2026-10-17 |
| 6.12.117 | `eedc1254d309cac861cb0f7af080ee8de8296506` | 1794479564 | 2026-11-12 |
| 6.12.118 | `f33f5fd10b53232b5670862f832f4ec5ea835e84` | 1794945586 | 2026-11-17 |
| 6.18.44 | `b1f9e8e5c35c7a56b0345395df276a01afe074a1` | 1791790430 | 2026-10-12 |
| 6.18.49 | `b1f9e8e5c35c7a56b0345395df276a01afe074a1` | 1791790430 | 2026-10-12 |

```sh
git log -M --follow --format='%h %s' "$base" -- os/packages/linux/available-kernels.nix
git log --full-history --diff-merges=separate --format='%H %ct %P %s' \
  -G '"(6[.]18[.](44|49)|6[.]12[.](48|95|109|110|113|117|118))"[[:space:]]*=' \
  "$base" -- os/packages/linux/available-kernels.nix os/packages/linux/availableKernels.nix
date -u -d '@1791790430' +%F
```

## Checks and limits

- `python3 tools/test-kernel-entry-check.py` (7 groups, 13.4 s): good/docs-only and invalid candidate trees, a missing tree and Nix evaluation failure, missing/malformed/future metadata, leap day, month/30th/31st date handling, hold and typo, selector and date immutability, stale working contents vs staged companion file, companion rename/repin and retirement/restoration, and regular-file-only version discovery. Retention eligibility and its 30-day threshold remain D's pure-policy behavior, not decisions by this checker.
- `python3 tools/kernel-entry-check.py check --as-of 2026-11-23 --base "$base" --tree "$head"` and `--base "$head" --tree "$head"` validate the exact A commit in both backfill and normal modes. `git diff --check "$base..$head"`, `nixfmt --check -- os/packages/linux/available-kernels.nix os/packages/linux/catalog/*.nix`, and standalone workflow YAML and job shape checks passed.
- `git archive "$base"` into a disposable directory, `nix eval --json --offline --no-update-lock-file --option allow-import-from-derivation false --impure --expr ...`, overlay only the A catalog facade and records, repeat. Compared the evaluated full nine `f.lib.availableKernels` tuples (remove dates/normalize copied source-root prefix), plus actual `f.lib.vpsadminosSystem` QEMU config for each `system.vpsadminos.enableUnstable` and `boot.zfsBuiltin` combination: selectors stable `6.12.118`, unstable `6.18.49`; Linux source and derivation, ZFS user derivation and built-in/external ZFS module derivations unchanged. Larger all-explicit-config evaluation exceeded its quick 22 s bound; complete tuple comparison and four actual selector/default derivation comparisons passed. No build was requested.
- Official upstream release/tag queries verified `actions/checkout` v7.0.1 (`3d3c42e5aac5ba805825da76410c181273ba90b1`, Node 24) and `cachix/install-nix-action` v32.1.0 (`382a9ed9481c7c1f94f68b72ef105b3417c73877`, composite). The workflow uses those exact SHA pins, a GitHub-hosted runner, `contents: read`, no persisted checkout credentials and no repository mutations. No merge queue enabled by YAML. Actual fork/retarget/docs-only executions, exact-SHA dispatch and repository rules still need later authorized test-target evidence before administrator enforcement.

## Hook setup and evidence

- Existing shared hook executables matched installed Overcommit 0.71.0. This version uses explicit `git config --local` for trust, which maps to the common bare config in linked worktrees. Overcommit's newer Git worktree config support still requires enabling the common `extensions.worktreeConfig` setting; command-local override was rejected with multiple worktrees. No common settings were changed. `nix develop --offline` could not realize `nixfmt-tree` because `remarshal` v1.3.0's fetched source returned HTTP 404. Focused checks used existing Nix store Git 2.54, Ruby 3.4.9, Python 3.13.18, Nixfmt 1.5, Nix 2.34.9 and installed Overcommit 0.71.0.
- Source the worktree-specific environment from its root before a commit: `source "$(/nix/store/1k2lblqlj39azh6wn1sffa2869vrg3mr-git-2.54.0/bin/git rev-parse --absolute-git-dir)/kernel-retention-hooks/env"`. It locates actual Git and tooling, re-routes just Overcommit signature `git config --local` requests (including from hooks via `GIT_EXEC_PATH`) for this git-dir to its own `trust.config`. Hooks and signature checks remain active. The actual Git `commit` runs normal hooks. Do not source it for unrelated repositories or install/re-sign shared hooks; if config changes here, verify it and run `overcommit --sign` and `overcommit --sign pre-commit` with the isolated environment, checking common config remains unchanged.
- Note `.overcommit.yml` previously enabled `Nixfmt` by name without a command; installed/upstream Overcommit does not ship that hook. An explicit staged Nixfmt command now keeps the check active alongside unchanged RuboCop. Python 3 is needed by the metadata hook; D's clean writer needs to install or provide it alongside Git and Nix.
- In a discarded linked-worktree fixture, real `git commit -F` refused an invalid staged record with valid unstaged content, refused an unsigned changed hook config, and accepted valid docs-only changes. Common config and hook file checksums before/after matched. The valid hook environment advanced its branch via a disposable hydrated `GIT_WORK_TREE` with the same Git dir and index and preserved the original worktree's unstaged sibling edit.
- Used that clean hydration technique for A so Overcommit would not stash/reset the concurrent unstaged work: stage only package paths, use explicit original `GIT_DIR`/`GIT_INDEX_FILE`, run `git checkout-index --all --ignore-skip-worktree-bits` into a fresh `GIT_WORK_TREE`, require `git diff --quiet`, then `git commit -F`. Actual Nixfmt and KernelEntryCorrectness passed; commit-msg passed with advisory TextWidth because two body lines exceed the hook's 72-column advisory (all are within repo limit of 80). The index was empty after the commit; common config checksum unchanged. Disposable fixture/snapshot directories removed; retained worktree-local hook adapter needed for B–D and follow-up windows.

## Review follow-up: Python dependency belongs with the first hook

With the lead's exclusive window and D's clean tip `79efa90fd96f636543e9abfd4f5220ded5d2c6bd`, moved the existing `python3` dependency in `vpsadminosShell` from C to A. Replayed the four snapshots with standard `git commit -F` and real signed Overcommit hooks in a disposable standalone repo. `git range-diff` showed the single addition in A, its removal from C's patch, and identical B/D patches. A/B snapshot changes each amount to this one flake line; C/D snapshots are byte-identical. Authors, committers, dates, messages and the linear series were preserved.

| Package | Before | After |
| --- | --- | --- |
| A | `726de81563317ac2e6e7b67b09e07a35d20d783d` | `a1ce827b87c310254870a0537397fb07f891e63e` |
| B | `6a5c0cf49b8af3e1ce394d615aec9716e198f352` | `90d6bf104674a1c46ec278eebd3583a5197db574` |
| C | `feac129e2570bbd4df55c364eb24d63be3aa711f` | `be966218cb3bcafe05592a5ad32fcf53dffb6b16` |
| D | `79efa90fd96f636543e9abfd4f5220ded5d2c6bd` | `85a66f3637da08dc63eb443098fd95e37b248590` |

Both tips have tree `97a119f1baf93bec21b61cadbe3013c802db5d87`. Exact `git diff --exit-code <old-tip> <new-tip>` was empty; base-to-tip `git diff --check` passed. Actual Nixfmt, KernelEntryCorrectness, RuboCop where applicable, and commit-msg hooks passed (existing advisory widths in A/C unchanged). Exact first A passed the offline CLI against `b86287c1`; `nix eval --offline path:...#devShells.x86_64-linux.default.nativeBuildInputs --apply 'xs: map (x: x.name) xs'` showed `python3-3.13.18` directly. This is shell evaluation, not a claim that the complete development shell was realized.

Imported only the rebuilt objects and updated the owned branch with expected-old-SHA compare-and-swap. No other ref moved, common hook/config checksums matched, and the original index and worktree remained clean. No push, kernel build, DB migration or deployment action. Ignored supporting script and transcript: `package-a-history-rebuild.sh` and `package-a-history-rebuild.log`.

## Superseded follow-up: a fast path for unrelated PRs

The user later chose advisory, event-level path filtering instead. The runtime fast path below is not part of the final branch; see the replacement evidence.

Commit `aa0c5a04bebaf47981e73dade74cfab246161dce` on `a435f844d017da0b418a470f20fc695c6c0eadd0` (tree `de1dbefd23fa7e80be1c0ad2266982ead9e85581`). Four paths: `.github/workflows/kernel-entry-check.yml`, its `scripts/kernel-entry-check-scope.sh` helper, `tools/test-kernel-entry-check-scope.py`, and `docs/os/kernel-updates.md`. No migrations, action pin changes, or settings changes.

The required job still runs on every PR to `staging`. Before either Nix step, the scope helper verifies the candidate SHA and its first parent against the event, then compares only the declared checker inputs in those exact trees. Only a successful empty input diff sets `skip=1`. Both Nix steps use the same guard; diff errors fail the job, and dispatch always runs the full check against the current `staging` base. The guide tells maintainers to update the declared input set for new out-of-scope imports or patches.

`python3 tools/test-kernel-entry-check-scope.py`: six groups passed (4.4 s), with Git but no Nix available on the scope subprocess PATH. Covered docs-only and no-op candidates, every declared input, deletions, directory-to-file replacement, renames into/out of scope, wrong SHA/base, abnormal diff status, and dispatch with a local `staging` ref (including missing-ref failure). Existing seven metadata fixture groups passed (11.3 s). `bash -n`, YAML assertions for unconditional named job, permissions, checkout credentials, and identical Nix guards, plus `git diff --check` passed. Real commit hooks passed, including KernelEntryCorrectness and commit-msg. Index/worktree clean and common hook bytes unchanged. Rebase parity, independent review, and live GitHub-hosted evidence remain for the lead. No push, build or production operation.

## Replacement: advisory PR workflow with event-level paths

Amended only `aa0c5a04` to `418b83ee46cebad8c630c502f389a56064d8034e` (tree `80b460212b96991ea43fbe7b9aaa1daf8fa278d2`, parent `a435f844d017da0b418a470f20fc695c6c0eadd0`). The tip was subsequently amended to remove one path as described below. The net change is confined to `.github/workflows/kernel-entry-check.yml` and `docs/os/kernel-updates.md`. The runtime scope helper and its test are no longer present. A–D, action pins and the lockfile are unchanged; no new/repeated inputs or migrations.

Added ten `pull_request.paths` entries for the declared inputs, including the two exact directory names as well as their recursive patterns for file replacements. A parsed YAML comparison matched every other part of the workflow to `a435f844d`. That includes the stable job name, checkout permissions/credentials, candidate and PR first-parent checks, runtime steps without skips, and full `workflow_dispatch` validation. The guide describes applicable PR checks as advisory and the weekly writer’s exact-SHA dispatch gate separately. Repository reference search found no other general enforcement instructions.

All seven offline checker fixture groups passed (11.1 s), along with the YAML and extracted Bash syntax assertions, `git diff --check`, and real KernelEntryCorrectness and commit-message hooks. The index and worktree are clean. Common hook/config checksums are unchanged. No push, rebase, settings change, hosted run, build or production operation.

### Exclude the ZFS patch from the PR filter

At the user's direction, amended the same tip to `f78c00294416547fd40d92caedf1246b76595713` (tree `f575c8afc9776d22439ec5a5151cc780ac3c3a30`). The parent and commit message are unchanged. The sole old-to-new source difference is deletion of the `os/packages/zfs/zfs235-free-account.patch` filter in `.github/workflows/kernel-entry-check.yml`; the original patch blob and its catalog use are unchanged. Parsed YAML matched after removing just that path, with nine PR paths, the same named job and full dispatch. The extracted Bash syntax, diff whitespace/commit width, and actual KernelEntryCorrectness and commit-message hooks passed. The index and worktree were clean, and common hook/config checksums matched. No migration, new input, push, rebase or settings change.
