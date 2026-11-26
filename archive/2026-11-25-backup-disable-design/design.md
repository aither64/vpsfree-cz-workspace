# Disable VPS backups: implementation design

D3 supersedes D1/D2's two-call mechanism. The user requires **one ordinary
transaction chain**, rejects a special transfer fallback for missing older
snapshots, and keeps ordinary plan semantics. Lead accepted this correction.
Application implementation remains authorized; integration, package publication
and deployment are separate approvals. Architect0 owns this file and
[plan.md](plan.md); implementers own application changes. Lead owns
[state.md](state.md), package status, coordination, acceptance and final prose.

The user-approved locking simplification below supersedes the broad SQL-lock and
arbitrary enclosing REPEATABLE-READ guarantees in the initial D3 implementation.
It preserves the public contract, durable resource locks and safety checks.

## All-source integration and published SDK adoption

**Sufficient settled brief; latest user approval covers all initiative source
merges and the configuration's `vpsadmin` channel update, with no deployment.**
Do not wait for full CI; relevant specs workflows are the requested CI gate.
Root owns merge/push drivers and final acceptance. Owners prepare source and
evidence in their own worktrees/indexes. Accepted reviews/checks remain reusable
within their proven scope. Current state records the separately user-requested
cluster release as complete: prior live-service/fixture descriptions below are
historical, not authorization to recreate or activate anything.

### Independent I4 published 0.7.0 adoption package

Release this package independently of backend rebase, helper registrations and
configuration preparation. Start from accepted React
`39a1f17ce859600d10276da0fe29bfb1593c8132`, branch `dev/disable-backups`, target
`main`, reconciling fresh upstream under the normal owner workflow. npm 0.7.0 is
already published and verified from merged/tagged TS
`0f1cde21a6e3b64a06389d21a5a5124093520724`; public tarball SHA256
`19fedf46dc72f902fedb055595d1b4de18af58d121bc9dd2ff6bc0234abdafdd` matches its
retained tag receipt. Reuse that release proof, verifying the selected lock and
installed dependency against its exact registry SHA512 identity.

I4 owns `package.json`, npm-generated `package-lock.json`,
`packages/frontend.nix`, removal of the tracked
`packages/development-sdk/vpsadmin-typescript-client-0.6.0.tgz` and
`packages/vpsadmin-typescript-client-development.json`, plus directly affected
`docs/design/{PACKAGING,HAVEAPI_CLIENT}.md` and existing feature work-log text.
Use pinned npm's ordinary exact-version install/lock operation for
`vpsadmin-typescript-client@0.7.0`; preserve unrelated lock records and the
HaveAPI peer. Keep standard `importNpmLock { npmRoot = source; }` and its matching
`npmConfigHook`, removing only the SDK `packageSourceOverrides` entry. No return
to an aggregate frontend hash is necessary. BFF dependency inputs/behavior,
source boundaries, registry guards and UI behavior remain unchanged. Modify
guard tests only if an actual obsolete archive assertion needs updating; do not
invent a new provenance or dependency framework. Preserve the separate session
archive/receipts and retained refs as historical evidence when removing the
development archive from final source.

Prove exact registry/installed 0.7.0 action, declarations and ordinary wire
behavior; run focused policy/type/source/package checks and normal quick checks.
The new dependency inputs require their applicable package-consumption proof;
old local-archive evidence is not proof of registry consumption. Commit the
final dependency change and reconcile the complete branch history so temporary
dependency selection is not left as redundant update commits. Preserve reviewed
old/new ranges and deployed-source equivalence records. Root reuses accepted UI
reviews and requests only affected dependency/build/history review as required;
no repeat browser/OAuth/VM matrix or runtime deployment. This satisfies React's
published-SDK-before-merge rule without a new TS release or backend integration.

### Source order, owners and final proof

| Owner | Source/default target | Remaining dependency |
| --- | --- | --- |
| implementer0 | generic `dev-workspace` 15511ef8 and provider `vpsfree-dev-workspace` 39e7a09e → `master` | Independent; fresh target/rebase equivalence, retained accepted source/package review/checks. No workspace package switch. |
| implementer1 | `vpsadmin` 3a647f64 → `master` | Fresh upstream/rebase and final specs evidence; preserve separate API/PHP/fixtures/Incidents logical changes. |
| implementer2 | Go 70a29eff → `master`; Rust f03bab11 → `main`; TS source successor to 0f1cde21 → `main` | Forward-compatible feature plus minimal final-schema refresh below. No release/version bump. |
| implementer3 | React published-SDK successor → `main` | Independent package above, fresh upstream/PR workflow, final affected review/checks. |
| implementer0 | `vpsfree-cz-configuration` → `master` | Normal recovery/preparation complete; awaits root's actual merged vpsAdmin SHA, then only the requested channel update. |

The addresses above use the retained implementer numbering; existing team package
names I1–I4 remain lead-owned. TS 0.7.0 and workspace instruction changes are
already integrated; verify their remote evidence rather than merge/release again.
The HaveAPI generator checkout has no initiative delta. The exporter checkout is
an acquisition helper, not a second application patch to merge. Root/implementer2 reconcile
those registrations through supported ordinary operations with retained
provenance; never merge obsolete exporter history or relabel its raw acquisition.

No cross-repository atomic update is required. Infra and React preparation can
proceed independently; final backend then corresponding Go/Rust and the service
channel is the straightforward dependency order. Client-first integration also
remains compatible if its input correspondence is already established. Existing
capability gating prevents generated members from claiming server availability.
After any backend rebase, implementer2 binds the new head's complete relevant API/export/
fixture/tooling graph to the retained schema or reports a real changed contract;
do not regenerate unchanged schema or republish TS solely because a commit ID
changed. Conflicting semantic changes return to their owner for focused correction.

### Minimal final-schema synchronization after rebase

Implementer2's bounded comparison found real upstream declarations added to
`SystemConfig`: nullable Custom `choices` and nullable Boolean `value_nullable`.
The retained `cbe3` snapshot is therefore not the complete final rebased schema.
The reviewed backup-disable clients remain forward-compatible, so root may merge
those exact packages independently; that is not completion of current-source
synchronization. `docs/api-schema-export.md` requires the final API snapshot and
affected generated outputs. The smallest sufficient follow-up is source-only:

1. After implementer1 freezes the final clean rebased API, root allocates
   implementer2 one normal export and canonical comparison against retained raw
   `50aa`/`eb8` evidence. Preserve old receipts; capture the actual new source.
   Repeat determinism only when the exporter/fixture/tooling changed or existing
   determinism proof no longer applies. Use the ordinary disposable exporter
   database, not a cluster or live API; no broad acquisition audit.
2. In the existing Go/Rust/TS branches, update saved schema/provenance and their
   bound generator-input digests, then use the already-pinned generators to
   regenerate owned outputs. Keep the existing Go input projection. Expected
   contract delta is only the two additive SystemConfig outputs; inspect the
   complete canonical/output diff and stop for a consequential unexpected delta.
   No handwritten transport, generator, peer dependency or API redesign.
3. Keep TypeScript package version 0.7.0 unchanged in source. Its published tag,
   tarball and registry entry remain immutable; source ahead of that tag is
   unreleased synchronization, not a republished 0.7.0 artifact. React continues
   to consume the actual published 0.7.0, which already includes its required
   cleanup action. **No new TS release or React version churn is required.**
4. Run saved-input/offline regeneration checks, focused new-field typing/wire
   assertions and each changed client's normal compiler/consumer/package tests;
   preserve full generated-file/deletion accounting. Reuse unchanged feature
   semantics and accepted reviews. Mechanical generated metadata can use the
   review exemption, while whole-branch history and any new handwritten behavior
   still receive their applicable assessment. Wait only relevant specs/unit
   workflows, not full backend VM CI. Root integrates final source successors
   with fresh exact remote proof and records completed synchronization separately
   from already-completed npm publication.

This is a sufficient next source package, not dispatch or permission for architect
execution. Root sequences it after the current client-prep milestone; configuration
preparation remains a separate allocation. No stale-schema equality claim or
silent synchronization waiver is part of this route.

Root accepts routine patch-equivalent rebases under current approval. Owners
retain exact old/new base/head ranges, range-diff/input evidence and no-migration
conclusions; accepted final reviews are not restarted for unchanged scope.
Use the review skill's certified-equivalence or narrow-fix rules where applicable;
substantive conflicts/new dependency packaging receive affected review. Merge
claims stay confined to fresh target check, fast-forward merge/push and remote
verification; release before checks or records. Preserve refs and complete final
registration/provenance evidence, including any historical nonancestor sources.

### Configuration update and remaining checks

The actual mapping in configuration `flake.nix` is
`channels.vpsadmin.vpsadmin = "vpsadminServices"`; target is `master`. Once root
verifies the merged vpsAdmin revision on remote master, the separately allocated
owner uses its own configuration worktree and normal
`confctl inputs channel update --commit vpsadmin vpsadmin`. Keep the generated
history/changelog, inspect the exact resulting revision and transitive lock delta,
and preserve unrelated inputs/follows. No staging/production, WebUI or workspace
channel update; no manual lock edits, new host/module change or deploy command.
If upstream moves before resolution, report the extra range instead of silently
accepting unrelated source. Run normal hooks and bounded channel/lock evaluation;
a mechanical pin needs no new standalone content review, but remains in final
history assessment. Root integrates the prepared configuration commit under the
same approval; rollback is a new conventional pin change, never a hidden reset.
Root reports configuration checkout creation stopped in its post-checkout hook
with missing `bundle`; the clean checkout exists but registration may be absent.
Its owner must prepare the declared environment and reconcile the existing
checkout/registration through ordinary commands before a retry. Do not bypass the
hook, recreate over the checkout or edit private registration state. This does
not block independent React or other source packages.

Still required: applicable final specs workflows, quick checks for actual changed
inputs, affected SDK/package-consumption proof, final freshness/history and review
evidence. Existing API 53+3/node46, PHP actual-client 12/143, React defaults and
infra package results remain valid only for their proven inputs. I1 reports no
unresolved failed correctness assertion. Original full storage/PHP VM suites and
external KB capture certification remain **unrun/uncertified limits**, not source
merge gates under the latest user direction; do not launch them or recreate the
released cluster. Do not wait for the broad integration CI workflow or infer its
success. User CI-wait limits do not turn a failed required spec into a pass.
No production/development activation, lifecycle cleanup or further registry
publication follows these merges automatically.

## TypeScript client 0.7.0 release brief

**Sufficient release-preparation brief; user authorized merging and publishing
the TypeScript client only.** I3/implementer2 owns source/version preparation,
checks, provenance and review fixes after lead capacity/release. Root owns the
actual merge, tag/publication drivers and acceptance. API, PHP, React and other
client integration/deployment are not included. Keep current services/data and
the immutable local SDK archive `671b54f5…` unchanged until a separately prepared
consumer update.

There is no repository AGENTS.md; authoritative instructions are its README,
`docs/{development,releasing}.md`, `.github/workflows/release.yml` and
`tools/release.mjs`, under workspace Git/review rules. Configured remote default
is `origin/main`, also required by release preflight. The documented default is
the next minor: **0.7.0**, tag **v0.7.0**. The public registry check on 2026-11-26
found latest 0.6.0, versions through 0.6.0 and no 0.7.0; local tags agree. Registry
0.6.0 has integrity `sha512-bokNqgJIg7+tFkMBafXyWly9I4MtMK3o3HY9RWVbXMMvttuUUoL35U0Me2xdFAp5R9Mnmy9YZz/b80g+zvFwjw==`,
different from our development archive. Never republish that version or relabel
the retained archive. Root rechecks version/tag availability before release.

Source boundary: start from retained clean TS `6d4941bbf617a0d1e1c131a2bf14ca6476389809`,
reconcile with fresh remote main, update `package.json` and both root version
records in `package-lock.json`, then update its exact tooling digest in
`tools/generator.json`. Update the README installation version and narrowly
affected release/development explanation. Preserve dependency graph, peer
`haveapi-client` 0.32.0, generator and generated contract; no new generator,
workflow, acquisition or SDK runtime design. Full branch/history review must
include the already-generated feature commits and the final release adjustment.

Provenance remains an honest acquisition: API 7.0/protocol 2.0, all six plugins,
`vpsadmin-full-fixture`, raw API source `50aa37aede8926965598f4f8fb0782dce377afb6`,
schema SHA256 `cbe3a7ca90d7f1c94e2b769058b1c32a570e36fd92f55cf48a4302d4e50dc05d`.
I3's retained fresh-export/equivalence records establish the same schema through
the later API correction. I3 carries forward exact-current API input equivalence
and identifies any real intervening contract change; do not rewrite the raw
receipt to pretend acquisition from a newer commit or rerun unchanged exports
merely for a version bump. HaveAPI generator
`1ef9b204ba45bb261d3334be5c555cc1856b713b` is publicly retrievable (checked); the
release workflow can obtain it without another HaveAPI publication.

The added `dataset.disable_backups` is an optional generated call with the two
existing booleans, empty declared action output and ordinary action-state metadata.
Publishing the client before API/PHP/React integration is permitted: importing
it performs no mutation and does not deploy/enable that server action. Consumers
must retain authenticated capability checks until compatible API support exists.
React's eventual merge requires the published SDK dependency, but this release
does not itself replace its local archive/importer or activate new UI packages.

Acceptance/order: I3 uses the pinned Nix environment for offline regeneration
`--check`, build, strict source/consumer type checks, client/release tests and
archive consumer checks. Update lock digest before regeneration verification;
generated outputs must remain explained and complete. Commit all release changes,
pass quick checks, complete final independent review/history assessment and
branch build-only CI before root's ordinary fast-forward merge/push to `main`.
No migrations are introduced. The existing tag workflow then builds **once**,
validates and retains a tarball plus SHA256/SHA512 receipt, and publishes that
exact artifact from the protected `release` job using npm OIDC. Before tagging,
I3/root verify existing non-secret setup: `NPM_RELEASE_ENABLED=true`, release
environment protection/tag rules and trusted publisher for organization
`vpsfreecz`, repository `vpsadmin-typescript-client`, `release.yml`, environment
`release`, direct publish. Existing configuration is not assumed from npm login;
missing setup is a concrete release blocker, not grounds for a token fallback.

Root records exact merged/tagged head, workflow/artifact ID, tarball/receipt and
registry integrity/provenance equality. A branch/manual workflow run cannot
publish. On failed or uncertain publication, inspect the original run and exact
registry version first; retry only the failed publish job with the original
artifact. Never rerun the tag build, repack an approved archive, move the tag or
replace/unpublish a released version. Consumers may remain pinned to their
previous artifact; a released defect needs a new reviewed version. No current
runtime or fixture action is part of release preparation.

## Conventional PHP post-submit presentation

**Sufficient settled I2 correction, based on its completed read-only diagnosis.**
This is independent of the defaults correction below.
The user rejects the custom receipt-only screen: heading/empty body, separate
Transaction log block and an unknown warning despite a normal successful sidebar
transaction. Reuse existing PHP dataset action dispatch, standard perex messages
and ordinary redirect/render so useful dataset/page content remains available.
An accepted chain uses the normal in-progress presentation and existing transaction
sidebar; do not add a parallel task/progress/log page or require custom polling
to make the normal accepted response usable. Established action failures use the
ordinary error presentation.

I2 established the false-unknown path: HaveAPI 0.32.2's undeclared output inherits
`output {}` with object layout; the real PHP client returns `ResourceInstance`,
which has `getApiResponse()`, not `getMeta()`. The cleanup helper calls `getMeta()`
on that accepted result, throws through resource method lookup and catches it as
unknown **before polling**. The regression's synthetic action declaration used
hash layout and hid the defect. This is not evidence of an incorrect Poll body.
No output/schema change or custom metadata adapter is required.

Use the existing scheduled-action pattern from
`webui/pages/page_backup.php` (snapshot creation/restoration) and
`webui/pages/page_dataset.php` (expansion): one ordinary API call, then
`notify_user` with lead-approved scheduled/in-progress text and `redirect` to
the sanitized local return or dataset editor. `webui/lib/functions.lib.php`
already carries the notification to normal perex rendering on the next request.
Remove the cleanup-specific result-state/poll helper, log link and blank receipt
branch. Do not claim completion merely because the ordinary call returned.
For `ActionFailed`, reuse ordinary `perex_format_errors` and normal editor/backup
content. Other transport/response exceptions remain on the existing ordinary
exception path: no scheduled/success notification, automatic replay or success
redirect that disguises them. Do not introduce another persistent uncertainty
record or custom task UI to implement that boundary.

Keep the single ordinary mutation, role/capability checks, confirmation, consumed
single-use CSRF, actual receipt handling and no automatic replay after a lost or
ambiguous submission outcome. Preserve genuine unknown-outcome handling within
the ordinary page/message flow, without new warnings or receipt machinery.
Distinguish accepted-with-receipt from failure to obtain a receipt; do not label
accepted work unknown merely because optional status interpretation failed.
Use normal success/pending/error conventions rather than inventing a second
status vocabulary. The user's submitted operation and resulting data are current
state: no automatic resubmit, reset, repair or fixture reconstruction.

I2 owns `webui/forms/dataset.forms.php`, the narrowly necessary dataset action
dispatch/render integration, `webui/tests/Regression/DatasetDisableBackupsTest.php`
and affected locale/docs/assertions; shared helpers and unrelated actions remain
unchanged. Fix the test action to actual object layout and exercise the real
client result plus ordinary redirect/notification using the existing subprocess
redirect-stub pattern. Prove one mutation/no poll, scheduled perex rather than
completion/false-unknown, normal `ActionFailed`, transport exceptions without
success or replay, and consumed CSRF/default/explicit-POST invariants.

Focused offline route tests can certify post-submit behavior. After quick checks
and affected review, served-file binding plus GET markup prove deployment and
form defaults only; they do not prove a real mutation response. Any real action
proof needs a separately authorized disposable scoped fixture or existing isolated
VM scenario, never replay of the user's dataset1 request. Preserve the user's
current data; no new live request, reset or fixture repair is authorized here.

## Unified cleanup defaults correction

**Sufficient independent brief; latest user instruction supersedes every earlier
URL/shortcut precheck in this design and plan.** Every fresh cleanup form and
dataset/context reset starts `recursive=false`, `backup_first=true`, Confirm
unchecked. A page filter or query parameter never opts into recursive cleanup.
Local checkbox choices remain editable and independent; existing confirmation
invalidation, one-call, CSRF, task and uncertainty safeguards remain unchanged.

- **React / I4:** `src/pages/app/datasets/DatasetBackupCleanup.tsx` and its
  `.test.tsx`, with affected REQ-048/workflow/work-log statements. At inspected
  `1d895a5746561d15413f42afd83678b898de3b45`, `recursiveHint` from search initializes
  state and its context-mismatch fallback; the VPS root link supplies
  `plans?recursive=true`. Change initial and context-reset values to false/true/
  unchecked, including backup-first when the existing context boundary changes.
  The URL may remain an existing context-invalidation signal, never a checkbox
  value. Preserve page links/search/filter behavior; no route changes are needed.
  Explicit local recursion still submits true after fresh confirmation and does
  not write the URL. This package is independent of PHP receipt diagnosis.
- **PHP / I2:** `webui/forms/dataset.forms.php` and
  `webui/tests/Regression/DatasetDisableBackupsTest.php`, plus any affected usage
  statement. The inline caller already passes false; `dataset_disable_backups_page`
  still initializes from GET `recursive=1`, so PHP also needs a source correction.
  Initialize fresh GET scope false on all entry paths. Keep validated explicit
  POST checkbox values authoritative, including a deliberate true selection or
  presentation of that submitted choice; do not force false in the request helper.
  Existing URL-helper signatures need no redesign merely to ignore the old hint.

Minimal checks: omitted/false/true URL hints all render false/true/unchecked;
dataset/existing-context changes reset all defaults and invalidate confirmation;
explicit local recursion and preservation opt-out still reach the request;
PHP POST wins over conflicting GET and CSRF/duplicate/unknown safeguards remain.
Replace old precheck expectations rather than weakening independent-choice tests.
Owners retain focused quick checks, commits and affected review. React deployed
proof requires matching new immutable outputs and authorized refresh; PHP uses
existing live-file binding. Read-only browser proof checks defaults on direct
and VPS-link entry paths; no cleanup submission, fixture reset or data repair.
Retain prior package/source recovery evidence; no runtime action is authorized
by this design, and a reverted source may restore the old precheck behavior.

## Controlled UI refresh and peer package-switch admission

**Sufficient ordering clarification only; no stop or activation now.** The
lead reports that our intentional BFF/edge SSH processes `3807148`/`3816587`
hold shared `transition.lock` ownership for their registered lifetime, while
an original waiting workspace package switch needs exclusive ownership.
Provide the gap through an ordinary prepared app restart or UI refresh; do not
add a lock-release helper, lifecycle action or live-attach mechanism.

The prerequisite is a command-ready safe ownership transition with reviewed,
verified matching frontend/BFF outputs and prepared fresh-attempt restart/recovery
inputs. New UI source is not required: the current verified immutable pair from
`ff2cf8ae4b44781f90941611294a94fd6953763a` may be restarted unchanged if that
preparation is ready first. Use the final inline pair from reviewed `1d895` if its
build and required output proof are available and bound at the prep boundary;
otherwise do not delay the safe same-version gap for unrelated application work.
No unprepared outage, blind replay or restart over an unknown old process is
permitted. I1 owns the root-directed runtime preparation under lead sequencing
with its prevention package; this amendment assigns no second execution package.
I4 retains final application outputs/proof; root owns the actual restart/refresh
and communication with the peer lead.

At the separately authorized refresh, use normal registered component termination
for only the existing edge and BFF r2 owners (edge first avoids forwarding into a
stopped BFF). Existing registrations are edge
`c346723f-3467-4ed3-910c-24033cd45bd9` and BFF r2
`fe58b25f-b98f-4f9a-b491-c211fc513c7e`; bind execution to their actual recorded
identities, not PIDs alone. The existing owner contract propagates termination
through SSH/PTY to its exact remote unit. Preserve all receipts and reconcile
the matching InvocationID, terminal unit/MainPID0 and empty/gone owned cgroup
using the existing component inspection path. A local registration exit, 15-second
grace expiry, lost SSH link or freed lock does not prove remote termination.
UNKNOWN blocks replacement and requires exact-owner reconciliation; no broad kill,
guest stop, main-service stop or retrying a second instance.

After old long-lived readers exit, hold replacement BFF/edge launches. Notify the
peer lead of the gap and await the **original** switch's terminal outcome; do not
submit another switch or assume waiting writers have priority. A normal short
remote reconciliation command might run before the writer acquires its lock or
wait until afterward. Both remote-exit proof and the peer outcome must be known
before replacement; their exact completion order is not a safety requirement.
Avoid repeated new readers while the peer is waiting. If ordinary commands refuse
or outcomes remain unknown, retain the gap and report the concrete obstruction;
do not bypass generation/transition guards or manually release lock descriptors.

Root then verifies the actual selected package/generation from the peer's outcome
and fresh supported identity reads, rather than assuming the target was selected. On a
known failed/compensated switch, root decides continuation against the proven
current generation; on uncertainty, no replacement starts. Rebind the ordinary
commands to that generation and complete normal selected-pair/ownership/port
admission before registering the matching BFF and then edge. Verify TLS, actual
build metadata and nondestructive UI behavior through the existing refresh
contract. No guaranteed switch timing or uninterrupted React availability is
claimed during this controlled gap; PHP and cluster guests are not stopped.

Preserve every guest, VPS1/plan/source and backup snapshots, private OAuth/TLS
credentials, signing secret, BFF StateDirectory/session store, app roots and
recovery evidence. No credential reprovisioning, fixture mutation, cluster reset,
layout change or cleanup is needed. The retained
[runtime runbook](i1-react-runtime-prep/runbook.md#ownership-and-uncertainty)
defines exact-owner termination; its historical preparation status is superseded
by accepted runtime receipts in [state.md](state.md) and [I1 evidence](i1-evidence.md).

## Inline cleanup form and concise copy correction

**Sufficient settled UI brief; supersedes conflicting copy/layout requirements
below.** The user explicitly removes the extra warning/help prose and requests
the real React form inline like PHP. I2 owns PHP and I4 owns React independently;
lead supplies final English/Czech copy, releases packages and owns deployment.
Keep the separate Incidents/menu commit `cc922af3` outside this change. I1's
infrastructure prevention package is independent. No backend, SDK/dependency,
global CSS, generic dialog, fixture or runtime work belongs to these UI packages.

Use this exact single English paragraph in each cleanup form:

> This removes the selected datasets from all backup plans and deletes their local snapshots. Backups are preserved. Re-enabling backups will require a full transfer.

The confirmation checkbox label is exactly **Confirm** in English, required and
unchecked initially. Use lead's corresponding exact Czech copy. Remove the
dataset identity sentence, separate primary/manual/backup-retention paragraph,
long backup-first/no-new-snapshot/opt-out explanations and recursive help.
Do not move removed text into tooltips, alerts or checkbox descriptions. The
existing plan-removal explanation in Backup plans is a separate feature and
remains. Keep the cleanup title, independent recursive and backup-first controls
and existing submit label. Recursive defaults false; the existing explicit
recursive shortcut may precheck it. Backup-first defaults true. Confirmation
never changes either option and remains required even with backup-first enabled.

- **PHP / I2:** existing cleanup renderer in `webui/forms/dataset.forms.php`,
  its dataset-page integration, existing English/Czech catalogs and focused
  form tests/docs only. Keep the actual form immediately below Backup plans,
  including an empty plan list. Use existing standard form helpers and valid
  two-column rows/full-width paragraph placement; eliminate explanatory striped
  rows and the malformed lone left cell. One paragraph in the existing helper's
  `colspan=2` row, followed by ordinary two-cell control rows, satisfies this;
  moving it outside the table is not required. Remove the static descendant-name
  preview and its presentation-only `dataset_disable_backups_scope` enumeration/
  read if now unused; retain server dataset/recursive scope validation. Do not
  relocate a hidden preview. No global styling fix. Preserve the
  dataset-bound single-use CSRF token, independent POST booleans, server-side
  required-confirmation validation, admin/capability gating and receipt flow.
  Keep regression coverage in `webui/tests/Regression/DatasetDisableBackupsTest.php`;
  no menu changes or unrelated index content enter this correction.
- **React / I4:** `src/pages/app/datasets/DatasetBackupCleanup.tsx`, its placement
  in `DatasetPlansPage.tsx`, focused component/page tests, current locale keys and
  affected requirement/workflow/work-log docs. At inspected `ff2cf8ae`, cleanup
  uses `ConfirmDialog`, an opener and URL-derived recursion; remove only this
  cleanup opener/dialog. Render the actual form immediately after the assigned
  plan list or empty state. Keep other assignment/removal dialogs unchanged.
  Add a local recursive checkbox initialized from `recursive=true` in the URL
  (otherwise false); editing it changes only this request, not page filters or
  navigation. Preserve this shortcut when dataset/URL scope changes and reset
  acknowledgement for dataset or recursive-scope changes. Keep backup-first
  independent and default true. Reset acknowledgement after accepted submission;
  removing the dialog must not leave consent reusable for another scope/action.
  Retain the internal task object label even though its extra UI sentence
  disappears. Use ordinary existing Card/form/Button/Checkbox components.

Both packages retain pending/double-submit guards, button plus handler/POST
confirmation enforcement, current preflight, local locks, one mutation, task
receipt tracking and unknown-outcome reconciliation. The React error/uncertainty
panels remain available inline; do not hide them by removing the dialog or treat
an accepted request as completed cleanup. Browser exit does not cancel the chain.
No success, retry or reconciliation behavior changes are requested.

Acceptance: focused tests cover initial defaults, independent option values,
required unchecked Confirm, recursive shortcut and scope reset, no submission
without confirmation, pending duplicate prevention, admin/member/capability and
empty-plan rendering, and existing receipt/unknown results. Update obsolete
dialog assertions to the inline form rather than deleting behavior assertions.
PHP rendered markup must use valid complete rows and the text must span/alignment
match the existing form. Show English/Czech desktop and narrow captures after
quick checks; verify placement, exact short copy and absence of opener/pop-up and
removed help. Browser fixtures may test submission; live review is read-only and
must never submit cleanup or alter VPS1/plan/snapshots. Commit each disjoint
package, preserve the separate menu history, and independently review before
long build/deployment checks. Existing PHP live-file binding and React matching
package activation contracts remain; no activation is performed by this brief.

## Future-session React preparation and SSH prevention brief

**Sufficient settled brief for I1; lead owns dispatch and acceptance.** Keep the
accepted React runtime, all five guests and VPS1/plan/three source snapshots/one
backup unchanged. This package does not switch the selected workspace package.

The custom launcher was avoidable for a fresh cluster. We selected
`newWebui.enable=false` to start PHP before preparing the local SDK. Later React
enablement adds a credential virtiofs share, which ordinary update and retained
start reject as a layout change. Preserving the populated cluster led to the
separate registered BFF/edge. Future sessions should prepare the matching
frontend/BFF and SDK dependency first, retain `newWebui.enable=true` with distinct
`domains.newadmin`, then use ordinary
`vpsadmin-devcluster start <slug> --topology dual --network bridge`. The provider
supplies the credential share, OAuth client, packaged services and TLS route.
The workspace default already enables React; no default flip is needed. The local
SDK route below passed actual Nix consumption without registry publication.

The malformed `LoadCredential` belonged to our session's `remote-owner.sh`: one
property combined three paths, producing one malformed D-Bus entry and failure
before Node ran. `remote-owner-r2.sh` uses a separate property per credential and
passed. Existing module/provider credential lists are correct; no reusable
credential bug is established. Data fixtures did not cause either failure. The
client store's read-only mount also was not a fixture defect: socket activation
proved the daemon store writable, and mounted NAR import/rooting passed. Retain
[I1 evidence](i1-evidence.md); no new guest probes or fixture changes are needed.

The reusable defect is public SSH stdin loss. Generic `dispatch_cluster` sends
`ssh` through `system_env!`, whose `Open3.capture3` call supplies no input and
closes child stdin. The inner provider executes ordinary SSH. This caused tar
staging to fail before credentials or OAuth creation. Route **only `ssh`** through
existing `system_env_interactive!` inside the current generation guard. Preserve
provider/environment selection, lock lifetime, nonzero failure handling,
`capture-lease` streaming and non-SSH behavior. Inherited stdio supports pipes and
terminals without a new I/O abstraction.

I1's complete source/test/doc boundary, after lead allocation:

- **Preparation docs:** `vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`,
  existing initial-start/optional-React sections. Explain the sequence above,
  actual SDK action readiness, matching source/build prerequisites and retained
  share restriction. Link existing React `docs/design/PACKAGING.md` for local
  archive/`importNpmLock` details. Distinguish build readiness from activation;
  use generic host placeholders. No provider code, defaults or new preflight mode.
- **SSH fix:** `dev-workspace/libexec/workspace-host`, only dispatch helper
  selection; regressions in `test/workspace_host/commands_and_locks_test.rb`
  using existing fake-provider facilities. Clarify the inherited-stdio contract
  beside existing SSH documentation if needed. No generic launcher, fixture
  enrollment, live-layout migration or promotion of our session wrapper.
- **Ownership/dependencies:** use separate same-session infrastructure worktrees
  and indexes; never the vpsAdmin index owned by I2 for its PHP menu work. I1
  selects and records current repository bases. No API, React, SDK or live-cluster
  dependency blocks this package. Architect changes only design/plan; lead owns
  release, status, review and any later package activation.
- **Acceptance/checks:** real dispatch tests prove binary input/EOF reaches the
  fake provider, stdout/stderr stream separately, terminal stdio is inherited,
  nonzero remains failure, and the generation lock survives until child exit
  then releases. Preserve capture-lease/non-SSH coverage. Run focused Ruby and
  repository syntax/style/docs/organization-source checks. Commit and independently
  review exact source/docs before required longer package checks; generic
  `checks.x86_64-linux.package` is distinct from its default build. Apply normal
  watcher policy; no new cluster boot or current runtime deployment is included.

Compatibility/recovery: no state schema, provider protocol, credentials or
cluster descriptor changes. Old wrappers retain EOF behavior; existing mounted
file/argv workarounds remain valid. Rolling the package back restores the old
limitation without data conversion. Existing React-disabled clusters retain
their layout restriction. Do not migrate or stop current custom services.

Exact observed source identities (not guessed Git bases): generic installed
`/nix/store/gdjizaalss4banjmls2l3ah7ljdb3m3q-dev-workspace-0.2.0`, source
`/nix/store/5pnplssw3qqbjj0yii5dj27d9wzmx5vr-source`; `libexec/workspace-host`
SHA256 `0b06ee6bfd528328a8b918b34367c11c992a4b57aa0a77b930306a4b2a0db582`.
Provider installed
`/nix/store/bh1y6k99pc8d0prqcn44dylhd402ysks-vpsfree-dev-workspace-tools-0.1.0`,
source `/nix/store/nma0v0499qdyn4f2wwwdbzf5i49nhlip-source`;
`dev-clusters/vpsadmin/nix/test.nix` SHA256
`35a352280247396c2224f6fc55120f8023980dc95be8f984875140267d91550a`.
Workspace lock revisions/local bare HEADs are not asserted to equal those bytes.

## React development deployment with an unpublished SDK

**Completed and accepted:** final React source
`ff2cf8ae4b44781f90941611294a94fd6953763a`, tree
`2c1c9ff8928011b29d23ab96ab22ea2a14edfead`; matching packages, daemon import/roots
and real admin/member OAuth/UI proof passed. [state.md](state.md) and
[I1 evidence](i1-evidence.md) own current receipts. The following preserves the
packaging/runtime design, not outstanding activation work.

The user requests real React UI review against this development cluster without
publishing the TypeScript SDK. Repository instructions explicitly allow local
dependencies during development; the published-SDK prerequisite still applies
before production/default-branch integration. This adds no registry release,
SDK regeneration, production merge or changes to the backup API. PHP review and
the existing VPS/plan/snapshot fixture remain independent and intact.

The user's confirmation requirement also applies to React. I4 adds a
feature-local required acknowledgement, unchecked each time the dialog opens,
with submit gating and reset through the existing dialog flow. Use lead-approved
exact English/Czech wording covering all attached plans, local-snapshot removal
and that re-enabling backups will require a full transfer. Keep backup-first
checked by default. No generic dialog redesign, backend or dependency change.
Focused source/test/documentation checks, commit and independent review precede
the final matching frontend/BFF builds. The earlier `18597` package proof remains
valid for its own source; it is not the final checkbox-complete deployment.

### Sufficient local SDK packaging brief

I4 owns the exclusive React source/index/commit window from
`c723f2fab261153eddf7bee0cc967e5392836efe`. Use the existing immutable archive
`work/2026-11-25-backup-disable-design/i3-ts-candidate-final-50aa37ae/vpsadmin-typescript-client-0.6.0.tgz`,
SHA-256 `671b54f52da297cd465c1b7516841a859c84099ab30d776e5086802559d19a10`,
integrity `sha512-pX/rP/o+7idHacYBFZcbRkhwonUNDi9kzVBtgClhBTrb6R1xim4/z1uk9dxN2Gm3RyjoXK14BXKPlYog584UnA==`.
I3/I4 evidence binds it to SDK `6d4941bbf617a0d1e1c131a2bf14ca6476389809` and
API export `50aa37aede8926965598f4f8fb0782dce377afb6`. Its local version is 0.6.0;
it is not the registry 0.6.0 archive. Preserve those distinct identities. The
generated action has only recursive/backup_first and the ordinary task receipt.

Copy the unchanged archive as a regular, retained source file under
`packages/development-sdk/`. Do not reference an external symlink, absolute
workspace pathname, mutable node_modules or registry artifact with the same
version. With pinned npm, select that relative archive using the ordinary
`npm install --package-lock-only --ignore-scripts --save-exact ./packages/development-sdk/vpsadmin-typescript-client-0.6.0.tgz`
workflow. Commit the resulting development-only `file:` manifest/lock selection,
archive and standard dependency-import configuration as one coherent input set.
Inspect unrelated dependency records for churn; retain the exact HaveAPI peer,
XMLHttpRequest graph, BFF manifest/lock/hash and all non-SDK inputs. Never hand-edit
integrity or claim the previous registry hash describes this archive.

Bounded files: `package.json`, `package-lock.json`,
`packages/development-sdk/vpsadmin-typescript-client-0.6.0.tgz`,
`packages/frontend.nix`, the existing SDK provenance record, relevant packaging/
client-contract documentation and the existing work log. No adapter/generated
client/BFF runtime changes are required. `nix/source.nix` retains regular archive
files; `scripts/check-package-source.mjs` rejects symlinks/private/generated
directories and verifies the HaveAPI registry selection, not an SDK-registry-only
policy. Keep those guards; no checker bypass. Matching frontend and BFF derive
from the same final React source/provenance, even though the BFF npm graph stays
unchanged. Restore the matching published dependency/build-input set before eventual merge;
this development input does not silently satisfy the release prerequisite.

I4 validates archive identity, npm-generated lock/integrity and installed SDK
method/types, then runs the relevant existing typecheck/action tests and source/
documentation checks under pinned Node. A Vite build alone does not prove the
new method exists. The first prefetch attempt failed in 4.7 seconds because the
selected `prefetch-npm-deps` rejects this `file:` archive URL (`invalid format`);
no aggregate hash or successful Nix consumption was established. Do not retry
that unsupported route. Use the documented standard alternative below. Actual
buildNpmPackage consumption of the local archive is an explicit acceptance
check, not an already-observed result. After intended commits, quick
checks and independent review, build frontend/BFF and their declared provenance,
source-contents and package-contents checks. Record exact source/lock/archive/
derivation/output identities; no registry publication. This sufficient package
can proceed independently of the activation constraint below.

**Settled dependency-import correction.** In the selected nixpkgs source
`/nix/store/pgy8nq09hh4mdgr30ir9v0lcjpz34vxb-source`, the JavaScript guide
(180–219) documents `importNpmLock` with its own `npmConfigHook` as a supported
buildNpmPackage alternative using each lock integrity instead of an aggregate
`npmDepsHash`. `pkgs/build-support/node/import-npm-lock/default.nix` exposes
`packageSourceOverrides` for an exact dependency and retains its integrity when
rewriting resolved paths; HTTP modules use fetchurl with their declared integrity.
`pkgs/build-support/node/build-npm-package/default.nix` accepts both overrides.
Replace only the frontend's fixed-cache selection with:

```nix
npmDeps = pkgs.importNpmLock {
  npmRoot = source;
  packageSourceOverrides."node_modules/vpsadmin-typescript-client" =
    source + "/packages/development-sdk/vpsadmin-typescript-client-0.6.0.tgz";
};
npmConfigHook = pkgs.importNpmLock.npmConfigHook;
```

Remove the frontend `npmDepsHash` for this importer; keep the BFF hash unchanged.
The explicit SDK source override is necessary: the importer's generic local
resolver does not strip `file:` before appending to npmRoot. This public override
uses the included regular archive, its committed source identity and retained
npm lock integrity. The standard importer derives store-resolved package/lock
files for installation; the original npm-generated lock and prePatch source
check remain intact. Verify the complete graph and SDK bytes after installation.
No custom cache, lock stripping, integrity weakening, helper patch or checker
bypass. Evaluation and quick source checks precede review; full build/provenance
proof remains required before claiming this candidate usable.

### Existing provider activation constraint

The current applied services descriptor exports only `vpsadmin` and `vpsadminos`.
Installed fjr83 `nix/test.nix:1025–1029` adds a `webuiCredentials` virtiofs share
when `newWebui.enable` becomes true, and its credential unit reads that mount.
`lib/maintenance.rb:479–490,885–907` rejects changed shares on ordinary update.
`bin/devcluster:1137–1163` and `maintenance.rb:560–568` apply the same layout check
before retained start; stopping/restarting does not select a changed descriptor.
`restart <slug> services <service>` only restarts a systemd service. Maintenance
copy also requires identical mounts (`maintenance.rb:443–460`). Thus neither
ordinary services update nor whole-cluster stop/start provides a supported
preserving transition from this React-disabled layout. Do not run speculative
enable/update, reset, recreate or edit applied-state records. A built candidate
does not establish activation. Lead owns the separate concrete activation
decision; no provider feature or credential transport change is released here.

### Selected runtime route

Lead accepts a separate session-registered HTTPS development edge serving the
built frontend and its matching BFF. Keep `newWebui.enable=false` and the existing
provider/guest layout. Provider `nix/test.nix:997–1001,1629–1639` also gates the
newadmin TLS vhost on that flag; its usual `127.0.0.1:18082` upstream is not an
available ingress while disabled. No provider accommodation or Vite/HMR stack
is needed for the selected route. I1's bounded facts are accepted and lead selects
`https://newadmin.aitherdev.int.vpsfree.cz:8443`, with the independent edge on the
existing services VM at `172.16.106.53:8443` and BFF at `127.0.0.1:3001` on that
same VM. Both ports were unoccupied; admission rechecks them before activation.
DNS already resolves the hostname to that VM. Guest firewall currently drops
8443: the endpoint is not yet reachable. Lead explicitly releases a narrow,
owned TCP/8443 guest ingress allowance as part of development activation. Keep
the main HTTPS/PHP listener and all other rules unchanged; identify the new rule
exactly so uncertain effects and any later authorized removal are reconcilable.

The existing public certificate is
`.dev-clusters/vpsadmin/certs/default/vpsadmin-cert.crt`, with SAN for this hostname
and SHA-256 fingerprint
`A1:40:3A:EF:C4:D4:EA:37:EB:DD:08:B1:31:35:2B:EB:D3:7F:BC:A6:A0:0A:7E:4F:FF:B4:20:15:EC:36:33:C7`.
The public CA is the adjacent `vpsadmin-ca.crt`, fingerprint
`1C:60:3B:7C:2C:95:48:ED:32:DC:3B:49:33:5A:AF:89:C9:54:F0:7D:EE:04:77:07:03:1B:C6:7C:AD:FB:57:14`.
I1 observed validity through 2036-09-27. Use its matching TLS key only through
private runtime provisioning; no new CA, trust bypass or key in source/logs.

Use existing `dev-session service run` registration for each new owned runtime
process under the installed temporary-service workflow. I1 prepares the small
foreground SSH supervision wrapper and exact commands; root launches them.
Registering a one-shot SSH launch is insufficient. Each local registration must
remain attached to its exact owned remote edge/BFF process or transient unit;
bind the session/component identity, propagate termination through the ordinary
SSH/supervisor path and reconcile remote exit. A broken connection or uncertain
stop is not proof the remote process stopped. Preserve the remote identity for
inspection; never use broad process matching or stop a guest/main service.
Any later stop remains separately authorized; no timed or end-of-turn cleanup.
This is narrow command adaptation, not a new service-management framework.
Serve the immutable
frontend output; forward `/oauth`, `/oauth/*`, `/config.json`, `/config.js` and
`/session.json` to one private loopback BFF from the same built source. Reuse the
documented single-edge forwarding policy, exact host/proto/client-IP handling,
and no credential/query logging on OAuth endpoints. Other SPA/API calls use the
real cluster API directly. No synthetic transport, fallback runtime mode or
custom proxy framework.

Production-mode BFF settings bind the chosen HTTPS `PUBLIC_ORIGIN` to exactly
`https://newadmin.aitherdev.int.vpsfree.cz:8443/oauth/callback`, real API
`https://api.aitherdev.int.vpsfree.cz` version 7.0, and auth endpoints
`https://auth.aitherdev.int.vpsfree.cz/_auth/oauth2/authorize`,
`/_auth/oauth2/token`, `/_auth/oauth2/revoke` and `/oauth2/password-reset` on that
same auth origin,
`X-HaveAPI-OAuth2-Token`, `_meta`, scope `all`, type `web_server`, and the public
cluster CA for Node trust. Provision one normal separate nondefault OAuth client
through the existing API. I1's verified TLS preflight for this origin already
allows direct token-header API requests (origin `*`, credentials false); no CORS
policy change is needed. This does not replace real OAuth/runtime proof. Keep
client ID/secret and stable signing secret in private regular runtime
files; retain a private writable session directory owned by this one BFF.
No secret enters source, Nix store, command arguments, public config or records.

Lead owns OAuth/credential/firewall/activation drivers after exact input review.
I1 owns operational command/wrapper/edge preparation and effect evidence; I4
supplies final reviewed/built frontend+BFF paths and application/runtime proof.
Use the existing guest nginx binary
`/nix/store/v5yfyvpd7z7lbzh86bpbh5cjp10qad4m-nginx-1.30.7/bin/nginx` with a separate
owned prefix, PID/log paths and configuration, `-g 'daemon off;'`; validate that
configuration before launch. Do not reload or replace the main nginx instance.
Acceptance requires matching frontend/BFF build metadata, actual installed local
SDK action, healthy runtime/config/session endpoints, real admin OAuth, visible
VPS1/dataset1/plan/three source snapshots, default-on preservation/confirmation UI,
and member gating. Observe without submitting cleanup or plan removal; confirm
the retained backup and all five guests remain intact. Preserve registered runtime
and credentials/session state for human review. Failed/unknown activation retains
evidence for diagnosis, with no cluster reset or speculative retries. Exact
final package paths, private runtime inputs and occupied-port rechecks are
execution prerequisites; source/package success alone is not deployed proof.

### App closure import into the running guest

I1 found earlier app outputs absent from the guest and the client's `/nix/store`
mount read-only. This does not establish daemon-store write incapacity. Its one
bounded follow-up found `/nix/var/nix/daemon-socket/socket` present and
`nix-daemon.socket` active, with service inactive pending normal socket activation.
Root then authorized one ordinary `NIX_REMOTE=daemon nix-store --query --hash`
against the known current system. I1 reports exit 0, normal activation to daemon
MainPID37075, and `/proc/37075/mountinfo` showing the daemon's `/nix/store` ext4
mount `rw,relatime` with super-options `rw`. This establishes the actual daemon
route and writable mount; it does not claim an import succeeded. No explicit
service start, import/build, remount or configuration change was performed.
The installed Nix
store manual defines `daemon` as that socket and `NIX_REMOTE=daemon` as delegation
of store operations. The standard `nix-store --export/--import` manual preserves
store objects and references; export requires explicitly enumerating the complete
closure, and import rejects missing referenced paths.

Use this conventional route, prepared by I1 and executed by root only after the
final checkbox-complete matching outputs are reviewed/built:

1. Root the final public frontend and BFF outputs on the host. Enumerate their
   complete closure with `nix-store --query --requisites`, then export that set
   with `nix-store --export` into one secret-free payload under an existing
   Git-ignored, untracked backend-worktree staging directory. I1 verifies its
   identity and guest `/mnt/vpsadmin/...` mapping, complete path inventory, size
   and digest. No credentials or session state enter this payload or source.
2. Public provider SSH passes a shell command in argv. In the guest, check the
   mounted payload digest and run
   `NIX_REMOTE=daemon nix-store --import < /mnt/vpsadmin/<owned-payload>`.
   Redirection occurs inside the guest: the workspace wrapper's closed caller
   stdin is irrelevant. Normal socket activation is part of this root-owned
   import. Retain standard Nix validity/integrity/trust checks; no signature or
   safety bypass, raw directory copy, alternate store or remount.
3. Require successful import and daemon queries proving the exact final output
   paths and full closure valid. Register persistent, session-owned guest roots
   for each output with
   `NIX_REMOTE=daemon nix-store --add-root <absolute-owned-root> --realise <final-output>`;
   verify the root symlinks and their registration. Operate only on the imported
   output paths, not derivations requiring a guest build. Keep host and guest
   roots while the review runtime uses these outputs.
4. Rebind the prepared units/configuration to those exact output paths and
   verify matching build metadata before activation. Unknown or failed import
   stops activation and returns the exact daemon error to I1; do not infer
   success from socket presence or silently fall back to remounts/layout changes.

This is standard Nix transport through an already mounted public file, not a new
store/copy framework. Actual daemon import remains execution evidence to collect;
the read-only investigation does not claim it succeeded. Normal OAuth provisioning
is independent. Preserve all current guests, source snapshots and backup history.

## PHP layout correction and live review

The user's later UI review supersedes the initial PHP placement: put the exact
lead-approved plan-removal explanation **inside the Backup plans form**, remove
the cleanup link from the page perex, and render the actual admin-only cleanup
form immediately below Backup plans, including when no plans remain. Reuse the
existing renderer/action, CSRF and receipt workflow. I2 owns this small source,
translation, focused-test and documentation package from backend `140f0769`;
API, generated clients and React are unchanged.

The form names the escaped root dataset. An independent **Include subdatasets**
checkbox is unchecked by default; show the escaped descendant names beside it
as the additional scope applied only when selected. The existing recursive
shortcut may precheck it. Use a static, accurate optional-scope description,
without JavaScript or an extra request. **Back up existing snapshots first**
remains checked by default; the existing destructive-confirmation checkbox
remains unchecked and required before submission. The cleanup form explicitly
explains that it disables backup plans and removes local snapshots, and that
re-enabling backups **will require a full transfer**. Use lead-approved exact
English/Czech wording. The single-use CSRF token stays bound to the dataset;
recursion is a user-editable POST boolean, not immutable GET intent. Preserve
admin authorization, normal POST validation and API scope revalidation. No
destructive action or plan removal is part of the UI acceptance check.

The already-running review cluster retains VPS1, dataset1, Plan membership1,
three confirmed source snapshots and one confirmed backup copy. The installed
fjr83 provider's README, **Runtime Updates** (778–781), says existing PHP,
template and static-file edits are live. Its `nix/test.nix:1750–1862` mounts the
selected worktree into the webui container at `/mnt/vpsadmin`, then links its
top-level webui entries into `/run/vpsadmin-live-webui`; vendor and `.git-revision`
come from the packaged dependency. I2 confirms this correction adds no new
top-level entry or dependency. Therefore **no build, provider refresh, services
update or activation command is needed**. Provider `refresh` prepares pools and
restarts nodectld; it is unrelated to PHP rendering. Edits may become visible
before commit/review; final handoff after review must not claim a later technical
activation barrier or use packaged `.git-revision` as proof of live PHP contents.

After I2 commits, passes quick checks and receives independent review, lead
releases I2's focused nondestructive HTTP check. Bind the exact changed committed
host files to the guest's served files with hashes/resolved symlink paths via
ordinary public provider SSH, then prove the explanation is inside Backup plans,
no perex cleanup link, and the cleanup form follows it with correct defaults,
optional scope and admin/member gating. Use existing protected authentication;
do not print credentials, config or unfiltered status. Preserve all guests and
fixture data. No routine reload is planned; only observed HTTP staleness returns
to I1 for bounded diagnosis and any lead-owned corrective action. No reset,
recreate, stop, deletion, seed or fixture mutation is authorized by this follow-up.

## Persistent UI-review cluster

The user requests a session-owned development cluster with a VPS, backup plan
and snapshots for human review. This authorizes development startup/provisioning;
it does not authorize production deployment, integration, reset or teardown.
Keep the cluster and fixture available. The feature contract below is unchanged.
Lead owns release/startup/status; I1 owns technical preparation and provisioning.

### Sufficient startup brief

Use public `/home/aither/bin/vpsadmin-devcluster`, selected provider
`/nix/store/fjr83w57f3m5rvljszpwhgl7n33fm9b9-vpsfree-dev-workspace-tools-0.1.0/bin/vpsadmin-devcluster`.
Its full guide is that store root's
`share/vpsfree-dev-workspace/dev-clusters/vpsadmin/README.md`.
Read-only inspection found only `config.json` and `socket-dir` in this session's
cluster directory, with stopped status and empty topology/network; no disks,
applied selection, result or maintenance hold. Use initial creation:

```sh
vpsadmin-devcluster start 2026-11-25-backup-disable-design --topology dual --network bridge
```

Lead explicitly approved changing **only** `newWebui.enable` to `false` in the
existing session config. This recorded brief releases I1's preparation of that
one flag: preserve original bytes privately with mode 0600 and record their
SHA-256, then verify the semantic diff contains only the boolean. Initial hash:
`10819c2d393795f4909695f04e4caf3d4035a94e84e25c871ecfc1ab19a16332`.
Never print raw config, `urls`, or unfiltered JSON status; they contain account
credentials. Lead captures all startup output privately, mode 0600, because
startup itself prints credentials. Watchers receive only the log path and safe
status/progress, and observe the lead-owned driver rather than submit it.

The provider selects this session's backend worktree, verified at
`140f0769e222dd2aa51e64d08f11cd5e8dae397b`, tree
`a872181147d22917e37f2a5023af7c30557fd7ea`. I1 binds clean source, packaged gem
inputs and the effective OS/input graph to its packet. The provider uses a
session OS worktree if present, otherwise local canonical `origin/staging`
without fetching; I1 reports effective OS
`cf53d6703f735d196645ad8aefd2b2b69117481a`.
Automatic React selection is session HEAD
`c723f2fab261153eddf7bee0cc967e5392836efe`; its committed Nix dependency still
uses registry SDK 0.6 without the action. I4's installed development SDK proof
does not establish packaged React readiness. PHP-first/React-disabled is
accepted; no frontend edge, OAuth, dependency or publication work blocks startup.

Dual supplies services/node1/node2; unchanged enabled DNS adds two auxiliaries.
Addresses are `172.16.106.53`, `.41`, `.42`, `.61`, `.62`; gateway `.1`, bridge
`br0`. I1's admission packet must establish exact session/socket ownership,
stopped/nonpending state, no address/global-route conflict, usable KVM/bridge
helper, current RAM/disk headroom and no heavy verification overlap. Defaults
allocate 8 GiB each to services/node1/node2 plus 1 GiB per DNS guest; include
actual disk allocation and cache needs. I1 reports usable KVM/helper and ample
measured memory/disk. Cache/namespace checks remain execution admission gates,
not missing architecture. I1 derives the exact normal provider build expression
for a bounded cache check. Unexpected local kernel compilation stops for diagnosis
under the verification procedure; no source override or kernel exception is
implied. Earlier storage/PHP VM verification remains parked. No force/reset or
peer takeover.

Lead starts after accepting that packet. Require normal command completion,
ready status, full applied-boot proof, healthy API/supervisor/node workers and
online confirmed pools. Built result/URLs alone do not prove activation.
Unknown/failed startup retains state for diagnosis; no blind reset/restart.
Subsequent changes use ordinary `update` with activation proof. Retained
`start --existing` boots applied payloads, not merely the newest build/worktree.
Fixture command preparation may continue independently while the VMs boot.

### Minimal persistent fixture

Reuse seeded node1 hypervisor pool `tank/ct`; create one ordinary open backup
pool on node2, e.g. `tank/backup-review`, through Pool.Create. No storage profile,
enrollment, NAS or extra storage node. Discover all IDs and a compatible enabled
template. Create one small running VPS owned by a seeded user with resources.
Existing CLI shapes, executed through public provider SSH to services using its
configured authentication, are:

```sh
vpsadminctl --raw pool create -- --node NODE2 --label backup-review --filesystem tank/backup-review --role backup --is-open --max-datasets 10 --refquota-check
vpsadminctl --raw vps new -- --user USER --node NODE1 --os-template TEMPLATE --hostname backup-ui-review --cpu 1 --memory 1024 --swap 0 --diskspace 10240 --start --ipv4 0 --ipv4-private 0 --ipv6 0
vpsadminctl --raw dataset.plan create DATASET -- --environment-dataset-plan ENV_PLAN
vpsadminctl --raw dataset.snapshot create DATASET -- --label review-1
```

Uppercase values are discovered IDs. I1 owns exact private provisioning input
and receipts, adapting existing helpers, not launching the destructive suite.
At the selected backend, `tests/suite/storage/remote-common.nix` supplies
`create_pool:323`, `create_vps:340`, `ensure_dataset_in_pool:1026`,
`ensure_dataset_backup_plan:106`, `create_snapshot:1480`, `fire_backup:1615`.
The real `daily_backup` definition is in
`tests/configs/vpsadmin/api/dataset_plans.rb`. Bind its EnvironmentDatasetPlan to
the source environment and attach through Plan.Create. Create the backup copy
with existing `TransactionChains::Dataset::Create.fire(pool, source, [dataset],
label: source.label, properties: {})`, and transfer through ordinary
`TransactionChains::Dataset::Backup.fire(source, destination)`.
`tests/runner/extensions/vpsadmin_services.rb:302` gives the packaged API Ruby
invocation using systemd's API WorkingDirectory and `ruby-env-wrapped/bin/ruby`;
reuse the ordinary fixture admin context. Do not fabricate confirmed rows or
transfer outside the normal chains.

Set only the fixture's source/backup retention to keep at least three snapshots
(10 is sufficient), following the scoped existing helper. Write a known marker,
create snapshot 1 and complete its backup; then update the marker and create
snapshots 2 and 3. This leaves newer untransferred snapshots for default-on
preservation without an unsupported older gap. Require every chain done, locks
released, all three source SnapshotInPool rows confirmed, and at least snapshot
1 confirmed and physically readable on the backup branch with matching marker.
Keep the real attached schedule; report its next behavior. Save IDs/receipts and
safe counts/paths only. Reconcile failed or uncertain work before retrying; retain
successful objects. Do not invoke DisableBackups or delete the plan before review.

### Human handoff and retention

PHP is `https://webui.aitherdev.int.vpsfree.cz/`; real API is
`https://api.aitherdev.int.vpsfree.cz/`. Supply actual VPS/dataset IDs and
`?page=dataset&action=edit&role=hypervisor&id=<dataset-id>` plus
`?page=backup&action=vps`; ordinary task detail is
`?page=transactions&chain=<chain-id>`. Check admin action/default-on checkbox and
plan-removal explanation against the live API without submitting cleanup.
Credentials stay in the provider's protected service/account view; never record
them here or in prompts. `cert show-ca` exposes the public CA path/fingerprint
for browser trust. React is unavailable in this PHP-first handoff. Leave cluster
and fixture available; no automatic teardown or session lifecycle action.

## Scope and public contract

Add administrator-only `POST /v7.0/datasets/:id/disable_backups` with exactly:

| Input | Default | Meaning |
| --- | --- | --- |
| `recursive` | `false` | Include the selected logical dataset's existing subtree. |
| `backup_first` | `true` | Preserve all selected existing source snapshots on every configured open backup copy before destruction. |

Use `blocking true`, `ok!` and `state_id = @chain.id`, matching the existing
[Dataset::Snapshot::Rollback action][ordinary-action]. There are no declared
action-specific output fields. Inputs use the usual `dataset: {...}` envelope.
HaveAPI still emits its ordinary empty resource wrapper: the successful wire
response is `{"status":true,"response":{"dataset":{},"_meta":{"action_state_id":123}}}`
(123 is an illustrative chain ID). Clients that unwrap `response` retain
`dataset: {}` and `_meta`; read the receipt from `_meta.action_state_id`. The empty
dataset object is framework output, not a new declared action payload. SDK/UI code
uses the existing action-state receipt/polling facility. There is no
`preservation_chain` input, public phase value, continuation call or manifest.
Return one chain even for metadata-only/already-empty work, using an ordinary
NoOp where needed. Accepted is pending; only successful receipt completion and
refreshed state establish completion. A browser or CLI exiting does not cancel
accepted work. Unknown submission outcomes require ordinary receipt reconciliation,
not automatic resubmission.

I1 observed the `dataset` and `_meta` keys in runtime responses and traced the
empty wrapper to HaveAPI 0.32.2's inherited `output {}`, `ok!` default `{}` and
`safe_output` namespace wrapping. I1 reports passing runtime assertions for
`dataset == {}` and an integer receipt on the pre-consolidation API correction
`5526c99f7f675977f7b0e4da5b060791bbd09c06`. I1 reports unchanged API/node source
at consolidated final head `50aa37aede8926965598f4f8fb0782dce377afb6`; final
export/provenance must use that current head, not the superseded check SHA.
This verifies the ordinary wrapper and adds no production action/schema output.
Lead-owned state retains the complete graph, equivalence and check evidence.

Resolve the current primary/hypervisor copy for each selected dataset; reject
ambiguous/inconsistent placement. A VPS-wide shortcut names the root and existing
descendants and submits `recursive: true`. Unrelated mounted datasets are outside
that subtree. No attached plan is required: planless snapshots are a primary use
case. Remove all plans attached to selected sources, detach their backup tree and
branch heads, and remove **all source snapshots**, including manual/untransferred
snapshots. Do not create a fresh snapshot of live filesystem contents. Do not
change the live dataset, backup history retention, existing plan permissions, or
ordinary Plan.Create/Delete meanings. There is no member self-service action,
provenance system, destination picker or persistent disabled flag.

With `backup_first: false`, source-only restore points are deliberately lost.
Normal Plan.Delete remains nondestructive and both plan-management forms explain
that it leaves snapshots on primary and backup pools.

## Evidence and why one chain is sufficient

Read-only source inspection uses vpsAdmin
`81e930b25fa3252d7e849aff4819e663cec37b07` and React WebUI
`e311b1c0af0f50fa4c6f6ce83c514c1a866eb042`, cached canonical remote defaults.
No fetch, application edit or runtime test was performed for D3. These are source
conclusions; implementation and storage verification remain package work.

| Confirmed primitive | Consequence for this operation |
| --- | --- |
| [Backup][backup] appends Transfer, source Rotate and destination Rotate in one chain. [Chain construction][chain-build] runs inside a DB transaction; nested chains share locks and append dependencies. | Conventional same-chain transfer-before-delete is supported. Use Transfer directly, never Backup or either rotation. Construction rejection queues no work. |
| [Send][send] appends remote Recv → Send → RecvCheck, or LocalSend, and prepares copy/membership confirmations. [Node selection][node-select] requires the predecessor to finish and the chain to remain queued, across nodes. | Later destruction cannot run ahead of successful transfer/check dependencies. Use only linear append order, no alternate dependency anchors or keep-going. |
| [Recv][node-recv] starts a subprocess. [blocking_fork][subprocess] prevents later work in that chain on the destination node; [daemon blocking][node-block] waits for that process to exit. [RecvCheck][node-recv-check] checks actual snapshot existence. | Receiver-start success alone is insufficient. The destination check runs after receive exit and after source Send completes. Child exit status alone is not the proof. |
| [RecvCheck parameters][recv-check-params] name only the last snapshot in a stream. [LocalSend][node-local-send] runs its send/receive pipeline synchronously. | For selected newly copied snapshots, append existing per-snapshot RecvCheck commands at their actual branch paths before cleanup; do not infer every older snapshot from a tip check alone. No new node command/parameter is needed. |
| [Confirmations][confirmations] normally apply at chain completion. Successful create confirms rows; failed/future destruction restores pending source rows; just_destroy/edit_after apply only for successful forward transactions. | Pending rows created by this chain are planned work, not already-confirmed data. Successful ordered node work can prove preservation before deletion without an intermediate DB-confirmation barrier. |
| [Command.save][node-command] rolls back a reversible failure; an irreversible failure fails followers, applies forward confirmations and closes failed. [DestroySnapshot][destroy-command] is irreversible. | The entire metadata/destruction suffix must be explicitly not_reversible, including helper NoOps. Otherwise a later reversible helper failure could roll back backup copies after source deletion. |
| [Transfer][transfer] sends only the suffix after a common head tip, or nothing when tips match. It already starts a new tree for no head/no common history. | Validate planned coverage. An older missing snapshot outside ordinary selection rejects construction. Do not add force-full or prefix repair. Existing normal initial-full/history behavior remains. |
| [DetachBackupHeads][detach] clears all tree heads/head branches on all backup copies through ordinary metadata confirmations. [Source-copy destroy][sip-destroy] preserves logical snapshots with surviving copies. | Retain these primitives and backup history. Detach after transfer planning so current heads remain available for incremental sends and newly created heads are included. |
| [Plan actions][plans-api] do not currently resource-lock sources. [Worker][worker]/[DatasetAction][action] can load actions and group members before chain locking. | Narrow lock and post-lock validity fences are needed to prevent concurrent plan insertion or stale scheduled work recreating snapshots after disable. |
| [DatasetPlans.confirm][plans-lib] calls a nonexistent legacy regenerate method, and baseline source search finds no caller. | Do not repair it or add socket/Nix plumbing for this feature. |

## Coverage and preflight

Acquire the existing source, relevant VPS, associated backup-copy and selected
source-snapshot resource locks in stable order; nested chains share them. Reload
placement, subtree, snapshots, plans and targets after acquisition. Revalidate
recursive enumeration under the parent/source locks used by dataset creation.
Reject pending/unconfirmed preexisting state, conflicting locks, maintenance or
unavailable source/VPS, unsupported plan definitions and unexpected non-plan
automation targeting selected sources. Do not silently leave such automation.

Known source snapshot references, mounts/exports/clones and active uses reject the
whole request before it is queued. Lower-level SIP destruction does not itself
check all references, so this operation must. Report the blocking object; do not
force unmount, purge clones or break dependencies. Unmanaged ZFS holds/clones may
still fail destruction at runtime, producing an ordinary partial failure.

For every nonempty source, `backup_first: true` targets **every existing open
backup-pool DatasetInPool of that logical dataset**. Require at least one usable
target and confirmed consistent target metadata. A missing/unavailable/maintained
target rejects the whole request. Closed copies are retained and detached, but
are not preservation targets. Do not create or reopen destinations, select an
arbitrary successful replica or silently disable preservation. With false or an
empty source, target availability/maintenance is not required for metadata-only
detachment; pending-state checks and all-copy locks still apply.

Capture the selected source snapshot set under locks. For every selected snapshot
and every required target, establish one of these two facts before appending
cleanup:

1. A matching SnapshotInPool and at least one actual branch membership, branch,
   tree and target placement are already strictly confirmed. Non-head retained
   history counts; merely `live`/pending membership does not.
2. Ordinary Transfer in **this chain** schedules that snapshot at a specific
   target branch, with its required copy/membership create confirmations and an
   earlier successful receive check as a prerequisite of all deletion.

Keep preexisting confirmed coverage separate from this chain's newly planned
coverage. An unrelated pending row never counts. Compare snapshot identities and
associations, not counts/names/highest IDs. No persisted manifest is needed: locks
and one atomic construction bind the selected sets and planned commands.

Skip Transfer when a target already covers all selected snapshots. Otherwise use
ordinary Transfer unchanged, inspect its planned coverage, and reject the entire
construction if any selected snapshot is missing. In particular, an old gap below
a newer head produces a clear error naming the uncovered snapshot/target. No
bespoke fallback or new force-full option is authorized. Existing Transfer's
normal no-head/no-common-history full path may still cover everything. Multiple
targets and normal full sends can use substantial bandwidth and storage.

## Chain order and failure boundary

Build one chain with the following strict order across the **whole recursive
scope**, not preservation/deletion interleaved per dataset:

1. Lock and preflight all selected resources. Build all ordinary transfers and
   validate complete existing-or-planned coverage. Queue reservations/releases
   stay in their existing Transfer/Send positions.
2. Append any additional existing RecvCheck needed for each newly copied selected
   snapshot on each destination branch. All transfers and all these checks must
   finish before any source destruction. Do not clear backup heads beforehand.
3. Append plan-unregister confirmations and head-detach metadata steps using the
   existing machinery. Use a narrowly scoped unregister option to retain shared
   group action/task rows while deleting this source's membership. Enumerate all
   associated backup trees/heads, including closed copies and heads just created
   by transfer planning. Every metadata step is explicitly **not_reversible**.
4. Append source-only SnapshotInPool::Destroy for every captured source snapshot.
   Pass the existing not_reversible override through the whole cleanup suffix,
   including download-orphan NoOps. Never use keep_going. No backup rotation,
   backup-copy deletion, logical Snapshot::Destroy or dataset destruction.

Plan removal and head detachment use ordinary confirmations, applied at chain
closure; they need not become visible before physical cleanup. Source locks
exclude scheduling while those rows are still present. All metadata steps must
precede every source Destroy, so an irreversible failure after destruction starts
applies successful plan/head confirmations along with successful transfer and
source-delete confirmations. A failure within the metadata steps may leave only
some metadata changes applied, but cannot have deleted a source snapshot yet.
Do not add an artificial early-confirmation transaction, public phase or callback
orchestrator. The ordinary receipt and transaction results describe the outcome.

| Internal execution point/outcome | Required result |
| --- | --- |
| Construction/preflight error, including uncovered old gap | DB construction rolls back, no chain is queued, plans/data unchanged. |
| Transfer/check pending | Locks held; plans may remain visible; no source destruction has executed. Accepted work continues without the caller. |
| Reversible transfer/check failure | Cleanup followers do not execute. Source snapshots/plans remain; ordinary rollback may remove newly transferred copies. Fatal rollback retains locks for reconciliation. |
| Metadata boundary failure | Preservation succeeded; no source destruction executed yet. Successful metadata confirmations may apply. Report failed, refresh actual plans/heads. |
| Source destruction failure | Successfully transferred backups remain; successful plan/head edits and completed source deletions confirm. Failed/future source copies remain. Report failure/partial cleanup, never success or an all-or-nothing rollback claim. |
| Done | All selected source snapshots removed, plans absent, backup heads detached, live data and retained backup history intact. |
| Unknown receipt/node outcome | Reconcile existing chain/transactions and actual state before deliberate retry; do not submit a second operation automatically. |

Existing non-forced ZFS deletion and fatal-chain recovery remain authoritative.
Never clear locks as a substitute for reconciliation. With backup_first=false,
software rollback cannot recover source-only snapshots already destroyed.

## Only necessary adjacent safety fences

- **Plan.Create/Delete:** take the same source resource lock for their existing
  synchronous mutations and reload after locking. This only excludes concurrent
  mutation while disable holds that source: otherwise Create can add a plan/group
  membership after disable captured them, leaving new scheduled work behind.
  Preserve current authorization, environment checks and snapshot/head semantics.
  Do not reset heads on zero-to-one plan registration.
- **Scheduled Backup/GroupSnapshot only:** propagate the scheduled action identity
  into these two chains and revalidate its existence/relationship after source
  lock acquisition, including each group member. A Ruby action/list loaded before
  disable can otherwise execute after its DB row/membership is deleted. Removed
  members skip; unrelated shared-group members continue. Direct manual operations
  retain their current meaning. Use fresh ordinary existence reads under the
  supported READ-COMMITTED contract described below.
- **Asynchronous unregister:** an orphan count computed during construction cannot
  safely schedule shared action/task destruction: a different dataset can join
  that group while this chain runs. The new action retains the shared action/task
  and confirms deletion of only selected memberships. Existing unregister callers
  keep their ordinary behavior; no general group cleanup project.
- **No scheduler notifier/configuration change:** stale queued IDs are checked by
  existing worker lookup; already-loaded work is addressed by the post-lock guard.
  A socket refresh does not provide correctness and the unused legacy helper is
  outside this operation. Remove the D2 helper repair and API-service env stanza.

The accepted guard-scope correction follows the actual configured Plan DSL:
it emits only backup and group_snapshot, and DisableBackups rejects standalone
snapshot/transfer automation. Remove the standalone Snapshot/Transfer guard and
allow_empty additions and their DatasetAction dispatch arguments. Their ordinary
and nested execution needs no new scheduler identity check. Revert Transfer's
incidental Time.new → Time.now edit under the accepted source boundary. Subsequent
I1 evidence corrects its initial rationale: component RuboCop 1.92.3 flags restored
Time.new with Style/TimeNow, while required root-hook RuboCop 1.85.1 lacks that cop.
There is a component style reason, but no feature/safety requirement or observed
mandatory-hook failure. Lead/I1 own resolving that validation discrepancy; this
brief authorizes no skipped check or hook bypass. Keep the existing local
Backup/GroupSnapshot checks and empty-chain handling needed for stale work.

The real race needs no lock waiting: a worker loads an action/member while disable
is still running; final confirmations then remove it and release resource locks;
the worker subsequently acquires the now-free source and uses its stale Ruby
object. The post-lock check prevents that work. Acquisition before release instead
fails fast (group members skip); Worker logs the failure and does not retry that
job. Lookup after removal already skips it. This is a lookup-to-lock gap, not a
queued retry or an enclosing RR guarantee.

Moving the check ahead of the chains is not the selected correction. fire2's
preacquired-lock seam skips duplicate acquisition but does not transfer lock
ownership. A scheduler-boundary replacement would need an outer DB transaction
covering acquisition/check/fire2/assignment to the returned chain, plus invalid,
empty and error cleanup and per-group-member acquisition/skipping. That duplicates
existing lock handling and is broader than retaining the two local checks. No
new callback, framework, lock mode or API guarantee is authorized.

### Positive scheduled-work acceptance

Bounded source inspection at `eb8d111b6e0c318336b818aabeacc3d575ac3279` found no
normal valid-action false negative in scheduled_for?. DatasetPlans creates a
backup action with enum value 3 and its source/destination DatasetInPool IDs;
DatasetAction.execute passes that action's ID and those associations. The guard
requires the same current row/type/source/destination. Group actions use enum 4
and GroupSnapshot membership, not source/destination columns; each current member
independently satisfies the join. Multiple members do not exclude one another.
Deleted action/member or changed action type/source/destination versus the loaded
request is stale work and fails the predicate. A fresh current action uses its
current IDs. Direct manual chain calls omit expected_action and bypass the guard.

The ordinary scheduler has no added query-cache block. Chain/resource INSERTs
precede the predicate; inspected ActiveRecord 8.1.4.1 query-cache code invalidates
normal current-thread caches on create/insert (abstract/query_cache.rb:13–25,
default dirties=true at 55). READ-COMMITTED therefore remains the supported fresh
read boundary. Do not add cache-clearing production code or arbitrary enclosing
RR/disabled-invalidation guarantees without a demonstrated failure.

Source reasoning is not positive runtime proof. Existing positive Backup and
GroupSnapshot specs call the chains directly without expected_action; the three
scheduler concurrency examples only cover stale skips and plan exclusion. I1
must close this gap with the existing real models, fixtures and chain execution:

- Register the configured daily plan, take its actual backup DatasetAction and
  call execute. With existing source snapshots/ports/retention fixtures, require a
  queued Backup chain containing conventional transfer/receive checks before
  observable source/destination rotation. Exercise ordinary enabled query caching
  in one positive path; do not stub the predicate, locks or nested chains.
- Register two sources in the same pool/plan group and execute the actual shared
  DatasetAction. Require one grouped snapshot transaction and a prepared Snapshot
  plus SnapshotInPool for every current unlocked member.
- Retain a loaded two-member source list, remove one membership through ordinary
  plan removal, then pass that list and the real action ID through the actual
  GroupSnapshot chain (the existing stale-list path). Require no snapshot for the
  removed member and normal queued snapshot work for the surviving member; one
  rejected member must not suppress the group.

Keep the existing stale/deleted-action cases, resource-conflict behavior and
direct manual positive cases. Use the existing model/concurrency specs; no mock
replacement of actual chains, VM harness, new public contract or preemptive
production fix. If real behavior fails, report the concrete predicate/input
mismatch and smallest correction before changing behavior.

### Accepted locking simplification

Bounded inspection of `e303d336c538a75938eba08e646fbd9501afe124` and I1's rationale
established no production requirement for the operation's blanket SQL row locks.
The [product database default][rc-config] is READ-COMMITTED. The test harness uses
REPEATABLE-READ, and its deliberately older outer-transaction snapshots motivated
the extra locking reads. Those fixtures do not establish a production contract.
The supported boundary for this operation is the configured production
READ-COMMITTED behavior; no global database/test-isolation setting changes.

[ResourceLock][resource-lock] is a unique `(resource class, row ID)` row. It
excludes cooperating writers until the chain completes, including asynchronous
node work. SQL `FOR UPDATE` locks end when construction commits. Neither mechanism
refreshes an already loaded Ruby object; under READ-COMMITTED, a fresh ordinary
query/reload after resource acquisition sees current committed data. Thus retain
freshness and identity checks without turning every read into another SQL lock.

| Family in the e303 implementation | Concrete ordering and sufficient protection |
| --- | --- |
| Root/subtree/source selection, operation lines 49–79 | A child/source change can finish after initial enumeration but before resource acquisition. Reload/re-enumerate after acquiring resources and reject changed identities. Dataset::Create locks the parent copy, so held source locks exclude later descendant creation. Dataset/source `FOR UPDATE NOWAIT` adds no demonstrated requirement. |
| Source snapshots and copy reloads, lines 82–97 | A snapshot writer can finish before acquisition; a fresh list includes it. Snapshot creation locks its source; source-copy destruction locks its SIP, which disable also holds. Keep durable copy/SIP locks and fresh reads; remove SQL locks on their rows and repeated object graph reloads unless a cached value is actually used. |
| Mount/clone/reference predicates, lines 125–126 | A clone/export created before acquisition is visible to fresh checks; afterward UseClone needs the held source and SIP resources. Existing mount creation also locks its source. Keep the rejection checks; `.lock.exists?` adds no demonstrated protection for these writers. |
| Backup trees/branches/pending rows/coverage, lines 35–44 and 130–139 | Managed Transfer/Rotate require the held backup copy. Existing work either owns it first or finishes before disable reads it. Retain coverage/head/pending checks using fresh ordinary queries. Short SQL locks would not protect against a bypassing writer during later node execution anyway. |
| Pool/node/user/logical snapshot/VPS reloads, lines 89–97 | A preexisting object can be stale, so reload values used for preflight. No per-writer production justification was found for locking all related rows. These SQL locks expire before transfer; they cannot promise availability stays fixed throughout the operation. |
| Plan/action/group queries and shared-group policy | Plan APIs use the source fence. A worker may load an action, then disable completes, then the worker legitimately acquires the now-free source: fresh post-lock action/member existence still rejects that stale job. Another source can join a shared group during node work, so retain its action/task while removing only selected memberships. Neither concern requires blanket SQL locks. |

Sources: [operation][disable-operation], [plan helper][locked-plans],
[scheduled guard][scheduled-guard], [snapshot writer][current-snapshot],
[child writer][current-create], [clone writer][current-clone],
[mount writer][current-mount], [transfer][current-transfer],
[rotation][current-rotate], [source-copy deletion][current-sip-destroy].
These are bounded representative writers, not an exhaustive audit.

I1's smallest correction is to remove `.lock`, `reload(lock: ...)` and
`FOR UPDATE NOWAIT` from this operation's read/preflight families; retain its
durable VPS/source/backup/source-SIP acquisition and fresh post-lock scope
revalidation. Simplify DatasetPlans.with_locked_source's SQL reads while retaining
its resource fence, current source identity and ownership checks. Make
keep_shared_group control only retention of shared action/task rows, removing its
query-lock coupling. Use plain fresh reads in DatasetAction.scheduled_for? and
the disable chain's plan enumeration. Do not change existing storage writers,
resource-lock implementation, DB configuration, API/schema or generated clients.

Keep the same behavioral concurrency assertions: stale scheduled work is skipped,
concurrent plan mutation is excluded, changed source/owner is rejected, recursive
scope is revalidated, and an unrelated group member survives. Specific examples
may select READ-COMMITTED on their own connections and restore that setting;
replace only the unsupported arbitrary enclosing RR promise. Do not replace
behavior tests with assertions about exact SQL or method calls. All preservation,
irreversible failure, reference and one-receipt checks remain unchanged.

An arbitrary preexisting REPEATABLE-READ transaction would require targeted
current reads or a separately defined transaction boundary; plain reload is not
a guarantee there. Supporting that additional contract is outside this accepted
simplification. No broad redesign or new mechanism is authorized.

Successful disabling itself detaches heads. Normal subsequent plan assignment,
new snapshot and Transfer therefore start a new tree/full first send; later sends
can be incremental. Empty sources create no tree until a later snapshot exists.
No new policy overrides a deliberate restore/manual transfer that changes heads
in between. Ordinary plan registration and restore retain existing behavior.

## UI and CLI behavior

| UI | Exact placement |
| --- | --- |
| PHP | At `?page=dataset&action=edit&role=hypervisor&id=…`, explanation inside Backup plans; actual admin-only CSRF cleanup form immediately below it, including zero plans. No perex cleanup link. Preserve the VPS-backup shortcut's return context and recursive selection; see the later PHP layout correction above. |
| React | Shared DatasetPlansPage at `/app/datasets/:datasetId/plans`, `/admin/datasets/:datasetId/plans`, also embedded in `/app/backups?tab=plans&dataset=…`. Admin/capability gate the action including empty plans. VPS storage links to the existing plans route with its `/app` or `/admin` prefix; there is no admin Backup Center route. |

Sources: [PHP form][php-form], [page][php-page], [VPS backups][php-backup];
[React routes][ui-routes], [plans][ui-plans], [workspace][ui-workspace],
[VPS card][ui-vps].

Both confirmations show the selected dataset/root and recursive descendants,
all-primary-snapshot removal, retained backup history under normal retention, and
**Back up existing snapshots first**, checked by default. Explain existing
snapshots only, all-open-target policy, ordinary transfer cost and that inability
to preserve any selected snapshot stops the operation. Explicit opt-out warns
about loss of source-only restore points. Lead finalizes English/Czech wording.

Both UIs submit once and use their normal task receipt handling. PHP may poll for
its existing bounded interval and render a task status control if pending; status
requests only observe. Remove preserved/Continue cleanup controls, retained
continuation options, phase adapters and client orchestration. React follows its
existing pending/failed/unknown task behavior. Keep normal duplicate-submission
protection; do not add a new workflow/session receipt subsystem. Only successful
chain completion and fresh reads show completed disablement. Browser exit does
not promise to stop the operation.

Both existing dataset-plan forms explain beside removal that ordinary plan
deletion stops scheduled work but leaves primary and backup snapshots in place;
React repeats this in its removal confirmation. This explanation is available to
existing authorized plan users even without cleanup capability. Planless does
not mean empty backup history.

API/CLI documentation shows one POST with the two optional booleans and one
ordinary receipt wait. No caller orchestration or phase-specific retry protocol.

## Compatibility and correction boundaries

No migration, new node command, new node wire parameter, manifest or orchestrator
is needed. Existing node commands and persisted storage formats suffice. New API
and scheduler workers must carry the narrow source-lock/post-lock guards before
exposing the action; do not enable it with older workers lacking those guards.
No fleet-wide vpsAdminOS upgrade or Nix socket change is justified. Old clients
retain existing operations; UI capability gating handles an old API.

Export the final committed API and synchronize Go/Rust/TypeScript through I3.
The React final dependency must use a published SDK before merge; publication,
integration and deployment remain separately authorized. Unpublished D2 shapes
are superseded implementation work, not a compatibility version to support:
remove them and consolidate obsolete branch history before final review, retaining
prior evidence and exact-head provenance in lead-owned records.

Remove all D2-only continuation/manifest validators, NoOp payload, public phases,
forced old-gap fallback, first-plan head reset, scheduler notifier/Nix stanza and
their dedicated tests/docs. Preserve useful data-coverage, reference, concurrency,
ordinary receipt and UI tests, rewriting assertions for the corrected contract.
Do not discard unrelated source or evidence. Implementation stays with its owners.

Before backend rollback, reconcile queued/running chains; disable UI access before
removing API support. Detached history stays readable by existing versions.
Rollback cannot recreate destroyed snapshots or restore removed schedules.
Existing backup retention remains effective; this action does not promise an
indefinite retention exemption.

## Focused acceptance and checks

I1 quick checks cover authorization/defaults/false, planless and empty sources,
recursive scope, all-target confirmed/planned coverage, closed copies, missing or
unavailable targets, pending state, references and ordinary no-head/history full
transfer. An older/middle gap outside normal selection rejects the entire
construction with no queued work. No new force-full behavior or rotations.

Assert every transfer/check in every dataset/target precedes the first source
Destroy; copied intermediate snapshots get existing checks at their actual paths.
Test cross-node dependency/fail-stop behavior using existing node command specs.
Failure on a later target/check must leave all source snapshots untouched.
Assert every cleanup suffix transaction, including helper NoOps, is
not_reversible. A later destruction/helper failure must not roll back preserved
copies; confirmations reflect successful work, failed/future source copies remain.
Test metadata-only work and pending/unknown receipt handling.

Controlled concurrency checks cover plan mutation against disable, an already
loaded action, a stale group-member list, an unrelated dataset joining the shared
group, and recursive child creation. Preserve ordinary plan Create/Delete results
and restore behavior; no first-registration head reset. UI/CLI tests use one POST,
one ordinary receipt, no continuation and no completion claim before success.
Test default-on opt-out consequences, admin/capability/empty-plan states, both
plan-removal explanations, Czech/English and relevant desktop/mobile paths.

I1 owns fixture source before independent review; long VM execution follows review:

- `tests/suite/storage/backup-multiple-destinations-remote.nix`: extend its two-target
  fixture using known per-snapshot contents, a normally lagging target, one-call
  preservation/cleanup, retained-history readability and unchanged unsnapshotted
  live contents. Reenable normally; prove a higher new tree/full first transfer,
  then incremental transfer in that tree. Add an older non-tip missing snapshot
  case asserting construction error and unchanged source/plans/history, not repair.
- `tests/suite/storage/backup-remote-interrupted-send.nix`: reuse faulty-mbuffer
  injection for preservation failure; assert no source deletion or plan removal,
  readable source/live payloads and ordinary failed receipt; deliberate retry only
  after reconciliation. Include irreversible cleanup failure where the existing
  fixture can inject it narrowly; unit checks must cover its confirmation boundary.
- `tests/suite/storage/remote-common.nix`: only bounded needed helpers. Existing
  create/retention/snapshot/deletion, branch-path/content/checksum, chain/receipt and
  faulty-mbuffer helpers suffice as the starting point. No new test harness.

Read every retained backup snapshot's actual contents at its branch location;
DB counts alone do not prove data preservation. Raise fixture retention so its
setup/reenable cannot prune the evidence. Assert no extra live-state snapshot.
Both suites are already registered/selected; change tests/all-tests.nix,
ci-selection.yml or ci-tags.nix only if actual source choices require it. Existing
full-incremental suites are references, not another mandatory run batch.

[plan.md](plan.md) owns the complete package/file/dependency boundary. Owners run
repo-declared quick checks, commit complete intended source including fixtures,
and supply exact base/head/history/migration evidence before lead invokes final
independent review. Long checks follow review under the monitor procedure. No
runtime test result is claimed by this design correction.

## Source anchors

[rc-config]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/nixos/modules/vpsadmin/database.nix#L102
[resource-lock]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/lockable.rb#L25
[disable-operation]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/lib/vpsadmin/api/operations/dataset/disable_backups.rb#L35
[locked-plans]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/lib/vpsadmin/api/dataset_plans.rb#L60
[scheduled-guard]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/dataset_action.rb#L44
[current-snapshot]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/dataset/snapshot.rb#L9
[current-create]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/dataset/create.rb#L15
[current-clone]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/snapshot_in_pool/use_clone.rb#L6
[current-mount]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/vps/mount_dataset.rb#L6
[current-transfer]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/dataset/transfer.rb#L6
[current-rotate]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/dataset/rotate.rb#L5
[current-sip-destroy]: https://github.com/vpsfreecz/vpsadmin/blob/e303d336c538a75938eba08e646fbd9501afe124/api/models/transaction_chains/snapshot_in_pool/destroy.rb#L8

[plans-api]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/lib/vpsadmin/api/resources/dataset.rb#L706
[plans-lib]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/lib/vpsadmin/api/dataset_plans.rb
[backup]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chains/dataset/backup.rb
[detach]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chains/dataset_in_pool/detach_backup_heads.rb
[transfer]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chains/dataset/transfer.rb
[send]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chains/dataset/send.rb
[sip-destroy]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chains/snapshot_in_pool/destroy.rb
[worker]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/lib/vpsadmin/scheduler/worker.rb
[action]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/dataset_action.rb
[destroy-command]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transactions/storage/destroy_snapshot.rb
[node-command]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/command.rb#L91
[confirmations]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/confirmations.rb#L96
[php-form]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/webui/forms/dataset.forms.php#L466
[php-page]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/webui/pages/page_dataset.php#L362
[php-backup]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/webui/forms/backup.forms.php#L24
[ui-routes]: https://github.com/vpsfreecz/vpsadmin-webui/blob/e311b1c0af0f50fa4c6f6ce83c514c1a866eb042/src/routes/router.tsx
[ui-plans]: https://github.com/vpsfreecz/vpsadmin-webui/blob/e311b1c0af0f50fa4c6f6ce83c514c1a866eb042/src/pages/app/datasets/DatasetPlansPage.tsx
[ui-workspace]: https://github.com/vpsfreecz/vpsadmin-webui/blob/e311b1c0af0f50fa4c6f6ce83c514c1a866eb042/src/pages/app/backups/BackupCenterDatasetWorkspaceView.tsx#L101
[ui-vps]: https://github.com/vpsfreecz/vpsadmin-webui/blob/e311b1c0af0f50fa4c6f6ce83c514c1a866eb042/src/pages/app/vps/VpsControlCenterCards.tsx#L263
[ordinary-action]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/lib/vpsadmin/api/resources/dataset.rb#L634
[chain-build]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transaction_chain.rb#L73
[node-select]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/daemon.rb#L208
[node-block]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/daemon.rb#L438
[subprocess]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/utils/subprocess.rb#L4
[node-recv]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/commands/dataset/recv.rb#L8
[node-recv-check]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/commands/dataset/recv_check.rb#L6
[recv-check-params]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/api/models/transactions/storage/recv_check.rb#L7
[node-local-send]: https://github.com/vpsfreecz/vpsadmin/blob/81e930b25fa3252d7e849aff4819e663cec37b07/libnodectld/lib/nodectld/commands/dataset/local_send.rb#L6
