# INVALID premature watcher report

The report below is retained as received and is not accepted evidence. Actual
log shows focus2 passed20.8s, then full A began; no terminal full-A result was
retained. The watcher ended while its command item was in progress; recovery
reported Unknown process id39312. Exact server691415/npm691400 remained
orphaned. Owner2 is reconciling exact effects before another run. See state.md
and webui-browser-core-profile-fixed.log for the corrected disposition.

---

# Browser verification result

- Tested revision: `1bfad6ce1846aef2d21bb6a58d4529a962e7aa97`
- Command: assigned fixed command, invoked once
- Exit status: 1
- Elapsed: about 6 seconds
- Stage evidence: log reports `Running 2 tests using 2 workers`; profile spec ran on `[chromium]` and `[mobile-chrome]`. Full A18 stage was not reached.
- First failure: `Error: Process from config.webServer was not able to start. Exit code: 1`
- Log: `webui-browser-core-profile-fixed.log`
- Artifacts: none reported in captured log
- Cleanup: after command exit, port 5187 remained open (`port_5187_open`).
