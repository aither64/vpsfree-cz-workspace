# 2026-09-12-nfs-cancellation

## Goal

I'd like you to review recent changes in vpsadminos regarding nfs cancellation. There are currently failing tests, the issue was found by another codex session, who described it in this file: /home/aither/workspace/ai/vpsfree.cz/work/2026-09-11-devcluster-packaging-investigation/nfs-livepatch-handoff.md

I'd like you to review the nfs cancellation changes in kernel and vpsadminos and suggest solutions. I'd also like you to check if the changes in osctld are correct, if the new state survives osctld restart, etc.

## Affected repositories

- `vpsadminos`, remote default `staging`: kernel selection, livepatch inputs,
  osctld cancellation and container lifecycle, unit and integration tests.
- `linux`, remote default `vpsadminos-6.12`: retained cancellation implementation
  `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd` and default source
  `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd`.

## Approach

Review and propose repairs; do not implement, deploy, merge, or change legacy
fallback policy in this task. Verify the supplied handoff against exact source,
inspect kernel synchronization and lifetimes, then trace osctld cancellation
state through restart, recovery, stop, kill, and reboot. Distinguish confirmed
defects from plausible races and test gaps. Write a durable review with source
references, recommended fixes, and an ordered validation plan.

Use this session's own checkout and scratch space. Other sessions' evidence may
be read, but their worktrees, tracking, and clusters must remain untouched.

## Compatibility and deployment

Assess old/new daemon and kernel combinations, retained livepatch ABI/source
identity, default versus retained boot kernels, terminal cancellation semantics,
persisted run state and namespace ownership, and daemon rollback/restart. No
database, API schema, protocol, or production state changes are planned.
Any proposed hard-mount default requires bounded cancellation support before
rollout. Explain whether reboot or coordinated node updates are needed.

## Testing plan

Inspect failed CI artifacts before drawing conclusions. Run focused existing
Ruby unit tests and small isolated state/restart reproductions where useful.
Review integration assertions and kernel selection through source/evaluation.
No long VM suite or kernel compilation is planned for this review. Record
unverified runtime claims explicitly; propose the missing regression matrix.
