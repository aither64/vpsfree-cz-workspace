The authorized continuation run failed with exit status **1** after **115.406 seconds**: **15 passed, 1 failed, 1 interrupted, 161 unrun**.

The failure was a 90-second timeout in `security_advisories_admin.spec.ts:125`, waiting for `admin.security_advisories.nodes.editor.state`. The next test was interrupted when maxfail stopped the run. I did not diagnose or retry.

The observer log, terminal receipts, and browser artifacts are retained under the session root. I recorded the result in [second-ci-touched-continuation-native-result.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/second-ci-touched-continuation-native-result.md).