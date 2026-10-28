# Phase-aware progress observation

Implementation brief for the lead and implementers. The user authorized these
improvements and deployment to aitherdev, but no default-branch integration.
Architect investigation used canonical Git objects, shared source guidance and
this session's records only. No other session was inspected.

## Scope and source ownership

Change assessment guidance, not scheduling, concern state or team composition.
Recognize useful design work while continuing to challenge stalled work and scope
expansion. Avoid new frameworks, model evaluations, approval gates or telemetry.

Sources inspected:

- Workspace `config/agent-teams.nix`, `docs/agent-teams.md`,
  `docs/agent-instructions/verification.md` and `flake.nix` own site policy and
  package composition. The package receives `teamConfig` from this catalog.
- The selected generic runtime is
  `d5d2b39b13a6875a26b218ffaf7b589b9d71a1fb`, also the inspected
  `refs/remotes/origin/master`. Bare `HEAD` is stale and was not used for design.
  `portal/internal/progressobserver/instructions.go` owns refreshed stock policy;
  `portal/internal/web/progress_observer.go` supplies each assessment prompt and
  the lead's concern notice. Site-only changes would leave these paths inconsistent.
- `refreshProgressInstructions` recognizes exact released stock hashes and uses
  the existing idle-thread policy refresh. Current site and runtime stock text
  have the same trimmed SHA-256:
  `5703253227dfeff529a053bcc32501eb9ff58fb468f23690b1035d425e53684c`.
  This hash is not yet in `LegacyStockInstructions`.
- Configuration was inspected at freshly fetched
  `2cf292f465cee8b969d53f8c96f937b021ecb4a6`, not bare `HEAD`.
  Its `flake.nix` maps channel `dev-workspace`, role `devWorkspace`, to input
  `devWorkspace`; aitherdev's `config.nix` imports that input's host module.
  `docs/operations/codex-providers-aitherdev.md` describes the application/profile
  split and ordinary host commands. Do not resurrect obsolete operations docs.
- The installed coordination guide identifies package
  `/nix/store/pq2jwjcv4hbyiwzcam50x6j9fv008qiq-dev-workspace-0.2.0` and governs
  machine retention. The deployment owner must reread the selected guide at
  activation if the selected package changes.

## Assessment contract

Assess user-authorized scope and the current phase before output metrics. During
design, evidence includes resolved constraints, eliminated alternatives with
reasons, clarified invariants and dependencies, and fewer open decisions. During
implementation and verification, use the corresponding completed slices and
required results. A phase label or growing document alone is not progress.

Fourteen architect working minutes, zero code, absent design.md, waiting
implementers and no preview do not independently establish a stall. Repeated
requests for settled interfaces can justify a coordination checkpoint. Ask at
the next safe boundary for a concise account of learning, settled/open questions,
dependency reasons and the next observable milestone. Use existing notes or a
working draft; no per-check document or commit requirement. Preserve the existing
adequate design-brief requirement before substantive implementation.

Keep the 30-working-minute reassessment for small fixes/docs. Complex work uses
task-specific milestones; observation cadence is not a delivery deadline. State
which clock is being used, never add overlapping member clocks, and respect
coverage gaps. Missed milestones, repeated investigation without new evidence,
unexplained churn and optional expansion remain actionable at any appropriate
check. Extensions need a concrete reason and next observable result.

Release implementation packages only when their relevant interfaces and
cross-cutting invariants are stable. Provisional assumptions are not contracts.
Do not force parallel utilization or defer OAuth/authentication, permissions or
other dependencies without evidence of independence and preserved user scope.
Route consequential choices through the lead using existing ownership rules.

Keep unresolved concerns keyed and evidence-based. Observed design learning or
verified dependency necessity can refute a mistaken stall premise and resolve
its key without code delivery. Acknowledgment alone cannot. A repeated concern
must assess new evidence and identify the remaining gap; it must not mechanically
demand implementation. Missing essential context is unavailable, not proof of
either health or failure. The observer's targeted inspection is sufficient to
assess evidence; this does not assign independent final review.

## Shared stock observer text

Use the same trimmed text in the site observer role and runtime `Instructions`.
The two owners coordinate changes to this text through the lead; do not make
independent wording variants that break future exact stock recognition.

```text
Observe progress toward the user's goal. Use tools to read this session's files, conversations, Git status/diffstats and existing check output. Establish authorized scope, current phase and next milestone before judging output. During design, look for resolved constraints, narrowed alternatives, clarified invariants and dependencies; during implementation and verification, assess the corresponding deliverables and results. Time, zero code changes, an absent design file, waiting implementers or no preview alone do not prove a stall. If visibility is insufficient, suggest a lightweight checkpoint at the next safe boundary: learning, settled and open decisions, dependencies and next observable result. Preserve the required design brief before substantive implementation. Use task-specific milestones for complex work; the 30-working-minute reassessment applies to small fixes and documentation. Observation cadence is not a deadline; do not sum overlapping member clocks or ignore coverage gaps. Challenge missed milestones, repeated investigation without new evidence, scope expansion and verification loops. Do not force parallel work, freeze provisional contracts or defer authentication or other dependencies without evidence that work is safely independent and user scope is preserved. Keep concern keys stable while unresolved; assess new evidence and name the remaining gap. Observed learning or verified necessity can resolve a mistaken concern without code delivery; acknowledgment alone cannot. Missing essential information is unavailable. This is progress advice, not a full review or approval gate. Do not edit, run checks/builds, assign work, inspect other sessions, cancel development checks or waive requirements. Return the scheduled JSON result; do not call report_to_lead.
```

## Implementation packages

| Owner | Files and deliverable | Dependencies |
| --- | --- | --- |
| implementer0: site policy | Workspace `config/agent-teams.nix` observer text and compact aligned `leadRequirements`; `docs/agent-teams.md` and `docs/agent-instructions/verification.md` explain phase evidence, timing and resolution. Preserve other role requirements and the 4096-byte instruction cap. No AGENTS/session-procedure expansion is needed. | Can start from this brief; shared stock text above is fixed for both owners. |
| implementer1: runtime | `portal/internal/progressobserver/instructions.go`: replace stock text and add the exact preceding-stock hash, preserving older hashes and `PendingV2Instructions`. `portal/internal/web/progress_observer.go`: align only `progressPrompt` and newly constructed concern notice wording. `portal/internal/web/progress_evidence.go`: include optional design.md in the existing source-map hint if useful. Update `docs/dev-sessions.md` progress section and focused tests in `portal/internal/web/progress_evidence_test.go`, `progress_observer_test.go`, and `portal/internal/progressobserver/state_test.go` only as required. | Can start independently. No edit to scheduler logic, state schema, protocol, native injection or recovery code. |
| implementer0: composition and configuration | After published runtime head, update workspace direct nested runtime URL and generate its lock; update configuration's `dev-workspace/devWorkspace` channel using confctl. Only generated pin/channel files change in configuration. Recover the reported post-checkout hook failure in its Nix environment without bypassing hooks; verify registration instead of assuming success. | Depends on implementer1's published head. Lead coordinates final review and activation. |

The runtime prompt should briefly ask for phase and milestone evidence and allow
evidence-backed correction of a mistaken premise. Its JSON examples should use
phase-appropriate concern/recommendation language. Preserve `Progress check v3`,
the result shape, key/evidence requirements and compact-context limit. The lead
notice must allow an evidenced decision to continue design, not command automatic
simplification. Retain `Progress response <key>: <decision and reason>`.

## Compatibility and recovery invariants

- Keep concern/result/roster schemas, scheduling intervals, three-minute observer
  deadline, active-work gates and unavailable behavior unchanged.
- Exact released stock text refreshes on the same idle native thread. Preserve
  history, model, effort, access and custom instructions. Do not broaden stock
  detection to prefixes, role names or substrings; new stock must not refresh
  repeatedly. Custom member policy remains retained while the ordinary scheduled
  assignment receives the updated generic guidance.
- Updated lead defaults apply to new leads. Do not rewrite retained lead prompts;
  the ordinary concern notice supplies the phase-aware response guidance to them.
- Pending v2/v3 checks retain their stored message, ID, turn options and original
  recovery path; no refresh before settlement. Preserve manual retry deferral.
  Already stored notices remain their original messages until ordinary handling;
  do not rewrite queued submissions for new wording.
- Existing `State.Apply` already accepts matching-key evidence; do not add a new
  resolution status or treat arbitrary acknowledgment as proof. Automated tests
  verify transport/state behavior, not whether a model's judgment is true.
- No state migration, API/CLI change, Codex upgrade or coordinated fleet update.
  Mixed old/new packages read the same formats. Older package selection is not
  a supported workspace rollback: recovery remains a compatible forward package.

## Acceptance and checks

| Example | Expected assessment |
| --- | --- |
| Complex redesign, 14 architect minutes, no code/preview; new authorization invariants established | Recognize design progress; request visibility only if needed, not immediate coding. |
| Repeated requests for interfaces without an account of learning or dependencies | Ask for a safe-boundary checkpoint; do not infer safe OAuth deferral. |
| Long design.md repeats the same alternatives and misses milestones without new evidence | Actionable stall with the remaining question and shortest valid next step. |
| UI depends on identity/permission decisions | Waiting is legitimate; no forced parallelism or frozen speculative contracts. |
| Stable independent package withheld for unrelated optional exploration | Legitimate coordination/scope concern. |
| Prior stall concern is contradicted by inspected design learning | Resolve the same key with concrete evidence; no code requirement. |
| Only reassurance, wrong-key resolution or missing essential evidence | Preserve concern or report unavailable under existing rules. |

Quick checks in each repository's Nix environment:

- Workspace: formatting/declared hooks, `ruby test/agent_instructions_test.rb`,
  instruction byte limits and equality of the two stock texts. Do not add a
  large set of assertions mirroring prose. Evaluate the existing agent-team-policy
  contract against the composed package.
- Runtime: gofmt and `go test -mod=readonly ./internal/progressobserver ./internal/web
  ./internal/workspacecodex -run 'TestProgress' -count=1` from `portal/`.
  Extend existing fixtures for current-stock refresh, custom near-match retention,
  same-thread/settings preservation, and original pending v3 message/options
  across upgrade; retain existing v2/manual-work coverage. Exercise matching-key
  design evidence through the normal result path and updated lead notice.
  Keep the six-member source-map prompt at its existing compact bound.
- Composition: inspect generated lock changes, preserving extension revision,
  Codex and sibling inputs/follows paths; run
  `bin/check-dev-workspace-deployment --workspace-root WORKSPACE_WORKTREE
  --configuration-root CONFIGURATION_WORKTREE` against final locks.
- Semantic review of the examples above must cover all three guidance surfaces:
  stock member instructions, scheduled assessment, and lead notice. No new model
  evaluation harness or additional reviewer before the required final review.

Commit intended changes and pass quick checks before mandatory final review.
After review, run a bounded verification batch through the prescribed utility
watcher: runtime `nix build .#checks.x86_64-linux.package --print-build-logs`
(the full packaged runtime), the composed workspace default package and existing
agent-team-policy, agent-instructions and deployment-contract checks, and
`confctl build cz.vpsfree/machines/aitherdev` in configuration's Nix environment.
Add a focused runtime catalog/package contract check only for a specific changed
contract not covered by this selection. Monitor already-triggered exact-head CI
alongside the batch; its breadth does not justify duplicating unrelated suites
locally. Do not run aggregate runtime `nix flake check`, host-module-idempotency,
session-recovery-boot, session-archive-lifecycle or creation VM suites for this
guidance-only change. No host/session lifecycle implementation changed.
State each launch's expected duration and stopping condition. Finish verification
when the selected exact-head checks/builds and required CI succeed; do not repeat
or broaden checks without changed inputs, unresolved failure or a concrete
uncovered risk. Investigate a failure or duration overrun before selecting only
the affected follow-up; report missing risk coverage to the lead. Stop and
investigate unexpected local kernel builds under the verification procedure.
Reuse successful unaffected evidence only under existing evidence rules. Delegate
uncertain or long Go checks to the watcher too. Architect has not run these checks.

## Deployment and recovery plan

Publish feature heads; no merge is authorized. In the workspace feature worktree,
set `inputs.vpsfree-dev-workspace.inputs.dev-workspace.url` to the published exact
runtime and run `nix flake update vpsfree-dev-workspace/dev-workspace`. Preserve
extension `767dfd587e346168e1443e65ccdb67ce748f3fe3` unless an independently
justified later baseline changes it. In configuration's Nix environment use
`confctl inputs channel set --commit dev-workspace devWorkspace REVISION`.

Build/copy before reserving the physical machine where supported. The host is
`cz.vpsfree/machines/aitherdev`, coordination alias `vpsfree:aitherdev`.
Use confctl build, dry activation and ordinary no-reboot switch with configured
auto-rollback. Verify `/run/current-system` and `/nix/var/nix/profiles/system`.
Configuration selects the host module/runtime contract; it does not install the
workspace application. Select the composed workspace user-profile application
through ordinary `workspace-host switch --source WORKSPACE_WORKTREE`, passing the
held `DEV_WORKSPACE_CLAIM_ID` and exact session identity. Confirm current package
transition admission instead of interrupting threads or bypassing refusal.

Record exact system/profile store paths, source/input graph and deployed heads in
the lead's existing rollout receipt. Check portal health, conversation continuity,
the installed catalog's text and one naturally eligible same-session observer
refresh/check when available. Never wake or inspect another session for proof.
Fixtures establish custom/pending-path behavior without live roster manipulation.
Distinguish installation/refresh evidence from model-semantic evidence.

Preserve original journals and selected package roots. Failed activation uses
ordinary confctl recovery/auto-rollback for system effects and a compatible
forward package or same-operation retry for workspace effects. Do not run
workspace-host rollback, reset state or restart the shared daemon to force refresh.
Concrete activation status commands and store paths are deployment-owner follow-up,
not a reason to broaden these source changes.

Retain the machine claim while deployment is uncertain or deployed lineage lacks
integration evidence. User deployment authorization does not grant merge approval.
After separately approved integration and verified deployed lineage, inspect the
exact claim, release promptly and verify release; no separate UI acceptance is
needed. Session remains open. Lead owns tracking, review assignment, rollout and
any later integration request.
