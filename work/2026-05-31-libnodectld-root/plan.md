# Fix libnodectld CtHookInstaller specs and flaky CI tests

## Goal

Fix the GitHub workflow failure in the libnodectld specs where
`NodeCtld::CtHookInstaller` calls `NodeCtld.root` after only
`nodectld/ct_hook_installer` has been required. Follow up on the broader CI
failure on the same branch, which unexpectedly failed
`vps/migrate-with-open-maintenance-window` and `webui#storage-backup-export`.

## Affected Repositories

- `vpsadmin`
  - worktree: `worktrees/2026-05-31-libnodectld-root/vpsadmin`
  - branch: `2026-05-31-libnodectld-root`

## Approach

- Reproduce the focused spec failure locally.
- Make the minimal load/setup change so `NodeCtld.root` is defined whenever
  `CtHookInstaller` is used in isolation.
- Run the focused spec and component lint/checks required by the repository.
- Commit the libnodectld load fix and generated nodectld gem updates.
- Make the maintenance-window migration test independent of wall-clock weekday
  and timezone.
- Make the storage/export webui browser test prepare the node-side ZFS and
  osctl state it needs, then use normal `nodectld` initialization instead of
  direct `osctl-exportfs` setup.
- Fix the export add-host form so it lists VPS client addresses without asking
  the API to serialize export-side network interfaces for normal users.
- Add local MariaDB test database tooling for API/libnodectld specs and wire
  the shared spec DB setup to auto-start an isolated temporary DB when no
  explicit local or CI database config is present.

## Compatibility

The libnodectld change is limited to Ruby load behavior. It does not change
persisted state, database schemas, API contracts, protocol formats, Nix module
options, generated configuration, or hook file contents.

The webui form change changes only how the add-host select options are built:
it lists IPv4 addresses assigned to the export owner's VPSes instead of all
user-visible assigned IPv4 addresses. The submitted `export.host.create` API
contract is unchanged. The test changes are runtime preparation and waits only.

The test database tooling is local developer/spec infrastructure only. It does
not change production database schemas, migrations, API contracts, daemon
protocols, or deployment configuration. CI remains configured by GitHub
workflow service containers.

## Deployment Notes

No coordinated node or service rollout is required. Mixed-version operation is
not affected. The webui form can be deployed independently of the API because
it uses existing `vps.list` and `ip_address.list(vps: ...)` API calls.

## Testing Plan

- Run the focused `ct_hook_installer` spec.
- Run the libnodectld spec workflow command or the closest local equivalent.
- Run libnodectld RuboCop before committing.
- Run `vps/migrate-with-open-maintenance-window`.
- Run `webui#storage-backup-export`.
- Run PHP syntax and Nix parse checks for touched files.
- Run the manual `tools/test-db` lifecycle.
- Run focused API and libnodectld specs without `DATABASE_URL` to verify
  automatic DB startup.
- Push the branch and monitor GitHub Actions.
