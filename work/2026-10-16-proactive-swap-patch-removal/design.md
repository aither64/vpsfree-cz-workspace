# Remove the proactive swap experiment from Linux 6.12.113

Status: approved implementation brief, replacing the earlier proposal in full.
This records the user's final decisions and implementation authorization; it is
not evidence that source changes, checks, review or integration have completed.
Architect0 owns this design. Lead owns coordination, plan/state and acceptance.

## Approved scope and verification boundary

- Change **Linux 6.12.113 only**. Remove the whole experimental series, including
  custom DAMON quota and NUMA scope support. Keep upstream DAMON, native
  `memory.reclaim` and unrelated vpsAdminOS functionality and safety fixes.
- Retire the experiment's QEMU profile, positive tests and entry points. Do not
  preserve legacy experiment fixtures or add normal-reclaim tests.
- Leave every other kernel revision/hash, older selection, frozen boot output,
  Linux 6.18 source/pin and ZFS revision/hash unchanged. The shared DAMON Nix
  module intentionally becomes upstream-only for all kernel selections.
- The user states that the experiment has never been deployed and requires no
  backward compatibility or rollback. No capability negotiation, deprecated
  options, compatibility bridges, migration or coordinated rollout is needed.
- Publish a new Linux feature ref. Do not force-move an existing Linux release
  or default ref. Update the OS's 6.12.113 revision/archive hash once to the final
  Linux result. The user explicitly selected **vpsAdminOS `staging`** for the
  subsequent fast-forward integration.
- Merge after quick static/history checks, required hooks, Nix evaluation and
  mandatory final independent review. **Do not build kernels, boot systems, run
  runtime tests or wait for full CI before this merge.** The user will perform
  the subsequent staging build/boot/runtime validation. This explicit decision
  supersedes the proposal's earlier premerge runtime gates.

## Exact inputs and evidence

The OS investigation used vpsAdminOS
`60f9ed1c153a734880e002b63d6ab7ed5fe87d0e`. At that revision,
`os/packages/linux/available-kernels.nix:47-49` selects the 6.12.113 source below;
`os/packages/linux/packages.nix:25-26,43-44` uses that exact archive revision/hash.
`os/packages/linux/default.nix:38-44` has no proactive-swap package patch switch.
Moving a Linux branch alone cannot change the packaged kernel.

- Upstream Linux v6.12.113 base:
  `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e`.
- Current vpsAdminOS Linux 6.12.113 product tip:
  `11058eb4fe1cba30653e8e643546c13bc8bcd792`.

Exact source and owner history were inspected through read-only GitHub HTTP/API
when the local partial clone lacked the .113 object. The earlier .109-based
uncertainty is resolved. Implementers must materialize and verify these exact
objects before reconstruction, following the authorized Git procedure; do not
substitute a newer upstream release or another downstream branch.

Primary references:

- [Exact product commit history](https://api.github.com/repos/vpsfreecz/linux/commits?sha=11058eb4fe1cba30653e8e643546c13bc8bcd792&per_page=100).
- [Mixed controls owner](https://api.github.com/repos/vpsfreecz/linux/commits/a9dd8baca1c921a11942fdc63862be4fcab2dce3).
- [Upstream DAMON module parameters](https://raw.githubusercontent.com/vpsfreecz/linux/7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e/mm/damon/reclaim.c).
- [Upstream common parameter macros](https://raw.githubusercontent.com/vpsfreecz/linux/7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e/mm/damon/modules-common.h).

## Linux reconstruction: implementer0

Create an isolated session-owned feature worktree and preserve the exact old tip
in a dated backup before rewriting the feature history. The lead-approved scope
preserves the 50-commit published, OS-consumed prefix through
`108d4158fae3c0d0affb58491ee67b9f573b550e` (the first experimental owner's
parent) **commit-identically**. Start the new feature at that exact prefix and
reconstruct only the affected suffix, omitting all six owners below. The result
still descends from the exact upstream v6.12.113 base. This is a clean feature
suffix, not six revert commits followed by repairs. Do not rewrite existing
published release/default history or automatically normalize unrelated prefix
stages/messages such as loadavg, CPU visibility or Common functions.

The full upstream-to-result series remains inventoried and reviewed. Identify
those inherited stages/messages explicitly as existing consumed baseline, not
as newly normalized history. Also give the reviewer the task-owned
`108d4158..new-head` suffix and the old-product-to-new-product final tree diff.
This scope boundary is not a waiver for malformed new or revised suffix owners.

| Exact owner to omit | Subject |
| --- | --- |
| `a9dd8baca1c921a11942fdc63862be4fcab2dce3` | mm: add proactive DAMON reclaim controls |
| `b1fe371e52aa7e7bee1ee5490c408ffed9a28c5d` | mm: expose proactive swap via virtual swap views |
| `a2425d1734ae90527da3f8494c76d839c2a60712` | mm: account proactive swap on top of virtual swap |
| `7b11a3286173b93209b2c4c1f27614aed946cf5a` | mm/damon: add per-node reclaim scope support |
| `c89d7963a742b99287fd41c007f3358967ba15a2` | mm/damon: fix damon_reclaim scope updates from sysfs |
| `5bbdd2635be1a3ca6a34201626e93cee78256e70` | docs/mm/damon: document reclaim scope |

Remove the experiment's dependent interfaces, implementations and documentation:
`system_proactive_swap`/`MEMCG_RECLAIM_SYSTEM_PROACTIVE_SWAP` plumbing,
per-memcg proactive counters, swap-entry proactive bitmap, `proactive` swap-event
field, `virtual-system` reporting and synthetic swap totals, custom free-memory
quota metrics/parameters, and custom global/per-node reclaim scope.

The controls owner touches `include/linux/{damon,memcontrol,swap}.h`,
`mm/{internal.h,madvise.c,memcontrol.c,memory.c,shmem.c,swap.h,swap_slots.c,swap_state.c,swapfile.c,vmscan.c,workingset.c}`,
`mm/damon/{core,paddr,reclaim,sysfs-schemes}.c`, and related documentation. The
views owners also touch `fs/proc/meminfo.c`, `kernel/sys.c`,
`include/linux/swap_cgroup.h` and `mm/swap_cgroup.c`; scope owners additionally
touch `mm/damon/{dbgfs,lru_sort}.c`. Use the exact diffs as the file inventory;
this list is a guide, not permission to discard unrelated changes in a file.

Retain all other logical behavior, including these adjacent safety fixes:

| Retained owner | Behavior to preserve |
| --- | --- |
| `b2c3db758ae499f7b6cdb116e41fba26e219ba08` | Memcg CSS reference ownership in ordinary memory/swap views |
| `35b639015c452a5834371ee67b31554031780f31` | Missing/early memcg CSS guards |
| `0ffa2e5c545f333fc43f116ad4ce17e1e35e86be` | Null guard in memcg reclaim-iterator invalidation |
| `8d97a7a9c6aa096d58ff87269168b28c54a9b548` | Intersection of fake affinity masks |
| `11058eb4fe1cba30653e8e643546c13bc8bcd792` | Cold NLM client handling during NFS sysfs shutdown |

The affected suffix has these logical dispositions:

- Transplant `0ffa2e5c545f` as the independent generic memcg iterator fix. Preserve
  its original author, full explanation, report/sign-off and unmarked subsystem
  identity; do not invent an upstream commit for this locally authored fix.
- Combine `b2c3db758ae4` and `35b639015c45` into one `[vpsAdminOS]` CSS lifetime
  safety owner, including required ordinary-swap-view adaptation. Preserve Pavel
  Snajdr's authorship/sign-off, original CSS corruption and seq-file lifetime
  rationale, and truthful provenance for both source commits. Explain the early
  missing/disabled CSS guard as part of the same safe-reference contract. Advance
  the logical version for this fold/adaptation from the highest evidenced prior
  version; the inspected source owners are unversioned first versions. Record
  substantive development history; do not fabricate old runtime validation.
- Keep `8d97a7a9c6aa` as the independent affinity fix, with `[vpsAdminOS]` identity.
  Preserve Jakub Skokan's authorship/sign-off and the existing crun 1.27/CPU-quota
  rationale: intersect broad masks, reject empty intersections. A changed Git
  hash or marker-only correction is not itself a semantic version advance;
  substantive source/message changes follow the policy's version/history rule.
- Keep `11058eb4fe1c` as the independent marked NFS cold-NLM fix, preserving
  Pavel Snajdr's authorship, sign-off and existing 6.12.109 provenance. A pure
  transplant does not require a new logical version.

The combined CSS owner can precede affinity because the safety and scheduler
changes are independent; preserve final-tree behavior and account for the move.
Do not retain a separate early-guard repair after the combined CSS owner. No
unrelated prefix consolidation is required for this assigned change.

### Ordinary reporting retained from the mixed owner

Removing `a2425d1734ae` also removes useful ordinary reporting behavior when
proactive swap is absent. The lead approved a standalone ordinary-view owner
in the new suffix, and accepted the final review's concrete related corrections
below. All six experimental owners remain omitted. The allowed scope is these
reporting paths in `kernel/sys.c`, `fs/proc/meminfo.c` and `mm/swapfile.c`;
this supersedes the earlier kernel/sys.c-only restriction.

| Reporting path and ordinary state | Required behavior |
| --- | --- |
| `kernel/sys.c:do_sysinfo()`, unlimited cgroup-v1/v2 swap controller | Preserve host capacity from `si_swapinfo()` rather than returning zero for v1 or treating `PAGE_COUNTER_MAX` as finite capacity for v2. Retain the already prepared ordinary fix. |
| `fs/proc/meminfo.c`, cgroup-v1 unlimited memsw | Remove `PAGE_COUNTER_MAX` from the zero/no-swap case so the existing unlimited branch is reachable. Retain host swap capacity and subtract only actual swap charge. |
| `fs/proc/meminfo.c`, cgroup-v1 finite memsw | Establish container swap capacity (`memsw - totalram`) before deriving free swap; do not calculate free swap from the earlier host capacity. |
| `kernel/sys.c` and `fs/proc/meminfo.c`, cgroup-v2 finite limit below current usage | Report free swap as zero. Lowering `memory.swap.max` below existing use is legal; unsigned subtraction must not wrap. Preserve the configured capacity and actual usage. |
| `mm/swapfile.c:fake_swap_show()`, computed capacity zero | After controller/host capacity selection, return without a synthetic row when `totalswap == 0`. The header already emitted remains; an unlimited controller on a host with no swap is header-only for both cgroup versions. |

For the changed cgroup-v1 paths, ordinary swap charge is
`max(memsw_usage - memusage, 0)` because memsw combines resident memory and swap.
The cgroup-v2 aliased counter is already swap-only. Compute free space using the
selected capacity and clamp subtraction to zero when usage reaches/exceeds that
capacity; the resulting value must stay within `0..capacity`. These local
calculations are part of the precise reporting corrections, not a new accounting
model. Keep the existing zero-limit behavior and do not alter swap enforcement,
charge counters, host reporting, unrelated memory fields or other paths.

Do not reintroduce proactive counters/bitmap/events, synthetic `virtual-system`
metadata, quota/scope controls or limit bypass. In the empty-capacity path, add
only the ordinary no-row guard; do not restore the removed experimental row
selection logic. Do not use this boundary to create shared reporting frameworks,
add new tests, or make a general saturation cleanup across other paths.

Provenance: extract the ordinary intent from
`a2425d1734ae90527da3f8494c76d839c2a60712`, credit its original author and explain
adaptation to ordinary counters. Do not copy its treatment of combined v1
memory-plus-swap usage as if all of it were swap. Do not claim that the complete
experimental owner is retained. Keep the resulting ordinary owner marked
`[vpsAdminOS]`, with a meaningful explanation and truthful development history.

Fold all accepted reporting corrections into this same ordinary-view owner;
do not append repair/fixup commits. The reviewed owner at `86d54e7adff8` is v2;
advance it to v3 for the substantive meminfo/empty-capacity/reduced-limit fixes
and describe those changes in its history. Preserve source provenance and the
previous published head as directed by the lead. Implementer0 owns diagnosis,
source edits, check evidence and commit preparation. Await the reviewer's
consolidated findings and the lead's final feature-ref/publication choice before
final publication and the dependent OS repin; keep the OS history to one final
logical pin update. Rerun affected quick checks and independent review.

Concrete source evidence at reviewed head `86d54e7adff8`:
`fs/proc/meminfo.c:83-90` contains the unreachable v1 unlimited branch and
host-before-container calculation; its lines 99-100 and
`kernel/sys.c:2903-2904` contain finite-v2 unsigned subtraction;
`mm/swapfile.c:3043-3064` prints a row without checking selected zero capacity.
Existing vpsAdminOS `tests/suite/kernel/vpsadminos/memory-view.nix:198-219`
expects ordinary meminfo swap totals/free values, lines 265-282 cover native and
compat sysinfo, and lines 329-340 expect header-only output when unlimited mode
has no host swap. Keep these tests unchanged. Give the final reviewer the exact
reporting-path diff and the ordinary-state reasoning, including usage above a
lowered finite v2 limit. No new test or premerge runtime gate is introduced;
runtime results remain unverified until the user's staging validation.

Adapt the CSS lifetime fixes around restored ordinary swap views where their
context overlaps removed feature code. Preserve upstream `proactive_swappiness`
and `MEMCG_RECLAIM_PROACTIVE`; a broad search-and-delete for "proactive" is wrong.
Keep ordinary meminfo, `sysinfo(2)`, `/proc/swaps`, cgroup controls and native
DAMON/pageout semantics. Do not disable generic DAMON kernel configuration.

Follow `docs/os/patch-series-policy.md`: record old-to-new owner mapping in
ordinary Markdown evidence, preserve unrelated patch equivalence, fold caused
adjustments into the logical owner and advance revised owner versions/history
where required. Do not expand scope into unrelated functional cleanup. Supply
complete range/final-tree evidence and explicit no-migrations provenance for
independent review. Publish the final new feature ref over SSH; retain it because
the OS pin will consume its exact commit. Publication is not release promotion.

## OS consumers, tooling and final pin: implementer1

Work in the session-owned vpsAdminOS feature worktree, rebased onto the selected
`staging` integration target under the Git procedure. The module/tooling package
can proceed independently while implementer0 reconstructs Linux. The final pin
is dependent on the final published Linux head.

### Upstream-only DAMON module

In `os/modules/config/damon-reclaim.nix`, delete these public options and their
assertions, descriptions and generated service writes:

- `boot.damon.reclaim.scope`, including the `write_scope` helper/call;
- `boot.damon.reclaim.quota.freeMemRate` and `quota_free_mem_rate`;
- `boot.damon.reclaim.quota.freeMemBytes` and `quota_free_mem_bytes`.

Retain the module, its global import and ordinary enable/disable/reconfiguration
behavior. It declares a service even when disabled and writes parameters whenever
the parameter directory exists (`damon-reclaim.nix:293,300,341-359` at the
investigation revision). Unsupported writes therefore break disabled instances
too. Remove them outright; add no version checks, capability probes, fallbacks,
fake files or legacy aliases.

The remaining currently-written parameters were checked against upstream
v6.12.113 and must remain supported:

`min_age`, `quota_ms`, `quota_sz`, `quota_reset_interval_ms`,
`quota_autotune_feedback`, `wmarks_interval`, `wmarks_high`, `wmarks_mid`,
`wmarks_low`, `sample_interval`, `aggr_interval`, `min_nr_regions`,
`max_nr_regions`, `monitor_region_start`, `monitor_region_end`, `skip_anon`,
`enabled`, and `commit_inputs`.

### Retire the experiment tooling

Delete:

- `os/configs/proactive-swap-qemu.nix`;
- `tests/suite/kernel/proactive-swap.nix`;
- `tests/suite/kernel/proactive-swap-cgroups-v1.nix`;
- `tests/suite/kernel/proactive-swap-common.nix`.

Remove their targets/output entries from root `Makefile`, `os/Makefile` and
`flake.nix`. Remove proactive-swap test registration, environment selectors and
selection branches from `tests/all-tests.nix`, preserving unrelated local-only
and livepatch selectors. Search for dangling references to deleted paths,
outputs, removed options and experiment environment variables. Retire any
remaining experiment-only references within this boundary; refer unrelated
consumers or scope changes to the lead.

Do not replace these with legacy fixtures or a new normal-reclaim suite. Leave
existing ordinary memory-view cgroup-v1/v2 test files unchanged. Leave
6.18-specific documentation and generic DAMON configuration alone unless a
reference directly names tooling being removed.

### Final source pin

After implementer0 supplies the final published Linux ref/head, compute and
verify the source archive **byte hash** used by the existing `fetchurl` path.
Change only the 6.12.113 `rev` and `sha256` in
`os/packages/linux/available-kernels.nix`. Keep one final logical pin update;
no placeholder or sequence of superseded pins may remain in final history.
Do not change any ZFS pin, other kernel entry or frozen boot artifact.

## Premerge acceptance and sequencing

Lead prepares the mandatory initial plan/state tracking commit before the first
project-code commit or external mutation. Architect0 edits only this brief;
implementers own source, project documentation, hooks, commits and remediation.
Lead serializes Git/integration steps and reviews material design deviations.

1. Linux reconstruction accounts for all six omissions and all retained owners.
   Compare the complete series and final tree with the original product tip;
   verify unrelated retained behavior is patch-equivalent or explain required
   context adaptation. Confirm experimental symbols/interfaces/docs are absent
   while native DAMON/reclaim and ordinary virtualization remain.
2. OS quick checks cover the intended diff and required formatting/hooks; confirm
   removed files/options/selectors have no dangling consumers. Inspect generated
   DAMON service text for supported upstream parameters only.
3. Run bounded Nix evaluation/instantiation for default and explicitly selected
   6.12.113 configurations, with DAMON disabled and enabled. Check surviving test
   discovery, flake/Makefile references, and unchanged other kernel/ZFS pins.
   These are evaluation checks, not system/kernel builds. Stop and investigate
   any unexpected kernel build rather than expanding the approved gate.
4. Commit all intended changes, including the exact final OS pin/hash. Run the
   mandatory independent final review over both final deliverables, complete
   branch histories, source diff, pin linkage and no-migrations conclusion.
   Resolve findings through the assigned implementers and repeat affected quick
   checks/review as required. Review must cover the final pin, not a placeholder.
5. After acceptance, lead integrates vpsAdminOS into `staging` fast-forward-only
   through the selected package's coordinated merge workflow. Read
   `workspace-host coordination guide` and the required workspace procedures
   before integration; use the operation queue/reservation where applicable.
   The Linux feature ref remains published; do not force-move any existing Linux
   release/default ref. Keep final exact heads and evidence in session state.

No premerge kernel/module compilation, VM boot, runtime test, full suite or full
CI wait is required or authorized by this gate. CI may start automatically after
publication/integration; do not wait for it or make its completion a merge gate.
Quick checks and independent source review cannot prove compilation or runtime
correctness. Report the result as merged with staging validation pending.

## Subsequent staging validation and compatibility

The user owns the next stage: build the exact merged system with matching kernel,
in-tree and ZFS modules, boot it on staging nodes, run existing ordinary
memory-view cgroup-v1/v2 cases and smoke-check DAMON disabled/enabled operation.
No new tests are to be authored. Confirm the system/kernel store path or build
identity; `uname` alone cannot distinguish old/new builds named 6.12.113.
Do not launch this stage autonomously. If later assigned long focused checks,
use the required fresh verification watcher; do not expand to full CI.

Expected behavior is normal cgroup charging and swap views, no `virtual-system`
row or custom proactive swap event, no custom scope/free-memory quota parameters,
and a healthy DAMON service using upstream controls. Cgroup-v1 memsw is a combined
memory-plus-swap limit, unlike cgroup-v2's independent `memory.swap.max`; do not
interpret their limits as identical when assessing staging observations.

No database, API/client, Terraform, daemon protocol, persisted container format
or on-disk migration is introduced. Removed experimental Nix options deliberately
stop evaluating; retire known callers directly. Other retained kernels still
contain their own old code, but the common module no longer offers experimental
controls and the experiment test tooling is retired by explicit user choice.
There is no requirement to preserve old experimental configuration behavior.

The never-deployed premise means no coordinated fleet update, compatibility
transition or rollback design is part of this work. Backups of source refs protect
reconstruction evidence only; they do not introduce a deployed recovery contract.
Actual staging deployment remains the user's next action, separate from merging
vpsAdminOS `staging`. Keep the session open and describe validation limits honestly.
