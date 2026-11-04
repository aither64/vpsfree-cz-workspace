# Browser core request case fixed run result

- Result: failed; command exit status 1.
- Tested revision: `4b69fe0b87f56402703550d17ba9f1a9ac4f083a`.
- Command: `bash /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-request-case-fixed-command.txt` with the five specified E2E variables unset.
- Elapsed time: approximately 6 minutes 15 seconds (started near 22:57:46 UTC, ended 23:04:01 UTC on 2026-11-01).
- Focused case: 1 passed, 0 failed; full suite ran.
- Full suite: 64 passed, 1 failed, 1 interrupted, 58 did not run; stopped after first failure.
- First failure: `[chromium]` `e2e/specs/app/vps_storage_tab_mounts.spec.ts:148` — timed out waiting for `vps.storage.root_dataset.create_subdataset` at line 179.
- Log: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-request-case-fixed.log`.
- Artifacts: `/home/aither/workspace/ai/vpsfree.cz/work/browser-4b69fe0b-nix1228/core-results/app-vps_storage_tab_mounts-4780e--the-VPS-storage-entrypoint-chromium/` (screenshot, video, error context, trace); interrupted test artifacts are also listed in the log. HTML report directories: `/home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/browser-4b69fe0b-nix1228/focus-report` and `.../core-report`.
- Cleanup: command exited; port 5187 had no listening socket when checked at 23:04:01 UTC.
