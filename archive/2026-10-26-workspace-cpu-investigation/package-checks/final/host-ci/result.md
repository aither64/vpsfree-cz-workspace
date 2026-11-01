# Final host CI observation

- Run: `aither64/dev-workspace` / 40404893088
- Tested head: `0fd31c1fa8858ef15d516e58c883f8dea9aa727e` (exact expected SHA)
- Final run conclusion: `cancelled` (completed)
- Jobs: `host` success; `archive`, `fast`, and `creation` cancelled by @aither64.
- `host` job 121859999869 passed “Activation, renewal, rollback and user-service boot tests” in 8m39s.
- Watch command exit status: 1 because the run was cancelled. The fast build and creation job were interrupted; their status does not establish pass/fail.
- The run watch remained attached until all jobs reached terminal state. No still-running operation.
- Full watch output: `watch.log`.
