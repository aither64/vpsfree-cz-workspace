# Implementation validation

Abandoned on2026-09-17. The corrected109 normal/diagnostic builds and external-ZFS
fixture completed, but their runtime tests did not run. Final95 pins and
validation remained unfinished. See [abandonment.md](abandonment.md). Earlier
references to running jobs and retries below describe the development history.

Current committed source: OS `18332a06d`, retained95 `a2bdcc5b5067`, default109
`7c66ab3c284a`. The corrected109 source is pinned;95 still needs its verified archive hash.
The migration correction passed focused review and object compilation; runtime
validation remains pending. Earlier candidate results below are not acceptance of that correction.

| Check | Result |
| --- | --- |
| Focused cancellation, forced stop, persistence and deadline tests | 259 daemon +24 library examples pass |
| Pool and console tests after frozen restart fix | 36 examples pass |
| Full repository RSpec CI | Pass at OS2bb3c25, run34697775040; daemon code unchanged |
| RuboCop and required commit hooks | Pass, including corrected migration fixture |
| Old6.12.48 without cancellation, cgroup v1/v2 | Both variants pass; four examples and eight kill/start cycles |
| Previous normal109 candidate, NFS3/4.0/4.1/4.2 | All44 protocol examples pass; separate migration fixture failed before triggering replacement |
| Previous normal95 plain kernel compilation | Pass at6090ca00 |
| Previous normal109 compilation/cache publication | Pass atcb16974b, CI34701121709 |
| Previous diagnostic plain95/109 compilation | Outputs available; final built-in ZFS builds deliberately interrupted after migration regression |
| Corrected kernel objects and full builds | Changed objects and109 normal/debug builds pass; final95 build was not run |
| Real migration on previous candidates | NULL dereference on both95/109; corrected RPC sysfs recreation committed, runtime pending |
| Matching rebuilt livepatch and identity guards | Pending corrected base build |
| Historical6.12.95 livepatch lifecycle, AMD/Intel | Both pass in CI; local AMD lifecycle also passes |
| Original queued final matrix | Deliberately interrupted before guest boot to replace superseded sources |

The old-kernel VMs exercise both ordinary and frozen containers. Each example
restarts osctld, requests an explicit kill, then starts the container again and
verifies a payload write/read. All eight explicit kill commands succeeded in
2.77–6.45 seconds. The frozen cases initially exposed a missing tty0 reconnect
on pool import; the fix restores the existing console/writeback completion path
for freezing and frozen containers.

Diagnostic configuration initially rejected DEBUG_KOBJECT_RELEASE. Exact Linux
Kconfig requires DEBUG_OBJECTS_TIMERS and DEBUG_OBJECTS; both are now enabled.

Kernel CI failed before compilation with HTTP 429 on both GitHub archive
endpoints. Logs were inspected before retries. Local builds use verified source
archives. The historical archive subsequently downloaded after backoff with its
unchanged expected hash. No runtime pass is inferred from a build, evaluation,
or source-level check. Detailed commands, logs and retry evidence are in state.md.

At 17:48 UTC, the rescheduled normal 6.12.109 suite completed all 44 protocol
examples successfully (NFS3/4.0/4.1/4.2, including osctld restart, both dirty-init
namespace modes, processless namespaces, locks and tenant isolation). Its one
migration example failed before triggering migration because BusyBox readlink
has no -e option; the pending test change uses test -e plus readlink -f.
The overall suite is correctly reported FAILED, not a full pass.

Focused probes reproduced a real NULL dereference on BOTH final candidate
kernels: cb16974b 6.12.109 clean migration and 6090ca00 6.12.95 race setup.
The crash is sysfs_delete_link+0x23, called by nfs_sysfs_link_rpc_client from
nfs4_update_server. clnt->cl_sysfs is NULL. The newly added link refresh exposed
that rpc_switch_client_transport destroys the RPC sysfs client and does not
recreate it before returning success. This is a regression in our follow-up,
not a passing migration result. Both first-oops traces are retained in
scratch/migration{109,95}-null-sysfs.txt. Correct the transport replacement
sysfs lifecycle and handle optional sysfs allocation failure before rebuilding.
The two crashed disposable probe guests were closed after capturing evidence;
the development session and feature worktrees remain open.
