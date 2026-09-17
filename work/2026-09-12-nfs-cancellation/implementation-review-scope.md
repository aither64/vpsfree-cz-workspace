# Scope and proportionality review

Reviewed the requested outcome, `plan.md`, `state.md`, the three exact revision
ranges in `implementation-review-packet.md`, repository history, the exact OS
tree at `75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d`, the retained-kernel change at
`fbe36622894dbc46f82e970dcae5da18d6e58c8c`, and
`scratch/linux-default-final.patch` for
`fb4ad1506c1d22ab92251b3ba167ca951d453b8e`.

## Blocking

None.

## Important

### 1. Diagnostic instances rerun the complete functional NFS matrix

Commit `75e1d26df4acaea85f20c3ce2ac6ec6046fc1d5d` registers normal and diagnostic
instances for both 6.12.95 and 6.12.109 in `tests/all-tests.nix:163`. In
`tests/suite/osctl/nfs-cancellation.nix`, only the fault-injection block at line
155 is conditional on `diagnostic`; the full common suite at line 217 still runs
for every diagnostic instance. That common suite already iterates NFS 3, 4.0,
4.1, and 4.2 and contains deliberate 30-second outage waits, repeated five-second
blocked-operation waits, container restart cycles, and all userspace persistence
cases. The base revision already ran this functional matrix once; the change now
runs it four times, including twice under costly KASAN/lockdep kernels.

The repaired source in each kernel needs its fault-injection/lifetime regression,
and the functional cancellation path should run once on each repaired kernel.
Running every protocol-independent stop, restart, namespace, and isolation case
again merely because the kernel has diagnostic instrumentation does not validate
additional owned behavior. It materially increases integration time and the
number of unrelated ways the source-specific lifetime test can fail.

Keep the normal functional instance for each repaired kernel, but make diagnostic
instances run only the sysfs lifetime test, either through a separate diagnostic
test template or by excluding the common matrix when `diagnostic` is true. This
preserves all requested kernel coverage without duplicating the full suite.

### 2. Any `flake.nix` edit now schedules the complete kernel build matrix

The same commit adds `flake.nix` to both push and pull-request path filters in
`.github/workflows/kernels.yml:9-21`. A matching change starts every regular
kernel build plus both new diagnostic builds (`.github/workflows/kernels.yml:44-57`),
each on a self-hosted runner with an eight-hour timeout. `flake.nix` owns the
whole repository flake, including test plumbing, packages, development shells,
and unrelated system outputs; most edits to it do not affect kernel or diagnostic
closures.

The broad trigger is an incidental consequence of defining the two diagnostic
outputs directly in `flake.nix`, not a requirement of publishing those outputs.
It permanently expands an expensive workflow for unrelated future work. Put the
diagnostic output definition or its eligibility data in a kernel-specific file
already covered by `os/packages/linux/**`, add a narrow watched file, or use the
detect job to skip builds when kernel-relevant inputs did not change. The workflow
should still run when the diagnostic config, kernel registry, or workflow changes.

## Advisory

None.

## Scope assessment and residual gaps

The substantive implementation is otherwise proportionate to the accepted
boundary. Durable namespace bind mounts, the boot/RunId sidecar, ownership and
namespace checks, terminal intent, and the inherited worker lock each address a
specific restart, PID reuse, namespace-departure, or duplicate-worker failure in
the request. The shared forced-stop deadline and deadline-aware child runner have
current consumers in all forced-stop paths and are necessary to bound killing,
recovery, and verification without deleting a live ephemeral container. The
final userspace tree removes the rejected legacy per-filesystem/per-netns fallback
rather than retaining an obsolete compatibility layer.

The retained 6.12.95 commit is limited to the demonstrated sysfs/client lifetime
repair and its fault-injection hook. The default 6.12.109 commit ports the already
accepted full cancellation ABI, sticky admission machinery, NLM locking
prerequisite, and the same lifetime repair. Its global registration and
user-namespace barrier are warranted by the explicit requirement to cover
initializing, processless, and future descendant namespaces; a process scan or
per-mount fallback would not satisfy that contract. Kernel pins, livepatch
identity selection, documentation, and action-version updates follow directly
from the requested exact-kernel rebuild and repository workflow rules.
The three OS commits keep userspace behavior, kernel selection, and long-running
VM/CI coverage reviewable, while each Linux range contains one coherent source
change. No superseded branch iteration remains in the reviewed history.

Actual NFSv4 migration/transport-replacement runtime coverage remains absent, as
the packet records. That is a material test gap for risk review, but it does not
justify rerunning protocol-independent userspace behavior in diagnostic instances.
