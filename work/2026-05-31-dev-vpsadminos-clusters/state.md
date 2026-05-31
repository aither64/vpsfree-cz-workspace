# vpsAdminOS-only dev clusters state

Date: 2026-05-31

Affected repositories/workspaces:

- coordination workspace: `/home/aither/workspace/ai/vpsfree.cz`
- consumed worktrees: optional `worktrees/<slug>/vpsadminos`
- default vpsAdminOS source: `repos/vpsadminos.git` `origin/staging`

Progress:

- Planning completed. User selected:
  - network support: local and bridge modes;
  - VM state: ready `tank` pool by default;
  - default topology: single node.
- Implemented `dev-clusters/vpsadminos/` tooling:
  - `bin/devcluster` command wrapper;
  - `default-config.json` for node addresses, SSH forwards, sizing, and
    topologies;
  - `flake.nix` and `nix/test.nix` for vpsAdminOS-only OSVM configs;
  - `README.md` usage notes.
- Added shared Ruby OSVM runner in `dev-clusters/lib/devcluster_runner.rb`.
  The existing `dev-clusters/vpsadmin/` runner now delegates to this shared
  implementation with `services` as the priority machine.
- vpsAdminOS cluster behavior:
  - `local` mode uses QEMU user networking on `eth0` for internet/SSH
    forwarding and socket multicast on `eth1` for VM-to-VM traffic;
  - local mode uses configured `localNameservers`, defaulting to public
    resolvers, because QEMU's built-in `10.0.2.3` resolver timed out during
    live vpsAdminOS boots;
  - `bridge` mode uses QEMU user networking on `eth0` and `br0` bridge
    networking on `eth1`;
  - all nodes import the vpsAdminOS `pool-tank.nix` test config, enable root
    SSH with the generated devcluster key, and get peer host entries.

Commands/results:

- `bash -n dev-clusters/vpsadminos/bin/devcluster
  dev-clusters/vpsadmin/bin/devcluster`: passed.
- `ruby -c dev-clusters/lib/devcluster_runner.rb`: passed.
- `ruby -c dev-clusters/vpsadmin/lib/devcluster-runner.rb`: passed.
- `ruby -c dev-clusters/vpsadminos/lib/devcluster-runner.rb`: passed.
- `jq -e . dev-clusters/vpsadminos/default-config.json`: passed.
- `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
  dev-clusters/vpsadmin/flake.nix dev-clusters/vpsadminos/flake.nix
  dev-clusters/vpsadminos/nix/test.nix`: passed.
- `git diff --check`: passed.
- Added `--timeout seconds` to the vpsAdminOS `start` command and reran
  `bash -n dev-clusters/vpsadminos/bin/devcluster`: passed.
- Added `network.localNameservers` to the default vpsAdminOS devcluster
  config and reran `jq -e . dev-clusters/vpsadminos/default-config.json`:
  passed.
- Reran `nix shell nixpkgs#nixfmt-rfc-style -c nixfmt --check
  dev-clusters/vpsadmin/flake.nix dev-clusters/vpsadminos/flake.nix
  dev-clusters/vpsadminos/nix/test.nix`: passed.
- Nix eval matrix passed for all vpsAdminOS devcluster combinations using
  local `repos/vpsadminos.git` `origin/staging`:
  - `single/local`;
  - `single/bridge`;
  - `dual/local`;
  - `dual/bridge`;
  - `triple/local`;
  - `triple/bridge`.
- `nix build --impure --override-input vpsadminos
  git+file://$PWD/repos/vpsadminos.git?ref=refs/remotes/origin/staging
  path:$PWD/dev-clusters/vpsadminos#cluster-config` passed for
  `single/local`; generated config name was
  `vpsadminos-devcluster-2026-05-31-dev-vpsadminos-clusters` with machine
  `node1`.
- Runner packaging checks passed:
  - `nix run --impure --override-input vpsadminos
    git+file://$PWD/repos/vpsadminos.git?ref=refs/remotes/origin/staging
    path:$PWD/dev-clusters/vpsadminos#runner -- help` built and printed
    usage with exit code 2;
  - `nix run --impure --override-input vpsadmin
    git+file://$PWD/repos/vpsadmin.git?ref=refs/remotes/origin/master
    --override-input vpsadminos
    git+file://$PWD/repos/vpsadminos.git?ref=refs/remotes/origin/staging
    path:$PWD/dev-clusters/vpsadmin#runner -- help` built and printed usage
    with exit code 2.
- `pgrep -af
  'vpsadminos-devcluster|/tmp/vpsadminos-devcluster|driver/vpsadminos|os-test-driver__vpsadminos'`:
  no remaining matching process except the `pgrep` command itself.

Smoke test status:

- Initial live vpsAdminOS boot attempts appeared stuck at SeaBIOS
  `Booting from ROM...`, and the same symptom reproduced with the stock
  vpsAdminOS driver test from
  `worktrees/2026-05-30-dev-vpsadmin-clusters/vpsadminos`:
  `./test-runner.sh test driver/vpsadminos`.
- Retried with a longer timeout:
  `dev-clusters/vpsadminos/bin/devcluster start
  2026-05-31-dev-vpsadminos-clusters-smoke --topology single --network local
  --timeout 2400`.
  The VM eventually booted; SSH was reachable on `127.0.0.1:11122` after
  roughly 3-4 minutes.
- Single-node smoke results:
  - SSH worked;
  - raw internet connectivity worked (`ping 1.1.1.1`, HTTP by IP);
  - DNS through QEMU `10.0.2.3` timed out;
  - DNS-backed HTTPS worked immediately after using `1.1.1.1`.
- Retried dual-node local mode after adding `localNameservers`:
  `dev-clusters/vpsadminos/bin/devcluster start
  2026-05-31-dev-vpsadminos-clusters-dual-smoke --topology dual
  --network local --timeout 2400`.
  Both VMs reached ready after roughly 7-8 minutes.
- Dual-node smoke results:
  - `node1` SSH: `127.0.0.1:11122`, passed;
  - `node2` SSH: `127.0.0.1:11222`, passed;
  - DNS-backed HTTPS to `https://example.com`, passed on both nodes;
  - peer ping by internal IP, passed both directions;
  - peer ping by generated host names `dev-os1`/`dev-os2`, passed both
    directions;
  - ZFS `tank` pool online on both nodes;
  - `osctl pool list` reported `tank` active on both nodes after osctld
    finished starting.
- The dual-node smoke cluster is intentionally still running for manual SSH:
  `dev-clusters/vpsadminos/bin/devcluster ssh
  2026-05-31-dev-vpsadminos-clusters-dual-smoke node1`
  and `... node2`.
- The stopped single-node smoke cluster state was removed with
  `dev-clusters/vpsadminos/bin/devcluster reset
  2026-05-31-dev-vpsadminos-clusters-smoke`.

Open questions:

- vpsAdminOS boots can spend several minutes after SeaBIOS without console
  output; a longer default or documented timeout may be worth considering if
  this is common on other machines.
