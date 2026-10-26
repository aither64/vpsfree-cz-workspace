# Final independent review packet

Read `/home/aither/.codex/skills/mandatory-change-review/SKILL.md` and all four
lane references: general, architecture, scope, risk. Read workspace AGENTS.md,
applicable procedure files and each affected repository AGENTS.md before review.
Perform the review directly, read-only, without nested reviewers or subagents.
Do not run long checks, mutate live state, or edit source. Write the final report
to `work/2026-10-25-message-delivery-reliability/review.md` (only this evidence file
may be written). Report exact findings with lines/commits and lane/severity.
Explicitly conclude on complete branch history, repeated pin streams and migration
lineage. Include residual risks and meaningful verification gaps.

## Requested result and acceptance

The user cannot send `Implement the plan.` in session
2026-10-24-context-copy-performance-tests. The error is `message outcome is still
unknown; retry with the same browser attempt: failed to write msg: failed to
acquire lock: context deadline exceeded`. Investigate the cause and implement
the complete reliability plan, including transactional receipt storage, safe
background retries, plan dispatch lifetime, timing diagnostics, compatibility
fencing, aitherdev deployment and exact original-attempt recovery. See plan.md,
design.md and state.md here for full boundaries, evidence and acceptance.

The initial no-tracking request was superseded by `you can start tracking this
session`. New tracking binds the already verified current native thread. The
roster is null; no retained reviewer exists. Standalone fallback is the installed
catalog default development team delegated, role reviewer: gpt-6.1-sol/xhigh,
read-only. Catalog digest
840de47527dea8325fcac0c2eb7ca5ae9728b31523ec368bcce595c6f15983fa.
This is HIGH risk: persistent-state migration, delivery protocol semantics,
package selection and forward-only recovery. All four lanes apply.

## Boundaries and consumers

codex-web owns the generic Go state machine, SQLite store/import/export and
browser scheduler. dev-workspace is the direct Go/flake consumer and owns
socket-based private state, plan authorization, browser integration and package
compatibility. The workspace's extension consumes generic dev-workspace through
its preserved nested override. Configuration owns aitherdev's matching host
module input. Inspect actual imports, pins, wrappers and manifest contracts.
Native Codex stays 0.163.0; no native protocol change is intended. No default
branch integration, archive-storage cleanup, session archival or unrelated
attempt reset is authorized. Local operator is trusted; remote clients remain
untrusted as described in dev-workspace AGENTS.md.

JSON schema 3 is deployed. This branch introduces SQLite user_version 1 and
schema-4 JSON predecessor fences directly. No earlier branch schema, migration,
or intermediate pin has been merged/released/deployed/externally consumed.
Initial published library revision 073f6db was used only in disposable checks,
then superseded by a folded atomic-schema-bootstrap correction. Final library
is 7c84dc4; required source refs remain in Git. No live state has been migrated.
Schema creation is atomic, and missing v1 receipt tables must fail closed.

Repeated pin streams have one consolidated final update per repository. The
runtime pin refresh was folded into its original dependency commit; no
intermediate schema or pin transition remains. Dependencies are split from the
backend and browser behavior; runtime pins, storage/package integration, and
plan/browser behavior are separate commits. Backend admission/transport changes
are intentionally coupled with claim-aware state restoration to prevent stale
recovery. Tests/docs remain with their owning behavior.

## Quick verification

Full library Go suite passed (codex ~22 sec), generic browser/retry contracts
passed, Go vet and protocol coverage passed. Focused database tests passed again
after atomic schema bootstrap. Portal focused tests against the published library
passed for plan decisions/delivery/disconnection, archive exports and shipped
browser assets/versions. Ruby compatibility: 2 tests, 34 assertions, passing.
The final composed-lock check passed at runtime 9bf4282185f9440eb9257d71d03636a353ee1282.
Logs remain under /tmp/message-delivery-reliability-2026-10-25/.
Library GitHub Check on 7c84dc4 already passed; runtime CI is in progress.
No long local native/lifecycle/package integration has run before this review.

Relevant docs: codex-web README.md, docs/reference.md and docs/submission-storage.md;
dev-workspace README.md and docs/workspace-portal.md; configuration
AGENTS.md and docs/operations/codex-providers-aitherdev.md. Reusable migration and
forward-recovery contracts belong with their components; exact rollout evidence
belongs in this session, not in configuration docs.

## Prepared deployment and recovery (not executed)

After review and builds, acquire vpsfree:aitherdev through the normal coordinator
for this verified session, then activate compatible system contract if it changes,
then the exact composed user profile. Exclude old application writers through
normal package transition; do not interrupt native turns. Keep compatible forward
recovery available. Verify health, naming, conversation continuity and receipts.
Release only after verified effects and approved integrated deployed lineage.
User has authorized deployment, not merges.

Original recovery is limited to thread 01a16fb2-77cb-7421-a66c-b7274a178ea2,
attempt 3466274b-d2c6-45f9-8ccb-4fe12ca9a382, text `Implement the plan.`, digest
9d4eca07d13e161a4368f619f36d20bbb0af84f871ac5519f977762e693eb1dc,
context plan:01a171ef-b55b-76e0-b926-3e28b706e421:d35959b62010430b2221daf3909deab4917b63970bdcb8d2e31baff04669610a.
Revalidate current state and complete history first. Recover acceptance if present.
The old writer-acquisition failure is pre-transmission proof; absent history alone
is insufficient. A narrow repair must hold appropriate writer exclusion and update
SQLite payload/state/claim consistently, preserve a backup and reuse the original
UUID. No repair script has been executed or committed; review this operational
boundary and identify any required evidence/tooling before an actual repair.

## Complete ranges

### codex-web

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/codex-web`

Base: `872c7ad3962f9fa9b17358244e27f3e3fac59fc5`
Head: `7c84dc4d29566d99d7935627920dd653565aa379`

````
66ab8c0d7e86af214555f8a17cd7ecae68f51831 deps: add SQLite submission storage driver
5c42185745bcd02eb036487feb1c285db15ea381 codex: preserve delivery recovery across durable admission
7c84dc4d29566d99d7935627920dd653565aa379 conversation: retry transient non-delivery in the background
````

Full final diff: `review-codex-web.diff`. Status: `clean`.

### dev-workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/dev-workspace`

Base: `10bb047513c82d1310e8fcaa797e8772f948dd8a`
Head: `9bf4282185f9440eb9257d71d03636a353ee1282`

````
1aa8a76439c0404b4bf4397c51919dcc6c77cb79 deps: select transactional message delivery support
0d1b27fa948d4afbb310034f94303927dce007fb portal: use transactional shared submission receipts
9bf4282185f9440eb9257d71d03636a353ee1282 portal: finish admitted sends and retry transient failures
````

Full final diff: `review-dev-workspace.diff`. Status: `clean`.

### vpsfree-cz-configuration

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/vpsfree-cz-configuration`

Base: `d12a77374b18e15fe7600f95307114e2e1882828`
Head: `59ade10f2c8b14de54303528e66e1538572d6a4d`

````
59ade10f2c8b14de54303528e66e1538572d6a4d inputs: set devWorkspace to 9bf42821
````

Full final diff: `review-vpsfree-cz-configuration.diff`. Status: `clean`.

### workspace

Worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-message-delivery-reliability/workspace`

Base: `b1b86b2b8a075666ccdef7f9d254047be972508a`
Head: `db59ca58df9b649c01aeca7a5303bde270b53db2`

````
df1944a2004282d5eb988323e25c9c3010791b8d Use the published Rust crate in API KB candidates
7253da4a1f40bcc7992c693a672e5a62d91ff414 Record reviewed Rust registry adoption and external performance work
00fe575aff47eff8174c77281846f628aafd326e workspace: plan storage retention improvements
01c06f603629a57c5e9ea784dcdb94065c427065 work: track message delivery reliability repair
db59ca58df9b649c01aeca7a5303bde270b53db2 workspace: select reliable transactional message delivery
````

Full final diff: `review-workspace.diff`. Status: `clean`.

The workspace feature was rebased onto the current shared master before its
pin commit. Its four preceding coordination commits (df1944a20, 7253da4a1,
00fe575af, 01c06f60) are pre-existing shared-master records or this initial
tracking commit, not changes to application behavior in this fix. Inspect the
complete series; the actual workspace feature diff from 01c06f60 is only its
flake.nix and flake.lock pin. They are retained as shared-master ancestry, not
superseded feature iterations. No schema migration exists in runtime,
configuration or workspace beyond the owning library migration above.
