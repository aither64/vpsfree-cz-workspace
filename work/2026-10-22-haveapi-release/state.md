---
lifecycle: active
---

# 2026-10-22-haveapi-release

## Status

- Phase: release-process audit and design.
- Verified `dev-session current` and both environment markers against this
  conversation's exact session/workspace binding.
- Retained Full team: architect0 owns investigation/design; implementer0 and
  implementer1 will own execution packages; reviewer0 is reserved for final review.

## Next actions

- Accept architect's release audit and design, then assign independent packages.
- Prepare a published release branch, review it, verify artifacts and hand off
  exact pending trusted-publisher settings and release steps.

## Phase checklist

- [x] Verify session identity and retained roster/access.
- [ ] Audit release processes and write design.
- [ ] Prepare release metadata/workflows/documentation; commit and quick-check.
- [ ] Complete independent whole-branch review.
- [ ] Complete release dry-runs and applicable longer verification.
- [ ] Hand off prepared release and remaining registry/integration actions.

## Backlog

| Owner | Expected result | Acceptance / checks | Dependency |
| --- | --- | --- | --- |
| architect0 | Release audit and design | Exact packages, workflows, environments, bootstrap order and compatibility | None |
| implementer0 | Version/artifact preparation | Aligned metadata and package checks; committed changes | Design |
| implementer1 | Release-process preparation | Correct documented workflow and publisher requirements; quick checks | Design; independent boundaries |
| reviewer0 | Independent final review | Final diff, history and migration conclusions | All commits and quick checks |

## Documentation

## Repositories

- `haveapi`: worktree and branch pending audit; no integration approval.

## Commands run

## Results

## Open questions

## Cleanup

- Leave session open. No lifecycle actions authorized.
- Preserve unrelated shared workspace changes and retain feature refs.
