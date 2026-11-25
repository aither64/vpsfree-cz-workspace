# Existing GitHub Actions run observation

Repository: `vpsfreecz/vpsadmin`
Head: `f60d41a453b1703e42de4341285bdc6ba339aff0`
Observed 2026-10-31 UTC.

## API topic aggregate (41185457084)

Conclusion: success. 26 RSpec topic jobs completed successfully. Downloaded 26 result files report 9,456 examples, 0 failures, 412 pending; environments and selected-spec manifests are retained alongside them. The aggregate and job identity are in `shared-f60-api-completion-status.json` and `shared-f60-api-completion-jobs.tsv`; artifacts are under `shared-f60-api-completion-artifacts/`.

## Integration CI (41185457135)

Conclusion: failure; workflow job `Run selected ci-tagged tests` failed. The `Run tests` step failed with exit code 1 after 18,752.4 seconds. Native final counts: 118 tests successful; 1 test expected to succeed but failed; no expected failures or unexpected successes. The named failed script is `webui#incident-escalation`. `webui#vps-admin-ops` also appears in the runner's failed-script set, though final summary names only the incident-escalation script as the expected-success failure. The assigned alert scenario `alerts/incident-escalation` itself completed successfully (its example passed; test duration 613.1 seconds). Selection preview listed both alert and WebUI incident-escalation tests, and logs later confirm WebUI test execution.

Native run status and conclusion: `shared-f60-ci-completion-status.json`, with compact job summary in `shared-f60-ci-completion-summary.json`. Full native job log: `shared-f60-ci-completion-log.txt`. All downloadable runner, per-scenario results, environment/manifests and VM logs are preserved under `shared-f60-ci-completion-artifacts/`; 119 per-test result records were found. No images were downloaded. No rerun or diagnosis was performed.
