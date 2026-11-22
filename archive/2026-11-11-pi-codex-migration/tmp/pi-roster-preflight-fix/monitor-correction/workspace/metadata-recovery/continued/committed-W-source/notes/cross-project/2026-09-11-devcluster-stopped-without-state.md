# A stopped development cluster may have no retained state

`vpsadmin-devcluster status <slug>` reports `stopped` when the cluster state
directory is absent, as well as when a retained cluster is not running.
That result alone does not establish that an in-place update can preserve its
database or VM disks.

Before promising a retained-state deployment, inspect the exact slug beneath
`<workspace>/.dev-clusters/vpsadmin/clusters/`, its recorded socket/runner
identity and the actual VM processes. Inspect only the intended initiative.
Use the installed stable command so package-generation and ownership checks
remain active; do not invoke an old helper or change ownership records to
bypass a refusal.

In the password-reset September 11 reconnect, no cluster state or VM process
remained, although its September 9 handoff recorded a healthy running cluster.
The shared provider certificates and SSH keys still existed. The user-requested
deployment therefore needs initialization and fixture restoration, and must
not be reported as preserving the earlier database. The prior removal's cause
was not established by this inspection.

Related initiative: `work/2026-08-18-vpsadmin-password-reset/`.
