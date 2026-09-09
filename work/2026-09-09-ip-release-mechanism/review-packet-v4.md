# IP release: remaining scope and focused compatibility review

Root /home/aither/workspace/ai/vpsfree.cz; initiative
2026-09-09-ip-release-mechanism. Read this directory's plan.md, state.md,
review-packet-v3.md, relevant repository AGENTS.md, and the mandatory-change-review
skill plus your lane reference. Review committed files directly; do not edit or
spawn agents. Report evidence-backed Blocking/Important/Advisory findings.

## Immutable inputs

Worktrees: worktrees/2026-09-09-ip-release-mechanism/<repository>.
Vpsadmin base 19971f039771500d5d0304610f91fe6f4af5fed3; HEAD 4d8e9947df69cc8da2dd6fb65dd1bfa358606c66.
Final commits retain three functional boundaries: existing ownership/accounting
prerequisite (including existing WebUI compound removal compatibility), campaign
API/schema/notification registry, and campaign WebUI/browser coverage.
Overlay base 9e1ddbd973703cf48a43f0e5afc2bfb392a8b676; HEAD 420c98c.
KB contract unchanged at 81d6d7dfe530884aff3e1d2634e02e4b12fe28e8; exact
feature pin/check follows the vpsadmin push. No production writes are planned.
Risk HIGH: destructive ownership, persistent accounting, tenant boundaries and
asynchronous cleanup. Review model gpt-5.6-sol, effort xhigh, fresh context.

## Assigned boundaries

The scope reviewer reviews the full final series and affected overlay, including
review-driven growth. This lane has not reviewed the final deferred-cleanup
implementation yet. The v3 packet supplies the complete accepted product
contract, consumers, deployment assumptions and earlier verification evidence.

Architecture and risk reviewers perform a focused review of the new Network
quota-identity restriction and serialization with registration. This is a new
public-contract choice following v3's finding that changing role/IP version
silently reinterprets persisted quota provenance. Relevant code is Network's
preserve_allocation_resource, IpAddress.register, Network#add_ips, the Network
API, network_write_spec and doc/ip-release.md. Review its consumers and concurrent
behavior where needed. This is not a request to repeat the full v3 review or
merely confirm narrow fixes already requested there.

The restriction refuses role/IP version changes while allocations exist;
registration and the validation acquire the same SQL network row lock. We chose
a bounded rejection rather than an allocation/quota conversion framework.
Owned Network.AddAddresses requires user and environment together and validates
availability before rows are created. Owned registration refuses absent charge
provenance. Legacy NULL provenance remains an explicit operator reconciliation
requirement, not a guessed backfill.

## Other v3 remediations, verified directly

- Fresh actor and assignment-policy checks after IP/interface/VPS locks in public
  route and host assignment/removal; shared model validation helpers.
- Exact charged-environment selection and current owner/provenance checks in
  resource freeing, with ownership removed only after cleanup confirmation.
- All NFS ExportHost writers lock their parent IP; active export-client grants
  protect campaign addresses, including otherwise free allocations.
- Existing WebUI disown/removal polls the native ActionState and runs Free only
  after success. Pending/failure keeps the route, links the chain and offers
  explicit resubmission. No worker or automatic campaign retry was introduced.
- Legacy provenance guards in automatic allocation and migration replacement.
- Older failed-attempt bookkeeping cannot replace a newer pending release.
- Fixed 100 cap uses API/PHP constants with a cross-language invariant test.
  Seven-day default remains a documented coordinated API/UI contract.

No mail delivery gate, automatic release, policy freeze, delayed submission,
reminder/result email, general conversion framework, new daemon protocol,
production merge/deploy or generated-client adoption is in scope.
Current policy applies to future attempts; started cleanup is not canceled by
policy changes or Close. Admin may release before deadline or notices. Existing
writer rollout and draining old chains remain explicit operational requirements.

## Current verification

- Focused concurrency/provenance/retry suite: 40 examples, no failures.
- Fresh route/host authorization and Network API: 29 examples, no failures.
- PHP/gettext: 91 tests / 368 assertions, all passed.
- Overlay installed through real MailTemplates.reconcile!, then actual Notify
  rendering: 8 examples, no failures across CS/EN, initial/update and both
  policies. Harness overlay-check.rb; no messages delivered.
- Broader existing writer regression result and final hook results are recorded
  in state.md when this packet's immutable head is filled.
- Previous real API + NodeCtld success/failure/rollback: 3/0; expanded deferred
  API/model suite 120/0/1 existing pending; capacity/concurrency 23/0.
- Long webui#networking-dns VM integration waits for remaining findings to be
  reconciled. Branch pushes/CI and exact KB contract pin/check follow.

Final series: prerequisite 5f606a5edd631f4b8dfe4fe7041eda41d4f26c3d,
campaign API f58216e531baf5eeafcac6f0255beac6d1e7905f, and WebUI head above.
All hooks passed on each rewritten commit. Final tree exactly matches the
verified pre-rewrite remediation tree cd768cb574a87cc6a359401ff40df1bb818c9ef4.
Existing writer regression run is still running; prior focused results above
passed before review. All implementation trees are clean.
