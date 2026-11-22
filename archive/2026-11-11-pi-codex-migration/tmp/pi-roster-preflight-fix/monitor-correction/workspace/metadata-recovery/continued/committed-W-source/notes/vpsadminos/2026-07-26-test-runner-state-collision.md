# Concurrent VM test runners can share one state directory

Related initiative:
`work/2026-07-24-ct-start-hang`

## Symptom

Two independently launched `./test-runner.sh test ...` commands that select the
same VM test can write to the same path below `/tmp/os-test-runner`. Logs,
sockets, and VM state then overwrite or remove each other, producing misleading
startup, connection, or cleanup failures.

The executor derives `os-test-<name>-<hash>` from the test path. The hash makes
different test paths distinct, but it is deterministic and does not distinguish
two concurrent invocations of the same path.

## Workaround

Run matching VM tests sequentially. In particular, do not launch the cgroup-v1
and cgroup-v2 variants from separate runner processes when their selected test
identity resolves to the same state basename.

If concurrency is necessary, pass a different test-runner `--state-dir` to each
invocation and verify that the derived socket and state paths are disjoint.
Before retrying a collision, stop only the affected runner/VM process group and
inspect its exact state path rather than deleting the shared
`/tmp/os-test-runner` root.

## Verification

For the lifecycle redesign, local `osctld/lifecycle` and CPU cgroup tests are
scheduled sequentially. Their terminal results are recorded in the initiative
state file.
