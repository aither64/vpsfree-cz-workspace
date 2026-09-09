# IP release final implementation review

Root: /home/aither/workspace/ai/vpsfree.cz
Initiative: 2026-09-09-ip-release-mechanism. Read plan.md and state.md in this
directory, repository-local AGENTS.md, the mandatory-change-review skill and your
assigned lane reference. Review the committed series yourself. Do not edit files
or spawn agents. Report evidence-backed Blocking/Important/Advisory findings.

## Immutable inputs and series

All worktrees are under worktrees/2026-09-09-ip-release-mechanism/.

- vpsadmin base 19971f039771500d5d0304610f91fe6f4af5fed3
  - efe60cf3493e5ca784776bfd24ce4d497ef77c06: existing ownership, locking,
    cleanup and accounting prerequisite; independently reviewable/deployable.
  - 9fd2d741b7da8df57b7ffc078b4932a147d4c7bf: additive campaign schema,
    models/API, notification registry, tests and operational documentation.
  - HEAD 5a028e0f9529befc0e849a186b0d10a1a2fd149a: WebUI, catalogs and browser test.
- vpsfree-notification-templates base
  9e1ddbd973703cf48a43f0e5afc2bfb392a8b676; HEAD 420c98c. Localized overlays.
- vpsfree-kb-contracts unchanged at 81d6d7dfe530884aff3e1d2634e02e4b12fe28e8.
  Exact feature pin awaits branch push. Preliminary no-drift assessment is in
  kb-impact.md. No production wiki writes are intended.

All implementation trees are clean. No branches pushed yet. No long integration
test started. Risk HIGH: destructive allocation ownership, persistent schema,
tenant authorization, asynchronous node confirmation and quota concurrency.
All four review lanes apply, using gpt-5.6-sol / xhigh / fresh context.

## User requirements and accepted boundaries

- Admin manual whole-campaign Release is the only release trigger, permitted at
  any time. Deadline defaults to seven days and is advisory, with UI warning.
- No delayed submission handling, delivery checks, automatic releases/retries,
  reminders or release-result mail. Initial and updated notices are explicit.
- Admins may change deadline and allow_keep after sending notices; no implicit
  mail. Current policy governs each release attempt. False overrides stored
  user reasons; true restores their effect for items not yet being released.
- Users submit nonblank reasons up to 2,000 characters, including after the
  deadline, until release starts or campaign closes. Reasons persist. Separate
  reasoned admin exemptions protect regardless of allow_keep.
- Every interface assignment protects, including stopped VPS/export interfaces.
  Snapshot owner/allocation membership is fixed; one active campaign claim/IP.
- Maximum 100 allocations/campaign; paginated discovery/lists, final form marker
  rejects PHP-truncated selections. This is a bounded first version.
- Owner-scoped notice history is retained as the record of what was sent when
  admins subsequently edit policy. Bounded query fan-out and finite literal
  status values are accepted residual maintenance choices.
- No production merge/deploy, node protocol/OS upgrade, generated Go client or
  Terraform/Ruby client feature adoption is required.

## Final design and changes since v2 review

API owns campaign/request/address/append-only notice tables, authorization,
selection, current policy and per-item results. WebUI uses HaveAPI discovery and
the existing PHP client. The overlay consumes the API notification registry.
Campaign parent locks serialize policy/close/reasons/exemptions/release decisions.
Each item is attempted independently; failures do not undo other items. Manual
retry is idempotent. Original owners, address identity, actors and chain remain
auditable after ownership changes.

The existing IP writer prerequisite now locks/reloads parent allocations and
host addresses through node-chain completion; it centralizes DNS transfer cleanup
and current relative quota updates. It covers registration, Network#add_ips,
Ip::Update, host/PTR/transfer creation/deletion, bulk DNS deletion, routes,
VPS creation/clone/chown/migration/swap. Migration replacement candidates are
revalidated after locking. Multi-config accounting locks use canonical order.
New owned registration persists the actual charged environment. Legacy NULL
charged_environment causes a per-item error preserving ownership/quota; the
deployment doc requires explicit accounting reconciliation, not guessed backfill.

Crucial v3 change: asynchronous disown retains ownership and quota until the last
successful node confirmation. Ip::Update returns that final Confirmable; the
campaign puts its released actor/time, active-claim removal and result on the
same confirmation. Empty cleanup is immediate. Pending status is releasing.
Failed or rolled-back cleanup leaves owner/quota/claim intact for a later manual
retry. Reasons/exemptions cannot alter an initiated attempt. Policy changes
govern subsequent attempts, and Close does not cancel initiated cleanup. A
pending user quota lock can temporarily fail another item for the same user;
the admin retries after existing work completes. No retry worker is added.

Deferred raw SQL confirmation does not invoke PaperTrail callbacks. Accepted
audit authority is the snapshot/item and its attributed chain, alongside pending
attempt PaperTrail history. released_at identifies the initiating admin attempt;
chain records expose completion time. Do not stamp a premature final audit event.

The independent committed prerequisite was separated following v2 scope/general
commit-clarity concerns. No superseded migration/protocol/history remains.

## Compatibility and deployment

Read vpsadmin/doc/ip-release.md for the exact operational contract. Additive
schema precedes API/WebUI; notification overlays follow registry installation.
All API writers must be updated and pre-upgrade IP/host/DNS/quota chains drained
before use, because older writers/chains lack the locks. Existing IpAddress.Update
disown now completes ownership removal with asynchronous cleanup, using existing
chain metadata/confirmation protocol. No coordinated node update is required.
Old clients can continue existing API operations; WebUI probes new resources.
Rollback stops campaign operations and reconciles pending chains; retain history
tables and remove unsupported overlay registrations. Redistribution is irreversible.

## Quick verification

- Expanded API/model/chain suite: 120 examples, 0 failures, 1 pre-existing pending
  migration-with-multiple-interfaces example. /tmp/ip-release-deferred-checks.log
- Capacity/concurrency: 23 examples, 0 failures; includes 100-allocation managed
  network campaign/repeat, legacy provenance, standalone/bulk DNS deletion locks,
  real-connection quota and stale migration candidates, opposing transfers.
  /tmp/ip-release-capacity-concurrency.log
- Actual API chain + NodeCtld Confirmations/Command.close_chain: 3 examples,
  0 failures for success, execute failure and rollback with DNS/PTR/host cleanup,
  accounting, manual retry and audit. Durable harness confirmation-check.rb in
  this tracking directory; /tmp/ip-release-confirmations.log. It uses a temporary
  composite API/libosctl bundle in the libnodectld Nix shell, not new dependencies.
- PHP: 88 tests / 356 assertions. Gettext/selector: 16 tests / 55 assertions.
- API locale health, root RuboCop/format hooks, migration up/down (2 examples),
  overlay nix flake check and 393-spec exact topic coverage all pass.
- Existing create/clone/route workflows passed earlier expanded suites; see state.
- Browser scenario syntax checked; actual webui#networking-dns VM integration
  waits for this review. Scenario covers notice/login, retention escaping,
  assignment, mutable forced policy, exemption, repeated release and incomplete
  form rejection. Fixture enables local Mailpit delivery and accurate quota.
- KB preliminary checks: 44 controls / 35 paths / 35 concepts / 3 selectors pass.

Review the entire final series and affected existing consumers, not merely prior
findings. Prior review details are evidence in state.md, not a requested verdict.
