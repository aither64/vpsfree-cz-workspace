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

The next real-DNS run showed two additional integration details. A primary's
first active readiness check may validly use `axfr_probe`, not `ixfr_probe`,
when the managed secondary has no local serial yet. Tests that need to prove an
active check should accept both and reserve an exact IXFR assertion for a
fixture that first establishes a local serial.

Deleting a DNS primary or zone uses transaction confirmations whose success
path removes rows with raw SQL. ActiveRecord `dependent` callbacks therefore
do not run. Any dependent readiness rows must be explicit `just_destroy`
confirmations in the same transaction, registered while holding the shared
server-zone lock. This preserves them on transaction failure/rollback and
prevents a concurrent event consumer from recreating state during deletion.

Registering existing dependent rows is not sufficient by itself. The endpoint
remains in `confirm_destroy` until the remote transaction finishes, so a
delayed event can arrive after the registration transaction releases its row
lock. The consumer must scope and recheck the server zone as current after
taking that same lock, and treat a row deleted between lookup and locking as an
obsolete event. When primary deletion also locks the transfer row, acquire
ordered server-zone locks first to match the consumer's lock order and avoid a
server-zone/transfer deadlock.
