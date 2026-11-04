# WebUI browser core payments verification result

- Result: failed (exit status 1).
- Tested revision: `6fabda0b80e04fde4490f22ed079c83ae899f0e1` in `worktrees/2026-11-01-typescript-client-migration/vpsadmin-webui`; checkout was clean before the run.
- Command identity: direct `bash` execution of `webui-browser-core-payments-fixed-command.txt`, with the five requested E2E variables unset. Run once; no retry.
- Duration: approximately 2 minutes 6 seconds (reported by Playwright as 2.1m).
- Counts: 33 passed, 1 failed, 1 interrupted, 89 did not run (124 total planned).
- First failed case: `[chromium] e2e/specs/app/security_advisory_update_mutations.spec.ts:61:1` — `@pr-smoke edits and deletes an advisory update with confirmation and refreshed readback`; assertion at line 117 expected `[{}]`, received a nested `security_advisory_update` object.
- Interrupted case: `[chromium] e2e/specs/app/session_expiry_redirect.spec.ts:5:1` — `@smoke expired session redirects to public overview with a fresh notice`.
- Full stdout/stderr log: `webui-browser-core-payments-fixed.log`.
- Playwright artifacts: `work/2026-11-01-typescript-client-migration/browser-6fabda0b-nix1228/core-results`; failure screenshot, video, error context, and trace are present for the first failed case. The interrupted case also has screenshot, video, error context, and trace paths in the log.
- Native cleanup/port: command process exited; the Playwright log contains no explicit server shutdown or port-release confirmation. Cleanup/port status is therefore unverified.
- No retries or additional checks were run.
