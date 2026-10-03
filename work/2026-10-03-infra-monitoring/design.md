# Infra monitoring: design and verification brief

Status: prepared for implementer0, 2026-10-03. This is a design, not verification
or deployment evidence. Accepted scope is in [plan.md](plan.md). Repository base:
`b66c929bb7c202ad31bd8994a691ade14c40ebf0`.

## Ownership and scope

Only `vpsfree-cz-configuration` changes. Work in
`worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration`, on branch
`2026-10-03-infra-monitoring`. The architect owns this brief and
[architect-result.md](architect-result.md); the implementer owns application,
fixture and project-documentation edits. Refer material departures to the lead.
The lead owns plan/state/portal updates, review and verification coordination.

Implement three changes: typed machine metadata and host target labels; the
infra VPS critical filesystem SMS exception; and playground's adoption of the
existing staging CPU usage policy. Do not change disk thresholds, filesystem
selection, load-average rules, I/O-wait rules, CPU calculations, alert names,
severity, repeat policies, inhibition or notification transports. No input
updates, deployment, integration, cluster operations or cleanup are authorized.

## Interfaces and files

Paths below are relative to the configuration worktree.

| File | Change |
| --- | --- |
| `modules/cluster/default.nix` | Add `cluster.<name>.machineType` to the existing machine submodule. |
| `cluster/cz.vpsfree/machines/aitherdev/module.nix` | Set `machineType = "vm"`. |
| `cluster/cz.vpsfree/machines/em1/module.nix` | Set `machineType = "vm"`. |
| `cluster/cz.vpsfree/machines/build/module.nix` | Set `machineType = "vm"`. |
| `modules/clusterconf/monitor/default.nix` | Add authoritative `machine_type` to local/remote monitoring, infra and shared node exporter labels. |
| `modules/clusterconf/alerter/default.nix` | Insert the exact terminal exception between Telegram and the first SMS route. |
| `modules/clusterconf/monitor/rules/nodes.nix` | Edit only the four named CPU usage rules below. |
| `tests/prometheus/infra-monitoring-rules.{nix,yml}` | Add focused rule and timing checks using existing promtool conventions. |
| `tests/prometheus/infra-monitoring-config.nix` | Add generated metadata/target assertions and offline amtool routing checks; a small fixture helper is acceptable. |
| `flake.nix` | Register the two focused checks, using existing pinned inputs. |
| `docs/services/monitoring.md`, `mkdocs.yml` | Explain the lasting metadata/routing/CPU policy and link it in Services. |

The test filenames/check names are the recommended implementation interface, not
existing files. A small naming adjustment is routine; changing production
architecture to accommodate fixtures is not required. Keep rollout status and
temporary base comparisons in this session, not in project feature docs.

### Machine metadata and labels

Use a `mkOption` with `types.enum [ "vps" "vm" "physical" ]`. Its default is
`if config.container != null then "vps" else "physical"`. This classifies
managed containers through their existing metadata, not hostname, OS spin,
node role, carrier status or runtime detection. Explicit typed overrides remain
possible. Invalid enum values fail Nix evaluation. The three VM overrides belong
in metadata `module.nix`, not their system `config.nix` files.

Append the generated label **after** the existing custom-label merge:

```nix
existingLabels // metaConfig.monitoring.labels // {
  machine_type = metaConfig.machineType;
}
```

Apply this to all four construction sites: the local monitoring target pair,
remote monitoring targets, infra targets, and `mkNodeLabels`. Use
`confMachine.machineType` for the local pair and `m.metaConfig.machineType`
elsewhere. Do not alter the precedence or meaning of other custom labels.

`scrapeConfigs.monitorings` produces actual Prometheus job `mon`, not a job
named `monitorings`. Both local targets (Prometheus itself and node-exporter)
and the peer monitor's node-exporter get the label. `infra` and `nodes` label
all exporters already sharing their static target group. `mkNodeLabels` also
feeds `nodes-zfs-hypervisor`, `nodes-zfs-storage` and `nodes-ipmi`; these must
receive the same authoritative classification. Preserve `type = "node"` and
all existing alias, FQDN, domain, location, OS, role and storage labels.

Do not expand into ping, DNS, HTTP, log, service-specific or independently
constructed SSH-exporter target labels. Do not change `honor_labels`, relabeling,
target selection, exporter enablement or scraped endpoints. The authoritative
contract here is the final generated static target label. A conflict in
`monitoring.labels.machine_type` is resolved by merge order, without adding a
new rejection mechanism.

### SMS-only exception

Reuse the existing empty `blackhole` receiver. Add one sibling route immediately
after the email and Telegram siblings and before **both** SMS siblings:

```nix
{
  match = {
    job = "infra";
    machine_type = "vps";
    alertclass = "fsavail";
    severity = "critical";
  };
  receiver = "blackhole";
  continue = false;
}
```

The earlier email and Telegram routes retain `continue = true`; the terminal
match prevents traversal into the later SMS routes. This follows the existing
route style and Alertmanager's documented sibling traversal semantics. See
[Alertmanager routing](https://prometheus.io/docs/alerting/latest/configuration/#route).

Do not use inhibition, severity changes, an alert-name filter, a mountpoint
filter, a silence, or a broad container route. The existing common filesystem
rules remain byte-for-byte unchanged, including warning `<20%`, critical
`<=10%`, both `for = "5m"`, their mountpoint selector and `frequency = "hourly"`.
The exception therefore covers `/run` too. `/run` being tmpfs means disk
auto-expansion is not its recovery mechanism; that does not narrow the accepted
notification exception. Monitors themselves use job `mon`, so their filesystem
alerts remain eligible for SMS even when `machine_type = "vps"`.

### Playground CPU usage

Limit changes to these four rules:

| Alert | Selector after change | Hold | Aggregation/labels |
| --- | --- | --- | --- |
| `HypervisorHighCpuLoad` | `location!~"stg\|pgnd"` | existing 10m | unchanged |
| `HypervisorHighCpuLoadStaging` | `location=~"stg\|pgnd"` | existing 50m | add `location` to `avg by`; remove static `location = "stg"` |
| `HypervisorCritOsCpuLoad` | `location!~"stg\|pgnd"` | existing 10m | unchanged |
| `HypervisorCritOsCpuLoadStaging` | `location=~"stg\|pgnd"` | existing 50m | add `location` to `avg by`; remove static `location = "stg"` |

The backslashes in the table escape Markdown pipes; PromQL uses `"stg|pgnd"`.
The two relaxed aggregations become `avg by(instance, alias, fqdn, location)`.
Keep `100 - avg(irate(idle[5m])) * 100`, hypervisor/OS/mode selectors and the
existing `and on(instance) time() - node_boot_time_seconds > 3600` guard.
Warning remains strictly `>80%`, critical strictly `>90%`; the critical rule
remains restricted to `os="vpsadminos"`. Alert names retain `Staging` for
compatibility although the relaxed policy now covers both locations.

Do not add `location` to the strict aggregations or carry new labels through
other aggregate alerts. Every other rule, including all `node_load*`, storage
CPU, I/O wait, filesystem and ZFS rules, must compare equal to the base.

## Compatibility, rollout and recovery

This adds site-owned Nix metadata and a target label. Existing metadata callers
receive a default; exporters require no changes. There are no DB migrations,
seeds, persisted-format changes, API/client/CLI/Terraform changes, daemon
messages, or vpsAdminOS fleet updates. No coordinated update of running nodes
or VMs is necessary. Existing Prometheus TSDB and Alertmanager state remain
readable on rollback.

Adding a label creates new metric and unaggregated-alert identities. Old and
new series can coexist in historical queries; label changes can reset pending
alerts and cause resolution/refiring notifications. Short rate windows need
fresh samples after target relabeling. Staging's relaxed CPU alert preserves
its existing location; playground changes from the strict alert identity to the
relaxed one and adopts the longer pending interval. These are intentional.

For a later, separately authorized rollout, prepare both alerters before
updating either monitor, then update both monitors promptly:

1. `cz.vpsfree/containers/prg/int.alerts1` and `int.alerts2`: install the route.
2. `cz.vpsfree/containers/prg/int.mon1` and `int.mon2`: install labels and CPU rules.
3. Check effective configuration/reload health, representative target labels,
   and expected rule labels on both replicas. Do not send live test messages
   without separate authorization.

Old alerts without `machine_type` retain old SMS eligibility. New labels with
old alerter configuration also retain old eligibility. Partial monitor rollout
can temporarily produce both alert identities; HA notification deduplication
must not be assumed across different label sets. The alerter-first order makes
the exception available to each new labeled alert, but does not suppress an
old unlabeled alert still emitted by the other monitor.

Rollback to the prior central configurations restores their former routing and
CPU policy. Restoring old alerter config restores SMS eligibility even while
new labels remain; restoring old monitor config also removes the required VPS
label and returns playground CPU to the strict rules. Expect series/alert
identity transitions again. No TSDB deletion, migration reversal or exporter
rollback is needed. These are implications and prepared steps, not deployment
authorization; preserve the old central generations when executing a later
approved rollout under normal procedures.

## Acceptance and focused verification

Tests must consume production expressions/routes/label generation, not a copied
implementation of the new policy. Use only synthetic alert labels and local
files with promtool/amtool; no live Alertmanager or messaging endpoint is needed.

### Generated configuration checks

Use real machine metadata evaluation to assert defaults and the three explicit
VMs. The pinned confctl flake exposes `confctl.machines.<name>.metaConfig`; its
`mk-confctl-outputs.nix` does not expose a complete NixOS `config` output. Do not
invent a `nixosConfigurations` or `confctl.config` attribute.

A small Nix fixture can import the actual monitor/alerter modules with test
arguments and select their generated configuration. Both modules currently
wrap their configuration in `mkIf`; a direct-import fixture can select
`module.config.content` with `enable = true`, or use `lib.evalModules` with
minimal receiving options. Nix's lazy evaluation allows selection of target
groups/routes without evaluating full machines, unrelated services or secrets.
Supply realistic metadata/services and `confData.meet = { }` as needed. Keep
fixture mechanics in tests; do not extract production modules solely for this.

Required assertions:

- Managed container defaults to `vps`; ordinary node and physical infra host
  default to `physical`; aitherdev/em1/build explicitly evaluate to `vm`.
  Force evaluation of an invalid enum fixture and require failure.
- Generated `infra`, `nodes`, and local/remote `mon` static targets have the
  expected `machine_type`. Check an infra container, each explicit VM, a
  physical infra host, hypervisor and storage-node fixtures, and both monitors.
- Verify `nodes-zfs-hypervisor`, `nodes-zfs-storage` and `nodes-ipmi` use the
  same type and retain `type = "node"` and existing identifying labels.
- Give custom labels a deliberately conflicting `machine_type` plus an
  unrelated custom label. Generated type wins in all four constructors; the
  unrelated label survives. Generated target lists and jobs otherwise match.
- Render the actual alerter route/time-interval tree. For an offline route
  fixture, replace receivers with name-only declarations and omit templates
  and transport credentials; retain routing and time intervals verbatim.
  This tests route selection, not delivery or inhibition execution.
- Require route order, all four exact matchers, terminal behavior and unchanged
  email/Telegram/SMS subtrees, including hourly repeat routes and SMS daytime
  intervals. Preserve the entire inhibition configuration in the base diff.

Use amtool's exact receiver-set verification for these label combinations:

| Input labels, in addition to a synthetic alert name/instance | Expected receivers |
| --- | --- |
| `job=infra machine_type=vps alertclass=fsavail severity=critical frequency=hourly` | `team-mail,team-telegram,blackhole` |
| Same case with `/`, `/run`, `/nix/store` mountpoint labels | same; no SMS |
| Same critical case with machine type `vm`, `physical`, or missing | `team-mail,team-telegram,sms-aither,sms-snajpa` |
| Same VPS critical case with `job=nodes` or `job=mon` | all four notification receivers |
| Same VPS critical case with another/missing `alertclass`, or missing `job` | all four notification receivers |
| Same VPS filesystem case with severity `fatal` | all four notification receivers |
| Same VPS filesystem case with severity `warning` | `team-mail` |
| Existing `severity=none` case | `blackhole` |

`amtool config routes test` resolves matching routes; it does not prove actual
delivery, daytime activation, repeat timing, or inhibition. Check preserved
intervals structurally. Upstream implementation confirms the command compares
the ordered receiver list against `--verify.receivers`:
[amtool routing test source](https://github.com/prometheus/alertmanager/blob/main/cli/test_routing.go).

### Prometheus rule cases

Follow existing `tests/prometheus/process-count-rules.nix`: import production
rule groups, serialize JSON with `builtins.toJSON`, replace `@ruleFile@` in the
YAML fixture, and run `promtool check rules` plus `promtool test rules`.
Use group-aware 20-second samples/evaluations and explicit expected labels.

- Both stg and pgnd: 85% CPU fires only the relaxed warning after 50 minutes;
  95% fires relaxed warning and OS critical after 50 minutes. Never emit the
  strict counterparts; retain actual `location=stg` or `location=pgnd`.
- Production and a missing-location case: same thresholds fire the strict
  rules after 10 minutes and never the relaxed counterparts. The strict rules'
  existing label shape stays unchanged.
- At exactly 80%, no warning; at exactly 90%, no critical. A non-vpsAdminOS
  hypervisor can warn, but cannot trigger these OS-critical rules.
- Boot age exactly 3600 seconds does not satisfy the strict `>3600` guard;
  the next qualifying evaluation starts the hold. Preserve a boot-guard case
  for both policy locations, not only steady-state old hosts.
- Use two CPU cores with distinct idle rates in at least one fixture, so the
  result exercises the existing average, rather than only single-core data.
- A common critical filesystem sample retains job, machine type, critical
  severity, `alertclass=fsavail` and `frequency=hourly`; it still fires after
  five minutes on `/run` as well as the other selected mountpoints.

For predictable hold-boundary fixtures, an old boot timestamp such as `-7200`
and counters beginning at t=0 work. With 20-second sampling, the first usable
`irate` occurs at t=20s: relaxed checks should be pending at 50m and firing at
50m20s; strict checks pending at 10m and firing at 10m20s. Counter increments
of 3/4/2/1 seconds per 20 seconds represent 85/80/90/95 percent utilization
respectively. Confirm these assumptions in the fixture rather than silently
moving boundary expectations to make a failure disappear. See the
[promtool fixture format](https://prometheus.io/docs/prometheus/latest/configuration/unit_testing_rules/).

## Commands, tooling feasibility and gates

No command below was run as a test/build by the architect. The pinned repository
shell uses Ruby 3.4 and `mkConfigDevShell` in tools mode; entering it bootstraps
Bundler and gems under `.gems`. `.overcommit.yml` enables Nixfmt and RuboCop.
The four existing flake checks demonstrate `pkgs.prometheus.cli`; a locally
available nixpkgs package definition confirms `pkgs.prometheus-alertmanager`
builds both `alertmanager` and `amtool`. Resolve the latter against this flake's
pinned nixpkgs during implementation; it is not supplied by the current shell.
No tool or input upgrade is part of this change.

Run commands from the configuration worktree. Environment setup, uncached Nix
realization and other work of uncertain duration belong to a fresh policy
watcher under the monitor skill. Known bounded checks may run inline once the
environment and tools are available.

```sh
# Implementer setup: use the pinned shell or the lead's realized pinned-shell
# environment, and verify the declared hooks. The watcher installed the bundle.
nix develop --no-write-lock-file
bundle check
bundle exec overcommit --install
bundle exec overcommit --sign

# Quick static checks, after adding the focused fixtures.
git diff --check
bundle exec overcommit --run
nix eval --impure --no-write-lock-file --json .#confctl.machines \
  --apply 'ms: builtins.mapAttrs (_: m: { inherit (m.metaConfig) machineType; }) ms'

# Proposed focused checks. Stage owned new files first: Git flakes omit
# untracked files. Delegate if realizing dependencies or duration is uncertain.
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.infra-monitoring-config \
  .#checks.x86_64-linux.infra-monitoring-rules

# Preserve the adjacent existing rule regressions using cached dependencies.
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.vps-autostart-prometheus-rules \
  .#checks.x86_64-linux.process-count-prometheus-rules

# Inspection against the accepted base: common/infra files must have no diff;
# nodes.nix must change only the four approved CPU rules.
git diff b66c929bb7c202ad31bd8994a691ade14c40ebf0 -- \
  modules/clusterconf/monitor/rules/common.nix \
  modules/clusterconf/monitor/rules/infra.nix
git diff b66c929bb7c202ad31bd8994a691ade14c40ebf0 -- \
  modules/clusterconf/monitor/rules/nodes.nix
```

Inside the focused config derivation, the principal offline commands are:

```sh
amtool check-config "$route_fixture"
amtool config routes test --config.file="$route_fixture" \
  --verify.receivers=team-mail,team-telegram,blackhole \
  alertname=FilesystemCritFreeSpace instance=test:9100 \
  job=infra machine_type=vps alertclass=fsavail severity=critical frequency=hourly
promtool check rules "$rule_file"
promtool test rules "$test_file"
```

Those variables are fixture paths supplied by the check derivation. Repeat
receiver assertions for the matrix above, including the negative cases. Do not
infer success from only the positive exception case.

After quick checks and implementation commits, the lead must run mandatory
independent review before long configuration builds. Supply the complete
base-to-head commit inventory and final diff; explicitly record **no database
migrations** and whether obsolete intermediate approaches remain. A successful
focused derivation is not a full system-build result.

After that review gate, a fresh watcher runs these longer checks in the pinned
shell, with logs and exit results retained for the lead:

```sh
confctl build 'cz.vpsfree/containers/prg/int.mon[12]'
confctl build 'cz.vpsfree/containers/prg/int.alerts[12]'
```

Confirm selection includes exactly both monitors and both alerters using
`confctl ls` before building. Inspect source for the selector if its CLI behavior
differs; four explicit single-machine builds are an equivalent fallback. This
validates central system configuration and generated service files, including
the real receiver/template configuration. Metadata-only VM changes do not
require deploying or building aitherdev/em1/build systems to apply the policy.
Stop unexpected local kernel builds and investigate cache misses under the
workspace verification procedure. No deploy/dry-activate command is part of
verification here.

## Inspection evidence and remaining gaps

- `dev-session current` from the session directory returned the exact bound
  slug; both environment markers were absent, so the trusted developer binding
  supplied ownership. The initial command from the workspace root reported no
  current session; changing to the intended session directory resolved it
  before any session records were read.
- The configuration worktree remained clean at the stated base throughout
  architect inspection. No application source, input, plan, state or portal
  was changed by the architect, and no commit was made.
- Read the root/worktree instructions, applicable procedures, README, accepted
  plan/state, monitoring modules and representative existing fixtures. Inspected
  the exact pinned confctl source at
  `7bee58a52372b95c2198ce3f2a719807a3c2c66b` for flake outputs and shell setup.
- An offline metadata-only `nix eval`, with import-from-derivation disabled,
  failed because this member cannot access the Nix daemon socket. No build or
  test started. The lead subsequently confirmed that the authorized fresh
  watcher successfully entered the pinned shell and installed all 40 gems with
  the frozen bundle. Functional Nix checks can use that watcher path; the lead
  is capturing the realized shell environment for implementer quick commands.
  This is an available execution path, not a design blocker.
- The implementer still verifies declared hook installation/activation.
  Test packages, direct-import fixture mechanics and all suggested functional
  verification commands require execution; none is reported as passed here.

Stable session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-infra-monitoring/.
Keep the session open.
