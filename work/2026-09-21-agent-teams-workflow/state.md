---
lifecycle: active
---

# 2026-09-21-agent-teams-workflow

## Status

Phases 0, 1 and 2A are complete. Phase 1 delivered and reviewed the immutable
package-time catalog and site policy. Phase 2A added the bounded option-aware
`codex-web` turn/retry API at `52b8ca6` and the dormant generic
catalog/pin/state/CAS foundation at `729e5e08`. Mandatory Phase 2A review found
one Blocking commit-structure issue and two Important history-validation issues;
the retained implementer resolved all three and the same retained reviewer
accepted every lane. Fresh Luna/low watchers passed focused exact-head tests and
both packaged `nix flake check` suites. Phase 2B.1 dormant creation,
registration, retained-publication and helper contracts are committed at
`abbce9fd` with exact-head focused tests passing. Phase 2B.2 host registration
and forward-only reconciliation is committed at `285e998f`; its exact-head Go
and Ruby suites pass. Phase 2B.3 managed creation is complete at generic head
`6aa9be1`: mandatory high-risk review and every affected rerun are clean,
Chromium acceptance passes, the default package builds, and `nix flake check`
passes. The reviewed `codex-web` feature branch is published; no deployment or
default-branch integration has been performed. Phase 2C.0 durable provenance
dispatch is complete at generic head `bb3de38`: its high-risk Sol/xhigh
General, Architecture/repetition, Scope/proportionality and Risk/compatibility
review findings were fixed before phase consolidation, and final fresh
Luna/low watchers passed the focused Go packages, agent-team creation 12/148,
and workspace host 92/524. It permits four strictly validated recovery windows
while preserving schema-1 and `--no-codex` legacy sessions without migration.
Phase 2C.1 retained members is complete at generic head
`abbbb3e9e58757337902739462d1174691002a3b`. It persists append-only retained
assignment provenance, including immutable requested task names, selection and
catalog provenance, and replacement links. Member operations use strict CAS
`prepare`/`submitting`/`accepted`-or-`unknown` records; unknown native outcomes
block replacement until exact-root observation and reconciliation establish the
result. The portal presents managed-team status read-only. C1 adds no native
portal spawn, dispatch, or team-transition path. Phase 2C.2 managed selection
transitions is complete at generic head
`394884b8c1e62e868625b1911eaca3c2c98a85fe`: it applies pinned-catalog team
changes with public selection CAS, exact request replay, and an exact-root,
turn-bound pending boundary. Its non-sending `ApplyPendingBeforeSend` helper
revalidates the boundary and applies a valid pending transition atomically for
the later C3 managed-send path. It adds neither portal controls, native member
actions nor dispatch; schema-1 and unmanaged sessions retain their legacy path.
Phase 2C.3 managed dispatch and feedback controls are complete at generic head
`0594e3f9c175bdb617a17fddb1dee8cccaec0156`. It adds managed dispatch-ledger
and dual-ledger recovery records, persists the pending transition before a real
send through C2's `ApplyPendingBeforeSend` fence, binds every managed send to
the exact selection identity, and supports same-selection steering without a
selection change. The portal now exposes the corresponding managed-team
controls while retaining restrictions for legacy, unmanaged, recovery, corrupt,
uncertain and otherwise ineligible states. C1–C3 together form the deployed
feedback release candidate. The repaired wrapper was built and selected in the
user profile at `/nix/store/aavh5axl72bv9ivxb85yjyr79rxdp9z0-dev-workspace-0.2.0`;
a fresh managed delegated feedback session `2026-09-22-team-test` was then
created successfully. The user-feedback stage is now open. No approval,
publication or default-branch integration is recorded.

## Next actions

1. Collect the user's feedback from the managed delegated session at
   `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-22-team-test/`.
   The prior failed managed-creation receipt was the sole artifact (no
   manifest, tracking directory, worktree, process, retained state or
   lifecycle journal); after its older-package decoder deadlock was confirmed,
   the user explicitly authorized removal of that exact receipt on 2026-09-22.
2. After that feedback stage, run one mandatory independent consolidated
   Sol/xhigh review across all completed implementation phases. Apply reviewer
   fixes only after that review, following its required reruns; route long or
   uncertain verification to fresh Luna/low watchers.
3. Publish the reviewed generic feature series when authorized, while retaining
   the branch; default-branch integration remains out of scope.

## Deployment preparation

- The authorized aitherdev deployment path is the local-input wrapper at
  `work/2026-09-21-agent-teams-workflow/deployment-wrapper`.
- Its intended exact inputs are `codex-web` `52b8ca6`, generic
  `dev-workspace` `e33344f`, organization extension
  `vpsfree-dev-workspace` `583647dd`, and site workspace `0ccd1101`.
- The local wrapper built successfully and `workspace-host switch --source`
  selected `/nix/store/aavh5axl72bv9ivxb85yjyr79rxdp9z0-dev-workspace-0.2.0`.
  The post-switch router, Codex and portal services are active; `dev-session
  validate` passed with 55 manifests. A fresh delegated managed session was
  created at the feedback URL above. No configuration repository was changed.

## Documentation

- Accepted specification: `tmp/codex-workspace-token-efficient-workflow-v3.md`
- Durable design and authorization decisions: `plan.md`
- Phase 2 runtime-team design: `design-phase2-runtime-teams.md`
- Phase 2A exact dormant state schema: `phase2a-state-schema.md`
- Phase 2A review evidence: `review-packet-phase2a.md` and
  `review-results-phase2a.md`
- Phase 2A verification: `verification-phase2a.md`
- Phase 2B.3 review evidence: `review-packet-phase2b3.md` and
  `review-results-phase2b3.md`
- Phase 2B.3 verification: `verification-phase2b3.md`
- Phase 2C.0 review packet and results: `review-packet-phase2c0.md` and
  `review-results-phase2c0.md`
- Phase 2C.2 focused module-mode check:
  `logs/phase2c2-agentteams-module-mode.log`
- Phase 2C.3 final explicit verification:
  `logs/phase2c3-final-explicit-verify.log`
- Phase 1 mandatory review evidence: `review-packet-phase1.md`
- Phase 1 review findings and decisions: `review-results-phase1.md`
- Phase 1 focused and long verification: `verification-phase1.md`
- Stable portal URL:
  `https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-09-21-agent-teams-workflow/`

## Repositories

- `dev-workspace`: registered at updated `origin/master` base `b52a2363`.
- `vpsfree-dev-workspace`: registered at updated `origin/master` base
  `298a8a42`.
- workspace feature: registered from tracking commit `e55bb318`, which already
  descends from current `origin/master`.
- `codex-web`: Phase 2A option-aware turn/retry API is complete at `52b8ca6`.
- Conditional after deployment proof: `vpsfree-cz-configuration`.

## Commands run

- Read all workspace procedures routed for project selection, session setup,
  lifecycle, documentation, Git/worktrees, verification, deployment and
  commits.
- `dev-session current` reported no current session.
- `dev-session start agent-teams-workflow --no-attach --no-codex --json`
  created slug `2026-09-21-agent-teams-workflow`.
- `dev-session worktree add` registered the generic, organization and workspace
  feature worktrees.
- The generic and organization feature branches were fast-forwarded to their
  current remote default branches before implementation after the designer
  identified newer Codex/Luna/portal commits.

## Results

- Portal/session registration is ready; no Codex thread was created because
  this conversation remains the persistent root lead.
- User-profile deployment and any necessary aitherdev development
  configuration deployment are authorized.
- Aitherdev is the only `dev-workspace` deployment. The user explicitly removed
  rollback and mixed-generation compatibility requirements and confirmed that
  all current sessions are idle and may be stopped, migrated forward and
  restarted. Current-format integrity and crash recovery remain required.
- The first activation of the forward-only host is a one-time operator
  bootstrap because the currently installed pre-2B.2 host still contains its
  old compensation path: verify idleness, quiesce services, select/activate the
  new profile forward, then use the new registration reconciliation. Later
  package switches use the implemented forward-only path.
- Official Codex configuration documents
  `agents.max_concurrent_threads_per_session` as excluding the root. The site
  catalog therefore requires four native child slots: three retained
  specialists and one transient watcher.
- Installed Codex/App Server inspection supports explicit child model/effort,
  fresh context, follow-up turns, thread settings updates and observed child
  identities. The portal cannot itself invoke in-process collaboration tools;
  it will persist selection and observed identity while the root reconciles
  native membership.
- Codex source confirms four configured child slots exclude the root, retained
  child identity/role survives a cold App Server restart, and completed idle
  children can be unloaded without retiring identity.
- The retained designer found that the prior `codex-web` send API did not expose
  per-real-turn model/effort and application context. Phase 2A added that
  bounded compatible interface. No portal-side child scheduler is required or
  supported.
- Generic catalog evaluation and default-package evaluation pass. Focused Go
  tests for `workspacecodex`, portal web and portal command packages pass in
  module mode; the unflagged command encountered the repository's stale local
  vendor tree and made no changes.
- Site config validates against the generic schema. Organization/site Nix
  parsing, Ruby syntax, and diff checks pass.
- Phase 1 commits are `39bfa664` (`dev-workspace`), `583647dd`
  (`vpsfree-dev-workspace`) and `0ccd1101` (site workspace). The review packet
  records their exact bases, heads, compatibility assumptions and quick checks.
- The fresh independent Sol/xhigh reviewer covered general,
  architecture/repetition, scope/proportionality and risk/compatibility. It
  found generic watcher policy still duplicated the concrete site model,
  unmanaged creation confused the product catalog default with the effective
  configured Codex setting, and team/native identities omitted material input.
  All three findings are accepted for remediation before long checks.
- Generic remediation now resolves managed watcher settings only from pinned
  utility policy, preserves omitted unmanaged model/effort settings through
  native thread creation, removes obsolete Astra defaults, strengthens
  team/native identity inputs, and covers utility TOML restrictions. Focused
  Go tests and skill validation pass. The retained reviewer accepted the
  remediated contract with no Blocking or Important finding; its sole Advisory
  test gap is fixed by independently recomputing every native name in final head
  `39bfa664`.
- The Luna-owned long build batch passed generic catalog/package, organization
  package, and site team-policy/instruction checks using local feature-worktree
  dependency overrides. Full evidence is in `verification-phase1.md`.
- `codex-web` is registered from pinned/default-branch base `0a75d720`. The
  generic Phase 2A half stayed within dormant catalog/state/CAS primitives and
  a package-retention interface only.
- Phase 2A is complete. `codex-web` head `52b8ca6` keeps zero-option schema-3
  ledger bytes compatible while binding nonzero turn options to retries.
  Generic head `729e5e08` is one coherent dormant-state commit with strict
  catalog/package pins, CAS storage, revision/history equations and inert
  retention-path primitives.
- The retained Sol/xhigh reviewer accepted the remediated Phase 2A ranges with
  all four lanes clean. Fresh Luna/low watchers passed both exact-head focused
  suites and `nix flake check --print-build-logs` in both repositories.
- Phase 2B.1 commit `abbce9fd` adds dormant strict creation bindings, neutral
  initial-turn options, retained state publication, immutable registration
  planning and internal helper commands. It has no production caller. The
  retained designer closed GC-root/state durability and package-provenance
  findings; a fresh Luna/low watcher passed the exact committed focused Go
  packages.
- Phase 2B.2 commit `285e998f` adds strict per-workspace Codex registration,
  private launch/inventory records, semantic restart reconciliation and the
  forward-only host switch contract. The retained designer accepted the final
  slice with no Blocking or Important issue. Fresh Luna/low watchers passed 87
  Ruby runs with 497 assertions and the focused portal command/session Go
  packages at the exact committed head.
- Phase 2B.3 locally activates strict managed `new` and plan-to-new creation,
  immutable selection receipts, retained-root-first publication, launch/socket
  evidence, option-aware first turns, direct CLI selection, lifecycle guards,
  team-aware browser controls and retry-safe drafts. Managed forks and later
  lifecycle operations remain fail-closed for their owning phases.
- The browser acceptance test found and fixed a real acknowledgment-state bug:
  explicit stale-catalog confirmation was being immediately unchecked. The
  final Chromium run passes both forms, independent plan draft keys, reload
  recovery, failure retention and accepted-receipt cleanup.
- Phase 2B.3 is committed as `f2754b8`, `e423e02`, `187d41b`, `da7d935`,
  `45e6bde`, `327f4e8` and `6aa9be1`. It activates managed new and plan-to-new
  creation, strict receipts, retained-root-first publication, launch evidence,
  direct CLI selection and browser controls. Schema-1 sessions remain legacy;
  managed lifecycle operations remain fail closed. All mandatory-review
  findings were resolved and rerun by the same retained Sol/xhigh reviewers.
  Fresh Luna/low verification passes final Go packages, host 91/520,
  dev-session 325/3,513 with 12 intentional skips, Chromium acceptance, the
  default package build and `nix flake check`. Evidence is in
  `verification-phase2b3.md`.
- The user selected the lowest-cost legacy approach: existing sessions remain
  schema-1/unmanaged and are not migrated or adopted. New schema-2 sessions use
  teams. This preserves already-tested legacy operations and removes the
  dedicated migration/deployment work from this initiative.
- The reviewed `codex-web` feature head `52b8ca6` is published to its feature
  branch and the generic Go/Nix pins now use that exact head. Default-branch/
  configuration integration, archive and deletion remain unauthorized.
- Phase 2C.0 is complete at generic head `bb3de38`. Its durable provenance
  classifier recognizes only legacy unmanaged, managed, managed recovery and
  corrupt state. The four allowed recovery windows are the valid schema-2
  pre-publication record, post-publication/pre-authority-record state, and the
  two ordered finalization prefixes ending with runtime authority `creating`
  and `ready`, respectively. Schema-1 and `--no-codex` sessions remain legacy
  without migration or adoption. The high-risk Sol/xhigh General,
  Architecture/repetition, Scope/proportionality and Risk/compatibility review
  findings were fixed before final phase consolidation. Fresh Luna/low watcher
  evidence is focused Go pass, agent-team creation 12/148 and workspace host
  92/524. No deployment, publication or default-branch integration is recorded
  for C0.
- The per-numbered-phase review cadence was superseded for the remaining work.
  Complete the remaining runtime-team slices as one release candidate, deploy
  it to aitherdev for user feedback on portal controls and team selections, then
  run one mandatory independent consolidated Sol/xhigh review across all
  completed implementation phases. Reviewer fixes follow that review under its
  required reruns. Long or uncertain verification remains owned by fresh
  Luna/low watchers. The completed Phase 2C.0 review remains historical
  evidence and does not record approval, deployment, publication or
  default-branch integration.
- Phase 2C.1 is complete at generic head
  `abbbb3e9e58757337902739462d1174691002a3b`. It retains append-only member
  assignment evidence with immutable requested task, selection/catalog and
  replacement provenance; a historical completed assignment remains evidence
  after a selection changes, but cannot authorize current work or writes.
  Strict CAS records move an operation through `prepared`, `submitting` and
  `accepted` or blocking `unknown`; exact-root observation/reconciliation is
  required before an uncertain member can be replaced, reused or closed. The
  focused generic Go checks passed in module mode. The ordinary unflagged Go
  invocation encountered the repository's stale local vendor tree; module mode
  resolved that verification-environment issue without changing vendor files.
  The C1 portal view is read-only status for selection and observed member
  state. It neither spawns nor dispatches native members and implements no team
  transition. Phase 2C.2 is next and its existing detailed contract in
  `design-phase2c-runtime-dispatch.md` correctly depends on these C1
  observation, unresolved-operation and reconciliation invariants.
- Phase 2C.2 is complete at generic head
  `394884b8c1e62e868625b1911eaca3c2c98a85fe`. It resolves a managed target
  only from the pinned catalog after runtime-authority and host-registration
  evidence validate, then uses the public `selection_revision` CAS while the
  private state revision advances for durable writes. At a fully quiescent idle
  root it applies the transition immediately and records exact
  before/requested/after state with bounded replay history; compatible retained
  members remain eligible and incompatible members become inactive, without any
  member create, close, retask or wake action. Only the authenticated exact-root
  path may record one pending transition while its observed turn is active; its
  root-and-turn boundary is later revalidated by the non-sending
  `ApplyPendingBeforeSend` helper before C3 prepares a real send. Other active
  or uncertain work, stale or mismatched requests, legacy/unmanaged/recovery or
  corrupt evidence, and invalid registration all refuse without a fallback.
  No portal control, native dispatch, native member action, deployment or
  review is recorded for C2.
- The focused exact-head check in
  `logs/phase2c2-agentteams-module-mode.log` passed
  `portal/internal/agentteams` in 1.115 seconds. The repository's pre-existing
  stale local vendor tree remains unsuitable for this check, so it was run in
  module mode; no vendor files were changed. The current uncommitted C3 contract
  in `design-phase2c-runtime-dispatch.md` remains consistent with C2: it calls
  `ApplyPendingBeforeSend` under the managed submission fence and cannot report
  a switch as applied while sending under the old selection.
- Phase 2C.3 is complete at generic head
  `0594e3f9c175bdb617a17fddb1dee8cccaec0156`. It records managed dispatch in
  a durable dispatch ledger and preserves/reconciles the related dual-ledger
  recovery state. Under the managed submission fence it persists and applies a
  valid pending selection with `ApplyPendingBeforeSend` before issuing the real
  send, so the send is bound to its exact selection identity. A same-selection
  steer follows the managed dispatch path without changing selection. Portal
  controls expose only the permitted managed feedback actions and remain
  restricted for legacy, unmanaged, recovery, corrupt, uncertain and otherwise
  ineligible states. Fresh Luna/low verification in
  `logs/phase2c3-final-explicit-verify.log` passed
  `portal/internal/agentteams` and `portal/internal/web` in 48.140 seconds.
  The verified follow-up from the former C3 head changes only a stale test
  fixture and makes no product-behavior change. Its focused verification passed
  2 runs/14 assertions, and fresh Luna/low generic-package verification passed
  92 runs/508 assertions. The later aitherdev wrapper build and user-profile
  switch succeeded; the current package is
  `/nix/store/aavh5axl72bv9ivxb85yjyr79rxdp9z0-dev-workspace-0.2.0`.
  By user decision, no Phase 2C.3 review has run yet; C1–C3 are the combined
  deployed feedback release candidate. No review approval, publication or
  default-branch integration is recorded.
- The original `2026-09-22-team-test` managed creation left only a failed
  receipt and no session state. Its installed-package decoder could not resume
  it. The user authorized removal of that exact failed receipt; after the
  forward deployment, a fresh managed delegated session with that slug was
  created successfully.
- Generic commit `e33344f` contains the identified root-cause fix. Focused
  regression verification passed 10 runs with 202 assertions. Fresh Luna/low
  watchers then passed the wrapper build (about 4m26s), profile switch (43.5s),
  and fresh managed creation (91s). This is deployment and feedback-session
  evidence, not consolidated-review evidence.

## Cleanup

Not authorized. Keep the initiative active, retain branches and leave the
session open after implementation/deployment.
