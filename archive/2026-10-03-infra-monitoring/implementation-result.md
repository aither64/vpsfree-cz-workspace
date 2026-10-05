# Implementation result: final global filesystem policy

The revised implementation is committed and locally clean at
`657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da`. Its exact tree is
`c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9`, identical to the lead's passing focused and adjacent
check snapshot. The complete branch contains exactly two behavior commits from
`b66c929bb7c202ad31bd8994a691ade14c40ebf0`. It is ready for the lead's revised whole-branch independent
review; full builds and integration remain pending and lead-owned.

## Identity, authorization and exact series

`dev-session current` was rechecked from this tracking directory and returned
`2026-10-03-infra-monitoring`. Both environment markers were absent; the exact
trusted developer binding to `/home/aither/workspace/ai/vpsfree.cz` established
ownership. Retained member settings remain implementation,
`gpt-6.1-sol/xhigh`, workspace_write. The retained configuration worktree and
branch are `worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration` and
`2026-10-03-infra-monitoring`.

Base: `b66c929bb7c202ad31bd8994a691ade14c40ebf0`.

| Order | Exact commit | Subject |
| --- | --- | --- |
| 1 | `f53354dec1596bf665c80f85c557a9b05755805a` | monitoring: restrict critical filesystem alerts by type |
| 2 / final | `657cc0a8e087f8c4bed7fe8d7176cb9f06a6e2da` | monitoring: apply staging cpu alert policy to playground |

The lead explicitly authorized this consolidation after passing checks and
provenance inspection. The user authorized eventual verified integration into
`vpsfree-cz-configuration/master`; the lead owns that action and the user owns
deployment. No member push, master update, deployment, input change, lifecycle
operation or cleanup occurred. The session remains open.

## Complete changed-path inventory

The first commit owns metadata, authoritative host/JVB labels, global critical
filesystem eligibility and its fixtures/docs/check registration (12 paths):

- `cluster/cz.vpsfree/machines/aitherdev/module.nix`
- `cluster/cz.vpsfree/machines/build/module.nix`
- `cluster/cz.vpsfree/machines/em1/module.nix`
- `docs/services/monitoring.md`
- `flake.nix`
- `mkdocs.yml`
- `modules/cluster/default.nix`
- `modules/clusterconf/monitor/default.nix`
- `modules/clusterconf/monitor/rules/common.nix`
- `tests/prometheus/infra-monitoring-config.nix`
- `tests/prometheus/infra-monitoring-filesystem.yml`
- `tests/prometheus/infra-monitoring-routing.sh`

The second owns the four CPU edits and their fixture/check registration, with
only CPU-related additions to the final monitoring page (five paths):

- `docs/services/monitoring.md`
- `flake.nix`
- `modules/clusterconf/monitor/rules/nodes.nix`
- `tests/prometheus/infra-monitoring-rules.nix`
- `tests/prometheus/infra-monitoring-rules.yml`

Their union is the entire 15-path final diff. No unrelated source or generated
dependency file changed. `modules/clusterconf/alerter/default.nix` is absent
from both the final diff and first commit: it equals the base exactly.
See [machine-readable inventory](revised-final-inventory.json) and
[complete production diff](revised-final-production.diff).

## Final behavior and preserved invariants

Typed `machineType` accepts `vps`, `vm` and `physical`; managed containers
retain the VPS default and other hosts the physical default. The explicit VM
assignments for aitherdev/em1/build remain unchanged. All four authoritative
host label constructors are retained byte-for-byte relative to the accepted
prior implementation: local/peer `mon`, `infra` and shared node labels,
including ZFS/IPMI. They preserve custom-label precedence except for the
intentionally authoritative `machine_type`, and retain node role/identity.

All configured JVB groups now add literal `machine_type="vps"`. Real Meet data,
alias/type/project labels and paired 9100/9700 endpoints remain unchanged.
The common `FilesystemCritFreeSpace` numerator alone gains
`machine_type=~"vm|physical"`. The denominator, mount selector, percentage
value, <=10% threshold, five-minute hold, name, annotations, severity, class
and hourly frequency remain intact. Eligibility is global and type-based:
VPS/missing/empty/invalid/lookalike types are excluded, regardless of job.
There is no job fallback, `unless`, join, recording rule or SMS exception.

`FilesystemLowFreeSpace` and separate node fatal-rootfs rules remain unchanged.
The alerter equals the base, including normal receivers, five routes, timers,
daytime settings, inhibition and its original severity-none blackhole.
Independently supplied critical/fatal alerts retain normal notification routes.

Exactly the accepted four CPU source edits remain. Relaxed staging/playground
alerts preserve real locations and 50-minute holds; strict rules exclude both
and retain ten-minute holds. Names, >80/>90 thresholds, calculations and boot
suppression remain unchanged. Raw load-average, I/O-wait, storage CPU, other
filesystem, ZFS and Meet-specific rules remain intact. All tracked locks and
generated gemsets were compared byte-for-byte with the base and are unchanged.

## History reconciliation and old/new equivalence

The prior published first/head were
`e7b029165e3304e6f1ca4ec7e261d007ff4cab81` / `f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`.
The first is superseded by the approved global policy. The clean series
introduces that policy directly: no add/remove-SMS, fixup, unused compatibility
path or obsolete behavior commit remains. The base has not changed.

[Whole-series range-diff](revised-range-diff.txt) maps both old commits to the
new ones. The first differs by the accepted global-policy revision and matching
fixtures/docs. The second's differences are only the documentation adaptation
to the new first commit. The complete patch for nodes.nix, both CPU fixtures
and the CPU flake registration is byte-identical to the prior CPU commit;
see [compared CPU patch](revised-cpu-patch-equality.diff). The complete final
nodes.nix and both CPU fixture bytes also equal the prior head. Metadata/VM
modules, flake.nix and mkdocs.yml equal that head. Removing the single critical
selector restores common.nix exactly to the base; removing the single JVB
label restores monitor/default.nix exactly to the prior head.

The lead's fresh provenance check found origin/master at the base and
origin/feature at the prior head, unmerged, with no PR, other containing refs
or branch CI runs. No session release, deployment or consumer pin occurred.
No migration versions exist. The prior objects remain available and a verified
bundle preserves their series at
`/tmp/infra-monitoring-consolidation-ayx0k2fm/prior-series.bundle`; scoped snapshot/patch/message files are
also retained there. The prior report is preserved as
[historical implementation result](implementation-result-before-global-revision.md).
No repository-wide reset, clean or stash was used.

At final inspection, origin/master still points to `b66c929bb7c202ad31bd8994a691ade14c40ebf0` and
origin/feature still to `f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`. A separate local master ref was
observed at `b6e650ad902482b4c4e66b5a89a4275bed92419e`; it was not changed.
The lead must account for that pre-existing ref when selecting the integration
target. No remote operation was performed by the member.

## Verification and hooks

[Revised successful result](revised-quick-checks-2-result.json) and
[log](revised-quick-checks-2.log) record the lead's known-warm checks on the
exact final tree: `infra-monitoring-config` + `infra-monitoring-rules`
exit 0 in 6.760 seconds, then autostart + process-count checks exit 0 in
2.929 seconds. Final `HEAD^{tree}` and `git write-tree` both equal that tree,
so consolidation changed no tested bytes. No member functional daemon access
was attempted or retried.

The config fixture evaluates real metadata, enum rejection, conflicting custom
labels, all host/ZFS/IPMI constructors and both monitor identities. It imports
real Meet data and checks all eleven groups' exact labels/paired targets. Its
production common-rule fixture covers VM/physical positives and excluded types
across all four jobs, absent/unrecognized job positives, mounts, thresholds,
percentage values, complete alert labels/annotations, pending/firing timing,
multiple filesystems/types on an instance and unmatched denominator labels.
Warning fixtures cover VPS/missing types plus selected 20% equality and 19%
positive cases. Routing covers restored normal critical/fatal delivery selection,
warning and none behavior with inert transports. CPU tests retain their full
threshold/hold/location/average/boot-boundary coverage.

The first revision focused run failed only because two warning queries also
selected the independent eligible `missing-job:9100` VM. Those two queries were
restricted to the intended eight four-job instances; every input/expected sample
and production byte stayed intact. The successful rerun verifies the correction;
see [check request](revised-implementation-check-request.md) for diagnosis.
The earlier R1 selected-mount 20%/19% boundary correction remains covered.
No material design deviation occurred.

Pinned Nixfmt check, Bash syntax, unstaged/staged whitespace and full active
Overcommit Nixfmt/RuboCop checks passed before consolidation; see
[revision static log](revised-static-checks.log) and
[fixture correction static log](revised-fixture-static-checks.log).
Executable declared pre-commit and commit-msg hooks were reverified. Both final
commits ran active applicable pre-commit and commit-msg hooks using inherited
`os.environ` merged with `/tmp/infra-monitoring-realized-dev-env.json` and the
frozen bundle. Exact temporary message files were passed with `-F`; no hook
was bypassed. Both final hook runs passed without warnings; see
[consolidation/hook log](revised-consolidation-hooks.log).

The temporary sequence editor's initial interpreter error stopped before any
history change; the corrected editor succeeded. An intermediate first subject
width advisory was corrected by an active-hook amend. Neither intermediate
attempt is part of the final two-commit series. Final base-to-head whitespace
checks passed, `git rev-list --count base..HEAD` returned 2, and
`git status --porcelain=v1 --untracked-files=all` returned empty. These checks
and exact equality assertions are recorded in the inventory artifact.

## Documentation, compatibility and remaining gates

The [project monitoring policy](../../worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration/docs/services/monitoring.md)
and Services index link are reconciled with the final source and passing
fixtures. The page explains classification/precedence, JVB VPS labels, global
critical eligibility, missing types, warning/fatal behavior, preserved /run,
CPU policy, mixed versions, rollback and focused commands. SMS-only and
alerter-first prose is removed. The final CPU section remains byte-identical
to the accepted prior page. First/second commit docs describe their respective
behavior; the final page equals the checked snapshot exactly. Writing guidance
was applied directly during implementation. Session rollout evidence remains
here rather than in lasting project behavior docs.

**No migrations**: no database schema, seeds, persisted format, API/client/CLI/
Terraform contract or daemon protocol changed; there is no migration lineage
to preserve or consolidate. Existing Prometheus/Alertmanager state remains
readable on rollback. Exporters, nodes, VMs and JVBs require no update or
coordinated fleet rollout. Both monitors should receive labels/rule together;
new series/alert identities can reset pending windows and prevent mixed-label
HA deduplication. An old monitor can still emit VPS criticals during rollout.
Existing criticals may resolve normally. Warning visibility remains subject to
other existing inhibition. Reverting Alertmanager alone cannot restore an alert
that Prometheus no longer emits.

Fresh all-lane whole-branch independent review and both-monitor/both-alerter
full builds remain required and lead-owned; prior SMS-policy review/builds do
not validate this new boundary. Offline routing checks selection, not actual
notification delivery, activation times, repeat timers or inhibition execution.
No production scrape/reload/live notification behavior is claimed verified.
The lead owns precise-lease feature publication and authorized default
integration after remaining gates; the user owns deployment.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
Session remains open.
