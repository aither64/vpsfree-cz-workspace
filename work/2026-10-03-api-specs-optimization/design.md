# Static API specs rebalance: implementation design

Approved scope, 2026-10-04. Architect: architect0. This replaces the earlier
options paper with the implementer brief for [implementation-plan.md](implementation-plan.md).
Only static topics are selected. Weighted assignment, a new selector, custom
formatters and profiling infrastructure are out of scope.

## Scope and baseline

Keep thirteen topics in each of `VPSADMIN_PLUGINS=all` (full) and `none` (core):
26 independent test jobs and the stable aggregate check. Reuse the existing
anchored YAML matrix, shell pattern expansion and sorted/deduplicated manifests.
Preserve every spec, example, assertion, metadata filter, plugin skip and
randomized order. No spec moves or runtime/authentication/schema changes.

Owned worktree: `worktrees/2026-10-03-api-specs-optimization/vpsadmin`, initially
at `f9beb46e5206864bca9d37672e1419cf03661467`. This includes the upstream SSO
closure changes and **60-minute** topic timeouts; preserve both. Historical
measurements used older code and cannot serve as the implementation baseline.
Fresh enumeration still finds 415 eligible files, but that count is evidence,
not a constant for the implementation.

Retain current workflow name, triggers, permissions, same-ref supersession,
`fail-fast: false`, runner type, Ruby-series selection and Bundler settings.
No default-branch integration is authorized by the implementation request.

## Selected static map

All resource entries below mean `spec/api/resources/<entry>_spec.rb`. Explicit
`spec/...` paths are relative to `api/`. Each row is one topic in both modes.
Keep the five unchanged domains' original patterns verbatim.

| Topic | Patterns or resource entries |
| --- | --- |
| `foundation` | `spec/smoke/**/*_spec.rb`; `spec/api/custom_routes_coverage_spec.rb`; `spec/api/endpoint_coverage_spec.rb`; `spec/api/generate_pending_endpoints_spec.rb`; `spec/api/routes/**/*_spec.rb`; `spec/models/**/*_spec.rb`; `spec/supervisor/**/*_spec.rb` |
| `plugins` | `spec/api/plugins/**/*_spec.rb` (unchanged) |
| `dns` | `dns*` (unchanged) |
| `storage` | `dataset_*`, `environment_dataset_*`, `pool_*`, `snapshot_download`, `export` (unchanged) |
| `mail` | `mail*`, `mailbox`, `user_mail_*` (unchanged) |
| `vps` | `vps_*` (unchanged) |
| `platform-infrastructure` | `node_*`, `os_*`, `migration_plan` |
| `platform-operations` | `security_advisory*`, `oom_report*`, `incident_report`, `lifecycle_bypass`, `object_history`, `transaction*` |
| `platform-config` | `spec/lib/**/*_spec.rb`; `action_state`, `api_server`, `cluster*`, `component`, `debug`, `default_object_cluster_resource`, `environment_read`, `environment_write`, `language`, `location_read`, `location_write`, `metrics_access_token`, `system_config` |
| `auth` | `oauth2_client`, `password_change_log`, `webauthn`, `user_known_device`, `user_public_key`, `user_session`, `user_totp_device`, `user_webauthn_credential` |
| `users` | `user_cluster_resource*`, `user_environment_config`, `user_namespace*`, `user_read`, `user_state_log`, `user_touch`, `user_available_ips`, `user_write` |
| `ip-ownership` | `ip_address*`, `ip_release*` |
| `network` | `network_*`, `network_interface*`, `host_ip_address`, `location_network` |

This combines five short topics into foundation, using the four freed slots
for platform in three parts, users/auth in two, and network/IP in two. The
existing overlapping patterns within mail/network remain deduplicated inside
one topic; a file must never occur in two topic manifests. New files must be
placed explicitly or fail coverage; no catch-all domain is introduced.

Historical full-mode estimates for the three platform groups were roughly
13.3–14.3 minutes each. Auth/users were about 10.0/12.2 minutes; IP/network about
11.0/12.9; combined foundation about 5–6. DNS (~19 minutes) becomes a likely
critical path. These estimates come from older timestamped logs and are
**unvalidated for the new partition**. Target <=25 minutes for the slowest test
job in each of two candidate runs, recording queueing separately. Evidence and
method limitations remain in [investigation.md](investigation.md) and
[timing-summary.json](timing-summary.json).

## Two commits and changed interfaces

**Commit 1: evidence and aggregate correctness.** Keep the original thirteen
topics. Add RSpec native JSON alongside current readable output, seven-day
mode-qualified manifest/result artifacts, and the stronger aggregate check.
This is the instrumented baseline and a useful independent change.

**Commit 2: partition and placement guidance.** Apply the map above; update
`docs/agent-instructions/testing.md` and `AGENTS.md` with placement, artifact,
aggregate and local reproduction requirements. Keep commit 1's instrumentation
and gate unchanged except for the expected topic names.

The primary implementation stays in `.github/workflows/api-specs.yml`; keep
bounded validation in its existing steps. Small fixture-based verification of
those steps is appropriate, but no generic selection framework is needed.
Avoid changes to `api/.rspec`, API support helpers, gems, package locks or test
contents. Use workflow command options for the extra formatter. Verify imported
actions against their current official releases before choosing refs; any
necessary action change belongs in commit 1 so both benchmark snapshots match.

## Manifest, result and aggregate contract

1. Keep `set -euo pipefail`, `nullglob` and `globstar`. Expand the topic patterns,
   sort/deduplicate, and reject an empty list before RSpec. Pass the complete
   manifest to one RSpec process; an empty list must never cause default suite
   discovery. Do not silently split the invocation into multiple processes
   that overwrite the same JSON output.
2. Upload a manifest from **both modes** before setup/testing, using
   `if: always()`, `if-no-files-found: error`, and `retention-days: 7`.
   Canonical names: artifact `rspec-files-<mode>-<topic>`, file
   `api/tmp/rspec-files-<mode>-<topic>.txt`, containing paths relative to `api/`.
3. Add native JSON output to `api/tmp/rspec-results-<mode>-<topic>.json`, preserving
   the documentation formatter on stdout and RSpec's nonzero failure status.
   Upload as `rspec-results-<mode>-<topic>` with the same seven-day policy and
   `if: always()`. Missing JSON after boot failure or timeout is an incomplete
   result, never a passing run. An upload step must not hide the RSpec failure.
4. Keep job ID `api-spec-topic-coverage` and display name
   **`API specs - topic coverage`**. Set dependencies to both full/core matrices
   and run with `if: always()`. Require each dependency's result to be exactly
   `success`; failed, cancelled, skipped or timed-out work must not turn into a
   green aggregate because its early file manifest exists. Keep coverage
   diagnostics available on failed runs where practical, then fail the gate.
5. Determine expected topic names from trusted workflow configuration, not
   downloaded filenames. A small explicit expected-name list in the gate is
   sufficient; verify it equals the anchored matrix in quick checks and update
   both atomically. Require thirteen distinct configured names and **exactly
   those thirteen nonempty manifests for each mode**. Reject wrong-mode,
   unknown-topic, duplicate-topic or nested unexpected manifest files. Keep
   artifact directories distinct so duplicate filenames cannot overwrite and
   disappear during download.
6. Derive the eligible universe at the tested checkout with the existing
   `git -C api ls-files 'spec/**/*_spec.rb' ':!spec/migrations/*_spec.rb'` rule.
   For each mode independently, reject duplicate paths, missing eligible paths
   and extra/untracked paths. Compare the complete file sets; no hardcoded
   count. Do not pool full/core manifests before duplicate detection. Since
   both modes share the matrix, their per-topic file lists must also agree.
7. JSON upload success is part of test-job success. The aggregate gate need
   not parse all JSON to prove file partition correctness; executed-example
   parity is a separate benchmark acceptance check below. File manifests alone
   never prove that examples completed.

Retain endpoint/custom-route coverage specs in foundation. The generator file
stays selected with existing `:generator` exclusion unless
`RUN_GENERATOR_SPECS=1`. Plugin-required/excluded pending behavior remains as-is,
including core's mostly pending plugins topic. Migration specs continue through
their separate workflow and are excluded exactly as today.

Artifacts identify mode/topic by name and run/SHA/attempt through the workflow
artifact provenance. Download comparison evidence by explicit run and attempt;
never merge arbitrary latest artifacts or successful pieces from different
attempts into a synthetic passing run. Capture Ruby/Bundler/RSpec versions and
the effective generated lockfile or its fingerprint with each job's evidence.
Do not dump environment variables or credentials.

## JSON comparison rules

Use the native formatter's `examples`, `id`, `file_path`, `status`,
`pending_message`, `summary` and `seed` fields; confirm these against the
resolved RSpec version. The [upstream native JSON formatter](https://github.com/rspec/rspec-core/blob/main/lib/rspec/core/formatters/json_formatter.rb)
provides these identities and outcomes without custom instrumentation.

For each mode independently, compare the baseline and both candidate runs:

- Require thirteen complete parseable result files matched to the expected
  topics, internally consistent summaries, and zero failed examples or errors
  outside examples. Reject unknown result statuses and duplicate example IDs
  before turning the rows into a mapping.
- Normalize the harmless leading `./` on repository-relative paths. Preserve
  each RSpec ID's full scoped suffix, not only the file/line or description.
  Require equal sets of `(mode, normalized example ID)` and consistent file
  paths. Changed topic membership must not enter the identity key.
- For every identity, require identical passed/pending status and the same
  pending reason. Fail on missing/extra IDs, passed-to-pending changes or new
  skip reasons. Compare per-file counts as an additional diagnostic, not as a
  substitute for identity equality. Preserve descriptions for diagnosis.
- Ignore runtime, output order, seed and exception backtrace path differences
  in the equality key. Retain those fields as evidence. Do not normalize away
  substantive pending-reason differences. Different seeds are intentional;
  investigate discrepancies rather than weakening the comparator.

Filtered generator examples need not appear in JSON: the selected-file gate
preserves their placement, while equal effective filters preserve execution.
Files containing no selected examples are not required to invent a JSON row.
Do not require every manifest entry to have a passed example.

## Same-code benchmark and review sequence

1. Implement and commit both changes, run quick checks/hooks, and have retained
   reviewer0 independently review the complete two-commit history/final diff.
   Explicitly record no migrations, no removed test behavior and the check-name
   implications. The two functional commits are intentional, not superseded
   approaches to squash before the controlled comparison.
2. Push **only commit 1** to this session's feature branch. Run and retain the
   complete old-topic full/core baseline, JSON, manifests, versions and job/step
   metadata. Wait for completion and capture evidence before advancing the same
   branch, since its concurrency policy cancels superseded runs.
3. Push commit 2 to that branch, then run the candidate twice on the same head.
   Preserve normal random ordering and record every job's seed. Do not overlap
   the two same-ref runs in a way that cancels one. If a run fails, inspect its
   original logs/artifacts and diagnose before any retry.
4. Prove application/test/plugin code and dependency inputs are identical
   between commits 1 and 2. The allowed differences are static workflow
   membership/expected names and placement documentation. Compare resolved
   dependencies too: `api/Gemfile.lock` is ignored/generated, whereas the tracked
   package lock is `packages/api/Gemfile.lock`; the current CI does not directly
   use that package lock. Matching repository inputs alone is insufficient.
   Compare effective gem-lock fingerprints within each mode across baseline
   and candidates, plus Ruby/Bundler versions. If resolution drifts, report it
   through the lead and align dependencies before claiming a same-code
   performance comparison; do not introduce a new pinning system unilaterally.
5. Require the JSON parity above, all 26 jobs plus aggregate successful, and
   slowest candidate job <=25 minutes in both runs. Record queue delay, setup,
   RSpec duration, total workflow wall time and runner-minutes separately.
   A queued workflow may exceed 25 minutes even when the execution target is
   met; report both rather than obscuring queueing.

Long CI operations belong to fresh policy-selected Luna/low watchers arranged
by the lead. The architect does not launch CI. Keep failed evidence and do not
call a missing/incomplete baseline a successful benchmark. VM integration or
production deployment is unnecessary for this workflow-only change unless its
actual scope expands.

## Invariants, compatibility and recovery

Each runner retains its own RSpec process, temporary MariaDB data directory and
port, schema reset, application/plugin bootstrap and suite seed. Transaction
rollback is not enough to share a database: test startup drops/recreates it,
and some examples use `:no_transaction`. Full/core keep separate plugin
registries. No threaded examples or extra processes per runner are introduced.
Merging short topics can expose global/order dependencies; native JSON parity
and two randomized candidate runs are the required evidence against that risk.

No API/client/CLI/Terraform contracts, service protocols, persisted formats,
production DB migrations/seeds, NixOS/vpsAdminOS settings or node deployment
ordering change. No coordinated machine update is required. Production rollback
has no data compatibility implications.

CI check and artifact names are the compatibility surface. Unchanged topic
contexts are plugins, DNS, storage, mail and VPS. Network keeps its name but
covers a smaller set; its old meaning is restored only by also requiring the
new IP topic or the aggregate. Old smoke/coverage/routes/engine/supervisor map
to foundation; users-auth maps to auth+users; platform maps to its three new
names. Apply this mapping for both `API specs (full) - <topic>` and
`API specs (core) - <topic>`. Preserve workflow name and the stable aggregate.
Mode-qualified artifact names intentionally replace old unqualified manifests;
update consumers and reproduction guidance in the same change.

Classic master protection lookup previously returned 403, so required contexts
are not established. The lead must inventory rulesets/protection and consumers
before adoption. Document the exact mapping above if access remains unavailable;
never assume absence of protection or add no-op compatibility successes.
Implementing/pushing the feature does not authorize changing protection or
integrating into master.

Rollback restores the old topic matrix and corresponding expected-name/check
settings; commit 1's instrumentation/stronger gate can remain. If rolling back
all workflow changes, also restore old artifact consumers. No production DB
rollback is involved. Keep branch refs and session open. Route changes to the
partition, test semantics, dependency strategy or aggregate contract through
the lead before expanding implementation.

## Quick checks and completion criteria

Use the project Nix shell, declared hooks, workflow/YAML/shell validation and
appropriate Ruby lint only for any touched Ruby. Verify current action refs.
Quick checks must expand the actual old/new patterns and prove identical tracked
file universes, thirteen expected nonempty topics per mode and disjoint exact
coverage. Exercise the actual gate's missing, extra, duplicate, empty,
wrong-mode/topic and incomplete-manifest cases, plus success/failure/cancellation
matrix results; every incomplete case must fail. Check JSON malformed/missing,
duplicate-ID and changed pending/outcome fixtures for the comparison procedure.
Verify that readable RSpec output and exit status survive JSON/artifact handling.

Definition of done: two reviewed functional commits; passing quick checks/hooks;
one complete same-code baseline plus two successful candidate runs; exact
file/example/outcome parity in each mode; measured <=25-minute candidate job
maximum or an explicit unmet-target report; CI context migration documented;
no runtime/test reductions or migrations. Delivery remains on the feature
branch pending explicit vpsadmin/master integration direction.

Brief validation: fresh source/guidance inspected and 415-file old-topic
coverage recomputed; no application edits, tests, CI or commits by architect0.
Lead owns tracking/portal updates and implementation/review/verification handoff.
[Session](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-api-specs-optimization/).
