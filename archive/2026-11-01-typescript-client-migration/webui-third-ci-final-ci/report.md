# WebUI final CI watcher result

Result: **failed**. Both pinned workflow runs are terminal. All evidence is for `vpsfreecz/vpsadmin-webui` head `20aa0e9ea7568747f048242077f0cf15a325d990`, attempt 1. No rerun, cancellation, workflow dispatch, or other run control was issued by this watcher.

## Runs and job conclusions

| Run | Job ID | Conclusion | UTC start → completion | Elapsed |
| --- | ---: | --- | --- | ---: |
| CI `41508552632` | `125494067403` Required nonbrowser checks | success | 19:17:31 → 19:22:45 | 5m14s |
| CI `41508552632` | `125494067555` Production build | success | 19:17:31 → 19:18:37 | 1m06s |
| CI `41508552632` | `125494067994` Chromium script regression | success | 19:17:31 → 19:20:11 | 2m40s |
| Playwright smoke `41508552554` | `125494067761` Chromium | cancelled | 19:17:31 → 19:58:18 | 40m47s |
| Playwright smoke `41508552554` | `125494068046` mobile-Chrome | cancelled | 19:17:41 → 19:58:12 | 40m31s |
| Playwright smoke `41508552554` | `125494068271` mobile-WebKit | success | 19:17:31 → 19:40:43 | 23m12s |

The metadata timestamps are UTC and durations are mechanically derived from them. Smoke run conclusion is `cancelled`; both Chrome job annotations explicitly say the job exceeded the 40m0s maximum execution time. Cancellation actor/cause is not established.

## Native Playwright observations

- **mobile-WebKit:** annotation and run log summary: 274 passed, 2 skipped, reported test time 21.7m. No flaky/retry observation found in the completed WebKit output.
- **mobile-Chrome:** no final all-cases summary was produced before the 40-minute cap. The retained log shows retry #1 and retry #2 observations, test timeouts, and assertion failures; examples include the VPS stop confirmation remaining visible after retry and 90-second test timeouts in lifecycle and private-IP scenarios. Do not treat this as a complete pass/fail case count.
- **Chromium:** no final all-cases summary was produced before the 40-minute cap. The retained log shows retry #1 and retry #2 observations and 90-second timeout failures, including lifecycle configuration and VPS power stop scenarios. Do not treat this as a complete pass/fail case count.

There is no evidence here of a flaky test finally passing; retry attempts and failures are reported as observed, without assigning a root cause.

## Evidence files

Raw run metadata, per-job metadata, annotations, complete available smoke run log, and artifact inventory are in `work/2026-11-01-typescript-client-migration/webui-third-ci-final-ci/`:

- `ci-run.json`, `ci-run.log`
- `smoke-run.json`, `smoke-run-latest.json`, `smoke-run.log`
- `chromium-job-final.json`, `mobile-chrome-job-final.json`, `mobile-webkit-job-final.json`
- `mobile-chrome-annotations.json`, `mobile-webkit-annotations.json`, `chromium-annotations.err`
- `smoke-artifacts.json`

Four artifacts were listed by the run: Chromium test results (ID `13175251820`, 132,233,790 bytes, SHA-256 `d4e1874908335f1b28a9d5ef6197fb810563e03a1e3db1afac1d4e320d114224`); mobile-Chrome test results (ID `13174362819`, 94,461,738 bytes, SHA-256 `fd32c2d12167fe7d68f137bf102dc9183a84fe72bdfe760ea27c9383bcf7f58f`); mobile-WebKit report (ID `13173361437`, 2,529,089 bytes, SHA-256 `4920588c39ba78d9467c41b4d63c42c4210f36e3a5cca71455953f61fb09c7c5`); mobile-WebKit test results (ID `13173029184`, 17,423,857 bytes, SHA-256 `f807a19d472158dba4e1ad98164b384b30747e70bd7df80ae9fe695f522b03b1`). Artifacts were inventoried, not downloaded.

The first smoke log request while the run was active returned “logs will be available when it is complete”; the post-terminal full log fetch succeeded (517,270 bytes). A guessed job-ID annotations endpoint returned HTTP 404; final check-run annotations were retained where available. No failure cause beyond directly emitted runner annotations/log observations is asserted.

The parent owns acceptance and all subsequent actions. No source, Git, index, initiative state, design, or portal files were changed.
