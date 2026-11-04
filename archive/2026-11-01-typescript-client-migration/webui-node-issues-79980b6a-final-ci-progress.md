# WebUI CI observation progress

- Session: `2026-11-01-typescript-client-migration`.
- Repository: `vpsfreecz/vpsadmin-webui`.
- Event head: `79980b6a6607d08cccd252439ced328a250bd5b0`.
- Base: `670cf286daf9bddb65594035507ca112a9e6d397`.
- Observation scope: exact attempt 1 of runs `41734450422`, `41734455856`, `41734455848`, `41734455889` only.
- Identity checks passed in the specified development session and WebUI checkout. Checkout was clean at the specified head/tree.
- All four runs completed successfully; all 10 expected jobs are terminal and successful. No rerun, dispatch, cancellation, approval, merge, deployment, or artifact download was performed.
- Three PR workflows checked out synthetic merge commit `448487d3c55e3c42f78706462fcd4be985a65dd5`, with parents base `670cf286daf9bddb65594035507ca112a9e6d397` and event head `79980b6a6607d08cccd252439ced328a250bd5b0`; merge tree `57d045735c136be50bfee0a832a51653692c00ed`. The push run checked out literal event head.
- CI: 348 test files and 2,271 tests passed; Chromium browser script regression 1 passed; production build and quick checks passed.
- Broad smoke push: Chromium 238 passed, 1 skipped, 1 flaky; mobile Chrome 96 passed. The Chromium log records a first-attempt failure in `admin requests: main input opens a typed ID or selects an applicant without request q`, followed by a passing retry/final run. Run conclusion is success; it is not a clean first-attempt pass.
- PR smoke: Chromium 632 passed; mobile Chrome 574 passed, 2 skipped; mobile WebKit 274 passed, 2 skipped.
- PR broad smoke: Chromium 239 passed, 1 skipped; mobile Chrome 96 passed.
- Full terminal metadata and logs are in `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/ci-79980b6a-final/`. Failed-attempt report/results artifact IDs for push broad Chromium: report `13277954688`, test results/traces `13279525188`. They were not downloaded.
- Terminal structured summary: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-node-issues-79980b6a-final-ci-result.json`.
- Final watcher report: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-node-issues-79980b6a-final-ci-watcher-result.md`.
