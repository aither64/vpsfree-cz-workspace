# Fourth CI touched continuation 2: native result

- Result: failed (native command exit status 1; 12 passed, 1 failed, 1 interrupted, 106 did not run; one runner error outside a test).
- Tested WebUI revision: `a27a076877f2227dbd5d23f82765740937a62a2e`.
- Command identity: observer `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation2-observed.py`; operation PID/PGID/SID `1725007`, start ticks `25849614`; started `2026-11-02T21:54:59.927977+00:00`, finished `2026-11-02T21:56:05.241355+00:00`, elapsed 65.313 seconds.
- Observer SHA-256: `9b15029f4924829685e0edee911dfcbf08b1e301b66b0d1cf6f57f92929c5661`.
- Command SHA-256: `f4ab33aa3d92fae80a0c12c026c384a356336c6c858fe43d12262a897c76555f`.
- Native output: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation2-observed.log`.
- Durable observer exit: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/fourth-ci-touched-continuation2-observed-exit.json` (exit 1).
- Failure: `e2e/specs/app/vps_lifecycle_tab_actions.spec.ts:293`, “focused lifecycle start action posts start endpoint”; assertion at line 310 expected `{}` and received `{"vps":{}}`.
- Retained failure artifacts: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-fourth-ci-touched-continuation2/results/app-vps_lifecycle_tab_acti-9c6fc-action-posts-start-endpoint-chromium/` (screenshot, video, error-context.md, trace.zip).
- A second test was interrupted by max-fail stopping: `e2e/specs/app/vps_resource_workspace.spec.ts:183`, “does not expose root resizing to a member”; artifacts are retained under `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-fourth-ci-touched-continuation2/results/app-vps_resource_workspace-b6ce4-e-root-resizing-to-a-member-chromium/`.
