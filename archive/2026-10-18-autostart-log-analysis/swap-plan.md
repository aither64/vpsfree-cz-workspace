# Swap activation fix plan

Planning only, 2026-10-18. This document does not authorize implementation,
repository integration, history rewriting, release-ref promotion, deployment or
reboot. The completed osctld work and its [design](design.md) are preserved.
Histfile changes are excluded. The lead owns plan acceptance and coordination;
architect0 owns this plan, with independent source reports from implementer0
(kernel lineage) and implementer1 (service and regression coverage).

## Scope and baseline

Fix the node1.stg incident on the stable **6.12.113** line. Use vpsAdminOS
`origin/staging` at `60f9ed1c153a734880e002b63d6ab7ed5fe87d0e`, the verified
merged osctld result; no deployment followed that merge. Revalidate the explicit
ref before a future implementation. Do not select the bare repository's HEAD,
stale master, 6.18, or an unrelated release as a substitute.

At this OS revision, `os/packages/linux/available-kernels.nix` selects:

- Linux 6.12.113: `11058eb4fe1cba30653e8e643546c13bc8bcd792`.
- Its ZFS source: `481845fca6ae3f61ca2262c1a5693a58ae364650` and existing
  `zfs235-free-account.patch`; retain both.

Only Linux's proactive swap bitmap allocation/freeing, the generated swap
service's failure propagation, focused regression coverage, and the eventual
single stable-kernel source pin/hash change are in scope. No kernel version
upgrade, swap-format change, repartition, container-limit change, disabling of
swap accounting, osctld follow-up, or configuration-repository edits are planned.

## Evidence and failure mechanism

The node's new boot logged at 10:21:08 CEST on 2026-10-18. At 10:21:09.918,
`__alloc_pages_noprof` warned while `swap_cgroup_swapon` requested order 11,
then reported `couldn't allocate enough memory for swap_cgroup`.
[Host evidence](node1-host-since-1014.log) lines 8475–8525 preserves the trace.
At 10:21:09.929 both `/dev/sda` and `/dev/sdb` failed swapon with
`Cannot allocate memory`, immediately followed by false service-success
messages ([runit evidence](node1-runit-since-1014.log), lines 145–148).

The exact deployed [swap source](deployed-swap_cgroup.c) allocates
`proactive_map = bitmap_zalloc(max_pages, GFP_KERNEL)` at line 211. Its
[page allocator](deployed-page_alloc.c), lines 4818–4823, rejects orders above
`MAX_PAGE_ORDER`. At 4 KiB pages with maximum order 10, a proactive bitmap for
more than 128 GiB of swap exceeds the 4 MiB contiguous allocation bound;
a 256 GiB swap area requests approximately 8 MiB (order 11). This is an
allocation-size defect, not proof of physical RAM exhaustion. Exact physical
swap sizes and current activation state were not established by the captured
logs. The service's successful-finish marker is not evidence of active swap.

## Intended changes and invariants

In Linux `mm/swap_cgroup.c`, allocate the zero-filled bitmap using
`kvcalloc(BITS_TO_LONGS(max_pages), sizeof(*proactive_map), GFP_KERNEL)`.
Use `kvfree` for **both** matching releases: failed `swap_cgroup_prepare`
cleanup and normal swapoff. Preserve overflow-safe sizing, zero initialization,
publication under the existing mutex, existing pointer clearing, lifetime,
locking, bit indexing and proactive/ordinary per-cgroup accounting semantics.
Do not change the separate existing map allocation or swap-entry format.
Allocation failure must retain its existing clean failure result, without
stale pointers or partial publication.

In vpsAdminOS `os/modules/config/swap.nix`, explicitly check the swapon result
and enter the existing failure path when activation fails. Keep the change
local to swapon; do not enable global `set -e` or change unrelated service
control flow. A successful service must correspond to the configured device
appearing in `/proc/swaps`; an activation failure must not reach the oneshot
success/done path. Repeated service attempts must retain normal supervisor
behavior and must not format or otherwise alter swap media.

## Kernel lineage and publication boundary

The deployed Linux head is consumed history and must remain available with all
published refs intact. The repository's
`docs/os/patch-series-policy.md` requires a caused downstream repair to be folded
into its logical owner, with an advanced patch version and development history.
It provides no blanket exception allowing a permanent later repair commit just
because the defective owner was deployed.

The planning task performs no history operation. An existing published candidate
has been found: `fix/swap-cgroup-bitmap-6.12-20261018` at
`50e2a54f0d04b1ad2885374637b3840be37a1344`. **Validate and reuse that exact
candidate if its source delta and owner history satisfy this plan; do not
duplicate an already completed kernel fix.** The lead and implementer0 are
checking its exact deployed-owner lineage and tree difference. Reconstruct a
new corrected sibling maintenance series only if that inspection identifies
required corrections, retaining both existing refs unchanged.

Never force-update the current Linux default/release ref. Promotion to any
existing target and OS integration require separate explicit direction and the
applicable fast-forward-only integration checks. A diverged sibling needs a
separately selected target, not a force push; OS consumption of its exact SHA
does not establish Linux default integration or session completion.

After the corrected Linux head and its history are final, update only the
6.12.113 source revision/hash in `available-kernels.nix`. Hash the fetched
archive bytes used by `fetchurl`, not the unpacked source tree. Keep one final
pin commit and preserve all other kernel entries and the ZFS inputs.

## Implementation packages and dependencies

| Owner | Independent files and result | Dependency |
| --- | --- | --- |
| implementer0 | Validate existing Linux candidate's `mm/swap_cgroup.c`, owner/version/provenance and complete sibling series; make kernel corrections only if validation requires them | Exact deployed owner/lineage and candidate delta verified first; no consumed ref may change |
| implementer1 | vpsAdminOS `os/modules/config/swap.nix`, focused VM test(s), `tests/all-tests.nix` registration, and final `available-kernels.nix` pin/hash | Service/test authoring can proceed independently; final pin and combined runtime check require implementer0's final head |
| architect0 / lead | Design decisions, source-boundary acceptance and sequencing / shared Git coordination and final review assignment | Reconcile reports and any material deviation before integration work |

When implementation is authorized, use session-owned isolated worktrees after
the normal preflight. Owners may edit independent files concurrently. Serialize
staging, commits, rebases and publication within each repository through the
lead; stage only owned paths and retain all refs. Record source rationale with
the owning component, test evidence in session records, and no parallel ledger.

## Acceptance and verification sequence

1. Quick checks: kernel patch/style and allocation/free-path inspection; Nix
   formatting and evaluation of generated service and registered tests. Confirm
   exact stable kernel selection, unchanged ZFS input and preserved osctld fix.
2. Commit the complete intended kernel, service, tests and single final pin;
   consolidate development follow-ups. Run mandatory independent final review
   of exact committed heads after quick checks, before long builds/tests.
   Review the entire corrected sibling range, provenance, final source delta,
   publication boundary and OS base-to-head series; explicitly note no migration.
3. Use a fresh prescribed verification watcher for long kernel builds and VM
   tests. Kernel compilation is intentional for this change; record that reason
   and follow the normal cache/build path. Final evidence must use the exact
   Nix-pinned kernel and OS heads, not merely an unrecorded local kernel stage.
4. In a disposable VM, provide a dedicated **sparse 256 GiB virtual block
   device** with 4 KiB guest pages. Format only that explicitly owned test device
   as swap. Never activate host swap or allocate 256 GiB of real host storage.
   Keep guest workload and written backing storage bounded; this tests metadata
   size, not filling the entire device. Confirm the old kernel's allocation
   failure when feasible, then corrected activation in `/proc/swaps`, matching
   capacity, absence of allocator warnings, and successful swapoff/swapon cycles.
5. Exercise real bounded anonymous memory in cgroup v1 and v2: verify actual
   per-cgroup ordinary/proactive swap accounting, page-content integrity after
   reclaim/refault, counter cleanup after freeing the workload, and swapoff with
   sufficient memory. Reuse existing proactive-swap coverage while explicitly
   forcing corrected stable 6.12.113 so its config cannot silently select 6.18.
6. Test the generated service with successful activation and a controlled
   failed activation (a disposable device without a valid swap signature).
   Failure must be observable and must not create a successful done marker;
   success must show the device in `/proc/swaps`. Verify repeated activation
   and failure cleanup without corrupting the test device or other service state.
7. Reconcile any findings, rerun affected quick checks/final review before long
   retest, and report exact heads and results. These are planned checks, not
   tests performed by the planning task.

## Compatibility and future rollout/recovery

No database/schema, public API/CLI, generated client, Terraform, service-wire or
on-disk swap-format change is required. The bitmap is kernel memory only.
Generated Nix service behavior changes to report activation failure honestly;
no new module option is needed. Old/new nodes can coexist and there is no need
for a coordinated fleet-wide upgrade.

A future authorized rollout would first build/cache the exact tested stable
kernel and OS, then select node1.stg for a maintenance reboot after validating
its current swap devices, capacity, container workload and memory headroom.
Deploying the source fix alone cannot change the running kernel. After reboot,
check exact kernel/build identity, both expected devices in `/proc/swaps`,
actual swap totals and cgroup accounting, service state and absence of the
allocator warning. Do not treat a done marker alone as success.

Retain a bootable previous generation and operational console access. Rollback
can read existing container/filesystem/swap state, but the old affected kernel
reintroduces the activation defect; choose a separately verified known-good
generation if rollback is needed. Never require repartitioning, reformatting
production swap, or disabling swap accounting. No reboot/deploy/recovery step
is authorized or executed by this plan.
