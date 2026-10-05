---
lifecycle: active
---
# 2026-07-20-binary-cache-kernels

## Repositories

- `repos/vpsfree-cz-configuration.git` at fetched `origin/master`
  `fa8de8a8`; temporary detached worktree
  `worktrees/2026-07-20-binary-cache-kernels/vpsfree-cz-configuration`
- `repos/vpsadminos.git` at fetched `origin/staging` `702155fb`; temporary
  detached worktrees
  `worktrees/2026-07-20-binary-cache-kernels/vpsadminos` and
  `worktrees/2026-07-20-binary-cache-kernels/vpsadminos-37d87632`

## Status

Investigation complete. No deployment, cache, GitHub, or project repository
content was changed.

## Commands run

- Verified the active session with `bin/dev-session current` and
  `VPSFREE_DEV_SESSION_SLUG`.
- Fetched both affected canonical bare repositories over SSH.
- Inspected the cited vpsAdminOS commit, current remote refs, workflow paths,
  configuration cache references, and backuper2 references.
- Inspected GitHub Actions run and job metadata and downloaded the relevant
  kernel/default CI logs with `gh run list` and `gh run view`.
- Evaluated the `6.12.48` and `6.12.95` vpsAdminOS CI toplevel derivations at
  revisions `37d87632` and `702155fb` without building them.
- Queried derivation outputs and `cache.vpsadminos.org` narinfo records.
- Ran `nix build --dry-run` for the current `6.12.48` CI toplevel.
- Used a temporary `PWD` containing only a generated `kernels.json` entry for
  backuper2 while attempting the configuration evaluation. Full node
  evaluation stopped at unavailable deployment-only initrd host keys, so the
  supplied derivation list and the equivalent vpsAdminOS CI derivation were
  used for the remaining derivation analysis.

## Results

- Backuper2 uses the `production` channel, currently pinned by configuration
  commit `92bb5f67` to vpsAdminOS `702155fb`. Its generated runtime-kernel
  inventory selected the running kernel `6.12.48`; the default/boot kernel is
  `6.12.95`.
- The cited commit `680f26f9` is the cause of the newly required build chain,
  but it did not change any of the three kernel/ZFS derivation hashes. The
  exact `z2f05...`, `q9w0h...`, and `p17g8...` derivations are identical when
  evaluated at the pre-merge revision `37d87632` and at `702155fb`.
- `680f26f9` added `kernelConfig = toString kernel.configfile` to
  `etc/vpsadminos/security-evidence.json`. The retained Nix string context
  makes the final built-in-ZFS kernel config an output dependency of the
  evidence file and therefore of the system closure.
- The `6.12.48` dependency chain is:
  `security-evidence.json` -> final config `p17g8...` -> ZFS built-in
  `q9w0h...` -> auxiliary kernel development output `z2f05...`. The final
  deployed built-in-ZFS kernel is built by `dkyp5...`, whose output
  `/nix/store/9zx2...-linux-6.12.48` is already cached. Nix nevertheless has
  to realize the auxiliary/build-time chain before it can produce the newly
  referenced config output.
- Direct cache checks found:
  - cached: final `6.12.48` kernel outputs `9zx2...` and `0y5n...`;
  - missing: auxiliary `6.12.48` kernel outputs `qjq...` and `czvh...`, ZFS
    built-in output `2zx3...`, and final config output `0hin...`;
  - cached: the corresponding final config for default `6.12.95`,
    `/nix/store/689v...-linux-config-6.12.95`.
- The daily kernel workflow run
  <https://github.com/vpsfreecz/vpsadminos/actions/runs/29721522938> started at
  `2026-07-20T06:22:59Z`, succeeded for all versions including `6.12.48`, and
  evaluated staging revision `37d87632`. Its `6.12.48` closure references only
  the already-cached final kernel/configuration shape that existed before the
  evidence commit; its narinfo references the final kernel `9zx2...` but not
  `0hin...`.
- Commit `680f26f9` was committed onto staging at
  `2026-07-20T08:19:43Z`, almost two hours after that daily run started. It did
  not trigger `kernels.yml`, because the workflow's push filter only includes
  `.github/workflows/kernels.yml` and `os/packages/linux/**`, while this commit
  changed `os/modules/misc/version.nix`.
- The normal CI workflow did run after the merge and populated the default
  `6.12.95` closure, explaining why that kernel/config did not need a local
  build. Normal CI builds only the default kernel; it does not warm retained
  old kernel versions.
- Evaluating the current `702155fb` `6.12.48` kernel CI toplevel with
  `nix build --dry-run` requests the same `z2f05...`, `q9w0h...`, and
  `p17g8...` derivations seen in the backuper2 deployment. Therefore the next
  scheduled all-kernel run at the current staging revision should warm the
  missing config chain and make the backuper2 deployment substitutable.
- The immediate gap is a cache-warming race, not a cache connectivity, trust,
  signature, retention, or failed-matrix-job problem.

## Open questions

- Operational choice: wait for the next scheduled all-kernel run, build and
  publish the exact closure manually, or first add a safe manual-dispatch/cache
  warming mechanism.
- Follow-up design choice: retain the `kernel.configfile` string context so
  the config is guaranteed to exist in the booted closure, or discard the
  context if the evidence contract only needs the immutable store-path
  identity. This requires an intentional vpsAdminOS change and review.
- Follow-up reliability improvement: add `workflow_dispatch` to
  `kernels.yml`, and consider requiring target-revision cache warming before
  promoting a vpsAdminOS production pin that changes kernel closure
  dependencies.

## Cleanup

- The configuration worktree post-checkout hook reported missing ambient Ruby
  gems after Git had successfully created it. This known behavior is already
  documented in
  `notes/vpsfree-cz-configuration/2026-06-04-overcommit-dev-shell.md` and
  `notes/cross-project/2026-06-07-overcommit-worktree-add.md`.
- All temporary worktrees were clean before cleanup.
- Removed all three temporary project worktrees and the diagnostic temporary
  directory. Bare repositories and refs were retained.
