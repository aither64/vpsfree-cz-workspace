# WebUI browser verification result

- Result: failed (command exit status 1).
- Tested revision: `b7bc887e10e46c62684281ace9bb7290d557832c` (`dev/typescript-client-migration`), clean worktree at launch.
- Command: exact invocation of `webui-browser-core-storage-case-fixed-command.txt`, run once from the WebUI worktree. Fixed command SHA-256: `$(sha256sum /home/aither/workspace/ai/vpsfree.cz/work/2026-11-01-typescript-client-migration/webui-browser-core-storage-case-fixed-command.txt | cut -d ' ' -f1)`.
- Elapsed: approximately 4 minutes (single shell command; wall time from launch to exit).
- Focused case: 1 passed (15.5s).
- Full suite: 124 cases scheduled; 59 passed, 1 failed, 64 did not run; stopped at maximum 1 failure (3.9m). First failure: `[chromium] e2e/specs/app/vps_storage_tab_mounts.spec.ts:326` (“deletes mount via confirm dialog”); `toBeHidden()` timed out because `vps.storage.mounts.delete_confirm` remained visible. This records the test output only, without diagnosis.
- Log: `webui-browser-core-storage-case-fixed.log`.
- Failure artifacts: `browser-b7bc887e-nix1228/core-results/app-vps_storage_tab_mounts-6ec10-es-mount-via-confirm-dialog-chromium/test-failed-1.png`, `video.webm`, `error-context.md`, and `trace.zip`.
- Focused artifacts: `browser-b7bc887e-nix1228/focus-results` and `browser-b7bc887e-nix1228/focus-report` (as configured by the fixed command).
- Cleanup: native Playwright command exited; port 5187 was checked after exit and has no listener.
