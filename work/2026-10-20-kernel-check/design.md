# Kernel hang investigation brief

## Question and scope

Determine whether changes in vpsAdminOS's custom Linux patches between
6.12.95 and the 6.12.113 kernel used on node24.prg can explain the reported
hang: the console remained at a login prompt with a blinking cursor, while
the machine was otherwise unresponsive.

This is an investigation, not an implementation or rollout. Read canonical
bare repositories and production logs without changing them. Only this
session's investigation records are writable. The lead serializes any necessary
fetch/ref changes. Do not build kernels, change host settings, reproduce on
production, reboot, deploy, merge, or alter the session lifecycle.

Audit custom patch changes first. The user subsequently authorized an upstream
patch investigation if the custom audit yields no supported cause. That second
phase must be explicitly identified and targeted by incident evidence; do not
mix broad upstream change counts into the downstream conclusions.

## Evidence and confidence

Keep three separate propositions for every finding:

1. A code defect exists in a precisely identified version.
2. Its required configuration and triggering conditions are possible on the
   affected node.
3. The incident actually exercised that defect.

Source proof can establish the first proposition and sometimes the second; it
does not automatically establish the third. Report a cause only when a complete,
reachable failure chain is obvious from source and consistent with incident
evidence, or when focused verification reproduces it on the relevant code.
An unproven concern, commit subject, plausible subsystem match, absent log
message, or blinking console cursor does not establish causality.

Use these outcome labels:

- **Confirmed incident cause:** exact deployed code and trigger tied to a
  matching stack, trace, dump, or controlled reproduction with a discriminating
  old/new or fix/revert comparison.
- **Source-proven defect, incident attribution unresolved:** exact code proves
  the failure, but deployed identity or triggering evidence is missing.
- **Not supported:** no demonstrable failure chain or runtime corroboration.
- **Excluded within stated scope:** a specific hypothesis is contradicted by
  exact code, configuration, lineage, or runtime evidence. This does not
  certify the whole kernel.

For concurrency claims identify every lock, context, acquisition order,
reference owner, and progress dependency needed for the proposed cycle or
lifetime violation. Check error paths and compare old and new behavior.
Separate a newly introduced regression from a pre-existing defect.

## Version provenance

The version string alone is insufficient. Record the vpsAdminOS package
revision, Linux commit, matching upstream baseline, applied package patches,
configuration and boot/livepatch identity where evidence is available.
Distinguish the initial 6.12.113 pin from any later repin.

Package values read from the canonical vpsadminos repository's
`os/packages/linux/available-kernels.nix`, corroborated at incident OS revision
`2abbe3cc`:

| Package label | Linux revision | Qualification |
| --- | --- | --- |
| 6.12.95 | `a2384967b90f24d2470c9eb15f0e66d938df7e08` | Current retained pin; has `features.livepatch = true` |
| Initial 6.12.113 | `11058eb4fe1cba30653e8e643546c13bc8bcd792` | Historical first pin; includes proactive swapping |
| Incident/current 6.12.113 | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | Pin at incident OS revision `2abbe3cc`; proactive swapping removed |

The log owner found `vpsadminos=2abbe3cc`, OS `26.05.git.2abbe3c`, generation
144, and a Linux 6.12.113 build timestamp of 2026-10-18 17:47:47 UTC. This build
booted on 2026-10-19 and again after the incident. The previous kernel was
reported as 6.12.95.6; its livepatch identity must be accounted for separately
from the .95 boot source. The inventory owner records immutable package-history
refs and upstream/custom boundaries in
[patch-inventory.md](patch-inventory.md). Runtime identity and timestamps belong
in [log-evidence.md](log-evidence.md).

## Independent work boundaries

The lead owns plan/state, assignments, fetches, portal registration and external
communication. Architect0 owns this brief, causal standards, cross-lane
synthesis and follow-up verification design. Retained roster settings apply.
No repository source files are assigned for edits.

| Owner | Package and writable artifact | Acceptance and dependencies |
| --- | --- | --- |
| implementer0 | Custom patch inventory and exact old/new provenance; `patch-inventory.md` | Account for added, removed, changed and equivalent downstream patches against each version's own upstream baseline. Include initial/current .113 and runtime-identity uncertainty. Send changed symbols early. |
| implementer1 | Central log analysis; `log-evidence.md` | Establish incident interval, timezone, last/first messages, boot/build identity and specific diagnostic evidence. State collection limits and distinguish logging failure from host failure. |
| implementer1, follow-up | Packaged ZFS free-accounting patch; `zfs-patch-audit.md` | Audit `os/packages/zfs/zfs235-free-account.patch` at incident OS `2abbe3cc` against ZFS `481845fca6ae3f61ca2262c1a5693a58ae364650`, including dnode/dbuf locks, reference ownership and transaction accounting. This custom patch ships with .113 but not .95; finish before the conditional upstream phase. |
| architect0 | Fake affinity/scheduler source check and causal synthesis; `scheduler-analysis.md`, `synthesis.md` | Compare the identified affinity owner and immediate helpers; distinguish code changes from message-only identity changes; integrate all lanes without overstating causality. |
| implementer2 | Memory cgroup lifetime, proactive DAMON removal and swap; `memory-audit.md` | Consume inventory; trace changed lifetime, locking and progress behavior. Prove or reject concrete claims against incident pin. |
| implementer3 | Syslog namespace and NFS cold NLM guard; `syslog-nfs-audit.md` | Inspect changed ownership, formatting/iteration and lock paths; report exact source refs and exclusions. |
| implementer4 | Kernel packaging and runtime reachability; `packaging-audit.md` | Identify Nix-applied custom patches/config/livepatch/boot selection outside linux.git; test whether source findings can execute on the deployed package. Coordinate deployed identity with log owner; avoid repeating inventory. |

The lead assigned these refined boundaries after the early inventory. The
architect reports any necessary split or expansion through the lead. Source
reads may overlap to establish interfaces; each artifact has one writer.

The packaging lane identified a relevant kernel-resident change outside
`linux.git`: OS commit `9bca43d3` added
`os/packages/zfs/zfs235-free-account.patch`, selected for .113 at `2abbe3cc`.
Both compared versions select the same ZFS source commit, but .95 lacks this
package patch. Its changes to `dnode_sync.c` move free accounting across
dbuf-mutex/rwlock boundaries. Include this in the custom phase and its coverage
accounting; a Linux-tree-only audit is incomplete.

## Interfaces and invariants

- A direct old-to-new Linux diff includes upstream work. Compare downstream
  ranges against their own upstream bases before assigning semantic ownership.
- Commit subjects and patch versions help locate lineage; equivalent patch
  identity and exact source determine whether behavior changed.
- Package-applied patches and configuration may change effective behavior even
  when the referenced Linux tree is unchanged.
- Historical boot, current running kernel, and on-disk generation can differ.
  A current node read does not prove incident identity without continuity.
- Retain exact hashes and file/function/line references for reproducibility.
  Summarize logs and redact credentials or unrelated tenant content.
- Absence of an error in central logs cannot exclude a lockup that prevented
  local logging or log forwarding.

## Compatibility, deployment and recovery

No persisted state, API, protocol, ABI, schema, Nix option, or production
configuration changes are planned. No coordinated node update is required for
this investigation. A future remedy must receive its own implementation brief:
kernel/module compatibility, livepatch versus reboot choice, mixed fleet
operation, deployment ordering, rollback to a compatible boot generation and
ability to read existing persistent state must be explicit.

No recovery operation is authorized here. Recommendations to collect dumps or
enable diagnostics remain proposals unless separately authorized.

## Checks and stopping conditions

Quick checks: resolve immutable refs; verify upstream ancestry and patch
boundaries; compare corresponding source and caller paths; cross-check
timestamps/timezones and boot identity; verify artifact references and clearly
mark unavailable evidence.

Longer checks are conditional on an actual source candidate: define the
smallest isolated reproducer that distinguishes the proposed mechanism,
specify old/new and fix/revert controls, observable failure signature and
timeouts. Route the experiment through the lead; use the required fresh
verification watcher for long or uncertain execution. Do not start a kernel
build merely to seek a generic passing test.

The downstream phase is complete when the custom delta inventory is accounted
for, source lanes have explicit evidence-based outcomes, and log/package
identity is established or its limits are documented. If no supported custom
cause remains, report that bounded result and propose the authorized targeted
upstream phase. A negative source audit is not proof that the kernel is safe.

The final synthesis must say what is proven, what remains unknown, and the
specific additional evidence or experiment needed to settle remaining claims.
Investigation and evidence alone do not require a mandatory change review.

## Authorized targeted upstream phase

The lead accepted the custom-negative gate after complete Linux inventory,
memory/syslog/scheduler conclusions, package coverage and the bounded ZFS source
audit. The targeted upstream phase is now complete. This was an authorized
investigation expansion, not a claim that upstream Linux caused the incident.

Use these exact stable boundaries, supplied by the inventory owner and resolved
in the canonical Linux repository:

- Old baseline: `296aabce459470a4c1b68ffd0c0c0920e563aaad` (6.12.95).
- New baseline: `7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e` (6.12.113).
- Effective incident tree: `1dfea587406b7dd79973831d1677fb2418e5e9aa`.

An upstream-range commit is a locator, not a finding. Inspect its final
incident-tree source and downstream interactions. The old effective runtime
also included livepatch v6, so an upstream change already backported there
cannot automatically be called new at the upgrade.

Assigned independent packages, now completed:

| Owner | Source boundary and artifact | Evidence/acceptance boundary |
| --- | --- | --- |
| implementer0 | Stable-range provenance, custom-overlap map and old livepatch applicability; `upstream-provenance.md` | Own missing-object materialization. Confirm exact stable ancestry and whether a candidate was already active on .95.6. Supply facts to other lanes, not a second full semantic audit. |
| implementer0, follow-up | Seven upstream printk changes and custom namespace intersection; `upstream-printk-audit.md` | Check final panic predicates, namespace/global locking, console handover and pre-kexec ordering. Equivalent custom bodies alone do not exclude changed upstream context. |
| implementer2 | Upstream reclaim/memcg, cgroup lifetime and memory-accounting changes; `upstream-memory-audit.md` | Focus on changed paths called by downstream helpers and paths compatible with cgroup-v1 `cgroup.memory=nokmem`. Distinguish tenant-local OOM from global allocator or reclaim failure. Identify a concrete new invariant violation or known-fix match. |
| implementer3 | Upstream NFS client, SUNRPC, lockd and directly implicated VFS/writeback paths; `upstream-nfs-audit.md` | Investigate the actual timeout-adjacent evidence, but require an escalation mechanism from one container's NFS failure to host-wide loss. Check transport/error/unmount/close lock dependencies. Earlier .95.6 NFS blockage is a separate control. |
| architect0 | Upstream scheduler, RCU and locking changes that intersect the custom CPU/cgroup paths; `upstream-scheduler-audit.md` | Check changed lock/progress dependencies under observed `preempt=full`, online CPU topology and cgroup namespaces. Avoid attributing cause from cursor blinking or lack of watchdog output. |
| implementer4 | Runtime/config applicability and platform/diagnostic gates; `packaging-audit.md`, `upstream-platform-audit.md` | Match candidates to available boot/config/hardware evidence; verify watchdog/panic and dump expectations from actual configuration. Expand to a driver delta only with a matching incident clue or source-proven defect. No trust bypass or host mutation. |
| implementer1 | Incident follow-up on source-directed discriminators; extend `log-evidence.md` | Search bounded intervals for exact candidate signatures, determine which live checks actually failed from user evidence, and retain logging/console limitations. Do not rescan unrelated history without a new discriminator. |

Use `GIT_NO_LAZY_FETCH=1` for other owners' reads. Implementer0 is the single
lead-authorized owner of object-only retrieval; missing blobs are dependencies
to report, not permission to fetch refs. Keep external upstream references
limited to primary patch/code discussions and exact fixes whose mechanisms
can be checked in the incident source.

End each upstream package with either a supported defect/fix chain or a bounded
negative result and the diagnostic evidence needed next. A host hang with no
stack, dump or reproducible trigger may remain unattributed after a correct
source audit; do not substitute a ranked list of guesses.

## Final evidence constraints and disposition

The user reported that the normal crash-kernel/upload recovery did not happen,
and confirmed that configured sysctls had no runtime changes. The traced
configuration therefore supplies incident policy: hardlockup panic is 0,
softlockup panic is 1, watchdog/NMI watchdog are enabled, and the threshold is
10 seconds. A detected hard lockup need not panic under this policy.
Positive `Kdump: loaded` markers at 18:31:57/59 prove a crash image was present
about 26.5 minutes before the last log. No upload does not identify whether
panic occurred, crash transfer completed, or capture/upload failed.

The VGA text cursor can blink in hardware without scheduler progress. Neither
that observation nor missing forwarded diagnostics supplies a failure stack.
The full custom inventory/package coverage and the targeted upstream lanes
found no supported incident cause. Three definite source defects are recorded
separately from attribution in [synthesis.md](synthesis.md). No source change,
generic test, policy change or further broad audit is proposed as verification
of an unidentified mechanism. A future incident's CPU/task trace or a concrete
source-specific trigger is the next discriminating evidence. This completes
the assigned source investigation; the session remains open.
