# IP release follow-up review packet

Initiative: 2026-09-09-ip-release-mechanism. Tracking plan.md and state.md in
/home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism.
Worktrees root: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism.

## Requested result

Users requested empathetic informational IP release notices, with no request for
an email response and no explanation of manual administrator implementation.
Mention public IPv4 scarcity only when the actual address list includes public
IPv4. Include location labels in parentheses. Provide Czech/English HTML and
text versions and a visible button that opens the authenticated request page.
Replace the unused update notice with manually triggered repeatable reminders.
User explicitly chose reminders only for previously notified users with eligible
addresses under current policy; omit kept/assigned/exempt/exported/released/
releasing/changed allocations and send nothing for an empty list.

Handle users deleted or IPs reassigned between notification and release. Keep
snapshots/history, permanently exclude obsolete allocations with a reason and
free their active claim. Do not affect a new owner's ownership, quota or DNS.
Unset PTR records on default and user-created host IPs, including IPv6.

Prior accepted behavior remains: admins alone release whole campaigns at any
time, including before mail/date; dates advisory; policy/date editable after
mail; no mail checks, automatic release/retries, delayed submission or scheduler.
Current allow_keep policy controls user reasons; independent admin exemptions
always protect. Users assign addresses or submit reasons, not email replies.

## Committed repositories and history

vpsadmin: base 19971f039771500d5d0304610f91fe6f4af5fed3,
head d21a376be6e708b289d4b32f2a0d1760ac3ae295.
Three functional commits: existing writer ownership/accounting prerequisite
664e1e184; campaign API/schema/mail 74172b64d; WebUI/browser d21a376be.
The predecessor feature head 1e2d2d7c9bec10d7eb06feaa2c172d10d9fb7a15 was fully
reviewed in packets v1-v4. Compare that tree to the final head to focus this
follow-up. History now introduces final reminder/exclusion semantics directly,
without a legacy updated-event alias or migration from an abandoned schema.
The rewrite preserved tree 22d953df92b6d358c7d9c368cb76045258db59cf.

vpsfree-notification-templates: base 9e1ddbd973703cf48a43f0e5afc2bfb392a8b676,
head fd58bc05cceb883d41f98c568069dc30a0d6a3eb.
One initial/reminder CS/EN text/HTML template commit. Previous feature head
420c98c51ed3db015a366a5564e2128fc83a91b4 is available for the focused diff.

vpsfree-kb-contracts stays at 9d79ff9d04d9df852898042aecf69b5e4c74567f for now.
After review and vpsadmin push, repin its exact API revision and run contract
checks. No existing managed page or screenshot concerns IP release screens;
this step is mechanical revision metadata if the impact checks remain green.
Preserve nested vpsAdminOS runtime pin 6bdf458fd9105379860234ff33d352e55844f08f.

## Ownership and compatibility

API owns eligibility, lifecycle/IP locking, quota accounting, cleanup and mail
payloads. Notify and member status use the same eligibility criteria; the
release chain rechecks locked current records. It shares the User resource lock
with Lifetimes::Wrapper until deferred cleanup confirms; pending cleanup can
require later manual retry for other allocations of the same user (already the
case for the deferred quota lock). Default PTR cleanup machinery is reused.
Historical original user IDs and nullable current logins in API output avoid
resolving deleted users in the PHP client. Exclusion metadata is in the existing additive unmerged
campaign migration. No existence guards or guessed accounting repairs.

Templates consume IpReleaseRequestAddress.location_label/public_ipv4? and the
existing user/request/campaign/address/webui_url payload. Both repositories
must deploy with the matching registry. Built-in EN fallback is included.
No change to node protocol, OS fleet, CLI implementation, HaveAPI or Terraform.
No merge, production deployment, real recipients, wiki writes or session cleanup
is authorized. Existing deployment audit/writer rollout constraints in
vpsadmin/doc/ip-release.md and plan.md continue to apply.

## Quick verification already passed

- All 9 API resource examples passed, including deleted-owner reads and admin/
  owner authorization (part of initial 53-example pass).
- Final model/concurrency suite: 48 examples, 0 failures. Includes permanent
  exclusion, fresh owner checks, two-connection reassignment and lifecycle lock,
  reminder filtering/current policy, escaped HTML and location/date cases.
- Separate migration suite: 2 examples, 0 failures.
- PHP suite: 91 tests, 368 assertions. Gettext health and generated catalogs pass.
- Localized overlay reconciliation/rendering: 24 examples across two languages,
  two events, two policies and IPv4/IPv6/mixed; all pass with absolute test URLs.
- Expanded API + actual NodeCtld confirmation engine harness: 12 examples, all
  pass across execute success/failure/rollback, host origin and IPv4/IPv6.
- Ruby lint, PHP formatter, Nix syntax, JS syntax, CI selection (16 tests/55
  assertions), notification flake check and all commit hooks pass.
- Saved HTML previews and harnesses under the tracking directory are synthetic
  fixtures only. No mail delivery to real recipients.

Long integration NOT started for this follow-up. Planned after required review:
webui#networking-dns (actual email button/login and reminder list) and
 tasks-dns-reverse-record-check (live authoritative PTR disappears after release).
The DNS test now has a dns tag so the existing IP release selector includes it.

## Review classification

High risk: release safety, persisted exclusion metadata and a cross-project mail
contract. All four lanes apply: general, architecture/repetition, scope/
proportionality, risk/compatibility. Every reviewer uses gpt-5.6-sol/xhigh and
must perform its lane directly without spawning nested agents.

Inspect committed code and applicable AGENTS.md plus the review skill/lane.
Report Blocking/Important/Advisory findings with concrete file/line evidence.
Do not mutate these worktrees or run database-reset tests concurrently. No code
changes are being made by the coordinator while the review runs.
