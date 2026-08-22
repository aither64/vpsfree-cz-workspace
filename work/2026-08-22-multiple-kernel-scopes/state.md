# 2026-08-22-multiple-kernel-scopes

## Repositories

- `vpsadminos`
  - branch: `2026-08-22-multiple-kernel-scopes`
  - worktree: `worktrees/2026-08-22-multiple-kernel-scopes/vpsadminos`
  - base: `origin/staging` at `4ebcaab16`
- `vpsfree-cz-configuration`
  - branch: `2026-08-22-multiple-kernel-scopes`
  - worktree:
    `worktrees/2026-08-22-multiple-kernel-scopes/vpsfree-cz-configuration`
  - base: `origin/master` at `d5a7df8e`

## Status

- Implementation, mandatory review follow-up, local integration tests, feature
  push, and feature-head GitHub Actions validation are complete.
- Scope decision: add the multi-range mechanism without adding 6.18 ranges.
- vpsAdminOS was fast-forwarded to `staging` at `3bf14ec67`.
- The `staging`, `os-staging`, and `production` configuration channels were
  pinned to that exact revision in generated commit `3bd35c6c`, which was
  fast-forwarded to configuration `master`.
- Default-branch integration, downstream pinning, validation, CI, and worktree
  cleanup are complete.
- The configuration repository has no push-triggered workflow for this commit.

## Commands run

- `bin/dev-session current`
- `bin/dev-session worktree add 2026-08-22-multiple-kernel-scopes vpsadminos --as-is --branch 2026-08-22-multiple-kernel-scopes --base origin/staging`
- Inspected the eBPF registry, service module, tests, monitoring collector,
  compiled livepatch filters, incoming 6.18 branch, and pinned Nixpkgs version
  helpers.
- `nix develop --command nixfmt os/livepatches/ebpf/available.nix os/modules/services/ebpf-livepatch/default.nix tests/suite/ebpf-livepatch.nix`
- `./test-runner.sh test ebpf-livepatch`
- `nix develop --command overcommit --run`
- `git commit -F work/2026-08-22-multiple-kernel-scopes/vpsadminos-commit-message.txt`
  (failed because the ambient shell did not provide `nixfmt` to the active
  Overcommit hook)
- `nix develop --command git commit -F work/2026-08-22-multiple-kernel-scopes/vpsadminos-commit-message.txt`
- `git fetch origin`
- `./test-runner.sh test ebpf-livepatch` after the review fixes (first attempt
  failed during Nix evaluation because the synthetic registry override was
  declared as an optional module argument)
- `./test-runner.sh test ebpf-livepatch` after wrapping the module import for
  the test-only registry override
- `nix develop --command overcommit --run` after the review fixes
- `nix develop --command git commit --amend -F work/2026-08-22-multiple-kernel-scopes/vpsadminos-commit-message.txt`
- `./test-runner.sh test ebpf-livepatch-lifecycle`
- `./test-runner.sh test prometheus/exporters` (matched zero scripts; not
  counted as validation)
- `./test-runner.sh ls | rg -i 'prometheus|exporter|ebpf'`
- `./test-runner.sh test 'prometheus/exporters#ebpf'`
- `nix develop --command git push -u origin 2026-08-22-multiple-kernel-scopes`
- `gh run view 32566122706 --repo vpsfreecz/vpsadminos --log-failed`
- `gh run rerun 32566122706 --repo vpsfreecz/vpsadminos --failed`
- `gh run view 32566122706 --repo vpsfreecz/vpsadminos --attempt 2 --log-failed`
- `gh run list --repo vpsfreecz/vpsadminos --branch staging --workflow CI ...`
- `gh run rerun 32566122706 --repo vpsfreecz/vpsadminos --failed` after a
  four-minute backoff
- Monitored GitHub Actions run `32566122706` through completion.
- Created a fresh detached vpsAdminOS target worktree from `origin/staging`,
  fast-forwarded it to `3bf14ec67`, and reran
  `./test-runner.sh test ebpf-livepatch`.
- `git push origin HEAD:staging`
- Removed the temporary vpsAdminOS target worktree.
- `bin/dev-session worktree add 2026-08-22-multiple-kernel-scopes
  vpsfree-cz-configuration --as-is --branch
  2026-08-22-multiple-kernel-scopes --base origin/master`
- `nix develop --command bundle exec overcommit --install`
- `nix develop --command confctl inputs channel set --commit
  staging,os-staging,production vpsadminos
  3bf14ec679229ab6c19387593e3a34db2da20220`
- `nix develop --command confctl inputs channel ls
  staging,os-staging,production`
- `nix flake check --no-build --no-update-lock-file`
- `nix develop --command confctl build -y --max-jobs=0
  cz.vpsfree/nodes/stg/node1`
- `nix develop --command confctl build -y --max-jobs=0
  cz.vpsfree/nodes/prg/node25`
- `nix develop --command confctl build -y --max-jobs=0
  cz.vpsfree/containers/int.vpsfbot`
- `nix develop --command confctl build -y
  cz.vpsfree/containers/int.vpsfbot`
- Pushed configuration feature branch
  `2026-08-22-multiple-kernel-scopes`.
- Created a fresh detached configuration target worktree from `origin/master`,
  fast-forwarded it to `3bd35c6c`, reran the no-build flake check, and pushed
  `HEAD:master`.
- Removed the temporary configuration target worktree.
- Monitored vpsAdminOS default-branch CI run `32573492517` through completion.
- Removed the retained vpsAdminOS and configuration feature worktrees after
  verifying that their local and remote feature refs matched.

## Results

- The existing eBPF registry supports one half-open kernel range per program.
- Compiled kernel livepatches already use arbitrary filter functions and need
  no structural change.
- Other kernel predicates are feature thresholds rather than backport windows.
- The eBPF monitor JSON and Prometheus labels can remain unchanged by emitting
  only the range that matched the configured kernel.
- `ebpf-livepatch` passed all 35 examples, including synthetic disjoint ranges,
  invalid range definitions, boundary behavior, module errors, and monitoring
  metadata.
- All Overcommit pre-commit hooks passed: Nixfmt and RuboCop.
- The first commit attempt did not create a commit. The hook ran as expected,
  but its Nixfmt check could not find `nixfmt` outside the repository's
  development shell. The commit was retried through `nix develop` without
  bypassing hooks.
- Commit `3c24acd5e16d53891477be5ce20530dc4fdbba91` contains the focused
  vpsAdminOS change. Its Nixfmt pre-commit hook passed; commit-message checks
  passed with non-fatal 72-column warnings while all lines remain within the
  workspace's required 80-column limit.
- `origin/staging` remains at the recorded base after the pre-review fetch, so
  no rebase is required.
- The mandatory standalone review found that invalid ranges on an enabled
  registry entry could disappear from the default selection before module
  assertions checked them, and that unknown range attributes or arbitrary
  non-empty version strings were accepted. It also advised testing monitoring
  metadata through a synthetic second-range module evaluation. All findings
  are addressed in the amended focused commit.
- The first post-review test rerun failed before examples ran because the Nix
  module evaluator tried to resolve the optional test argument through
  `_module.args`. The test now calls the production module through a wrapper
  import that supplies the override directly; the production module interface
  is unchanged.
- The corrected focused suite passed all 37 examples, including registry-wide
  fail-closed validation and second-range monitoring metadata.
- All post-review Overcommit hooks passed: Nixfmt and RuboCop.
- Amended commit `3bf14ec679229ab6c19387593e3a34db2da20220` contains the
  complete reviewed change. The commit's Nixfmt hook passed, and no hooks were
  bypassed.
- `ebpf-livepatch-lifecycle` passed all 3 VM examples. The vpsAdminOS system
  closure was built locally, but kernel 6.12.95 was substituted from the cache
  and was not built locally.
- The broad `prometheus/exporters` selector matched zero scripts. Listing the
  evaluated catalog identified `prometheus/exporters#ebpf` as the exact target.
- `prometheus/exporters#ebpf` passed both VM examples. Its system and exporter
  closure was built locally, but the kernel was not built locally.
- Pushed commit `3bf14ec679229ab6c19387593e3a34db2da20220` to
  `origin/2026-08-22-multiple-kernel-scopes`.
- GitHub Actions run `32566122706` failed in `Build toplevel closure` because
  GitHub returned HTTP 429 for all four attempts to download the existing Linux
  source archive at revision `a2384967b90f24d2470c9eb15f0e66d938df7e08`.
  This is an upstream rate-limit failure unrelated to the eBPF registry diff;
  downstream build and test jobs were skipped. A failed-job rerun is warranted
  now that the cause is established.
- Attempt 2 failed for the identical reason: four HTTP 429 responses for the
  same archive. The current `staging` head passed CI earlier on 2026-08-22, so
  the pinned source and base branch are known-good. Further retries should be
  spaced out to avoid extending the rate-limit condition.
- Attempt 3 cleared the rate limit and passed at the exact pushed head
  `3bf14ec679229ab6c19387593e3a34db2da20220`:
  - `Build OS and populate binary cache`: passed.
  - `Run test suite`: passed.
  - `Livepatch lifecycle (intel)`: passed.
  - `Livepatch lifecycle (amd)`: passed.
  - Run: https://github.com/vpsfreecz/vpsadminos/actions/runs/32566122706
- The vpsAdminOS target worktree was a clean direct fast-forward from
  `4ebcaab16` to `3bf14ec67`; its focused registry suite passed all 37 examples
  again before the default-branch push.
- `confctl` generated configuration commit
  `3bd35c6ca62f7e9a9c77d3f21b1c146d49f6b036` with all three inputs set to
  `3bf14ec679229ab6c19387593e3a34db2da20220` and the same resolved NAR hash.
  Its Nixfmt pre-commit hook passed, and no hook was bypassed.
- `confctl inputs channel ls` confirmed the `vpsadminos` role in `staging`,
  `os-staging`, and `production` resolves to `3bf14ec6`.
- `nix flake check --no-build --no-update-lock-file` passed in both the feature
  and fresh target worktrees.
- Staging `node1` and production `node25` evaluated to vpsAdminOS
  `26.05.git.3bf14ec`; both stopped only because the intentionally external
  `/secrets/nodes/initrd/ssh_host_ed25519_key` is unavailable locally. With
  `max-jobs=0`, neither attempted a local build.
- The dry build of managed `os-staging` consumer
  `cz.vpsfree/containers/int.vpsfbot` requested only five configuration and
  activation derivations, with no Linux or ZFS derivation. Building those five
  derivations normally succeeded.
- vpsAdminOS default-branch CI run `32573492517` passed at the exact merged
  head `3bf14ec679229ab6c19387593e3a34db2da20220`:
  - `Build OS and populate binary cache`: passed.
  - `Run test suite`: passed.
  - `Livepatch lifecycle (intel)`: passed.
  - `Livepatch lifecycle (amd)`: passed.
  - Run: https://github.com/vpsfreecz/vpsadminos/actions/runs/32573492517
- `vpsfree-cz-configuration` has no push-triggered workflow for the merged
  configuration head.
- The downstream change is a generated dependency-only lock update, so it did
  not require a second mandatory review after the reviewed vpsAdminOS code was
  integrated.

## Open questions

- None.

## Cleanup

- Keep both feature branches locally and remotely after integration.
- Temporary target and retained feature worktrees have been removed. The local
  and remote feature branches remain at `3bf14ec67` for vpsAdminOS and
  `3bd35c6c` for configuration.
