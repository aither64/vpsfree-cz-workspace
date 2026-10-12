# 2026-10-12-session-archive-policies

## Goal

Explicit archival closes the selected session without merge/publication or clean
checkout prerequisites. Automatic archival retains its strict completion policy.
Implement the accepted conversation plan, deploy on aitherdev, then archive
2026-10-11-diagnose-vpsadmin-api-exception. The later user instruction "merge it, no waiting for ci" authorizes the three
registered branches into master. It does not authorize archiving this
implementation session.

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

## Artifact metadata prevention (user-requested scope extension)

The network-ipv4-left-counter thread prepended three uncommitted artifact entries
with name captions instead of label. The existing strict Go and Ruby readers
reject this presentation-field mismatch and disable normal session access. At
investigation time no typed artifact writer existed; agents edited YAML directly. The user
explicitly requested correcting this record and preventing recurrence.

Add matching name-as-label reads in Go/Ruby, retaining label as the canonical
written field and preserving path confinement, explicit scope and all identity
validation. Add dev-session artifact add SLUG PATH --label TEXT --as-is as a
locked, generation-checked, fully validated atomic manifest update. It updates
normalized existing paths without duplication, refuses pending lifecycle/creation
operations and never starts a session or changes repositories/conversations.
Document the command in the session guide/documentation skill and site procedure.
Repair only the three specified caption keys in the selected record. No automatic
repair of arbitrary identity metadata; no schema bump or new persisted format.
Old executors read every newly written canonical manifest. Aliases supplied by
hand remain a forward-readable input extension; canonical writers remove them.
Quick checks cover shared Go/Ruby alias fixtures, unsafe paths and caption
precedence, update/insert without scope loss, failed update leaving bytes unchanged,
operation exclusion and CLI parsing. New public mutation/interface requires
affected independent review before final long checks and deployment.


## Implementation outcome

The accepted scope is implemented, independently reviewed and deployed. The
selected original session is archived with verified recovery. See state.md and
rollout.md for final revisions and execution evidence. All three registered feature heads are now merged into remote master under
explicit user direction. This initiative is complete and remains open.
