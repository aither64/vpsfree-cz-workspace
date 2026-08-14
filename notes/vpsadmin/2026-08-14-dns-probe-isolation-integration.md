# DNS probe isolation integration tests

Initiative: `work/2026-08-12-dns-secondary-zone-transfer-failure`

The real-DNS scenario wrapped each packaged probe worker with assertions for a
dynamic non-root UID, inaccessible nodectld state and a blocked connection to
the other primary. The transient units all exited before the packaged worker
on one host even though the systemd isolation properties were present.

The wrapper rescued only `Errno::EACCES` for an inaccessible directory and
`Errno::EACCES`/`Errno::EPERM` for the denied network destination. Kernel and
systemd combinations may surface another `SystemCallError`, or a connection
timeout, for the same enforced boundary. Rescue the broader syscall family and
`IO::TimeoutError`, while still aborting when directory access or the blocked
connection actually succeeds. The real worker executing afterward proves that
the selected primary remains reachable.

Do not require a transient failed path state after injecting a passive BIND
diagnostic. The independently scheduled probe may update current state before
the API poll. Assert that the meaningful BIND diagnostic remains in history,
then assert the intended eventual state transition. Routine successful probes
may be deliberately absent from history under transition-only retention.

Nix parse/format, CI selection, range diff-check and repository hooks passed
after the correction. The long scenario rerun remains the definitive runtime
verification.
