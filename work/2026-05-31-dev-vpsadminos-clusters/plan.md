# vpsAdminOS-only dev clusters

Goal: implement workspace-local tooling for booting small vpsAdminOS VM
clusters without vpsAdmin services on top.

Affected components:

- coordination workspace: add `dev-clusters/vpsadminos/` tooling and docs;
- coordination workspace: share the generic OSVM runner with the existing
  `dev-clusters/vpsadmin/` tooling;
- vpsadminos: consumed as a source worktree or bare `origin/staging`, but not
  modified unless implementation discovers a missing OSVM capability.

Approach:

- store generated runtime state under `.dev-clusters/vpsadminos/`;
- select a feature worktree by slug from `worktrees/<slug>/vpsadminos` when it
  exists, otherwise use `repos/vpsadminos.git` `origin/staging`;
- support `single`, `dual`, and `triple` topologies with `single` as the
  default;
- boot each VM with SSH enabled, a persistent file-backed disk, and an installed
  active `tank` pool;
- keep QEMU user networking on `eth0` for internet access;
- use `eth1` for the internal node network, either QEMU socket multicast in
  local mode or `br0` bridge networking in bridge mode;
- expose SSH through localhost forwards in local mode and through the VM bridge
  addresses in bridge mode.

Compatibility:

- production systems, schemas, APIs, generated clients, and deployment
  configuration are not changed;
- per-slug runtime state isolates VM disks and generated SSH keys;
- the existing vpsAdmin devcluster command surface and runtime behavior must
  remain unchanged;
- one bridge-mode vpsAdminOS cluster using the default bridge IPs should run at
  a time unless the per-cluster config is edited to use different addresses.

Testing plan:

- shell and Ruby syntax checks;
- Nix evaluation/build checks for all topologies and both network modes;
- local-mode smoke test with SSH, internet access, peer connectivity, `tank`
  zpool, and active osctl pool;
- bridge-mode smoke test on aitherdev when bridge helper and IP availability
  permit.
