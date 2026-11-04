# WebUI second CI verification

Result: **failed**. Both pinned runs were verified on head `9d9617c048dded592b6362e3370d92cfca2793cb`, attempt 1. Observation elapsed approximately 1h42m from first status read through final native terminal state.

- CI run [41480946099](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480946099): success. `Production build`, `Required nonbrowser checks`, and `Chromium script regression` all succeeded.
- Playwright smoke run [41480945591](https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41480945591): failure. `PR smoke E2E (mobile-webkit)` failed (35m21s); `PR smoke E2E (chromium)` was cancelled; `PR smoke E2E (mobile-chrome)` was cancelled after 40m41s.

Bounded failure excerpts:

- Mobile WebKit: `e2e/specs/app/vps_expiration_reactivation.spec.ts:69`, expected `lifetimes.admin.modal` hidden, received visible after 15s. The run annotations reported seven failed cases for this job.
- Mobile Chrome: `e2e/specs/app/transaction_chain_detail_page.spec.ts:195`, expected `transactions.chain.detail.info` visible, but element was not found after 15s.
- Chromium: final native conclusion `cancelled`; no actor is inferred.

Raw metadata, full available run log, and artifact inventory are in this directory. Artifacts were inventoried only; no archives were downloaded.

Artifacts (inventory only):

- `13163190622` `playwright-test-results-mobile-chrome`, 196441411 bytes, `sha256:4c934f4da547c1ecc1dc36061b4d297cd9aef2bba8119edf87c7a8e9cadfb31c`
- `13162417238` `playwright-report-mobile-webkit`, 57041743 bytes, `sha256:943d2d08c85dc52e778ffb606c32e79283cd7039b63b6efcfec6a033b14ec5ce`
- `13162172353` `playwright-test-results-mobile-webkit`, 74051919 bytes, `sha256:9db2573fd2c03d6f11ad50939a89cd6c4bcefd7e1a2d43ed486857bc3a74a45a`
- `13161334021` `playwright-test-results-chromium`, 313152166 bytes, `sha256:90f0004267ba2ae30f60188e497f05afb906fad946c244316df7b92c7ad7c6d0`

The available run log is retained as `run-41480945591.log`. The attempted job log/annotations endpoint returned HTTP 404; the empty per-job log capture and 404 response are retained without treating them as job output.

The retained final metadata concludes both Chromium and mobile Chrome jobs `cancelled`. Their run log output showed test failures before cancellation: the transaction detail assertion at line 195 occurred in both Chromium and mobile Chrome. This records observed test output and final status separately; cancellation actor is unknown.

The `gh run watch` native command terminated with exit status 1 after the workflow completed. Workflow start was 16:23 UTC and final status was observed at 18:05 UTC (about 1h42m elapsed overall).
