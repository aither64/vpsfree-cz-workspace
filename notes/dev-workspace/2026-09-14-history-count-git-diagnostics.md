# Diagnose Git history-count fixture failures

Organization CI 34886053176 failed TestReviewTotalMatchesFullHistoryAcrossPageBoundaries
at count 101 with Git exit 128. Its companion package suite and runtime CI passed.
The runner had captured but discarded stderr. Preserve it on exec.ExitError and
print it with the tested revision pair, while leaving Error() and the HTTP error
text unchanged.

A 50-run local reproduction failed once with `Could not read <object>` and
`revision walk setup failed`, again at count 101. A separate write-side
GIT_TRACE2_EVENT capture showed `git commit-graph write --split --reachable`
starting at the fixture's 100-commit boundary. This is consistent with a
background commit-graph maintenance race; it does not prove an upstream cause.
[Git documents that automatic commit-graph maintenance defaults to 100 commits](https://git-scm.com/docs/git-maintenance/2.47.1.html).

Configure `gc.auto=0` and `maintenance.auto=false` in this disposable fixture,
as the bulk-rename fixture already does. Production Git configuration is
unchanged. Keep failures as failures; diagnostic reads must never turn a failed
assertion into a passing retry. Verification is recorded in the initiative state.

Related initiative: work/2026-09-14-portal-review-fixes.
