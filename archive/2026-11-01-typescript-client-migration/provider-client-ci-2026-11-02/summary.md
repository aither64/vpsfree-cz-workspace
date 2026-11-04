# Provider client CI observation

Observed 2026-11-02 via read-only `gh run view`. All four requested runs completed successfully (attempt 1) on their requested exact heads. No failed-job logs were needed.

| Repository / run | Head | Conclusion | Job outcomes |
| --- | --- | --- | --- |
| `vpsfreecz/haveapi` / [41461452497](https://github.com/vpsfreecz/haveapi/actions/runs/41461452497) | `52c37027f194ba1141fb7f5e5b6b45828989b126` | success | Validate, test and build: success; Publish approved artifacts: skipped |
| `vpsfreecz/haveapi` / [41461452603](https://github.com/vpsfreecz/haveapi/actions/runs/41461452603) | `52c37027f194ba1141fb7f5e5b6b45828989b126` | success | i18n health: success |
| `vpsfreecz/haveapi` / [41461452542](https://github.com/vpsfreecz/haveapi/actions/runs/41461452542) | `52c37027f194ba1141fb7f5e5b6b45828989b126` | success | Compare endpoint performance: success; Performance gate: success |
| `vpsfreecz/vpsadmin-typescript-client` / [41460425540](https://github.com/vpsfreecz/vpsadmin-typescript-client/actions/runs/41460425540) | `e16663a9e7ed1bbd7e25337b824283f635f47395` | success | build: success; publish: skipped |

The observation ran for about two minutes after session verification. No operations remain active. Per-run raw status, attempt, exact head, URLs, jobs and step conclusions are in the adjacent JSON files.
