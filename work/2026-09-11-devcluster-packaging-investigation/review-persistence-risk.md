# Mandatory change review: persistence risk and compatibility

Lane: risk and compatibility
Organization repository range: `9e8783d68fdf40de04683e419d4f373bc27e3730..19238ca67ad822b362ae60f0cf7e7b4b27d60397`
vpsAdminOS repository range: `3eaf7b7320754715b38fc629e7f0ce23d13402cd..e6c4c5cfa27ce3b139bba6475be80cfead4b8df4`

## Blocking

None.

## Important

None.

## Advisory

None.

## Assessment

### Node pool readiness

- The remote wait performs only `zpool list` and `osctl pool show` probes under
  a 180-second process timeout before any dataset, directory, device, or service
  mutation (`dev-clusters/vpsadmin/bin/devcluster:791-855`). Its one-second
  forced-kill grace also bounds a stuck `zpool`, `osctl`, or child shell.
- Requiring both the ZFS pool and osctld's pool state to be `active` covers the
  observed race. In the reviewed vpsAdminOS source, pool import loads groups and
  containers before setting the pool state to `active`
  (`osctld/lib/osctld/pool.rb:290-325`), so `/default` is available before the
  subsequent device grants.
- Timeout and permanently-unready paths exit before mutations. The actual remote
  script tests use delayed and never-active states, verify known event order,
  and confirm that the never-ready path contains only probes. Mutating refresh
  steps remain single-shot and propagate failures.

### Persistent NixOS root disks

- `preserve_root_disk` is opt-in and defaults to false, retaining ordinary test
  machines' fresh-root behavior. The organization runner passes it only to
  NixOS machines; vpsAdminOS nodes and standalone OS-only clusters retain their
  previous constructor and disk behavior.
- A missing root is copied into a `Tempfile` in the destination directory,
  chmodded, and published with `rename`
  (`osvm/lib/osvm/nixos_machine.rb:61-72`). A failed copy or chmod therefore
  cannot expose a partial retained root, and default fresh-root replacement also
  preserves the old complete image until the new copy is ready. The tests verify
  known file contents across separate machine instances, failed initial copy,
  continued additional-disk preparation, default refresh, and explicit destroy.
- Normal runner shutdown calls machine finalization and cleanup, neither of
  which destroys disks. Explicit `destroy_disks` and provider reset still remove
  the NixOS root and created data disks. This preserves the existing destructive
  reset contract rather than making retained roots undeletable.

### Cross-project minimum and lifecycle ordering

- A vpsAdmin cluster containing any NixOS machine rejects an OSVM without the
  new interface before the machine-construction loop
  (`dev-clusters/lib/devcluster_runner.rb:140-164`). PID publication now follows
  successful construction (`dev-clusters/lib/devcluster_runner.rb:58-65`), so
  the unsupported combination cannot publish a managed runner identity or reach
  disk preparation. The exact companion vpsAdminOS revision is pinned for the
  package smoke input.
- The compatibility change is explicit in the plan and provider documentation:
  the vpsAdmin provider now requires `e6c4c5cfa` or a compatible later OSVM,
  while the vpsAdminOS-only provider retains its earlier minimum. Existing
  complete disk images require no format conversion and no coordinated machine
  update.
- Direct boot passes `init=<toplevel>/init`; that closure must exist inside a
  retained root. The documented rollout copies and activates the reviewed
  configuration in each running NixOS guest before stop/start. This ordering is
  necessary and sufficient for the selected closure to survive host-side result
  root removal. A failed update must be retried while the guest remains running,
  or the prior matching configuration must be restored before boot.
- The reverse mixed-version direction is deliberately unsafe and is documented:
  an older organization runner omits the keyword, selecting OSVM's default
  fresh-image behavior and replacing retained roots on start. Rollback may still
  inspect or stop existing state, but operators must not start retained NixOS
  disks with the older provider. This incompatibility, its impact, update order,
  and operator action are recorded in the initiative plan and README.

## Residual risks and test gaps

- No new VM has been booted with these commits. The planned acceptance must
  verify known API/database data and known container/host marker contents across
  a full stop/start, not only machine status or disk metadata.
- The OSVM unit tests prove process-failure atomicity and exact content retention;
  they do not simulate host power loss around `rename` or validate filesystem
  durability with `fsync`. They also cannot identify a corrupt or partial root
  left by older tooling: preservation intentionally trusts an existing image, so
  an incomplete legacy image requires explicit reset or recovery.
- The cross-project runner tests use focused fake constructors. Final packaged
  runner build/load and exact-pin smoke remain necessary to prove the actual Ruby
  load path exposes the keyword before deployment.
- A configuration build can select a new direct-boot closure before an in-guest
  copy succeeds. If that update fails and the VM is then stopped or crashes,
  restarting with the new configuration can fail because the closure is absent;
  the retained data is not erased, but recovery requires retrying the update or
  selecting the prior configuration. The deployment plan explicitly avoids this
  state by updating while the current VM is running before restart.
- The node tests shorten the never-ready path through their timeout stub rather
  than waiting the full 180 seconds. Live bridge restart remains the material
  check for the original osctld startup ordering.
- The vpsAdminOS worktree contains an unrelated generated `libosctl/tmp/`
  directory from local verification. It is outside the committed review range
  and should be removed during normal initiative cleanup.
- The previously accepted non-transactional forced-certificate replacement
  behavior is unchanged and must remain unused during live acceptance.
