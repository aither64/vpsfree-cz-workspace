---
lifecycle: abandoned
---
# 2026-06-10-vpsadminos-nftables-bug

## Repositories
- `vpsadminos` bare repo inspected at `repos/vpsadminos.git`.
- Upstream Linux commit fetched into `/tmp/codex-linux-f41c` for source
  inspection.

## Status
- Implemented a vpsAdminOS eBPF LSM mitigation in worktree
  `worktrees/2026-06-10-vpsadminos-nftables-bug/vpsadminos` on branch
  `2026-06-10-vpsadminos-nftables-bug`.
- The guard uses `lsm/netlink_send`, with a stateful policy that tracks risky
  verdict maps/sets and denies only transaction batches that delete them from
  non-initial user namespaces on vulnerable kernels.
- Added a compact Bash checker,
  `work/2026-06-10-vpsadminos-nftables-bug/check-cve-2026-23111-nft.sh`,
  that uses `unshare -Urn` and `nft` to exercise the public catchall verdict
  map abort pattern in a private network namespace. It infers vulnerable
  behavior only from nft command outcomes and does not attempt heap spraying,
  privilege escalation, or post-UAF access.

## Changes
- Added `os/livepatches/ebpf/programs/nft_cve23111_guard.bpf.c`.
- Registered `nft_cve23111_guard` in
  `os/livepatches/ebpf/available.nix`, enabled only for kernels
  `6.12.33` through `6.12.69`.
- Extended `tests/suite/ebpf-livepatch.nix` to assert the guard is included
  through `6.12.69` and excluded from `6.12.70` and current fixed kernels.
- Committed and pushed vpsAdminOS branch
  `2026-06-10-vpsadminos-nftables-bug`.
  - Original commit: `ad8f663ac os: add nftables CVE-2026-23111 eBPF guard`
  - Rebasing on `origin/staging` changed the commit to
    `d9c4552dd os: add nftables CVE-2026-23111 eBPF guard`
  - Remote: `origin/2026-06-10-vpsadminos-nftables-bug`

## Commands run
- `bin/dev-session current`
- `git fetch --depth=2 https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git f41c5d151078c5348271ffaf8e7410d96f2d82f8`
- `git show FETCH_HEAD`
- `git grep` over upstream Linux source for `netlink_send`,
  `security_netlink_send`, nfnetlink constants, and nftables abort paths.
- `git grep` over `repos/vpsadminos.git` for BPF LSM/kernel config and eBPF
  livepatch infrastructure.
- `nix shell nixpkgs#nftables -c unshare -Urn ...` to verify the nft syntax for
  a catchall verdict map and the expected fixed-kernel command outcomes.
- `CVE23111_ACCEPT_RISK=1 nix shell nixpkgs#nftables -c work/2026-06-10-vpsadminos-nftables-bug/check-cve-2026-23111-nft.sh`
  to run the Bash checker on this development host.
- `nix shell nixpkgs#clang nixpkgs#bpftools -c ... clang -target bpf ...`
  to compile `nft_cve23111_guard.bpf.c` against host BTF and generate a
  libbpf skeleton.
- `nixfmt --check os/livepatches/ebpf/available.nix tests/suite/ebpf-livepatch.nix`
- `./test-runner.sh test ebpf-livepatch`
- `nix build --no-link --print-out-paths --impure --expr ... ebpf.loader`
  with `kernel.dev` set to cached
  `/nix/store/8mk4cz1dsds7l0aiz4rpxmmakir0xixz-linux-6.12.59-dev`.
- `git diff --check`
- `nix develop --command overcommit --run`
- `nix develop --command git push -u origin 2026-06-10-vpsadminos-nftables-bug`
- `git fetch origin staging`
- `nix develop --command git rebase origin/staging`
- `./test-runner.sh test ebpf-livepatch`
- `nix develop --command git push --force-with-lease origin 2026-06-10-vpsadminos-nftables-bug`

## Results
- Upstream fix is a one-line change in `nft_map_catchall_activate()` that
  corrects an inverted active-element check.
- The vulnerable action is in the nf_tables batch abort path for
  `NFT_MSG_DELSET` and `NFT_MSG_DESTROYSET`, where map/object sets are
  reactivated via `nft_map_activate()`.
- Public reproductions trigger the bug by deleting a verdict map with a
  catchall `goto` element and forcing another operation in the same batch to
  fail, causing abort.
- nfnetlink continues processing messages after non-OOM errors and records the
  batch as failed, so a failing message before or after a risky delete can lead
  to abort.
- The LSM hook definition includes `netlink_send(struct sock *sk,
  struct sk_buff *skb)`.
- `netlink_sendmsg()` copies userspace data into an skb, then calls
  `security_netlink_send(sk, skb)` before `netlink_unicast()`, so the hook can
  inspect and deny the request before nfnetlink processes it.
- nfnetlink message type format is `(subsystem << 8) | operation`, with
  `NFNL_SUBSYS_NFTABLES = 10`; batches use `NFNL_MSG_BATCH_BEGIN` and
  `NFNL_MSG_BATCH_END`.
- vpsAdminOS has `CONFIG_BPF_LSM = yes` for kernels >= 6.12.33 and already
  has an eBPF livepatch registry and examples.
- Bash checker validation on the development host:
  - kernel: Linux 6.18.34
  - command:
    `CVE23111_ACCEPT_RISK=1 nix shell nixpkgs#nftables -c work/2026-06-10-vpsadminos-nftables-bug/check-cve-2026-23111-nft.sh`
  - result: `FIXED/NOT OBSERVED - chain deletion is still blocked`
  - exit status: 0
- Standalone CO-RE compile against host BTF succeeded and generated
  `nft_cve23111_guard.bpf.o` and a libbpf skeleton.
- `nixfmt --check` succeeded for the modified Nix files.
- `./test-runner.sh test ebpf-livepatch` succeeded: 30 examples, including
  the new vulnerable-kernel selection check.
- Overcommit pre-commit hooks passed before commit, and commit-msg hooks
  passed during commit.
- Rebase onto `origin/staging` succeeded without conflicts.
- Post-rebase `./test-runner.sh test ebpf-livepatch` succeeded: 30 examples.
- Force-with-lease push updated the remote branch from `ad8f663ac` to
  `d9c4552dd`.
- eBPF package build for vulnerable kernel `6.12.59` succeeded using cached
  kernel dev output:
  `/nix/store/lsy3ipad0bfbfzc9llfbrm4p047dpggc-ebpf-livepatch-loader-6.12.59`.
- The development host has `kernel.unprivileged_bpf_disabled = 2`, so the BPF
  program was not loaded or attached on the host. A verifier/runtime attach
  test still needs root/CAP_BPF or a vpsAdminOS VM.
- An initial ad hoc Nix expression used plain
  `kernelPackages.genKernelPackage "6.12.59"`, producing uncached kernel dev
  output `/nix/store/kqcfj87p6xkp9867hjbnqym8pwy3s4yx-linux-6.12.59-dev` and
  causing Nix to start building Linux. The build was stopped. The cached CI
  output is a different derivation,
  `/nix/store/6bppv7blrm039vn4xgifcivg2940p73v-linux-6.12.59.drv`, with ZFS
  builtin handling and dev output
  `/nix/store/8mk4cz1dsds7l0aiz4rpxmmakir0xixz-linux-6.12.59-dev`. That dev
  output was fetched successfully from `cache.vpsadminos.org` and used for the
  package build.

## Open questions
- Runtime verifier/attach validation in a vpsAdminOS VM on `6.12.59`.
- Whether to add a VM test that loads the guard and asserts ordinary nftables
  operations still work while the risky delete batch is denied.

## Cleanup
- The checker is stored only under the initiative directory. Earlier raw
  netlink prototype files were removed in favor of the requested Bash+nft
  version. A duplicate checker created during subagent timeout handling was
  removed; the final checker is `check-cve-2026-23111-nft.sh`.

## Archival request, 2026-10-06

The workspace operator requested archival of sessions dated August 2026 or
older, retaining recorded work and branches. This checkpoint commits the
existing plan and active state before the ordinary archive transition.
