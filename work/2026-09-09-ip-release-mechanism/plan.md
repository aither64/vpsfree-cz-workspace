# Admin-managed IP release campaigns

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
- Edits send no email. Initial notices and explicit updated notices only.
  No mail delivery checks, delayed submission logic, reminders or result email.
- Assigned addresses always remain protected, including stopped VPSes and
  export interfaces. Assignment is evaluated at each release action.

## Repositories and scope

- vpsadmin: additive core schema/models, API, transaction chains, WebUI,
  translations, built-in notifications, and focused/integration tests.
- vpsfree-notification-templates: Czech and English initial/update notices.
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
update notice actions, whole-campaign release, add/remove IP exemption.
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

Add ip_release_requested and ip_release_updated registry/built-in English
mail templates and matching CS/EN overlay templates. Include affected prefixes,
response date/timezone, current policy and authenticated request URL. Do not
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
   claims, closure, snapshots and manual initial/update mail without delivery
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
