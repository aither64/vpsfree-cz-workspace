# Hosted CI observation: network layout V12 / K

Observation batch completed on 2026-10-08. This report covers only the pre-existing run IDs in the watcher handoff. All vpsadmin V runs tested `12a3cb677ee0482cad9f61fbb70a401283da82e6`; the vpsfree-kb-contracts run tested `abadbcc4849ec6f83274e145d47c88060ef499a4`.

| Repository | Run | Event | Result | Job summary |
| --- | ---: | --- | --- | --- |
| vpsadmin | 37784450080 | pull_request | success | API Specs (topic parallel), 27/27 jobs successful |
| vpsadmin | 37784450087 | pull_request | success | RuboCop |
| vpsadmin | 37784450088 | pull_request | success | API Migration Specs |
| vpsadmin | 37784450128 | pull_request | success | Webui PHPUnit |
| vpsadmin | 37784450029 | pull_request | success | libnodectld Specs |
| vpsadmin | 37784449999 | pull_request | success | i18n health |
| vpsadmin | 37784439880 | push | success | API Specs (topic parallel), 27/27 jobs successful |
| vpsadmin | 37784439846 | push | success | Webui PHPUnit; parent retained its standalone native 107/740 receipt |
| vpsadmin | 37784439754 | push | success | RuboCop |
| vpsadmin | 37784439748 | push | cancelled | One CI job; parent authorized cancellation after V12 was superseded |
| vpsadmin | 37784439832 | push | success | i18n health |
| vpsfree-kb-contracts | 37785143508 | push | success | `check` job, all steps successful; static contract/inventory check |

The selected API Specs runs finished successfully: push run 37784439880 completed at 13:57:31Z (about 30m24s after creation), and PR run 37784450080 completed at 14:14:38Z (about 47m27s after creation). Each provided 78 downloaded files containing RSpec file lists, environment metadata, and result JSON under `artifacts/vpsadmin-37784439880/` and `artifacts/vpsadmin-37784450080/`.

CI run 37784439748 started at 14:06:32Z. After the parent published replacement head `7e86ee211d898256bd93cac7221c256636f3fcc3`, the parent authorized cancelling this old-head run. Cancellation completed at 16:56:45Z (run duration 3h29m38s; job duration 2h50m12s), with the job conclusion `cancelled`. Its uploaded `vpsadmin-test-logs-37784439748` artifact contains 782 files under `artifacts/vpsadmin-37784439748/`. Preserve this as cancelled historical evidence; it is not a passing CI result for the replacement head.

K run 37785143508 completed at 13:43:31Z (11m06s after creation). It returned no valid downloadable artifacts. The selected K check provides static contract/inventory success; it provides no image-freshness proof. Successful browser PNG export availability remains unknown, and no local browser was run.

Final run metadata and jobs are in `snapshots-final/`. Native run logs are in `native-logs/`, except vpsadmin Webui PHPUnit run 37784439846, whose standalone native receipt was already captured by the parent and was not overwritten. Watcher traces for the four asynchronously watched runs are `watch-*.log`. Download status records are kept beside each artifact directory. No selected run remains ongoing.
