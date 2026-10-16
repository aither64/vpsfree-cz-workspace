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
- Verification found ambiguous pre-existing descendant-exit observation. An
  architect-scoped test-only correction now uses one identity-aware bounded wait,
  fails unknown observations closed and preserves safe failure context. Production
  cancellation remains unchanged; original causes remain unproved. Independent
  affected/history/composition reviews and final exact6e1 fullflake/CI passed.
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

## Accepted provider/disable amendment

Real headed unbranded Chromium147 issues jmt17.google.com subscription URLs.
Official matching-version constants/channel selection confirm the staging
provider for nonstable/UNKNOWN channel. Add that exact host under existing
transport guards; no suffix or arbitrary provider endpoint support.

Disable must attempt local unsubscribe independently from server cleanup. An
optional strict endpointDigest on existing disable API enables deletion without
re-registering a refused/lost-ID subscription. Retain one bounded ID/digest
cleanup selector locally until server absence confirmed, report pending outcome
accurately, and verify local absence. No raw endpoint/keys in local cleanup
receipt, no new persistent server schema or general cleanup framework.
Affected API/provider/security review follows committed quick checks before
real-provider/full-package rechecks. Architect owns design.md addendum.

Evidence/limits: actual Firefox Mozilla acceptance plus worker receipt with
zero portal tabs verified on Linux/Xvfb; OS/macOS display unverified. Actual
Chromium acceptance remains pending amendment. Original deployment jobs were
canceled unadmitted; no live activation by this session.

## Recovery verification follow-up

Final b8a6 full local flake verification failed in the unchanged provider-recovery
VM. A single exact-package fixture-only diagnostic passed with complete observer
coverage and no matching raises; the original discarded forward/recovery errors
remain unavailable. Preserve both results; do not infer a notification cause or
repair from non-reproduction. See recovery-check-investigation.md and
recovery-diagnostic/run/result.json.

Lead accepts the architect's bounded owning-provider observability improvement
as necessary verification work: safe failure-only diagnostics, plus prompt
unexpected-terminal-failure reporting and bounded fixture evidence in the
existing recovery VM. Architect records the accepted scope in design.md before
implementer0 edits the four owning Ruby/test/VM/docs paths. Preserve ownership,
service order, readiness deadlines, retries, fencing and all state formats;
no speculative provider behavior change or general diagnostics framework.
Quick checks, main-agent prose pass, committed affected independent review and
fresh watcher verification precede publication/composition refresh/deployment.
This repairs missing diagnostics, not the still-unproved original failure.

## User feedback after deployment

Move the index Browser notifications panel behind the existing workspace menu,
like Operations and Automatic archival, and add spacing between Enable/Test/
Disable. Investigate Firefox/macOS missing test notification: user sees the
ten-second queued message but no visible notification with page open or elsewhere.
Do not treat provider or worker receipt as physical display acceptance. Architect
owns bounded evidence/design, implementer owns edits, lead owns copy/review/
verification/redeployment under the existing reservation. Deployed6e1 state is
now a supported consumption boundary; preserve its formats and cleanup paths.

## New/refreshed notification clients (2026-10-15)

User refuses closing all portal tabs for a notification worker update. Latest
direction: old-tab notification compatibility is not required; notifications
must work on new/refreshed tabs while other tabs remain open. Architect0 owns
a bounded design addendum; implementer0 owns application edits from that brief.
Lead owns copy, coordination and deployment.

Acceptance: successor notification worker activates without closing other
controlled tabs; new/refreshed page obtains current behavior. No page-close or
automatic-reload workflow. Preserve subscriptions, permission and private session
state; no unregister/resubscribe workaround. Remove close-tabs update guidance.
A narrow real-browser regression should keep an old controlled tab open through
successor activation and prove the new/refreshed page uses the successor.
Quick actual-module/static checks and committed independent affected review
precede the longer browser check. Deployment stays under the existing approval
and reservation, branches remain unmerged.

This fixes the update barrier; it must not be represented as causal proof of a
physical Firefox/macOS display repair. Keep the exact4ed Linux UnknownError
rejection and successful scoped cleanup as preserved evidence.

## Browser notification sound preference (2026-10-15)

User now confirms actual Firefox/macOS popup works; wants choice of audible or
visual-only notifications. Per-browser controls own this setting across session
and Test notifications, including backgroundworker operation. Default preserves
existing OSdefault soundallowed behavior; visualonly uses native silent option.
NativeAPI cannot force audible output when OS/browser mutes it. Current Firefox
support documented since132; no synthetic audio workaround is planned.
Architect0 records minimal persistence/display/verification brief; implementer0
owns source after leadrelease; mainowns actualcopy pass. Preserve subscriptions,
permission, keys, sessionstate/ACK and cleanup obligations. New owning eighth
commit after consumed469; preserve prior7objects/receipts/evidence.
Quick actualmodule/store checks and committed affected independent review
precede meaningful browser tests, then published matching consolidated consumer
pins/compositiongate and authorized coordinated rollout. No defaultmerge,
reservationrelease or lifecycle authorization.

## Notification click focus investigation (2026-10-15)

User first described another tab, then directly rechecked: a likely Response
finished notification brings Firefox forward without selecting the relevant
session tab. Use corrected observation. Architect owns bounded read-only
inspection and minimal design/verification brief. Lead accepted focus-only
reuse of an existing same-origin session tab (strict optional trailing slash),
preferring target member when several exist. Preserve its current document/draft,
section/member; do not navigate before focus, add a protocol, or claim this proves
the user incident cause. Canonical authenticated navigation with attention identity
remains for no-existing-tab; user confirms that case already works. Separate ninth
owning commit after sound eighth; both complete/quick checked before final review.
Preserve ordinary authentication, ACK and identity fencing. Sound preference
implementation continues independently.

Sound UX clarification: quick workspace-menu on/off is required across the
current browser's workspace notifications, independent of per-session delivery.
One persisted preference and one shared control owner serve menu and fullpanel;
no separate mirrors or changing session mutes. Architect addendum precedes
extension; final copy/quick checks/commit/review encompass this final scope.
User also confirms the click-focus failure involved tabs in the same window.

Global controls extension: user also requests quick desktopnotification disable
across sessions while title updates always continue. Preserve title attention
observation/ACK independently and each session's own delivery setting. Prefer
reusing existing browser Enable/Disable and cleanup with honest incomplete-state
UX; avoid adding a server pause flag merely to duplicate existing controls.
Index/menu initialization must not request permission or subscribe/test without
an explicit action. Architect updating final brief; eighth not committed yet.

## Accepted compact-menu follow-up

User requested two menu checkboxes, Notifications and Sound, with other controls
and guidance on the dedicated settings page. User selected brief error in menu,
then explicitly instructed: Implement the plan. Keep a small Notification settings
link. Reuse existing shared action/state owner, committed-state rendering and
cleanup fences; disable competing actions, represent unknown delivery honestly.
Sound stays independently editable with desktop notifications off; title and
per-session behavior stays unchanged. No API/protocol/storage/worker-click changes.
Architect0 records bounded design; implementer0 edits; lead approves visible copy;
reviewer0 reviews complete committed deliverable/history before long checks.
Keep all nine deployed1038 objects untouched; add focused tenth commit. Quick
contracts/template/syntax/diff then independent review, finite two-engine fixture,
package/CI verification, matching consolidated consumer selections/composition
review, exact preparation and authorized ordered aitherdev activation. Preserve
deployed1038/653/2df refs and all existing evidence/state. No migration, merge,
reservation release or session lifecycle action. Existing native acceptance limits
remain version-bounded and are not explained by this UI simplification.
