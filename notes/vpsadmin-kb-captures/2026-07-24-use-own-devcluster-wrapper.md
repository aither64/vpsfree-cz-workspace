# Use the capture repository's devcluster wrapper

Related initiative: `work/2026-06-15-vpsadmin-events/`.

A screenshot cluster started by `vpsadmin-kb-captures/bin/devcluster` stores
its PID, topology, socket paths, and SSH key below that repository's
`.devcluster/` directory. The coordination workspace's
`dev-clusters/vpsadmin/bin/devcluster` uses different state.

Using the top-level wrapper against such a running cluster reported it as
stopped, rejected the repository-only `screenshots` topology, and its SSH
command failed with `Too many authentication failures` because it selected the
wrong cluster key.

Run status, SSH, update, and stop commands from the capture worktree with its
own `bin/devcluster`. The repository wrapper then reported the cluster running
with `topology: screenshots`, and two consecutive
`systemctl restart vpsadmin-devcluster-seed.service` calls completed
successfully.
