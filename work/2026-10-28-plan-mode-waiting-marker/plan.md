# Plan mode waiting marker

## Goal and scope

Investigate and fix the missing browser-tab waiting marker when Codex in Plan
mode asks a question and waits for the user's answer. Preserve existing markers
for running, approval, idle and error states and clear waiting promptly when the
question is answered or no longer pending.

## Affected repositories and approach

The likely owners are codex-web (Codex request/status browser integration) and
dev-workspace (portal document title). Architect0 will trace the existing request
to title path in their canonical repositories and establish the smallest owning
change before implementation. Only repositories proven necessary will be edited.
One implementer will own the bounded fix, regression coverage, quick checks,
technical explanation if useful, commit and feature publication. Reviewer0 will
independently review the committed complete branch after quick checks.

## Compatibility and deployment

Prefer existing pending-request state and title semantics, with no new protocol,
persisted state, database migrations or coordinated server upgrades. Confirm
mixed-version behavior and rollback in the design. No merge or deployment is
authorized by this request; prepare a reviewed published feature branch.

## Documentation

Readers are maintainers of Codex browser status and the portal title. Preserve
root cause and verification in design.md and state.md. Add a code comment or
owning-project explanation only if it conveys a non-obvious lasting invariant.

## Acceptance and checks

- Pending Plan mode user input receives the existing waiting title marker.
- Answering, resolving or cancelling clears the pending waiting state correctly.
- Approval precedence and ordinary working/idle/error titles remain correct.
- Exercise the real event/status/title boundary in focused regression coverage.
- Pass repository-required quick checks, independent final review and applicable
  broader checks/CI; use fresh verification utilities for long/uncertain checks.

## Owners and dependencies

- Architect0: investigation and design.md; prerequisite for implementation.
- Implementer0: one complete fix package once the design boundary is accepted.
- Reviewer0: final independent review once all intended changes are committed.
- Lead: scope, acceptance inspection, tracking, check/review coordination, handoff.
