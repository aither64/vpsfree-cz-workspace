# Integration tests can lose all API backends

## Symptom

Long vpsAdmin integration tests can fail after otherwise successful transaction
chains because HAProxy has no healthy API backend. Clients then receive an
immediate `503 Service Unavailable` or wait for a `504 Gateway Timeout`.

The service VM can still report no failed systemd units, and the
`vpsadmin-api.service` journal may contain only normal Puma startup messages.
In one captured shutdown, Puma needed about 31 seconds to stop, which is
consistent with request threads remaining blocked.

## Evidence

CI run `32652787707` failed `storage/repeated-rollback-branching` and
`vps/clone-remote-consistent` this way. The complete test artifact contained no
OOM, RabbitMQ recovery, failed unit or application exception explaining the
backend loss.

`storage/repeated-rollback-branching` was then run at unchanged vpsAdmin base
`b12f41859a9ae198224cd6ca63eddbcdd0371db8`. The same second example failed:
`dataset.snapshot create` waited 74 seconds and received a 504, even though the
preceding chain and all of its transaction rows had completed successfully.
This proves that occurrence predates the feature branch under test.

An exact-base CI run from earlier the same day passed
`vps/clone-remote-consistent` while failing a different long integration test,
showing that the clone failure is intermittent rather than a consistently
broken handler.

## Investigation workflow

1. Download the full CI artifact before rerunning the job.
2. Inspect the failing test's `test-runner.log`, `services-shell.log`,
   `services-console.log` and service journals.
3. Check transaction tables collected by the failure hook; do not assume an
   unfinished transaction when the client timeout is the only visible error.
4. Compare the same test at the exact base revision in a detached worktree.
5. Check `/dev/shm` before local VM tests. Stop cleanly if the runner warns that
   requested shared memory exceeds the available limit, because other
   development sessions may be running VMs on the same host.

The existing failure artifact does not include Puma worker thread dumps or
HAProxy backend state at the moment health checks fail. Add those diagnostics
to the integration failure hook before attempting to determine the exact
blocked Ruby/native frame.

Related initiative:
`work/2026-08-23-vpsadmin-supervisor-issue/`
