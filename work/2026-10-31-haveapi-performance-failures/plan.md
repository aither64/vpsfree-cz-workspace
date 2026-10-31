# 2026-10-31-haveapi-performance-failures

## Goal

Investigate gh workflows failures for haveapi, the performance tests failed on current master. Suggest a solution.

User follow-up approved implementation, verification and merge: "agreed. implement the fix, verify and merge". Apply the accepted narrow solution and integrate into HaveAPI `master` after checks and independent final review.

## Affected repositories

- `haveapi`: performance CI resolver, regression tests and `doc/performance.md`.

## Approach

- Architect `architect0` owns workflow/log inspection and root-cause analysis.
- Compare failed assertions and benchmark metrics against comparable successful runs and source history.
- Lead assesses the evidence and presents a minimal proposed solution with verification criteria.
- Implementer0 owns the complete bounded execution package in `design.md`: source, regression tests, technical documentation, quick checks, commits and follow-up fixes. Reviewer0 independently reviews committed changes. Lead owns verification coordination and approved merge.

## Decisions

- Initial investigation scope is now extended to the approved resolver fix, verification and HaveAPI `master` merge. No deployment or release requested.
- Use the retained Full-team roster and preserve member settings; a single investigation owner is sufficient.
- Confirmed failure is a new release branch pointing at current master, with no distinct comparison baseline. Recommend explicit no-work resolution for that validated quick new-branch case; retain rejection of other equal-source comparisons.

## Compatibility and deployment

- Identify whether the proposed solution changes runtime/API behavior or only benchmark methodology. No deployment in this task.

## Documentation

- Readers: HaveAPI maintainers deciding how to address failed performance checks.
- Keep evidence and proposed fix in session `design.md`, with summary in `state.md`; update the equal-endpoint rule in HaveAPI `doc/performance.md` with implementation.

## Testing plan

- Inspect exact failed runs/jobs and artifacts, compare with successful controls and implementation of the assertions.
- Prefer existing CI evidence and bounded read-only analysis; identify follow-up checks for the proposed fix. No long benchmark campaign unless needed to distinguish remaining causes.
- Prospective regression checks: branch created at default head or an ancestor produces no-work; a branch with unique relevant commits still compares; manual/existing-push equal pairs and missing/unrelated source histories still fail. Preserve maintenance-lineage and weekly fixed-reference tests.
