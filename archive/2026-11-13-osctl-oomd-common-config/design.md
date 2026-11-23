# Common osctl-oomd tuning

Original D/I brief (2026-11-13), subsequently accepted and implemented. Architect:
`architect0`; implementation owner: `implementer0`. The original scope and source
evidence below remain historical. Follow-up D2 is recorded at the end of this
file. User scope remains configuration only, **no deployment**.

## Scope and source evidence

Change only `vpsfree-cz-configuration`. Investigation used its existing local
`origin/master` at `08d68a85f24a95b70b2d806f995f04b236e4d89a`; no fetch, worktree,
configuration edit, commit, push, merge or deployment was performed by the
architect. The bare repository's `HEAD` is older and must not be used as the
implementation base. The lead/implementer must use the refreshed approved feature
base and report a material change to these source facts.

That source commit, `cluster: lower oomd restart thresholds on node25.prg`, adds
exactly this block to `cluster/cz.vpsfree/nodes/prg/node25/config.nix:110`:

```nix
  osctl.oomd.settings = {
    restart_hits = 4;
    load_multiplier = 1.5;
  };
```

The destination is the existing `osctl.oomd.settings` attribute set in
`cluster/cz.vpsfree/nodes/common/all.nix:176`. It currently contains
`verbose = true;`; the surrounding `osctl.oomd` set has `enable = true;`.
A source search of all tracked Nix files found no other definitions of these two
settings or additional oomd policy blocks.

The production and staging vpsAdminOS inputs both resolve to
`c0ad0ad8f970e04099830ff1c2ebfda01e8c9d62`. At that revision:

- `os/modules/osctl/osctl-oomd.nix` defines `osctl.oomd.settings` as a JSON
  freeform submodule and passes its generated JSON to the daemon's `--config`.
- `osctl-oomd/lib/osctl/oomd/cli.rb` accepts both settings. Its unchanged defaults
  are eight restart hits at the default 15-second interval and load multiplier
  2.0; explicit configuration preserves the requested four hits and 1.5.
- `osctl-oomd/lib/osctl/oomd/watcher.rb` computes the activation threshold from
  the rolling host-load median multiplied by `load_multiplier`. This is a
  multiplier, not an absolute load-average value. Other selection guards remain
  untouched.

These repositories were read only as bounded configuration/interface evidence;
neither vpsAdminOS nor confctl needs a change or input update.

## Implementation package I

Owner: `implementer0`. Routine technical clarification: `architect0` in this
verified session. Scope or consequential design changes go to the lead.

| File | Required change |
| --- | --- |
| `cluster/cz.vpsfree/nodes/common/all.nix` | Add `restart_hits = 4;` and `load_multiplier = 1.5;` inside the existing `osctl.oomd.settings` set, preserving `verbose = true;` and `enable = true;`. |
| `cluster/cz.vpsfree/nodes/prg/node25/config.nix` | Remove the entire now-redundant five-line `osctl.oomd.settings` block. |

Use ordinary assignments, matching the original node25 tuning. No `mkForce`,
`mkDefault`, new module, import change, generated file, test framework, software
change, pin update or project documentation addition is needed. Expected diff:
two added setting lines and the five-line local block removed.

Dependencies: lead acceptance of this brief; the lead's initial tracking commit;
a correctly based session-owned configuration worktree; normal repository shell
and hooks. These are execution prerequisites, not unresolved design choices.
The implementer owns only the two configuration files and its assigned Git
mutation window. Architect exclusively owns this brief; lead owns plan, state,
portal and review coordination. No machine or repository merge claim is needed
for feature implementation and verification.

## Coverage and invariants

All 13 nodes registered beneath `cz.vpsfree/nodes/` already import this common
module and already enable oomd:

| Existing import route to `common/all.nix` | Nodes |
| --- | --- |
| `brq/*/config.nix` → `brq/common.nix` | `brq/node5`, `brq/node6` |
| `pgnd/*/config.nix` → `pgnd/common.nix` | `pgnd/node1` |
| `prg/node*/config.nix` → `prg/common.nix` | `prg/node19` through `prg/node25` |
| `prg/backuper2/config.nix` → `common/storage.nix` | `prg/backuper2` |
| `stg/*/config.nix` → `stg/common.nix` | `stg/node1`, `stg/node2` |

The 11 non-staging nodes select the production channel; the two staging nodes
select staging. Include backuper2 because it is an existing node/common-policy
consumer. Do not broaden imports to containers, general machines or another
configuration repository.

Acceptance invariants:

1. Every listed node inherits numeric `restart_hits = 4` and
   `load_multiplier = 1.5` from one common definition.
2. Node25's effective oomd configuration is unchanged; its duplicate definition
   disappears. The other 12 nodes gain only these two explicit settings.
3. Oomd enablement, verbose logging, interval, CPU/memory conditions, stop-hit
   policy and all unrelated configuration remain unchanged.
4. Exactly the two owned configuration files change. Existing input locks and
   generated inventory remain untouched.
5. No deployment, dry activation, reboot, remote runtime check, machine
   reservation or integration is part of this package.

## Compatibility, deployment and recovery

This uses existing keys supported by the pinned daemon and module. It changes no
persisted format, database, migration, API/client, protocol or binary. Nodes may
continue running their existing configurations independently; no coordinated
update is necessary. There is no runtime effect during this task.

If deployed in separately authorized future work, the other nodes would respond
to qualifying pressure at the same lower thresholds as node25. This brief does
not authorize that operation. Configuration recovery is a revert of the move:
remove the two common values and restore the node25 block. No data migration or
state recovery is required; an old configuration can load the same existing
state. Runtime rollback, if ever needed after a future deployment, belongs to
that rollout's own approval and records.

## Verification and evidence

Quick checks, owned by the implementer, expected to take under a minute once the
repository environment is available:

- Inspect the complete diff and run `git diff --check`.
- In the repository's `nix develop` environment, check RFC-style formatting of
  the two changed files and parse both with `nix-instantiate --parse` (discard
  the parsed output). Preserve the normal commit hooks.
- Search for `restart_hits`, `load_multiplier` and `osctl.oomd` to confirm the
  common values occur once, the node25 duplicate is absent, and enable/verbose
  stay unchanged. Confirm the 13 existing import routes above against the final
  base. These source checks are sufficient for release to final review; do not
  add a synthetic test that merely duplicates the assignments.

Longer check after all intended changes are committed and independent final
review passes: the configuration repository's AGENTS.md requires
`confctl build <path>` for touched nodes. The common change affects all 13, so
the bounded build scope is `confctl build 'cz.vpsfree/nodes/*'` from the pinned
development shell. Use the mandatory fresh verification watcher for this
uncertain-duration batch. This is a build only: do not run any `confctl deploy`
variant, including `dry-activate`.

Allow roughly 10 minutes for cached evaluation/builds before reassessing actual
progress and remaining derivations. Success is all 13 selected node builds;
stop and diagnose an unexpected kernel build, source failure or unrelated
expansion. Do not waive a required build by calling a parse/import check a full
evaluation. If a repository/environment problem prevents the required check,
report the concrete gap to the lead without changing inputs or expanding scope.
No VM integration campaign or production test is needed for this relocation.

Deliver to lead: exact base/head, two-file diff, quick check outcomes, unchanged
pin evidence, all-node import coverage, check logs/results or explicit remaining
gaps, and whole-branch history provenance with **no migrations**. The lead owns
final review, publication/readiness sequencing and any later integration gate.

## Documentation placement and handoff

The existing settings block is self-explanatory; no lasting project documentation
needs changing. This brief records maintainer rationale and temporary execution
checks in the owning session. Lead maintains plan/state/portal and records actual
verification results; this design document is not evidence of builds or runtime
verification having run.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-osctl-oomd-common-config/)

## D2: update OS and node-management channel inputs (2026-11-23)

Status: sufficient brief, ready for lead acceptance and allocation to
`implementer0`. Prior package D is complete; architect capacity and the retained
same-session roster were confirmed. Identity was verified by `dev-session current`
from this session's directory against the trusted thread binding; both environment
identity variables were absent. No technical decision blocks preparation of this
pin update. The existing full-node-build gap remains an explicit verification
limit, not a successful check.

The user requested the original oomd move be merged and added an update of
`vpsadminos` and `vpsadmin` in `production`, `staging` and `os-staging`. The lead
owns the original integration. This package prepares the subsequent channel
updates; it grants no further integration or deployment authority.

### Mapping and selected revisions

Source snapshot: configuration remote `master`
`baf73377af387a8ef1c90e20b17bb559fcd15c45`, confirmed equal to the local
`origin/master` by a fresh SSH `ls-remote` on 2026-11-23. All facts below use that
snapshot rather than the old feature-worktree head. Read-only inspection used
canonical bare repositories and this session's records; no other-session content
was used. The lead/implementer refreshes the working branch and supplies its
actual update base after the original move is integrated.

`flake.nix` defines five applicable inputs, not six:

| Channel | Role | Configuration input | Old revision |
| --- | --- | --- | --- |
| `production` | `vpsadminos` | `vpsadminosProduction` | `ccd51ed38ebffa2e744f7f8847668bc2e3413378` |
| `staging` | `vpsadminos` | `vpsadminosStaging` | `e9d55bada43c888ae91139d549d156a0831817de` |
| `os-staging` | `vpsadminos` | `vpsadminosOsStaging` | `e9d55bada43c888ae91139d549d156a0831817de` |
| `production` | `vpsadmin` | `vpsadminProduction` | `2c390959ee089f99e07c476d072ffdf80116fa7d` |
| `staging` | `vpsadmin` | `vpsadminStaging` | `c26465c0be452bbf5843d782a324dc82c122f28b` |
| `os-staging` | `vpsadmin` | Absent | No input to update; preserve the mapping. |

The inputs use unqualified GitHub URLs, so their upstream default branches
determine ordinary updates. Fresh SSH `ls-remote --symref origin HEAD` established:

- `git@github.com:vpsfreecz/vpsadminos.git`: default **staging**, selected revision
  `b86287c105b749827cd63632ac35936533910f63` for all three OS inputs.
- `git@github.com:vpsfreecz/vpsadmin.git`: default **master**, selected revision
  `4062a8da3314aa7b48170b0d6f441446bad9b207` for both node-management inputs.

The exact objects already exist in the canonical repositories. Each old revision
in the table is an ancestor of its selected target. If upstream advances before
the update, record the actual selected revisions and inspect only the additional
range for the boundaries below; escalate a material incompatibility to the lead.

Production/staging cover the same 11+2 nodes as package I. `os-staging` is also
used by 45 current machine declarations, predominantly NixOS containers, plus
the build machine and three `org.vpsadminos` declarations in this repository.
`profiles/ct.nix` imports the selected OS container module. This requested channel
update therefore has wider source coverage than the original oomd-only move;
do not change host declarations or imports.

### Implementation package I2: files, command and ownership

Owner: `implementer0`; routine technical peer: `architect0`. The lead accepts D2,
confirms capacity after the refresh package, supplies the post-integration base,
and allocates one exclusive configuration index/commit window. Architect retains
`design.md`; lead retains plan/state/portal. No repository or machine claim is
needed for this feature work.

Only tracked deliverable: **`flake.lock`**, generated with the configuration
repository's pinned confctl (`d8ab7d4c062a5d0b36ff65ac42c8617f10fb8c49` at the
snapshot). In the normal repository `nix develop` environment, run sequentially:

```sh
confctl inputs channel update --commit '{production,staging,os-staging}' vpsadminos
confctl inputs channel update --commit '{production,staging,os-staging}' vpsadmin
```

Pinned `lib/confctl/cli/inputs/channels.rb` skips absent roles within a matched
channel set. The first command selects three inputs; the second selects two.
It does not add a `vpsadmin` role to `os-staging`. Do not omit the role argument,
which would also select unrelated channel inputs such as nixpkgs.

Preserve hooks and confctl-generated commit messages, including useful upstream
Git changelogs and their original line wrapping. The updater commits only
`flake.lock` through `git commit -F` using a temporary message file. Expect one
generated update commit per role; do not add hand-written changelog files or
manually edit the lock. Keep only the final update for each logical input stream
if a refresh becomes necessary. Do not rewrite the already integrated oomd move.

### Pin invariants and expected transitive effects

- Set the three OS pins to the same selected OS revision and the two node-admin
  pins to the same selected vpsAdmin revision, with generated content hashes.
- Preserve every root channel/input mapping, `original` URL and existing follows
  edge. Preserve nixpkgsProduction, nixpkgsStaging, nixpkgsStable and
  nixpkgsUnstable revisions, confctl, devWorkspace and all unrelated root pins.
- The separate `vpsadmin` channel owns `vpsadminServices`, already at
  `4062a8da3314aa7b48170b0d6f441446bad9b207`; do not update that input or the
  separate WebUI/notification-template inputs as extra work.
- `vpsadminProduction` follows `vpsadminosProduction` and `nixpkgsProduction`;
  `vpsadminStaging` follows their staging counterparts. `vpsadminServices` also
  follows `vpsadminosStaging`, so its effective OS dependency changes even though
  its own source revision remains fixed. Record this intended existing follows
  effect rather than treating the services dependency graph as unchanged.
- The inspected OS production range changes only its upstream root nixpkgs and
  nixpkgsUnstable locks; configuration follows edges override both. Its
  impermanence, netlinkrb and ruby-lxc inputs are unchanged. The inspected vpsAdmin
  production range changes its upstream OS dependency graph, but the
  configuration's OS/nixpkgs follows edges override it. Staging ranges have no
  upstream lock changes. Thus only the five selected source identities should
  change semantically in this configuration lock. Nix may renumber/deduplicate
  lock nodes; compare reachable input paths and identities, not raw node names.
  Explain any additional semantic change before accepting it.
- Preserve the original common oomd tuning and all configuration source files.
  `.confctl` caches, fetched source and logs are disposable evidence, not tracked
  deliverables. No runtime, secret, profile, machine or deployment mutation is
  part of I2.

### Bounded compatibility and migration findings

The production OS range has eight commits, with three functional Top/oomd
changes; staging/os-staging need only the final two. The production vpsAdmin
range has eighteen commits; its concrete node interface change is
`597da69b14aca0e838b54410d76a52193c19b7ed`. The rest includes packaged dependencies,
WebUI/mail changes and incident policies. This is compatibility evidence for a
configuration update, not an independent audit of upstream implementation.

The OS range changes `osctl -j ct top` to bare **schema 2** records. New oomd and
new libnodectld consume that format and reject older wire formats without an
unsafe fallback. Upstream `docs/os/oomd.md` requires matching Top and oomd plus
osctld support for guarded commands. Preserve the existing explicit oomd values;
no OS Nix module, OS upgrade migration, kernel package or ZFS package changes
occur in the inspected OS range.

For a separately authorized future rollout, stop/restart local Top JSON readers
as required, drain or reconcile pending oomd actions, and switch the matching OS
and nodectld consumers together on each node. Changing the sampler does not
cancel a blocked action. A matching old OS/reader set is required for rollback;
host-load history format is unchanged. There is no evidence requiring all nodes
to switch simultaneously: the changed wire format is local to each node, so
mixed nodes may coexist provided each node's producer/consumers stay matched.
Do not infer that replacing configuration pins has updated running services.

The vpsAdmin range contains published migration
`api/db/migrate/20261030180000_add_incident_escalation.rb`, adding incident policy
and action history plus VPS/report fields. It is already included in the
unchanged `vpsadminServices` source pin. Node channels consume node-management
components; this update runs no migrations and does not advance API-services
source. Runtime schema/deployment state was not inspected and is not claimed.
Do not describe the upstream range as having no migrations.

Upstream `docs/incident-escalation.md` requires the compatible backend/schema and
`create_incident_report` RPC handler before the new nodectl is activated; old
SQL-writing nodectl must not be used after policy activation. A future rollout
must verify that prerequisite, reconcile mail templates/site declarations and
use compatible clients/frontends before enabling new calls. Schema downgrade
removes incident-policy history and is unsafe while services/actions depend on
it. Retain schema/data and reconcile submitted work when rolling back compatible
software. This task neither deploys that feature nor changes its existing site
policy. Before any future rollout, follow those upstream recovery contracts.

Configuration-only recovery is a revert of the generated pin update commits,
retaining the independently integrated oomd change. With no deployment, this
does not require a data rollback or coordinated service operation.

### Checks, acceptance and remaining build gap

Quick checks: preserve hooks; run `git diff --check`; parse `flake.lock` as JSON;
inspect `confctl inputs channel ls '{production,staging,os-staging}'`; and compare
the before/after semantic lock graphs against the five-input table and invariant
list. Confirm only `flake.lock` changed in I2 and both generated messages contain
the correct old/new ranges. Capture the final base/head and the complete branch
history, keeping original oomd integration evidence separate from I2 approval.
Allow a few minutes for ordinary pinned-shell/input metadata setup; unexpected
builds or unrelated lock changes require diagnosis rather than more scope.

Use channel/machine metadata evaluation to verify final selection for production,
staging and os-staging without realizing complete host systems. This proves
selection and graph validity, not successful system builds. No new test framework,
VM campaign, upstream unit-suite rerun, runtime probe or deployment is needed to
validate a generated pin diff.

The existing all-13-node `confctl build 'cz.vpsfree/nodes/*'` failed after 41 seconds
because `/secrets/nodes/initrd/ssh_host_ed25519_key` is absent during evaluation.
The bounded setup diagnosis found no sanctioned alternate local setup. Preserve
that full-build gap in the I2 handoff; do not retry unchanged, fabricate/copy
secrets, override source configuration or weaken the repository build requirement.
With an authorized environment that provides the required keys, run the node
batch and a representative os-staging container build under the monitor skill
after applicable final review. Use `cz.vpsfree/containers/brq/int.ns1` as the
existing container-profile representative. Reassess at roughly ten minutes or
on the first concrete failure, and stop an unexpected local kernel build. A
successful representative build does not certify all 45 os-staging consumers.

Lead chooses the applicable mandatory-review path and records any required
verification/integration decision; neither mechanical source updates nor this
brief waive the existing build gap. I2 may be implemented and published with the
gap reported accurately. No `confctl deploy` variant, including `dry-activate`,
is authorized.

Completion evidence for I2: actual five-input old/new revisions and hashes,
unchanged follows/root-pin inventory, generated commit IDs/messages, quick check
results, known build gap, upstream migration/interface boundaries above, and
the final range's history/consolidation conclusion. Keep evidence in this
session; routine channel updates need no new project documentation.
