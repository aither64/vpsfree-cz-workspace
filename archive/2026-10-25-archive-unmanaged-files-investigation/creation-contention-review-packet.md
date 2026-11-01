# Final affected-lane review: creation contention fixes

Perform an independent final review of the completed, committed extension to the
archive initiative. Read /home/aither/.codex/skills/mandatory-change-review/SKILL.md
and all four lane references (general, architecture/repetition, scope/proportionality,
risk/compatibility). Review directly, without nested agents. Stay read-only; the
CLI captures your final response as creation-contention-review.md. Do not edit
application or tracking files, start an initiative, deploy, merge, or run long tests.

Source: /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-25-archive-unmanaged-files-investigation/dev-workspace
Tracking: /home/aither/workspace/ai/vpsfree.cz/work/2026-10-25-archive-unmanaged-files-investigation
Read source AGENTS.md and the applicable workspace guidance at
/home/aither/workspace/ai/vpsfree.cz/AGENTS.md, especially git, lifecycle,
verification, documentation and commits procedures. Read design.md's creation
follow-up, plan.md, state.md and the prior review reports for context.

Risk: high (creation/lifecycle synchronization, exact persistent identities,
interruption/cancellation and lock ordering). Trust boundary: the local workspace
operator is trusted; remote requests remain untrusted. No hostile-root filesystem
framework or new persisted schema is in scope.

User explicitly requested root cause and fixes for the creation failures found
while verifying archive work. Prior descriptions left their competing holder
unresolved. New deterministic Go/Ruby regressions hold a real portal queue/reconcile
conversation admission SH lease and prove the contender uses the same runtime
lock inode. The pre-fix log reproduces both CI messages; the fixed tests pass.
Independently assess whether this evidence and fixes establish the root causes.

Before this extension, archive head 5e4e99df passed final review plus narrow
verified fixes, archive/fast CI and an actual older shipped portal reader VM.
Reports: review.md, review-followup.md, verification.md, implementation-history.md.
Do not rerun unaffected content lanes wholesale. Review the added creation
boundaries in all affected lanes, and inspect the complete current series/final
diff for the mandatory final history and migration conclusion.

Base/merge base: 9634151b9836311c331a58880fbb4c46133fd98f
Current head: b974f2f3f83792a494610d1ea03f3d69e97bc1a4
Full series:
e4f6180fa7340335db0d0db8033d164639985e78 archive: check readiness before stopping agents
5e4e99dfecfda94da47c10cd154dfa98269a6533 portal: prepare archives with lead-assisted cleanup
a27fd38e8d760605eb3ac8074cd1080723401e8a portal: skip occupied names before locking candidates
b974f2f3f83792a494610d1ea03f3d69e97bc1a4 session: wait for plan source readers before destination admission


The last two commits are independent fixes: occupied automatic/custom name
selection, then accepted plan source admission. Both support tests/docs. Earlier
archive fixes were consolidated into the two owning commits. No repeated
input/dependency/channel/generated update streams. No migrations, schema changes,
release, deployment or external consumption. No master integration authorization.

Intended behavior:
- An already occupied name is rejected/skipped before acquiring its runtime EX;
  unused candidates still pass the original locked ownership/occupancy checks.
  Custom names stay exact. Unknown lock holders on unproved names are not adopted
  or blindly skipped.
- Accepted plan source EX validation waits before destination/provider creation
  admission, matching the accepted-fork order. Changed source fails after EX and
  before native/provider effects. Cancellation terminates the ordinary worker.
  An existing plan creation journal still recovers without its old source.

Interfaces unchanged: public browser API, Ruby CLI syntax, receipts/journals,
model/provider/native protocol, package contracts. Owning implementation is generic
runtime, not its site extension. Relevant consumers are the portal's accepted
plan/name flows and Ruby initializer. Direct CLI fork policy remains unchanged.
Docs: docs/session-preparations.md naming/reservation and docs/dev-sessions.md
source ordering. Previous supported archive behavior remains unchanged.

Quick checks completed:
- New reproductions fail before fix with the exact errors (contention-reproduction.log).
- New name/plan/recovery tests pass (contention-quick.log, web 2.937s).
- Related preparation, accepted-fork, creation source/plan and implementation
  tests pass (contention-related.log, web 12.803s).
- Ruby source/binding/journal recovery regressions pass: 9 tests / 117 assertions
  (contention-ruby.log).
- Go formatting and diff whitespace pass; no declared hook framework in repo.

Inspect code/tests/docs, commit split and final history. Especially check hidden
lock-order changes, waiting before destination/provider admission, recovery when
source disappears, cancellation, exact replay, and the untrusted request boundary.
Report findings by severity with locations, then test gaps and explicit history,
repeated-update and migration conclusions. Do not assume the packet's conclusions
are correct. The parent will handle any fixes and long VM/CI verification.
