# Control-thread shutdown and fixture diagnostics

The hosted machine/session suite at K a1897006 reported three public-stop
errors from `Engine#cleanup_socket`: unrecognized retained socket contents.
An explicit stop in a test body could fail, then the fixture's ensure called
stop again and replaced the first exception. The displayed ensure stack alone
therefore did not identify the first failure.

Preserve the primary exception object and backtrace, mark an explicit stop
attempt before calling it, and retain private native runner/controller logs
plus a bounded socket-directory inventory before removing temporary fixtures.
Report cleanup failures separately. CI-local private copies do not become
available download artifacts unless the workflow explicitly exports them.

The old runner closed its UNIX listener before killing/joining its accept
thread. Since Ruby join can rethrow that thread's exception, interrupted accept
could prevent the runner from unlinking its own control socket. Native failure
logs did not establish that exact interleaving. A deterministic real-listener
barrier test exercises the ordering through the actual public stop command.
K74b0717d joins the thread before closing the listener; both canonical hosted
Checks pass, including machine/session/shutdown12/299. No local test was run.

Complete/all-recorded-processes-gone proof precedes resource release, and
release precedes socket cleanup. A late cleanup refusal can leave claims
released while the phase is not stopped. Do not infer retained claims or an
incomplete process receipt from that error alone.

This correction cannot replace code in a running genuine K68 predecessor.
That crossing requires its own reviewed compatibility boundary. It also does
not establish the disappearance/finalization cause of the retained incomplete
G4/G6 real campaigns or grant cleanup authority over them.

Session: work/2026-10-05-network-ipv4-left-counter; evidence:
finish-k-runner-shutdown-diagnosis1.json and
finish-k-runner-shutdown-canonical-acceptance1.json.
