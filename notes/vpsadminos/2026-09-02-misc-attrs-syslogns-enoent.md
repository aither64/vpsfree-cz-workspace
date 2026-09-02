# misc-attrs can expose a transient syslog namespace lookup failure

## Symptom

The vpsAdminOS aggregate test can report
`kernel/vpsadminos#misc-attrs` failing on an ordinary
`osctl ct exec ... touch` command with `user runner failed`.

## Cause boundary

Inspect the osctld journal before treating this as an attribute failure. In
GitHub run `33562536093`, the requested command never ran. The forked runner
failed while opening the live container init's
`/proc/<init-pid>/ns/syslog` in
`OsCtl::Lib::Sys#attach_syslogns`:

```text
Errno::ENOENT: No such file or directory @ rb_sysopen -
/proc/16266/ns/syslog
```

The parent received EOF instead of the runner's JSON response and returned the
generic `user runner failed` message. The container and PID were still
running in diagnostics two seconds later. The VM had about 4.8 GiB available,
so this was neither the intended memcg OOM workload nor global OOM.

The custom kernel proc link can return `ENOENT` when proc/nsfs cannot
materialize the namespace. Post-failure diagnostics cannot distinguish a null
return from the custom `syslogns_get()` operation from an earlier proc inode
instantiation failure. Capture that distinction on the next recurrence rather
than assuming the container exited.

## Reproduction results

- Isolated `misc-attrs` passed.
- The aggregate passed `misc-attrs` under six-way script concurrency.
- A forced queue matching the failing OOM-to-attrs handoff passed.
- 2,000 `ct exec true` calls with 16 concurrent attachments passed in 691
  seconds on the same 6.12.95 kernel.

This rules out a deterministic attribute, OOM-ordering, UID-reuse, or ordinary
concurrent-attachment failure. It remains a low-frequency proc/syslog
namespace anomaly.

## Diagnostics for a recurrence

Before teardown, capture the following at the instant
`attach_syslogns` gets `ENOENT`:

- the target PID, `/proc/<pid>/stat`, and start time;
- `ls -la /proc/<pid>/ns` plus `readlink` of every namespace entry;
- direct `open` or `readlink` results for `ns/syslog` and a standard
  namespace such as `ns/user`;
- container state and its recorded init PID; and
- memory availability and the target runner cgroup's memory events.

Retrying the proc open may make osctld resilient, but log the first failure and
verify PID identity before retrying so the underlying kernel condition remains
observable.

## Separate test defect

The attribute test itself currently passes while every `chattr` invocation
prints `Permission denied`, because it trusts the command status and never
checks the flags or their semantics. A meaningful test must verify `lsattr`
and the expected immutable/append-only file behavior.

Related initiative:
`work/2026-06-15-vpsadmin-events`.
