# Review verification

This is the original review, before implementation. For the fixes and current
test results, see [implementation validation](runtime-validation.md).

All work used vpsadminos `1a6c9980cf6e8c7eb8c73f063788708f5c93d447`.
No tracked project files changed. No VM or kernel was built or booted.

Follow-up: nine additional old-kernel compatibility characterization examples
passed (seed 28483), including side-by-side execution of old/new stop frontends
with absent cancellation controls and simulated freezer timeouts. See the
[compatibility report](backward-compatibility.md). These expose a behavior
regression; their passing result is not a compatibility sign-off.

## Native checks

Used `nix develop .#vpsadminos`, which selects `ruby_vpsadminos`, then built
the libosctl/osctld native extensions and the pinned ruby-lxc extension as in
the repository CI script. Set the component Gemfile and owned `.gems` path;
ran from `osctld`:

```sh
bundle exec rspec \
  spec/osctld/container/nfs_cancellation_spec.rb \
  spec/osctld/container/run_configuration_spec.rb \
  spec/osctld/monitor/process_spec.rb \
  spec/osctld/monitor/master_spec.rb \
  spec/osctld/container_control/commands/stop_spec.rb \
  spec/osctld/commands/container/lifecycle_spec.rb \
  spec/osctld/user_control/commands/ct_pre_mount_spec.rb \
  spec/osctld/cgroup_spec.rb
```

Result: **123 examples, 0 failures**, random seed 60836, 0.547 seconds of
example execution. These are focused unit tests with mocked/synthetic
namespace and lifecycle cases; they do not validate kernel concurrency or
daemon-restart recovery after init disappears. The stop tests explicitly
expect the kill to be skipped after cancellation errors.

The `.#osctld` shell uses unpatched Ruby and failed to load libosctl/native
with undefined symbol `rb_thread_start_timer_thread`. The repository's
`.#vpsadminos` shell fixed this; no source or runtime shim was used.

## Kernel selection

Evaluated the actual kernel and livepatch expressions with the worktree's
pinned nixpkgs library. Result:

| Selection | Source | Patch version | Patches |
| --- | --- | --- | --- |
| Stable/unstable 6.12.109 | `9ccd5d6597a6ddbe5b44fb885ddf96e4dbc332dd` | 0 | none |
| Retained 6.12.95 nfs-cancel | `563bbb35e8753e1bb34dad19ebeec8962ee3c1cd` | 6 | nfs-cancel cumulative and uname |

See [machine-readable output](kernel-selection.json). Both affected fixtures
inherit the default. Their contents match between original candidate
`36589f991` and rebased integration `c3f219a38`.

## Existing runtime evidence

Downloaded the artifact from [run 34630335805](https://github.com/vpsfreecz/vpsadminos/actions/runs/34630335805)
into this session's scratch directory. Independently inspected:

- `os-test-osctl__nfs-cancellation-e35cd711`: forced-soft assertion mismatch
  and a kernel oops during cleanup.
- `os-test-kernel__livepatch-kernel-identity-01903708`: missing monitor JSON
  before the identity examples run.

Relevant NFS oops:

```text
BUG: kernel NULL pointer dereference, address: 0000000000000028
CPU: 0 UID: 0 PID: 5025 Comm: master.rb:47 Not tainted 6.12.109 #1-vpsAdminOS
In memory cgroup /system/service/osctld
RIP: 0010:rpc_cancel_tasks+0x4f/0xb0
RAX: 0000000000000000 RBX: ffff8ffe990b1e18
R15: fffffffffffffff8
Call Trace:
 shutdown_store+0x103/0x1b0
 kernfs_fop_write_iter+0x14a/0x1f0
 vfs_write+0x2bd/0x4d0
```

The NULL list link is visible in the register/instruction sequence. The
specific client and interleaving responsible are not identifiable from this
log alone. No rerun was used to dismiss the crash.

## Remaining validation

The report's initialization-error race is established by conflicting source
paths, not by a new kernel reproduction. Restart-after-init-loss and
partial-cancellation scenarios also require targeted VM regressions. The
earlier reported 40 NFS/5 identity passes refer to the old candidate's
6.12.95 selection, not current default-kernel validation.
