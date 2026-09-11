# General review: node readiness and persistent NixOS disks

Reviewed:

- `vpsfree-dev-workspace`
  `9e8783d68fdf40de04683e419d4f373bc27e3730..19238ca67ad822b362ae60f0cf7e7b4b27d60397`
- `vpsadminos`
  `3eaf7b7320754715b38fc629e7f0ce23d13402cd..e6c4c5cfa27ce3b139bba6475be80cfead4b8df4`

Used the mandatory general lane at high risk and `gpt-5.6-sol`/`xhigh`.

## Findings

No Blocking, Important, or Advisory findings.

## Assessment

The three commits are divided into coherent review units: node pool readiness,
the generic OSVM persistence primitive, and its organization-side consumer plus
exact companion test pin. Commit messages satisfy both repositories' rules and
describe the final behavior and rationale.

The node refresh now keeps all filesystem and device mutations after a bounded,
read-only check that requires both `zpool list` success and osctld's exact
`active` state. GNU `timeout` is available inside supported vpsAdminOS guests
through the core system packages. The actual-heredoc tests exercise delayed
osctld readiness and permanent failure, verify mutation ordering, and verify
that the lifecycle lock is released.

`OsVm::NixosMachine` keeps the existing fresh-root default and adds persistence
only when explicitly requested. Additional disks are still prepared before the
root decision, `destroy_disks` still removes the root and file-backed data disks,
and a same-directory temporary file plus rename prevents a failed new copy from
being published as the retained root. The specs verify exact retained contents
across separate machine instances, reset behavior, extra-disk preparation, the
unchanged default, and failed-copy cleanup.

The organization runner requests persistence only for `nixos` machines. It
checks the public OSVM capability before constructing any machine and publishes
its PID only after construction, so an unsupported input exits without making a
stale runner PID appear live. A vpsAdminOS-only runner remains compatible with
the old constructor. The exact smoke-test pin points to the reviewed and pushed
OSVM commit.

The raised vpsAdmin provider minimum is intentional and explicit. Both the
provider README and OSVM integration documentation describe the direct-boot
closure constraint: configuration changes must be copied and activated while
the retained VM is running before it is stopped and booted with the new config.
They also document that an older runner can replace a retained root with a fresh
image. This matches the planned deployment order and accepted rollback limit.

## Residual limits and test gaps

- The new heads have not yet completed the planned live bridge start and
  stop/start retention proof. Acceptance must verify known API database content
  and the existing container/host marker contents after restart, not only VM or
  dataset metadata.
- Persistence deliberately trusts an already existing root path as a complete
  image. A partial file left by an interrupted pre-atomic runner is outside the
  compatibility promise and may require explicit reset; the plan and README
  scope reuse to existing complete images.
- Closure availability is an operator-enforced ordering contract. Starting a
  stopped retained root against a changed direct-boot configuration before an
  online `update` can still fail to boot; both documentation locations state
  this limitation.
- The node tests model osctld delay with ZFS already available. The combined
  condition and outer timeout were inspected directly, but live acceptance is
  still needed for the real import/socket startup sequence.
- The vpsAdminOS worktree contains the untracked generated directory
  `libosctl/tmp/`; it is outside the reviewed commits and should be handled as
  test cleanup without altering the reviewed delta.
