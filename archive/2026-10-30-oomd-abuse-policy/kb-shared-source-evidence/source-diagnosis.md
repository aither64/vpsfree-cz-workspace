# Source-check failure diagnosis

Original full check exited1 after about64s on staged9ffcfb0a/appf60; two earlier
groups passed. Full stdout was not redirected by the utility; only partial PTY
output exists. Do not call its missing log complete. Result JSON is preserved.

Actual reported failure: RunnerSessionTest public-stop fixture, line1728, child
identity array changed during successful shutdown: Ruby STDIN.read argv became
empty. Initial4child identities were live/matching; shutdown/exit assertions
before the failing equality passed. Native event reconstruction pending.

Source hashes prove test-machine/kb_process/devcluster_runner/kb_machine/bin/check
unchanged from basece2 and prior1119 to staged. No contract drift observed; source
contract phase was not reached.

ProcessIdentity.read reads stat first, excludes Z, then exe then cmdline. Exit can
occur between those reads. cmdline can be empty during exit despite earlier
non-Z stat/exe. Discover stores each record over the same PID/start_ticks key,
so such a partial observation can replace a previously retained complete argv.
The synthetic stand-in VM uses a dedicated pipe; PTY stdin is not its input.
This is a concrete race hypothesis, not deterministic proof yet.

Lead authorized one narrowly targeted actual failing test with complete native
redirection after diagnosis. No whole-check rerun, sleep, weakened assertion,
private runtime helper or foreign cleanup. Baseline code fix requires separate
smallest-change/negative-control proposal before edits.

The single authorized targeted test passed (native exit0,14.01s,1run57assertions)
on the unchanged staged tree. Full redirected log/result retained. This does not
erase the original full-check failure or establish that PTY caused it. The
assertion's observed mutation and separate proc reads support an intermittent
shutdown observation race; deterministic negative control and any baseline fix
remain a separate source scope decision. No full batch retry has been launched.
