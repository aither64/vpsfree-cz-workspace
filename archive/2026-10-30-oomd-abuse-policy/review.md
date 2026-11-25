# Independent final application review: original ranges

Report received through reviewer0 team reporting on 2026-10-30; preserved by
the lead because reviewer0 remains read-only. Reviewer: retained gpt-6.1-sol /
xhigh, no overrides/fallback/nested reviewers. High risk; all four mandatory
lanes completed: general, architecture/repetition, scope/proportionality,
risk/compatibility. This record preserves findings, evidence and conclusions;
remediations are outside the original reviewed ranges.

**Verdict: one Blocking and two Important findings. Original backend is not
cleared for long integration tests. No additional blockers in frozen legacy UI,
React or site templates. No separate Advisory findings.**

## Exact reviewed ranges and identity

Worktrees under `worktrees/2026-10-30-oomd-abuse-policy/`:

- vpsadmin: `ac10a62f1cb0fc890378ae83cdf18dd0e29f049a..51297de1a05fee60aaba8a31e443abf95675396c`.
  Entire series: `a9e5fe4ff1c7071672c76e7627ff870008eb99a4` backend/support,
  `51297de1a05fee60aaba8a31e443abf95675396c` legacy/support;47files,+2522/-123.
- React: `40653dffed4561dd6086716fd506a7223d3631d7..6fcbbc172277677785b59ec2ee66724c3b1c1bb6`,
  one coherent UI/API-consumer commit;28files,+836/-18.
- Templates: `2cfd218d9152888feea4109f064459078ea9f76e..e8c2c3df4ae57015ff4fba3647b13aa219d0c216`,
  one localized-template commit;11files,+209.

Reviewer verified matching dev-session current from bound tracking cwd, absent
both environment markers and exact trusted thread binding. Initial root-CWD
inference failure resolved before record access. Tracked sources matched packet;
only reported disposable PHPUnit cache remained untracked.

## R1: Blocking, ordinary notification preference bypasses stops

Original backend a9e5fe4, `api/models/vps_oom_policy.rb:69-75,199-207`:
process! prepares IncidentReport::New before dispatch_actions! within one outer
serialized transaction. Members may disable public vps_incident_report through
User::MailTemplateRecipient Update (`api/lib/vpsadmin/api/resources/user.rb:1520-1552`).
send_mail! returns nil (`mail_template.rb:133-134,219-223`), Send has no
transaction, New does not allow empty, and TransactionChain.fire raises empty
(`transaction_chain.rb:99-105`). Every immediate/scheduled pass aborts before
enforcement; a pending stop eventually expires. Invalid ordinary template
preparation has the same coupling.

Required: acknowledge intentional disabled/no-message processing; ordinary-mail
preparation failures must not prevent or roll back enforcement. Preserve dedup
and retry progress. Test actual member preference and injected prep failure,
proving one durable stop chain. If shared New allows empty, inspect/test every
nullable-chain caller, especially API Create state_id. No general transport or
workflow expansion warranted.

## R2: Important, unconfirmed transfer breaks VPS summaries

Original backend, `api/models/vps_oom_summary.rb:64-65`: transfer.done? && find
assigns false for queued/rollbacking/failed/fatal/resolved chains. Safe navigation
chown&.finished_at still calls on false, breaking Show and any Index page that
includes that VPS during ordinary or uncertain transfer.

Required: unconfirmed Chown is nil. Test pending/failed/fatal states and done
successful-chain virtual epoch before scheduler persistence. Narrow guard fix.

## R3: Important, mixed updates evade final validation and audit

Original backend, `transaction_chains/vps/update.rb:7-9,121-123,195-207` and
`sys_config.rb:17-24`: OOM fields mixed with hostname/CPU/etc. validate at prep,
then persist via deferred raw NoOp confirmation after configuration locks end.
Global5/10 -> queue mixed warning8 -> global stop6 validates against inherited
warning5 -> confirmation persists8/6 without revalidation, disabling dispatch.
Raw confirmations also bypass VPS PaperTrail audit.

Required/lead accepted: reject mixed OOM/non-OOM writes before effects; require
isolated synchronous settings updates (both actual UIs already isolate). Test
mixed rejection/no changes or prepared chains, global-limit changes after save,
and audit evidence. Clarify React docs; avoid deferred-validation framework.

## Independent scope/history/migration conclusions

Reviewer compared user scope, selected5/10, accepted email wording, authorization,
plan/contract, diffstats and milestones. Backend, both UIs, overrides/exemption
and truthful mail justify the substantive surface. One action model with existing
scheduler/stop/mail chains is conventional. No new queue/transport, burst rule,
quiet-period latch or node subsystem; declined3/8 did not enter code. Growth is
primarily paired UIs, tests, locales and owning docs. No unsupported expansion.

Every complete log, per-commit ownership and final diff independently inspected;
each supplied base equals merge-base. Backend/legacy split coherent;
React/templates each focused with rationale. ORIGINAL series contain no obsolete
approach, fixup stream, transitional shim, abandoned schema step or repeated
dependency/channel/input/generated-pin stream. Autostart wording is folded.
Origins match packet bases; no local release tag contains these feature heads.
Later remediations/rewrites and fresh remote ancestry remain outside this report.

Exactly one new backend migration20261030180000_add_vps_oom_policy directly
introduces additive VPS/incident/action schema from immediate predecessor;
committed core schema matches. No existence guards/transitional migrations.
Schema rollback removes feature history and is correctly documented unsuitable
while upgraded services/actions remain. Owner provenance: unmerged, unreleased,
undeployed, no external persistence; consistent with local refs/tags. Reviewer
did not inspect production or independently exclude unrecorded deployment.
Only disposable local migration tests used. React: **no migrations**. Templates:
**no migrations**. New acknowledgment column may fold into never-consumed
migration with fresh schema/test proof instead of obsolete intermediate step.

## Cross-project/compatibility and positive findings

Actual daemon/nodectld/supervisor flow traced. Backend pinned vpsAdminOS
8e44a5124439b1f3048ffc56b1717614a5360358 broadcasts after successful stop/restart
and preserves integer-second occurrence. Existing protocol sufficient;
same-second same-action collision documented. Unqualified legacy incidents
cannot retroactively arm actions. Existing VPS Index/Show/Update owns contract;
actual legacy/React consumers use batch summaries, not browser incident counting.
Existing owner scope/admin settings retained; manual incident creation cannot
supply source provenance. Old APIs hide additions. No generated-client or
coordinated all-node prerequisite, new route or BFF capability.

Existing registries/renderer/transactions/Message-ID reused; site renderer
9fc0648 unchanged and React terminology a65a4df retained. Beyond R1-R3, no new
authorization or unsafe rollback finding. Positive source evidence: open-lower
7/30-day windows, new timely event,24h actual-stop cooldown, observe default,
stop-only exemption, VPS serialization, dedup before incident/mail, actual
transaction finished_at plus successful chain proof, no uncertain physical
auto-retry, independent stop/mail progress. SMTP exactly-once not claimed.
Current mode/exemption/limits used at mail attempt, counts remain snapshot.
CS/EN templates condition consequences, retain restart advice, describe autostart
as past effect, retain expansion/incident links and omit policy wording.

## Verification/docs limits and next action

Reviewer ran read-only source/history commands and exact-range diff checks
(passed), no application tests/builds/CI/browser/production actions. Owner
packets report corrected backend16/0,migration2/0,mail1/0 after205example fixture
failures; legacy116/803 plus9/65; React57focused plus16rendered/type/audits;
templates75/373,16render cases/8equivalences/exact-head CI. Original tests do not
cover R1-R3.

Prepared real-node scenario covers daemon-format RabbitMQ events/dedup, actual
stop/autostart, SMTP retry, restart and known data. It does not induce memory
abuse. It and browser flows remain unrun. Physical ownership transfer/epoch with
preserved data is a long-check gap; unit manually completed chains are not
physical transfer proof. Real API, completion/rollback, current-owner history,
cooldown across chown and member/admin workflows need bounded verification.
React fixtures/captures do not certify enforcement. No deployed/usable claim.

Owning docs reviewed: backend oom-abuse-policy.md/index; React API/workflow/
REQ-051/evidence/worklog; templates README; session design/contract/copy/packets.
Feature behavior/rollback appropriately owned, rollout evidence separate. KB
still needs published app pin, committed KB source/check and separate source
review before captures. Two-concept/fourPNG plan/details crop is not certification;
runtime capacity/production KB writes not cleared.

Owners finish fixes; lead verifies narrow changes/tests, consolidates final
history, and requests only affected architecture/risk follow-up for new mail
ack/schema/adjacent caller semantics. Long tests follow corrected clearance.
Merge/deployment remain separately authorized; session remains open.
