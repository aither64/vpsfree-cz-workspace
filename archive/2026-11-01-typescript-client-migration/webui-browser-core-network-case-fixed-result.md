# Fixed browser verification result

- Revision: `337b3be5b6f0933e5fefe6308cf6fbb9ec6d22c5`
- Command: exact one-time invocation of `webui-browser-core-network-case-fixed-command.txt` from the specified WebUI worktree, with the five requested environment variables unset.
- Exit status: 1
- Elapsed time: 221.7 seconds
- Focus stage: completed; 1 passed, 0 failed (24.0s).
- Full stage: started after focus passed; stopped by `--max-failures=1` after 1 failed test and 1 interrupted test: 46 passed, 76 did not run. The first failure was `user requests: independent ID spaces paginate the complete merged history without skips`; it timed out waiting for `app.requests.row.change.2` to be visible (15s). The following network test was interrupted. No retries.
- Log: `webui-browser-core-network-case-fixed.log`
- Artifacts: focus and core HTML reports under `browser-337b3be5-nix1228/focus-report` and `browser-337b3be5-nix1228/core-report`; Playwright failure screenshot, video, error context and trace are under `browser-337b3be5-nix1228/core-results` (paths are listed in the log).
- Cleanup: owned command exited; port 5187 has no listener.
