# Infra monitoring: accepted implementation plan

## Goal and scope

Implement the user-approved machine-type label and infra VPS critical filesystem
SMS exception in vpsfree-cz-configuration. Apply the existing staging CPU usage
policy to playground. Leave all filesystem thresholds, ZFS thresholds, raw
load-average alerts, I/O-wait alerts, and CPU calculations unchanged.

User decisions: "keep the rules as they are, except making the exception for
VPS"; introduce a reusable machine-type label; label the main host exporter jobs;
classify build as a VM; "keep pgnd loadavg alerts as they are. relax just cpu
usage alerts." The user subsequently requested "Implement the plan."
Implementation does not authorize master integration. Prepare and verify the
feature branch; central deployment is a distinct operational step.

## Affected repository and approach

- Repository: vpsfree-cz-configuration.
- Branch: 2026-10-03-infra-monitoring.
- Worktree: worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration.
- Initial base: b66c929bb7c202ad31bd8994a691ade14c40ebf0.
- Architect owns design.md and verification brief; implementer owns application
  edits and quick checks; independent reviewer owns final committed-branch review.
  Lead owns coordination and acceptance of their reports.

## Accepted behavior

1. Typed cluster metadata machineType has values vps, vm and physical. Infer vps
   for managed containers and default other machines to physical. Explicitly mark
   aitherdev, em1 and build as vm. Generate authoritative machine_type labels on
   infra, nodes and monitorings exporter targets, including local monitoring
   targets and related node exporters sharing the label helper. Preserve type=node.
2. After email/Telegram and before both SMS routes, add a terminal route matching
   job=infra, machine_type=vps, alertclass=fsavail and severity=critical. Keep
   severity, email, Telegram, inhibition and hourly repeats. This covers the
   existing rule's filesystems, including /run; it does not change the disk rule.
3. Extend only the two staging CPU usage rules to location=~"stg|pgnd" and exclude
   those locations from strict counterparts. Retain real location through relaxed
   CPU aggregation instead of hardcoding stg. Keep existing alert names, boot
   suppression and calculations. Warning stays >80% for 50m and critical >90%
   for 50m on stg/pgnd; production retains its existing 10m holds.

## Compatibility, deployment and recovery

No schema migration, client/API/daemon contract, persisted format or vpsAdminOS
update is needed. The new target label changes series/alert identity and may
restart pending alerts. Missing labels retain old SMS behavior during rollout.
Deploy both Alertmanagers before both monitors if deployment is requested;
rollback either configuration restores the previous notification policy.
No coordinated fleet update is needed. /run is normally tmpfs, so auto-expansion
is not its recovery mechanism; the requested SMS exception still covers it.
Do not merge or push feature content to master without explicit integration
approval for this repository/target. Leave the session open.

## Documentation and verification

Future operators and reviewers need a concise owning-project description of the
machine type and routing policy, with rollout evidence retained in this session.
Architect records concrete interfaces, invariants, checks and implementation
boundaries in design.md before application edits.

Quick checks must cover representative generated labels, exact SMS routing,
retained email/Telegram, unrelated alerts, CPU hold-time boundaries and pgnd
location. Prove filesystem and raw load-average rules unchanged. Run declared
hooks in the pinned Nix environment, commit changes, then mandatory independent
review of the complete series and final diff, explicitly recording no migrations.
Only after review, run configuration builds for both monitors and both alerters
under a fresh catalog-policy verification watcher. Do not deploy while merely
verifying the implementation.

## Historical investigation

Initial findings and broader threshold suggestions were recorded in coordination
commit 4123553c. Those threshold changes were declined and are superseded by the
accepted scope above. Initial inspection used origin/master 2a3e6a977db4464b585e413839953f08f57521f7;
worktree creation fetched the newer base stated above.
