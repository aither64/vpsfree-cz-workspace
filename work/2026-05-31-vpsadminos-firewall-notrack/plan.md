# vpsAdminOS Firewall Without Init-Namespace Conntrack

## Goal

Rework vpsAdminOS firewalling so vpsAdminOS nodes run without conntrack in the
host/init network namespace by default. The firewall installs raw-table notrack
rules:

```sh
iptables -t raw -I PREROUTING 1 -j CT --notrack
iptables -t raw -I OUTPUT 1 -j CT --notrack
```

The production configuration changes must affect vpsAdminOS nodes only. Other
NixOS systems in `vpsfree-cz-configuration` must keep the nixpkgs stateful
firewall behavior.

## Affected Repositories

- `vpsadminos`: implements the vpsAdminOS-specific firewall module and tests.
- `vpsadmin`: no functional changes found or needed for this phase.
- `vpsfree-cz-configuration`: converts vpsAdminOS node firewall policy from
  allow-listed services to protected services.

## Implemented Design

### vpsadminos

vpsAdminOS no longer imports nixpkgs' `firewall-iptables.nix`. It still imports
nixpkgs `firewall.nix` for the shared firewall option schema and keeps a local
iptables implementation under `os/modules/services/networking/firewall-iptables.nix`.

The new option `networking.firewall.conntrack.enable` defaults to `false`.
When it is false, the firewall:

- installs owned raw-table `CT --notrack` rules in `PREROUTING` and `OUTPUT`;
- removes/re-adds those rules idempotently on start and reload;
- removes them on stop;
- preserves the existing chain names `nixos-fw`, `nixos-fw-accept`,
  `nixos-fw-log-refuse`, `nixos-fw-refuse`, and `nixos-fw-rpfilter`;
- uses a stateless default-open filter policy;
- applies `networking.firewall.protectedRules` first, then runs
  `extraCommands`, then accepts the remaining traffic.

`protectedRules` protect selected TCP/UDP ports or port ranges by allowing only
configured IPv4/IPv6 source ranges and dropping the rest. Legacy
`allowedTCPPorts`, `allowedUDPPorts`, and their range variants are intentionally
ignored in no-conntrack mode and emit a warning.

When `networking.firewall.conntrack.enable = true`, the module keeps a
nixpkgs-like stateful policy with `ESTABLISHED,RELATED` and the legacy
allowed-port options. This is used by development/test configurations that still
need host-namespace NAT.

`networking.lxcbr.enable` now asserts that
`networking.firewall.conntrack.enable` is true. The qemu, ISO, vpsAdminOS test
base, and container-image repository configurations opt into conntrack because
they enable or may enable `lxcbr`.

### vpsfree-cz-configuration

vpsAdminOS node configuration now protects only services that need source
restrictions:

- `cluster/cz.vpsfree/nodes/common/all.nix` protects goresheat,
  vpsAdmin ZFS send/recv ports, and optional vpsadmin-console.
- `configs/node/bird.nix` protects BGP and BFD from configured BGP neighbors.
  OSPF remains open because the previous rule was unrestricted.
- `modules/system/monitoring.nix` uses `protectedRules` for exporters only on
  vpsAdminOS nodes and keeps `extraCommands` for NixOS machines.
- `configs/munin-node.nix` uses `protectedRules` only on vpsAdminOS nodes and
  keeps `extraCommands` for NixOS machines.

Previously allowed services such as SSH, rpcbind, NFS, mountd, statd, lockd,
and iperf are intentionally left open under the new default-open node policy.

### vpsadmin

No vpsAdmin module was found to add host iptables rules to vpsAdminOS nodes.
The worktree is kept for later integration testing or input pinning if needed.

## Compatibility And Deployment

- Persisted state: no database, disk format, or generated state changes.
- API/client contracts: no API changes.
- Mixed versions: `vpsfree-cz-configuration` must not deploy the new
  `protectedRules` configuration until the corresponding vpsAdminOS revision is
  pinned. Older vpsAdminOS revisions do not define the option.
- Rolling upgrades: nodes can be upgraded individually after the new vpsAdminOS
  revision is pinned, because firewall state is local to each node.
- Rollback: rebooting into an older generation naturally clears raw-table
  notrack rules. Firewall stop/reload also removes the owned notrack rules.
- NAT impact: host-namespace NAT/MASQUERADE is incompatible with strict
  PREROUTING notrack. Configurations using `networking.lxcbr` must explicitly
  enable conntrack.

Deployment order:

1. Push or merge the `vpsadminos` branch.
2. Pin staging in `vpsfree-cz-configuration` with `confctl inputs channel set`
   or the normal channel workflow.
3. Build/deploy staging nodes and run representative node/vpsAdmin integration
   tests.
4. Pin production after staging validation.

## Validation Plan

- Run the focused vpsAdminOS VM test `firewall/conntrack`, including both
  `no-conntrack` and `conntrack` scripts.
- Evaluate qemu and ISO outputs to catch `lxcbr` assertion regressions.
- Format and whitespace-check both changed repositories.
- Build/evaluate representative staging node configuration with the local
  vpsAdminOS revision overridden, where local secrets permit it.
- After the vpsAdminOS revision is pushed/pinned, run `confctl build
  "cz.vpsfree/nodes/stg/*"` with access to production/staging secrets.
