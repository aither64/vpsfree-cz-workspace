# Final review packet: archive preparation

## Request and boundaries

User requested implementation of the accepted plan. Priority recovery of
2026-10-22-haveapi-release completed through original portal receipt attempt 2.
The feature is explicit portal Archive preparation: read-only readiness before
stopping agents, retained lead repair, progress-based retries with three
unchanged cycles stopping, cancellation, restart and non-blocking unrelated work.
No generic auxiliary-file deletion, automatic policy change, post-destruction
lead revival, default-branch integration or configuration deployment.

## Identity and revisions

Initiative: 2026-10-25-archive-unmanaged-files-investigation.
Workspace: /home/aither/workspace/ai/vpsfree.cz
Project worktree: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace
Base: 9634151b9836311c331a58880fbb4c46133fd98f
Head: e0c6c248311cf488f291b9ff3e451e40cc400555
Plan/state/design/recovery are in this packet's directory.

Complete series:
3a28445270eb1df11b949c1fcc4dada7bad424f8 archive: check readiness before stopping agents
e0c6c248311cf488f291b9ff3e451e40cc400555 portal: prepare archives with lead-assisted cleanup

The checker and CLI refusal are independently reviewable from their portal
consumer. Tests/docs/packaging for each behavior stay in its owning commit.
There are no superseded approaches, repeated input/dependency/generated update
streams or database migrations. The private preparation files introduce schema 1;
archive/cleanup/revival journals and strict lifecycle receipt schemas stay as
previously supported. None of this branch has been deployed, merged or consumed.

## Review policy and trust boundary

High risk: persisted state, destructive lifecycle handoff, native agent delivery,
concurrency and rollback. Review ALL lanes: general, architecture, scope, risk.
Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md and its four
references. Perform review directly, remain read-only, do not spawn agents.
Inspect the full series and final diff independently and explicitly conclude
history consolidation and migration lineage, including no migrations.

No eligible retained reviewer: this is a threadless tracking-only initiative.
Installed catalog digest 840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa
selects delegated/reviewer, gpt-6.1-sol/xhigh. Keep those settings.

The repository trusts its local operator; review normal mistakes, remote input,
wrong ownership, concurrent operations, interrupts and data safety. Do not invent
hostile-root filesystem attack requirements.

## Contracts and consumers

Generic dev-workspace owns the CLI JSON checker, private preparation store,
portal operation/cancel endpoint and native repair orchestration. The shipped
portal and packaged CLI are the immediate consumers. vpsFree extension/site
consume the generic package; no old CLI signatures or Nix module options change.
No codex-web pin/protocol update: existing send/options/reconcile/metadata/turns
methods are reused. Older packages ignore preparation files and read ordinary
retryable lifecycle receipts after shutdown. Existing journals bypass preparation.

Docs: docs/session-archive-recovery.md is authoritative for supported preparation
and recovery, with the session guide command list updated. README already links
both guides. Session recovery evidence stays separately in recovery.md.

## Verification

- New Ruby readiness tests: 3 runs, 60 assertions, pass.
- Focused Ruby archive batch: 13 runs, 375 assertions, pass, 51.661 seconds.
- Focused Go preparation/lifecycle target/worker/shipped browser client: pass,
  web package 5.044 seconds; extended preparation batch passed 3.214 seconds.
- Ruby/JavaScript/Python syntax, Nix parse and diff whitespace checks pass.
- Native packaged archive-lifecycle VM has NOT run: required after final review.
  It now includes a synthetic Responses provider, a real native shell-tool
  cleanup, portal restart while inference is held, unrelated session creation,
  preflight permission refusal and an independent post-removal filesystem error.

Do not treat mocked client unit tests as evidence that the native VM scenario
works. Report concrete findings with file/line and commits, severity and lane.
Save the report to review.md beside this packet and return a concise result.
