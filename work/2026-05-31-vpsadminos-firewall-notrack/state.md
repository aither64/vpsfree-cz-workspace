---
lifecycle: active
---
# vpsAdminOS Firewall Without Init-Namespace Conntrack State

## Worktrees

- `vpsadminos`
  - path: `worktrees/2026-05-31-vpsadminos-firewall-notrack/vpsadminos`
  - branch: `2026-05-31-vpsadminos-firewall-notrack`
  - base: `origin/staging`
  - initial HEAD: `dfed89a5d os: update gems to 25.11.0.build20260531170948`
- `vpsadmin`
  - path: `worktrees/2026-05-31-vpsadminos-firewall-notrack/vpsadmin`
  - branch: `2026-05-31-vpsadminos-firewall-notrack`
  - base: `origin/master`
  - initial HEAD: `31942d6d2 packages: update nodectl gems`
- `vpsfree-cz-configuration`
  - path: `worktrees/2026-05-31-vpsadminos-firewall-notrack/vpsfree-cz-configuration`
  - branch: `2026-05-31-vpsadminos-firewall-notrack`
  - base: `origin/master`
  - initial HEAD: `5c6f69e4 inputs: update vpsadminosProduction to 8a76972f`

## Implemented Changes

### vpsadminos

- Removed the nixpkgs `firewall-iptables.nix` import from
  `os/modules/nixos-modules.nix`.
- Replaced the runit wrapper around nixpkgs' generated firewall service with a
  vpsAdminOS-specific iptables firewall module.
- Added `networking.firewall.conntrack.enable`, defaulting to `false`.
- Added `networking.firewall.protectedRules` for source-restricted TCP/UDP
  services in the default-open, no-conntrack firewall mode.
- Added idempotent raw-table notrack handling for IPv4 and IPv6.
- Kept a conntrack-enabled stateful mode for `lxcbr` and other NAT-based
  development/test systems.
- Added an assertion that `networking.lxcbr.enable` requires
  `networking.firewall.conntrack.enable`.
- Enabled conntrack in qemu, ISO, the vpsAdminOS test base, and the
  build-vpsadminos-container-image-repository configuration.
- Added the focused VM test `tests/suite/firewall/conntrack.nix` and
  registered it in `tests/all-tests.nix`.
- The test has two Ruby/RSpec-style scripts, `no-conntrack` and `conntrack`,
  runs them with `testScriptJobs = 2`, and uses an in-VM network namespace as
  the traffic source instead of a client VM.

### vpsfree-cz-configuration

- Converted vpsAdminOS node service restrictions to
  `networking.firewall.protectedRules`.
- Gated monitoring exporter and munin firewall rules so NixOS machines keep
  `extraCommands` while vpsAdminOS nodes use `protectedRules`.
- Left unrestricted services open under the new default-open node policy.

### vpsadmin

- No code changes.
- No vpsAdmin modules were found to append iptables rules to vpsAdminOS nodes.

## Validation

Successful checks:

- `nix develop -c nixfmt --check` on all changed vpsAdminOS Nix files.
- `nix develop -c nixfmt --check` on all changed
  `vpsfree-cz-configuration` Nix files.
- `git diff --check` in `vpsadminos`.
- `git diff --check` in `vpsfree-cz-configuration`.
- `nix eval --json --impure --expr 'let flake = builtins.getFlake (toString ./.); in flake.tests.x86_64-linux."firewall/conntrack".drvPath'`
  in `vpsadminos`.
- `nix eval --json --impure --expr 'let flake = builtins.getFlake (toString ./.); in flake.packages.x86_64-linux.qemu.drvPath'`
  in `vpsadminos`.
- `nix eval --json --impure --expr 'let flake = builtins.getFlake (toString ./.); in flake.packages.x86_64-linux.iso.drvPath'`
  in `vpsadminos`.
- `./test-runner.sh test --state-dir /tmp/os-test-runner-firewall-conntrack-netns-3 'firewall/conntrack#*'`
  passed in 390.29 seconds.
- `nix eval --impure --json .#confctl.toplevel.m_cz_vpsfree_containers_int_munin_13634c7c.drvPath`
  in `vpsfree-cz-configuration`, to verify that NixOS systems do not see the
  vpsAdminOS-only `protectedRules` option.

The focused VM test verifies:

- no-conntrack mode installs raw PREROUTING and OUTPUT notrack rules;
- no-conntrack mode leaves unprotected TCP/UDP ports reachable;
- no-conntrack mode allows protected TCP/UDP ports from configured sources and
  drops other sources;
- no-conntrack mode does not duplicate notrack rules on firewall reload;
- no-conntrack mode leaves `conntrack -L` empty after exercised traffic;
- conntrack mode keeps the `ESTABLISHED,RELATED` rule and installs no raw
  notrack rules;
- conntrack mode accepts configured legacy TCP/UDP service ports, drops
  unconfigured service ports, and creates conntrack entries for active
  connections.

Partial/blocked validation:

- `nix eval --impure --json --override-input vpsadminosStaging path:/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-05-31-vpsadminos-firewall-notrack/vpsadminos .#confctl.toplevel.m_cz_vpsfree_nodes_stg_node1_cd7ccd6a.drvPath`
  reached the staging node system derivation with the local vpsAdminOS override,
  but failed because local `/secrets/nodes/initrd/ssh_host_ed25519_key` is not
  present. No `protectedRules` unknown-option failure was encountered before the
  missing-secret error.

Earlier failed test attempts:

- Initial test composition passed module lambdas through `mkMerge`
  incorrectly; fixed by applying the extra config function.
- The raw-rule check used an immediate `iptables` check; fixed by waiting for
  `iptables-save` output because `sv check firewall` can report the runit
  service before the firewall script has finished.
- One run failed because Nix variables leaked into Ruby as unbound locals;
  fixed by interpolating the source addresses as strings.
- The first Ruby version used `Socket.tcp` with unsupported keyword arguments;
  fixed by using explicit `Socket.new`, `bind`, and `connect`.
- Separate client VMs were removed. The final test uses a veth pair and a
  client network namespace inside each server VM, so no qemu socket/multicast
  network is needed.
- Parallel `testScriptJobs = 2` initially exposed top-level Ruby helper method
  sharing between scripts; fixed by using per-script lambdas.

## Current Status

- `vpsadminos` changes were committed as `7a520ff07`
  (`os: add conntrack-free firewall mode`) and pushed to
  `origin/2026-05-31-vpsadminos-firewall-notrack`.
- GitHub Actions CI run `26723384139` was created for the pushed branch and
  remained queued for a self-hosted runner for at least 49 minutes, still with
  no assigned runner as of 2026-05-31 23:07 CEST. Local monitoring was stopped
  after repeated queued checks because there were no CI logs or failures to
  act on.
- Monitoring resumed and the same run was still queued with no assigned runner
  as of 2026-05-31 23:20 CEST, 1h1m after creation.
- The run was rechecked again in the next goal turn and remained queued on the
  `self-hosted` label with empty `runner_name`, no steps, and no logs to
  inspect.
- CI later started: `Build OS and populate binary cache` ran on
  `gh-runner2.int.vpsadminos.org` and succeeded at 2026-06-01 01:03 CEST. The
  next job, `Run test suite`, is queued for a self-hosted runner.
- `Run test suite` started on `gh-runner1.int.vpsadminos.org` at
  2026-06-01 04:46 CEST.
- CI run `26723384139` failed after the test suite:
  `incus/arch#latest` and `osctl/image-repository-build-service`.
  `incus/arch#latest` also failed on the preceding `staging` run and is treated
  as inherited for this branch. `osctl/image-repository-build-service` failed
  during Nix evaluation with the new lxcbr/conntrack assertion.
- Fixed `tests/suite/osctl/image-repository-build-service.nix` by adding
  `networking.firewall.conntrack.enable = lib.mkDefault true` to the nested
  vpsAdminOS config that enables `lxcbr`.
- Local validation after the fix:
  `./test-runner.sh test --state-dir /tmp/os-test-runner-image-repository-build-service-fix osctl/image-repository-build-service`
  passed in 269.51 seconds.
- Fix committed as `e4f1dcf62`
  (`tests: enable conntrack for image repository VM`) and pushed to the
  feature branch. New CI run `26733855889` started for the branch.
- CI run `26733855889` fixed the image-repository evaluation failure:
  `firewall/conntrack` and `osctl/image-repository-build-service` both passed.
  The only remaining failure was `incus/arch#latest`.
- `incus/arch#latest` now succeeds on current Arch/Incus, but the test was
  still marked `expectFailure = true`, causing an unexpected-success failure.
  Removed the stale expected-failure marker from `tests/suite/incus/arch.nix`.
- Local validation after that fix:
  `./test-runner.sh test --state-dir /tmp/os-test-runner-incus-arch-fix 'incus/arch#latest'`
  passed in 339.16 seconds.
- Fix committed as `395ec3daa`
  (`tests: stop expecting incus arch to fail`) and pushed to the feature
  branch. New CI run `26735959605` started for the branch.
- CI run `26735959605` passed on `395ec3daa`. `Build OS and populate binary
  cache` and `Run test suite` both completed successfully on
  `gh-runner1.int.vpsadminos.org`.
- Full `overcommit --run` initially failed on Nix formatting in four files that
  were not introduced by this branch: `os/configs/proactive-swap-qemu.nix`,
  `os/livepatches/ebpf/default.nix`,
  `os/modules/config/damon-reclaim.nix`, and
  `tests/suite/kernel/proactive-swap.nix`.
- Applied nixfmt to those files in a separate commit `4350b4bc7`
  (`format: apply nixfmt to existing files`) and pushed it.
- `nix develop --command overcommit --run` passes on `4350b4bc7`; Nixfmt and
  RuboCop both report OK.
- CI run `26743014011` for `4350b4bc7` passed the build/cache job, then failed
  only in `podman/debian#latest`. The failure was an external registry error:
  `podman run hello-world` received HTTP 504 Gateway Time-out while pinging
  `quay.io`, so no branch code change is indicated.
- Attempted to rerun failed jobs with `gh run rerun 26743014011 --failed`, but
  GitHub rejected it with `Resource not accessible by personal access token`.
- `vpsadminos` worktree is clean at `4350b4bc7`.
- The latest `staging` CI run on the base commit failed before this branch, in
  unrelated-looking tests: `incus/arch#latest`, `cgroups/mount-v2#rocky-8`,
  and `dist-config/netif-routed#almalinux-8`.
- Fetched upstream defaults on 2026-06-01. `vpsadminos` was already on top of
  `origin/staging`; `vpsadmin` was rebased onto `origin/master` and has no
  repository changes.
- `vpsfree-cz-configuration` was rebased onto current `origin/master`
  (`a38c85ec`). Its Overcommit run exposed an unrelated RuboCop failure in
  `configs/vpsadmin/api/abuse_notice_parser/master_dc.rb`; fixed separately in
  commit `4b99498d` (`vpsadmin-config: fix abuse notice regexp style`).
- Committed the firewall configuration changes in `vpsfree-cz-configuration`
  as `c6e17a51` (`cluster: protect vpsAdminOS firewall services`) and pushed
  `origin/2026-05-31-vpsadminos-firewall-notrack`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration`; Nixfmt and RuboCop both report OK.
- `vpsfree-cz-configuration`, `vpsadmin`, and `vpsadminos` worktrees are clean.
- `gh run list --branch 2026-05-31-vpsadminos-firewall-notrack` in
  `vpsfree-cz-configuration` returned no workflow runs.
- Rewrote the two `vpsfree-cz-configuration` commit messages after spotting
  overlong body lines. The old pushed commits were `89c3cae3` and `e328a8ca`;
  the branch was force-updated with lease to `4b99498d` and `c6e17a51`.
- Updated `vpsfree-cz-configuration` vpsadminos inputs for channels
  `production`, `staging`, and `os-staging` with
  `confctl inputs channel set --commit --no-editor
  '{production,staging,os-staging}' vpsadminos
  4350b4bc71fa3ba364139115fe67f0dc92d01c31`.
- Initially amended the generated input commit message to keep lines within
  the generic workspace limit, but this was wrong for `confctl --commit`
  updates. Restored the exact generated `confctl` message and force-pushed
  with lease. The resulting commit is `79d3fc6d`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to 4350b4bc`).
- `confctl inputs channel ls` shows `production`, `staging`, and `os-staging`
  vpsadminos entries all at `4350b4bc`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration` after the input pin; Nixfmt and RuboCop report OK.
- No GitHub workflow runs were created for the pushed
  `vpsfree-cz-configuration` branch.
- Added explicit guidance to the workspace `AGENTS.md`: generated
  `confctl ... --commit` messages in `vpsfree-cz-configuration` must be kept
  exactly as generated and are exempt from generic line-length rewrapping.
- Added the same reminder to `vpsfree-cz-configuration/AGENTS.md` and committed
  it as `23c004cd` (`docs: preserve generated confctl commit messages`), then
  pushed the branch.
- Fetched `vpsadminos` upstream on 2026-06-01 and rebased
  `2026-05-31-vpsadminos-firewall-notrack` onto current `origin/staging`
  `b360b3a01`. The branch replayed cleanly and was force-pushed with lease.
  New `vpsadminos` tip is `e96aa4bb8`.
- New GitHub Actions CI run for the rebased `vpsadminos` branch:
  `26775781138`, queued at `e96aa4bb8`.
- Replaced the previous `vpsfree-cz-configuration` input pin commit instead of
  adding another one. Rewound the branch tail to `c6e17a51`, reran
  `confctl inputs channel set --commit --no-editor
  '{production,staging,os-staging}' vpsadminos
  e96aa4bb8adfc04ce969a92ddb763d324873b61c`, then replayed the docs reminder
  commit.
- New generated input commit is `df2135d6`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to e96aa4bb`).
  Its generated `confctl` message was kept unchanged, including hook warnings
  about long lines.
- New docs reminder commit is `1f6cbffb`
  (`docs: preserve generated confctl commit messages`). The branch was
  force-pushed with lease to `origin/2026-05-31-vpsadminos-firewall-notrack`.
- `confctl inputs channel ls` now shows `production`, `staging`, and
  `os-staging` vpsadminos entries all at `e96aa4bb`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration` after the replacement pin; Nixfmt and RuboCop
  report OK.
- `gh run list --branch 2026-05-31-vpsadminos-firewall-notrack` in
  `vpsfree-cz-configuration` still returns no workflow runs.
- Fetched `vpsadminos` upstream again on 2026-06-01. Upstream `origin/staging`
  had moved to `3d1a935f6` (`os: load l2tp_eth by default`).
- Created a temporary detached `vpsadminos-staging` worktree from
  `origin/staging`, cherry-picked the requested cleanup commits onto staging,
  and added the newly exposed upstream formatting fix for
  `tests/suite/zfs/fallocate-deadlock.nix` into the formatting commit:
  `353e46ff0` (`tests: stop expecting incus arch to fail`) and `e87f64fad`
  (`format: apply nixfmt to existing files`). Pushed `staging` by
  fast-forward from `3d1a935f6` to `e87f64fad`.
- Rebuilt the `vpsadminos` feature branch on top of new `origin/staging` with
  only the remaining firewall commits, then force-pushed with lease:
  `7c7eaa024` (`os: add conntrack-free firewall mode`) and `0545dbd04`
  (`tests: enable conntrack for image repository VM`).
- `nix develop --command overcommit --run` passes in both the temporary
  staging worktree and the final `vpsadminos` feature worktree. Removed the
  temporary `vpsadminos-staging` worktree after pushing.
- Replaced the `vpsfree-cz-configuration` input pin commit again, keeping the
  generated `confctl --commit` message unchanged. New generated input commit
  is `939c97e5`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to 0545dbd0`).
- Replayed the docs reminder as `53e91a84`
  (`docs: preserve generated confctl commit messages`) and force-pushed the
  configuration branch with lease.
- `confctl inputs channel ls` now shows `production`, `staging`, and
  `os-staging` vpsadminos entries all at `0545dbd0`.
- New vpsAdminOS CI runs are queued: feature branch run `26778286264` at
  `0545dbd04`, staging run `26778235453` at `e87f64fad`, plus older queued
  staging/feature runs from previous pushes.
- Fetched upstreams again on 2026-06-03. Current defaults:
  `vpsadminos` `origin/staging` moved to `a23367b0e`
  (`flake: nixpkgsUnstable 64c08a7ca -> 331800de5`),
  `vpsadmin` `origin/master` moved to `4ffac2b0e`
  (`webui: update dependencies`), and `vpsfree-cz-configuration`
  `origin/master` moved to `dc474a75` (`geminabox: update dependencies`).
- Rebasing `vpsadminos` onto current `origin/staging` replayed cleanly.
  The feature branch now has only `c6d122801`
  (`os: add conntrack-free firewall mode`) and `4e9b22214`
  (`tests: enable conntrack for image repository VM`) above staging.
  `nix develop --command overcommit --run` passes, and the branch was
  force-pushed with lease.
- Rebased `vpsadmin` onto `origin/master`; the branch has no local commits and
  now points at `4ffac2b0e`.
- Rebuilt `vpsfree-cz-configuration` on current `origin/master` by replaying
  the non-generated commits, then regenerated the input pin with
  `confctl inputs channel set --commit --no-editor
  '{production,staging,os-staging}' vpsadminos
  4e9b222144a67449a591178bb8fd90e65e829f0a`.
- New `vpsfree-cz-configuration` commits are `21f607d3`
  (`vpsadmin-config: fix abuse notice regexp style`), `e8940ce1`
  (`cluster: protect vpsAdminOS firewall services`), generated `confctl` commit
  `ee37ae4c`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to 4e9b2221`),
  and `7c6e82fb` (`docs: preserve generated confctl commit messages`).
  The configuration branch was force-pushed with lease.
- `confctl inputs channel ls` now shows `production`, `staging`, and
  `os-staging` vpsadminos entries all at `4e9b2221`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration`; no GitHub workflow runs were created for this
  branch.
- New vpsAdminOS workflows for `4e9b22214` are running:
  CI run `26884642104` and RSpec run `26884642144`.
- Implemented refused-firewall logging cleanup in `vpsadminos`.
  Commit `5e83719cb` (`os: disable refused firewall logging by default`)
  sets `networking.firewall.logRefusedConnections = mkDefault false` and
  routes protected-rule denials through `nixos-fw-log-refuse` instead of
  dropping directly, so existing explicit logging/reject options still apply.
- Extended `tests/suite/firewall/conntrack.nix` with refused logging coverage:
  no-conntrack protected denials use the compatibility refuse chain, both
  conntrack and no-conntrack variants are silent by default, and a separate
  `logging` testScript verifies `logRefusedConnections = true` adds a LOG rule.
- Local vpsAdminOS validation:
  `nix develop --command nixfmt --check
  os/modules/services/networking/firewall-iptables.nix
  tests/suite/firewall/conntrack.nix` passed;
  `./test-runner.sh test --state-dir
  /tmp/os-test-runner-firewall-refuse-logging 'firewall/conntrack#*'`
  passed `conntrack` and `logging` but exposed an over-strict expected count in
  `no-conntrack`; after fixing that assertion,
  `./test-runner.sh test --state-dir
  /tmp/os-test-runner-firewall-refuse-logging-rerun
  'firewall/conntrack#no-conntrack'` passed all 8 examples.
  `nix develop --command overcommit --run` passed.
- Pushed `vpsadminos` branch
  `2026-05-31-vpsadminos-firewall-notrack` to `origin` at `5e83719cb`.
- Replaced the generated `vpsfree-cz-configuration` input pin commit again,
  keeping the generated `confctl --commit` message unchanged. New generated
  input commit is `bf7cce78`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to 5e83719c`).
- Replayed the docs reminder as `7aff9e3c`
  (`docs: preserve generated confctl commit messages`) and force-pushed the
  configuration branch with lease.
- `confctl inputs channel ls` shows `production`, `staging`, and `os-staging`
  vpsadminos entries all at `5e83719c`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration`; no GitHub workflow runs were created for this
  branch.
- Current vpsAdminOS workflow status after pushing `5e83719cb`: CI run
  `26887562734` is queued, while the older CI run `26884642104` for
  `4e9b22214` is still in progress. The earlier RSpec run `26884642144` for
  `4e9b22214` passed.
- Fetched upstreams again on 2026-06-03 after the refused logging change.
  Defaults after fetch:
  `vpsadminos` `origin/staging` moved to `9e01370d8`
  (`os: update gems to 25.11.0.build20260603142841`),
  `vpsadmin` `origin/master` remained at `4ffac2b0e`, and
  `vpsfree-cz-configuration` `origin/master` remained at `dc474a75`.
- Rebasing `vpsadminos` onto current `origin/staging` replayed cleanly.
  The feature branch now has `c14a9fb3c`
  (`os: add conntrack-free firewall mode`), `1cf33bd5d`
  (`tests: enable conntrack for image repository VM`), and `cb665cd26`
  (`os: disable refused firewall logging by default`) above staging.
  `nix develop --command overcommit --run` passes, and the branch was
  force-pushed with lease.
- `vpsadmin` required no rebase; the worktree is still exactly at
  `origin/master` `4ffac2b0e`.
- Replaced the generated `vpsfree-cz-configuration` input pin commit again,
  keeping the generated `confctl --commit` message unchanged. New generated
  input commit is `afc71921`
  (`inputs: set vpsadminosOsStaging, vpsadminosProduction, vpsadminosStaging to cb665cd2`).
- Replayed the docs reminder as `4e9e27ff`
  (`docs: preserve generated confctl commit messages`) and force-pushed the
  configuration branch with lease.
- `confctl inputs channel ls` shows `production`, `staging`, and `os-staging`
  vpsadminos entries all at `cb665cd2`.
- `nix develop --command overcommit --run` passes in
  `vpsfree-cz-configuration`.
- New vpsAdminOS workflow status after pushing `cb665cd26`: RSpec run
  `26887952883` is in progress, CI run `26887953161` is queued, and RuboCop run
  `26887953030` passed. Older runs for pre-rebase commits are still visible in
  GitHub Actions.
- Merged the feature into default branches on 2026-06-03 using fresh merge
  worktrees and fast-forward-only merges.
- `vpsadminos` `staging` was fast-forwarded from `9e01370d8` to `cb665cd26`
  and pushed to `origin/staging`.
- `vpsfree-cz-configuration` `master` was fast-forwarded from `dc474a75` to
  `4e9e27ff` and pushed to `origin/master`.
- `vpsadmin` had no feature commits for this initiative and was already
  identical to `origin/master` at `4ffac2b0e`, so no default-branch merge was
  needed there.
- Validation before pushing defaults:
  `nix develop --command overcommit --run` passed in the `vpsadminos` staging
  merge worktree, and `nix develop --command overcommit --run` passed in the
  `vpsfree-cz-configuration` master merge worktree.
- During merge setup, initial `git worktree add` commands used relative paths
  from the bare repository and created temp worktrees under `repos/*.git`.
  Those clean temp worktrees were removed and recreated under
  `worktrees/2026-05-31-vpsadminos-firewall-notrack/` with absolute paths.
- Post-push workflow check: new `vpsadminos` `staging` CI run `26889296877` is
  in progress for `cb665cd26`. `vpsfree-cz-configuration` did not show a
  branch push workflow; `gh run list --branch master` only showed scheduled
  daily runs.
- Cleanup completed after default-branch pushes. Removed all initiative
  worktrees:
  `vpsadminos`, `vpsadmin`, `vpsfree-cz-configuration`,
  `merge-vpsadminos-staging`, and
  `merge-vpsfree-cz-configuration-master`. The empty
  `worktrees/2026-05-31-vpsadminos-firewall-notrack` directory was removed.
  Feature branch refs were kept locally and remotely per workspace policy.

## Next Steps

- With secrets available, run `confctl build "cz.vpsfree/nodes/stg/*"` from a
  fresh `vpsfree-cz-configuration` checkout or worktree for the `cb665cd2`
  vpsAdminOS pin.
- Run a representative vpsAdmin integration test after the staging pin if node
  control-plane behavior needs extra confirmation.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
