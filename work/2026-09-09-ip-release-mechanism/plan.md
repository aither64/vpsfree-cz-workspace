# IP release mechanism

## Goal and scope

Propose an admin-managed mechanism to recover user-owned IP allocations that
are not assigned to an interface. Notify each user, normally allow seven days
to respond, and release remaining eligible allocations after the deadline.
Users can retain individual allocations by assigning them to a VPS or
submitting a reason in the WebUI. Admins can disable the reason-based opt-out.

This is an implementation proposal, not an approved operational campaign.
No project code, production data, or notification templates are changed.

## Affected repositories

- `vpsadmin`: additive schema/models, API, transaction chains, scheduled
  processing, WebUI, translations, built-in notification types/templates, tests.
- `vpsfree-notification-templates`: Czech and English email variants. Use this
  current repository, not the older `vpsfree-mail-templates` repository.
- `vpsfree-kb-contracts`: assess final WebUI documentation impact and update
  affected contracts, pages, and screenshots during implementation.
- `vpsfree-cz-configuration`: eventual deployment pins and worker activation.
- No planned HaveAPI, vpsAdminOS, node protocol, CLI, or Terraform changes.
  Generated client exposure of the new resources can be considered separately.

## Source findings

Inspected fetched vpsAdmin origin/master at
`19971f039771500d5d0304610f91fe6f4af5fed3` and notification templates at
`9e1ddbd973703cf48a43f0e5afc2bfb392a8b676` on 2026-09-09.

- `api/models/ip_address.rb`: ownership is `user_id`; assignment is
  `network_interface_id`. `free?` means no interface, not unowned. An IpAddress
  represents an allocation/prefix, possibly containing multiple HostIpAddresses.
- `api/lib/vpsadmin/api/resources/ip_address.rb`: admins update ownership;
  users can assign owned addresses to their VPS interfaces. Existing filters
  include version, role, purpose, network, location, and assignment.
- `api/models/transaction_chains/ip/update.rb`: ownership changes adjust resource
  allocation using `size` and `charged_environment`, and removing ownership
  cleans reverse DNS and user-created host addresses. Reuse this behavior.
- `api/models/transaction_chains/network_interface/add_route.rb` and
  `network_interface/cleanup_host_ip_addresses.rb`: resource locks participate
  in asynchronous assignment and cleanup. Acquire the IP lock before deciding
  release eligibility; an earlier listing is not authoritative.
- `api/models/network_interface.rb`: an interface can belong to an export too.
  Exclude every assigned interface, not only interfaces attached to a VPS.
- `api/models/transaction_chain.rb#mail` links MailLog to a specific mail
  transaction. `Transactions::Mail::Send` uses the mail queue and keep-going
  behavior. A queued mail or finished containing chain does not prove that
  this particular SMTP submission succeeded.
- `TransactionChains::SecurityAdvisories::Mail` demonstrates per-user mail with
  a WebUI link. Its filtering of users with disabled mail must not silently
  make unnotified IPs eligible for release.
- Notification overlays are reconciled before API startup. New template types
  require compatible registration in vpsAdmin and coordinated template rollout.

## Proposed persistent model

Use three tables with distinct responsibilities. Names are proposals.

| Model | Purpose and principal fields |
| --- | --- |
| `IpReleaseCampaign` | Admin batch: label, explanation, creator, grace period (seven days by default), `allow_keep` (true by default), draft/active/finished/cancelled state, timestamps. |
| `IpReleaseRequest` | One user notice per campaign: owner, announced deadline, notice revision, mail log/transaction reference, queued/submitted timestamps, notification error, completion/cancellation timestamps. |
| `IpReleaseRequestAddress` | One selected allocation: request, IP ID, address/prefix snapshot, expected owner, outcome, keep reason/actor/time, release chain reference, processing error. |

Snapshot the actual selection when starting a campaign. Filters are useful for
preview and audit, but never rerun them at expiry to select unannounced IPs.
Default selection is owned, unassigned public IPv4 suitable for VPS use;
allow filtering by user, network, and location. The data model supports IPv6
prefixes too. Preview both allocation count and actual IPv4 units.

Enforce one request per campaign/user and at most one active request per IP in
the database, not just model validation. A MariaDB-compatible option for the
latter is a unique nullable active-IP reference cleared at terminal outcomes,
separate from the historical reference. Index deadlines and pending items.

Outcomes distinguish pending, kept by reason, retained because assigned,
released, skipped because owner/identity changed, and cancelled. Track release
in progress and processing errors without presenting them as successful release.
Use existing audit/versioning for actor changes and notice revisions. Retain
historical snapshots and mail references after reassignment or record removal;
do not cascade away completed requests when an allocation disappears.

## Flow and permissions

1. Admin creates a draft, previews exact recipients/IPs/email, and starts it.
   Revalidate addresses that may have changed since preview. Persist requests,
   selection snapshots, and outgoing mail references transactionally.
2. Each user receives one email listing their allocations, recovery explanation,
   exact deadline with timezone, and a link to their request in the WebUI.
3. The link opens an authenticated, read-only detail page. Preserve the local
   return path across login. No secret token is needed; authorization depends
   on the logged-in owner, not on knowing the request ID.
4. For each pending IP, show assignment and, when enabled, a keep form requiring
   a nonblank reason (suggested maximum 2,000 characters). One reason can be
   applied to selected IPs, persisting the reason on each selected item.
5. A valid keep submission takes effect immediately without admin approval.
   Users see only their own requests. Enforce this in API queries/actions,
   including nested IDs and bulk input. Mutations use normal CSRF protection.
6. A periodic worker processes due pending items. Admins see outcomes, reasons,
   notification failures, and processing errors; they can cancel pending
   requests/items and extend deadlines with an updated notice.

Proposed API: admin campaign create/list/show/edit-draft/start/cancel;
owner-scoped request list/show and address keep; admin notice retry, deadline
extension, and processing inspection. Users cannot edit the selection, owner,
policy, deadline, or release state and cannot trigger release.

Freeze selection, explanation, and `allow_keep` after activation. New addresses
or stronger policy require a fresh notice. Deadlines may only be extended with
notification. Cancellation does not undo an already committed release.

## Recommended policies

- Default grace is configurable seven days. Persist UTC; display the exact
  localized date/time/zone, not only a relative number of days.
- `allow_keep = false` disables reason-based retention in both UI and API.
  Assignment still protects the IP. This mode does not detach VPS addresses,
  bypass notification, or override resource locks.
- A reason exempts selected IPs from this request, not every future campaign.
  Show past reasons to admins preparing a later campaign.
- Assignment protects an IP if it is still assigned at release time. Briefly
  attaching and detaching it does not permanently satisfy the request. Show
  assignment live and record retained-as-assigned when finalizing at expiry.
- A stopped VPS still uses its allocation; network traffic is not a criterion.
- In-flight assignment defers release until its outcome is known. Changed
  ownership or deleted/recreated allocation records invalidate the old item.
- Keep must commit before the deadline and before release. Serialize the keep
  action, cancellation, and release decision. Reject new opt-outs after the
  deadline even if the worker runs late; honor all previously accepted opt-outs.

## Notification reliability and templates

Use per-user deadlines and separate notification state so one failed recipient
can remain blocked while other requests proceed. No automatic release if the
initial notice was suppressed, missing, failed, or remains queued. Verify the
specific mail transaction's successful SMTP submission; this is not evidence
of inbox delivery or reading.

The email needs an absolute deadline known at render time. Allow a bounded mail
queue delay when choosing it, then verify successful submission still leaves
the configured full grace period. If mail arrives too late at the SMTP relay,
block release and send a revised notice with a later deadline. Only the current
successfully submitted revision authorizes release. Never silently change the
deadline behind the user's email. Disabled mail needs admin attention, not an
unnotified countdown.

Use unique notice revisions and durable MailLog references to avoid duplicate
queueing on retry. SMTP itself can duplicate a message after an ambiguous
failure; retries for one revision must preserve its deadline and IP set.

Add `ip_release_requested` and `ip_release_completed` to the vpsAdmin registry,
built-in English templates, and Czech/English notification overlay. The request
email explains whether reasons are allowed; assignment remains an option in
both modes. Completion mail summarizes actual released/retained outcomes once
processing settles. Keep failures visible to admins. Deadline extensions can
reuse the request template with explicit revision context. Reminders are an
optional follow-up and never restart the deadline.

Stable template variables: user, request ID/URL, allocation snapshots,
explanation, exact deadline, `allow_keep`, and outcomes. Apply the workspace
user-facing writing skill directly before committing real mail/UI copy,
including informal singular Czech and matched semantics in both languages.

## Release operation and concurrency

Add a focused service/transaction chain and periodic API processing through the
existing task/scheduling framework. Database state must survive worker restarts
and downtime. Process bounded batches, isolating errors per IP.

For each item, claim it transactionally, acquire the resource lock used by IP
assignment, reload request/IP, and verify all of the following:

- Current notice succeeded and the active request is due.
- No accepted keep/cancel action has won the race.
- Current allocation identity and owner match the snapshot.
- No interface uses it, including an export interface. Inconsistent host-address
  or routed dependencies block automatic release for inspection.
- No conflicting transaction is active. Transient locks defer processing.

Reuse `TransactionChains::Ip::Update` with a nil owner/environment, preserving
resource accounting and reverse-DNS/host cleanup. The wrapper must lock and
recheck before ownership mutation. Audit interacting assignment/ownership
paths to ensure lock and reload ordering interoperates: a new-worker-only lock
cannot prevent races with other writers.

Persist release state and chain reference atomically with the ownership change.
The existing update changes ownership while constructing the chain; cleanup may
continue asynchronously. Track the distinction, retain allocation resource
locks until cleanup permits reuse, and reconcile completion. Failed cleanup
must retry/recover the existing chain, not subtract quota or disown again.
Handle synchronous empty-chain completion atomically where applicable.

Concurrent workers and restarts must cause one ownership/accounting change.
Broken accounting state or failed cleanup stays visible and blocks completion.

## Compatibility and deployment

Use additive tables/indexes and API resources; preserve IP formats and existing
ownership/quota contracts. Migrations never release addresses. Assume the exact
preceding migration schema; do not add guards for stale disposable test DBs.

Deploy schema and compatible API template registration/built-ins, then overlay
and API/WebUI. Keep campaign activation and expiry disabled until all API
writers implement the required locking behavior and notification/form paths
work. No expiry while incompatible old writers remain during a rolling update.
Existing mail and cleanup transactions should require no vpsAdminOS or node
protocol change and no coordinated OS update of all nodes.

Rollback stops campaigns/expiry, drains or reconciles in-flight release chains,
and retains additive tables/history. Old code may ignore tables but cannot
continue the workflow. Remove new overlay templates before rolling back to a
registry that does not recognize them. After a prolonged pause, reissue notices
when needed. Rolling back code/schema cannot restore already redistributed IPs;
restoration must inspect current ownership.

Follow `vpsfree-kb-contracts/docs/webui-change-workflow.md` during implementation.
Its impact review does not itself authorize production wiki publication.

## Implementation and testing sequence

1. Schema/models, candidate preview, owner-scoped API, retention action,
   notification tracking, and release service with focused specs.
2. Cases: deadline boundaries, blank/long reasons, forced mode, foreign/nested
   IDs, duplicates, cancellation, assigned/stopped VPSes, attach-then-detach,
   exports, ownership changes, and deleted allocations.
3. Real concurrent DB connections: keep/assign/cancel versus release, competing
   workers, and ownership updates. Verify accounting once, PTR cleanup, lock
   lifetime, asynchronous failures, and restart recovery.
4. Mail cases: missing/disabled notices, failed individual transactions, late
   submission, revised deadlines, retries, and rendered CS/EN variants for both
   policies and single/multiple allocations.
5. WebUI browser tests: admin preview/start, login return, reason form, forced
   mode, assignment, and results. Apply documentation impact workflow.
6. Commit implementation with hooks and quick checks, then run the mandatory
   change review at xhigh effort before long integration tests.
7. Run relevant API specs, notification `nix flake check`, and targeted service/
   WebUI integration tests. Update API topic and integration CI selection for
   new files. Prepare deployment pins and activate after compatibility checks.

## Discussion points

Recommended defaults above remain proposals. Main policy choices to confirm
when implementing: whether force only disables reasons (recommended), whether
retention is request-scoped (recommended), and reminder inclusion. No admin
approval queue, permanent exemption scheme, or forced detachment is proposed.
