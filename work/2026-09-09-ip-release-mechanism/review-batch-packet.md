# Atomic batch release review packet

Initiative: 2026-09-09-ip-release-mechanism. Plan/state at /home/aither/workspace/ai/vpsfree.cz/work/2026-09-09-ip-release-mechanism.
Review committed code, including the commit series, directly. Do not edit files,
run deployments, or launch nested agents. No screenshots. All four lanes use
fresh gpt-6-astra/xhigh context. Risk: high (destructive ownership changes,
quota, persistent attempts/schema, asynchronous DNS cleanup and admin boundaries).

## Requested outcome and acceptance

See accepted atomic release plan at the start of plan.md. A manual campaign
release shares one transaction chain for the entire eligible batch. This fixes
User resource-lock collisions between per-IP chains. All owners, charge
provenance, quota and released markers remain unchanged until final confirmation;
rollback releases none. All cleanup, including PTR for host addresses, must
complete first. A no-cleanup IP is still deferred in a campaign batch. Ordinary
single-IP disown without cleanup remains immediate.

Persist admin-only attempt membership/history (including failed preparation or
empty batch), report latest outcome and numeric chain links at campaign level,
return the same active attempt on repeated submission. No automatic retries or
time gating. Admin can change policy/close during cleanup without cancelling it.
Reassigned/deleted/protected allocations are excluded; eligible contention aborts
preparation. Members see only their own requests and no attempt internals.

User also wants a fresh dev cluster and campaign1 after verification. Five owned
unassigned addresses with public/private IPv4 and IPv6, two users, PTR and a real
closed VPS assignment history. Old fixture had no VPS assignment, explaining the
empty history (release does not erase assignments). Do not reset during review.

## Repositories and range

- vpsAdmin /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsadmin: base 15ae9175c, head b282bbe779ce6c03981339ab3fa1e557051b8f3d.
  Follow-up delta from previous reviewed/published b76affa12; first six
  prerequisites are unchanged. All handwritten implementation is committed.
- KB contracts /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsfree-kb-contracts: unchanged c4c4ba469becafde34ea058c4333106725b41678.
  Exact pin will be refreshed mechanically to the final vpsAdmin head after it
  is pushed (canonical flake workflow requires that order). Current source
  contract check passes using --vpsadmin-source ../vpsadmin.
- Notification templates /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-09-ip-release-mechanism/vpsfree-notification-templates: unchanged
  f275bf35abc0dc501881b5af78b1e19fb98aec68. No new mail template behavior here.

## Commit boundaries

be803e87b api: add explicit relative cluster resource adjustments
027a1033b api: record the charge environment of owned IP allocations
382498ff6 api: serialize network registration with resource identity changes
d04af1047 api: share IP reservations and revalidate assignment writers
c2a2a1468 api: combine relative IP accounting changes before confirmation
70b672da4 api: retain IP ownership until address cleanup succeeds
40794b31a api: share batch IP disowning and combine deferred quota changes
cb9c5323a api: add administrator-managed IP release campaigns
c9ae137c8 webui: manage IP release campaigns and user retention
2408a76b8 api specs: avoid collisions in generated IP fixtures
b282bbe77 webui tests: account for owned export pool addresses

New shared Ip::Disown helper has its own commit before campaign code. This is
IP-specific; no new generic ClusterResources contract. Helper consumed by
Ip::Update and campaign Release, delegating existing cleanup, current IP locks,
quota adjustment and transaction confirmations. Campaign API/schema/specs/docs
and engine/integration assertions are one cohesive feature commit. WebUI and
its browser/localization support are separate. Storage export fixture repair
is independent from IP generator fixture repair.

## Key files and contracts

- api/models/transaction_chains/ip/disown.rb, ip/update.rb
- api/models/transaction_chains/ip_release/release.rb
- api/models/ip_release_{campaign,attempt,attempt_address,request_address}.rb
- api/lib/vpsadmin/api/resources/ip_release_campaign.rb
- api/db/migrate/20260909170000_add_ip_release_campaigns.rb and core schema
- webui/forms/ip_release.forms.php, webui/pages/ip_release.php and catalogs
- api/spec/models/ip_release_campaign_spec.rb, ip_release_concurrency_spec.rb,
  transaction_chains/ip/disown_spec.rb, ip_release_api_spec.rb
- libnodectld/spec/nodectld/command_spec.rb actual confirmation engine cases
- tests/suite/tasks/dns-reverse-record-check.nix; tests/suite/webui.nix;
  tests/playwright/webui/specs/networking.spec.cjs
- docs/ip-release.md and docs/ip-locking.md explain invariants, operator
  recovery, ownership/assignment distinction, deploy/rollback restrictions.

Existing transaction engine owns persistent resource reservations and final
SQL confirmations. Campaign saves selected attempt outside the chain savepoint
so a preparation error is retained. Final revalidation uses SQL current locks.
Quota is combined once per owner/recorded environment/resource because deferred
confirmation edits store absolute totals. A fatal or incompletely reconciled
resolved chain keeps the attempt active for operator action.

## Compatibility and bounds

Unmerged campaign migration is rewritten directly, disposable review DB will
reset. No stale-dev-schema guards or legacy branch conversion. Production must
apply charge-provenance prerequisite reconciliation and schema/API rollout in
order as documented. Stop incompatible old API writers before enabling ownership
reservations. Existing daemon transaction protocol is unchanged; no vpsAdminOS
or coordinated node update is introduced. Deploy schema/API before matching UI.
Rollback with pending chains requires completion/recovery first. No production
write, mail to real users, session cleanup, merging or screenshots authorized.

No delayed mail submission/delivery acknowledgements, automatic release/retries,
campaign labels, new cap, or member attempt/history exposure. Keep Notice history
name. Generic resource locking broader changes were already split and reviewed;
focus this delta while checking consumers for concrete regressions.

## Quick verification completed

- API/model broad run: 90 examples, 3 stale assertion failures from code loaded
  before fixes. Focused corrected examples + mail matrix: 4 examples, 0 failures.
  Remaining 87 broad examples passed. No remaining runtime failure identified.
- Independent DB concurrency: 14 examples, 0 failures including simultaneous
  submissions and repeat caller with a previously established RR snapshot.
- Attempt API/auth focused: 2 examples, 0 failures, including other administrator
  getting same active attempt without another user's ActionState reference.
- Migration up/down + membership uniqueness: 2 examples, 0 failures.
- Actual libnodectld engine success/rollback/fatal: 3 examples, 0 failures.
- PHPUnit: 96 tests, 398 assertions. Node syntax, API/gettext health, commit
  hooks, CI selection 16 tests/55 assertions all pass.
- Documentation contract: 45 controls, 36 paths, 35 captures, 3 selectors pass
  against the changed source. No KB page/capture semantic change expected.
- Shared libnodectld gem cache was incomplete; verification used an isolated
  /tmp/ip-release-engine-gems bundle rather than modifying shared cache.
- API specs and migration specs require separate runs (migration harness resets
  DB globally); core schema was dumped with RACK_ENV=test VPSADMIN_PLUGINS=none.

Long integration tests have not started for this change. Plan after review:
focused reverse DNS batch, networking WebUI and storage export tests; push/CI;
reset single/bridge review cluster and recreate untouched campaign1.

Prior CI35126167637 failed only storage-backup-export: owned fixture pool IPs
lacked charge environment/quota, correctly rejected by Export::Create. New
fixture repair retains production validation and handles ownership-clearing
caller. Logs were investigated before accepting a new test run. API Specs
35126167621 passed all topics/coverage on previous head.
