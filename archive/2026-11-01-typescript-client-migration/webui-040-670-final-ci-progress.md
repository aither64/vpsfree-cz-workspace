# Final CI watcher milestones

- 2026-11-03: Exact attempt-1 CI run 41691007867 and smoke run 41691007905 validated against repository, pull_request event, branch and feature head 670cf286daf9bddb65594035507ca112a9e6d397. Source checkout HEAD/tree matched the supplied values. Current-session verification CLI was unavailable (`wrong number of arguments for current`); environment identity variables match.
- CI completed success at 18:13:01Z. Jobs: Production build 126109269440; Chromium script regression 126109270033; Required nonbrowser checks 126109270148. Logs and available artifacts retained in `ci-670-final/`.
- Smoke milestones: mobile-webkit 126109271856 success (274 passed, 2 skipped); chromium 126109271988 success (632 passed); mobile-chrome 126109271134 success (574 passed). All completed by 18:36:25Z. Full logs and downloaded reports/results retained in `ci-670-final/`.
- All five GitHub checkout logs identify the PR merge checkout SHA 75c58bf57f10d6017d8e75bbeed6021e0558bc78 with message merging feature head 670cf286 into base 1c8478b. A 3-second base SHA fetch timeout appears in smoke `GitCommitInfo` lines; the actual merge checkout and workflows succeeded.
