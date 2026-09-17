# Keep exportfs fixture server names short

The scratch NFS migration fixture created server `migration-target`. The start
command returned success (it schedules a runit service), but the server PID
never appeared. Operations::Server::Spawn uses `nfsns-<server name>` for a veth
peer, exceeding Linux's 15-character interface-name limit with that name.
Use a short fixture name such as server2 and bound readiness checks; inspect
service logs when the command succeeds but no server PID appears.

Related initiative: work/2026-09-12-nfs-cancellation. The corrected migration
trigger is still being validated; this note does not claim a migration pass.
