# Second touched browser verification

- Result: failed; native observer exit 1.
- Revision: `96d9c996f3556a8e5d4322e79c11b0657564d33d`.
- Operation: `second-ci-touched-observed`, launched once through the existing observer; elapsed 155.366 seconds.
- Native outcome: 42 passed, 1 failed, 1 interrupted, 176 did not run. The summary reports one error outside a test.
- Bounded failure evidence: `[chromium] e2e/specs/app/security_advisories_admin.spec.ts:11:3` failed; `[chromium] e2e/specs/app/snapshot_delete_availability.spec.ts:87:5` was interrupted.
- Observer state: `second-ci-touched-observed-state.json`; terminal receipt: `second-ci-touched-observed-exit.json`; full log: `second-ci-touched-observed.log`.
- Artifacts are under `../browser-second-ci-touched/results/`, including the snapshot availability screenshot, video, error context and trace named in the log.
- No running operation is reported by the terminal observer receipt. No diagnosis, retry, or additional cleanup was performed.
