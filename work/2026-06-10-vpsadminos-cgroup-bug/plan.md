# 2026-06-10-vpsadminos-cgroup-bug

## Goal
Find and fix why starting a container can fail in osctld with
`Unable to set .../cpuset.cpus ... parameter not found` because cgroup v2
controllers were not delegated to the container cgroup.

Merge in the completed `2026-06-10-osctld-crash` work so one branch contains
both the missing-rootfs crash hardening and the cgroup v2 delegation fix, with
only one generated gem rebuild commit.

Also fix the container console restart problem found while validating the
branch: `osctl ct restart` can fail when tty0 connection returns
`ECONNREFUSED` even though the container continues starting.

## Affected repositories
- `vpsadminos`: osctld cgroup and container start handling.

## Approach
- Reproduce the failing code path from the reported osctld backtrace.
- Inspect cgroup v2 delegation/setup for pool, group, user, and container
  cgroups.
- Patch osctld so required controllers are enabled before container start or
  scheduling writes controller-specific files.
- Add focused regression coverage if the repository has suitable tests for this
  behavior.
- Treat refused tty0 console socket connections as transient during container
  start/restart, matching the existing retry behavior for missing sockets.
- Cherry-pick the non-generated functional commits from
  `2026-06-10-osctld-crash`, skip its older gem rebuild commit, and rebuild
  packaged gems once after all functional changes.

## Compatibility and deployment
- The change must be compatible with existing cgroup v2 hierarchies and running
  pools.
- It must not require coordinated updates of all nodes unless the investigation
  proves the persisted cgroup layout is incompatible.
- Mixed-version operation should be acceptable because osctld manages local
  node cgroups; no API or on-disk format change is expected at this stage.
- Rollback should leave only kernel cgroup controller state, which older osctld
  already understands.
- The missing-rootfs crash hardening is backward compatible with existing
  persisted container state: non-staged containers with unavailable rootfs are
  marked `error`; staged containers remain staged for import/receive workflows.
- Broken-container cleanup remains conservative: it tolerates already-missing
  container datasets and direct empty stale shared-dir children, but does not
  recursively remove arbitrary contents.
- Console retry handling is local to osctld start/restart behavior and does not
  change persisted state, APIs, or deployment ordering.

## Testing plan
- Run the focused osctld tests or Ruby specs covering cgroup/controller setup.
- If no focused automated test exists, run the closest available osctld test
  target and record any limitation.
- Run focused RSpec coverage for the imported crash hardening and the new
  cgroup delegation behavior.
- Run focused RSpec and RuboCop coverage for console retry handling.
- Run `./test-runner.sh test osctld/resilience` against rebuilt packaged gems.
- Run `./test-runner.sh test osctl/ct-map-mode` against rebuilt packaged gems
  because it reproduced the restart/tty0 failure locally.
- Push the combined branch and monitor GitHub Actions.
