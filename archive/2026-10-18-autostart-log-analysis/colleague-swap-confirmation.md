# Colleague swap fix confirmed

Read-only verification on 2026-10-18, following the user's request to avoid
duplicate work. No colleague worktree, source or refs were modified.

- OS branch fix/kernel-stability-20261018 observed at
  8118a58792050b22fc2ba0fe790b7f7aa8246473.
- Commit d59b3068c534d3968348d36681fb9972ce2ebb33 pins corrected Linux 6.12.113
  source 50e2a54f0d04b1ad2885374637b3840be37a1344. Stable version and ZFS retained.
- Linux owner95ca3c3a83db5da6dba01c187aa8e45643fd295b uses kvcalloc and BOTH
  kvfree cleanup paths. Prior exact-tree evidence shows only mm/swap_cgroup.c
  differs from deployed11058eb4. This addresses the node1.stg bitmap ENOMEM.
- OS branch also repairs 6.18.49 and adds tests/suite/kernel/large-swap.nix:
  sparse256GiB guest disk, stable/unstable x cgroupv1/v2, two swapon/swapoff
  cycles, capacity and cleanup assertions, kernel warning checks.
- Author records all four old-pin cases reproduced ENOMEM; fixed runtime was
  explicitly pending. Observed exact-head CI39110027047 and39109997210 queued.
- Separate swap-service false-success issue remains: swap.nix still invokes
  bare swapon without an explicit failure guard. This is outside kernel repair.

Decision: stop duplicate swap planning/implementation. swap-plan.md is a retained
superseded DRAFT, not an accepted execution brief. Colleague owns kernel fix and
qualification; no deployment inferred. Osctld already merged60f9ed1c. Session open.

Sources:
- https://github.com/vpsfreecz/vpsadminos/commit/d59b3068c534d3968348d36681fb9972ce2ebb33
- https://github.com/vpsfreecz/vpsadminos/tree/fix/kernel-stability-20261018
- https://github.com/vpsfreecz/linux/commit/95ca3c3a83db5da6dba01c187aa8e45643fd295b

Evidence: colleague-os-ref.json, colleague-os-compare.json,
colleague-os-kernels.nix, colleague-os-swap-service.nix,
colleague-large-swap.nix, colleague-ci.json; prior Linux owner/tree artifacts.
