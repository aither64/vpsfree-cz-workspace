# Published advisory corrections

## Expanded scope: authoritative delta brief

This section supersedes conflicting restrictions in the original brief below.
The user explicitly requested published CVE-link/node-membership corrections,
editable publication time, retract/delete, and matching `vpsadmin-webui` changes
where appropriate. The lead accepted the lifecycle and compatibility decisions
below. Existing committed heads inspected: vpsAdmin
`d80ac520c66a9d4a318df517a06f13ac717f2399`, client
`9140e4bf4d286865b016f2549d0b883ccbb624e1`, KB contract
`0a12d7d97703ce5e6405130bf9325f28ddcf4bee`. No production action is authorized.

### Settled API behavior

Use the existing parent/CVE/node resource and model owners. Original edits,
CVE create/update/delete and node create/update/delete work for draft, published
and retracted advisories. Add `retracted` to expected-state choices. Each action
requires the existing parent `expected_content_revision`, accepts optional
`expected_state`, locks/reloads the parent before checking both, rereads scoped
children under that lock, and increments the revision once on successful mutation.
No CVE can move between advisory parents. Keep existing normalized CVE format,
uniqueness and node scope validation. Published/retracted node create/update
require resolved states and mitigation timestamps as previously designed.
Removal may leave missing node rows or zero CVEs: do not run whole-advisory
publication validation on corrections or introduce a new minimum constraint.

Original PUT accepts and intentionally changes/clears `published_at` in every
editable state, following its nullable model type. Preserve exact seconds on UI
round trips and preserve null rather than pre-filling the current time. Clearing
it leaves the public value blank/dash; current list ordering falls back to
`created_at` via existing COALESCE logic. No automatic publish/state reset occurs.
Other identity/authorship fields, state and existing update history remain
unchanged by corrections. Only explicit lifecycle actions change state/delete.

Every published/retracted node create/update/delete rebuilds affected VPS/user
projections under the parent lock in the same transaction, including localized
notes, row deletion, derived membership/counts and the revision. Draft behavior
remains unchanged. Failure rolls all of it back. Parent/CVE edits do not rebuild.
The existing locked manual rebuild remains. No schema or new correction endpoint.

Add ordinary admin-only lifecycle actions to `SecurityAdvisory` resource:

| Action | Interface and result |
| --- | --- |
| Retract | `POST /security_advisories/:id/retract`, scope `security_advisory#retract`, ordinary advisory wrapper/output |
| Delete | `DELETE /security_advisories/:id`, scope `security_advisory#delete`, ordinary advisory wrapper/input and `ok!` result |

Both require expected revision and accept expected state under the parent lock.
Retraction permits published only; it sets `state=retracted`, stamps
`retracted_at` once and increments content revision once. It preserves publication
time/authorship, every report/update row and projections, with no mail/update
post. A stale retry conflicts; a fresh already-retracted request is an invalid
transition. Corrections to the retracted report remain allowed. There is no
implicit restoration or automatic reannouncement.

Deletion permits any existing state, uses transactional `destroy!` and existing
dependent associations, and returns 404 if repeated after success. It permanently
removes the advisory, original/update translations, update posts, CVE links, node
rows/notes, affected projections and outage links. It does not delete referenced
users, nodes, VPSes, environments, locations, outages, transaction concerns or
mail/log history. No soft-delete framework, tombstone or new cascade migration.
Recovery of deleted content needs an existing backup; software rollback cannot
restore it. This is an implementation capability, not permission to delete live
data. Existing scoped tokens gain no new retract/delete scope automatically.

Publication now checks `draft` under its existing lock before doing anything;
published/retracted requests fail without resetting a cleared publication time.
Successful draft publish retains its existing unchanged-content-revision contract
and publication recovery behavior. The separate advisory-update resource retains
its existing explicit state/publication-time fields and optional mail choice;
do not silently remove its supported announcement behavior.

### Deletion races and ownership

There are no advisory SQL FKs in the inspected schema. The model already owns
all core dependent deletions; `plugins/outage_reports/api/models/outage_security_advisory.rb`
adds `SecurityAdvisory.has_many :outage_security_advisories, dependent: :delete_all`.
Use these existing associations, including both plugin modes, instead of manual
hard-coded child-table cleanup.

Parent locking must also cover `SecurityAdvisory#create_update!`,
`SecurityAdvisoryUpdate#update_translations!` and the separate update Delete
action, and outage-link Create in
`plugins/outage_reports/api/resources/outage_security_advisory.rb`.
Reload the parent under lock, and reload the update child under the parent lock
before writing its translations. These narrow supporting changes prevent an
already-loaded object from creating children after parent/child deletion.
Preserve announcement mail defaults, choices and rollback behavior. Missing
parents/children fail conventionally. Serialize correction/delete/update creation
without a generic lifecycle framework or modifying unrelated resources.

### Ready implementation packages

**A delta, implementer0:** existing model/resource/spec/docs/locale ownership,
plus `api/lib/vpsadmin/api/resources/security_advisory_cve.rb`,
`api/models/security_advisory_update.rb`, its resource's Delete path and the
outage-link Create owner above. Extend existing advisory model/API/concurrency
specs and `api/spec/api/plugins/outage_reports/security_advisory_spec.rb`.
Own broadened corrections, lifecycle actions, parent-lock serialization and
updated behavior/compatibility docs. Inspect existing route/default Delete
conventions; do not add an HTTP variant. A can start now.

**B delta, implementer1:** same two legacy PHP advisory files, existing browser
scenario/helper and only necessary fixtures/locale outputs. Restore publication
time/CVE editing in published/retracted forms; allow an explicit empty CVE set
when editing while retaining existing draft-creation requirements. Pass rendered
state/revision to every parent/CVE/node mutation. Add explicit node add/remove
controls using existing CRUD; omission from a partial POST must not implicitly
delete rows, and a removed row must not be silently re-created on the next save.
Node removal must work even when the node is no longer eligible for a new row.
Keep per-request atomicity and stop sequential saving on the first conflict.
Use POST+CSRF confirmation forms for lifecycle actions, with expected state and
revision; delete confirmation describes loss of advisory/updates/node assessments.
Retract appears for published only; delete for all states; success redirects to
detail or list as appropriate. No mail toggle on these silent actions. B can
start against A's settled interface; browser acceptance depends on A.

**C delta, implementer1:** same reconciler/spec/README/permissions files. Before
the first applying-sync write, require expected-state capability on all SIX
mutation types the sync actually uses: parent Update, CVE Create/Delete and node
Create/Update/Delete. Every such request sends `expected_state: draft` alongside
its revision; API CVE Update also accepts the guard although sync does not use it.
Keep the existing root OPTIONS validation, refuse missing/malformed capability
on any action with zero writes, and preserve read-only/dry-run operation. Never
downgrade after a refusal. Existing draft/digest/source/evaluation protections
and checkpoints remain. No client retract/delete/correction command or new token
scope is needed. C can start against A's agreed metadata. Implementer1 sequences
B/C; implementer0 serializes all Git/index operations in the vpsAdmin worktree.

**E ready for lead assignment:** the separate React `vpsadmin-webui` package is
specified below. It depends on A's settled API, has independent repository/file
ownership, and does not block A/B/C. No app redesign or client migration.

### Delta acceptance, compatibility and delivery

Use the previously specified Nix quick checks, adding touched CVE/update/plugin
Ruby files. Required focused API/model/concurrency checks now prove all new
mutations in published/retracted states, intentional null timestamp/zero CVEs,
authorization, missing/stale revision, wrong state, invalid node rollback and
projection refresh on membership add/remove. Verify new action metadata/scopes,
DELETE JSON body parsing, repeated retract/delete behavior, blocked republish,
preserved explicit update announcement state/time/mail behavior and draft
publication readback. Browser coverage includes CVE empty/nonempty correction,
node add/remove, timestamp edit/clear and confirmed retract/delete.

Deletion tests assert the complete owned cascade and preservation of referenced
objects/logs in full and core modes, rollback on a dependent failure, and races
against correction, update creation/translation and outage-link creation. Reuse
bounded concurrency barriers; no sleep-only assertions. C tests publication
racing each newly enabled CVE/node membership write and refusal of missing
capability for each of the six actions before any mutation, with unchanged
baseline on failed writes and retained publication recovery coverage.

No migration or state conversion is planned. Updated sync requires the expanded
API metadata; the earlier two-action-only API is insufficient and must fail
closed. Earlier client `9140e4b` remains unsafe for membership writes against the
expanded API, so update all sync consumers before resuming writes and avoid mixed
API pools. Nullable time and empty CVE/node sets already fit persisted types;
older publication validation may reject them if deliberately returned to draft.
Correction does not return an advisory to draft. Retraction uses the existing
state enum; deletion is irreversible without backup. No deployment is authorized.

After all expanded deliverables and quick checks, consolidate superseded
unmerged restrictions/tests/docs and repeated KB pin commits into coherent final
history. Preserve earlier heads as evidence, never rewrite remote defaults.
Refresh D to the final pushed vpsAdmin head, then run new mandatory whole-branch
review before longer verification. The paused earlier review does not certify
this expanded result. No open correctness decision blocks A/B/C.

## Package E: React advisory management

### Base, ownership and scope

Fresh canonical SSH fetch and remote HEAD inspection selected `main` at
`f2765d3fd778927f4cda3563f66615bfcf72b7cf`. The lead registered
`worktrees/2026-11-01-published-advisory-corrections/vpsadmin-webui` on
`dev/published-advisory-corrections` from that exact revision. E belongs to one
retained implementer assigned by the lead after its A/B/C workload boundary;
no concurrent Git work in this repository. Architect inspection made no app edits.

Open canonical PR file inventories checked on 2026-11-01 contain no advisory
implementation overlap. PR74 changes shared HaveAPI transport; other open PRs
overlap common requirements/workflow/work-log docs. Preserve their changes,
recheck before publishing, and keep E in the existing advisory adapters. Do not
import another feature branch or access another session's checkout. The repo
requires a focused PR against canonical `main`, naming REQ-055 and preserving
REQ-054's public/admin access boundary. PR approval is not merge/deploy approval.

The application owns handwritten TypeScript adapters using `haveapi-client`
0.32.0, not a generated advisory SDK. No client generation, dependency upgrade,
BFF, router, infrastructure or database change is needed. The current adapters
omit content guards, CVE reconciliation uses parallel writes, and the header
couples edit eligibility with publication. These are concrete compatibility
changes within the existing management flow.

### Interfaces and behavior

- Add typed `content_revision` and advisory mutation preconditions. Parent PUT,
  CVE CRUD, node CRUD, retract and delete send the captured revision and state;
  namespace DELETE bodies conventionally (`security_advisory`,
  `security_advisory_cve`, `node_status`). Publish sends its required captured
  revision and existing publication/mail payload; it remains draft-only and
  does not increment the revision. Do not add unsupported state input to publish.
- Before an affected workflow's first write, fetch authenticated root OPTIONS
  through existing `haveApiCall({ method: 'OPTIONS', path: '/' })` against the
  configured versioned API base, following C's resource/action graph. Validate
  the complete selected workflow's actions, including CVE mutations following
  draft creation. Use real lifecycle endpoint OPTIONS when the parent exists;
  do not invent child IDs such as `/0` for action discovery. Keep the helper
  advisory-specific and leave shared transport unchanged.
  In the unwrapped root description, parent actions are under
  `resources.security_advisory.actions`, CVE actions under
  `resources.security_advisory_cve.actions`, and node actions under
  `resources.security_advisory.resources.node_status.actions`. Guarded actions
  require `input.parameters.expected_content_revision.type == 'Integer'` and
  `expected_state.type == 'String'`, with `expected_state.validators.include.values`
  an array of strings containing the captured state. Parent Create has no
  revision precondition; Publish has revision but no expected-state parameter.
  Missing/malformed/denied capabilities or invalid revision disable affected
  writes with an upgrade/unavailable explanation. Never retry without guards.
  Root metadata with an authenticated user is authorization-filtered, but pinned
  HaveAPI 0.32.0 only runs endpoint `prepare` for endpoint OPTIONS. Root metadata
  therefore proves contract capability, not authority over a specific record.
  Preserve admin route guards and every mutation's server authorization/locking.
  Fetch once per attempted workflow, or scope any local cache to API/auth identity;
  do not reuse anonymous bootstrap/discovery metadata or fall back to it after an
  auth failure. Public reading, admin inspection and the separate announcement
  flow remain available. A mixed API pool is unsupported.
- Capture state/revision with the data shown when opening an edit, confirmation
  or bulk operation. Obtain a coherent parent/children snapshot (read parent,
  children, then verify unchanged parent revision/state before enabling the form)
  where the operation reconciles children. Do not fetch a fresh revision at save
  and apply old form values to it. Background invalidation must not reset input,
  close a failed editor, or silently rebase a stale edit onto newer content.
- Serialize parent/CVE saving and bulk node writes. Start at the captured
  revision; advance exactly once after each acknowledged successful correction,
  using returned revision where supplied or the API's established +1 contract
  for child responses. Never adopt an arbitrary newer read-back revision.
  Stop on conflict, refusal or uncertain outcome. Preserve additions-before-CVE-
  deletions, unchanged row IDs, and the existing explicit partial-success UI.
  A parent+children save is not one transaction. Show completed work and retain
  unsaved values; stale/uncertain bulk work needs explicit reload/review before
  continuation, not blind retry. Draft create must pass the returned draft
  revision/state into CVE reconciliation and must not create a duplicate parent
  after a child failure.
- Enable original name/localized text/CVEs/publication-time editing in all three
  states. Empty CVEs are valid on edit; draft creation retains its existing
  required-CVE rule. Separate `canEdit` from `canPublish` and `canPostUpdate`:
  publish only draft; existing update posting stays published-only with its
  explicit mail/state/time behavior. Original corrections have no mail choice.
- Preserve seconds and null in publication/mitigation timestamps. Use an opt-in
  precision helper or advisory-local conversion and `step=1`; do not change all
  unrelated datetime controls. A no-change round trip must retain the exact
  persisted value; explicit blank sends null, with no current-time fallback for
  correction. Publication readiness checks apply to publishing, not correction.
- Extend existing node row edit/add/remove and bulk controls; published/retracted
  create/update offers resolved states with required mitigation timestamps.
  Existing rows for nodes outside the active inventory remain visible/removable;
  use included node identity or an ID fallback. Removal is explicit and does not
  silently re-create rows on later ordinary saves. Missing rows stay missing
  unless an explicit add/bulk operation includes them. Node notes use actual
  localized `LANG_note` fields (current generic `note` input is not an API field),
  preserving other languages when editing one. Reuse loaded languages and the
  existing localized form patterns.
- Add direct retract and advisory delete adapters and confirmation dialogs.
  Retract is published-only, silent, and preserves the report and history;
  deletion is available in every state and clearly describes permanent loss of
  the advisory, updates and assessments. Use captured guards, prevent duplicate
  submission, retain errors, and navigate to the list only after acknowledged
  delete success. Do not report an uncertain response as successful deletion or
  retry automatically. Read-back 404 may reconcile an uncertain delete explicitly.
- After corrections/partial success, invalidate advisory, CVE/node, list and
  affected-user/VPS queries; include existing public advisory cache keys when
  returning to public/member views. Retract refreshes state without clearing
  projections; delete evicts the removed detail and refreshes lists/relations.
  Preserve direct admin route gates, public read access, outage linking, manual
  rebuild, and separate update edit/delete/announcement behavior.

### File boundaries and required documentation

E owns `src/lib/api/securityAdvisories.ts`, `securityAdvisoryRelations.ts`, their
focused tests, and advisory-specific helpers if needed; existing shared transport
stays unchanged. UI owners under `src/pages/app/admin/security/` are
`AdminSecurityAdvisoryDetailPage.tsx`, `AdminSecurityAdvisoriesPage.tsx`,
`securityAdvisoryAdminApi.ts`, `securityAdvisoryAdminModel.ts`,
`SecurityAdvisoryEditorModal.tsx`, `SecurityAdvisoryNodesPanel.tsx`,
`SecurityAdvisoryNodeForm.tsx`, `SecurityAdvisoryDetailHeader.tsx` and
`SecurityAdvisoryDetailDialogs.tsx`, plus focused tests and both
`src/i18n/locales/{cs,en}/admin/security_advisories.ts` catalogs. A small advisory
mutation hook/helper extraction may keep the detail page within its existing
structural limit; remove its resolved ledger exception rather than refreshing a
hash to excuse growth. Adopt changed deferred E2E files into `tsconfig.e2e.json`
and `scripts/fixtures/e2e-type-coverage.json`; do not weaken the type gate.

Update REQ-055, affected workflow/API/action contracts and evidence entries,
generated `docs/design/IMPLEMENTATION_INVENTORY.md`, and one dated
`docs/work-log/` entry with a WORK_LOG pointer. Explain per-request atomicity,
partial/uncertain outcomes, supported API upgrade ordering and rollback limits.
The API's advisory documentation remains the authoritative mutation contract.
Read local AGENTS/procedures before edits. Locked terminology was resolved with
the repository's Nix expressions and both guides read at
`a65a4dfeb92a59df4a80a737a20bcbf8558793ff`; record it with E. Do not bump that
runtime/module input merely to change UI forms. The context-owning lead applies
the user-facing writing skill to final cs/en copy before commit.

### Acceptance and commands

Use the pinned `nix develop` shell and root `npm ci`; install BFF dependencies
only if a required aggregate check actually needs them. Quick verification:
`npm run docs:inventory`, `npm run ci:quick`, and focused
`npm test -- src/lib/api/securityAdvisories.test.ts src/lib/api/securityAdvisoryRelations.test.ts src/pages/app/admin/security`.
If a new test lives under a different advisory-specific name, include that file.
Verify configured author/committer identity and declared hooks before committing.

Tests must exercise real HaveAPI serialization, especially namespaced DELETE
bodies and all guards; all editable states; empty CVEs; exact/null timestamps;
localized notes; sequential revisions; draft publish race; concurrent edit/retract
conflicts; no writes without capabilities; retained input and partial outcomes;
affected-count refresh; explicit retract/delete; and unchanged announcement mail
and state/time controls. No UI-only fixture claims backend atomicity or cascade.
Package A owns that real API evidence.

After committed-deliverable independent review, required longer checks are
`npm test`, `npm run build`, and focused browser runs using the repository wrapper:

```sh
npm run e2e -- e2e/specs/app/security_advisories_admin.spec.ts e2e/specs/app/security_advisory_update_mutations.spec.ts --project=chromium
npm run e2e -- e2e/specs/admin/security_advisory_nodes_mobile_actions.spec.ts e2e/specs/admin/security_advisory_outages_mobile_actions.spec.ts --project=mobile-chrome
nix build .#frontend .#bff .#checks.x86_64-linux.provenance .#checks.x86_64-linux.source-contents .#checks.x86_64-linux.package-contents
```

Add new correction/lifecycle cases to the selected browser files; include desktop
and mobile cs/en confirmation/error interactions. The current mobile-WebKit
testMatch excludes these advisory files, so do not claim a zero-test WebKit run
as coverage. Capture implemented desktop/mobile UI using synthetic fixtures for
progress and final PR handoff. Use an own free local server port, no production
credentials or live scenario commands. Long/uncertain commands use the mandated
watcher workflow. Inspect normal feature/PR CI without expanding into a release
campaign; any required gate failure is investigated and recorded.

### Compatibility, KB and recovery

Deploy A's complete API before enabling E's writes, with C already upgraded before
resuming sync. New E remains readable against older APIs but affected writes fail
closed; old E does not satisfy the current revision protocol and is not a safe
admin-write rollback target. UI rollback leaves persisted corrections intact;
re-enable writes only with a compatible UI/API pair. No new persisted browser
format, schema, daemon/OS coordination or generated-client dependency is introduced.
Cleared timestamps, removed CVEs/nodes and retraction are intentional persisted
state; deletion needs backup restoration, not a software rollback.

Canonical KB inspection at `0a12d7d9` found no advisory semantic/page/capture
bindings and no `vpsadmin-webui` input in the contract inventory. E therefore has
no contract pin or KB page/capture to fabricate. Its repository screenshots are
UI review evidence, not KB publication. D still refreshes all five existing
vpsAdmin pins to final A/B source and runs the mandatory full strict `bin/check`;
do not substitute targeted checks or start unrelated content/capture work.

No open E product decision or cross-API change blocks assignment. No application
edits, builds, production writes, deployment or integration were performed by
the architect; implementation and verification remain with assigned owners.

## Original brief (superseded where the expanded delta differs)

Status: implementation brief. architect0 owns this design; the lead accepted
the decisions below in the same-session assignments on 2026-11-01. No application
edits, production requests, deployments or commits were performed by the architect.

## Scope and source evidence

Allow administrators to correct an original published advisory's name, localized
summary/description/response, and existing structured node rows (state, mitigation
times and localized notes) through the existing PUT actions. Corrections never
send mail, publish again, reset state, create another advisory or append an update.
The separate `security_advisory_updates` announcement interface remains unchanged.

Fresh SSH fetch of canonical `repos/vpsadmin.git` selected `origin/master` at
`610a96f8ce523afbcd3e4374a70047dbe3264b0d`. This contains the advisory feature.
The supplied reference `ff730be468e366ee346dc6d02dc0fe57c3f8677c` is its ancestor,
23 commits behind; canonical local `master` was stale and was not selected.

The necessary companion change belongs in `security-advisories`. Fresh SSH fetch
and `ls-remote --symref origin HEAD` identify its actual default as
`2026-07-13-security-advisory-automation` at
`7b6c71807e3c5a41f585fd1d9563e151ada71244`; there is no `origin/master`.
Use a new session-owned branch from that exact default. Comparison against public
feature `33f253a9dd8242ed23271399339db023068b86db` shows no changes to APIClient,
`update_advisory`, `reconcile_node_statuses`, revision checks or draft guards.
That feature adds status-history handling around `sync`, `ready`, `evaluate` and
`publish`; retain it when applying this narrow companion patch later. Do not import
its unrelated history into this initiative. Comparison used only canonical Git
objects, not another session's files or checkout.

Read guidance: workspace AGENTS and required projects/sessions/git/lifecycle/
documentation/verification/knowledge-base/commits procedures, documentation and
handoff skills, vpsAdmin AGENTS and development/localization/testing procedures,
docs index, advisory owners and specs; security-advisories AGENTS, README and
API permissions; canonical KB-contract AGENTS and WebUI workflow. vpsAdmin has
no existing advisory behavior page, so add one concise page and index entry.

## Interface contract

The existing parent `PUT /security_advisories/:id` and nested
`PUT /security_advisories/:id/node_statuses/:row_id` retain their scopes, payload
wrappers, response shape and required `expected_content_revision` integer.
Add optional `expected_state`, with `draft` and `published` choices, to these two
PUT actions only. Omission leaves deliberate ordinary corrections possible;
supplied state is a precondition, never a state assignment. Check it under the
same parent lock as the revision. State/revision conflicts return HTTP 409 without
any changes. Do not add an endpoint, schema migration, mail option or API version.

| Operation | Draft | Published | Retracted |
| --- | --- | --- | --- |
| Original name and localized text PUT | Existing behavior | Allowed, silent | Rejected |
| Existing node-row PUT | Existing behavior | Allowed, silent, atomic projection refresh | Rejected |
| CVE create/update/delete | Existing behavior | Still rejected | Still rejected |
| Node-row create/delete | Existing behavior | Still rejected | Still rejected |
| Separate advisory-update resource | Unchanged | Unchanged | Unchanged |

`published_at` remains editable for drafts. On a published original, omission
preserves it; an exactly equal normalized timestamp is accepted as a no-op;
a different value, including null when currently non-null, rejects the entire
request. Compare typed time values, not textual timezone representations.
Use conventional record/input validation errors for this field. Preserve
`id`, `external_id`, state, `created_by`, `published_by`, `created_at`,
`published_at`, `retracted_at`, CVE associations and every existing update row.
Only the intended content, `updated_at`, and one content-revision increment change.

Published node corrections must leave the edited row `not_affected` or
`mitigated`; the existing model still requires both mitigation times for
`mitigated`. Keep draft `unknown`/`vulnerable` support. Do not run global
`validate_publishable!` on corrections: a newly added unrelated active node must
not block correction of an older advisory. Preserve existing active-node scope
validation; permitting edits to retired nodes or changing publication validation
is outside this package. Omitted localized fields are preserved, and explicit
blank/null notes retain their current clear semantics.

## Atomicity, projections and concurrency

Keep the existing draft mutation helper's contract for its other callers. Add a
small content-edit path in the same model/resource owners, sharing revision logic
where useful; do not globally loosen `mutate_draft!` and thereby enable CVE/node
membership changes. All correction steps run in the parent row's `with_lock`
transaction:

1. Reload/lock the parent and check allowed state, optional expected state and
   expected revision before writing anything.
2. For parent PUT, validate publication-time immutability and apply original
   attributes/translations. For node PUT, reread the scoped child under the lock
   before applying attributes/notes and validating the resulting row.
3. After a published node PUT, run the existing affected-VPS/user rebuild before
   committing. Parent text edits and draft node edits do not start a rebuild.
4. Increment parent `content_revision` once only after every step succeeds.

Any row/translation/projection failure rolls back all preceding changes,
including deletions and the revision. Do not catch and suppress errors inside the
transaction. Reuse the existing rebuild meaning: current active/suspended VPSes
on mitigated nodes, with current owner/environment/location/node and corrected
mitigation times. `not_affected` removes those VPS rows; affected users and their
VPS counts are derived again; transitions back to mitigated add them. Node count
continues to count mitigated rows. This is a current snapshot, not reconstructed
historical VPS placement. Never implement a second projection algorithm.

The public manual `rebuild_affected!` path must take the same parent lock, since
an unlocked rebuild could otherwise overwrite a committed correction with old
rows. Prefer making the model entry point lock so publish/manual/correction calls
share the serialization. Avoid stale loaded associations; use fresh scoped reads
under that lock. Inspect locking reads where an existing outer transaction can
retain a repeatable-read snapshot, and verify actual concurrent behavior rather
than substituting a mocked lock. Production uses READ-COMMITTED; the test helper
uses REPEATABLE-READ with snapshot isolation off. Do not change database defaults.

Two edits using the same revision must have exactly one winner. A subsequent
fresh-revision correction must use current child/projection data. A manual
rebuild waiting on a correction must finish with its corrected projections.
Use bounded barriers/timeouts and independently committed fixtures for meaningful
concurrency coverage, following existing model concurrency specs.

## Draft-sync race and required client protection

`publish!` currently leaves `content_revision` unchanged, and the companion
client's publication readback/recovery requires that contract. Preserve it.
Once PUT accepts published rows, a request prepared while draft could otherwise
cross publication with the same revision and mutate the published original.
This is why the optional expected-state precondition is necessary.

The WebUI submits the state rendered with each edit form, alongside its rendered
revision. It must retain submitted state/revision when rerendering an error,
rather than silently rebasing a stale form onto fresh values. The draft-sync
client sends `expected_state: draft` on both parent and existing-node PUTs.
Existing draft-only node/CVE create/delete paths need no new parameter.

Before `sync --apply` performs its first write, verify advertised support for
`expected_state` on both PUT actions via ordinary OPTIONS metadata. Root schema
discovery can cover the new-advisory case without creating a row just to probe
capability. Keep the check local to applying sync; read-only commands and dry-run
planning should remain usable on older APIs. Missing/malformed capability or an
OPTIONS refusal stops applying sync before any create/update/delete; no fallback
to an unguarded PUT, server-version guessing or retry after removing the parameter.
Check all required capabilities before the first write, not after parent content
has already changed. Existing revision/digest/draft/committed-source/evaluation
checks and post-write checkpoints remain intact. A state conflict stops the run
and propagates; do not rewrite the committed baseline to conceal it.

Add client tests simulating publication between preflight and parent PUT, and
between preflight and node PUT. The simulated corrected API must reject the
draft precondition without changing published values, sending mail or updating
the client's recovery baseline. Also test missing capability on either action,
malformed metadata, no writes on refusal, guarded successful sync, and preserved
publication/recovery behavior with the same content revision.

## WebUI behavior

Keep the existing Edit advisory and Node statuses actions and their CSRF/admin
checks. On a published original, show publication time and CVEs as read-only
values; omit `published_at` and skip CVE parse/reconciliation on submission.
The current form sends the timestamp rounded to minutes, so leaving it in the
payload would either reject otherwise valid corrections or corrupt original time.
Use existing labels and rendering helpers; no new announcement workflow.

For published node forms, edit existing eligible rows only. Do not automatically
POST a new row because an active node was added after publication; filter the
display/save set consistently. Draft forms keep their existing create behavior.
Preserve full seconds when round-tripping existing node timestamps so saving a
note does not truncate mitigation times on every submitted row. Preserve blank
values and language-specific notes. The existing form makes sequential per-row
requests: each request is atomic and revision-checked, while an error in a later
row does not undo already successful rows. Keep and document that boundary; a
batch endpoint or new transaction protocol is not required.

Extend the existing advisory browser scenario for published text and node edits,
unchanged publication time/CVEs, no automatic update, read-only publication
fields, stale form state/revision refusal, and affected-user display after node
correction. Reuse current fixtures/helpers where possible; avoid touching shared
unrelated browser infrastructure. API specs establish the mail/history guarantee.

## Implementation packages and ownership

The lead assigns these complete packages after accepting this brief. Two
implementers can work on distinct files in the vpsAdmin worktree; implementer0
owns serialized Git/index/hook operations. Nobody stages another owner's unfinished
files. The companion repository has its own session-owned worktree and branch.

### A: vpsAdmin API, model, focused tests and behavior docs — implementer0

Files: `api/models/security_advisory.rb`,
`api/lib/vpsadmin/api/resources/security_advisory.rb`, existing
`api/spec/models/security_advisory_spec.rb` and
`api/spec/api/resources/security_advisory_spec.rb`; a focused model concurrency
spec if needed. Add `docs/security-advisories.md` and its `docs/README.md` link.
API locales generated/normalized for changed metadata/errors belong to this
package. Change node model only if needed for the narrow state validation.

Own locked corrections, expected-state contract, published timestamp protection,
atomic rebuild serialization, rollback and authorization coverage. Document
silent original edits versus explicit announcements, field/state restrictions,
revision/state preconditions, projection meaning and per-request atomicity.
No changes to migrations, `security_advisory_update.rb`, notification templates,
or CVE mutation behavior are planned. This package has no implementation dependency.

### B: WebUI and browser regressions — implementer1

Files: `webui/forms/security_advisory.forms.php`,
`webui/pages/page_security_advisory.php`,
`tests/playwright/webui/specs/security-advisories.spec.cjs`, its existing
`lib/pages/security-advisory.cjs` helper if needed, and only necessary advisory
fixture changes in `tests/suite/webui.nix`. WebUI locale artifacts belong here
only if source wording actually changes. No API/model/spec/docs overlap with A.

Own the UI behavior above. It may be implemented in parallel against the settled
PUT contract; executing browser acceptance depends on A. Route new required API
behavior through the lead instead of independently editing A's files.

### C: security-advisories guarded sync and compatibility docs — implementer1

Files: `lib/security_advisories/reconciler.rb`, `spec/reconciler_spec.rb`,
`README.md`, `docs/api-permissions.md`; modify APIClient only if its existing
OPTIONS helper proves insufficient (it currently supports OPTIONS). Keep scope
descriptions accurate; this change adds no token scope or correction command.

Implement after B, or independently before B at the lead's choice. Contract
depends on A's agreed parameter/metadata, not its unfinished code. Use focused
fake-API tests to prove guarded writes and pre-write fail-closed behavior. Preserve
feature-line status-history logic when later consuming this patch; it is not
needed in our default-based narrow deliverable.

### D: pin the final WebUI revision and run the KB contract — implementer1

Lead disposition: this is a required verification package under the canonical
WebUI procedure. The targeted checker is diagnostic only and does not replace
the pinned full check. Assign after B/C, when the final vpsAdmin feature commit
is committed and pushed. D has independent repository files but depends on that
exact immutable revision; a later vpsAdmin change requires updating the pin and
repeating affected verification.

Fresh SSH fetch and `ls-remote --symref origin HEAD` on 2026-11-01 confirmed
`git@github.com:vpsfreecz/vpsfree-kb-contracts.git`, default `master`, at
`ce2c8cd9358c3636e5d39343e595df813a0b197f`. The architect read its complete
`AGENTS.md` at this head, along with the canonical
`docs/webui-change-workflow.md`, relevant README setup and `flake.nix`.
The lead registers a new session-owned worktree/feature branch from this base;
the implementer reads those repository instructions in full before editing.
Also follow workspace Git, verification, commits and configuration-input
procedures. Refresh upstream before branch publication and report any moved base.
The architect creates no worktree and changes no pins.

Only these five files belong to D:

| File | Exact value to update |
| --- | --- |
| `flake.nix` | `inputs.vpsadmin.url` to `github:vpsfreecz/vpsadmin/<final-40-character-SHA>` |
| `flake.lock` | Regenerate the selected `vpsadmin` input with Nix |
| `captures.json` | Top-level `vpsadmin_commit` |
| `contract/navigation.yml` | Top-level `vpsadmin_revision` |
| `contract/pages.yml` | `revisions.vpsadmin` |

All four source pins currently contain
`939159f27b5d627930281d5fac0c0aa9ba53bfc7`. Change them to the same pushed final
vpsAdmin SHA; do not use a branch name. Preserve the explicit
`inputs.vpsadmin.inputs.vpsadminos.url` override and `revisions.vpsadminos` at
`6bdf458fd9105379860234ff33d352e55844f08f`, and preserve unrelated root input pins.
Inspect the generated lock diff: any transitive change must follow from the
selected vpsAdmin input; do not refresh all inputs or hand-edit lock metadata.
Do not change screenshot provenance to pretend existing images were recaptured.

From the new contract worktree, after updating the four source pin values:

```sh
nix flake update vpsadmin
git diff --check
git diff --stat
git diff -- flake.nix flake.lock captures.json contract/navigation.yml contract/pages.yml
```

Verify those files agree on the full SHA, inspect/install any declared hook
framework (none is declared in the inspected root/package.json), and commit the
focused pin update under the workspace commit procedure. Keep its complete
base-to-head diff/history in the initiative's final review packet; the lead
applies mandatory-review mechanical-content rules without inventing an extra
substantive review gate. Do not bypass hooks. The full check uses the pinned shell
and its default pinned `VPSADMIN_KB_VPSADMIN_SOURCE`, not an environment override
to a mutable checkout:

```sh
nix develop -c bin/check
```

Have a fresh verification watcher launch/monitor this uncertain-duration check
under `dev-session-monitor`; do not start a cluster, run captures or perform
production/staging operations. Use the strict command above, without
`--allow-missing`. Preserve exact contract and vpsAdmin heads, command, exit status
and log path. A successful targeted checker or permissive CI check is not a
substitute. Stop unexpected kernel builds under the verification procedure.

Acceptance: all five pin locations are coherent, the final diff is pin-only,
the full contract check succeeds, and the final source still has zero advisory
controls/page/capture bindings. No page text, PNG, fingerprint, semantic ID or
capture record is fabricated to make the result pass. Publish the feature branch
and inspect its CI; integration into `master` still requires explicit direction.

If the full check fails, preserve its first actionable failure. Distinguish an
environment error, final-feature drift and existing baseline drift using a
same-session clean snapshot of the recorded contract base and, when relevant,
the pre-correction vpsAdmin base. Reuse the standard checker; do not repair
unrelated fingerprints, missing media or stale capture provenance automatically.
Report the exact failing command/path, base/final comparison and smallest needed
follow-up to the lead. A baseline failure is a recorded verification limitation,
not a passed check. No baseline-drift investigation is needed before a failure
provides concrete evidence.

## Acceptance and verification

Quick checks per owned repository/component: `git diff --check`, Ruby/PHP/JS
syntax as relevant, component RuboCop/formatting and installed Overcommit hooks.
Use the repository's Nix shells, whose component shell hooks change directory.
Suggested commands from the vpsAdmin root:

```sh
nix develop .#api -c bundle exec rubocop models/security_advisory.rb lib/vpsadmin/api/resources/security_advisory.rb spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
nix develop .#webui -c php -l forms/security_advisory.forms.php
nix develop .#webui -c php -l pages/page_security_advisory.php
nix develop .#webui -c node --check ../tests/playwright/webui/specs/security-advisories.spec.cjs
```

Include a new concurrency file in lint/spec commands if created. Existing
foundation patterns cover model specs; platform-operations patterns cover the
existing resource spec. Do not add arbitrary CI topic changes. Honor generated
locale hooks. Lead applies required user-facing writing guidance before commits.

After intended changes are committed and quick checks pass, mandatory independent
review covers complete branch histories and migration provenance (no new
migrations). Longer/uncertain test runs use the mandatory fresh verification
watcher; do not launch them inline. Target these bounded checks, then stop when
they resolve the identified risks:

```sh
VPSADMIN_PLUGINS=all nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
VPSADMIN_PLUGINS=none nix develop .#api -c bundle exec rspec spec/models/security_advisory_spec.rb spec/api/resources/security_advisory_spec.rb
./test-runner.sh test 'webui#security-advisories'
```

Companion repository: `nix develop -c bundle exec rubocop --parallel --force-exclusion`
and `nix develop -c bundle exec rspec spec/reconciler_spec.rb`, followed by its
ordinary complete suite when appropriate. Its Nix shell installs the locked
bundle. Keep successful exact-head evidence; investigate failures before retries.
Inspect branch CI after publication without merging. Stop unexpected local
kernel builds under the workspace verification procedure.

Required assertions across these checks:

- Authorized published parent/name/localized corrections and node/note/time
  corrections succeed; original publication identity, CVEs and update history
  survive; no mail chain, advisory creation or publish call occurs.
- Missing/stale revision, wrong expected state, unauthorized writes, changed
  publication time, unresolved published node state and invalid mitigated times
  reject with no partial text/note/projection/revision mutation.
- Node transitions add/remove/update VPS projections, user membership/counts and
  advisory affected filters/counts, preserving ordinary user visibility isolation.
- Inject a rebuild failure after some writes and prove rollback of rows, notes,
  projection inserts/deletes, parent revision and update timestamp.
- Concurrent same-revision writes have one winner; rebuild/correction ordering
  cannot restore stale projections; publish racing a guarded draft PUT is refused.
- Draft edits/publication, draft CVE/node membership management and explicit
  announcement mail behavior remain compatible; retracted corrections stay denied.

## KB impact, documentation and client scope

Canonical owner is `vpsfree-kb-contracts`, not the historical
`vpsadmin-kb-captures` spelling in vpsAdmin's localization procedure. At inspected
contract head `ce2c8cd9358c3636e5d39343e595df813a0b197f`, searches of navigation,
managed pages, captures, scenarios and tests find no advisory controls, page
bindings or screenshot concepts. The two advisory PHP files contain no semantic
documentation IDs. The intended visual changes concern administrator forms only;
no shared renderer or member navigation changes are planned.

Package D implements the mandatory final-revision pin and full
`nix develop -c bin/check` workflow in a dedicated contract branch. The existing
`tools/check-contract.rb --vpsadmin-source <exact-checkout>` may additionally
compare base/final source when diagnosing a reported failure, but cannot replace
D. Record exact source revisions and zero advisory bindings. Do not invent
advisory captures or fetch/stage/publish KB content when no page is affected.
If final scope touches a bound shared control, revisit the impact decision and
follow its reported page/capture requirements. No KB production write is authorized.

No generated Go/Rust/TypeScript SDK, Terraform or general CLI change is required:
existing update routes and resource fields remain, with an optional precondition.
The draft-sync companion change is required because it relied on the previous
server state restriction; do not treat that protection as optional documentation.

## Compatibility, deployment and recovery

There are no new persisted formats, schema migrations, seeds, daemon protocols,
Nix module options or vpsAdminOS changes. Old software can read corrected rows and
projections. API and WebUI rollout should complete together before claiming the
UI usable. Old WebUI against the new API can reject timestamp-bearing edits
safely; new guarded UI against old API may reject the unknown precondition.

Updated draft-sync requires the new API capability to apply writes and stops
before any write on older servers. Update every active draft-sync consumer before
resuming it against the upgraded API. A stale client against the new API can
still make an unguarded PUT; the optional parameter cannot enforce client intent
retroactively. Pause sync during API/client rollout and do not use a mixed API
pool as a stable capability guarantee. Read-only client operations remain usable.
Keep publication's unchanged-revision readback/recovery contract.

Software rollback needs no data conversion; already corrected content/projections
remain. Rolling API back restores the old inability to edit published originals;
the updated sync client refuses to apply until the required capability returns.
Restoring incorrect content would be a separately reviewed correction, never a
database reset, republish or automatic reverse update. No production corrections,
credential operations, deployment, default integration or session lifecycle
cleanup are authorized here. Future deployment requires its own approval and
coordination procedure. Session remains open.

No unresolved product/correctness decision blocks A, B or C. D waits for the final
pushed vpsAdmin revision. The lead owns later operational/integration approvals.
