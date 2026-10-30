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

## Accepted design

See [design.md](design.md). Confirmed scope: codex-web activity-request identity
projection and dev-workspace attention consumer plus exact dependency pins.
Reuse existing recorder state; preserve passive observers and acknowledgement.
Implementer0 owns the serial cross-repository package. No database migrations;
optional schema-1 identity metadata and HTTP snapshot field require explicit
compatibility review. Independent review will include all four applicable lanes.

## Verification sequence

Focused provider/passive and portal checks plus 75-case browser harness passed.
Validate exact downstream vendorHash, commit all intended changes, then
reviewer0 reviews the complete branch ranges and four applicable lanes. After
review reconciliation, lead assigns one fresh Luna/low utility for required
packaged flake checks and exact-head CI observation. Source fixes remain with
implementer0; do not broaden native release or live deployment scope.

## User-added deployment milestone

User steering: "aitherdev can be deployed using vpsfree-cz-configuration"
(current conversation, after source publication while final review runs).
Prepare and execute aitherdev deployment through the configuration-owned
procedure after review and checks, keeping separate explicit merge approval.
Architect0 owns bounded deployment/composition addendum; implementer1 will own
necessary config/workspace pin preparation after contract stabilizes. Lead owns
activation coordination and machine claim. Read selected package coordination
guide and preserve forward-recovery/continuity contracts. No default integration
is authorized by this deployment steering.

## Delivered outcome

Implemented the passive request identity projection and paired attention consumer,
with regressions and independently reviewed published branches. Added a separate
bounded diagnostic fixture commit after local hydration timeouts; original
acceptance and production target stayed unchanged. Verification is reconciled in
verification.md, including successful exact CI reuse, diagnostic archive and
recovery acceptance. System and user-profile deployment on aitherdev completed
and effects verified; rollout.md owns exact paths, inputs and recovery/ownership.
User subsequently approved "ok, merge and release aitherdev". All four reviewed
final heads are integrated into remote master, with fresh ancestry evidence.
Aitherdev reservation was released and independently status-verified. Keep the
session open; post-merge CI reconciliation is the final remaining gate. Optional real browser Plan-question smoke and positive naming canary
are explicitly distinguished from automated/artifact/health verification.
