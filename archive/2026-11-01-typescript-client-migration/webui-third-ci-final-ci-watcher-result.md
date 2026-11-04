Result: **failed**. Both pinned runs are terminal on head `20aa0e9ea7568747f048242077f0cf15a325d990`, attempt 1.

- CI `41508552632`: all three jobs succeeded — nonbrowser checks (5m14s), production build (1m06s), Chromium script regression (2m40s).
- Smoke `41508552554`: mobile-WebKit succeeded (23m12s); Chromium was cancelled (40m47s); mobile-Chrome was cancelled (40m31s). Both Chrome jobs’ annotations state they exceeded the 40-minute execution limit. The cancellation actor/cause is unknown.
- WebKit’s native summary reports **274 passed, 2 skipped** in 21.7m. Chromium and mobile-Chrome have no final all-cases summary; their logs contain retries and test failures/timeouts.

Raw run/job metadata, available annotations, the 517,270-byte terminal smoke log, and artifact IDs, sizes, and digests are saved under [the evidence directory](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-third-ci-final-ci/). The concise report is [webui-third-ci-final-ci-watcher-result.md](/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-third-ci-final-ci-watcher-result.md).

No run controls were used and no source, Git, index, or initiative records were changed.