# 2026-06-10-vpsadminos-firewall

## Goal

Prevent the vpsAdminOS firewall runit service from being restarted solely
because its declared firewall kernel module set changes, and prevent the
`kernel-modules` runit service from unloading modules when the service is
stopped.

## Affected repositories

- `vpsadminos`
- `vpsfree-cz-configuration`

## Approach

- Remove the firewall service's `restartTriggers` entry from
  `os/modules/services/networking/firewall-iptables.nix`.
- Keep the existing `onChange = "reload"` behavior so firewall script/rule
  changes continue to reload the service.
- Remove the `kernel-modules` stop-time module unload path from
  `os/modules/config/kernel.nix`; service stop should only terminate the
  service process.
- Add/adjust a switch-to-configuration regression check showing that changing
  firewall conntrack mode reloads the firewall instead of restarting it.
- Add a regression check showing that stopping `kernel-modules` leaves loaded
  modules loaded.
- Update `vpsfree-cz-configuration` channel inputs `production.vpsadminos` and
  `staging.vpsadminos` to the pushed vpsAdminOS revision using `confctl inputs
  channel update --commit '{production,staging}' vpsadminos`.

## Compatibility and deployment

- No persisted state, database schema, API, generated client, protocol, or
  NixOS module option compatibility changes.
- Existing systems can roll forward normally. Mixed-version operation is not a
  concern because this affects only local activation decisions.
- Rollback restores the old activation metadata and may again restart the
  firewall when the old `restartTriggers` differ, and may again unload tracked
  modules when stopping `kernel-modules`.
- No coordinated update of all running machines or nodes is required.
- Configuration input bumps affect vpsAdminOS nodes that consume the
  `production` and `staging` channels. The underlying OS change is compatible
  with rolling deployment and does not require all nodes to update together.

## Testing plan

- Run the focused switch-to-configuration VM test if feasible:
  `./test-runner.sh test system/switch-to-configuration`.
- Run formatting/check hooks before committing if a commit is requested.
- For `vpsfree-cz-configuration`, run `confctl build` for staging and
  production vpsAdminOS nodes if feasible after the input update.
