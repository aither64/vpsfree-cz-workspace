# 2026-10-24-workspace-session-ui

## Goal

some issues in the dev-workspace portal:

- session settings page mixes up checkboxes with on/off sliders. the sliders are actually nice, let's use them instead of checkboxes
- codex output shows the "New output" button even when none is visible. I imagine that it doesn't consider filters -- I usually look only at messages and I guess it considers tool calls or team messages as new output, which isn't shown in reality.
- after sending a message to codex, I can't send another message until the first message is accepted by codex -- the submit buttons are disabled. I think I should be able to queue multiple messages/steers.

suggest a solution.

## Affected repositories

- `dev-workspace`: portal session settings and prompt submission integration.
- `codex-web`: inspected shared delivery/queue contracts; no changes proposed.

## Approach

The user approved implementation, then added a fourth issue: keep routine
"Checking queued messages..." checks silent and reuse the shared refresh
timeout/policy. Architect `architect0` owns the design amendment; the lead owns
scope, acceptance inspection, tracking and user-facing writing. Implementers
own implementation, quick checks, commits and follow-up fixes. Integration and
deployment require separate direction.

Inspect canonical repository refs read-only and identify the smallest fixes for
consistent switches, filtered-output notifications, and multiple queued prompts.

## Decisions

- Prefer the existing switch appearance for binary session settings, retaining
  accessible controls and existing persistence semantics.
- New-output notifications should reflect content visible under active filters.
- Reuse existing prompt queue and delivery semantics where possible.
- Accept repeated immutable submissions in the browser and dispatch them in
  order, retaining each submission's Send/Steer versus Queue next intent and
  durable identity. Pause dispatch and reconcile on uncertain results.
- Implementation is authorized by the user's "implement it" followed by the
  additional queue-refresh requirement. Default-branch integration and
  deployment are not authorized.
- Routine queue checks should be silent, retain last confirmed content and
  surface actionable failures through the existing shared refresh policy.

## Compatibility and deployment

The design must identify whether browser-only changes suffice or server/API
changes are needed. Preserve existing settings, prompt ordering, persistence,
and retry behavior; do not introduce a state-format change without justification.
No deployment is planned for the proposal phase.

## Documentation

Readers: the user deciding the scope and implementers taking the resulting
packages. Keep proposal rationale and verification cases in `design.md`, current
progress in `state.md`; lasting project documentation is assessed during any
later implementation.

## Testing plan

Use focused browser and relevant Go quick checks for switches, filtered unread
tracking, repeated submissions, ordering/recovery and silent queue refresh.
Complete and commit the intended implementation before mandatory independent
final review. Run packaged/native longer checks after review through a fresh
verification watcher. Publish only the feature branch, monitor applicable CI,
and leave integration/deployment pending.
