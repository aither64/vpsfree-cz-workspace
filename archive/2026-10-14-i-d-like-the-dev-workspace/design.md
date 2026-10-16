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

## Provider compatibility addendum, 2026-10-15

Status: ACCEPTED IMPLEMENTATION BRIEF. The lead accepted the exact-host addition
and endpoint-digest deletion-only cleanup amendment on 2026-10-15 and assigned
implementer0. Inspected application source
`e414ed31806d2b91620d5e5fad8b5b5ee56e07ac` and this
session's `push-provider-probe/native/run/results.json`; no new test, subscription,
deployment or host change was performed by the architect.

### Chromium provider evidence and correction

The probe identifies Chromium `147.0.7727.15` and a native subscription on public
hostname `jmt17.google.com`. Official source for that exact version defines it as
the staging GCM push endpoint. `GetGcmEndpointForChannel` selects staging for a
non-stable channel; the alternative Web Push path uses the already allowed
`fcm.googleapis.com` host. Current main retains the same provider selection.
This is the normal upstream route for the observed unbranded Chromium build,
not a headless artifact or JavaScript mock. The lead retained the official source
URLs and line evidence in [chromium-provider-source-evidence.json](chromium-provider-source-evidence.json).
See [147 constants](https://raw.githubusercontent.com/chromium/chromium/147.0.7727.15/components/push_messaging/push_messaging_constants.cc),
[147 selector](https://raw.githubusercontent.com/chromium/chromium/147.0.7727.15/components/push_messaging/push_messaging_utils.cc)
and [current selector](https://raw.githubusercontent.com/chromium/chromium/main/components/push_messaging/push_messaging_utils.cc).

The version's [POSIX channel implementation](https://raw.githubusercontent.com/chromium/chromium/147.0.7727.15/chrome/common/channel_info_posix.cc)
returns UNKNOWN for unbranded Chromium. That explains the observed hostname for
an unbranded Linux build without assuming every Chromium distribution selects
the same provider. Web Push standardizes the protocol, not a fixed provider host.
Upstream staging ownership does not prove delivery availability or a production
service guarantee for this build.

Add only exact host `jmt17.google.com` to the shared registration
and transport allowlist, retaining the existing Mozilla and FCM hosts. This
preserves the accepted Chrome/Chromium scope; requiring branded stable Google
Chrome instead would narrow that scope unnecessarily. Document the staging use
in provider operations guidance. Preserve port 443, HTTPS, public-IP validation,
checked-address dialing, TLS hostname checks, no proxies/redirects, deadlines
and bounded responses. Add no suffix/wildcard or speculative alternate hosts.
Use the browser-issued subscription unchanged; never rewrite its host or path
to a production endpoint, force a browser channel, or send it to another service.

The native evidence reports registration refusal before any Chromium delivery;
Chromium is therefore not yet verified. After committed changes, quick checks and
affected independent security/provider review, rerun the bounded native probe
with zero portal tabs. Require provider acceptance and a worker receipt before
claiming that path works. Keep actual OS display separate. Existing Firefox
evidence reports Mozilla acceptance and worker receipt with zero portal tabs;
its overall phase remains `delivery_incomplete`, and physical/macOS display was
not verified. Log only public hostnames and diagnostic outcomes, never capability
endpoint paths or subscription keys.

### Disable must separate browser and server cleanup

The current browser handler recovers a missing registration ID by calling
`/register` before `unsubscribe()`. An endpoint rejected by registration policy
therefore prevents local removal. Conversely, rejection now does not prove that
an earlier attempt never committed: a response or saved registration ID can be
lost, and policies can change. Do not infer server absence from a missing ID,
an HTTP validation error, or successful local unsubscribe.

The required bounded correction is two independent cleanup results under the
existing Disable action. Always attempt browser unsubscribe even if server
cleanup/recovery fails; verify absence with `getSubscription()` rather than
interpreting every false return as
an enduring subscription. A known registration ID remains the normal server
deletion identity and must survive until its idempotent deletion is confirmed.

For a missing ID, report local removal separately from unknown server state;
never label both disabled just because registration was rejected. Implement the
accepted optional `endpointDigest` alternative on the existing authenticated
`/disable` endpoint:
SHA-256 of the exact browser-issued endpoint string. Require exactly one of the
registration ID or a strict 64-hex digest. Match only registrations in the
current trusted workspace and exact authenticated portal origin; delete matching
records and their pending outbox entries, or return idempotent success if absent.
Do not create a registration to delete it. This deletion-only lookup performs no
DNS or outbound request and does not require the host to remain allowed for new
registrations. It must never enable or send to a refused provider.

Before local unsubscribe, retain the known ID in its existing registration-ID
storage. Only when that ID is missing, retain at most one pending digest selector
locally so reload can retry uncertain server deletion without subscription keys
or endpoint capabilities. Do not introduce a generalized cleanup receipt store.
The existing server store is bounded, so digest matching
can scan its registrations without a new index/schema. Keep ordinary origin,
authentication, payload and method checks; this is an additive deletion API, not
a provider-policy exception. If the server response is unknown, report
"Browser subscription removed; server cleanup still pending" and retain Retry.
Only confirmed server absence plus confirmed local absence earns fully disabled
status. A never-accepted endpoint then cleans up without enabling it, and a lost
registration acknowledgement still cleans up honestly. No worker unregistration
or unrelated browser-data cleanup is implied.

This accepted deletion selector is a bounded additive API amendment, not a new
cleanup service or framework. A rejected recovery call alone cannot establish
that a previous registration was never accepted. Do not broaden provider policy
or silently discard known pending cleanup to make Disable look successful.

Focused verification should cover the new exact host and deceptive suffixes;
the unchanged DNS/private-IP/redirect protections; refused subscription cleanup;
lost registration reply/ID; offline or denied server deletion with successful
local unsubscribe; reload/retry; already absent local/server records; local
unsubscribe failure; digest scoping and idempotence; and cancellation of the
matching outbox only. After committed changes and quick checks, apply affected
retained API/provider security review before long native rechecks. This addendum
changes no deployment or reservation ownership:
the lead reports no own activation, canceled unadmitted activation jobs, and a
foreign hold still blocking deployment. No Chromium readiness or deployment
claim follows from official-source confirmation alone.

## Provider failure diagnostics addendum, 2026-10-15

Status: ACCEPTED IMPLEMENTATION BRIEF. The lead accepted this bounded
verification remedy before assigning implementation. Full evidence and rationale:
[recovery-check-investigation.md](recovery-check-investigation.md#follow-up-after-the-single-diagnostic-run).
The original b8a6 recovery VM failed; its exact-package diagnostic did not
reproduce the failure. Both original exceptions were discarded. This change
addresses that demonstrated loss of diagnostic evidence; it does not identify,
repair or exonerate the original unknown failure. Preserve all existing
evidence and frozen source/pins until the lead assigns source implementation.

The product code/test/docs scope is exactly:

- `libexec/workspace-codex-providers.rb`
- `test/workspace_host/codex_provider_test.rb`
- `nix/tests/session-recovery-boot.nix`
- `docs/codex-providers.md`

Refer any required deviation to the lead before editing another product path.

Use local, per-invocation fixed-step context in the provider apply/recovery
path. Before each existing outer rescue replaces its exception, emit one
structured stderr record, at most 2 KiB, for that escaping failure. Keep forward
and recovery records distinct, including when recovery is nested under apply.
Record validated operation UUID, direction, existing stage, fixed step,
monotonic elapsed time, safe allowlisted exception class/numeric errno and a
bounded selection of package-relative source labels/lines. Unknown exceptions
use a fixed fallback; never print their messages. Do not persist this context.

For readiness failure, include only values already observed by that invocation:
MainPID/ActiveState, executable-match and socket-presence booleans, and the last
safe health-error category. Mark unavailable fields explicitly; do not turn
absence into false or carry observations across attempts. Emit no per-poll log
and add no probe, subprocess, TracePoint or general logging framework. Exclude
raw argv, helper output, arbitrary backtraces/paths, tokens, snapshots and RPC
payloads. Diagnostic formatting/sink failure must not replace the original
exception, change compensation or prevent existing state writes.

In the existing VM test, return unexpected terminal results to Python and fail
promptly with bounded fixture journal and safe state/count diagnostics. Returning
another nonzero status inside `wait_until_succeeds` would still wait 900 seconds.
Compare against the expected phase first: later expected `failed` recovery
results remain valid, and `recovery-required` remains a supported intermediate
or explicitly expected phase. Retain the foreign-cgroup assertion and all later
deliberate compensation/reboot scenarios. Collection failure must preserve the
original assertion failure. Document the stderr location and diagnostic limits
briefly in the provider guide.

Preserve service order, native ownership checks, locks, deadlines, health retry
and restart policy, terminal restoration and recovery fencing. No state schema,
operation-stage, receipt, API, protocol, successful CLI stdout or notification
behavior changes. Existing state remains compatible; diagnostic stderr is
additive. Normal forward-only deployment/recovery rules apply to any later
approved successor package; this addendum authorizes no deployment or pin change.

Quick acceptance: inject distinct forward/recovery failures and prove both safe
records survive with unchanged state/service-call order; cover immediate
identity failure, readiness timeout/last health category, explicit unavailable
fields, unknown exception fallback, secret canaries, byte bounds and failing
sinks. Verify prompt unexpected-terminal reporting without breaking expected
recovery phases. Use the declared repository environment. After substantive
changes are committed and quick checks pass, complete affected independent
review before a fresh lead-assigned watcher runs the full recovery VM, including
later compensation/reboot cases. Passing verifies the diagnostic amendment;
the original failure stays unresolved without concrete causal evidence. The
architect performs no implementation, review assignment or test execution.

## Frontier refresh implementation brief, 2026-10-15

Scope: refresh the existing feature onto fetched, integrated predecessors while
preserving both the accepted feature and upstream behavior. This addendum does
not authorize integration, lifecycle changes, reservation release or execution
by the architect. Session/current/environment and the retained architect roster
were reverified. Earlier source, reviews and verification evidence remain valid
historical records; do not overwrite them with refreshed results.

### Inspected frontier and overlap

The frozen runtime range is `ba8669b14536f72b559abc912bba8eac430111e4` through
`0b403305e085aa01884cf56acea7c717f78f7e86`: `b8a6be2` adds attention/Web Push and
`0b40330` adds bounded provider failure diagnostics. The complete fetched runtime
delta to `832d9f1a6a21337dd44063ddf39f7a88cfc95450` comprises:

- `3d60ced`: shared, bounded coordinator admission and a separate coordinator
  notification worker. Preserve generation/incarnation checks, exclusive
  lifecycle writers, ledger serialization and existing request identities.
- `69399c5`: cached Ruby suite derivations, isolated session/coordination shards,
  coverage aggregation and source-filter checks; development-shell factoring.
- `832d9f1`: resumable integration/certification, immutable recipe configuration,
  optional package capability metadata, artifact incarnation checking and tests.

Only `libexec/dev-session`, `libexec/workspace-host` and
`nix/workspace-portal.nix` overlap our changed paths. The Ruby edits concern
different functions: retain upstream artifact/command dispatch changes together
with our optional, strictly boolean creation preference receipt readers. In
packaging, retain upstream `integrationConfig`, installed helper/catalog files,
package metadata, `rubyChecks` import/passthru and aggregate dependency; retain
our Web Push vendor hash, four JavaScript syntax checks and attention browser
test. Do not restore the removed inline Ruby suite block or run the same suites
twice merely to resolve context. Keep upstream `flake.nix` check exports and
development shell intact.

`portal/internal/agentteams/catalog.go` changes upstream only for optional
integration capability decoding/validation. Digit-bearing role names are already
accepted by `roleNameIdentifier` at both `ba8669b` and `832d9f1`; this refresh
needs no new role grammar. Preserve strict metadata validation and old metadata
without the optional capability. Upstream does not change the attention/Web Push
browser/server files, provider implementation or recovery VM fixture. Retain
their accepted behavior and exact source where possible, but that absence of
direct edits does not prove runtime equivalence.

Coordinator delivery here means messages to retained agent threads. Keep its
separate Ruby worker distinct from our server-side browser Web Push observer and
service worker. Preserve exact-session status/acknowledgement, baseline/dedup,
foreground presence, `R`/`R2` ownership markers, deletion-only cleanup and SSRF
guards; no notification scope or persistence redesign belongs in this refresh.
Keep bounded forward/recovery diagnostics and the full recovery VM scenarios.
The original lost provider exception remains unresolved.

### Composition and conflict boundaries

The selected integrated predecessors are runtime `832d9f1`, configuration
`d28926183eb9f1dc427ed597819cf157796ade88`, and workspace
`86d4a05768c95e36081730ec9c18f13eefb9970d` (substantive adoption `c5e2a693`,
followed by tracking). Workspace and configuration locks both select that exact
runtime and content hash. Workspace now selects extension
`767dfd587e346168e1443e65ccdb67ce748f3fe3`, whose own default runtime is also
`832d9f1`. These supersede the earlier workspace `d22b5341` baseline.

The extension passes `integrationConfig` to the runtime and supplies the
immutable `workspace-pins` recipe. Preserve this API, the workspace's
`config/integration.nix`, selected extension revision/hash, sibling inputs and
follows. A runtime candidate based only on the old `ba8669b` frontier would lose
this supported composition. Rebase our two runtime commits onto `832d9f1`;
resolve only the overlap described above, retaining each feature's effect.
Unexpected conflicts or behavioral changes go to the lead before expansion.
Use only fetched upstream; consume no foreign unmerged branches or worktrees.

Lead-owned downstream refresh must start from the new workspace/configuration
baselines and select the exact final published runtime in both the nested
`vpsfree-dev-workspace/dev-workspace` input and configuration `devWorkspace`
channel. Use the declared generators and deployment consistency checker; preserve
extension selection and integrated coverage. No new migrations, private-state
formats, dependency upgrades or compatibility framework are needed. Retain
upstream versioned integration journals/capability fencing and the already
accepted creation-receipt compatibility contract. Recovery remains forward-only
through a compatible package, preserving subscriptions, VAPID keys and outbox;
never downgrade to the old composition to reuse its build.

### Review, verification and deployment sequence

1. Implementer records the new exact range and `git range-diff` against the
   frozen two-commit range, plus final upstream-to-feature diff. Check all three
   overlapping files and unchanged feature blobs. Keep both functional changes
   and their no-migration conclusion reviewable; preserve prior evidence.
2. In the declared Nix environment, run focused Go checks for `agentteams` and
   `web`, attention/notification browser contracts and JavaScript syntax;
   focused Ruby creation-receipt, artifact ownership, provider-diagnostic,
   admission/integration/certification tests as applicable. Cover omitted/true/
   false preference compatibility and rejection of malformed values. Check Nix
   formatting/evaluation and the resulting package/check graph. Quick checks
   must not accidentally launch the full suite through development-shell setup.
3. After committed substantive changes and quick checks, obtain affected
   independent review before long checks. Supply old review, exact ranges,
   overlap resolution, new baseline contracts and downstream composition.
   Runtime admission/integration and workspace adoption are substantive changes;
   stable patch IDs or a clean rebase do not qualify the whole refresh for the
   certified-equivalence exception. Reuse unaffected review conclusions only
   with explicit source/contract evidence. Pure generated-pin reuse separately
   needs exact semantic proof; it cannot hide the extension/baseline change.
4. A fresh lead-assigned watcher runs the final packaged flake checks, including
   complete Ruby shard coverage/aggregate, source-filter check, host/package and
   catalog contracts, and the full `session-recovery-boot` VM with later
   compensation/reboot scenarios. Preserve unsharded diagnostic mode. Evaluate
   final derivations first: reuse a successful result only when schema-1 receipt,
   exit status zero, full derivation path and every recorded input match exactly.
   Source/tree equality or an old aggregate log is insufficient. The shared Ruby
   filter includes `libexec/`, `test/` and `nix/`, so our Ruby/fixture changes
   invalidate those shards even when most individual test files are unchanged.
   Let identical Nix derivations reuse their outputs; do not rebuild them for
   appearances. Changed derivations need their own successful evidence.
5. Retain prior native Firefox/Chromium proof as browser/provider feasibility
   evidence. Final deployment acceptance should bind a bounded no-portal-tabs
   provider/worker smoke check to the refreshed package and exact harness/browser
   inputs; an older package receipt cannot claim that final-package check.
   Browser permission and actual macOS display still require the real browser;
   Linux worker receipt proves neither. No broadened platform investigation.
6. Lead refreshes exact machine/profile artifacts and prepared snapshots after
   final checks/review and lock consistency, preserving machine-before-profile
   ordering and the existing reservation. Per the lead's latest receipt, machine
   job `2e8a96bc` refused before activation with `needs_refresh/baseline_changed`;
   profile `19311887` waits on it and reservation `1956d2a0` is now held. No own
   activation occurred. These are lead-reported observations, not architect
   runtime queries. Do not retry the stale prepared artifact or bypass coverage
   checks. The new integration CLI has been read for awareness; its merge modes
   cannot infer the missing user merge approval. Existing individual jobs remain
   the lead-owned refresh path.

Acceptance is preservation of both upstream and feature contracts at a recorded
final composition, affected review, valid exact-check receipts and refreshed
deployment preparation. This planning addendum itself changes only this design
record; it runs no checks and grants no additional operational authorization.

## Process-group verification failure investigation, 2026-10-15

Status: PROPOSED bounded test-only remedy for lead decision. Identity/environment
and the retained architect roster match. Source remains frozen at published
`bb9e6291bec10227c961c36559fba406938f1eaa`; this investigation changes no product
source and executes no check or retry.

**Established evidence.** [frontier-runtime-flake.status](frontier-runtime-flake.status)
records local exit 1 after 6m10s. [The log](frontier-runtime-flake.log), lines
1977–1980 and 2262–2293, identifies failed package variant
`/nix/store/qxa600ysy8j7n9nx6b7spljabm531s87-dev-workspace-0.2.0.drv`:
`TestRunKillsDescendantsOnTimeout` failed at line 57 after 1.00s, reporting PID
12682 alive. Other processgroup invocations passed; host-idempotency completed.
[Same-head CI](ci-frontier-result.json) succeeded in run 38702143420. These facts
do not establish local aggregate package `q4f1bdkixw6dkc6cdh90mbjqwfizj4lb` or
`session-recovery-boot` success and do not exonerate the failure.

Both processgroup source/test blobs are identical at `0b403305`, `832d9f1` and
`bb9e6291` (`9e7d02c4e8c234d2d4f12fb446e7e082bf74b45a` and
`55bbc05e33e4c2698905f03bca3720d3b27764d1`). The failing test/helper originates
in `3457f29`; `f1791bf` later added graceful cancellation and its test. This
establishes unchanged code, not absence of an interaction or product defect.

After the one-second context expires, the test starts a fresh two-second polling
deadline. Its 1.00s total failure is inconsistent with exhausting that budget:
the loop exited on a false helper observation, then its extra final call returned
true. The helper conflates absence, zombie state, malformed/short stat data and
start-time parse failure into false. On other read errors it falls back to
`kill(pid, 0)`, losing the start-time identity check. No state, start-time value,
read category or signal result from these observations was logged.

The lead's `Z` then `X` hypothesis is technically plausible: the helper excludes
`Z` but counts `X` with matching start time as live. Canonical Linux reference
source `fc37ccc43227ab8eef70b50660a081f2615d0ead`, `fs/proc/array.c:125` and
`kernel/exit.c:1174`, labels `X` dead and implements `EXIT_ZOMBIE` to `EXIT_DEAD`
reaping. This reference is not evidence of the failed builder's actual states
or kernel revision. The original cause remains unestablished.

`Run` creates a process group, sends its group SIGKILL on cancellation, ignores
the signal error, waits for the leader and returns the context error. The test
did validate captured child PGID against leader PID. However, stdout/stderr are
unset, hence connected to `/dev/null`; there is no descendant-held Go copy pipe
in this test. A surviving child need not keep `Wait` running after the shell
dies. Therefore the short duration cannot itself prove successful group cleanup.
There is no recorded SIGKILL error or confirmed live descendant after the grace
period that would justify changing production cancellation.

**Smallest justified change.** Limit implementation to
`portal/internal/processgroup/processgroup_test.go`, retaining the existing
timeout and graceful-cleanup assertions. Correct the demonstrated ambiguity of
the test's observer and add failure evidence; do not present this as a proven
repair of the original incident:

- Use one test-local bounded wait result. Accept only validated absence, a
  different start time (the original process is gone), or matching identity in
  terminal `Z`/`X` state. Once established, do not reverse that result with an
  independent final probe. Keep the current two-second deadline and polling
  interval; a matching live child at the deadline must fail.
- Keep PID/startTime ownership and the fixture's PGID assertion. Parse only the
  required stat fields safely, accounting for the parenthesized command field.
  Treat malformed data, parse/read errors and unknown states as unknown, never
  proof of death. Retry unknown observations only within the original bound;
  unresolved unknown fails with its category. Remove the identity-free kill-zero
  fallback. No generic proc library, scanning, process-name matching, additional
  group signaling or foreign-process operation.
- On failure emit one bounded diagnostic (at most 1 KiB) containing expected
  PID/startTime/PGID, leader PID, elapsed time, last observed identity/state and
  fixed read/parse category or errno. Retain at most the first and last sample
  in memory if needed to explain a transition. No raw proc dump, command line,
  environment, per-poll logging or product diagnostic framework.

This is sufficient to justify a test-observer correction without first running
an uninstrumented reproduction. If the corrected assertion still finds the same
live identity, preserve its observations and stop: the next bounded diagnostic
would use a disposable fixture with the exact product/toolchain inputs and
record the cancellation syscall outcome, separately authorized by the lead.
Do not broaden product code or attribute the original failure to `X` merely
because the corrected check passes.

**Verification and compatibility.** Quick checks should deterministically cover
matching live `S`/`R`/`D`/stopped states failing at the bound; terminal `Z` and
`X`; absent/reused PID; malformed stat and read/permission errors failing closed;
and the `Z`-then-`X` regression without reversing an established terminal result.
Retain a real owned live-child control so the helper cannot become an always-dead
predicate, and both existing cancellation tests. Disposable fixture cleanup must
use its own spawned child handle/verified identity only. Use the declared Go
environment with `-mod=readonly`, syntax/format checks and uncached test results.
No cancellation behavior, service, ownership rule, timeout, API, schema, private
state, browser feature or deployment policy changes are proposed.

After the intended test change is committed and quick checks pass, lead obtains
affected independent review. Then a fresh watcher may run a finite focused
uncached processgroup check and the necessary final packaged flake verification;
neither repeated-until-green runs nor increased timeouts establish correctness.
Bind results to the new exact derivations and preserve the failed log and CI
receipt. Reuse previous successful checks only under the existing exact-input
rules; the failed variant and uncompleted aggregate/recovery checks need their
own successful final evidence. Pins, reservation and stale jobs remain lead-owned;
deployment stays blocked on verification. The architect performs no execution.

## Deployed Firefox delivery feedback, 2026-10-15

Status: ACCEPTED IMPLEMENTATION BRIEF; implemented per lead report and reconciled
for final source-review context. The lead's four copy corrections have been
applied; final copy approval and independent source review remain lead-owned.
This reconciliation is not a new source inspection or verification gate.
The user reports
no visible notification in Firefox on macOS, including after Test while staying
on the page, switching tabs and switching applications. The UI remained at its
ten-second message. Bound session/current/environment/roster were reverified;
the inspected deployed source is `6e1d9a191724d376cad2a71f234f0e4d1c01f36f`.
This is now a supported consumed version: preserve its three commits, pins,
private notification state and old-ID cleanup contract. No execution or product
edit is performed by this investigation. Preserve the forward-only lineage from
deployed `6e1` and its retained evidence. The accepted menu/spacing change places
browser controls on `/browser-notifications` and retains them in session
Settings; the index remains free of browser controls and notification-client
initialization.

### Evidence and limits

The following source observations describe deployed `6e1`, before the accepted
amendment, and remain evidence of the original report.

`browser-notifications.js` calls `refresh()` only on load. Test awaits the queue
POST, prints its ten-second text and immediately clears busy; it neither polls
provider status nor listens for worker results. The server response confirms
queue admission, not sending or delivery. This is a concrete observability
defect, not an established explanation of missing display.

The lead's bounded [metadata projection](feedback-delivery-metadata.json) shows
one non-disabled Mozilla registration for the portal origin, last result
`provider_accepted`, and zero pending tests. This is consistent with the user's
report and a completed send, but neither proves association with this user's
browser nor correlates acceptance with this exact test. The architect read only
that sanitized artifact, not live subscriptions or private host state.

The Test event has a separate `test-<browserID>` identity, an empty session slug,
ten-second delay and one-minute expiry. Session presence/acknowledgement cannot
match it, and the worker bypasses its session-status trust fetch. A delivered
Test calls `showNotification` regardless of foreground focus. The worker does
not catch/report that API's rejection. Its IndexedDB event is saved **before**
the call, so worker receipt is not evidence that the display API resolved.

[Retained native results](live-native-6e1d9a19/run/results.json) report real
provider acceptance and a new pre-display worker record with zero portal tabs
for both browsers. Chromium has a browser notification record; Firefox has
none. The [harness](live-native-6e1d9a19/live-check.cjs) counts test-kind IndexedDB
events and `getNotifications()` entries separately. It records no post-display
promise outcome or physical display/click proof; its successful exit means
diagnostics completed. Linux/Xvfb is not the user's macOS environment. The user
failure and the Firefox browser-record gap remain unresolved; neither may be
dismissed as an OS setting or erased by another green provider/worker run.

All Test events for a registration currently reuse one tag with `renotify:
false`. Later explicit tests can replace an existing entry without another
alert. This is a concrete repeat-test limitation, but does not explain a first
missing notification or prove the Firefox incident's cause. Ordinary session
tags, focus leases and attention acknowledgement remain intentional behavior.

### Accepted delivery amendment

Keep the server observer, transport, provider guards, subscription/key storage,
expiry/retry policy and session attention semantics unchanged. Improve the
existing Test path, without a new receipt service or server-state schema:

1. Add the already-created test event's `id`, `identity`, `revision` and
   `expiresAt` to the existing successful `/test` response. This small additive
   response field is justified by exact correlation: a stale browser result or
   another tab's test must not certify this click. Old clients ignore it; old
   servers without it yield limited/unknown diagnostics, not success. Do not
   expose endpoints, keys or provider response bodies.
2. Retain at most one pending descriptor and one latest matching outcome in the
   existing browser attention record for that test identity. Add optional
   bounded fields, with no IndexedDB version/object-store change and no server
   receipt persistence. Worker stages distinguish received, display API resolved,
   display API rejected, and browser-record lookup present/absent/unavailable.
   Capture rejection by a small allowlisted error-name category, never arbitrary
   messages or payloads. A resolved API means only that the browser accepted the
   display request; a record is still not physical OS display. Match event IDs
   and monotonic revisions so old/duplicate/out-of-order delivery cannot replace
   a newer result or certify another test. Missing fields from an older worker
   mean unknown. Diagnostic storage failure must not prevent the display attempt.
3. After Test, poll the existing provider-status GET and local correlated outcome
   on a bounded schedule (for example every two seconds through expiry plus a
   short grace). Refresh on worker message and on visible revisit/pageshow;
   closing the page must not affect push delivery. Resume the pending result
   after reopen, and stop timers on pagehide or completion. A timeout reports
   which stage is unconfirmed, never "delivered" or guaranteed OS failure.
   The current server `result` is registration-wide and uncorrelated: label it
   as the last provider result, not this test's receipt. Do not mistake an old
   `provider_accepted` value for this request. Disable/replacement must stop the
   old UI wait without losing either server deletion obligation.
4. Make each explicit Test event a fresh notification entry using its event ID
   in the test-only tag; keep duplicates of that event coalesced. Bound retained
   test notifications by closing only previous entries of that same test
   identity. Do not alter session tags, neutral stale-event display or session
   acknowledgement. Keep the portable requirement to attempt visible display
   for every incoming push; do not introduce silent suppression as a repair.

Use the existing `workspaceAttentionStore` on the dedicated
`/browser-notifications` page and in session Settings. This replaces the earlier
index-include proposal; do not restore index controls or notification-client
initialization, and do not create a second store.
For existing subscribers, check/update the existing worker registration and
handle pending activation honestly; no unregister/resubscribe or key reset is
needed. Do not claim post-display diagnostics while an old worker is active.
Preserve version-1 push payloads and old queued events through worker updates.

Accepted owning paths: `static/browser-notifications.js`,
`static/notification-worker.js`, the existing attention-store helper only as
needed for bounded record reads, `notifications.go` for the additive Test reply,
the existing notification/attention browser and Go tests, and the two notification
guides, plus shared-store inclusion on the dedicated notification page. Template
and test overlap with the separate UI work is coordinated through the lead.
No sender/transport/private-format change is justified by current evidence.
Lead owns final user-facing wording.

The user's removal of the top `p#session-attention-status` is a separate tiny UI
change. Its existing observer remains unchanged and null-guarded when that node
is absent. This removes the visible status line; it is not a delivery mechanism
or a repair for the missing notification. It does not change title markers,
focus acknowledgement, reservations, push delivery or stored notification state.

### Verification and next diagnosis

Quick checks must prove queue text advances; rejected and resolved display calls
are distinguished; zero/error browser-record lookups do not become OS success;
old/duplicate/other-tab results cannot satisfy a pending test; reload/no tabs and
storage failure are honest; a repeated explicit test can alert afresh; focused
session acknowledgement never closes the Test; and old-ID/digest Disable still
cleans both obligations. Preserve existing payload, origin, route, mute, privacy
and SSRF tests. Correlate `/test` response metadata with its actual queued event
without altering the private version-1 snapshot.

After committed changes and quick checks, affected independent review precedes
fresh bounded verification. Record separately: queue accepted, last provider
result (correlation limit explicit), exact worker receipt, `showNotification`
resolved/rejected, matching browser record, physical OS appearance and click.
Native probes must use the new post-display evidence; pre-display IndexedDB
alone cannot complete display acceptance. Final user acceptance requires actual
Firefox/macOS with the browser running: Test on the current page, then a finite
background case with every portal tab closed/minimized or unfocused, plus a
real input/done event under its documented focus rules. Verify click navigation
and ordinary authentication. Retain Chrome/Chromium regression coverage and
distinguish Linux automation from the user's physical display. Physical
Firefox/macOS display and click acceptance remain open; implementation and copy
completion do not establish them.

If provider acceptance still has no worker receipt, investigate that boundary
with the correlated evidence. If the API rejects, use its safe category to select
the next bounded fix. If the API resolves but no notification is visible, keep
that result explicit and investigate the actual browser/platform boundary; do
not claim delivery fixed. No browser-local display control is included in the
accepted amendment. A separately authorized, explicit browser-local
`showNotification` control can isolate that boundary if needed, but must never
count as server-push success or silently substitute for the Test path. No
repeat-until-green run or speculative settings diagnosis is proposed. Session
and deployed-review reservation remain open under lead ownership.

## Configuration frontier refresh: 130c2248 (planning brief)

Read-only inspection confirms `d2892618..130c2248` contains three integrated
input commits (`555acfb9`, `583e0809`, `130c2248`) changing only six lock nodes.
Production/stable/staging nixpkgs select `a033e66a`; unstable selects `55bfb4d7`;
both vpsAdminOS staging inputs select `7fd09b9b`. The own clean configuration
feature remains the deployed `45fa9962df83b9bec65523ae6ee7d19b63bb03ea` over
`d2892618`. This brief authorizes no ref, input, build or deployment operation.

### Reachability and environment

Aitherdev selects `nixos-stable`, `home-manager`, `llm-agents`, and
`dev-workspace` in `cluster/cz.vpsfree/machines/aitherdev/module.nix`. Root
`nixpkgs` and home-manager's nixpkgs follow `nixpkgsStable`; the stable update
therefore reaches host packages/services, home-manager, and the same-pkgs KB
staging container. Its standalone NixOS configuration does not import the fleet
base environment. The other five updated nodes have no direct selection through
these aitherdev channels; retain them without expanding verification to fleet
deployments. Exact final closure remains an evaluation result, not a source-only
claim. The host's Codex wrapper receives host `pkgs`, even though selected
llm-agents and runtime nested nixpkgs inputs remain unchanged.

The configuration dev shell also imports root `nixpkgs`, overlays Ruby 3.4, and
passes those packages to `confctl.lib.mkConfigDevShell` in tools mode. At pinned
confctl `7bee58a5`, `nix/flake/mk-config-devshell.nix` uses that `pkgs.mkShell` for
Ruby, Git, formatters and extra packages. Confctl's own pin and packaged closure
being unchanged does not establish shell equality. Treat retained
`config-dev-env.sh`/status as old-baseline evidence. Obtain the final baseline's
declared environment before its channel update/hooks/checks; reuse the capture
only with exact shell derivation and effective-input equality evidence. No such
proof was obtained here, and no shell was sourced or evaluated for this brief.

### Smallest downstream refresh and verification

1. Preserve a durable exact deployed `45fa9962` ref and its old base, composed
   revisions, artifact and activation receipts before replacing the superseded
   pin stream. Preserve all consumed runtime history and deployed notification
   state. Rebase the pending configuration onto `130c2248`; generate one final
   runtime selection through `confctl inputs channel set --commit dev-workspace
   devWorkspace REVISION`. Do not restore an old lock or update all inputs.
2. Compare final lock semantics against `130c2248`: retain all six integrated
   nodes and unrelated inputs/follows; permit only the exact final runtime pin
   and justified generated consequences. Match the workspace's direct nested
   runtime selection and retain its selected extension. Run the existing
   deployment-composition checker on those final roots. No API, private format,
   schema or migration change is introduced by this refresh.
3. Quick evidence comprises declared-environment identity, generated lock/input
   mapping, repository hooks, exact aitherdev input/evaluation results, and the
   final composition/history inventory. Lead's final affected independent
   review covers the actual new base and locks after final source fixes and
   quick checks. This planning record needs no separate automatic review.
4. Prepare/build the exact final aitherdev configuration revision after review.
   The stable update can change service and kernel derivations; old host
   artifacts do not prove the new build. Confctl also embeds `self.rev`, so even
   equal Git trees do not substitute for final-revision preparation. Compare
   final inputs/artifacts and planned activation effects; refresh stale prepared
   jobs through existing coordination only. Long/uncertain work belongs to a
   fresh lead-assigned watcher. Stop and investigate any unexpected local kernel
   build or substitution miss under the verification policy; this is no kernel
   build or reboot authorization.
5. Reuse prior runtime checks only when their exact derivation and effective
   input identities match. Configuration-only upstream updates do not by
   themselves require repeating unchanged runtime tests; current runtime source
   remedies still require their affected verification. No whole-fleet or
   vpsAdminOS migration campaign follows from unselected lock-node updates.

Later authorized activation keeps the existing reservation and ordered machine
then profile jobs, the adapter's dry activation, and no-reboot boundary. Preserve
old receipts and recovery journals, configured system auto-rollback, and the
forward-only application selection contract from deployed `6e1`; retaining a
deployed ref does not authorize selecting an older application. Reconcile any
uncertain original attempt before another activation. Lead owns final checks,
pins and preparation; no new readiness, merge, release or lifecycle claim follows
from this brief.

## 5a07708e browser fixture: Enable observation failure

**Investigation / bounded remedy proposal, pending lead assignment.** The sealed
`feedback-5a-browser.log` and `.status` record the first, unretried actual-browser
fixture at `5a07708ea80a2649265c3ef268b8379daaec47bb`: exit 1, 17 seconds overall,
`TestNotificationsBrowser` 9.74 seconds. Chromium failed at CJS line 70, before
Test or synthetic push, expecting Enabled but observing first Disabled and then
"Browser setup is incomplete". The log contains no registration response,
queried-ID provenance, controller-change ordering or exception category. It
does not establish which asynchronous path produced the final text. This is
separate from the user's original physical Firefox/macOS display failure.

### Concrete source finding and limits

At this exact revision, `static/browser-notifications.js:174-188` reads the
worker/subscription and server status across awaits, then assigns shared local
subscription, registration and status fields without checking whether an action
or newer refresh superseded that observation. `controllerchange` at line 314
launches it; `notification-worker.js:129` claims clients on activation. Enable
registers the worker, waits for readiness, registers the subscription with the
server, saves the returned ID, and sets Enabled (lines 190-228).

A source-permitted ordering is: refresh queries an empty/old ID; Enable saves
the new ID and succeeds; refresh's older false `registered` response then marks
the same browser incomplete and disables Test. An earlier refresh can also
mutate `localSubscription` during an action, or overwrite an action's error.
This is an actual missing freshness/ownership guard, independently of whether
it caused this failed run. Merely checking `busy` at refresh entry would leave
already-running refreshes able to commit stale results after the action ends.

The fixture (`notifications_browser_test.cjs:61-68`) deliberately supplies a
local fake subscription before any server registration. That models a possible
existing-local/missing-ID condition, but makes an empty-ID refresh observe
local-present/server-absent immediately after first worker registration. It
does not itself prove a product registration failure. Do not remove that case,
delay assertions or serialize away worker activation merely to make it pass.
If a separate first-subscription case is useful, model `getSubscription()` as
null until `subscribe()` and retain this pre-existing-subscription case too.

The Go fixture uses the real notifications handler and isolated private store;
it replaces only the subscription supply and session attention/coordination
reads. Its fresh symlink host profile is captured by `New` and not replaced;
the provider catalog is explicitly absent and the fixture has no workspace
name, which permits provider admission. Its HTTPS listener host becomes the
exact trusted origin. The real mutation-origin and current-profile checks,
subscription validation and atomic store change still apply. No static fixture
setup error in those checks was found. A failed `/register`, fetch, or local
storage operation remains possible because Enable masks errors as incomplete
once a local subscription exists. The recorded status cannot distinguish those
from the stale refresh; do not relax authentication, profile or store checks.

### Smallest justified implementation and next evidence

Limit the source remedy to client refresh ownership in
`static/browser-notifications.js`, with deterministic controls in the existing
`attention_browser_test.cjs` harness. Stage refresh observations locally; commit
them only if that refresh is still current, its captured registration identity
still matches, and no explicit action/page retirement superseded it. Invalidate
pending reads when actions begin and on existing cross-tab revocation/pagehide;
ignore or coalesce refresh triggers during an action. Guard success and failure
paths, including status/buttons and any resume work. A newer refresh must win
over an older response. Do not introduce a shared framework, API, new persistent
field, automatic resubscription, or a new server registration on refresh.

Add a finite failure-only diagnostic trace to
`notifications_browser_test.cjs` around this boundary: numbered GET/register
request and completion order, HTTP status, queried ID absent/current/stale as a
boolean/category, response registered/available booleans, saved-ID presence,
worker/controller state and fixed local exception category if observed. Capture
the register response explicitly, so a non-2xx response cannot disappear behind
the generic status assertion. Keep the trace bounded and omit raw URLs with
queries, IDs, endpoints, keys, arbitrary messages/bodies and browser storage
dumps. The Go fixture needs no behavior change; add a fixture-only safe category
projection there only if HTTP outcomes cannot distinguish its refusal boundary.

Quick deterministic checks should force old GET success and rejection to finish
after Enable success, a refresh begun before Enable, a controller-change refresh
during Enable, two reversed refresh completions, and pending refresh completion
after Disable/revocation. Assert no stale status/local-subscription replacement,
Test enabled only after valid registration, and real registration failures still
reported as incomplete. Exercise both absent and existing local subscription;
retain all old-ID/digest cleanup, pending Test and cross-tab invariants. No
product transport, worker delivery, payload/private-store format, mute or
forward-only deployed `6e1` compatibility change follows from this correction.

After the lead assigns the bounded change, committed quick checks and affected
independent review precede one fresh exact-head browser fixture with the added
diagnostics. Keep the original failure intact; a green result proves the forced
orderings and current fixture behavior, not the original causal ordering or OS
delivery. If it fails, stop at the recorded response boundary rather than retry.
Lead selects subsequent full-flake/native/deployment checks separately; original
physical Firefox/macOS display and click acceptance remain open. No browser,
test, build, provider or host operation was performed for this investigation.

## In-place notification-worker activation, narrowed user requirement

**Accepted implementation brief, 2026-10-15.** The latest user direction supersedes the
earlier close-all-tabs guidance and the proposed broader retained-client
compatibility exercise: notifications must work on new/refreshed documents while
other portal tabs remain open. Our code must not close or reload those tabs;
preserving their old notification semantics or retrofitting their loaded scripts
is not required. Bound current/environment and roster rev17 were checked; the
inspected deployed source is `4ed9af55127743b7564cb4dd01d10c9f7fee5120`.

### Current cause and minimal change

The current worker has no install-time `skipWaiting()`. An update can finish
installing but remain waiting while an old worker controls open documents. Its
existing activate-time `clients.claim()` runs only after activation and cannot
remove that wait. The client calls `registration.update()` for an existing
registration, then treats installing/waiting as a reason to close tabs. This is
the ordinary worker lifecycle, independent of the Firefox display rejection.

Add `install` handling with `event.waitUntil(self.skipWaiting())` and retain the
existing `activate` handler with `event.waitUntil(self.clients.claim())`. Choose
automatic activation, with no new button, page reload, worker-message command,
version negotiation, or update framework. The worker has no fetch handler or
page/API cache; taking control therefore does not replace conversation assets,
requests or document state. Initial installation remains behind explicit Enable;
opening an unsubscribed page must still not request permission or register it.

On a new/refreshed notification-controls document, use the existing update check
for the root registration. Replace close-tabs advice with bounded observation of
installation/activation, followed by the existing Test-diagnostics capability
check. `navigator.serviceWorker.ready` alone can resolve to the old active worker;
do not treat it or a matching capability reply from that old worker as proof a
known waiting successor activated. Confirm the current document's controller
has taken over before probing it; a reply from `registration.active` alone must
not certify a document still controlled by the predecessor. Reinspect state on
state changes/controllerchange, with a finite deadline (about ten seconds),
cleanup of listeners/timers, and the existing refresh-generation guards. No
continuous update polling or new capability protocol is needed. Preserve the
existing bounded capability check solely for honest Test-result support.

An old already-waiting `4ed9` worker has neither skipWaiting nor an activation
message handler; sending it a new message cannot install this behavior. The
new/refreshed page's update check must fetch the newly deployed successor at the
same worker URL; that successor's own install handler removes the waiting
requirement. A `6e1` active worker with `4ed9` waiting is handled by that same
successor fetch. If fetch/install/activation fails or exceeds the deadline,
report update unconfirmed/failed and limited diagnostics truthfully. Do not
claim success, tell users to close all tabs, loop retries, unregister, or reset
data. A later new/refreshed page may check again. Existing loaded old copy cannot
be rewritten remotely and is outside the narrowed criterion.

### State and delivery boundaries

Keep root scope, PushSubscription, permission, VAPID keys, registration ID,
old-ID/digest cleanup obligations, server private state and IndexedDB version 1
unchanged. Current optional Test fields need no database upgrade; existing
records and version-1 queued payloads remain readable. No session, provider or
conversation operation belongs to activation. Do not cancel/resend queued push
or clear attention/notifications during install/activate. Retain push
`event.waitUntil(display(payload))`; browser-managed activation and in-flight
events retain the existing delivery/crash limits, not an exactly-once guarantee.
No promise is made that an old worker already processing a push will produce new
diagnostics. This fix does not explain or repair Firefox's separate display-call
rejection; physical Firefox/macOS acceptance stays open.

### Owning paths and verification

Implement only `portal/internal/web/static/notification-worker.js`, bounded
readiness/copy handling in `static/browser-notifications.js`, existing
`attention_browser_test.cjs`, and the actual-template
`notifications_browser_test.go`/`.cjs` fixture as needed. Update the two owning
browser-notification guides to remove current close-all-tabs advice and explain
automatic activation on new/refreshed pages. Lead owns final visible wording;
template changes are needed only if actual current copy resides there. No API,
sender, dependency, private format or database schema change is intended.

Quick Node coverage must exercise install skipWaiting and activate claim,
successful transition from waiting/installing to activated, bounded failure or
nonresponse, no stale readiness overwrite after a newer refresh/action, and no
subscription/permission/cleanup mutation caused by update. Retain the existing
attention, Test correlation and Disable regression tests.

The real browser fixture must first establish an old active worker controlling
an open portal conversation page, with an in-document/draft sentinel. Then serve
the actual successor at the same root URL and open or refresh a second controls
page. Verify the successor activates while the first controlling page remains
open, neither page is automatically reloaded/navigated/closed, the sentinel
survives, and the new page is controlled by the actual successor. Require this
real old-active-plus-waiting to successor transition in both Firefox and
Chromium, using a finite fixture-only served-version switch and an old waiting
worker without an activation handler. A new uncontrolled page alone is not this
regression proof. Keep registration/update/control lifecycle unmocked.

Playwright `context.serviceWorkers()` and worker evaluation are Chromium-only
in this fixture. Require correlated synthetic Test push/display from the
successor in Chromium only, clearly labelled synthetic. Existing actual-module
tests retain worker logic coverage. Do not add a production message/test API or
a Firefox fixture workaround to imitate the unavailable evaluation capability.
Real lifecycle coverage in Firefox does not establish provider delivery or
physical display; native Firefox and actual macOS acceptance remain separate.

After committed quick checks, affected independent review precedes the finite
actual-browser fixture. Lead owns later checks, final pins and authorized ordered
deployment; no provider/native run is added by this brief. Preserve the deployed
`6e1`/`4ed9` history and sealed evidence. This design adds no merge, reservation
release or session-lifecycle authorization, and no execution occurred here.

## Browser-local notification sound preference

**Accepted implementation brief, 2026-10-15; implementation released by lead.** The user confirms
Firefox/macOS popups are visible after system-settings changes and requests
sound versus visual-only notifications. This supersedes the unresolved physical
visibility status for that user-reported case; historical diagnostic evidence
remains intact. Base is deployed `469757183ba9491d642b56e91658dc64e390647b`.
Use a separate owning commit; preserve all seven deployed source objects.

### Contract and feasibility

Add one browser-local sound checkbox to the existing shared Browser notifications
panel, on the dedicated page and session Settings. Checked means sound is
allowed, subject to browser/OS settings; unchecked requests visual-only delivery.
Lead-preapproved label: **Play sound**. Hint: **Turn off for visual-only
notifications. Browser and system sound settings still apply.** Main agent must
see the actual final copy diff before commit.
Missing preference defaults to checked and preserves today's display options.
This applies across this origin/profile's sessions, including Test and background
notifications; other browsers/profiles/origins remain independent. It does not
mute a session, enable delivery, request permission or change subscriptions.

Use standard `showNotification` option `silent: true` for visual-only. When sound
is allowed, omit `silent`, preserving existing browser-default behavior; do not
promise a sound will play. Lead's official evidence is
[Firefox 132 release notes](https://developer.mozilla.org/en-US/docs/Mozilla/Firefox/Releases/132)
documenting `Notification.silent` support, with bug 1809028. Check the native
`Notification.prototype.silent` capability and final MDN/BCD evidence; absence
must make visual-only unsupported explicitly, not silently advertise success.
API presence/recorded options do not prove audible behavior or OS compliance.
No Web Audio, audio file, synthetic background sound or OS-setting workaround.

### Persistence and display

Own this one preference in the existing `workspaceAttentionStore` IndexedDB
database, not localStorage plus a second copy, server registration state or push
payload. Add small read/write helpers for a reserved singleton record in the
existing version-1 `sessions` object store, using an identity outside session and
Test identity patterns and one strictly boolean sound field. Exclude that exact
record from the current 512 attention/Test record eviction; do not count it as a
session. No database version upgrade, new object store, private server schema,
API, key or outbox migration. Existing absent state means sound allowed; a
present malformed record is unavailable rather than silently interpreted as
permission for sound. Disable/re-enable retains the preference; clearing browser
site data resets it. Old data stays readable. Old loaded clients/workers do not
implement the new choice and are outside the existing new/refreshed-tab contract;
no compatibility protocol or retrofit is required.

Read/write the checkbox through that helper. Show saved state only after the
write transaction commits; on failure retain/re-read the last known value and
report that saving failed. Bound storage work; do not declare a timeout a
successful save or let a stale read overwrite a newer selection. Abort a timed
out write transaction where available and reconcile any uncertain outcome.
Reuse existing page lifecycle/observation guards. Read on opening/revisiting
either panel; last committed write wins across tabs. No live multi-tab preference
synchronization framework is required.

For each incoming push, take one bounded local preference snapshot and apply its
sound option to every `showNotification` branch: Test, ordinary input/done,
neutral/stale, missing-session/auth and malformed-payload fallback. This adds no
network request. A read failure/timeout/malformed record falls back to requesting
silent visual display, not dropping the notification or enabling unexpected
sound. Keep a known missing record distinct from read failure. The value at the
display attempt governs; changing it cannot recall a provider-queued message or
alter an already displayed notification. Preserve display rejection diagnostics;
never retry a rejected silent call without `silent` to make it appear successful.

Subscription, permission, VAPID keys, registration/cleanup selectors, Test
correlation, TTL, tags, ACK, presence and session mute remain unchanged. Preserve
automatic worker activation/current-controller checks, open documents and drafts.
Current controls must not imply the new preference is effective while worker
activation is unconfirmed; reuse that limited-readiness state without a new
negotiation protocol. The browser and OS retain final control of sound/display.

### Owning paths, checks and rollout

Scope: shared `templates/notifications.html`, `static/browser-notifications.js`,
`static/session-attention-store.js`, `static/notification-worker.js`, their
existing module/template/real-browser tests, and the two notification guides.
Update asset query versions in owning templates/imports if needed. Main agent
owns visible copy approval and the writing skill; no server sender/store change.

Quick tests: missing/true/false/corrupt state; commit and read failures/timeouts;
singleton survival past attention pruning; panel persistence/revisit; unsupported
silent capability; latest-write/read ordering; every display branch's exact
options; read failure still attempts silent display; rejected silent call stays
rejected without audible retry. Retain existing subscription/permission/Disable,
Test and session acknowledgement regressions.

After committed quick checks and affected independent review, finite browser
fixtures cover Firefox and Chromium native silent capability, shared panel
persistence on a new/refreshed page, unchanged registration and in-place worker
activation with another controlled tab open. Chromium-only worker evaluation
may verify synthetic Test/session options and correlation; actual-module tests
cover all branches. Do not invent a Firefox production test API. Browser
notification records/options are implementation evidence, not acoustic proof.
Final real Firefox/macOS acceptance is one explicit Test in each choice plus a
background session event with visual-only selected; record popup and actual
sound separately under the user's OS settings. Sound-allowed remains permission
to use native sound, not an unconditional audible result.

Lead owns final downstream pins, review/long-check selection and authorized
ordered deployment. Recovery uses a compatible forward successor and preserves
the local preference and all existing private state; do not reset keys or browser
data. No code, test, browser/provider, host or lifecycle operation is performed
by this brief, and no merge or reservation release is authorized.

## Notification click destination: bounded investigation

**Sound remains accepted and independent.** At deployed `46975718`, the click
handler already uses `clients.matchAll({type: "window", includeUncontrolled:
true})` and matches exact same origin plus pathname, not full URL. Different
`?member=...`, `attentionIdentity` and section hashes do not prevent reuse. It
then navigates the selected client to the validated notification route and
focuses it; `openWindow` runs only when no matching pathname was enumerated.
This source does not establish the user's exact runtime cause.

`attentionRoute` produces `/<slug>/#codex` for lead/done, or
`/<slug>/?member=<address>#codex` for member input. Reused tabs intentionally
select that member/conversation instead of retaining their previous Settings or
other section. The page's member selector also navigates to that query and hash.
Worker click navigation adds the validated attention identity; the server checks
it against the current session incarnation. Keep those checks and ordinary
authentication. Client enumeration does not include another origin/profile, and
the worker has no cross-profile authority.

The concrete Test distinction is `displayTest`'s saved `data.route: "/"`, also
the server Test payload route. A Test sent from session Settings therefore seeks
an existing home tab, not the originating session tab, and opens home if none
exists. It does not save the initiating page. This is a source-supported
explanation **if the user clicked Test and the new tab was home**. Lead has asked
Test versus session notification; do not change general session matching or
claim a proved incident cause before that answer.

If that Test case is confirmed and the lead selects return-to-origin behavior,
the smallest correction is local only: retain an optional canonical return
route beside the exact pending Test descriptor in the existing browser store.
For session controls, construct it from validated session/member metadata with
`#codex`, not arbitrary current query/hash data; dedicated browser controls may
retain the existing home fallback. The worker may copy a return route only from
the record matching all descriptor identity/id/revision/expiry fields, after
applying the existing strict same-origin route validation. Missing, malformed or
unreadable local metadata falls back to home and must not delay/prevent display.
Do not put a test identity into the session attention-identity field. No API,
server outbox/payload, subscription or session-state change is needed.

Conditional owning scope: worker, notification client/shared-store Test metadata
helpers, their existing Node/browser tests, and a brief guide clarification;
separate coherent correction from sound if assigned. Preserve click validation,
member grammar, authenticated navigation, no authenticated caches, current
focus-ack rules and ordinary no-match `openWindow`. No broad tab registry,
cross-origin lookup or automatic conversation mutation.

Quick regression coverage should first pin existing behavior: same session path
with different member/hash reuses navigate+focus and passes the intended member;
other origin/session does not match; invalid routes are refused; Test home target
does not treat a session tab as home. For the conditional return route, add exact
descriptor match/mismatch/storage-failure and malicious-route cases. A real
Chromium click fixture can keep a session tab on Settings/member variant, use the
actual worker's notification-click handler with synthetic data, and assert tab
count unchanged plus intended route/member/focus. Label that plumbing proof;
do not claim a physical macOS click or use unavailable Firefox worker evaluation.
If the user instead clicked a real session notification, retain current matching
and first obtain only its target origin/path and the existing tab's origin/path
(no credentials/query dump); the present evidence justifies no matching rewrite.

This is a pending click investigation/conditional brief, not a source assignment.
No test, browser, network, provider, host or lifecycle operation was performed.

### Clarification: likely Response finished, not Test

The user subsequently recalls **Response finished**. Treat this as a session
event; the Test-return proposal above is not selected for implementation. Lead
is asking whether the new tab opened the correct session and the same hostname.

There is a concrete accepted-route mismatch in `46975718`:
`server.go:766-767` trims surrounding slashes and renders `sessionPage` for both
`/<slug>` and `/<slug>/`, with no canonical redirect in that handler. Notification
routes from `attention.go:156-162` always use `/<slug>/`. The worker's literal
pathname equality does not match an existing slashless session. This establishes
a real missing reuse case, not proof the user's tab used that form. Query/member
and hash variants already match. No evidence establishes a Firefox enumeration
bug, a focus restriction, different browser container/profile, or hostname
alias in the incident. `includeUncontrolled:true` is already used; it does not
provide access to other origins/profiles. The source does not record the client
list seen at the actual click.

The narrow route correction, if assigned, is strict session-path equivalence
for an optional final slash on the same validated slug and exact origin. Do not
use path-prefix matching, remove arbitrary segments, decode encoded separators,
or match another origin. Leave home distinct and preserve target member grammar,
canonical destination, attention identity and ordinary authenticated navigation.
Pin this case with a focused worker regression and server-handler assertion
that both path forms are accepted. This fix stands on source evidence, but a
green test would not explain the user's original same-slash incident if that
turns out to be their URL.

Separately, `notification-worker.js:114` unconditionally awaits
`existing.navigate(route.href)` before focus. It adds `attentionIdentity` even
when the existing conversation/member is already correct. That requests
navigation and can reload document state; do not retain it as an automatic
fallback when focus would suffice. Its failure cannot itself explain this
handler's `openWindow` branch, which is reached only when no match was found.
For a later focus correction, first prefer an existing tab already on the target
member; preserve its draft and document. A focus-only path must not pretend it
performed the server's incarnation check: either keep it strictly as focusing
an existing view without event acknowledgement/selection, or use a bounded
existing-page message that validates rendered observation identity before
selecting `#codex`. Do not bypass stale-incarnation protection or introduce a
general tab registry. A different-member fallback needs a deliberate decision
about navigation versus keeping that tab's draft; it is not justified as an
unconditional reload by this report alone.

Minimum meaningful regressions: slashless/slashed same-session reuse; different
hash/member queries reuse without a new tab; exact-member preference if added;
other-origin/session rejection; no matching client opens the canonical route;
focus-only preserves a document/draft sentinel. Chromium's real worker click
fixture can verify tab count and navigation behavior with synthetic notification
data. Firefox/macOS click acceptance remains actual user evidence, not synthetic
worker-evaluation coverage. Obtain the already-requested safe origin/path facts
before claiming the incident repaired; no retry or browser operation is assigned
by this investigation. Sound work proceeds independently.

### Latest correction: Firefox foregrounds, relevant tab is not selected

This user correction supersedes the new-tab symptom above. No new tab creation
is established. The Test-return and trailing-slash explanations are not incident
conclusions; the independently identified slashless reuse gap remains a separate
source fact. Hostname/origin equality and the client chosen during the actual
click remain unconfirmed. Sound implementation continues independently.

The concrete sequence in `46975718` is still
`await existing.navigate(route.href); await existing.focus()`. A rejected or
unresolved navigation prevents/delays the focus call, and the returned
`WindowClient` from navigation is ignored. There is no branch outcome evidence
from the user's click, so neither navigation failure nor Firefox focus rejection
is established. Browser foregrounding alone does not prove `WindowClient.focus`
ran or fulfilled: the browser may foreground as part of notification interaction.
No inspected evidence establishes a Firefox/macOS-specific focus limitation or
proves aliases, container isolation, permission failure or a browser defect.

For the clarified requirement, the smallest defensible correction is to focus
the existing matching session tab directly, without navigating/reloading it.
That removes the source-visible navigation dependency and preserves its draft,
section and selected member. Prefer an already matching target-member tab when
several session tabs exist; otherwise focus the matching session view without
silently changing its member. This is tab selection, not delivery of a new
conversation command or proof of event-incarnation validation. Keep ordinary
visible/focused attention acknowledgement unchanged; do not mark the notification
event read from the worker. Canonical authenticated navigation with the validated
attention identity remains for the no-existing-tab path. Do not add a message
protocol merely to force section/member changes not requested by this correction.
Lead must select this boundary before a separate click source change; the
actual user's focus outcome would still need confirmation.

Meaningful quick coverage must expose the harness's existing window list and
assert that a matching client receives exactly one awaited `focus()` and no
`navigate()`/`openWindow`, regardless of query/hash; include a navigate stub that
would reject to prove it is not on the focus path. Cover exact-member preference,
same-origin/strict-path boundaries, no match, invalid route, rejected focus and
closed-client behavior without an automatic duplicate-tab retry. Keep failures
observable in bounded test output; do not claim a fulfilled focus from a void
mock proves actual selection. The current harness tests only empty window lists
and therefore supplies no existing-tab regression evidence.

The smallest further incident evidence is the already-requested safe origin/path
comparison plus one actual authorized Firefox/macOS notification click with a
different tab active, recording whether the intended tab becomes selected. A
bounded diagnostic, only if needed, should record matched-client count and
focus requested/resolved/rejected category, never URLs with queries, payloads or
private state. Synthetic browser handler invocation cannot establish OS focus
or trusted user-activation behavior; real-browser tab/draft checks must state
that limit. No probe, diagnostic implementation or rerun is authorized or
performed by this planning update, and no causal repair is claimed.

#### Accepted minimal focus contract

Accepted by lead; implementer queues this as the separate ninth owning commit
after the eighth sound-preference commit. The user confirms clicking correctly
creates a session tab when that session is not open; preserve this no-match path
exactly. Existing-tab Firefox/macOS selection remains unproved until the user
checks the deployed correction. Architect design is complete and on hold.

Choose focus-only reuse, not focus-then-navigate or navigate-then-focus. In a
separate click commit after sound, keep strict validated notification routes and
same-origin lookup; recognize the same session slug with or without its final
slash. Prefer a matching tab already on the target member (absent member means
lead), otherwise use the existing matching session view. Await that client's
`focus()` exactly once. Do not navigate, reload, change its member/section or
send a page message. Existing draft/document state remains intact. For a home
target, only a same-origin home tab matches; do not revive the Test-return idea.

Only when no matching client exists, retain `openWindow` of the canonical
validated destination with its existing session attention-identity guard.
Rejected focus or a client disappearing after enumeration must not trigger an
automatic new-tab retry. Preserve promise failure semantics; there is no new
success receipt, logging framework or persistent click state. Focusing an
existing view performs no new incarnation/authentication check and must not be
described as one; it performs no worker acknowledgement or conversation action.
Normal focused-page observation keeps its existing session identity checks.

This makes the discarded `navigate()` return value irrelevant on reuse; using
that returned WindowClient would matter only if navigation were still required.
The demonstrated source concern is unnecessary navigation before focus and the
uncovered slash variant. Neither proves why Firefox merely foregrounded in the
reported click. Scope is the worker and existing focused Node/Chromium browser
regressions (plus a concise guide sentence if needed), with the cases above;
no client protocol, server or storage change. Actual Firefox/macOS tab selection
remains a post-change user check, not a promise from synthetic tests.

## Quick workspace-menu sound control

**Superseded by the combined browser-controls amendment below.** In particular,
the separate sound module and index-no-full-initializer requirements here are
no longer implementation constraints; use one existing control owner instead.

**Bounded amendment to the accepted sound commit.** The user wants a quick
global sound switch for this browser, independent of per-session delivery.
Add **Play sound** to the shared `sidebar-menu` template in `templates/index.html`,
used by index and session pages. Retain its Browser notifications link and the
full dedicated/Settings panel with guidance. The switch changes the same single
origin/profile-wide IDB preference already specified; it does not turn session
notifications on/off or affect other browsers. Main owns final copy approval.

Read-only inspection of the in-progress sound work found its control/read/write
logic currently inside `browser-notifications.js`. Extract that bounded sound
controller into one small owning module, for example `notification-sound.js`,
loaded after the existing store on index, session and dedicated controls pages.
Bind all sound controls in the document through that owner. Do not copy the
handler into menu code, add another preference, mirror storage, or load the full
notification initializer on the index. Existing store and worker contracts,
singleton pruning protection, default, silent fallback and save-failure behavior
remain unchanged.

On native popover open (`toggle` with open state), reread the persisted choice.
Keep one saved value, write-in-progress state and generation guard per document;
disable all its controls while saving and update every menu/panel instance only
after commit. A failed/uncertain write keeps or re-reads actual saved state and
shows an accessible bounded error; do not present a successful mute. Re-read on
visibility/pageshow and Settings reveal; last committed cross-tab value wins.
No polling/synchronization framework is required. Use distinct accessible hint
and status IDs per surface; preserve native checkbox keyboard operation, menu
Escape/focus behavior and usable spacing at narrow widths.

Menu saving and worker readiness are separate facts. Reuse the single existing
bounded current-controller readiness implementation; if needed, extract it with
the small controller and let the full client consume its result rather than
duplicating it. Menu-open may check/update an **existing** root worker through
native service-worker APIs so the setting can take effect; no registration is
created. No sound success/capability claim may be inferred merely from IDB save,
`registration.active`, native `silent` presence or an old Test-support reply.
Keep existing activation/current-controller checks and honest unconfirmed or
unsupported status. A preference can be saved before delivery is enabled, but
must not be described as immediately effective without confirmed current worker.
Index load or menu use must never request permission, subscribe/unsubscribe,
call registration/Test/presence/session-mute APIs, or reset keys/state. It must
not initialize the full panel. No tab is closed or reloaded by these controls.

Owning amendment paths: shared sidebar template and script includes in index,
session and notifications templates; the small sound module; removal of the
duplicated panel sound owner from `browser-notifications.js`; minimal menu style
if needed; existing module/template/browser tests and notification guides.
No API or payload extension. Preserve the first seven deployed source objects;
lead/implementer own the final coherent eighth sound commit and separate ninth
focus-only commit. User confirms the focus issue involves the same Firefox
window; this does not establish its cause or change the accepted focus contract.

Acceptance: menu-open reflects a choice saved elsewhere; toggling either control
updates the other on the same session page; reload/revisit retains it; changes
apply to both Test and session/fallback displays and never change session mute.
Cover write/read failure, stale read, unsupported capability and unconfirmed
worker without fabricated success. Browser fixtures in Firefox and Chromium
exercise index/session menus, Settings consistency, keyboard/narrow layout and
persisted reload, and assert opening/toggling makes no notification permission,
subscription, Test or session-mute mutation. Index remains free of the full
initializer. Reuse the existing worker option/activation tests; no new native
provider run is implied. Committed quick checks and affected review precede
longer verification under lead ownership. Only design was edited here.

## Combined menu controls: browser delivery and sound

**Accepted by lead and released to implementer; supersedes the sound-only menu
brief.** The eighth owning commit now provides quick controls across all sessions
in this browser/origin; focus-only click correction remains a separate ninth.
Preserve the seven deployed source objects. No application edits or operations
were performed for this amendment.

Use the shared sidebar menu on index/session pages for a concise current browser
status, the existing **Enable browser notifications** / **Disable on this
browser** actions, **Play sound**, and the existing Browser notifications link.
Use buttons rather than a boolean delivery switch: setup and cleanup have real
incomplete states. Keep Test and detailed guidance in the full panel. Main owns
the actual final wording/layout diff before commit.

Retain `browser-notifications.js` as the single per-document owner of delivery,
sound, busy state, generation guards, readiness and cleanup. Bind collections of
menu/panel controls to the same actions and rendering; do not forward clicks to
a hidden panel or duplicate business logic. The index may load the existing store
and this bounded owner with absent panel/Test elements handled safely. A new
controller framework or mandatory separate sound module is unnecessary. Session
menu and Settings controls must always reflect the same committed state, and
one pending action disables competing controls on both surfaces.

Loading the index and opening the menu may read existing local subscription,
saved preference/cleanup selectors and existing status GET. Re-read on menu-open
and visible revisit with current generation guards. They must not request
permission, register/subscribe, Test, Disable, write session mute, or repair
subscription state automatically. Keep worker-update/readiness behavior within
the existing bounded owner and distinct from subscription mutations; never
claim current activation merely from saved preference or an active old worker.
No page closure, reload or new activation protocol is introduced.

Only an explicit menu or panel Enable invokes the existing permission request,
worker registration, subscription and authenticated server registration path.
Only explicit Disable invokes the existing independent server and local cleanup
path, including both saved old ID and current endpoint digest obligations.
Fully off requires confirmed server removals and local absence. Partial failure
must say incomplete/server cleanup pending, preserve retry selectors, and keep
Retry Disable usable; Enable stays blocked by pending cleanup. Do not introduce
a pause flag, tombstone, second subscription owner or new server API. Site
permission remains unchanged by Disable. An already provider-accepted message
cannot be recalled; do not promise instantaneous cancellation of in-flight push.

Sound uses exactly the existing single IDB preference. It can be saved while
delivery is off and survives Disable/re-enable. Render checked state only from a
committed/read value; keep unsupported, failed save/read and unconfirmed worker
states honest on both surfaces. Default sound-allowed, `silent:true` when off,
bounded silent fallback and native OS limits remain as previously accepted.

Per-session delivery settings remain untouched and take effect again on browser
Enable. **Session title attention and reservation markers remain independent**
of browser registration and sound. Keep `session-attention.js` observation,
rendering, focus acknowledgement and reservation reads running with browser
delivery disabled; the optional presence hook may return early, but cannot stop
title processing. Menu actions neither acknowledge a session nor release holds.

Owning paths: shared menu/full-panel templates and their index/session script
includes, single notification client, existing sound store/worker additions,
minimal menu styles, existing module/Go-template/browser tests and the two
notification guides. Update changed asset query versions consistently. No server
store/API, private-state schema, notification payload or per-session mute change.

Quick tests cover same-document menu/panel consistency, one action under competing
clicks, persisted sound across global Disable/re-enable, all existing incomplete
cleanup cases, stale status reads and absent full-panel elements. Assert no
permission/subscription or mutation requests on load/open. Prove unseen input/done
and reservation title markers still update with no browser registration and with
sound off; focus still acknowledges only the matching observed session. Browser
fixtures in Firefox/Chromium cover menu on index/session, keyboard and narrow
layout, saved state on reload, explicit action routing, and unchanged session mute.
Keep existing Chromium-only synthetic push and module coverage boundaries; do not
claim native acoustic or macOS focus acceptance from them. Committed quick checks,
affected review and later lead-owned verification/deployment retain their order.

Architect handoff complete: retain the single control owner and existing
Enable/Disable cleanup paths, with no pause flag. Lead owns final copy, review,
verification and deployment. Further architect work is on hold unless a material
implementation deviation needs a decision; session and reservation remain open.

### Reserved sound record retention with already-open pages

**Accepted by lead and released to implementer:** exact three-field unconsumed
format plus the old-pruner regression; no dual reader or compatibility framework.

Bounded source finding before final review: deployed `46975718`'s loaded store
sorts every record by `b.at - a.at` and deletes entries beyond 512. The new
two-field sound record has no `at`; comparisons involving it yield NaN, providing
no retention guarantee. With enough existing keys preceding its reserved key,
it can remain beyond the cutoff and be deleted. A current worker then interprets
absence as the default sound-allowed choice. This threatens the new setting's
persistence while supported old tabs remain open, not merely old notification
semantics. The new pruner's exclusion cannot constrain an already-loaded writer.

Recommend the smallest correction: write the singleton as exactly
`{identity: soundIdentity, playSound: boolean, at: Number.MAX_SAFE_INTEGER}` and
strictly validate that exact retention constant and field set when reading.
For this reserved identity only, `at` is a fixed retention rank, not a wall-clock
timestamp. It sorts ahead of valid `Date.now()` attention records under the old
algorithm. Keep the new exact-key pruning exclusion. The old writer may retain
511 attention records plus this preference; the new writer retains 512 plus it.
Never pass the singleton through the ordinary attention-update timestamp writer.
No database/version change, mirror, migration or refresh loop is needed.

The two-field sound format is still uncommitted/unreleased implementation, not
a supported deployed state; update its strict reader/writer and fixtures together
rather than add a second-format recovery layer without consumption evidence.
Focused quick coverage should save explicit false, apply the exact old pruning
algorithm to more than 512 valid attention records with adversarial key order,
and prove retention plus current `readSound()` remains false; also cover new
pruning, true, invalid/missing retention metadata and unchanged missing-record
default. No test was run here. Do not broaden into general old-client
compatibility. Architect work is on hold unless a material implementation
deviation needs a decision; final copy, review, verification, pins and rollout
remain lead-owned.

### Located browser-fixture failure: popover dismissal focus

**Bounded investigation / recommendation, pending lead assignment.** Exact clean
published source `6c7d3851b005b47357e43688efccddde56f4e53b`, session/environment and
roster rev17 verified. The sealed diagnostic
`notification-controls-browser-diagnostic-6c7d3851/run/summary.json` records
`active_with_fixture_location`, `exception_located`, line 297 column 65 twice,
category `other`, checkbox exception false. This locates that diagnostic run's
`expect(toggle).toBeFocused()` after Escape. It does not establish the original
unlocated run's cause or a failed sound write. Preserve both results separately.

At that point the fixture has mouse-opened the menu, checked sound, confirmed
the committed IDB value and the full-panel checkbox, then pressed Escape. The
earlier explicit keyboard open (focus toggle, Enter, assert Operations focused)
and Escape-return assertion at line 259 passed. The menu is a native auto
popover with an autofocus link; `app.js` only positions it. The sound owner
temporarily disables all sound controls while saving, then re-enables them
without restoring focus. Disabling a focused input can remove focus; re-enabling
it does not establish that focus returned.

Native popover restoration is conditional on its saved pre-open focus and the
focus still being inside the closing popover; Escape is not an unconditional
instruction to focus the toggle after arbitrary pointer/async interactions.
Thus the line-297 assertion assumes a focus precondition it never establishes.
The diagnostic does not capture pre-Escape active element or popover state, so
it does not prove whether disabled-control focus loss caused this instance.
Pointer opening alone is also not a portable guarantee of which element held
pre-open focus. This is not evidence for a speculative Playwright checkbox fix.

Recommend the smallest immediate correction in
`portal/internal/web/notifications_browser_test.cjs` only: keep the mouse-driven
sound/persistence/panel/layout sequence, press Escape and assert the popover
actually closed. Keep the existing explicit keyboard Enter/autofocus/Escape
restoration test, and exercise that explicit keyboard sequence again after the
sound save (focus the toggle before Enter, assert focus is inside before Escape,
then assert return to toggle). Do not simply drop Escape or all focus assertions,
change check/uncheck, insert sleeps, or extend deadlines to get a pass. This
separates actual menu dismissal from keyboard restoration under known conditions.

The source-supported possibility of lost focus when a keyboard user changes the
sound checkbox is a separate accessibility concern; the located pointer-driven
assertion does not settle it. If lead elects to require continuity through that
async action, first cover keyboard focus -> Space -> committed save with finite
focus-state evidence. A product remedy would belong narrowly to preserving the
initiating control's focus after its own save, only while that menu remains open
and the user has not moved focus. Do not add unconditional focus-on-menu-close,
refocus every enabled control, or steal focus from another tab/element. That
product change is not selected by this recommendation without the additional
keyboard evidence or an explicit lead behavior decision.

Quick checks: fixture syntax and the existing focused quick checks, inspect the
diff to retain every persistence, layout, permission, shared-control and worker
assertion. If a bounded failure snapshot is needed, use only fixed categories
for menu-open and active element (toggle/menu-control/menu-link/other), never raw
DOM/errors/URLs. After committed quick checks and affected independent review,
one fresh exact-head fixture in Chromium and Firefox is justified by the corrected
focus preconditions; retain failure and diagnostic evidence. Do not treat a green
run as proof of the original cause or macOS notification-click focus. No browser,
test, source, host or lifecycle operation occurred during this investigation.

### Located 55af fixture failure: retained-page navigation counter

**Bounded fixture-only recommendation for lead assignment.** Verified clean
`55af728332471ef16a9587723c6964c563227748`, bound session/environment and roster
rev17. The sealed `notification-controls-browser-diagnostic-55af7283/run/summary.json`
locates line 238 column 92 three times: the final retained-page
`assert.equal(navigations, 0)`. The separate line 47 location is in the failure
snapshot. No raw count or navigation history was captured; the ordinary 55af
failure remains unlocated. This diagnostic reached synthetic push/display,
sound-option and click assertions. It supplies no basis for changing worker
handle selection. The trace records GET/register only, so absence of a Test POST
there is not evidence that Test was never reached.

The source establishes an incorrect counter boundary. The retained main-frame
listener starts at line 97 and correctly proves zero navigation through takeover
at line 114. The fixture then explicitly clicks Settings at line 152. That link
has `href="#settings"`; its application click listener selects the panel without
preventing native fragment navigation. This intentionally leaves `#codex` and
belongs to fixture setup, but the cumulative counter is reused as zero at the
notification-click assertion. Only the controls-page counter is reset after its
explicit reloads. Current worker click handling focuses a matching session window
without navigating it. These source facts justify correcting counter ownership;
they do not reconstruct every event in either failed execution.

Change only `portal/internal/web/notifications_browser_test.cjs`. Prefer accounting
for the deliberate Settings transition at its exact boundary: assert no unexpected
retained navigation before that click, arm a main-frame `framenavigated` wait for
the fixture's Settings destination before clicking, await that event and the click,
and verify the expected single transition/current section. Then reset the retained
counter immediately, before sound persistence continues. Keep the final zero
assertion; it now covers sound save, delivery and notification click rather than
counting the fixture's own section change. This is narrower than discarding all
retained navigation accumulated during the entire sound setup. Use existing finite
fixture timeouts; no sleeps or extended deadlines. Keep takeover/controller,
capability, keyboard, persistence, subscription, correlation, silent-option,
page-count/URL, sentinel and draft assertions intact. Give the phase assertions
fixed descriptive messages so a later failure identifies the boundary without
printing raw browser state.

History ownership is confirmed from `git show 55af7283` and line blame: the final
zero-navigation/sentinel/draft assertions predate both new commits (`46975718`);
the eighth commit `97ebdc0a` introduces Settings navigation and the controls-only
reset; the ninth adds the synthetic click block ahead of unchanged assertions.
Therefore amend the owning eighth fixture setup and replay the ninth unchanged,
if authorized by lead. Preserve the exact first seven deployed objects and the
old 55af ref/evidence. Report the eighth's changed patch and prove ninth patch
equivalence; do not claim all nine original commit objects remain identical.
This brief authorizes no history operation by the architect.

No production asset, worker protocol, API, storage, lifecycle or deployment change
is warranted. Quick verification is fixture syntax/diff plus the owning focused
checks and confirmation that production blobs remain unchanged. After committed
quick checks and affected fixture review, one fresh exact-head Chromium/Firefox
fixture can verify the corrected boundary; Chromium retains synthetic delivery
and click coverage, Firefox retains its native takeover/control/persistence scope.
Lead owns authorization and execution. A green result cannot establish the cause
of the original ordinary failure or physical macOS focus/sound behavior. Preserve
all previous evidence; no browser, test or product operation was run for this brief.

### Located 197 fixture failure: native subscription-read availability

**Bounded recommendation, pending lead acceptance.** Verified clean published
`197782df20a0776842fb914ba2a2caa674b45186`, bound environment/session and roster17.
The sealed `notification-controls-browser-diagnostic-197782df/run/summary.json`
locates the pre-sound snapshot `controls.evaluate` at 137:20 three times; 47:49
belongs to the later failure snapshot. Native takeover, current-controller
capability and sound-support/render assertions had already passed. The evaluation
contains registration lookup, `getSubscription()` and optional serialization;
the projection does not isolate an inner call or capture its exception category.
Do not label permission, provider, headless operation or worker readiness as the
established cause. The ordinary 197 failure remains separately unlocated. Lead
records Chromium main/upgrade/sound/click and Firefox main passing in that run;
the full flake remains unrun.

Adapt only the eighth commit's sound snapshot in
`portal/internal/web/notifications_browser_test.cjs`. Keep real registration
lookup and assert a present registration, then compare the exact same registration
object after the sound save. Catch only the native `getSubscription()` invocation
and await, never the surrounding evaluation, registration lookup, serialization,
controller assertions or sound operations. Represent its result as readable
(including an actual null subscription) or unavailable with a finite native
DOMException category. A small local fixture function is enough; no reusable
exception framework or production interface. Recognized categories may be
`AbortError`, `InvalidStateError`, `NotAllowedError`, `NotSupportedError`,
`SecurityError` and native `UnknownError`; this is an observation enum, not a
claim about the recorded failure. Any non-DOMException or unrecognized exception
fails with fixed safe wording, rather than comparing two generic `other` values.

Require readable snapshots on Chromium. On Firefox allow either two readable
snapshots with identical serialized subscription identity, or two unavailable
reads with exactly the same recognized category. Readable/unavailable changes,
category changes, absent/replaced registrations and unequal readable snapshots
fail. Keep subscription JSON in page memory for comparison; return/log only the
engine, finite read outcome/category and comparison booleans, never endpoints,
keys, raw errors or stacks. The one explicitly recorded unavailable result means
native subscription identity was **not verified**; do not turn it into null or
claim absence. Same registration identity, zero register/disable POSTs throughout
sound interaction, unchanged native controller proof and committed preference
checks remain independent evidence. This limitation is preferable to granting
permission or altering native push behavior just to make a snapshot readable.

Retain both engines' native lifecycle, current-controller, keyboard, sound
save/reload/shared controls and navigation/draft coverage, and all Chromium
synthetic delivery, correlation, silent-option and click assertions. No permission
grant, resubscribe, mocked Firefox API, product change, retry loop, added timeout
or worker-handle change is selected. The next authorized fixture execution can
report the finite native category directly; no separate broad diagnostic run is
needed. If failure is outside this narrow native-read boundary, preserve it and
stop rather than widening the catch.

Quick checks: fixture syntax, existing focused checks, and inspection that changed
read outcomes cannot pass and production blobs remain unchanged. Preserve the
first seven deployed objects and all 197 evidence; amend the owning eighth and
prove unchanged ninth replay only under lead authorization. After committed quick
checks and affected fixture review, one fresh exact-head Chromium/Firefox fixture
checks the adaptation. An unavailable comparison cannot prove native subscription
identity. A green run cannot establish the old inner exception, physical macOS
display/sound/focus, or the unrun full flake. No state/schema/rollout change follows;
no source, browser, test or operational action was performed for this brief.

### Compact notification menu over deployed 1038

**Implementation brief for the user-accepted compact-menu plan.** Source is clean
at deployed `1038d4abdde8b115c21b5940b14be637cfa967b6`. Current resolved to this
thread-bound session from its tracking directory; both environment variables are
absent and roster17 retains architect0's design/workspace-write settings. This
supersedes the menu presentation in the combined-controls addendum, not its
single-owner delivery/cleanup or sound-persistence contract. Implement as one new
coherent tenth commit; preserve the first nine deployed objects and sealed evidence.

The notification section of the shared index/session workspace menu contains
exactly two native labelled checkbox rows, **Notifications** and **Sound**, then
a small **Notification settings** link to `/browser-notifications`. No ordinary
help, checking/saving/success text, provider/Test status or Enable/Disable buttons
belongs in the menu. Allow one brief error region only when needed, as the user
requested. Keep full guidance, detailed status, Test and explicit recovery buttons
in the dedicated page and existing session Settings panel. Remove the section's
fixed `22rem` width; use content sizing within existing viewport bounds, compact
row spacing and wrapping errors. Preserve other navigation entries, Operations
autofocus, native popover opening/dismissal, mobile positioning and keyboard access.

Keep `browser-notifications.js` as the sole owner. Extract the existing Enable and
Disable listener bodies into private functions used directly by full-panel buttons
and the menu checkbox, with their existing guards, locks and sequencing. Never
dispatch synthetic button clicks or duplicate registration/compensation logic.
The owner's initialization must accept a menu-only page without requiring a
`data-notification-status` element; absent detailed sinks are harmless. The menu
gets its own delivery-toggle and error hooks; Sound uses the existing sound hook.

The Notifications checkbox describes confirmed browser setup, not guaranteed OS
display. Its rendering is a small local projection of the owner's observations:

| Observation | Menu checkbox / action |
| --- | --- |
| Successful Enable, or a fresh valid read confirms eligible server registration, current local subscription, granted permission and no cleanup obligation | Checked; unchecking directly invokes existing Disable. |
| Confirmed local absence and no known server registration/saved-ID/cleanup obligation, including completed Disable | Unchecked; checking invokes existing Enable when supported and permission is not blocked. |
| Initial/unreadable/retired observation, incomplete setup/cleanup, or contradictory local/server evidence | Disabled and indeterminate (mixed); no optimistic on/off claim. Completed read/action failures get the brief error and settings link. |
| Unsupported browser, blocked permission or server-disabled delivery | No actionable toggle; show a brief reason. Use mixed when setup/cleanup remains uncertain, otherwise the confirmed off value. Recovery stays in settings/browser controls. |

During an action, immediately undo the browser's optimistic checkbox toggle and
render the previous confirmed value disabled until the existing operation proves
its outcome; an incomplete outcome becomes mixed. A refresh in progress cannot
enable actions from stale evidence. Keep any projection fields in this controller
only: no persisted flag, new server state or generic state framework. A failed read
cannot become off just because `registered` was set false. Do not infer successful
delivery from permission, a worker, provider acceptance or a message string alone.
Shared menu/panel locks prevent competing enable/disable/sound actions. Sound stays
editable with delivery off when its existing native/storage preconditions permit;
its checked state still changes only after a committed write or verified reread.

The same owner selects a fixed, short menu error category at the existing failure
branches; it must not parse detailed DOM text, truncate arbitrary exceptions or
show backend strings. Keep detailed settings messages as they are. Render at most
one brief notice with the always-present settings link: prioritize cleanup/setup
or retired/read failure, then explicit delivery failure/blocking, then sound
save/read/unsupported failure, then an actually failed worker-update check. Normal
loading, saving, worker checking and a delivery-off browser with no worker are not
errors. Test progress/outcomes and registration-wide provider history stay in the
full panel. Associate the short notice with affected controls using accessible
description/live-status markup; hidden means no empty status space in the menu.

Error state is transient and domain-owned: opening/closing the menu does not
discard it; starting a retry removes only that action's obsolete notice, and only
the current action or fresh matching observation may clear its resolved failure.
Sound success cannot clear uncertain delivery cleanup, and a delivery refresh
cannot clear a failed/unreadable sound setting without its own reread. Retired or
superseded results cannot change either the checkbox or notice. Reuse existing
generation, pagehide/storage retirement, cleanup-ID/digest and test-retirement
fences; do not alter their deadlines or add background retries. Main owns final
short error wording and all visible copy approval.

Files: shared menu in `templates/index.html`, `static/browser-notifications.js`,
menu rules in `static/style.css`; owning module contracts in
`attention_browser_test.cjs`, template checks in `notifications_test.go`, and
actual template fixture in `notifications_browser_test.cjs`. Update the two
owning notification guides and client/style cache queries in their existing
consumers where assets change. Session/dedicated templates need only necessary
asset references; the full panel remains. No worker, attention/store, server/API,
protocol, private persistence, key/permission/subscription format, session mute or
title behavior change. Loading/reopening the menu performs only existing reads
and worker-update checks, never permission/register/subscribe/Test/mute mutations.

Quick verification must cover menu-only initialization; known on/off/mixed and
blocked states; immediate visual restoration through delayed Enable/Disable;
partial server/local cleanup and old-ID/digest obligations; shared panel/menu
locks; stale/retired response rejection; brief error priority/clear rules; and
independent committed Sound while delivery is off. Keep existing title/session
mute independence tests. Template checks require exactly the two menu checkbox
rows/link and no detailed controls/help; full-panel contract stays intact. Run
declared syntax, focused module/template checks and diff review before committed
affected independent review, all lead/implementer-owned.

Then one finite exact-head Chromium/Firefox actual fixture verifies compact
desktop/mobile fit, both keyboard and pointer dismissal, menu/panel consistency,
read-only opening and sound save/reload. Exercise the checkbox action through the
existing Chromium synthetic-subscription scope; Firefox retains native lifecycle
and honest subscription-read availability coverage, without new grants or fakes.
Preserve prior click-plus-commit assertions, explicit keyboard focus preconditions,
Settings-navigation counter boundary, controller/draft checks and synthetic
delivery/correlation/silent-option/click coverage. No retry-until-green or longer
deadlines. This UI follow-up does not require a new provider/native push proof or
claim physical sound/focus acceptance. Lead selects any remaining package checks.

Roll out the new asset/template package through normal lead-owned composition;
new/refreshed pages show the compact menu, retained pages keep their loaded UI.
Both use the same existing persistent records and worker. No migration, data reset,
tab closure or subscription replacement is part of deployment/recovery; use a
corrected successor if needed. No application edit, check, browser, network, host,
pin, history or lifecycle operation was performed by the architect for this brief.
