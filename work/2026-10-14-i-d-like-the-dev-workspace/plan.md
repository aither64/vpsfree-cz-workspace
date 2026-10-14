# 2026-10-14-i-d-like-the-dev-workspace

## Goal

I'd like the dev-workspace portal to change page titles of individual sessions, so that it'd be clear when a session is waiting for user input or is done. This marker could be removed after the user visits the window. Similarly, it could mark sessions that are holding machine reservations. These markers should be compact so that I can still read session name.

And, well, we could integrate with browser notifications, so that the portal would be able to send a notification for the same condition of being done or needing user input. I should be able to turn notification off per-session, put this in session settings and session creation form.

Suggest a solution.

## Affected repositories

- `dev-workspace`: portal titles, session settings/creation, observation and
  reservation integration. Inspect canonical bare clone read-only for this proposal.
- `codex-web`: existing activity/pending contracts are a dependency; change only
  if investigation finds a reusable missing capability.
- No application edits, branches, deployment or integration are requested yet.

## Approach

- Full-team architect `architect0` owns the proposed design and verification
  brief in `design.md`; lead reconciles it with the user's request and source.
- Propose compact attention and persistent reservation markers, explicit visit
  acknowledgement, browser notification opt-in and per-session controls.
- Define human-attention events separately from automatic waits and session
  lifecycle completion, with deduplication and stale-status handling.

## Decisions

- This task is a suggestion/design phase only. Implementation and final review
  remain future work; routine planning does not trigger automatic review.
- Keep the session open and its lifecycle active for follow-up.

## Compatibility and deployment

- Reuse current identity-bound session and reservation authority. Display or
  acknowledgement must never answer requests or release reservations.
- Prefer additive private portal state over lifecycle/manifest format changes.
- Record browser permission, closed-browser delivery limits, mixed-generation
  behavior, rollout and recovery in the architect's proposal.

## Documentation

- Readers: portal user deciding behavior, future implementer and reviewer.
- Current proposal: this session's `design.md`; status/evidence: `state.md`.
- Accepted implemented behavior would belong in dev-workspace's portal guide.

## Testing plan

- Investigate existing title, activity, pending request and reservation paths.
- Specify meaningful browser and server acceptance checks in the proposal.
- No builds, tests or runtime changes are necessary for this planning phase.
