# Follow-up review: progress ownership and retries

Reviewed committed runtime `960dd816b7e56cbdd4af0da15bf0b26257775151..39b0ee29739b315049e18510ce334ae2a9f080dd`
and workspace `0fe886f56031da55d16aa30e6f110243a0ed0e28..24764c677d9a384fe96142b432ef166754939f35`.
Reassessed general, architecture/repetition and risk/compatibility lanes; retained
the previous scope assessment. Read-only source review; no long tests or agents.

## Finding

**Important: an automatic progress check can cancel a manually assigned observer task's pending retry.** Runtime commit `39b0ee29`,
`portal/internal/workspacecodex/progress.go:19` unconditionally calls
`CancelAutomaticRetry(..., "manual_input")`. The scheduler only checks whether
the observer has an active native turn (`portal/internal/web/progress_observer.go:353`);
an ordinary capacity retry can be scheduled while that transcript is idle.
For example, a user assigns the observer a manual analysis, it fails with
`serverOverloaded`, and its normal retry is waiting on backoff when the 15-minute
progress check becomes due during other development work. The scheduled check
clears the manual retry's pending record and submits its own task. This gives
automatic oversight cancellation authority over explicitly assigned work and
contradicts the promised preservation of manual observer assignments.

Defer scheduled checks while ordinary retry work owns that observer, preserving
the exact pending retry. The existing `RequireThreadIdle` contract recognizes
owned automatic retries, unlike a transcript-status check alone. Any retirement
of stale retry bookkeeping should distinguish terminal state from owned manual
work under the normal locks. Add a regression starting with a manual assignment
already awaiting capacity retry; assert that progress submits nothing and leaves
the retry identity/deadline intact. The new test checks a manual assignment
*after* progress, so it does not cover this ordering. Lanes: general,
architecture, risk/compatibility. A narrow deferral/preservation fix can be
verified directly under the mandatory review skill's remediation rule.

## Original findings

The original three findings in [final-review.md](final-review.md) are addressed:

- Scheduled checks bypass ordinary retry admission; the native-wire regression
  exercises both eligible failure classes through the real retry controller.
- Pending settlement and exact cancellation precede unrelated development
  evidence and ordinary execution admission. Regression covers unavailable
  lead/member evidence.
- Retained removed/archived member evidence retires the old pending ownership
  without transferring it; replacement regression covers completed, uncollected
  work followed by remove/re-add.

The new unsent-pending regression also preserves idle-session behavior.

## Final series and remaining verification

The runtime final feature series remains one owning commit, with remediations
folded in. Workspace retains the two policy commits and one amended final
runtime-selection commit. No obsolete unmerged approach or fixup history
remains. There is one final runtime-input update and **no repeated update
streams requiring consolidation**. Extension/sibling lock entries are preserved.
The remote/local workspace tracking-base distinction recorded in the original
report still requires the ordinary fresh target check before integration.

**No migrations.** The optional private schema-1 store and unchanged
roster/lifecycle/native formats retain the original lineage conclusion.
Both feature trees are clean and `git diff --check` passes. Inspected the new
source, native-wire/timeout/replacement tests, final history and mechanical pin
diff; the supplied focused progressobserver/web/workspacecodex checks pass.
Broader packaged validation and disposable pilot remain pending. Resolve or
explicitly decide the Important finding before proceeding under review policy.
