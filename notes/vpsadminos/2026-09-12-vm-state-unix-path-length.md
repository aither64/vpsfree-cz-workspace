# Keep VM test state paths short

The test-runner derives shell UNIX sockets from --state-dir/socks. Putting
state beneath a deeply nested initiative scratch directory made both legacy
VMs fail before boot: `too long unix socket path (121bytes given but 108bytes max)`.
This is a launcher path limit, not a guest/kernel failure.

Use a short unique directory, e.g. `mktemp -d /tmp/nfs-cancel-legacy.XXXXXX`, and
record its exact returned path in the initiative state. Preserve logs through
an artifact or copy the useful evidence after testing. The socket path must
remain short even if long test names are hashed by the runner.

Related initiative: work/2026-09-12-nfs-cancellation/.
