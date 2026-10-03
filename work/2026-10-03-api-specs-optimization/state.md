---
lifecycle: active
---

# API specs workflow optimization

## Current status

Phase: proposal preparation. Historical timing investigation is complete;
architect design is written; independent documentation review is pending. Request remains
read-only analysis and a solution proposal.
Session identity verified against thread binding and both environment markers.

## Phase checklist

- [x] Verify ownership and inspect retained team roster.
- [x] Collect representative completed workflow/job/step timings.
- [x] Architect assesses parallel partitions and verification requirements.
- [ ] Reconcile evidence and present recommendation.

## Repositories and ownership

- vpsadmin canonical bare clone: `repos/vpsadmin.git`; inspect origin/master.
- No feature branch or worktree created; no application changes planned.
- architect0 (design, Astra/xhigh, workspace_write): design investigation.
- Lead: historical timings, coordination, integration of findings.

## Evidence and limits

The workflow already has 13 topics × two plugin modes. Sample of 14 successful
runs: eight master runs median49.59min including queueing, six feature runs
median43.19min. Platform is the critical path in all14; full platform median
41.58min. Setup usually costs ~0.5min. Detailed evidence: investigation.md and
timing-summary.json. Raw job metadata/logs remain local, not portal artifacts.
No new tests, builds, CI runs, review of implementation, or deployment launched.

## Next action

Reconcile architect design with timing evidence, then independently review
the committed proposal under the documentation-only general review lane.
No application implementation or CI run is authorized by this investigation.

## Documentation

Session records own this unimplemented investigation and proposal. Application
documentation remains unchanged. Keep session open for follow-up.

## Coordination

Initial plan/state committed as `8bd7c4e7`. No hook framework declared in the
coordination repository; only sample Git hooks present. Shared master preserved
and only this session tracking paths staged. Upstream vpsAdmin SHA confirmed
through GitHub API as well as canonical fetch. No other session records or
worktrees accessed.

## Recommendation and checks

Architect design.md supplies a three-way platform partition (~13–14min/group),
a same-count static rebalance, and preferred 13 timing-balanced shards per mode.
All targets are estimates. Recommended low-complexity option: combine short
topics and split platform/users-auth/network while retaining26 runners; target
~20–25min plus queueing. Durable option: collect per-file timings, then balance
13 shards per mode for a15–20min target. Preserve every test and both modes.
Timing JSON sanity checks passed (14unique successful runs, coherent durations).
No implementation benchmark, suite rerun, code review, or deployment performed.
Proposal review uses mandatory-change-review general lane only, documentation
low risk, retained reviewer0 Sol/xhigh/read_only with no override or fallback.
