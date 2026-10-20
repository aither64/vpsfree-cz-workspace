---
lifecycle: active
---

# Node24 kernel hang investigation

Current phase: source investigation and final synthesis complete; findings
handed off with cause unattributed. All owner source artifacts accepted. No cause established with the user's required confidence. Session
remains open. No application/configuration changes or deployment.

## Phase checklist

- [x] Verify exact bound session identity and retained team/write access.
- [x] Establish incident window, deployed kernel and old livepatch provenance.
- [x] Account for every custom Linux patch and extra packaged ZFS change.
- [x] Complete independent custom source analyses.
- [x] Complete authorized targeted upstream source analyses.
- [x] Finish reconciled synthesis and user handoff.
- [x] Validate evidence local links and whitespace (17 Markdown artifacts).

## Current conclusions

- Node24 stopped logging Oct20 at18:58:26.658330+02:00; recovery boot logs begin
  19:12:04.761663+02:00. Other nodes continued reporting. No forwarded kernel
  panic/lockup/RCU/blocked-task/hostOOM/storage/hardware error signature found.
- Exact incident OS2abbe3cc1c102a4b39022d3f73ef4a432ad4d616 selects Linux
  1dfea587406b7dd79973831d1677fb2418e5e9aa, later6.12.113 after proactive swap
  retirement. Earlier6.12.113 pin11058eb4 is different and was distinguished.
- Initial .113 carries all60 old custom patch bodies unchanged plus NLM guard.
  Incident .113 retains52, removes6 proactive/DAMON owners, consolidates2 memcg
  lifetime fixes into identical helper source, adds defensive NLM guard and
  ordinary swap reporting. All55 incident custom commits accounted.
- Extra .113 ZFS free-account patch removes a concrete prepatch lock-order edge;
  no replacement hang/race/lifetime chain found. Patch selected in both modes
  at exact incident OS:358cd303c is its ancestor despite equal timestamps.
- Targeted upstream memory/NFS/scheduler/RCU/locking/platform/printk intersections
  yielded no supported host-wide failure chain. This is not exhaustive review
  of all7278 stable commits/5291 changed paths or all drivers.
- Definite defects kept separate: preexisting syslog allocation-cleanup NULL
  dereference; new swap reporting unsigned underflows; upstream FREE_STATEID
  allocation-error reference leak pinning a mount. No incident trigger or
  host-hang chain established. Documented old-v6 effective FREE_STATEID error
  unwind differs; exact old loaded module/controlstate remains unknown.

## Missing crash upload: evidence and configuration

User confirms normal panic should crashboot/upload, none happened, and sysctls
had no runtime changes. Exact OS/config/Nixpkgs source trace gives configured
hardlockup_panic=0, softlockup_panic=1, watchdog1/NMIenabled, threshold10,
panic timeout0 and panic_on_warn/oops/RCU/hungtask0. Compile defaults are
source-inferred through unchanged Kconfig/recipe lineage, not recovered.config.
A detected hardlockup therefore need not invoke panic/kdump. This is compatible
with no upload, not proof a hardlockup occurred or evidence of a causing patch.

Kdump:loaded is positively logged18:31:57/59,26.5min before lastlog. Source marker
checks a nonnull crash image; crashentry/transfer/capture/NFSupload remain
unobserved. Configured SPLspl_panic_halt1 calls Linuxpanic, so deliberate SPL
assertion freezing with value0 is excluded. VGA hardware cursor can blink
without scheduler progress. Missing dump/cursor alone does not locate failure.

## Owners, results and evidence

| Owner | Completed result | Acceptance evidence |
| --- | --- | --- |
| architect0 | Design, scheduler/custom intersections, final synthesis | Exact source chains/gates; bounded negative |
| implementer0 | Full custom inventory, upstream/livepatch provenance, printk7 audit |60/61/55 accounting; exact bodies/blobs; panic ordering |
| implementer1 | Central logs, hardware/crash markers, ZFS patch audit | Exact bounded excerpts; ownership/lock cycle proof |
| implementer2 | Custom and upstream memory audits | Balanced refs; complete retirement; reporting defect/source gates |
| implementer3 | Custom syslog/NFS and upstream RPC audit | Defect proof; TLS wait actor exclusion; mount leak scope |
| implementer4 | Packaging, applicability, platform and watchdog policy | Exact selectors/ancestry; repo precedence and user attestation |
| lead | Scope, assignments, acceptance, tracking and portal | All final source artifacts read and registered |

Entry point: [synthesis.md](synthesis.md). Design: [design.md](design.md).

Custom evidence: [patch-inventory.md](patch-inventory.md),
[packaging-audit.md](packaging-audit.md),
[scheduler-analysis.md](scheduler-analysis.md),
[memory-audit.md](memory-audit.md),
[syslog-nfs-audit.md](syslog-nfs-audit.md),
[zfs-patch-audit.md](zfs-patch-audit.md).

Upstream evidence: [upstream-provenance.md](upstream-provenance.md),
[upstream-memory-audit.md](upstream-memory-audit.md),
[upstream-nfs-audit.md](upstream-nfs-audit.md),
[upstream-scheduler-audit.md](upstream-scheduler-audit.md),
[upstream-platform-audit.md](upstream-platform-audit.md),
[upstream-printk-audit.md](upstream-printk-audit.md).

Logs: [log-evidence.md](log-evidence.md) and its linked exact selected excerpts.

## Verification and limits

- Canonical bare repos read; no feature branch/worktree/source edits. Old boot
  a2384967b90f24d2470c9eb15f0e66d938df7e08; stable source bases
  296aabce459470a4c1b68ffd0c0c0920e563aaad to
  7fdb7c1824a1f9979d648d7ae28ac446bcee9c6e.
- Source checks include patch/body/blob identity, lock/ref/error-path traces,
  configuration predicates/ancestry and complete owner accounting. No dynamic
  test, kernel build, reproduction, configuration mutation or deployment run.
- Source-proven defects do not justify a blind host-hang reproducer without a
  demonstrated progress chain. No automatic review for findings/evidence alone.
- Central logs read as root@log.int.prg.vpsfree.cz. Direct node SSH blocked by
  absent trusted key; no trust bypass/change. Historical runtime mounts/NFS
  transport and final binary.config not recovered.
- Partial Linux clone missing blobs materialized only by implementer0, authorized
  exact object-only fetches67+11, no refs/FETCH_HEAD refresh. Early implicit
  retrieval was disclosed/stopped. No future stable history fetched; local later
  refs limit does not prove no later upstream fix exists.
- Initial plan/state/portal commit78f1ea18. Subsequent evidence is consolidated into one end-of-work daily checkpoint
  under normal tracking cadence; unrelated shared workspace changes preserved.

## Remaining evidence / next action

Assigned investigation is complete; no further source work planned without new
discriminating evidence. Attribution remains blocked by absent stalledCPU/task stack, NMI/IP/held-lock
trace or source-specific reproducible trigger. A future diagnostic decision can
consider hardlockup_panic1 and independent crash-progress capture; no such
configuration change or forced crash has been authorized/performed.

Stable session URL:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-20-kernel-check/
Session lifecycle stays active/open; no archive/delete/stop action authorized.
