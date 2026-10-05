# Infra monitoring: revised implementation plan

## Current user correction

The user now requests that the critical filesystem alert itself stop firing
for VPS targets, and remain only for VM or physical targets. Remove the added
Alertmanager blackhole exception. Keep the typed machine metadata and labels,
existing filesystem thresholds/holds, warning alerts, and pgnd CPU-only policy.

Scope is now settled globally after source/compiled-job investigation. Relevant
filesystem jobs are infra (mixed types), nodes (physical), mon (two VPS monitors)
and meet-jvbs (eleven video bridges previously without a type). User confirmed:
"the video bridges are VPS, you can add the label to them". Add their VPS label,
then apply positive machine_type=~"vm|physical" eligibility to the common critical
filesystem numerator across all jobs. Missing/invalid types do not emit the
critical alert. Leave warning and separate node-fatal rules unchanged. No job-
based exception or fallback is needed. See filesystem-job-inventory.md.

Only vpsfree-cz-configuration is affected; reuse this session/worktree/branch.
The previous feature head f725dd3f was pushed but no session integration,
deployment or consumer-pin update occurred. Inspect fetched upstream/feature
provenance before rewriting unmerged history. If the branch remains unmerged,
replace its first behavior commit with the final metadata/critical-alert policy
and replay the unchanged CPU commit; retain a clean two-commit series and push
with a precise lease. Do not rewrite merged history or change master.

## Ownership and gates

Architect0 owns the revised design/verification brief; implementer0 owns code,
fixtures/docs and active-hook commits; reviewer0 owns independent complete-branch
review. Lead owns coordination, acceptance and known-quick verification;
fresh catalog-policy watchers own uncertain Nix operations and full builds.

Test critical-alert absence for VPS and applicability for VM/physical, warning
visibility, five-minute hold/threshold labels, missing/invalid machine types
and all four relevant jobs according to the settled global boundary. Assert the added terminal
route is absent and normal receiver paths restored. Preserve machine-label
constructor tests and all CPU behavior. Run focused checks, declared hooks,
then mandatory whole-branch review before full configurations. Reconcile docs
and rollout ordering because the final policy no longer needs an SMS exception.

The later user instruction explicitly authorizes integration of the verified
revision into vpsfree-cz-configuration/master. Deployment remains user-owned;
no lifecycle action or cleanup is authorized.
Session remains active/open. The architect must record mixed versions,
identity/pending changes, rollback and existing-state compatibility; no schema
or persisted-format change is expected.

## Prior accepted implementation

The earlier SMS-only approach and its successful review/build evidence are
historical and superseded by this correction. Metadata/labels and pgnd CPU
policy remain accepted. See tracking checkpoint d863cc64 and the previous
verification/review records for exact prior commits and evidence; they do not
verify the upcoming revised rule.

## Verified outcome

The settled revision passed all checks, independent all-lane review and four
central builds, then fast-forward merged and pushed to master at 657cc0a8.
See revised-verification.md and integration.md. The user owns deployment;
session remains open with no lifecycle/cleanup action.
