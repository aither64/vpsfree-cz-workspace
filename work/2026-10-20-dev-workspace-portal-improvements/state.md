---
lifecycle: active
---

# Portal improvements

## Current phase

Design and diagnosis. Session identity and retained roster verified. No source
changes, deployment or merge has been performed.

## Phase checklist

- [x] Verify session identity, scope and team access.
- [ ] Architect design and implementation boundaries.
- [ ] Both implementation packages, technical docs and quick checks.
- [ ] Commit inventory and mandatory independent final review.
- [ ] Long verification and published feature branches.
- [ ] Deployment if requested; integration only with explicit approval.

## Backlog

| Owner | Expected result and acceptance | Dependencies / checks |
| --- | --- | --- |
| architect0 | Diagnose all reported behaviors; design.md covers interfaces, compatibility, recovery and complete packages | Read current sources and docs; no application edits |
| implementer0 | Reliability and portal UI package, exact boundary pending design | Architect brief; targeted checks and commits |
| implementer1 | Shared conversation presentation package, exact boundary pending design | Architect brief; targeted checks and commits |
| reviewer0 | Final correctness, security, history and migration conclusions | Completed committed deliverable and passing quick checks |
| lead | Tracking, acceptance, wording, resource coordination and handoff | Assess member reports; keep selected runtime usable |

## Repositories

Planned: dev-workspace and codex-web. Worktrees and exact heads pending design.

## Evidence and risks

- `dev-session current` returned this exact slug; both environment markers match
  the trusted workspace/session binding.
- Full-team retained roster: architect0 (design, workspace_write), implementer0
  and implementer1 (implementation, workspace_write), reviewer0 (review,
  read_only); all ready. Saved models/efforts retained.
- Submission 502 root cause is unconfirmed. Avoid automatic retries until
  idempotency and durable acceptance behavior are established.
- Shared workspace contains extensive unrelated changes; preserve them and stage
  only this initiative's tracking files under the tracking lock and claim.

## Documentation and next action

Architect owns design.md and package boundaries. Lead prepares initial tracking
commit before project-code commits or external mutation. Project docs will own
lasting behavior; session artifacts will retain verification and review evidence.
No deployment or lifecycle action is authorized by completing this work.
