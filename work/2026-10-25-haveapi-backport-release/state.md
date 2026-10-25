---
lifecycle: active
---

# HaveAPI 0.30.2

Current phase: investigation and release design.

## Phase checklist

- [x] Verify exact session identity and ready retained roster.
- [ ] Architect inventory, compatibility assessment and design.
- [ ] Backport all applicable master changes and release metadata.
- [ ] Quick checks and complete committed-history inventory.
- [ ] Independent final review.
- [ ] Longer verification and branch CI.
- [ ] Publish authorized 0.30.2 release and verify external results.

## Backlog

| Owner | Expected result | Acceptance and dependencies |
| --- | --- | --- |
| Architect0 | design.md and full master/0.30 coverage | All changes classified; compatibility/release procedure; first |
| Implementer0 | Functional backport with tests/docs | Design accepted; hooks and quick checks pass |
| Implementer1 | Independent release preparation | Architect boundaries; no overlapping Git mutations |
| Reviewer0 | Final review | Committed complete deliverable and quick checks; explicit history/migration conclusion |
| Lead | Release coordination and receipts | Review/check gates; exact target authorization |

## Identity and scope

`dev-session current` returned `2026-10-25-haveapi-backport-release`; both
DEV_SESSION environment values match the trusted thread binding. HaveAPI only.
Roster ready with saved write access for architect0/implementer0/implementer1;
reviewer0 retains read-only instructions. Architect investigation assigned.

## Verification and release evidence

Pending design. No project changes or publications yet. No machines reserved.

## Risks and next action

Exact maintained branch, master delta, release conventions and publication access
remain to be established by architect0. Lead will commit initial tracking and
assign complete execution packages when the design is ready.
