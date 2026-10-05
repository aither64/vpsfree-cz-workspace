# Architect result: settled global filesystem policy

[Final design](design.md) is implemented in the committed revision now under
final review. User confirmation that video
bridges are VPS resolves the boundary. SMS-only routing and interim job-restricted
or hybrid candidates are obsolete; no scope question remains.

Retained implementation scope (design inspected at `f725dd3f`, base `b66c929b`):

1. Add only `machine_type=~"vm|physical"` to the existing
   `FilesystemCritFreeSpace` numerator selector. Preserve denominator, ratio,
   mountpoints, <=10%, 5m hold, value, labels, annotations and name. No `unless`,
   job filter or missing-type fallback. Leave warning and node fatal-rootfs intact.
2. Add literal `machine_type = "vps"` to `jitsiMeet.jvbConfigs.labels`, preserving
   alias/type/project and both exporter ports for all eleven groups. This single
   explicit label is the smallest placement for the now-confirmed homogeneous
   bridge fleet. Keep data/meet.nix unchanged; no new schema/field/inference is
   needed. Existing authoritative host labels and metadata stay unchanged.
3. Restore alerter/default.nix exactly to base, keeping its original none route
   and blackhole receiver. Retain the complete pgnd CPU-only change.
4. Update filesystem/config/routing fixtures and monitoring.md to the final
   global policy. Import actual data/meet.nix into the existing monitor fixture
   and assert production-generated JVB labels/endpoints. Keep check interfaces.

Acceptance includes positive VM/physical and negative VPS/missing/empty/invalid
type cases across infra/nodes/mon/meet-jvbs, type-based behavior independent of
job name, threshold/hold/value/label correctness, warnings at 19% and 10% (not
20%), restored normal routing, and unchanged fatal/CPU behavior. All relevant
configured host jobs will be classified; missing types are intentionally
ineligible globally. Synthetic VM/physical JVB cases test the expression,
not actual fleet classification.

The lead reports final commits `f53354dec1596bf665c80f85c557a9b05755805a` then
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`. Their tree
`c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9` matches four passing focused/adjacent
checks. Reviewer0 now owns mandatory whole-branch review **in all lanes**;
both monitor/restored-alerter builds remain gated on it. Prior review/builds
do not verify this new boundary. Preserve the pinned environment and active hooks.

User explicitly authorized: "okay, verify it and when done, merge it into the
default branch. I will deploy it myself." The named integration target is
`vpsfree-cz-configuration/master`, after checks/review/builds. Deployment is
user-owned; session closure and cleanup are not authorized. A normal clean
patch-equivalent rebase retains this approval with the Git procedure's
equivalence proof, appropriate checks and final-head record.

The feature remains published at old f725dd3f until the final precise-lease
update. The lead confirmed local project master b6e650ad is an ancestor of fresh
origin/master b66, stale rather than divergent. Preserve it while integrating
from the fresh remote-default checkout; final push and fast-forward integration
are lead-owned. Keep feature refs and provenance records. No session deployment,
integration or consumer-pin update has occurred yet.

No alerter-first rollout is needed under the undeployed premise. The user's
monitor updates carry labels and rule together; mixed versions may still emit
old VPS criticals. Relabeling changes identities and pending windows, including
Meet. Rollback restores old monitor policy without state migration; an alerter
rollback alone cannot recreate suppressed Prometheus alerts.

This reconciliation changed only authorization/provenance statements in the two
architect documents. No policy redesign, application edit, check, build, Git
mutation, deployment or lifecycle action was performed by the architect.
Current committed-head/check evidence above is reported by the lead.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
Session remains open.
