# Test-runner state paths must leave room for VM socket names

Initiative: `work/2026-06-15-vpsadmin-events`

Running `./test-runner.sh test --state-dir DIR TEST` with a descriptive
`mktemp` directory under `/tmp` failed before any test example started. The
generated virtiofs socket path was exactly 108 bytes, and `virtiofsd` logged
`path must be shorter than SUN_LEN`; QEMU then failed because the socket did
not exist.

Use a short isolated state directory such as `/tmp/vt1.XXXXXX`. The same
`alerts/notification-routing` scenario passed 2/2 examples with a short path,
and QEMU exited and tore down cleanly. Keep state directories isolated between
concurrent runs, but put descriptive names in retained log or artifact paths
rather than in the runner state-directory basename.
