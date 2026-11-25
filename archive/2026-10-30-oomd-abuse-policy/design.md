# Shared incident escalation — implementation brief

## Nov24 merge preparation — three bounded independent packages

**Sufficient brief; implementation owners0/4/2 proceed within root allocations.**
The user's “prepare it for merge” authorizes preparation, checks, feature publication
and review. It does not authorize a default merge, a new npm/tag release or deployment.
Session/roster44 and saved Astra/Sol xhigh/workspace_write/full_access are unchanged.
This architect package changed only this design record; no remote/CI/live read,
fetch, source/index/Git mutation, test/build/evaluation or runtime action.

### SDK preparation and eventual React registry adoption — owner0, then owner2

Reuse reviewed SDK source aed11d01c0d1436293f45a1a4e83d88421375bc1 and its immutable
0.6.0 archive:348079 bytes, SHA256
9cba02754bec157616c66207312f44312e9af36fe5deb05e8e68585615e17ca9.
Artifact commit b619eb8324bfe80c7b225f698fb83efe97639c83 is a direct aed11 successor
and retains those exact bytes; it is not their packed source. Schema7e2a and raw74c0
provenance429f remain literal. The accepted final-client receipt already binds the
byte-equal8846 export; history consolidation alone needs an exact successor-input
comparison, not a new export, generation or archive. Owner4 supplies that comparison
for the95860 replay. Preserve exporter lock2e9a, HaveAPI generator1ef9 and runtime
peer0.32.0; update no generated files or captured source labels without a real change.

Existing receipts `nov24-client-sync/{result.json,candidate-receipt.json,
artifact-publication/result.json,final-acceptance/result.json}` and combined
`nov24-admin-incidents/final-review.md` cover source, archive, checks and history.
Owner0 verifies retained bytes, clean intended series and current release prerequisites;
reuse passed exact-source build/type/strict-consumer/unit/archive checks. No second
build/pack merely to produce another readiness receipt. Current owner0 read confirms
latest registry0.5, no0.6/tag, NPM_RELEASE_ENABLED=true and the protected release
reviewer/tag policy. npmwhoamiE401 does not invalidate OIDC; no login/setup campaign.
README's0.5 example names today's published stable version; any publication-time
prose alignment belongs to root's writing pass and must not silently relabel9cba.

Preferred reviewable automated release proposal: SDK **main to b619**, covering both
registered source and auxiliary-artifact lineage, then **v0.6.0 at aed11**.
`docs/releasing.md:76–93` and `tools/release.mjs:14–30,66–70` require the tag's commit
to be on main, not equal its tip. The package whitelist excludes development-artifacts.
The ordinary tag workflow builds/validates once and retains its own archive+receipt;
the protected publish job publishes exactly that immutable artifact ID. Its bytes
are independently bound, not assumed to equal the earlier local tarball. Preserve
the tag-run receipt for registry readback and uncertain-publication recovery.
Manual publication of the retained archive is separately documented and has no
universal main/tag prerequisite, but currently requires npm authentication; the
already configured automated route is the concrete shortest supported path here.

Owner0 prepares the exact clean target, refs/commands, archive evidence and approval
boundary now. **Only after that package is reviewable** does root resolve explicit
SDK-main integration plus0.6 publication/tag authority and the protected job approval.
The completed Nov23 release supplied no new0.6 authority. Do not create a tag,
change npm settings or start publishing during preparation. SDK release can precede
backend integration: the generated reads remain capability-gated, with no server
activation implied. Other API-client source delivery obligations remain separate.

After a real0.6 registry artifact is read back and verified, owner2 follows
React `docs/design/PACKAGING.md:53–63`: pinned npm-generated exact0.6 manifest/lock,
current SDK provenance selection, frontend npmDepsHash and affected
HAVEAPI_CLIENT/PACKAGING/work-log docs. Preserve historical archive receipts, HaveAPI
runtime, BFF lock/hash and transport. Verify registry integrity, required Exposure/
Evaluation Index members/metadata and peer, then typecheck and affected SDK wire/
admin-incident tests, design/source audits and dependency prefetch. Bind any final
package/build evidence to the actual final lock/hash; no generic system build campaign.
The repository's published-SDK requirement is a genuine **React premerge gate**;
backend deployment and this session's already accepted demo are separate. Prepare
commands/docs now, but do not fabricate registry resolution while0.6 is absent.

### Backend95860 rebase and source isolation — owner4

Root's current target is95860bc2432844b243741532d165b79e5b973488, direct4062 successor.
Owner4's authorized fetch/diff proves exactly twelve package lock/gemset paths:
API jwt3.3.0→3.3.1; client/download-mounter/libnodectld/nodectl/nodectld
json3.1.0→3.2.0 with matching gem-source hashes. No HaveAPI, Ruby source, exporter,
fixture, schema, plugin, PHP or Composer changes. Architect's earlier local object
lookup lacked95860; owner4 supplied the concrete delta without a duplicate fetch.

Reconstruct the accepted two-purpose669fb9 series in the nonmounted checkout,
preserving API→PHP order/authorship and feature patches. Quick admission is ordered
patch/full-binary-diff equivalence4062..669fb9 versus95860..NEW_BACKEND, exact twelve
upstream-only differences669fb9..NEW_BACKEND, lock/gemset version/hash consistency,
normal hooks and complete migration/history review. Preserve consumed migration
20261030180000/blobff9dd726/SHA2eec970f; no new schema or obsolete migration. API
source/declarations/exporter/fixture/tooling inputs remain exact, permitting a
revision-specific client no-change record without SQL/export/regeneration. Packaged
jwt changing is distinct from the exporter's unchanged locked toolchain.

Do not call old native bundles or old API results execution of the new packaged
dependencies. API CI resolves its effective component bundle independently of
packages/api/Gemfile.lock (`docs/agent-instructions/testing.md:116–133`); use actual
environment/version evidence for any matching dependency claim. Current669 Ruby/API
pending remains unresolved. Root owns final-head ordinary CI disposition; reuse
unaffected source checks, avoid broad local reruns and report any package-execution
gap. If a concrete matching-dependency failure appears, diagnose its focused case;
no environment restoration, package rebuild or new database is allocated here.

Keep served canonical669fb9 files/index/ref and public selection frozen during this
preparation. A replayed successor is not its descendant and has a different package
tree: do not use the previous tree-equal metadata-only reselection trick. Publish
and register the prepared successor through an ordinary separate owned feature
branch/worktree under root's Git window; preserve old669/a25b/deployed refs. It can
be reviewed and later integrated from that nonmounted source without changing the
provider's canonical path. Any eventual canonical checkout selection is a separate
root-owned source/runtime boundary, not a prerequisite for merge preparation. The
immutable running API does not make arbitrary edits to live-mounted PHP harmless.
No configuration/KB repin or redeployment is allocated by this package.

### React structural correction — owner2, independent of SDK publication

Saved run45447641643 fails only the structural step: AdminIncidentViews.tsx581lines
and routes/router.tsx502 exceed500. Subsequent chained quick commands did not run;
production build/script regression/broad smoke are separately passed evidence.
Use ordinary local file extraction, retaining markup, text, links, types and null/
false/action semantics. A small AdminIncidentFacts.tsx containing DateFact, counts,
Fact, ChainLink and OutcomeSummary removes the shared display functions from Views;
retain existing exports where callers/tests depend on them. No classifier/framework.
Extract the five existing admin incident route objects to an ordinary
adminIncidentRoutes.tsx RouteObject array and spread it at the same admin position,
following securityAdvisoryAdminRoutes.tsx. Preserve paths, order, parent guards and
lazy/CoreRoutes elements; leave member/per-VPS routes unchanged. Add that source to
the inventory reader's explicit routeFiles list and update its existing fixtures/
generated inventory, without changing parsing semantics. No budget/debt exception.

Run structural/design audits, typecheck and existing focused AdminIncidentViews/
admin-controller/router-inventory checks; finish the ordinary quick chain once so
commands previously skipped after structural are covered. Reuse prior visual/broad
smoke evidence if rendered behavior is unchanged; no automatic browser/VM repeat.
Commit the completed narrow correction, preserve the consolidated purpose history,
and supply affected independent review with the complete final series. Registry
adoption later is a separate dependency change with its own exact lock/provenance
checks. Root coordinates any consolidation to avoid renewed fixup/pin history.

**Exit:** SDK publication proposal ready for the final authorization boundary;
backend rebase accepted with exact input/migration equivalence and check limits;
React structural checks clear, with registry adoption held only on the real release.
Then root assembles exact final review/check/default-target evidence. No blanket
merge-ready claim while required results or the React registry gate are unresolved;
no default mutation is authorized by “prepare”. Session/runtime remain open and
unchanged; root owns state/portal and consequential decisions.

## Nov24 UX redeployment — delta to the accepted services update

**Sufficient source-only refresh for owner0; root releases execution after the
final PHP/React commits, quick checks, affected review and accepted visuals.**
Final inputs are `FINAL_PHP_UX` (owner4, descendant of8846) and `FINAL_REACT_UX`
(owner2, descendant ofef6); their exact SHAs/trees are not yet handed back here.
This adds no source implementation, API/schema/SDK change or lifecycle action.
Same session and roster44/settings verified; architect performed no live probe,
evaluation, build, browser, source/Git or runtime mutation.

**Selected tooling still supports the ordinary route.** Stable commands now select
`/nix/store/g7wvpp2nc9cvsa8pdf1azfdib80kkcjm-dev-workspace-0.2.0`, whose extension
manifest selects `/nix/store/f3cgycvhipw7yffj2jpn8wms71qzk76c-vpsfree-dev-workspace-tools-0.1.0`.
Its provider README, command, flake, test configuration, runner, shared runtime
helpers and runtime-contract.json are byte-equal to the previously inspected74l17
provider. The current installed coordination guide retains the same ownership and
recovery boundaries. Use stable `vpsadmin-devcluster update
2026-10-30-oomd-abuse-policy services`. Existing session-owned guest/bridge ownership
and provider locks remain sufficient; this package needs no configured physical
host claim. A refusal is a stop for diagnosis, never authority to repair a provider,
change aliases, switch packages or acquire a different target.

**Source selection is an activation boundary.** Provider
`dev-clusters/vpsadmin/bin/devcluster:686–810,815–893` resolves fixed session paths
`vpsadmin` and `vpsadmin-webui`, derives HEAD/dirty labels, and supplies normal Nix
source overrides; it has no alternate public backend-worktree argument. The
existing `portal.yml` registration for vpsadmin remains the canonical feature
branch `2026-10-30-oomd-abuse-policy`. Do not repoint it, rename a mount or create a
provider alias to select the nonmounted preparation checkout.

Owner4 keeps all drafts in `worktrees/2026-10-30-oomd-abuse-policy/vpsadmin-nov24-ux`,
branch `2026-11-24-incident-admin-php-ux`. Keep canonical `vpsadmin` frozen at
8846c22b20d805ee3d63718d9d23a5be5319b4bf until root accepts the final package and
releases the deployment source/runtime window. Then the allocated Git owner checks
that canonical HEAD is still8846, both relevant checkouts are clean, and8846 is an
ancestor of the exact accepted `FINAL_PHP_UX`; advance the existing canonical
feature checkout with ordinary `git merge --ff-only FINAL_PHP_UX`, required hooks
and exact post-command HEAD/tree proof. Publish/update its normal feature comparison
and session records through the existing workflow, retaining both feature refs.
This is feature advancement, not a default merge; it requires no repository merge
claim and grants no default-branch authority. Any divergence returns to root before
mutation, not a reset/cherry-pick/rebase during deployment.

This fast-forward itself makes PHP files live: provider `nix/test.nix:1815–1863`
symlinks served content to `/mnt/vpsadmin/webui`. It must therefore occur only after
review and visual acceptance, with owner0 aware of the exact activation point.
PHP can become visible before the packaged services/React switch; that short mixed
state is compatible because API behavior, schema, dependencies and policy data are
unchanged. Do not label it the completed deployment. React stays at the ordinary
`vpsadmin-webui` path, frozen at accepted `FINAL_REACT_UX`; its running artifact is
immutable. No draft PHP copy into the canonical mount and no runtime SDK shim.

**Reuse the terminal baseline, refresh it once at execution.**
`nov24-dev-cluster-update/packet.md` is the last proved baseline, not a fresh live
claim: services rprb7zmgphpmy0hhxikn03cv8vkw34sj, API8846, Reactef6/BFFba85,
pending=null; config baf73377, OS52eb, statusf783 and all non-target descriptors.
Owner0 binds full old/new source and store identities in the same receipt mechanism,
with a fresh status/pending check and preservation baseline before activation.
Preserve existing data, saved22/20 and25–29 facts, stopped VPS disks, sessions,
credentials, policy3/10 declaration, recipients/preferences, exports and kernels.
New legitimate authentication/arrival records extend the baseline rather than
invalidating preservation of its original subset.

Mailpit now uses persistent `/var/lib/mailpit/mailpit.db` and the retained
`/usr/local/lib/systemd/system/mailpit.service.d/50-preserved-database.conf`
(MP_DATABASE; digest0a826ef127f987fe74d516561f74e96e5bd95dfc0dff8319aa6fa9a53468e12f).
Last accepted total22 includes7 legitimate login captures. Take a fresh native
online SQLite backup/private recovery copy using the accepted backup procedure;
verify the actual selected database/drop-in and protected IDs/full contents before
and after this update. Do not repeat the old temporary-to-persistent migration,
remove the drop-in, restore over newer captures or reconstruct mail from API JSON.
This remains retained per-demo state, not source-reproducible on recreation.

Keep the accepted effective templates
`/nix/store/anvr4fnymyq9ckfadzy0qc969xhagnss-vpsadmin-effective-notification-templates-1`.
PHP/React presentation changes do not alter backend daily plain text, site7af HTML,
plugins or recipients. Compare actual packaged template inputs/bodies with that
accepted composition if the new backend package path changes; a new derivation or
revision label alone does not require reconciliation. No raw7af reconciliation,
old activation-script replay, or blind repeat of the previous effective reconcile.
Unexpected effective body drift goes to root before template mutation.

**One bounded execution and acceptance batch.** Reuse the accepted services graph/
dry-run recipe with selected f3 provider, final clean sources and fresh applied
context. Admit only the affected application/packages and services assemblies;
keep one job/core and guest/headroom allowance. Previous226 builds/449.675s and
239.375s update are historical costs, not this batch's required work or budget.
Stop unexpected kernel/compiler/root-image/nodeOS/host-tool work, unrelated input
or layout changes and material restoration; reassess substantive build work at15min.
Freeze inputs through the ordinary update and readback. Its pending-before-copy,
API restart, node nodectld refresh and exact promotion still apply
(`bin/devcluster:1457–1517`); node system/kernel and other guests stay unchanged.

After pending clears, prove exact PHP source and served React artifact/BFF mapping,
Mailpit preservation, unchanged effective daily plain/HTML, data/session/credential
invariants and healthy ordinary services. Perform only the finite affected UI pass:
admin Overview/Reports/History links, filters/paging/details and meaningful saved
outcomes;1280 desktop PHP sidebar beside content without overflow;390 mobile
viewport/wrapping; EN/CS and existing member boundaries. Reuse accepted source
checks and historical API evidence within their scope; no new VM/CI/media campaign.
On failure reconcile actual files, pending target and guest effects first. Preserve
all recovery copies/old refs and the complete deployed input graph; root owns any
same-target forward correction. No automatic downgrade, reset, restart of the
cluster, DB restore or replay of an uncertain activation. All previous preservation
and recovery obligations remain; this addendum replaces only stale input/tooling
selection for the UX redeployment.

## Nov24 UX correction — compact Incidents views

**Sufficient presentation-only brief; root releases owner4/PHP and owner2/React.**
The user inspected deployed8846/ef6 and requested PHP sidebar subpages, a narrower
vertical Overview, substantially less React density, removal of the quoted
technical help blocks, and understandable History. Same session/roster44/settings
verified. API semantics, endpoints, selected fields, SDK/schema, policy decisions,
queries and daily report stay frozen. Preserve all IDs/URLs/filters/paging/cutoff
handling, old-API gates and administrator/member/support boundaries. Do not amend
merged history. No live/browser/build work was done for this design.

**Observed source and captures.** Actual deployed screenshots are
`nov24-dev-cluster-update/private/{php,react}-admin-{overview,history}.png`.
PHP `forms/admin_incidents.forms.php:365–373` forces #content to100%, overriding
normal820px content beside300px #aside in template/css/main.css:168–177. Its7-column
Overview and nested counts table then push the sidebar below. React's fixed-width
7-column TableCard fits, but every row shows normal flags, dates and action metadata.
History puts saved evaluation jargon and current action details on equal footing,
so the actual incident and result are difficult to scan.

### Shared information hierarchy and truth rules

Overview still shows **all current VPS/policy matches**, including stopped VPSes.
Each entry first identifies linked VPS/hostname, owner and policy; then two short
count/threshold lines (warning count/limit/period and shutdown count/limit/period),
server-provided remaining/reached state, current threshold status and a short latest
recorded outcome. Keep remaining counts accessible and unambiguous, especially one
remaining; never relabel remaining as a forecast. Avoid repeated paragraphs,
permanent normal Yes/No flags and a separate date column. Invalid configuration and
failed/uncertain outstanding actions remain prominent. Show effective observe/notify
mode or explicit disabled shutdown as a short restriction when it matters, without
computing a new eligibility decision. Other flags, global/effective modes, node,
accounting epoch, cooldowns, last incident/warning/stop, chain/notice links and full
latest-action/mail facts move into closed row Details. All existing facts remain
available without another request. A null restriction remains unknown, never false.

History retains **one saved incident-report/policy evaluation per entry**, the same
server order/filters/page membership. Lead with evaluation date/time, report link,
VPS and policy. Show two separately labeled parts: saved decision/context, and
latest recorded result. The former uses only saved decision, matched/state,
threshold and count/limit/period fields; the latter uses the attached action/mail
fields at read time. A concise saved threshold/count line provides context for the
decision; do not claim it proves the cause of suppression or no action. In particular,
report29 can show shutdown threshold reached with decision none: do not infer a
cooldown, exemption, duplicate action or successful stop from that combination.
No recorded reason means no invented reason. Put owner, policy key, detected time,
complete saved limits/modes/booleans and technical timestamps in Details.

Keep evaluation error/skipped/audit-only or explicit unmatched/unknown membership
visible when it changes interpretation. Completed warning action is not evidence
that mail arrived; sent means accepted by the mail server. Pending, queued,
suppressed, failed, uncertain and absent action/mail remain distinct. Only an
explicit stop_completed_at supports confirmed physical shutdown; a completed request
without that field remains a completed request. A repeated physical_stop_action_id
must be identified as the same shutdown reference (short ID/link or Details), never
counted as another shutdown. Do not group/deduplicate server rows or turn History
into an event timeline. Keep report/transaction/notice links and original/deleted
VPS identity handling intact. There is no new classifier/evaluator or API fallback.

Remove PHP's full cutoff/latest-facts and History-evaluations/retries/mail/shared-stop
help rows (`admin_incidents_page`378–380), and React's snapshotHelp+actionHelp
Overview Alert in `AdminIncidentPageView`. Also omit the equivalent long default
History Alert in React for the shared clarity correction. Do not replace them with
a new banner. Keep one compact time indicator and History period/scope near controls;
put as_of/read_at distinction and detailed semantics in existing technical docs or
closed page Details if useful. Do not change the actual cutoff controller or imply
that as_of freezes mutable state. Root owns final concise EN/CS wording and applies
the writing skill before commits; owners supply the exact changed string/key list.

### Package PHP — owner4

Use the established `$xtpl->sbar_add(label,url,docId)` / `sbar_out` mechanism for
Overview, Reports, History on admin incident subpages. Remove the inline pipe-nav;
keep `admin.incidents.overview/list/history` semantic IDs, exact routes including
Reports `list=1`, current-page indication, existing Back/policy sidebar links, and
member rendering. Keep the top-level Incidents menu. No second navigation framework
or global sidebar helper redesign. Relevant seam: pages/page_incidents.php and
forms/admin_incidents.forms.php:16–30; helper lib/xtemplate.lib.php:601–624 already
accepts doc IDs. Preserve report Show/New/member behavior.

Remove the100% content override. Render Overview and History as a vertical list
within the normal content column: identity/header, compact count/decision context,
status/result, then native keyboard-accessible `<details><summary>` and a wrapping
label/value list. Use existing visual classes; no nested multi-column matrix that
sets a large minimum width. Long hostnames/labels/IDs wrap. Keep the current filter
form behavior; collapse secondary filters only with all current values retained and
applied nondefault filters visibly indicated. Page-local styling only. At1280 the
aside must remain beside the content and Overview/History must fit that column.
At390 stack these page's entries/labels/controls without added projection overflow;
use only narrowly scoped responsive adjustments if the legacy fixed shell needs
accommodation, and report remaining unrelated chrome limits honestly. Do not
redesign the entire PHP application shell.

Viewport clarification: template/template.html:35 currently hardcodes width=1150,
so real390px mobile browsers never enter the intended narrow media query. Use one
ordinary template variable for the viewport content, initialized to the exact
existing `width=1150` in public/index.php beside the other template assignments.
Only the administrator Overview/History rendering path overrides it to the literal
`width=device-width, initial-scale=1`. Use existing XTemplate::assign; no new
XTemplate class API/default lifecycle or JavaScript meta mutation. Keep Reports,
Show/New, member and all unrelated routes at their existing1150 default, including
error/unauthorized paths unless the authorized new page shell is actually selected.
Pair device width with the already-scoped narrow CSS for these pages; changing the
meta alone does not cure legacy header/navigation minimum widths. Keep any required
narrow header/nav wrapping or local containment scoped to these two pages, preserve
all controls and zoom, and do not hide overflow to conceal inaccessible content.
Regression checks assert one correct meta for both new pages and unchanged meta for
Reports/member/unrelated routes;390 browser acceptance must use a mobile context
that honors viewport meta, as well as the1280 desktop sidebar geometry.

Owner4 files: scoped admin form, incident page, local scoped style if necessary,
public/index.php's default assignment and template/template.html's meta only,
PHP gettext POT/CS PO/generated MO, existing AdminIncidents regression tests and
owning incident UI documentation. No Ruby/API/package-lock changes. PHP is served
from the live vpsadmin worktree: use a root-approved **non-mounted** owning checkout
based on8846, not the served source. Existing vpsadmin-php-admin-commit is73cd and
must be prepared to the accepted baseline before editing; root serializes backend
Git windows. Do not expose draft PHP through the current runtime symlink.

### Package React — owner2

Keep routes, admin sidebar and existing tabs. Retain TableCard and mobile-card
patterns, with a compact four-column desktop Overview: VPS/owner+policy;
warning/shutdown counts; status; latest result+Details. Use two short count lines,
not repeated sentences. Closed Details holds the expanded existing facts; avoid
showing both expanded desktop and mobile copies to assistive technology. Native
`details/summary` is already used in ErrorState/SmartInputHelp and needs no new
accordion library. Give the disclosure a clear accessible name. On mobile, use the
same information hierarchy in existing cards. No font-size reduction as a density fix.

Reduce the permanent filter area: Overview keeps policy, status and sort readily
available; History keeps policy, scope and period. Put IDs, modes/permissions,
action/mail-state refinements and direction in a closed More filters disclosure.
Preserve all fields and URL semantics, keep hidden inputs enabled, indicate active
advanced filters (or open the disclosure for a nondefault URL), and preserve Apply,
Back, Refresh and cutoff-transition disable behavior. Scope=outstanding still disables
period exactly as today. This is presentation state, not a new query/debounce scheme.
History can use compact existing TableCard rows or the same vertical pattern, with
source/time, saved decision/context and current result clearly separated. Keep
secondary facts in per-entry Details rather than dense default columns.

Owner2 files: AdminIncidentViews.tsx, AdminIncidentPageView.tsx,
AdminIncidentFilters.tsx and corresponding focused tests; ops/incidents EN/CS
catalogs; REQ-051/work-log/owning design docs. Keep adapters/models/capabilities,
URL/controller semantics, SDK archive/lock/Nix hash/BFF untouched. If a minimal
presentation label helper is useful, keep it local and test explicit states; no
new domain abstraction. Final application head is a new commit after ef6.

### Acceptance and delivery

Both owners run focused quick checks: PHP changed syntax/format/gettext and existing
admin-render regression; React typecheck, affected views/filters tests, i18n/design
audits and normal hooks. Tests must cover none versus false/null, no-action with
reached threshold, evaluation error, queued/failed/uncertain/suppressed mail, completed
warning without delivery claim, physical-stop proof/shared ID, disclosure content,
active hidden filters, unchanged offset/as_of/Refresh and admin/member gating.
Use existing fixtures; no new DB/API/VM/browser campaign. Commit complete changes,
then affected independent review; root releases final finite browser verification
and later redeployment. No source edits before this sufficient brief is released.

Final screenshots: both pages in both EN/CS at1280 and390, collapsed default plus
one opened Details per interface. Check actual geometry: PHP content/aside bounds
stay side-by-side at desktop, no table/entry extends past content; React default
rows are materially shorter and no overview/History horizontal page overflow.
Exercise sidebar/tab links, one expanded row, advanced filter persistence and
page/refresh once using existing fixture flows. Preserve source-bound evidence;
fixtures do not claim deployed behavior. Current deployed8846/ef6 stays unchanged
until root accepts corrected final inputs and releases owner0's later update.

KB impact is admin-only. Existing registered incident controls are per-VPS/member
`vps.incidents.menu` and `vps.incident-reports.menu` in incident_policy.forms.php;
their routes/labels/landmarks remain unchanged. Preserve admin IDs while moving
navigation. Root allocates any required final backend pin/contract check once after
publication; assess only reported factual drift. No member page rewrite, canonical
media recapture/full-page fetch/wiki publication follows from these scoped changes.
No migrations/protocol/API change; old/new backend clients remain compatible.
Rollback is presentation-source selection through the existing deployment procedure,
not state restoration; preserve the new Mailpit persistence/recovery contract.

## Nov24 Mailpit preservation — required before services activation

Root accepted this necessary runtime preservation step within the existing demo
update. Owner0 owns execution; architect made read-only observations only. The
226-build admission is independent; services activation remains held until this
transition succeeds. No provider/source change, cluster/session stop/reset, host
change, new mail send or reimport is included.

**Proven current boundary.** Captured candidate graph changes the mailer container
and restart triggers but retains the identical Mailpit1.33.1 binary
`/nix/store/cgipyklpzpmr7l3pzjrwcslmjw7i19rj-mailpit-1.33.1/bin/mailpit`.
Nov24 coordinated read-only observation found PID312, no database flag/MP_DATABASE,
empty StateDirectory, and
`/tmp/mailpit-1795442529536356826.db` with WAL/SHM on tmpfs. The current15 captures
remain protected; their API JSON is not a native recovery backup. Mailpit1.33.1
`internal/storage/database.go` creates a temporary database when no path is supplied
and deletes it on SIGTERM/Close. An ordinary restart cannot preserve it as-is.

The same read confirmed container `/` is persistent ext4
`/dev/sda[/var/lib/nixos-containers/mailer]`. The captured start script uses
systemd-nspawn `-D` on that retained root without ephemeral flags. Only `/tmp` is
volatile. `/etc/systemd/system` points to `/etc/static/systemd/system`; do not edit
it. `systemd-analyze unit-paths` explicitly includes
`/usr/local/lib/systemd/system`; `/usr` is an ordinary persistent directory and
`/usr/local` is absent. This permits an ordinary local drop-in and database in
persistent root. No existing persistent Mailpit binding already solves the issue.

**Finite owner0 execution (root releases this boundary).**

1. Complete application builds first. Under the existing exclusive runtime window,
   recheck the exact Mailpit process/executable/database paths and same persistent
   root; abort on drift. Use the resident SQLite tool, for example
   `/nix/store/6slrxch2idk9v1hz54yf8bw8sknpxwhc-sqlite-3.53.3-bin/bin/sqlite3`.
   If absent in services, ordinary Nix-copy this existing closure using the established
   provider SSH target/options; the mailer shares the services Nix store. No tool build
   or environment restoration. Keep private files0700/0600 and no credential output.
2. Take a fresh read-only API identity/content baseline covering all current captures,
   including the protected15. Prevent operator/API mailbox mutations for the short
   transition. Gracefully stop only the mailer container's
   `vpsadmin-nodectld.service` through ordinary `nixos-container run mailer -- systemctl
   stop vpsadmin-nodectld.service`; establish no active/uncertain SMTP delivery before
   taking the final snapshot. Leave API/scheduler, RabbitMQ and node1 running. Queued
   mail stays queued, never purge/ack/replay it manually. No new login/test mail during
   the gap. If graceful completion is uncertain, reconcile it before proceeding.
3. While old Mailpit still runs, use SQLite's online backup API, via
   `sqlite3 -readonly "$ACTUAL_DB" ".backup '$NEW_PRIVATE_RECOVERY_FILE'"` inside
   the mailer. Require a new, nonexistent destination under persistent `/var/lib`,
   not /tmp. This copies a consistent native database including WAL-backed commits;
   do not copy only the live `.db`, concatenate WAL, use immutable=1, or dump/ingest
   messages. Validate `PRAGMA quick_check` returns only `ok`, capture full native
   schema/content digests and expected mailbox IDs/count, and compare the API baseline
   again while deliveries are quiesced. Retain an additional verified private recovery
   copy outside the container using the existing owner0 transfer mechanism. Never
   print raw SQL/bodies publicly. Any missing/changed protected record stops the step.
4. Require `/var/lib/mailpit/mailpit.db` and the chosen drop-in to be absent (or
   already exactly this proved transition on retry); reject symlinks/collisions.
   Install a byte-identical copy of the verified snapshot as
   `/var/lib/mailpit/mailpit.db`, root-owned0700 directory/0600 file, preserving the
   separate immutable recovery copy. Old process still uses its temporary file.
   Create ordinary `/usr/local/lib/systemd/system/mailpit.service.d/50-preserved-database.conf`
   with exactly:

   ```ini
   [Service]
   Environment=MP_DATABASE=/var/lib/mailpit/mailpit.db
   ```

   Run `systemctl daemon-reload` inside mailer, then verify DropInPaths, selected
   MP_DATABASE, unchanged ExecStart/binary/SMTP/listen options and user. Do not replace
   the managed unit or override ExecStart. Mailpit1.33.1 `cmd/root.go:202–203`
   explicitly reads MP_DATABASE. Snapshot+recovery validation must precede restart.
5. Restart only `mailpit.service` normally. Its old temporary DB may now be deleted;
   the verified recovery copies are authoritative. Prove new process opens exactly
   `/var/lib/mailpit/mailpit.db` (and its own WAL), same binary, healthy existing HTTP/
   SMTP listeners, and every protected capture retains its ID, received time, flags,
   tags, headers, bodies and attachments. Compare native contents with the snapshot
   before allowing new mail. No message ingest or replacement IDs. Then restart the
   exact previously-active mailer `vpsadmin-nodectld.service`, verify healthy queue
   processing, and account for legitimate queued arrivals separately. Do not send a
   test message. If any proof fails, keep the producer stopped and report exact effects
   to root; do not erase the new DB or overwrite a database that has newer messages.
6. Root may then release the existing ordinary services update. Before/after it,
   retain native backup, drop-in digest, mount/path/binary proof and original capture
   subset. Recheck that the persistent path/drop-in survived and all original captures
   remain; normal new arrivals may extend the set. Preserve the source freeze, other
   data, templates and acceptance/recovery requirements below.

**Why this survives and what it does not promise.** This candidate preserves the
services disk/container-root location and does not configure/remove `/usr/local` or
`/var/lib/mailpit`; normal NixOS `/etc` switching does not own this local unit-search
path. The container restart therefore reuses both the database and drop-in. Later
ordinary updates with the same retained root/search-path contract retain them too;
verify selected Environment/DropInPaths at each update and do not silently allow a
new declarative override to retarget the DB. This is recorded per-demo operational
state, not a reproducible setting in current Nix sources. A clean recreation or a
future declarative persistence feature would need a separately scoped committed
configuration/provider change; neither is necessary or authorized for this retained
update. Do not introduce an auxiliary supervisor or claim a source-only rebuild
recreates this local state.

**Failure/recovery.** Before Mailpit restart, leave the old process/data intact and
resume the previously-active producer only after reconciling effects. After restart,
retain all current files/backups; prefer correcting the local selection forward.
A restore requires stopped Mailpit and producer, proof that no newer captures would
be lost, and root disposition; never replace a live WAL database or remove the
persistent selection to fall back to an empty temporary DB. The same-version native
backup preserves Mailpit IDs and metadata. The prior70-message waiver does not apply.
This is a service-level transition only and leaves the session/cluster running.

Evidence: nov24-dev-cluster-update/{bounded-build-classification.json,
graph-layout-and-build-names.json,private/graph.stdout}; Nov23
mailpit-retained-db-observation.json is historical. Current provider
`nix/test.nix:1921–1935`, selected Mailpit1.33.1
[database.go](https://github.com/axllent/mailpit/blob/v1.33.1/internal/storage/database.go)
and [root.go](https://github.com/axllent/mailpit/blob/v1.33.1/cmd/root.go).
No backup, SQL, copy, stop, configuration write or restart was executed by architect.

## Nov24 dev-cluster update — execution brief for implementer0

**Authorized scope.** The user's “deploy the dev cluster when done, so that I can
see the UI changes” authorizes a data-preserving update of this session's existing
demo after root accepts the final React fixes/checks. Owner0 owns one complete
preparation/build/update/live-acceptance package; root releases execution and owns
consequential recovery. This is not default integration, npm/production/wiki
publication, host/profile activation, or cluster/session lifecycle authority.
Retained roster44: architect0 Astra/xhigh; owner0 and owner2 Sol/xhigh, all
workspace_write, execution full_access. No settings changed.

**Observed baseline and tooling.** Read-only Nov24 status returned running
PID2458866, single topology, bridge/br0, ready. Fresh applied-config.json has
pending=null and React source label25c8; result-config points to
`/nix/store/9grpiq8nqyv0y4yakgzxf6kkhhnwr0z1-vpsadmin-devcluster-2026-10-30-oomd-abuse-policy-services.json`.
Fresh guest readlinks confirm services
`/nix/store/yccply7y5slim1p16fgy9195c3mld4z6-nixos-system-vpsadmin-services-26.05pre-git`
and node1
`/nix/store/zv0wss6qmc5s1ip995ycf66nb5b61pr1-vpsadminos-system-dev-node1-26.05.git.ccd51ed`.
Active API/supervisor WorkingDirectory still identifies backend
0d1db93cd0d38b77f1e29c40ddd71b45581ecfff. Applied labels are not a fresh served
frontend/template proof: actual React25c8/frontend/BFF and templates64665 readback
remain historical receipts until owner0's admission/readback. PHP uses the live
backend worktree with packaged vendor dependencies, so its files can advance
independently of the active API. Do not call this mixed state the final deployment.

Selected generic runtime is
`/nix/store/waw0fw7vmz4z0f5ym5cjh8p4ij0xqq70-dev-workspace-0.2.0`;
provider is
`/nix/store/74l17zczj71cj3hanx44sb4asivpa18a-vpsfree-dev-workspace-tools-0.1.0`.
Use stable `vpsadmin-devcluster`, whose current README/bin/flake were inspected,
not the old k3/xq8 helper. This provider supports ordinary `update SLUG services`
with retained applied descriptors, pending-before-copy and exact guest promotion.
It retains host QEMU/virtiofsd, /mnt/vpsadminos export, preserved root image and
all non-target descriptors. It switches services without reboot, then performs
normal API restart and node refresh (including nodectld restart); it does not
update the node system. The existing session-owned cluster/bridge ownership and
provider mutation locks are sufficient for this guest-only operation. No
configured aitherdev machine claim is needed for these steps. Any host/profile,
bridge, or configured physical-machine change is outside this package and would
need root's separately prepared claim/authority; never bypass an ownership refusal.

**Freeze and admission.** Before building, owner0 obtains root's exact accepted
final React commit/tree (hard prerequisite; current c27d is not the final fix
handoff), and freezes relevant worktree writes through activation/readback.
Bind backend8846c22b20d805ee3d63718d9d23a5be5319b4bf/tree24623e460c686325fa88c5a59d5c2dfae1f8302a,
templates7af51cd6164fd5aad7633f39f6cf4e7ef64c18a7/treee1872cbc645947495160b0b6a13a56cb5b2689d4,
and final React's checked SDK archive9cba/public b619 exact full hashes from the
client handoff. Development artifacts are allowed here; registry release remains
a separate merge requirement. No generated-client or SDK regeneration is needed.
Record actual config checkout baf73377af387a8ef1c90e20b17bb559fcd15c45 and its
selection scope: only the existing configuration export and incidentPolicyFile
are used, not production channels. Per-cluster config SHA remains
c78bbe075305acedcfa5d883454910e4ce610722dff4056f640f72e5302c900b;
its incident declaration still hashes
8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714
(sole trusted OOM3/10). Preserve it and all overrides/recipients/seed values.
Keep OS52eb4de029f385c3e2d1b614d9b6ff32bbfb29bf and packaged status
f783d045ac49a0ae9e8501a8f9a38d0523177b9e; no local status/client injection.
The current provider still pins f783. HaveAPI, web and legacy template alias
paths are absent; do not create them. Preserve recorded node/runner/kernel/disk
and mount identities. No migration/core-schema/plugin-migration diff exists
between deployed0d1 and8846; the API schema7e2a is separately unchanged since
final export. Preserve the original migration lineage and all old/deployed refs.

Owner0 reuses `nov19-demo-refresh-execution/nov23-status-f783/services/evaluation-plan.json`
with current provider path, exact final revisions, unchanged source selections,
and a fresh private applied configuration context for target services. Inspect
one complete dependency graph and dry-run before realizing the selected services
config; retain old/new input/derivation/system/frontend/BFF provenance. Use normal
Nix source overrides (backend, both OS inputs, React), no lock edits, private
provider helpers or source shims. The current public update recomputes the build,
so its frozen inputs/environment must match admission. Any IFD needed to assemble
source is a real build and must be bounded/recorded. Keep one job/core, reserve
current guests'16GiB plus their16GiB shared-memory allocation and actual build
headroom; inspect free memory/disk before starting. Expected scope is one frontend/
BFF/backend/dependency build and services configuration assembly, followed by one
update, not tests or a VM campaign. Historical47 small builds/11fetches and307s
update are sizing references only, not a fresh cost claim. Stop before activation
for kernel/root-image/node/host rebuild, unrelated input drift, topology/export
change, provider repair, material tool restoration or a materially larger build.
Report concrete missing work to root; do not silently broaden. Reassess a build
still doing substantial work after about15min. Use the installed monitor procedure
for uncertain native work; owner0 retains effects and may use its visible fallback.

**Preservation, activation and templates.** Take a fresh private consistent DB
recovery backup and bounded pre-state before activation using the established
helpers. Preserve all existing report/evaluation/action/MailLog records and saved
facts (especially22/20 and25–29), owners/limits/preferences, snapshots, stopped
VPS state and disks, credentials/signing keys, BFF sessions, Mailpit captures and
exports. The last saved checkpoint was29reports/23evaluations/6actions/67MailLogs;
it is not today's count. Current captures remain protected; the old70-capture
waiver does not extend to newer mail. Compare baseline subsets after normal seed/
refresh, allowing only identified operational/authentication effects. Do not
restore libnodectld's isolated ignored gem cache, change tracked locks, re-seed
fixtures manually, rotate secrets, rematch incidents or generate test violations.

Run exactly the ordinary `vpsadmin-devcluster update 2026-10-30-oomd-abuse-policy services`
with the admitted environment. It must complete copy, switch, refresh and
residency promotion with pending=null. Verify actual API/supervisor/database-setup,
scheduler/PHP/auth, served frontend and active BFF package paths and source bytes;
labels alone are insufficient. Confirm exact policy3/10 in the three packaged
contexts, retained node system/kernel/disks and healthy existing services.

The provider's optional template lookup is still `vpsfree-mail-templates`; it
will not automatically select registered `vpsfree-notification-templates7af`.
Root accepted the normal documented overlay composition: **do not reconcile
raw7af**. Its daily variant has HTML/subject only; direct reconciliation assigns
missing text_plain=nil and would omit the new backend daily text. Before activation,
prepare the immutable effective artifact with the existing
`pkgs.vpsadmin-notification-template-tools.mkEffectivePackage` constructor:
`{ vpsadminPackage = EXACT_8846_API_PACKAGE; plugins = EXACT_SELECTED_PLUGINS;
source = EXACT_7AF_SOURCE; mode = "overlay"; }`.
The authoritative constructor is backend8846
`packages/notification-templates/default.nix:53` (bundled API, missing plugin
templates, then site source overlay); its ordinary module call is
`nixos/modules/vpsadmin/api/default.nix:27–35`. This is a small copy/check assembly,
not a new template merger. Bind the actual API package,7af Git archive/hash, plugins,
effective store path and every resulting body. Compare against fresh stored template
metadata/variants before reconciliation; preserve site overrides and explain normal
fallback additions. Unexpected unrelated body drift stops before the mutation and
goes to root. The new daily HTML and actual8846 plain text must both be present.

After compatible API activation, copy the immutable effective artifact through
ordinary Nix copy/SSH and verify its body hashes. Read notifications.template_source
and current bodies; skip reconciliation only when the exact effective artifact is
already loaded. From actual API WorkingDirectory/User, use its packaged bundle with
RACK_ENV=production and
`vpsadmin:notification_templates:reconcile[EFFECTIVE_STORE_PATH,EFFECTIVE_STORE_PATH]`,
the module's normal source-ID convention. Record the composed source marker with
its8846+7af bindings rather than falsely labeling overlay bytes as raw7af.
Use the existing successful command pattern and corrected public readback helper
from `nov19-demo-refresh-execution/payload/guest-activate-forward.sh` and
`payload/template-proof-source.rb`; do not replay the old full script, its0d1
assertion or failed config-install/private-helper portion. Compare stored source,
metadata and all effective variant bodies, including new daily HTML and backend
text. Preserve recipients/preferences and existing MailLogs. This changes template
content/source only, sends no mail and requires no alias/provider modification.
If reconciliation succeeds but readback fails, inspect that effect; do not blindly
run it again. Normal daily scheduling remains; do not invoke mail_daily_report.

**Finite acceptance and recovery.** Reuse existing authenticated sessions where
possible; if fresh login is necessary, identify its ordinary auth/MailLog effects
separately. On both PHP and React, inspect admin Incidents Overview/Reports/History,
current matched stopped VPS rows, one sort/filter/page/refresh, truthful history
and report22 saved facts/deep link. Check one owner and one foreign/member denial
without changing accounts, ownership or policy. Inspect desktop and narrow layout
on the real served build, including cutoff-transition/long-table fixes; reuse final
local browser results, no browser campaign. Daily acceptance is loaded template/
producer source and a read-only render if available, not a sent report or historical
MailLog rewrite. Empty rolling24h activity is legitimate. Finish with preserved-data
comparison and exact current-system/served-source/applied-envelope proof. Leave
URLs running: https://webui.aitherdev.int.vpsfree.cz/ and
https://newadmin.aitherdev.int.vpsfree.cz/ (API/auth/Mailpit retain existing domains).
Keep credentials and private captures out of public output.

Retain prior systems, source graphs, configuration, backup and data receipts.
Before activation failure leaves the old runtime; after copy/switch/refresh failure
it may already have changed. Reconcile the exact native process and pending target,
then use the supported same-services-target forward retry under root disposition.
No automatic downgrade, DB restore, alternate target, pending-record edit,
start/stop/reset/recreate or maintenance recovery is authorized. There is no
new schema migration, but that alone does not authorize an old application/provider
rollback or restore over current data. Return the complete observed outcome and
any blocker; leave the session and cluster open.

Source contracts: selected provider README “Build candidates and retained boot
selections”, “Email”, “Runtime Updates”; bin/devcluster668–881,1457–1515;
flake.nix73–174; backend api/lib/vpsadmin/api/tasks/vpsadmin.rake51–70.
Historical recovery/preservation sources: nov19-demo-refresh-preparation/refresh-plan.md,
nov19-demo-refresh-execution/nov23-status-f783/services/, and
nov23-restart-cs-example/{packet.txt,preservation-result.json,runtime-after.json}.
This addendum records design/read-only observations, not completed deployment.

## Nov24 implementation — admin Incidents and daily policy summary

**Sufficient execution contract; root releases packages.** User approved Incidents
→ Overview (default), Reports (existing), History in PHP and React, plus the daily
report. Baselines are clean backend 4062, React 4499 and templates 64665 as confirmed
by their owners. Build forward from these integrated commits; never amend/replay
merged history. Identity/roster 44 and retained architect settings verified. This
brief supersedes the Nov24 proposals below where it specifies the interface.
No policy-engine behavior, schema/migration, node/protocol, default integration,
registry publication, deployed runtime, recipient or lifecycle change is included.

### A. Frozen API and shared read projection

Add two top-level resources, avoiding collisions with existing policy-key Show:
`IncidentPolicyExposure` / `incident_policy_exposure.index` at
`GET /incident_policy_exposures`, and `IncidentPolicyEvaluation` /
`incident_policy_evaluation.index` at `GET /incident_policy_evaluations` (normal
API-version prefix). They expose only Index; no Show/write/reset/retry actions.
Existing registry, nested policy/evaluation and report resources remain unchanged.
Both require exactly `current_user.role == :admin`, including metadata capability
visibility; members/support cannot call them or gain data through a known ID/filter.
Use ordinary HaveAPI resource fields for live Exposure VPS/User/Node references
and typed scalars for derived facts. No raw JSON snapshots, source text, selector,
recipient, private error or MailLog body.

Both use normal HaveAPI object-list envelopes and global metadata. Remove
`from_id`; inputs are `offset` integer>=0 default 0 and `limit` integer1..100
default 25. Always supply metadata `total_count`, `offset`, `limit`, nullable
`next_offset`, `as_of` and `read_at`; History also supplies nullable `from`,`to`.
`next_offset = offset + returned_count` only when more rows remain. Exact counts
and page membership use the same filtered relation. Use small endpoint-local
PHP page links/React offset state; do not change shared keyset/ID pagination.

`as_of` is an optional UTC datetime, default captured server now, normalized to
whole UTC seconds before querying and echoed exactly even for empty results. Reject future or more-than-24h-old cutoffs; UI uses returned cutoff
for subsequent pages/filter/sort changes, Refresh obtains a new cutoff. `read_at`
is this request's captured time. Cutoff fixes event-window arithmetic and excludes
evaluations recorded after it; it does NOT freeze settings/ownership/action state
between HTTP requests. State this in docs/help; current restrictions/outcomes are
read now. Capture registry/config once and materialize each collection consistently:
use an ordinary read snapshot where available, or select total/page/count/limit/order
facts in one SQL statement and carry them unchanged through batched presentation.
Do not obtain total and sorted row values from inconsistent READ-COMMITTED reads
or recompute selected values later. DailyReport already runs inside fire2's write
transaction: preserve that transaction and use the single-statement collection
projection there; do not change global isolation, add a connection or start a
nested isolation transaction. The three daily collections share the cutoff, not
a promise of one immutable database-wide historical image. No locks, selectors,
callbacks, reconciliation or persistence on a GET, and no retained snapshot/token
framework. Concurrent transfer/configuration changes can change later pages;
Refresh reanchors the view.

**Exposure identity and membership.** One row per `(vps_id, policy_key)`; string
`id` is `vps_id:policy_key`. All active policy keys and active-lifecycle VPSes with
`count_30d > 0` qualify; physically stopped VPSes remain included. Do not require
owner active to display a row. Counts use saved `matched=true` evaluations with
`evaluated_at <= as_of`, original report owner equal to current VPS owner, the
existing virtual successful-Chown/current accounting epoch, and detected time in
`(as_of−7d,as_of]` / `(as_of−30d,as_of]`. Generated notices never count. A matched
configuration-error evaluation can count; no match is inferred from a settings
row, codename or today's selector. Keep existing per-VPS reads/engine semantics
unchanged; add optional cutoff support only to read helpers where needed.

Exposure filters: optional exact `policy_key` (active key); ordinary HaveAPI
resource parameters `vps` (VPS), `user` (current User), `node` (Node), accepting
normal resource IDs and framework validation; `status` = clear/near_limit/warning/stop_threshold/invalid;
`effective_mode` = observe/notify/enforce; `stop_enforced` boolean. Unknown keys or
choices fail validation. Default has no threshold filter: **All with current matches**.
Aged-out failures are available through History/outstanding, not mislabeled as matches.

Exposure output (all fields required unless marked nullable):
- `id` string; ordinary Resource attributes `vps` (VPS, value_label hostname),
  `user` (User, value_label login), `node` (Node, value_label domain_name).
  Return normal partial references with id plus that label, unresolved metadata
  and path params; no automatic full includes. `policy_key`, `label` strings;
  `owner_active`, `transfer_pending` booleans. No parallel API vps_id/user_id/node_id
  or hostname/user_login/node_name fields. Row identity still uses vps.id and key;
  sort names vps_id/user_login mean these referenced values, unchanged.
- `count_7d`, `count_30d`, `warning_period_days=7`, `stop_period_days=30` integers;
  `warning_limit`, `stop_limit`, `warning_remaining`, `stop_remaining` nullable integers;
  `configuration_valid` boolean; nullable `status` clear/near_limit/warning/stop_threshold.
- `global_mode` string; nullable `effective_mode`, `warning_permitted`, `stop_enforced`;
  nullable `last_incident_at`, `last_warning_at`, `next_warning_allowed_at`,
  `last_stop_at`, `next_stop_allowed_at`, `accounting_since` datetimes.
- `outstanding_stop_state` none/pending/failed/uncertain and nullable
  `outstanding_stop_action_id`, `outstanding_stop_chain_id` integers.
- Nullable `latest_action_id`, `latest_action_chain_id`, `latest_notice_report_id`
  integers; `latest_action_kind` warning/stop, `latest_action_state`,
  `latest_mail_state` strings; `latest_stop_completed_at` datetime.

Limits/modes/status use existing VpsIncidentSummary/effective_result rules:
VPS→global→declared overrides, >= thresholds, stop precedence, existing ceil(80%)
near-limit. Remaining is max(limit−count,0), null if invalid. Do not invent a
risk score. `warning_permitted` means effective mode is notify/enforce and declared
actions are not suppressed; `stop_enforced` keeps its existing mode/exemption/
suppression meaning. Neither promises an eligible next action. Display owner/
transfer/outstanding/cooldown restrictions as separate facts. Warning cooldown is
7 days from first queue per policy, stop cooldown 24h from confirmed stop per VPS;
use existing virtual transfer/stop completion read semantics. Empty nullable dates
mean no recorded boundary. New eligible source incidents, not these dates, trigger
actions. Latest per-policy action is highest ID within current owner/epoch; shared
outstanding stop deliberately remains VPS-wide, including old-owner work.

Order inputs: `sort` = severity(default),vps_id,user_login,policy_key,count_7d,
count_30d,warning_remaining,stop_remaining,last_incident_at; `direction` asc/desc
(default desc for severity, asc otherwise). Nulls last. Severity ranks descending:
failed/uncertain shared stop 5, invalid config 4, pending shared stop 3, stop threshold 2,
warning 1, near_limit 0, clear −1. Remaining ties use min(warning_remaining,
stop_remaining) ascending, then last_incident_at descending; every order ends with
vps_id ascending + binary policy_key ascending. Reverse only primary sort when
requested. No client/page-only sorting. SQL builds a quoted/bound per-active-policy
UNION ALL of the existing count/override/epoch logic, then filters, counts, orders
and LIMIT/OFFSET across pairs before Ruby enrichment. Do not load/sort all VPSes
in Ruby. Reuse/batch VpsIncidentSummary and page associations once per unique VPS;
query count may scale with active policies, never with rows. Return the selected
count/limit facts consistently with ordering; no separate client calculations.


**Live-reference correction (root clarification).** Primitive references were a
projection convenience, not a necessary compatibility constraint. Use the existing
HaveAPI Resource declaration/partial-reference contract without a new model or
adapter. The normal Hash projection can carry already-selected id/label/reference
metadata; batch any required associations once. Do not invoke per-row Show requests
or AR association preparation that re-queries each referenced object. Exposure is
admin-only and current VPS/owner/node are real live references. History intentionally
keeps raw original IDs/nullable current labels: deleted or retired records must not
vanish or become a different owner's history. Derived action/chain IDs remain raw
retained evidence references where absence is meaningful. Daily payload retains its
flat vps_id/user_id/node_id and hostname/user_login/node_name fields for the existing
prepared-template contract; API reference formatting is a thin projection of the
same authoritative data, not a separate evaluator or duplicate model. These choices
follow existing Resource parameter declarations (e.g. node_sysctl_change.rb) and
HaveAPI's Hash/Resource support; sorting/count/time semantics are unchanged.

**History identity and time.** One row per saved evaluation (`id` integer), with
its at-most-one policy action attached. No synthetic rows for notices or each
mutable transition. Original report owner/VPS IDs remain historical truth after
transfer/deletion; current names are nullable conveniences. Retired keys remain.
Filters: optional `policy_key` (retired allowed), `vps_id`, `user_id` (original
owner); these History input IDs remain integer filters so deleted/nonresolvable
original identities can still be searched. `decision` none/warning/stop,
`action_kind` warning/stop, `action_state` and `mail_state`; `scope` violations(default)/matched/all/outstanding. Violations
means a complete saved threshold is reached OR an action exists; matched means
saved matched=true; all includes safe skipped/error/audit outcomes. Outstanding
means action.state != suppressed and either action state or mail state is one of
pending/queued/failed/uncertain. It intentionally has no lower date bound and
ignores `from`/`to` (return null; UI disables period controls); it exposes current
unresolved work regardless of age. All scopes exclude evaluated_at after as_of.
Other scopes use `from <= evaluated_at < to`, default `[as_of−30d,as_of)`, maximum
366-day span, valid from<to<=as_of. Select older history by changing this range,
not by abusing the recent as_of cutoff. History ordering is fixed to `evaluated_at`,
then evaluation ID; its only ordering input is `direction` asc/desc (default desc),
applied to both fields. There is no History `sort` parameter or sort-key selector;
capability checks require `direction`, not `sort`. Exposure retains its separate
multi-key `sort` input. Returned current action outcome may
postdate the evaluation period; label it separately and include timestamps.

History output: `id`, `incident_report_id`, nullable `vps_id`,`user_id`, nullable
`hostname`,`user_login`; `policy_key`,`label`,`evaluated_at`, nullable `detected_at`;
`matched` nullable boolean; `state` recorded/skipped/error/audit_only; periods 7/30;
nullable saved counts/limits/effective_mode/stop_enforced/threshold_status;
`threshold_status` uses clear/near_limit/warning/stop_threshold with saved values,
null for missing/invalid facts. `decision` none/warning/stop. Attached nullable `action_id`,`action_kind`,
`action_state`,`action_created_at`,`action_updated_at`,`transaction_chain_id`,
`physical_stop_action_id`,`stop_completed_at`,`notice_report_id`,`mail_state`,
`mail_queued_at`,`mail_finished_at`. Integer IDs, native datetimes, string enums. Action states are
pending/queued/failed/uncertain/completed/suppressed; mail states are
pending/queued/sent/failed/uncertain/suppressed, matching existing stored values.
No raw snapshot or error payload. `physical_stop_action_id` is stop_owner_action_id
or own action ID for stops, null for warnings. Policy rows sharing it are labelled
as one shared stop; aggregate physical counts use DISTINCT identity/chain, never
row count. `stop_completed_at` requires confirmed physical completion, not merely
warning action.state=completed. Mail queue comes from retained current MailLog
created_at; finish from its actual finished Send transaction, nullable if unknown.
Mail state sent means SMTP acceptance; suppressed/queued/failed/uncertain are not
sent. A completed stop may have failed mail. Preserve immutable evaluation values;
never recompute saved counts/limits from current config. Missing old facts stay
null, not zero or inferred success. There is no exhaustive transition/retry audit.

### B. Frozen daily-template payload (owner1 → owner3)

Add optional registered `incident_policy_summary: Hash` to DailyReport#vars(now),
using the same shared projection at that now (native UTC Time values). Exact shape:
`{ as_of:, period_start: now−24h, period_end: now, overview:, activity:, outstanding: }`.
Each collection is `{ total_count: Integer, rows: Array, omitted_count: Integer,
url: String|nil }`, capped at 25 rows AFTER server sorting. Missing entire payload
means older producer: omit the new sections. Present empty collections say no
current matches / no recorded activity / no outstanding actions; never show empty
headings. Rows use the complete Exposure/History facts above (Exposure uses the flat live
reference fields specified in the correction, not API Resource objects) plus prepared nullable
`vps_url`, `report_url`, `policy_url`, `transaction_url`; ERB only escapes/formats.
`overview.url` is the full admin Overview; history collections link to History with
appropriate filters, with an honest historical-state limitation rather than a
promise to reproduce an immutable email. Invalid/empty base_url yields null links.

`overview` = All with current matches, severity descending. `outstanding` = History
outstanding, newest evaluation first; identify old unresolved work as current.
`activity` = one History row per evaluation with a decision/threshold or action
and at least one retained relevant timestamp in `[period_start,period_end)`:
evaluated_at; stop_completed_at; current mail_queued_at/mail_finished_at; or
`action_updated_at` when current action/mail state is failed/uncertain. Add
`activity_at` (greatest qualifying timestamp) and `activity_basis` one of evaluation,
stop_completed,mail_queued,mail_finished,action_updated; ties prefer stop_completed,
mail_finished,mail_queued,evaluation,action_updated. Sort activity_at desc, ID desc.
The final basis means “failure/uncertainty last updated”, not first failure time.
Deduplicate evaluation IDs; no union duplicates/multiple physical-stop claim.
This is recorded activity plus current outcomes, not an exhaustive event log.
Later retries can replace state/mail pointers; disclose that existing history limit.
Do not enumerate intermediate failures from generic updated_at. The new section
retains rolling 24h semantics, not “since previous successful delivery”.

HTML and plain text show VPS/owner, policy, counts/limits/remaining, restrictions,
then compact action/mail outcomes with dates and links. Preserve every existing
report section/layout/recipient; add bounded sections near Incident reports.
Show shown/total/omitted explicitly whenever capped. Current recipients are configured
admin-report To/Cc/Bcc, not automatically all admin accounts; no recipient query,
new address or mail send in implementation checks. No new template language matrix;
existing daily English HTML and built-in English plain text remain equivalent.

### C. UI routes, capability boundary and package ownership

PHP: add an admin-only Incidents menu target `?page=incidents&action=overview`.
`action=overview` is the admin no-action default, `action=history` is new, and
`action=list` remains Reports with all existing filters/deep links. show/new and
per-VPS URLs/labels/doc IDs remain unchanged. Members/support retain their prior
navigation/routes. Admin tabs Overview/Reports/History appear only in the admin
context; unavailable new capability shows unavailable feedback without replacing
existing Reports. No per-VPS requests or shared paginator changes.

React: admin Incidents entry targets `/admin/incidents/overview`; admin bare
`/admin/incidents` remains a compatibility Reports path so old list/filter links
retain meaning. New `/admin/incidents/history`, optional canonical Reports alias
`/admin/incidents/reports`; existing `/admin/incidents/new`, `/:incidentId` and
all `/app/incidents`/per-VPS paths remain. New-entry default is Overview. Tabs retain
active filter/query state locally in URL; changing filters resets offset, Refresh
resets as_of. Prefer this compatibility redirect/alias over reinterpreting old URLs.
API capability checks must cover both new authorized Index actions and required
fields/meta before calls. Admin role plus capability; no client-generated SDK or
raw HTTP fallback, no hardcoded policy key. Existing SDK calls remain unchanged.

- **Owner1/backend**: shared projection under `api/models/` or `api/lib/vpsadmin/api/`,
  two resource files, bounded optional read-helper changes, daily producer/template
  registry/default text, API locales and focused specs; docs/incident-escalation.md.
  Own any necessary API topic/CI runtime selection amendments and default text render
  fixture. All engine mutators/schema/migrations unchanged. Base/Git prep complete;
  root serializes commit/index windows with owner4, source edits are disjoint.
- **Owner4/PHP**: webui/public/index.php, pages/page_incidents.php, new scoped admin
  forms (include from existing entry), relevant existing forms only for tabs,
  PHP CS/EN catalogs and focused PHP/render tests. Preserve member controls and
  avoid unrelated report redesign. Contract A sufficient now; root releases.
- **Owner2/React**: admin nav/routes, scoped overview/history components, typed
  API adapters/hooks, CS/EN strings, focused tests, REQ-051/design/work-log/inventory.
  Keep colleague PR307 experiment and shared keyset hook untouched. Layout/fixture
  prep is independent; executable new API calls depend on owner0 generated SDK.
- **Owner3/site template**: only daily HTML and its ordinary render fixtures/checks
  and concise template docs if useful. Contract B sufficient now; no producer/query
  code or recipient changes. Render missing/empty/capped/full states and both known
  success and failed/uncertain/suppressed outcomes. Owner1/3 share synthetic payload.
- **Owner1/export producer**: sole owner of the final supported export from the clean
  committed backend interface and its own NEW ordinary disposable fixture DB. Retain
  raw schema/provenance/tooling lock unchanged and hand the immutable bundle to owner0;
  owner0 does not launch a second API export or reuse the test database.
- **Owner0/clients**: consume owner1's immutable final export and regenerate Go/Rust/TS
  with exact existing tooling and normal focused checks. Preserve handwritten
  files/old release provenance. Hand immutable TS candidate to owner2; SDK source
  synchronization requires no release. Prepare candidate archive as needed; compatible
  registry publication remains a separate authority and React premerge prerequisite.
  No new npm publication/default integration is authorized by this implementation.

### D. Quick acceptance, docs and compatibility

Use declared environments/normal hooks and resident tooling first. Owner1 may run
normal focused RSpec in a NEW disposable MariaDB instance through existing automatic
harness; reject inherited DATABASE_URL/config/database.yml/test/DB connection overrides
before launch. Each necessary full/core RSpec process and the final export gets its
own fresh ordinary fixture/database; no reuse between processes and no shared demo DB.
Reuse retained working native environment only with
explicit actual dependency identity; stop material install/ABI restoration/system build
rather than promoting old evidence. Run changed projection/resource/summary/daily examples
as a bounded batch, with syntax/RuboCop and source/topic checks appropriate to changed
paths. Core/full coverage is required for new resources; source topic membership remains
exact once. A batch exceeding about 5 minutes triggers scope/environment reassessment,
not an automatic pass or a repeated full suite. No VM/integration/CI-watch campaign.

Meaningful cases: multiple policies per VPS spanning page boundaries; sort/filter/count
parity and deterministic ties; zero/one/below-limit/at-limit/expired/future/late events;
>=7/30 boundaries and fixed as_of across pages; transfer away/back and virtual Chown;
stopped VPS included; invalid settings count with null limits; mode/exemption/cooldown
facts without fake eligibility; retired history/original owner/deleted associations;
admin success/member/support denial; no selector/mutation/mail on reads; batched query
count independent of VPS count; old-action completion in period; shared-stop dedupe;
SMTP/suppressed/failed/uncertain distinction; capped/empty/older-payload rendering and
HTML escaping. PHP focused regression + changed syntax/format/catalog checks; React
pinned typecheck and focused adapter/component/route/i18n tests, relevant doc audits.
Owner3 uses retained render/check route, no fullflake build if outside quick boundary.
Rendered local synthetic desktop/mobile evidence and new UI browser behavior remain
explicit acceptance items; no VM/capture campaign is silently launched to obtain them.
Root resolves any missing mandatory check environment before final readiness; no bypass.

KB assessment is narrow: registered `vps.incidents.menu` and
`vps.incident-reports.menu` live in webui/forms/incident_policy.forms.php and feed
`vps.incidents.open`/`vps.incident-reports.open` for CS navody:vps:incidenty and EN
manuals:vps:incidents. Preserve their labels/routes/intent/semantic IDs. Neither
control currently binds a capture. New admin-only entry/tabs do not by themselves
change these member pages or mandate six existing media recaptures. After final
source, assess exact changed controls/capture bindings and run the source contract
with current pins when allocated; any real member drift names its exact page/concept.
No production full-page fetch, media/VM run or wiki write from this brief.

Backend projection/API and daily producer precede their consumers; guarded old/new
payloads and API capabilities permit staggered rollout. Generated clients and later
TS registry release remain explicit cross-repo dependencies. No changes to Terraform,
HaveAPI generator, nodectld, OS/kernel, scheduler or configuration pins are expected.
Rollback removes new UI/projection/template sections while preserving all reports,
evaluations/actions and old API routes. Source publication/normal final independent
review follows focused quick checks; deployments and merges require separate scope.
Root applies final user-facing prose pass before commits and owns acceptance/tracking.

## Nov24 proposal extension — incident policies in the daily report

The user also wants the overview in the daily report. Extend the proposal only:
reuse the same authoritative backend read projection for UI and mail, passing a
single generation time to its current-count/limit/cooldown calculations. Add a
compact **All with current matches** table across policies and a separate
recorded-actions section beside the existing incident content. Keep the current
report layout, content and recipient configuration. If rows are capped, state
“showing N of M”, keep severity ordering and link to the authenticated full view;
do not silently reduce the default to only near-threshold VPSes.

Existing pipeline at backend 4062 is the scheduled `vpsadmin:mail_daily_report`
task → `Tasks::Mail#daily_report` → `TransactionChains::Mail::DailyReport` →
`MailTemplate.send_mail!` and the ordinary mail transaction. The configured Nix
default is 09:00; no live schedule was checked. Producer `vars(now)` already
includes new incident reports selected by creation time, shown with detection
time in the site's template. It does not yet provide policy exposure/actions.
The accepted 64665 template is `templates/daily_report/email/en.html.erb`; backend
also supplies `api/notification_templates/templates/daily_report/email/en.text.erb`.

The generation cutoff is `Time.now.utc`; existing dates are now−24h through now,
rendered in local time. This is a rolling reporting period, not a saved prior-run
or prior-success watermark. Keep explicit start/end/as-of labels. A literal
“since the previous successful report” guarantee across missed/delayed/repeated
runs would require additional durable checkpoint semantics and is outside this
small extension. Use the existing half-open report-period helper convention for
new event queries; retain policy counters' own 7/30-day rolling-window rules.

Show recorded warning/stop decisions created during the period and confirmed
stops by `completed_at`, including actions originating earlier. Warning mail
queue/SMTP-acceptance facts require their retained MailLog/transaction timestamps;
`action.state=completed` alone is insufficient (suppressed warning mail can also
complete the action). Keep requested, queued, suppressed, failed/uncertain and
confirmed outcomes separate, and deduplicate shared physical stops. Show current
outstanding failures even when older, explicitly labelled outstanding now.
Action `updated_at` is not a failure-transition log: retries can overwrite state
and the latest mail pointer. Existing records cannot promise an exhaustive list
of every failure/retry “since last report”; use timestamped recorded outcomes
where available and current unresolved state, with the same history limits as UI.

Privacy: this is intended as an admin report, but recipients are configured
MailRecipient To/Cc/Bcc addresses, not an automatic query of admin accounts.
The chain supplies no member user, and the daily template declares no per-user
mail role. Recipient management is admin-only; preserve its existing admin
mailing-list boundary and do not add member delivery or recipient discovery.
Include operator identifiers/counts/action links, not raw selectors, report
bodies, private errors or additional personal details. Actual recipient contents
and current deployed template bodies were not queried.

Lowest-scope future changes: shared backend projection consumed directly by
DailyReport and the proposed API; one additive template variable contract in
`api/models/mail_template.rb`; optional guarded sections in built-in text and
site HTML, escaping values and supporting older payloads. ERB only presents
prepared facts; it must not query, rematch or evaluate policy. Backend producer
and templates can roll independently with missing-data guards; old templates
ignore the added variables. No schema, node, scheduler or evaluator change is
needed for this bounded snapshot/recorded-outcome view. This proposal does not
authorize implementation, template reconciliation, tests, deployment or sending.

References: [producer and 24h cutoff](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/models/transaction_chains/mail/daily_report.rb#L13),
[existing incident section](https://github.com/vpsfreecz/vpsfree-notification-templates/blob/64665b3944da4ebf5045ef00f403e410ce88e3ad/templates/daily_report/email/en.html.erb#L772),
[configured recipient expansion](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/models/mail_template.rb#L115),
[actual action/mail reconciliation](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/models/incident_escalation.rb#L344).

## Nov24 proposal only — admin incident-policy overview

Source basis: accepted backend `4062a8da3314aa7b48170b0d6f441446bad9b207`
and React `4499f90fe11df0e4df6f23e5fa54829e2254ec1b`, matching inspected
local heads. This is a recommendation, with no implementation allocation or
new live/runtime verification. Session identity and roster44 were confirmed;
architect0 retains Astra/xhigh/workspace_write and execution full_access.

**Existing capability.** PHP and React already offer admin-wide VPS filters by
policy and clear/near-limit/warning/stop-threshold status. Per-VPS views show
counts, effective limits, modes, cooldown/action facts and report-history links.
Global reports can be filtered by saved policy membership, with evaluations
shown on report details. The missing piece is a cross-VPS table combining these
facts, plus a joined view of recorded decisions and outcomes. Current list
responses expose aggregate threshold indicators; detailed rows require the
nested per-VPS API, so calling it once per VPS would create an N+1 request pattern.

**Recommended Current view.** The user selected **All with current matches**:
all active/nondeleted VPS and active-policy pairs with currently counted saved
matches, including physically stopped VPSes and counts below near-limit status.
A policy selector and optional threshold filters narrow this cross-policy view;
the sole-policy case is naturally equivalent. Requiring one policy upfront would
be an implementation simplification, not a correctness constraint. Keep an
attention filter/history route for unresolved/failed/uncertain actions whose
counts have aged out, explicitly distinct from current matches. A configured
policy/override alone does not prove that a VPS has matched it.

Columns: VPS/hostname and owner; policy; warning count/limit and remaining in
7 days; stop count/limit and remaining in 30 days; threshold status; effective
mode and stop permission; relevant cooldown/blocking action; last matched
incident; latest warning-mail/stop outcome. Link to existing policy, report and
transaction details. Show “1 more to the warning threshold” or “threshold
reached”, without promising that the next report will cause an action. Existing
near-limit means ceil(80% of limit): at limit 3 it starts at 3, so explicit remaining
counts are useful even when the existing status filter does not flag 2/3.

Prioritize unresolved actions, reached thresholds and proximity to a threshold.
Filter by policy/status and owner/VPS, with server-side stable ordering and
pagination over VPS/policy pairs before enrichment, not sorting one browser page.
Return an as-of time. Recent matched activity is the default membership boundary;
an optional all-configured view must be labelled separately rather than inventing
matches. No percentage-only risk score or client-side matching/evaluator is needed.

**History view.** Provide paginated recorded evaluations/actions, initially a
bounded recent period, narrowed by owner/VPS/policy. Show source report/time,
saved counts/limits/matched flag/decision, action state, mail state and confirmed
stop/chain when present. Keep retired-policy history. A matched report, reached
threshold, warning decision, queued/SMTP-accepted mail, requested stop and confirmed
stop are distinct facts. Shared-policy followers must not look like separate
physical stops. Existing state supports this history, but not every intermediate
transition or the first instant a threshold crossed between evaluations.

**Smallest API/UI gap.** Add admin-only paginated read projections using existing
summary/count/override logic and saved evaluation/action/report associations.
`VpsIncidentSummary.policy_rows` already batches detailed policy rows. Select and
page the cross-policy relation on the server, then batch its detail; exact query
contract remains implementation work. A schema-free initial projection is
feasible; no new counter/event tables or matching engine is needed. Reuse the
same projection in PHP and React; retain the current settings editors. Admin
means the existing admin role, without expanding member/support visibility or
exposing selectors, recipients, private errors or new reset/retry/write controls.

Preserve saved-match/current-owner-epoch accounting, rolling windows and >=
thresholds. Modes, suppression, VPS stop exemption, outstanding actions and
revalidation can block effects. Warning cooldown is 7 days per policy from first
mail queue; confirmed-stop cooldown is 24 hours per VPS. Stop takes priority;
new eligible incidents trigger actions, while expiry alone does not. Counts can
fall as old reports expire. Current status must not overwrite saved decisions.

Future delivery would be additive API first, then PHP/React with capability and
generated-client compatibility assessed, including normal SDK publication if
new generated members are required. No node/kernel/protocol change or persisted
state rewrite is proposed; rollback can hide the view while retaining history.
Acceptance would cover cross-policy paging/sorting, count expiry, overrides and
cooldowns, unresolved actions, owner isolation and truthful history. No checks,
implementation, deployment or wider campaign are authorized by this proposal.

Source references:

- [Existing VPS filters and batched list loading](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/lib/vpsadmin/api/resources/vps.rb#L223), [PHP controls](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/webui/forms/incident_policy.forms.php#L105), and [React controls](https://github.com/vpsfreecz/vpsadmin-webui/blob/4499f90fe11df0e4df6f23e5fa54829e2254ec1b/src/pages/app/vps/VpsIncidentFilters.tsx#L27).
- [Saved membership, rolling counts, near-limit and batched policy rows](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/models/vps_incident_summary.rb#L21).
- [Nested policy detail API and permission boundary](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/lib/vpsadmin/api/resources/vps_incident_policy.rb#L34).
- [Saved report evaluations](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/lib/vpsadmin/api/resources/incident_report.rb#L181) and [action eligibility/reconciliation](https://github.com/vpsfreecz/vpsadmin/blob/4062a8da3314aa7b48170b0d6f441446bad9b207/api/models/incident_escalation.rb#L241).

## Nov23 confctl continuation — four small assemblies, no full shell

Root released owner3's minimal tool setup and existing configuration pin package.
The saved failed full-shell admission did not prove that required confctl needs a
material restore. Pinned d8ab source/package separates its Ruby3.4.9 gem runtime
from the repository's prepared Ruby3.4.12 hook environment; `mode=tools` keeps
confctl packaged and additionally runs Bundler bootstrap/install for the full shell.
No alternate retained executable exists. Exact runtime Ruby/source/Git/SSH/Nix/Bash
paths are resident; wrapper and its gem-union environment are absent.

One narrow public `source#confctl` dry-run now proves only four local assembly
outputs plus two substitutes,19.7KiB download/61.8KiB unpacked. The assemblies copy
Gemfile/lock, prepare buildEnv's Perl script, union resident gems/generate bin-stubs,
and create the public shell launcher. No constituent gem/compiler/system build is
in the plan. Substitute-only cannot finish the four tiny outputs; their ordinary
local assembly is within the user's quick scope and earlier admitted tool pattern.
Full nix-shell, optional shell tools and Bundler-install shellHook are unnecessary.

The complete exact argv/output/allowed-set contract is
[architect-confctl-plan.json](nov23-configuration-successor-alignment/architect-confctl-plan.json).
Owner3 substitutes only the two named cache paths with builds disabled, verifies
remaining work is a subset of those four assemblies, then assembles the exact
confctl drv offline with one job/core and substitution disabled. Stop extra
paths/derivations, missing cache, real compilation or material overrun (two-minute
setup bound); no restoration campaign. All plan commands remain unexecuted by
architect. The initial direct-drv dry-run found its saved drv missing and was not
usable; the successful public-output plan regenerated that metadata without builds.

Invoke the resulting exact `vcxb3…-confctl/bin/confctl` public channel command
under owner0's saved hook environment, retargeting only BUNDLE_GEMFILE to owner3's
own configuration Gemfile. Keep ordinary hooks/Nixfmt and config Ruby3.4.12 distinct
from the package's own Ruby3.4.9; do not hand-create a launcher or lock edit. Owner3
owns admission through existing4062 pin/consolidation/quick/publication completion.
No new source/review/permission gate or host/profile/default/runtime action follows
from this exception. Root accepts the finite setup and final configuration result.

## Nov23 backend default advance — sufficient owner1 rebase and consumer alignment

Root's fresh canonical observation (already fetched; not repeated here) advances
backend master from `c26465c0be452bbf5843d782a324dc82c122f28b` to
`628c17661cc4c9bbe7d566072305c7de95284794`. Inspecting only that local delta finds
one commit, `webui: update dependencies`: `webui/composer.lock` and
`webui/php-packages.nix`,11 insertions/11 deletions. Guzzle7.16.5 becomes7.17.0,
source/dist f61ba5ea0a55032a55ddbb72cab7d307c1043654 and matching generated Nix
archive/hash. Its tightened promises^2.6.2 and psr7^2.13.6 requirements are satisfied
by the unchanged locked2.6.2/2.13.6 packages. No feature-changed path overlaps;
no API/schema/migration/OS/Ruby/exporter/fixture or instruction change is present.
This is sufficient for immediate backend preparation, not a wider source audit.

**Owner1 complete package.** Exclusively own the registered backend feature's
source/index/rebase/normal-hook/publication window after root allocation. Preserve
accepted634d6bf50c07d54b7ceededea00a890cdfe63593, genuine basec264, old0d1/deployed
and all consumer/recovery refs in existing receipts and create-only owned refs
where needed. With the existing verified clean feature, replay exactly its four
purposes using ordinary `git rebase --onto 628c17661cc4c9bbe7d566072305c7de95284794
c26465c0be452bbf5843d782a324dc82c122f28b` on that feature branch. No repository claim
for preparation; no other feature/default mutation. Keep authors/messages/purposes
and required hooks. Conflict or additional source delta stops equivalence acceptance
and returns the concrete difference to root; do not invent a semantic fix.

Prove ordered stable patch IDs and full binary base-to-head feature diff equal
oldc264..634d versus new628c..successor; retain range-diff and exact old/new trees.
Require old634d→successor tree difference to be exactly the two inherited dependency
files above. Migration20261030180000 SHA2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e,
preceding20261006120000, schema and obsolete-migration absence remain exact. API,
plugins, exporter inputs/locks and client source are unchanged, so bind the existing
revision-specific no-change assessment to the successor; do not rewrite savedde4
capture provenance, export/regenerate clients or change SDK release inputs.

Quick acceptance: ordinary hooks, scoped `git diff --check`, patch/tree/history/
migration comparisons and JSON/generated-Nix source/ref/hash/constraint consistency.
Do not rerun unchanged Ruby/API/exporter/localization checks. The affected executable
check is existing PHP policy/transport regression with actual inherited dependencies:
from `webui`, `composer test -- --filter 'IncidentPolicyTest|IpReleaseFilterTransportTest'`
using already-resident supported PHP/vendor tooling. Verify installed package metadata
actually matches successor's new lock before claiming this composition tested.
No Composer install/update, shell realization, dependency restoration, new test or
browser/VM/system build in this package. A missing/mismatched resident dependency
is an explicit current-PHP verification limit; do not run the old vendor and relabel
it. Preserve earlier successful PHPUnit as historical. Root may use the ordinary
new-head hosted PHP result when available under its separately bounded observation;
no wait/watch/repeated CI query is released by this brief. Quick checks stop on
material setup/overrun rather than becoming a restore campaign.

Owner1 publishes only the owned feature with normal hooks and an exact fresh remote
lease, proves canonical successor SHA/tree/default and clean source, updates the
ordinary comparison capture and supplies compact old/new equivalence plus migration/
input evidence to root. Fresh lease/readback belongs to this execution, not an
architect remote repeat. Normal superseded-run handling must target only proven
old feature heads, coordinated with root's known old634d VM; never cancel a current
head or another branch. Preserve that old run's actual terminal/cancellation result;
its evidence cannot become successor-runtime PASS. No CI launch/rerun/watch.
Root retains explicit merge approval for a proven patch-equivalent rebase. Reuse
review83595c20 outside the affected PHP dependency composition and refreshed history;
root requests only the required affected final/history/equivalence review after
committed source/quick checks. Do not turn this into another full four-lane audit.

**Dependent consumers: HOLD configuration and KB merges.** Once owner1 hands off
its verified public successor, owner3 owns the configuration alignment and owner0
owns the KB alignment under root allocation. Owner1 retains exclusive backend
ownership; no duplicated owner3 backend package. Configuration76403's `vpsadmin` channel/role must select that
exact successor through documented `nix develop -c confctl inputs channel set
--commit --no-editor vpsadmin vpsadmin <PUBLIC_SUCCESSOR>` only with already-resident
accepted tooling. Keep useful generated changelog and ordinary hooks; no hand lock
edit. Consolidate the existing unmerged backend pin stream into one final logical
update, preserving separate templates64665 and policy purposes. Verify semantic
67-node lock/follows diff changes only the backend source identity and necessary
metadata; keep generic0abe/OS/node/React/templates and65 sibling nodes exact.

KBd68's sole backend pin stream owns exactly `flake.nix`, `flake.lock`,
`captures.json`, `contract/navigation.yml`, `contract/pages.yml`. Use its ordinary
exact source selection and `nix flake update vpsadmin` for lock metadata only;
retain sibling nodes/follows/explicit OS override. Amend/consolidate that existing
unmerged source purpose, preserve earlier history and candidate/media records.
Verify the20 factual inputs and257 nonpin entries stay byte/mode equal; the upstream
PHP dependency files introduce no new label/template/capture change. Use the prior
bounded pin/parse/annotation checks as affected, without repeating a whole source
aggregate or capturing media merely for a new SHA. No build/eval-runtime campaign.
Owner1's completed saved-artifact diagnosis establishes KB45224131510 firewall#nixos
failed on external GitHub504 while resolving floating OS HEAD inside the guest,
before the firewall fixture ran. Root accepts qualified source integration with
that explicit environment limit and no source fix. Pin alignment does not relabel
the failed runtime or establish firewall PASS; do not rerun or change OS selection.
See `nov23-backend-readiness-diagnosis/kb-firewall-diagnosis/`.

Both consumer refreshes retain normal hooks/public feature evidence and receive
only affected pin/history review as required. No direct default mutation by these
owners; root verifies producer/default ancestry and all accepted consumer heads
before short claimed integrations. SDKd8cb main/v0.5.0 integration and root protected-publication approval are
already complete; claim released. Do not replay them; actual release/registry
readback and React work stay with owner2. Independent Go/Rust/
templates preparation continues. Demo/source/data/policy3/10, migration/recovery and
released machine state remain unchanged; source rebase/pin updates are no deployment.

Evidence: [fresh canonical default observation](nov23-integration-preparation/vpsadmin/fetch-result.json),
[accepted four-purpose/source provenance](nov23-backend-rebase/packet.md),
[prior KB five-file alignment](nov23-kb-alignment/packet.txt). Architect performed
local source/record reads only, no remote/CI repeat, test or application edit;
session/roster44 and retained Astra/xhigh/workspace_write/full_access reverified.

## Nov23 authorized integration — exact remaining set and dependency order

User now explicitly directs “merge it all” and “and yes you can publish the
typescript client”. This supersedes the earlier keep-unmerged/release-unapproved
statements for the eight delivery repositories below. Keep checks quick; no
production/demo deployment, wiki publication, profile/host or session lifecycle
action is authorized. Bound session/roster44 reverified; architect retains
Astra/xhigh/workspace_write/full_access. Root owns acceptance, release execution
and short merge claims; this note adds no approval or source-design gate.

Portal registrations and current accepted source records establish this set.
Heads are prepared candidates, subject to the owners' fresh premerge checks;
there is no new architect remote/source audit.

| Canonical GitHub repository | Target | Accepted candidate / dependency |
| --- | --- | --- |
| vpsfreecz/vpsadmin-typescript-client | main | d8cb484748db8687554822772a98a1f873414d65; SDK0.5.0 candidate/reviewd4bcc0dd |
| vpsfreecz/vpsadmin-go-client | master | 5934903568862a95b688479f0b13e11e4a36692f |
| vpsfreecz/vpsadmin-rust-client | main | 15db0ffd95ccd34247de9f839c906d860afb1b69 |
| vpsfreecz/vpsfree-notification-templates | master | 64665b3944da4ebf5045ef00f403e410ce88e3ad |
| vpsfreecz/vpsadmin | master | 634d6bf50c07d54b7ceededea00a890cdfe63593; current required CI disposition |
| vpsfreecz/vpsfree-cz-configuration | master | 76403e0dd960838fb16d13ed5043c2a1f88095bd; exact backend634d/templates64665 inputs |
| vpsfreecz/vpsfree-kb-contracts | master | d68bb0a9a98d74198c736956f254d63d71523e81; backend634d pins/current required CI disposition |
| vpsfreecz/vpsadmin-webui | main | successor to25c8db48d087a1f77a9c1dae02c2cdcae0f4e098 after real registry0.5 adoption |

Excluded: HaveAPI1ef9 is the unchanged generator reference; vpsAdminOS52eb is the
retained source snapshot; vpsadmin-api-advisory-diagnostic/f6d is reference-only.
Do not rebase/merge those registrations merely to make their names disappear.
Already completed: extension `vpsfreecz/dev-workspace:master` contains exactbf12,
and `aither64/vpsfree-cz-workspace:master` containse020, the independently proven
equivalent successor of deployed5c9. Accepted integration/lineage receipts in
state.md establish completion; no unfinished delivery from either is identified.
Keep all historical refs, recovery records and existing registrations intact.

**Execution order and owners.** Root can integrate SDKd8cb first and publish0.5.0
through the existing supported route prepared by owner2. The compatible optional
client additions can merge before backend activation; no live feature use follows
from source integration. Go, Rust and templates are independent prepared merges
(owner0 prepares, root integrates) and need not wait on SDK publication. Merge
backend after its selected required checks have a settled acceptable outcome,
then configuration and KB consuming that exact public source. This consumer order
keeps the accepted pins; reaching master does not require a new channel update or
floating to newer unrelated commits. Cross-repository merges are not atomic:
record each exact remote result and keep unmerged consumers pending if a producer
changes or fails. A patch-equivalent refresh needs the existing equivalence and
affected-check rules; substantive changes return to their owner/review, not an
unrelated rebase campaign.

For SDK release, ordinary main integration precedes the matchingv0.5.0 tag on the
automated route. Root may perform the required protected environment approval under
the user's explicit publication direction; preserve configured protections. Owner2
prepares exact commands/identities; do not change publisher settings or tokens.
The automated tag build's archive/receipt is distinct from the validated local
candidate; verify its source and integrity, and publish that retained artifact
without rebuilding in the publish job. The documented manual route instead uses
the already validated archive and existing maintainer authentication. Choose one
supported route, reconcile uncertain registry/tag/default effects before retry,
and never overwrite0.4.0, move a published tag or repack an accepted release to
hide uncertainty. Release validation remains the ordinary small SDK package batch,
not a new long test/build campaign. Registry readback of actual0.5.0 integrity and
required incident members is a prerequisite for React adoption.

Then owner2 completes the existing React package boundary: manifest, npm-generated
lock, frontend-only npmDepsHash, SDK selection/provenance and affected maintained
docs/work-log. Keep API/UI/BFF/transport and unrelated dependencies unchanged.
Apply the prior quick-check/normal-hooks/affected-final-review brief to its exact
successor; published SDK plus final registry manifest/lock/provenance is the real
premerge prerequisite (WebUI AGENTS127–134). Preserve repository PR convention;
root still uses approved ff-only default integration. No additional user approval
is needed for this authorized consumer correction. Old development-archive package
PASS is not automatically a new registry-input package PASS; identify any required
changed-input check that cannot finish quickly instead of silently waiving it.
React configuration adoption/deployment is separate from the already-approved
backend/templates configuration change and is not added to this batch.

**Required gates versus later operations.** Reuse accepted full-series reviews,
refresh83595c20 and SDKd4bcc0dd; owner0/root verifies final heads/history/migration
and normal hooks before each merge. Current634d API aggregate is successful with
full/core exact-once coverage and named unit scopes. Owner1 owns the one newly
allocated finite disposition of backendVM45223174682 and KB runtime45224131510;
this design does not duplicate it or infer their outcomes. If a selected required
check remains active/failed, the affected integration remains blocked until its
ordinary acceptance condition is resolved; “quick only” supplies neither PASS nor
permission to ignore the result. No new watch/rerun or VM/source-fix campaign is
allocated. OldEE telemetry-race and OS stream causes retain their evidence limits;
passing new unit checks cannot certify physical stop/ZFS transfer. A later actual
current runtime result can establish its tested scope without rewriting old causes.

KBd68's actual pinned source check and affected review already pass. Canonical
media review/strict/full-page/real-cluster/staging/wiki publication evidence is
separate from source integration; pending media labels are legal, not demonstrated
strict failure. No blanket recapture or production-publication prerequisite is
added. Future production wiki publication still needs its exact staged-content
approval. Backend deployment still requires migration/API/supervisor/task/template
ordering from the prior brief; merging these sources does not activate them or
require an all-node/kernel rollout.

**Critical section and recovery.** Current installed coordination guide uses
`dev-session coordination acquire/claim-status/release`; a claim carries a resource,
not target authority. Root prepares clean target/environment/hooks before ownership,
acquires one repository at a time, freshly checks target and exact feature, performs
ff-only merge/normal hooks/non-force SSH push/remote proof, and releases before CI,
records or another repository. Baseline drift or hook repair returns to unclaimed
preparation after effects are reconciled. Do not hold a claim across SDK publication,
React preparation or waiting for checks. Preserve consumed migration20261030180000,
schema and deployed-lineage evidence; no reset/rewrite or claim/profile/cluster
operation is needed. Demo/data/policy3/10 and existing machine-release state remain
unchanged. Session stays open after integration; no archive/cleanup follows.

Sources: [portal target map](portal.yml), [accepted SDK candidate](nov23-sdk-0.5-candidate/packet.md),
[remaining-branch classification](nov23-remaining-branch-inventory/packet.md),
[current source/review and completed workspace proofs](state.md),
[prior CI disposition](nov23-backend-readiness-diagnosis/final-disposition.md),
[KB source/release distinction](nov23-kb-gates/packet.txt). Owner0/1/2 provide fresh
preparation/status/release observations in their allocated packages; no further
architect investigation is required.

## Nov23 readiness resolution — sufficient quick SDK candidate package (a4c2967b)

User authorizes resolving readiness gaps and says “Keep checks quick”. Root owns
allocation/acceptance and state; this brief releases no merge, registry publication,
production KB, deployment or lifecycle action. Session identity/roster44 and
architect Astra/xhigh/workspace_write remain verified. Accepted review83595c20
covers backend634d6bf5, configuration76403e0d, KBd68bb0a9 and unchanged feature
contracts; React25c8db48 still needs a published compatible SDK.

**Immediate package: owner2, SDK0.5.0 candidate, independent of backend/KB.**
Root released40a3ecbe under the direct-lead small-edit exception with root-written
changelog; owner2 exclusively owns SDK source and its complete quick candidate
package. This addendum records that allocation and adds no execution/design gate.
Official npm inventory proves published0.4.0 lacks the required incident-policy
members; its bytes differ from the retained development archive also named0.4.0.
Do not replace that release. From clean own SDK2d251bb0, prepare the ordinary next
minor0.5.0 using the existing five-file release pattern: `package.json`,
npm-generated `package-lock.json`, `tools/generator.json`'s lock-file SHA256,
README install version and CHANGELOG entry. Preserve every dependency/version
other than the package identity, all686 generated files, schema/provenance/exporter
lock, HaveAPI1ef9 generator0.32.2 and runtime peer0.32.0. Preserve the historical
development archive. The de4df3d capture remains literal; accepted634d unchanged
export-input evidence establishes freshness within that profile, not a new export.
No backend/client schema regeneration, toolchain refresh or production source edit.
Root applies the required writing skill to version/changelog prose before commit.

Owner2 owns the complete feature preparation: read current instructions, inspect
only required resident tool/dependency availability, make the five-file change,
run normal hooks and the following bounded existing release checks, commit/publish
the feature normally, and hand off the concrete candidate for affected final
review. This is one package, without per-command approval gates. Use the repository
pinned environment only if resident; missing tools/cache, Ruby ABI mismatch,
unexpected downloads/builds or material setup stop this package with an exact
limitation. Do not restore/install a new environment or upgrade dependencies.
Ordinary locked npm setup and the small SDK library compile/pack are allowed when
quick. No frontend/BFF/system/kernel build, full integration suite or VM/browser
work. Do not turn an admission refusal into a retry/setup campaign.

Use `.github/workflows/release.yml:54–66` / `docs/releasing.md`'s existing batch:
locked `npm ci --ignore-scripts --no-audit --no-fund` where necessary; exact local
HaveAPI `./tools/regenerate --haveapi-source <retained-1ef9-checkout> --check`;
one `npm run build`; `npm run typecheck`; `npm run typecheck:consumer`;
`node --test test/client.test.mjs test/release.test.mjs`. Complete normal hooks and
commit the final source; pack its unchanged built output once from that clean
commit with `npm pack --ignore-scripts --pack-destination <fresh-own-output>`,
`node tools/check-package.mjs --archive <exact-tgz>` and
`node tools/release.mjs receipt --archive <exact-tgz> --output <receipt>`.
Avoid `npm test`/`test:package` wrappers that rebuild/repack. Each check is intended
to be quick; if the related batch exceeds two minutes or needs material setup,
stop at the safe native boundary and report before broadening. Use ordinary
owned-effect reconciliation; no orphaned background work. Keep the exact archive,
SHA256/SHA512 integrity and clean committed source identity; never attribute an
older archive to changed source or replace an accepted archive. A substantive
change after the build invalidates that candidate rather than silently reusing it.
Acceptance: only the five intended metadata/prose files changed, generated/input
bytes preserved,0.5.0 identity coherent, required exports and unchanged runtime
peer present, archive/consumer checks passed, normal hooks and feature publication
proven. Retain any failed admission/check literally. A missing required check is
an explicit candidate limit, not PASS. Root invokes only affected independent
review of the completed committed candidate; unaffected83595/SDK evidence remains
scoped to its actual inputs. No new packet framework is needed.

**Dependent React package: prepare after actual SDK release.** SDK
`docs/releasing.md:3–8` requires candidate validation before a “separately
authorized publication” and defaults to the next minor. Prepare the concrete
candidate first. Root then resolves the existing supported release route and its
actual authority/prerequisites; no tag, npm publication, publisher-settings change
or default integration is implied here. Automated publication additionally needs
reviewed source on main and its matching stable tag (`:79–93`); the documented
manual retained-archive route (`:44–70`) has its own conditions. Do not invent a
universal manual-main requirement. Publish only the approved validated archive;
uncertain publication requires registry reconciliation before any retry/repack.

After registry0.5.0 integrity and required members are actually verified, owner2's
dependent React boundary is root `package.json`, npm-generated `package-lock.json`,
frontend-only `packages/frontend.nix` npmDepsHash, existing SDK selection/provenance
record, and affected HAVEAPI_CLIENT/PACKAGING/current work-log explanations.
Use documented `npm install --package-lock-only --ignore-scripts --save-exact
vpsadmin-typescript-client@0.5.0`, preserve unrelated lock entries, then ordinary
`prefetch-npm-deps package-lock.json` only if bounded; no fabricated registry
integrity/hash or premature committed registry selection. Preserve BFF lock/hash,
UI/API/transport behavior, runtime0.32.0 and historical archive receipts. Quick
acceptance is exact installed registry integrity/members/provenance, typecheck,
focused SDK wire/policy/incident units and affected design-doc audit. Existing
`check-package-source.mjs` does not automatically validate SDK selection: check it
explicitly. Final frontend/Nix/package verification remains a separate changed-input
limit if quick scope cannot cover it; old development-archive builds do not certify
registry input. AGENTS127–134 makes a published compatible SDK and resolved final
manifest/lock/provenance a real React premerge gate. Backend capability/deployment
and merge permission remain separate. Rollback restores the coherent source,
manifest, lock, provenance and frontend hash set; never unpublish or overwrite SDKs.

**Backend disposition: no new speculative control/test or source fix.** Owner1's
single exact634d snapshot establishes six terminal workflow successes (PHPUnit,
i18n, migrations, client, libnodectld, RuboCop); API25/26 jobs and VM were active.
Do not poll/replay or claim complete current runtime PASS. OldEE44414971213/1 stays
116/119 failed. StopOverQuota has an observed telemetry update during enforcement,
but no captured eligibility/predicate value proves the proposed race. Existing
`dataset_expansion_spec.rb` plus real `StorageStatus` could cheaply demonstrate an
overwrite in an isolated temporary DB; it cannot recover that missing observation
or by itself justify an atomic-fixture correction. Therefore no control/spec/DB
allocation is necessary now. Remote replacement demonstrably entered OS send-state
and stalled in stream work; sender/receiver evidence is insufficient for cause.
No mocked quick check clears this ZFS/SSH limit; no product/OS/threshold/timeout
change or assertion weakening. Future closure needs the relevant current terminal
VM result and, for any persistent failure, causal runtime evidence under a new
bounded allocation. Ruby3.4.12 loading an old3.4.9 JSON bundle is a local ABI/cache
mismatch; exact current CI narrows dependency coverage, not a reason to reinstall
or modify product code. Owner1 returns capacity with these explicit limits.

**KB disposition: source work is complete; publication evidence stays separate.**
Exactd68 Check45224131578/1 succeeded with ordinary pinned `bin/check --allow-missing`;
source pins/factual content/history/review gates are satisfied. No KB source edit,
rerun or recapture is justified by the SHA-only alignment. Existing six variants'
`pending` label is legal to the validator, not a demonstrated strict failure.
Canonical visual review/strict/full-page/real-runtime/staging/production receipts
remain absent; review OR regeneration depends on actual impact. None is a blanket
source-merge prerequisite in the inspected guidance. Managed runtime45224131510
was still active; retain its unresolved outcome if selected as a required check.
No more status reads/watch/capture/publication are allocated. Root can clear stale
source-gate metadata now, keeping release/runtime limits and missing explicit
repository/target integration direction distinct.

**Protected compatibility/recovery.** Existing demo stays at its accepted old
source graph, with data/report22/eval20/original28 plus29, policy3/10 and runner
unchanged. Preserve consumed migration20261030180000 SHA2eec970f/schema and all
recovery refs; no reset or migration rewrite. Config76403/backend634d/KBd68 remain
frozen by this brief; any substantive successor requires corresponding source/pin
assessment before readiness. Keep generic0abe/OS/node/workspace and other channels
unchanged. Current dependency workflows do not retroactively certify old runtime
or new deployment. No all-node rollout is added by SDK metadata work. Session
remains open; all machine/claim/profile/lifecycle operations remain outside scope.

Evidence: [backend diagnosis](nov23-backend-readiness-diagnosis/findings.md),
[exact backend snapshot](nov23-backend-readiness-diagnosis/snapshot.json),
[KB gate disposition](nov23-kb-gates/packet.txt), owner2 terminal4938dff1 registry
and exact five-file release inventory; accepted refresh review83595c20 in state.
This is sufficient for immediate SDK candidate allocation and honest remaining-gap
reporting; no broader readiness-history or review campaign is required.

## Nov23 merge-readiness refresh — sufficient source and channel packages

**Release boundary.** User requests default-branch rebases, the configuration
vpsadmin channel update, and **quick verification only**. Root also accepts the
necessary companion notification-template channel pin. Feature preparation and
publication are authorized; default integration, registry release, production or
demo deployment, host/profile/claim/lifecycle actions are not. Preserve the running
demo at its accepted old sources, report22/eval20, all original28 reports and the
new report29. Architect retains verified roster44 Astra/xhigh/workspace_write.
This brief is sufficient now; unrelated readiness limits do not hold the rebases.

**Owner1 source package.** Its fresh inventoryf524b6d5 is authoritative; do not
repeat remote inventory. Rebase only backend's four reviewed purposes from
`537b0b7c4ce1d8a930c5fd24b8f4317271ae4f02..0d1db93cd0d38b77f1e29c40ddd71b45581ecfff`
onto freshly observed master`c26465c0be452bbf5843d782a324dc82c122f28b`
(15 upstream commits, no file overlap). Preserve old heads/receipts and normal
hooks; use range-diff/full-patch comparison and explicit lease for feature
publication. Do not call old deployed0d1 literally rebased/deployed. Upstream
contains dependencies, libnodectld observation and OS-input changes: even an
equal feature patch is a changed composition, not an old runtime PASS.

Remaining reviewed delivery heads currently have zero default lag:

| Deliverable | Reviewed range / current final head | Remaining boundary |
| --- | --- | --- |
| Backend/PHP | `537b0b7c..0d1db93c` | Rebase above; retain four purposes and original H styling patch |
| Configuration | `15e3b9af..1b4052c7` | Owner2 rebase and paired channels below |
| Go client | `af9a819c..5934903568862a95b688479f0b13e11e4a36692f` | Final API freshness assessment; no rebase needed |
| Rust client | `823a4f84..15db0ffd95ccd34247de9f839c906d860afb1b69` | Same; no rebase needed |
| TypeScript client | `2da950a9..2d251bb0e10f5379a19df3a07eb7a0b0f19e3c88` | Same; registry release remains separate |
| React frontend/BFF | `88ac13b8..25c8db48d087a1f77a9c1dae02c2cdcae0f4e098` | No rebase; registry SDK required before merge |
| Templates | `2cfd218d..64665b3944da4ebf5045ef00f403e410ce88e3ad` | No rebase; final exact tuple feeds companion channel |
| KB contracts | genuine `ce2c8cd9..62472721c148e94b8d073b4dbc72550a0db0317c`; default`cb782524` | Two unmerged purposes; final backend pin freshness, media limits below |

HaveAPI`1ef9b204` has no session commits and is a pinned generator reference,
not a rebase of its rewritten default history. OS`52eb4de0` is the retained exact
demo source reference; diagnostic`f6d690ed` is reference-only. Do not rebase,
republish or turn these into deliverables. Workspace/extension already integrated.
Owner1 preserves complete old/new reviewed ranges, source/input identities and
no-migration conclusions for clients/templates/React/KB. No gratuitous regeneration,
release/version bump or new commit where source remains unchanged.

**Immutable migration and generated clients.** Keep migration20261030180000
immediately after20261006120000, SHA256
`2eec970fb3620ad25f3ac01c06a9eae61af2d208f88184e995c74b8ad2ba2c1e`, and its
consumed demo/SDK provenance. No schema rewrite, renumber, reset or compatibility
guards. Compare the complete final API export inputs against retained schema,
plugins, generator/runtime and tool locks. Exact unchanged-input evidence may
support a revision-specific no-change assessment; inherited changes that affect
schema/export require the ordinary bounded exporter and affected regeneration.
Never edit provenance to pretend an old export ran at the successor. If needed
preparation/checks exceed quick-only scope, report the specific gap rather than
launching builds, a long database/export matrix or VM campaign. React's immutable
development SDK archive is not a registry release: final manifest/lock must use
the published registry artifact before React merge. That release/adoption is not
silently included in this refresh.

**Owner2 configuration package, independent rebase first.** Rebase the sole
policy/docs purpose from`15e3b9af..1b4052c7` onto observed canonical
`588259a54bcfaf0913974d58b0990b148fc7e0e3` (27 commits, no overlap), using its
accepted preparationa53e82f4. Inherit current default's complete graph, including
`devWorkspace=0abe` and current site settings; do not import old1b's9241 lock.
Wait only for owner1's exact published backend/template tuples before pinning.
From the configuration's ordinary pinned shell, run the documented commands:

```sh
nix develop -c confctl inputs channel set --commit --no-editor vpsadmin vpsadmin FINAL_PUBLIC_BACKEND_SHA
nix develop -c confctl inputs channel set --commit --no-editor vpsfree-notification-templates vpsfree-notification-templates FINAL_PUBLIC_TEMPLATE_SHA
```

Each generated input update is a separate logical commit, useful changelog on;
retain confctl's generated message and normal hooks. The first selects
`vpsadminServices`; the second selects`vpsfreeNotificationTemplates`, whose
vpsadmin input follows`vpsadminServices`. Current default templates`2cfd218d`
are insufficient for the new collection payload, hence the accepted companion
pin. No hand-edited lock, global channel update, private override or runtime
reconcile. Preserve staging/production node channels, OS/nixpkgs/workspace pins,
sibling identities and follows edges except the necessary declared transitive
closure of the two selected inputs. Unexpected lock churn is a bounded blocker.
React's separate channel remains unchanged at88ac; its SDK gate is explicit.

**Deployment answer and compatibility.** This needs the central control plane,
not only HTTP API, and does not require deploying all compute nodes or kernels.
Existing node oomd event format and physical Stop command remain compatible;
backend537b..0d1 changes no nodectld implementation or NixOS module. It adds the
server-side incident RPC plus nodectl/libnodectld client support. Install the
new supervisor handler before using new nodectl; retire old direct-SQL incident
writers because they bypass creation-time matching. Update CLI installations
where used; this is not a coordinated fleet reboot prerequisite for oomd events.
Reassess only actual rebase conflicts/inherited relevant protocol changes.

Site configuration places API and supervisor on`int.api1` and`int.api2`;
`int.api1` also owns scheduler/default rake tasks and replacement-template
reconciliation. Tasks use the API package/config, not a distinct task daemon on
the MariaDB host. The database-role application handles migrations; changing
MariaDB itself or deploying every machine tagged vpsadmin is not implied.
`databaseSetup.autoSetup=false`: a config switch alone does not apply migrations.
For a later separately authorized rollout: back up persistent state; apply the
supported migration once; install/reconcile paired templates; converge compatible
API/supervisor/task code and the same policy declaration before activation, then
update PHP readers and separately ready React frontend/BFF. Do not run old/new
incident producers indefinitely together or infer mixed-version enrollment of
legacy SQL rows. Global mode defaults observe; existing overrides/mode persist,
so loading3/10 is not proof enforcement is enabled. No historical rematch occurs.
Rollback must preserve schema/evaluations/actions and reconcile submitted effects;
dropping the migration or restoring the whole old database is not recovery.
These are deployment constraints, not permission to execute them now.

**Quick checks and review.** Owner1/2 read current repository instructions and
run normal hooks, `git diff --check`, exact range/patch/migration comparisons and
only affected fast syntax/lint/unit checks from existing packets. Configuration:
Ruby syntax/normal RuboCop/Nixfmt hooks, generated lock semantic diff and exact
channel/sibling/follows checks; use narrow `confctl inputs channel ls vpsadmin`
and `inputs ls vpsadminServices` only with the available pinned shell and no
heavy realization. Preserve final policy digest and source semantics. User's
quick-only instruction excludes full flake builds, application/VM/browser/full
integration suites and new long CI campaigns. Old successful checks remain
literal historical evidence; absent outputs are not resident artifacts, and
changed dependency/derivation inputs do not inherit runtime PASS. Root schedules
only affected final review after committed refresh and quick checks, carrying
complete branch history/migration conclusions and old/new composition evidence.

**Readiness limits to state honestly.** Existing all-lane reviews remain useful:
backendd20c1edf, configurationb850e2d9, Reactb8167734, templates/history review and
KB mechanical certificatef930612b. Native PHP0d1 run7552994f and React25c8 twelve
browser/five package targets passed; demo runtime/data acceptance is for its
retained old source graph. OldEE CI44414971213/attempt1 remains116/119 FAILED:
StopOverQuota and remote replacement causes are unresolved despite unchanged
relevant blobs. Later targeted PHP PASS does not clear those transaction failures.
No new long diagnostic campaign is authorized. KB final62472721 already replaced
95f/bd18 with public0d1 and ordinary pinned `bin/check --allow-missing` PASS;
canonical media/strict/full-page/staging/production proof remains separate.
A refreshed backend SHA requires affected KB pin/factual source alignment, not
new media merely because a SHA changed. Root must report any changed-source/media
impact that cannot be covered quickly. These gaps, SDK registry prerequisite,
final refresh/review and missing merge direction prevent a blanket fully-verified
merge/production-ready claim. Source preparation proceeds within this brief.

Existing authoritative evidence: [final backend review](nov19-php-usability/followup/review-result.md),
[configuration review](nov19-usability-feedback/configuration-review.md),
[React verification](nov19-usability-feedback/react/postreview/packet.md),
[template history](nov19-daily-report-history/addendum.md),
[KB final source check](nov19-usability-feedback/kb-followup/check-history/packet.md),
[KB publication](nov19-usability-feedback/kb-followup/publication/packet.md),
[configuration preparation](nov23-configuration-consumer-preparation/).
Root owns source allocation, residual-risk disposition, final answer and any
later repository-specific merge approval. Architect made no source/remote/runtime
mutation; only this short tracking addendum. Session remains open.

## Nov23 fresh report examples — two current CS/EN captures, existing demo only

**Sufficient package for implementer0; root allocates and accepts.** Verified
session/roster44, retained architect0 Astra/xhigh/workspace_write; prior packages
terminal. User authorizes fresh examples. Create exactly two synthetic trusted
OOM-policy source reports: VPS1/user2/test-user1 (CS), VPS2/user3/test-user2 (EN).
Required deliverable: two new report links plus their actual current captured
notification bodies. No warning/stop matrix, real OOM, VPS start or counter reset.

**Source/presentation.** Backend0d1, templates
`64665b3944da4ebf5045ef00f403e410ce88e3ad`, site1b/digest8d923a and policy3/10 stay
fixed. Reuse [loaded policy](nov19-demo-refresh-execution/nov23-status-f783/services/loaded-policy-result.json),
[source/state](nov19-demo-refresh-execution/nov23-status-f783/services/terminal-state.json)
and [accepted template hashes](nov19-demo-refresh-execution/template-loaded-final.json).
The template receipt is historical loaded proof; freshness is checked narrowly below.
`api/lib/vpsadmin/supervisor/node/vps_events.rb` ingests trusted events;
`api/lib/vpsadmin/api/incident_reports.rb` generates localized source/notice text
from `api/lib/vpsadmin/api/locales/{cs,en}.yml`. PHP
`webui/forms/incidents.forms.php` displays that stored text and saved evaluations.
Full updated notification text is rendered separately from
`templates/vps_incident_report/email/{cs,en}.{subject,text,html}.erb`, or
`vps_memory_pressure_stopped` for a naturally confirmed stop. Pair report and
captured-email links. Manual API/nodectl reports fail the trusted node-event
selector and omit its changed policy summary; do not forge provenance/evaluations.

**Execution boundary, after root release.** Use ordinary
`vpsadmin-devcluster ssh 2026-10-30-oomd-abuse-policy services -- ...` and the
already-used deployed API Ruby environment selected from unit WorkingDirectory
(`nov17-devcluster-demo/postreview-2026-11-18/guest-ruby.sh`). Adapt only the existing
`event-publish.rb` transport into one new private two-event payload/attempt record;
never run its old20-event plan or fixture creation. No repository source/build work.

1. Before any send/login, verify actual nodectld mailer SMTP targets Mailpit at
   `127.0.0.1:1025`, with no automatic external relay, forwarding or webhook.
   Inspect safe selected options without printing secrets. Verify only the stored
   CS/EN subject/plain/HTML fields for `vps_incident_report` and
   `vps_memory_pressure_stopped` against64665 and applicable delivery preferences.
   Mismatch blocks sending; no template reinstall/reconcile or preference change.
2. Save original report/evaluation/action/MailLog IDs/hashes (especially22/eval20),
   current capture IDs, owner/node mapping, stopped state and policy/counts/cooldowns.
   Reuse accepted system/source proof. Plan exactly two new nonfuture whole-second
   events: `{id: VPS_ID, time: CURRENT_SECOND, type: "oomd", opts: {action: "stop"}}`.
   Bind each to its current node and an absent SHA256 source key of
   `node_id:vps_id:oomd:time:stop`. These are synthetic examples, not real OOM evidence.
3. Publish each once with the existing configured Bunny transport: direct exchange
   `node:<node.domain_name>`, routing key `vps_events`, persistent JSON and publisher
   confirms. Record the attempt before sending. Reconcile uncertain outcomes using
   the original key; never invent another tuple or replay to repair email. Normal
   supervisor/task/chain processing owns all effects.
4. Verify two new ordinary reports and two matched saved evaluations at3/10,
   their two sent ordinary MailLogs, and actual CS/EN captured plain/HTML bodies.
   Saved acceptance had10/10 per VPS, so11/11 is expected absent natural window
   expiry/intervening events; actual saved facts govern. Do not patch counts.

**Natural consequences.** Warning cooldown remains active; stop cooldown has
elapsed. Each new event may prepare one normal Stop action/chain even though its
VPS is already stopped. Existing escalation sets `rollback_stop: false`; no VPS
start is needed or allowed. Stop-on-stopped is not pre-certified as a no-op:
observe actual transaction/action results. Only authentic completion may create
up to two additional stop-completed notices and specific-template captures; link
those if produced. Do not force a notice or claim a fresh running-to-stopped
transition. New stop logs/cooldown timestamps are expected possible effects;
old report/evaluation/action rows remain unchanged. Observe normal processing for
up to10minutes; hand back any failed/uncertain effect by exact identity for normal
reconciliation, without extra events, direct row writes or broader repair.

**Visible acceptance.** Open each fresh report at
`https://webui.aitherdev.int.vpsfree.cz/?page=incidents&action=show&id=NEW_ID`
with existing demo accounts. Pair it with its actual authenticated message URL
under `https://mailpit.aitherdev.int.vpsfree.cz/` (derive the route/ID from the UI).
Capture a small CS/EN rendered HTML pair/screenshots or stable links and inspect
plain text too: current policy table/3/10 facts, localized copy, and stopped
message guidance/contributors only when genuinely generated. Template source is
not rendered proof. No new React/warning/browser campaign. Separate incidental
login mail; keep credentials/rendered private content untracked. Root owns final
wording and identifies these as synthetic demo examples.

Finish with original22/eval20 and baseline rows unchanged, both VPSes stopped,
policy3/10 intact, exact new report/evaluation/action/chain/MailLog/Mailpit IDs and
terminal effects. Preserve examples and old-mail waiver. No rematch, cleanup,
reset, persistence feature, template reconcile, schema/source/build/deployment,
profile/host/default/lifecycle action; released machine ownership stays released.
Architect made only source/docs/saved-evidence reads and this short locked design
edit. Capacity returns ROOT ONLY; implementation is owner0's package.

## Nov23 Mailpit preservation — no exact recovery source identified; user disposition required

**Bounded conclusion for root.** Identity/session and roster44 reverified;
architect0 retains Astra/xhigh/workspace_write, prior package terminal. The
policy selection/services update remains parked. No intact old capture database
has been identified in the ordinary retained locations. The saved70 message
API objects preserve useful historical content, but do not constitute a database
or raw-email backup and cannot restore the original capture identities exactly.
Do not declare the original mail-preservation condition satisfied.

Owner0's [postboot receipt](nov19-demo-refresh-execution/nov23-status-f783/postboot-partial-receipt.json)
retains successful start, applied descriptors/pendingnull, all24reports,
20evaluations,4actions,45MailLogs and report22/eval20, plus byte-equal original
BFF files. Mailpit has0 captures versus the original70 IDs. Its installed
Mailpit1.33.1 command uses a temporary default database; selected providerxq8
`dev-clusters/vpsadmin/nix/test.nix:1921–1935` supplies no persistent database
selection. The backend generic test option is not used by this provider command.
This establishes current volatility, not when the old captures disappeared.

**Finite retained-file finding.** Owner0 alone performed the necessary
[one metadata observation](nov19-demo-refresh-execution/nov23-status-f783/mailpit-retained-db-observation.json),
native99944 exit0/joined. Top-level `/tmp` contains only current PID293's database
4096B, WAL477952B and SHM32768B; every matching file is its recorded open target.
`/tmp` is tmpfs and `/var/lib/mailpit` is absent. Exact private observation SHA256
`0270adde2043a65cd41c9c90d5eb1dc98f8f0206383a93bbbe835b216665983f`.
No old pathname was saved. This supports no available ordinary recovery
candidate in those locations, not a whole-disk absence/irrecoverability claim.
No extra filesystem archaeology, guest probes or SQLite opening is needed for
this disposition. Current database files are not substitutes for the missing70.

**What the saved evidence actually contains.** Private
`nov19-demo-refresh-execution/private/mailpit-before.stdout` is370266B,
SHA256`2db92a4a70a350240ea58ce370f95de4d7409fa492c8f8ceff337dd0674c4f45`.
Offline schema inspection confirms70 listing entries and70 message objects:
decoded Text/HTML, addresses, subject, saved database ID and MessageID, and
available dates/tags/read/other metadata. All attachment/inline lists are empty.
There is no raw RFC822 payload or complete header set. Keep this file and its
existing per-ID canonical-JSON index private and unchanged; no subjects,
addresses, bodies or message IDs are copied into tracking. Existing MariaDB
backup covers vpsAdmin, not Mailpit.

The [Mailpit storage contract](https://mailpit.axllent.org/docs/configuration/email-storage/)
distinguishes temporary SQLite (deleted on normal exit) from reopening a named
persistent database. A genuine compatible database, with committed WAL content
preserved, could retain stored identities; none is available in the bounded
proof. The installed provider exposes no database selection here, and this
brief does not authorize overriding its unit or adding persistence.
[Supported ingest/dump](https://mailpit.axllent.org/docs/usage/import-export/)
uses individual raw email files and SMTP ingestion. The exact
[v1.33.1 API schema](https://raw.githubusercontent.com/axllent/mailpit/v1.33.1/server/ui/api/v1/swagger.json)
separates `ID` (database identity), `MessageID`, and received `Created`; its Send
request provides content/headers/tags, not a chosen database ID or original
received timestamp. JSON reconstruction could retain decoded bodies and selected
metadata but creates new captures; original MIME/header bytes, database IDs,
receipt chronology and transport history would not be restored faithfully.
Changing the RFC Message-ID alone does not restore the database ID. A raw-email
backup would improve content recovery but still would not establish exact
capture identity through ingest. Do not remail, fabricate rows or call such
reconstruction exact recovery.

**Required user decision and shortest completion.** Root should ask whether to
continue the requested policy demo while retaining the original70 solely in the
unchanged private JSON evidence archive and explicitly accepting their absence
from live Mailpit. That is the smallest recommended route, with no reconstructed
mail or source expansion. Alternatively remain parked for an identified genuine
Mailpit database backup; any requested reconstructed visible copies require
explicit acceptance of new IDs and the above fidelity limits. This is a change
to the original preservation requirement, so root must not infer that consent
from the prior profile/demo approval. No global search or persistence feature
is implied by either option.

After that disposition, root alone releases owner0's existing finite policy
continuation. Keep all source pins, descriptors, reports, MariaDB records,
credentials/BFF state, templates64665-no-repeat, seedcs and same-target forward
recovery unchanged. Preserve the original0-vs70 finding and JSON hashes through
acceptance; new captures are separate records. No recovery/restore/resend,
source/config/profile/build/VM/restart/claim/lifecycle action was performed by
architect. Only source/docs/saved evidence were read and this short locked
tracking note written. Owner0's one read is terminal; design capacity returns
ROOT ONLY with the user decision outstanding.

## Nov23 status pin — required verification in the actual consumer composition

**Sufficient verification allocation; source stays frozen.** Session/roster44 and
architect0 Astra/xhigh/workspace_write retained. Use extension
`bf12ac71a8a00b1581eed5352f99c1b2daaeff5b` with the actual consumer's generic
`0abe5fe48955b1bcdc8cc368fcb27e11e0676f70`, then verify consumer
`5c9d99dc72c0e4263d7e8d13806b200713a78c46`. This is an operation-scoped check
composition, not a source/lock/runtime pin change. Root retains review, cost and
execution allocation; owner1 owns extension verification, owner2 consumer
verification. No new source-design gate or host/demo/claim action is introduced.

**Why this is faithful.** Frozen extension `AGENTS.md` requires focused Ruby
checks before ordinary `nix flake check`; its README and `flake.nix:323–end`
declare nine checks, with no requirement to repeat every default-runtime matrix.
Workspace `verification.md` explicitly permits exact derivation/input reuse and
requires repetition for relevant changed inputs, unresolved failure or missing
required verification. It does not invalidate successful evidence after GC.
Consumer `flake.nix` explicitly overrides generic to0abe and follows the
extension's nixpkgs. Offline immutable-lock comparison resolves all19 reachable
generic input edges identically to5c9's generic subtree; consumer/extension use
the same nixpkgs node. Preserve all fixture inputs, including status587cd65,
KB/runtime contracts and host-path assertions.

After existing final review/allocation, run the existing nine checks normally:

```sh
nix flake check github:vpsfreecz/dev-workspace/bf12ac71a8a00b1581eed5352f99c1b2daaeff5b \
  --override-input dev-workspace github:aither64/dev-workspace/0abe5fe48955b1bcdc8cc368fcb27e11e0676f70 \
  --no-write-lock-file --print-build-logs --max-jobs 1 --cores 1 \
  --option keep-going false --option allow-import-from-derivation false
```

Owner1 first binds that effective graph/dry-run within the same finite package:
exact bf12/NARhlCQ and generic0abe/NARnQLc, unchanged root fixture identities,
all nine declared roots and actual missing work. Do not rewrite a lock or add a
`doCheck` override. Generic0abe's existing `nix/workspace-portal.nix:7,682–714`
separates package construction (`doCheck=false` by default) from exported Ruby
shards/aggregator and checked package. Old generic832's package embeds the Ruby
aggregator in `checkPhase`. This explains avoided restoration; the proposed
run is **not a fresh full-generic-suite PASS**. Reuse successful generic results
only with their actual identical derivation/full-input receipts and complete
unique shard coverage. No test marker/output may be synthesized.

**Exact reuse and realization limits.** The saved
[default graph comparison](nov23-status-pin/reuse-and-missing-work.json) binds
5585 identical common entries,12new entries, and ca7's3533.357253s PASS. Its
unchanged `rejects-invalid-site-config` root and unchanged runtime shards retain
that historical result even when absent. The28-build default dry-run includes
11missing unchanged shards plus their aggregator; absence is not failure, but
those real outputs would still be needed to build dependent default832 packages.
All eight changed default roots remain unverified for bf12/default832; do not
label an overridden run as a default-root PASS. No inspected policy makes that
extra composition a prerequisite for this narrow actual-consumer delivery. If
root elects to certify it too, normal realization/substitution of its dependencies
is necessary; historical receipts cannot satisfy Nix input availability.

Under generic0abe, realize every changed ordinary extension root: `tests`,
`integration-recipe`, `organization-source`, the three fixture packages
(`package`, `compatibility-package`, `kb-provider-package`), `package-metadata`
and `kb-provider-contract`; the effective graph determines exact identities and
reuse. Keep all nine selected, including invalid-config rejection. Existing
provider-context evidence already binds statusf783 to exact historical
yz96/v8l/sp5l/source3y96/versionf783d04/clientv0.2.0; root smoke fixtures remain
a separate consumer, not proof of the demo's selected status recipe.

**Actual workspace acceptance.** Owner2's ordinary `nix build --no-link
--print-build-logs --no-write-lock-file --max-jobs 1 --cores 1 --option
allow-import-from-derivation false` targets the frozen own5c9 source's
`packages.x86_64-linux.default` plus all seven `checks.x86_64-linux.*`:
`pi-runtime-composition`, `tracking-source`, `deployment-contract`,
`storage-retention`, `agent-instructions`, `agent-team-policy`, and
`cluster-provider-composition`. These cover the actual configured package,
provider/catalog, Pi/site/team/instruction/source/host contracts; they do not run
the full generic suite. Reuse c087 outputs only where owner2's actual recursive
graph proves identical recipes/inputs; changed package/check outputs need real
realization. Preserve c087's literal [eight-output receipt](nov19-workspace-selector-preparation/refresh-f6b/realization/receipt.json),
including its explicit no-generic-suite-reexecution limit. Existing review,
focused checks and failure records remain independent and unchanged.

No migration VM is required: the pin changes neither migration behavior nor
host-state compatibility. Before realization, stop for unexpected input drift,
additional changed check policy, kernel/VM/system work or material cost outside
the allocated finite batch. Cache savings are conditional on actual graph and
availability, not promised by this source-only assessment. Architect performed
no eval/build/fetch/restore/store query or source/runtime mutation; only this
tracking clarification was written under the short lock. Capacity returned.

## Nov23 status-source drift — preserve the packaged branch with one exact input pin

**Sufficient dependent source/operation boundary for root allocation.** Verified
session/roster44, architect0 Astra/xhigh/workspace_write and capacity retained.
Owner0's [83s graph/dry-run](nov19-demo-refresh-execution/nov23-execution/evaluation-results.json)
and [boot projection](nov19-demo-refresh-execution/nov23-execution/boot-selection-proof.json)
remain PASS for their exact input set: all recorded guest descriptors equal,
15small builds/19fetches/6.9MiB download/19.7MiB unpacked, no kernel/image/system
build. No boot/config/update followed. Their
[input drift](nov19-demo-refresh-execution/nov23-execution/input-drift.json)
binds packaged statusf783→561; services consumes the selected package/module, so
this difference cannot be dismissed as irrelevant merely because boot retains
old payloads.

**No public operation-scoped exact Git selector exists.** Actual selectedca7
provider at `/nix/store/bqpissz82xvb48ahbpmyswsh0bzs0yn8-vpsfree-dev-workspace-tools-0.1.0/share/vpsfree-dev-workspace/dev-clusters/vpsadmin/`
accepts fixed start/update options. `bin/devcluster:693–710,787–810,837–860`
chooses an own `vpsf-status` directory and internally supplies the Nix override;
there is no exposed status-revision flag/config or passthrough. Supplying a raw
Nix override outside that command does not bind its later ordinary build.

The ordinary worktree alternative is **not equivalent**: `nix/test.nix:442–471`
uses local `callPackage`, version`dev`, local module and the existing own Go-client
checkout. Old Nov19 packaged source instead uses version`f783d04`, empty
`postPatch`, released clientv0.2.0 and vendorHash
`sha256-phYdInfe1dU4fnhquNjJpIcaT3E/lubbTTa5uaV8Cb0=`. Its local branch changes
the hash toN6v and adds a Go-module replacement. Current own client is clean
`5934903568862a95b688479f0b13e11e4a36692f`, distinct from v0.2.0 commit
`7bc136e1d72f15174229bea2bb7de284174512f2`. Owner0 independently confirmed its
client path was already nonempty but ignored on the old packaged branch. Do not
create a status checkout, hide/move the client checkout or silently accept this
composition change. No fetch/worktree/registration command is needed for the
recommended route.

**Smallest faithful correction:** extension successor of reviewedca7 changes
ONLY `dev-clusters/vpsadmin/flake.nix`, replacing the existing `vpsfStatus.url`
with `github:vpsfreecz/vpsf-status/f783d045ac49a0ae9e8501a8f9a38d0523177b9e`.
Keep its nixpkgs/API/OS follows and all local-source precedence unchanged. No new
selector, config key, script, lock framework or subflake lockfile; none currently
exists there. Leave the extension root's separate smoke-fixture status input/lock
at its existing587cd65 identity; it is not the ordinary provider selector and
must not be silently upgraded to make an unrelated fixture align. This pins the
packaged fallback for this provider generation; it does not alter already-applied
guest payloads or existing local-worktree overrides.

Retained f783 commit/tree are **absent from canonical local Git** (no fetch was
performed). Its original immutable source exists at
`/nix/store/3y96glvxz3v981nz63czjkjwzyn7kraw-source`, with recorded input NAR
`sha256-KstSOkR6Nu0qUAq4awECduPQ7ueacqo+7rBdwGosbEk=`; do not invent a Git tree.
The saved Nov19 graph binds status drv`yz96clc4djqj8dl9h3fjaqbv5hn8sy51`,
output`v8l13bc6fgzl12z6g8ddlkmxnbiv5zxz`, and Go-module output`sp5l9k02a3rh0ikz3axjy9v6zf1n7agw`.
The exact GitHub revision can use the ordinary Nix input resolver during allocated
preparation, with that source/NAR binding; a canonical status clone/worktree is
not a prerequisite. Present source residency is not a future fetch/cache guarantee.

**Source delivery:** root allocates the existing extension owner the one-file
pin/normal successor, focused existing provider checks and required package/flake
checks. No host-migration VM: no lifecycle/host contract changed. Obtain affected
final configuration/history review, retaining ca7's selector and prior evidence.
Owner2 then consumes that published exact successor from accepted workspacec087
through only `flake.nix`/generated `flake.lock`, retaining generic0abe/codex-web3209,
Pi, other38-node identities/follows, instruction relocation and all site/team/native
settings. Preserve all original c087/vg3/nnia source/check/review/activation evidence.
Required checks/package realization may reuse only actual identical successful
derivations/inputs; changed outputs need their normal checks, not a new full
runtime/API/SDK campaign. Root performs the ordinary reviewed forward profile
switch under its current verified machine ownership; no host upgrade or user
product decision is introduced. No architect source/build/profile action occurred.

**Owner0 resumes the complete existing48adc82d package after installed-provider
proof.** Keep no own status checkout; require actual selected input exactf783/NAR
KstS, packaged module/package, versionf783d04, empty postPatch, released0.2.0/vendor
hashphYd and unchanged five frozen sources/OS52eb. This does not assert status
output equality: compare actual derivation/input identity to the saved package
before reuse. Perform one bounded changed-input admission for the ordinary boot
config+runner, then the already-required services target after policy selection.
Retain the original83s proof without rerunning it merely for this design decision;
new results cover the changed provider. Stop for any unrelated input/client/layout
change, unexpected kernel/image/system work in retained-start admission, or new
material build beyond the allocated budget; do not broaden targets or adjust
vendor hashes. Services naturally has its allocated system build and retains
its existing material/kernel guards. No repeated discovery, test campaign or
review for unchanged evidence/source preparation.

Ordinary retained start and services-only update keep their existing ownership,
source/schema, payload/root, pending-forward-recovery and authenticated acceptance
contracts. Preserve report22/evaluation20 membership and saved5/10 snapshot while
loading current3/10, DB/VPS/mail/secrets/BFF sessions, seedcs,64665-no-repeat,
retained caches and recovery. Root accepted preservation of the packaged branch
in clarification25738c5b; this record supplies the necessary implementation delta,
not another user approval gate. Only this locked design note changed; all
architect commands terminal, capacity returned.

## Nov22 profile-switch refusal — preactivation admission, active external archive

Session/roster44 and architect0 Astra/xhigh/workspace_write reverified; prior
packages terminal. Root's [invocation](nov19-workspace-selector-preparation/refresh-f6b/activation-invocation.json)
and [result](nov19-workspace-selector-preparation/refresh-f6b/activation-result.json)
retain the single19:54:21–29UTC switch, exit1/7.416s, PID26701 and joined native
62572. Candidatevg3x7/c087 acceptance remains valid; this is an external admission
blocker, not a source failure or deployment attempt needing code repair.

Installedxyyx `libexec/.workspace-host-wrapped:659–688` first resolves/builds the
candidate, then calls session admission. The exact error comes from
`:3229` → `:2673–2723`, which finds archive/cleanup journals. Peer journal
`worktrees/.locks/2026-11-11-pi-codex-migration.archive.json` predates this call:
operation `bbc146b02684dca6280b226878f7672c6f13b89cd90d8991ba036811c43d632a`,
modearchived, phase`clusters_released`, finalized19:08:56UTC, journalmtime19:22:34.
The refusal therefore occurs at the first preparation admission, **before**
`switchOperationId` creation(:713), maintenance-switch dispatch or
`activate_candidate`(:758). Pending writes(:780/787), profile selection(:793),
portal drain/quiesce and native/service activation are not reached. Preparation
is not literally effect-free: `workspace-coordination-host.rb:31–42` runs ordinary
`nix build --no-link --print-out-paths` and retains a private preparation build
log. Those are preparation/cache evidence, not activation intent. At19:58:48UTC,
selected profile still resolves to exactxyyx and `state/codex/pending` is absent.
No current pending or new activation recovery was created by this failed call;
the historical maintenance status is not used to establish that conclusion.

**The external operation is currently running.** Source sensitivity marker was
absent and its manifest ordinary before this bounded read. Matching unit
`workspace-archive-72c39b7d89259d6d04ede8ef6f3bfc872dfe648b144ea3fad699f3c022d5fceb-1.service`
is active/running, MainPID2648170 present, start19:07:44UTC and no exit timestamp;
its cgroup contains2648170/198887. Its command names the exact peer slug and
operation above. Sealed schema3 cleanup remains completed=false; sidecar progress
mtime advanced to19:57:43 while inspected. Thus this is active archive cleanup,
not evidence of a stranded operation or reason to start a retry. No cause or
completion deadline is inferred. Its existing supervised worker and retained
portal request own completion; if interrupted, only that owner's matching
ordinary Archive Retry/recovery may resume the same operation. This session must
not invoke it, modify journals or bypass the guard. No peer message was sent.

**Claim disposition:** recommend root release exact claim
`1716c449-736f-45bc-9c10-1a4df896411c` as unused, using its authoritative HELD
revision1/source1b/owner06ec0ea6 status and joined-effect proof. This call never
entered deployment, so it creates no failed/uncertain-deployment retention or
new deployed-lineage integration obligation. Preserve the failed result and
preparation diagnostics. Root alone performs and verifies ordinary release;
no release was performed here. Reacquire fresh configured-machine ownership
for any later switch after external lifecycle admission clears; do not poll or
retry activation as recovery. Built/rooted candidate/source, demo/OS52eb/data
and all earlier recovery evidence remain retained. No source, profile, claim,
lifecycle or peer mutation; only this locked note changed. All architect
commands terminal; design capacity returned.

## Nov22 retained-demo recovery — pin existing OS source, then public start/update

**Sufficient owner0 boundary after root's operation release.** Session/roster44,
architect0 Astra/xhigh/workspace_write and capacity reverified; prior3752d98b
terminal. Owner2 independently owns the current-compatible workspace selector.
This clarification uses owner0's [current preflight](nov19-demo-refresh-execution/nov22-readonly-preflight/packet.md)
and saved applied descriptors; no duplicate runner/guest/data probe was made.
Runner719334 and its recorded owners are absent, while applied envelope
SHA256 `0f111dc310bcf358843ec7afd1921d8a4feedd3755af5781e90c64e94c7fad06`
is unchanged with pending=null. Disk/credential presence is evidence for
preparation, not a claim of current DB/mail/session contents or a cause of loss.

**Ordinary exact OS selection is available.** The accepted build input is
`52eb4de029f385c3e2d1b614d9b6ff32bbfb29bf`, tree
`c998787d3499daaa9d1f77474710176631a0dae5`; both commit and tree are available
in local canonical `repos/vpsadminos.git`, consistent with the
[Nov19 selection receipt](nov19-demo-refresh-execution/os-selection-drift.json).
Create only an unchanged own-session source checkout through the public helper,
for example, after confirming the name/branch is unused or already exact:

```sh
dev-session worktree add 2026-10-30-oomd-abuse-policy vpsadminos --as-is   --base 52eb4de029f385c3e2d1b614d9b6ff32bbfb29bf --no-fetch   --branch 2026-11-22-oomd-abuse-policy-os52eb
```

Owner0 owns this disjoint preparation at
`worktrees/2026-10-30-oomd-abuse-policy/vpsadminos`; no OS source edit, new OS
feature, dependency update or source commit is needed. A conflicting existing
registration/ref refuses; never reset/rebind it. Preserve canonical local
`origin/staging=e9d55bada43c888ae91139d549d156a0831817de`, other refs and peers.
Installed public worktree instructions support `--base`, `--branch`, `--no-fetch`
and record the exact new base. Provider `bin/devcluster:693–710,790–801` selects
that directory as `path:` for BOTH `vpsadminos` and `vpsadmin/vpsadminos`;
otherwise it follows local origin/staging. No config exact-revision key,
private override or ref rewind is necessary. ca7 leaves this helper, flake and
shared recovery code unchanged from installedd76. Keep the checkout frozen at
exact52eb through both operations. A path input can change derivation identity:
tracked-tree equality does not promise cached outputs or build equivalence.

**Run the supported existing-cluster route, without recreation.** After the
reviewed selector/profile is selected and exact52eb preparation is complete,
owner0's released sequence is ordinary
`vpsadmin-devcluster start 2026-10-30-oomd-abuse-policy --existing`, then
`vpsadmin-devcluster update 2026-10-30-oomd-abuse-policy services` with the sole
approved `incidentPolicyFile` selection. Start uses saved single/bridge settings,
validates the candidate against the applied layout, and boots the complete saved
payloads. The projection retains old QEMU/virtiofsd and
`/nix/store/nc24ff7jzy7p5zb1g5xya2anmy5vs9q0-source` OS export even though an
own build checkout now exists. Services/root and node tank disks must remain the
same existing positive-size files. Preserve all applied/provenance/payload roots.
Stale socket files are handled only by the ordinary provider's ownership guards;
absence of a process does not authorize legacy ownership reconstruction.
Missing disk/proof, unexpected owner, layout drift or pending conflict stops the
operation for root disposition. No `--force`, reset, fresh image creation,
maintenance conversion or manual applied/socket/pending edits are in this package.

**Cold boot has a real kernel consequence.** Retained node1 is exact
`/nix/store/zv0wss6qmc5s1ip995ycf66nb5b61pr1-vpsadminos-system-dev-node1-26.05.git.ccd51ed`,
with recorded kernel `alkl9mci57k88bzql9n7rh609q9c5d73-linux-6.12.118`, initrd
`l4kvhdwirdl7p4kv5rkrrqgpylwwqamw` and squashfs`2i893z5l9nh4p903bn7xyzqx75qcsij2`.
The expected new node boot is6.12.118; historical running6.12.117 cannot survive
runner loss. This is booting the already-applied descriptor, not selecting52eb
or e9d node software. Retained services descriptor boots its recorded6.12.117.
Accept only exact recorded systems/boot payloads and full guest residency/root
proof, plus actual postboot kernel identity; do not preserve a false continuity
claim or rewrite old results. A services-only update subsequently retains node
payloads and does not switch its kernel. Any unexpected actual identity requires
diagnosis, not a node update or rollback. No host upgrade is implied.

**Finite execution/check scope:** public start still performs selected-source
configuration construction and runner realization; public services update performs
its selected services build. Owner0 binds their actual input graphs and missing
work, reuses identical resident derivations and retains the existing space,
material-build and unexpected-local-kernel guards. No kernel build, OS campaign
or new VM fixture is authorized. Start boot-target projection retains all applied
guest descriptors; services-target projection replaces only services payloads.
A build failure may publish result-config without activation: reconcile that
actual effect, retain original applied/pending evidence and use the ordinary
same-target forward recovery. No automatic whole-old-envelope/database restore.

After ordinary boot, owner0 obtains the minimal real schema/data/source baseline;
after update, bind exact1b declaration SHA256
`8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714` in the
closure and loaded sole OOM3/10 across API/supervisor/database, followed by the
already-scoped authenticated PHP/React checks. Preserve frozen0d1/25c8/1b/64665,
report22/evaluation20 saved membership and5/10 snapshot, all data/VPS/mail,
credentials/BFF sessions, seedcs, retained cache and capture SMTP. The accepted
64665 reconcile is not repeated manually. No rematch or historical relabeling.
Root already accepts necessary retained start for the running demonstration;
no renewed user approval for the profile scope is required. Root owns operation
release and owner0 its complete plan; source preparation is now sufficiently
specified. Only this locked note changed; all architect commands terminal,
capacity returned.

## Nov22 authorized selector activation — current immutable baseline

**Sufficient owner2 source brief.** Session/roster44 and saved architect0
Astra/xhigh/workspace_write reverified; prior packages terminal. The user's
“you can proceed with the workspace change / profile switch regarding the policy
limits” is recorded by root in [state.md](state.md). It covers this selector and
profile activation; default integration, host upgrades and lifecycle remain
outside it. Root allocates execution/current machine ownership; owner0 retains
the demo. This assessment performed no build/evaluation, source/ref/profile/claim
change or guest probe.

**The selected package still lacks the selector.** Current
`/nix/store/xyyxqzxl8s6w20idl6mpwwx2zmqi0dn5-dev-workspace-0.2.0`, deriver
`/nix/store/cwpilan6licyrgmmag0ryirbr1sqyrqj-dev-workspace-0.2.0.drv`, installs
extension tools `v2c0db4q8090farqmrvwi1dlm4kfc9mb` from immutable source
`/nix/store/jacbqhagyhqx2ri78977ivcl03q8q72s-source`; its provider has no
`incidentPolicyFile`. Its actual workspace source
`/nix/store/jsxqf2y19k7rvk0ngk5rb1nhsp422xxq-source` matches **all655 committed
non-tracking files** at workspace `f6bcb4c4d7c4d3275657734bebc28e763e11a52a`,
tree `4e5413f05c031409ee58d1ade01477f9f91fa545`. Use that exact immutable
integrated source as the own-feature base. Deployed source
`cc6265625091da2ed1466d5ee39e7febc286fb4a` differs from f6b only in18 tracking
paths; do not adopt a peer checkout. The ordinary peer's
[current record](../2026-11-11-pi-codex-migration/state.md) and
[merge preparation](../2026-11-11-pi-codex-migration/tmp/pi-usability/backend-contract-followup/merge-preparation/merge-ready.md)
retain deployment and reviewed integration lineage; those are reference evidence,
not present ownership proof.

**Preserve the complete current38-node graph and settings.** Actual lock SHA256
`74cc383ca1f14cee9f92161f7763bc7081fbe35fff1834708cce6edc4c266d86` selects
extension `d76bd681c6db981907a52c187a3298549af87ab0`, generic
`0abe5fe48955b1bcdc8cc368fcb27e11e0676f70`, codex-web
`3209aa7bf93e2c7067b07494d1b254741812d714` and Pi
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`. Only extensiond76 becomes reviewed
`ca7d8bdf982ef459fe4e09ac3740e0ea2edfcc36`: change `flake.nix` and regenerate
`flake.lock` through its existing input. Keep the direct nested generic override,
all other locked identities/follows, native/runtime/worker selection,
`.dev-workspace.json`, site/team/coordination/machine identity and Pi models/providers
unchanged. Existing profile target remains repository origin
`github.com/vpsfreecz/vpsfree-cz-configuration`, name
`cz.vpsfree/machines/aitherdev`, with the exact legacy alias bridge.

One already-settled build prerequisite also carries forward: current AGENTS is
still18,185bytes, SHA256 `7c6fe0170bd9806415c51bf2261e80869c6a0f3072a5d531301e7fe52ecaac28`,
and projects.md4,106bytes, both byte-equal to the earlier failing base. Reuse ONLY
the accepted relocation in workspace `ecefa547c2aa2c6a5e2a832774567990d51d3562`:
`AGENTS.md`15,341bytes and `docs/agent-instructions/projects.md`7,453bytes,
including its one-LF EOF correction. Every instruction/anchor and the unchanged
16KiB test remain; the earlier reverse-splice proof applies to the identical
starting bytes. Thus the complete source boundary is **four existing files**, no
runtime or instruction rewrite. Preserve old92rz/kcgi roots, ecefa/fdcca checks,
review, literal dirty metadata and failure labels. Old92rz selects caba66/0bf443
and would replace the current runtime/codex-web; its acceptance is not authority
to activate it. Only those two lock nodes plus the extension differ between its
lock and the current lock; Pi and all remaining nodes agree.

**Host contract, not a host deployment:** configuration
`58cbe758efb9b38c8b0a423bb6fa89ddcc418d62`, tree
`0050025e1799fe5242ceba6a9bb9c96eb1c2ae01`, is the matching immutable integrated
reference in `/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git`.
Its `devWorkspace` is exact0abe, NAR
`sha256-nQLcoU71l61Kdw9dAZ/mXGkZ4K4oTuEgulIf69VR594=`, and its site fields match
the selected workspace registration. Owner2 may prepare its own exact source
reference for `bin/check-dev-workspace-deployment --workspace-root <own-final-feature>
--configuration-root <own-exact-58c-source>`. Do not repin declaration1b or use it
as this contract reference. Retained deployment evidence distinguishes actual
H9acd/systemc77/native0.169 from later source-H42c/58c; H599/native0.170 was not
activated. The current `/run/current-system` link remains
`/nix/store/c77zq8lh6fcaaq03fcv8h1i5d4xijzic-nixos-system-aitherdev-26.05.20261113.f1e5c35`.
No host upgrade is indicated by an extension-only change; normal package/host
compatibility admission must still pass, with no equivalence or live-health claim
inferred from source equality.

**Acceptance and next step:** owner2 proves the four-file diff, exact38-node
preservation, unchanged core settings, relocated-byte/route preservation and the
unchanged focused instruction test; run the existing deployment-contract checker
against58c and normal quick hooks. Supply affected final review/history evidence,
preserving original W749/W5 and deployed/ref lineage without replaying obsolete
runtime pins. Realize the needed final package and affected declared composition
checks after release/review; reuse successful outputs only by actual derivation
and input identity, not old source PASS. No generic runtime/VM campaign is required.
Bind the new actual catalog to ca7 and its package source; root then uses ordinary
`workspace-host switch --source <own-reviewed-feature>` with exact session env and
its current configured machine claim. Preserve compatibility/transition journals
and forward recovery; an older candidate is not rollback. No fresh user approval
is needed for the already-authorized switch, while any new consequential scope
returns to root.

Owner0 then uses the selected public provider's existing `incidentPolicyFile`
with frozen config1b file `configs/vpsadmin/api/incident_escalation.rb`, SHA256
`8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714`, and the
ordinary services-only update. Preserve managed preStart ownership, all three
configDirectory consumers and sibling files; bind actual closure bytes and loaded
3/10 before authenticated acceptance. Preserve report22/DB/mail/VPS state, BFF
secrets/session store, seedcs, OS52eb guards, old node/hosttools/export/kernels,
retained cache and same-target pending recovery. Templates64665 are already
reconciled: no repeated reconcile, reset or rematch. Source allocation can proceed
now; owner0's independent current-demo preflight remains separate. All architect
commands terminal; design capacity returned.

## Nov22 targeted-delete semantics — reconciliation supersedes retry

The original [cleanup receipt](nov22-test-image-cleanup.json), SHA256
`9b6468d99ddae737b3696419d55d5e7bf9c1e5c8d74b5b123c32d168c8f3b227`, remains
literal:16 external roots retired, one12-image targeted delete exited1 and
freed0bytes, all effects joined. Its first21vmy image had no reported GC roots,
but still had stored config referrer
`/nix/store/acdfrkb9ix2bjn3irp7s0vbpzbxlyj06-os-test-alerts-incident-escalation.json`
plus its self-reference. The254,347-byte config is already backed up and hashed.
Installed Nix2.34.9 `--delete` help defines targeted GC with liveness/referrer
protection: root absence alone is not sufficient to remove a still-referenced
image. The finite correction, while paths exist, is to include its unused native
config output in the deletion set, not bypass liveness. The only permitted
potential extensions are the12 exact `files[].config_backup.resolved` outputs
already bound to the retired roots, with original backups preserved. Any future
remaining-set operation requires actual roots empty and actual direct referrers
contained within that finite set (self-reference allowed); extra/protected
referrers refuse, with no automatic scope expansion or new root retirement.

**Current root steering b90864e0 supersedes a24-path retry:** root has since
observed11of12 image outputs absent, onlyd90z remaining, protectedbfs47 present,
and free108,146,356,224B. These are root's observations, not architect rechecks;
no actor/cause or reclaimed-byte attribution is yet established. Do not replay
against vanished paths. Owner3 now owns only bounded ordinary-GC-journal and
remaining-effect reconciliation1acc5fa4; no new delete/GC is released. A future
d90z decision depends on that result and its actual remaining referrers. Preserve
original zero-freed failure, all backed-up config bytes/logs and protected97roots,
92rz/kcgi/bfs47/demo/profile/recovery/peers. No broad GC, ignore-liveness, direct
store unlink, source change or process stop. Architect read only saved receipts
and installed help, reverified session/roster/settings, made this locked note and
performed no new store query/inventory or deletion; capacity returned.

## Nov22 requested Nix test-image retirement — exact store scope

Session/roster44 and architect0 Astra/xhigh/workspace_write verified; prior work
terminal. The user's47GiB is accounted for by13 immutable
`/nix/store/<hash>-nixos-test-disk-image/nixos-test.img` files:50,722,615,296
allocated bytes (47.24GiB),81,073,799,168 apparent bytes (75.50GiB). This is a
measured pathname category, not a captured portal API label. The prior Nov19
three writable test images remain absent; the bounded ordinary `/tmp/os-test-*`
scan found no remaining image files. The separate protected demo state has
services-root.img12,884,951,040 allocated bytes and node1-tank.img632,578,048
(12.59GiB total;32GiB apparent), under
`.dev-clusters/vpsadmin/clusters/2026-10-30-oomd-abuse-policy/state/`.

**At discovery all13 store outputs were rooted: zero presently unrooted image
bytes. Retiring the exact old own-test roots below makes12 outputs/46,760,964,096
allocated bytes (43.55GiB) eligible for targeted collection, subject to final
no-use checks and Nix liveness.** Root accepted the category finding and owns the
execution release; the user's request authorizes demonstrated unused-image
retirement, not a profile switch or cluster/session lifecycle change.

Each table hash denotes the exact store directory
`/nix/store/<hash>-nixos-test-disk-image`; allocated/apparent measurements are for
its `nixos-test.img`. Retire only `config.json` symlink in the exact listed run
root, plus the four additional root links specified afterward. Preserve all
other files, logs, results and extracted diagnostics. No whole-tree removal.

| Store hash | Allocated bytes | Apparent bytes | Exact own-test run root (`/config.json` is the root link) |
| --- | ---: | ---: | --- |
| `21vmybk9vrlnqp7zi6w78hjqbg0xf5df` | 3,590,619,136 | 5,330,960,384 | `/tmp/os-test-20261118-oomd-g1-ee9025-6c1a/os-test-alerts__incident-escalation-4593dbf6` |
| `cgl2r7mhq47mq6l8bhqlf4c1h0jl0idr` | 3,590,676,480 | 5,329,911,808 | `/tmp/os-test-20261118-oomd-g1-d304-419a/os-test-alerts__incident-escalation-4593dbf6` |
| `mv0gh8xf1lkqak8h6n456idlhsyl5hyg` | 4,202,844,160 | 6,034,554,880 | `/tmp/os-test-20261118-oomd-webui-d304-e163/os-test-webui-fd1a3b33` |
| `5jl0jmcd22ljl9qw0b7dphy86q8ld3xh` | 4,202,803,200 | 6,034,554,880 | `/tmp/os-test-20261118-oomd-webui-0117035-61d7/os-test-webui-fd1a3b33` |
| `rr8kfaqc8qxmwdy8r2srbvb9aq14x1vz` | 4,202,971,136 | 6,034,554,880 | `/tmp/os-test-20261118-oomd-webui-ee474f-normalized-cd4a9301/os-test-webui-fd1a3b33` |
| `xn35b6l8kdc26cjzrbg4rml9zhvrnr0y` | 4,203,069,440 | 6,034,554,880 | `/tmp/os-test-20261119-oomd-webui-bcc5-976e3528/os-test-webui-fd1a3b33` |
| `clsmcpi31cc4ab21g5vq7mxmmdrszvbp` | 4,202,987,520 | 6,034,554,880 | `/tmp/os-test-20261119-oomd-webui-bd18-recovery-6fb1070a/os-test-webui-fd1a3b33` |
| `67if5g74mnhbdf28pb13xbmgl0il86w1` | 4,203,024,384 | 6,034,554,880 | `/tmp/os-test-20261119-oomd-webui-followup-0d1-1ca3a27d/os-test-webui-fd1a3b33` |
| `zjp6mp7nhhq8pafpsygr38vajjqhsnbg` | 3,590,778,880 | 5,330,960,384 | `/tmp/os-test-20261118-oomd-alerts-de4-clean-c7ee18d0/os-test-alerts__incident-escalation-4593dbf6` |
| `d90zklvp65w96qhjdjar4pgazpsr3gy9` | 3,590,385,664 | 5,329,911,808 | `/tmp/oomd-quota-diag-20261116-owner3/os-test-tasks__dataset-expansion-enforce-and-resolve-e2924ff6` |
| `g9jdf1pdisjqydv25mmp189mg1kiiq8p` | 3,590,410,240 | 5,329,911,808 | `/tmp/oomd-smtp-20261116-owner3/os-test-alerts__incident-escalation-4593dbf6` |
| `vsbaggfph4kk736zqm3azwamvrrqnnz1` | 3,590,393,856 | 5,329,911,808 | `/tmp/oomd-smtp-final-owner3/os-test-alerts__incident-escalation-4593dbf6` |

Four images also need retirement of these exact own-session evidence root
symlinks, relative to this tracking directory; old retention was for completed
verification/reuse, not a current fixture allocation:

- d90z: `nov16-quota-diagnostic/admission/gcroots/remaining-construction-v2-82c`.
- g9jd: `nov16-smtp-admission/gcroots/constructed-v2-f9`.
- vsba: `nov16-smtp-admission/gcroots/final-constructed`.
- zjp6: `nov18-reusable-policies/alerts-de4/retry-clean-de4/actual-config-output-root`.

Owner3 confirmed the first three packages terminal, no known remaining allocated
execution/recovery/fixture need: [quota accepted handoff](nov16-quota-diagnostic/admission/brief.md),
construction44d4ef05/single-scenario2c1d4e28; [SMTP handoff](nov16-smtp-admission/brief.md),
construction4945581d/failed runtime98ac5789 and final construction9d835ea2/runtime
ff1a51f2. The zjp6 [alerts receipt](nov18-reusable-policies/alerts-de4/retry-clean-de4-receipt.json)
is terminal PASS/all joined. PHP receipts under nov18-postreview-webui and
nov19-php-usability retain exact PASS/failed/joined outcomes; original ee9025/d304
failure ownership is also bound by the accepted Nov19 cleanup receipt. The d304
alerts native result is `expected_success`. All twelve current run roots have
no enclosing `.keep`; native `.lock` is absent, and failed runs lack a result
file. Do not synthesize either or weaken the host collector's seven-day policy.
This is explicit creator retirement with saved ownership/effects proof. Before
unrooting, owner3 retains exact config target/bytes in existing evidence where
needed; retiring a root does not rewrite an earlier receipt or its result.

**Protected thirteenth output:**
`/nix/store/bfs47mz1mxsna7bk1mydcdjfnc38kkh3-nixos-test-disk-image`
contains3,961,651,200 allocated/12,884,901,888 apparent image bytes (3.69GiB
allocated). Actual roots are registered demo
`maintenance-payload-a5203eae22d5e8f60f5672ec36a84f0c67984f7398afe538b65207e88a6e8ce8`
and `maintenance-source-df7a7d0e378408b9521fad23a03a12406c7262e4eac187f99c501ef156255361`
under that cluster directory. Preserve it for the existing demo maintenance/
recovery contract even though it is named a test image. No other peer/profile
root was reported for the12 candidates. Preserve92rz candidate, kcgi source and
all97 retained package/check roots, current profiles, KB/old-state recovery,
backups, credentials/mail/report22, peer data and all diagnostic logs.

**Owner3 execution boundary:** immediately rebind the16 external symlinks and12
store outputs to exact targets/inodes/devices; exclude any changed ownership or
new dependency. Complete existing privileged FD/cwd/mmap/mount/loop/file-lock/
backing-image checks and `.keep`, terminal/recovery/current-check checks; relevant
unreadability skips that candidate. Use existing native locks nonblocking where
present; never manufacture a missing lock/result or stop a runner. Current
installed SSH authorized-key restriction and known-host ED25519 still match the
previous strictly verified `root@172.16.106.40` read-only transport; owner3 verifies
actual privileged guard success. Preserve backing images and registered state.

Then remove only the admitted external root symlinks, retaining their receipt
and config evidence; never directly unlink anything inside `/nix/store` or
`/nix/var/nix/gcroots`. Use the installed documented targeted GC operation:
`nix-store --store unix:///nix/var/nix/daemon-socket/socket --delete <the admitted
exact store directories from the table>`; NEVER `--ignore-liveness`. Installed
help defines this as a targeted `--gc` that refuses root-reachable paths. No
whole-store GC, profile pruning, collector-age override or store bypass. If Nix
refuses a still-live target, preserve/report its concrete dependency; do not
expand root retirement automatically. Record actual native removals/freed bytes
and before/after df; the measured image allocation is potential image reclaim,
not a guarantee of filesystem delta or complete closure reclaim. Stop when the
admitted set is collected or explicitly refused; no campaign follows.

**Read-side effect/limit:** bounded ordinary `nix-store --query --roots` commands
all exited0, but the daemon printed stale auto-root removals during the clsmcpi
query. Captured prefix identifies auto/ddhq4gnfjvabx7r9i54xcnszz9rn2blz to an old
9e2458aa/708ad0dd notification, then auto/iqkgklfhaqyw8a5k15bhkz5l4cil76gb to an
old bbd9a7da notification. The formatter retained only400 stderr characters, so
the full second target/any later warnings are unavailable. This unintended daemon
side effect was reported promptly to lead27ef3964; do not call that query purely
read-only or infer any store deletion. No explicit GC/unlink was invoked; further
Nix root queries stopped. No automatic repair/restore is authorized. Current
profilew25 is a point-in-time observation only, not this session's deployment.
Architect wrote only this locked note; all commands terminal, no own deletion,
new inventory tool, build, profile/claim, guest probe or lifecycle action.

## Nov19 workspace package blocker — two-file instruction relocation

**EOF layout clarification (owner2 5f743edf):** the original portal block's
1,774bytes include its inter-section separator. At the destination EOF, omit only
the final extra LF rejected by ordinary `git diff --check`; keep the normal final
newline. Destination is therefore7,453bytes (portal content1,773bytes), with no
instruction word, paragraph, route or heading change. The reverse-splice audit
must restore that one structural LF explicitly before comparing to fdcca; original
AGENTS reconstruction and the unchanged4,106-byte destination prefix remain exact.
AGENTS stays15,341bytes/1,043headroom; combined entry/procedure is22,794bytes.
This narrowly qualifies the literal destination/body sizes below. Owner2's existing
unchanged10-case/219-assertion PASS remains literal; the EOF-only correction needs
the adjusted byte audit and ordinary diff check/hooks, not an unchanged test rerun.
Preserve the first diff-check failure and tool-environment preflight refusal.

Prior design/cleanup packages are terminal; session/roster44 and architect0
Astra/xhigh/workspace_write were reverified. Owner2's exact
`fdcca6c8147d5f8a2e8636480458a4a3c094fb07` build remains FAILED, native13264
joined1 after2439.189s. [Failure scope](nov19-workspace-selector-preparation/realization/failure-scope.json)
and `realization/build.log` show the unchanged `agent-instructions` check failed
only its18,185-byte AGENTS limit (16,384);9 other cases passed,10 runs/219assertions.
Immutable fdcca AGENTS is byte-equal to inherited W749. This is a required package
prerequisite, not a selector-pin regression or a reason to relax the test.

**Owner2 source boundary, after root releases its reconciliation/window:** only
`AGENTS.md` and existing `docs/agent-instructions/projects.md` in this session's
workspace feature. Append two sections to that existing project-map procedure:

1. Copy the body of AGENTS `## Compatibility And Deployment` verbatim EXCEPT the
   complete paragraph beginning `Follow the mandatory Git procedure for repository
   claims;` and ending `recovery contracts.`; keep that paragraph verbatim in the
   core, including its `docs/coordination.md#machine-retention` link. The moved
   body includes every compatibility dimension, incremental/incompatible deployment
   condition, vpsAdminOS coordinated-update condition and migration/reset/guard
   restriction. It is1,510 UTF-8 bytes with existing paragraph spacing.
2. Copy the complete body of `## Portal backend interfaces` verbatim (1,774bytes),
   including capability refusal, common UI/Team/Fork parity, adapter boundaries,
   exception criteria, supported paths and authorization/cancellation/history/
   receipt preservation. No paraphrase, rule deletion or new policy.

Retain both original core headings/anchors as forwarding sections. Use this
compatibility pointer before the unchanged machine-retention paragraph:

```text
Before planning any feature, read the complete
[compatibility and deployment requirements](docs/agent-instructions/projects.md#compatibility-and-deployment).
```

Use this portal pointer below its retained heading:

```text
Before designing, implementing or reviewing portal/backend interfaces, read the
[portal backend interface requirements](docs/agent-instructions/projects.md#portal-backend-interfaces).
```

Expand only the existing project-map activity cell to `Selecting affected projects
or changing cross-project scope; planning feature compatibility; designing,
implementing or reviewing portal/backend interfaces` (one table line). Keep its
existing direct `docs/agent-instructions/projects.md` link. The full mandatory
read/re-read/unreadable-refusal routing contract stays intact. Destination titles
match the original headings and all existing project-map bytes remain unchanged.
This is an appropriate existing home for component boundaries and compatibility;
no new procedure, documentation framework or unrelated rewrite is needed.

**Preservation/size acceptance:** an in-memory splice of those exact blocks and
pointers gives AGENTS15,341bytes, leaving1,043bytes below the existing16KiB gate;
projects.md grows4,106→7,454bytes. Target this layout and at least1KiB headroom,
not a one-byte pass. Verify exact moved body equality and reconstruct original
AGENTS by reversing only the two moves, pointers and route-cell addition; require
byte equality to fdcca, and require destination's prior prefix unchanged. This
accounts for EVERY old instruction, not just test-matched phrases. No local link
in the moved bodies needs rewriting; the machine-retention link stays at its
original location. Keep all core/test-required merge, design ownership, saved
model/reviewer, final-history/migration and review-timing contracts untouched.

The source contract is the existing16KiB AGENTS test. The retained discovery
[limit note](../../notes/dev-workspace/2026-09-17-agent-instruction-discovery-limit.md)
records a historical32,768-byte automatic load, not a guarantee for every current
session. Entry plus this one routed procedure is22,795bytes; moving rules changes
retrieval, not total instruction meaning or a claimed universal token saving.
Verify packaged `workspaceSource` retains both exact files and routes; that source
already excludes only work/archive. Existing sessions must reread the changed
core and applicable full procedure. No fresh-session/runtime probe is required
for this unchanged routing mechanism.

**Small checks and delivery:** owner2 runs unchanged
`ruby test/agent_instructions_test.rb` (all10cases, existing pinned Ruby/minitest),
the byte/reverse-splice/relative-anchor audit and ordinary hooks; no test threshold
or test implementation change. Preserve the full38-node caba graph, ca7 selector,
flake/package/site/team/native settings byte-for-byte. Make a normal successor
commit; root arranges affected independent final instruction/history review before
resumed realization. Preserve inherited W5/deployed history and original fdcca
failure literally; shared master and peer branches stay untouched. After review
and explicit heavy-window return/release, resume only the necessary declared
package/check outputs, reusing successful outputs by actual derivation/input
identity and current availability. A changed workspaceSource may change workspace
checks; textual equality alone cannot transfer their PASS. No entire failed-batch
PASS, new default/runtime/pin, live/profile/claim/CI/integration/lifecycle operation
is implied. Architect performed source/evidence reads and this locked brief only;
root retains scope/release/acceptance.

## Nov19 requested unused test-image disposal — bounded owner3 package

**Access clarification:** owner3's unprivileged preflight read770 descriptor
directories and encountered690 additional PermissionError results; `sudo -n true` required a password, so nothing was deleted.
An existing supported host SSH route is now established: immutable H340
`cluster/cz.vpsfree/machines/aitherdev/config.nix` authorizes the aitherdev key
for root from127.0.0.1/172.16.106.40/::1. Installed sshd permits public-key root
login and the installed restricted entry matches the current public key. The
existing known-hosts entry for172.16.106.40 matches the installed ED25519 host
public key. Ordinary `ssh -T -o BatchMode=yes -o StrictHostKeyChecking=yes
-o UpdateHostKeys=no -o ControlMaster=no -o ControlPath=none
-o ClearAllForwardings=yes -o ConnectTimeout=5 root@172.16.106.40 'id -u'`
returned0, exit0. An earlier127.0.0.1 attempt refused unknown host identity;
no host key was added and checking was not weakened. Owner3 can use this normal
SSH transport for only its existing exact-three-file read-only guard, including
privileged process/mapping/mount/loop/backing visibility. Any remaining incomplete
inspection still skips disposal. No sudo/SSH/credential/runtime changes or new
privileged helper are needed; no process contents/secrets should be emitted.
This identity proof is not the guard itself and does not authorize extra files,
root deletion, GC or lifecycle actions. Root retains execution allocation.

User explicitly requested deletion of unused test images. Prior selector design
is terminal; this session/roster and architect0 Astra/xhigh/workspace_write were
reverified. Architect performed read-only inspection only. Root releases owner3's
execution; no runner stop, GC, reset or lifecycle action follows from this brief.
Read [host retention](../../worktrees/2026-10-30-oomd-abuse-policy/vpsfree-cz-configuration/docs/operations/aitherdev-disk-retention.md)
at frozen configuration1b4052, plus the installed cleanup helper. Prior
[state cleanup](state.md#cleanup-recovery-and-historical-evidence) and
[storage receipt](storage-cleanup.md) remain historical; the separate Nov10 KB
services image was already deleted and offers no new reclaim.

**Smallest candidate set is three files in two receipt-bound own-session runs:**

| Exact containing run directory | Disposable file | Allocated bytes observed |
| --- | --- | ---: |
| `/tmp/os-test-20261118-oomd-g1-ee9025-6c1a/os-test-alerts__incident-escalation-4593dbf6` | `services-root.img` | 5,330,989,056 |
| same alerts run | `node-tank.img` | 392,814,592 |
| `/tmp/os-test-20261118-oomd-webui-d304-e163/os-test-webui-fd1a3b33` | `services-root.img` | 6,034,649,088 |

Total11,758,452,736 allocated bytes (about10.95GiB); the20GiB logical node disk
must not be counted as20GiB reclaim. These are explicit own-run image-retirement
candidates, not automatically eligible whole trees. Retained state records the
alerts owned source/utility joined after its original CLI failure; the
[PHP failed receipt](nov18-postreview-webui/failed-receipt.json) records all owned
effects terminal. The [extraction receipt](nov18-postreview-webui/original-artifact-extraction.json)
binds already extracted original PHP trace/screenshot/context; preserve those
artifacts, logs, configs, roots and original failures. No remaining recovery use
of an image may be assumed away: owner3 verifies it before disposal.

Fresh bounded reads found no enclosing `.keep` and no matching runner/QEMU argv
for these two runs, but this is not a complete current reference check. Neither
run has the collector's required `.lock` or `test-result.txt`, and both are younger
than seven days. **Do not run global `nix-store-cleanup --apply`, reduce its age
threshold, manufacture completion/lock files or delete either whole tree.**
The supported distinction is explicit creator retirement under this user request
and root allocation, using saved ownership/terminal proof, not a collector sweep.

Owner3 preflight must bind each exact regular non-symlink file/inode/device and
allocated size; recheck path ancestors and `.keep`; verify the retained terminal
owner/evidence and absence of current check, reusable fixture, recovery or
registered demo dependency. Check current open descriptors/cwd/mappings, file
locks, loop/mount use and backing-image references using existing inspection
commands and recorded raw-image configuration. Acquire any existing owning
operation/run locks nonblocking; never invent a missing runner lock or stop a
process to qualify a file. If relevant visibility, backing relationships or
ownership is unresolved, skip that file and report the specific gap. Revalidate
identity immediately before unlinking only the admitted files. Preserve all
other run contents and record absence plus allocated/df before-after; concurrent
writes mean df delta is not exact attribution. No new cleanup tool is needed.

Shared recognized completed tests remain eligible only under the host's native
seven-inactive-day/terminal-result/available-lock/no-process/no-`.keep` rules;
none is selected by this bounded inspection. Unknown layouts and peer-owned
ad hoc/private test state are excluded, regardless of name or age. Do not extend
the three-file allowlist by glob. Preserve all `.dev-clusters` state, the current
services/node1 disks and report22/database/mail, KB parked/recovery images and
backups, isolated failed-build cache/evidence, all Nix store/root/profile/package
candidate inputs, and owner1/owner2 mutable outputs. Current demo processes were
visible using the separate `.dev-clusters/.../state` disks and remain untouched.
The observed shared filesystem free83,837,890,560 bytes is a point-in-time read,
not reserved capacity. Stop after the admitted exact-file removal and receipt;
no further campaign or source/guest operation is included.

## Nov19 selector consumer — corrected deployed dependency base

Prior design package is terminal. Architect0 reverified this session and live
roster44, retaining Astra/xhigh/workspace_write. Root accepts the explicit
published/deployed dependency base below. **This supersedes the later section's
9241 runtime assumption and its proposed consumer base; the single-declaration
selector contract and source ownership remain unchanged.**

Owner2 prepares its own workspace feature from exact
`749e4cc3639649711f2fa10327153ca759976c06` (W749, tree
`a74d15ee95188c9ef32743cd42a4a5b07867aba5`), published at
`git@github.com:aither64/vpsfree-cz-workspace.git`, branch
`2026-11-11-pi-codex-migration-pi-aitherdev-trial`. This is an explicit unmerged
dependency, not current default master. Do not replay its files onto9610 or
select9241. Retain the prior W5 history/review and deployed lineage literally;
this allocation does not establish default integration or authorize rewriting
that dependency. Later integration preparation remains separate.

The actual selected package `v31a7azi67rnl1rppzbvsgwaynvrxpc8-dev-workspace-0.2.0`
(deriver `58zvql0zzc1bv9bkqq3qvfx8g3svkcnf`, workspace source `bjf0v1nf...`)
uses extensiond76 and generic
`caba66cce8755398db768398749eebab86d5d97f`, with38 lock nodes. Root independently
matched eight package/settings files to W749. The only package-file differences
from default9610 are `flake.nix`, `flake.lock`, `config/pi-models.json` and
`config/pi-providers.json` (+592/-20); these are required installed composition,
not optional additions. Preserve the complete actual graph, including codex-web
`0bf44388b0bebc13b35155ee8e23746eb25f6d24`, Pi
`a22b888a58fe55b668cc45b80749ec88d4eb4ddc`, its locked inputs/follows, and all
site/team/native/provider settings. Owner2's new functional delta is only the
workspace `flake.nix`/generated `flake.lock` extension pin to owner1's reviewed,
published selector successor ofd76; no generic/runtime/configuration upgrade.
Evidence: [selected source proof](nov19-workspace-selector-preparation/selected-source-input-proof.json),
[selected derivation](nov19-workspace-selector-preparation/selected-package-derivation.json)
and [baseline discrepancy](nov19-workspace-selector-preparation/baseline-discrepancy.json).

The matching host-contract source is configuration
`340bb049ee7e0e9f82ff864ab74738129682a525` (H340, tree
`7296178bb6f88e845c07133a5b757d158ef15262`), whose `devWorkspace` is exactcaba,
NAR `sha256-nWwhjhosx3hQZlM0xK0AQQ2Gtn8n2G1hO61Y7mlaSTE=`.
Canonical immutable source is available through
`/home/aither/workspace/ai/vpsfree.cz/repos/vpsfree-cz-configuration.git` at that
commit; canonical SSH remote is `git@github.com:vpsfreecz/vpsfree-cz-configuration.git`.
No existing immutable checkout directory is claimed: owner2 may obtain its own
exact H340 source under normal preparation, then use that directory as
`--configuration-root` for `bin/check-dev-workspace-deployment --workspace-root
<own-final-feature> --configuration-root <own-exact-H340-source>`.
Do not use a peer's mutable checkout or substitute declaration1b for this check.
Reviewed1b and declaration hash8d923a remain frozen for the demo selector.

The retained ordinary-session [candidate handoff](../2026-11-11-pi-codex-migration/tmp/pi-usability/team-ui-parity/delivery-caba66/candidate-handoff.json)
and [activation completion](../2026-11-11-pi-codex-migration/tmp/pi-usability/team-ui-parity/delivery-caba66/activation/completion.json)
bind H340/W749/caba to system
`/nix/store/j4k1zx57ky3fkl8n6nlfq696dfxzs9z8-nixos-system-aitherdev-26.05.20261113.f1e5c35`
and applicationv31, with successful joined activation and postchecks. Thus no
additional host-system deployment is indicated for this selector-only delta.
These receipts prove the recorded deployment, not present machine availability;
historical claimad4 is not a current claim. Source alignment alone does not
activate the selector or prove new derivation equivalence.

**Next boundary:** root may release owner2 source preparation independently of
machine availability. Preserve exact graph/settings in the generated pin diff,
run the existing narrow composition/deployment-contract and ordinary required
package checks, and supply final history/review evidence distinguishing the
preserved W749 dependency from the new selector pin. Owner1 and KB work continue
independently. Shared user-profile switch still requires separate later user
authority, current ownership and normal transition/recovery checks; use the
ordinary public switch, then owner0's services update and loaded-declaration/UI
acceptance. No profile/host switch, claim, build, source mutation or runtime
operation was performed by this design package. All prior data, cache, OS52eb,
old-node/kernel, pending-forward-recovery and no-reset boundaries remain intact.

## Nov19 declaration selector — sufficient source and activation boundary

Prior gap package is accepted/terminal; architect0 reverified session/roster44
and retained Astra/xhigh/workspace_write. Root accepts the optional single-file
boundary in principle. **The source package below is sufficient for allocation;
shared profile deployment remains a separate authority dependency.**

**Public field:** `incidentPolicyFile` in the existing per-cluster `config.json`.
Absent or JSON null keeps the current selection exactly; otherwise require an
absolute host pathname naming one readable regular, non-symlink file. Reject
empty/relative paths, other JSON types, missing paths, directories and symlinks
before realization/activation. No cwd-relative expansion, URL/fetch, implicit site
lookup or Ruby execution during Nix evaluation. Parent directories retain normal
host path semantics; this is a trusted local-operator input, not a new sandbox.
Read that file once and use `pkgs.writeText "incident_escalation.rb"` to snapshot
its bytes. Build the selected directory from the existing fixture directory, or
existing storage-profile directory when that profile was already enabled, replacing
only `incident_escalation.rb` with the snapshot. Preserve all sibling files. Assign
that same directory through `lib.mkForce` to API, supervisor and databaseSetup
`configDirectory` when an override is selected; preserve the current absent/null
paths and storage-profile behavior. Keep the ordinary preStart link installation.
No Ruby loader/hot reload, managed-state edit or broader site configuration import.

For this demo select the absolute host file under its existing configuration
worktree: `configs/vpsadmin/api/incident_escalation.rb` at reviewed
`1b4052c798c0496369c5c67a55d2626f5fe2ecfb`. Owner0 binds its bytes to SHA256
`8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714`, and the
actual closure snapshot must have that same hash before activation. The pathname
alone is not provenance. No new metadata format or hash API is needed. Later host
file edits do not change the already built closure; a new selection requires the
ordinary services build/update. Null deliberately restores the original fixture
selection on a later update, without rematching or changing historical records.
Older providers ignore this new key: do not run an old provider update as recovery
for a demo that must retain the selected declaration.

**One source owner, allocated by root:** extension baseline
`d76bd681c6db981907a52c187a3298549af87ab0` (its provider flake/test.nix/README bytes
match installed cwy). Edit only `dev-clusters/vpsadmin/nix/test.nix`, its README,
and the existing `test/devcluster_nix_smoke.rb` harness/necessary small fixtures.
Use an isolated `--incident-policy-only` mode in that harness for quick real Nix
selection and tiny config-directory realization, without runner/VM/system builds.
Cover absent/null original selection; exact supplied bytes and all three equal
directories; invalid types/empty/relative/missing/directory/symlink; and enabled
storage-profile sibling preservation without enabling it in this demo. Use the
repository's pinned tooling, focused Ruby/syntax checks and required ordinary
package checks, then committed affected independent review. No application head,
provider shell, runtime protocol, schema or migration change; no host-migration VM
is indicated by this composition-only delta. Default JSON needs no new required
key because the input is optional; README documents its null default.

**Supported execution requires the shared selected package.** Actual installed
`v31.../bin/vpsadmin-devcluster` fixes the catalog. Its
`libexec/.workspace-host-wrapped:1627–1657` resolves the registered workspace and
holds `with_current_generation_lock`; `3803–3814,3853–3860` require the invoking
package to equal the selected profile. The candidate entry (`3820–3833`) is for
explicit switch/recovery, not ordinary cluster commands. Therefore neither an
unselected candidate wrapper nor direct tools/catalog/profile overrides supplies
the supported session-only route. Do not bypass those guards.

The smallest deployment package set is the extension selector commit plus a
consuming-workspace feature checkout's `flake.nix`/`flake.lock` pin to its exact
published revision. Preserve nested generic runtime
`9241a342a6ef4ca69148594e98cce7ddcfb459a6`, sibling inputs/follows, actual native
Codex/team settings, site configuration and provider/registration set. The current
workspace selects extensiond76 with that nested runtime; this is a narrow extension
replacement, not a general runtime upgrade. No host configuration source/system
change is indicated while the generic/host contract remains unchanged; the normal
`bin/check-dev-workspace-deployment --workspace-root <feature> --configuration-root
<current-compatible-config>` check verifies that boundary. Root must separately
obtain/allocate the shared user-profile activation and exact configured aitherdev
machine claim. Its public entry is **`workspace-host switch --source <reviewed
workspace-feature-checkout>`**, with the verified session environment and claim,
using existing preparation, compatibility, transition and recovery checks. A switch
can affect shared workspace services; do not describe it as session-only or invoke
it from this design package. No default integration authority is implied.

After that accepted selection, owner0 sets only this cluster field and performs
the ordinary services update. Bind actual changed services graph/derivers, reuse
application outputs only by actual identity, retain OS52eb/kernel/material/space
guards, then prove managed links and loaded digest/sole OOM3/10 rule across the
three component contexts plus pendingnull and authenticated report22/UI acceptance.
Completed64665 template proof needs no separate manual reconciliation. Preserve
all data/history/credentials, saved5/10 snapshots, old node/tools/export/running
kernels, isolated cache, CS seed field and same-target forward recovery. No reset,
rematching or extra integration campaign. The earlier live/source evidence below
remains literal; architect performed only source reads and this locked note.

## Nov19 current refresh — site declaration selection gap

The services update has activated accepted backend0d1/React25c8 with pendingnull;
owner0 also completed the64665 template reconciliation and stored-field proof.
The remaining declaration activation is blocked by an actual composition limit,
not missing report history. Owner0's saved
[config-path readback](nov19-demo-refresh-execution/private/config-path-readback.stdout)
and [installation ownership](nov19-demo-refresh-execution/private/config-install-owner.stdout)
bind all three component links to
`/nix/store/q5m7q104c9y3js539sdkmrjdyhym79h6-api/incident_escalation.rb`, SHA256
`5bc3d69c65e3b8d9b6c429a98301a22ed472ff12f367464613da976bc2da7335`:
the ordinary test declaration (manual_category/manual_content/oomd, OOM5/10).
The API preStart `j758i2` and backend `nixos/modules/vpsadmin/api-app.nix:122–129`
recreate these managed links on restart. **This supersedes the earlier proposal
to install persistent regular declaration files manually.** Owner0 stopped
before changing the managed paths; no additional live probe was needed here.

There is no existing supported declaration selector in installed provider
`cwyjgqfsslzclvim4pcrrwxwgvm6jqif`. Backend
`tests/configs/nixos/vpsadmin-services.nix:497,512,530` selects the test config
for databaseSetup/API/supervisor. Provider `nix/test.nix:50–55` merges the public
cluster JSON, but no consumed key selects an incident file/configDirectory or
extra module. Its only configDirectory override (`1517–1521`) is the storage
profile, whose directory (`365–372`) still copies that incident fixture.
`configSourcePath` only supplies the configuration mount (`998–1034`). Neither
mounting the site source nor enabling that unrelated profile selects1b.

**Smallest proposed change, pending root disposition:** add one optional public
per-cluster declaration-file input in the provider's existing config/composition
surface, default absent. When selected, closure-copy exactly that file as
`incident_escalation.rb` over the otherwise unchanged effective API config
directory, preserving any existing storage-profile composition, and pass the
same resulting directory to the three existing `configDirectory` options.
Select reviewed configuration `1b4052c798c0496369c5c67a55d2626f5fe2ecfb`,
`configs/vpsadmin/api/incident_escalation.rb`, SHA256
`8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714` (OOM3/10).
The necessary owner files are provider `dev-clusters/vpsadmin/nix/test.nix`, its
existing default-config/README interface and focused composition checks. Keep
absent behavior unchanged and reject an invalid selected file before activation;
prove exact selected declaration plus unchanged sibling config content and
identical selection for all three components. No new API/schema/policy engine,
full production config-directory import or runtime reload mechanism is needed.
This is a concrete required source boundary, not authorization to implement or
install a changed provider. Root owns that allocation and normal acceptance.

After an accepted provider selection, owner0 retains the ordinary services-only
build/activation and authenticated acceptance. Reuse completed application outputs
only where actual derivation/input identity permits; bind the changed services
composition and its selected declaration rather than claiming equivalence.
Preserve completed template proof without another manual reconciliation. Confirm
the managed links target the reviewed declaration and running processes load its
digest/sole site rule3/10; preserved report22 must still show saved memberships and
historical5/10 snapshots. Keep OS52eb graph/kernel/material/space guards, old node,
host tools/export/running kernels, retained isolated cache, CS seed field, all data
and credentials, and same-target pending/forward recovery. No managed-link
replacement, preStart suppression, signal/private-helper workaround, broad profile
or topology change, reset or rematching. Architect changed only this note; owner0
retains demo/source/heavy ownership while root settles the provider dependency.

## Nov19 current refresh — accepted build-source preparation

Root accepted the terminal pre-copy/pre-pending failure in
[update-build-failure-receipt `9e464ab1`](nov19-demo-refresh-execution/) (all19
bindings verified) and released owner0 through `2c3ab5bc`. The applied envelope
remains unchanged, pending is null, and the running services/API remain011.
This is a failed build attempt, not an activation or test pass.

The first-party gem helper copies the provider's complete path input before
entering `libnodectld`; the separate `vpsadmin-source` filter does not protect
that gem build. The failed source included ignored `libnodectld/.gems`, causing
recursive gemspec selection to choose mini_mime. Preparation is limited to
reversibly isolating that sole confirmed ignored/untracked/non-symlink directory
outside the copied backend root, at a collision-free retained destination.
Preserve the cache, leave no replacement symlink and do not automatically restore
it. Keep every tracked byte/mode and force-tracked lock at exact backend
`0d1db93cd0d38b77f1e29c40ddd71b45581ecfff` unchanged.

Owner0 binds the newly selected library source/deriver and intended
`libnodectld.gemspec` selection, then performs **one corrected public services
attempt** under the existing graph/kernel/material-build/space, preservation and
forward-recovery contract. Removing the ignored input changes source/derivation
identity; neither the failed8glg nor prior clean-de4 library acceptance is reused
as a pass. No source/provider/dependency fix, metadata regeneration, ref change,
broader cleanup or additional design gate is introduced. Original failure and
no-activation evidence remain literal. Owner0 retains full execution/heavy/demo
ownership; this note only records root's accepted preparation and release.

## Nov19 current refresh — accepted services OS selection

Architect0 reverified session/roster44 with retained Astra/xhigh/workspace_write;
the prior package was terminal. Root accepted this bounded recommendation and
released owner0's existing refresh package through disposition `3224bb1a`.
Only this tracking addendum changed; no source, OS checkout, ref or provider was
modified, and no Nix evaluation/build or runtime operation was performed here.

The installed provider `cwyjgqfsslzclvim4pcrrwxwgvm6jqif` selects an existing
`worktrees/<slug>/vpsadminos` directory, otherwise the canonical local
`origin/staging`; it does not fetch. There is no ordinary update/config exact-rev
selector. An exact-old ordinary checkout would be a separate source-selection
change, not an existing retained-config switch. Revision metadata and the old
`/mnt/vpsadminos` export do not select the build input. Use the accepted normal
`vpsadmin-devcluster update 2026-10-30-oomd-abuse-policy services` route with
**`52eb4de029f385c3e2d1b614d9b6ff32bbfb29bf`**, tree
`c998787d3499daaa9d1f77474710176631a0dae5`, in both provider OS inputs.

Compared with retained `ccd51ed38ebffa2e744f7f8847668bc2e3413378`, immutable Git
contains one commit changing only `flake.lock` (6 additions/6 removals): stable
`nixos-26.05` changes `b349185bb79c7cf7ad8ea8c097931730bf473c71` →
`f68407657ad294471eb4b2e65d193df26edf729f`; unstable changes
`d5cc6833999746cffdfe0598f7bc801a57b887a9` →
`04906337b6d53e8bb0eaf0470ae9f070a4d4eb55`. Stable is the actual services
NixOS/module/package basis; the provider also declares WebUI and status nixpkgs
follows to it. Unstable is not this services package basis. OS module, runner,
disk-interface and kernel-catalog source are unchanged, including the NixOS VM
`linuxPackages_6_12` default. **This is a changed input graph, not package,
derivation or deployment equivalence, and proves no cache availability or size.**
Stable package changes can affect services dependencies and kernel derivations;
source inspection alone does not establish their realized versions or cost.

Owner0 retains the existing actual selected configuration/full graph and
missing-work assessment, kernel/material-build/space guards and final services
proof. Do not infer permission for a local kernel build from this input acceptance.
The unchanged provider projection preserves every non-target guest descriptor,
old host QEMU/virtiofsd, recorded OS export, topology/networks/mounts and reused
services root image. Only services payloads are selected for realization/switch;
the normal API restart and node refresh remain part of that operation. Existing
node software and running kernels remain old; no node software update, reboot,
reset or new test campaign is authorized. Selected services kernel/initrd paths
may change without changing the running kernel. Preserve DB/history/report22,
mail and session credentials, sole approved CS seed-language field and existing
acceptance. The pending-before-copy/activation and exact-residency promotion
contract is unchanged; failure stays pending for supported same-target forward
recovery, with no automatic downgrade or restore.

Evidence: [os-selection-drift.json](nov19-demo-refresh-execution/os-selection-drift.json)
and [selected-provider.json](nov19-demo-refresh-execution/selected-provider.json).
Within that selected installed provider's `share/vpsfree-dev-workspace/dev-clusters/vpsadmin/`,
`bin/devcluster:693–710,790–801,850–876,1458–1512` establish selection, both
overrides and update order; `flake.nix:4–20,73–169,207–216` establishes follows,
projection and services evaluation. Immutable OS `52eb4de:flake.lock` root edges,
`tests/make-test.nix:39–51,133–153` and
`tests/configs/nixos/base.nix:104–111` establish the stable evaluator and retained
kernel-family default. Root owns execution acceptance; this record adds no gate.

## Nov19 follow-up — simpler legacy settings and completed demo refresh

Prior timeout-disposition package is terminal; architect0 confirmed capacity and
reverified this session/roster44 with retained Astra/xhigh/workspace_write. This
bounded design changes tracking only. Sources inspected are backend
`bd18b570300d1b66fbe29fac1b74ce93e4768ae1` and React
`25c8db48d087a1f77a9c1dae02c2cdcae0f4e098`. **The following PHP source package is
sufficient for immediate root release, independently of runtime diagnosis.**
The user's latest simplification supersedes the earlier explicit-mode/numeric-
prefill design for legacy PHP only; React's form is unchanged. Final copy and
bilingual candidate successors are root-owned in
[followup/root-copy.md](nov19-php-usability/followup/root-copy.md).

**Owner4: one small PHP package.** In
`webui/forms/incident_policy.forms.php`, render just two ordinary number inputs
and Save. Initial VALUE is the raw `warning_limit_override` /
`stop_limit_override`: null becomes blank; a non-null value remains explicit even
when equal to the default. On POST, trim each ordinary string independently;
blank means null, a filled positive integer means an explicit override. Reject
arrays/noninteger/zero/negative/overflow values and preserve API cross-limit
validation. Never infer inheritance from numeric equality. Remove the required
`*_limit_intent` inputs, per-field selectors/reset buttons/pending labels and the
both-field reset. Retain admin/action-capability checks, POST/CSRF, failed drafts,
server authorization and authoritative Show readback. An untouched blank sibling
stays null. A known inherited effective value may be placeholder/helper only when
that field's saved override is null and the effective value is valid; an override
hides its inherited target, so clearing it gets only the generic inheritance hint
until save/readback. Current effective values remain in the existing summary table.
Do not relabel an old custom value as a default or introduce new API metadata.

Remove the page's redundant Incident policies heading/link-only introductory table;
keep the general VPS heading, separate sidebar report/policy entries, per-policy
sections/history links and shared Automatic shutdown editor. Preserve
`vps.incidents.page` as a nonvisual page-container landmark using existing rendering
primitives (the page intent survives); do not attach it to a different policy or
retain an empty visible row. If this requires the route-local container, the
`incidents` branch in `webui/pages/page_adminvps.php` is included. Keep
`.policy`, `.settings`, `.permission` and sidebar IDs/routes unchanged.
Render current-status periods as localized **Last N days**, from the API period
fields (7 and30 today). `vps_incident_period_table` also renders saved report
snapshots: pass current/historical context at its call sites, keeping saved periods
relative to their saved evaluation and never substituting current data. Remove
Automatic shutdown from `vps_incident_filter_form` **and** stop forwarding its
legacy `incident_enforcement_enabled` query in `vps_incident_list_filters`; otherwise
an old bookmark could apply an invisible filter. Ignore that old UI parameter,
without changing the API's supported filter or shared permission false value.
Preserve the useful policy/status filters and separate report-list policy select.

Owner4 also owns removal of obsolete incident-intent/reset handlers in
`webui/public/js/vps.js` (retain the local unit helper only if still used), required
gettext POT/CS PO/MO, `webui/tests/Regression/IncidentPolicyTest.php` and
`tests/playwright/webui/specs/incident-escalation.spec.cjs`. The report-filter cursor
handler belongs to `incidents.forms.php`'s route-local AJAX_SCRIPT and stays intact;
report pages do not load vps.js. No model/API/schema/engine/selector/mail changes.
Owner4 retains technical fix ownership through normal checks/commit and root's
exclusive backend window. Quick checks cover blank/null and explicit equal-default,
edit-one/blank-sibling, custom-clear with unknown inherited target, invalid0,
failed POST preservation, no-JS submission, member write denial, false shared
permission, removal of invisible URL filtering, current versus saved periods,
landmarks and unchanged saved multi-policy/owner privacy. Inspect normal and failed
CS/EN rendered forms. Update existing assertions instead of adding a framework.
After committed source/quick checks and affected independent review, use the
existing targeted PHP browser scenario in root's allocated heavy window; earlier
bd18 acceptance remains literal, not a pass of the follow-up.

**KB source: existing owner0 stream after PHP handoff.** Root's candidate successors
in `nov19-php-usability/followup/` change only the settings-action/explanation
paragraphs (EN SHA256 d48f6ab77883a89c2a7b5981cc47c641546fe912156002c37d4833e51a128c87;
CS1b3fda4cda17701b91445c8281a004b385058e6b2ab2c006be9c25425e91022c).
Preserve previous accepted candidates. Reconcile existing
`vps.incidents.open` / `vps.incident-reports.open` annotations and
`contract/navigation.yml` source/related fingerprints against the final PHP file;
no new route or screenshot concept. Five final public backend pins and normal
source contract checks remain the same later dependency. Current-page geometry and
VPS-list filter removal require impact assessment of the existing six bilingual
capture concepts; canonical media/runtime/capacity remain parked, not resumed by
the demo refresh. No SDK generation or migration is needed for this PHP change.

**Report22 cause established; no history repair.** Owner0's
`nov19-demo-refresh-preparation/report22-finding.json` binds actual report22 to
owner3/VPS2 and evaluation20: matched1/recorded, saved counts10/10 and limits5/10,
with current owner still3. Global24reports/20evaluations/4actions are unchanged.
The live PHP `incidents.forms.php` (SHA256
ce6b5b9503814ba8c392bf70a1e865404f761b8af43ccdb2942142e8331fdc38) is mounted from
`/mnt/vpsadmin/webui`; its guard requires advertised matched and period fields.
Actual running API/supervisor/database011's resource omits all three, so the newer
PHP selects unavailable **before fetching the saved row**. The anonymous OPTIONS401
is not capability evidence; deployed source and saved-row proof establish the
cause. Do not fabricate no-match, rematch, relabel or expose private outcomes.
After compatible activation, verify this existing record renders its saved policy
and authorized link; no new incident or data repair is needed. Immutable011→bd18
comparison shows the original feature migration and schema.rb unchanged; owner0
still owns actual schema/readiness confirmation and ordinary recovery preparation.

Owner2's current public read proved metadata, entry, main and EN locale bytes
identical to resident old frontend0fb7, still serving “Warning limit reached” /
“Shutdown limit reached”; metadata stays unknown/dirty, externally bound to
historical b1fb by the retained receipt. Its evidence is in
`nov19-usability-feedback/react/demo-diagnosis`, with the explicit unverified-TLS
origin-authenticity limit. Clean25c8 already has the corrected incident-report
warning; no additional React source fix is indicated. Healthz proves BFF liveness,
not its revision. Owner0's fresh ordinary runtime proof, consumed by owner2,
binds the active BFF unit/process to oldjrcw and API/supervisor to011; both UI and
backend remain older. Their resource lacks the later matched/period fields, so a
React-only activation leaves a mixed-version seam. Owner2's final receipt ef9baa3c
binds the public and owner0-derived evidence. Previously accepted25c8 standalone
frontend/BFF outputs are currently absent, so ordinary refresh preparation must
resolve/realize and bind actual selected outputs; old acceptance is not present
residency or composition proof. Completion now includes a **data-preserving refresh of this
existing registered demo and authenticated verification**, not merely source
publication. Preserve its DB/VPS/reports/evaluations/actions/MailLogs/Mailpit,
credentials and BFF sessions/signing/config. No second reset/reseed, history rewrite,
production/default integration or session lifecycle operation is authorized.

**Owner0's supported refresh boundary is established.** Its
`nov19-demo-refresh-preparation/{current-input-summary,schema-compatible-bd18,
node-compatibility-scope,target-declaration}.json` bind the actual011 state:
pending null, schema SHA25686bd0dbc and original migration SHA2562eec970f equal
bd18, highest migration20261030180000 after20261006120000, no new migration.
After root freezes/reviews/checks the PHP successor and confirms those schema
hashes remain equal, the ordinary command is
`vpsadmin-devcluster update 2026-10-30-oomd-abuse-policy services`.
The provider's `refresh` command only prepares pools/devices and restarts nodectld;
it is not a services software update. Owner0's selected-provider inspection proves
update builds the services target, records pending before copy/switch, restarts API
and performs the node refresh, and promotes the descriptor only after exact
current-system/rooted-closure proof. Node1/disks/layout/session credentials remain.
A failed target stays pending for **same-target forward recovery**: no automatic
downgrade, old whole-envelope/database restore or reset. Preserve recovery inputs,
pending state and command effects until that ordinary path reconciles them.

Bind actual composed services/frontend/BFF paths and complete inputs during the
allocated build/update; they are unresolved now and are not the absent standalone
outputs by assumption. Retain capture SMTP, Mailpit, DB/reports/snapshots/actions,
VPS state, BFF sessions/signing/config/OAuth and original evidence. Current node/CLI
remains explicitly old source:011→bd18 changes nodectl/RPC-client use, not nodectld
server code; services-only update suffices for the requested existing read-only UI
acceptance and does not certify final node-CLI ingestion. Reassess only if the
final successor expands beyond the accepted PHP scope; no new event campaign here.

Owner0's final [refresh plan](nov19-demo-refresh-preparation/refresh-plan.md)
qualifies template activation: first bind actual provider selection of exact
`64665b3944da4ebf5045ef00f403e410ce88e3ad` and its normal reconciliation result.
The literal optional `vpsfree-mail-templates` directory is absent while this session
registers `vpsfree-notification-templates`, but alias resolution/build composition
was not exercised. Use the supported manual reconciliation only if normal loading
did not already achieve the exact template state; do not duplicate reconciliation
or change provider/registration. Current declaration hashes are fresh; historical
0440 modes were not separately re-probed and remain historical. After the compatible
API is installed, activate the regular
component-owned declaration files for API/supervisor/database and restart/load
through the existing procedure: current1efe/f3b4549a is5/10, target
`1b4052c798c0496369c5c67a55d2626f5fe2ecfb` / SHA256
`8d923a4af0c1e28a62fec5c2a0ce308ae089a1ea7ecab7e6529db8b8e18a6714` is3/10 with the
trusted selector. Config mounting alone does not activate it with storage profile
disabled. Do not edit saved evaluations to reflect new limits or recreate messages.

Finally verify actual served PHP/25c8 React assets and active BFF, compatible API
fields, report22's existing saved matched policy/link under its authorized owner,
current effective3/10 versus saved5/10, and unchanged data/owner/privacy baselines.
New incidental login records are separate from preserved incident/mail history.
No source publication or old package proof substitutes for this live acceptance.
Root owns final execution release and acceptance; this design allocates no command,
production/default integration, node-source upgrade or lifecycle operation.

## Nov19 old ee474f CI timeouts — bounded saved-evidence disposition

Architect0 reverified this session/roster and retained Astra/xhigh/workspace_write;
previous design capacity was returned. This assessment reads only the accepted
`nov19-usability-feedback/backend-history/publication/old-ee-ci-diagnosis/`
receipt a2f62654, sanitized job/runner logs, its existing ZIP and immutable Git
objects. Run **44414971213 attempt 1 at ee474f60 remains FAILED: 116/119 tests
passed, three failed**. The PHP final-logout failure remains with owner4; no second
investigation or execution was performed. The two other failures are distinct:

- **Dataset expansion: missing chain, not a demonstrated stuck Stop worker.**
  Archive `os-test-tasks__dataset-expansion-enforce-and-resolve-e2924ff6/`
  `services-shell.log:1938` records enforce exiting 0 in 4.28s, printing only
  “Stopping VPS with datasets over quota”; every subsequent lookup was empty.
  Final SQL at lines15254–15279 contains only completed chains1–4 and their completed
  transactions, with no StopOverQuota chain. The helper in
  `tests/suite/tasks/common.nix:68` first waits for a new matching chain to exist;
  the timeout occurred there. The test wrote referenced=10250 and running/uptime
  fixture values, then the task ran at01:48:08–12 +0100. Node-shell line980 records
  a live referenced/refquota probe at01:48:10.662, inside that interval. A telemetry
  overwrite of synthetic eligibility is therefore plausible, but the actual values
  consumed by `DatasetExpansion#stop_vps` were not captured. Its active/stop-enabled
  expansion, overquota, cooldown, active/running/uptime and count/time predicates
  can skip silently; no failed predicate or scheduler fault is proven.
- **Replacement: dispatched send-state remained unfinished.** Archive
  `os-test-vps__replace-with-descendants-and-mounts-a77cf6d7/node1-shell.log:1128`
  records trans34/rootfs completion, line1130 dispatches chain11/trans35/handle3033
  `osctl -j ct send state --clone --no-start --no-restart --no-consistent 1` at
 02:45:15.413, and line1504 records osctld receiving `ct_send_state`. The300s chain
  wait expired at02:49:36; preceding transactions were done, trans35 had no saved
  error/output, and teardown's recorded buffer still found the container held by
  that command (`replace-runner.log:27`). Both nodes continued status/probe activity.
  The archive shows no causal disk/OOM error or receive-side failure, and lacks the
  blocking stack/process/lock state needed to distinguish transfer/lock/I/O causes.
  Dataset-expander minimum-reserve messages are not proof of actual ENOSPC.

The job used `--jobs auto`, but these failures used separate scenario guests and
nonoverlapping failure intervals; no common stalled worker or shared-host shortage
is established. Task, StopOverQuota/Stop, handle3033, both scenarios and their wait
helpers have identical Git blobs at feature predecessor `63bd0c8ab`, ee474f and
final `bcc5ce474191c168a87886d9bb0a5fdff98cbeab`. EE→BCC changes locale/PHP/docs/spec
presentation, not these paths. This excludes a direct Nov19 source change in those
operations; it does **not** exonerate the whole feature (shared VPS/model/runtime
paths changed), prove identical Nix/deployed graphs, or provide a BCC pass. There is
no evidence-backed incident-policy fix to make from this archive. Preserve the
original receipt/classification as history alongside this more precise disposition.

**Smallest remaining diagnostic, only if root allocates it:** owner1 after owner4's
exclusive backend/heavy window can prepare focused diagnostics for the existing two
selectors, without changing topology, limits or assertions. For dataset enforcement,
capture the actual eligibility fields/predicate decision used by the one task
invocation and any concurrent telemetry update; a before-only snapshot cannot prove
what it read. For replacement, retain both node osctld/nodectld state, send/receive
process and lock/stack information at the existing chain timeout before teardown.
Use those exact scenarios only after the small diagnostic change passes its quick
checks/review; no119-test replay, timeout inflation or uninstrumented green rerun
as an explanation. Root owns allocation and acceptance of this unresolved readiness
limit; current owner4 PHP and owner0 KB work remain independent. Existing source,
input/resource guards and native-effects retention still apply. No run, provider/CI
read, build, technical-source edit, lifecycle action or broad inventory occurred;
all inspection commands are terminal and design capacity is returned.

## Nov19 usability feedback — sufficient source packages

Architect0 confirmed capacity after the terminal reference-impact package and
reverified session `2026-10-30-oomd-abuse-policy`, roster 44 and retained
Astra/xhigh/workspace_write. This is the sufficient implementation boundary for
root allocation; this design pass edits no application source and runs no checks.
Starting accepted sources are backend `ee474f60`, React `6b14ae5e`, templates
`1ba7169b`, configuration `2a06` and KB `ce9387f`. Final bilingual copy is owned by
root in [root-copy.md](nov19-usability-feedback/root-copy.md); use it directly,
preserving existing plural conventions and dynamic placeholders.

**Source versus demonstration.** The still-running demonstration in
`nov17-devcluster-demo/postreview-2026-11-18/packet.md` uses backend `0117035f`,
React `b1fb37b0`, templates `125f132a` and configuration `1efed32a` (5/10).
It does not demonstrate the accepted current source. Current PHP and React already
mount multiple saved matched-policy tables and authorized current/history links on
ordinary incident details, and explicit Period/Incidents/Limit/Action tables.
Preserve that implementation and close only actual presentation/route gaps. No
historical report, sent mail, recorded evidence or old demo identity is rewritten.
The one authorized reset remains consumed; there is no refresh/deployment here.

### Settled shared contracts

- **Existing API suffices.** Registry `IncidentPolicy.Index` supplies actual active
  keys/localized labels; VPS policy rows supply current effective `warning_limit`,
  `stop_limit`, periods and nullable admin-only overrides. Saved
  `IncidentReport.PolicyEvaluation.Index` supplies historical membership/counts/
  limits. No API fields, enum, schema, migration, selector, transport or generated
  SDK change is needed. Keep existing capability checks and authorization.
- **Numeric prefill with independent inheritance intent.** Each limit field starts
  with its current effective numeric value and explicit inherited/custom intent,
  derived from whether its override is null. Use existing input/checkbox/select
  primitives and the existing reset action; do not create a form framework.
  Keep the intended nullable override separate from the displayed number. Saving
  an untouched inherited field sends null, including when its sibling changes;
  saving a custom field sends its explicit positive integer, even when equal to
  the default. A deliberate edit/custom selection affects only that field.
  Clearing/resetting selects inheritance. When an existing custom override is
  switched to inheritance, its hidden inherited target is not available in this
  API: show a pending inherited selection until save/readback, not the old custom
  value labelled inherited, an invented default, or a replacement API call.
  Successful authoritative readback supplies the new effective value. PHP must
  encode intent explicitly in ordinary form controls/POST, not infer null from a
  prefilled number or depend on an unchecked client-only dirty flag. Preserve
  POST drafts/errors, React confirmation/busy locks/readback, admin-only writes,
  CSRF and server validation. Zero is invalid for these positive limits, never an
  inheritance sentinel; zero counts and explicit false shutdown permission remain
  meaningful. Unknown/misconfigured effective limits remain unknown, not zero.
  In PHP, keep saved current values in the four-column table; remove duplicate
  effective-value rows below the form inputs. Attach the approved count/period
  units to each displayed draft input with matching plurals. A pending inherited
  field stays blank with its pending label, without a stale numeric summary.
- **Policy filter and detail.** Both report lists expose a select populated once
  from the existing authorized active registry, with root's All policies label.
  Preserve `policy_key` URLs, owner/VPS filters and pagination reset. If a current
  deep link names a retired key absent from the registry, retain that exact key as
  a historical option; do not silently clear its filter or invent a current label.
  No scans of all reports/users and no per-row API requests. A registry failure is
  unavailable, not an empty successful choice list. Ordinary details visibly show
  every authorized saved `matched === true` recorded/audit_only policy using the
  existing saved label and authorized links. Keep error/skipped diagnostics admin
  only, generated-notice treatment and owner-epoch privacy unchanged. Reserve
  root's no-matching-policies label for exhaustive saved evidence of no match.
  An empty member-visible result can hide private matched/error outcomes, so a
  successful fetch alone must instead use the existing neutral unavailable text:
  “Policy information is unavailable for this report.” / “Informace o pravidlech
  nejsou pro toto hlášení dostupné.” Keep visible saved matched rows and links;
  do not query hidden outcomes or expose error/skipped rows. Never rerun
  selectors or use current registry presence to reconstruct historical membership.
- **Meaningful compact presentation.** Use root's incident-report warning/stop
  messages; reaching a threshold does not claim a completed shutdown. Include the
  localized policy name where already loaded. Aggregate overview/list alerts have
  counts, not policy names: retain threshold-only triggers, zero=>no alert, compact
  geometry and existing fetch count. Separate the action label from a complete
  threshold value, e.g. `3 reports in 7 days`, using supplied periods, actual limits
  and existing EN/CS plurals; no naked ratio or label-plus-period without a count.
  Keep the already-clear detailed period/count/limit/action tables. Remove the
  requested generic counting paragraph and SMTP/inbox disclaimer, including the
  duplicate delivery caveat in EN/CS `notices.warning` and
  `notices.stop_completed` bodies. Preserve each factual first sentence, internal
  delivery states/errors and diagnostics; sent is simply Sent/Odesláno. Permanently render policy/shared settings Details contents;
  remove the disclosure, not facts, links, permission boundaries or error states.
- **Site default only.** Change declared warning 5→3 with the same 7-day window;
  stop stays 10/30. No generic engine default exists: declarations remain required,
  arbitrary policies/custom values remain supported and an empty registry stays
  empty. Existing non-null global/VPS overrides retain precedence and can mask the
  new base. Do not reset settings or reclassify saved incidents to force a display.

### Independent owners and exact file boundaries

| Owner/package | Files and deliverable | Dependency and acceptance |
| --- | --- | --- |
| **owner0 — already released a7a8a607** | `vpsfree-notification-templates/templates/daily_report/email/en.html.erb` only: remove its 640px maximum and use full available window width with small outer/inner padding, retaining dense readable tables and containment. | Independent. This family has only EN HTML; built-in daily report is plain text. Do not create variants or restyle other accepted families. Rendered text/data/conditions/actions/links/escaping unchanged. Existing normal template checker plus actual wide/narrow render inspection is sufficient; no new renderer/tests for a width-only change. |
| **owner1 — source text and site default** | Backend `api/lib/vpsadmin/api/locales/cs.yml` `incident_reports.oomd.restart` and corresponding stop wording, plus `locales/{en,cs}.yml` `notices.warning` / `notices.stop_completed` delivery-caveat removal only, `api/spec/supervisor/node/vps_events_spec.rb`, and site-shaped example in `docs/incident-escalation.md`; site `configs/vpsadmin/api/incident_escalation.rb` and its `README.md` warning base 3. | Owner1 holds the **FIRST full backend source/index/hooks window** to prevent API/WebUI i18n hook collisions. Use the settled root restart and analogous stop sentences in root-copy.md with `%{vps_id}`/`%{hostname}`. English locale scope is only the duplicate notice disclaimer removal; factual first sentences and delivery semantics remain unchanged. `templates/vps_incident_report/email/{cs,en}.{text,html}.erb` already renders saved `@incident.text`, so the source locale correction reaches both formats without copying the sentence into templates. Preserve EN facts, stop/restart action truth, optional hostname and standard footer. The separate `vps_oom_prevention` plain-only process-OOM path does not assert this shared-resource cause; do not graft it there. Keep explicit generic test fixture limits (including `tests/configs/vpsadmin/api/incident_escalation.rb` 5/10) unless a test intentionally mirrors site defaults; do not mass-rewrite historical fixtures. |
| **owner2 — React** | `src/pages/app/vps/{VpsIncidentPoliciesPage,VpsIncidentPolicySection,VpsIncidentsPage,VpsIncidentSettingsEditor,VpsIncidentLimitFields,VpsIncidentThresholdAlert,VpsIncidentIndicator}.tsx`; `src/pages/app/incidents/{IncidentsPage,IncidentPolicyHistory,IncidentNoticeSummary}.tsx`, relevant existing tests; `src/i18n/locales/{en,cs}/{vps/incidentEscalation,ops/incidents}.ts`; affected existing design/work-log docs. | Existing API/SDK permits immediate independent source work. Add select with existing cached registry API helper. Preserve saved-detail implementation and add only heading/known-empty/actual missing-render fixes. Fix empty Automatic shutdown strip at the editor's unconditional `border-t border-border pt-3` inside the already-bordered CardHeader; keep conditional mutation/gate alerts. Expand both policy and shared Details. Scope label/value formatter to affected surfaces; no global Card CSS, routes, BFF or transport rewrite. Keep actual unavailable/error/permission behavior. |
| **owner4 — legacy PHP** | `webui/forms/{incident_policy,incidents}.forms.php`, `webui/public/js/vps.js`, gettext `webui/lang/locale/vpsAdmin.pot` and `cs_CZ.utf8/LC_MESSAGES/vpsAdmin.{po,mo}`, `webui/tests/Regression/IncidentPolicyTest.php`, `tests/playwright/webui/specs/incident-escalation.spec.cjs`. | Read-only inspection/preparation while owner1 holds FIRST. Owner4 automatically takes the **SECOND full backend source/index/hooks window** only on owner1's explicit direct terminal handback; no PHP edits or shared hooks before that handback. React remains independent. Implement same prefill/intent, select, status/membership copy and expanded contents. Remove the useless System config/category row from policy settings. Preserve both separate reports/policies sidebar entries, exact routes/return, all doc IDs, threshold triggers, no permanent list column and no hidden VPS/trigger lookup. No API/model/locale-YAML or shared fixture edits. |
| **owner3 — small KB source follow-up** | After PHP handoff: `contract/navigation.yml` affected source/related fingerprints for `vps.incidents.menu` / `vps.incident-reports.menu`, retaining `vps.incidents.open` / `vps.incident-reports.open`; `cluster/fixtures/incident_escalation.rb` site-shaped 3/10 default with the exact existing trusted selector; existing local `nov18-kb-source/incidents-{cs,en}-candidate.txt` only where current controls/defaults are described. | Root releases once final PHP/default facts settle. No new route, scenario, provider, capture or publication. Preserve fixture membership and explicit generic/non-OOM policies. Link current source and geometry impact to prior `nov18-php-policy-presentation/kb-impact.md`; assess the same six CS/EN concepts below, not a historical inventory. |

Owner0 has no remaining incident-template sentence edit from item 10: the producer
locale is authoritative. If a render reveals duplicated literal source wording,
report that concrete path to root before widening owner0's boundary. Owner2/4 may
resolve routine local component/form questions directly; consequential API,
security, persistence or scope changes return to root. Root-copy.md is the shared
wording input, not an invitation to another prose-design round.

### Acceptance, verification and later dependencies

Quick implementation checks use each owning repository's declared environment and
hooks. Backend: targeted existing node-event/source-text specs plus a focused
load of the changed real site declaration proving warning3/stop10, unchanged
trusted selector and override precedence; no engine redesign. React: typecheck,
affected component/filter/detail tests, catalog/plural audit, relevant build and
doc checks. PHP: syntax/formatter plus existing IncidentPolicyTest cases and
actual-PHP CS/EN render inspection. Test the behavior, especially inherited 3/10
prefill with null unchanged, edit-one/keep-other-null, explicit equal custom value,
custom→inherit pending then authoritative readback, failed save draft retention,
false permission, invalid numeric0 versus real zero counts, and member/admin
capability differences. Two matching policies must both render with their saved
labels/links; a removed policy deep link still filters, a known empty list differs
from fetch failure, and no unauthorized old-owner lookup occurs. Assert expanded
contents, no stray strip with/without permission/errors, and complete localized
count/period values for 1/3/5 and differing periods. Preserve actual positive list
row assertions and no-alert zero state in the existing browser scenario.

Commit the complete source packages and pass quick checks before the normal
independent affected-change review. Root then allocates the existing React
incident browser fixtures/captures and required exact clean-source package checks;
for PHP, extend/run the existing `./test-runner.sh test
'webui#incident-escalation'` at final combined backend source. Reuse existing
accepted generic/non-OOM/two-policy evidence within its actual unchanged scope;
do not add a new VM topology or repeat alerts/engine integration solely for labels,
forms or a changed site literal. A real API form regression or changed action
logic would justify the relevant existing check, not a broad campaign. Synthetic
renders remain synthetic. Native operation ownership, kernel/input/space guards
and failure retention remain as settled; root owns any heavy-window release.

There is no data migration or SDK regeneration/release from this feedback. Record
revision-specific no-change API/client assessment against final source, retaining
original schema/generator/SDK provenance. Existing prior TypeScript release-before-
merge and integration gates remain. The canonical KB five final source pins
(`flake.nix`, `flake.lock`, `captures.json`, `contract/navigation.yml`,
`contract/pages.yml`) follow the final published backend only when allocated;
source-only preparation can use the already-supported exact local-source override
without pretending the old public pin tests new code. Run the allocated pure
contract/annotation checks, then normal pinned `bin/check --allow-missing` after
coherent public pins. Changed warning text/form expansion affects geometry; keep
CS/EN `getting-started/vps-details`, `getting-started/vps-list` and
`restore-backups/playground-vps-list` as the existing minimum reassessment set.
No new canonical capture concept is needed. Canonical media/runtime/strict check,
all-page candidates/staging/production promotion remain parked and separate.

Activation is not allocated. A later approved deployment must distribute the
changed declaration consistently to API/supervisor/task processes and restart
through the existing process contract; no hot reload. Existing saved membership,
counts/action snapshots and sent reports remain literal; existing config-identity
handling of not-yet-dispatched actions is unchanged. Rolling UI updates use the
same API fields. Rolling back these presentation/default changes needs no schema
rollback or reset and cannot undo delivered mail/actions. No default integration,
registry release, cluster mutation, second reset or lifecycle action follows from
this brief. Root released owners1/2/4 under 8191b625/dabc977e/1a5303e5; owner1
then owner4 use the full backend windows above. Owner0 width is accepted at
535b/tree8e0c (34 hashes and two renders); its allocated checked-tree history fold
precedes independent review. Owner3's bounded source follow-up waits PHP handoff.

## ee474f test-only successor — downstream references and remaining delivery

Prior PHP-budget package is terminal; architect0 confirmed capacity, exact session
and roster 44, retaining Astra/xhigh/workspace_write. Root accepted reviewed backend
`ee474f60bb28b4a027767cf0b2d196b143a2c1ee` / tree
`79c1caccc2802fb7d4869b14a7db62fe7f753729` and the real PHP pass
`nov18-postreview-webui/finalee474f/normalized-execution/root-acceptance.json`
(receipt 8e9d3055). The complete accepted de4→ee474f difference is one removal of
the copied 0444 fixture file before its unchanged heredoc in `tests/suite/webui.nix`.
`fixture-copy-correction.md`, receipt fdaceb4f and its affected independent review
prove every other tracked blob/mode unchanged, including product/API/exporter,
schema, migration, plugins, UI, locks and assertions. No product redesign follows.

**Required final reference update: owner0, after owner1 publication.** The canonical
KB workflow's exact-feature revision requirement and this session's final five-pin
stream still apply to the delivery candidate. Current KB 036bb5fa/de4 remains valid
historical source-check evidence; it does not name the final backend successor.
After owner1's exact public ee474f proof, root may allocate one mechanical package
from KB 036bb5fa: change only `flake.nix`, `flake.lock`, `captures.json`
(`vpsadmin_commit`), `contract/navigation.yml` (`vpsadmin_revision`) and
`contract/pages.yml` (`revisions.vpsadmin`) coherently to ee474f. Use canonical
`nix flake update vpsadmin`; require every other lock node/edge/OS input and all
257 other KB files unchanged. No fingerprints, article prose, screenshot fixture,
PNG or runtime-contract edit is justified by this backend test-only change.
Run the normal pinned `nix develop --command bin/check --allow-missing` once on
those final inputs in root's allocated window; retain actual selected source/NAR,
lock graph, checked-file identity and native exit. The old de4 check is not a check
of the new pin. Drift beyond the five pins returns to root instead of expanding
this package. Preserve 036bb/de4 and old checks; consolidate the mechanical refresh
into the existing unmerged source/pin purpose, preserving merged d3af/f977/cb782
and independent runtime 91d history. Root can reuse accepted review via the existing
mechanical-only reconstruction/whole-history/no-migration proof, then release
feature publication. No independent review rerun is required for proved pin-only
content; no default integration is implied.

**SDK readiness evidence, not regenerated artifacts.** vpsAdmin's synchronization
procedure requires revision-specific no-change evidence. Owner3 (or owner1 as a
bounded evidence handoff after publication) should append the ee474f assessment to
the existing `nov18-reusable-sdk-sync/packet.md`: link accepted de4→ee474f complete
blob/mode comparison and unchanged exporter/profile/tooling input inventory;
record schema 7cb28ebd, provenance a9e536e9, exporter lock 2e9a124e, generator 1ef9b204
and unchanged Go 59349035 / Rust 15db0ffd / TS 2d251bb0 heads with their existing separately
bound runtimes/options and Go-only projection. This successor changes no API or
export input, so the existing actual export plus complete current-source comparison
supplies freshness without another export, generation or SDK test campaign. Say
explicitly that the export ran at de4; do not fabricate an ee474f export or rewrite
raw provenance, generated-client input records, the TS archive or old manifests.
The evidence-only note has no application/Git window or review requirement unless
root separately allocates a tracking commit.

**React and retained verification.** Leave React 6b14's `package.json`,
`package-lock.json`, `packages/vpsadmin-typescript-client-development.json`, its
frontend dependency hash and SDK contract unchanged. They describe actual
TS 2d251 / packed 44c651 / API de4 / archive 983061 generation and delivery; that contract
explicitly preserves generation provenance after history changes. Backend HEAD
is not their dependency selector. Keep the five-target/browser proof at 6b14 and
alerts at de4, with their recorded inputs; PHP is the accepted affected integration
pass at ee474f. The one-line test fix creates no reason to repeat alerts, API/SDK
suites or React builds/captures. This is scope-based coverage reuse, not a claim
that de4 and ee474f Nix derivations, deployed closures or running demo are equal.

**Shortest order and remaining gates.** Owner1 completes its already released
exact ee474f feature publication/public-source proof; the small SDK evidence note
can proceed independently, then owner0 performs the final KB pin/check/history
and feature publication package when root allocates it. Observe ordinary triggered
CI within its actual scope; do not dispatch a duplicate integration campaign.
No config/template successor or pin is implied. All failures and original receipts
remain literal. Canonical bilingual media/runtime, strict inventory/hosted strict
check and later complete-page/staging/publication obligations remain parked as
recorded; this test-only delta adds no capture concepts or geometry change.
Before eventual React merge, a separately authorized TS registry release containing
the existing support and coordinated manifest/lock/provenance/cache-hash adoption
are still required. Explicit repository/target integration approval, fresh target
readiness, actual deployment/source attestation and exact production-KB approval
remain separate gates. The running older demo is not refreshed; no reset, resource
resume, cleanup or lifecycle operation is allocated by this brief.

## Nov18 PHP disk admission — corrected incremental budget

Sufficient for root's release of owner4's existing complete PHP package; this
addendum authorizes no execution. Architect0 reverified exact session/roster 44,
retains Astra/xhigh/workspace_write, and the prior design package is terminal.
For `webui#incident-escalation` at frozen de4/tree5c0a, **replace the inherited
120 GiB gate below with 60 GiB (64,424,509,440 bytes) free on the shared store,
build-temp and runner-state filesystem, with 32 GiB available RAM and shm each
unchanged**. The former 100+ 20 GiB came from Nov17 fresh-demo planning (full tank
growth plus unspecified construction/import overlap), not a measured PHP peak.
The old 127,200,624,640-byte reading failed that allowance only: PHP attempts
remain zero, and that receipt remains historical admission failure, not test failure.

**Measured remaining work.** Owner4's
`nov18-postreview-webui/finalde4df3d6/budget-corrected/measurement-receipt.json`
(SHA256 `18ea7b9fe1025520d4eeffad9068223215b96c902de48e64973c51314da907db`)
binds the terminal nonrealizing measurement. Selected root is
`qp3q521wh9xg952zvfk8lhw5b0hp9l0q-os-test-vpsadmin-webui.json.drv`; its 6687-entry
graph shares 6581 identical derivations with accepted alerts, has 106 PHP-only
entries and no changed common entry. The successful sy949 library and all 1486
relevant input derivations match; kh8 output is resident. Dry-run requires 43 local
builds and 16 fetches: 190.9 MiB download, 280.1 MiB unpacked, no local kernel build.
Resident API/PHP/browser/alerts closures are already deducted from free space;
do not add them again. Optional absent derivation outputs are not required work:
the corrected output-presence inventory is descriptive, not a storage forecast.

**Physical allocation and allowance.** `tests/suite/webui.nix:493` starts only
services and node1; `manageCluster=false` excludes the common all-node startup.
The evaluator constructs node2 but never starts it for this script. OSVM
`machine.rb:110,799` creates a tank only at start using `truncate -s20G`: node1
starts sparse and can grow to 20 GiB; node2's tank is not created. Both selected
node squashfs outputs still must build. Their recipe streams tar into sqfstar,
without a complete extra uncompressed archive. Services uses `FileUtils.cp`
(`nixos_machine.rb:58`, Ruby `IO.copy_stream`), so assume a fully allocated writable
copy; do not rely on sparse/reflink preservation.

Selected services image dwbm6d94 is absent and AUTO-sized by sabf28: stage the
system closure, allow inode blocks+5.2%+512 MiB, create/fill the image, then move
it into the output. There is no fixed 12 GiB requirement. Comparable retained
alerts image is 5,330,960,384 bytes logical / 3,590,778,880 allocated (4.97/3.34 GiB);
its services closure is 2.89 GiB NAR. Resident browser closure is 2.05 GiB NAR,
partly shared; its copy into the new image is a real incremental cost. Allow
8 GiB for the new image, explicitly an estimate with margin for browser/inode
changes, not a measured size. Each retained comparable node squashfs is 0.398 GiB;
allow 2 GiB total for the two newly generated node images.

| Phase | Incremental physical-space allowance |
| --- | --- |
| Build, one Nix job/core | 8 GiB services image + 8 GiB staging + 2 GiB node images + 4 GiB downloads, generated outputs, database/metadata and scratch = 22 GiB |
| Runtime after build scratch is gone | 8 GiB retained services image + 8 GiB writable copy + 20 GiB maximum node1 tank growth + 2 GiB node images + 2 GiB fetched/config/log/host overhead = 40 GiB |

Use the phase maximum 40 GiB, not their sum. The download+unpack total is under
0.5 GiB and included in overhead. The 20 GiB free-space floor is an operational
reserve for existing shared-host writes and orderly failure handling, not PHP
consumption, a reservation, or a measured universal requirement. This makes the
admission 60 GiB; the estimate deliberately covers full possible tank growth even
though fixtures create sparse/empty storage. Exact AUTO-image size and transient
peak remain unmeasured until build. The source recipes and retained comparable
sizes support this bounded allowance; they do not prove a hard quota.

**Execution condition and stop.** Root may release owner4's unchanged ordinary
`./test-runner.sh test 'webui#incident-escalation'` package with
`TEST_RUNNER_REPO_ROOT=/nix/store/fz1ndj3iybgaya15vcpyhya10rznxd2s-source` exported
for that command and the existing native watcher/isolated namespace. Refresh free
space once at admission: require 60 GiB,
RAM/shm 32 GiB each, unchanged approved graph/input identity and bounded
realization cost, no concurrent local heavy batch and no newly identified competing
large write. The 43-build dry-run list is a transient residency snapshot, not an
immutable allowlist: an already approved small source copy or unit may need
rebuilding if its output is no longer resident. Root accepted c7a85432 as a
pre-VM guard stop; the unchanged ahq source derivation/inputs and missing former
23.67 MB output do not alter this budget. The reason for its disappearance remains
unknown; preserve the original stopped receipt and its evidence limits. Owner4 measured
118,883,659,776 bytes free (110.72 GiB), RAM 50,854,719,488 and shm 37,662,318,592 at
21:06:44 UTC; this passes but is not reserved. Keep the declared three-machine
24 GiB resource accounting/topology and all assertions/timeouts. As part of the
existing bounded watcher, observe the 20 GiB floor and 40 GiB maximum drop from
admission; unexpected growth, an actual services image above 8 GiB, node images
above 2 GiB total, changed build/input plan or a local kernel build stops advancement
and returns evidence to root. Interrupt only this owned disposable operation via
its native recovery path if needed to protect the floor; join/reconcile effects,
retain failure evidence, and do not automatically retry or reclaim storage.
Capture actual emitted config/deriver/full graph and image sizes with the existing
receipt. Image-size observation is a check on the estimate, not another campaign
or per-command approval gate. No cleanup/GC, topology reduction, demo refresh/reset,
parked KB work or lifecycle action follows from this correction.

## Alerts pre-VM packaging failure — clean-source correction boundary

Prior design package is terminal; architect0 retained Astra/xhigh/workspace_write
and reverified session/roster44. Owner1 owns diagnosis and verification. Attempt13190
failed before VM boot because the actual source included ignored `libnodectld/.gems`
and the unchanged builder selected mini_mime first among84 gemspecs. Retain
`nov18-reusable-policies/alerts-de4/package-selection-diagnosis.json` and its actual
versus clean selection control. Adding Git would build the wrong gem. No source,
recipe, dependency, assertion, topology or timeout change is needed for this route.

**Supported override.** The exact sv2 test-runner wrapper leaves
`TEST_RUNNER_REPO_ROOT` intact. Its bv1 `cli/command.rb:original_repo_root` uses that
path for runner extensions, then RepositorySource resolves/roots its flake outPath
and supplies that resolved path to metadata/config evaluation and subprocesses.
Therefore the normal repository `./test-runner.sh` may run with
`TEST_RUNNER_REPO_ROOT=/available/verified-clean-de4-source`; it still selects the
runner through the clean de4 worktree's locked flake. No direct/private runner,
source symlink substitution or framework patch is required. Keep wrapper/system/
Nixpkgs environment as declared by the selected runner; record both runner identity
and actual resolved repository source. A store-path input may lack Git revision
labels: external exact-source proof must establish de4, not invented metadata.

**Source availability and focused proof now satisfied.** Owner1's
`nov18-reusable-policies/alerts-de4/focused-clean-lib-receipt.json`
(SHA256 `6a9423a3050a04a3ddd4c63ffa9020c85c13cdf35f3c304ed0aec65cc1f8b92d`)
records restored/verified/retained exact-de4 fz1 source, all3226 tracked paths and
seven package locks, successful sy949 library build to kh8hmk1m output, and joined
native38261/utility81247. The6610 helper graph remains selection evidence only;
no scenario or VM ran. Root still allocates any retry with fresh ordinary admission
and exact actual library/input membership proof below. The earlier availability
finding remains historical: recorded fz1 and some attempted paths were absent at
those reads; no actor/cause is inferred. Owner1
retains `publication/public-de4.tar.gz` (3054974B, SHA256
`bc7dedd21e6a75c0e9f48481d7caa3ea548dfc2aca07cf1b36c3d0f24c071640`) and
`public-source-proof.json`, binding all3226 tracked files, executable/symlink modes
and tree5c0a69fd to exact de4 plus canonical public availability at publication.
Root may allocate ordinary exact `github:vpsfreecz/vpsadmin/de4df3d63f4d4afb0c27e8b9be2785c15d24811c`
source resolution/retention for the focused check. Reverify the resulting clean
snapshot against that tree; neither historical fz1 nor a fresh public response alone
proves current available source. No restore/build/query was run by architect.

Match every tracked input, including force-tracked package `Gemfile.lock` files
that match broad ignore rules: root VERSION/.ruby-version, flake.nix/lock and its
actual follows edges, overlays/Ruby source recipe, package Gemfile/lock/gemset,
libnodectld gemspec/version/lib/templates and the ordinary scenario/config/seeds/
extensions. Preserve locked OS8e44 and effective Nixpkgs a9e6, Ruby/OS gem versions,
builder hooks and declared environment. The source recipe copies repoPath verbatim;
its intended gemspec needs no ignored local .gems, .bundle, generated component
Gemfile.lock, node_modules, result links or .git directory. These caches are not
required inputs. The inspected ordinary scenario declares no extra ignored input;
if a real external/test-config input is found, bind its exact existing value/path
rather than dropping or inventing it. Do not copy arbitrary ignored checkout state
into the verified snapshot or remove anything from the working checkout.

**Two bounded stages, root allocated separately.** First use the same clean source,
locked helper/overlay graph and source-selection contract to identify the intended
libnodectld gem derivation and build only that package. The historical sy949 preview
is a candidate, not a required identity or a successful build. Retain the selected
derivation/full relevant inputs, actual source/sourceRoot/buildPhase, sole intended
gemspec, native successful output and installed libnodectld4.2.1 gem/files. A new
snapshot path can change derivations; compare inputs explicitly. Do not substitute
an ambient `gem build` or a different package graph. This proves the packaging
correction only and creates no scenario or VM success.

Only after root accepts that focused result, reassess the already-defined headroom
and allocate one ordinary alerts scenario attempt with the same verified override.
The focused result carries forward only if the actual scenario graph references
the exact successful library derivation/output and bound inputs; de4/tree equality
alone is insufficient. Capture the actual runner-resolved/rooted source and the
attempted config root derivation/full recursive graph as soon as the native build
identifies them, while available—not only after configuration success or command
exit. On successful emission, retain actual config bytes/deriver, selected machine
inputs, package/source/fixture parity and ordinary assertion/native/quiescence
results. Use normal operation-owned Nix retention for selected source/package
artifacts; do not depend on an expired runner root or claim a reconstructed graph
was actual. The original failed root graph remains unavailable, and preview6610
remains preview. Any missing current identity or further package failure stops
advancement for owner1/root reconciliation; no blind replay or broad campaign.
PHP stays held. Demo, canonical KB resources, cleanup and lifecycle remain untouched.

## Nov18 accepted source — bounded post-review verification

Root accepted `nov18-final-review-result.md` with no findings. The eight exact
ranges/trees in `nov18-final-source-inventory.json` are authoritative: backend
`de4df3d63f4d4afb0c27e8b9be2785c15d24811c`, configuration
`2a06abc21b23e9e500bfdb6d657854c545511d21`, React
`6b14ae5e1702ee8c137605d3512c123c9a24b582`, templates1ba7169b, KB9e0f6c06,
Go59349035, Rust15db0ffd and TS2d251bb0. Roster44/session reverified; architect
settings retained. This current sequence supersedes older post-review execution
instructions, including any unconsumed-reset assumption. It releases no operation
by itself and leaves all source frozen except root's mechanical KB pin allocation.

1. **Already released in parallel:** owner2 owns scoped React browser/implemented
   desktop/mobile captures and the five clean-head Nix targets, with the FIRST
   local heavy-verification window. Preserve exact SDK archive/input and actual
   package/source/provenance outputs; the six optional WASI warnings remain a
   build question until that result. Owner1 independently owns backend/configuration
   feature publication, fresh default assessment and exact public de4 proof.
   Default drift is an integration concern, not grounds to rebase this reviewed
   verification input. No local VM run belongs to that publication package.
2. **Owner0 after public de4 proof:** update the coherent five files `flake.nix`,
   `flake.lock`, `captures.json`, `contract/navigation.yml`, `contract/pages.yml`
   from literal5aa1 to de4 using canonical `nix flake update vpsadmin`. Preserve
   every other lock node/edge and OS input; unexpected movement stops the pin.
   Run `nix develop --command bin/check --allow-missing` in the KB worktree in
   the next root-allocated heavy window, not concurrently with owner2. Preparation
   and local source comparison can proceed without that window. Consolidate this
   mechanical completion into existing unmerged purpose9e0f6c06; preserve merged
   d3af/f977/cb782 and independent runtime91d, previous refs and review evidence.
   Retain exact final tree/range, pin diff and checked-input/patch equivalence for
   review-policy reconciliation before publication. The earlier six pure checks
   stay valid for their local-de4 scope; they do not replace this pinned check.
3. **Owner1 then owner4, one disposable native batch at a time:** after owner2's
   returned window and root's scheduling of the KB check, run only any uncovered
   `./test-runner.sh test alerts/incident-escalation` and
   `./test-runner.sh test 'webui#incident-escalation'`, respectively, from clean de4.
   The wrapper is the repository's `nix run .#test-runner`; use its normal isolated
   state namespace and selected flake inputs, never the registered demo/provider.
   The slash-form alerts selector is required; the hyphenated display name selects
   nothing. Keep unchanged user+socket topology and scenario timeouts.

Before scheduling a duplicate native run, assess the already-triggered exact-de4
CI once at the execution boundary: require the actual selected script, terminal
scenario success, emitted derivation/config and complete relevant source/input
identity, including packaged test/fixture bytes. A green workflow, matching Git
head, skipped integration job or historical011/b1fb result alone cannot establish
reuse. The current CI uploads full logs only on failure/cancellation; success
therefore does not guarantee the required input evidence is available. Reuse each
proved scenario separately; otherwise its assigned local run supplies the gap.
Do not wait for unrelated CI tests or dispatch a broad replacement workflow.

Acceptance remains the existing reviewed scenarios: alerts creates a non-OOM
`fixture_abuse` report matching `manual_category` and `manual_content`, then proves
normal node ingest/dedup, one real Stop, independent SMTP failure/retry, preserved
restart data/cooldown and owner transfer. PHP's existing fixture_alpha/beta rules
exercise two-policy current/saved facts, reports/policies navigation, explicit
period/count/limit/action, safe detail links/admin diagnostics, settings/Inherit,
member denial, scoped history and CS navigation. Its reached/zero indicators and
real visible-row prerequisite remain. Do not copy test policies into site config
or substitute synthetic rendering for the live PHP/API scenario. Retained engine
and concurrency checks cover multi-policy arbitration; no new scenarios are needed.

**Admission and stopping conditions.** Reuse the ordinary test-runner assessment,
not parked KB construction allowances. The prior exact PHP receipt
`nov18-postreview-webui/final0117035/host-preflight.json` sets32GiB available RAM
and shm (24GiB declared plus8GiB runner reserve), and120GiB free disk (100GiB
incremental allowance plus20GiB shared floor). Current source retains services8GiB,
nodes8GiB each,20GiB node tanks; PHP defines three machines though only node1 is
prepared, while alerts defines services+one node. The conservative previous PHP
bounds may cover either sequential batch after fresh host/shared-use checks and
confirmation of the actual emitted resources. They are allowances, not measured
peaks or reservations; fresh free space already accounts for existing usage.
Keep one Nix job/core and preserve the running demo/private guests. Insufficient
headroom, unexpected local kernel build, changed inputs/resources, failed assertion
or uncertain native effects stop advancement and return the concrete evidence to
root; do not reclaim old state, alter topology, start a capacity campaign or replay
an uncertain command. Fresh watcher/active-parent ownership follows the installed
monitor policy. Join all owned handles and retain actual config/deriver/full input
graph, source parity, logs, exit and quiescence before returning the window. Normal
runner teardown covers only its disposable fixture; no session cleanup is implied.

Milestones are public de4 proof; coherent final KB pin/pinned-check receipt; exact
React package/browser result; and each accepted or properly reused scenario result.
Current open prerequisites are publication proof, window return, fresh normal
headroom and evidence for any CI reuse—not a new product/design decision. Source
failures return to the owning implementer with focused checks/review as needed.
No canonical KB media/runtime/capacity resume, demo refresh, second reset, default
integration, registry release, production or lifecycle action follows from these
results. Keep all earlier receipts and native uncertainty fences literal.

## Nov18 feedback — reusable creation-time policies and clear presentation

**Sufficient interface boundary for root allocation; no execution authorized here.**
This supersedes the adapter-gated G enrollment design. Inspected baseline is backend
`0117035f22a465c2b3d78f02df05bc828775afab`/tree`90b3f6101cf089124b77cfe3f0209870a2e986db`,
React `b1fb37b0de3af6ef2f6f9e5f4f73ea0296b19c89`/tree`7f62ae155b397e22614c0ffc10c36451a1ec99c6`,
templates125f and configuration1efe. Roster44 and exact session were reverified;
architect0 retains Astra/xhigh/workspace_write. Preserve the accepted demo and all
historical receipts. Its one reset was consumed. Owner0's older-email preview
operation is independent and has the sole current runtime/Mailpit-write window.

### Nov18 KB source package — sufficient owner0 release boundary

Source-only package, pending root allocation. Backend is frozen local
`de4df3d63f4d4afb0c27e8b9be2785c15d24811c` / tree
`5c0a69fdb65828faaaf7c770d0d099390ccd1c49`; KB starts at accepted
`4be305f13fcd15ba79c5c7bde95a277a6164f442` / tree
`4aadfe21daaa3983406997a3b352dc80fc06e1ed`. Owner4's exact PHP impact is
`nov18-php-policy-presentation/kb-impact.md`. Architect inspected these sources;
no checker, fetch, evaluation, build or runtime operation ran for this brief.
Owner0 owns the following source changes; root owns final bilingual prose.

- `contract/navigation.yml`: retain `vps.incidents.open` and its policy intent.
  Change `vps.incidents.menu` labels to the exact backend catalog (Incident policies /
  Pravidla incidentů), move its source to `webui/forms/incident_policy.forms.php`,
  and retain the related route fragment `return '?page=adminvps&action=incidents&veid='`
  in that same file. Add control `vps.incident-reports.menu` in that helper and path
  `vps.incident-reports.open` with steps `[vps.menu, vps.incident-reports.menu]`,
  bound to the same two incident articles. Its actual catalog labels are Incident
  reports / Incidenty, and its related fragment is
  `'?page=incidents&action=list&list=1&vps='` (including the existing return behavior).
  Recompute coupled fingerprints with the existing normalized one-line context
  algorithm; inspect related contexts, do not accept unrelated drift blindly.
  `contract/kb-annotations.yml` gains the two language bindings for the new path;
  keep one policy-path binding per article. Existing inventory page IDs stay fixed.
- Update the existing local candidates
  `owner3-runtime-policy-evidence/incidents-cs-candidate.txt` and
  `owner3-runtime-policy-evidence/incidents-en-candidate.txt` under this session,
  for `navody:vps:incidenty` and `manuals:vps:incidents`. Distinguish restored reports
  from policies, describe saved matching on ordinary creation and per-policy
  period/count/limit/action, and explain saved report policy links versus current
  settings. Preserve mode/suppression, confirmed-stop, owner privacy and immutable
  mail/history facts. Annotate both navigation instructions. These remain existing
  unmanaged page candidates, not newly registered managed pages; preserve language
  markers and unrelated article sections. Root finalizes wording before delivery.
- `cluster/fixtures/incident_escalation.rb`: use `rule :oomd do` (no adapter) and
  an explicit `applies_if` requiring codename `oomd`, source kind `node_vps_event`,
  non-null source key/node, source node equal to `ctx.vps[:node_id]`, and action
  restart or stop. Preserve the sole key, labels, templates, limits5/10, default
  false suppression and existing screenshot-only injection. Removing the adapter
  without this selector would wrongly enroll all ordinary fixture incidents.
  `cluster/README.md` must describe the selector and current declared limits;
  other topologies inherit the backend's explicit test configuration, not a builtin
  policy (de4 has oomd plus two manual test rules there). No new fixture scenarios
  or Nix injection changes. If its adjacent comment is updated in
  `cluster/nix/test.nix`, that change is comment-only; runtime behavior stays exact.

**Supported local check and publication dependency.** `tools/check-contract.rb`
supports `--vpsadmin-source DIR`; `tools/test-contract.rb` supports the matching
`VPSADMIN_KB_VPSADMIN_SOURCE` environment variable. Both read local sources without
fetching or evaluating Nix. They do not verify Git provenance: owner0 must retain
exact de4/tree and clean source-byte evidence alongside results, using the frozen
checkout (or an exact local Git archive if it no longer matches). In the existing
prepared pinned tool environment, from the KB root, the bounded source checks are:

```sh
ruby tools/check-contract.rb --vpsadmin-source /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin
VPSADMIN_KB_VPSADMIN_SOURCE=/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-30-oomd-abuse-policy/vpsadmin ruby tools/test-contract.rb
ruby tools/check-kb-annotations.rb
ruby tools/test-kb-annotations.rb
ruby -c cluster/fixtures/incident_escalation.rb
```

**Retained Ruby tools (availability clarified).** The earlier shell drv
`k19km3m5zwvmnpkwgh9ikdc8c21fqkmq` is absent; do not claim a recreated shell.
The recorded `kb-source-evidence/shell-plan.log` and
`g-kb-source/root-ci-44223451383-attempt1-job.log` identify still-present
`/nix/store/yq6pmvy7ya79974bjxw4bn6q4n8k9ccl-ruby-3.4.9-with-packages.drv`, whose
output is `/nix/store/jglb2dvyidk8qzhf2gcvwci9gn4djixw-ruby-3.4.9-with-packages`.
Use its `bin/ruby` explicitly for the allocated pure checks. Its retained
installPhase binds Ruby `/nix/store/rc5ywk2fcw0939v498ykjns5sirmlhr0-ruby-3.4.9`
and sets GEM_PATH to
`/nix/store/0x3pb0psj70j84028cdqpm60y356dv69-ruby-gems/lib/ruby/gems/3.4.0`, with
minitest5.26.1 from
`/nix/store/6xb0flcihilwc7afnn8rh01nsdrlpjiw-ruby3.4-minitest-5.26.1`.
Apply the existing shellHook's Ruby/Bundler variable clearing and set GEM_HOME
to the raw Ruby output's `lib/ruby/gems/3.4.0`; the wrapper supplies its GEM_PATH.
Record effective interpreter/minitest identity with the checks. This reuses the
pinned shell's exact existing Ruby tool subset, not ambient Ruby/minitest or a
claim of whole-shell restoration; no evaluation/build/installation is needed.

Also load the fixture with de4's pure `api/lib/vpsadmin/api/incident_policy.rb`
(no API/DB boot) and assert sole oomd key,5/10, unchanged metadata and suppression,
plus true restart/stop cases and false manual-lookalike, missing-key/node,
wrong-node/action and generated-notice cases. Reuse the earlier pure-parser
approach, no new runner. Review the two candidate annotations and factual diff;
this does not replace the later complete-page candidate/release validation.

Keep all five current public pin identities at literal5aa1 during this preparation:
`flake.nix`, `flake.lock`, `captures.json`, `contract/navigation.yml` and
`contract/pages.yml`. The local check is explicitly a **de4 source override / final
pin pending**, not evidence that the revised contract works with5aa1 or that de4 is
public. Do not write a local path into public pins, fabricate a remote narHash, or
run `bin/check`: the aggregate includes Nix evaluation and unrelated runtime helper
checks. Commit the substantive source changes for independent review with this
known pin dependency recorded; hold feature publication until the coherent pin.

After root's final independent source review, publish the exact backend feature
head through the normal route (its CI push trigger is real). Then replace the
five pins with exact de4 using the canonical `nix flake update vpsadmin`, preserving
all other lock nodes/edges and OS inputs, and run the normal pinned
`nix develop --command bin/check --allow-missing` under a separately released
verification package. Retain exact diff/provenance; mechanical pin finalization
uses the applicable review policy, and any source/input change returns to root.
This is the only publication dependency; it does not block substantive KB editing
or local source review. No backend push, Nix command or check is authorized by this
architect brief itself.

Canonical-media obligations are unchanged: reassess CS/EN
`getting-started/vps-details`, `getting-started/vps-list` and
`restore-backups/playground-vps-list`; retain semantic IDs and the known1150px
layout. Source/synthetic PHP evidence is not canonical media or live acceptance.
The final runtime attestation, affected captures, strict inventory validation,
staging and production publication remain separate parked work. No provider,
capacity, cluster, old native uncertainty fence or session lifecycle is changed.
No schema/migration/API changes belong to this KB package. Recovery is source
reversion; no live resources or published pages are touched.

### What was too narrow; complete ordinary writer boundary

The current site `configs/vpsadmin/api/incident_escalation.rb` contains one rule
with `adapter: :node_oomd`, limits5/10 and no selector. The backend supports selectors,
but its `ADAPTERS`/`qualified_reports` gate admits only node oomd restart/stop reports.
That gate is a product requirement defect for reusable ordinary-incident policies.
It is not fixed by adding a redundant selector or explaining the existing gate.

Real producers are: admin/API `resources/incident_report.rb:Create`; site abuse
parsers (`configs/vpsadmin/api/abuse_notice_parser/*.rb`, including common utils)
using `IncidentReport.new/save!`; supervisor `node/vps_events.rb`; and
`nodectl/lib/nodectl/commands/incident_report.rb:save_incidents`, which currently
inserts SQL directly. The last path bypasses ActiveRecord. Generated policy notices
are deliberately not ordinary incidents. Per-process `OomReport` is another model
and remains separate. Imported parser dry runs construct unsaved objects only.

Use ONE model creation envelope (`around_create`, delegating to IncidentEscalation)
for ordinary `IncidentReport` persistence. Acquire the existing settings/VPS locks
before inserting, reconcile ownership, insert, then save every policy outcome and
prepare its action records in the same transaction, before any source notification
can render. Notices bypass the envelope. Remove the duplicate policy-evaluation
loop from node ingestion; keep its node validation and source-key dedup before
creation. Concurrent ordinary writers must obey the same lock order. Rollback
removes the report, memberships and action records together. Database errors must
propagate; selector errors remain isolated per policy. Updates, reads, Send/Process,
retries, reconciliation and configuration reload never enroll or reclassify rows.
No callback runs for an unsaved dry run. Hooks run once per committed creation;
a rolled-back transaction can retry, so selector side effects remain unsupported.

**Nov18 concurrency clarification.** The ordinary-producer failure in
`nov18-reusable-policies/source-concurrency-remainder-results.json` (concurrency
case `[1:2]`: two Stop decisions instead of one; node case passed) does not change
the atomic creation contract. Move VPS resolution into the existing settings-first
serialization and yield the locked VPS; do not perform the preliminary plain
`Vps.find_by` in the save transaction. This alone is insufficient for an importer
or API caller whose outer transaction already established a REPEATABLE-READ
snapshot. Keep the database isolation and existing settings/VPS lock order.

Within mutation serialization, use ordinary ActiveRecord current locking reads
for membership/count/contributor queries and pending/outstanding action eligibility,
and consume current locked settings/per-policy rows instead of discarding them
and rereading through a stale snapshot or cached association. Reconciliation and
source-key dedup reads reached in the same transaction must retain that current-row
property. Existing `security_advisory.rb:rebuild_affected!` and
`rebuild_affected_users!` supply the local `.lock`/`.lock.pluck` precedent. The
membership scope currently uses an evaluation subquery: an outer report lock alone
must not be assumed to refresh that nested membership read. Prefer the narrow
joined report/evaluation relation with the existing policy-key, matched, owner,
epoch and time predicates; project only fields needed for counts/contributors.
Use fresh locked relations rather than loaded association caches. Keep these
mutation reads separate from public read-only summaries; no new advisory lock,
registry, isolation override, independent transaction, schema or API change.

Owner1 applies this within the existing package after owner0's renderer freeze
ends. Focused acceptance is both existing producer concurrency cases plus a
controlled older-outer-transaction case: establish the old snapshot, let another
connection commit its qualifying report/action, then create normally. Assert the
second selector sees the prior committed membership, saved counts include both
reports, and only one Stop decision/action is prepared. Include current override
and warning-exclusion assertions in the affected focused coverage; retain rollback,
exactly-once evaluation and no-hook-on-update/retry checks. The original failed
receipt remains evidence, not a passing result. No runtime work is released here.

Replace nodectl's direct INSERT with one narrow `create_incident_report` command on
the existing node RPC Handler/RpcClient, using `send_write_request`. The server
validates fields and the bound node's VPS, assigns current owner and provenance,
and invokes ordinary creation/processing. Preserve subject/text/codename, admin
attribution, CPU limit and explicit VPS action semantics. Never accept caller-supplied
source_kind/node attestation or owner IDs. Generate one request token per report
before the call; derive the existing unique source_key from node+token, keep it
stable across transport retries, and return the same report ID on redelivery.
Reject a reused token with different report facts. A reply timeout is uncertain,
not permission to issue a fresh token or fall back to SQL. Retain/report the token
for reconciliation. Existing RPC transport/credentials suffice; no policy-specific
transport, background importer or new registry is needed.

### Declaration, context and effects

The single declaration format becomes `rule :key do ... end`, with existing
labels/descriptions, declared limits, suppression, templates and optional
`applies_if`. Remove the required adapter and source_type admission catalog.
Every ordinary creation visits all configured rules in lexical key order. An
absent selector matches; false does not count; exceptions/nonbooleans save a
selection error, without affecting other rules. With no site file/declarations,
there are NO active policies, not an OOM-specific built-in policy. This is an
intentional missing-configuration behavior change. Settings and historical
outcomes survive removal; new declarations do not adopt historical incidents.

Give selectors deeply frozen plain values, not models: `ctx.report` contains id,
codename, subject, text, detected_at, created_at, user_id, vps_id, filed_by_id,
mailbox_id, ip_address_assignment_id, cpu_limit and vps_action; `ctx.source`
contains kind, key, node_id and action from trusted producer-assigned provenance.
Retain captured `now`, VPS/owner identity and state, accounting epoch, policy key,
prior matched counts, last warning/stop, mode/overrides and stop exemption. Report
text/codename are content, not source authentication. Document exactly this input
surface; do not add speculative resource queries or allow database/network I/O
inside selectors. Keep arbitrary report text out of duplicated evaluation snapshots:
persist the existing bounded identity/count/restriction/metadata/decision facts and
matched outcome needed for history, never data merely to rerun a selector.

Initial site rule keeps key `oomd`, labels,5/10 limits and templates, and explicitly
matches report codename `oomd` plus source kind `node_vps_event`, non-null source
key/node ID, bound VPS node and source action `restart` or `stop`. These are the
existing authenticated-channel source facts, not an independent proof of memory
pressure. A manual report named oomd therefore does not match this particular
site rule. Another rule can match an ordinary manual/imported category from
`ctx.report` without backend source edits. Put this real selector in the site file;
add one short two-policy/non-OOM example and input reference to the existing docs.

Preserve original-owner epoch checks: missing/noncurrent owner/VPS or transfer
in progress cannot act or expose predecessor history; record audit-only without
running the selector where the existing ownership prerequisite fails. Historical
import attribution must not be overwritten with today's owner. Source validation
remains at its producer. The node event path still verifies current node, accepted
protocol action and stable dedup key; manual/API remains admin-authorized and
imports retain their existing parser validation. No codename grants provenance.

Counts use saved matched=true membership and event timestamps in the existing
7/30-day rolling windows. Selector counts exclude the new report; saved decision
counts include it when in range. Old/future events remain audit-only for action
eligibility; no delayed replay. The engine still owns positive declared limits,
mode/override precedence, suppression, active owner/VPS and transfer restrictions,
shared stop permission/cooldown, resource locks and deterministic one-Stop arbitration.
Explicit report Stop/Suspend retains ownership of that report's requested effect:
record policy membership/counts/effective snapshot with decision=none, adding
neither an automatic warning nor another stop for that report. Its ordinary mail
and explicit chain retain ownership; later incidents can still count the membership.
Never infer a completed policy stop from the request. Existing CPU/network
handling remains in normal chains. Confirmed-stop mail still requires successful
real Stop completion; one source matching several stop policies uses one physical
chain and distinct saved per-policy outcomes.

The creation hook prepares database decisions only. Keep ordinary notification
ownership with API New, imported Handler/Send, node notification recovery, and
legacy Process. API/RPC source creation plus its normal chain preparation must be
atomic where they already perform explicit actions. Node retains its immediate
postcreation reconciliation; the scheduled task dispatches saved pending actions
for all policies and reconciles transfers, never calls selectors. Replace OOM-only
scheduler/history selection with saved membership/action coverage. Generalize
owner-epoch visibility to policy-evaluated ordinary reports and notices, without
backfilling or changing the content of older unevaluated records. Preserve existing
mail identity/notification markers; callback evaluation must not enqueue a second
ordinary mail. Old raw-SQL rows retain ordinary processing without new matching.

### Public data and display contract

Current VPS policy rows already supply periods, counts, limits, configuration_valid,
mode and stop permission. Keep the existing flat warning/stop fields and fixed
7/30-day semantics; do not invent configurable windows or another policy registry.
Remove obsolete `source_type` from active-policy discovery/VPS metadata. Add only
readonly `matched` (nullable boolean), `warning_period_days` and `stop_period_days`
to IncidentReport.PolicyEvaluation Index. `matched` distinguishes false audit-only
from true membership and null selection errors; state alone cannot do so. Periods
expose the existing fixed contract, including old snapshots, without rewriting
rows. Preserve member-visible outcome restrictions and admin-only error details.
Specifically, members see only matched=true recorded/audit_only outcomes. ALL
error-state evaluations, including matched=true configuration failures, remain
admin-only diagnostics. Administrators see their saved membership value and safe
failure details separately from successful matched-policy tables. A matched error
still contributes to membership counts; never relabel it skipped. Omit an empty
member section without asserting that no policy matched or inventing unknown cells.
Add nullable `notice_policy_key`/`notice_policy_label` to existing report notice
fields, from the notice's saved action metadata with owner/epoch checks. Validate
internal notice/action user, VPS, epoch and metadata consistency; reader permission
stays with the resource's existing scope. Do not require today's VPS owner to match
historical ownership: admins can inspect valid old-owner notices. Missing or
inconsistent linkage returns null without reconstructing identity from codename or
the active registry. Ordinary reports return null. A notice identifies its originating
policy, not all policies
on its trigger; it never acquires membership or invokes matching. Retired policies
keep their saved names and authorized filtered-history links.

Ordinary mail retains ONE `incident_policies[]` collection and one source email.
Use each matched, member-visible evaluation with complete usable saved facts;
include matched audit-only outcomes only when that snapshot supplies the facts.
Do not invent values for failed/incomplete evaluations. Counts/limits are the
saved creation-time assessment, anchored at evaluated_at, not recomputed at send
or presented as the incident's past calendar window. Aggregate mail retains its
single originating policy, saved action counts and the existing saved-base plus
current-restriction calculation; do not substitute current declared limits or
change contributor selection. No new mail payload fields are required.

Each mail policy gets its label and two clear rows with **Period / Incidents /
Limit / Action**: warning-window count/limit and stop-window count/limit. Plain
text uses equivalent labelled rows, HTML the existing card with a readable table.
Use supplied period values, not hardcoded weekly/monthly prose. Label the action
category (warning, VPS stop), not a guaranteed future operation; retain conditional
stop guidance and mode/suppression truth. Do not add enabled-warning promises from
fields that do not expose suppression. Both UIs use the same explicit columns or
responsive labelled cells, keeping current facts separate from saved evaluations.
Invalid current configuration retains null limits; no snapshot fallback. This
clarity requirement covers every visible count/limit on affected summary surfaces,
including compact overview/list alerts: numeric ratios must identify their period
and warning/stop meaning. Preserve threshold-only alert triggers and compact layout;
no full alert tables or per-row API requests. Keep generic discovery and shared
permission unchanged.

Legacy sidebar always restores **Incident reports** to the original filtered list
URL/return behavior. Add separate **Incident policies** pointing to existing
`?page=adminvps&action=incidents&veid=ID`; retaining this route avoids needless
breakage. Existing `vps.incidents.menu`/`.page` keep the policy-page intent and get
new labels; give the restored report-list link its own semantic ID. Alert links
continue to the policies page. React retains `/vps/:id/incidents` for policies
and adds a distinct reports navigation tab to the existing `/incidents?vps=ID`
list, preserving app/admin basePath and admin owner query context. The accepted
b1fb baseline has no report-list tab; this is a navigation addition, with no new
route/page/API. Root finalizes both labels. Preserve existing list/back behavior.
Individual source-report details show all authorized matched policies in stable
order, with per-policy saved detail and links. Active keys link to the relevant
VPS policy anchor; every saved key can link to authorized policy-filtered history,
including retired keys. No false/skipped outcome is labelled applicable; admin
error/skipped details remain separate. Notices use their explicit originating
policy fields. Never derive membership from codename or fetch arbitrary hidden
reports; use an authorized VPS association for live links and omit unavailable
links. No per-row list N+1 expansion is required by this detail-view request.

### Packages, compatibility and checks

| Owner | Files and complete deliverable | Dependency / faithful checks |
| --- | --- | --- |
| Owner1 | Backend `incident_policy.rb`, IncidentReport/IncidentEscalation/summary/action projections, ordinary Create/processing seams, task, node RPC handler; nodectl incident-report and libnodectld RPC client; affected API locales/specs/docs/packaging. Site `configs/vpsadmin/api/incident_escalation.rb` and its existing README. Own source/reference and fixture DSL updates. | Creation/selector/context and API contract above. Focused registry/model/concurrency/resource/task/mail/RPC/nodectl tests; real parser .save! and dry-run coverage. No template/gettext edits. Preserve actual producer authorization and no-duplicate effects. |
| Owner2 | React incident policy/history/notice components, API adapters/capabilities, CS/EN catalogs, affected unit/wire/browser tests and existing handbook/work log. | Layout can start from this contract; generated-member integration waits final SDK. Prove two policy rows with distinct limits, both links, retired/false/null cases, owner/admin and narrow layout; normal typecheck/i18n/audit/build checks. |
| Owner4 | PHP incident forms, VPS sidebar/routes, report detail, gettext and relevant regression/Playwright tests/landmarks. | Layout can start; real API execution waits owner1. Verify restored reports entry and separate policies destination, four facts per row, two matching policies, safe links, admin-only details and zero/reached alerts. No backend/mail locale writes. |
| Owner0 | Five incident template families in site CS/EN and built-in EN plain/HTML, associated renderer specs and site AGENTS writing rule. Existing older-email previews remain separate. | Existing plural mail payload and timing above; coordinate shared backend specs/Git window with owner1. Real builder renders for zero/one/two policies, unequal thresholds, late saved facts, mode/suppression, notices, escaping and desktop/narrow previews. No older-template restyling in this package. |
| Root-allocated SDK owner | Exact final API export and Go/Rust/TS regeneration/checks; deliver immutable TS development artifact for owner2 when required. | Remove source_type and add the readonly fields; retain raw export/provenance. Follow ordinary client synchronization. Registry publication remains a separate eventual React-merge prerequisite. |

No database columns/tables or migration rewrite are needed: existing source fields,
unique source_key and immutable report/key evaluations suffice. Preserve the single
original feature migration and current demo data. The declaration/context change
and removal of adapter metadata are an intentional unreleased feature-contract
revision, not a compatibility shim. Deploy paired backend/site declarations and
restart API/supervisor/task processes consistently before enabling new selectors.
Missing site file yields an empty registry. New backend RPC support must precede
new nodectl; old direct-SQL CLI use is unsupported for creation-time policies and
must be retired/held at activation, never repaired by later matching. Existing
node oomd transport remains compatible. Update templates before new senders where
needed, and API before new client fields are used. Capability-aware readers must
not infer missing membership. Preserve old rendered MailLogs, snapshots, source
refs and outcomes. Rollback requires a compatible backend/config/client set and
reconciliation of pending effects; do not silently downgrade or reset the demo.

Quick acceptance must prove: one ordinary manual or imported non-OOM report matches
two config-only rules; different selectors/limits remain independent; absent rules,
false results and failed selectors do not contribute; matched configuration failure
stays isolated; dry runs/updates/read/retry/scheduled processing do not invoke hooks;
rollback/retry and concurrent inserts preserve atomicity, dedup and one Stop; node
RPC rejects foreign VPS/provenance injection and token-content conflicts; old-owner,
late/future and explicit-action cases preserve privacy/count/mail semantics. Exercise
actual notification builders, not payload-only assertions. Final API export/SDK and
source checks follow committed source; mandatory independent review precedes long
checks. Then run only affected existing `alerts/incident-escalation` and
`webui#incident-escalation` integrations, extending their existing fixtures for the
generic/non-OOM and two-policy contracts, plus the scoped React browser/package
checks. Stop and return substantive failures to their owner; no broad CI campaign.
Root owns serial Git windows, final writing, review and any later demo refresh.

KB follow-up is source-scoped after final PHP: update the existing navigation
binding/related fingerprint for policies, add report-list navigation as needed,
and revise CS `navody:vps:incidenty` / EN `manuals:vps:incidents` instructions to
distinguish reports from policies. Preserve/reassess the existing three bilingual
concepts `getting-started/vps-list`, `restore-backups/playground-vps-list` and
`getting-started/vps-details`; sidebar geometry and labels require final-source
inspection, not an assumed new capture campaign. The capture fixture's policy DSL
must consume the new site-independent format. Final five-pin/source-contract work,
canonical media/runtime and production publication remain separately allocated;
this package starts none of them and reuses the parked assessment honestly.

**Nov18 PHP source closure.** Owner4's accepted source is
`51b79d2058ab4588b73a123aaff7a5a65ee610fe`, tree
`3313179196e1b204d39300a79adbc4f4ed03c07b`. Architect verified all ten committed
owned hashes against the accepted source inventory. Exact routes, landmarks and
geometry are retained in `nov18-php-policy-presentation/kb-impact.md`: policies
keep `vps.incidents.menu/page`; reports add `vps.incident-reports.menu`; saved
report sections add `incident-report.policies/policy/policy-diagnostics`.
The two article pages and three bilingual screenshot concepts above remain the
complete retained impact set. Root-accepted synthetic actual-PHP views retain
the legacy 1150px layout; they do not establish live browser or canonical media
acceptance. The existing browser scenario remains unexecuted on this package.
Final KB binding/fingerprint, fixture DSL, pins and affected media work still
require separate root allocation; this handoff starts none of them.

### Root-owned copy for owner0 (verbatim)

CS resource paragraph: Taková zátěž narušuje provoz ostatních VPS na stejném nodu.
Zkontroluj prosím využití paměti a nastavení služeb ve VPS. U webového serveru nebo
aplikace může pomoci snížení počtu pracovních procesů.

CS membership paragraph: Parametry VPS včetně paměti můžeš násobit současně
s navýšením členského příspěvku.

EN resource paragraph: This load disrupts other VPSes on the same node. Please
check memory usage and service settings. Reducing the number of worker processes
in your web server or application may help.

EN membership paragraph: For more memory, you can multiply your VPS resources
and increase your membership fee accordingly.

Keep existing actual KB URLs and the conditional stop warning; plain/HTML retain
the same facts. Root finalizes remaining table/UI terms. Add only this rule to the
existing mail repository AGENTS: “Read adjacent sentences and paragraph openings
together. Remove accidental repetition of ordinary words and repeated openings
(for example, consecutive If or Pokud) by restructuring the passage. Keep established
technical terms stable when repetition prevents ambiguity; do not cycle synonyms
solely for variety.” No installed skill/runtime package change is needed.

## Actual React package provenance — demo acceptance recommendation (2026-11-18)

The one reset is consumed; owner0 retains start parent 89743 and holds load/events
for root's assessment. This source/evidence inspection authorizes no operation.
Selected provider xgghi `bin/devcluster:nix_overrides` passes the React worktree
as a `path:` flake. Separately, `nix_common_env` obtains Git HEAD/dirty state for
cluster labels. Provider `flake.nix`/`nix/test.nix` pass those labels through but
select the React flake's frontend/BFF packages unchanged; labels do not supply
package provenance. React b1fb `nix/provenance.nix` reads `self.rev`/`dirtyRev`.
The path input supplies neither trustworthy revision, so its intentional fallback
is schema 1/unknown/dirty=true/source=unavailable. Actual frontend derivation
`dxhmd661...` explicitly has `VITE_BUILD_SHA=unknown`, `VITE_BUILD_DIRTY=true`;
`build/buildInfo.ts` preserves this fallback. Actual BFF derivation `y2wrm5yy...`
installs a separate writeText file from the same provenance value.

Existing owner0 evidence in
[the package receipt](nov17-devcluster-demo/postreview-2026-11-18/actual-react-packages.json),
[source parity](nov17-devcluster-demo/postreview-2026-11-18/actual-react-source-parity.json)
and [actual graph summary](nov17-devcluster-demo/postreview-2026-11-18/actual-store-graph-summary.json)
binds frontend `/nix/store/0fb7nng36g9820s28zhnfgklxsyrqp31-vpsadmin-webui-frontend-1.0.0`
and BFF `/nix/store/jrcw5s6bqc9pnkyqay2lkg48gf1x6fwd-vpsadmin-webui-bff-0.1.0`
to their captured derivations and cleaned source
`/nix/store/5cr6axnk9vs3rwwx49sawqgz4j5ddb58-source` (BFF subdirectory).
All 2,835 retained regular-file byte contents match reviewed
`b1fb37b0de3af6ef2f6f9e5f4f73ea0296b19c89` Git blobs, with no mismatches or extra
untracked files. The four omitted tracked paths are `.env.example` and three
`output/pdf/` files, all excluded by the reviewed filter. Actual recipes retain
the reviewed frontend/BFF npm dependency hashes and install/build hooks.
Provider `vpsadminWebui.inputs.nixpkgs` follows its OS-selected nixpkgs, so this
composition is not asserted identical to the independently tested standalone
outputs. The complete 6,707-derivation input capture stays with owner0; no duplicate
scan or output-equality claim is needed to establish this source-byte binding.

**Recommendation to root:** accept these as externally source-bound DEVELOPMENT
packages once owner0 closes the existing start and applied-output proof. Unknown
metadata is supported by React's resolver and the module's equal-provenance
assertion; it is not evidence of incorrect content. However, `PACKAGING.md`
requires matching full commits and false dirty flags for **clean release
acceptance**. These packages do not meet that requirement. Preserve embedded
values and historical standalone acceptance literally; do not relabel the
packages, describe the provider label as runtime proof, or claim full standalone
verification transfers to this composition. No provider/source correction or
rebuild is required solely to demonstrate this reviewed feature with the stated
metadata limitation.

The remaining acceptance fact belongs to owner0: after same-operation native
completion/reconciliation, bind the actual applied services/container selection,
effective nginx document root and BFF executable to the two exact outputs above,
then perform the already-planned authenticated UI verification. An unknown
`build-info.json` response alone cannot identify the running package. Root owns
release of the existing load/events package after assessing this result; template,
policy and Mailpit checks remain prerequisites to events. Any source/input mismatch,
unproved activation or failed start keeps that hold and preserves disks, roots,
credentials and evidence. Return the concrete fault for root's recovery allocation;
no second reset, automatic package change, rollback, or additional build/capture
campaign follows from this finding. KB/native uncertainty fences remain unchanged.

## Postreview verification and one refreshed demo (2026-11-18)

**Sufficient execution boundary for root allocation.** Reviewer0 returned no
findings across the four lanes and eight exact ranges in
[the final packet](nov17-generic-policies/final-review-packet.md). This addendum
supersedes the old demo's callback/unknown-limit and two-migration assumptions;
it authorizes no operation by the architect. Keep
[the original demo receipt](nov17-devcluster-demo/receipt.md) and raw evidence
intact. The user authorized ONE reset/reseed of this session's registered
`vpsadmin` cluster, slug `2026-10-30-oomd-abuse-policy`, after final reviewed
source. This is not authority over another cluster, the private KB/SMTP guests,
production, defaults or the session lifecycle. Leave the old demo running until
the released execution package reaches the reset boundary below.

### Inputs and reusable verification

Use backend `ee9025a8c99f3714d483daed0a6f028520594fbc`, React
`d26cfea0b7e993bc40a9a987c9e13dc78d552080`, site templates
`125f132a4c45ea8e8dbf6c392c7ca5f96e15a508`, and the single site declaration from
configuration `1efed32a70a91e8705be2ceeb6b7dac4ad19e10c`. Retain SDKs Go `bd0d1d2f`,
Rust `e34ef441`, TS `3cb7cf83` and the final packet's exact archive/hash. Export
and KB provenance remain literally backend `5aa1df7b`; the packet proves the
only successor differences are two spec paths, not new exporter/runtime inputs.
KB `4be305f1` remains a separate source deliverable, not the demo provider.
No rebase onto current backend default is required to run this reviewed demo.
Default drift must be reconciled for later integration readiness, not silently
introduced into this execution and its evidence.

Reuse API CI44214920284 (all26 topic jobs plus coverage), existing migration/
mail/PHP checks and the actual Rust44211967472 full matrices. Main
CI44214920366 skipped integration execution and cannot fill that gap. Owner2's
already released63242a68 owns exact React frontend/BFF package outputs and its
declared package checks; require its successful exact-source/output provenance
handoff, not another npm/type/build or Rust matrix. Provider packaging may
compose a different Nixpkgs input: record actual selected outputs rather than
asserting standalone output equality without evidence.

### Execution packages and order

| Owner | Complete bounded package | Required result / dependency |
| --- | --- | --- |
| Owner1 | From clean exact backend, run existing `./test-runner.sh test alerts/incident-escalation` in a fresh ordinary test-runner namespace. No application edits planned. | Real normal ingest/Stop, independent SMTP failure/retry, data-preserving restart and owner transfer pass. Retain native exit, selected source/OS/config, chain/mail evidence and artifacts. This test's mail outage/transfer belongs only to its disposable test cluster, never the demo. |
| Owner4 | Run existing `./test-runner.sh test 'webui#incident-escalation'` against the same reviewed backend, using its existing fixture and runner. | Real PHP/API Playwright: two metadata policies, independent override drafts/Inherit+Save, one shared permission, member denial, filtered history and CS navigation. `fixture_alpha`5/10 and `fixture_beta`3/6 are already declared in `tests/suite/webui.nix`; do not copy them into site configuration or the user demo. This proves generic UI/settings, not two-policy physical-stop behavior; retained engine/concurrency tests cover arbitration. |
| Owner0 | Prepare exact inputs/config/template/declaration and adapt the retained demo scripts to final resources; after the two checks and owner2 output handoff, own the one reset/start/load/seed/mail/UI demonstration. | Actual applied backend/React/template/policy/schema, two isolated CS/EN owners/VPSes,20 qualifying source events, real stop and mail outcomes, authenticated UI and user links. Keep the receipt in the existing demo record with a new dated section and separate raw filenames. |

Root sequences the two native VM checks and demo mutation so they do not compete
for unassessed headroom. Preparation can proceed meanwhile. Use the existing
runner and dev-session-monitor workflow, a fresh installed-policy watcher for
each long native operation, exact logs/exit and all owned handles accounted for.
Do not rerun broad API/PHP/WebUI suites or manually dispatch full CI. Stop at the
first substantive failure, retain evidence and return it to its source owner;
only affected corrections/checks/review follow. The existing webui definition
includes node2 but its selected script prepares node1; do not modify topology or
fixtures to optimize this batch. Builds may dominate elapsed time; milestones
are selected inputs, cache/build progress, guest readiness and test exit, not a
new arbitrary timeout. Unexpected local kernel compilation returns to root
under the existing cache rule, without a new capacity/build campaign.

### Demo preflight and the single reset boundary

Read-only installed-source inspection now selects runtime
`/nix/store/sm3pykcvx9yxjv8vimyzaw1l3dm4vd2i-dev-workspace-0.2.0` and provider
`/nix/store/xgghi0ln5akiy0kbl1n1g64svdz50fwv-vpsfree-dev-workspace-tools-0.1.0`.
Their public coordination guide and vpsAdmin README were read; these differ from
old receipt3shank/gzmnal and are not asserted runtime-equivalent by this design.
Execution must rebind the stable wrapper's selected package, exact registered
cluster/socket/runner, applied/pending state and shared bridge-address ownership.
A provider refusal or pending/uncertain operation is a concrete stop condition,
not permission to clear records or use private helpers. All old diagnostic/native
uncertainty fences, including the separately registered API diagnostic branch
and private KB/SMTP operations, retain their original recovery owners/contracts.

The provider still selects this session's backend/React/config worktrees; without
an OS worktree it uses canonical local `origin/staging`, with no automatic fetch.
Bind the actual OS hash and all optional selected inputs during preparation;
old42baba is historical evidence only. Check normal compatible disk/module APIs
and cache availability before destructive work where the public interface permits.
No provider pin/alias/worktree registration or production configuration update
is part of this package. Preserve current regular per-cluster config privately
outside `.dev-clusters/vpsadmin/clusters/<slug>/` before reset, including seed
accounts and intended domains, without printing secrets. Retain `dns.enable=false`,
React enabled, Mailpit capture, `single`/`bridge`, existing resources and no storage
profile. Do not restore old applied envelopes, disks, database or callback files
into the new cluster. Let the ordinary reset/start own fresh cluster credentials;
do not manually rotate provider-global certificates or other session secrets.

Refresh host capacity/shared use once before each native VM batch and again at
the reset/start boundary. For the demo reuse the assessed100GiB incremental disk
plus20GiB shared floor,48GiB available RAM and20GiB shm, with one Nix job/core;
these are operating allowances, not measured peaks/reservations. Current provider
source declares services8GiB/4CPUs, node1 normally8GiB/4CPUs,12GiB services root
image/writable disk and the retained20GiB tank configuration. Bind emitted actual
resources. Existing usage is counted once in fresh free values; do not add the
parked128GiB vendor allowance or reclaim private state to pass. Material resource,
OS/source or provider incompatibility returns to root before reset if known.

After these preconditions, use ONLY the normal stable commands on this exact slug:

```sh
vpsadmin-devcluster reset 2026-10-30-oomd-abuse-policy
vpsadmin-devcluster start 2026-10-30-oomd-abuse-policy --topology single --network bridge
```

Between them, initialize/restore the saved intended per-cluster configuration
through the supported config path; capture `config`/`urls` output privately since
they contain credentials. The public reset owns runner shutdown/reaping and
cluster-state removal; do not call internal reset/stop helpers or broaden cleanup.
There is no separate public build-only command to prebuild the complete fresh
cluster here. Preparation/package checks therefore cannot promise all start work
will finish before reset. Old start took53m14s; use20–60minutes as a cache-dependent
planning estimate, not an enforced cutoff or promise. Report cache/source failures
with the exact phase. Do not perform a second reset as a retry.

### Load, fixtures and acceptance

Fresh DB setup must install the ONE original feature migration20261030180000
after its normal predecessor;20261115120000 must be absent. Verify the evaluation
table/per-policy membership schema and matching API resources before events.
The installed provider still discovers only the legacy template basename; use
the proven ordinary public reconciliation seam, with no alias/symlink/provider
edit: copy hash-verified site125f `templates/` to an owned guest directory and run
`vpsadmin:notification_templates:reconcile[PATH,SOURCE_ID]` through the deployed
API package, binding SOURCE_ID to125f/digest. Verify the five incident families'
CS/EN subject/plain/HTML DB contents and source identity; builtin installation
alone is insufficient. Preserve the separately reviewed older HTML content.

Install only config1efe's exact `configs/vpsadmin/api/incident_escalation.rb`
as regular restricted component-readable files under the actual API/supervisor/
database `configDirectory` paths (normal defaults
`/var/lib/vpsadmin/{api,supervisor,database}/config`). Do not load the whole
production configuration. Reuse the accepted regular-file installation method,
resolve actual unit paths/users, then restart normal API, supervisor and scheduler
processes and await health. Bind identical file digest and loaded registry in each
deployed package/config and subsequent saved evaluations; a standalone parser
alone is not proof that a running process reloaded. Tasks use the API config.
Template reconciliation and process activation both precede any fixture event.
Verify the actual nodectld SMTP endpoint is capture-only Mailpit (previously
loopback1025) and the authenticated capture UI; never send production mail.

Reuse the retained demo's normal API-create and node-scoped `vps_events` publisher.
Adapt only IDs/digests/collection reads to the final schema. Dedicated CS
`test-user1` and EN `test-user2` each get one clearly named1CPU/1GiB/4GiB VPS with
no IP allocation; record actual IDs and wait for completed create/running state.
Only this isolated demo's global mode becomes enforce; keep site base5/10,
null limit overrides and shared shutdown permission enabled. Save one new event
plan with20 unique nonfuture whole-second node/VPS/time/action tuples before
publishing. These are explicitly synthetic memory-pressure events, not real
resource diagnoses. Publish one per owner and verify ordinary mail; reach five
and wait for warning mail; only then reach ten. Reuse an already-published tuple
only for reconciled recovery/deduplication, never invent a new event to retry mail.

Expected results:20 ordinary source reports/evaluation memberships plus two
warning and two confirmed-stop notices, four action rows, exactly two successful
physical Stop chains and24 corresponding incident messages. Count incidental
login mails separately. Prove Stop transaction success, action completion and
actual node stopped state before accepting stopped mail. Prove mail transaction/
MailLog and Mailpit plain+HTML separately; queued is not sent. Check both languages
at ordinary/warning/stopped milestones, saved policy identity/contributors and
the compact source/policy text. Existing no-selector site declaration remains
unchanged: create-time-only selector behavior is covered by the exact engine
tests, not falsely demonstrated by this no-hook demo. Read/retry/reconciliation
must retain saved evaluations and never reclassify membership.

Inspect authenticated PHP and packaged React as admin and each owner: zero-count
baseline has known5/10 limits and no overview warning; after thresholds the
hostname/overview alert links to Incidents, and the subpage/tab shows current
counts/limits, generic policy metadata, saved historical detail and scoped links.
Verify owner isolation/foreign-report denial and admin-only forms. Do not accept
old callback-based Unknown/unavailable limits as normal. Multi-policy discovery/
settings acceptance comes from owner4's reviewed two-policy test; no second
production/site policy or selector instrumentation is needed in this demo.

Owner0 records applied system paths, loaded component/React package identities,
template/declaration hashes, migrations, actual fixture/report/action/chain/mail
IDs and authenticated route evidence. Preserve ordinary secret handling: user
links remain PHP `https://webui.aitherdev.int.vpsfree.cz/`, React
`https://newadmin.aitherdev.int.vpsfree.cz/` and Mailpit
`https://mailpit.aitherdev.int.vpsfree.cz/` only after actual readiness confirms
them; supply new deep links/IDs, and retrieve logins through existing portal
Accounts/secret channel. Do not reuse old Mailpit IDs or put credentials in notes.
The useful intermediate milestone is healthy exact-input UI/Mailpit, then first
ordinary mail; fixtures normally need5–15minutes after readiness.

On failure retain new disks/config/roots, logs, pending chains and original
receipts. An interrupted command is not proof of no effects; inspect its native
status and provider/DB/queue evidence before same-operation recovery. After reset,
prefer forward recovery on the reviewed compatible schema; old4842/callback
software cannot be assumed to load final data. No automatic downgrade, repeated
reset, fake completion, message deletion or replay. Leave the successful refreshed
demo running. KB canonical runtime/media remains independently parked: source4be,
three bilingual crop concepts and existing capacity/evidence are retained; the
minimum later package is final-source supported runtime admission plus only
actually affected captures/strict validation, separately allocated by root.

## Live-demo feedback revision — implementation boundary (2026-11-17)

This section supersedes the card-layout and overview-panel instructions below.
Inspected baseline: backend4842e75b, site d42ad451, React8ce6baac and site config
0be59e51. The running demo is recorded in [its receipt](nov17-devcluster-demo/receipt.md):
24 incident reports/MailLogs, two real completed stop chains and two stopped VPSes.
Preserve that historical evidence and running state during implementation. The
user subsequently confirmed no external migration consumers and authorized one
final ordinary reset/reseed after reviewed source/schema/UI stabilize; that reset
may replace the24 demo rows/messages. No new events or runtime mutation belongs
to this design task. Root owns final CS/EN wording and package
allocation. Application owners implement the following sufficient boundaries.

### M — mail/source wording (independent; sufficient to start)

**Latest user decision:** use the card layout throughout. M keeps the existing
incident card; H separately brings older HTML templates to that layout. This
supersedes the earlier blue-table proposal. Plain/source edits remain released.
The UI/API boundary is now configuration-driven policy discovery, superseding
the earlier one-policy/no-schema-change recommendation. Its sufficient contract
is being settled before owner1/owner2 edits.

Owner0 owns site `templates/{vps_incident_report,vps_incident_warning,vps_incident_stopped,vps_memory_pressure_warning,vps_memory_pressure_stopped}`
(CS/EN subject/plain/HTML as affected), matching built-in EN templates under
`api/notification_templates/templates/`, and only the oomd restart/stop source
message entries in `api/lib/vpsadmin/api/locales/{cs,en}.yml`. Owner0 also owns
the affected existing mail-template, ordinary-send and source-event renderer
specs. Owner1 must not edit these locale entries/specs concurrently; shared Git
index/commit windows remain serialized by root. Retain the site AGENTS card-style
reference under the user's final uniform-card choice.

Source text describes the observed restart/stop and its effect on availability
of other VPSes on that node. It contains no appended policy explanation. Root
supplies final source translations. Existing source qualification, owner language,
captured evaluation, counts, payload fields, notice provenance and retries remain
unchanged. Ordinary `incident_policy` uses its saved evaluation. Aggregate mail
retains the existing current-restriction calculation for limits/stop_enforced,
alongside saved action counts/contributors. M changes templates/locales only;
do not change either producer's payload, current-setting lookups or timing.

Use the heading `Přehled incidentů` / `Incident summary` (root final copy pass).
Show the 7-day count without a warning threshold and the 30-day stop count as
`7/10`, with its period and meaning clear. Align warning messages with this compact
format; remove claims that snapshot limits are current. The ordinary/warning
possible-stop sentence is exactly conditional on the existing saved
`stop_enforced`: `Pokud se tato situace bude opakovat, VPS může být vypnuto.`
Root supplies the matching English. Preserve real confirmed-stop wording and
conditional repeat-stop semantics; missing optional evaluation produces no
invented counts or policy section. Keep useful contributor/history links without
empty/unavailable filler. Do not remove meaningful source actions or details.

All five incident HTML families retain the existing `ip_release_requested`
card outer layout, with compact readable data tables and ordinary paragraphs/
links inside. No new layout/renderer abstraction. Explicitly escape all dynamic
HTML/URLs. Preserve
plain/HTML and CS/EN factual parity and the standard automated-mail footer.

Quick acceptance: existing normal producer/render specs plus template checker;
inspect actual rendered CS/EN ordinary/warning/stopped messages, saved7/10 case,
both stop_enforced outcomes, missing policy/manual mail, plural boundaries,
escaping and whitespace. Use repository Nix commands/hooks. No enforcement,
schema/client contract, migration, site-policy or runtime change in M. All old
MailLogs stay byte-identical; later demonstration of changed mail uses separately
authorized fresh examples, never rewriting or replaying the24 old reports.
Template reconciliation before any new producer/event remains required. Root's
final writing pass precedes commits; independent final affected-lane review follows
committed quick checks, with ordinary CI selection and no new full-suite campaign.

The UI/current-limit contract and separate migration recommendation are being
settled below; neither is a prerequisite for M.

### H — existing HTML uniformity (independent; sufficient to start)

Owner4 owns styling only in existing `*/email/*.html.erb` outside M's five incident
families: site templates currently have28 such variants, including the already
conforming IP-release pair; built-ins have4 (`ip_release_requested` EN,
`ip_release_reminder` EN and `password_recovery` CS/EN). Do not create HTML for
plain-only templates or change subject/plain/meta files. Reference the actual
site/built-in IP-release card: document charset/viewport, gray body background,
Arial text and white centered max-width640px presentation table, border/radius,
24px inner padding. Reuse that outer layout directly, preserving readable data
tables, headings, lists and operational links inside. Keep already-conforming
files byte-identical unless a real inconsistency needs correction.

Preserve rendered text, conditionals, dynamic data, URLs/actions, footer, escaping
and recipient/privacy behavior exactly. Existing template-local formatting helpers
stay local. No shared renderer/CSS framework, logic cleanup or unrelated wording
change. Necessary escaping correction must retain visible text/URL meaning and
be called out, not mixed into a silent broad refactor. Owner0 owns M and site
AGENTS; coordinate shared renderer/spec files rather than editing them together.
H must be committed separately from new incident templates, per explicit user
instruction (separate scoped commit in each affected repository). Root sequences
each repository's index/commit window; no branch integration is authorized.

Quick checks: actual template checker for site and built-ins, render each changed
variant through the existing builder with synthetic representative inputs, compare
visible text/link targets and conditional content with its baseline, inspect
representative dense table, simple message and both languages at narrow/desktop
width. No personal data, production sending or new fixture events. Preserve raw
previews outside Git and hand root a concise changed-file/render comparison for
the final visual pass and independent review. Styling has no API/client/migration
dependency; it does not block M, registry design or preserved-demo work.

### G — generic policies: final creation-time contract

**Settled user choices:** several policies may match the same stable source type;
configuration declares limits and an optional applicability hook. There is ONE
policy format, not fixed/dynamic threshold variants. Applicability runs only
when a trusted source incident is created. Reads, retries, scheduled processing
and later configuration changes never reclassify existing incidents. No product
question remains for this package. This replaces the older callback/unknown-limit
contracts below; M/H's wording/layout work remains independent.

#### Registry, source boundary and execution

A policy has a stable configurable string key, supported source adapter/type,
localized labels and optional short description, declared warning/stop limits,
optional applicability block, optional declared action suppression, and optional
warning/stopped template names (generic fallback). One conventional declaration:

```ruby
rule :memory_pressure, adapter: :node_oomd do
  labels en: 'Memory pressure', cs: 'Přetížení paměti'
  limits warning: 5, stop: 10
  applies_if { |ctx| ctx.owner[:role] != 'admin' } # optional; absent means true
  suppress_actions false                        # optional; default false
  templates warning: :vps_memory_pressure_warning,
            stopped: :vps_memory_pressure_stopped
end
```

Names/copy in the example are illustrative; root supplies final site text.
Keep the actual site's existing stable key to avoid unnecessary identity changes.
Keys use the existing SystemConfig identifier alphabet:1–59 ASCII letters,
digits or underscores (`[a-zA-Z0-9_]{1,59}`). The16-character `incident_policy_`
prefix must fit its75-character category. Configurable/arbitrary means not a
hardcoded policy list or generated enum, not unrestricted free text. Reuse this
direct category mapping; no encoding/hash/alias subsystem. Preserve each accepted
key exactly, and reject duplicate keys including case variants that collide under
the database's identifier-value collation. Use the returned key in paths/settings;
do not infer it from a localized label. Check the59/60-character boundary and
invalid characters alongside ordinary unknown-key handling.
No policy key is an API enum or a UI branch. The initial adapter remains
node_oomd; it owns source type/codename oomd, restart/stop qualification and node
provenance. Multiple declarations may bind it. Transport is not source identity.
Adding a policy using an existing adapter needs only config/restart; a genuinely
new protocol needs a backend adapter. The generic registry does not make arbitrary
manual codenames trusted. Reject duplicate keys, invalid declarations/limits,
unknown adapters and malformed templates at startup. Remove the old threshold
callback form rather than supporting abandoned development formats. Missing site
file supplies the ordinary built-in declaration in this same format.

Global mode remains per-policy SystemConfig (observe/notify/enforce); it is the
permission ceiling. Existing global/VPS nullable limit overrides retain precedence
VPS > global > declared base. Suppression is a declared boolean: matched incidents
still count, but create no action. A false applicability result excludes membership
and counts. Shared VPS exemption still prevents escalation stops, not collection
or eligible warnings. No arbitrary per-event limit/mode/suppression evaluator is
retained. Limits are current declared facts, independent of whether the next
incident matches. Valid current status describes thresholds, not a promise of a
future action. Persisted invalid override combinations fail closed for that policy
and report configuration_valid=false with null effective limits/status; this is
an actionable configuration error, not the old dynamic-policy Unknown state.

At ordinary trusted ingestion: validate source/node identity and dedup key; under
existing settings/VPS locks reconcile owner epoch and prior physical outcomes;
insert ONE source report and perform the source log effect once. Capture one now,
owner/VPS/source/settings view, then visit bound policies in lexical key order.
Each optional applies_if receives frozen values, never model objects: source event
id/type/action/time/node, VPS id/node/state, owner id/role/state, accounting epoch,
policy key, prior matched7/30-day counts, global mode/overrides, VPS overrides and
stop exemption. Prior counts EXCLUDE this event for the selector. Matching must
return exactly true/false; exception/nonboolean is an isolated selection error.
Trusted hooks must be short and side-effect-free, with no I/O. No new sandbox,
workflow engine or hook scheduling subsystem.

An absent selector matches. A true result records membership, then the engine
computes counts INCLUDING this event and its declared effective policy/decision.
Compute all policy outcomes before creating/dispatching effects, so policy order
cannot hide another policy's matching/evaluation. One policy's selector or effective
configuration failure neither drops the source nor prevents other policies from
being processed. Save safe error stage/class, never exception messages or raw
external data. Selection errors do not count; matched incidents count even if
subsequent configuration/decision evaluation fails. No retry reruns the hook.

Source-qualified late/future events still receive their one creation-time match
attempt, but existing timeliness gates prevent actions: late matched reports may
count within rolling windows; future matched reports count only once their event
time enters a window and are never replayed for action. Prior-owner/epoch and
unqualified reports are retained only under their existing audit/privacy rules,
without hooks or membership in the current epoch. This explicitly extends only
creation-time matching to source-qualified audit-only events; there is still no
threshold callback/effect there. Manual API/nodectl/mail reports and generated
warning/stopped notices do NOT enroll merely because they share a codename.
Source adapters are the only ingress to automatic matching; no broad model-create
callback. Duplicate source delivery returns the existing report/outcomes and
never tries newly added policies. Policy removal/edit/addition affects subsequent
source creations only. A renamed key is a new policy, with no historical backfill.

#### Persistence, counting, history and privacy

Replace the singular report policy_evaluation JSON with a small
IncidentPolicyEvaluation model/table in the ONE original feature migration.
One row per (incident_report_id, policy_key), enforced by a unique index, stores:
policy_key; source report association; matched nullable boolean; state
(recorded/skipped/error/audit_only); evaluated_at; and one JSON snapshot containing
policy metadata/digest, captured context, effective limits/mode/suppression and
decision none/warning/stop. Error rows also retain safe stage/class. matched=false
+skipped means deliberate nonmatch; matched=null+error means failed selector;
matched=true+error means selection succeeded but decision/configuration failed.
Audit-only retains match result where attempted and no action. These are internal
outcomes, not an audit subsystem or new routine member-facing diagnostics.

The snapshot includes stable source_type, bilingual label/description and selected
template identities needed to explain/render that historical policy after edits.
It does not contain callback code, whole model objects or credentials. Keep key,
matched/state and report association indexed for real SQL membership queries;
avoid JSON scanning for ordinary counts. Source report/user/VPS/event time remain
the authority, not duplicated mutable identity columns. Decisions/snapshots never
change after durable ingestion; action/notification state remains separate.
A source report and all outcomes commit atomically. Uniqueness plus existing locks
protect duplicate/concurrent delivery. 'Once' means once for a successfully
persisted creation; a transaction failure before commit must not be advertised as
exactly-once arbitrary external side effects, hence the pure-hook requirement.

Each policy counts only its persisted matched=true source reports in the existing
UTC open-lower/closed-upper7/30-day windows and current owner epoch, once per source
report. No matching scan over old incidents, no enrollment by codename, and no
re-evaluation after settings changes. Contributors, latest incident and warning
cooldown use the same policy membership. New policies start at zero. Removing a
policy leaves its historical evaluations/actions/notices intact; do not create new
actions for it. Pending actions from a removed/changed declaration obey the normal
saved-digest/current-restriction fail-closed rule. Already dispatched physical work
still reconciles from its chain; its factual outcome/notice uses saved metadata,
not a missing live registry entry. Retain ordinary mail/retry identities.

Actions use policy_key explicitly and reference their exact evaluation. Preserve
unique source-report/policy action identity, per-policy contributor snapshot,
notice ID, stable message ID and mail state. History supports an explicit
policy_key filter distinct from source codename: source rows qualify via their
saved matching membership, notice rows via their owning action. Filter with EXISTS
or distinct IDs so multiple policies never duplicate a source report or pagination
total. Historical retired keys remain queryable within authorized history even
though active discovery omits them. Raw contexts/errors stay internal. Owner scope
and ownership-transfer epoch apply to evaluations, report links, contributors and
notices just as to existing source reports; forged/foreign keys do not widen access.

#### Multiple actions and one physical stop

First derive each matching policy's candidate under its own counts, global mode,
suppression, warning cooldown and current shared VPS restrictions. A policy chooses
stop over warning when both qualify. Eligible warnings remain per-policy and have
independent7-day cooldown/mail identity. If the same source event has an eligible
stop group, suppress redundant warning candidates for that event; do not describe
suppression to members. Preserve already dispatched messages and their history.

Stop candidates for one source report form a bounded group using the existing
VpsIncidentAction rows, not a new orchestration service/table. Add nullable
stop_owner_action_id for follower linkage. In the existing VPS serialization and
normal resource lock, revalidate current restrictions/digest/counts for every
pending candidate WITHOUT hooks. Suppress ineligible candidates independently.
Among the remaining candidates choose lexical policy key (ID tie-break) as physical
owner, invoke the normal Stop chain ONCE, and atomically bind all eligible group
rows to that same chain; followers point to the owner. Pending resource contention
leaves the unsubmitted group retryable. A selector/config failure or revoked
candidate cannot prevent another eligible candidate from becoming owner.

Any outstanding physical stop group excludes another stop chain for the VPS,
including later incidents/other policies. New incidents still get all saved match
outcomes/counts, but cannot duplicate the outstanding physical action. Once a chain
exists, neither owner nor follower dispatches another one on retry. Failed or
uncertain physical outcomes keep the shared exclusion and require existing
reconciliation; do not elect a follower to replay an uncertain stop. A successful
chain plus successful Stop transaction confirms the entire submitted group,
updates the VPS-wide last-stop timestamp once and starts the existing24-hour
cooldown. Reconciliation never reruns selectors. A fresh qualifying creation at/
after cooldown is still required; no daily timer stop.

Each submitted policy retains its own action/history and may send ONE policy-named
confirmed-stop notice after that common success; these are several explanations
of one physical stop, not several stop operations. Never claim a skipped/revoked
candidate caused it. Warning/stop subjects or body metadata identify the policy
using saved localized labels. Mail failure/retry is independent per action and
must never retry the physical stop. Shared VPS read state collapses followers to
one outstanding physical operation/chain, including failure/uncertainty. Exemption,
mode changes and ownership reconciliation retain existing pre-dispatch gates;
already submitted work may finish. This deterministic choice needs no user-facing
priority setting or additional product decision.

#### Generic API and UI data

Authenticated IncidentPolicy Index/Show at /incident_policies[/{key}] discovers
all active declarations, including no saved overrides/incidents. Typed fields:
key, localized label, nullable plain-text description, source_type,
warning_period_days=7, stop_period_days=30; settings_category is admin-only.
No evaluation_kind/fixed/dynamic choice remains. Keys are runtime strings, never
schema enums. Unknown active key fails explicitly. No callback source is exposed.

VPS::IncidentPolicy Index/Show/Update at
/vpses/{vps_id}/incident_policies[/{key}] returns one typed row per declaration:
the above metadata; count_7d/count_30d; configuration_valid; nullable effective
warning_limit/stop_limit/status (clear/near_limit/warning/stop_threshold);
global_mode; nullable effective_mode and stop_enforced; last_incident_at,
last_warning_at; evaluation_report_id/evaluated_at/evaluation_state
(none/recorded/error). Latest evaluation metadata means latest matched or failed
attempt, not a claim of applicability now; silently skipped attempts need no UI
banner. Raw nullable warning_limit_override/stop_limit_override are admin-only.
Valid declarations/configuration supply known limits and threshold state even
when applicability uses a hook or there are zero matches. All configured rows
remain visible; never run the hook to decide which panels to show.

Admin-only Update targets the key and only those two nullable overrides. Omission
preserves, null inherits, positive/order validation is atomic and audited; return
the authoritative row. Shared shutdown permission is a separate VPS update with
no policy key requirement. VPS retains shared accounting_since/confirmed-stop/
next-stop/action-state/chain fields exactly once. Add incident_warning_count and
incident_stop_threshold_count: batched counts of active policies at each reached
threshold, with stop precedence per row and configuration-error rows excluded.
They support list icons and overview alerts without per-VPS HTTP requests or hooks.
Retire this unreleased feature's old default-selected flat summary/override API.
An optional server policy/status filter takes an explicit key, no implicit policy;
filter before pagination with the same membership/status logic as returned counts.
All new resources use existing owner/admin authorization and epoch/privacy.

IncidentReport::PolicyEvaluation Index at
/incident_reports/{incident_report_id}/policy_evaluations provides the compact
historical detail through the already-authorized parent report: policy key/saved
localized label, evaluated_at, saved counts/limits/effective mode/stop_enforced,
decision and state. For members return matched successful/audit-only outcomes
with absent facts left null; admins may also inspect skipped/error state and safe
error stage/class. No raw context, hook, reason dump or exception message. A notice
uses its existing trigger link and action's policy identity. History filtering and
this nested reader use saved keys/metadata even after registry removal. Both UIs
can render this typed collection on incident detail without source-policy branches
or historical values becoming current limits. This is a bounded projection of
the same evaluation rows, not a second audit store.

PHP: one Incidents VPS sidebar subpage via existing vps_details_submenu/sbar_add.
React: one Incidents tab under VpsLayout/VpsTabsNav, preserving app/admin and list
context. Both iterate policy rows generically, with compact count/limit rows,
metadata label, policy-filtered history and a collapsed details area for meaningful
timestamps/history. No oomd key/adapter/memory-help branches. Live thresholds use
declared+override values; saved snapshots remain dated history, never fallback
current limits. Remove verbose overview panels and permanent per-policy list
columns. Show only reached warning/stop-threshold overview alerts linked to the
page; PHP warning.png beside hostname/top detail, React existing Alert conventions
and compact desktop/mobile indicators. Preserve disk/rescue/network/action errors.
No near-limit/unknown/prose panel on the overview; threshold does not promise a stop.

Admin controls group each policy's limit fields and one shared permission control
separately. Inherit clears the selected limit draft, Save performs the explicit
write; it must not reset shared exemption. Show inherited values only from current
server facts. Preserve PHP CSRF and React target confirmation/preflight/uncertain
write locks/exact readback. Link admins to existing policy-global SystemConfig
using metadata; no new global settings subsystem. Root owns final CS/EN copy.
For legacy PHP this is the existing `?page=cluster&action=sysconfig` page,
which lists all categories and has no category route/anchor. Link there with an
honest global-settings label and show the escaped `settings_category` beside it
for admin orientation. Do not append an ignored category query or imply a scoped
editor. No `cluster.forms.php` expansion is needed for this package. The new VPS
subpage uses `?page=adminvps&action=incidents&veid=...`; ordinary nested HaveAPI
access remains subject to owner1's actual resource-description proof before
real API execution.

#### Ordinary mail collection: dependent follow-up after M

ONE ordinary source report still produces ONE ordinary source email. Replace the
singular incident_policy variable with incident_policies, a lexical-key-ordered
array of bounded saved summaries for matched, successfully recorded evaluations.
Each entry has key, localized saved label and the existing saved counts/limits/
mode/stop_enforced/time fields. No entry for skipped/failed/audit-only decisions;
empty array produces source facts only. Do not select an arbitrary first policy,
combine incomparable counts or duplicate the ordinary email. Policy-keyed warning
and stopped mail retain per-action saved counts/contributors and existing
current-restriction calculation; hooks never run during rendering/retry.

**Aggregate base clarification (2026-11-18).** For an existing action whose
policy is still registered, apply the deterministic current global/VPS limit
overrides, global mode and shared shutdown permission to that action's saved
evaluation `base`, preserving the pre-G `action_result` calculation. Do not
replace that base with the active declaration merely because declared limits
are now available without a callback. A later declaration edit affects new
evaluations and the live policy summary; it does not replace the base of a
dispatched/completed action's delayed email. For example, saved stop10 then
declared stop20 yields aggregate stop10 without overrides, or stop25 with a
current override25; live summary without an override is20. Aggregate templates
must not label this projection as the live policy configuration. Ordinary mail
and historical evaluation readers remain entirely snapshot-based. Retired-policy
factual outcomes retain saved effective values with observe/suppressed behavior
and no possible-stop claim, as already designed. Pending-action digest checks,
dispatch eligibility, saved counts/metadata/contributors and existing MailLogs
are unchanged. Owner1 owns the narrow calculation correction after the active
source freeze ends; coordinate the existing delayed-mail case with owner0's
spec ownership. Add only the declaration-edit versus override distinction to
the affected existing case, plus its live-summary assertion; no new framework,
hook invocation or runtime event is needed.

Owner0 owns this small dependent G-mail follow-up AFTER M commits, under a separate
root edit/Git window: ordinary producer/projection and affected producer/render
specs, ordinary site CS/EN+built-in EN templates loop over summaries, retaining M
copy/card. Show the label when multiple summaries need disambiguation; retain the
single-policy compact appearance. Put the conditional possible-stop sentence once
when any entry permits it. Generic aggregate templates must identify their owning
policy from metadata, without source-specific code. Owner1 owns evaluation model
access/typed snapshot contract and exposes it before handing these paths to owner0;
no concurrent shared-spec/producer/template edits. H's older templates stay out.
Root's final wording pass still applies. M's singular tests prove only M, not G.

#### Packages, compatibility and bounded verification

G1 owner1: registry/selector/source-dispatch, evaluation/actions/group reconciliation,
counts/privacy/history filters, public API, ONE consolidated migration/core schema,
backend/API reference and metadata, and focused Ruby/API specs. G-PHP is the
independent owner4 boundary below. Owner1 has returned it without PHP/gettext/test
edits and owner4 has confirmed capacity after accepted H; root allocates the
source/layout start. Avoid M/H paths until the named
dependent handoff; coordinate any source-event spec changes.
G2 owner2: React typed adapters/tab/collection/settings/alerts/catalogs,
requirements/workflow/inventory/docs and tests. G3 owner3 (root allocates): final
Go/Rust/TS generation from G1's clean committed export plus site declaration/docs,
using declared5/10 and optional real applicability only if intended; production
site behavior otherwise unchanged. Root assigns source/config/SDK Git windows.
No enum generation from configured policy keys; use generated resource members
and actual backend capability gates, no raw transport bypass or single-policy
fallback. Owner2 may build generic UI against the agreed typed fixture contract,
but final checks use G3's exact SDK. Preserve registry release prerequisite before
React default integration; development artifacts remain allowed meanwhile.

**G-PHP ownership and dependencies (sufficient; ready for root release).**
Owner4 can own legacy presentation in `webui/forms/incident_policy.forms.php`,
`webui/forms/vps.forms.php`, `webui/forms/incidents.forms.php`,
`webui/pages/page_adminvps.php`, `webui/pages/page_incidents.php`, a focused new
incident-policy subpage/helper if the existing dispatch convention needs it,
and narrowly necessary `webui/public/js/vps.js` draft-clearing behavior. Scope is the
generic sidebar/subpage, policy collection/settings, policy-filtered incident
history/saved detail, hostname/top-detail threshold warnings and removal of the
old overview panel/list column. Own corresponding PHP gettext source/catalogs
under `webui/lang/` and existing PHP regression/browser tests, especially
`webui/tests/Regression/IncidentPolicyTest.php` and
`tests/playwright/webui/specs/incident-escalation.spec.cjs`. Keep meaningful
documentation landmarks/source-contract assertions beside the actual controls.
No API model/resource/schema/Ruby locale/mail edits and no shared
`docs/incident-escalation.md` write; owner1 retains backend reference/API metadata.

The settled resource/privacy/field contracts above are sufficient for layout,
helpers, generic client calls and synthetic response tests. No unresolved product
or authorization choice invalidates starting those after transfer. PHP consumes
the ordinary HaveAPI resources and their discovered capabilities; absent support
hides the feature, while forbidden/not-found responses retain normal error and
owner boundaries. Do not fabricate server data, bypass authorization, hardcode a
policy or reinterpret historical values as current to make fixtures pass.
Real backend/API browser execution waits for owner1's stable resources and
evaluation/history/mutation contracts, followed by a joint API/PHP freeze.

Owner1 confirmed no webui/gettext/PHP-test edits and returned these paths; owner4
confirmed availability with H effects terminal. The transfer prerequisites are
satisfied; root can release source/layout now. Owner1 sends exact implemented
resource methods when stable before real API tests. Root
serializes shared worktree index/commits and locale generation. The existing
incident browser fixture/case in `tests/suite/webui.nix` may pass to owner4 only
in an explicit short file window after owner1 supplies the stable creation/schema
seam; no parallel edits to that shared fixture. Owner1 owns any necessary
cross-cutting CI selector changes, incorporating owner4's changed-path list.
Owner4 returns focused PHP syntax/regression and gettext checks, two arbitrary
policy response cases, escaping/owner/admin/CSRF/draft-inheritance behavior and
the bounded Playwright update. Actual browser evidence follows review/stable
backend and the separately released final demo reset; no new runtime campaign.
Owner4 supplies the final PHP route/landmark/layout delta to the existing KB
assessment owner without changing capture pins/media or reviving parked capacity
work. Root retains final CS/EN wording, acceptance and Git order. This is an
ownership split only; the data, privacy, UI and runtime contracts above stand.

Quick G1 matrix: two policies on the SAME real supported source with always/true/
false/error matching; stable lexical order; saved outcomes and exact counts; one
source/mail identity; one selector call per durable creation and zero on duplicate,
read, retry, scheduled processing/config change; late/future/old-owner/manual/notice
boundaries; one failing policy does not affect another; overrides/suppression/
shared exemption; two stop candidates -> one normal chain, distinct policy outcomes,
no follower replay after failure/uncertainty; warning cooldown/stop cooldown and
transfer/concurrency regressions. Assert no extra source effect/log and correct
membership/pagination/history privacy. One consolidated migration from its exact
pre-feature predecessor, schema equality and intended rollback on disposable DB;
no old-feature upgrade guards. Use existing RSpec/API/PHP facilities and update
static topic/CI selection only for real new file placement.

G2/G-mail: two arbitrary policy keys with different labels/matches/limits; zero
matches still discovered; history distinct IDs; threshold-only overview warnings;
member/admin/CSRF/confirmed target/uncertain write behavior; generic count layout,
mobile/tab/sidebar routes/context; saved multi-summary plain/HTML/CS/EN parity and
escaping, all-skip/error source-only mail, one ordinary delivery plus per-policy
notices. Run focused Nix-native API/PHP specs, typecheck/React tests/build and
locale/docs checks, all three client checks and final-source schema provenance.
Independent final review follows committed quick checks; longer concurrency/
alerts/affected-WebUI integration follows review via normal runner/CI selection.
No new workflow, arbitrary full-suite repetition or private guest/capacity campaign.

This is an unreleased contract/schema replacement with user-confirmed no external
migration consumers. G changes share the ONE original feature migration, remove
the additive migration, and need no old-feature data conversion, dual-format reader
or compatibility subsystem. Keep old refs/evidence. Running demo stays untouched
until final reviewed source/schema/UI/M/H/G-mail are stable; then root releases ONE
ordinary reset/reseed and source/template/policy/SDK attestation with representative
CS/EN normal source/warning/real-stop fixtures. No new schema code against old demo
DB, no production/default/session lifecycle authority. Root owns final runtime
release; incomplete/uncertain operation effects retain their ordinary recovery.

#### KB impact addendum — G-PHP (2026-11-18; exact source scope closed)

This updates the obligations in [the retained assessment](kb-source-evidence/impact-assessment.md),
which remains evidence for its recorded older source range. Owner4's final
[handoff](g-php/kb-handoff.md) is bound to commit
`4db0de750500baffb16c7fbc0ac30a2aa198baa7`, tree
`63cc6814777d1435750dcf12901cef0e12aefc16`, parent
`93dcd30d0ed1b6db43ae6e04111fb8c53b544891`. Read-only inspection confirmed all11
committed blob hashes against `g-php/committed-source-hashes.json` and the route,
landmarks, removed column and threshold placement described below. The retained
formatter evidence proves token equivalence for five PHP files and byte equality
for the other six to the accepted source. This closes provisional source scope;
it does not certify canonical media/runtime or a later history successor. Owner1
owns the compact final-source section in the retained assessment and any
equivalence proof for the final published successor. Follow the canonical
`vpsfree-kb-contracts/docs/webui-change-workflow.md`; the existing source checks,
runtime receipts and images retain only their original input/coverage claims.

**Navigation and source contract.** The supported generic API exposes the VPS
sidebar **Incidents** entry at
`?page=adminvps&action=incidents&veid=ID`, with `vps.incidents.menu`, after the
OOM-report entries and before admin Report incident/Outages. It replaces the
direct Incident reports entry in that branch; the current PHP keeps the old
history link when the generic API capability is absent. Incident-report history
itself remains supported. The new page has `vps.incidents.page`, repeated
metadata headings `vps.incidents.policy`, per-policy forms
`vps.incidents.settings`, one shared `vps.incidents.permission`, and threshold
links `vps.incidents.warning`. Old `vps.oom-summary`, `vps.oom-details` and
`vps.oom-settings` disappear. None of those old or new incident IDs is currently
registered in `contract/navigation.yml`: record the old feature destinations as
superseded, without inventing an existing registry path to remove.

The smallest new KB binding is `vps.incidents.open` through
`[vps.menu, vps.incidents.menu]` for the two incident articles below. Bind the
static menu label/landmark in `webui/forms/vps.forms.php` and its route helper in
`webui/forms/incident_policy.forms.php` as related source; a helper call alone
does not couple the route text. Register settings/permission paths only for
instructions actually included in those articles. Repeated metadata headings
remain generic landmarks, not one hardcoded KB control per configured policy.
Existing `vps.menu`, `userdata.menu`, `networking.manage-host-addresses`,
`vps.create`, `vps.clone`, `vps.swap`, `vps.features` and `vps.boot-rescue` keep
their intent. The checker hashes normalized declaration contexts with
`source_context_lines: 1`, not whole files: changed PHP filenames/line numbers
alone require neither new fingerprints nor unrelated page/capture work.

**Exact page/content scope.** Retain the existing image bindings for CS
`informace:novacci`, EN `information:new_members`, and CS
`navody:vps:obnova_webu_zo_zalohy`; the English playground-list image still has
no source-page binding but remains a required language variant. The local
`owner3-runtime-policy-evidence/incidents-{cs,en}-candidate.txt` pair targets CS
`navody:vps:incidenty` and EN `manuals:vps:incidents`. These inventory-listed
articles are not new managed pages and have not been staged/published. Their
feature sections need revision: Incidents subpage/tab instead of the overview
panel; current declared limits/overrides instead of callback-based unavailable
limits; multiple saved policy memberships, create-time-only matching and shared
shutdown permission. Preserve saved history/privacy and real-stop distinctions;
reconcile email descriptions with final G-mail, including removal of claims that
mail always shows unavailable-list filler or decision-time prose. Root owns final
CS/EN writing and navigation annotations. No unrelated incident-type article
rewrite or managed-page/scenario expansion is required by this delta.

**Screenshot dependency, both CS and EN, existing 1440×1100 viewport:**

| Existing concept | Actual crop and revised obligation |
| --- | --- |
| `getting-started/vps-list` | `navigationTitleAndFirstTable` takes main navigation, first h1 and first content table; it explicitly hides `#aside`. The permanent incident column is removed, and zero aggregate threshold counts add no hostname icon. Compare the final zero-fixture table width/content; a sidebar label change does not itself enter this crop. |
| `restore-backups/playground-vps-list` | `titleAndFirstTable` takes first content h1/table. Same removal/zero-icon condition; retain the storage/base-VPS/snapshot fixture and both language variants. |
| `getting-started/vps-details` | `titleAndFirstTable` is a rectangular union of h1/table, not isolated element images. A threshold perex now lies between those elements and would enter the crop. The zero-incident fixture should emit no perex; the prior unconditional exclusion based on a panel *after* the table no longer suffices. Check the final zero-fixture geometry. |

These selectors are in `lib/capture-session.cjs:183–198`; the shared union crop
includes intervening pixels. The sidebar is outside the content crop, but final
layout still needs inspection because the legacy template declares width1150.
Root accepted owner4's actual-PHP synthetic CS/EN admin/member desktop/narrow
views for navigation, zero/threshold visibility and layout; the retained source
equivalence carries that scoped evidence to4db0de75. It does not certify canonical
capture/runtime provenance. Section/form crops below the former overview panel retain their
selectors and intent; changed absolute vertical position alone is not a new
capture concept. No incident-subpage PNG is currently bound or needed merely
to document the new navigation in text.

**Smallest follow-up and stop.** Owner4's committed source/landmark/visual handoff
is complete and leaves this affected set unchanged. A later root-assigned KB owner
uses the final published source (or owner1's proven equivalent history successor),
reconciles this bounded change set, pins that vpsAdmin revision in the existing five
pin files, adds the necessary incident path/article bindings, and runs ordinary
`nix develop -c bin/check`, interpreting actual drift rather than accepting it
blindly. Review the three concept pairs above against their final zero fixtures;
use the application's threshold cases to cover icon/perex visibility. Only
images actually changed require canonical bilingual regeneration through the
existing supported runtime/scenario and strict inventory/visual verification.
The older four-PNG requirement is therefore reassessed, not silently discharged;
pending canonical media/runtime proof stays pending. Stop this scoping task once
the final-source dependency and affected set are recorded: no pin, check, build,
capture, media, staging or publication operation is released here. No revival of
the parked capacity campaign, no new product gate, and no substitute of ordinary
demo screenshots for canonical KB media. Application ownership stays with owner4;
only a final source/landmark contradiction is routed back through root.

**Historical final-pin fixture compatibility (2026-11-18; superseded for Nov18 reusable policies).** The adapter/absent-selector instructions below describe the earlier G input only. The current owner0 KB source boundary near the top replaces them with the reusable DSL and explicit OOM selector; retain prior receipts literally. Owner0's G-KB-source preparation
found a necessary one-file compatibility change: retained KB source c4393704
injects `cluster/fixtures/incident_escalation.rb` through the existing
`screenshotApiConfig` link farm into database setup, API and supervisor only for
the `screenshots` topology; other topologies keep their existing configuration.
Its `policy do |ctx|` threshold callback is not
supported by final4db0de75 `IncidentEscalation::RuleBuilder`; keeping it with the
new backend pin would fail configuration loading. Replace only that callback
with `limits warning: 5, stop: 10`, preserving key `oomd`, adapter `node_oomd`,
labels, templates and existing Nix injection. No applicability hook is necessary:
the absent selector matches qualified source incidents, as the old unconditional
fixture did. Default suppression remains false; base enforce restricted by the
current global mode preserves the old `ctx.global_mode` result. The obsolete
`reason` field has no new equivalent or required downstream fixture consumer.
This is a format conversion, not a new scenario, provider or policy behavior.

Root allocates that file to the current KB-source owner; no architect source edit.
Shortest validation is Ruby syntax plus loading the fixture through the exact
selected backend's pure declaration file and checking its one rule/key/adapter,
5/10 limits, unchanged metadata, absent selector and false suppression. Reuse
the existing source-check package/environment; no API boot, database, Nix runtime
evaluation/build or new test framework is required for this format seam. Keep
existing pin/navigation/article checks and later final-runtime attestation
separate. This necessary source correction does not release the parked capture
or capacity work.

### Migration decision — one final migration; one final demo reset

The two files are not technically necessary for the final feature schema.
`20261030180000` adds four VPS execution/accounting columns, source/delivery
columns and indexes on incident_reports, and the per-policy settings/actions
tables. `20261115120000` adds report policy_evaluation JSON, action
contributor_snapshot JSON, notice_incident_report_id and its unique index. Its
only data-related up block reads/logs existing global overrides; it changes none.
Both current files originate in reviewed commit67cc2998b and are published on
the feature branch through4842. Retained publication proof leaves remote master
c51d8a41 unchanged; local containment finds only feature refs and no containing
tag. Prior private tests and current demo consumed both. The user now explicitly
confirms no external consumers and permits this session's dev-cluster reset.
There is no supported first-only predecessor to preserve.

Owner1 consolidates all final feature schema into20261030180000, removes
20261115120000, regenerates the core schema and updates migration tests/docs.
The forthcoming generic-policy schema belongs in that same original migration.
No second/third bridge migration, existence guards, ledger repair, dual formats
or dev-state compatibility subsystem. Keep original source/evidence refs and
historical receipts; do not rewrite their claimed results.

The current demo stays running during edits. After final source/schema/UI are
committed, quick-checked and independently reviewed, root releases ONE ordinary
supported reset/reseed for this exact registered cluster, followed by genuine
CS/EN source/warning/confirmed-stop fixtures and UI/mail verification. Do not
reset repeatedly while developing or silently point new schema code at old DB
state. Existing24 reports/MailLogs are historical evidence, not required live
rows after the authorized reset. No reset, production probe, default integration
or session lifecycle action is performed by this design assignment.

## Current dev-cluster demonstration — released execution brief (2026-11-17)

Owner0 owns normal preparation/start/configuration/fixtures/verification under
root's package `63dd8841`. This user-authorized reversible setup needs no further
per-command permission. No reset, cleanup, default merge, production mail or
private KB/SMTP runner reuse. Prior capture/capacity work stays parked.

**Target/inputs.** Stable `vpsadmin-devcluster` uses runtime `3shank2g` and provider
`gzmnal2b`. Native status is stopped; the exact session directory has no VM disks,
runner, result or applied configuration. Public `urls`/`config` inspection
unexpectedly initialized only `config.json`/`socket-dir`; preserve them. Those
commands print credentials and must not be copied unfiltered into evidence.
No other registered vpsAdmin cluster directory/runner was present in this workspace.
This is fresh creation, not preservation of an existing database.

Verified clean source heads: backend `4842e75b17df5453b0c5883dd5d54524bf69b8a2`,
site `d42ad451db702a4bf7982c3d94369c3e3d31d76a`, React `8ce6baac538061d5b51b84c09044947a22004435`,
TS SDK `3b98b045684528d0c38cc2abfef012ebf75e3e5a`, Go SDK `87745f1f54b8928620893c6b64cc1ef3a4f2b90a`,
site configuration `0be59e51d8473ca0b26b4a9cfe49ca3fe6818fcb`. React names the exact
TS development archive; retain its existing lock/integrity evidence. No session OS
worktree exists, so the ordinary provider selects local canonical `origin/staging`,
currently `42baba6117bebcde3d04555a71377381df197925`, for both OS inputs. Bind that
actual source; do not reuse private-KB OS evidence or silently move a ref. Normal
fresh DB setup applies the unchanged reviewed additive migrations
`20261030180000` and `20261115120000`.

**Start is released independently of fixture preparation.** Set only per-cluster
`dns.enable=false`, retaining React and Mailpit capture; standalone DNS guests are
unnecessary, and the services resolver remains enabled. Use the ordinary monitored
`vpsadmin-devcluster start 2026-10-30-oomd-abuse-policy --topology single --network bridge`.
Actual resources are services 8 GiB/8 CPUs plus node1 8 GiB/4 CPUs, 12 GiB services
image and writable root, one 20 GiB tank. KVM, br0 and bridge helper were present.
Observed free disk 209,334,816,768 B, available RAM 70,161,059,840 B and shm
50,613,465,088 B are not reservations. Refresh normal capacity/shared-address
ownership before launch. Proposed operating allowance: 100 GiB incremental disk
plus shared 20 GiB floor, 48 GiB available RAM, 20 GiB shm; include full tank growth
and positive construction/import overlap, with one Nix job/core and normal caches.
This is assessed headroom, not a hard peak. Unexpected local kernel compilation,
source incompatibility or material resource drift returns to root; no generic
measurement campaign. First readiness estimate: 20–60 minutes if caches work.

**Load exact mail/policy before fixture ingestion.** The installed launcher only
discovers the legacy `vpsfree-mail-templates` basename and overwrites an attempted
environment override. Avoid alias, duplicate worktree or provider changes. After
fresh boot, copy reviewed d42 `templates/` into an owned guest directory, verify
bytes and use the deployed API's existing public rake task
`vpsadmin:notification_templates:reconcile[PATH,SOURCE_ID]`; bind SOURCE_ID to the
reviewed revision/digest. Verify all five incident families' CS/EN subject/plain/
HTML. Built-in defaults preserve existing translations, and no external reconciler
is selected without that legacy worktree. No demo VPS/event exists before this step.

Copy exact `configs/vpsadmin/api/incident_escalation.rb` from site `0be59` as a
regular additional file into deployed API/supervisor/database state `config/`
directories (defaults `/var/lib/vpsadmin/{api,supervisor,database}/config`). Resolve
actual paths/user/group from units; preserve existing files and refuse an unexpected
conflict. Use restricted component-readable permissions, not a Nix-store write or
symlink: `api-app.nix:121–133` rebuilds symlinks but preserves regular extra files.
Tasks/scheduler use API config. After template reconciliation and file installation,
restart normal API/supervisor/scheduler services, await health and verify site-file
digest/loading under each relevant deployed package/config. Supervisor-generated
fixture evaluations must carry that same digest. The site rule supplies base5/10
and inherits global mode. This is explicit local demo configuration, not a claim
that the provider declaratively loaded the production configuration tree.

**Fixtures (only after source/policy/capture checks).** Use two dedicated seeded
test owners, CS and EN, and one clearly named synthetic VPS each, created through
normal API chains with modest defaults (1 CPU/1 GiB RAM/4 GiB disk). Wait for real
running VPSes. Confirm mailer transport targets only Mailpit and synthetic addresses;
then enable global enforce only in this fresh isolated demo and retain base5/10.
Reuse `tests/suite/alerts/incident-escalation.nix`'s node-scoped `vps_events`
producer (`oomd`, `restart`) through the existing supervisor protocol. These are
explicitly simulated memory-pressure source events, not a real daemon diagnosis.
Save VPS IDs and unique nonfuture whole-second timestamps before publishing; reuse
that tuple on recovery so the normal source key deduplicates it. Send first event
and verify ordinary mail; reach five and wait for warning mail before reaching ten.
Require a successful real Stop chain/node stopped status/action completion before
claiming stopped notice/mail. Never fabricate action completion. Expected total:
20 ordinary source reports, two warning notices, two confirmed-stop notices with
corresponding captured mail; verify actual preferences/delivery. No SMTP outage,
transfer/cooldown test, automatic restart or extra event campaign.

**Semantics/acceptance.** New eligible ingestion inserts under lock, evaluates once
including that event, saves the result/action and processes it; stop wins if both
thresholds qualify. The periodic task reconciles queued effects/retries/pending
reports, not old-event callback replay. Repeat stop requires a new event at least
24 hours after confirmed stop; warnings have a seven-day cooldown. Queue existence
is not delivery. Verify MailLog/mail transaction and Mailpit separately from stop.
Record built/applied system paths, loaded backend/policy/template/React identities,
migration versions and fixture IDs. Open PHP/React VPS counts, incident history,
ordinary detail and notice/trigger navigation as admin and owner. Site Ruby's current
dynamic limits/status may correctly be unavailable; do not invent live thresholds.
Inspect CS/EN plain/HTML and access/privacy without broad new CI.

After readiness, user links are `https://webui.aitherdev.int.vpsfree.cz/`,
`https://newadmin.aitherdev.int.vpsfree.cz/`, and
`https://mailpit.aitherdev.int.vpsfree.cz/`. Retrieve seeded login/password and
Mailpit basic auth through existing portal account fields/approved secret channel,
never raw values in notes. Use normal provider CA trust. First useful milestone is
reachable UI/Mailpit with source/template proof, then first ordinary mail; allow
roughly 5–15 minutes for fixtures after healthy services/template availability.
On failure retain disks/config/roots and all old private evidence; inspect exact
provider/chain effects before resuming, with no reset/replay/cleanup or old binary
against uncertain schema. Failed starts can retain live guests and capacity use.

## Bounded copy and writing-rule follow-up (2026-11-17)

The user's follow-up supersedes the visible evaluation-time and no-action prose
requirements below. Ordinary mail shows saved counts/limits and the possible-stop
sentence only when saved `stop_enforced` is true; omit all other mode explanations
and `Stav k` / `As of`. Keep source-event times and the payload unchanged. Czech
period labels use `1 den`, `2–4 dny`, otherwise `dní`. Stopped-mail restart and
conditional repeat-stop sentences form one plain-text line / HTML paragraph in
site CS/EN and generic EN variants.

Owner0 implements this bounded correction under the direct lead brief e044b17d;
root applies final wording before commit. Repository AGENTS.md gains concise
rules for useful member consequences, short natural language, plural forms and
rendered whitespace checks, using the existing dataset/card examples. README
remains unchanged. Existing renderer/tests cover both conditional values, missing
policy, no-action modes, Czech plural boundaries and language/format parity.
All previous data, escaping, ownership, history, compatibility and rollout
invariants remain. No new API, migration, helper framework or capacity operation.

## Mail presentation revision — implementation boundary (2026-11-17)

**Current package:** owner0 owns backend/template implementation and focused
checks; root owns the final CS/EN wording pass before commit and release decisions.
Node-capacity work is parked: final node roots remain unmeasured; its source-only
checkpoint distinguishes OS `makeInitrd` closure-copy staging from services
`makeInitrdNG`, and streamed node squashfs. No node preparation is released here.

**Settled interface.** Remove `IncidentEscalation.explain!` and its ingestion call.
New ordinary `IncidentReport.text` remains exactly the source message; keep the
existing locked evaluation and saved `policy_evaluation` unchanged. Ordinary
`TransactionChains::IncidentReport::Send` passes one optional `incident_policy`
Hash through the existing mail variables, projected only from that saved result.
Return nil for absent/non-recorded/incomplete evaluation (manual, legacy,
audit-only or error); do not invent limits or expose internal diagnostics.
For a complete recorded evaluation use symbol keys:

```text
evaluated_at: Time from saved evaluated_at
count_7d, count_30d: saved context counts, including this incident
warning_limit, stop_limit, mode, stop_exempt, suppress_actions: saved effective values
warning_period_days: 7; stop_period_days: 30; repeat_stop_hours: 24
stop_enforced: saved mode == enforce && !stop_exempt && !suppress_actions
```

No current settings lookup or Ruby callback on render/retry; no raw context/user
dump, new API field, schema migration or policy-format marker. Templates own the
wording and optional simple remaining-count arithmetic. Show snapshot counts and
limits from the first qualifying report, with one concise time label. Explain
threshold/window consequences only as allowed by the saved mode/exemption/
suppression. Enforce permits a possible future stop, not a guaranteed action,
minimum warning interval or automatic stop when cooldown expires. Notify,
observe and exempt/suppressed cases must not threaten an escalation stop. Source
actions such as an oomd stop remain distinct factual actions in the source text.

**Mail/history and compatibility.** Keep existing report bytes and rendered
`MailLog` subject/plain/HTML bodies unchanged. Delivery retries use the existing
MailLog; a new rendering uses the same saved policy facts and the normal selected
template language/time zone. No heuristic stripping or historical backfill.
The earlier appended-prose iteration was feature-development-only, not a released
production format; do not add a migration/dual mode to replay its unsent rows.
Retain that evidence and use fresh fixtures for this change. Supported old/manual
production rows have no evaluation and render source facts only.

New ordinary templates guard missing/nil `@incident_policy`, so old producers
continue rendering. Reconcile the updated site templates **before** running the
new producer; new producer + old ordinary override renders but loses the policy
explanation and is not a complete supported rollout. Built-in `install_defaults!`
does not update existing DB translations: existing unmanaged installations must
explicitly update/reconcile the affected definitions through the existing template
workflow before switching producers. Fresh installs receive the updated built-ins.
Keep updated sender code/templates available for pending source-only reports;
an older sender cannot reconstruct the new payload. No deployment is authorized.

**Templates and copy.** Site: CS/EN plain plus HTML for the five existing IDs
`vps_incident_report`, `vps_incident_warning`, `vps_incident_stopped`,
`vps_memory_pressure_warning`, `vps_memory_pressure_stopped`. Built-ins: matching
EN plain plus HTML, retaining normal English fallback; no new translation system.
Dataset-expanded/shrunk supply the concise plain-text/data-row precedent (they
have no HTML). Reuse `ip_release_requested`'s escaped 640px presentation-card
structure for HTML. Escape every dynamic text/attribute/URL explicitly: the actual
ERB builder does not autoescape. Preserve source line breaks in escaped text;
plain and HTML carry the same facts, links and standard automated-mail footer.

Apply the user's exact CS changes, with equivalent concise EN: `bylo vypnuto`,
`narušuje provoz`, `Nutno řešit`, `Prosíme o řešení.` Remove the autostart-disabled
sentence, unavailable-incident/list/link filler, `k okamžiku rozhodnutí` and
repeated `rozhodnutí`. Under existing aggregate `stop_enforced`, say only that a
repeat incident may stop the VPS (again for a confirmed-stop mail); omit that
claim otherwise. Retain existing
aggregate payload meanings: action-time counts/contributors, and current
deterministically restricted limits/stop permission at rendering. Do not label
current limits as historical or reevaluate policy to simplify wording.

Contributor templates display only available authorized selected entries (at most
five), with safe subject/time/detail links; derive displayed/total from the visible
subset and saved total, not the old selected-slot count. Omit empty sections and
missing URLs. For legacy snapshots, show the known authorized trigger only if
available; no replacement query or unavailable filler. A history link remains a
current history link. Preserve frozen selection, original-owner checks and single
sender semantics. Remove the feature-only section from the template README;
retain/update the actual variable/compatibility contract in vpsAdmin docs.

**Files/checks.** Backend: `api/models/incident_escalation.rb`, ordinary Send,
`api/lib/vpsadmin/api/incident_reports.rb`, mail-variable registration, the five
`api/notification_templates/templates/*` families, relevant existing specs and
`docs/incident-escalation.md`; remove only unused policy-explanation locale keys.
Site: the same five `templates/*` families and the README addition. No enforcement,
client/UI or general renderer change. Quick validation uses existing ingestion
and actual mail-render specs with `VPSADMIN_SPEC_MAIL_TEMPLATES` pointing at the
site tree: unchanged source text; saved-snapshot rendering after config changes;
nil/manual/error cases; CS/EN and built-in fallback; escaped hostile text/URLs;
mode branches; contributor omission/counts/transfer privacy; retry MailLog byte
stability. Render representative plain/HTML previews for root's copy pass, then
run touched lint and existing template checker/hooks. Follow the repository's
final-source schema/no-client-change evidence requirement without expanding SDKs.
Commit complete source/copy and pass quick checks before mandatory final review;
long verification remains separately selected by root. No migration, deployment
or default-branch integration is part of this boundary.

## D public-start prospective capacity assessment (2026-11-16)

**Decision: the unchanged public `start` can use a prospective phase-peak
assessment; numeric sufficiency is not yet accepted.** Scope is KB `c4393704`
(`r42` immutable source), backend `024ab881`, OS `6bdf458f`, configuration
`c9d1f3a0`, and the accepted generic stage receipt `ff27025e`. Owner3 retains
source/measurement preparation; root owns construction and runtime admission.
There is no new prepare API, private helper, placeholder guest or postbuild pause.

Source proof: `cluster/lib/kb_runtime.rb:79–116` generates fixed-algorithm
Ed25519/RSA-2048 credentials with the fixed configured SAN list, then prepares,
builds and launches. `kb_source.rb:74–96,129–163` binds UUID/identity/configuration
content to that build. `cluster/nix/test.nix:63–75,1318–1327,2013–2082` takes
resource sizes from configuration and embeds identity/key content. Random values
change paths/hashes, not topology or workload selection. Budget affected generated
outputs as new; do not assume cache reuse by similar names. Runtime contract
`480–497` permits assessed headroom with explicitly unknown scratch and a final
fixed-image fit gate inside start. It does not guarantee advance exact drv names
or an opportunity to reconsider admission after building.

For the shared state/store/builder filesystem, use this conservative accounting
shape (split terms by actual filesystem where different):

```text
D_start = C + max(12 GiB + B, 24 GiB + G + H)
fresh free >= 20 GiB + S_other + G_old + D_start
RAM_start >= max(R_build, 14 GiB + O_live)
```

`C` is newly retained non-image closure/output allocation, including generated
configuration/squashfs/boot outputs. `B` is peak additional construction space:
download/unpack/import overlap, payload staging, extra temporary image copies,
builder scratch and metadata, excluding the one retained 12 GiB image already
counted. The live phase retains that image plus its independent 12 GiB writable
root; `G` covers assessed three-tank boot/provisioning/background growth and `H`
host runtime logs/metadata/other overhead. Count existing allocated bytes once,
through fresh free space. Three 320 GiB sparse tanks are 960 GiB logical extent,
not the value of `G`. `G_old=0` only while the accepted old instance stays
untouched/unrestarted. `S_other` remains unknown until separately assessed or
explicitly addressed by root; the floor does not make it zero.

All four guests can coexist: services 4 GiB/4 CPUs, node1 4/4, node2 4/4,
backuper1 2/4, totaling **14 GiB/16 vCPUs**. The **4 GiB image-builder VM**
precedes runtime, so use a phase maximum, with positive evaluator/builder/QEMU
and host overhead in `R_build`/`O_live`, not merely max(4,14). Assess shared memory
and inode demand separately. Bind effective ordinary Nix job/core concurrency
(intended one job/one core) and any offload/fallback costs before admission.
The reduced network example's 8 GiB images, 24 GiB total, 16 GiB base reserve
and ip-inventory fixture are **not** this profile's resource values.

Finite remaining evidence, without another inventory campaign:

- **Owner3:** final-source missing immutable closure/payload allocation and inode
  assessment, cache/kernel prerequisites and affected generated-output allowances
  (`C`); source-only PHP probe establishes only its prerequisite. Supply assessed
  construction overlap/scratch (`B`), actual builder filesystem and concurrency.
  Generic stage's 3 GiB allowance and 73,728-byte outputs do not cover these costs.
- **Owner3:** positive boot/background/host-growth and RAM/shm allowances
  (`G`,`H`,`R_build`,`O_live`), including continuing guests while an unsuccessful
  start is assessed. Use source recipes and relevant existing measurements;
  label assessments as such, not measured peaks or hard quotas.
- **Root:** accept those allowances, fresh capacity and treatment of `S_other`
  while preserving the shared 20 GiB floor and old-instance condition. Scratch
  may remain explicitly unknown with justified headroom and live reserve
  monitoring under the existing contract; require neither fictitious exact bytes
  nor an automatic zero. If a defensible allowance is unavailable, hold start.

Launch includes service seeding, pool initialization and background services,
but not the later selected capture fixtures. After ready/identity attestation,
separately admit the incremental primary VPS/template import+unpack, mounted
1 GiB-refquota data child, public key and real snapshot, and the two concepts
`getting-started/vps-list` and `restore-backups/playground-vps-list` in CS/EN.
Assess actual template/snapshot/background/browser/output costs; root quota
122880 MiB and empty NAS quota 256000 MiB are not write estimates. Refresh
service/ZFS free bytes/inodes and positive overhead without counting live guest
RAM or already allocated disks twice. Boot success alone does not admit capture.

On build/readiness/capacity failure, stop advancing and retain the exact evidence;
no automatic replay, resize, alternative input or private recovery. Public-start
timeout is not a guest-stop guarantee, and 900 seconds is not a disk-write ceiling.
Reserve assessment must cover retained live effects, not expire with the caller.
Any separately authorized stop uses the ordinary exact-owner public path and
complete exit rules; this design grants no stop/cleanup/release authority.
Generated receipts later verify conformity; they cannot replace advance admission.

### Selected next measurement: services payload envelope (2026-11-17)

**Proposal for root release; owner3 prepares and executes one metadata-only
pass.** Use final `c439/024/6bdf/5df` and unchanged private configuration
`c9d1f3a0`. The public `runtimePlan.machines.services.toplevel` represents the
complete selected services system, unlike the accepted 13-component cohort.
OS `tests/make-test.nix:253–288` passes that same toplevel to the image recipe;
`copyChannel=false`, default empty `additionalPaths`/`contents`, and
`make-disk-image.nix:418–424` establish the payload root. Explicit kernel/initrd
contexts cover boot outputs even if a particular reference is outside that root.

Select through the existing public output, not an imported private constructor:

```sh
nix eval --offline --no-write-lock-file --impure --json \
  --option allow-import-from-derivation true \
  --option pre-build-hook "$DENY_HOOK" --option max-jobs 0 \
  --option builders '' --option substitute false \
  path:/nix/store/r42v6x3iay0ygcd4yilsbb883cglidb3-source#runtimePlan \
  --apply 'p: let s = p.machines.services; in {
    drv = s.toplevel.drvPath; out = s.toplevel.outPath;
    inherit (s) kernel initrd memory cpus;
    bootContext = builtins.getContext (s.kernel + s.initrd);
  }'
```

Owner3 binds the retained deny hook and the normal cleared-prefix environment:
session slug, `topology=screenshots`, `network=bridge`, exact `c9d1` config file,
ordinary bridge helper, Telegram disabled and no source overrides. Use the
immutable source's existing certificate/key planning defaults and empty guest
identity **only for metadata**. Never construct their guest/config/image outputs.
Their bounded difference from start-generated inputs needs an explicit positive
generated-content allowance; these paths are not eventual identity proof. Allow
IFD solely to read the already realized/rooted ordinary PHP source. Missing IFD,
input fetch or attempted realization stops this pass without an alternate graph.

Then use `nix derivation show --recursive` on the returned toplevel/boot drv roots
and ordinary local `nix-store --query --requisites` / `nix path-info --json`
accounting. Form one conservative dependency cut: stop at each valid output and
include its runtime closure; for an absent output include its declared selected
inputs and retain an allowance for that output itself. Deduplicate store paths;
reuse accepted component/source measurements only on exact path identity. This
includes base packages and generated system/unit/boot recipes omitted previously.
No image derivation realization, cache downloads, output imports or repeat cohort.
Keep environment-bearing derivation JSON in private local evidence; publish only
the required path identities, size/count totals and limitations in the brief.

Report numeric logical bytes, allocated bytes, NAR bytes where available, and
namespace entries for the locally valid cut, plus the complete residual output
set with assessed bytes/entries. For staged-copy sizing, count each file occurrence
without assuming store hard-link sharing survives copying; include filesystem
rounding/metadata and temporary install DB/profile/etc costs in the allowance.
Existing store allocation is already in free space, but its staging copy consumes
`P` within `B`. A complete conservative `P` is the measured cut plus justified
missing-own-output/generated/install allowances; it is not the runtime closure's
exact size. Do not auto-size arbitrary recipes from their names or output hashes.

This is one necessary coverage/size pass, expected 2–5 minutes (the historical
public projection took 97 seconds), capped at five minutes. Proposed incremental
metadata headroom is 1 GiB disk / 50,000 metadata entries and 8 GiB evaluator RAM,
subject to root's fresh admission and the existing shared floor/other obligations;
these are assessments, not measured peaks. Stop on the cap, denied realization,
input/shape drift, or an unassessable residual; retain the result and name that
specific residual without another evaluation cycle. Success is a complete
conservative payload estimate with bytes/entries and declared allowances, not
merely a successful projection.

Exact preconstruction `P` is not exposed: `closure-info.nix` obtains runtime
references/NAR sizes through build-time `exportReferencesGraph`, after missing
outputs exist, and supplies no inode total. If the residual cannot be assessed,
root must choose between accepting a justified conservative allowance or separately
authorizing ordinary construction of the necessary immutable package outputs to
measure them. Neither option permits a placeholder guest build or private prepare;
there is no metadata-only flag that fills absent output sizes. Owner3 records the
result in [the existing capacity brief](owner3-postreview-capacity-brief.md);
whole-start numerical admission and later fixture/capture remain separate.

## Quota CI discriminator — bounded diagnostic brief (2026-11-16)

**Design only; root releases implementation/review and separately admitted
execution.** Implementer0 owns source after the independent SMTP correction.
Reuse [owner0's offline diagnosis](nov16-ci43765668910-attempt1/quota-offline-diagnosis.md)
for A `1ada4b`, run `43765668910` attempt 1/job `132970076360`.
The synthetic writes succeeded, but actual enforcer inputs were not captured;
supervisor overwrite is a candidate, not an established cause.

Use one isolated diagnostic commit/ref touching only
`api/lib/vpsadmin/api/tasks/dataset_expansion.rb`,
`tests/suite/tasks/dataset-expansion-enforce-and-resolve.nix` and the necessary
opt-in helper arguments in `tests/suite/tasks/common.nix`. This is temporary
instrumentation, not a quota fix or supported product subsystem. Retain its
commit/result as evidence and remove the task instrumentation after the single
discriminator, before final feature publication/integration. No schema, API,
workflow, supervisor, threshold or timeout changes. Owner0 verified standard
Rake `--rakelib` can install test hooks after loading classes; it is unnecessary
here because multiple getter prepends add complexity to direct guarded observation.

Scope observation to the exact fixture expansion ID, passed only to the existing
fresh enforcer rake process. Keep the original query, predicate/getter order,
short-circuiting and updates verbatim. Record whether its real relation yielded
that ID; at entry retain task `now`, effective constants, `exp_cnt`, IDs and
pre-update expansion attributes (state/stop flag/original quota, last stop,
over-quota check/duration/maximum). Add small branch markers for strict suspension,
ordinary-gate rejection, stop submission/return and `ResourceLocked`/raised error.
An `ensure` around the existing iteration records outcomes even across `next`;
buffer evidence and emit bounded JSON to the existing task log on method exit.
Do not move a stop or suppress, retry or replace any original exception.

Read diagnostic values only from already-loaded association targets: the
first matching `referenced` property in the generated Dataset getter's collection,
its ID/dataset/pool/value/`updated_at`, and loaded VPS/current-status
state, running, uptime, row ID, `updated_at` and `update_count`. Include related
loaded refquota metadata separately from the consumed `original_refquota`.
Do not call a getter again, reload, preload, lock or issue diagnostic SQL at the
decision boundary. Mark an unloaded cache unavailable and distinguish a loaded
missing status; evaluation attribution is clarified below. If the target never
yielded, report `not_selected`,
without inventing which query filter rejected it. Diagnostic failures must not
mask the original exception; mark their evidence incomplete. Capture fixture
write row counts/IDs/values/timestamps from the objects just updated in the
existing helper processes, with opt-in JSON fields, not another intervening
process/readback. Property `updated_at` can be node-report time with second
precision; it does not authenticate the writer or establish precise commit order.

Capture clarification: copy scalar cache metadata immediately before an existing
stop/suspension effect call, since that call may reload associations; iteration
`ensure` fills the snapshot only if none was captured. Keep later outcomes/errors
separate and never replace the pre-effect snapshot with mutable model references
or post-effect values. Label these fields **loaded-cache metadata at the recorded
stage**, not a per-getter trace. A cached uptime value may exist even when running
status short-circuited its getter. Distinguish cache availability from evaluation:
use `not_evaluated` only for an established unvisited path, otherwise `unknown`.
Reaching stop submission establishes that the original conjunction passed; it
does not establish consumption of every cached field. No getter wrappers or
predicate rewriting are required to strengthen that limited observation.

Preserve the current fixture/order, `MAX_EXPANSIONS=-1`, `OVERQUOTA_MB=1`,
`COOLDOWN=0`, strict defaults, 600-second rake timeout, 900-second chain wait,
stop/shrink assertions and ordinary cleanup. Do not rewrite the fixture again,
pause reporting, combine seeding with enforcement or introduce real disk filling.
The later execution is exactly the existing
`./test-runner.sh test tasks/dataset-expansion-enforce-and-resolve`, once, under
the repository's normal runner and root-owned admission/monitoring. Expected
warm duration is about 20–25 minutes (retained script 1209.16 seconds/example
1023.48 seconds), excluding separately assessed builds; this is not a new timeout.

Execution-input correction: use the pinned OS `8e44` runner's supported
`TEST_RUNNER_REPO_ROOT` pointing to the **rooted immutable exact Git source**
identified as `2lrz` in owner3's retained receipt, while keeping the ordinary
command above. The default `RepositorySource` helper's `getFlake(abs checkout)`
captured ignored directories and produced a different source. Clean HEAD alone
therefore cannot establish reusable graph identity. This explicit supported root
preserves the scenario contract; it does not change fixture logic or select a
different test. Owner3 owns canonical source retention and guarded proof that the
actual helper, selected test and dependency graph use that root and pinned inputs.
Before construction, the receipt must bind the full source path and immutable
identity to the reviewed diagnostic revision, the effective root/runner/input
identities, exact selected test, and exact derivation/output paths and dependency
closure of the proposed stage. A source or derivation mismatch stops admission.

The evaluated plan supersedes provisional 10 GiB/6-vCPU estimates: services uses
**8 GiB/8 vCPUs**, node **8 GiB/4 vCPUs**, totaling **16 GiB/12 vCPUs**;
the image builder separately requests **8192 MiB**. These are configured demands,
not measured host peaks. AUTO image size remains unknown until realized
closure-info and payload allocation/inode evidence permit sizing. The proposed
first stage is services closure-info and its toplevel dependencies only; prove
its exact graph excludes disk-image/VM construction before root considers it.
Stage boundaries change preparation order, not the scenario or its image-sizing
algorithm. After separately admitted realization, use actual payload evidence
for the next image/construction budget. Root retains every construction/runtime
admission; no output realization or test is released by this clarification, and
routine evidence/planning adds no independent review gate.

Before that run, owner0 performs applicable syntax/hooks and focused controls
showing disabled diagnostics preserve behavior; observed rejection/submission
paths retain getter order/count, short-circuiting, original errors and writes;
unloaded associations are not forced; and output is fixture-only/parseable.
Use existing focused spec/helper facilities, not a new harness. Confirm the exact
test remains selectable through the existing runner/CI rules; no new workflow or
full six-hour rerun is required to acquire this discriminator. Root then obtains
independent affected-lane review of the committed diagnostic and releases one run.

Accept evidence only with fixture and real-task identity, yielded/not-selected
marker, observed branch/consumed values, original assertion outcome and terminal
effects receipt. Changed property values can establish loss of eligibility in
this attempt, not supervisor authorship or the historical failure's cause.
Submission followed by a missing/failed chain points to the downstream boundary;
`fire` returning is not proof of physical stop. A pass is a non-reproduction;
missing observations or an unselected row leave the corresponding reason unknown.
Stop after this one result and report the finite finding—no automatic retry,
timeout increase or speculative product fix. Previous capacity/effects assessments
remain accepted and independent.

## Runtime policy implementation plan — final recommendation (2026-11-15)

**Implementation is now authorized by the user. Package A is active under
implementer0's exclusive vpsAdmin ownership; other package allocation remains
with the lead. Architect0 owns design clarification only.**
This supersedes the static catalog and unfrozen runtime proposals below. The
lead's [plan and A–F package table](plan.md) own status, allocation and release.
There is no unresolved product blocker under these recommendations; migration
provenance remains an implementation prerequisite, not an assumed deployed state.

### Site DSL and evaluation contract

Use `vpsfree-cz-configuration/configs/vpsadmin/api/incident_escalation.rb`,
distributed by existing `configDirectory` and loaded once per process through
`VpsAdmin::API.load_configurable('incident_escalation')`, after DSL classes exist
and before registry/SysConfig initialization. No duplicate Nix rule catalog.
The new DSL interface is illustrated by this behavior-preserving initial rule:

```ruby
IncidentEscalation.configure do
  rule :oomd, adapter: :node_oomd do
    labels en: 'VPS memory-pressure incidents', cs: 'Incidenty přetížení paměti VPS'
    templates warning: :vps_memory_pressure_warning,
              stopped: :vps_memory_pressure_stopped

    policy do |ctx|
      {
        warning_limit: 5, stop_limit: 10, mode: ctx.global_mode,
        suppress_actions: false, reason: 'standard_memory_pressure'
      }
    end
  end
end
```

`ctx.global_mode` preserves existing configured notify/enforce behavior; the
new-install global mode remains observe. A policy may conditionally change base
limits, request a less permissive mode or suppress actions based on context.
Those dynamic choices are supported; the initial sample intentionally adds none.
Site Ruby is trusted operator code, not sandboxed. Require short, side-effect-free
callbacks using supplied values, not live queries, commands or service calls;
this is a policy callback, not a workflow engine.

Evaluate at accepted ingestion of each new eligible, trusted source incident
under existing serialization, after ownership reconciliation and insertion so
counts include it correctly. Duplicate delivery uses the stored evaluation;
late/future/prior-epoch audit-only events do not acquire new actions. The context
is a read-only value snapshot: one UTC `now`; event identity/type/action/detected
time/source node; current VPS ID/node/state and owner ID/role/state; ownership
epoch; fixed 7/30-day counts; last queued warning and confirmed stop; global mode,
global/per-VPS limit overrides and stop exemption. No model objects or full
user/VPS dumps. Keep existing 7/30-day windows and 24-hour stop cooldown.

The callback returns only the serializable fields shown above: positive integer
base limits, supported mode, boolean suppression and a bounded reason string.
Normalize symbols/keys, apply overrides/caps, validate effective stop>=warning,
then let the engine derive `none`, `warning` or `stop` using existing eligibility,
threshold, recurrence, cooldown and outstanding-action rules. No arbitrary
force-stop branch bypasses the describable policy. Persist the rule/config-file
digest, evaluation time, base/effective result, derived decision and necessary
context facts with the source report's audit; actions retain their existing
trigger/count/link identities. No separate decision-log subsystem is needed.
Render the immutable first-event explanation from that effective snapshot;
distinguish requested decision from dispatch and confirmed outcome. Future
context can change policy, so no guaranteed remaining credits or notice period.

### Authority, failures and later execution

Precedence is **Ruby base limits → non-null global overrides → explicit per-VPS
overrides**. Reuse global `warning_limit`/`stop_limit` settings as nullable audited
overrides, with null meaning inherit; do not introduce a parallel settings store.
New installations seed null overrides. Preserve every existing non-null value
as a legacy override when intent is unknown, including values equal to old
defaults. Give the operator one transition summary identifying which overrides
mask Ruby edits; clearing them is an explicit audited choice, never a guessed
reset. Update the existing settings validation/help/reset behavior accordingly.
Global mode is always a hard ceiling on the requested mode, and VPS exemption
always prevents escalation stops. Ruby cannot activate enforcement above that
ceiling. Observe/notify/exempt explanations must reflect the actual result.

A malformed present DSL file, unknown adapter or invalid declaration fails
startup/readiness with a diagnostic, rather than silently using another policy.
An absent file retains the equivalent built-in legacy rule, with a distinguishable
identity; it does not disable existing behavior or reset settings. A runtime
callback exception/invalid result preserves the source incident and records a
safe evaluation-error diagnostic, but creates no new automatic action and uses
no permissive fallback. Existing unrelated actions retain ordinary reconciliation.
Policy updates require restarting all relevant API/supervisor/task processes;
there is no hot reload. Verify consistent config identity before activation.

Do not rerun callbacks for mail retries or queued-action reconciliation. Before
a new warning/stop submission, compare the stored policy digest with the loaded
one and check current ownership, mode, exemption, applicable counts/limits,
cooldown and expiry against the saved decision. Current deterministic checks
may suppress it; they cannot promote it, substitute another action or loosen
its saved eligibility. A digest mismatch suppresses an old **undispatched**
warning/stop decision; even a comment-only file change conservatively changes
that identity. A new eligible event evaluates the new policy. Preserve the old
snapshot/reason and record suppression separately in existing action state.

Already queued or uncertain physical/mail effects cannot be recalled by editing
the DSL or restarting a worker: reconcile their existing identities, without
automatic duplicate submission. Confirmed-stop notices and their factual mail
recovery remain possible under current owner/privacy checks and the saved
outcome; they never request another stop. Keep stable mail identity and distinguish
queued, successful SMTP, failed, uncertain and suppressed states. No claim of
inbox delivery, revocation API or retroactive policy rewrite is introduced.

### Current summaries versus historical policy evaluation

**Accepted Package A clarification; SDK/PHP/React contract.** Summary/list/filter
reads never execute the Ruby callback or write an evaluation. Keep current
qualified 7/30-day counts, ownership epoch, warning/stop times, cooldown and
outstanding-action facts. For any site Ruby policy, even the constant initial
sample, `incident_warning_limit`, `incident_stop_limit` and `incident_status`
are nullable **unknown current policy values**. Neither a previous evaluation,
matching digest/settings nor guessed defaults supplies a current event-context
result. The built-in missing-file legacy rule retains its known static values.

Retain `incident_mode` as the current configured rule-global mode ceiling and
`incident_stop_enforced` as the current global-enforce-plus-VPS-permission boolean,
matching their existing calculations. Update descriptions/UI labels to identify
administrator permission: neither field is the callback's chosen mode or a promise
that a stop will occur. No duplicate ceiling field or new mode/bool nullability.

Add only these read-only history references to the VPS summary:

- `incident_policy_evaluation_report_id`: nullable integer source-report ID.
- `incident_policy_evaluated_at`: nullable datetime, evaluation time.
- `incident_policy_evaluation_state`: `none`, `recorded` or `error`.

They describe the latest evaluation attempt for the selected rule and current
owner/epoch, loaded in a batch from the existing report audit. `recorded` always
means historical, never fresh/current; a later policy/settings/context change
does not rewrite it. With no evaluation, return null references/time and `none`;
an errored attempt has its reference/time and `error`. The authorized source-report
history supplies the saved explanation; expose no raw audit or second projection.
PHP/React show current counts and permission separately from policy unavailability
and the dated history link, not a fabricated clear state or zero threshold.

Preserve current-status filter meaning: add input choice `unknown` matching NULL
status; existing `clear`/`near_limit`/`warning`/`stop_threshold` exclude unknowns.
Use the same SQL status expression before pagination for filter, totals and output.
Checks cover no callback/write on reads, never-evaluated/error/history cases,
policy/settings/time/count changes, owner transfer, static fallback, null rendering
and filter/count/page parity. Owner0 confirmed the existing evaluation/notice
storage seams fit; no new projection table, scheduler or action endpoint.

This changes three fields from non-null to nullable; it is not unconditionally
backward-compatible. Export/synchronize SDKs, update PHP/React capability/null
handling and assess relevant old clients, CLI and Terraform decoding/behavior.
Compatible readers must precede activation of **any Ruby file**, even in observe
mode with constant limits; keeping the legacy fallback during transition avoids
introducing these unknown payloads before readers are ready. Do not declare old
consumers supported without the relevant evidence. Lead controls C/E release.

**Accepted Go compatibility boundary:** retain this API contract and normal scoped
generation. [Package C preparation](nov15-clients/preparation.md) records that
Go client `a2ab4ead` decodes null current limits/status as `0`/`0`/empty string.
Owner1 confirmed the retained generator ignores scalar output nullability, so
schema-only regeneration does not fix that loss. Both retained and newly
regenerated Go typed outputs are unsupported for interpreting dynamic current
incident limits/status; these values are not zero thresholds or a clear state.
Preserve the actual decoding evidence and document the boundary in Package C;
no generated-file patch, generator redesign or provider expansion is authorized.
Any required Go reader consuming these fields remains an explicit Ruby-policy
activation dependency until it uses a representation that preserves unknown or
ceases that interpretation. This does not block unrelated resource operations
or source publication. The inspected Terraform pin ignores incident fields;
that source assessment does not certify arbitrary or installed consumers.

### Contributing incident links in escalation emails

**Scope within A (evidence/audit payload) and D (generic/specific EN/CS templates);
execution status follows the lead's package table.** At the original action
decision, select at most **five** source
reports from its actual qualifying rule/VPS/original-owner epoch snapshot:
the warning's 7-day window or the stop's 30-day window. Include the triggering
report only if it belongs to that set; fill remaining slots from the other
contributors ordered by `detected_at DESC, id DESC`, without duplicates, and
display the selected set in that same order. Aggregate notices never qualify.

Preserve selected IDs, original event times and brief safe subject snapshots
(plain text, bounded to 160 characters), total qualifying count, decision time
and window in the existing action audit. Each email shows those entries with
authenticated incident-detail links, shown/total and omitted count, and the
window/decision time. Build links from the existing configured WebUI base and
canonical incident route/helper, verified by the owner during implementation;
do not invent a URL path or add an endpoint. Add the existing general history
link, clearly describing current history rather than an immutable decision set.

Retries and confirmed-stop mail reuse the original selection, including when
new reports arrive while stopping; no mail-time reselection. Current ownership,
authorization and suppression checks still apply, so a transferred owner never
receives predecessor evidence. Deleted/inaccessible entries are marked unavailable
without replacement; omit unauthorized descriptions/links. Preserve recipient
language/fallback, escape text/URLs for their rendering context and exclude full
report bodies, attachments and credential-bearing links. Listed evidence says
nothing about mail delivery status.

Legacy actions without a contributor snapshot remain renderable: show only the
known trigger (labeled as such, not asserted to be a reconstructed contributing
set) when authorized, and general history, with an explicit snapshot-unavailable
limitation. Do not fabricate historical membership or shown/total claims.
Focused checks cover limit/omissions, exact eligibility/trigger inclusion,
deterministic ties/retries, delayed stopped mail, deletion/legacy fallback,
transfer privacy and safe EN/CS links/text. No new knob, observability subsystem
or change to the existing UI-history plan is introduced.

**Accepted action-recovery clarification:** at decision creation, also retain
the immutable normalized policy digest/time/base/effective result/reason/decision
and two count facts inside the existing action `contributor_snapshot` JSON.
This preserves the original decision for recovery when its source report is
deleted, without a new column/public field or callback reevaluation. Pending
missing-source decisions stay suppressed; queued/uncertain effects reconcile by
their existing identities, and confirmed-stop factual mail uses saved evidence
with current ownership/privacy checks. Legacy actions lacking that evidence keep
the snapshot-unavailable limitation above; never invent historical base limits
or introduce a separate fallback subsystem. Generated notices retain their
approved factual text and trigger metadata, without the ordinary source-only
“when this report was received” policy explanation. First-event explanations
remain on ordinary source reports.

### Implementation boundaries and verification

The existing A–F table remains the single status inventory:

- **A, implementer0:** DSL loader/context/normalizer and ingestion/preflight in
  the existing API escalation/configuration paths; nullable global-override
  contract; minimal persisted evaluation and separate trigger/notice linkage;
  report metadata/permissions, PHP history and focused specs. Retain warning
  notices, confirmed-stop-only notices, no recursive qualification/ordinary-mail
  duplication, historical text and owner-transfer privacy from the accepted plan.
- **B, implementer3:** the Ruby site file above and existing
  `configs/vpsadmin/api/README.md` in the separate configuration worktree, using
  the frozen DSL contract while A finishes. No A edits; API-loading validation
  waits for the lead's final stable committed A head. Same source for
  API/supervisor/tasks, no duplicate deploymentConfig catalog, implicit pin update
  or activation. D remains parked on its final A/KB dependency.
- **C, implementer1:** exact final API export and Go/Rust/TypeScript generation or
  revision-specific no-change proof; preserve handwritten consumers. SDK publication
  required by a dependent React merge remains separately controlled.
- **D, implementer3:** existing EN/CS templates and KB contracts; preserve unique
  template README interface/retry/compatibility content in
  `vpsadmin/docs/incident-escalation.md` and leave a concise link. A owns that doc
  first, then D gets the exclusive edit window; lead owns final member-facing prose.
- **E, implementer2 after A/C:** existing React incident history/detail and VPS
  navigation, nullable notice metadata/mail state and old-API capability handling;
  no dashboard, second sender or action-control endpoint.
- **F, reviewer0 later:** independent complete-change/history/migration review
  after committed changes and focused quick checks, then affected integration,
  browser and KB verification. No review or check is launched by this plan.

Focused acceptance covers legacy equivalence; null/global/per-VPS precedence;
dynamic selection with truthful first-event text; mode/exemption ceilings;
duplicate/concurrent ingestion; callback errors retaining the incident; notice
idempotency/no recursion/no duplicate sender; transfer privacy; unchanged snapshots
and no callback rerun on retry; digest suppression before submission versus
queued/uncertain reconciliation and factual stopped-mail recovery. Reuse existing
API/model/resource tests, Ruby/PHP checks, template renders/checker, SDK checks,
React checks and scoped configuration checks. Final exports follow completed API
source/docs. Longer affected full/core API and integration/browser/KB checks
follow review; previous CI limitations and recovery evidence remain separate.

### Initial transition and rollback

Before changing migration `20261030180000_add_incident_escalation.rb`, establish
its exact predecessor/lineage and any merge, release, deployment or external
consumption from authoritative retained/schema receipts. Publication status
does not establish schema use. Prefer an additive successor when uncertain or
consumed; consolidate only proven unconsumed migrations against their exact
predecessor, resetting disposable databases without existence guards.

Keep existing overrides initially; deploy additive schema and compatible readers,
permissions, exclusions and nullable-setting support to all API/supervisor/task
processes before clearing globals or activating the new producer. Do not invent
evaluations for old reports/actions: reconcile queued/uncertain legacy effects;
suppress undispatched legacy decisions lacking the required saved policy identity.
Distribute the equivalent Ruby rule and templates, verify effective settings and
consistent identity only after the compatible summary readers described above
are ready, then deliberately enable the desired mode only under a
later rollout authorization. No node protocol change or coordinated node update.

Rollback preserves audit/schema and reconciles dispatched effects after disabling
new decisions. It requires a version that understands null overrides and generated
notice privacy/exclusions; an arbitrary older binary is not a safe rollback.
Restoring an older static configuration requires an explicit compatible settings
transition, not silent materialization/reset of dynamic values. Completed stops
are not undone. Integration, deployment, publication and KB writes retain their
separate approvals; implementation allocation follows the lead's package table.

## Runtime Ruby policy — superseding discussion (2026-11-15)

**Historical discussion, superseded by the finalized runtime plan above.**

**Discussion only; dynamic Ruby policy is preferred for the newly clarified
goal of on-demand decisions. Context, return values and override authority are
not frozen.** The earlier Nix recommendation optimized for static declarations;
the static-only/no-policy-callback recommendation is superseded for this goal.
The accepted static plan below remains a baseline to revise before implementation,
not a release to change code or live mode.

Use trusted operator-owned Ruby policy, evaluated per new qualifying incident
against a defined current-context value snapshot: trusted source/event, counts,
current owner/VPS facts and settings. Conditions may select effective policy and
request record/warning/stop, returning normalized values plus a reason. Application
code still owns source qualification, locking, deduplication, ownership/privacy,
cooldown and durable action/mail/stop execution. Site policy requests a decision;
it does not perform side effects. This is neither a Ruby sandbox nor a general
workflow engine, and does not imply new windows or grace periods.

Retain the evaluated context, policy identity, effective values and result for
first-event explanations and durable history. Later action preflight checks
current ownership/permissions/settings separately from that historical snapshot.
Any policy reevaluation must have an explicit contract, retain the same action
identity and not replay events, duplicate effects or rewrite the original reason.

**Precedence to settle:** a useful starting proposal treats DB global thresholds
as policy input defaults, applies explicit per-VPS limit overrides to the result,
and retains current DB mode and VPS exemption as hard execution ceilings. Ruby
can then choose policy within those bounds. Making globals merely advisory, or
letting Ruby override those ceilings, is a different intentional authority choice.
Neither that proposal nor the exact context/decision API is yet selected; the
earlier static precedence assumption cannot settle runtime-policy authority alone.

## Implementation plan — pending, not released (2026-11-15)

**Historical static baseline, superseded by the finalized runtime plan above.**

**The user requested an implementation plan only. All packages A–F are pending.**
The lead's [plan and single package/status table](plan.md) own allocation and
release. This section settles the implementation boundary using the accepted
[discussion](#incident-notices-and-first-event-explanations--discussion-only-2026-11-15)
and [configuration proposal](#site-policy-configuration-and-warning-visibility--pending-plan-2026-11-15).
No implementation, checks, review, integration or deployment starts from this plan.

**Configuration syntax alternative — discussed, unselected:** a small Ruby DSL
in site `configs/vpsadmin/api/incident_escalation.rb` would fit the existing
`incident_reports.rb` convention. API `load_configurable(name)` already requires
`config/<name>.rb`; `api-app.nix` links the configured directory. It would need a
new, thin `IncidentEscalation.configure`/`rule` builder loaded before catalog use
in every relevant process, producing the same validated adapter/labels/templates/
defaults object below. This is trusted operator-owned configuration, not a new
trust boundary; keep named adapters rather than qualification callbacks. The
specific template IDs remain `vps_memory_pressure_warning` and
`vps_memory_pressure_stopped`. Recommend the planned Nix declaration for the
current single flat rule, using the existing DeploymentConfig JSON loader.
Ruby becomes more useful with repeated declarations or a preference for the
existing Ruby style; its cost is builder/loading/validation coverage, not a rule
engine. No syntax preference is settled. Either choice preserves SysConfig and
per-VPS authority, fixed 7/30-day windows and the existing 24-hour stop cooldown;
do not introduce two simultaneous declaration authorities or custom policy timing.

### Interfaces and invariants

- **Site declarations:** use the existing
  `vpsadmin.deploymentConfig.incident_escalation.rules` object, keyed by stable
  rule ID. Each entry supplies `adapter`, `labels` (English fallback),
  `templates = { warning, stopped }` and
  `defaults = { mode, warning_limit, stop_limit }`. Initial `oomd` uses named
  adapter `node_oomd`, current template pair and defaults `observe`/5/10;
  category remains derived as `incident_policy_oomd`. Application code owns
  adapter qualification/provenance, deduplication, windows and action mechanics.
  No Ruby/SQL evaluation or automatic enrollment from a freeform codename.
  Validate the complete declaration: known adapters, stable unambiguous keys,
  supported template references, mode and positive limits with stop>=warning.
  Absent section retains legacy registration; malformed explicit data cannot
  silently activate a fallback policy. Preserve ordinary incident audit.
- **Precedence assumption:** site values bootstrap missing SysConfig rows;
  existing audited global values remain authoritative, with nullable per-VPS
  limit overrides above them and the existing VPS enforcement exemption.
  Changing site defaults does **not** reset effective mode/limits. Making site
  configuration authoritative for existing global values is a different product
  choice requiring an explicit writer/migration change; it is outside this plan's
  assumed implementation. Keep `oomd` selection compatible; do not rename,
  remove or rebind persisted rules, or replay incidents on configuration changes.
- **History and delivery:** retain `VpsIncidentAction.incident_report_id` as
  trigger; add a nullable, uniquely linked `notice_incident_report_id` for one
  generated notice per action. Create warning notices with the decision and
  stop notices only after confirmed successful stop, atomically with their link
  under existing serialization. Use internal `source_kind=incident_policy_notice`,
  distinguish warning/stop-completed, and retain rule codename for history filters.
  Do not copy node provenance/source key; notices have no executable VPS/CPU
  action and never enter qualification, counts, decisions or ordinary mail queues.
  Preserve the action's original owner/VPS/epoch and apply equivalent history
  authorization to trigger and notice, including transfer away and back.
  `IncidentEscalationMail` remains the sole aggregate sender and retry identity;
  ordinary source-event mail remains distinct. No backfill or new dashboard.
- **Read interface:** add only nullable read-only `notice_kind`
  (`warning`/`stop_completed`), `trigger_incident_report_id` and `notice_mail_state`
  to IncidentReport Index/Show. Ordinary reports return null. Derive mail state
  from the linked action's existing states; do not expose private errors,
  recipients or admin MailLog content. Existing history views show recorded
  decision/outcome separately from queued/sent/failed/uncertain/suppressed mail.
  Queue time is not send time; successful SMTP is not proof of inbox delivery.
- **First-event explanation:** within locked ingestion, reconcile ownership,
  insert/deduplicate the source incident, then capture counts as of that same
  decision time and effective limits/mode/exemption/cooldown before commit and
  dispatch. Include the event once only when eligible in the rolling windows.
  Persist localized subject/body as the historical snapshot; no extra snapshot
  service or recalculation of old text. Explain 7/30-day counts and applicable
  consequences from the first event using effective values, not hardcoded5/10.
  Observe/notify/exempt modes must not threaten escalation stops; expired/future
  audit-only events must not claim to trigger them. Explain new-event/cooldown
  conditions, not a timer or guaranteed remaining credits/prior-warning period.
  Execution still checks current settings. Preserve the existing mail contract
  of decision counts plus render/retry-time consequences, explicitly separating
  those from the immutable notice snapshot when settings change; MailLog retains
  the actual prepared message. Invalid policy data must not lose the source fact.

### Package boundaries and order

The labels below refer to the lead's table; proposed owners are not assignments.

- **A — implementer0, backend and PHP:** `incident_escalation.rb`,
  `vps_incident_action.rb`, `incident_report.rb`, the DeploymentConfig/SysConfig
  seams, incident resource/ingestion/task/mail paths, required migration/schema,
  API locales/specs, and existing PHP incident list/detail/policy navigation.
  Implement the interfaces above and preserve current action recovery. Update
  `vpsadmin/docs/incident-escalation.md`. Deliver exact schema/output names and
  template variables for C/D/E, including old-API null/capability behavior.
- **B — implementer0, after A's reader contract:** site declaration in
  `vpsfree-cz-configuration/cluster/cz.vpsfree/vpsadmin/common/api.nix`, with
  reference in `configs/vpsadmin/api/README.md`. Verify identical effective input
  for API, supervisor and tasks. Serialize with A under the same owner; no pin
  change, activation or deployment is implicit.
- **C — implementer1, after final API source/docs:** export exact committed API
  schema/provenance using the existing exporter; update Go/Rust/TypeScript owned
  generated outputs or retain revision-specific no-change evidence. Preserve
  handwritten client/CLI/Terraform behavior; additive reads need no new commands.
  Supply the TypeScript candidate to E; its required registry release remains
  a separate prerequisite before merging an SDK-dependent React change.
- **D — implementer3, after A's message variables settle:** existing generic and
  specific notification templates, EN/CS variants, `vpsfree-notification-templates`
  README and existing affected KB contracts/pages. Move the README specialist
  section (retained lines82–108) into `vpsadmin/docs/incident-escalation.md`,
  preserving unique interface, retry, compatibility and recovery facts; leave a
  concise link and keep `docs/README.md` discoverability. A first owns that API
  document, then hands D one exclusive edit window; A confirms technical facts.
  No new documentation catalog or rule rewrite. Lead owns final member-facing
  wording; KB staging/publication remains separately controlled.
- **E — implementer2, after A/C's interface:** React existing
  `src/pages/app/incidents/` history/detail and VPS incident-card navigation.
  Render notice kind, trigger link and mail state with old-server capability
  handling; reuse member/admin user/VPS filters. No action endpoint/dashboard.
- **F — reviewer0 later, lead coordinated:** after all intended changes are
  committed and quick checks pass, independent final review of the complete
  cross-repository diff and migration lineage, then longer verification.
  Review is not launched for this plan. Lead schedules shared Git/index windows;
  disjoint template/React work may proceed after interfaces settle, without
  concurrent edits to A's API locales/docs or C's generated output.

### Acceptance, compatibility and recovery

Before editing migration `20261030180000_add_incident_escalation.rb`, A must
record its exact predecessor/current revisions and whether any version was
merged, released, deployed or externally consumed, using retained lineage and
authoritative schema/version receipts for supported databases. Schema consumption
and deployment must be established before choosing consolidation versus an additive
migration; neither is inferred from feature publication status. Default to an
additive successor if provenance is uncertain
or an existing version must remain supported. Consolidate only positively proven
unmerged/unreleased/undeployed migrations against their exact predecessor schema;
reset disposable stale databases, without existence guards hiding mismatches.

Focused quick checks must prove: legacy/default/override equivalence and invalid
catalog refusal; concurrent/deduplicated ingestion with correct inclusive counts;
one notice and one aggregate send across retries; notice exclusion from every
ordinary/qualification path; member/admin/transfer privacy; mode, custom-limit,
window, cooldown and simultaneous-threshold wording; immutable snapshots after
language/settings changes; no completed-stop notice on failed/uncertain stops;
and truthful queue/send/failure states. Use existing focused API/model/resource
specs and Ruby/PHP checks, template checker/rendered EN/CS cases, client generation
checks, React type/tests/build and scoped configuration evaluation. D compares
documentation's factual content and links so the README move loses no contract.
No checks are run now.

After review, run affected full/core API topics and the existing relevant
integration/browser/KB scenarios against the completed contract, including mixed
old/new API-client behavior and failure/retry paths. Record exact inputs/results;
prior CI failures, later nonreproductions and old monitoring receipts remain
separate evidence and are neither rerun nor waived by this plan.

For a later authorized rollout, apply compatible additive schema first, then
reader/permission/exclusion support and templates across all API/supervisor/task
processes before enabling new notice production; deploy clients/UI with capability
gates. New site bootstrap defaults do not change existing effective settings:
inspect them and deliberately select observe for rollout if needed, rather than
claiming a reset. Only later explicit activation selects notify/enforce, waiting
for new eligible events. No node protocol or coordinated node update is needed.
Retain reports/actions/schema on rollback, disable new decisions and reconcile
already dispatched effects. Revert only to a version/configuration that can
safely read and exclude generated notices and preserve their owner/epoch privacy;
an older binary is not automatically a safe rollback after notices exist.
Completed stops are not undone. Integration, publication, deployment and KB writes
retain their separate approvals. Documentation lives with the owning components;
temporary rollout/check evidence stays in session records.

## Incident notices and first-event explanations — discussion only (2026-11-15)

**Proposed, not implemented. The user explicitly requested discussion/design
only.** This extends the [pending configuration plan](#site-policy-configuration-and-warning-visibility--pending-plan-2026-11-15);
it does not replace the implemented contract below or release changes/checks.

The dataset precedent supports explaining consequences early: site template
`vpsfree-mail-templates/templates/vps_dataset_expanded/email/{en,cs}.text.erb`
(canonical retained HEAD `9e1ddbd973703cf48a43f0e5afc2bfb392a8b676`, lines10–22)
shows the expansion count and explains stopping only when the expansion is active
and `stop_vps` applies. API `operations/dataset_expansion/process_event.rb:71–79`
records history before `tasks/dataset_expansion.rb:26–43` sends through
`Mail::VpsDatasetExpanded`. Reuse this factual, conditional explanation pattern;
its literal three-expansion/30-day wording is not incident policy. Current
`IncidentReports.oomd_event_message:3–23` records only the intervention fact;
aggregate warnings currently have action/mail records, not their own reports.

**Recommended history:** create one warning notice in existing `IncidentReport`
history for each durable warning decision, with a separate notice link from
`VpsIncidentAction`; preserve its existing `incident_report` link as the original
trigger. Also recommend one stop-outcome notice after the existing successful
chain/physical-stop confirmation, never a “stopped” report for a pending, failed
or uncertain stop. Creation/reconciliation retries must reuse the same notice.
Keep action counts, original user/VPS/ownership epoch, mail identity and stop
lifecycle authoritative. A recorded warning decision does not mean email sent.

Give notices an explicit internal classification, retain the selected rule for
history filtering, and exclude them from every qualification/count/decision and
ordinary report-processing path. Do not copy trusted node source identity onto a
notice or make it another stop request (`vps_action` remains `none`, no CPU action).
The existing ordinary queues and `IncidentReport::New/Process/Send` must not send
it again. `IncidentEscalationMail` remains the sole aggregate-mail authority with
its existing retry identity; ordinary source-event mail remains a distinct event
notification. This avoids a duplicate aggregate email without introducing mail
coalescing. Preserve original trigger provenance and extend its owner/epoch
privacy protection to notices, including transfer-away-and-back cases.

Reuse the existing incident list/detail and user/VPS filters rather than add a
dashboard: `resources/incident_report.rb:34–125` already scopes member history;
React `IncidentsPage.tsx:136–137,235–246` selects the member or admin-filtered user.
Notice text identifies the decision/outcome; a small associated action-status
display can distinguish pending/queued/sent/failed/uncertain/suppressed without
exposing admin mail logs. Report existence and `last_warning_at` are not delivery
proof; current `last_warning_at` advances on queue, and sent means successful
SMTP transaction, not inbox receipt. No new user-wide aggregate counting is implied.

**Recommended ordinary report text, from the first qualifying event:** snapshot
the effective rule, 7/30-day counts, warning/stop limits (defaults5/10, including
overrides), mode/exemption and relevant cooldown as of ingestion. Compute after
ownership reconciliation and insertion within the existing locked transaction,
before commit/dispatch, so an eligible in-window event is counted exactly once.
Retain detected time separately; delayed/future or prior-epoch audit-only events
must not claim to initiate an action. Render for the captured owner's language
with existing fallback, and preserve that text through deduplication/retries.

Explain the applicable next consequence and distance to its rolling threshold,
not guaranteed remaining credits. Observe records only; notify warns without
automatic stops; exemption prevents escalation stops while warnings can remain.
Enforcement needs a new eligible event, respects the confirmed-stop cooldown,
and never schedules a stop merely when time expires. Warning and stop thresholds
can be reached together, so do not promise an earlier threshold email or grace
period. Distinguish this escalation policy from the node's immediate intervention.

Historical report text remains an immutable, dated policy/count snapshot.
Execution eligibility still uses current settings. Current threshold mail uses
decision counts but render/retry-time consequences (`incident_escalation.rb:321–331`);
retain that distinction explicitly if settings change, without rewriting the
stored notice. MailLog retains the actual prepared message; a report is not a
receipt for that message. The pending site-config authority decision determines
where effective rules come from; templates must not hardcode their own limits.

All implementation remains pending: minimal additive notice linkage/classification
and scoped status exposure in the API, localized report/mail text, then existing
history UI linkage. Preserve old reports/actions; no backfill/replay or node
protocol change. Any later implementation must cover idempotency/no recursion,
single aggregate send, transfer privacy, mode/threshold/window boundaries,
snapshot/retry behavior and confirmed-stop-only notices; additive API/client
compatibility and rollback retaining audit data belong to that future package.
No further product choice is needed to discuss this recommendation; no source,
template, configuration, test, review or deployment work is authorized here.

## Site policy configuration and warning visibility — pending plan (2026-11-15)

**User requested PLAN ONLY. No product/configuration implementation, tests,
integration or deployment is released.** Findings below inspect owned vpsAdmin
`7919441ccb8e9587ad0afc84674b074ca9c5a880`, React WebUI
`bbd820a65536564756484f6dd037f10224901b35` and canonical configuration HEAD
`86e19685313270d88e4db30038c056ce4b807abd` (read-only reference, not a fresh remote
or deployed-state claim). Root owns plan/state and the user-facing response.

### Pending configuration change

Feasible through existing infrastructure: configuration repository
`cluster/cz.vpsfree/vpsadmin/common/api.nix:32–37` already sets
`vpsadmin.deploymentConfig`; `configs/vpsadmin/api/` supplies the common API and
supervisor configuration directory. vpsAdmin `nixos/modules/vpsadmin/main.nix:50`
declares the JSON option; `api-app.nix:22–24,127–133` renders/copies
`config/deployment.json` for API-based services. Existing
`api/lib/vpsadmin/api/deployment_config.rb` loads/caches that object. No new
configuration transport, Ruby hook evaluation or separate deployment service is
needed. Proposed site key: `vpsadmin.deploymentConfig.incident_escalation.rules`.

Move the **rule declarations/selection**, not only thresholds: stable key `oomd`,
localized labels, a named trusted qualification adapter (proposed `node_oomd`),
warning/stopped template names, and default mode/limits into that site object.
The initial declaration preserves current5/10, `observe`, and the memory-pressure
template pair. Derive/preserve category `incident_policy_oomd`. Application code
retains the named adapter implementation, trusted node provenance/identity checks,
deduplication, ownership/locking,7/30-day windows, cooldown and physical-stop/mail
mechanics. Existing `IncidentEscalation::RULES:42–52` becomes a validated catalog
resolved from data; it never evaluates supplied Ruby, SQL or a freeform codename.
Adding another supported source still requires a reviewed application adapter;
merely adding a codename must not enroll admin/manual/abuse-mail reports in stops.
The site's existing `configs/vpsadmin/api/incident_reports.rb` remains its ordinary
abuse-mail parser, not an automatic qualification source.

Validate the complete catalog once before API/schema/scheduler use: recognized
adapter names, stable unique keys/categories, English label fallback, bounded
strings, supported registered templates, exact mode and positive integer limits
with stop>=warning, and no ambiguous duplicate adapter binding. Invalid explicit
configuration refuses activation/actions with a diagnostic; it must not silently
fall back to an enforcing rule. Preserve existing unknown-selector API errors,
generic-template fallback only when the specific definition is absent, recipient
suppression, language fallback and ordinary incident collection/mail opt-outs.
Keep `oomd` as the default selector in this first move. Do not remove/rename/rebind
keys with persisted policies/actions, or replay old reports on configuration
change; rule retirement needs an explicit recovery design. `observe` disables
new automatic decisions while reconciliation retains already dispatched effects.

**Precedence decision pending:** recommend site-owned declarations and bootstrap
defaults with existing audited `SysConfig` global overrides and nullable per-VPS
overrides preserved. Actual `SysConfig.register:118–150` seeds missing rows but
does not replace existing values, so changing Nix defaults alone will not change
existing global mode/limits. If the user wants configuration to be authoritative
for those globals too, explicitly change that authority instead of leaving two
competing writers or overwriting the database silently. Absent new section should
retain legacy registration during rollout; malformed present data must refuse.
Deploy compatible reader support before site declarations, distribute identical
data to API/supervisor/task processes, and explicitly verify effective `observe`
before later intentional activation. Old binaries ignore the new section: rolling
back requires restoring matching old declarations/effective settings, not merely
removing JSON. Preserve additive schema, actions, timestamps and unresolved chains;
no migration/table rewrite or node protocol change is needed for the basic move.

Pending implementation/check packages (not released): (1) API owner: small catalog
loader around `DeploymentConfig`, `incident_escalation.rb`, `sys_config.rb`,
`vps_incident_policy.rb`, selector/summary/task and trusted supervisor adapter
seams; update `docs/incident-escalation.md`. Prove legacy equivalence, malformed/
unknown refusal, trusted qualification, existing overrides and no action on reload
with focused registry/escalation/resource specs. (2) Configuration owner, after
the interface/precedence choice: declaration in existing `common/api.nix` and
`configs/vpsadmin/api/README.md`; check resulting API/supervisor JSON and scoped
configuration evaluation before any separate deployment request. (3) Verify
old/new and rollback behavior plus API schema/generated Go/Rust/TypeScript
freshness under `docs/api-schema-export.md`; selector choices are schema metadata
even if no endpoint/field changes. UI/history additions are a separate possible
follow-up, not part of this externalization plan.

### Current warning audit and UI facts

Warnings aggregate incidents **per VPS, selected rule and current ownership epoch**,
not across all VPSes of a user. `incident_escalation.rb:186–207` creates a durable
`VpsIncidentAction` with VPS/user/trigger report/type/epoch, warning-or-stop kind and
7/30-day count snapshots. Migration `20261030180000:31–50` also stores action/mail
states, chain/mail-log links, retry/error, created/updated timestamps and stop
completion time. These are mutable action rows, not a complete transition-event
log. `completed_at` is populated for confirmed stops, not a warning delivery
timestamp. Original user attribution/audit survives ownership transfer; current
counts and `last_warning_at` reset at the new epoch (`incident_escalation.rb:212–224`).

`IncidentEscalationMail:6–28` renders the recipient-language message, creates a
MailLog/chain and records queued/suppressed. `incident_escalation.rb:297–299`
advances `last_warning_at` only on the first actual queue; this can remain set
when later mail fails. Reconciliation at229–249 reads the **mail transaction**
result to mark sent/failed/uncertain; retry/expiry/ownership checks at271–318 retain
the same action/message identity. MailLog stores actual rendered text/recipients
before sending (`mail_template.rb:101–132`, `transaction_chain.rb:404–410`).
`libnodectld/.../commands/mail/send.rb:47–72` uses SMTP; a successful send is not
proof of inbox delivery/read, and timeout retries can duplicate mail. A failed or
uncertain result is not delivery. No new warning decision is created in default observe
mode; count status `warning` merely means a threshold was reached.

| Surface | What current source exposes |
| --- | --- |
| VPS API Index/Show | Owner-scoped summaries: counts/limits/mode/status, last warning **queued**, last confirmed stop and outstanding **stop** state/chain. Raw limits/admin writes are restricted. No `VpsIncidentAction` history endpoint, warning mail state, mail-log ID or sent timestamp (`resources/vps.rb:59–78,160–178,472–500`; `vps_incident_summary.rb:74–102`). |
| Legacy PHP VPS list/detail | List counts/status/exemption (`forms/vps.forms.php:873–875`); detail Incident escalation section with counts/mode, “Last warning queued”, stop state/transaction link and underlying incident-report link (`forms/incident_policy.forms.php:105–150`, `pages/page_adminvps.php:1281`). No aggregate-warning action timeline or delivery status. |
| React VPS list/Overview | Desktop/mobile count/status badge; Overview `VpsIncidentCard` shows “Last threshold warning queued”, counts/limits/mode/exemption and stop-state alert. Its “Incident history” link opens ordinary reports filtered by VPS/codename, not warning actions (`VpsIncidentCard.tsx:17–59`, `VpsIncidentIndicator.tsx:7–21`, `VpsOverviewPage.tsx:62`). |
| Generic admin mail log | API `MailLog` Index/Show is admin-only and exposes user/template/recipients/subject/body/message ID/created time, not send state (`resources/mail_log.rb:6–39,54–63`). React `/admin/mailer/log` and detail render these, including a user link and body (`MailLogDetailPage.tsx:160–198,279–315`). No warning-card/history cross-link; only pagination and direct log-ID lookup, not user/template filtering. No legacy PHP MailLog screen/reference found in the inspected source. MailLog existence alone means prepared, not delivered. |
| User/account UI | No aggregate-warning history/banner or cross-VPS warning rollup in inspected user API/PHP/React source. Admin generic mail detail links to its user, but that does not create a user warning history. |

Both feature summaries are capability-gated for old APIs. These are source-level
facts about the owned feature, not proof any running site has this UI deployed.
If a direct “this user/VPS was warned, with queue/send/failure history” screen is
wanted, the durable action data is a starting point, but scoped API exposure,
permissions and UI linkage remain unimplemented future work. No new UI or audit
endpoint is authorized by this inquiry.

## Complete original-topic diagnostic — current design (2026-11-14)

**Completed: one faithful full-topic nonreproduction; stop after this pair.**
Lead verified [the captured result](nov14-original-topics-result.json) for run
`43555466662`/attempt 1/job `132327212562`, diagnostic head
`f6d690eddc48c6cff7ed3172c24b3f467a403df4`, testing exact application source
`7919441ccb8e9587ad0afc84674b074ca9c5a880` and frozen lock
`7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`.
Run, job and all 15 steps succeeded. Operations passed 243/243 and plugins
337/337, with pending/outside-example errors 0 and both native exits 0.
Complete original manifests, executed ID order and seeds 42376/55119 matched;
both original failing targets passed. Captured software and image versions
matched; original full kernel/library identity remains unproved.

Actual job time was **43m45s**. The 30-file, 64,794-byte ZIP has verified SHA256
`0b32f24815a1237e693f9586097d84e029e70f90d4910b0acecc02eb32ca0fae` and matches
its extracted files. Owner0 accounted for all new cells/commands: utility
`85220` and 12/12 command items exited 0, parent `73620` and all 120 joined GETs
exited 0, and log/ZIP/metadata collection joined. No new unknown-effects fence
remains. Both old scopes, `43528601963/99295` and `43551864218/3b57fd25`, remain
held and excluded; this result supplies no authority to inspect or resolve them.

The [failure diagnosis](nov14-api-failure-diagnosis.md) retains the unresolved
causal question. This result establishes neither contamination nor a
feature/baseline cause and does not waive the original CI failures. No automatic
round, speculative fix or repetition follows. Any next execution needs a new
concrete discriminator/input and a separately released scope. Published source,
consumers and dependency inputs remain unchanged.

### Original execution plan — historical

The accepted plan below, including its input, observation and recovery limits,
is retained for provenance; it grants no standing execution authorization.
Run one
controlled pair with the complete original sorted manifests and seeds. This
supersedes the prefix-selection proposal below. Prefixes retain 221/243 (91%)
and 288/337 (85%) examples; their roughly ten-minute saving does not justify
509 description alternatives, selection data and dry-run ordering gates. Native
full-topic execution preserves original loading, fixture hooks and predecessors
with less implementation and review surface.

Owner0's [offline acceptance](nov14-diagnostic-offline-result.json) confirms run
`43551864218`/attempt 1/job `132315936018`: both isolated IDs passed, with native
exits 0 and all strict software gates satisfied. Original and diagnostic observed
OS/image/provisioner/runner versions match (Ubuntu 26.04.1, `20261111.196.1`,
`20261103.629`, `2.338.2`). Original kernel/full library inventory is absent;
bit-identical machines are not established. Original full-topic failures remain
unresolved. This control tests original loaded-file and preceding-execution
context; contamination or another cause has not been established.

**Fixed selection and inputs.** Use the retained originals under
`nov13-final-ci-artifacts/api-run-43528601962/`: each topic's
`rspec-files-full-<topic>/rspec-files-full-<topic>.txt` and canonical native JSON
under `rspec-results-full-<topic>/`. Keep every path and its sorted order.

| Execution order / topic | Files | Seed | Original examples / target position | Original duration |
| --- | --- | --- | --- | --- |
| 1 / platform-operations | 8 | 42376 | 243 / 221 | 1349.263 s |
| 2 / plugins | 17 | 55119 | 337 / 288 | 1029.887 s |

Retain tested source `7919441ccb8e9587ad0afc84674b074ca9c5a880`, frozen lock
`7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`, Ruby
3.4.12, Bundler 2.6.9, RSpec 3.13.7, the full 122-gem-version graph,
`VPSADMIN_PLUGINS=all`, `BUNDLE_WITHOUT=development`, `RACK_ENV=test` and frozen
Bundler setup. Keep MariaDB server/client 11.8.6 and exact Ubuntu packages
`1:11.8.6-5ubuntu0.1`, actual test DB REPEATABLE-READ/snapshot 0. Reuse the
completed diagnostic's gates, source/lock preservation and environment receipts.
Record actual future image/kernel/package identities; no silent software-gate
relaxation, dependency resolution or floating failed-job rerun. An unavailable
required input stops before examples.

**Minimal owner0 package.** Modify only
`.github/workflows/api-advisory-diagnostic.yml` and add the small fixed data file
`.github/diagnostics/api-advisory-topics.json` with two records containing topic,
seed and complete manifest. No example descriptions or runtime ordered-ID dataset.
Keep the frozen lock unchanged. Copy the fixed data beside that lock into
`$RUNNER_TEMP` before checkout of exact tested source. Preserve diagnostic head
`dbe74d30dd9b880691762494abc1158169d58ac0` and its receipts; use the existing
dedicated diagnostic branch/event boundary, without changing ordinary workflows,
published application source, generated clients or KB pins.

From `api/`, read each fixed manifest into the ordinary Bash `files` array:

```sh
bundle exec rspec "${files[@]}" --seed "$seed" --fail-fast \
  --format documentation --format json --out "$result"
```

Use separate processes and ordinary temporary DBs. Run operations first; run
plugins only after its successful native exit. Stop at the first gate/example
failure or timeout; no `continue-on-error`, dry-run, selector, bisect or automatic
round. Preserve native exits through any output capture. Missing second output
after first failure means not run. If both pass, stop after this one pair.

**Evidence and acceptance.** Upload source/workflow/run/attempt, manifests,
lock/software/DB gates, native JSON, logs, exits and step outcomes using the
existing seven-day artifact scheme and a distinct output directory. Offline,
compare the actual seed and complete executed scoped-ID sequence with the
original canonical JSON (normalize only leading `./`). A fail-fast result must
match the original leading sequence through its failure; a pass requires all
243/337 IDs in original order, zero failures/pending/outside-example errors and
native exit 0. Classify target reproduction, an earlier/different failure, order
mismatch or one full-topic nonreproduction; none alone waives the original CI.
For compact comparison, SHA256 of original normalized IDs, one per LF-terminated
line, is `616d61d4a07187778f3613eadafacceaa0035ebcf5a7ba59000e84fd4c370f03`
(operations) and `9cd2cdb5460d4b0ad733df9c5f14b227f02d2023a5f6e3d9beb29807873a5e9f`
(plugins). Keep original JSON for failure-prefix comparison; no new runtime gate.

Owner0 checks fixed manifests/seeds against retained originals, checkout/lock
preservation, actual push-trigger fanout, declared hooks and workflow/shell lint;
verify official action refs under the existing procedure. Committed independent
review precedes the executing push. This is a disposable diagnostic-only change:
no API/schema/migration/deployment or runtime/helper instrumentation. Ordinary
temporary DB/hosted runner disposal applies; retain refs, evidence and session.
Original topic durations total 39.7 minutes; allow setup and potentially longer
successful target loops, approximately 45–55 minutes with a **60-minute job
ceiling**. Timeout is incomplete evidence, not a diagnosed failure or rerun trigger.
Next result is one captured controlled full-topic outcome for lead assessment.

**Observation decision for this distinct future run.** The installed
[monitor skill](/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz/skills/dev-session-monitor/SKILL.md)
states: "Use this path for member-owned checks or when runtime registration is
unavailable." Owner0 owns this verification package as a **member-owned check**,
so native delegation is supported directly without declaring managed registration
unavailable. Owner0 prepares the supported native-utility plan in the review
packet; launch waits for review and lead execution release. The lead coordinates
and accepts results, with no parallel provider polling. The owner0 parent keeps
its turn active during native delegation. The new run has its own exact
run/attempt/revision/output directory. Do not repair either old operation by
replacing it.
The two old fixed scopes remain held: `99295` belongs to primary `43528601963`;
`3b57fd25` belongs to isolated diagnostic `43551864218`. No watcher or parent in
the new package may observe, reuse, clear or resolve those scopes. Their unknown
effects are not certified by the new run or its independently captured results.

At the future handoff, resolve the installed validated catalog's
`utilities.verification_watcher` and matching native configuration from the same
digest, retaining package/config identities. Require exact **Luna/low/full_access**
and explicit `--sandbox danger-full-access --ask-for-approval never` for a
standalone CLI utility, with fresh context and one-operation lifetime. Verify
actual launch policy, identity and acknowledged exact-source ownership before
relying on delegation. Keep the parent turn active; the watcher is sole observer
and must account for every native cell/tool session in its terminal report.
Tool availability alone is not handoff proof. An uncertain new launch remains
fenced; do not add a duplicate watcher or parent observer for that new scope.

If supported native delegation cannot be established **before any uncertain new
launch**, owner0 discloses that once and uses the skill's active-parent fallback
solely for the new run, with interruptible blocking waits and bounded output. This
requires no old-quiescence assertion or settings change. A confirmed independent
new observation boundary and lead release are execution dependencies; this design
launches nothing. Do not bypass a refusal covering the new scope. If such a
refusal/uncertain launch occurs, report its exact receipt and unresolved authority
rather than resume old reconciliation or invent command completion.

## Original-order prefix diagnostic — superseded analysis (2026-11-14)

Historical proposal only, superseded in full by the complete-topic brief above.
The preserved selection reasoning and timings are evidence, not implementation
instructions; regex data, dry-runs and runtime order gates are not in scope.

**Offline design only; no next execution released.** Strict hosted software is
available: run `43551864218`/attempt 1/job `132315936018`, workflow head
`dbe74d30dd9b880691762494abc1158169d58ac0`, ran the two isolated original examples
successfully on source `7919441` and lock `7e2f9b…`, with the required software/DB
settings. This establishes isolated nonreproduction, not failure resolution.
Owner0 separately owns fidelity reconciliation of those retained native receipts.
The original `99295` fence and watcher `3b57fd25` unknown command effects remain
held; native turn termination does not settle them. Lead must establish the next
execution/observation boundary separately before any executing push. This design
neither starts a replacement observer nor resolves either fence.

**Select the original prefix through each target, once.** Derive from canonical
`nov13-final-ci-artifacts/api-run-43528601962/rspec-results-full-<topic>/` JSON and
the matching `rspec-files-full-<topic>` manifest, retaining their digests:

| Topic | Original seed | Target position / total | Prefix example time | Original topic duration |
| --- | --- | --- | --- | --- |
| platform-operations | 42376 | 221 / 243 | 935.7 s | 1349.3 s |
| plugins | 55119 | 288 / 337 | 855.4 s | 1029.9 s |

Targets remain `spec/api/resources/security_advisory_spec.rb[1:3:1]` and
`spec/api/plugins/outage_reports/security_advisory_spec.rb[1:3:1]`. Include every
preceding example, not just the previously tested immediate/concurrency pair.
Native result SHA256s are respectively
`f610489b04e66d0d47785858a25e8c3226e32d93b176c7ff90a54db7849526a8` and
`a0aae2e5b4d4e1032ea4f5c4272e24e47c6024c835b9c88d41d7c53c5ac1bd53`.

**Native selection preserves loading and ordering.** Keep the original complete
sorted manifests loaded: 8 operations files and 17 plugin files. Plain prefix-ID
arguments would omit four plugin files that originally loaded before execution.
Instead use RSpec's public `--example-matches` with
`\A(?:<Regexp.escape(full_description) alternatives>)\z` for the original prefix.
Both original topics have unique full descriptions; offline comparison found
exactly 221/288 matches and no suffix collision. Pass the regex as one quoted
argv value, never shell-evaluate descriptions. The short inline workflow code
only reads fixed JSON data and assembles native CLI arguments; add no custom
formatter, ordering callback, helper instrumentation or reusable replay wrapper.

Inspected RSpec 3.13.7 `ordering.rb` sorts by a deterministic hash of seed plus
stable group/example ID, so filtering preserves relative order. Its
`configuration.rb` loads all manifest files before execution; `reporter.rb`
appends examples when started, and the JSON formatter retains that sequence.
The unchanged `spec_helper` seeds RNG once, bootstraps fixtures before the suite,
and wraps each example in rollback unless `:no_transaction`; preserve those
exceptions and all predecessor effects. Topic/support inspection found no custom
ordering or context-hook dependency requiring suffix execution. Keeping all
files loaded preserves declaration-time effects; all executed ancestors and
predecessors before the target remain present. Wall time, thread scheduling and
random sources outside the seeded RNG remain nondeterministic.

**Bounded owner0 package.** On the retained diagnostic branch, modify only
`.github/workflows/api-advisory-diagnostic.yml` and add
`.github/diagnostics/api-advisory-prefixes.json`. Keep the frozen-lock file and
application source unchanged. Fixed data holds each original manifest, seed,
target, ordered prefix `{id, full_description}` entries and source-result digest;
no user-supplied selector or external runtime input. Copy this data beside the
lock into `$RUNNER_TEMP` before exact-source checkout. Reuse the reviewed hosted
Ruby/Bundler/graph/SQL/OS/isolation gates and bounded artifact collection. Preserve
the executed `dbe74d30` source/ref and evidence rather than rewriting it.

For operations first, then plugins only if operations passes: assemble `files`,
`seed` and anchored `pattern` from that fixed data, then invoke the ordinary CLI:

```sh
bundle exec rspec "${files[@]}" --seed "$seed" --example-matches "$pattern" \
  --fail-fast --format documentation --format json --out "$result"
```

Before each actual prefix, run this same selection with native `--dry-run` in a
separate hosted process. Require its JSON seed, count and complete ordered scoped
IDs to equal the retained prefix exactly, normalizing only leading `./`. A mismatch
stops before that prefix; no automatic whole-topic fallback. Dry-run loads the
existing spec helper/database but runs no examples/suite hooks; its separate
temporary DB has the ordinary native cleanup. No local dry-run is authorized here.

Actual runs use fresh processes/DBs, original seeds and `--fail-fast`. Preserve
native exit and complete JSON/logs even on failure; compare their executed ID
sequence to the corresponding leading segment of the original prefix. A valid
pass requires the complete expected count, target last, no failures/pending and
zero native exit. Stop the entire batch at the first failure: distinguish a
reproduced target failure from an earlier/different failure or order mismatch.
If both prefixes pass, record one faithful-prefix nonreproduction and stop.
No bisect, automatic extra rounds, suffix execution or floating whole-topic rerun.

**Review, cost and next result.** Owner0 derives/checks the fixed data offline
against original digests, unique names and complete manifests; runs declared hooks,
YAML/actionlint/shell checks and inspects native-exit/artifact paths. After changes
are committed, independent review of the workflow/data delta and retained history
must precede the next executing push; this changes the previously reviewed test
selection and runtime bound. Keep published `7919` API/exports/clients/KB pins and
ordinary workflow triggers unchanged; prove the actual two-path push fanout.
No public API/schema/migration/deployment change is introduced.

Prefix example time totals 29.9 minutes; original full-topic durations total
39.7 minutes. Allow approximately 35–45 minutes with setup/order gates, one
60-minute hosted job ceiling, and no promised timing. A timeout is incomplete.
Always retain frozen inputs, derived selection/digests, dry-run and actual native
JSON/order comparisons, exit codes, logs and step outcomes in the same seven-day
artifact scheme. Ordinary DB/hosted runner cleanup applies; no session/ref cleanup.
The next observable result is one proven-order target reproduction, an earlier
failure/gate mismatch, or one pair of matching-prefix nonreproductions. Lead
assesses that result before any further reduction or source change. Architect
performed only offline evidence/source reads and this design update.

## Hosted two-example diagnostic — completed isolated control (2026-11-14)

Historical specification, implemented at `dbe74d30dd9b880691762494abc1158169d58ac0`
and exercised by hosted run `43551864218`; current next-step scope is above.
The original design/allocation boundary follows for provenance.

**Original implementation package.**
Owner0 owns the complete isolated workflow/Git/check/execution package. This
supersedes the stopped local-runtime route below. Keep published API
`7919441ccb8e9587ad0afc84674b074ca9c5a880`, exports, clients, KB pins and ordinary
workflows unchanged. The primary `99295` effects fence is independent and stays held.

**Two files and one dedicated ref.** Branch
`2026-11-14-api-advisory-diagnostic` directly from `7919441`, in an owner0-isolated
worktree under this initiative. Add only:

- `.github/workflows/api-advisory-diagnostic.yml`: one fixed job, no matrix,
  arbitrary selector, reusable runner or application change.
- `.github/diagnostics/api-advisory-frozen.lock`: the recovered 8283-byte full
  lock, SHA256 `7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`.

Use only `push` on that exact branch, guarded against branch-deletion events;
no schedule, PR, tag or manual-dispatch interface. GitHub's official
[event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#push)
explicitly permits push workflows not merged into default. A new unregistered
`workflow_dispatch` alone is not the initial execution route. Use read-only
`contents` permission, no deployment secrets, one job, no automatic retries and
a diagnostic-only concurrency group with `cancel-in-progress: false`.

At `7919441`, the two new paths match none of the ordinary push workflows' path
filters, including API topics, integration, i18n and RuboCop. Before publishing,
owner0 verifies the actual SSH remote/base, that the diagnostic commit's parent
is the already-published `7919441`, and the effective new-branch push diff and
all trigger filters. Only the two files may be new. If that fanout cannot be
established, stop before push with the exact uncertainty; do not weaken ordinary
workflow filters. The first push is the hosted launch and must follow quick
checks, committed-source independent review and lead execution release. No
earlier publication for convenience. Retain the diagnostic ref as evidence;
it is not a product merge candidate and no ref deletion is authorized.

**Immutable source and lock.** Checkout the diagnostic event SHA only to copy
the frozen lock into `$RUNNER_TEMP`; verify its digest. Then checkout exact
`7919441ccb8e9587ad0afc84674b074ca9c5a880` into the normal repository directory,
with persisted checkout credentials disabled. Assert its HEAD, copy the retained
lock to ignored `api/Gemfile.lock`, and verify the same hash again. Retaining it
outside the checkout preserves it across checkout cleanup. All application and
spec files now come from the exact failed source; the workflow runs from its
separately reviewed diagnostic commit. Record both SHAs and preserve the lock
unchanged through dependency setup and both examples.

**Hosted inputs and explicit drift.** Use the already-declared `ubuntu-latest`
hosted label and fail early unless the actual OS is Ubuntu 26.04. Hosted image
build/patch and kernel cannot be pinned to historical image `20261111.196.1` by
that label: record their actual identities and differences. This package accepts
that image-build drift as a controlled software comparison, not original-image
equivalence. Keep Ruby **3.4.12**, Bundler **2.6.9**, frozen full graph (122-gem
proof), full plugins, `RACK_ENV=test`, `BUNDLE_WITHOUT=development`, jobs 4/retry 3.
Set `BUNDLE_FROZEN=true` before the normal `ruby/setup-ruby` Bundler-cache step.
No reconstruction, `bundle update`, lock rewrite or restore of a Nix gem prefix.

Use ordinary Ubuntu apt packages with exact version `1:11.8.6-5ubuntu0.1` for
MariaDB server/client/common/core and `libmariadb3`, dev and dev-compat packages.
Record available package versions before installation and actual installed
versions afterward. Require server/client **11.8.6**, actual test DB
REPEATABLE-READ and `innodb_snapshot_isolation=0` before examples. A small inline
preflight may load the existing `spec_helper` and query its automatic temporary
DB without running RSpec examples; normal `tools/test_db.rb` owns its exit cleanup.
No changed runner/helper, private DB setup, container/image or Ruby/SQL/kernel
compilation. Ordinary frozen-bundle native-extension setup remains permitted.

If the hosted OS, exact Ruby/Bundler or exact SQL packages are unavailable, fail
the input gate, upload evidence and run **zero** examples. No automatic fallback.
The smallest subsequent SQL-gate decision would name the exact available Ubuntu
server/client package version recorded by that run, retain every other frozen
input, and label the result a different DB control; it is not authorized here.
Do not reopen a package search or accept a floating `11.8` range. A different OS
likewise needs an explicit revised diagnostic boundary.

**Actions.** Candidate immutable refs from the original run are
`actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1`,
`ruby/setup-ruby@b3aaceaef7e0ee231b499e7b5f49c03fc1d32199`, and
`actions/upload-artifact@cf430e030ddbb5b0abf93d22962f4752f3646cd9`.
Owner0 verifies current official action refs/compatible versions before writing
the workflow. If retaining an older original ref, document the specific
reproduction reason in the workflow; do not silently assume a moving tag equals
the retained action. No additional action or custom transport is needed.

**Exactly two examples, sequentially.** From `api/`, use ordinary
`bundle exec rspec` with documentation and native JSON formatters:

1. `'spec/api/resources/security_advisory_spec.rb[1:3:1]' --seed 42376`.
2. `'spec/api/plugins/outage_reports/security_advisory_spec.rb[1:3:1]' --seed 55119`.

Use separate processes/temporary databases and normal step success dependency;
stop at the first failure, with no `continue-on-error`. Preserve native exits
through any tee pipeline. No topic expansion, predecessor batch or rerun. The
planned JSON names are `matching-software-operations.json` and
`matching-software-plugins.json`; missing second output after a first failure is
explicitly **not run**, never pass. Verify source/lock before and after each step.

**Evidence, cost and checks.** Always upload one seven-day artifact containing
source/workflow/ref/run/attempt identities, lock/hash, OS/image and Ruby/Bundler/
gem/package versions, DB settings, gate results, stdout/stderr, each native exit
and RSpec JSON. No credentials, full environment dump, dependency directories,
cache archives or images. The existing temporary DB cleanup and hosted runner
disposal suffice; retain branch/source and failed evidence. One job has a
30-minute execution budget; expected preparation plus two controls is roughly
10–20 minutes, with no duration guarantee. Timeout is incomplete evidence, not
a diagnosed application failure. No new watcher is part of this design; lead
assigns observation of this new exact run without touching the old primary.

Owner0's quick checks: declared commit hooks, workflow YAML/actionlint, shell
syntax/ShellCheck, exact lock hash, two-file diff, trigger/fanout and pinned-source
checkout/lock-preservation inspection. No local API tests for this package.
After all intended changes are committed and quick checks pass, independent
review covers the full `7919441..diagnostic-head` range, inherited-source boundary,
no new migrations, scope, gates, credentials and failure/artifact paths before
the first executing push. Source-local design records need no separate review.
No API/schema/client compatibility or deployment change is introduced.

**Next observable result:** one exact hosted attempt produces either a documented
input-gate failure with zero examples, the first example failure with the second
not run, or two original-ID/seed results. A pass is only controlled isolated
nonreproduction; it does not waive the original failed matrix or exclude order
effects. Lead assesses that evidence before allocating any further diagnosis.

## Earlier CI-input investigation — stopped local attempt (2026-11-14)

**Admitted attempt stopped at the software-input gate; no preparation or tests ran.** Owner0 retains
source/Git/execution ownership at clean `7919441ccb8e9587ad0afc84674b074ca9c5a880`.
The [diagnosis record](nov14-api-failure-diagnosis.md) preserves both actual full-mode
failures and four local nonreproductions. Unchanged spec/runtime files do not
classify either failure as inherited or feature-induced.

Owner0's [terminal preflight receipt](nov14-matching-software-preflight.json)
records the remaining gap: an ordinary prebuilt MariaDB 11.8.6 server/client
definition and substitution were not identified within the bounded search.
Registered source `/nix/store/7sa2x9c9566lfxkaxs36n3z4yayl5cy4-source` supplies
Ruby 3.4.11 and MariaDB 11.4.13 or 11.8.9. Thirty inspected MariaDB path commits
include the verified 11.8.5-to-11.8.8 jump; this is not a claim about every external
source. Ruby 3.4.12 has a definition at
`2062f852f3cfca91480c6c90f3720845c039be78`, but its binary substitution/closure
was not probed after the SQL gate failed. No version override, workaround,
package/cache download, checkout/gem-prefix preparation or test followed; all commands ended.

The smallest existing hosted units are the individual failed topic jobs
`132240405849` (operations, 243 examples) or `132240405844` (plugins, 337 examples).
Their reruns regenerate the ignored lock and random seed; they are not the frozen
two-ID control, are not authorized by this attempt, and cannot resolve acceptance
by turning green. Lead must choose the next input path: a supplied exact ordinary
prebuilt runtime, or a separately scoped hosted diagnostic/explicit gate change.
No further preparation or expanded search is released by this record. The literal
two-ID commands below remain unexecuted, retained for that subsequent decision.

**Declared environment.** `.github/workflows/api-specs.yml:29-275` runs on
`ubuntu-latest`, installs MariaDB/client headers through apt, asks
`ruby/setup-ruby@v1` for the latest stable `3.4` series, and enables its Bundler
cache in `api/`. The source `api/Gemfile` evaluates the full plugin Gemfiles;
`api/Gemfile.lock` is ignored/untracked and generated by dependency setup. Result
artifacts retain only its SHA256; the complete setup logs also print its bytes,
which owner0 has now recovered. `packages/api/Gemfile.lock` is a different
packaging input (SHA256 `3c23473f34c8ffbf52d46b6c32fc3f858a35b5d84b1cb746e3e0a3d13f0ab5ba`);
neither it nor the export-tooling lock reconstructs the observed CI lock.

Offline, no-IFD evaluation of the frozen flake confirms only these checks:
`effective-notification-templates`, `notification-templates`,
`replacement-notification-templates`, `replacement-notification-templates-module`,
`webui-software-revision-links`. There is no exported full API test check or
CI-equivalent test environment to enter with `nix develop <check>`.
The existing `devShells.x86_64-linux.api.nativeBuildInputs` selects Ruby 3.4.9
and MariaDB 11.4.12. Its hook installs Bundler if absent and runs `bundle install`;
entering it is not a read-only input probe. The followed nixpkgs revision is
`a9e6d84f9c2f9012f5fe7d964a7851352300e61a`, via vpsadminos `8e44a5124439b1f3048ffc56b1717614a5360358`.

**Recovered original inputs.** Owner0 retrieved only the completed failed jobs
`132240405844` (full plugins) and `132240405849` (full platform-operations) from
run `43528601962`, attempt 1, source `7919441`. Their `Print lockfile` blocks
independently yield byte-identical 8283-byte files, verified by architect against
the original SHA256 `7e2f9babb3b733a438ab5a77c8bf813ae53a32025df1ce55990a2270fec69e51`:
[plugins lock](nov14-ci-original-plugins.Gemfile.lock) and
[operations lock](nov14-ci-original-operations.Gemfile.lock).
[Recovery evidence](nov14-ci-input-recovery.json) records the exact raw logs,
hashes and extraction bounds. Only log timestamp prefixes were removed; this
supersedes the earlier missing-lock dependency and failed reconstruction attempt.

[Runner/cache evidence](nov14-ci-runner-cache-evidence.json) identifies Ubuntu
26.04.1, runner image `ubuntu-26.04` version `20261111.196.1`,
`ruby/setup-ruby` commit `b3aaceaef7e0ee231b499e7b5f49c03fc1d32199`, toolcache Ruby
3.4.12 revision `366f5fdc00` at `/opt/hostedtoolcache/Ruby/3.4.12/x64`, and bundled
Bundler 2.6.9. MariaDB/client/native library packages are Ubuntu
`1:11.8.6-5ubuntu0.1`; actual DB is `11.8.6-MariaDB-5ubuntu0.1`,
REPEATABLE-READ/snapshot 0. Use the recovered full lock, including AR/AS 8.1.4.1,
RSpec 3.13.7 and HaveAPI 0.32.2, rather than selecting those versions individually.

The observed matching dependency-cache hit was 28,810,681 compressed bytes
(about 27.5 MiB), at the exact key recorded in the linked evidence. Its configured
target is `api/vendor/bundle`; archive contents, unpacked size, availability and
native-extension compatibility have not been verified or downloaded. Ubuntu
native extensions must not be transplanted into the Nix shell on the strength
of Ruby's version alone. Following recovery of the original lock and the
122-gem version proof, lead admitted one isolated attempt using standard prebuilt
user/Nix tools. This is a controlled software-version match, not bit-identical
Ubuntu CI acceptance. Hard gates are Ruby 3.4.12, Bundler 2.6.9, MariaDB 11.8.6
and matching client, the frozen full graph/unchanged lock, full plugins,
`BUNDLE_WITHOUT=development`, `RACK_ENV=test`, REPEATABLE-READ and snapshot 0.
Owner0 records exact input/store paths, ABI compatibility and resource preflight
before ordinary isolated preparation. Preserve shipped dependencies, pins, source
and existing bundles. No VM/container/image, global switch, bespoke FHS/linker or
raw client, Ruby/SQL/kernel compilation, or bulk restoration is authorized.
If ordinary prebuilt versions are unavailable or a workaround is needed, stop
and report the exact input gap and smallest existing hosted diagnostic option.
Do not silently adopt a different version or execute with an unmet hard gate.
The workflow has no example-selector dispatch input; do not run its whole matrix
or change a test runner merely to obtain a selective handle.

**Retained conditional owner0 execution brief (not released after the preflight stop).**
If lead subsequently releases execution with the required inputs,
use an owned isolated checkout of the exact source with the original full lock,
matching runtime/native gems and all plugins, preserving the existing API and
tooling bundles. In its `api/` directory, require no inherited external database
configuration; ordinary `spec_helper`/`tools/test_db.rb` starts a fresh temporary
database for each RSpec process and owns its shutdown. Execute only these two
commands, separately to retain each original seed, stopping at the first failure:

```sh
set -euo pipefail
env RACK_ENV=test VPSADMIN_PLUGINS=all SPEC_MODE=full BUNDLE_WITHOUT=development BUNDLE_JOBS=4 BUNDLE_RETRY=3 \
  bundle exec rspec 'spec/api/resources/security_advisory_spec.rb[1:3:1]' --seed 42376 \
  --format documentation --format json \
  --out /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov14-matching-software-operations.json
env RACK_ENV=test VPSADMIN_PLUGINS=all SPEC_MODE=full BUNDLE_WITHOUT=development BUNDLE_JOBS=4 BUNDLE_RETRY=3 \
  bundle exec rspec 'spec/api/plugins/outage_reports/security_advisory_spec.rb[1:3:1]' --seed 55119 \
  --format documentation --format json \
  --out /home/aither/workspace/ai/vpsfree.cz/work/2026-10-30-oomd-abuse-policy/nov14-matching-software-plugins.json
```

Before execution, record source and Gemfile/plugin hashes, actual complete lock
and its digest, Ruby/Bundler/all loaded gem versions, actual OS/native package
build identities and every difference from the recovered CI image. Capture native exit, stdout/
stderr, JSON, actual example ID/seed and DB startup version/isolation; verify the
lock is unchanged afterward. Stop before testing if the required input identity
does not match. Stop at the first failure and return exact evidence for owner0
diagnosis. If both pass, stop and report controlled isolated nonreproduction;
this neither proves the original environment equivalent, excludes predecessor/order
effects nor waives failed CI. No automatic extra rounds.

Dependency scope is ordinary Ruby/Bundler/gems (including native extensions) and
the matching MariaDB/client libraries, not a guest/image build. The observed
27.5 MiB gem-cache hit does not establish total environment or unpacked size,
current availability, or a usable local runtime. The admitted hard gates and
resource preflight precede isolated preparation;
given prior 283-432 second controls, execution needs a fresh permitted watcher or
the documented visible parent fallback. No builds, installs, tests, provider
queries, source changes, client/pin changes or runtime probes were performed here.
This source-neutral diagnostic admission changes no API contract and authorizes
no release/integration. The original primary watch's `99295` external-effects
fence remains separate and unresolved; no parallel preparation by architect.

## Current addition — ordinary osctl-oomd report localization (2026-11-13)

**Ready for owner0 implementation.** User requested rebase on current default
branches and localization of each ordinary osctl-oomd action report to the user's
configured language. Owner0 freshly fetched SSH default
`2d0946c4e699aa61092228d8a7cb275477ee46d0`; original feature
`f60d41a453b1703e42de4341285bdc6ba339aff0` and its evidence are retained.
Both immutable sources have identical English stop/restart subjects and one-line
bodies. No upstream paragraphs, URLs or metrics are missing. Owner0 owns all
vpsadmin Git/rebase/source work. Stable rebased source before localization is
`c02f56e1c45d6dfeb4f5fbfbee486ee584ef1460`, tree
`7d2adf1f4b7aafd829fa754f8c02f9977baf10e1`; the traced formatter/ingestion/mail/i18n
source files are unchanged from f60. Owner0 records the final localized revision.

**Route and semantics.** `api/lib/vpsadmin/supervisor/node/vps_events.rb` validates
the node/VPS and stop/restart action. The feature's `record_oomd_event` supplies
trusted provenance to `IncidentEscalation.ingest!`, which deduplicates and creates
`IncidentReport` under its VPS lock. `IncidentReport::New/Send` later passes that
stored object to ordinary `vps_incident_report` mail. API subject/text fields and
WebUI report rendering consume stored strings. The current hardcoded strings
therefore need translation at creation; translating escalation mail would not
solve this request.
Specifically, `api/lib/vpsadmin/api/resources/incident_report.rb` exposes the
stored subject/text and `webui/forms/incidents.forms.php` applies existing `h()`
escaping to both. No frontend translation or new field is required.

Render **once**, inside the existing ingestion serialization after source-node
validation/dedup and immediately before creation, for the same freshly locked VPS
owner assigned to `incident.user`. Use `user.language.code` when supported by the
existing API catalog; nil, blank or unsupported language uses
`VpsAdmin::API::I18n::DEFAULT_LOCALE` (English). Ignore the supervisor's ambient
locale and any API viewer locale. Use existing `::I18n.with_locale` scope so
locale is restored even on failure and cannot leak to another thread/report.
Do not swallow unrelated rendering errors.

**Small source boundary.** Add a focused
`VpsAdmin::API::IncidentReports.oomd_event_message(vps:, user:, action:)` formatter
to existing `api/lib/vpsadmin/api/incident_reports.rb`, returning only subject/text.
Its four literal `VpsAdmin::API::I18n.t` keys live under:
`incident_reports.oomd.stop.subject`, `incident_reports.oomd.stop.text`,
`incident_reports.oomd.restart.subject`, `incident_reports.oomd.restart.text`.
This file is already scanned by the catalog; supervisor files are not.
Use literal keys in the action branches, not runtime-built keys or a new registry.

The necessary lock-safe seam is one optional internal `report_message:` callable
on `IncidentEscalation.ingest!`, called with the locked VPS and its selected owner
after duplicate rejection. The node adapter supplies the focused formatter; merge
only its subject/text into the static source attributes before the single create.
Existing callers keep passing their attributes unchanged. Preserve the existing
after-create block for logging. This small producer-supplied builder is not a
public API, callback registry or message framework; it avoids translating for a
stale owner before lock acquisition. Owner0 confirmed no existing earlier
creation seam can do this without changing the logging block or double-writing.

**Approved copy**, supplied by lead after the writing skill; body has exactly one
terminal newline, shown here as `\n`:

| Key suffix | English (unchanged) | Czech |
| --- | --- | --- |
| stop.subject | Stop due to abuse | Zastavení kvůli nadměrnému využívání prostředků |
| restart.subject | Restart due to abuse | Restart kvůli nadměrnému využívání prostředků |
| stop.text | VPS #%{vps_id} %{hostname} abused shared system resources and was stopped.\n | VPS #%{vps_id} %{hostname} nadměrně využíval sdílené systémové prostředky, a proto byl zastaven.\n |
| restart.text | VPS #%{vps_id} %{hostname} abused shared system resources and was restarted.\n | VPS #%{vps_id} %{hostname} nadměrně využíval sdílené systémové prostředky, a proto byl restartován.\n |

Keep hostname interpolation as data, with existing downstream escaping; no ERB
evaluation or translated action/codename/source identity. Edit existing en.yml
and cs.yml and use normal catalog normalization/checks. No new report fields,
endpoint, migration, node message, client member or mail-template variable.

**Persistence and compatibility.** Store the rendered subject/text as today.
Historical reports, duplicate redeliveries and queued reports are never rewritten.
Changing language or VPS owner later does not translate an existing report.
Creation means receipt-time owner under the existing lock, not an inferred owner
at historical occurrence time. Keep occurrence timestamps, source dedup,
qualification, ownership epochs and old-owner notification suppression unchanged.
Ordinary mail wrappers retain existing language selection/English fallback at
mail preparation; they embed the stored body unchanged, even if preference changed
between report creation and mail preparation. Existing mail opt-out, retries,
`notification_processed_at`, escalation templates/counts/stops are unaffected.
Rollback simply creates future reports with old wording; persisted strings remain
readable by old clients. No deployment or merge is authorized here.

**Files and acceptance.** Owner0 owns the supervisor adapter, small ingestion seam,
existing incident-reports formatter file, en/cs catalogs, focused supervisor/model/
mail specs and a short note in `docs/incident-escalation.md`. Use current source
selection rules; a new formatter spec in existing `spec/lib/.../incident_reports_spec.rb`
already belongs to platform-config, supervisor/model specs to foundation.
Tests must traverse actual accepted node event → stored report and ordinary mail
preparation for stop/restart in EN/CS, exact English bytes/newline/interpolation,
nil/unsupported language fallback, ambient-locale restoration/isolation, and
locked-owner selection. Prove duplicate replay after locale change keeps original
report/log/count/mail decision; historical/manual report text and disabled
ordinary mail are unaffected. Reuse existing dedup/transfer controls, adding only
the localization assertion needed to establish this boundary. Include a real
template-render assertion, not only a mocked mail call. Use owned disposable
databases; no guests or old-state mutation.

Run required focused specs, catalog normalization/health and hooks in declared
Nix environment. Commit complete intended source and quick-check results before
independent review, then applicable longer checks under the monitor policy.
Lead/owner0 coordinate CI; no duplicate monitor. The intentional deletion of the
old services-root image remains effective: no recreation/resume/capture launch.

**Generated-client dependency, separate from this four-string change.** Current
repository instructions require final-source API export/comparison for Go, Rust
and TypeScript even for behavior-only work. The earlier shared-escalation fields
also need assessment on the rebased API. Owner0 produces exact committed API
schema/provenance/tooling lock under `docs/api-schema-export.md`; owner1 can own
client-generation packages in `vpsadmin-go-client`, `vpsadmin-rust-client` and
`vpsadmin-typescript-client` from that frozen export, reading each repo's guide.
Owner2 reports current React default uses TypeScript client0.4.0 / HaveAPI0.32.0
without shared incident fields: coordinate the regenerated typed-client dependency
before final React source/checks. Preserve generator/runtime/version provenance,
generated versus handwritten boundaries and per-client no-change evidence where
applicable. No version/release is inferred from synchronization. A published
TypeScript package containing required members is a later WebUI merge prerequisite
under the current procedure, not authorization to publish now. These dependent
packages do not delay the independently implementable localization above.
Owner2's exact types, wire null/reset/filter and capability requirements are in
[React SDK requirements](react-rebase-nov13/sdk-requirements.md); owner1 received
this technical handoff. The existing canonical KB impact workflow remains with
owner3 for the final backend pin and actual reported page/capture impact; this
localization brief adds no screenshot scenario or runtime admission.

**Generated choices clarification (2026-11-14).** Owner1's retained HaveAPI
`1ef9b204` generation represents `incident_policy` and `incident_status` as
primitive strings; runtime descriptors preserve kind/required/nullable and do
not compile schema `validators.include` into client-side choice enforcement.
That is the accepted current generator boundary, not a defect requiring provider
changes. Preserve the raw schema constraints/provenance and generated output as
produced. The API remains authoritative for registered selector/status values,
unknown/blank/null rejection and isolated setting-write validation. The SDK must
preserve omitted selectors, explicit values, nullable override resets and false
booleans; existing primitive/null validation remains in force. Unknown strings
may reach the server and its validation failure must be surfaced normally.
No new enum generator, local cast/shim or duplicate choice validator is needed.
React uses generated operations, the returned selector and its existing known
status presentation; synthetic second-rule strings stay test-only. Earlier
“preserve generated choices/validation” wording means preserve the actual
generator/schema/server division, not add client-side enum enforcement. Verify
these wire cases and server refusals within the assigned checks; no new provider
scope or publication authority follows from this clarification.

Verification repair, 2026-10-31: [current KB tracker implementation contract](kb-tracker-repair.md)
records the proved setuid/capability helper procfs incompatibility, schema2
wait-only descendant lifetimes separated from strict control authentication,
and supervised readiness/drain. Lead accepted and released owner3's bounded
implementation after the user directed “find the root cause and fix it”.
Old dead/incomplete run recovery remains separate and uncertified; no receipt
conversion or runtime replay is authorized. Incident-escalation scope is unchanged.

User approved the bounded shared design on 2026-10-30: “ok, agreed, reworkit”.
[Released implementation contract](implementation-contract.md) is authoritative
for all field names, schema, registry, API, mail, behavior and package boundaries.
The [previous narrow contract](implementation-contract-before-shared.md) is retained
as historical evidence only. [Reassessment](reassessment.md) records alternatives;
the predefined-rule option is now selected. No merge/deployment authorization.

## Scope and rationale

Share counting, escalation and durable stop/mail execution across explicitly
registered incident types. Initially register only existing codename `oomd`,
displayed as “VPS memory-pressure incidents” / “Incidenty přetížení paměti VPS”.
The qualifying source is a trusted successful whole-VPS daemon restart/stop.
Existing process-kill `OomReport` concepts and node event protocol remain intact.

`IncidentReport.codename` is free-form and accepted from admin API, nodectl and
mail parsers; it cannot alone authorize automatic stops. Each code registry entry
owns its qualification relation, default settings and optional specific templates.
No arbitrary admin-created rules, new actions, transport or generalized workflow.
Future rules may explicitly qualify manual reports, but none are enabled now.

## Policy and state boundaries

- Warn at 5 unique qualified occurrences in rolling 7 days, at most weekly per type.
- Stop after a new occurrence at 10 in rolling 30 days; stop email follows actual
  success. No requirement for a previously delivered warning.
- Counts, overrides and warning recurrence are per VPS/type/current owner epoch.
  VPS stop permission, pending/uncertain physical action guard and last successful
  stop cooldown are shared across types. Only one stopping type is registered.
- Further stop requires a new occurrence at least 24h after the last confirmed
  stop. Incidents during cooldown never schedule future stops. Manual restart
  remains possible; falling below rolling stop count restores ordinary rules.
- Observe is default; notify adds warnings, enforce permits stops. Exemption
  suppresses these vpsAdmin stops while retaining counts/warnings and the node's
  protective daemon. Settings/mode changes alone never act.
- Keep source dedup, occurrence-time windows, >24h stale visibility-only dispatch,
  successful-transfer epoch reset/old-owner action suppression, audit retention,
  failed/uncertain stop reconciliation and independent durable mail retries.

Use existing VPS row/resource locks, Stop chain, incident scheduler and MailTemplate
registry. One per-type settings/warning-state table and one durable action table
replace narrow state; VPS retains shared ownership/physical state. IncidentReport
gets backend-only source identity and ordinary-mail progress metadata. All exact
names and selector semantics are in the contract; no competing interface here.

## API, UI and mail

Existing VPS routes expose a flat summary for selected registered `incident_policy`,
default `oomd` on reads. Explicit selector accompanies isolated admin setting writes;
unknown/empty/mixed requests fail before effects. Counts/status filter before
pagination with batched queries. Owners read summaries; only admins alter overrides
or shared exemption. Older APIs gracefully hide new UI through capability detection.

Keep existing VPS list/detail/admin surfaces in legacy and React UIs. Show selected
type label and explain shared physical cooldown/exemption. No rule editor or extra
navigation with one rule. Separate process OOM screens retain existing meaning.

Four mail templates: specific memory-pressure warning/stopped and generic incident
warning/stopped. Explicit registry mapping chooses specific when installed,
otherwise generic; opt-out/render/SMTP failure never switches templates. Counts
are decision snapshots; limits/enforcement permission use current settings at
render/retry. Lead's [copy brief](mail-rework-copy.md) owns final EN/CS text, current
consequence, actual stop/autostart effect, remedies and specific membership/KB links.

## Compatibility and migration

Owner0 reconfirmed migration20261030180000 unmerged, unreleased, undeployed and
not externally persisted; only owned disposable test databases used it. Revise
that single migration and core schema, resetting disposable databases. Preserved
4d72e3e7 provides old-source review evidence. No transitional/existence-guard schema.
No new protocol or coordinated node deployment is needed. Unreleased frontend/API
names change together; old ordinary clients remain compatible with additive data.

Future deployment: migration, matching templates/backend in observe mode, then
compatible UIs; verify before deliberate notify/enforce selection. Software rollback
disables dispatch and reconciles already dispatched effects, retaining additive
state/audit. It cannot undo actual VPS stops. Deployment/integration remain separate
approval boundaries; heavy runtime allocations are presently held.

## Owners and checks

Backend owner0 owns API/schema/evaluator/registry/scheduler/mail and vpsAdmin Git;
legacy owner1 owns disjoint webui/ and agreed browser fixture; React owner2 owns
separate vpsadmin-webui adapters/components/catalogs/tests/docs; owner3 owns site
templates and later KB pin/capture. Lead owns wording, state and review coordination.
Consumers can execute from the released contract; serialize shared Git operations.

Quick checks cover current behavior plus synthetic second-rule isolation/shared
stop limits, selector/permission/null/receipt cases, migration, fallback versus
suppression/errors, actual localized/timezone renders and consumer wiring. Existing
CI failures remain owner diagnosis obligations, not waived by redesign. Changed
runtime/spec paths require CI selector/topic updates. After final committed source
and quick checks, independent final code/API/schema/history review precedes long
real stop/restart/mail/ownership scenarios and affected UI/KB captures. Fresh watchers
own long checks after lead capacity release. No tests/builds run by architect here.

Canonical KB workflow retains the two impacted bilingual list concepts, final
published backend pin and source-review-before-capture sequence. No unrelated
baseline refresh, new screenshot scenario or React certification is implied.

[Log evidence](evidence.md) retains calibration: selected 5/10 limits, VPS28376
below stop threshold, inferred-success/coverage caveats and rejected3/8 comparison.
No further log scans. [Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-30-oomd-abuse-policy/)

## Monitor registration diagnosis (2026-11-14, complete)

Read-only diagnosis confirmed watcher capacity refusal, not a verification failure.
Identity and live roster match this session; architect0 retains Astra/xhigh and
workspace_write. Installed runtime is `22x45q9snm46qw95c1zjsbavifv9fki9`, with
immutable source `/nix/store/882d9278smpacf3czxzc0wliggx03a9f-source` and catalog
`f2d5a8909570f32bf65098940649922528d081974eefdb3bf678fb38e4ad568d`.

The public CLI requires both verified session markers plus
`DEV_SESSION_EXPECTED_MONITOR_THREAD_ID` and `DEV_SESSION_EXPECTED_ROOT_THREAD_ID`;
`CODEX_THREAD_ID` alone does not supply that binding. Only the actual lead/root
invoked its own bound CLI. The MCP adapter collapses command errors into the same
unconfirmed-action message (`portal/cmd/workspace-portal/monitor_mcp.go:73`).
Native stderr exposed the actual React unchanged-start refusal:
`monitor utility concurrency is full; prior execution must be proved terminated`.
See [stderr](react-rebase-nov13/r1-monitor-native-start.stderr) and
[exit 1](react-rebase-nov13/r1-monitor-native-start.exit).

`portal/internal/monitoroperation/store.go:303-339` checks same-session active
reservations against the frozen policy's `maxConcurrent` (installed value 1),
and returns that error **before saving the new operation**. `Service.Start`
(`service.go:328-401`) returns it before `launch`; native project/thread creation
starts only in `launch.go:67+`, after durable reservation. Thus the observed
React refusal caused no native watcher launch. Root-bound public status returned
missing operation JSON for all three new IDs, with no record removal or alternate
launch reported:

| Scope | Requested operation | Native status evidence |
| --- | --- | --- |
| React | `9f879ec7-d5a1-452d-a581-ddfd18486bfb` | [stderr](monitor-native-status-batch/react.stderr) |
| Rust | `db78ba13-302d-4d2e-ade1-ad618315d504` | [stderr](monitor-native-status-batch/rust.stderr) |
| KB | `b65b0538-9b40-4181-b2f3-ff3cc9b2d993` | [stderr](monitor-native-status-batch/kb.stderr) |

These missing records and the write-before-launch contract establish that no
registered watchers own those requested IDs. Rust/KB original start errors were
not individually recovered; no additional retry is needed to settle observation
ownership. Existing backend operation `a8c49117-6d98-4afd-9b5d-15afe4132919`
remains with its confirmed sole observer; it was not inspected or changed here.

Supported next action: lead visibly uses the monitor skill's active-parent
fallback for only the three new exact saved source/run-attempt scopes, with bounded
status output and interruptible waits. Keep the parent turn active; this path has
no durable automatic continuation. Do not rerun checks, launch replacement watchers,
duplicate backend observation, or cancel/resolve another operation to gain capacity.
No runtime fix, package change, provider observation or lifecycle operation was
performed by architect. The lead owns fallback execution and state tracking.

### Owner-local persisted receipt accounting — complete (2026-11-14)

The newly authorized owner-local route supplies the exact missing evidence for
monitor `3b57fd25-6069-4e96-bda7-9eb1b2714b14`; it does not add a public API route
or revisit `99295`. Installed dd90 `codex/activity_lineage.go:80–115,181–217`
confirms suffix-only discovery in `sessions`/`archived_sessions`, symlink skip,
duplicate refusal and nofollow regular-file/session metadata checks. Installed
`workspace-host:3765–3779` derives the home from the registered workspace name.
Own registry entry `vpsfree-cz` matches this workspace and yields
`/home/aither/.local/state/dev-workspaces/codex-homes/vpsfree-cz`; ambient
`CODEX_HOME` was not used.

Filename-only traversal found one exact utility file. Nofollow open/fstat and
first-line metadata match utility `01a1d81c-1350-78a0-b6b8-ab8e63bd3dfd`, expected
session cwd/workspace roots, owner UID 1000, dev-workspace and native 0.165.0.
The lead's fresh public status supplies root/incarnation/project binding.
Original turn `01a1d81c-1ce3-74b0-b103-d723ff449e18` is bound at `task_started`
line 14 and `turn_context` line 15. The stable file has 460,196 bytes and 148
complete JSONL lines, SHA256
`996cc15bc96158699af0f4144e03ae4449ec9ab62d761d5ed0b2fd95765ea26f`.

Private [machine accounting](nov14-diagnostic-ci/monitor-3b57-persisted-accounting.json)
records each call ID, paired outer call/result, native item/handle and exact
line/timestamp/hash provenance without raw prompts or command output:

- All **19 outer calls have results**: 17 `functions.exec` scripts completed
  with their nested calls awaited, and both clock sleeps returned.
- All **10 native command handles are terminal**: nine exit 0; handle `84723`
  exits 1 at line 97, paired with outer result line 98. Failure is retained.
- Six monitor calls returned terminal receipts, including **two failed report
  calls**. Those failures do not become a successful monitor report.
- No `functions.wait`, `write_stdin`, yielded cell, returned live session,
  unpaired call/result or unmatched native item remains. All terminal producer
  receipts precede `task_complete` at line 148/EOF; there are no later records
  and no unresolved handle requiring a late receipt. No background launch
  indicators were found in the recorded command/control syntax.

**Disposition:** recorded command-effect accounting is complete for this exact
utility/turn, based on paired receipts rather than turn termination, CI success,
OS absence or root-local tool access. Root independently verified the exact file,
hashes and complete accounting, rechecked owner status, then performed supported
effects resolution for `3b57` only. Separate status readback verified resolution
`bb30ad72-d92d-44fa-8ef7-5379d556cd4c` at `09:49:34.242429707Z`; see the private
[verified resolution receipt](nov14-diagnostic-ci/monitor-3b57-resolution-verified.json).
The immutable terminal `INCOMPLETE`, failed report attempts and separate captured
remote CI result remain unchanged. The API's internal `canceledAt` is its normal
continuation fence; no separate cancel, wake, lifecycle or cleanup action occurred.
The unrelated `99295` fence remains held and excluded. Architect performed no
resolution or additional investigation. The persisted route supersedes earlier
missing-evidence limits only for this exact accounted `3b57` turn; the initial
public-route gap and other historical limits remain recorded below. This package
is complete; no broader reconciliation follows.

### Passive utility history contract — public route gap (2026-11-14)

Earlier API-route finding retained below. The authorized persisted-receipt route
above now supplies evidence for this exact utility without changing that public
interface finding or authorizing any other history access.

New peer-supplied contract evidence is confirmed in our installed immutable
package `22x45q9snm46qw95c1zjsbavifv9fki9`: its source `882d9278…` pins
codex-web `dd90fb4308ba85617ee2a4267cc835aa9a4f11ce` (`portal/go.mod`,
`flake.lock`) and packages native 0.165.0 (`nix/workspace-portal.nix:528`).
Installed `share/workspace-portal/codex/history_reader.go:31` allows only the
three passive methods; `thread_page.go:249` confirms `includeTurns:false`.
This establishes a client-library contract, not an accessible root invocation.

**Bounded route finding: no supported exposed invocation established.** The
installed portal's thread CLI has `observe`/`activity`, but no raw metadata,
turn-page or item-page command (`portal/cmd/workspace-portal/main.go:833+`).
Its public history routes resolve to the session lead or a ready roster member,
not an arbitrary utility (`portal/internal/web/server.go:4013–4041`;
`docs/workspace-portal.md:490+`). The library's `HistoryPool.Request` is not a
CLI/MCP endpoint. Available monitor MCP actions likewise expose no raw-history
operation. Ambient `/run/current-system/sw/bin/codex` resolves to 0.167.2;
that binary is not evidence of a pinned 0.165 registered-client route. No native
request, proxy retry, new client/process, raw socket or private-history read was
performed. This finding does not assert that the native methods are absent.

Smallest public clarification for the lead/runtime owner: **Which existing
installed CLI, MCP or authenticated HTTP invocation exposes these three raw
passive methods over this workspace's registered pinned connection for the
exact monitor-owned utility, without loading/resuming it or creating a client?**
Supply the supported invocation and binding/authorization contract, not only
method schemas or Go source. No literal executable root command is justified
until that interface is identified; no implementation/package change is released.

If the lead establishes that route, first recheck current operation `3b57fd25`
status and its exact utility/turn. The bounded passive request plan is:

- `thread/read`: `threadId=01a1d81c-1350-78a0-b6b8-ab8e63bd3dfd`,
  `includeTurns=false`; verify returned identity and session cwd.
- `thread/turns/list`: same thread, `limit=20`, `sortDirection=desc`,
  `itemsView=notLoaded`; follow `nextCursor` only to establish original turn
  `01a1d81c-1ce3-74b0-b103-d723ff449e18` and its status.
- `thread/items/list`: same thread and exact original `turnId`, `limit=32`,
  `sortDirection=asc`; consume `{turnId,item}` rows and all `nextCursor` pages
  for that turn. Reject mismatched identities, repeated cursors/rows, malformed
  or incomplete pages; a partial read stays incomplete. No other-turn inventory.

Keep any later raw receipts private in this session's tracking. Terminal
`commandExecution` items/exits alone do not inventory `functions.exec` cells or
`write_stdin` sessions: require outer call/result pairing and authoritative late
producer results for every known nested/yielded handle. Missing or unmatched
receipts retain the fence. Turn termination and captured CI success cannot fill
that gap. Lead owns applicability, actual reads and any later resolution decision;
this package performs no ResolveEffects/cancel/cleanup and does not revisit
`99295`. Both old fences remain held. The earlier backend finding below remains
historical evidence, not a prohibition on evaluating this new specific contract.

### Original backend observer reconciliation (2026-11-14)

#### Current local a8 metadata check — owner0 brief (2026-11-14)

**Sufficient bounded read-only package; root releases execution and accepts the
result.** Supplied operator statement via peer `da2c76bf`, “there wasn't any
remote executor”, answers whether this workspace ever had remote execution
configured. Root accepts this factual declaration, with the accepted source fact
that local shell-snapshot execution remains local, to exclude the nonlocal
alternative. It grants no control authority. This supersedes the startup-evidence
blocker below for this assessment; peer P1's older zero-gh result is not current
own evidence. No further configuration/history/source search is required.

**Narrow preflight correction after the first stopped acquisition.** Retain
`monitor-a8-current-local-metadata.json` SHA `ac611999d83cec4570bfb7d0ca0d61a62312ff76589033353b7e6e75c52c04e7`:
the exact native/socket binding passed, but `/proc/1/ns/pid` returned EACCES before
inventory. It supplies no count or absence proof. Namespace-link access is subject
to Linux ptrace-read permission checks; denial for root-owned PID1 does not prove
hidden UID1000 processes. PID1's namespace link is not required for this daemon's
domain. Replace that probe with these checks before/after the bounded acquisition:

- Reader `/proc/self/ns/pid` and exact native `/proc/1309145/ns/pid` links must
  be readable and equal, alongside the unchanged native PID/start/UID binding.
- `/proc/self` must resolve to the reader's `os.getpid()`; its status `Pid` and
  single-entry `NSpid` must equal that value. Native status `Pid`/single-entry
  `NSpid` must similarly equal1309145. `NSpid` lists PID mappings starting at the
  procfs mount's PID namespace: this rejects an ancestor-mounted view and binds
  the active namespace to the view being enumerated. Missing or inconsistent
  fields refuse; no claim about the system's initial namespace is needed.
- Parse the reader's mountinfo to require the actual `/proc` mount is procfs
  with root `/`, without a hiding/restricting option (`hidepid` absent or0),
  subset restriction, or an overmount obscuring numeric PID entries. Preserve
  mount/namespace/mapping identity through the closing pass. Non-PID auxiliary
  mounts do not by themselves hide the PID inventory.

These establish coverage of the daemon's PID namespace, including visible child
namespaces, without reading root-owned PID1 metadata. Ordinary Linux references:
`pid_namespaces(7)` procfs visibility, `proc_pid_status(5)` NSpid semantics and
`proc_pid_ns(5)` namespace-link access. This is a replacement criterion, not a
permission-error ignore rule: all inaccessible owner/unknown-UID entries, possible
candidate reads, mapping/mount changes and unresolved races still refuse. No
privilege elevation or additional process/config/source discovery is needed.
Root must separately release any corrected acquisition; do not repeat the old
probe or overwrite its receipt. Historical exit/INCOMPLETE and all other filters,
ownership checks, bounds and acceptance conditions below remain unchanged.

**Current composite finding: local quiescence supported; root resolution decision
remains separate.** Lead-accepted supplied evidence `ea97ac40`, source/result SHA
`6d4003969acebd9837aa5a7f6ce483e8da1d54026b54d2be760812992eea2036`,
classifies the previous errors at18:58:38.189056–18:58:38.190497Z:
1663 is stable UID1000 `(sd-pam)`, start1097;3852288 is stable UID1000 Python,
start119009438. Both predate this invocation and cannot be its freshly spawned
command/wrapper/descendants under the accepted construction.1229082 is an older
UID1000 codex zombie, start53340886, incapable of executing; its dangling executable
was not a disappearing live gh.3275616/3275617/3275739 have no proc record at that
targeted read. Native boot/PID/start/ELF matched before/after; this supplied probe
did not recheck the full socket epoch and is not our independent reproduction.

Together with the accepted own fullproc/namespace/native/socket acquisition,
zero gh/original payload, corrected531-entry exclusions, operator nonremote
declaration and211 terminal outer cells/31 other terminal handles, these targeted
classifications close the recorded eligibility gaps. No eligible unresolved
known local work or future-capable original cell remains under this fixed-command,
trusted-operator scope. Transient-PID absence alone supplies no historical exit;
the finding is composite current-local accounting, not continuous atomic absence
or remote CI proof. Original exit remains UNKNOWN and immutable `INCOMPLETE`
unchanged. Root may accept the evidence for normal supported effects resolution
with fresh exact-owner/native/launch/delivery/submission guards and readback.
No new scan, history/config/source query or control/resolution was performed by
architect. The following insufficient-projection findings are historical and are
superseded only by this explicitly supplied additional evidence.

**Retained corrected-acquisition eligibility assessment.** Receipt
`monitor-a8-current-local-metadata-corrected.json`, SHA256
`fe4635c5434bdb378dd3dedf814c12c807b7ca8ea0071ab4d0ad1b261f8a1a0e`,
passes the before/after native/socket/proc-view guards and records zero gh/exact
original payload matches. Its531 possible entries are not531 owned-work obligations:
489 are bash processes and42 are existing node/esbuild/mosh/Ruby/podman services;
all have UID1000 and predate the original launch interval under the retained
clock mapping. None falls within that interval or contains the original payload.
Latest bash start121507585 precedes the interval's lower bound121541461.6 by
338.766 seconds; latest service start120401345 is earlier still. Native execution
creates a fresh per-command process; this fixed literal has no explicit background
or escalation. Combining that construction with these earlier starts and the
nonmatching executable/payload roles excludes them as the invocation's newly
spawned shell/gh/descendants in the accepted trusted-operator model. Existing
shared services are not eligible merely because they could execute other work.
This supersedes the old-command-capable-shell/unclassified-age catchall, not
genuine wrapper evidence; timestamps, cwd or PPID alone do not establish exclusion.

**The retained projection is nevertheless insufficient for complete eligibility.**
Denied1663/3852288 appear in both passes only as generic PermissionError records,
with no retained UID, comm, start identity, failing field or candidate-stage flag.
They are absent from the531 detailed entries. Disappearance records for1229082,
3275616,3275617 and3275739 likewise omit identity/eligibility; numeric inventories
retain counts rather than those mappings. Therefore this record cannot distinguish
root/pre-existing unrelated services from genuinely eligible unreadable work.
Minimum missing information is the already-observed UID/comm/start and failure
stage for each such record (or an explicit record that failure preceded obtaining
those fields). No such metadata was fetched in this assessment. Do not reinterpret
the errors as owned processes or silently discard them. a8 remains held; no new
acquisition or resolution is released and historical exit/INCOMPLETE remain.

Owner0 performs one bounded local acquisition using a short direct metadata
script, with a 30-second bound and one closing inventory pass, not a reusable
scanner or monitoring loop. Keep one compact private receipt in the existing
`nov14-final-primary-reconciliation/` directory, including actual completion or
refusal. No build, provider/native-client query, environment/memory/log read,
process control or test is part of this package.

1. Before and after, bind the original boot
   `8f3d3e6c-c527-42bd-aad9-bd1ef3fd7c3d`, native PID1309145/start75094898/UID1000,
   retained actual executable identity and registered 2rq/native0.165.0 pin, and
   socket target epoch
   `8f3d3e6c-c527-42bd-aad9-bd1ef3fd7c3d:64769:18744292:1794148953:681548376`.
   Read only relevant proc mount/namespace identity metadata to establish that
   the reader's procfs covers the native daemon's local PID domain. A different
   namespace, hidden/subset mount, inaccessible owner entries or other uncovered
   visibility boundary makes the result incomplete; do not elevate or broaden.
2. Enumerate numeric proc entries across that domain, not just current daemon
   descendants. Read minimal UID/stat/comm for classification and discard
   other-UID data. Include every UID1000 `gh` and possible command-carrying shell
   (`sh/bash/dash/ash/zsh/ksh/fish/nu`, including truncated/name variants), plus
   plausible per-invocation shell/backend wrappers. An unclassified UID1000
   entry potentially overlapping the original launch interval is a candidate,
   not silently excluded. Current PPID, cwd or cgroup never alone excludes a
   candidate: reparenting and changed cwd must not defeat coverage.
3. Read candidate argv/cwd/executable and identity/start/cgroup metadata only.
   Match gh argv to `gh run watch 43528601963 --repo vpsfreecz/vpsadmin --exit-status`;
   for shells inspect the `-c`/login-command payload, allowing the already known
   native shell-snapshot wrapping. No arbitrary substring match establishes
   ownership. Preserve exact matching/ambiguous candidate metadata privately;
   suppress unrelated command text. Original tracking cwd and launch interval
   `2026-11-13T23:43:37.616Z–23:44:07.872Z` corroborate attribution, not sole
   exclusions; record clock/tick uncertainty rather than narrow it away. Numeric
   99295 is only a logical handle. A shared local executor need not exit, but an
   unexplained per-command wrapper or pending-dispatch possibility keeps the
   result incomplete. The already returned running-gh result and completed outer
   cells distinguish this invocation from an unsubmitted command.
4. Read PID/start identity around candidate reads and close with another proc
   inventory within the same bound. Inspect newly appearing possible candidates;
   do not misattribute PID reuse. Record disappeared entries, read errors and
   coverage exclusions. A live match, unresolved identity change, inaccessible
   possible candidate, continuing churn or timeout stops as held/incomplete.
   No retry, kill, wait, resume or follow-up provider action. An entry vanishing
   is not by itself proof of quiescence; acceptance requires complete closing
   coverage and no remaining candidate capable of continuing this invocation.

Root may combine a complete candidate-free current-domain receipt with the
retained211 terminal outer cells, 31 other terminal native handles and original
utility completion/notLoaded, then apply normal exact-owner/launch/delivery/native
queue/submission resolution guards. None alone suffices. The result can establish
current local quiescence only: original exit remains unknown, immutable
`INCOMPLETE` is preserved, and no remote CI conclusion is inferred. Root alone
decides any later supported resolution/readback. a8 stays held pending actual
combined evidence; 3b and b5 are resolved per the current lead update. Earlier
assessments below retain their historical evidence limits.

#### Current-effects accounting boundary (2026-11-14)

**Separate b5 retained-evidence assessment: remote completion proved; local
accounting gap remains.** Operation `b5c332f4-b21a-458b-b40a-cd2d56e0e5be` has
an immutable `INCOMPLETE` report in
[retained status](nov14-ack-loss-evidence/managed-durable-terminal-status.json),
with `stillRunning` explicitly naming remote run43539527454/job132276549208.
Later `ci-parent-observation/kb-fixed-managed/checkpoint-4-{run,jobs}.json`
bind repository vpsfreecz/vpsfree-kb-contracts, workflow336079991, attempt1 and
headedf5c326d253e750ad84ca61994ff3275ba4744c to completed/success; the sole job
completed at01:54:59Z with test/evaluation/summary/cleanup/runner steps successful.
`complete.log` SHA256 `a6895b80ce6a05ef6a05144ce6ecf8ad58a778265b1e20620a58ef9b0aaf1a40`
confirms checkout at lines92/115 and run-specific state removal at742.
The inspected watcher status/observe receipts and existing coverage summary
contain no producer call/result, returned-cell and native-handle terminal inventory;
the report's “calls finished and joined” statement and native idle are not that
proof. No local call/handle count is established by these records. Resolution is
not supported by this assessment alone. The smallest next retrieval for root
assessment is a separately authorized exact persisted receipt check for utility
`01a1d7b8-936c-7450-984b-0101d6b775d4`, turn
`01a1d7b8-9c35-7c61-9443-b97424e91b08`, using the already validated unique-suffix/
nofollow/metadata/turn/stability route and accounting through late producer
receipts, including reporting calls. No raw history was opened here; no new
provider/native/process query or resolution occurred. Preserve `INCOMPLETE`;
eventual queue/submission guards remain root-owned. This is independent of a8.

**Bounded investigation complete; a8 remains held. No OS observation route is
released.** Earlier M2 preparation/alias statements saying held or unexecuted are
historical: root reports the reviewed successor ran once at `11:39:19Z`, exit2,
`notLoaded`, pages0, `ListComplete=false`. It supplies no completion evidence.
3b remains resolved; immutable a8 `INCOMPLETE` and the unknown original exit remain.

The original exit receipt was a sufficient proof route, **not an exclusive
requirement of the installed resolution contract**. In immutable runtime source
`/nix/store/882d9278smpacf3czxzc0wliggx03a9f-source`, monitoroperation
`service.go:266–325` stores immutable lead evidence after `CheckResolution`;
`lifecycle.go:66–88,91–127` retains exact launch/submission and native-quiescence
guards. `portal/cmd/workspace-portal/monitor.go:307` wires that check to
`ProveQuiescent`. Installed monitor skill lines67–74 require “native quiescence
and receipt proof”, accounting for “the source command and every known
operation-owned code cell or tool session”, and keeping known uncertainty fenced.
Lines83–86 explicitly exclude complete cell/tool inventory from automated checks.
Complete current-effects accounting could therefore be relevant while preserving
the unknown historical exit; no clause makes empty process search, idle turn or
CI success sufficient. This corrects the earlier exclusive-receipt interpretation,
not the evidence requirement or the current refusal.

**Concrete missing proof: original execution backend/domain.** Retained
`backend-monitor-native-terminal-status.json` records Luna/low, full-access/never
and thread policy, but no resolved execution environment/backend. Exact utility
metadata/turn contexts at lines1/15/875 likewise record native0.165.0, local-looking
cwd and full-access policy without environment/backend/shell-snapshot selection;
launch49 supplies command/cwd/yield/output bounds only. Retained immutable native
`exec_command.rs:253–281,400–409` passes the resolved turn environment;
`process_manager.rs:1369–1398` uses `environment.get_exec_backend()` for remote
environments **or** an exec-server shell snapshot, otherwise reaching local
spawn at1459–1473. The retained evidence does not select that branch or establish
the original PID namespace/execution domain. `99295` remains a logical handle.
A host-local cwd/policy/socket does not fill this gap; no further config/source
discovery or process scan was undertaken.

**Returned code cells are terminal, not merely paired.** Rechecked only the exact
accounted file, unchanged SHA `b0f17f74…`, 2,674,739 bytes/1078 complete lines,
matching nofollow metadata and original turn. All211 original `exec` calls have
later matching results whose first producer block says `Script completed`;
zero missing, orphan, nonterminal or misordered results. No `functions.wait` or
yielded outer cell is present. Under the exposed completed-script lifetime
contract these returned cells cannot later resume/spawn; this does not terminate
already launched nested work. The retained32 launches/31 terminal handles leave
only known nested session99295 unresolved. Current native queue/submission
quiescence still requires the runtime's own guards; it was not queried here.

The next necessary input is authoritative original resolved backend/domain
binding, including shell-snapshot routing where applicable, and enough continuity
to bound any later observation to that complete domain. Only then could root
assess a separately authorized metadata-only route covering reparented descendants,
visibility exclusions and outstanding submissions. Absent that input, no concrete
owner-domain command can be justified. A found live original process retains the
fence; PID absence alone cannot clear it. No resolution, process/native/provider
query, continuation, control or lifecycle action is authorized by this note.

#### M2-PASSIVE — sufficient preparation brief (2026-11-14)

##### Registered socket alias correction (2026-11-14)

**Current narrow owner0 package; live invocation remains held.** Root's preflight
found the normal registered socket is a symlink before executing any binary.
Change only `os.Lstat(socket)` to `os.Stat(socket)` in `socketIdentity`; keep the
registered path, socket-type check, target device/inode comparison and every
metadata/read/candidate/output guard unchanged. This supersedes only the frozen
main hash in the reviewed preparation baseline below. Delivered main `4c5f02d0…`,
private client `924f8225…` and reviewed unexecuted binary `af1a…` remain retained.

Concrete installed contract: immutable runtime source
`/nix/store/882d9278smpacf3czxzc0wliggx03a9f-source/portal/internal/session/recovery.go:222–234`
uses `unix.Stat(path)`, requires `S_IFSOCK`, and forms the owner epoch from boot ID
and the **target** device/inode/ctime. `monitoroperation/authority.go:84–88` uses
that helper for the registered endpoint. Following the declared alias therefore
matches ordinary owner authentication; pinning a different pathname is unnecessary.
Root reports the target is uid1000/mode0600 and matches retained a8 epoch
`8f3d3e6c-c527-42bd-aad9-bd1ef3fd7c3d:64769:18744292:1794148953:681548376`.
Root must freshly verify that full epoch and exact owner tuple before the read;
driver before/after stamps continue to compare target device/inode. These checks
are not atomic endpoint-generation or historical-manager continuity proof.

Owner0 copies the reviewed private main to
`nov14-final-primary-reconciliation/m2-passive-prepared/main-socket-alias.go`,
applies the one-line change, and builds a new `m2-read-socket-alias` beside the
retained baseline using the same offline Go1.26.6/private module inputs/cache.
Record the one-line diff, new source/binary hashes and actual check results in the
existing preparation receipt. No client, installed input, protocol, flags or
candidate-authority changes. Focused checks use disposable socket nodes only:
`Stat` plus `socketFields` gives equal stamps through a symlink and its target;
retargeting that alias to a different socket makes `finishSocket` report
`changed/socket-identity` with `ListComplete=false`. Retain ordinary missing/non-socket
refusal controls. No native server fixture or new test framework is needed.

After quick checks, reviewer0 assesses only the changed alias guard and its
evidence against the retained cleared baseline; root then owns fresh preflight
and release of the same single bounded read. Reuse the already verified registered
native link `/home/aither/.local/state/dev-workspaces/codex/current` and installed
0.165.0 pin evidence above/below, not a guessed CodexHome-relative path. No live
attempt has occurred. A refusal stops; no automatic retry or mutation follows.
Candidate/absence remains metadata only, `EffectsProof=false`; a8 stays held and
3b stays resolved. No migration, deployment or recovery-contract change.

The following preparation specification is the reviewed baseline, with only the
socket-alias correction above pending implementation and affected-risk review.

**Source contract settled; owner0 preparation package ready for lead release.
Live execution remains held for independent reviewer0 assessment and root release.**
Use the existing [delivered recipe](nov14-final-primary-reconciliation/m2-passive-delivered/peer-build-native-contract.md)
and [five-file public source receipt](nov14-final-primary-reconciliation/m2-passive-delivered/native-source/source-receipt.json).
No further source inventory or peer packet is required. Earlier assessments below
retain their then-unresolved dependencies; this brief settles the native-handler
and portable-input contract without claiming a built or tested artifact.

At public commit `360319d8dee62d87e2d59fc0c21805d79519cfed`, inspected
`thread.rs:1243–1277`, `thread_processor.rs:1019–1033,2558–2586,6842–6867`,
`process_manager.rs:1262–1269,1876–1893`, `delegate.rs:323` and
`exec_command.rs:176–182,243,279–282,400–404` establish the supplied types and
existing-loaded-thread list path: `load_thread` uses `get_thread` or errors;
the handler lists/maps/paginates without resume, start, subscription or process
control. The producer locks and reads the process map, filters exited entries,
sorts numeric process IDs and returns stored inner-call ID, handle, hook command
and cwd. Hook command is `args.cmd`, separate from shell argv. The outer call ID
is therefore provenance only. Filtering exited entries is not a terminal join.

Own installed runtime and registered `codex/current` both select
`2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0`, backed by `94pabr…`.
Its retained derivation `c1ql1zd4…` declares native 0.165.0 and source derivation
`l0x81jkc…`, with NAR hash `sha256-b9PpwNQeZsJIN4wbGA3FLfWAKd2EDMN5E/zj/Y62/vk=`.
Recorded patches affect daemon installation/recursion limit, not these handlers.
The original source store output is absent; no rebuild/NAR rehash was attempted.
The supplied tag/commit binding and immutable public file hashes are retained
with that limit. Ambient native 0.167.2 is not an input.

**Owner0 owns one complete private preparation package.** Create a new mode0700
directory `nov14-final-primary-reconciliation/m2-passive-prepared/` under this
session; refuse an existing destination. Keep delivered main/patch/receipts
immutable. Copy main and patch there as mode0600, copy only the exact public dd90
module into `codex-web/`, and apply only the delivered allowlist line to that
copy. Verify the 146-file public manifest and every unchanged file; disclose the
local derivative. Main stays SHA `4c5f02d0…` (12,829 bytes), base client
`c8f0e7a1…`, patched client `924f8225…`; incoming readLoop bytes must stay identical.
Do not require a cosmetic main rewrite or expand this into an installed change.

Set `PUBLIC_RUNTIME=/nix/store/882d9278smpacf3czxzc0wliggx03a9f-source`:
its `portal/go.mod` and `go.sum` were verified byte-hash equal to the recipe's
`05b6de24…` / `9e714fdb…`; its dd90 module sum is
`h1:w7r/pzWLCevSAArjYC6bHOHJ/w6CLTeAbfa66BAESeY=`. Owner0 preflights existing
Go1.26.6/module availability, uses the recipe's private driver.mod/copied sum and
explicit local replace, and builds with `GOPROXY=off GOSUMDB=off GOTOOLCHAIN=local`,
`-mod=readonly`. Keep writable build cache/temp/output private, existing source
and module cache unchanged; stop on missing inputs rather than download/install
or enter mutating shell hooks. No shipped source, pins, Git, runtime or package
changes. Record the actual tool/input paths, whole-copy manifest/diff, main/patch/
client/binary hashes and `go version -m` local-replacement evidence. Binary0700;
private receipts0600. Path-dependent binary hash need not equal the peer binary.

Quick checks are limited to exact input/copy/patch identity, ordinary offline
compile, and focused read-admission/no-answer plus candidate/conflict/empty-list,
bounded-page/guard and exclusive-output controls using the existing small seams.
No live server fixture, generic harness or application tests. Record actual
outcomes; peer tests are not ours. Owner0 hands the complete immutable prepared
artifact and compact receipts to root for retained reviewer0's independent final
assessment. Routine tool availability stays owner0's preflight; no per-command
approval sequence. No live invocation is part of preparation.

**Only potential next live action:** after review/root release, root freshly
verifies a8 session/root/incarnation/project/utility/original turn and registered
socket/native identity, then invokes the reviewed binary once with the exact
recipe flags and a new private exclusive output. The driver retains before/after
socket and metadata guards, loaded original terminal turn, two six-RPC captures,
maximum four 32-row list pages and 30-second request budget. Outcome `candidate`
or exit0 locates current metadata only; mismatch, empty, unloaded, changed,
deadline or error stops without another call. `ListComplete` is traversal only,
`EffectsProof` always false. No result supplies the missing historical 99295
terminal receipt, continuity or effects-resolution authority. a8 remains held;
3b remains resolved. No execution occurred during this source/design package.

**M2-PASSIVE delta assessed; adoption/execution still held.** The delivered
[passive assessment](nov14-final-primary-reconciliation/m2-passive-delivered/passive-assessment.md)
binds revised main SHA256 `4c5f02d0a58c6b8b9ae85b5d2cf5807c548d363f19c67612bc4968f3508b59cb`
and the one-line private-copy allowlist patch. Own installed client hash matches
`c8f0e7a1…`; in-memory patch arithmetic matches expected `924f8225…`, with incoming
readLoop unchanged. ObserverOnly:true closes the client automatic-reply gap while
the added outgoing read is admitted. Outer call ID is now provenance only; the
99295 row retains its observed inner ID as a candidate, with command/cwd mismatch
reported as candidate-conflict. ListComplete never means effects proof, and
EffectsProof stays false. Original source-layer concerns below remain historical;
the corrected client/candidate boundaries supersede those two findings only.
Exact private-copy/build provenance and pinned native existing-loaded-manager /
pure-list handler evidence remain required, followed by proportional quick checks
and root-owned final assessment before any execution release. No copy, patch,
build, native read or installed change occurred; a8 stays held, 3b stays resolved.

**Delivered M2 artifact assessed; execution held.** Source-only
[assessment](nov14-final-primary-reconciliation/m2-delivered/assessment.md)
binds delivered `main.go` SHA256
`d3eaf20c9e65ca25bd1daf4011fcd4927a1691667b6a69a45dc1652cc2c32545`
to our installed dd90 contracts. Construction/Ensure is socket-only; the two
six-RPC captures genuinely use the supplied HistoryReader gate and do not spawn,
subscribe or cold-resume. Two dependencies remain: ordinary-client inbound
unsupported-request replies bypass the gate unless pinned native routing proves
none can arrive, and public background-terminal item/command mapping is unproved
(outer call ID is not established as native item ID). ObserverOnly alone refuses
this list method. Exact guards, bounded pagination, socket checks and exclusive
private output are assessed with their race/receipt limits. Every result retains
`EffectsProof=false`: a positive can locate a proven tuple; a negative is not
terminal proof. No build/test/native/provider invocation or source alteration
occurred. Peer build contract remains supplied evidence; lead owns further
acceptance/review. a8 stays held and 3b stays resolved.

**Exact owner-local receipt check completed; `99295` remains unresolved.**
The newly authorized check used the validated registered-home suffix/nofollow
route only for utility `01a1d74b-2c77-79a1-984f-0c5f7ada0667`, original turn
`01a1d74b-3675-76e0-b039-354de57a1c2e`. Metadata, cwd/workspace roots and turn
binding match the lead's fresh owner status. The unique stable file contains
2,674,739 bytes and 1,078 complete JSONL lines, SHA256
`b0f17f74b6fcd2d60ad3e92277e5b8d072957602bbdd392fa63f97e40f183911`.
Private [a8 accounting](nov14-final-primary-reconciliation/monitor-a8-persisted-accounting.json)
retains decisive line hashes and the 31 terminal-handle summary, without raw
prompts or a full per-call transcript inventory.

Launch `call_78784388a337495bb0a86a631d6184ab` at lines 49/51 ran
`gh run watch 43528601963 --repo vpsfreecz/vpsadmin --exit-status` and printed
the actual returned `session_id=99295`, exit undefined. Its 166 retained
`write_stdin` calls culminate in `call_956cec0a3fbe4a5686409edf113991bd` at
lines 1042/1044: the producer result at `01:22:48.846Z` still contains
`session_id:99295`, with no exit code. No terminal native item for `99295`
appears through `task_complete` at line 1078/EOF, and there are no later records.

All 211 outer scripts have paired `Script completed` results; none yielded an
outer cell or used `functions.wait`. Of 32 native command launches, the other
31 have terminal receipts (28 exit 0, three exit 1). The other returned session,
`1289`, has its terminal exit-0 producer receipt at line 460. Outer-script
completion does not complete the still-returned nested session `99295`.

This evidence **does not support effects resolution**. Preserve the original
terminal `INCOMPLETE` and its still-running claim; present process liveness and
remote CI outcome are not inferred. The specific dependency is the original
authoritative terminal producer receipt for `99295`; any supported retrieval
capable of returning that receipt would suffice. The exposed `write_stdin`
schema does not establish a same-thread or original-caller restriction.
After independently verifying the retained accounting, root made one ordinary
empty poll of the verified owned handle, with no input or signal. It immediately
returned `write_stdin failed: Unknown process id 99295`; see the private
[empty-wait refusal](nov14-final-primary-reconciliation/root-empty-wait-receipt.json).
That refusal supplies no terminal producer proof, so the ordinary root poll
could not close the gap. No retry, resume, provider query, effects resolution,
cancel or lifecycle action followed. `a8` remains held; `3b57` remains resolved
and was not reopened. This exact-file package is finished. Earlier evidence follows.

The original `a8c49117-6d98-4afd-9b5d-15afe4132919` operation subsequently
reported terminal `incomplete`, retaining primary CI run `43528601963` attempt 1
and executor watch session `99295`. Its [native status](backend-monitor-native-terminal-status.json)
authenticates the original utility/turn and records `termination=completed`,
`terminatedAt=2026-11-14T01:23:38.249977592Z`; the historical launch state remains
`running`. [Thread observation](backend-monitor-native-thread-observe.json)
proves exact utility/cwd, `activityKnown=true`, `idle=true`, no blockers.
These prove native turn termination/idleness, not executor-session completion.

Installed `NativeDelivery.ObserveUtility` authenticates the original project,
thread and receipt turn before recording termination. Public thread observation
also checks prompts, queues and known submissions, but neither interface provides
a cell/tool-session inventory. Root's missing executor handle and absence of an
exact matching OS `gh run watch` process do not supply the missing native result.
Portal history routes select only the retained lead or roster members. A bounded
probe through the installed public `codex app-server proxy --sock` returned no
native history receipt on the exact retained socket; the probe exited 0 and its
separate read-only proxy session `39978` exited 0 after stdin EOF. No continuation,
provider query, private state inspection or new interface was used.

No usable supported exact-utility receipt path was established within this
bounded investigation. Remaining evidence needed: the authoritative final result
for `99295` from its original owning executor context (or its supported native
receipt reader). Any owner-context continuation is outside this read-only package.
Preserve the original incomplete report and effects fence; do not equate model
text, idle status or a missing root-local handle with a completed command. Sole
parent takeover has not been certified by this evidence. Lead owns further
recovery coordination; API failure diagnosis remains owner0's independent work.
