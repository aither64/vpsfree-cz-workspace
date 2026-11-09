# Final branch review packet

Requested outcome: explicit portal/team message delivery must not fail because a
long active turn fills automatic-retry evidence. User asked to implement the
proposed SQLite/shared-settings and asynchronous-proof solution, then authorized
tracking. No merge or deployment authorization.

Scope: dev-workspace only, at `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-06-portal-message-delivery/dev-workspace`.
Base: `240a53dafabf24b6718195b88bee012a4ead8698`. Head: `79a1cc869b1c9631ac4ca8070f1a082793f7f149`.
Branch: `2026-11-06-portal-message-delivery`.

## Complete commit series

```
c74544517d1d77a7c18c1eb6e9fd933f4d7aa85f portal: decouple message delivery from retry proof
79a1cc869b1c9631ac4ca8070f1a082793f7f149 portal: settle confirmed turn interruption immediately
```

Review `git diff 240a53dafabf24b6718195b88bee012a4ead8698..79a1cc869b1c9631ac4ca8070f1a082793f7f149` and both commits, not only the last commit.
The first commit couples storage, delivery decoupling, proof diagnostics, idle
revision invalidation, migration compatibility, fixtures and documentation.
These implement the replacement of bounded aggregate evidence as an admission
condition. The second independently changes confirmed interrupt settlement.
There are no abandoned/superseded branch commits or repeated pin updates.
The SQLite module is already pinned transitively; go.mod now marks direct use.
No dependency version, Codex protocol or codex-web revision changed.

## Design and acceptance

See plan.md, design.md, state.md in this directory. Accept hundreds of active-turn
inputs and queued inputs without waiting for transcript proof, including restart
and aggregate evidence above 1 MiB. Keep bounded reads and shared settings, exact
message IDs/options, cancellation-before-dispatch, unknown-outcome reconciliation,
automatic proof requirements, and immediate settlement only for a confirmed exact
interrupted turn. Distinguish definite rejection from unknown delivery. Preserve
private content in logs/status. Live incident state is untouched.

The owner is portal/internal/turnretry with workspacecodex delivery/proof wrappers.
Consumers include web retry scheduling, idle hints/status, team/CLI sends through
workspacecodex, lifecycle CancelSession, workspace-host package compatibility and
native creation test evidence readers. codex-web owns submission receipts and
existing typed send outcomes; its current pinned API is sufficient.

Non-goals: raising arbitrary total caps, dropping unknown receipts, weakening
execution proof, changing automatic backoff/quota policy, live record repair,
merging/deploying, or adding a second repo. Original native-prefix stall cause is
unproven; this change removes its effect on explicit delivery and adds diagnostics.
Trust boundary: local operator is trusted under repository AGENTS.md. Remote
request authorization and ordinary data-integrity/concurrency/recovery still apply.

## Migration lineage and compatibility

One new schema: legacy retry JSON 1/2 -> schema-3 identity/cutover marker and
sibling SQLite state/snapshot/settings tables. Both legacy formats exist in
supported predecessors. There are no intermediate branch migration versions.
New migration has never been merged, released, deployed or externally consumed;
only disposable test state has used it. Backup/marker/database/completion writes
run under the existing lock. Incomplete conversion recovers forward; completed
missing databases fail. Old strict readers reject the marker. New package checks
require `turnRetryEvidenceSQLite: 1` while retaining predecessor capability keys.
Rollback requires compatible new-reader code. Native ledger and policy schemas
are unchanged; no database guards for unreleased intermediate schemas are added.

## Verification

All commands use repository Nix environment, prepared with nix print-dev-env.
- turnretry package: passed, focused-final-storage.log (25 s).
- workspacecodex/web focused new delivery, crash, interrupt, optional-proof,
  idle-digest, settled worker and submission validation tests: passed,
  focused-final-delivery.log (80 s wall time).
- prior retention/exact-replay/queue/crash/automatic-result tests: passed,
  quick-delivery.log (86.760 s).
- Ruby aggregator filtered for retry records/proof/policy: passed 11 tests,
  243 assertions, focused-final-package.log.
- gofmt, git diff --check, Python AST check and compilation of three affected Go
  packages: passed. No declared hook framework; only sample Git hooks exist.
- Earlier failed checks were fixture JSON/cache assumptions and launching a Ruby
  subfile without its shared harness. Both corrected, evidence retained in state.

Broad Go/browser/package/native integration checks are pending after this review.
Review content is committed and worktree is clean. Documentation lives in
`docs/turn-retry-recovery.md` (behavior, storage, upgrade/recovery) and
`docs/workspace-portal.md` (delivery notice behavior). Workspace writing skill
was applied by the context-owning lead. No rollout has occurred.

## Review assignment

High risk: persisted state migration, uncertain delivery and rollback compatibility.
All lanes: general, architecture/repetition, scope/proportionality, risk/compatibility.
Use `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all its lane
references in full. Also read repo AGENTS.md and relevant workspace procedures.
There is no retained roster: threadless initiative intentionally retains this
conversation; team list reports no valid lead thread. Installed default catalog
fallback reviewer is reviewer role of delegated: gpt-6.1-sol / xhigh, read-only
review purpose, full-access execution policy. Do not edit code or spawn subagents.
Return findings, severity, concrete evidence and explicit whole-branch history,
migration lineage and repeated-update conclusions. Report your actual identity
and configured model/effort. Save the report as review.md in this tracking directory.
