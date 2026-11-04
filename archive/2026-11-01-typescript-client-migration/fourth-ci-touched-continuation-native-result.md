# Fourth CI touched continuation native result

- Native Playwright exit: `1` (durable exit JSON: `exit_code: 1`).
- Tested WebUI HEAD: `be42b595a2a1746c55842cbfc0a6786d015fead6`.
- Native process identity: PID/PGID/SID `1446111`, start ticks `25678823`.
- Started UTC: `2026-11-02T21:26:32.012014+00:00`.
- Finished UTC: `2026-11-02T21:28:31.307212+00:00`.
- Elapsed: `119.295` seconds (durable exit JSON; UTC difference approximately `119.295198` seconds).
- Summary: `14 passed`, `1 failed`, `2 interrupted`, `113 did not run`; stopped at maximum allowed failures.
- First failed case: `e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:239:3`, “posts legacy rescue boot payload”. Error: test timeout of `90000ms`; `page.waitForRequest` at `e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:252` timed out waiting for a POST matching `/api/v7.0/vpses/123/boot`.
- Trace: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-fourth-ci-touched-continuation/results/app-vps_lifecycle_tab_acti-71d52--legacy-rescue-boot-payload-chromium/trace.zip`.
- Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation-observed.log`.
- Durable state: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation-observed-state.json`.
- Durable exit: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation-observed-exit.json`.
- Browser report/results: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-fourth-ci-touched-continuation/report` and `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-fourth-ci-touched-continuation/results`.
