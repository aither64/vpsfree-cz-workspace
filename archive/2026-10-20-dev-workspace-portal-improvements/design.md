# Portal usability and delivery design

Current executable brief: [Accepted follow-up — 2026-10-21](#accepted-followup-2026-10-21). Where stated, it supersedes earlier artifact UI, A-unchanged and machine-release guidance; prior design and deployment evidence remain retained.

Design owner: architect0. Initial executable brief, 2026-10-20.
Source baselines: dev-workspace `2c29b80`, codex-web `738b064`, workspace
`44285bbb`. Lead owns plan/state, registration and tracking commits. This brief
authorizes implementation within the assigned boundaries; it does not authorize
deployment, default-branch integration or session lifecycle actions.

## Scope and acceptance

| Request | Intended behavior and acceptance |
| --- | --- |
| 1. Index loading | First usable session list is independent of slow activity/cluster enrichment. Ordinary initial/background loading is silent. Real sustained failures retain the existing grace period and compact inline warning. A deliberately blocked enrichment reader must not block initial list display or remove existing rows. |
| 2. Older-history notice | Successful legacy fallback has no persistent warning. Initial and background history repair are silent; manual older-page failures remain actionable in normal layout, never over messages. Authorization/timeouts must not become legacy fallback. |
| 3. Submission 502 | No browser alert for ordinary Send/Queue/retry delivery failures. Keep exact input, attachment IDs and durable attempt ID; reconcile or explicitly retry that same attempt. Retain accepted/observed receipts and never generate a second turn after response loss. Diagnose the proxy failure as described below. |
| 4. Team communication | Distinct team color and readable sender/recipient label. Default Messages excludes team traffic; Team shows team traffic; All includes it; Activity shows non-message activity excluding team traffic. Error entries remain visible in every view. Lead's pending optional preference may adjust this default. |
| 5. User Markdown | User messages use the same sanitized Markdown rendering as assistant messages. Canonical text, delivery digests, question envelopes and copied source are unchanged. Prefer displayText when supplied by attachment/question decoration. |
| 6–7. File links | Real anchors with working href, target=_blank and rel=noopener noreferrer. Standard click, middle click, Ctrl/Cmd-click and browser Open in new tab work. Preserve line fragments, spaces/escaping, source authorization and current/archive behavior. |
| 8. Source viewer actions | Compact Copy content and Download controls alongside existing Copy link. Copy exact complete displayed source, without line numbers; disabled/unavailable when complete text is not loaded. Download original file bytes through the same authorized source resolver, including supported binary/preview-limited files. |
| 9. Artifact navigation | Compact file rows grouped by relative directory, native directory disclosure, filename primary and label available as secondary information/tooltip. Handle hundreds of artifacts without card-like spacing. Preserve normalized-path deduplication and manifest labels. |
| 10. Artifact actions | Compact accessible copy and download icons. Copy raw complete text/Markdown, not rendered innerText/HTML. Images cannot be copied as text. Existing download behavior remains. |
| 11. Artifact scrolling | On desktop, bounded navigation and preview panes scroll independently; selecting a file changes preview without moving the page to the top. Narrow screens retain usable layout without inaccessible content. Selection, directory expansion and navigation scroll survive routine detail refresh. |
| 12. Receipt dismissal | Temporary submitting/accepted message bubble has a compact X at the right, with title and aria-label Dismiss message. Preserve the existing dismissal behavior exactly; dismissal must not cancel delivery, delete durable retry state or acknowledge an unseen message. Apply to any equivalent mounted control; do not invent a second receipt system merely for parity. |

## Findings and consequential choices

The portal implements its own conversation UI in `portal/internal/web/static/app.js`.
It imports codex-web primitives rather than `mountConversation`. Updating only the
shared mounted UI therefore cannot satisfy the portal requests.

`renderIndexWarning` explicitly displays loading after the shared 750 ms notice
delay. `indexStatus` also synthesizes a loading warning. `index()` already renders
a session list before status enrichment, but `computeIndexStatusWithPending`
awaits repository discovery, Codex activity and bounded cluster inspection before
publishing the status snapshot through `operation_state.go`. Preserve the
distinction between authoritative session membership and incomplete enrichment.
Do not publish unknown cluster counts as confirmed zero or use stale observations
to grant controls or generate new notifications. Package B must measure the
remaining first-list bottleneck and separate minimal membership from optional
enrichment where needed; merely removing the string is insufficient verification.

Both `app.js:renderHistoryControls` and shared `conversation.js` unconditionally
show the older-history notice after successful legacy fallback. Portal CSS uses
`position:absolute` for `.history-controls`, explaining overlap. This capability
notice is independent of the shared fetch deadline. `readTranscriptPage` allows
legacy fallback only for missing route (404) or explicit 501
`transcript_paging_unavailable`, followed by a validated authorized legacy read.
Preserve that contract and all transcript continuity/scroll-anchor behavior.
Current reads have 35-second browser transcript deadlines; handler operations
default to 30 seconds. Do not globally enlarge timeouts to hide these symptoms.

The shared conversation handler emits 503 for server failures, not 502.
`portal/cmd/workspace-portal/router.go:proxyWorkspace` emits 502 when its reverse
proxy cannot complete the portal request, and nginx can also emit 502. Browser
POSTs do not inherit the conversation client's GET-only 35-second timeout.
Thus the reported 502 is not explained by that shared fetch timeout. No exact
failed-request timestamp/log has been supplied, so an upstream outage/restart is
a hypothesis, not an established production diagnosis. Package B owns narrowly
scoped read-only proxy/service-log correlation and a response-loss/restart fixture;
report evidence to the lead before changing transport/restart behavior. Never
restart the live portal or send test turns into retained conversations.

The portal already persists attempt IDs before sends, recognizes matching
transcript receipts and exposes explicit retries; its catch paths call alert.
Keep this delivery system. A 502, EOF, abort or malformed response is an unknown
outcome even when the client saw no receipt. No generic POST retry, text-only
deduplication, new-ID resend or deletion of unknown attempts is permitted.
Automatic read/reconciliation is safe; explicit same-ID retry uses the existing
server ledger. Preserve the distinction of `notSent: true` only when the server
has established that fact. Browser navigation must not erase retry identities.

User Markdown is currently omitted by `Server.presentTranscript`, which renders
only agentMessage/reasoning/plan. Server Markdown already uses Goldmark and
Bluemonday, with `rewriteSourceLinks` before sanitization. Native source URL
rewriting already exists. Verify failing link examples as rendered DOM; preserve
the actual anchors and ensure sanitizer allows the required target/rel. Do not
replace anchors with click handlers or use raw HTML from user input.

Accepted by the lead on 2026-10-20: the shared handler currently invokes
`TransformTranscript` before `Attachments.ObserveTranscript` for both page and
legacy reads. Attachment decoration then replaces displayText. Rendering user
HTML in that earlier callback would expose the internal attachment envelope.
Add optional `Target.PresentTranscript func(*codex.Transcript)` after successful
attachment decoration. Both `thread/page` and `thread` follow this order:
validated transcript, existing TransformTranscript, optional
Attachments.ObserveTranscript, optional PresentTranscript, JSON response.
PresentTranscript also runs when no attachment provider is configured; attachment
errors return through the existing error path without invoking presentation.
Keep TransformTranscript timing unchanged. A owns the hook and ordering tests;
B installs its presentation callback there for lead and member conversations.
This additive API is part of the accepted implementation brief.

Team assignments and reports arrive as ordinary userMessage entries, with a
runtime-generated first line `Team assignment from <address> to <address>:`.
The native reporting tool routes through the same team assignment service.
Do not globally recolor all user messages or all tool calls. Package B owns
application-specific detection and can annotate this exact envelope, plus known
outgoing `team_reporting.report_to_lead` activity where the native activity data
identifies it. Anchored envelope recognition is a presentation hint, not proof
of sender identity: a user can quote it. Unrecognized/ambiguous entries stay
ordinary messages. Do not strip canonical text or alter delivery digests.

## Shared interfaces and independent boundaries

Package A — implementer1, codex-web only:

- Own `conversation/assets/conversation.js`, `conversation.css`, associated
  browser contracts and `docs/reference.md`. Own additive transcript type in
  `codex/client.go`, the accepted presentation hook in `conversation/handler.go`,
  and focused Go tests. Further handler/client delivery changes require an actual
  diagnosed defect; preserve protocol and ledger.
- Add `Target.PresentTranscript func(*codex.Transcript)` with the ordering above
  to both paged and legacy transcript routes. Nil preserves current behavior.
  Keep authorization and identity validation ahead of all transforms. Test both
  routes with and without attachments, nil callbacks, attachment-provider failure,
  and both callbacks installed: TransformTranscript sees the original text,
  PresentTranscript sees decorated displayText, including an empty string.
  Assert original text, client message ID and digest remain unchanged, and no
  presentation callback runs after an attachment error or rejected read.
- Add optional presentation metadata to `TranscriptEntry`:
  `communication: {kind: "team", from?: string, to?: string}`. Suggested exported
  Go types are `TranscriptCommunication` and
  `Communication *TranscriptCommunication`. It is generated by the trusted host
  transform; codex-web does not parse dev-workspace role names or paths.
- Export `transcriptEntryPresentation(entry)` returning
  `{kind, label, team}`. `kind` is user/agent/team/event/error. Team is recognized
  only by supported communication metadata; absent/unknown metadata preserves
  existing classification. Labels include sender and recipient when present,
  otherwise Team. Rendering uses textContent for labels.
- Export `transcriptEntryVisible(entry, filter = "all")`: all includes every
  entry; messages includes userMessage/agentMessage/reasoning/plan except team;
  team includes entries classified team; activity includes other kinds except
  team; error entries are always visible. Unknown filter falls back to all.
- Export `submissionFailurePresentation(error)` returning
  `{message, uncertain}`. Explicit `notSent === true` means uncertain=false;
  transport/502/503/504/abort/unclassified errors remain uncertain. Message is
  useful inline text, never a success assertion. This helper does no retry,
  storage write, receipt clearing or request dispatch. Retain error metadata.
- Shared mounted UI consumes presentation/filter helpers, receives a compact
  Team selector if needed, hides routine legacy history notices and keeps
  manual failure controls in normal flow. It may render `entry.html` only under
  the existing trusted-host, sanitized-HTML contract; text fallback remains.
  User Markdown generation and workspace URL mapping remain host responsibilities.
- Test unknown metadata, default classifications, team labels/filter matrix,
  escaped sender labels, mounted history capability fallback, same-ID durable
  retry after response loss and no success/receipt loss on transport error.
- No dev-workspace/workspace edits. Publish exact shared API choices to lead/B
  before changing these signatures. Package A can complete without package B.

Package B — implementer0, dev-workspace only:

- First independent slice: `portal/internal/web/static/{app.js,style.css,
  source-file.js,source-file.css}`, `templates/{index,session,details,source-file}.html`,
  `source_files.go`, source resolver/download helpers in
  `portal/internal/repository/source.go`, focused web/repository tests and
  `docs/workspace-portal.md`. `server.go`/`operation_state.go` changes are limited
  to index publication, transcript presentation and artifact preview metadata.
- Supply communication metadata in the trusted PresentTranscript callback; consume A's
  helper interfaces for the custom filter/render paths. Keep per-filter scroll,
  follow and disclosure state for Team just as for existing views. Old assets
  missing additive helpers must retain an ordinary usable transcript; no imports
  that make an old/new cached asset combination crash the page.
- Render user Markdown from decorated displayText when present, canonical text
  otherwise, via existing sanitizer. Move the portal presentation registration
  from TransformTranscript to PresentTranscript in both lead and member targets.
  Test paged and legacy reads with attachments and attachment-only messages so
  internal wire envelopes never appear as user Markdown. Preserve ordinary
  question and receipt controls and canonical delivery fields.
- Use existing durable attempt/receipt path for inline sending/accepted/unknown
  notices and retries. Keep textarea/uploads on failure; an acknowledgement
  observed while the HTTP request fails must not be downgraded to unknown.
  Apply the compact dismissal icon without changing dismissal/storage semantics.
- Keep real server-rendered file anchors, add safe new-tab attributes after URL
  rewriting, and preserve sanitizer protocol restrictions. Source view adds a
  raw download endpoint backed by the same resolver/eligibility checks, not an
  arbitrary filesystem path reader. Exact route can be `<existing file API>/download`
  with the existing query shape; choose one route and document/test it. Preserve
  bounded reads and attachment disposition; no content-type execution. Reuse the
  same archive Git-object resolution and symlink/special-file/ignored-file rules.
- For Copy content use complete preview text only, not CodeMirror DOM. Download
  is independent of the 512 KiB/12,000-line preview omission; impose a documented
  finite raw-download bound (initially the existing artifact 10 MiB limit is a
  reasonable shared ceiling). Oversized files return a clear bounded error.
- Artifact preview Markdown response adds `text` alongside existing `html` so
  raw-source copying needs no reverse conversion or second fetch. Preserve
  existing 10 MiB bound, type allowlist and path eligibility. Empty string is
  valid copyable text. For invalid UTF-8 either omit text-copy eligibility or
  clearly preserve existing replacement semantics; do not claim byte fidelity.
- Group the already deduplicated artifact catalog into directory disclosures;
  prefer native details/summary and buttons to an incomplete ARIA tree widget.
  Use relative paths as identity and original labels as descriptions. Use a
  selection generation/AbortController so stale requests cannot overwrite the
  latest selected preview or copy/download target. Preserve directory open state
  and scroll across details polling; handle selected-artifact removal explicitly.
- Own narrow read-only 502 diagnosis in router/service logs and regression fixture
  before deciding whether any router.go change is justified. No infrastructure
  configuration changes or restart is part of this package.
- B can implement index, file and artifact slices immediately. Its conversation
  integration waits for A's helper exports or uses agreed test fixtures until
  the published dependency is available; all final checks use the actual pin.

Dependent pin package — lead assigns an implementer after A/B source heads settle:

1. Update dev-workspace's codex-web Go/Nix selections and corresponding hashes
   together to A's published exact head; verify the browser assets and compiled
   Go handler come from that same source. Use repository-declared generation
   commands and check effective lock graph; no transient local replacements.
2. Publish final dev-workspace head, then update the dedicated workspace worktree's
   direct `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` and generated
   lock with `nix flake update vpsfree-dev-workspace/dev-workspace`.
3. Preserve extension selection, sibling inputs, follows edges and Codex version.
   This is source preparation only. Configuration runtime/host-module pin parity
   is an explicit future rollout prerequisite; no configuration repository scope
   or selected-package switch is implied here.

## Invariants, compatibility and recovery

There are no intended database, session-manifest, lifecycle-journal, team-roster,
queue or submission-ledger migrations. No Codex upgrade, RPC shape, generated
client, CLI, Terraform, NixOS module or daemon protocol change is required.
Presentation fields and download endpoints are additive. Older browsers ignore
communication/raw-text metadata; newer browsers fall back safely when it is
absent. Existing file and artifact URLs remain valid. Team classification is
never an authorization decision or a reason to remove underlying history.

Keep exact-origin mutation checks, opaque conversation resolution, canonical
directory identity, Markdown sanitization, upload bounds, source Git eligibility
and path confinement. Remote browser input remains untrusted. The trusted local
operator threat model in repository AGENTS.md applies.

Old/new assets must coexist during page reloads and caching: version imports
where appropriate and feature-detect additive helpers. No browser schema rewrite
is needed. Old code must still read existing pending attempts. The sender must
bind attempt identity to the same thread, endpoint, text, attachment IDs and
action context; a UI/filter change cannot retarget it. Dismissal affects only
presentation and cannot retire an unresolved delivery.

Deployability: publish A before pinning B, then publish B before pinning the
workspace. Build/check/review final composition before any separately authorized
switch. Selected workspace packages are forward-only: recovery means a reviewed
newer package restoring behavior or retrying the same admitted switch, not an
unauthorized profile rollback. Preserve existing browser retry records and
server ledger throughout recovery. This task does not select any package.

## Verification plan

Quick checks, in each repository's Nix environment:

- A: focused Node browser contracts for transcript/history/durable attempts and
  `node --check` for changed modules; focused Go tests for changed transcript or
  handler paths. Existing same-ID receipt, response loss, queue and origin tests
  must keep passing.
- B: focused Go web/repository tests (`-mod=readonly` from portal), Node contracts
  for index notices, source viewer, paging, custom transcript filters, receipts,
  artifact selection and refresh retention. Add failure injection, not tests
  that only assert implementation text. Document exact commands/results.
- Source/Markdown cases: headings/lists/fences/links and malicious raw HTML or
  javascript URLs; attachment/question display text; spaces, percent signs,
  Unicode and :line/:line:column/#Lline; actual anchors after sanitization;
  authorized active/tracking/shared/archive download and refusal of unsafe files.
- Presentation order: paged and legacy routes, lead and member target wiring,
  existing transform semantics, decorated and empty displayText, nil hooks,
  attachment failures and rejected reads; no change to canonical message text,
  attachment identity, delivery ID or digest.
- Delivery matrix: 502 before dispatch, lost response after acceptance, accepted
  receipt arriving before failure, queue uncertainty, reload with pending record,
  repeated explicit same-ID retry, browser storage failure and member navigation.
  Assert at most one backend turn and retention of input/attachments/retry state.
- Layout fixture with at least 500 artifacts, deep folders, long names, empty
  and image artifacts; select near the bottom, switch rapidly, refresh catalog,
  remove selected item, copy exact source, download original bytes. Keyboard and
  accessible names work; desktop panes and narrow layouts remain navigable.
- Block slow optional status enrichment and assert the first usable list is
  served promptly with membership intact. Compare durations and call counts to
  baseline; leave a real persistent failure visible after its grace period.

After all intended commits and quick checks, lead invokes mandatory independent
review of the complete branch series, final diff, pin consolidation and explicit
no-migration conclusion. Routine design itself does not trigger final review.

Longer checks only after final review: delegate each uncertain-duration/full Nix
build, Go suite, live App Server fixture and packaged composition check to the
required fresh verification utility. Use disposable state/socket/thread fixtures,
never the selected workspace's conversation service. Browser-level visual and
interaction checks must cover actual context-menu/middle-click links, clipboard,
downloads, history failure layout and independent artifact scrolling. Readiness
requires the real pinned combined assets, not only separately passing sources.

## Documentation and open evidence

Durable browser and shared-helper semantics belong in codex-web's reference;
portal behavior, source-download bounds and submission recovery belong in
dev-workspace's portal guide. This document holds assignment boundaries and
remaining diagnostic uncertainty. Lead applies user-facing writing guidance to
final copy before commits. Lead registers this design artifact and records phase
and verification evidence in state under the normal tracking cadence.

Remaining evidence: exact production 502 request/log correlation, baseline and
new index timing, concrete failing workspace-link render fixture, final filter
preference, combined-package browser verification. These are explicit execution
items, not reasons to block independent index/files/artifact and shared-helper work.

## Extension: default Full team and implementer-count variants

The user additionally requested Full team with two implementers as the default,
plus Full team variants with three, four, five and six implementers. The lead
accepted the following IDs, labels, capacity interpretation, reviewer fallback
effect and implementation boundaries on 2026-10-20. This is an independent
workspace configuration package and a small dependent runtime label change;
it is not a roster reconfiguration or a general team-policy refactor.

### Catalog selection and counts

| Catalog ID | Display name | Implementer addresses | max_open_agents | Persistent threads including lead |
| --- | --- | --- | --- | --- |
| `delegated` | Full team (2 implementers) | implementer0–implementer1 | 4 | 5 |
| `delegated_3` | Full team (3 implementers) | implementer0–implementer2 | 5 | 6 |
| `delegated_4` | Full team (4 implementers) | implementer0–implementer3 | 6 | 7 |
| `delegated_5` | Full team (5 implementers) | implementer0–implementer4 | 7 | 8 |
| `delegated_6` | Full team (6 implementers) | implementer0–implementer5 | 8 | 9 |

Set both `default_team` and `default_development_team` to `delegated`. Keep that
existing ID; do not introduce a redundant `delegated_2`. Keep `solo`,
`lead_designed` and `lead_reviewed` selectable with their existing roles, models,
efforts and ownership. The expected final catalog has eight presets total.

Use one Full-team constructor parameterized by N in `[2 3 4 5 6]`, with
`initial_member_counts.implementer = N` and `max_open_agents = N + 2`. Omitted
designer/reviewer counts remain one. Each family member reuses the existing
`solLead`, `designer`, `implementer` and `reviewer` records; do not copy divergent
role policies into five separate definitions. Preserve existing schema 6,
execution access, routing, work policies, role lifetimes and review freshness.
Derive `capacity.required_native_child_threads` from the largest team specialist
maximum, which is 8, rather than maintaining another magic count.

New Full-team settings remain lead Sol/high (allowed high/xhigh), architect
Astra/xhigh, N implementers Sol/xhigh and reviewer Sol/xhigh. Preserve exact
model IDs `gpt-6.1-sol` and `gpt-6-astra`, saved role access, allowed efforts and
instructions except the narrowly necessary count-independent lead wording.
Change “Use both implementers” to “Use available implementers for independent
work” in the Full-team lead instructions. Do not add members dynamically or
make work availability authorize new role/member creation.

### Capacity, utilities and review selection

N counts implementers only. Specialist slots are N implementers plus one
architect and one reviewer; the lead is not counted in `max_open_agents`.
The Nix and Go catalog validators already support this expansion and require
count-bearing teams to fit their specialist maximum, which must fit catalog
capacity. Eight is below the supported 63-specialist/64-capacity bounds.

Despite the historical field name, this catalog capacity is not an instruction
to start eight native children for each session. Direct team members are
independent App Server threads. `agentteams.BuildRegistrationPlan` explicitly
emits `required_native_child_threads: 0` and no child-role startup arguments;
catalog metadata still publishes `agents.max_concurrent_threads_per_session`
with required value 8. Keep this existing distinction and registration policy.
Do not edit native daemon capacity, launcher configuration or user settings,
and do not restart Codex to apply the catalog change.

The verification watcher remains the separate `gpt-6-luna`/low utility with
`max_concurrent = 1`, not a ninth specialist. Its standalone operation/thread
and fallback rules remain those of dev-session-monitor. A temporary independent
reviewer is likewise a separate fallback operation, not an extra persistent
member created by this preset. Native utility capacity failures retain the
existing visible fallback; raising a catalog bound does not promise native
spawn availability or authorize reconfiguration of retained sessions.

Changing `default_development_team` changes the mandatory-review standalone
fallback when no eligible retained reviewer exists: the lexicographically first
review-purpose role is now delegated's `reviewer`, Sol/xhigh, instead of
lead_reviewed's Astra/xhigh. The lead explicitly accepted this consequence.
Keep the selection rule and skill unchanged. Existing retained reviewers,
including this session's reviewer0, keep their saved model and effort. An
explicitly selected lead_reviewed team still receives its Astra reviewer.

### Independent workspace execution package — implementer1

Only edit the session-owned `workspace` worktree, under its own repository
ownership when catalog-covered mutations require it. This package can begin
while codex-web ownership is waiting; it has no source dependency on the new
conversation helpers and does not require the runtime label patch to evaluate.

Owned files and exact work:

- `config/agent-teams.nix`: parameterized Full-team family, exact eight preset
  IDs, both defaults, derived capacity 8 and count-neutral lead instructions.
  Keep all other role definitions and policies unchanged.
- `flake.nix`, only the `agent-team-policy` check at this stage: replace old
  default/capacity4 assertions; test all five variants using a count table and
  explicit expected IDs. Retain existing exact model/effort/access/role-policy
  checks and extend family checks rather than weakening them. Assert N+2 slots,
  designer ownership, initial implementer counts, identical role definitions
  across variants, the separate one-watcher policy, and generated metadata
  required native value 8. Check independent-review fallback resolves to the
  expected delegated reviewer policy. Pin edits remain the later dependent
  package; coordinate any overlap through the lead.
- `docs/agent-teams.md`: default and all five variant rows, member totals and
  specialist slots, dynamic “available implementers” wording, catalog versus
  direct-thread capacity, separate utility and review fallback effect. Preserve
  the retained-snapshot and existing-roster caveats.
- `AGENTS.md`: remove the statement that lead_reviewed is the default; explain
  Full team with two implementers is default and preserve the distinct
  lead_reviewed model settings. Do not rewrite unrelated orchestration policy.
- `test/agent_instructions_test.rb`: update the assertion tied exclusively to
  “two implementers, reviewer (5 total)” to cover the documented default and
  family totals while retaining ownership, saved-setting and review-policy
  assertions. Add only focused configuration/documentation contract coverage.

No edits to shared-root AGENTS.md or config, live roster/receipts, selected
package, retained prompts, native launch state or another session are included.
Do not refresh this session's lead/member instructions merely because the
catalog now has new defaults.

### Dependent friendly-name patch — package B, implementer0

The existing strict catalog schema has no arbitrary display-name field.
`PresetsFromCatalog` in `portal/internal/teamruntime/runtime.go` maps only the
existing IDs to friendly names; new IDs otherwise display “Delegated 3”.
Avoid a schema extension solely for labels. Add a narrowly scoped Full-team
family name projection for `delegated` and numeric `delegated_N` IDs, deriving
the displayed implementer count from the actual catalog role count rather
than trusting the suffix. Preserve generic fallback names for unrelated IDs,
member expansion, sorting, preset IDs and retained snapshots.

Owned runtime files: `portal/internal/teamruntime/runtime.go`, focused
`runtime_test.go` coverage, and the relevant Full-team example/name paragraphs
in `docs/workspace-portal.md`. Keep this in package B's repository ownership;
implementer1 does not edit these files. The lead may schedule it independently
of B's portal UI slices. No Go/Nix catalog validation or wire-format change is
needed for these five supported counts.

Runtime checks must project all five variants to the specified labels and
expanded addresses; count=6 produces architect0, implementer0–implementer5,
reviewer0 and lead. Preserve one-member defaults for older catalogs without
initial_member_counts, and do not rewrite retained preset names or creation
snapshots. Existing creation, fork and retry invariants remain authoritative.
The browser's new-session count summary already derives counts from preset
members; check it reports 5–9 total without new fixed-count UI branches.

### Compatibility, acceptance and verification

This remains schema 6 with schema-5 repeated-role support already present in
the selected runtime. Existing newer-than-schema-5 readers understand every
new count and ID; a predecessor without friendly-name projection can display
“Delegated N” but still reads/expands the same catalog. Final composition must
include B's label patch to satisfy the requested names. No new catalog fields,
roster schema, database migration or Codex protocol change is needed.

Catalog and per-team digests change as expected. New sessions use the new
defaults; explicit selections still win. Creation retries and forks continue
using their retained snapshots, and existing rosters/models/efforts/instructions
remain unchanged. More members enlarge creation records, so verify the largest
expanded preset against the existing complete 64 KiB journal contract instead
of weakening the bound. No rollout or live team creation is authorized by
preparing these sources.

Quick checks in repository-declared environments:

- Evaluate `config/agent-teams.nix` as JSON and assert exact IDs/defaults,
  per-count expansion/slot arithmetic and unchanged non-family settings.
- Run the focused workspace agent-instruction tests and formatting/static
  checks. Inspect the source diff for unrelated role/model/policy changes.
- Runtime focused projection/selection tests cover all variants, default
  selection, unknown-ID fallback, member addresses and source-count labels.
  Use a disposable largest-preset selection/creation-journal fixture to prove
  exact count/model settings fit the existing bounded record; no live roster.
- Check the generated catalog and package metadata together: capacity=8 in
  catalog/metadata, while direct-thread registration remains capacity=0 and
  does not acquire native role startup arguments.

After complete commits and quick checks, include the workspace configuration,
instructions/tests/docs and runtime label patch in mandatory final review.
Long/uncertain builds of `checks.x86_64-linux.agent-team-policy` and final
composed-package checks run through the required fresh watcher after review.
The final workspace pin package consumes B's published runtime with labels;
source preparation still does not select or deploy a package. Forward-only
package recovery and source-ref retention remain as in the original brief.

## Accepted bounded addition: preserve Add member selection

The lead assigned this small fix directly to package B under the bounded-edit
exception. After adding a member, the form currently refreshes/resets slowly;
a rapid subsequent Add can use low effort before defaults finish loading.
Retain the selected role, model and effort after a successful addition. Avoid
an unnecessary form reset or model/default refetch. Capture the complete,
immutable displayed selection at dispatch and prevent overlapping duplicate
dispatches. Keep current validation and deliberate role-change behavior;
errors preserve the user's selected values.

Acceptance: a focused delayed-response fixture performs rapid sequential
additions with the same displayed role/model/effort and verifies each accepted
request carries that exact selection, with no temporary low-effort fallback.
Repeated input during an in-flight dispatch cannot create a duplicate request.
Also cover a failed addition and an intentional role change so retained values
do not bypass validation or overwrite a newer user choice. Use disposable
browser/API fixtures only; no live roster operations.

Package B owns the form/controller and focused regression checks. This does
not change catalog defaults, package C's boundaries, team schemas, retained
rosters or member configuration policy. The user confirmed the existing model
and effort choices for the larger-team variants; the preceding catalog brief
therefore remains unchanged. No further architect application investigation is
needed for this accepted bounded brief.

## Index membership compatibility decision

Architect recommendation to the lead, 2026-10-20, after comparing package B's
early-membership implementation with baseline `2c29b80`: retain the existing
integer `runningClusters` wire field. Do not emit null or omit it on the existing
index-status route. The baseline browser interpolates the value directly and
hides only an exact numeric zero without a notice; null therefore displays
“null running clusters” and omission displays “undefined running clusters”.
New JavaScript's integer check does not protect already-open baseline pages.

Use the additive boolean `runningClustersKnown` for display completeness:

| Observation | runningClusters | runningClustersKnown | Display behavior |
| --- | --- | --- | --- |
| No trusted same-identity count | 0 compatibility placeholder | false | New UI treats as unknown; old UI hides the zero summary when no notice exists. |
| Same-identity cached measured count | cached nonnegative integer | true | Preserve the last known count while enrichment runs; do not claim a fresh cluster observation. |
| Successful fresh enrichment | measured nonnegative integer | true | Show the current count; confirmed zero retains the existing hidden-summary behavior. |
| Legacy server without the new flag | existing integer | absent | New UI uses the legacy integer behavior. |

The explicit false flag means the integer is not a measured zero. Do not put
routine loading text in `clusterNotice`; this keeps baseline pages quiet too.
Real cluster failure notices remain independently available through existing
notice/grace behavior. A known count and an error notice can coexist as the last
known display. No valid same-identity count means unknown, not confirmed zero.

Before updating a reused card's observation identity, compare its previous
identity with the incoming one. Explicit unknown must not retain the cluster
label from another incarnation with the same slug. Clear/hide such a label.
Use only same-identity cached enrichment; the simplest new-UI behavior for
explicit false is to hide the count, leaving any actual failure notice visible.
The server supplies known cached values when available. Do not label an unknown
placeholder as zero in new UI or use it in aggregate/control decisions.

Membership authority remains separate: only a complete successful membership
read may set authoritative=true and remove absent session cards. Partial or
failed membership reads retain false and existing cards. Publishing membership
early must not make cluster/activity snapshots fresh, grant controls, or emit
notifications; those paths retain their independent ownership and observation
checks. The additive flag is display-only and adds no persisted state schema.

Package B owns the representation and tests. Cover old browser/new server and
new browser/old server, unknown-to-known zero/nonzero, known-to-refresh/error,
same slug with changed observation identity, failed partial membership and
authoritative removal. Test the baseline rendering expression or its existing
consumer fixture, not only the new integer guard. This one-field addition avoids
a second membership array or endpoint while preserving the current consumer
contract. The lead relays this recommendation before the implementation changes.

## Accepted refresh onto integrated citation support

The lead accepted this bounded refresh before final review on 2026-10-20.
Investigation used only canonical repository objects, this session's worktrees,
read-only remote ref queries and selected-package status. No source or ref was
changed by the architect. Earlier source baselines in this document describe
the initial implementation; the following bases govern the refreshed deliverable.

### Provenance and supported baseline

| Repository | Current remote default, confirmed by SSH ls-remote | Our published head before refresh | Common base |
| --- | --- | --- | --- |
| codex-web | `57972192e30fe52ab33b867c8fe4d171f59a7fd5` | `441ebeea0eb3befa91006e2e3de9c73eab1ca32c` | `738b064a564d4f0050c676a742996cbe7680519c` |
| dev-workspace | `52dcd471186ef874c5c93f4133744195d4815454` | `2dc2dc720deb7069f913a9c0381bf7ce5bc72edc` | `2c29b8019f35f86563ef9725aba7073533eafe67` |

Canonical local master and origin/master matched those remote defaults during
inspection. Shared workspace master/origin master
`0ea5682410a38fe19627bc731e13894c1e51db57` selects runtime `52dcd47` and the
transitive codex-web `5797219` in its source/lock graph. These are integrated
upstream commits, not merely unmerged selected feature refs. Our earlier heads
diverge from them and a straight final pin to those heads would remove supported
citation behavior.

The entire added upstream codex-web range is `5797219`, “citations: resolve web
sources for shared transcript clients”. The added runtime range is
`af4c853dfbd9f6fc71d1b79a10d3c8d4ea2ceedf`, “inputs: select shared web citation
support”, followed by `52dcd47`, “portal: render numbered web citations in
assistant messages”. Both citations and the integrated input update remain
baseline history; do not rewrite or selectively discard them.

Source selection is not deployment evidence. `workspace-host status` reports
selected package `/nix/store/1pbxq09x01amjaczfxq3lzyh8s6mq6kp-dev-workspace-0.2.0`;
its metadata does not directly expose source revisions. Exact correspondence
between that installed package and the citation source heads was not established
in this investigation. Preserve the integrated citation contract regardless;
do not claim a deployment, restart or runtime version change from source pins.

### Execution order and ownership

1. Implementer1 refreshes package A under codex-web ownership. Fetch/recheck
   upstream before mutating, then replay the two feature commits after
   `738b064` (`f977598` presentation hook and `441ebee` UI helpers) onto exact
   `5797219`. The conceptual range is
   `git rebase --onto 57972192e30fe52ab33b867c8fe4d171f59a7fd5 738b064a564d4f0050c676a742996cbe7680519c`
   on the existing session feature branch, after verifying owned cleanliness.
   Resolve only the contract intersections below. Keep two logical feature
   commits; fold conflict follow-ups into the owning commit before final review.
   Run quick combined checks and publish the final feature head with the normal
   reviewed-history/lease protections. Retain exact prior-head provenance.
2. Implementer0 refreshes package B after A's final published head is available,
   under dev-workspace ownership. Replay the seven feature groups after
   `2c29b80` onto exact `52dcd47`: shared dependency (`3ca73c1`), team labels
   (`b1c4054`), source downloads (`19ea2a6`), artifact navigation (`0208147`),
   index membership (`5c1f065`), Add member retention (`d877b46`) and transcript
   presentation/recovery (`2dc2dc7`). The conceptual rebase range is
   `git rebase --onto 52dcd471186ef874c5c93f4133744195d4815454 2c29b8019f35f86563ef9725aba7073533eafe67`.
   Replace the feature's shared dependency update with one final update from
   integrated citation A to refreshed A. Preserve upstream citation rendering,
   retry and fixture changes. Verify/publish the final B head.
3. C's final-pin owner preserves the owned dirty workspace override/lock intent
   and releases idle workspace ownership while dependencies refresh. Do not
   replay the old dirty lock as authoritative final input data. Refresh the
   workspace feature onto current shared master while preserving the owned
   catalog/instruction commits, then regenerate one final nested runtime
   override/lock from current baseline `52dcd47` to final B. Keep extension
   `767dfd587e346168e1443e65ccdb67ce748f3fe3`, sibling inputs and follows edges
   unchanged unless the dependency graph itself requires a documented change.
   Serialize workspace flake edits and shared-ref mutations through the lead.

These are authorized routine feature refreshes, not default-branch integration.
No merges to master, deployment, package switch or lifecycle action is included.
If remote defaults advance again, report the new delta and preserve any newly
supported behavior before selecting another base; do not silently pin behind it.

### A conflict boundaries: shared transcript and citation contract

- `codex/client.go`: retain both optional `Communication` metadata and upstream
  `Citations`/`CitationsPending` fields, citation cache and ReadThread enrichment.
  Citation offsets remain UTF-8 byte offsets into original `Text`; user Markdown,
  labels, copied presentation and attachment decoration cannot rewrite that text.
- `conversation/handler.go`: retain upstream embedded `assets/citations.js` and
  both routes' accepted post-attachment PresentTranscript hook. Existing
  TransformTranscript timing and all validation remain unchanged.
- `conversation/assets/conversation.js`: retain citation imports/exports,
  citation-aware assistant/reasoning/plan copying and raw user-copy behavior.
  Keep team presentation/filter helpers and inline submission recovery. Mounted
  body precedence is typed activity first, then host-sanitized HTML when supplied
  for supported message presentation, then citation DOM fallback for citation
  entries without host HTML, then ordinary text. Do not lose citations when
  integrating the new host-HTML branch or bypass sanitization with raw Markdown.
- Retain upstream `requestCursor`, pending-citation page tracking and
  `citationsPending` repair scheduling, including completed entries that leave
  the newest page. Page merges still use existing turn/item identity. Team
  filtering must not stop offscreen citation repair or receipt observation.
  The quiet-history change suppresses routine notices; it must not suppress
  the background refresh required to resolve sources.
- Keep upstream `codex/citations.go`, `citation_history.go`, history-reader and
  page hooks, Goldmark dependency, protocol corpus coverage, citation browser
  tests and flake test inclusion. Existing bounded passive source recovery,
  thread/connection/rollout cache identity and URL validation remain baseline.
  No citation parser redesign is part of the refresh.
- Merge reference documentation so both web-citation and presentation/unknown
  submission contracts remain discoverable. Keep resulting asset versioning
  coherent; choose a new cache key where both branches used the same previous
  version, and ensure all fixture servers can serve citations.js.

### B conflict boundaries: Markdown, refresh and packaging

- `presentTranscript` continues running through PresentTranscript for lead and
  members after attachments. For agentMessage/reasoning/plan, use
  `codex.CitationMarkdown(*entry)` before existing Markdown rendering and
  sanitization. For userMessage, use decorated DisplayText when present,
  including empty text, otherwise canonical Text; do not resolve citation tokens
  in user messages or artifact previews. Keep team envelope/tool classification
  and delivery fields unchanged. Do not apply original-text offsets to a
  transformed user/display string.
- Combine the sanitizer's upstream anchor `title` allowance with the new safe
  target/rel attributes and source URL rewriting. Preserve source titles with
  Unicode/quotes as escaped text, protocol filtering, raw HTML protection and
  code examples containing literal citation tokens.
- Preserve upstream pending-citation conditions in newest-page metadata retries,
  `canRepairHistory`, repair completion and backoff in static/app.js. Keep this
  initiative's quiet loading/history UI, filters, per-filter state, additive
  index-known flag, safe delivery recovery and Add member fixes.
- Keep upstream `portal/internal/web/citations_test.go`, its test changes,
  session asset cache refresh and `test/repository_browser.cjs` route for
  `/citations.js`. Combine template/asset versions with this branch's changes
  rather than choosing one side wholesale. Keep the citation guide alongside
  the portal improvements and correct any statements that assumed only plain
  assistant text was rendered.
- Dependency files `flake.nix`, `flake.lock`, `portal/go.mod`, `portal/go.sum`
  and `nix/workspace-portal.nix` must all select the refreshed A source and its
  generated module/vendor hashes. Preserve upstream citation's new dependency
  closure. No stale local replace or pre-citation vendoring is acceptable.

### Quick checks and review evidence

A quick checks in its declared environment: run the existing citation browser
contract and conversation/paging/question/refresh/sync browser contracts, focused
Go citation/history tests (`TestCitationReportedResponse`,
`TestCitationCodeUnicodeAndFallbacks`,
`TestCitationHistoryContinuationAndEarlierTurns`,
`TestCitationCacheWarmReadsAndThreadIdentity`) and presentation-hook tests.
Retain protocol corpus coverage for the passive citation reads. Add focused
composition assertions for mounted HTML precedence plus citation DOM fallback,
portable copy, team filters and pending citation repair after a row leaves the
newest page. Raw canonical message text and UTF-8 offsets must be unchanged.

B quick checks in its declared environment: run `TestCitationMarkdownPresentation`
and focused portal presentation, source/download, artifact, index-cluster,
submission-loss and Add member tests, with `-mod=readonly` for Go. Exercise one
mixed transcript containing assistant numbered citations, user Markdown with
attachments, team metadata, a literal citation token inside code, Unicode before
the citation, and a late-resolved older-page source. Assert sanitized titles and
links, preserved original text/digest, exact user display text, citation-aware
copy, stable filtering/scroll and no duplicate submission. Keep the server-backed
repository browser fixture's citation asset route intact.

After the refreshed commits and quick checks, regenerate review packets from
the new exact base-to-head ranges and final diffs. Include old/new range-diffs
and list conflict resolutions. This is semantic conflict reconciliation, not a
claim of automatic patch equivalence. Review both preserved citation behavior
and the initiative's complete intended result. Previous packets/checks describe
superseded heads and cannot certify the refreshed composition.

Migration/history conclusion for this refresh: inspected upstream citation
changes add optional transcript metadata and disposable in-memory lookup state;
they explicitly do not rewrite conversations or durable runtime state. The
initiative also introduces no persistent schema migration. No migration needs
rewriting or schema guards. Integrated `5797219`, `af4c853` and `52dcd47` must
remain intact baseline ancestors. Earlier A/B feature heads were published and
consumed by this initiative's dependency preparation; keep their exact IDs in
provenance while updating published feature refs under normal protections.
No external release or deployment of those feature heads was established here;
do not infer absence of consumption from that uncertainty.

Consolidate each feature dependency stream to one final update: B has one
codex-web update above integrated af4c853; C has one nested runtime update above
integrated workspace 0ea5682. Do not retain intermediate feature pin churn simply
because it was built or published, and do not squash/rewrite the upstream
integrated pin history. Give the final series, migration conclusion and pin
dispositions to mandatory independent review. Full packaged/integration builds
and actual browser composition checks remain after review through fresh policy
watchers; no new long checks or deployment are started by this design handoff.

## Final review disposition: enrichment failure display

Lead accepted Advisory A1 from final-review.md: after a final cluster-enrichment
failure, hide the numeric count as unknown even if an earlier same-observation
measurement existed. Early membership may preserve the same-identity count while
enrichment is pending. The final error notice remains independently visible.
This intentionally conservative display grants no control, notification freshness
or persisted state; no new cache behavior is required by this initiative.

F1 history splits and F2 matching delivery-notice clearance are bounded review
remediations, not new application contracts. Keep delivery identity/state and
all existing presentation/citation/attachment behavior; verification accepts only
matching attempt/thread confirmations and retains unrelated warnings.

## Deployment extension: preserve the selected short-merge policy (2026-10-21)

Lead accepted this bounded forward refresh before user-authorized aitherdev
deployment. It supersedes the earlier no-deployment scope only for preparation
and the authorized system/profile deployment; it grants no default-branch
integration, reboot, session lifecycle action or live roster change. Architect
owns this brief only. Application/configuration edits, verification, review and
activation remain assigned to implementers and lead. No repository claim is
needed for development, rebase, feature publication, review or checks under the
selected runtime. Machine ownership is acquired only near prepared activation.

### Established graph and required refresh

The selected package is
`/nix/store/6bbjch8a42315qq855803c3y97knis2l-dev-workspace-0.2.0`, with derivation
`/nix/store/k6998rvsyqw26v76rrmxn6cs5pl26qzv-dev-workspace-0.2.0.drv`.
Its derivation identifies runtime source
`/nix/store/l9s3r62qm75dj8vw5b2qcyj25mza1b3h-source`; its measured NAR hash
`sha256-vVRdqrCIjp/ySq4R3hv2Mmfge9/jiTU1AyYJUG5hoJc=` matches the workspace
lock for runtime `968646471b1190c16a8cf60ff50736cd0525fa3f`.
The derivation's shared source
`/nix/store/xijkpqmn3nnjx17g02ii7abwzddqp55r-source` has measured hash
`sha256-PIvAf2Qd80Cw1Kws1l5XpUDqm2OgjS32OZH6sJt5e5I=`, matching locked
codex-web `57972192e30fe52ab33b867c8fe4d171f59a7fd5`; its module check also
names that exact revision. This is installed derivation/input evidence, not an
inference from package version or current checkout. The selected composition
retains extension `767dfd587e346168e1443e65ccdb67ce748f3fe3`.

SSH remote default reads confirmed runtime `9686464`, codex-web `5797219`,
workspace `11d2a692951f2cd2f79460d4c04c40a43416e9df`, and configuration
`37a338b25192d9271ee211110800c2dc6a094a57`. These are separate from the
reviewed feature heads A `852e8c51091512bc79ca6c921ef1f5ccc46a9535`,
B `db25364999aa4bf12b67506662a08e9e464bee33`, and
C `3de65bbd0e90f0c3b19e0d64ed925158155647a6`.

Runtime `52dcd47..9686464` adds one integrated short-merge-policy commit.
It changes generated lead/member technical instructions, docs and tests; it
introduces no new durable schema or claim wire format. Selecting old B would
restore obsolete broad claim instructions even though the claim capability
marker is identical. Passing package admission therefore does not establish
behavioral compatibility. Preserve this integrated baseline by refreshing B.

### Independent implementation packages and exact boundaries

1. **B, implementer0: runtime refresh.** In our existing clean dev-workspace
   worktree, replay the eight reviewed groups after `52dcd47` onto exact
   `968646471b1190c16a8cf60ff50736cd0525fa3f`. The conceptual command is
   `git rebase --onto 968646471b1190c16a8cf60ff50736cd0525fa3f 52dcd471186ef874c5c93f4133744195d4815454`.
   Retain A `852e8c5` exactly, with one final shared dependency update across
   flake.nix/lock, portal/go.mod/sum and nix/workspace-portal.nix. Preserve the
   eight groups: dependency, team labels, source actions, artifact tree, early
   membership, Add member retention, transcript presentation, delivery recovery.
   Upstream touched README.md, docs/coordination.md,
   portal/internal/teamruntime/{runtime.go,runtime_test.go},
   portal/internal/workspacecodex/{lead_policy.go,lead_policy_test.go}, and
   test/{coordination_claims_test.rb,coordination_claims_overcommit_test.rb}.
   The concrete feature overlap is teamruntime: preserve upstream
   `workspacecodex.CoordinationInstructions` in memberPolicy and its retained
   instruction/identity tests alongside our count-derived team labels/tests.
   Keep the upstream shared constant and lead-policy tests unchanged. Preserve
   upstream README/coordination text and claims tests; no claim-policy redesign
   or retained roster rewrite is part of B. No A edit/rebase is required.
2. **C, implementer1: workspace refresh and composed pin.** Prepare independently
   against exact workspace `11d2a692951f2cd2f79460d4c04c40a43416e9df`;
   final lock generation waits for B's published exact head. Replay the three
   reviewed feature groups after `0ea5682`: instruction discovery-limit test/fix,
   count-driven Full-team catalog/docs, final nested runtime pin. Our files are
   AGENTS.md, config/agent-teams.nix, docs/agent-teams.md,
   test/agent_instructions_test.rb, flake.nix and flake.lock. Preserve upstream
   short-merge rules in AGENTS.md and docs/agent-instructions/{deployment,git,
   verification}.md plus docs/coordination.md. AGENTS composition keeps both
   current coordination semantics and our Full-team defaults/reviewer guidance.
   Keep delegated/delegated_3..6, existing role models/efforts, capacity8 and
   native child registration0. Retained member settings never change.
   Regenerate the one final direct nested runtime override/lock onto B;
   preserve extension767dfd5, siblings, follows edges and unchanged A852e8c5.
   Do not replay the old db25364 lock wholesale or add a second feature pin.
3. **Configuration package, separately assigned after B exact.** Register/use
   only this initiative's vpsfree-cz-configuration worktree from current remote
   master (observed `37a338b25192d9271ee211110800c2dc6a094a57`). Read its AGENTS
   and docs/operations/workspace-coordination-aitherdev.md. Its flake channel
   `dev-workspace`, role `devWorkspace`, maps to input `devWorkspace`.
   Use `confctl inputs channel set --commit dev-workspace devWorkspace FINAL_B`
   in its declared Nix shell; preserve the generated commit message/history.
   Scope is the exact channel lock update plus required transitive shared A
   source update. No unrelated host/provider/nixpkgs/module edits. One final
   configuration pin; no application package installation through NixOS.
   Run the workspace deployment graph checker against final C and configuration
   locks. Matching module/runtime selection is required even when host code is
   unchanged. Actual host contract and prepared activation steps follow below.

B can start immediately; C can prepare catalog/instruction rebase independently.
C final pins and configuration pin require B publication, then their checks can
run independently. Lead owns new scope registration, tracking and activation.
Recheck remote heads before implementation; report any additional substantive
baseline delta rather than silently reverting it.

### Verification and review reuse

Keep the original final-review.md and verification-summary.md evidence bound to
A852/Bdb253/C3de65. A is unchanged, so its exact reviewed checks remain applicable.
B/C old package passes do not certify the refreshed composed derivations.
For a clean patch-equivalent rebase plus mechanical pins, preserve the original
review only with the independent-review policy's independently reconstructed
proof: exact old/new bases and complete series, range-diffs/patch IDs, final
functional diff reconstruction, exact nested input graph, and no-migrations
conclusion. Mechanical pin exemption never skips history consolidation. Any
semantic conflict or altered public contract needs the affected reviewer lane;
do not call it equivalent merely because Git completed the rebase.

Quick B checks: existing focused teamruntime label/member binding and
workspacecodex lead-policy tests; upstream coordination_claims_test.rb and
coordination_claims_overcommit_test.rb in the declared environment; focused
presentation/citation/delivery/index/source/artifact/Add-member contracts and
shared pin consistency. Keep Go `-mod=readonly`. Confirm technical bindings
contain the short merge critical section and preserve exact retained role
instructions. Pure claim fixtures use disposable state, not live ownership.

Quick C/config checks: instruction discovery tests and agent-team policy checks,
semantic lock graph and `bin/check-dev-workspace-deployment --workspace-root C_PATH
--configuration-root CONFIG_PATH`; compare unrelated inputs and host source.
Full branch inventories must retain integrated 9686464 and workspace11d2a692
as baselines, with one final dependency update per consumer and no migrations.
After the review/reuse gate, fresh policy watchers realize the final package and
required host generation and run applicable package/browser/host-contract checks.
Use exact derivation/input receipts to reuse unchanged checks; tree equality
alone is insufficient. Preserve output roots through deployment preparation to
avoid losing the rebuilt candidate to pressure GC again.

### Accepted C instruction-size adjustment

Lead accepted implementer1's bounded composition finding: preserving the new
upstream short-merge paragraph projects AGENTS.md to 16,691 bytes, above the
unchanged 16,384-byte discovery limit. C may make factual-equivalent wording
compression in the owning instruction-size group. Preserve every requirement,
procedure route, role/model/effort setting and full new coordination semantics;
do not relax, remove or increase the assertion or discovery limit. Aim for useful
headroom (at least several hundred bytes, preferably 512) rather than landing
one byte under the limit. Lead must accept the exact draft before commit.
This is a prose composition change beyond automatic patch-equivalent rebase.
After final commits and quick checks, retained reviewer checks the affected
general/risk lanes, with the final instruction diff and byte evidence; unaffected
application lanes retain their prior review under the normal reuse policy.

### Actual host contract and prepared deployment

Read-only live evidence on 2026-10-21:

- `/run/current-system` and `/nix/var/nix/profiles/system` both resolve to
  `/nix/store/75w4s3zavi0g6z05scrb9ldck4lf2hfg-nixos-system-aitherdev-26.05.20261020.cd4ea8d`.
  That system's `etc/confctl/configuration-info.json` records clean configuration
  `37a338b25192d9271ee211110800c2dc6a094a57`; `inputs-info.json` records
  devWorkspace `968646471b1190c16a8cf60ff50736cd0525fa3f`. These prove the
  running host selection independently of current canonical refs.
- The selected package's catalog maps `aitherdev` and its machine selector
  `cz.vpsfree/machines/aitherdev` to resource `vpsfree:aitherdev`, which is also
  its profileMachine. Profile and system activation share that one reservation.
- Aitherdev imports `devWorkspace.nixosModules.host`, keeps application selection
  in the user's profile, and retains the existing system Codex compatibility
  package. Host identity is `vpsfree-cz.workspace.aitherdev.int.vpsfree.cz`,
  alias `vpsfree-cz-workspace.aitherdev.int.vpsfree.cz`, wildcard
  `*.workspace.aitherdev.int.vpsfree.cz`. No auth, TLS, provider, firewall or
  application installation changes are required for this feature.
- Comparing runtime9686464 with reviewed Bdb25364 shows identical libexec,
  nix/host-module.nix, nix/host-paths.nix, nix/codex-package.nix, nix/systemd,
  runtime-authority/cluster/session contract JSON, and claim/coordination/
  integration contract files. Only the portal package/vendor pin changes under
  nix. The refresh must retain that host substrate equivalence. The required
  configuration change is the matching runtime selection, not a module redesign.
- Both publish claim schema1/recordSchema1, coordination ledger/snapshot/attempt
  schema1, integration journals1/2, livePackageSwitchPolicy1,
  workspaceReportingPolicy1, sensitiveSessionsPolicy1, sessionRecoveryPolicy1,
  development-cluster schema1/policy3, tracking limit8MiB, and the same provider,
  archive, registration and runtime-authority policies. No database, conversation,
  roster, cluster or claim-state migration is introduced.
- Selected and active native Codex resolve to
  `/nix/store/jrsm1rzxm1ak23j1f2vn0lil9qgxblym-codex-package-0.163.0/bin/codex`.
  Installed source and C locks retain llm-agents `e85b99217baf13a38fc887b31338b1833f1159c0`
  and runtime nixpkgs `a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4`.
  Exact final candidate executable/argv must still be checked from its rebuilt
  artifact. Catalog capacity4 ->8 does not imply a native-child launch change:
  direct team registration remains child capacity0/reporting-only configuration.
- Baseline service reads found nginx and user workspace-router,
  workspace-coordinator, workspace-portal@vpsfree-cz, workspace-codex@vpsfree-cz
  and workspace-tmux@vpsfree-cz active. Codex MainPID3387667 and tmux MainPID435397
  are observation evidence, not values to hardcode in later checks. The correct
  coordinator unit is `workspace-coordinator.service`.

The derivation also references installed workspace source
`/nix/store/wdpln1wf7c939gayj8x7w7aip0za7b8f-source`, measured NAR
`sha256-8jtrVVP6HR6JCiCEfJs5ikQCIXj+hLSiIkZQQmdy5nM=`. Its flake graph selects
runtime9686464/shared5797219/extension767dfd5. Its exact originating workspace
Git revision is not established; current workspace11d2a692 is a separately proven
remote default, not inferred installed provenance. No other initiative records
or worktrees are needed to establish this deployment boundary.

The previous verification receipt names composed candidate output
`/nix/store/5d43h2q5q7d494l6v718l71lfk0sm5in-dev-workspace-0.2.0` and derivation
`/nix/store/6vf82012b1ljprmznm2jcdizml8g6spx-dev-workspace-0.2.0.drv`.
The derivation is also absent in this latest read, beyond the already reported
GC of its output. Saved receipts remain useful evidence for the old exact heads;
rebuild the refreshed candidate and retain its output/derivation roots. Do not
substitute the older installed1pbx package for the verified candidate.

### Execution and continuity acceptance

These are instructions for the deployment owner after final sources and review;
no command in this section has been executed by architect0.

1. Finish B, final C and the configuration channel commit. Preserve source
   cleanliness, exact published heads and independent review/reconstruction
   evidence. Run the final graph checker: workspace nested runtime and config
   devWorkspace must match exact FINAL_B; verify the transitive shared A852e8c5,
   extension767dfd5, sibling inputs and follows paths. Retain final source,
   derivation/output and configuration-generation identities. Confctl embeds
   its commit, so a prior equal tree does not replace final committed build proof.
2. Outside machine ownership, watcher-owned verification realizes the composed
   workspace default package from final C and builds only
   `cz.vpsfree/machines/aitherdev` from the configuration worktree. Use its Nix
   shell and ordinary `confctl build cz.vpsfree/machines/aitherdev`. Preserve
   the resulting named generation and recovery artifacts. Stop and investigate
   an unexpected local kernel build under the verification procedure. Prepare
   copies with `confctl deploy --generation GENERATION --copy-only
   cz.vpsfree/machines/aitherdev` when supported by the pinned confctl CLI.
   The configuration owner confirms the pinned CLI help before execution;
   canonical confctl currently exposes --generation, --copy-only and
   --dry-activate-first. No new legacy prepare/approve/submit job is needed.
3. Assert rebuilt package metadata/contract compatibility, same native Codex
   executable and validated registration argv, expanded catalog/digest and
   unchanged retained settings. Compare actual derivations before reusing
   prior host checks. Run affected quick checks before independent review and
   longer build/browser/host checks after it. Keep live session creation,
   lifecycle, delivery and naming fixtures on disposable state. Read-only
   runtime health cannot prove provider naming success; keep that limitation
   explicit if no fresh isolated naming check is necessary.
4. Lead takes only `machines:["vpsfree:aitherdev"]`, `repositories:[]` through
   ordinary coordination acquire with a fresh request UUID. Read authoritative
   claim-status and proceed only when held. If queued, do independent work or
   yield; no build or repository claim is held while waiting. Immediately
   recheck source/artifact identities, current selected profile and live/system
   profile generation. Changed selection or unsettled operations requires
   reconciliation/replanning, not bypassing admission or releasing another owner.
5. Under that claim, perform ordinary confctl dry activation and the prepared
   no-reboot switch (for example `confctl deploy --generation GENERATION
   --dry-activate-first cz.vpsfree/machines/aitherdev switch`, confirmed against
   the pinned CLI). Retain configured auto-rollback, generation metadata and
   health checks. Verify `/run/current-system` and system profile both select
   the prepared generation, with final configuration revision and FINAL_B in
   embedded metadata. A zero exit, live path alone or SSH disconnect is not
   enough. Resolve uncertain system effects before profile selection.
6. With the same held claim and exact verified session environment, run stable
   `workspace-host switch --source C_ABSOLUTE_WORKTREE`, passing
   `DEV_WORKSPACE_CLAIM_ID=CLAIM_UUID`. Use the final composed C checkout, not
   generic B. Ordinary switch internally rechecks/builds source and compares
   generation, registry, registration plans and compatibility under transition
   locks; pre-realization makes this a cached preparation, not permission to
   replace its preflight with private helpers. Do not override Codex selection
   or use --from-candidate for an ordinary update.
7. Verify selected profile equals the exact prepared package; system and profile
   contract selections agree; router, portal, coordinator and nginx recover.
   Probe `/healthz` through the normal authenticated portal route and read this
   session's page/transcript/status. Check pending reconciliation clears through
   ordinary completion, the package's exact A source and catalog are installed,
   retained roster/settings are unchanged, and Codex/tmux/socket/launch identities
   remain continuous. A compatible live switch restarts portal/router and
   browser connections, while retaining native Codex and tmux. New catalog
   defaults affect future selections; launch provenance remains the original
   marker. If preflight requires a native restart, surface the reason and wait
   for safe ordinary idle transition; do not stop active conversations.
8. While retaining the machine for live review, inspect current index, Messages/
   Team views, existing Markdown/citations and source/artifact links. Use previous
   disposable acceptance evidence for duplicate-submit and rapid Add behavior;
   do not create live turns or roster members merely to verify deployment.
   Keep ownership through user feedback/redeployment. When machine work is
   finished and effects are known, explicitly release the exact claim. Release
   does not grant merge approval or close/archive/delete this session.

### Forward recovery and acceptance limits

Before profile selection, a failed candidate preflight leaves the predecessor
selected; retain diagnostics and repair preparation without forcing contract
acceptance. After selection, retain the selected forward package, pending
reconciliation, roots, exact source and machine ownership. Retry the same
ordinary stable switch for that candidate, or use a reviewed compatible forward
successor after diagnosis. Never select an older workspace generation, delete
claim/lifecycle/provider/cluster state, manufacture a launch marker or use a
candidate/private recovery helper to clear a refusal. Pre-existing lifecycle
journals belong to their original owners; this deployment authorizes no lifecycle
repair action. System recovery retains confctl's supported auto-rollback and
both live/profile evidence; it must remain compatible with any already-selected
application generation.

The final deployment report must distinguish source refresh/review/build success,
actual system and user-profile activation, read-only live health, continuity and
human UI acceptance. It must not claim the historical production502 root cause
was resolved by deployment. The tested contract is preserved exact submission
identity and recovery after uncertain transport. No default branch merge or
lifecycle action is required to deliver this authorized deployment.

<a id="accepted-followup-2026-10-21"></a>
## Accepted follow-up execution brief — 2026-10-21

This is the current executable brief for all five follow-up concerns. User authorization: “Implement the plan.” It supersedes the prior registered-only artifact proposal and specialized inline artifact UI, the earlier instruction to keep A unchanged, and any earlier permission to release a deployed machine without integration and user acceptance. All other delivered features, compatibility obligations and historical evidence remain retained.

Lead owns plan/state, tracking commits, assignments and the final context-aware user-facing prose pass. Architect0 edits this design only. Lead reports aitherdev machine-only claim 755910ab-a78b-4d30-a057-03b555b336db HELD; retain through review/deployment, integration evidence, user result acceptance AND explicit release direction. No default integration, machine action by architect0, native Codex upgrade or session lifecycle action is authorized. Feature edits/pushes/tests require no repository claim. Shared tracking writes use only the short .git/dev-session-tracking.lock.

### Exact deployed provenance and current upstream guards

| Component | Deployed feature head | Original source baseline |
| --- | --- | --- |
| A codex-web | 852e8c51091512bc79ca6c921ef1f5ccc46a9535 | 57972192e30fe52ab33b867c8fe4d171f59a7fd5 |
| B dev-workspace | f8f2938b4e2cfd6e5b82657d08f014357817808f | 968646471b1190c16a8cf60ff50736cd0525fa3f |
| C workspace | 530038a8ee2bf6772144b07ca0cb02426fc1e6d6 | 11d2a692951f2cd2f79460d4c04c40a43416e9df |
| Configuration | 450e1ff538c1e94c1ec74f57b50fbe2efb31502b | 37a338b25192d9271ee211110800c2dc6a094a57 |

Preserve [deployment receipt](deployment-receipt.json), [rollout](deployment-rollout.md), [verification summary](verification-summary.md) and prior review/migration provenance. Do not infer installed source identity without the recorded graph. Lead freshly SSH-verified unchanged A/B defaults at 5797219/9686464; workspace default advanced to 5276ad798d3dcf2c714f2336b0a50636bab900ae and configuration default to 38e7c837893695999e588a73f5d2a0088b8257b1. Preserve these upstream changes at final C/config composition; do not write master. Recheck exact refs before refresh.

<a id="followup-packages"></a>
### Execution ownership and independent boundaries

| Package | Owner | Dependency and serialization |
| --- | --- | --- |
| A shared responsiveness | implementer1 first | Own shared source/optional contracts and quick checks; preserve original A852 features/citations. |
| B Files and browser recovery | implementer0 first | Proceed independently, then consume exact A. One owner integrates app.js/templates/cache versions. |
| B dynamic claims | implementer0 after Files/browser core | Independent of A; serialize coordination docs and every B Git/index operation. |
| B notifications | implementer1 after A | Explicit B handoff; no overlapping B app.js or Git/index work. Gate/store ownership is distinct from attention polling. |
| Policy/C/config | implementer1 later | Runtime policy/docs serialized with claims docs; C/config prepare source docs but final pins wait for final B. |

Parent launches utilities under retained installed watcher policy. Implementers own source, tests, technical docs and commits. Lead coordinates handoffs even for disjoint files sharing B. No member commits another member's work. One final shared pin in B, runtime pin in C, and matching confctl runtime/A channel stream in configuration. No remaining product choices.
<a id="followup-evidence"></a>
### Responsiveness evidence and causal limits
Actual canonical frontend negotiates HTTP/2 (TLS1.3/ALPN h2, curl HTTP/2, effective nginx http2 on). No host protocol change is justified. Host evidence shows no current pressure/restart: portal NRestarts0; CPU/memory PSI0; 64 CPUs/load5.9;59GiB memory available;137GiB disk. Own-session sequential safe reads were health1ms/index-progress5ms/pending63ms/queue62ms/activity67ms/limits219ms/details2.385s. Neither a universal stall nor exact reported-incident timing was reproduced. Failures occur both after switch/restore AND during continuous foreground use. Do not call all AbortErrors cosmetic.

Demonstrated steady-state/recovery defects:
• Hidden documents retain SSE; session-attention.js also does attention+coordination reads/IDB every5s (49 hidden tabs ~19.6 HTTP reads/sec).
• B pending reads follow every applied transcript, potentially each200ms, without success freshness floor.
• Provider catalog 1s refresh has no single-flight/deadline/cancellation/generation:20s latency can produce20 overlapping reads per tab.
• Resume can coalesce into an already aborted limits/details/pending/queue/activity promise and miss the required successor (limits up to60s).
• Shared mounted pending/queue lacks pause-generation exclusion.
• B createRequest swallows JSON-body aborts into {}, causing undefined details rendering or silent limits failure.
• A upload metadata initial GET fails once and never recovers; absent limits keep composer unready even with zero attachments.
Repeated native thread verification (three per ordinary read) and serial expensive details work amplify cost, but are NOT proven stall causes. Non-context-selectable native connection/write waits are possible contributors, not observed causal findings. Preserve authority checks; no broad caching, global scheduler, timeout inflation or backend refactor.

<a id="followup-files"></a>
### Normal Files — B / implementer0
Accept lead's exact UX: rename Artifacts tab Files; lazy load first open and explicit Refresh; filename tree links open existing /files/<slug>?artifact=<canonical-relative-path> in new tab with noopener. Existing viewer owns source, Copy, line links and byte-exact Download; remove specialized inline artifact preview from new UI. Keep #artifacts as alias to Files. Show Files without a global count until listing is known; no listing in initial page/details refresh.

GET /api/sessions/<slug>/files lists already-eligible own-session tracking files. Route beside existing early file GET before normalizeInteractivity so Codex availability does not gate local files. Use ReviewReader's bounded/context-aware Git execution and SAME eligibility/excludes semantics: tracked regular files and non-ignored untracked files under verified current work/archive root, plus existing built-in/explicitly registered eligibility. No filesystem-wide discovery, extra roots, metadata, symlink/special files or ignored-unregistered publication. Enumerate candidates without reading content; recheck normal reader authority on open/download. Bound output/entries/work using existing Git limits and an honest limit/error notice; do not present an incomplete listing as complete or replace a prior good tree with empty data on failure.

One canonical relative-path row; filename primary, first registered label optional metadata, never a second registered section. Retain literal-first confined-file alias handling for old registrations/URLs: only ENOENT + exact own work/<slug>/ or archive/<slug>/ prefix + existing confined suffix allows canonical fallback; actual nested literal wins, errors never fall through, missing both remains unavailable. No rewrite on reads. Keep manifest schema, artifact_add, existing routes and explicit-publication compatibility. Later own-manifest repair through validated writer remains allowed in execution; normal files need no registration.

Files: B repository/source.go (shared listing/eligibility helpers) + tests; session/manifest.go + legacy alias tests; web/source_files.go + list tests, artifact_tree.go/templates/details.html/app.js normal tree/tab, docs/workspace-portal.md and relevant README. Preserve old handlers instead of expanding their .sh allowlist; scripts work in ordinary passive source viewer.
Checks: all listed files pass existing reader predicate; tracked/ignored-untracked/global-local-excludes/no-Git registered fallback; path escape/other-session/symlink/special/Git metadata denied; legitimate nested alias distinct; registered ignored files retain existing access; archived root; missing file/large bounded listing; .sh/.py/HTML-like text passive and download bytes identical; filenames/optional labels one row; unopened tab causes zero enumeration; #artifacts works; new-tab opening preserves composer/draft.

<a id="followup-responsiveness"></a>
### Responsiveness — A / implementer1, then B / implementer0
A now needs a narrow follow-up on852e8c5; preserve all prior features/citations. No Codex version/schema upgrade.

A1. conversation/assets/sync.js: hidden/pagehide suspension closes EventSource, cancels/invalidates current read and pending retry/watch/reconnect timers. Initially hidden documents open none. Retain transcript/history/drafts/controls; this never stops a session or server monitor. Visible/pageshow resumes exactly one current stream and snapshot read with coalesced focus/online events. Allow bounded replacement of a pre-open read when SSE opening makes it stale; do not wait indefinitely for SSE before snapshot fallback. Late old callbacks cannot apply data/errors, clear newer work or schedule retries. Reset visible warning grace; genuine current failures remain warnings after existing grace, access errors immediate. Existing handler stream context cancellation already unsubscribes. Change test that intentionally kept stream across brief hiding to new bounded lifecycle contract.

A2. Mounted pending/queue read lanes: per-lane current cycle/generation, explicit cancellation vs deadline failure, identity checks for success/error/finally. Cancel clears current ownership immediately; visible resume starts a new read even if old transport settles late. Every finally updates only its own cycle. Keep one active read and at most one coalesced invalidation rerun. Retain rows, prompt response identities and queue reconciliation semantics.

<a id="followup-pending-contract"></a>
#### Typed pending invalidation contract

A3. Narrow immediate pending invalidation bridge:
- Base Client.Subscribe and generic 'data: update' stay unchanged.
- Optional PendingRevisionProvider interface: PendingRevision(threadID string) uint64; native Client implements in-memory revision of visible pending request/notice projection, with reset revision for connection changes. Increment BEFORE existing broadcast on prompt arrival/resolution/claim-visible change/local reply/snooze/notices/reset. No native RPC, payload, IDs or persistence in this getter; retire per-thread bookkeeping with existing watched/pending lifetime.
- Handler SSE checks revision on each coalesced generic update and additionally emits 'event: pending\ndata: update\n\n' when changed. Initial/reconnected reads remain authoritative. A coalesced generic channel cannot lose the pending invalidation because latest revision is compared.
- Ready JSON adds pendingInvalidation:true only for an authorized Pending target whose client supports the optional interface. Preserve generic messages/heartbeat.
- createConversationSync adds onPendingInvalidation() and read-only pendingInvalidationSupported getter, reset on reconnect; callbacks require current stream. Mounted A and custom B force/coalesce pending read on this event, local response, manual retry and actual reconnect/resume. In-flight invalidation sets one rerun bit, consumed after settlement without overlapping.
- With advertised capability, ordinary transcript/output hints respect15s SUCCESS freshness floor. A due timer guarantees eventual refresh if hints stop; failures keep existing capped backoff. Without capability, custom B retains legacy generic behavior instead of silently delaying questions; no-stream uses bounded polling. Old clients ignore named event and retain generic update. Candidate graph must include matched A/B for full50-tab guarantee. Forward optional capability through any B trusted wrappers without changing authorization.

A4. Upload metadata GET recovery: createUploadClient.list accepts optional signal; bounded, single-flight, generation-aware initialization/refresh with capped retry, Retry action and real visible resume. Do not overwrite newer draft/file status with stale list. Distinguish persistence/configuration failure from transient read failure; valid eventual metadata calls onChange so composer becomes ready without reload, including zero files. Keep upload/attachment limits and durable draft checks. No automatic replay of create/append/complete/delete/send; selected files and existing upload attempts retain semantics. New read lifecycle only, not aborting accepted mutations on hide.

A files: conversation/assets/{sync,conversation,uploads}.js, codex/client.go pending projection revision, conversation/handler.go optional SSE capability; associated browser/handler/native-client tests; docs/reference.md. Required asset revisions must invalidate both direct mounted and B's bundled custom clients.

B1. static/session-attention.js: cancel and retire attention/coordination read cycle on hidden/pagehide, stop5s scheduling/IDB polling; initially hidden no reads. Resume one current bounded refresh, no stale marker overwrite. Preserve cached title markers while hidden and server/browser Push policy; this does not acknowledge/clear attention or alter notification enablement. Do not touch reserved notification gate logic owned by the separate notification package.
B2. static/app.js read scopes/limits/details/pending/queue/activity: intentional cancellation retires current identity immediately and invalidates late settlements; resume explicitly schedules fresh successor. Single-flight applies only to CURRENT cycle. Success may not apply after signal abort; true deadline rejection remains current failure. Pass explicit timeout reason instead of raw operation-aborted copy. Keep existing timing/notice freshness budgets.
B3. static/codex-providers.js catalog GET + app dialog polling: bounded single-flight current read, options.signal, selected provider/session generation, cancel on hidden/pagehide/context change; preserve last catalog during refresh. Restore one fresh successor; one-second tick cannot overlap requests. Existing provider CHANGE operations remain durable mutations, not replayed, canceled or inferred failed by read timeout.
B4. createRequest must propagate body cancellation/transport failures; successful invalid/malformed JSON is an error rather than {}. Preserve generic HTTP error fallback only when an error body cannot be decoded, with signal checked; preserve explicitly bodyless response contracts. No synthetic successful snapshots or silent empty limits. Apply equivalent read-body handling to upload metadata. Do not change mutation uncertainty/receipt policy.
B5. consume A typed pending bridge and15s floor as above; fixed read lanes retain exact conversation/thread identity and last valid questions/queued messages, and force authoritative refresh after control responses. Known question invalidation cannot be delayed15s.

B files: static/{app,session-attention,codex-providers}.js; focused browser fixtures, trusted optional-client adapter if needed, docs/workspace-portal.md. These overlap Files app.js/asset references: one designated integrator owns combined edits/cache versions; no simultaneous Git/index operations.

<a id="followup-diagnostics"></a>
### Narrow diagnostics and unproven incident
Keep native verification/mutation authority and current server budgets. Add bounded, privacy-safe slow-read diagnostics at known read lanes and dependency boundaries using the existing logger/metrics approach: request correlation token, fixed lane/stage names, measured admission/wait duration where actually instrumented, native verification/dependency time, total time, status, cancellation/deadline category. No query/body/prompt/transcript, credential, raw socket/path or native/session identifiers; bound sampling/output. Report 'unmeasured' rather than fabricated queue timings. Instrument implicated connection/write admission waits only to measure them; do not change synchronization policy speculatively. If useful, expose non-sensitive Server-Timing for authorized read responses so network dispatch/body delay can be distinguished from server stage time. Browser test diagnostics retain protocol + lane counts/concurrency/durations and cancellation reason, not payloads.
B owns route/authority/details timing; A owns tiny native wait timing hook only if required to make dependency wait measurable. Keep this separate from semantic fixes so reviewer can assess overhead/privacy. Current evidence warrants NO host HTTP2/stream-limit change and NO blanket deadline increase. If50-tab acceptance still shows real stalls, use these measurements for a separate affected-lane correction; do not declare all causes solved.

<a id="followup-verification"></a>
### Quick and longer verification
Quick deterministic tests:
•50 independent document controllers, initialized then hidden and initially hidden/unloaded: zero hidden SSE/attention/coordination/provider/read work; bounded one current stream/read per visible lane; repeated focus/visibility/pageshow coalesces.
•Old pending/queue/limits/details/activity/provider success/error/finally settles AFTER a fresh resumed read: cannot apply or clear it; actual deadline/network/403 failure still rendered correctly.
•Hundreds of generic transcript hints over>15s produce only freshness-bounded pending reads; TRUE request invalidation/local reply forces timely read, including in-flight coalesced rerun; typed hint survives event coalescing, disconnect/reconnect and optional-provider fallback. No lost prompt or duplicate response/send.
•Delayed20s provider responses with1s ticks never overlap; switching provider/dialog/page lifecycle cannot commit wrong catalog.
•Abort AFTER headers/DURING JSON body produces failure/cancellation, never successful {}; malformed2xx JSON cannot render undefined or silently mark limits fresh.
•Upload first GET fails/aborts then succeeds via retry/resume without reload: composer recovers with zero or retained attachments, with no replayed write/duplicate turn and no draft loss.
•Diagnostic fixture delays distinguish measured stage/wait/dependency/cancellation, no sensitive payload emitted.
•Existing submission uncertainty, queue deletion recovery, citations, sound/notification and file-eligibility suites still pass.

After committed quick checks and affected independent review, longer verification must include REAL Firefox with50 initialized open tabs, some then unloaded/discarded/restored, repeated actual foreground switches and sustained foreground streaming/use. Record actual document.hidden/visibilityState transitions in the test and real Firefox evidence; Playwright headless multi-page behavior alone does not establish real tab visibility. Use a deterministic visibility harness additionally, not as substitute. Verify background HTTP/SSE counts stay bounded, foreground pending questions remain timely, draft/controls and queue state survive, retry recovers real failure, and ordinary durable send occurs once. No suggestion to reduce tabs or lengthen deadlines. No live50-tab load in this planning phase. Use authorized disposable sessions/fixtures later, never other sessions' records or live roster manipulations.


<a id="followup-notifications"></a>
### Disabled-browser notifications — B / implementer1
Server disable already atomically deletes this browser registration/outbox; register does not scan old sessions, and reducer baselines advance while off. Definite defect class is provider/in-flight delivered pushes: current worker deliberately displays every push, including obsolete/untrusted ones, and status.enabled is only session preference. This is evidence for the class, not proof of the user's particular provider queue. A genuinely new event from a later team-idle transition in an old session remains eligible.

Keep server state schema1, attention identity/revisions, title markers, session mutes and acknowledgments. Add registrationId to transport payload version1, including Test, using existing browser ID as epoch; do not add it to persisted/global attentionEvent identity. Immediately before provider send, revalidate copied job/registration/mute eligibility under current state; completion must never recreate a removed job/registration. Provider-accepted delivery cannot be recalled.

Use reserved IDBv1 record {identity,enabled,actionToken,registrationId,at:Number.MAX_SAFE_INTEGER}, protected from pruning and generic attention writes. Bounded transaction-commit helpers implement CAS. Disable commits gate off and a fresh token BEFORE server cleanup/unsubscribe, then performs cleanup even if storage failed; cannot claim durable success if the gate write failed. Fence stale results AND localStorage/registration/unsubscribe side effects. Serialize destructive Enable/Disable/cleanup among updated same-origin tabs with Web Locks; CAS also protects delayed completions and label state. Avoid a new lock framework.

A new managed enable/off->on requires server capability advertisement, confirmed ACTUAL controlling-worker capability, and Web Locks support. Unsupported/mixed clients show incomplete/refresh-needed capability status and cannot silently claim protected enablement. Negotiate an optional fresh-registration request precondition ONLY after server capability is known (old JSON decoder is strict): endpoint must be absent under registration mutex; existing endpoint ->409/incomplete cleanup, never adopt its ID. Retry bounded cleanup/verification before a fresh activation. This closes lost/late register-after-disable adoption. Continuously enabled idempotent re-register retains its ID and outbox; it is not a fresh activation. Enable commits on for the returned fresh ID only if its action token is still current.

Worker reads gate before ALL payload branches (invalid, expired, status-failure neutral and Test included), and rechecks immediately before showNotification AFTER status/sound awaits. Managed off, wrong epoch and missing epoch are permanently dropped, with no neutral popup and no queued replay. Current enabled epoch keeps existing neutral fallbacks for unavailable session meaning. Storage error fails closed. Legacy installation with no gate retains prior semantics until first explicit updated control action; new first-enable is managed, and once managed it never silently returns to legacy mode. Old assets require upgrade to achieve the guarantee; confirm controlling worker, not only registration/waiting worker. Existing shown/started OS notifications cannot be recalled, and userVisibleOnly:true may have browser/vendor effects outside app control; document narrowly without retaining the app's obsolete every-push-visible rule.

Files: notifications.go, associated Go tests; static/browser-notifications.js, notification-worker.js, session-attention-store.js and existing browser fixtures; docs/browser-notifications.md and browser-notifications-operations.md. No team reporting changes.
Quick acceptance: provider-held old-epoch pushes before/during/after off->on never invoke app show; every fallback and Test covered; disable during status/sound awaits; late/lost register, existing-endpoint409, retry and continuous registration retention; two-tab reversed completions; storage failure, old server/actual-controller upgrade/no Web Locks; off baselines/no catchup, future event works, other browser unaffected; title markers unchanged. Existing sound/test receipt contracts remain intact. Browser integration uses disposable origins/state, no live subscription or roster manipulation.

<a id="followup-dynamic-claims"></a>
### Dynamic repository claims — B / implementer0 after Files/browser core
Root cause is Engine.repository(owner,name): registration and canonical clone already resolve, then Catalog.repository(name) unconditionally refuses. Fix normal registered-repo resolution, plus queued grants AND target-package capability. No new repository registry; machine/adapters/configurationRepository/inputPaths catalogs remain static.

Validate unambiguous current registration (name/project/default_branch/optional github and reserved workspace naming) before deriving repos/<project>.git, or the workspace special case. Use real Git common-dir and normalized canonical SSH origin; require optional GitHub registration identity agreement and any configured catalog remote agreement. Reject ambiguous/invalid/conflicting identities with actionable error naming which registration/catalog/origin disagrees (no credential-bearing remote output). Catalog presence is optional for registered repos; its configured defaults/inputPaths retain their existing use. Explicit registration default_branch main is authoritative; do not substitute master or catalog defaultTarget. Claims have no target field and grant no merge authority.

Keep BOTH existing resource strings git:<real-common-dir> and repository:<normalized-remote>, sorted/deduped. Aliases sharing a common dir and separate clones sharing a remote contend; do not lock only by local alias or target branch. Preserve SSH spelling normalization and legacy repo:...:refs/... exclusion. Frozen held/waiting resource strings never get rewritten. Use existing admission mutex for owner/idempotency, mapping validation and conflict/grant transaction. Resolve Git outside ledger mutex; carry an unchanged registration/local Git identity proof into admission, recheck bounded proof under mutex and retry/refuse on concurrent change. Do not introduce network commands inside that mutex or a new global lock. Queued grants rederive before admission and refuse mapping drift; never silently grant a new resource. Exact request-ID retries return their existing record, including terminal records, without demanding a now-removed clone first. Release/cancel ownership and recovery semantics remain unchanged.

Capability minimum: retain claim-contract.json EXACTLY {schema:1,recordSchema:1}, since old readers compare equality. Add separate immutable nix/repository-claim-contract.json installed at share/dev-workspace/repository-claim-contract.json with {schema:1,registeredRepositories:true}. This advertises code capability, not mutable registry/ledger schema. require_claim_capability! must inspect ALL held/waiting repository requests: target configured mappings must match validated retained registration identity/frozen keys; absence from target catalog requires this capability and preserved identity proof. Preserve git/common keys too; remaps or unavailable/conflicting active identity fail with forward-recovery guidance, never repair state. Keep internal workspace-tracking special case supported. Thus old->new with normal claims works; capable->capable with dynamic held/waiting works; new->old with an unknown active repo refuses safely. Old target with an explicit matching catalog entry can still support that repo. Released/canceled history alone does not require the new capability. Same machine-remapping checks remain.

Files: libexec/workspace-coordination.rb (validated resolver/optional catalog lookup), workspace-coordination-claims.rb (admission/idempotence/queued grant/candidate checks), nix/repository-claim-contract.json + workspace-portal.nix install; test/coordination_claims_test.rb plus package/coordination fixtures where capability is asserted; docs/coordination.md and short operations/troubleshooting update. Preserve strict legacy job/catalog contracts unless the shared validated resolver naturally applies; do not revive snapshot jobs.
Quick tests: disposable registered uncatalogued GitHub-style main repo; aliases/same common/separate clones and normalized SSH spelling contention; disjoint remote concurrency/FIFO; duplicate/malformed registration, unsafe project, invalid origin/github/catalog disagreement; registration/remote drift before grant; exact idempotency after release/clone removal; legacy exclusion, owner/suspension/cancellation; held AND waiting dynamic package switches, old->new, safe old-candidate refusal, configured remap refusal, machine identity unchanged. No live reproduction of the reported other session.

<a id="followup-machine-policy"></a>
### Universal machine retention — implementer1 after notifications
Instruction/workflow change ONLY. No release receipt schema, coordinator state machine, automatic legacy finish gate, timeout or idle release. Existing API remains cooperative owner-only/idempotent. Generated instructions and lead workflow must enforce: retain EVERY deployed physical machine until (a) deployed feature lineage is integrated into approved remote defaults, (b) user accepts the resulting UI/behavior, and (c) user explicitly directs release of that machine. Idle/feedback/review/redeployment/turn completion are not release permission. Integration still requires separate explicit approval; quoted other-session merge permission authorizes nothing here. Repository locks remain short approved-integration locks, released before CI/records; do not bundle them into retained machine ownership.

Existing rollout/review receipts provide per-machine system/profile/store paths and full source/input graph, canonical repo/target mapping, exact deployed and final intended feature heads, and fresh remote ancestry evidence. Account for dependency pins and repo/machine aliases. If history was refreshed, retain reviewed old->new base/head and range-diff/patch-equivalence/migration lineage; never describe a nonancestor deployed commit as literally merged. Independently proven equivalent successor may establish integrated feature lineage; substantive successor behavior requires redeployment and renewed user acceptance. Preserve ordinary session exact-final-head completion rules. Acceptance must identify environment/result, not be inferred from review/CI. Before release inspect fresh own claim and known command effects, verify all gates and explicit machine-specific release direction, release exact own claim, verify state. Missing evidence keeps the machine held.

B files: docs/coordination.md ('release needs no integration proof', interruption wording and generic machine rules); current claims portion of docs/coordination-operations.md; portal/internal/workspacecodex/lead_policy.go shared CoordinationInstructions and tests proving normal/retained-role leads and members receive it without changing saved roles/settings (lead_policy_test.go and existing teamruntime binding test).
C files: AGENTS.md concise rule within size cap; docs/agent-instructions/{deployment,git,lifecycle}.md and docs/coordination.md. Explain legacy automatic reservation-release behavior as legacy implementation, not user permission; do not modify lifecycle behavior. Site consumer: configuration docs/operations/workspace-coordination-aitherdev.md links universal rule and its exact system/profile evidence. Reconcile other directly linked conflicting current-release wording only. Keep rules generic, no aitherdev-only exception.
Quick checks: generated policy assertions for three gates, all deployed machines, no expiry/idle release and preserved short repo lock/independent work; retained role/member bindings unchanged; existing workspace instruction size/routing checks with useful headroom; focused scan for contradictory current guidance. Substantive prose gets general/risk review; no tests pretending the release API enforces human acceptance.



<a id="followup-team-status"></a>
### Final team-status recovery amendment

“Team status unavailable” is stale peer-work observation while the selected member is idle/waiting and other retained peers appear active; it does not establish a stopped roster/member. Existing pause generation correctly rejects old team read success/error, but teamStatsInFlight remains until old finally and can skip immediate resume until the next5s tick. Include teamStats in B current-cycle retirement: cancellation retires ownership immediately, visible resume starts fresh, and old finally cannot clear/block the successor. The shared body-abort fix applies.

HTTP200 may contain genuine per-member missing/stale cached activity. Preserve server Stale and original observedAt, plus client15s observation/receipt freshness. Successful HTTP alone MUST NOT clear genuine stale data or manufacture a fresh observation time. Fresh observer evidence plus current receipt clears the warning. No backend/index-cache/roster truth change.

Checks: delayed old settlement after hide/resume/new read; old finally cannot clear successor; stale200 stays stale, later fresh observation clears; preserved rows/member state;50 hidden tabs produce zero team reads. Existing backend stale/aged/recovery fixtures remain sufficient.

<a id="followup-firefox-preparation"></a>
### Firefox preparation and verification gates

Current PATH has no firefox executable. Existing repository Playwright suites import Firefox, but compatible cached executable/driver and headful display/Xvfb availability are not yet certified. Architect0 may inventory those dependencies read-only after this brief is written; no uncertain install/build/test before final source review. Prepare exact bounded commands and dependency identities for parent-owned utility execution after review. If missing, report and plan post-review realization in repository Nix tooling; never substitute Chromium or call headless multi-page visibility proof of real Firefox tabs.

Real acceptance records actual document.hidden/visibilityState during foreground switches,50 initialized tabs, genuinely unloaded/discarded/restored tabs and continuous foreground work. Deterministic visibility harness supplements actual Firefox evidence. Use disposable owned profiles/sessions; no other-session records, live credentials or live roster manipulation. Hidden tabs produce zero read/SSE/attention/coordination/provider/team traffic after cancellation, true questions stay prompt, no old callback overrides current state, no duplicate dispatch, and read recovery needs no reload. Genuine failures remain visible.

Gate order: focused declared Go(-mod=readonly)/Ruby/browser checks in repository Nix environment; intended source commits; mandatory affected-lane independent review with complete series/diff and deployed lineage; only then watcher-owned long A/B package/browser/CI checks, real50-Firefox acceptance, C instruction/deployment-graph checks. Claims changes retain required disposable collection/preparation/package-switch and creation/naming-failure regressions. No review is required merely for this planning record. Lead retains the final user-facing prose pass.

### Final composition, deployment and forward recovery

Preserve current upstream C/config before final composition. B pins final A once, C final B once preserving extension/siblings/follows, configuration uses its existing confctl runtime/A channels once. Run the existing graph checker against final exact locks; preserve original review/receipt/migration provenance. There is no native Codex change or needed HTTP2 workaround.

Machine-only ownership is already held for this continuing deployed review; earlier near-activation acquisition timing does not undo this hold. Source completion does not authorize merge or release. Prepare/copy reviewed matching application and only strictly necessary host contract, then lead owns authorized activation, health/naming/conversation continuity and distinct user acceptance. No architect machine operation.

Recover forward from exact profile/system/source receipts. Preserve claims, durable attempts, notification gates and stores. Old workers cannot honor managed gate semantics: keep notifications off and restore capable code forward before enabling. Dynamic active claims reject incapable candidate packages; never delete records/catalog-edit around refusal. Alias projection is read-only; later repaired session-relative manifests remain old-reader compatible. Optional SSE/interfaces preserve older clients, but full50-tab guarantees require matched new A/B assets. No lifecycle/cleanup is authorized.

All five concerns are decision-complete. Unknown universal incident causality remains explicit: measure and satisfy real50-Firefox acceptance before claiming responsiveness resolved.

<a id="followup-firefox-inventory"></a>
### Read-only Firefox dependency inventory and bounded run design

Inventory after the executable brief was written (no browser/driver/test launched):

| Dependency | Existing executable/module |
| --- | --- |
| Playwright test1.61.1 | /nix/store/5cwkzbaxg65vbbnjvz05w8jm9m9kbam7-playwright-test-1.61.1/lib/node_modules (@playwright/test present) |
| Matching Playwright Firefox | /nix/store/bcf8w1529mgspizwjsp3iwvaq26plrgj-playwright-browsers/firefox-1532/firefox/firefox; driver browsers.json requires revision1532 / Firefox151.0 |
| Node24.21.0 | /nix/store/frlyjd2wya3rk8xmdc98yq3x0rhpkh9n-nodejs-24.21.0/bin/node |
| Ordinary Firefox155.0 | /nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0/bin/firefox |
| Geckodriver0.36.0 | /nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0/bin/geckodriver |
| xauth1.1.5 | /nix/store/4nvdi78v3rx435p09bk9hxmnp0z0ig7w-xauth-1.1.5/bin/xauth |

All listed executables exist; execution compatibility is not yet tested. Node, Firefox, driver and display tools are absent from ordinary PATH. DISPLAY/WAYLAND_DISPLAY/PLAYWRIGHT_BROWSERS_PATH/NODE_PATH are unset. No Xvfb or xvfb-run executable was found in current store outputs, and no live display was supplied. The user cache has no matching Firefox binary; use the already present matching store pair rather than installing an arbitrary npm browser. Recheck existence before execution because unrooted outputs may be garbage-collected.

Repository pinned nixpkgs is a5cc6f2c37bf518436dc8d1c288ccd0c43c2f4c4 (lock node nixpkgs_2). After final source review, parent utility may realize Xvfb/xvfb-run from that pinned environment (confirm the exported package attributes first), without any host configuration change. Existing xauth is available. No installation, Nix realization, Firefox launch or test was performed during this inventory.

Implementation owner prepares a bounded acceptance runner with fixture origin supplied explicitly. Reuse existing Playwright browser suites for ordinary contracts using the matched driver/browser paths. For actual tab visibility, use one ordinary Firefox155 window and WebDriver native tab creation/switching through Geckodriver; do not assume Playwright pages/headless imply hidden tabs. A privileged Firefox chrome context may discard a background test tab in the isolated disposable profile, then restore by selecting it; this must not touch a user profile or another session. If that supported driver operation needs an explicit Firefox automation option, verify it in the post-review fixture and record it; never replace genuine discard evidence with navigation or a mocked visibility property.

Proposed command shape, NOT executed; acceptance runner path below is an implementation deliverable, and xvfb-run must first be realized from the pinned environment:

```sh
timeout 1800 xvfb-run --auto-servernum \
  --server-args='-screen 0 1920x1080x24 -nolisten tcp' \
  env FIREFOX_BINARY=/nix/store/nhqwiw8s88b3zy3pka98gizjgw6i2h8d-firefox-155.0/bin/firefox \
      GECKODRIVER_BINARY=/nix/store/b5g0k5g2bsvar0y38mn4zdfailhk0b77-geckodriver-0.36.0/bin/geckodriver \
  /nix/store/frlyjd2wya3rk8xmdc98yq3x0rhpkh9n-nodejs-24.21.0/bin/node \
  portal/internal/web/firefox_tabs_acceptance.cjs "$FIXTURE_ORIGIN"
```

Runner requirements: own loopback driver/fixture and disposable profile; bounded driver-start/request deadlines;50 genuine initialized tabs; actual document.hidden observations for foreground/background transitions; native background discard/restoration and sustained foreground use; fixture-level request/stream/duplicate-mutation counters; only payload-free timing/cancellation diagnostics. On every exit settle owned driver/browser/display processes explicitly; no live portal50-tab load or unrelated process cleanup. Parent launches/monitors via the required utility after review. If exact driver/browser/display compatibility fails, report the concrete dependency and repair preparation, never relabel mocked/headless results as real50-tab acceptance.


<a id="followup-pending-retry-freshness"></a>
### Accepted correction: failed pending invalidation must retain its retry budget

Lead accepted this bounded disposition on 2026-10-21 after the actual native
Firefox run exposed a product defect. This section supplements the accepted
pending invalidation/read-lifecycle contract; it does not widen that contract.
Architect0 owns this design only. Lead assigns implementation after implementer3
explicitly returns exclusive B source/Git ownership with a clean handoff.

Evidence and diagnosis:

- [Native run](verification/browser-corrected-965aadc5/watcher/firefox50.log) and
  [operation receipt](verification/browser-corrected-965aadc5/watcher/operation-result.json)
  bind tested B `965aadc51dfb4a7d838a401b20ecafa38c8a70db`. The Firefox operation
  exited 1 after 101 seconds; its Go test failed at `pending-read-retry` after
  90.16 seconds. This is not a passing full native acceptance run.
- The sequential harness had established 50 initialized tabs, actual visibility,
  35 seconds of foreground operation, zero settled hidden read/stream work,
  native discard/restore with a new SSE, and typed question appearance/removal.
  It then injected a pending 503 immediately after successful question removal.
  The existing 10-second retry gate failed. Durable original-send retry and final
  one-dispatch/one-journal-entry acceptance follow this stage and were not reached.
- `refreshPending` applies its 15-second success freshness floor before retry
  admission. Its current failure path preserves `pendingSuccessAt`, then schedules
  the normal 2-second retry via `refreshPending(false)`. That retry sees the prior
  success as fresh and is deferred until its remaining 15-second window expires.
  This demonstrates a pending retry defect; it does not establish an explanation
  for every previously reported portal stall.
- Read-only inspection found B clean at `1a25bffc8d85fc726ecb971e64d382e51471887d`
  during the assigned serialized fixture work. A focused comparison with B965
  showed unchanged `app.js`, `read_cycle_browser_test.cjs` and native Firefox
  harness. This observation grants no ownership to edit or replace that head.

Implementation decision and invariants:

1. In the pending read rejection handler, immediately AFTER
   `if (!read.isCurrent()) return`, invalidate only its success-freshness
   eligibility with `pendingSuccessAt = -Infinity` (the existing initial sentinel).
   Keep the notice's last successful value/time and displayed questions intact.
   Do not reset this field before dispatch, for retired failures, or in `finally`.
2. Leave retry timer admission, delay progression and reset-on-success unchanged:
   2 seconds, 4 seconds, then existing exponential progression capped by
   `refreshPolicy.retryMaxMs` at 30 seconds. Ordinary output hints cannot bypass
   an outstanding retry timer. A successful recovery starts a new 15-second
   freshness window. Typed invalidation/manual control refresh and the one
   coalesced forced rerun retain their existing behavior.
3. Preserve current-generation/identity checks, single flight, cancellation and
   hidden-tab suspension, current deadline/error presentation and existing access
   status handling. An old failure must not erase a successor's freshness, show
   a warning, change its timer or clear its slot. No cleared questions, forced
   mutation, replayed response, changed authority or dropped control event.
4. Do not change scheduler abstractions, TLS, transport/API/schema/native policy,
   deadlines, warning grace or fixture budgets. Keep the native harness's 10-second
   pending retry gate and all visibility, stream, question and durable-send checks.

Owning package and exact boundary:

- B `portal/internal/web/static/app.js`: the current-failure freshness change,
  with a short rationale comment only if useful.
- B `portal/internal/web/read_cycle_browser_test.cjs`: regression using the
  actual shipped pending function and deterministic clock/timer/transport hooks.
- B `portal/internal/web/templates/{session,index,automatic-archival}.html` and
  `portal/internal/web/auto_archive_test.go`: one consistent app cache revision
  increment, currently 53 to 54 if unchanged at ownership handoff. No unrelated
  asset revision changes. These six paths are the expected complete source delta.
- A and the native Firefox fixture remain unchanged. Preserve implementer3's
  separately assigned recovery-loading fixture correction and its history.
  One owner performs B edits, quick checks, history consolidation and publication;
  no overlapping B worktree/index/Git operations.
- Existing `docs/workspace-portal.md` refresh documentation and the accepted
  pending contract already require successful-read freshness plus failed-read
  recovery. No new user-facing prose/API documentation is needed for restoring
  that behavior. Record the defect and verification in this initiative.

Quick verification before committed-deliverable review:

- Reproduce successful typed pending read, immediate forced invalidation failure,
  and the first scheduled retry after 2 seconds while still inside the previous
  success's 15-second window. Assert a real transport read begins, displayed
  questions remain, and repeated generic hints before that timer do not dispatch.
- Fail the retry and assert the next delay is 4 seconds with no overlap; cover
  continued progression bounded by the unchanged 30-second cap. Recover
  successfully; assert backoff resets and ordinary hints are again freshness
  limited, while forced invalidation/coalesced rerun still works.
- Retire an old pending read, complete a newer successful read, then reject the
  old one. Assert no stale warning/retry or loss of the new success freshness.
  Keep existing pause/resume, current deadline/access-status and legacy server
  tests. Use the actual shipped-function fixture, not a copied implementation.
- Negative control: execute the new regression against a disposable extraction
  of the unchanged failing B965 pending function. Require failure at the expected
  missing-2-second-dispatch assertion. Do not swap files in the shared feature
  worktree, weaken assertions or alter native budgets to obtain green output.
- In B's Nix environment run `node --check portal/internal/web/static/app.js`,
  `node --test portal/internal/web/read_cycle_browser_test.cjs`, the focused Go
  template/cache assertions including `TestAutomaticArchivalPageIsSeparateFromIndex`
  with `-mod=readonly`, and whitespace/cache-reference consistency checks. Record
  exact final source/tree and negative-control identities. Existing package
  checkPhase also executes the read-cycle Node suite.

Review and longer verification:

Lead classifies the retained deliverable HIGH and assigns the retained independent
reviewer all four applicable lane references (general, architecture, scope,
risk), focused on this newly affected product/test delta, cache and history proof.
This is a behavior correction discovered after review, not mechanical pin reuse.
Run that affected review only after intended changes are committed and quick
checks pass, then preserve unaffected conclusions. Do not repeat the unaffected
whole review. Include complete final series and deployed lineage in the packet;
consolidation must preserve the separate accepted fixture changes and original
receipts, with no invented migration boundary.

After affected review, parent-owned Luna/low verification reruns the unchanged
native `TestFirefoxTabs` acceptance on the exact corrected B with its already
prepared Firefox155/Geckodriver/display dependencies. Require the full run to pass,
including the previously unreached durable original retry: exactly one dispatch,
one fsynced journal entry and two send attempts after the lost-response retry.
Keep the 50-tab/native visibility/35-second foreground/hidden-zero/discard/restore
requirements and the 10-second pending retry gate. The prior failing run is
retained evidence, not reusable full acceptance. Complete remaining broad browser
coverage and final package/CI checks under the existing coverage mapping; narrow
source checks alone do not replace them. Durations remain uncertain; architect0
runs no tests, browsers or operations in this assignment.

Compatibility, composition and rollout:

This is ephemeral per-document GET freshness state only. No persistent format,
notification gate/epoch, native submission attempt, wire contract, schema,
access policy, roster or native Codex version changes. Old cached app assets
retain the defect until refreshed; the app cache revision makes new pages load
the correction. No old/new server compatibility requirement is added. Refresh
C's sole B pin and configuration's sole runtime channel only after final B,
retain unchanged A and input siblings, and reconstruct mechanical composition
proofs with new exact candidate derivation/output; old candidates do not certify
the correction. User-profile-only deployment remains appropriate with unchanged
host contracts. Recover forward through the supported profile procedure,
preserving claims, gates and durable attempts. The held machine, integration,
user acceptance and explicit release conditions remain unchanged. No lifecycle,
merge, release, restart or system activation is authorized by this amendment.


<a id="targeted-read-performance-replacement"></a>
### Accepted verification replacement: bounded read performance

The user's 2026-10-21 direction withdraws the native 50-tab gate: the attempt is
"too heavyweight" and smaller targeted performance regression checks are wanted.
This section supersedes every earlier requirement in this design to run or rerun
native `TestFirefoxTabs`, including the pending-retry correction's longer gate.
No further native 50-tab run, discard/restore setup or 35-second foreground soak.
Retain earlier receipts honestly as partial/failing evidence. This does not revoke
the pending-retry correction or weaken application invariants. Cheap synthetic
multi-document unit tests remain useful; they launch no browser tabs.

Identity and boundary: architect0 reverified exact current/env binding and saved
roster revision 34; architect0 is ready/design/workspace_write, implementer2 is
ready/implementation/workspace_write. Read-only checks found clean B
`f00e67833dce74621b3f20643273364c9cbbbc10` and clean A
`ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5`. Lead's frozen C `c61d` and config
`13e` remain the composition baseline. Lead assigns the following test-only B
package to implementer2; no overlapping B edits/Git operations. Parent retains
review, verification launch and pin ownership. Architect runs no checks here.

Existing coverage to reuse, not duplicate:

| Contract | Existing executable evidence source |
| --- | --- |
| Successful pending freshness and coalescing | B `read_cycle_browser_test.cjs` extracts shipped functions: 300 ordinary hints within the 15-second floor dispatch no extra GET; 20 forced hints during an active read produce exactly one follow-up; legacy-server behavior stays covered. |
| Failed pending recovery | Same suite: a recent successful read followed by forced failure retries after 2 seconds, then 4/8/16/30/30 seconds; ordinary hints cannot bypass backoff, recovery restores freshness, retired failures cannot erase successor freshness, questions/access status survive. |
| Read lifecycle | Same suite: limits/details/team/activity/pending/queue and history retire old slots before settlement; old success/error/finally cannot replace or clear current work; body-abort and team-stale truth are covered. |
| Provider fanout | B `codex_providers_browser_test.cjs`: 20 one-second ticks coalesce one catalog read; pause/resume and late completions are fenced. |
| Hidden attention traffic | B `attention_browser_test.cjs`: synthetic documents issue zero hidden HTTP/storage work, retain title markers and retire stale results on resume. |
| SSE/read scheduling | A `test/sync_browser_contract_test.cjs`: deterministic streams/timers, event-burst backoff, wake coalescing, hidden suspension, fresh reconnect and capability-checked pending invalidation. |

The B package checkPhase already runs the three B Node suites. The existing
Playwright page-lifecycle case exercises mounted UI and synthetic visibility,
but does not prove request-count bounds across a real foreground/background
pair. That is the only new browser gap addressed below. These tests prevent
specified fanout/recovery regressions; they are not throughput benchmarks or
proof of the separate live Firefox/HTTP2 incident's cause.

Minimal implementation package (two existing B test files only):

- `portal/internal/web/firefox_tabs_test.go`: factor the existing disposable
  fixture setup narrowly for reuse. Add `TestFirefoxReadBudget`, gated by
  `PORTAL_FIREFOX_READ_BUDGET_TEST=1`, which invokes the runner's explicit
  `--read-budget` mode. Keep the old native test separately gated and unselected.
  Reuse the existing controller, 200ms output hints, typed invalidation, per-page
  lane counters and one-shot pending-503 injection. Do not add production hooks.
- `portal/internal/web/firefox_tabs_acceptance.cjs`: add the explicit short mode
  before any 50-tab loop or extended phase, reusing existing driver, fixture,
  readiness and cleanup helpers. Exactly two genuine Firefox tabs; reject an
  unknown mode. Keep result identity/mode/tab count unambiguous. No new runner,
  framework, dependencies, product assets, cache versions or documentation sweep.
  If reuse requires a broad refactor, return the concrete issue to the lead.

Short scenario, with real `document.hidden`/visibility events (never overridden):

1. Initialize exactly two fixture tabs, confirm normal pending/SSE reads and
   composer readiness, and leave an unsent draft in tab 0. Record native
   visibility events. Bring tab 1 forward; wait for tab 0's already-started reads
   and SSE to settle/cancel before taking a baseline. Do not count cancellation
   latency or initial load as new hidden polling.
2. Observe ONE existing attention-poll interval (5000ms) under the fixture's
   ordinary 200ms output hints. Require all hidden lane Count deltas to be zero
   and hidden Active counts zero, including events, attention, coordination,
   details, pending, queue, activity, team, limits and providers when present.
   Compare the union of lane keys so a newly appearing hidden lane cannot escape
   the assertion. Require foreground thread Count to increase and exactly one
   active foreground SSE. Require pending Count delta <=
   `1 + floor(observedWindowMs / 15000)` in this no-control/no-failure window:
   the one allows the preexisting freshness boundary; the divisor is the shipped
   freshness contract. Exact boundary/coalescing proof stays in deterministic
   tests. Do not add arbitrary requests/second or latency-performance thresholds.
3. Select tab 0 once. Its native event history must show hidden then visible;
   verify retained draft, a newly opened single SSE and fresh pending read while
   tab 1 settles to zero active traffic. No unload/discard/restore phase.
4. Use existing typed question and clear-question controls with their existing
   5-second completion guards. Immediately after successful removal, inject the
   one-shot pending 503. Require exactly one injected failure and a subsequent
   pending GET without reload under the existing 10-second retry guard; normal
   recovery should use the existing 2-second backoff. This preserves the concrete
   defect's failing oracle without waiting through the full native campaign.
   The deterministic suite owns exact later backoff values and coalesced reruns.
   Require no message submissions, native dispatches or acceptance-journal entries.

Reuse existing operation deadlines as failure guards, not new performance targets.
Expected successful execution with prepared binaries is seconds/tens of seconds;
this is a design expectation, not a measured result. If it instead takes minutes,
stop and report the blocked stage; do not add setup retries, timeout inflation,
more tabs, more observation windows or a steady-state campaign. Keep bounded
stage/count/visibility diagnostics, disposable loopback state and owned-process
cleanup on success/failure. Do not use the live portal or host configuration.

Quick checks in the repository's prepared Nix environment, before commit/review:

```sh
# B root; all three are existing deterministic suites.
node --test portal/internal/web/read_cycle_browser_test.cjs portal/internal/web/codex_providers_browser_test.cjs portal/internal/web/attention_browser_test.cjs
node --check portal/internal/web/firefox_tabs_acceptance.cjs
# B portal directory; compiles the shared fixture and retains its cheap guards.
go test -mod=readonly ./internal/web -run '^TestFirefoxFixture(Readiness|JournalReconcilesOriginalAttempt)$' -count=1
# A root; unchanged component suite, reusable with exact source/check receipts.
node --test test/sync_browser_contract_test.cjs
```

After the two-file deliverable is committed and its quick checks pass, obtain
focused independent review of fixture selection, assertion validity, cleanup and
history; preserve unaffected product-review conclusions. Parent then schedules
ONE short browser check through the required utility, using already prepared
Firefox/Geckodriver/Xvfb/Node paths and B's normal Go environment. Exact test argv
from B `portal/`:

```sh
env -u PORTAL_FIREFOX_TABS_TEST PORTAL_FIREFOX_READ_BUDGET_TEST=1   go test -mod=readonly ./internal/web -run '^TestFirefoxReadBudget$' -count=1 -v
```

The existing prepared Xvfb wrapper supplies DISPLAY and exact FIREFOX_BINARY /
GECKODRIVER_BINARY. Do not rerun preparation, install tools or let the full native
test environment leak into a broad test invocation. Do not claim a 50-tab pass
from this smaller check. Unrelated required browser/source/package checks retain
their existing acceptance and exact-receipt reuse rules; this amendment replaces
only the withdrawn native stress acceptance.

Test-only compatibility: no application/wire/state/API/schema/cache/native Codex
or host-contract change. The fixture shares the existing candidate application
unchanged; review must ensure it does not patch production behavior to pass.
After final B is committed, implementer1 consolidates the sole downstream B pins
in C/config with source/hash/closure proof and the existing package gates.
User-profile-only deployment and forward recovery remain as already accepted.
No machine action, merge, release or lifecycle permission follows from this brief.


<a id="files-inline-all-session-files"></a>
### Accepted Files correction (2026-10-22)

This supersedes the earlier new-tab-by-default/Git-eligible/registered-metadata
Files design. User-approved result: a left directory tree and right inline
content pane containing all regular files beneath the selected session tracking
folder, including Git-ignored and unregistered files. No registrations, labels
or Registered badges. A plain primary click selects inline; genuine standalone
hrefs retain modifier/middle/context-menu opening. Preserve lazy first-open and
manual Refresh, #artifacts alias, draft, independent scrolling, selection and
expanded directories; stack panes on narrow screens. No initial/details scan.

Grounding: exact current/env binding and saved roster 34 verified; architect0
retains design/workspace_write. B clean `bc40cdda2d28c9732396db4163daa244bba79acb`,
A `ea64` unchanged; C `40b0`, config `5a524` are lead-supplied composition bases.
Preserve deployed f5h/Bbc40 receipts and existing links. This is a substantive
Files correction, with no notification, submission, host or native Codex change.

**Reader and API contract — imp0 supplies; imp2 consumes.**

- One session-confined opener resolves the validated summary's current
  `work/<slug>` or `archive/<slug>` root on every request. Reuse
  `OpenRegularFile`/openat2 nofollow confinement. All regular files there are
  eligible regardless of Git status/manifest registration; exclude .git path
  components, symlinks, directories as files, special files and escapes.
  Do not loosen workspace-wide or registered-repository readers. No filesystem
  outside this root, worktree discovery, Codex connection or Git command is
  required for session listing/content/preview/download.
- Retain old literal-first aliases: own work/archive prefix may fall back to its
  confined suffix only on literal ENOENT and an existing suffix. Two actual files
  remain distinct; permission/symlink/nonregular failures do not fall through.
  Existing manifest parsing/schema and artifact links remain supported, with no
  migration or read-time rewrite. Registration no longer authorizes extra roots.
- `GET /api/sessions/<slug>/files` retains `{files:[{path:...}]}` and stable sorted
  session-relative paths. Optional old metadata need not be emitted; any retained
  `registered` field is false and no labels are projected. Enumerate metadata
  only, with cancellation and existing whole-result limits 5,000 files/4 MiB;
  bound traversal/output before returning, never publish a partial successful
  tree. Use confined nofollow directory enumeration and revalidate selected files
  through the same opener. No Git-index enumeration. A failed refresh retains
  the last tree. Large files still appear and can report preview/download limits.
- `GET /api/sessions/<slug>/file?artifact=<path>` keeps existing `SourceFile`
  fields and `content` unchanged. Add OPTIONAL top-level `preview`:
  `{kind:"markdown",html:"<sanitized HTML>"}` or
  `{kind:"image",url:"/artifact-previews/<slug>/<canonical-path>"}`.
  For ordinary text, unsupported binary or omitted preview, omit this field.
  Raw/Copy use original `content.text`, never DOM text or rendered Markdown.
  Markdown uses existing `renderTextMarkdown` and sanitizer only when complete
  text passes existing 512 KiB/12,000-line source bounds. Binary/limited content
  cannot be copied as complete text. `source` remains artifact/archived-artifact.
- Images reuse the existing image route and 10 MiB image/download ceiling.
  Only the existing PNG/JPEG/GIF/WebP raster types, checked against detected media
  bytes, are embeddable. SVG, HTML and scripts are passive source when valid
  bounded UTF-8, otherwise a preview-unavailable notice plus Download. Never
  iframe, execute, inject untrusted HTML, or serve SVG/HTML inline. Image fetch
  revalidates the same current-root opener; retain sandbox/nosniff and explicit
  safe content type. Download remains byte-exact application/octet-stream with
  attachment disposition and existing 10 MiB/413 contract.
- Existing `/artifact-previews/`, `/artifacts/` and `artifact-preview?path=`
  routes become compatibility adapters over that opener/classifier, preserving
  existing response shapes and URLs. They must not retain registered-only access
  or introduce a second resolver. Canonical slug/path URLs do not encode the
  work/archive root. No image/preview path grants access beyond the file reader.
  Reuse existing Markdown link rewriting/sanitization; no generalized renderer.

**UI contract — imp2.** Reuse `static/source-file.js` and the existing read-only
editor. Export the small renderer
`renderSourceFileContent({parent,file,mode,nonce,isCurrent,lineURL,onLineSelect})`
returning a Promise of `{destroy()}`; `mode` is preview or raw. It renders only
server-sanitized Markdown HTML, a safe image URL or passive source, and checks
`isCurrent()` after deferred editor imports before committing DOM. Both inline
Files and the standalone mount use it; optional line callbacks retain existing
standalone #L behavior (a line link selects raw). No second editor or framework.

Each new selection retires its request/render generation; apply, error, toolbar
and delayed image/editor outcomes belong only to the newest selected path.
Use existing read scope/deadline/page suspension patterns; hide/navigation aborts
reads, resume retries only still-needed selected content. Switching Raw/Preview
reuses the already fetched content. Default Markdown/image to Preview, other
text to Raw. Toolbar uses icon-only Raw/Preview, Copy and Download with matching
title and aria-label; toggle states describe the action. Copy is enabled only
for complete original text, including CRLF/empty text; Download retains a real
href. Filename anchors retain `/files/<slug>?artifact=<canonical-path>` with no
forced target. Intercept only unmodified primary activation; native link
behavior otherwise remains. Show loading/error/unavailable states locally without
clearing the previous tree or composer. Refresh preserves current selection if
still present; a missing selection clears its actions rather than displaying
another file under that identity. No repeated listing from ordinary snapshots.

**Disjoint implementation ownership.** Lead serializes every B Git/index/commit
operation; disjoint working-file edits may proceed after assignment.

| Owner | Complete files and dependency |
| --- | --- |
| imp0 backend | `portal/internal/repository/source.go`; confined helper in `portal/internal/session/manifest.go` or adjacent session file; `portal/internal/web/{source_files.go,server.go}`; their Go reader/route tests including existing server/source/duplicate-artifact assertions; focused new `tracking_files_lifecycle_test.go` and any fixture-only Ruby helper. Own server/template-output Go expectations. No docs, browser JS or templates. |
| imp2 frontend | `portal/internal/web/static/{app.js,source-file.js,style.css}`, `templates/{session,source-file,index,automatic-archival}.html` as needed for UI/cache closure, `auto_archive_test.go` cache assertion, `portal_improvements_browser_test.cjs`, `source_files_browser_test.cjs`, affected source-function `browser_contract_test.cjs`; `question_browser_test.go` only for shared fixture setup if required. Backend API above is fixed. One consistent affected asset-version update, preserving unrelated cache refs. |
| imp3 CLI/guidance | `libexec/dev-session` artifact-add/help branch, `test/dev_session/artifact_registration_test.rb`, B `docs/{workspace-portal,dev-sessions}.md`, `skills/dev-session-documentation/SKILL.md`, narrowly affected installed/generated registration guidance if found. No backend Go/frontend files. |
| imp1 later C/config | C `docs/agent-instructions/sessions.md` and any actual registration requirement in C AGENTS/guidance; instruction-size/package checks; sole final B runtime override/lock and matching config channel after final B. Preserve A/extension/input siblings. No host change. |

CLI `artifact add` retains parsing of the old arguments/options, including
--label/--as-is/--expected-owner. A syntactically valid old invocation returns
success and prints that registrations are no longer needed and session files
appear automatically. It does not check a file into a catalog, open/change the
manifest, acquire lifecycle/creation locks, rewrite receipts or require a live
conversation. Keep syntactic CLI errors; do not retain mutation readiness gates
for a no-op. Test stdout/exit 0 and byte-identical manifest/records, including an
old expected-owner invocation. Preserve manifest validators and other callers'
creation/lifecycle guards; only the obsolete registration mutation is removed.

Residual external wording, explicitly outside this package per lead: installed
`dev-session-handoff` comes from the extension source
`skills/dev-session-handoff/SKILL.md`, step 2: “Keep portal.yml free of secrets and
transient files. Add only useful artifacts stored beneath the initiative tracking
directory.” B's corrected documentation skill, C instructions and the no-op
notice supersede registration advice. No extension repository/pin expansion or
installed-store edit; lead may scope that wording separately. Main context owns
final user-facing prose polish after technical facts settle.

**Focused acceptance and verification.**

Backend: ignored/untracked/nested files are listed/read/previewed/downloaded with
no registration and with no Git/Codex/worktree access; exact text/download bytes;
Markdown sanitization, raster sniffing, passive SVG/HTML/script; nofollow/path/
Git-metadata denials; legacy aliases and old routes; large-list/preview/download
limits. New/old `/file` clients tolerate optional preview. New UI against an older
server falls back to raw/no-preview; rollback retains files/manifests but restores
old visibility/registration behavior, without data conversion.

Disposable actual lifecycle regression: invoke ordinary archive and revive code
on one temporary tracking-only fixture using existing lifecycle test facilities
and stub only external runtime launch/stop effects. Do not replace the transition
with directory rename, private finalize helper or edited lifecycle front matter.
At active, actually archived and actually revived phases, query the real HTTP
handler for listing, `/file`, preview/image and download at the SAME saved
slug/relative URLs; assert ignored/unregistered/nested fixtures and bytes survive.
Preserve existing manifest/journal/recovery assertions and no live Codex/worktree
requirement. A focused Go test may call a fixture-only Ruby helper using existing
cross-language contract-test conventions. This needs no host VM or live-session
operation; add no general archive framework. Owner returns a concrete preparation
issue if the focused fixture cannot use normal lifecycle code safely.

Browser: extend the existing short Files segment to verify split rendering,
Markdown Raw/Preview and byte-exact Copy/Download, image/passive-content states,
rapid reversed selection completion, no popup on plain click, genuine modified
new-tab link behavior, draft retention, lazy/Refresh request counts, selected/
expanded/independently scrolled panes across refresh and narrow stacking. Reuse
existing 500-file fixture; remove old badge/forced-new-tab expectations. No native
50-tab run, performance soak or unrelated browser campaign.

Quick checks in prepared repository Nix environments, before committed review:

```sh
# B portal directory: existing and new focused reader/HTTP/lifecycle contracts.
go test -mod=readonly ./internal/web ./internal/repository ./internal/session -run 'Test(Source|TrackingFiles|Artifact|DuplicateArtifact|AutomaticArchivalPageIsSeparateFromIndex)' -count=1
# B root.
node --check portal/internal/web/static/app.js
node --check portal/internal/web/static/source-file.js
node --test portal/internal/web/source_files_browser_test.cjs
ruby test/dev_session/artifact_registration_test.rb
```

Include the new actual transition test under `TestTrackingFilesArchiveRevive`;
run it explicitly if the focused selector changes. Retain applicable existing
shipped-function/read-cycle and manifest checks, formatting/cache/whitespace
checks and negative cases; no redundant full rerun without new reason. After
all intended changes are committed and quick checks pass, lead assigns affected
mandatory review of reader exposure/sanitization, UI races, no-op compatibility,
lifecycle fixture validity and complete history. Preserve unaffected conclusions.
Then parent utility runs the existing bounded browser subtest in the prepared
environment:
`PORTAL_BROWSER_TEST=1 go test -mod=readonly ./internal/web -run '^TestQuestionBrowser$/^portal_improvements_browser_test.cjs$' -count=1 -v`,
plus the normal final composed package checks. No new tool/install/host campaign.

No persistent schema, migration, lifecycle policy, notification/send authority,
model or host contract changes. Feature source/pins precede ordinary authorized
user-profile deployment; use existing forward recovery. Retain held 755 claim,
receipts and native attempts. No merge, archive/revive of this real session,
release, restart or system activation is authorized by this amendment.


<a id="creation-notification-enospc-recovery"></a>
### Creation blocked by retained notification save failure (2026-10-22)

**Disposition: operational forward recovery; no source patch.** Lead accepted
normal authorized profile activation's validated notification loader plus the
exact postactivation status below as the parser/recovery gate. Source/pins remain
frozen. Do not bypass preference binding, clear the failure flag, regenerate keys,
edit/delete state, issue a standalone restart, or retry/create a user session.
The exact attempted name is still pending for separately scoped recovery.

Read-only evidence from the selected workspace portal:

- `GET /api/browser-notifications` returned HTTP 503 with the exact storage error.
  Source `browserNotificationsAPI` proves this means a successfully initialized
  service with `notificationStore.failed == true`, not the nil-service loader
  failure branch. `change()` retains this flag after a failed persistence attempt;
  the sender and subsequent writes stay fenced for the process lifetime.
- The workspace-specific state directory is owner UID 1000/mode 0700; its regular
  notification file is UID 1000/mode 0600, 95,159 bytes. The disabled marker is
  absent. No credential-bearing file contents or preference values were read.
  Current filesystem has about 132.7 GB free and 47.7 million free inodes;
  portal has 21 descriptors against a 524,287 soft limit. No current ownership,
  size, capacity or descriptor-limit defect was found.
- In a bounded exact-unit journal window, the same portal PID logged 1,192
  activity save/write ENOSPC errors between 2026-10-22 05:14:11.984137 UTC and
  05:21:50.169814 UTC. Notification file mtime is 05:14:11.499680 UTC, within half
  a second of that onset. The process has not restarted since October 21.
  This strongly supports a transient disk-full write followed by the deliberate
  sticky fence. The precise notification failing syscall was not logged and is
  not proved. Only fixed categories/counts/timestamps were retained.

Existing transaction/recovery contract:

`initializeCreation` runs the helper and verifies its exact durable creation
proof before `bindCreationUploads`, whose first step saves the notification
preference. That final save can fail after the session, team and initial request
already exist. A same-receipt retry with valid proof skips the helper and only
finishes binding; it must not create another conversation or resend the request.
`bindCreationNotificationPreference` preserves an already-bound same-identity
preference, including a saved mute. A not-yet-bound creation's saved default or
explicit mute remains in its immutable receipt; failed/non-ready creations are
ineligible for notification observation. Preserve those fences and preferences.
No speculative default-enabled no-write optimization is part of recovery.

Ordinary profile activation runs the existing user-service configuration and
restarts the portal as part of its supported transition. Startup reloads retained
notification state with its existing strict format/key/ownership parser, obtaining
a new in-memory store only if valid. It retains VAPID keys, registrations, outbox
and preferences. `loadCreations` reloads receipts and pauses interrupted running
ones; startup preparation reconciliation does not dispatch creation workers or
initial prompts. Explicit accepted creation/retry paths own those dispatches.
Existing ordinary notification processing resumes under its existing rules; do
not promise absence of legitimate retained/new notification delivery.

The file is NOT parser-prevalidated. The installed CLI has no read-only
notification parser command, and its constructor can mkdir/chmod/initialize state;
it was not invoked separately. Parent's ordinary forward activation is the
accepted validation path. Malformed/unreadable state must remain unavailable;
stop recovery and report, preserving all bytes. Do not treat a successful package
switch alone as notification availability.

After normal activation readiness, parent executes this exact READ-ONLY status
recipe. It makes no Test, subscription, preference, session or message request;
it prints only HTTP status and the advertised availability boolean. There is no
browser selector, credentials file, response-body log or raw identifier output.

```sh
python3 - <<'PY_STATUS'
import json, subprocess
r = subprocess.run([
    'curl', '--silent', '--max-time', '5', '--max-filesize', '8192',
    '--unix-socket', '/run/user/1000/dev-workspaces/vpsfree-cz/portal.sock',
    '--header', 'Host: vpsfree-cz.workspace.aitherdev.int.vpsfree.cz',
    '--write-out', '\n%{http_code}',
    'http://localhost/api/browser-notifications',
], capture_output=True, text=True)
status, available = 0, False
try:
    body, code = r.stdout.rsplit('\n', 1)
    status = int(code)
    payload = json.loads(body)
    available = r.returncode == 0 and status == 200 and payload.get('available') is True
except (ValueError, TypeError, AttributeError):
    pass
print(json.dumps({'http_status': status, 'available': available}))
raise SystemExit(0 if status == 200 and available else 1)
PY_STATUS
```

HTTP 200/available true proves the loader constructed a usable, unfenced store
and server disable marker is absent at observation time. It does not certify
push delivery, a particular browser, physical notification appearance or every
future disk write. Other results preserve the hold for focused diagnosis; do not
repair or weaken fail-closed behavior to pass this gate. Existing package checks
already include key/mute retention and persistence-failure fencing; no new test,
build, browser campaign or code review is needed for this operational disposition.

After the exact attempted slug is supplied, parent may scope its recovery using
the existing receipt/proof and normal same-attempt continuation. Note that the
creation status GET can reconcile/persist completion and preference binding;
it is not a purely observational substitute for reading scoped receipt metadata.
Do not probe it under the current read-only assignment. Preserve all failed
receipts, pending uploads and original attempt identity. No session record scan
was authorized. Parent alone owns activation and any later recovery action under
held machine claim 755; no merge, release, cleanup or real-session lifecycle
permission is added. The realized Files package retains its independent gates.


<a id="notification-portal-only-recovery"></a>
### Portal-only recovery before the guarded profile switch (2026-10-22)

**Decision: one ordinary restart of the existing portal is the minimum supported
operational recovery now.** This supersedes the preceding prohibition on a
standalone restart and its activation-first ordering. Parent alone executes,
under held machine claim 755910ab-a78b-4d30-a057-03b555b336db:

```sh
systemctl --user restart workspace-portal@vpsfree-cz.service
```

The two normal switch attempts refused before selection; the latest diagnostic
proves an unfinished session operation, with current f5h profile/system jwnd and
no pending transition unchanged. It does not prove which session or operation
blocks selection. Restarting the same selected portal restores the opportunity
for strict notification-store loading without changing package generation,
clearing a journal or bypassing the package-switch guard. No source/pin changes,
new tests, build, system switch, native restart or cleanup are needed.

The selected f5h unit has Wants for Codex and Requires for tmux, with no restart
propagation directive. Parent must confirm both dependencies are already active
and retain their before/after PID/socket identities, selected profile/system and
claim. Restarting this portal does not restart those active dependency units.
The portal may drain for its existing 150-second stop budget; do not force-kill
or broaden the restart if it takes time. Browser connections briefly reconnect.

Existing Close/startup cancels portal-owned work, pauses interrupted preparations,
loads creation receipts, reconciles saved inputs and restarts ordinary monitors,
recovery and notification processing. It is not a globally read-only operation.
`loadCreations` does not dispatch creation or initial prompts; interrupted running
receipts become paused, with ordinary receipt-retirement rules retained. Existing
recovery preserves execution permission for the unchanged native socket and
respects lifecycle/provider gates. No manual journal, creation receipt, key,
preference or outbox edits are permitted. The strict notification loader retains
saved keys/preferences, including mutes, or fails closed on invalid/unreadable
state. Normal eligible notification delivery may resume.

After readiness, use the exact bounded, payload-suppressing GET recipe in
[#creation-notification-enospc-recovery](#creation-notification-enospc-recovery).
HTTP 200 plus available true is the required availability gate; no Test/send or
preference mutation. If unavailable, preserve state and report the result; no
automatic repeat restart, repair or regeneration. Restoring notifications is
useful independently of whether the profile transition remains blocked.

The supported `workspace-host status` reports package/registry, not unfinished
operation identities. The ordinary switch refusal itself contains blocker
workspace/slug/kind; its lost text/hash-only diagnostic cannot recover those
identities. There is no supported read-only unfinished-operation checker in the
inspected CLI. Do not invoke private guard methods, scan receipt namespaces or
retry a switch solely to enumerate them. Await the exact attempted name (or
already retained, narrowly trusted refusal identity and explicit routed scope).
Only then inspect/recover that original attempt using its saved proof and normal
completion route. Creation status GET can persist completion and preferences;
it is not a purely read-only inspection. Validated existing creation proof skips
the helper/initial request on same-attempt completion. No replacement or resend.
Then use ordinary profile activation, which must still pass every original guard;
an unrelated blocker requires its own scope rather than inferred authority.

This is an operational amendment, not a new product deliverable or lifecycle
permission. Architect performed no restart/probe/recovery. Lead retains all
activation, machine-hold and user-acceptance responsibilities.


<a id="creation-candidate-already-ready"></a>
### Confirmed creation needs no recovery request (2026-10-22)

User identified and then confirmed `2026-10-22-codex-thread-retries` as the
creation attempted despite the notification error. Read-only inspection was
restricted to that exact tracking manifest, creation receipt/completion proof,
matching retained roster and exact journal paths. The primary session binding
remains `2026-10-20-dev-workspace-portal-improvements`.

The candidate exists under work, not archive. Its portal receipt is already
schema 3/new/validated/ready; the canonical manifest and CLI creation journal
are ready, with `initial_goal_sent: true`. Matching completion proof agrees on
workspace, slug, receipt, retained thread, canonical goal digest, model/effort,
tracking device/inode and direct-team preset/digests. Manifest sensitivity and
retained roster identity/settings match the immutable creation snapshot; all
expected member threads are ready. No candidate start/fork/archive/removal/revive,
archive-cleanup or agent-teams-migration journal is present. No prompt content,
raw thread/receipt IDs, keys or preference values were printed.

Receipt timestamps: started 2026-10-22T08:59:16.577648548Z; updated
2026-10-22T09:22:19.648900128Z; file mtime
2026-10-22T09:22:19.648425939Z. These record already-completed reconciliation;
they do not identify what caused it. Parent's earlier portal-only restart
restored notification GET 200/available true while preserving native/tmux and
f5h/system jwnd identities, as recorded in
`verification/files-final-composition/notification-recovery/result.json`.

**No creation status GET, retry, helper, new session or resend is needed.** The
candidate is no longer an unfinished creation under the inspected guard. Scoped
inspection cannot prove that all workspace blockers are clear or identify the
historical refusal's sole blocker. Parent may resume the intended ordinary Files
profile deployment with every original guard enabled and held755 retained. Any
new refusal remains authoritative; stop and report its scoped reason rather
than enumerate or recover other sessions. No recovery argv or receipt-ID file
was prepared because there is no completion operation to perform.


<a id="four-repository-integration"></a>
### Authorized four-repository integration (2026-10-22)

User: “are we done? can we merge our changes?” Lead recorded this as explicit
integration direction for the known four targets below and announced the scope.
No further approval question is needed for unchanged reviewed patches in this
scope. This supersedes earlier “merge approval absent” planning text; original
review/deployment receipts remain historical evidence, not rewritten approvals.

| Order / owner | Repository and target | Reviewed/deployed feature head |
| --- | --- | --- |
| 1 / imp0 | codex-web/master | ea64ef57fdd2ff5fd60715b62f2d1696bc0133e5 |
| 2 / imp0 | dev-workspace/master | 483d4e7eafeda974dfe19de45687795562072d7d |
| 3 / imp1 | workspace/master | 12b4491bd6e5bfa6799e938fd555c8f15d588a1d |
| 4 / imp1 | vpsfree-cz-configuration/master | 354e944f9dcf071e4878f0a0bbf2e71f52693801 |

A precedes B's sole A dependency stream; B precedes both final runtime consumers.
C and configuration are independent consumers of B, serialized in the above
order for a compact handoff. Their pins already select exact published sources;
an unchanged-head merge needs no repin, build, redeployment or native change.
Lead routes actual execution after imp0's A/B and imp1's C/config inventories.
Architect does not duplicate their remote inspection or mutate source/Git.

Before each integration, lead checks complete current ranges/final diffs against
[final review](files-final-review.md) and its parent inventory: A6+B19+C5+config2,
32 commits, no migrations, no obsolete correction tails, one final stream per
dependency. Exact [deployment receipt](files-deployment-receipt.json), package
acceptance, exercised-source reuse proof, CI and bounded Files/lifecycle browser
receipts remain valid for unchanged source/dependencies/environments. Reuse them;
do not rerun a broad suite because only a branch ref will fast-forward. Preserve
withdrawn native50 and unrelated host exclusions and the unproved network-incident
cause. Inspect required merge-hook outcomes and resulting default-branch CI under
the normal repository policy; release merge claims before any CI wait.

Fresh remote/default drift policy, prepared outside claims:

- If the current target is an ancestor of the exact reviewed feature, integrate
  unchanged. If the feature is already in the remote target, record ancestry
  instead of rewriting it. Never force a default ref or create a merge commit.
- If target drift prevents fast-forward, stop that lane and hand exact new base
  and changed paths to lead. An authorized clean feature rebase may retain the
  four-target approval only with independently checked old/new complete ranges,
  range-diff/ordered patch IDs and final diff; preserve upstream additions.
  A clean apply alone is not proof. Retain deployed refs and old evidence.
- A changed A/B identity requires its dependent owner to close the existing sole
  pin stream after the upstream feature is final/published. Use the existing
  workspace nested-input and configuration confctl-channel procedures; preserve
  unrelated input nodes. Independently reconstruct mechanical pins and compare
  effective sources/derivations before reusing checks. Tree equality alone does
  not prove verification equivalence. Run only checks affected by changed inputs,
  source, fixtures or environment; record new exact heads and evidence.
- Substantive conflicts or new behavior stop for scoped diagnosis/design and
  applicable affected-lane independent review after committed quick checks,
  under the existing review policy. Do not blindly resolve/rewrite or start an
  unaffected review/test campaign. Route material approval-scope changes through
  lead under the Git procedure; no such change is presumed here.

Prepare clean independent-repository target worktrees, repository-local guidance,
Nix environment and hook trust outside ownership. Workspace integration uses the
existing shared master, preserving every unrelated dirty/index path and staging
nothing. Save each final comparison before merge with
`dev-session worktree capture-comparison 2026-10-20-dev-workspace-portal-improvements NAME --as-is`;
repeat only if the final head changes. No branch/worktree/receipt cleanup is
included in this assignment.

For each routed merge, acquire only that repository with a fresh request ID and
`machines: []`; wait interruptibly for authoritative held status. Recheck exact
feature, target/remote and worktree state under the short claim, run ordinary
`git merge --ff-only`, inspect required hooks (including post-merge failures),
push master normally over canonical SSH, and prove remote SHA/feature ancestry.
For shared workspace master, acquire the repository claim first, then try the
tracking lock without waiting; release/retry if busy. Hold both only through
merge/hooks/push/proof. On drift/hook intervention, inspect effects and release
once safe before repair. If push outcome is uncertain, reconcile refs before
release; do not repeat blindly. Explicitly release each repository claim and
verify released status before records/CI/next repository. No batch repository
reservation and no legacy job framework are needed.

Final integration evidence records each old target, final feature/new remote,
hook outcome, SSH/ancestry proof and released repository claim. Preserve existing
reviewed nonancestor lineage for older B/C/config deployments; never call those
old SHAs literally merged. Unchanged m8b source heads can gain literal ancestry
proof after integration, while system jwnd/config450/Bf8 stays deployed unchanged.
A later substantive successor needs its normal deployment/acceptance evidence.
Machine755 remains held: this merge request grants neither UI acceptance nor
machine release. Session stays open; no archive/delete/stop, cleanup, system or
profile operation is part of integration. Lead owns state, final readiness and
user communication.


<a id="automatic-machine-release-policy"></a>
### Automatically release after verified deployment and integration (2026-10-22)

**Accepted correction:** user said “release should be automatic after deploy and
merge.” This replaces every earlier three-gate retention decision in this design.
For every deployed physical machine, the lead promptly invokes the normal release
command once deployment/effect verification has succeeded and its complete
deployed feature lineage is integrated into approved remote defaults. No separate
human UI-acceptance or release-direction gate remains. “Automatic” means the
agent performs this ordinary supported step; no background worker, timer, new
API, receipt schema or coordinator enforcement is added.

Before release, inspect authoritative status for the exact session-owned claim,
reconcile unfinished/uncertain command effects and prove both conditions. Run
`dev-session coordination release SLUG --as-is --id CLAIM_UUID --json`, then verify
released status. Missing integration or failed/uncertain deployment keeps ownership;
idle time and turn completion are not substitutes for proof. Preserve separate
merge approval, independent review, short repository claims, original legacy
recovery contracts and the separate exact-session lifecycle authorization gate.
Release does not archive, delete, stop or clean a session. A later deployment
requires fresh machine ownership. The lead reports claim755 already released at
13:04:53 UTC/revision2; do not reacquire it for this source work.

Retain exact machine aliases, system/profile paths, full source/input graphs,
repository/default targets and remote ancestry proof in existing rollout records.
For nonancestor deployed history retain reviewed old/new ranges, independently
proven equivalence and migration provenance; never call a nonancestor SHA
literally merged. When relying on a substantively changed successor, verify its
new deployment before release; replace old “renewed user acceptance” wording with
that concrete verification requirement. No new evidence framework is needed.

Execution packages are disjoint and may begin independently:

| Owner | Exact source paths |
| --- | --- |
| imp0 / B dev-workspace | `portal/internal/workspacecodex/lead_policy.go`, `portal/internal/workspacecodex/lead_policy_test.go`, `portal/internal/teamruntime/runtime_test.go`, `docs/coordination.md`, `docs/coordination-operations.md` |
| imp1 / C workspace | `AGENTS.md`, `docs/coordination.md`, `docs/agent-instructions/deployment.md`, `docs/agent-instructions/lifecycle.md`, `docs/agent-instructions/git.md`, `test/agent_instructions_test.rb` |
| imp1 / configuration | `docs/operations/workspace-coordination-aitherdev.md` |

B changes the shared `CoordinationInstructions` text used by both generated lead
and member bindings, updates existing instruction-contract tests and reconciles
all current claim-policy paragraphs. Keep retained role instructions/settings
unchanged. C reconciles core/routed policy and adds a small instruction-consistency
assertion to its existing suite, retaining discovery-size headroom and every
unrelated route. Configuration follows the generic rule, removes its extra
UI/release gates and updates evidence wording. Existing coordinator owner-only
release, claim shapes, legacy executor tests and lifecycle behavior stay unchanged.
Generic documentation/handoff/monitor skills contain no independent machine
release gate requiring edits; keep installed skill files untouched. No catalog,
model, roster, notification, browser or host-policy change belongs here.

**Delivery:** selected m8b's guide AND generated developer bindings contain the old
three gates. This user's correction applies immediately here. Shared-root prose
can clarify an older guide, but cannot by itself guarantee correction of directly
injected developer instructions for future agents. Lead therefore accepted a
minimal dependent delivery lane: after B's focused change is final and published,
imp1 adds one new runtime-pin stream to C and one matching configuration channel
stream using the ordinary nested-input/confctl tools. Preserve extension and
unrelated nodes; independently prove the resulting graph and B/A identities.
A stays unchanged. All already merged source/history, old pins, deployment roots,
review receipts and lineage remain immutable: append focused follow-up commits;
never fold/rewrite merged groups. These new pins serve a new instruction delivery,
not obsolete iterations of the already integrated Files change.

Parent owns bounded package realization and ordinary user-profile selection so
future technical bindings and the selected guide agree. No system activation is
needed for instruction strings/docs and matching source pins; verify unchanged
host contract. Acquire a fresh machine-only claim near activation, preserve native
Codex/tmux/socket/retained-role identities and existing profile-transition guards,
and retain ordinary forward recovery. Follow-up default-branch integration and
deployment retain their separate authorization requirements. This material policy
correction is not automatically covered by the earlier 32-commit merge approval;
lead resolves exact integration authorization after the concrete reviewed candidate,
without delaying independent preparation or holding a machine while waiting.
Once separately authorized deployment is verified and the deployed follow-up
lineage is integrated, release that fresh claim promptly without another human
confirmation. Automatic release itself grants neither merge nor deployment approval.

Quick checks, in existing repository Nix environments:

- B portal: `go test -mod=readonly ./internal/workspacecodex ./internal/teamruntime -run 'Test(LeadPolicy|CoordinationPolicy|MemberPolicy)' -count=1`.
  Cover fallback/retained lead and member bindings, both release prerequisites,
  no extra human gate, exact-owner/effect checks, unchanged role suffix and
  separate merge/lifecycle boundaries. Rename the old three-gate test as needed.
- C: `ruby test/agent_instructions_test.rb`; check consistent policy across the
  six owned files, preserved merge/lifecycle rules and the unchanged size limit.
- All owners: normal hooks/format and `git diff --check`; configuration docs need
  no host build. For dependent pins use declared Nixfmt/lock checks and
  `bin/check-dev-workspace-deployment --workspace-root PATH --configuration-root PATH`.

Commit intended policy and pin changes and pass quick checks before affected
independent final review, then run only the bounded composed-package and ordinary
activation verification required for instruction delivery. Preserve unaffected
review/CI/browser evidence; no native50, incident reopening, full host suite or
new performance campaign. Acceptance: source guides and generated bindings state
verified deployment plus integrated deployed lineage, instruct prompt owner-only
release without another human gate, and the selected package delivers that text.
Parent records deployment/integration/release outcomes; architect performs none.
