# Admin-managed IP release campaigns

## Accepted atomic release and review reset (2026-09-16)

Supersedes per-address release attempts and preservation of current review data.
Prepare one transaction chain per manual campaign release, reserving current
eligible owners, allocations and quota rows in deterministic order. Exclude
changed/deleted/protected allocations; contention on an eligible allocation
aborts preparation of the complete batch. Aggregate deferred accounting by
owner, recorded environment and resource. A shared IP disown helper preserves
ordinary single-IP behavior; campaign batches always defer all ownership,
accounting and release markers to the final successful confirmation. No generic
cluster-resource contract change is needed. Cleanup rollback retains ownership;
fatal chains require operator recovery before retry.

Persist admin-only attempt records and membership, including preparation errors
and empty attempts. Return the existing attempt on repeated submission while it
is active. Show the latest outcome and attempt history in campaign details,
with one transaction-chain link containing its ID per attempt. Remove repeated
per-IP links. Policy changes and closure do not cancel in-flight work. Keep
member isolation and Notice history unchanged.

Extend the unmerged campaign migration directly. Deploy matching schema/API/UI;
there is no legacy review-data conversion. Existing charge-provenance migration
and production reconciliation requirements remain. Separate the batch helper,
campaign changes, and storage-export fixture correction into reviewable commits.
Update owning developer documentation, API specs, EN/CS copy and KB exact pin.
Run quick checks, all four mandatory review lanes, focused integration and CI.

After quick verification and production review, reset only this initiative's
single/bridge dev cluster while isolated integration checks can continue,
and rebuild at final revisions and recreate the existing private review accounts
and two running VPSes. Leave campaign #1 open, due in seven days, allow_keep=true,
with no notices, reasons, exemptions or attempts. Include five eligible owned
unassigned allocations: user1 gets two public IPv4, IPv6 and private IPv4;
user2 gets one public IPv4. Include a PTR and a real closed VPS-assignment
history produced through normal assignment/unassignment operations. Verify the
final fixtures read-only. Leave cluster and session open. No screenshots,
production writes, integration or archival.

## Accepted selection and member-view refinement (2026-09-15)

Supersedes the earlier label and capacity decisions below. Remove custom campaign
labels from schema/API/UI; administrators use translated headings with numeric
IDs. Members receive only deadline, request/action identity and their own address
status/reasons, without campaign metadata or release-attempt diagnostics.

Use separate navigation and campaign-action sidebars. Initial notices and
reminders depend on actual per-recipient eligibility and prior initial notices;
closed campaigns expose history only. Keep Notice history named as-is. Use a
narrow blank checkbox header, select-all above the table, and a full-width reason
textarea with localized placeholder and accessible label.

Creation supports multi-select versions/networks/locations, optional user ID and
public/private/both access. Defaults: public IPv4 and unrestricted owners,
networks and locations. OR within each filter, AND across filters. Preview and
creation share unassigned/owned/unused eligibility, including host-routing and
NFS export exclusions. Add private access using existing ipv4_private accounting.
Use comma-separated scalar query values for the three multi-value filters,
matching the pinned PHP client’s GET transport.

There is no campaign allocation cap. Expected scale is hundreds; display 500 IPs
per page in previews, campaigns and member requests. Select all matching preview
IDs with exclusions, preserving selection in authenticated per-preview session
state across pages. Changing filters starts a new preview. Keep API creation
atomic and explicit-ID based; new matches never silently expand the selection.
Use existing synchronous API and mail/transaction queues, bounded enumeration,
and no additional worker framework or generic lock changes.

Keep the accepted eight-commit split, amend the unmerged campaign migration and
reset/reseed the disposable review cluster if needed (already authorized).
Deploy matching API/WebUI with refreshed discovery. Update developer docs,
translations and KB contract pin; no screenshots. Verify >100 and multi-page
selections, availability transitions, member response whitelists, private/public
IPv4 and IPv6 quota, stale ownership and cleanup failures. Run quick checks,
mandatory astra/xhigh reviews, integration and current-head CI. Leave session
and review cluster running.

CI exposed an unrelated collision in the shared spec IP generator. Keep its
repair and deterministic regression in a separate ninth, test-only commit. The
eight feature commits retain their boundaries and all production locking code
stays unchanged by this CI repair.

## Earlier accepted WebUI redesign (2026-09-15)

Rework the campaign pages using rendered sidebars, standard tables with
`table_add_category`, read-only summaries and separate action forms. Reserve
perexes for errors and action confirmations. Admin navigation includes Cluster,
campaign list/create, details/edit, initial notices/reminders, release, close,
and Notice history (retain that exact label). Explain closing without initiating
release and that already-running release chains continue.

Use one campaign-wide IP table across owners (up to the existing 100 allocations)
with bulk set/remove administrator exemptions. Add campaign-scoped address and
notice list endpoints and an atomic bulk exemption action; retain the existing
single-address endpoint by delegating to shared validation. Reuse current
campaign/row locking, without generic locking changes. Expose persisted actor IDs,
login and timestamps to admins only; members see the exemption source without
administrator identity. No new schema migration is needed.

Test navigation beginning at Cluster, creation and failed-form redisplay, headers,
bulk selection across users, attribution/privacy, Notice history, policy/closure,
authorization, atomic rejection and release/close concurrency. Apply the writing
skill to EN/CS copy. Fold API changes into commit 7 and WebUI into commit 8; run
quick checks, mandatory review, integrations, CI and KB impact workflow.

The user explicitly permits resetting this initiative's dev cluster and reports
no fixture changes. Recreate it on bridge networking with review accounts,
campaigns and free IPv4/IPv6 allocations; leave it running. Do not archive,
remove worktrees, merge or close the session. API must precede the new UI; refresh
client discovery. Preserve the existing approved mail templates. The user does not want screenshot
deliverables; provide the live WebUI and review instructions instead.

## Accepted follow-up: commit separation, hardening and review cluster

The user approved splitting and hardening the prerequisite, not merely moving
history. Keep accounting unified: add an explicit generic
adjust_resource!(resource, delta:, ...) operation sharing validation/allocation
internals, and preserve the absolute reallocate_resource! contract. Do not
introduce an independent IP accounting implementation.

Rebuild the series on refreshed upstream, preserving the original head for
comparison. Commit boundaries, with matching tests/docs/fixtures, are:
1. Generic relative accounting and non-IP regression coverage.
2. IP charge provenance and owner/environment validation.
3. Populated-network resource identity and registration serialization.
4. Shared IP/host reservation/current-read helpers and writer hardening.
5. IP relative accounting adoption and combined composite-operation deltas.
6. Cleanup before disownership, including existing WebUI completion behavior.
7. Campaign API/schema/notifications and final notification/spec corrections.
8. Campaign WebUI/translations/browser checks and their follow-up fixes.
Consolidate final overlay wording in its template feature commit; refresh the
KB contract pin and verify it against the rewritten feature.

Audit all manual and automatic route/host, export, VPS create/clone/migration/
replacement/swap/chown/delete, resource-free, PTR and grant paths. Helpers must
distinguish current-state entry points from explicitly reserved staged objects,
preserve pending in-memory state, and use ordered parent/host/accounting locks.
Fix demonstrated gaps, including stale export selection and pre-lock internal
route accounting. Aggregate composite IP deltas before confirmations so
multiple interfaces or direct/routed groups cannot overwrite one another.

Test generic CPU/memory/swap/diskspace/IP accounting contracts, quota limits,
overrides, confirmation states and existing consumers (including automatic
disk expansion); use separate DB connections for concurrency and actual node
confirmations/rollback. Every intermediate commit must pass relevant checks.
Run all four mandatory review lanes after quick checks and before long
integration tests. Inspect current-head CI failures before accepting reruns.

After implementation/review/tests, start this initiative's dev cluster with
single topology and bridge networking. The user explicitly authorized this
development deployment and captured test mail; no production deployment or
merge is authorized. Prepare admin plus Czech/English member accounts and
working VPSes, six unassigned public IPv4 and two IPv6 allocations for the
primary member, additional second-owner and assigned controls, and a PTR on a
releasable address. Use real model/API/chain paths and correct provenance/quota.
Create one unsent, opt-out-enabled seven-day campaign with three IPv4 and one
IPv6 allocations, leaving other candidates for manual campaign creation.
Load the final overlay through the supported reconciler and verify actual
WebUI URLs and Mailpit capture. Smoke-test on separate fixtures; preserve the
user's prepared fixtures. Repeat setup must not reset later review decisions.
Hand off URLs, private access details, fixture inventory, suggested review
steps and stable portal. Leave the cluster and session running/open.

Existing campaign policy, manual contention retries, legacy provenance
reconciliation and compatible writer-rollout requirements remain unchanged.
No automatic retry worker, guessed backfill or new daemon protocol.

## Goal and accepted decisions

Implement persistent IP release campaigns with per-user requests and per-IP
retention records in vpsAdmin. This plan supersedes the original automated
release proposal. The user approved implementation after deciding:

- Only an explicit admin action releases IPs; it processes the whole campaign.
- The campaign deadline defaults to seven days and is advisory. Release is
  allowed at any time, including before notification. Early release gets a
  non-blocking UI warning and no API override requirement.
- Users can submit reasons until a release attempt starts or the campaign closes,
  while opt-outs are enabled.
- Deadline and allow_keep are campaign-wide and editable after notification.
- Current policy governs. Disabling opt-outs overrides existing user reasons;
  re-enabling restores their effect for unreleased IPs. Keep the reasons.
- Independent per-IP admin exemptions always prevent release until revoked.
- Edits send no email. Initial notices and repeatable admin reminders only.
  No mail delivery checks, delayed submission logic or result email.
- Assigned addresses always remain protected, including stopped VPSes and
  export interfaces. Assignment is evaluated at each release action.

## Repositories and scope

- vpsadmin: additive core schema/models, API, transaction chains, WebUI,
  translations, built-in notifications, and focused/integration tests.
- vpsfree-notification-templates: Czech and English initial/reminder notices with text and HTML variants.
- vpsfree-kb-contracts: WebUI impact assessment and affected contracts/captures.
- Production configuration/deployment and merge are not part of the requested
  implementation. Prepare reviewable pushed feature branches and validation.
- No planned HaveAPI, vpsAdminOS, node protocol, Go client or Terraform changes.

## Data and API

Four models: IpReleaseCampaign (label, creator, deadline, allow_keep, closed_at),
IpReleaseRequest (campaign/user), IpReleaseRequestNotice (append-only event,
MailLog, enqueue timestamp and actor), IpReleaseRequestAddress (IP identity/prefix/owner snapshot, user
reason, admin exemption, release timestamp/chain and attempt result).

Snapshot IP selection at creation and keep campaign membership fixed. Default
selection is paginated and each campaign is limited to 100 allocations to bound
synchronous work and WebUI input size. Reject incomplete form submissions.
Default selection is owned unassigned public IPv4 suitable for VPS use, filterable by
user, network, location and IP version. Support IPv6 allocation prefixes.
Enforce one request per campaign/user and one active campaign per IP using a
unique nullable active-IP claim separate from historical identity. Release or
close frees the claim. Retain history after IP reassignment or deletion.

Admins: candidate preview, campaign create/index/show/update/close, initial and
reminder actions, whole-campaign release, add/remove IP exemption.
Users: owner-scoped request/index/show and reason submission/update on selected
unreleased items. Required nonblank reasons, maximum 2,000 characters. Require
an admin exemption reason as well. Use standard audit facilities for actors,
policy, reasons, exemption/notification/release/closure timestamps.

Closing ends new notices/reasons/releases, frees outstanding claims, and cannot
undo committed release or cancel cleanup already initiated by an admin. Policy
changes apply to subsequent attempts; initiated cleanup retains its decision. User reasons and admin exemptions are separate from
terminal release state. Show current protection and transaction result live.

## Release and concurrency

For each unreleased item in a manual release, atomically serialize against
campaign edits/close, reasons/exemptions, assignment and other release attempts.
Acquire interoperable IP resource locks, reload, then recheck original owner
and allocation identity, absence of any interface/host routing dependencies or NFS export-client grants,
admin exemption, and user reason when allow_keep is true.

Use TransactionChains::Ip::Update to disown with nil environment and preserve
quota accounting, DNS transfer grants, reverse DNS and host-address cleanup.
Host writers use a shared parent/child lock helper and current locked reads. Record ownership change
and release tracking atomically. For asynchronous cleanup, retain ownership and
quota until a final successful database confirmation; update ownership, quota,
and release tracking together. Failed or rolled-back cleanup preserves ownership
and requires another manual attempt. Preserve resource locks during cleanup. Handle empty-chain completion. Link failed cleanup to the existing
transaction recovery path; do not disown or adjust accounting twice.

Report per-IP results and isolate lock/validation failures. Retry skipped
release decisions only on another admin action. No scheduled campaign worker.
Existing transactions may continue/recover cleanup initiated by an admin.
IP quota writers use relative accounting and respect the existing user-resource
lock while other chains defer quota confirmation; a blocked release is retried
only by another administrator action.

## WebUI and notifications

Add networking campaign management with exact candidate preview, create/edit,
request/IP details, reasons/exemptions, notice history, release results and
manual close. Whole-campaign release has a non-blocking early-deadline warning.
Users reach their request after login through an ordinary link, see current
policy/outcomes, can assign using existing networking flow or retain selected
IPs with a reason. GET never mutates; use existing CSRF and owner scoping.

Add ip_release_requested and ip_release_reminder registry/built-in English
mail templates and matching CS/EN text and HTML overlay templates. Include affected
prefixes with location labels, planned release date/timezone, current policy and
an authenticated request URL/button. Explain cooperation and redistribution,
without asking for a response. Mention public IPv4 scarcity only when present
in the actual recipient address list. Initial notices and reminders include only
currently eligible addresses; reminders require a queued initial notice. Preserve
append-only mail history and send nothing for an empty list. Do not
promise automatic release. Use normal mail queue/logs without gating release.
Apply the workspace writing skill directly to final UI/errors/email prose.

## Compatibility and deployment

Additive tables/indexes and resources; migrations never release IPs. Assume the
exact preceding migration schema. Existing ownership/resource formats and
client contracts remain compatible. New registrations persist their actual charge
environment. Audit legacy owned allocations with NULL charged_environment_id and
reconcile their historical quota before explicitly filling this identity; do not
infer an environment from current network locations. Release reports such rows
individually without changing ownership or quota. Existing assignment/allocation
paths also reject missing charge provenance. Network.AddAddresses requires owner
and charge environment together; role and IP version cannot change while a
network has allocations. Registration and that validation share a SQL row lock.
The existing WebUI disown-and-remove action waits for successful disown completion
before removing the route; pending/failure requires an explicit resubmission.
Freeze role/family updates and new IP registration during writer rollout and
rollback until all writers and old work are consistent. Retain the network
semantic freeze after rollback. Audit existing populated networks against
allocation/accounting history even when charge environment is non-null;
ambiguous history requires reconciliation before release or chown.
The fixed 100-allocation cap and seven-day default are coordinated API/UI
contracts, with a cross-language cap check. No new node transaction wire types or OS
fleet update expected. API writer lock-order changes must be deployed to all
writers before operators use release campaigns. Install compatible API/schema,
WebUI and notification registry/overlay together before feature use.

Rollback: stop admin release operations, reconcile in-flight transaction chains,
keep additive tables/history. Older registry requires removing new overlays.
Code rollback cannot recover already redistributed IPs. No production mutation
is authorized by this implementation request.

## Verification sequence

1. Focused API/model/migration specs: ownership/auth/nested IDs, reason limits,
   forced policy changes/restoration, admin exemption precedence, duplicate
   claims, closure, snapshots and manual initial/reminder mail without delivery
   gates. Check CS/EN rendering and API locale/catalog generation.
2. Release tests: early/unsent/after deadline, stopped/assigned VPS and exports,
   owner changes, deleted IPs, partial failures, retry idempotency, quota once,
   DNS/host cleanup, empty/asynchronous chains and resource-lock lifetime.
3. Real separate-connection concurrency for release versus release, assignment,
   policy, reasons and exemption. Preserve existing allocation lock behavior.
4. Commit focused implementation with installed hooks and quick checks. Run
   mandatory change review in all triggered lanes with gpt-5.6-sol at xhigh.
   Reconcile findings before long integration tests.
5. Browser coverage for admin preview/create/edit/notices/release, login return,
   member reason and assignment on a real stopped VPS, forced policy and
   warnings/results. Wait for node confirmation before checking assignment. Update API
   topic coverage and integration selectors. Follow KB WebUI impact workflow.
6. Notification flake checks and targeted integration/CI. Fetch/rebase before
   pushing. Monitor current-head CI; investigate failures. Record all results
   and outstanding review/deployment work in state; leave session active.

## Follow-up accepted on 2026-09-10

Replace update notices with manual reminders, remove response/manual-release
wording from member notices, and add empathetic bilingual HTML/text content.
Primary network location labels appear in parentheses; fall back to associated
locations or a localized unavailable label. Dynamic HTML content is escaped.

Permanently exclude items when the original user is missing/in a deletion state
or ownership/allocation identity changed. Persist exclusion time/reason and free
its active claim. Preserve snapshots/history and tolerate deleted user references
in API/WebUI. Suspension alone does not exclude an owner. Release acquires the
existing user lifecycle resource lock before fresh owner/IP checks and retains
locks through cleanup. Skipped items must not alter the new owner's quota or DNS.
Retain existing PTR cleanup, adding explicit default-host/IPv6 and node/DNS
regressions for completion, rollback and reassignment.

This branch is unpublished/unmerged. Extend its additive migration directly;
reset disposable test schemas instead of adding compatibility guards. No legacy
updated-event alias is needed. Registry/overlay/API/WebUI deploy together.

## Follow-up: email wording and failed CI investigation

Remove the sentence about previously submitted reasons from requested/reminder
emails in EN/CS and text/HTML, including built-in templates. Preserve current
retention behavior and the remaining assignment/admin-exemption instructions.
Investigate the failed vpsAdmin CI run using logs/artifacts, distinguish fixed
fixture failures from infrastructure failures, and verify affected scenarios.
This follow-up does not change API/schema or deployment compatibility.

When user opt-outs are disabled, omit the entire exemption paragraph. Do not
add support/reply instructions for this mode. Keep the shared VPS-assignment
instructions; describe the unassigned-address reason form only when opt-outs
are enabled. This supersedes the briefly proposed support-reply wording.

## 2026-09-15 follow-up

Use a neutral thank-you closing that does not assume the member will release
addresses. Investigate and fix the API spec failure using its logs and a
deterministic reproducer. Explain commit 664e1e184 by lock type, lifetime,
concrete races, operational cost, and scope beyond locking. Do not silently
rewrite or expand the locking design merely to answer the user's question.
Email/test-only corrections have no schema, runtime or rollout impact.

Review decisions for the rebuilt series (2026-09-15): automatic allocation and
migration replacement may reuse owned IPs only in ownership-enabled destinations
where those addresses are already charged. Explicit assignment retains its
existing cross-environment recharge path. This avoids adding transfer accounting
to the Create/Clone return-value contract and protects later VPS chown/migration.
Legacy charge provenance must be reconciled before account/resource teardown.
Teardown cleanup precedes the final quota/account confirmation in the actual
transaction dependency chain.

## Bulk exemption removal correction

Live browser validation found that haveapi/client 0.29.6 rejects a required
nullable reason before sending the bulk removal request. Current upstream
0.29.8 has the same behavior. The new, unmerged Campaign.Exempt API now uses an
explicit remove boolean (default false); reason is optional at parameter parsing
but a nonblank value is still required by the model when remove is false.
Missing/blank reasons never remove or overwrite an existing exemption.
This stays in the new campaign action and shared batch operation; no generic
client change, dependency release or additional repository is required.

This replaces the briefly deployed bulk reason:null request in the disposable
review cluster. The pre-existing single-address HTTP API continues to accept a
null reason; the WebUI uses the campaign action. Deploy the API before the WebUI
and refresh discovery. A mismatched version rejects removal and retains the
exemption. Persisted state, ownership and locking are unchanged.

## Accepted follow-up: counts, member navigation and mail grammar (2026-09-16)

Render singular/plural requested and reminder messages from the allocations
included in each message, in EN/CS subject, text and HTML. Preserve public IPv4
scarcity conditions, location labels, policy paragraphs and approved tone.
Move page selection into an unlabeled header checkbox with localized tooltip
and accessible name; retain preview-wide selection buttons and 500-row pages.
Members retain access to all of their own requests, including closed requests;
remove their current-request sidebar link and notice history in UI and API.

Admin campaign Index/Show gain total_ip_count, to_release_ip_count and
kept_ip_count. Count snapshot rows, not allocation sizes, using current
protection classification once per response with bounded iteration. Eligible
rows on open campaigns and all releases in progress count as to release.
Assigned, routed, exported, exempted and policy-honored user reasons count as
kept. Changed, released and unresolved closed rows remain in total only.
Explain the non-partition with localized tooltips. Display one IPs column in
the admin list and the same labeled summary in campaign details.

No schema, ownership, release, locking or daemon changes. API fields are
additive; member notice history intentionally becomes admin-only. Deploy API
before WebUI and refresh discovery; reconcile templates after final API start
without resetting existing review data. Keep locking prerequisites and the
independent fixture correction separate when folding feature follow-ups.
Verify API scoping, count states and 501 rows, EN/CS 1/2/5 address rendering,
shrinking reminders, and browser header/sidebar/stats without screenshots.
Run mandatory review before long integrations, monitor final-head CI and
refresh the KB contract pin. Leave the session and review cluster open.

## Compact campaign-list count columns (2026-09-16)

Replace the administrator list's combined IPs cell with Total, Release and
Keep columns (Celkem, Uvolnit, Ponechat), showing right-aligned integer counts
and existing explanatory header tooltips. Use standard table headers and a
seven-column empty row. Details, member lists and API count behavior stay as-is.
Update existing browser assertions; verify both locales, empty/paginated lists
and unchanged details using DOM checks without screenshots. Fold into the WebUI
commit, preserve API/locking patches, refresh the exact KB pin, run the required
review and relevant checks/CI. The live WebUI bind mount needs no API restart or
seed reconciliation for this presentation-only change. Preserve all review data.
