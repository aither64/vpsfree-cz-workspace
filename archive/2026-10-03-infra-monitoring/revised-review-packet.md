# Revised complete-branch review packet

Status: final committed packet, ready for independent all-lane review.
The exact committed tree equals the passing snapshot and checkout is clean.

## Outcome and acceptance

The user replaced SMS-only suppression with removal of the critical filesystem
alert for VPS, requesting eligibility only for vm or physical. Investigation
found four relevant filesystem-exporting jobs: infra, nodes, mon and meet-jvbs.
User confirmed all configured video bridges are VPS and authorized their label.
The final rule has global positive machine_type=~"vm|physical" on only its
numerator. VPS/missing/empty/invalid/lookalike types cannot emit this critical
alert; VM/physical eligibility is independent of job. Warning (<20%, five
minutes) and separate node-fatal rootfs (<=5%, five minutes) remain unchanged.
Critical threshold remains <=10%, five minutes, with original percentage and
labels/mounts. Alertmanager source returns exactly to base; independently
supplied critical alerts route normally. No job restriction/unless/fallback.

Keep the accepted typed metadata/defaults/VM overrides and four authoritative
host-label constructors. Add literal vps to the existing homogeneous JVB target
labels, preserving data/meet.nix and both ports, alias/type/project. Keep exactly
the four accepted pgnd CPU rule edits; CPU source/fixture patch is unchanged.
Raw load-average, I/O wait, storage CPU and ZFS policy remain unchanged.

The user now expressly authorizes integration into vpsfree-cz-configuration's
default branch master after verification and will deploy personally. No agent
deployment/live message, pin update, default rewrite or session lifecycle action.

## Repository, history and provenance

Session 2026-10-03-infra-monitoring, workspace /home/aither/workspace/ai/vpsfree.cz.
Worktree: worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration.
Branch: 2026-10-03-infra-monitoring.
Base: b66c929bb7c202ad31bd8994a691ade14c40ebf0.
Head: 657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da.
Checked/final expected tree: c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9.
Read plan.md, state.md, design.md, architect-result.md,
filesystem-job-inventory.md, revision-provenance.md, implementation-result.md,
revised-branch-inventory.md and revised-final.diff.

Complete exact series:

```
f53354dec1596bf665c80f85c557a9b05755805a monitoring: restrict critical filesystem alerts by type
657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da monitoring: apply staging cpu alert policy to playground
```

Commit split rationale: first metadata, authoritative labels and their
immediate global critical-rule consumer, with related checks/docs; second the
independently reviewable CPU policy with related fixtures/docs. The obsolete
SMS route approach and correction/fixup history are consolidated before review.
No migrations, schemas/seeds/persisted formats or transitional migration
versions. Lead checked fetched origin/master at base and origin feature at old
f725dd3f, which was unmerged. Only local/origin feature refs contained it; no
PR in any state or branch CI runs. No session release/deploy/integration/pin.
This is known session/repository provenance, not a live deployment audit or
proof against unknown external consumption. Assess history/migration conclusions
independently across the whole base-to-head series, not only latest delta.

## Interfaces and actual consumers

The owning site provider is modules/cluster/default.nix, exposing typed
cluster.<name>.machineType enum vps/vm/physical. Containers default vps, other
machines physical; aitherdev/em1/build explicitly vm. Pinned confctl 7bee58a
preserves metadata into machines.metaConfig and confMachine. The production
monitor module consumes it at local/peer mon, infra and shared node label
constructors; authoritative machine_type follows custom labels. Node ZFS/IPMI
shares labels and keeps type=node. JVB address-only inventory has no cluster
lookup, so the user-confirmed homogeneous fleet gets one literal vps label in
its existing constructor. No data schema or runtime inference was introduced.
The common critical rule is the policy consumer; no provider/pin update occurs.
Both monitor fixtures import real Meet data and actual production constructors.

## Verification and docs

Known-warm root checks on the exact staged tree passed:

- infra-monitoring-config + infra-monitoring-rules: exit 0, 6.760 seconds.
- vps-autostart-prometheus-rules + process-count-prometheus-rules: exit 0, 2.929 seconds.

Evidence revised-quick-checks-2-result.json/log; active static checks are in
revised-static-checks.log and revised-fixture-static-checks.log. Initial revision
focused run failed only two warning assertion selectors unintentionally matching
the separate missing-job VM case; exactly those selectors were narrowed, then
the actual focused derivation passed. Production did not change for that fix.
The config/routing fixture uses actual modules with inert transports and covers
metadata/type precedence/real JVB endpoints/normal receivers. Filesystem fixtures
exercise global positive and negative type/job cases, thresholds/holds, original
labels and percentage values, matching devices/types and warning visibility.
R1's selected root warning equality 20% and positive 19% cases are retained.
CPU fixtures retain strict/relaxed threshold/time/boot/location/average coverage.

Owning-project docs/services/monitoring.md is linked from mkdocs Services and
records classification, global rule eligibility, warning/fatal preservation,
CPU policy and lasting identity/mixed-version/rollback constraints. Individual
prepared rollout details remain in session design. No deployment occurred.
Offline amtool verifies selection, not delivery, activation/repeat timers or
inhibition execution. Full builds are gated on this review.

## Risk, reviewer and lanes

Overall High risk: live monitoring policy and new label identities affect
mixed-version operation, HA deduplication, pending/rate windows and rollback.
No persisted format or protocol migration; no coordinated exporter/node/VM/JVB
update required. Both monitors later receive rule/labels together. Old monitors
can still emit VPS criticals while mixed versions; missing-type exclusion is
intentional. Existing alerts can resolve normally. /run selection remains and
tmpfs is not dataset-expanded. No alerter-first policy is needed.

Retain independent reviewer0, index 0, purpose review, thread
01a1021a-42ed-7e62-9bc2-43fbd84c6a48, saved gpt-6.1-sol/xhigh, read_only.
No override/fallback. This is a related substantive policy revision, so prior
SMS-only review and narrow R1 closure do not cover it. Review all four lanes:
general, architecture/repetition, scope/proportionality, risk/compatibility.
Read mandatory-change-review/SKILL.md and every selected reference in full;
read applicable workspace/repository procedures and reconcile documentation
placement under dev-session-documentation. Perform directly without agents.

Deliver complete read-only report to lead: findings by severity with path/line/
commit, per-lane conclusions, explicit whole-branch obsolete-history conclusion,
explicit no-migrations lineage conclusion and residual verification/deployment
limits. Do not edit, run builds/hooks, commit/push, integrate/deploy or change
lifecycle. Lead records report and decisions. Session remains open.
