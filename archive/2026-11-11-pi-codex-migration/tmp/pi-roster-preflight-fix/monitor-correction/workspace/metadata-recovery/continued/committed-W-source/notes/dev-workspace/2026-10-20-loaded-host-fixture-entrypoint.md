# Loading workspace-host in fixture executables

`workspace-host` starts its CLI when `$PROGRAM_NAME` contains `workspace-host`,
even when another Ruby script loads it. A generated fixture executable with that
basename must set `$PROGRAM_NAME` to a fixture name before loading the source and
installing private host overrides. Otherwise the real CLI runs too early and
fails its package/service identity check.

The command-coordination systemd fixture initially timed out before its marker
was written. The transient unit's journal exposed this entrypoint error. Its
wait helper now retains the fixture unit journal on timeout, so teardown does
not erase the useful failure evidence. The corrected fixture passed both worker
survival and interruption checks.

Related initiative: `work/2026-10-20-coordinator-command-wrappers/`.
