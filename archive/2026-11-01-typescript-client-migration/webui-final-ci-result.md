# vpsadmin-webui final CI observation

- Final snapshot: 2026-11-02 00:56:19 UTC
- Repository: `vpsfreecz/vpsadmin-webui`
- PR: [#126](https://github.com/vpsfreecz/vpsadmin-webui/pull/126), OPEN; base `main`
- PR head SHA: `14cfdcb6d2a3bc337fd445932fd38916b3dcd9ab`
- Event: `pull_request`; both workflow runs report this same head SHA.

## Runs

| Workflow | Run ID | URL | Final status | Conclusion |
| --- | ---: | --- | --- | --- |
| CI | `41366168908` | https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168908 | completed | success |
| Playwright smoke | `41366168907` | https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168907 | completed | cancelled |

CI jobs passed: Chromium script regression (`125026671033`), Required nonbrowser checks (`125026671322`), Production build (`125026671360`).

Playwright smoke jobs all ended `cancelled`: chromium (`125026671252`, https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168907/job/125026671252), mobile-webkit (`125026671379`, https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168907/job/125026671379), mobile-chrome (`125026671433`, https://github.com/vpsfreecz/vpsadmin-webui/actions/runs/41366168907/job/125026671433). GitHub reported each as running its E2E step for about 40 minutes, then showed `Upload Playwright traces` for chromium and mobile-chrome while mobile-webkit still showed `Run PR smoke E2E`. At 00:56:19 UTC the run and all three jobs were completed with `cancelled`; no job had a `failure` conclusion. Direct log requests while the jobs were active said logs would be available when complete. No failure excerpt or artifact names were collected.

## Result

INCOMPLETE for required Playwright smoke checks: GitHub's terminal conclusion was `cancelled`, not success or failure. CI workflow conclusion was success. PR remained OPEN at the exact head above on last checked status. The observation did not initiate a cancellation, retry, rerun, dispatch, or other CI action. The source of the cancellation is unknown from the observed status; parent owns follow-up and acceptance.
