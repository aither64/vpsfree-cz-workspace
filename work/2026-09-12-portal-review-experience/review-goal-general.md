# Goal normalization general review

Reviewer lane: general  
Model and effort: `gpt-5.6-sol`, `xhigh`  
Risk classification from the packet: high

Reviewed committed runtime range:
`f5d587823368e530c5d9f52a17e1befed9fd54e1..d3bfd0f5a7c419c9df0ed53aa5f1acb77f8e10c2`.
I also inspected the unchanged Ruby `dev-session` goal reader, creation binding,
journal and completion-evidence consumers. The organization and workspace pin
updates described in the packet are mechanical and were not present in this
reviewed range.

## Findings

No Blocking, Important, or Advisory findings.

The single commit has one logical purpose and follows the repository's
`area: action` subject convention. Its body explains the deployed compatibility
case, immutable identities and recovery behavior. The implementation introduces
the final behavior directly, without a schema change, migration, compatibility
shim, dependency update, generated output, or unrelated cleanup.

The changed identity path is consistent with the CLI:

- `normalizedCreationGoal` trims exactly NUL and the six ASCII whitespace
  characters removed by Ruby `String#strip`, while leaving Unicode whitespace
  intact ([creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:22)). The parity test calls the actual private Ruby `read_goal` implementation and covers every trimmed byte plus nonbreaking and ideographic spaces ([creation_test.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_test.go:485), [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:3610)).
- New plan creation normalizes only the derived initial goal after the exact
  transcript text, turn ID and digest have been checked. It does not rewrite
  `Request.PlanText`, `PlanTurnID` or `PlanSHA256` ([creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:496)). Once validated, retries retain the frozen goal and settings and do not reread the source transcript ([creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:459)).
- For predecessor receipts, normalization is confined to goal-digest
  comparisons in canonical conflict classification, completion proof and CLI
  binding verification ([creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:211), [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:354), [creation.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation.go:677)). Receipt ID, request/source identity, deletion history, model, effort, tracking inode/device, thread ID, manifest goal digest and journal state remain exact. The normal-read regression proves the same failed receipt becomes ready without changing its attempt, raw goal or request and rejects an internal content change ([creation_test.go](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/portal/internal/web/creation_test.go:512)).
- The Ruby owner continues to hash and submit the result of `read_goal`, so the
  portal now compares against the identity actually recorded in the binding,
  start journal, manifest and completion evidence ([dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:614), [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2397), [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2839), [dev-session](/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-09-12-portal-review-experience/dev-workspace/libexec/dev-session:2922)).

## Material gaps

Per instruction, I did not run tests. I relied on the packet's focused race-test
results and inspected their code. The deployed-receipt regression constructs
the canonical binding, manifest and evidence through test helpers rather than
executing a predecessor package followed by the new installed package. It also
checks the no-evidence binding/conflict predicates separately instead of driving
that exact predecessor receipt through an actual Ruby CLI retry. Existing tests
cover those recovery components, but the retained real profile-28 fixture is the
remaining end-to-end proof that no additional thread or initial turn is created.

The new immutable consumer pins, package build, retained-fixture completion and
live upgrade/rollback validation were intentionally deferred until this review;
they remain the material integration and deployment checks.
