# Revised global filesystem policy: checks requested

The settled revision is staged in the retained configuration worktree; no commit
or history rewrite has begun. HEAD remains
`f725dd3f407b0e5b82c9f9c1ad7720bbc7b14b68`; base remains
`b66c929bb7c202ad31bd8994a691ade14c40ebf0`.

Exact staged tree: `c3a20ba419ff6bc8e2b3ed2a6d4600087d143af9`.
There are seven owned changed paths, with no unstaged changes:

- `modules/clusterconf/monitor/rules/common.nix`
- `modules/clusterconf/monitor/default.nix`
- `modules/clusterconf/alerter/default.nix`
- `tests/prometheus/infra-monitoring-config.nix`
- `tests/prometheus/infra-monitoring-filesystem.yml`
- `tests/prometheus/infra-monitoring-routing.sh`
- `docs/services/monitoring.md`

## Functional commands for the lead

The first focused run on tree
`9dcb7400a5fe933c7e2fc4bb3b7e1b2e10543b04` failed in 7.398 seconds;
see [result](revised-quick-checks-result.json) and
[log](revised-quick-checks.log). Production config/routing assertions and rule
validation passed. The two warning sample assertions also selected the separate
eligible `missing-job:9100` VM. Only their pending-at-4m40s and firing-at-5m
queries now use `instance=~"(vps|missing)-(infra|nodes|mon|meet-jvbs):9100"`.
All inputs and expectations remain byte-for-byte intact. The empty pre-hold
assertion remains unchanged. This corrected tree awaits functional verification.

Run the known-warm focused and adjacent checks from
`worktrees/2026-10-03-infra-monitoring/vpsfree-cz-configuration` through the
authorized parent environment; delegate if realization or duration is uncertain.
The member has not retried denied daemon access.

```sh
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.infra-monitoring-config \
  .#checks.x86_64-linux.infra-monitoring-rules
nix build --no-write-lock-file --no-link \
  .#checks.x86_64-linux.vps-autostart-prometheus-rules \
  .#checks.x86_64-linux.process-count-prometheus-rules
```

## Concrete revision and acceptance

The common critical filesystem rule changes only its numerator selector by
adding `machine_type=~"vm|physical"`. The denominator, calculation, mountpoints,
threshold, hold, values, labels, annotations and name remain unchanged. JVB
exporter groups add literal `machine_type = "vps"`; their real inventory and
9100/9700 endpoints are unchanged. The alerter source is restored byte-for-byte
to the base, with its original five routes and severity-none blackhole.

The filesystem fixture consumes the production rules. Its full critical alert
and annotation expectations verify exact percentage values and labels. It tests
VM/physical positives and VPS/missing/empty/unknown/vmx negatives across infra,
nodes, mon and meet-jvbs; absent and unrecognized job positives; pending/firing
boundaries; selected root/run/nix-store and excluded mounts; above/equal/below
10% availability; device/fstype matching and multiple types/filesystems sharing
an instance; and a deliberately unmatched size metric. Negative types must have
no pending or firing criticals. VPS and missing-type warnings remain visible
across all four jobs, with their five-minute hold. The selected 20%/19% warning
boundary cases retained from R1 are present on distinct instances.

The config fixture retains all metadata, enum, label-precedence and shared
node/ZFS/IPMI checks. It now imports actual `data/meet.nix`, checks all generated
JVB groups and their exact existing labels/targets on both monitor fixtures,
and explicitly compares jvb1's two endpoints. Expected group coverage follows
the real inventory. Routing checks expect normal mail/Telegram/both-SMS for
synthetic critical/fatal alerts, including VPS/missing types/Meet, with warning
and none behavior preserved. These are receiver-selection tests with inert
transports, not live delivery or inhibition tests.

The monitoring page describes global eligibility, confirmed JVB classification,
missing types, warnings/fatal behavior, monitor label/rule rollout, mixed
versions and rollback. It contains no SMS-only policy or alerter-first step.
Its CPU policy section is unchanged. The existing Services index link and
flake check interfaces remain unchanged.

## Static evidence and preservation

Pinned Nixfmt formatting, Bash syntax and staged whitespace checks passed.
Executable active Overcommit pre-commit/commit-msg hooks were verified. Full
`bundle exec overcommit --run` passed Nixfmt and RuboCop (exit 0), using inherited
`os.environ` merged with `/tmp/infra-monitoring-realized-dev-env.json`; see
[static hook log](revised-static-checks.log). No hook was bypassed.
The corrected fixture also passed pinned Nixfmt check, Bash syntax, both
whitespace checks and the full active hook run (exit 0); see
[correction static log](revised-fixture-static-checks.log). Exact comparison
against the first staged tree proves only the two requested query replacements.

Exact byte comparisons establish:

- alerter/default.nix, infra/Meet rules, Meet data, flake.lock and Gemfile.lock
  match the base;
- metadata/VM modules, nodes.nix, CPU fixtures, flake.nix and mkdocs.yml match
  the accepted prior head;
- common.nix differs from the base only by the single critical selector;
- monitor/default.nix differs from the prior head only by the JVB label.

Thus warning/fatal, raw load-average, I/O wait, ZFS and all CPU policy source and
fixtures remain intact. No migration or persisted-format change is introduced.
Functional assertions are not yet reported as passed for this revision.

## History and next gate

The lead reports a fresh fetch with origin/master at the base, origin/feature
at the prior head, and the feature not merged into master. Only local/origin
feature refs contain the prior head; there is no PR in any state and no branch
CI run. No session release, deployment, integration or pin occurred. There are
no migrations. The lead established that the Git procedure permits rewriting
this unmerged development branch and will give the exact go-ahead after checks
pass, then push with a lease on the prior head. Implementation still awaits
that go-ahead.

After checks pass and the lead gives the provenance/rewrite go-ahead, consolidate
the first behavior commit around metadata/labels/global critical eligibility,
then retain the CPU behavior as the second commit with unchanged source and test
patch. Remove obsolete SMS history and adjust only overlapping policy prose.
Record exact final heads/tree, old/new comparison, hooks and no-migrations
conclusion in implementation-result.md. A revised all-lane whole-branch review
is required before full builds. Push and coordination remain lead-owned.

No push, master integration, input update, deployment, lifecycle operation or
cleanup occurred. Session remains open.
