# 2026-10-05-review-pull-request-premise

## Goal

I'd like you to review pull request https://github.com/vpsfreecz/vpsadminos/pull/91 with our mandatory change review skill + check that the premise is actually true and the approach taken to fix it is the right one.

## Affected repositories

- vpsadminos PR #91, targeting `staging`, head
  `477d063b7b70a850188c8a2a550d6066d1c7d801`.
- Coordination workspace: review records only.

## Approach

Review the complete committed PR using mandatory-change-review. Independently
trace `make qemu` to `Machine#join`, reproduce the parent failure, and compare
the fix with timeout and kernel-failure semantics. Inspect focused specs and
actual consumers. Use one temporary independent reviewer selected from the
installed catalog; Solo lead owns investigation and evidence.

## Decisions

- Scope is assessment, not implementation, publishing a GitHub review, merging,
  or deployment. Do not rewrite the submitted branch.
- Review general, architecture, scope, and risk/compatibility lanes because this
  code controls host-side QEMU waits and kernel-failure propagation.
- No substantive implementation is planned, so no separate design is needed.

## Compatibility and deployment

Check finite and unlimited wait contracts and existing consumers. Determine
whether changes affect persisted state, protocols, packaging or rollout order.
No system deployment or live VM mutation is required for this review.

## Documentation

Readers: PR maintainer and future reviewers. Keep review packet, findings,
reproduction evidence, and limitations in this session; inspect relevant
vpsAdminOS development documentation without changing product docs.
Apply dev-session-documentation and dev-session-handoff.

## Testing plan

- Quick: complete diff/history inventory, diff whitespace check, syntax and
  deterministic reproduction without booting QEMU.
- Independent review of the exact committed head before longer verification.
- Focused RSpec and optionally the complete osvm suite in the declared Nix
  environment; delegate uncertain-duration runs to the monitor skill's utility.
- Acceptance: supported conclusion on premise, fix correctness/proportionality,
  compatibility and whole-branch history, with concrete findings and test gaps.
