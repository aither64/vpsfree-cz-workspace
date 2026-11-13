# vpsAdmin migration metadata assertions (F0)

Owner: implementer3. Investigated 2026-11-13 UTC from current remote metadata,
immutable GitHub content and the canonical bare clone. The verified session,
both environment markers and thread binding agree. Retained settings remain
GPT-6.1 Sol/xhigh with workspace-write role access and full execution access.

## Finding and selected repair

The weekly migration suite compares raw MySQL column metadata against typed
Ruby defaults. Correct eleven expectations across nine existing spec files to
the adapter's string defaults: `eq('0')` or `eq('1')`. Architect0 selected this
direction in current-package clarification. Keep `column()` returning the raw
column object, preserve type/nullability/unsigned checks and all data/rollback
examples, and leave migrations unchanged. Implementation awaits architect0's
sufficient F1 brief and lead release.

## Exact source and failed attempt

- Repository: `git@github.com:vpsfreecz/vpsadmin.git`; default `master`.
- Current remote snapshot: `6f71da9777edfc902f6483edcdd84a2ef7d464ab`, observed
  through `gh api repos/vpsfreecz/vpsadmin/commits/master`, then fetched over SSH
  into canonical `repos/vpsadmin.git` as `refs/remotes/origin/master`.
- [Failed scheduled run 42610017068](https://github.com/vpsfreecz/vpsadmin/actions/runs/42610017068),
  attempt 1, created 2026-11-09T11:33:43Z, head
  `e5e39bf380ebbb469d201f92d62434cd6ebca230`; job `API migration specs`
  (`129135732595`). Read with `gh run view ... --log-failed` before any retry.
- Runtime evidence: ActiveRecord `8.1.4.1`, MariaDB Ubuntu package
  `1:11.8.6-5ubuntu0.1`; 84 examples, 9 failures, 5.08 seconds of example time.
  Every reported failure is a default-value type mismatch (`"0"` versus
  `false`/`0`, or `"1"` versus `true`). The logs contain no migration execution
  exception establishing a schema repair requirement.
- Helper, migration specs and migration workflow have no diff between the failed
  head and the current remote snapshot. D0 records the preceding two weekly
  schedules failing as well; F0 has not independently diagnosed those attempts.
- Raw downloaded log is disposable `/tmp/f0-run42610017068.log`. This Markdown
  retains the consequential evidence; it does not depend on the log surviving.

## Adapter contract

The current [migration helper](https://github.com/vpsfreecz/vpsadmin/blob/6f71da9777edfc902f6483edcdd84a2ef7d464ab/api/spec/migration_helper.rb)
returns `connection.columns(table).find { |v| v.name == column.to_s }` unchanged.
In the exact [Rails 8.1.4.1 MySQL adapter](https://github.com/rails/rails/blob/v8.1.4.1/activerecord/lib/active_record/connection_adapters/mysql/schema_statements.rb),
`new_column_from_field` takes the default from the database field metadata and
passes it to `MySQL::Column`. The [Column initializer](https://github.com/rails/rails/blob/v8.1.4.1/activerecord/lib/active_record/connection_adapters/column.rb)
stores it unchanged. Its general constructor comment describing a type-cast
default does not match this numeric/boolean MySQL path; the implementation and
failed-run objects directly establish the actual contract.

Typed model defaults are a later operation: [Rails attributes](https://github.com/rails/rails/blob/v8.1.4.1/activerecord/lib/active_record/attributes.rb)
construct defaults with `ActiveModel::Attribute.from_database` and the column's
cast type. A separately named helper explicitly deserializing a default could
test that semantic contract, but is unnecessary for these raw-metadata specs.
Changing `column()` itself would disguise its adapter semantics. Generic `to_i`
or boolean coercion would also weaken detection of incorrect raw values.

All corresponding migration definitions specify the intended false/zero/true
defaults. No evidence requires changing any migration, production schema,
application, model or generated client.

## Complete expectation inventory

Paths below are relative to `api/spec/migrations/` at the current remote snapshot.
The nine failures expose eleven assertions: the capacity example stops at
`cpus`, leaving two later equivalent mismatches unexecuted.

| Spec file | Column(s) | Current expectation | Correct raw default | Assertions |
| --- | --- | --- | --- | --- |
| `20260707140000_add_sysconfig_localized_spec.rb` | `sysconfig.localized` | `be(false)` | `'0'` | 1 |
| `20260713120100_add_node_kernel_history_spec.rb` | `node_kernel_events.current` | `be(false)` | `'0'` | 1 |
| `20260713120200_add_node_kernel_evidence_spec.rb` | `node_software_versions.revision_dirty` | `be(false)` | `'0'` | 1 |
| `20260716120000_add_node_system_states_spec.rb` | `node_system_states.current` | `be(false)` | `'0'` | 1 |
| `20260716120100_make_node_capacity_reported_spec.rb` | `nodes.cpus`, `nodes.total_memory`, `nodes.total_swap` | `eq(0)` each | `'0'` each | 3 |
| `20260818115900_add_authentication_generation_spec.rb` | `users.authentication_generation` | `have_attributes(default: 0, ...)` | `'0'` | 1 |
| `20260818120000_add_password_recovery_spec.rb` | `oauth2_clients.authorization_start_requires_user_action` | `have_attributes(default: false, ...)` | `'0'` | 1 |
| `20260821120000_add_password_event_counters_spec.rb` | `password_event_counters.event_count` | `have_attributes(default: 0, ...)` | `'0'` | 1 |
| `20260909170000_add_ip_release_campaigns_spec.rb` | `ip_release_campaigns.allow_keep` | `be(true)` | `'1'` | 1 |

Existing nil-default assertions remain correct. The content-revision spec already
uses `revision.default.to_i`; expanding this package to change it is unnecessary.

## Proposed checks after release (not executed)

The repository development procedure supplies `nix develop .#api`, which enters
`api/`; its automatic isolated MariaDB setup supports local RSpec. Select core
mode with `VPSADMIN_PLUGINS=none`. The migration workflow deliberately uses
`--options /dev/null` so ordinary API RSpec options do not alter this suite.
Inside that shell, the narrow failing-file batch is:

```bash
bundle exec rspec --options /dev/null --format documentation \
  spec/migrations/20260707140000_add_sysconfig_localized_spec.rb \
  spec/migrations/20260713120100_add_node_kernel_history_spec.rb \
  spec/migrations/20260713120200_add_node_kernel_evidence_spec.rb \
  spec/migrations/20260716120000_add_node_system_states_spec.rb \
  spec/migrations/20260716120100_make_node_capacity_reported_spec.rb \
  spec/migrations/20260818115900_add_authentication_generation_spec.rb \
  spec/migrations/20260818120000_add_password_recovery_spec.rb \
  spec/migrations/20260821120000_add_password_event_counters_spec.rb \
  spec/migrations/20260909170000_add_ip_release_campaigns_spec.rb
```

Run the repository's required RuboCop and normal hooks before committing. A full
migration batch is `bundle exec rspec --options /dev/null --format documentation
spec/migrations/*_spec.rb` inside the same shell. No new test subsystem or machine
integration scenario is needed. Uncertain shell/bootstrap or longer checks must
use the monitor skill; actual execution remains gated by the lead's assignment.

## Delivery boundary and compatibility

F0 investigation is ready for acceptance. No feature branch, source edit, build,
test/rerun, PR, default-branch mutation or deployment was performed. Fetching the
canonical bare ref and writing this evidence are the only local changes made by
F0. No other session's worktree was accessed. Lead retains plan/state/portal and
tracking-commit ownership.

F1 should change test expectations only. No persisted format, migration lineage,
runtime API/client contract, rolling deployment ordering or rollback behavior is
affected. No client regeneration or machine rollout is required for a test-only
diff. All original migrations remain intact. A brief helper comment explaining
raw metadata is optional if architect0 includes it; otherwise these source-linked
session findings are sufficient documentation. Lead owns acceptance and final
independent review after committed changes and quick checks.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-scheduled-workflow-fixes/)
