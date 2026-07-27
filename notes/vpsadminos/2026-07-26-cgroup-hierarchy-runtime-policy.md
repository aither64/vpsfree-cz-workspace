# Cgroup hierarchy runtime policy ordering

## Symptom

The `kernel/vpsadminos#cpu-view-cgroups-v1` VM exposed two hierarchy failures
while validating runtime container policy changes:

- rebuilding a deleted child group cpuset before its parent can fail because a
  cgroup-v1 cpuset must inherit valid parent CPU and memory masks;
- lowering a stable container CPU limit from 400% to 250% failed with `EINVAL`
  when the parent quota was restricted while its payload child still allowed
  400%.

The first attempt to cover group recovery also applied an unrelated `pids.max`
configuration after manually deleting its unused cgroup path. Normal apply
correctly rejected that missing path; path creation belongs only to exact
quarantine recovery.

## Cause

Cgroup policy values are constrained by the complete live hierarchy, not by
one configured object at a time. Cgroup-v1 CFS bandwidth is additionally a
pair of separate quota and period files, so even a correct final ratio can
pass through an invalid intermediate ratio.

## Fix and workflow

- Reconstruct group cpusets as one hierarchy transaction: initialize parent
  masks before children, use unions while changing disjoint masks, then commit
  final leaf values.
- Expand CPU bandwidth parent-first and restrict it child-first.
- Choose quota-versus-period write order from the current and desired ratios;
  verify the final stable root, managed generation, and finite descendants.
- Never broaden residual generations.
- Use exact rollback ordering and retain the policy quarantine marker if
  rollback or verification fails.
- Permit missing controller-path creation only while recovering the exact
  quarantined group path. Ordinary full apply continues to report a missing
  unrelated controller path.
- Run cgroup-v1 and cgroup-v2 VM selectors sequentially. Tests with the same
  basename share `/tmp/os-test-runner` state and can collide when parallel.

## Verification

Initiative `work/2026-07-24-ct-start-hang`:

- `kernel/vpsadminos#cpu-view-cgroups-v1`: 147/147 examples, 1/1 test;
- `kernel/vpsadminos#cpu-view-cgroups-v2`: 147/147 examples, 1/1 test.

The v1 run covered group reconstruction, 400% to 250% restriction, quota
expansion, unlimited reset, and combined cpuset/bandwidth policy against the
real kernel.
