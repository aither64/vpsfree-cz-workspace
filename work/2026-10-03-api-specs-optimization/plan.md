# API specs workflow optimization

## Goal

Investigate typical vpsAdmin `api-specs` workflow duration and recommend a
way to evaluate every existing test faster than the reported 40+ minutes.
This phase is investigation and proposal only; no application edits, CI runs,
deployment, or feature integration are requested.

## Affected repositories

- `vpsadmin`: inspect upstream workflow, topic selection, test setup, and logs.
- Coordination workspace: retain evidence and a design/verification proposal.

## Approach

1. Sample recent completed GitHub Actions runs and separate queue, setup,
   topic test execution, failures, and the critical path.
2. Ask retained architect0 to inspect topic balance and propose safe parallel
   partitions with exact-once test coverage and isolated state.
3. Reconcile timing evidence with the architecture and recommend a concrete
   initial split, expected duration, costs, limitations, and validation.

## Decisions

Preserve all existing tests. Timing evidence shows topic imbalance, with
platform taking ~42min and several topics ~1min. Compare platform-only splitting
(~23–25min floor), same-count topic rebalancing (~18–22min floor), and
duration-balanced shards (15–20min target, subject to measurement/queueing). Use read-only canonical repository inspection;
do not borrow other sessions' worktrees. Do not launch a new full suite merely
to establish a historical baseline.

## Compatibility and deployment

A proposed CI-only change must preserve test discovery, plugin combinations,
database isolation, failure reporting, and required-check names. No production
API, schema, protocol, persisted-state, deployment, or rollback changes are
intended. Workflow runner capacity and added setup cost must be considered.

## Documentation

Readers: maintainers choosing the optimization and a subsequent implementer.
Record evidence in investigation.md and the architect proposal in design.md;
keep plan.md/state.md and portal links current. No project documentation edit
is needed for an unimplemented proposal.

## Testing plan

Read historical job/step logs and inspect exact-once topic validation. Model
candidate partitions from measured durations; distinguish estimates from
executed results. A future implementation must verify complete file/example
coverage and compare a full run on the same revision before and after.
