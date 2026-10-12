# 2026-10-12-session-archive-policies

## Goal

Explicit archival closes the selected session without merge/publication or clean
checkout prerequisites. Automatic archival retains its strict completion policy.
Implement the accepted conversation plan, deploy on aitherdev, then archive
2026-10-11-diagnose-vpsadmin-api-exception. This does not authorize integrating
feature content into any default branch or archiving this implementation session.

## Affected repositories

- dev-workspace: Ruby lifecycle, recovery, automatic merge proofs, Go readers,
  portal/API, tests and runtime documentation.
- workspace: lifecycle instructions and composed runtime selection.
- vpsfree-cz-configuration: matching dev-workspace channel and aitherdev rollout.

## Approach

Add an explicit policy and neutral archived lifecycle. Quiesce owned agents and
queued submissions, capture local recovery data, forcibly remove all owned
worktrees, archive tracking and retire runtime. Restore saved checkout/index/files
on revival. Keep automatic proofs and correct their multiple-target assumption.

## Decisions

- Manual archive skips merge and publication checks, including unavailable refs.
- Preserve local work automatically in private storage before removing worktrees.
- Stop owned active turns; retain conversation and queued-prompt records.
- Remove every owned checkout, including nested/detached/dirty checkouts.
- Explicit closure is archived, not an assertion of completion or abandonment.
- Keep normal cluster release and exact session ownership boundaries.

## Compatibility and deployment

Version new explicit-operation recovery formats; preserve existing manifests and
pending journal semantics. No database or node migration. Deploy matching host
runtime from the configuration feature branch, then the composed application
through its user profile. Finish pending lifecycle journals before package changes;
application package recovery is forward-only. Default integration needs separate
user direction. No coordinated update of running nodes is needed.

## Documentation

Runtime session/archive guides own behavior and recovery. Workspace procedures
own agent policy. This initiative owns temporary rollout and review evidence.

## Testing plan

Quick Ruby/Go/Node checks before committed independent review; then packaged and
browser verification. Cover dirty/index/untracked/ignored/binary recovery,
detached/unpublished/unmerged/missing refs, busy/queued agents, multi-target
automatic proof, interruption/retry, old journals and revival. Use fresh catalog
watchers for long checks and deployment observation.
