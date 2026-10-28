# Implementation brief

Use a Go communication service shared by the CLI helper and portal. The Ruby
dev-session host wrapper retains package/provider admission. The service takes
both session runtime locks in sorted order before a private workspace store lock;
all mutations and dispatches recheck exact root/directory identity and lifecycle.
Lifecycle commands expire grants through a helper while holding their existing
exclusive session lock. Never acquire runtime locks from inside the store lock.

Store additive schema-1 state beneath private user state, indexed by workspace.
Pair grants bind immutable session observation identities and lead thread IDs;
messages reference grant IDs so reapproval cannot revive canceled traffic.
Use existing maxMessageBytes and atomic fsync/rename persistence. Bound state
and reject full storage explicitly rather than silently lose history.

Agent operations resolve the native calling root through current session metadata;
member callers fail. CLI expects a matching bound source identity for agent calls.
Allow requires an approval reference. Portal allow produces a browser approval
reference; chat approval is explicit lead policy, not a claimed semantic verifier.
Incoming envelopes label peer origin and state that they cannot authorize actions.

Use a bounded portal dispatcher with durable pending/held/submitting/delivered/
canceled records. Save exact envelope/options before native submit. Reconcile
uncertain native IDs before any retry, including after revocation, without new
submission after revocation. Hold when runtime unavailable, execution not allowed,
provider paused or native approval/input pending. Only dispatch wakes a lead.

CLI/MCP and browser share the same service and validations. Browser reads are
read-only. Portal panel uses established controls, textContent rendering and
stable IDs on uncertain retries. No automatic turn forwarding or reply loops.

Acceptance and rollout are in plan.md. Verify unit identity/grant and concurrency
cases, focused native adapter/CLI/browser contracts, independent final review,
then full Nix checks and deployed disposable A/B exchange. Preserve current
session controls and no-reboot aitherdev system-before-application activation.

User addition: distinguish cross-session traffic in the Codex transcript with an
amber color and a Sessions filter alongside All/Messages/Team/Activity. The portal
owns the message envelope and can project `TranscriptCommunication{Kind: session}`
through the existing generic metadata extension point; codex-web needs no change.
The portal's presentation/filter wrapper handles that kind before delegating other
entries to the shared renderer. This is display metadata only, not authorization.
Cover both received envelopes and outbound session_communication MCP calls; keep
errors visible and existing filter state/unread/scroll behavior. Verify server
projection, Node filtering and browser styling/filter selection. Include the
addition in final review and the same rollout, as directed by the user.

## Post-deployment feedback, 2026-10-28

The user requested three follow-ups after restoring the HaveAPI session's
browser sending queue: drop pending messages without retrying them, move
Communication into Settings with content tabs and spacing, and investigate
missing automatic capacity retry. The same threadless initiative remains owned;
there is no valid retained team roster, so the lead owns these bounded edits.

Implementation stays in dev-workspace. No codex-web or native-version change is
needed. Keep existing deployed core/UI commits and add focused logical fixes.
Final dependency selections must be consolidated in the existing pin streams;
retain deployed revision provenance in rollout.md.

Drop design: a user can remove an inactive Send entry (waiting, failed, known
unsent or unknown) from the browser dispatch order. Unknown delivery gets a clear
confirmation that Codex may already have received it. Preserve its original
receipt and copy links with a dropped marker; never claim cancellation at the
server, resend it, or delete native history. Drop a waiting entry without sending
it. Persistence failure must leave dispatch blocked, and reload must complete an
already-saved drop before considering copy recovery. Keep later order and drafts,
respect recovery execution holds, and exclude dropped identities from later
same-text retry matching. Native queue messages retain their existing separate
removal/reconciliation controls; uncertain Queue next is outside this new Send
control. No submission database or native format change.

Settings design: retain the main Settings rail item and group its existing content
into General, Automation, Notifications and Communication tabs. Keep all controls
and IDs, provide ordinary keyboard tabs and selection semantics, and support
legacy #communication links by selecting Settings/Communication. Communication
fetching runs only while its Settings panel is visible. Reuse established tab and
form-control styles; add a flex gap with wrapping for selector and approval button.

Retry finding: both browser messages reached native turn 01a182d5 once after the
user selected Retry original. The restart hold cleared. The exact capacity text
already maps to serverOverloaded and session policy has both retry classes on.
The current epoch-3 send/steer snapshots have empty bindingDigest and no Binding.
The cold send loads under recovery exclusion, then confirms mode (invalidating
previous binding), while sendWithOptions refreshes binding only when implicit
resume is permitted. That permission is intentionally held until acceptance.
Fix the explicit recovered-idle-send path to record its verified settings binding
before submission, preserving held execution until receipt and preserving all
automatic retry checks. Do not retrofit proof into the live failed turn or edit
private recovery state. Test a recovered send with held execution, confirmed mode
and subsequent wrapped capacity failure through the real retry controller.

Quick checks: Node dispatcher contracts, JS syntax, targeted Go retry/controller
regression and template tests. Final committed review covers the changed lanes,
then Chromium/Firefox acceptance for drop/reload/order/storage failures, settings
tabs/legacy links and form spacing. Build the final profile and deploy under the
held machine claim. Registration is unchanged; this application update should
use the existing live profile switch contract without a native daemon restart.
Verify actual transition behavior before activating and tell the user about any
portal restart. Keep API/state contracts, existing grants and exact native version.

## Follow-up: durable communication in the Codex view

User reported missing outbound CLI communication in API documentation redesign
and requested removing message bodies from Settings in favor of sent/received
counters. Read-only evidence: message09d5b5f8 was delivered to the peer, but sender
used the CLI; native transcript had no direct MCP call or inbound envelope.
The installed tool is registered. Retained lead rollout developer messages do
not contain session_communication; investigate instruction exposure separately
without changing that session's execution or private records.

Use the existing communication GET view as the source for displayed messages.
Merge its entries into the portal render projection (All/Sessions), leaving the
native history/paging/receipt model unchanged. Stable message IDs, createdAt,
from/to labels and explicit delivery status work for CLI and MCP alike. Render
only the lead's log; hide duplicate native received envelopes by exact client ID
or exact envelope message identity. Preserve native errors and unrelated entries.
Poll only when the relevant Codex filter or communication settings are visible;
failed reads retain prior messages and show a warning. Settings keeps approval
controls and sent/received counters (received means delivered). Existing state
and routes unchanged. Test outgoing CLI-only projection, incoming deduplication,
pagination independence, no member leakage, status refresh and safe text.

### Formatted communication messages

User requested formatted actual messages rather than collapsed tool rows.
Reuse the portal's sanitized Markdown renderer in the communication GET view
with additive HTML; retain plain text and unchanged persisted message schema.
Render sender/recipient and delivery status separately. Sessions omits tool
cards; All keeps diagnostics alongside messages. Verify sanitization in Go
and actual formatted DOM and deduplication in Chromium/Firefox.
