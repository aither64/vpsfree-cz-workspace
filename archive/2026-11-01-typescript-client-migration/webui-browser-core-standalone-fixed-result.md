# WebUI browser core standalone fixed verification

- Revision: `a89277a6a4bcd7b5849d48f760c9728982c67aa9`
- Command: exact direct `bash` invocation of `webui-browser-core-standalone-fixed-command.txt` with the five specified `E2E_*` variables unset.
- Exit status: `1`
- Time: started 2026-11-01 (UTC); completed 2026-11-01T22:04:24Z (about 2m 15s).
- Strict E2E type gate: passed (`E2E type coverage passed: 102 checked, 180 deferred`; `tsc -p tsconfig.e2e.json --noEmit` completed successfully before browser execution).
- Browser result: 124 planned tests, 26 passed, 1 failed, 1 interrupted, 96 did not run. Playwright stopped at the first failure.
- First failed case: `[chromium] e2e/specs/app/payments_page.spec.ts:9:1 › user payments page: shows status, instructions and history`; expected heading `Payment in CZK` was not found within 15 seconds.
- Other reported browser error: `1 error was not a part of any test` (details are retained in the full log).
- Artifacts: full stdout/stderr at [webui-browser-core-standalone-fixed.log](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-standalone-fixed.log). Playwright output at `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-a89277a6-nix1228/core-results`; HTML report at `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-a89277a6-nix1228/core-report`. Failure screenshot, video, error context and trace paths are listed in the log.
- Native cleanup: command exited; the native Playwright run returned control after its configured failure stop. Port 5187 was free afterward (`ss` showed no listener).
- Worktree remained clean at the tested revision after completion.
