# Runit command waits differ from test-runner timeouts

In supervisor/runtime-ingestion, `node.succeeds('sv stop nodectld', timeout: 30)`
failed after 7.61 seconds: `timeout: run: nodectld ... want down, got TERM`.
The test-runner timeout only bounds the process; `sv` has its own default
seven-second wait. The nodectld wrapper allows 60 seconds before escalating
its child shutdown, so a busy daemon can legitimately exceed seven seconds.

Use `sv -w 90 stop nodectld` with a 120-second test-runner timeout, and protect
the stop with an ensure block that restores the reporter. Apply the explicit
wait to start as well. This fixes the integration harness's wait mismatch;
it does not change nodectld shutdown semantics. The observed wrapper also
logged ESRCH at later escalation, recorded as out-of-scope daemon behavior.

Related initiative: work/2026-09-14-kernel-history-fix. Final verification of
the revised scenario is recorded in its state.
