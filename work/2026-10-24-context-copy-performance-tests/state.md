---
lifecycle: active
---

# 2026-10-24-context-copy-performance-tests

## Status

- Phase: investigation and design. Bound identity verified by `dev-session
  current` and matching environment/thread binding.

## Phase checklist

- [x] Verify session and retained roster; scope to HaveAPI.
- [ ] Architect design and implementation boundaries.
- [ ] Implementation and quick checks, committed.
- [ ] Independent final review, including full history and migration conclusion.
- [ ] Longer verification and reproducible performance evidence.
- [ ] Publish feature branch and handoff; await integration direction.

## Backlog

| Owner | Expected result | Acceptance / dependencies |
| --- | --- | --- |
| architect0 | `design.md`: fix and performance-testing design | Actual call graph, immutable/auth invariants, independent packages and checks |
| lead | Tracking, worktree preparation and acceptance | Preserve shared checkout; commit initial records before project-code commits |
| implementers | Pending design boundaries | Fix, tests, documentation, quick checks and commits |
| reviewer0 | Final independent review after quick checks | Complete committed range, final diff, history and migration conclusions |

## Next actions

- Prepare registered HaveAPI worktree and accept architect design.

## Documentation

## Repositories

## Commands run

## Results

## Open questions

- Exact scope of Rust normalization reuse and safe request-local cache ownership.
- Appropriate synthetic description size and stable regression budgets.

## Cleanup
