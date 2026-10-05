Historical packet used for the completed independent review before narrow R1
fixture remediation. Current final heads/diff and verified history mapping are
in [branch inventory](branch-inventory.md) and [review record](review.md).

# Mandatory complete-branch review packet

## Outcome and acceptance

User requested implementation of the accepted infra-monitoring plan. Preserve
all filesystem rules/thresholds and pgnd raw load-average rules. Add reusable
machine-type metadata/labels; keep email and Telegram for critical infra VPS
filesystem alerts while preventing both SMS receivers. Apply existing staging
CPU usage holds to pgnd only; production keeps its strict policy.

Read [plan](plan.md), [state](state.md), [architect design](design.md),
[branch inventory](branch-inventory.md) and [complete final diff](review-final.diff).
Repository/worktree: `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration`.
Base: `b66c929bb7c202ad31bd8994a691ade14c40ebf0`.
Final head: `f3f8688b7ffc517a9a24150bd1f3d4056fbd35b7`.
Both intended commits are complete, with a clean worktree. The inventory lists
the complete series, split rationale, disposition of prior approaches and
explicit no-migrations provenance. Assess those conclusions independently.

## Selection and lanes

Overall risk: High, because notification routing changes live host behavior,
and target-label identities affect HA deduplication, rolling deployment and
rollback. No source deployment is part of this implementation task.

Independent retained review-purpose member: reviewer0, index 0,
thread 01a1021a-42ed-7e62-9bc2-43fbd84c6a48, read_only, ready,
saved gpt-6.1-sol/xhigh. No model or effort override and no fallback.
Review all four lanes: general, architecture/repetition, scope/proportionality,
risk/compatibility. Read the mandatory-change-review skill and every lane
reference in full. Perform the review directly without nested agents.

## Interfaces and consumers

The owning provider is site-local `modules/cluster/default.nix`:
`cluster.<name>.machineType`, enum vps/vm/physical, default vps for managed
containers and physical otherwise. Explicit vm overrides are aitherdev, em1,
and build. Confctl carries metadata through `confctl.machines.*.metaConfig`;
monitor module consumes it through confMachine and m.metaConfig. Static target
labels have machine_type appended after custom labels at all four constructors,
including mon local/peer, infra, and shared node labels/ZFS/IPMI. Existing node
`type=node` remains. Alertmanager is the immediate label consumer. No exported
cross-project API or pins change; all flake/Gem locks remain unchanged.

The exact terminal route follows continuing email and Telegram and precedes
both SMS siblings: job=infra, machine_type=vps, alertclass=fsavail,
severity=critical, receiver=blackhole, continue=false. No severity/inhibition/
interval/transport change. The CPU selectors change only four rules; relaxed
rules retain location through their aggregation. Names and calculations remain.

## User decisions and boundaries

- Keep filesystem thresholds, fatal policy and holds as they are.
- Exception includes every selected filesystem, including /run; /run is tmpfs
  and disk auto-expansion does not recover it. That retained behavior is accepted.
- Only CPU usage changes for pgnd, not node_load rules, storage CPU or I/O wait.
- Reuse existing blackhole after email/Telegram; no general notification framework.
- Classification defaults plus explicit known VMs; no runtime/hostname detection.
- Missing machine_type stays eligible for SMS, including during mixed rollout.
- No input updates, migrations, live test messages, production deployment or
  default-branch integration. Do not broaden these boundaries in remediation.

## Verification and documentation

Real machine metadata evaluation passed. Declared Nixfmt/RuboCop full Overcommit,
active hooks, Bash syntax and whitespace checks passed. Fresh watcher passed:

`nix build --no-write-lock-file --no-link .#checks.x86_64-linux.infra-monitoring-config .#checks.x86_64-linux.infra-monitoring-rules`

`nix build --no-write-lock-file --no-link .#checks.x86_64-linux.vps-autostart-prometheus-rules .#checks.x86_64-linux.process-count-prometheus-rules`

Evidence: quick-checks-2-result.json/log. Tested staged tree
406b654f992c65815806615e86c7a84fe267451c equals final committed tree. First
focused attempt failed due to incomplete synthetic service metadata; fixture
fields were corrected before commits and the actual derivations then passed.
No production fix or scope deviation. Common/infra rules and locks compare
unchanged; nodes.nix has only the accepted four CPU edits.

Owning-project explanation: docs/services/monitoring.md, linked by mkdocs.yml.
It records classification precedence, notification boundaries, CPU policy,
label identity/HA rollout/rollback constraints and verification limits. Session
design holds this initiative's proposed deployment ordering separately.
No deployment has occurred. Offline amtool checks receiver selection, not live
notification delivery, daytime activation, repeat timers or inhibition execution.
Central full configurations will be built only after this review gate.

## Deliverable

Start with Blocking/Important/Advisory findings ordered by severity with path,
line and commit references, then a brief conclusion for EACH lane. Explicitly
conclude on the whole branch history (obsolete approaches/fixups) and migration
lineage, including "no migrations". List residual test/deployment risks even
if there are no findings. Remain read-only: send the complete report via team
assignment message to lead, which will record it. Do not write fixes, run long
builds, commit, push, deploy or change lifecycle. Validate session/current and
read all applicable workspace and repository procedures before inspection.
