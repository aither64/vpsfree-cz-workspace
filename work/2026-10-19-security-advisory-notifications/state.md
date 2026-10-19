---
lifecycle: active
---

# Hourly security advisory digests

## Status

Implementation authorized by the user's “Implement the plan.” Deployment and
service restarts are excluded; no default-branch merge approval. Session open.
Identity matches current, both environment markers and trusted thread binding.

## Phase checklist

- [x] Investigation, architect design and finalized plan.
- [x] User selected implementation, including site bot package update.
- [ ] Bot and site implementation, documentation, quick checks and commits.
- [ ] Independent final review of complete branch histories/diffs.
- [ ] Targeted integration and affected-container build without activation.
- [ ] Publish final evidence and handoff, awaiting integration approval.

## Backlog

| Owner | Deliverable / acceptance | Dependency and checks |
| --- | --- | --- |
| implementer0 | Bot hourly digest plus modes, focused tests, docs, commits and publication | Accepted design; quick tests/hooks; lead prose inspection |
| implementer1 | Site summary/3600 and final bot revision/hash, commits and publication | Settings independent; final pin depends on bot head; evaluate settings |
| reviewer0 | Independent final review including history/pins/no-migrations conclusion | Both deliverables committed and quick checks pass |
| lead | Scope, tracking, writing inspection, review packet and monitored verification | Member reports; no deployment or merge |

Saved members are ready with workspace-write access for both implementers;
reviewer0 is read-only. Retain all model/effort/access settings.

## Repositories

Feature worktrees/heads pending registration. Canonical bare clones only were
used for investigation. No other session records/worktrees may be reused.

## Documentation and decisions

- [Design brief](design.md): accepted hourly aggregation design. Final chat plan
  and this plan exclude deployment and supersede proposal-only wording.
- Rejected per-poll summaries because gradual creation still produces spam.
- Pending counts are memory-only; restarts discard them and start a full interval.
- Existing API lists have no default limit; retain unlimited query shape.
- Configuration package pin is fetchFromGitHub, not a flake input.

## Verification and review

Not yet run. Mandatory review follows final commits/quick checks and precedes
long tests. No migrations expected. No deployment, service restart or integration.

## Next action

Commit initial tracking, create owned worktrees and assign both execution packages.
Preserve unrelated shared checkout/index changes; no cleanup or lifecycle action.
