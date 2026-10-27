# Affected final review: release fixture recurrence prevention

Same release/user scope, with explicit user emphasis to understand and prevent
recurrence. Original source review report final-review.md remains applicable
unchanged to metadata/SDK. Review exact final HaveAPI series now:

Base 4d36efcfb2a9f677b5dfe0e632d8353eefe9a79c
Original reviewed metadata 3bbb98e76e286d64707c368fe1c2cc4d03f35eed
Final head c9124da141adc258fbbaf67d4ec19ee3f8580849
Complete series: metadata release0.31.0 commit, then
`c9124da1` single bounded fixture-isolation test fix (inspect exact subject).
Worktree /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-prepare-client-releases/haveapi.
New delta only servers/ruby/spec/performance/release_lineage_spec.rb (confirm
actual path), +47/-18. Whole final diff19files+141/-35. All production, benchmark,
budget, reference, workflow, version and changelog bytes unchanged since original
review. No migrations/repeated updates/obsolete version or compatibility stream.
No version0.31.1 changes occurred.

## Cause and corrective design

Branch40551776399 and tagged40551850652 both failed637examples/7failures because
synthetic0.30 patch lineage spec fixture construction read actual root0.31.0 and
passed it into intentional0.30-only normalizer before substituting version.
Other real-input and HTML examples also assumed live checkout0.30. This is a
source/test fixture defect, no network/transient or upload failure. See saved
haveapi-ci-*-failed.log/status. Artifact API total_count0; no accepted artifact,
registry upload, protected approval or PHP update.

Architect independently confirmed and appended bounded brief to design.md.
Fix reads template own VERSION without calling narrow production guard; uses
owned synchronized0.30.2 source for Worker input/HTML examples; scopes loaded
version constants only within receipt test. Existing served HTML adaption remains.
Preserve production minor guard,0.30.99 mismatch rejection and actual worker/replay
logic. Add synchronized0.31 rejection and one recurrence test: template fully
synchronized0.32, helper derives working0.30.2 fixture, production rejects0.32
with intentional0.30-contract error. Inspect restoration/isolation and meaningful
future-minor coverage. No generalized fixture framework or application change.

## Authorization / operation boundary

User initially accepted0.31.1, then explicitly redirected: since0.31.0 was not
actually released, fix it up and try again (corrected typo to0.31.0). Lead accepted
this as direction to retain0.31.0 and replace exact failed/unaccepted tag after
source fix, checks and independent review, overriding project conservative new
patch policy for this exact failed tag. Old annotated object
73eb7726a245804b8aa3abdff9181772f827d2d9 peels3bbb98e7; preserve old identities/logs
in receipts, update only after final verification using exact-old-object lease.
No tag replacement/push or retry yet. No master integration approval.
SDK user publication0.1.0 is independently verified with exact retained integrity;
its source/artifact is unchanged and excluded from this rerun.
PHP preparation remains waiting successful actual tagged artifact and later
explicit master/tag/PHP-first integration approval.

## Evidence / requested review

Focused pinned Nix make doc +18 lineage specs passed at actual root VERSION0.31.0,
0failures(seed63695,8.55s), targetedRuboCop clean. Normal mandatory i18n/RuboCop
hooks passed; no bypass. Source fix committed; no full batch/push/replacement.
Details/logs retained by implementer0 in session haveapi-fixture* files.

Run independent affected final review with general, architecture/repetition,
scope/proportionality, risk/compatibility references. Read each in full and the
mandatory-change-review skill. Review new test design/guard semantics and whole
final history conclusion; original metadata/SDK evidence can be reused. Saved
reviewer0 gpt-6.1-sol/xhigh/read_only, no overrides. No nested agents/checks/builds.
Return report text for lead to save fixture-review.md, including findings,
explicit no-obsolete-history/no-repeated-stream/no-migration conclusion.
