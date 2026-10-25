# Live naming discovery correction

Session artifacts only; application source and feature refs remain frozen at
`4c6b9f177d5b205b21b45880c6ac1bc3c403eef6`. No model call, session preparation,
service start/restart, profile mutation or lifecycle action was performed.

The registry/service identity is `vpsfree-cz`; the workspace filesystem path
continues to end in `vpsfree.cz`. The recipe now uses the service identity.

Read-only inspection found portal PID `3386572` on selected package
`/nix/store/4cn1hh88xdpql5jp9pyrnf5fvnqsc829-dev-workspace-0.2.0`.
Its main task children list was empty, while the union across
`/proc/3386572/task/*/children` contained the native naming child `3386887`.
The child's executable, private socket/cwd, catalog argument and local-only
marker passed the original ownership checks. The old script missed the child
because Go can execute a child from a non-main OS thread. The smallest correction
collects/deduplicates every task's children before walking descendants; it does
not adopt orphan sockets or directories.

Corrected read-only discovery passed with `vpsfree-cz`; selected fields are
retained in `package-b-predeploy-discovery.json`. Provider was `openai` and the
catalog hash matched the immutable Luna catalog. No argv, environment values or
credentials were emitted. This proves current identity discovery, not final
candidate deployment or successful naming.

The startup contract at `portal/cmd/workspace-portal/main.go:318` calls
`startNamingRuntime` eagerly. `naming_runtime.go` asynchronously checks native
version/provider prerequisites and then starts one private app-server child.
It is not lazy. HTTP readiness can precede that child/socket; a failed/exited
child is not automatically restarted. Discovery should run after startup settles.
If it still fails, retain the failure and inspect bounded naming prerequisite/
exit messages. Do not create a preparation, guess another socket or restart
services to make the smoke run. Existing stale naming directories are neither
adopted nor removed.

After activation, main must verify that discovery's `packageRoot` equals the
exact activated candidate path in the rollout receipt, then use the before/after
identity snapshots and the compiled overlay recipe. Ordinary daemon/backend/
provider/profile identities must remain equal. The actual helper/model call,
useful name, deadline and settled cleanup remain unexecuted acceptance checks.
