**Verification result: failed**, exit status 1. The command ran once at head `337b3be5b6f0933e5fefe6308cf6fbb9ec6d22c5` and took 221.7 seconds.

- Focus case: **1 passed** in 24 seconds.
- Full suite: **46 passed, 1 failed, 1 interrupted, 76 did not run**. It stopped at the first failure: the user requests pagination test timed out waiting for `app.requests.row.change.2`.
- Port 5187 is free after exit. No retry was run.

The requested log and result are at [webui-browser-core-network-case-fixed.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-network-case-fixed.log) and [webui-browser-core-network-case-fixed-result.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-network-case-fixed-result.md). Playwright reports and failure artifacts are under `work/2026-11-01-typescript-client-migration/browser-337b3be5-nix1228/`.