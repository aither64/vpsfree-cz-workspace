# Final independent review: idle coordination workers

Read /home/aither/workspace/ai/vpsfree.cz/AGENTS.md and its applicable procedure routes, each worktree AGENTS.md, /home/aither/.codex/skills/mandatory-change-review/SKILL.md, and all four lane references: general-review.md, architecture-review.md, scope-review.md and risk-review.md. Perform the review directly, read-only, without nested agents or long checks. This is final committed-deliverable review, not early advisory review.

## Outcome and selected boundaries

User requested idle sessions instead of reservation polling, selected durable background continuation and wakeups only for needed agent action/review, and specified aitherdev deployment through vpsfree-cz-configuration. Implement the plan is authorization for implementation and planned rollout, not master integration. Lead owns edits. Reuse existing native transport; no Codex upgrade or codex-web change. Maintain approvals, exact reviewed inputs, FIFO, short resource claims, held review reservations and uncertain-effect recovery. Preserve synchronous/manual --no-wait behavior.

Plan/state/design are in this packet's directory. Core acceptance: background integrate returns after durable acceptance; preparation/continuation survive absent CLI/agent and worker restart; intermediate events do not start model turns; error/final notices are deduplicated; pause prevents future admission; lifecycle and package switches fence the correct owner/generation. Background completion leaves initiative lifecycle active for lead review.

## Risk and reviewer selection

High risk: persisted journals, scheduling, host mutations, lifecycle and package-transition safety. Lanes: general, architecture/repetition, scope/proportionality, risk/compatibility. No retained roster exists; team list refuses because this is tracking-only (no native lead). Standalone fallback uses the installed catalog's default_development_team lead_reviewed, sole review-purpose reviewer role: gpt-6-astra, xhigh, read_only. Catalog digest 437585347ac8b2cdbf498a169d8871e684f3f61ccf1dd48e8589d79ef9629abd. Preserve these settings on follow-up.

Local development operator is trusted; assess ordinary mistakes, concurrent operations, ownership, data integrity, recovery, and remote clients. Do not invent hostile-operator filesystem hardening.

## History, migrations, consumers and documentation

No database migrations. Schema-2 background journals are new, unmerged, unreleased, undeployed and unconsumed. Preserve support for deployed schema-1 manual journals; ledger/snapshot/attempt/adapter schemas stay 1. New package advertises journalSchema 2, readers accept 1 and 2. Retained schema-2 journals intentionally fence older packages. First selection must drain pending schema-1 manual runs because their predecessor demands exact metadata. This upgrade contract is in runtime integration docs.

Runtime is reusable provider. Actual consumers are workspace's nested vpsfree-dev-workspace/dev-workspace input, extension revision 767dfd587e346168e1443e65ccdb67ce748f3fe3 (unchanged), configuration devWorkspace input through channel dev-workspace/role devWorkspace, Nix host module and workspace profile composition. No mkPackage argument or Codex protocol change.

Runtime behavior/tests/docs/metadata/UI form one feature commit: its new schema, continuation, pause and notification semantics are coupled, and UI/doc/tests describe that behavior. Workspace waiting instructions and mechanical runtime input update are separate commits. Configuration contains one generated channel-pin commit only. Exactly one input-update commit per consumer stream, both selecting 4fd9128d46443f0ef8fe90f8f1d6455cb8f1d390. No superseded branch approaches, no repeated update streams, no retained intermediate migrations or pins. Independently verify these conclusions across complete histories.

Runtime docs changed: docs/integration.md, docs/coordination.md, docs/coordination-operations.md, existing README integration link checked. Workspace docs changed: docs/coordination.md and routed Git/verification procedures. Configuration operations guide checked and respected. The owning lead applied user-facing writing guidance to UI and operational text.

## Quick verification

- Nix environment Ruby integration suite: 27 runs, 133 assertions, no failures/errors/skips. Subsequent focused admission/pause/fence/capability: 5 runs, 29 assertions.
- Browser coordination contracts: 13 passing cases, including background waiting and attention states.
- Go internal/agentteams TestLoadInstalled: passed, covers journal capability 1 and 2 and rejection of 3.
- Existing coordinator notification regression selection: 2 runs, 11 assertions, passed (52.6 seconds).
- Ruby syntax, JS syntax and git diff --check: passed.
- Workspace/configuration deployment contract: passed at shared runtime 4fd9128d46443f0ef8fe90f8f1d6455cb8f1d390.
- Configuration Overcommit precommit Nixfmt and commit-msg hooks passed; generated message width warning retained as required.
- Full package/CI, systemd restart acceptance and native acceptance have not yet run; review precedes those checks.

## Deployment limitation

Normal start created a fresh session thread but initial request and supported retry both refused: materialized Codex thread has no initial user request. Its creating journal and thread remain preserved in 2026-10-16-idle-coordination. This separate tracking-only initiative permits edits/testing but cannot submit live deployment without a valid managed owner. Do not bypass that refusal or operate another session's reservation. Prepare and test code/inputs independently.

## Requested report

Findings ordered Blocking / Important / Advisory with file/line references and concrete failure scenarios, then residual gaps. Explicitly conclude on whole-branch history, update-stream consolidation, and migration lineage (no database migrations; new journal format with deployed predecessor support). Do not rubber-stamp. Report the actual model/effort and confirm read-only scope.

## Complete branches

### dev-workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/dev-workspace
Base: 2483b4eba6d3388bcbed0659f089f0e6edbe11bf
Head: 4fd9128d46443f0ef8fe90f8f1d6455cb8f1d390

```text
4fd9128d46443f0ef8fe90f8f1d6455cb8f1d390
coordination: continue approved integrations in the background
Let sessions end their turns while durable workers advance authorized
merge and deployment runs. Retain step identities across worker restarts
and notify the lead only for completed operations or required action.

Add pause and lifecycle fencing, generation handover and versioned
background journals. Preserve manual execution and schema-1 operation
contracts; retained schema-2 journals require a compatible runtime.
```

Diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/review-dev-workspace.diff

### workspace

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/workspace
Base: 9a74012ceed39027a5a0a0c7cc88fb3706510aaf
Head: 2a03ea91905314635fd77a425eb76549875f31b0

```text
1750725b5e43fce24af6f67a2d2f45e3f3f72c67
coordination: let agents idle during background integrations
Direct waiting sessions to durable background continuation and native
action or review messages. Keep preparation, authorization and
reservation ownership requirements in the existing coordinator workflow.

2a03ea91905314635fd77a425eb76549875f31b0
inputs: select background coordination runtime
Select the published runtime that continues approved integrations while
sessions are idle. Keep the extension revision and unrelated inputs
unchanged, matching the host configuration runtime contract.
```

Diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/review-workspace.diff

### vpsfree-cz-configuration

Worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-16-idle-coordination-worker/vpsfree-cz-configuration
Base: 29a9589f724829b2b1717a1a26b4d2c3f14165b3
Head: 752edf113d6a6cbcdc2a3c248d0914641edd0eda

```text
752edf113d6a6cbcdc2a3c248d0914641edd0eda
inputs: set devWorkspace to 4fd9128d
devWorkspace: 2483b4eb -> 4fd9128d
git log for 2483b4eba6d3388bcbed0659f089f0e6edbe11bf..4fd9128d46443f0ef8fe90f8f1d6455cb8f1d390
> 4fd9128 coordination: continue approved integrations in the background
```

Diff: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-16-idle-coordination-worker/review-vpsfree-cz-configuration.diff

## Final remediation supplement

Original report: review-report.md. Narrow requested fixes and regression checks are reconciled in review-remediation.md. No new design, approval, public contract, state format or supported boundary was added during remediation; the mandatory review narrow-fix rule applies without reviewer rerun.

Final exact ranges: final-heads.json. Final complete series and diffs are PROJECT-final-series.txt and PROJECT-final.diff; original reviewed diffs retained. Runtime corrections folded into its single feature commit. Workspace still has one policy commit and one generated input update. Configuration was replayed over 9105d416 (upstream's unrelated vpsadminWebui input update) and regenerated once from its default runtime input to final ced31b5f using the channel command. Generated message preserved. Range-diff artifacts show remediations and final-only consumer pins. No obsolete branch history or database migrations. No intermediate feature pins deployed or released. Extension and unrelated inputs preserved.

Independent whole-branch conclusions above remain applicable to the same final design and commit split. Local inspection verifies only the targeted fixes and generated pin refresh. Live acceptance remains bounded by the managed-owner issue in state.md.

Final fixture-only correction folded into runtime ced8e76e after diagnosing the asynchronous phase/event observation race. Product behavior unchanged; package and systemd acceptance passed. Final consumer pins are workspace 65926d04 and configuration b2c39068. Final pin proof and complete series refreshed. No reviewer rerun required for this narrow test correction or the mechanical final pin regeneration. Native fixture provenance correction remains session evidence only.
