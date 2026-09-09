# IP release implementation: review of expanded remediation

Initiative: 2026-09-09-ip-release-mechanism. Root workspace:
/home/aither/workspace/ai/vpsfree.cz. Tracking: work/2026-09-09-ip-release-mechanism/
(plan.md, state.md, this packet). Read repository-local AGENTS.md and the workspace
mandatory-change-review skill and your lane reference. Perform your own review;
do not edit files or spawn agents. Report concrete Blocking/Important/Advisory
findings with file/line evidence and residual test/compatibility risks.

## Immutable series

- vpsadmin worktree: worktrees/2026-09-09-ip-release-mechanism/vpsadmin
  base 19971f039771500d5d0304610f91fe6f4af5fed3
  API 1d6ebc97459bc2e4cb74407c68575e5669a53bd3
  head 3f5e700bf2969ca08bda928b824d8eb3fd14cf7c
- vpsfree-notification-templates in the same worktree group:
  base 9e1ddbd973703cf48a43f0e5afc2bfb392a8b676; head 420c98c
  unchanged since the initial review.
- vpsfree-kb-contracts in the same group, still clean at base
  81d6d7dfe530884aff3e1d2634e02e4b12fe28e8. Exact feature pin pending push.
  Preliminary contract has no drift; kb-impact.md explains crop/navigation impact.

Two focused vpsAdmin commits remain: API/state/behavior/interop writers/tests and
builtin notifications, then WebUI/catalogs/browser fixture/selector integration.
The interoperability changes are bundled with release because parent/child locks
and accounting serialization must be deployed together before destructive use.
No released migrations were rewritten. No dependency or node protocol change.
Trees clean, hooks passed before autosquashing own unpublished fixes.

## Acceptance and boundaries

User explicitly requires an ADMIN MANUAL whole-campaign release action at any
time. Deadline defaults to seven days and is advisory. Do not add delivery
checks, delayed-submission logic, automatic release/retries/reminders/result mail.
Admins can change deadline and allow_keep after notice; current policy governs.
False overrides prior reasons; true restores their effect for unreleased items.
Reasons persist. Users can submit nonblank reasons up to 2,000 characters until
release or closure, including after deadline. Separate reasoned admin exemptions
always protect until removed. All interface assignments (including stopped VPS
and exports) protect. Snapshot membership is fixed; overlapping active claims
are disallowed. Explicit initial and update notices only. No production merge or
deploy is part of this implementation.

## Expanded design since initial reviewed head dbc18632c

- Four additive models/tables: campaign, per-user request, per-IP snapshot/result,
  and append-only notices (event, MailLog, enqueue actor/time). Owner/admin scoped
  Notice.Index and paginated notice-history WebUI page. Users see subject/date/type;
  admin mail-log/actor fields are hidden from ordinary users.
- API campaign cap 100 allocations, paginated candidate action with IpAddress
  model, bounded WebUI preview and explicit page selection. Create/Keep reject
  forms missing a final selection completeness marker. Campaign lists/requests
  and notice history are paginated; each request shows all its <=100 allocations.
- Resource declarations own human labels; exemption-null instructions moved out
  of generic reason metadata. Member Keep avoids constructing admin-only clients.
- HostIpAddress owns parent/child lock-and-reload and shared transfer cleanup.
  Host create/delete, PTR writers, transfer creation, host assignment/removal and
  route-via creation share parent locks and refresh state/actor checks.
  Release uses current locked dependency reads; transfer cleanup precedes owner
  removal and PTR/user-created-host cleanup. Existing node transactions retain
  locks while queued cleanup runs.
- IP quota changes use relative values from current locked reads. Deferred quota
  updates hold existing UserClusterResource chain locks; synchronous relative
  updates acquire that lock for their transaction. IP registration, VPS create,
  clone/chown/migration and route removal were migrated to this shared mode, in
  addition to Ip::Update and AddRoute. Ambiguous absolute/relative calls rejected.
  Pending quota changes cause per-IP release failure and require a later admin
  retry. No campaign worker was introduced.

## Compatibility and ownership

API owns state/authorization; WebUI uses existing HaveAPI discovery and PHP
client; mail overlay consumes the new API notification registry and five existing
object/URL variables. Update all API writers and finish pre-upgrade IP, host/DNS
and quota chains before campaign use. Old queued chains lack the new locks.
Apply additive schema before API/WebUI, install overlay after registry exists.
No coordinated vpsAdminOS/node update needed. On rollback stop campaign actions,
reconcile pending chains, retain tables/history and remove unsupported overlays.
Rollback cannot recover redistributed addresses.

## Verification

- Focused new model/concurrency/host/DNS chain tests: 41 examples, 0 failures.
- Final expanded accounting/model/concurrency/VPS create/update/clone/migrate/
  route tests plus candidate API boundary: 71 examples, 0 failures, 2 existing
  pending contracts (clone keep_snapshots, migration with multiple interfaces).
- New API scope/notice/policy tests passed; corrected paginated candidate test
  passed in final expanded run. Existing HostIpAddress API examples passed in the
  earlier 91-example expanded run; its four failures were then corrected fixture
  and candidate-test issues, recorded in state.md.
- Migration up/down/unique claim and notices: 2 examples, 0 failures separately.
- PHP regression: 88 tests / 356 assertions pass. API locale update/health,
  gettext health, RuboCop and PHP formatter pass; all commit hooks pass.
- Browser script syntax pass. Added scenario covers login-return, incomplete
  selection rejection, member retention escaping, assignment, initial/update
  notices/history, forced policy, exemption and repeat release. Long integration
  intentionally not run before this review.
- Notification overlay nix flake check passed. API topic mapping checks passed.

Risk HIGH (destructive ownership/quota, schema, tenant scope and concurrency).
All reruns use gpt-5.6-sol/xhigh. Risk and architecture reassess shared locking,
accounting and public notice/pagination changes; scope reassesses the expanded
writer boundary; general reassesses new UI/history/pagination and the final series.
Do not merely rubber-stamp the previous findings' fixes.
