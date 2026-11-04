# Browser core storage specification result

- Tested revision: `536a1c5cbc49bb27a50e26af733e9b605e506f1c`
- Command: exact requested fixed command; invoked once, exit status 1.
- Duration: watcher reports about 5 minutes52s; stage log records focus1.0m + full5.7m. Preserve these stage values; the overall watcher estimate is inconsistent.
- Focus suite: 8 passed (1.0m), before the full suite. Parent corrected the watcher summary against the actual retained log; the shell runs focus first.
- Full suite: 90 passed, 1 failed, 1 interrupted, 32 did not run (of 124).
- First failure: `[mobile-chrome] e2e/specs/app/profile_keys_sessions.spec.ts:5` — expected `profile.keys.row.1` visible, but it remained hidden at line 104.
- Log: `webui-browser-core-storage-spec-fixed.log`
- Failure artifacts: `browser-536a1c5c-nix1228/core-results/app-profile_keys_sessions--8a47e-ile-ssh-keys-sessions-flows-mobile-chrome/` (screenshot, video, error context, trace); interrupted test artifacts are under `app-payments_page--pr-smok-5cb57--a-touch-safe-mobile-target-mobile-chrome/`.
- Cleanup: process exited; native runner cleanup completed. Port 5187 was not listening after exit.
