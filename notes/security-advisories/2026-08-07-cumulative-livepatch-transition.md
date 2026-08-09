# Evaluate cumulative live patches as stateful intervals

Initiative: `work/2026-08-07-security-advisories-6-12-95-2`

## Symptom

A current-node check alone cannot establish when a CVE first became mitigated.
Conversely, treating every kernel-history observation as an effective state
transition made an internal v3 inventory update look like loss of mitigation
and incorrectly reset `mitigated_since` to the v4 deployment date.

## Cause

Live-patch security content and activation safety are different facts. Patch 3
contained the selected security fixes and mitigated the staging interval where
it was loaded, enabled, and out of transition. Its Safe-RET adaptation was
unsafe to activate on AMD and crashed node5.brq. A reboot or removal ends the
active-patch state; neither a previous sample nor a configured successor proves
that the patch remained active.

The repaired vpsAdmin kernel-history evidence records effective boot, reported
release, and live-patch transitions alongside internal inventory, runtime, and
deployment observations. Retain every snapshot because an internal inventory
event can record `transition: true`. When an internal report omits unchanged
live-patch metadata or temporarily lists only an inactive configured successor,
carry forward the previous effective live-patch state. An accepted cumulative
successor carries earlier fixes forward without starting a new mitigation
interval.

## Workflow

Accept a cumulative patch only with its exact module ID, patch version, boot
kernel, and trusted clean vpsAdminOS identity. Require it to be loaded, enabled,
and non-transitioning. Treat an observed active patch as mitigation for that
interval even if the same release failed to activate elsewhere. Treat reboot,
effective removal, disabled state, or transition as a new non-mitigated
interval until another accepted patch becomes active. Missing identity in a
standalone or changed runtime state remains unresolved; missing unchanged
metadata in an internal observation inherits the preceding effective identity.
Continue to evaluate sysctl, eBPF, module, and deployment changes from their
retained internal snapshots.

Inspect the transition timeline, not only the final `vulnerable_until` value:
that field describes the last affected-to-mitigated transition when multiple
affected intervals exist. Keep activation crashes in internal availability and
deployment analysis. Public responses should name only the patch version that
first fixed the CVE. Keep the currently deployed cumulative replacement in
internal evidence and analysis; naming it in durable public text becomes stale
as soon as the next cumulative patch is deployed.

Keep slow historical reads outside the narrowly guarded current-component
snapshot window. Runtime attestations such as an eBPF program's `verified_at`
can legitimately refresh on every report and change the current snapshot digest
without changing the security conclusion. Collect events and reconstruction
history first, then bracket only the current component reads with the current
snapshot revision; continue to recheck event and history coverage separately.
