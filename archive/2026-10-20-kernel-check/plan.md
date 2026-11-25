# Kernel hang investigation

Investigate whether custom vpsAdminOS kernel patches changed between Linux
6.12.95 and 6.12.113 can explain node24.prg becoming unresponsive while its
console cursor continued blinking at the login prompt. Upstream stable patch
regressions are deferred until the custom patch audit yields no supported cause;
the user subsequently authorized upstream investigation on that condition.

## Scope and approach

Read vpsadminos and linux canonical repositories for exact version provenance,
custom patch inventory and semantic comparison. Read production configuration
only if required to establish deployed versions. Examine node24 records on
log.int.prg.vpsfree.cz with bounded read-only queries. Preserve concise evidence
and exact revisions in this session, without exposing credentials or unrelated
container logs.

The architect owns design and causal synthesis; implementer0 owns patch
provenance/inventory; implementer1 owns central logs. Three added implementers
will own independent source-analysis packages identified by the architect.
Lead owns coordination, acceptance and session records. Findings require an
obvious concrete source failure chain with reachable conditions, or verification.
Keep code defects distinct from proof that they caused this incident.

## Compatibility and deployment

Investigation only: no application edits, kernel build, deployment, production
mutation, persistent format/API/schema change or coordinated node update.
Any later reproduction must use an isolated environment and an explicit brief.
No integration, lifecycle closure or cleanup is authorized by this investigation.

## Acceptance and verification

- Establish exact old/new custom patch revisions and distinguish context-only
  rebases from semantic changes.
- Establish incident/reboot window and kernel evidence from central logs.
- Audit changed custom paths for hangs, locking, lifetime and compatibility.
- Report supported conclusions, eliminated leads and remaining uncertainty with
  source references and log evidence; do not infer causality from symptoms alone.
- Evidence and findings remain session artifacts; no product documentation
  change is useful unless investigation leads to an implemented change.

## Scope and evidence decisions during investigation

- User added three retained implementers, used for independent source lanes.
- User authorized upstream Linux investigation if custom audit yielded no
  supported cause. Full custom delta accounted first; then targeted upstream
  memory, NFS/RPC, scheduler/RCU/locking, platform and printk intersections.
- User confirms normal panic should crashboot/upload and none occurred; user
  also confirms no runtime sysctl changes. Repo-configured policy therefore
  applies. Sources establish softlockup panic1 but hardlockup panic0; this
  explains a possible missing-dump path without proving hardlockup occurred.
- Kdump loaded is positively logged26.5min before lastlog. Hardware VGA cursor
  can blink independently of scheduler progress. Neither observation attributes
  the hang.
- Proven source bugs are documented separately from incident attribution; no
  candidate establishes a host-hang chain or justifies blind reproduction.
  No source/config changes, builds, tests, deployment or merge is planned.

## Follow-up scope: hard-lockup survival history

User asks whether hard-lockup detections have happened nonfatally in cluster
history, fearing panic1 could turn transient events into outages. Investigate
read-only central logs with explicit coverage and bounded resource use; separate
true progress stall/detector falsepositive, sameboot continued operations and
affectedCPU recovery. Source owner traces warning suppression/reset and panic
semantics. No policy/deployment change or fault injection. Evidence lives in
session artifacts and updates the user's policy decision, not incidentcause.

## User-requested complete node24 historical scan

Search every retained node24 log, including rotations/legacy/compressed files
and verified aliases, for hardlockup detections and survival. Earlier cluster
sampling budget does not limit this explicit node24 corpus. Inventory and
snapshot/cutoff must account for growing/rotating current logs; complete all
files despite hits, pause/resume errors explicitly. Independent local analysis
assesses service survival and affectedCPU progress separately. No policy change
authorized; possible node24-only pilot remains a later decision.

## User-requested all-node last-three-month search

Search every retained node-log file overlapping July 20, 2026, 00:00 CEST
through the fixed October 20 snapshot, including boundary files and current
prefixes. Inventory all identified sources and disclose retention gaps. One
sequential low-priority collector owns the full manifest, byte cutoffs,
pre/post file identities and every match; continue after hits. Independently
reconcile local coverage and classify any actual episodes. The earlier cluster
sample budget does not apply. No configuration change or forced fault is
authorized. Report timestamp-selection and forwarding limits explicitly.

Completed: 1,221 selected files, 557,248,915,782 bytes, through October 20,
23:08:52 CEST. Independent reconciliation passed with zero hard-lockup reports.
Thirteen sources supplied data; thirteen older directories lack retention in
this interval. See the [final report](cluster-hardlockup-three-months.md).

## October 21: all-node hard-lockup panic configuration

Set `kernel.hardlockup_panic = 1` in the shared compute-node configuration,
as explicitly requested by the user. Preserve other watchdog thresholds and
panic settings. Prepare a dedicated vpsfree-cz-configuration feature branch,
validate effective node coverage without a system/kernel build, commit with
repository hooks, publish, and run independent final review. Do not merge or
activate production configuration without separate direction. The architect
owns the detailed compatibility and rollback brief in design.md; implementer0
owns source/Git/checks, implementer2 independently verifies node scope, and the
lead coordinates reviewer0 and the final handoff.

## Superseding policy owner: vpsAdminOS crashdump module

The user corrected the location and requested the same handling as existing
softlockup_panic. Move hard panic to the OS crashdump module under the existing
enablement condition and kernel-command-line mechanism. Use the recognized
`nmi_watchdog=panic` argument beside `softlockup_panic=1`. Withdraw the obsolete
unmerged configuration sysctl and consolidate its history. Evaluate enabled and
disabled module behavior, run declared hooks, publish the OS branch and obtain
final independent review. Keep pins and production runtime unchanged; consumers
will adopt through normal separately authorized update/rollout.

Final source result: OS branch `2026-10-20-kernel-check` at
`b81c43ff6865a033268072f55cd94ad763d0630b`, reviewed and quick-checked;
site configuration branch has zero diff at37a338b2. Automatic exact-head
CI39600028637 remains under the existing implementer/watcher ownership.
No downstream pin update, merge or runtime rollout is part of this handoff.

## October 22: runtime application follow-up

Keep the crashdump-gated boot panic argument, explain its hard-lockup purpose
with an adjacent comment, and add the requested runtime sysctl policy in the OS
module. Trace existing live sysctl application before promising automatic live
updates; choose the smallest supported path and keep deployment/runtime writes
separate. Check enabled/disabled/generated output and normal overrides, fold
unmerged iterations appropriately, publish and independently review the final
committed result. Previous broad-CI results are prior-head evidence, not new
head proof; do not repeat unrelated diagnostics or induce a lockup/crash.

## User-directed declaration-only simplification

Remove the custom hard-panic activation hook; declare hardlockup_panic and
softlockup_panic as ordinary sysctls under crashdump enable. Retain boot policy
and explanatory NMI comment. Preserve normal overrides, confirm disabled policy
omission and generated values/no hook, publish and independently review. The
user selected this narrower mechanism; NixOS's systemd-sysctl handles live
switching, while current runit OS lacks that automatic path. Do not silently
reintroduce activation/service machinery or claim automatic live application.

## Approved implementation: generic runit sysctl service

The user accepted the normal-service plan and requested implementation. Add a
generic logged one-shot sysctl service in default/rescue using existing runit
interfaces. Preserve early boot application exactly, accepting a later second
boot application. Restart on changed enabled declarative sysctl file targets
and sources, including generated60-nixos.conf; unchanged switches do not replay
the settings. Use ordinary procps --system precedence and one application
attempt, not automatic retries. Clear old completion before each attempt,
establish once mode before applying, exit explicitly on failure and atomically
publish current managed-input identity only on success. The custom check must
reject stale identities; supervisor and switch exit alone do not prove apply.
Document explicit retry and verify actual benign sysctl values in a disposable
VM. Removed/null settings do not reset live values; mixed versions require no
coordinated fleet upgrade or persisted-state migration.

Architect0 records the contract and boundaries before implementation. I2 owns
the module, registration, quick checks and all serialized OS Git operations;
i0 owns focused integration tests and operator documentation. Keep one generic
logical owner after the accepted paired panic declaration commit. After all
source/tests/docs are committed and quick checks pass, reviewer0 independently
reviews complete history and all four lanes before a fresh retained Luna/low
utility runs the focused VM test. Existing CI remains separately owned; no
duplicate observer/workflow. No merge, downstream pin update, deployment,
production runtime write or session lifecycle action is authorized.

## Conditional integration approval

The user subsequently directed periodic CI checks, about every ten minutes,
and merging when CI is done. Continue the existing sole watcher at that cadence
and integrate vpsadminos into staging after successful exact-head CI and the
final freshness/history check. Prepare outside repository ownership; hold one
short claim only for final checks, ordinary ff-only merge/hooks, non-force SSH
push and remote proof. Retain branches and release the claim before records/CI.
No deployment, downstream pins, configuration merge or session lifecycle action.

The user later explicitly waived the observed product-suite six failures and
AMD-scale-aged-v6 hotplug warning as blockers for this feature merge. Preserve
red CI evidence and finish the ordinary freshness/ff-only merge requirements;
do not represent this exception as a green pipeline. Investigate failure root
causes, recurrence and test purpose/usefulness in the separately requested new
Full-team session with four implementers, proposing solutions rather than
silently changing the tests here.
