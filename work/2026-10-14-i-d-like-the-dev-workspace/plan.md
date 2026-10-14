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
- `workspace`: nested runtime selection for user-profile application deployment.
- `vpsfree-cz-configuration`: matching devWorkspace channel and aitherdev system
  deployment. User authorizes implementation, verification and aitherdev deployment
  using this configuration; no default-branch integration is authorized.

## Approach

- Full-team architect `architect0` owns the proposed design and verification
  brief in `design.md`; lead reconciles it with the user's request and source.
- Propose compact attention and persistent reservation markers, explicit visit
  acknowledgement, browser notification opt-in and per-session controls.
- Define human-attention events separately from automatic waits and session
  lifecycle completion, with deduplication and stale-status handling.

## Decisions

- User accepted the proposal and requested implementation and verification through
  completion, and authorized aitherdev deployment using vpsfree-cz-configuration.
  Complete committed code and quick checks before independent final review, then
  long verification and coordinated deployment. Preserve master merge gate.
- Keep the session open and its lifecycle active for follow-up.
- Lead recommendation uses the architect's compact `R`/`R2` alternative for
  machine reservations, avoiding confusion with browser HTTPS lock indicators.
- User rejected open-session-page-only notification delivery. Notifications must
  work while the user is elsewhere, without relying on a running session page,
  or be omitted. Revised proposal uses server-side observation and Web Push via
  a service worker, subject to an actual browser/OS feasibility check.
- Targets confirmed by user: Firefox on macOS and Chrome/Chromium, minimized or
  unfocused (not fully quit). Standard Web Push/service worker/Notifications APIs
  address this case. Acceptance includes no portal tabs open while browser runs.
- Chromium builds must have a working push service. Setup must check actual
  subscription support and offer a test notification; unsupported builds report
  that limitation rather than presenting page-dependent delivery as equivalent.
- Recommend per-session notifications enabled by default, gated by an explicit
  browser permission action. No installed PWA or browser-specific implementation
  is needed for this target. Fully quit browser delivery is not required.
- Test notification sends after a fixed 10-second delay, allowing the user to
  close portal tabs or switch windows before delivery. This is test UX, not a
  configurable reminder or snooze mechanism.
- Unread title attention persists until a visit or superseding/resolving work.
  Push delivery TTL bounds desktop freshness only; it must not silently clear
  the title's unread completion marker while the session state is unchanged.

## Compatibility and deployment

- Reuse current identity-bound session and reservation authority. Display or
  acknowledgement must never answer requests or release reservations.
- Prefer additive private portal state over lifecycle/manifest format changes.
- Creation request's optional `browserNotificationsEnabled` also requires Ruby's
  strict captured-receipt allowlist to accept this boolean. Old omitted receipts
  remain supported; new flagged receipts require the capable bundled helper.
  Forward-only package selection and creation/package-transition fencing define
  the supported pairing. Do not add an extra receipt-preference framework solely
  to make an older helper recover newly flagged requests.
- Record browser permission, closed-browser delivery limits, mixed-generation
  behavior, rollout and recovery in the architect's proposal.

## Documentation

- Readers: portal user deciding behavior, future implementer and reviewer.
- Current proposal: this session's `design.md`; status/evidence: `state.md`.
- Accepted implemented behavior would belong in dev-workspace's portal guide.

## Testing plan

- Investigate existing title, activity, pending request and reservation paths.
- Specify meaningful browser and server acceptance checks in the proposal.
- Run focused reducer/browser contracts and Go/store/transport tests first.
- After committed final review, run packaged suite and background worker/browser
  integration checks under a fresh verification watcher, then deployment checks.
- Distinguish automated service-worker/push-provider verification from actual
  Firefox/macOS and Chrome/Chromium OS display on the user's computer; expose
  browser opt-in and a test action rather than claiming remote OS observation.
