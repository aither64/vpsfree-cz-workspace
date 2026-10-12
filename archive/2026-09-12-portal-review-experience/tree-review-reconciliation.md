# Tree and parent-navigation review reconciliation

High risk because ancestor selection/API and deployed package pins change.
Fresh gpt-5.6-sol reviewers at xhigh in all four mandatory lanes. Frozen original
ranges are in tree-review-packet.md; reports retain those identities.

General: no findings. Architecture: no findings. Scope: one Important finding,
no Blocking or Advisory. Risk: no Blocking/Important findings and one Advisory, reconciled below.

Scope found parent links retained view=diff although the approved route clears
view as well as file/version/line. Accepted and fixed: omit view in parentRoute,
letting the existing parser select default diff. Browser coverage now asserts
absent file/view/version and empty hash. All 21 component checks passed again.
The direct fix narrows the URL to the approved contract; no new design or contract
requires a review rerun. It was folded into the owning unmerged parent UI commit.

Final runtime: 41c6d75e8f7cdea1e5cbced7d0106d072d56484d; parent UI 9490e1e; native
backend 4e714b7 unchanged. Final organization 6c98b3676a46c9a9c2830198eae9042b064a71e7 and workspace
cd648e2bd31e3b5d43703320be7967a92bd1e06b pin that exact runtime; all are committed
and pushed. Only the scoped URL omission and its assertion changed after review.

General's new-tab test gap is closed by successful live acceptance through
actual Control-click and a second browser tab. Package and live checks passed.
A real live rollback is not required or attempted: no persisted format changed,
and old package ancestor-link availability is the documented limit. Architecture's
5,000-file DOM stress gap remains an explicit limit of this focused browser
acceptance (30 files, deep/Unicode paths); existing server limits remain unchanged.

Risk advisory accepted: Git objects can contain pathological paths thousands of
directories deep, and recursive tree rendering can exceed the browser call stack.
This produces a comparison-local unavailable view; it does not broaden scope,
execute project content or change data. Normal checked-out paths are constrained
by filesystem limits. Retain the current native tree for this extension and record
iterative rendering of extreme historical paths as a future improvement. The
existing 4 MiB/5,000-file bounds remain; this acceptance is not a claim that those
bounds also impose directory depth. No user approval is required for accepting
this Advisory under the mandatory review workflow.

All four lanes are complete. Every Blocking/Important finding is resolved and
quick verification passes. Subsequent exact-package checks and all 16 live browser
checks passed, including desktop/mobile visual inspection. Both final feature-head
CI runs passed, including organization development-cluster acceptance. Profile 31
is deployed normally. See tree-verification.md for evidence and limits.
