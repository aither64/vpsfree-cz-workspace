# Duplicate utility execution diagnosis

Bot source stable94ac4eb5a7caf0456fff7df86a44cae198463276. No source changes,
new test invocation, application acceptance or merge performed in this diagnosis.

The exact fresh utility thread01a15605-c9ae-7e42-97d3-ecdddbb703c8 started the
same command twice. Native JSONL item4 launched plain test-runner; item6 launched
it again solely to add tee/status capture. Both used `/tmp/os-test-runner` and the
same `os-test-vpsadmin-events-8aba1688` VM, disk, log and socket paths. The Nix
source lock delayed only evaluation, not test VM ownership; both started after
that lock. No cross-invocation runner lock protected this shared state.

First run exited1 after166.27s; before examples, services API readiness failed
with `IOError: stream closed in another thread` in OsVm::Shell#wait. No application
assertion ran. The second run was live, not merely lock-waiting: its services VM
was booted and `/proc/2285593/fd/32` referenced shared `services-root.img (deleted)`.
Concurrent runner teardown/log reuse makes these results contaminated. This is
not a valid application regression or passing verification result.

## Proven owned tree before stop

All runner/tee working directories were the exact session bot worktree.
Utility CLI PID2237728 was launched by the lead wrapper and bound by JSONL thread
identity above; it was not signalled. Start times are kernel boot ticks, preventing
PID reuse ambiguity; complete process command/cwd observations are retained in
[duplicate-process-observation.json](duplicate-process-observation.json).

| PID | Parent | Start ticks | Role |
| --- | --- | --- | --- |
| 2242089 | 2237728 | 1175231638 | second invocation bash/tee/status wrapper |
| 2242090 | 2242089 | 1175231642 | second test-runner parent |
| 2242091 | 2242089 | 1175231642 | tee to bot-runtime-ready.log |
| 2246311 | 2242090 | 1175233310 | second runner worker, VM owner |
| 2285283 | 2246311 | 1175249511 | services virtiofsd |
| 2285285 | 2285283 | 1175249513 | services virtiofsd child |
| 2285593 | 2246311 | 1175249612 | services qemu-kvm, exact state disk/socket paths |

The second wrapper began23:16:44, worker23:17:01, VM23:19:44. Native first run
started23:16:58 and failed23:19:44. The active log was bot-runtime-ready.log;
runner worker wrote shared test-runner.log and services VM logs. Complete fd
snapshot: [duplicate-open-files.json](duplicate-open-files.json).

## Authorized cancellation and final state

Lead explicitly authorized stopping only the exact proven accidental duplicate
invocation through runner/TERM. Immediately before signalling, rechecked worker
PID2246311 generation1175233310, parent2242090, exact cwd and full command. Sent
TERM only to that worker. See [duplicate-stop-action.json](duplicate-stop-action.json).
Its native TestEvaluator ensure terminated its services QEMU (exit0) and
virtiofsd; service machine log records TERM/qemu_exit. Parent/wrapper/tee then
completed. All seven listed PIDs were confirmed absent. No utility thread/session
or unrelated process was signalled; no broad process match was used for stopping.
The duplicate reports failure380.45s with bot-runtime-ready.exit1. Preserve this
as interrupted/invalid verification, not a clean runtime test failure.

## Preserved evidence

- [Pre-stop tree](bot-duplicate-before-stop-94ac4eb.tar.gz): entire then-existing
  shared runner tree, logs and dereferenced config before any signal.
- [Post-stop tree](bot-duplicate-after-stop-94ac4eb.tar.gz): native teardown logs.
- `duplicate-before-stop/`: native JSONL and captured second-invocation log before
  cancellation, preserving first-run tool output even if later appended.
- Existing runtime-ready-watcher-native.jsonl/.log and bot-runtime-ready.log/.exit
  retained. The original utility finished naturally; no instruction to stop it.

## Isolated supported invocation

Pinned CLI App#setup declares `state-dir` on the `test` command; Cli::Command passes
it to Executor, whose per-test logs/VM files and socket directory derive from it.
Use a fresh unique task-owned path, with the flag after `test`:

```sh
./test-runner.sh test --state-dir /tmp/security-advisory-notifications-94ac4eb-NEW_UNIQUE_ID vpsadmin-events
```

No invocation was launched here. A task-owned idempotent/locked launcher chosen by
the lead must invoke it once and expose durable logs/status for the watcher to
observe. Unique state paths do not by themselves make duplicate invocations
appropriate. Do not repeat plain command to attach a logger to a running process.
