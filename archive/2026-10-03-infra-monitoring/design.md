# Infra monitoring: final design and verification brief

Status: **scope settled; committed revision under final review**. User confirmed: "the video
bridges are VPS, you can add the label to them". Apply global positive
VM/physical eligibility to the common critical filesystem alert and label the
Meet exporters as VPS. The SMS-only approach and interim job-restricted/hybrid
candidates are superseded; do not implement their routes, `unless` clauses,
job filters or missing-type fallbacks.

Design inspection used `f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`.
Base: `b66c929bb7c202ad31bd8994a691ade14c40ebf0`. The lead reports final commits
`f53354dec1596bf665c80f85c557a9b05755805a` then
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`, with tree
`c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9` matching all four passing focused and
adjacent checks. Reviewer0 owns the revised all-lane final review; full builds
remain gated on that review. The published feature still points to f725dd3f.
No session deployment, integration or consumer-pin update has occurred. Earlier
[verification](verification.md) concerns the superseded policy; current evidence
and authorization are in [state.md](state.md). Current intent is in
[plan.md](plan.md), with job provenance in
[filesystem-job-inventory.md](filesystem-job-inventory.md).

## Scope, ownership and retained behavior

Only `vpsfree-cz-configuration` changes in the retained session worktree/branch.
Architect edits are limited to this document and [architect-result.md](architect-result.md).
Implementer0 owns source, fixtures, project docs and active-hook commits; lead
owns coordination, provenance, final verification/review, push and integration.
Uncertain Nix operations and full builds use the authorized fresh watcher path.
The user explicitly directed: "okay, verify it and when done, merge it into the
default branch. I will deploy it myself." This authorizes integration of
`vpsfree-cz-configuration` into `master` after the verification gates. Deployment
remains user-owned. No input update, lifecycle action or cleanup is authorized;
keep the session open.

Keep `machineType` enum `vps`, `vm`, `physical`; managed containers default to
`vps`, other machines to `physical`; aitherdev/em1/build explicitly `vm`. Keep
the four existing authoritative host label constructors and their precedence
over `monitoring.labels.machine_type`: local and remote monitoring, infra and
shared node labels. Actual monitoring job is `mon`. Preserve related node
ZFS/IPMI exporters, `type="node"`, all existing labels and target selection.

Keep the four accepted CPU usage rule edits: strict rules exclude `stg|pgnd`,
relaxed rules include both and retain their actual location through aggregation.
Warning stays >80%, vpsAdminOS critical >90%; relaxed holds 50m, strict holds
10m, with the original calculation/boot guard. Retain names including `Staging`.
All raw load-average, I/O-wait, storage CPU and ZFS rules remain unchanged.

## Relevant jobs and final classification

Counts are from the lead's complete previously built mon1 Prometheus YAML;
source inspection corroborates the constructors. This is configuration evidence,
not live metric/scrape-health evidence.

| Job | Node-exporter target groups | Final classification |
| --- | --- | --- |
| `infra` | 50 | 44 VPS, 3 VM, 3 physical |
| `nodes` | 13 | physical |
| `mon` | 2 | VPS: mon1 and mon2 |
| `meet-jvbs` | 11 | VPS, confirmed by the user; add the label |

Monitor metadata explicitly declares container IDs 14005 and 19501.
`data/meet.nix` declares eleven name-to-address bridges, with exporter ports
9100 and 9700 for each. The standalone JVB constructor reads that data without
cluster metadata; its existing labels are alias, `type="meet-jvb"` and project.
Commit `0e8aeac7e09111ce5cb5a46d8961ba2bd94d255a` introduced the paired node and
Jitsi exporters. The authoritative user confirmation supplies their type;
addresses, DNS and service-role labels were not used to infer it.

Add literal `machine_type = "vps"` to the existing
`scrapeConfigs.jitsiMeet.jvbConfigs` label block in
`modules/clusterconf/monitor/default.nix`. It applies to every configured group
and both ports. Preserve alias/type/project and target addresses/ports exactly.
A nearby comment may state that all configured video bridges run as VPSes.

This is the smallest clear placement for the confirmed homogeneous fleet: one
label in its existing target constructor. Leave `data/meet.nix` unchanged; no
per-bridge data conversion, new enum/schema, runtime inference, fallback or
additional project-level type field is needed. Do not extend ping/web/probe
labels. Project docs should make this explicit classification discoverable so
future changes to the bridge inventory reconsider it if the fleet changes.

## Critical filesystem expression and exact semantics

Change **only** the numerator selector of `FilesystemCritFreeSpace` in
`modules/clusterconf/monitor/rules/common.nix`:

```promql
(node_filesystem_avail_bytes{mountpoint=~"^(/)|(/run)|(/nix/store)",machine_type=~"vm|physical"}
 / node_filesystem_size_bytes) * 100 <= 10
```

Keep the existing percentage calculation, denominator, mountpoint selector,
threshold `<=10`, `for = "5m"`, alert name, annotations, `severity="critical"`,
`alertclass="fsavail"` and `frequency="hourly"`. Do not introduce a job matcher,
`unless`, `or`, recording rule, join modifier or `bool` comparison.

The positive regex is anchored: only exact `vm` and `physical` match. VPS,
absent/empty, unknown and lookalike types such as `vmx` cannot produce this
critical alert on any job. The selector filters series without removing labels.
Default arithmetic matching still requires the denominator's same non-name
labels, including instance, job, mountpoint, device/fstype and machine type;
there is no need to repeat the selector on the denominator or add `on`/grouping.
The result retains the original percentage value and labels. See Prometheus
[label matching](https://prometheus.io/docs/prometheus/latest/querying/basics/)
and [vector arithmetic](https://prometheus.io/docs/prometheus/latest/querying/operators/).

| Input, assuming selected mount and matching size metric | Critical behavior after five minutes at <=10% free |
| --- | --- |
| `vm` or `physical`, on any job | eligible |
| `vps`, on any job, including infra/mon/Meet | absent |
| Missing, empty, invalid or `vmx` type, on any job | absent |
| Missing/unrecognized job with `vm` or `physical` | eligible; eligibility is type-based |

Keep `FilesystemLowFreeSpace` byte-for-byte unchanged: warning below 20%, five
minutes, hourly frequency, same mountpoint selector and labels. On excluded VPS
criticals, this warning can remain visible because the removed critical cannot
inhibit it; other existing inhibition still applies. Keep the separate
`NodeFatalRootfsFreeSpace` entirely unchanged (fatal at <=5% on node rootfs,
five-minute hold). This task changes one critical rule, not every `fsavail` rule.

Suppressed criticals generate no new critical email/Telegram/SMS notifications.
Existing active critical alerts may resolve during rollout, with normal resolved
notifications. The `/run` selection stays as it is; this policy does not imply
that tmpfs expands with a VPS disk.

## Exact implementation delta from f725dd3f

All paths below are relative to the configuration worktree.

| Path | Required change |
| --- | --- |
| `modules/clusterconf/monitor/rules/common.nix` | Add positive machine-type matcher only to `FilesystemCritFreeSpace` numerator. |
| `modules/clusterconf/monitor/default.nix` | Add `machine_type = "vps"` to JVB exporter group labels only; retain earlier host-label edits. |
| `modules/clusterconf/alerter/default.nix` | Restore exactly to base b66c929b, removing this branch's added terminal exception. |
| `tests/prometheus/infra-monitoring-filesystem.yml` | Replace VPS-critical expectations with the global type matrix, threshold/hold and warning checks. |
| `tests/prometheus/infra-monitoring-config.nix` | Retain machine/label assertions; import real Meet data and check JVB labels/ports; remove exception assertion/binding; expect original five routes with SMS at indexes 2/3 and none at 4. |
| `tests/prometheus/infra-monitoring-routing.sh` | Remove `without_sms`; synthetic critical cases now use normal mail/Telegram/both-SMS routing. Preserve warning/none checks. |
| `docs/services/monitoring.md` | Explain global critical eligibility, confirmed JVB VPS label, missing-type behavior, warning/fatal preservation and revised rollout/rollback. Remove SMS-only/alerter-first descriptions. |

Restoring the alerter preserves original receivers, email/Telegram/SMS routes,
repeat/daytime settings, inhibition and the existing severity-none blackhole
route. Do not remove that original route or its empty receiver. There is no
filesystem-specific notification exception after this revision.

Keep the existing flake/check interfaces, pins, metadata/VM modules, CPU source
and fixtures, mkdocs link, Meet data and Meet-specific alert rules unchanged.
No new test framework or source-module extraction is needed. The synthetic VPS
critical in routing tests is intentional: although Prometheus no longer emits
it, Alertmanager must route an independently supplied critical normally.

## Focused acceptance and fixture plan

Use current production imports: `infra-monitoring-config.nix` already renders
real common rules and alerter routes with inert receivers, then invokes promtool
and amtool; `infra-monitoring-rules` covers CPU. Existing prior successes establish
tooling feasibility but do not prove this new policy.

1. For each of `infra`, `nodes`, `mon`, `meet-jvbs`, test synthetic VM and physical
   metrics as eligible, and VPS/missing/empty/invalid types as ineligible.
   Synthetic VM/physical cases verify expression independence from job names;
   they do not reclassify the actual monitors or bridges. Test `vmx` anchoring
   and a missing-job eligible case. Excluded series must never be pending or
   firing, including after five minutes.
2. Eligible VM/physical examples must be pending before five minutes and firing
   at five minutes at exactly 10% free; just above 10% must not fire, and below
   10% must fire. Check selected `/`, `/run`, `/nix/store`, and an excluded mount.
   Use realistic device/fstype labels on both metrics and assert the original
   percentage value and alert labels, including severity/class/hourly frequency.
   Include multiple filesystems/types on one instance to catch weakened matching.
3. Preserve warning equality test at 20% and positive test at 19% on selected `/`
   (the prior R1 correction). Verify VPS warning at 10% remains eligible across
   all four jobs, plus missing-type warning visibility and the five-minute hold.
   Keep the warning rule unchanged rather than copying it into a new policy.
4. Keep metadata enum/default/explicit-VM tests and all existing authoritative
   label conflicts/constructor tests for both monitors and node-related exporters.
   Change the monitor fixture's empty Meet data to
   `confData.meet = import ../../data/meet.nix;`. Select actual `meet-jvbs`
   generated by the production module. Check all configured groups have type
   `vps`, exact alias/type/project labels, and the existing 9100/9700 endpoints;
   fully compare a representative group and ensure counts/coverage follow real
   data. Do not manufacture a separate JVB renderer or query live targets.
5. Amtool must select `team-mail,team-telegram,sms-aither,sms-snajpa` for synthetic
   critical/fatal cases, including VPS/missing types/Meet; warning stays
   `team-mail`, none stays `blackhole`. Assert original five-route structure,
   hourly/daytime settings and no added exception. These checks do not test
   live delivery, activation times, repeat timers or inhibition execution.
6. Keep CPU fixtures/behavior unchanged: strict versus relaxed selection,
   actual pgnd location, >80/>90 thresholds, 10m/50m holds, boot guard and average.
   Compare node rules to the base: only the existing four CPU edits may differ;
   `NodeFatalRootfsFreeSpace`, raw load-average and I/O wait remain identical.
   Compare common rules: only the one critical selector may differ. No migrations.

## Commands and verification gates

Use the realized pinned Nix development environment and active declared
Overcommit hooks. The lead/watcher owns functional checks because member shells
cannot reach the Nix daemon; use the established authorized path without changing
access. Prior cached focused runs took 5–8 seconds. Delegate uncertain Nix
operations and all full builds to a fresh policy watcher.

```sh
# Implementer static checks, with declared hooks also active on final commits.
git diff --check
bash -n tests/prometheus/infra-monitoring-routing.sh
bundle exec overcommit --run

# Focused and adjacent regression checks on the revised tree.
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.infra-monitoring-config \
  .#checks.x86_64-linux.infra-monitoring-rules
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.vps-autostart-prometheus-rules \
  .#checks.x86_64-linux.process-count-prometheus-rules

# Must be empty in the final diff.
git diff b66c929bb7c202ad31bd8994a691ade14c40ebf0 -- \
  modules/clusterconf/alerter/default.nix \
  modules/clusterconf/monitor/rules/infra.nix \
  modules/clusterconf/monitor/rules/meet.nix data/meet.nix flake.lock

# Inspect: one common critical selector, four retained CPU rules, and labels only.
git diff b66c929bb7c202ad31bd8994a691ade14c40ebf0 -- \
  modules/clusterconf/monitor/rules/common.nix \
  modules/clusterconf/monitor/rules/nodes.nix \
  modules/clusterconf/monitor/default.nix
```

After final intended changes are committed and quick checks pass, run mandatory
independent whole-branch review **with all lanes**. This new global behavior
boundary requires a full revised review; the prior review and narrow R1 handling
do not cover it. Supply cleaned complete series, final diff and no-migrations
conclusion. Only after that gate run full central builds through a fresh watcher:

```sh
nix develop --no-write-lock-file --command confctl ls 'cz.vpsfree/containers/prg/int.mon[12]'
nix develop --no-write-lock-file --command confctl ls 'cz.vpsfree/containers/prg/int.alerts[12]'
nix develop --no-write-lock-file --command confctl build --yes 'cz.vpsfree/containers/prg/int.mon[12]'
nix develop --no-write-lock-file --command confctl build --yes 'cz.vpsfree/containers/prg/int.alerts[12]'
```

These selectors/build commands worked on the prior head. Confirm exactly both
replicas in each selection and record final head/tree, command/exit and build
generations. Alerter restoration is checked by both builds, not deployed.
Stop unexpected local kernel compilation and investigate under the verification
procedure. Do not run deployment or dry-activate as a verification substitute.

## Compatibility, rollout and rollback

No database schema/migration/seed, persisted format, API/client/CLI/Terraform,
exporter protocol or daemon changes. No coordinated vpsAdminOS/node/VM/JVB
update is needed. Nix defaults preserve existing metadata callers. Prometheus
TSDB and Alertmanager state remain readable on rollback.

For the user-owned rollout, update both monitors with the final
labels and rule together. No alerter-first step or SMS exception is needed:
final alerter contents equal base and this session never deployed the superseded
route. If new evidence contradicts that deployment premise, refer it to the
lead before changing the rollout plan.

Adding host/JVB labels changes series and unaggregated-alert identities and can
reset pending alerts/rate windows. During mixed monitor versions, the old one
can still emit VPS criticals, including previously unlabeled Meet alerts. The
new rule intentionally excludes all missing types. Finish both monitor updates
before judging the policy; label-set changes can also prevent HA deduplication.
Existing criticals may resolve and produce normal resolution notifications.
No TSDB deletion or state reset is required.

After that rollout, the operator should verify effective labels/rules/reload health on both
replicas: JVB targets are VPS, VPS criticals are absent across relevant jobs,
VM/physical remain eligible, and warnings remain visible subject to existing
inhibition. Do not send live test notifications without separate authorization.

Rolling back to the previous deployed monitor generation restores its old
filesystem eligibility, host/JVB label shape and pgnd CPU policy. Reverting only
the critical selector restores its previous eligibility while keeping labels
and CPU changes. Restoring Alertmanager alone cannot recreate alerts that
Prometheus no longer emits. Expect identity/pending transitions again, not a
state migration. Preserve old generations under normal deployment procedures.

## Branch history, provenance and handoff

The old published series is `e7b02916` (metadata/labels/SMS) then `f725dd3f`
(pgnd CPU). Its SMS approach is obsolete. The lead reports the final local
two-commit series as `f53354dec1596bf665c80f85c557a9b05755805a` (metadata/labels/
global critical policy) then `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da` (CPU).
Its tree `c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9` equals the four-check passing
snapshot. Preserve the cleaned series and unchanged CPU production/test patch;
there are no migration versions to preserve or reconcile. Do not rewrite
merged/default history.

The lead confirmed local project `master` at b6e650ad is an ancestor of fresh
`origin/master` b66c929b: stale, not divergent unpublished work. Preserve that
local ref while preparing integration from a fresh origin/master checkout.
The remote feature remains f725dd3f until the exact-lease update after gates.
Keep fetched merge/consumer provenance and old/new heads in the lead's record;
no deployment, integration or consumer-pin update was performed by this session.

Reviewer0 now owns the revised all-lane whole-branch review. After it passes,
complete final central builds, then let the lead update the published feature
with a precise force-with-lease and fast-forward integrate into the explicitly
authorized `vpsfree-cz-configuration/master` target. Retain both feature refs,
cancel only obsolete active same-branch CI if any, and refresh the portal
comparison for the final head. A clean patch-equivalent rebase keeps this
repository/target approval under the Git procedure: prove equivalence with
range-diff or patch IDs, rerun appropriate verification and record the final
head. Material changes return through the lead under that procedure. Deployment
remains user-owned; no lifecycle action or cleanup follows integration.
Plan/state/portal/tracking cadence remain lead-owned.

Identity was revalidated from the tracking directory against the trusted binding;
both environment markers were absent. Existing applicable guidance and skills
were reused, with current plan/state/source/fixture/inventory evidence read.
Architect work changed only design.md and architect-result.md; no application
edit, functional test/build, commit, branch operation, deployment or lifecycle
action was performed by the architect. The passing-check and committed-head
updates above are lead-reported evidence; final review/build gates remain open.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
Keep the session open.
