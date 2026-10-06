# 2026-06-07-vpsadminos-noconntrack-fw

## Goal

Investigate why `node1.pgnd` boots/deploys with an empty firewall after
switching to the no-conntrack firewall on a newer vpsAdminOS release.

## Affected repositories

- `vpsfree-cz-configuration`: production node configuration and vpsAdminOS
  channel pins.
- `vpsadminos`: firewall module, generated `firewall-start` program, kernel
  module expectations, and tests.

## Approach

1. Inspect the deployed `node1.pgnd` configuration and vpsAdminOS input pin.
2. Trace the generated no-conntrack firewall rules in vpsAdminOS.
3. Reproduce or explain the failing `iptables` invocation.
4. Add a generic `kernel-modules` runit service in vpsAdminOS that reconciles
   `boot.kernelModules` at boot and on configuration switches.
5. Have the iptables firewall module declare its required netfilter modules via
   `boot.kernelModules` and wait for `kernel-modules` before starting or
   reloading.
6. Log kernel-module service actions to stdout for svlogd and to syslog for
   centralized logging; log failed module loads without aborting the service.
7. Extend focused VM tests for module load, unload, failed-load handling,
   logging, and no-conntrack firewall behavior.

## Compatibility and deployment

The firewall runs on live vpsAdminOS nodes. Any fix must preserve rolling
upgrade behavior and avoid requiring all nodes to update at once unless that is
explicitly justified.

The selected design is compatible with rolling node updates: the new service is
local to each vpsAdminOS system and reconciles the module list during that
node's switch. Firewall startup/reload waits for the local module service, so a
node can receive the fix independently without requiring a coordinated update
of other machines.

## Testing plan

Run focused vpsAdminOS VM tests:

- `system/switch-to-configuration`
- `firewall/conntrack#no-conntrack`

For configuration pin updates, evaluate/build the affected node with
`confctl build`.
