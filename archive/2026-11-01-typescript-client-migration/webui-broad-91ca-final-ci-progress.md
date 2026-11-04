# CI watcher progress: 91ca final

Started observing 2026-11-03. Session slug and environment match. Actual WebUI CWD is clean at head `91ca5ab44d07d62a8226f5a2b774747a44ff2c0d`, tree `f17966b814588c9b90afc8cf302fdb13130c87b4`, base `670cf286daf9bddb65594035507ca112a9e6d397`.

All four requested exact runs validated as attempt 1, branch `dev/typescript-client-migration`, head above: 41724380477 (push, broad smoke), 41724392747 (pull_request, CI), 41724392828 (pull_request, smoke), 41724392837 (pull_request, broad smoke). Initial job inventories total 10 and are retained in `ci-91ca-final/*.initial.json`. PR #133 is open with base main at the stated base SHA. All jobs had started; selected CI jobs were already successful, while suite and browser jobs remained in progress at capture.

A single sequential native `gh run watch --exit-status` operation owns these four existing runs; no workflow controls were used. Watch logs and eventual terminal metadata are in `ci-91ca-final/`.

## Terminal outcome

All four exact attempt-1 runs completed success; all 10 jobs completed success. Native watch command exit codes are retained in `ci-91ca-final/watch-exit-codes.txt` and are all 0. Full logs were fetched once per run into `ci-91ca-final/<run-id>.log`; terminal API metadata is in the matching `.terminal.json`.

Push broad smoke run 41724380477 records 239 passed and 1 skipped in Chromium, 96 passed in mobile Chrome. The Chromium suite had one initial failed assertion in `admin/nodes_issues_only_filter.spec.ts` and a passing retry (one flaky test). PR broad smoke records 238 passed and 1 flaky in Chromium, 96 passed in mobile Chrome. PR smoke records 632 Chromium passed, 274 WebKit passed and 2 skipped, and 574 mobile Chrome passed. CI unit tests report 348 files / 2,271 tests passed; skip counts shown by script regressions and BFF suites are zero.

Every PR job log identifies merge checkout `1eb72d4ceaa425af33e259f431ed33f3b6a39ed7`, merge message `Merge 91ca5ab… into 670cf286…`. Push logs checkout the literal requested head. Logs do not provide complete tree/parent evidence for every job; no tree claims are made for those checkouts. GitHub emitted the Ubuntu runner image migration annotation on broad smoke jobs. No tests were rerun or workflow controls used.
