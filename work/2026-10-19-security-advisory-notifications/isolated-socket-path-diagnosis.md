# Isolated runtime socket path failure

Exact source94ac4eb5a7caf0456fff7df86a44cae198463276 unchanged and clean.
Single idempotent isolated run failed before any application example, exit1 after
72.64s. Preserved full failed tree and dereferenced config:
[bot-isolated-failed-94ac4eb.tar.gz](bot-isolated-failed-94ac4eb.tar.gz).
Original isolated-runtime.log/.exit and isolated-watcher-report.md retained.
No new run, source/runtime edit, cleanup, stop or CI monitoring performed here.

The exact failure is UNIX socket pathname length, not duplicate interference or
an application assertion:

```text
services-fs-vmSharedDir.log:
Error creating listener: socket error: path must be shorter than SUN_LEN

services-console.log:
qemu-kvm: ... Failed to connect to '...services-fs-vmSharedDir.sock':
No such file or directory
```

QEMU exited1 at23:26:18; OsVm shell acceptance then raised stream-closed IOError
in before-suite API readiness. The underlying vhost-user socket was never created.

The selected root is `/tmp/2026-10-19-security-advisory-notifications-94ac4eb-isolated`.
Pinned Executor#test_sock_dir appends `socks`; OsVm#socket_path appends the hash and
machine/fs name, producing:

```text
/tmp/2026-10-19-security-advisory-notifications-94ac4eb-isolated/socks/59f1e6f8-services-fs-vmSharedDir.sock
```

This pathname is108bytes. Linux UNIX pathname sockets require room for the
terminator; virtiofsd explicitly requires a length shorter than SUN_LEN. The full
long descriptive root I recommended did not account for the suffix limit.

Supported minimal correction: a SHORT fresh task-owned state root, recorded under
this session, with the same supported CLI flag and single-execution lock/cached
status launcher. Example `/tmp/sa-94ac4eb-r1` is absent at diagnosis time and yields
62byte socket path. Source, test behavior, VM inputs and runtime remain unchanged.
Do not reuse the failed launcher's cached exit/status, overwrite evidence or
simply invoke it again; lead should prepare a fresh approved operation/log/status
identity and short root before a new watcher runs it once. No symlink/kernel/
framework tweak, extra application fix or source commit is needed.

The failure is established by exact process output plus pathname arithmetic;
no retry or socket/server experiment was performed. Lead holds integration and
owns any environment correction and fresh verification launch.
