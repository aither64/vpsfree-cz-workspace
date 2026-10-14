# Session title markers and browser notifications

Status: IMPLEMENTATION BRIEF, 2026-10-14. The user authorized implementation,
verification and deployment to aitherdev using vpsfree-cz-configuration. Master
integration and session lifecycle actions are not authorized. Architect ownership
is limited to this design; the lead assigns application changes to the retained
implementer and owns verification/deployment coordination. Background notification
delivery must work without an open portal page.

## Accepted behavior and examples

Prefix the existing session title with at most one attention marker and one
reservation marker. Keep the full session name and existing suffix.

| Example | Meaning |
| --- | --- |
| `? api-cleanup · Workspace` | An unseen blocking answer or approval request |
| `✓ api-cleanup · Workspace` | The lead finished a response and the team is idle |
| `R api-cleanup · Workspace` | This session holds one machine reservation |
| `? R2 api-cleanup · Workspace` | Unseen input request; two distinct machines reserved |
| `✓ R api-cleanup · Workspace` | Response finished; the machine remains reserved |

Input takes precedence over completion. A visit clears attention, while the
reservation marker remains until a successful coordinator read confirms release.
Explain the symbols in Settings and expose their full meaning in the page's
status text. The existing Reservations tab supplies machine names and reasons.
Use `R` for one held machine and `R2`, `R3`, etc. for the distinct machine count.
This is the accepted reservation notation; do not use a lock glyph.

“Done” means the current response has finished. It does not certify that the
initiative is merged, reviewed, deployed or complete. It never changes lifecycle.

## Authoritative signals and team aggregation

- Input comes from an outstanding, actionable blocking question or approval
  belonging to the lead or a ready retained member of this exact session.
  Use normalized pending-request identities and current native activity.
  `waitReason: userInput` or `approval` can identify the category; a generic
  `waiting` state cannot. Sleep, automatic team waits, disconnection, ordinary
  idle time and optional nonblocking questions do not trigger this marker.
- Completion requires a positively identified successful completed lead turn,
  no newer lead turn, no unresolved blocking request anywhere in the ready team,
  and fresh evidence that every ready member is idle. An active, sleeping or
  automatically waiting member defers completion. Unknown or stale team state
  also defers it. Member completion alone never creates a completion event.
  A deferred lead completion can become eligible when the team settles; key it
  to that same lead turn so it cannot notify again. Interrupted or failed turns
  keep their existing error/status presentation and do not receive a success tick.
- The title describes the session regardless of the member currently selected
  in the Codex panel. Input notifications identify the member and link to its
  existing conversation route; completion links to the lead.
- Reservation ownership comes from the coordinator's complete
  `reservationHolders` summary, matched by workspace, slug and exact
  `observationIdentity`. Count distinct held machines, including review and
  recovery holds. Pending requests and temporary execution claims do not count.
  Neither conversation completion nor visiting the page releases a reservation.

Use structured state, not assistant prose, lifecycle-looking Markdown, a final
message alone, a disconnected stream, or a job's successful exit as a completion
signal. A first snapshot of an old idle session establishes a baseline and
does not manufacture a completion notification.

## Visiting, unread state and browser scope

A visit means this session document is visible (`visibilityState === "visible"`)
and its window is focused (`document.hasFocus()`). Any panel within the session
counts; the index and another session do not. A visit acknowledges only event
identities already observed, including fresh events received while still focused.
It cannot acknowledge an event arriving after focus is lost. Unresolved requests
remain visible in the page after the title marker clears.

Store acknowledgements in versioned origin-scoped IndexedDB, keyed by workspace,
session incarnation and root thread, shared with the service worker. Broadcast
changes to matching tabs. Acknowledgement changes presentation only: no request
answer, reservation release or lifecycle mutation. Another browser profile,
device or portal hostname has separate unread state and permission. Reload
retains acknowledgements; a replacement session with the same slug cannot inherit
them. A lifecycle move that changes observation identity starts a fresh baseline.
Resolved requests and superseded completions cease to be current attention.
Otherwise title attention persists until a visible, focused visit acknowledges
it; elapsed time or push expiry never clears it. The title/status projection
must retain current event identity independently of outbox delivery retention.

Title updates remain page behavior: a compact authenticated session snapshot
feeds a small controller independent of the selected Codex member or Reservations
panel. It may refresh in background tabs, subject to browser throttling. Failed
reads retain the same incarnation's last known reservation with a stale notice;
only a fresh, matching coordinator read proves release. Title timing is independent
of notification delivery. The service worker never attempts to edit page titles.

## Permission and per-session control

Keep **Browser notifications for this session** in creation and Settings,
defaulting on for existing and new sessions. Save it as a server preference so
muting a session applies to every subscribed browser. Title markers remain on.
Enabling this checkbox neither requests permission nor creates a subscription.
Re-enabling establishes the current baseline and does not replay muted events.

A separate **Enable browser notifications** action requests permission, registers
the portal's service worker and calls `pushManager.subscribe` with
`userVisibleOnly: true` and the server's public VAPID application-server key.
Only an explicit click starts this flow. The same control reports enabled,
blocked, unsupported or registration failed, and offers **Send test notification**
and **Disable on this browser**. Denial links to browser site-permission guidance
without repeated prompts. Disabling removes the server registration and
unsubscribes locally; permission itself remains a browser setting. If server
removal fails, show the incomplete outcome and allow retry.

Subscriptions belong to one browser profile and portal origin, covering sessions
that its authenticated owner may access and that have notifications enabled.
The server derives owner/workspace scope from authentication, not posted IDs.
For the current single-operator portal, bind to that authenticated workspace
operator; do not invent a multi-user identity system. Give each browser install
an opaque registration ID. Repeated registration of the same endpoint for the
same owner is idempotent; reject reassignment to another owner. Server-side
session mute is distinct from per-browser subscription enablement.

Show only the session name, member when relevant, and a generic reason:
**Your answer is needed**, **Approval needed** or **Response finished**. No prompts,
commands, credentials or excerpts. Explain session-name exposure on lock screens
and reliance on the browser vendor's push service before enabling. No reminders,
reservation notifications, per-event controls or sound settings in this version.

## Background delivery architecture

Extend the existing server activity observer with a small event reducer and
persistent outbox. It observes the lead and ready members regardless of browser
connections, using the authoritative rules above. It never resumes stopped/held
threads to obtain notification status. The first valid observation, newly enabled
subscription, or uncertain observation continuity establishes a baseline; old
idle turns do not become completion events. Existing live event invalidations
and bounded reconciliation remain the source of truth.

Use stable event keys based on exact session/thread identity and the lead turn or
blocking request's native turn/item identity. Connection-local tokens and
`stateSinceMs` alone are insufficient. Persist observation baselines and pending
outbox entries atomically so a portal restart neither replays a completed turn
nor loses a newly committed event between those writes. If a stable request key
is missing, expose the minimal generic field in codex-web. Do not add a parallel
transcript recorder or general messaging service.

The server's bounded background sender checks current ownership, subscription,
session mute and event relevance before each send. It encrypts the payload using
the subscription's `p256dh`/`auth` material and authenticates the Web Push request
with the retained VAPID key. Use a maintained Web Push library rather than new
cryptography. Browser-provider acceptance means queued by that provider, not
shown to the user. The portal need not be publicly reachable by the provider:
ordinary Web Push sends outbound to the subscription endpoint. Browser access
to the private portal is still needed for registration, fresh validation and clicks.

A payload carries a schema version, event ID, session incarnation, monotonic
session event revision, expiry, minimal display data and a same-origin relative
conversation route. Coalesce pending work per browser/session to the current
highest-priority event; input supersedes completion. New lead activity cancels
an unsent completion. Proposed TTLs are five minutes for completion and fifteen
minutes for input, bounded by delivery expiry. These TTLs bound push delivery
and retries only; they do not expire unread title attention or its current-state
projection. Use the provider's Web Push Topic
and the browser notification tag to replace older messages for the same session;
local revision checks remain necessary because providers can reorder messages.

Retry network errors, 429 and transient server errors with capped backoff and
Retry-After within the original expiry. Expired subscriptions (404/410) are
retired; other permanent errors surface in Settings without a retry storm.
Retain the same event ID across uncertain sends. Provider delivery can duplicate.
The worker records the latest event/revision in IndexedDB and uses one session
notification tag with `renotify: false`; a repeated or superseded delivery
replaces that notification rather than creating another notification entry.
Bound stored history and outbox size; coalesce or drop expired work before send.
A worker crash can lose a display; no exactly-once guarantee is claimed.

Suppress at the server before sending. A visible, focused session page can publish
a short-lived, authenticated presence lease for its own browser registration and
report which event it actually displayed. Defer that browser's push while the
lease is fresh; suppress it once the focused page confirms the event. If the
lease expires without confirmation, send the still-relevant event. Presence is
optional, ephemeral delivery metadata, not a new shared unread-state authority;
it never answers a question or changes session/reservation state. A browser with
no open portal page needs no presence lease to receive pushes.

Every valid incoming push is handled with `event.waitUntil` and a visible
`registration.showNotification` call. Do not depend on silent push for foreground
suppression, stale-event cancellation, deduplication or periodic checks. Once the
provider accepts a push, it cannot be reliably recalled. A bounded authenticated
status read, when available without a tab, can update its display to current
state; if resolved, expired, muted, superseded or unverifiable, display neutral
**Session update available** rather than claim an obsolete completion or answer
request. A known deleted/inaccessible session uses **Workspace update** without
session details. Never overwrite newer locally known state with an older payload.
Use the same session tag for replacement and close a notification when a live
page acknowledges it. A foreground or mute race can still yield one visible
notification; short TTLs and neutral copy limit its impact. This is the explicit
tradeoff for portable user-visible Web Push behavior.

On notification click, close that notification, validate its route against the
portal origin and session route grammar, then focus/navigate an existing matching
window or call `clients.openWindow`. Authentication remains the ordinary portal
flow. Acknowledge only after the destination reports visible and focused; a click
alone is not proof that the user reached the session. A replaced or unavailable
session must show its normal missing/changed-session result, not another session.

## Persistence, trust boundary and provider dependencies

Keep VAPID private keys, subscriptions (endpoints are capability URLs), browser
registrations, preference records, baselines and outbox under the existing private
runtime state root, with versioned atomic writes, directory mode 0700 and file
mode 0600. They never belong in Git, session artifacts, browser logs or ordinary
request/error logs. Keep the VAPID key stable through package changes and back it
up with private runtime state. Lost keys require explicit browser resubscription;
planned rotation retains the old key for existing subscriptions until replaced.

Subscription create/update/delete and settings endpoints require the portal's
normal authentication, exact-origin/CSRF protection, bounded payloads and trusted
workspace/session resolution. Only the bound owner can change a registration.
Validate key lengths/encodings and subscription expiry. Recheck authorization
and exact session ownership when selecting recipients, not only at registration.
Subscriptions are workspace/browser resources; session mute is incarnation-bound.

A subscription endpoint is untrusted outbound input and must not become an SSRF
primitive. Allow only HTTPS on port 443 with no credentials, fragment or IP
literal, and exact supported provider hosts validated by the bounded prototype and acceptance
checks. Disable redirects. Reject loopback, private, link-local, metadata and
other non-public destinations after DNS resolution and at connection time;
protect against rebinding and avoid an unchecked proxy/dial path. Keep normal
TLS hostname verification, connection deadlines, response-size limits and
bounded concurrency. Do not accept arbitrary endpoints as a convenience for
new browsers. A new provider needs an explicit allowlist/configuration change.

Depend on outbound HTTPS from the host to the supported push provider and on the
browser/OS's own push connection. Providers may observe delivery metadata even
though Web Push encrypts payload contents. Secure-context trust, certificate
trust, private portal origin support and browser enterprise policies need actual
validation. Worker script and APIs stay same-origin with the portal's existing
authentication; do not expose an unauthenticated subscription/status API.

Serve a small root-scoped worker at a stable URL. It handles push and notification
clicks only: no fetch interception, offline shell, authenticated HTML/API caching,
or credential storage in IndexedDB. Use explicit asset/worker versions and
compatible payload schemas for old installed workers during rollout.

## Target browsers and acceptance evidence

Use the standard Push API, service workers and Notifications API for Firefox on
macOS and Chrome/Chromium. The target is a running browser, minimized or
unfocused, with all portal tabs closed. No separate Safari path or installed PWA
is required for this scope. Fully quit browsers are a non-goal; offline devices,
OS notification denial/focus modes and provider outages can delay, suppress or
expire delivery.

A bounded Web Push prototype and its acceptance checks are part of the already
approved implementation, not an additional approval gate. Develop the sender,
worker and **Send test notification** flow alongside the feature and validate
quick synthetic cases locally. Commit the intended substantive implementation,
pass quick checks, and complete mandatory independent final review before long
integration or live push proof. The lead can proceed with authorized deployment
and verification without first obtaining the user's browser permission.

Actual permission and subscription must come from the user's explicit browser
action. On the deployed portal, record the user's browser/version, macOS version,
notification settings and observed test result when available. The real-browser
check covers another site active, all portal tabs closed, browser minimized or
unfocused, and notification-click navigation through portal authentication.
Exercise host provider egress, browser push access and certificate trust.
Linux-host synthetic integration, provider acceptance and service-worker tests
do not prove macOS OS display. Keep the latter explicitly unverified until the
user confirms it or equivalent evidence from the target browser is available;
this outstanding evidence does not prevent authorized implementation/deployment.

Some Chromium distributions omit or disable the push service. Setup checks for
service-worker/Push API/Notifications support, successful subscription and an
actual **Send test notification**. A failure must distinguish unsupported build,
permission denial and network/provider error without claiming success. The
server cannot prove OS display from provider acceptance, so the user confirms
that the test appeared. If a build cannot provide useful background delivery,
report it unsupported; never substitute open-page polling. If evidence shows
that none of the user's chosen browsers can deliver, route that finding through
the lead and omit the unusable notification feature. Missing user confirmation
alone is an unverified acceptance item, not evidence of unsupported delivery.

Reference: [MDN Push API](https://developer.mozilla.org/en-US/docs/Web/API/Push_API)
describes waking a service worker for incoming push. The cross-browser design
must also respect user-visible delivery; [WebKit's Web Push guide](https://webkit.org/blog/12945/meet-web-push/)
provides a concrete reason not to rely on silent pushes. These are design
references, not evidence that the user's particular browser setup was tested.

## Implementation ownership, interfaces and files

Primary owner: `dev-workspace`. Investigated read-only at
`92b2576d82a850fa4e24f889a8ff592a1e7f3e42`, using its pinned codex-web revision
`5f15b9293f9b1eef7469a34d7b2044c743160283` (the bare clone's HEAD was older).
These are investigation references, not implementation bases. The implementer
must fetch current `origin/master`, use a same-session feature worktree, reread
current repository guidance and check current runtime/dependency interfaces
before editing. Do not force the historical revisions onto newer source.

| Area | Implementation boundary |
| --- | --- |
| `portal/internal/web/static/session-attention.js` (new), `app.js`, `coordination.js` | Page title reducer, snapshot refresh, local acknowledgements and worker messages; no desktop delivery loop |
| Session/index templates and creation/preparation flow | Checkbox, explicit browser enable/disable/test actions, permission/delivery state, retained draft |
| `portal/internal/web/attention.go`, `activity.go`, `server.go` | Read-only compact status projection and observer event reduction; stable source freshness and identity |
| New private notification store/sender and focused tests | Browser subscriptions, VAPID, event baseline/outbox, coalescing/retries, guarded provider transport |
| New service-worker asset and registration module | Push display, bounded current-status validation, IndexedDB deduplication, coalesced visible display and safe click route |
| Existing creation receipts and notification preference storage | Capture optional strict-boolean `browserNotificationsEnabled`; preserve explicit false on retry; Settings updates the normal notification preference record |
| `docs/workspace-portal.md`, operations guidance | Feature semantics, provider prerequisites, key/subscription recovery, worker update and disable procedure |

Use existing atomic store patterns; keep preferences out of strict `portal.yml`
schemas shared by Ruby and Go. Capture the optional boolean directly in the
existing accepted creation request/receipt. Creation retains the checkbox before
the session becomes observable and retries initialize the normal notification
preference record idempotently. Do not add a separate creation-preference sidecar
framework merely so obsolete helpers can read new receipts. A failed or
partial creation cannot emit completion. New forks and plan-derived sessions
start with the visible default-on choice and fresh event baselines; they inherit
neither unread acknowledgements nor outbox entries. Existing browser subscriptions
can receive their future events after readiness.

Archive, delete, explicit stop and recovery hold make new attention delivery
ineligible and cancel unsent session events; reservation markers still follow
coordinator ownership. Preserve the mute preference for the same retained
session through archive/revive, while revival rebaselines event delivery. Reused
slugs receive fresh preference/observation identity. Reconcile against lifecycle
and ownership authority; notification cleanup cannot trigger lifecycle changes.

Application scope remains dev-workspace. A small direct generic dependency field
change in codex-web is permitted only if current interfaces cannot provide the
required stable request identity; preserve optional/additive compatibility, add
focused tests and update its direct pins together. No browser vendor/push policy
belongs in codex-web. Route consequential design or dependency scope deviations
through the lead. Deployment composition also covers the workspace feature
worktree and vpsfree-cz-configuration as described below.

## Compatibility, deployment and recovery

Preserve the Codex/App Server version selected by current source, reservation
ledgers, native submission receipts and CLI behavior. Do not introduce an
unrelated Codex version change for this feature. No database migration or coordinated node update is
expected. Use optional versioned private notification files and the existing
creation receipt format with one optional request field. The supported reader
contract is explicit:

- Old receipts with `browserNotificationsEnabled` omitted remain fully accepted
  without rewrite or new required fields. Omission keeps the legacy request
  identity and means notifications enabled when initializing new preference state.
- New readers accept omitted, literal JSON `true` and literal JSON `false`.
  Preserve explicit false; reject null, strings, numbers, arrays and objects.
  Extend only the relevant request allowlist and strict-boolean validation;
  retain every existing identity, receipt, digest and unknown-field check.
- The new portal and Ruby helpers ship together. Older helpers cannot read a
  new receipt containing this field, and that is outside the supported recovery
  contract. Profile selection is forward-only; unfinished creations/forks retain
  their package-transition fence, and waiting commands recheck generation after
  the transition lock. Recover using the current generation or a compatible
  successor, not an older helper against newly captured state.
- Cover both `libexec/dev-session#validate_current_direct_portal_receipt!` and
  `libexec/workspace-host#valid_portal_managed_creation_request?`, as called by
  `validate_portal_direct_creation_receipt!`. The host scans and validates receipt
  shape before excluding ready/conflict receipts during package-transition
  inspection. Updating only the session helper would leave a concrete supported
  forward-update path rejecting completed new receipts. Keep the host's existing
  state/admission rules; only admit the optional well-typed field where captured.

Contract evidence: workspace lifecycle instructions require generation checks
under the transition lock; dev-workspace `docs/workspace-portal.md` sections
“User-profile state” and “Switching while Codex threads are active” specify
forward-only selection and retained unfinished-creation checks;
`docs/dev-sessions.md` section “Design and package compatibility” keeps unfinished
creations/forks with their originating generation. Source inspection confirms
`workspace-host` validates schema-3 request fields before its ready/conflict
filter. No supported rollback/old-helper recovery path requiring a new creation
sidecar was found. Implementer verifies these paths against current feature base.

Old browser requests remain valid. New browsers on an older server leave ordinary
conversation access intact and show unsupported notification controls accurately;
they must not claim that an older server saved the new field. A notification-state
failure stops sending, never erases a mute or fails open to default-on delivery.

The user authorized aitherdev deployment through vpsfree-cz-configuration. Prepare
and publish feature branches in these deployment composition repositories:

- `dev-workspace`: application/server/worker and the packaged feature; codex-web
  is conditional on the narrow generic-interface need above.
- `workspace`: dedicated same-session worktree for the nested runtime selection
  `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` and generated lock.
  Preserve the extension pin, siblings and follows relationships; update the
  nested input with `nix flake update vpsfree-dev-workspace/dev-workspace`.
- `vpsfree-cz-configuration`: existing confctl channel/role that selects
  `devWorkspace`, pinned to the exact published feature revision using the
  repository's channel tooling. Inspect its AGENTS.md and channel-to-input map
  first; do not hand-edit channel-owned lockfiles.

The workspace nested runtime and configuration `devWorkspace` must resolve to
matching runtime revisions. Run `bin/check-dev-workspace-deployment` against the
final workspace/configuration locks. The application is still activated from its
user profile; configuration provides the matching aitherdev host module/runtime
contract and must not install or iterate the application through system pins.
Record final revisions and prepared/executed rollout evidence separately.

Before activation, the lead reads the selected package's
`workspace-host coordination guide` and workspace coordination instructions,
then uses the authorized queue and machine reservation for the reviewed exact
snapshots. Build and copy outside execution claims; keep waits interruptible.
Validate provider egress, and place VAPID material in private runtime state outside
Nix/store. Preserve keys and compatible worker payload handling through upgrades.
No portal page or API response enters a worker cache. Deployment, branch
publication and passing tests do not authorize merges to any master/default
branch. Keep all feature branches, including configuration, unmerged until the
user explicitly directs integration; retain the machine reservation through
review under the coordinator's normal ownership rules.

Recover through a corrected successor package under the existing forward-only
selection policy. An operational notification disable stops the sender, cancels
unsent events and preserves subscriptions/keys/preferences for recovery; it does
not stop sessions. Decommissioning must unregister browser subscriptions and
retire the worker safely, since deploying old server assets cannot retract an
installed worker or a push already queued with its provider. Losing deduplication
state rebaselines rather than replaying old events. Losing keys requires explicit
resubscription; it cannot affect conversation or reservation ownership.

## Acceptance and verification brief

Quick synthetic proof and focused verification are part of implementation.
They do not require the user to grant browser permission. Quick checks use the
repository's Nix environment, existing browser-test patterns and focused Go tests
with `-mod=readonly`. Cover:

1. Exact title examples, input priority, same-browser focus-and-visibility
   acknowledgement, and persistent exact-identity machine markers. Advance beyond
   both push TTLs: unacknowledged current title attention must remain until
   focus acknowledgement or authoritative resolution/supersession. Stale holder
   reads, idle owners and recovery holds cannot imply release.
2. Blocking lead/member requests alert; sleep, team waits, optional input and
   unknown/stale states do not. Done requires successful lead completion and
   freshly idle ready members; failed/interrupted turns and member-only completion
   do not notify. First observation, resubscription and unmute do not replay idle.
3. Observer and outbox operate with zero browser clients. Restart at each
   baseline/outbox/send boundary, duplicate/reordered push, TTL expiry, newer lead
   activity, request resolution and mute/archive/delete races have defined results.
4. Explicit permission/subscription flow, per-browser disable and session-wide
   mute, retryable registration failure, ownership refusal, denied permission,
   subscription expiry and VAPID key preservation/replacement behave as specified.
5. Endpoint URL/key validation, private/non-public IP rejection, DNS rebinding,
   redirects, bounded retries and 404/410 retirement; logs never expose endpoint
   capabilities, keys or payload contents. Outbox failure cannot block Codex.
6. Service worker uses no authenticated-page/API cache, handles unknown payload
   versions safely, deduplicates through IndexedDB and falls back to neutral copy
   when freshness cannot be verified. The server defers delivery for fresh
   foreground presence. The worker shows a visible coalesced notification for
   each valid delivered push and rejects cross-origin click routes. Old workers survive package updates.
7. Creation receipt readers in both session and host helpers accept omitted,
   true and false values and reject malformed values; unchanged old receipt
   fixtures still pass without rewrite. Test new/plan creation paths and retry
   preservation of false, plus host transition inspection of completed flagged
   receipts and continued blocking of unfinished ones. Creation retries, forks,
   retained-session revival, slug reuse and access loss cannot inherit events or
   escape mute/ownership rules. Notification reads never
   resume stopped/held threads or answer requests.

After committed implementation and independent final review, run the packaged
suite and real-browser acceptance on Firefox/macOS and the actual Chrome/Chromium
builds: zero portal tabs, other sites active, minimized/unfocused browser, two
profiles, permission denial, network loss, expired portal authentication and OS
suppression. Fully quit browser delivery is not an acceptance requirement.
Distinguish provider acceptance, worker receipt, OS display and click completion
in evidence. Long or uncertain checks use the required verification watcher.
This architect assignment ran no tests, push proof, subscription changes or
deployments. The lead records implementation checks, independent review, synthetic
integration, deployment and actual OS display as distinct evidence. Missing
macOS user confirmation must remain explicit in the handoff. The lead owns
acceptance, tracking and artifact registration.


## Implementation sequence

1. Lead confirms the retained implementer, registers affected same-session feature
   worktrees from current fetched `origin/master`, and maintains plan/state.
   Implementer verifies current interfaces and starts with a bounded local
   sender/worker prototype plus quick synthetic checks inside this design scope.
2. Implement the server observation reducer, private persistence/provider
   transport and worker delivery, then wire title markers, settings and creation.
   Update owning project behavior/operations docs, commit intended changes and
   pass focused quick checks. Preserve event and ownership invariants throughout.
3. Prepare exact published runtime/dependency revisions and workspace/configuration
   composition. Consolidate superseded pin updates; inventory full branches,
   final diffs and migration/state lineage. Pass quick composition checks.
4. Lead runs mandatory independent final review on committed substantive changes
   and final branch inventories, using the retained review-purpose member and
   required lanes. Resolve blocking findings before long integration or push
   proof; use affected-lane reruns only when required by the review skill.
5. Launch long packaged/integration checks through the required verification
   watcher. Deploy reviewed exact snapshots to aitherdev using the coordinator,
   then verify live health, delivery plumbing and the exposed Test notification
   flow. Record what the Linux host proved and what needs actual macOS browser
   confirmation; do not report OS display on the basis of a fake push endpoint.
6. Hand off the deployed feature, evidence and remaining browser-confirmation or
   integration items. No master merge, reservation finish or session lifecycle
   action follows merely from implementing, deploying or handing off this work.
