# Devcluster Fresh-State Smoke

- Date: 2026-05-30
- Project: cross-project
- Initiative: `work/2026-05-30-dev-vpsadmin-clusters`
- Workflow: create a temporary feature-slug worktree group, run
  `devcluster start <slug> --topology single --network local`, mutate seeded
  state through the API, then `devcluster reset <slug>` and remove the
  temporary worktrees.
- Symptom: reviewing config alone missed boot-time ordering and packaged-gem
  behavior. Fresh starts exposed issues that an already-running cluster had
  hidden.
- Findings:
  - node pool refresh must wait for the node-side ZFS pool, not only for the
    services DB seed row;
  - DNS behavior must be verified with a real PTR transaction and queries to
    both authoritative servers;
  - libnodectld changes used by Nix-built VMs require regenerated packaged
    gems.
- Verification: after fixes, a fresh single/local devcluster seeded users,
  pools, networks, IPs, mail templates, DNS servers, and reverse zones. A PTR
  change for `198.51.100.10` propagated from hidden primary to public
  secondary, and `VpsAdmin::API::Tasks::Dns.new.check_reverse_records` reported
  `2 records ok`, `0 dns errors`, and `0 records incorrect`.
