# 2026-08-07-vpsadminos-test-failures

## Goal

Prevent the test-runner from exhausting host memory when automatic scheduling
starts many QEMU machines, and make externally terminated QEMU processes
diagnosable and safe to clean up.

## Affected repositories

- `vpsadminos`: test-runner resource scheduling and OSVM machine lifecycle.
- `vpsadmin`, `confctl`, `terraform-provider-vpsadmin`, `vpsf-status`,
  `vpsfree-irc-bot`, `web`, and `vpsadmin-kb-captures`: update their locked
  vpsAdminOS test framework after the framework changes and Fedora mitigation
  reached `staging`.
- `vpsadminos-org-configuration`: previously inspected for context; no change
  is planned.

## Approach

1. Base memory and `/dev/shm` scheduling on the smaller of assigned and
   initially available capacity, and keep that limit monotonic for the run.
2. Raise the default memory and `/dev/shm` reserves from 4 to 8 GiB while
   preserving explicit CLI and environment overrides.
3. Preserve run-alone behavior for oversized tests, but log a prominent
   warning with the requested and available resources.
4. Record QEMU terminating signals and synchronize QEMU process/reaper state so
   cleanup cannot signal a nil or reused PID.
5. Keep scheduler and OSVM changes in separate commits, run focused specs and
   hooks, obtain the mandatory standalone review, then run integration CI.
6. Lock every workspace test-framework consumer to vpsAdminOS staging revision
   `837baf04054c6ee0e71d288b8870ac42a6990c38`. For consumers that obtain it
   through vpsAdmin, update only the nested `vpsadmin/vpsadminos` lock and keep
   the vpsAdmin application revision unchanged.
7. Validate each lock-only update locally and in its integration workflow,
   then fast-forward every updated default branch after exact-head CI passes.

## Compatibility and deployment

The changes affect only test scheduling, diagnostics, and consumer dependency
locks. There are no protocol, API, persisted-state, database, production-node,
mixed-version, or deployment ordering concerns. Existing resource options
remain compatible and override the new defaults. Machine logs gain additive
signal fields. Consumer lock updates also inherit intervening vpsAdminOS
Nixpkgs and packaged-gem updates, so test packages and VMs rebuild. Rolling
back the commits restores the previous test framework without data conversion.

## Testing plan

- Add resource-pool and executor specs for initial availability, cgroup
  headroom, monotonic limits, fallback behavior, overrides, and oversized-test
  warnings.
- Add OSVM specs for normal and signaled exits plus process-exit/cleanup races.
- Run focused RSpec suites in the repository Nix shells and mandatory
  Overcommit hooks.
- After the mandatory change review, run the full GitHub Actions VM suite and
  inspect test artifacts and runner memory metrics. Do not accept QEMU signal
  failures, cleanup TypeErrors, or memory approaching the previous 1.2 GiB
  low-water mark.
- For every consumer, verify that only `flake.lock` changes, evaluate the flake
  and CI-tagged tests, run declared hooks, and require exact-head integration
  CI. Build the KB capture runner and cluster configuration and run its local
  check suite; it has no GitHub workflow.

## Decisions

- Implement code-only mitigation; do not add a temporary runner configuration
  cap.
- Keep oversized tests running alone with a warning instead of failing fast.
- Do not add swap, automatic infrastructure retries, or broadly reduce guest
  memory as part of this fix.
- Keep downstream vpsAdmin application revisions and KB capture provenance
  unchanged; update only the nested vpsAdminOS input.
- Skip another standalone review for consumer updates because they are
  isolated generated dependency-lock changes with no consumer code or design
  changes.
