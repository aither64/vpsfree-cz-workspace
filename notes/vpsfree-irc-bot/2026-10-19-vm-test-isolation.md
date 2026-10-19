# Isolating IRC bot VM integration runs

The pinned vpsAdminOS test runner accepts a test-specific state root:

```sh
./test-runner.sh test --state-dir /tmp/sa-unique-id vpsadmin-events
```

Use a short unique root. A long descriptive session root produced a 108-byte
virtiofs UNIX socket pathname; virtiofsd rejected it with “path must be shorter
than SUN_LEN”, and QEMU then failed to connect before any example ran. A root
such as `/tmp/sa-unique-id` leaves space for generated socket names. Keep full
session ownership and the exact command in session records instead of encoding
all metadata in the pathname.

Serialize actual runner execution. Two concurrent invocations sharing a root
can overwrite or remove one another's images and sockets, producing misleading
stream-closed failures. An idempotent launcher can lock execution, check the exact
clean source revision, capture log/exit status itself, and return a cached result
if invoked again. A monitoring agent should launch that wrapper once and retain
its handle, rather than starting a second command to add output capture.

Confirmed during `work/2026-10-19-security-advisory-notifications/` at bot94ac4eb.
Duplicate ownership/cleanup and exact socket-limit evidence are retained there;
no application failure was inferred from either contaminated or pre-boot run.

With the short unique state root and single guarded invocation, all eight examples
passed at the same source revision (513.15 seconds), confirming the environment
correction. Complete final evidence is in the owning session.
