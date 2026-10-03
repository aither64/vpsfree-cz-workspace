# API specs CI optimization proposal

Status: investigation and suggestions only, 2026-10-03. Architect: architect0.
No application edits, branch creation, new tests, CI runs, or deployment were
performed. The lead owns coordination records; this design has not been implemented.

## Recommendation and scope

The principal bottleneck is the partition of test execution. Prefer **13
duration-balanced file shards in each of the existing full/core modes**, keeping
26 test jobs. Collect file timings in the existing jobs first, then use a
deterministic, versioned allocation. This reuses capacity currently spent on
very short topics instead of adding many more runners. A **15–20 minute
execution target**, excluding unusual queueing, is plausible but unverified;
complete per-file timings, especially DNS and plugins, are still needed.

For the smallest initial change, divide `platform` into the three concrete
groups below. Their estimated RSpec times are about 13–14 minutes each. This
adds four jobs across both modes and should reduce the execution critical path
to roughly **23–25 minutes**, when runners start promptly. Other unsplit topics
then determine completion. Do not promise a 15-minute workflow from this change.

Both approaches preserve every selected spec, both plugin environments, every
example and assertion, existing metadata filters, failure reporting, and the
separate migration-spec workflow. Application behavior, fixture semantics,
cryptographic cost, schema loading, and test assertions are outside the initial
optimization. No test is removed merely because it is slow or normally pending
in one mode.

Readers are the maintainer choosing the approach and the later implementer.
This unimplemented proposal belongs in the session. If implemented, selector
and reproduction documentation belongs in vpsAdmin's testing guidance.

## Evidence and its limits

Source snapshot: canonical `repos/vpsadmin.git`, `origin/master` at
`148ef0eaed0459c825f1ba94b8dad2b9f3311b2f` (2026-10-03). Inspection used Git
objects, without opening another session's worktree or records.

Primary source files:

- [.github/workflows/api-specs.yml](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/.github/workflows/api-specs.yml)
- [api/spec/spec_helper.rb](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/api/spec/spec_helper.rb)
- [api/spec/support/db_setup.rb](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/api/spec/support/db_setup.rb)
- [tools/test_db.rb](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/tools/test_db.rb)
- [api/spec/support/spec_plugins.rb](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/api/spec/support/spec_plugins.rb)
- [docs/agent-instructions/testing.md](https://github.com/vpsfreecz/vpsadmin/blob/148ef0eaed0459c825f1ba94b8dad2b9f3311b2f/docs/agent-instructions/testing.md)

Historical evidence collected by the lead is in [workflow-runs.json](workflow-runs.json),
[workflow-runs-master.json](workflow-runs-master.json), and `jobs-*.json` in this
directory. Fourteen successful sampled runs comprise eight master runs from
September 13–17 and six storage-feature runs from September 25–October 2.
Master wall time has median 49.59 minutes (42.52–55.77); the feature sample has
median 43.19 minutes (40.67–47.40). These are different revisions, not a
controlled before/after experiment. October 3's additional run is not included
in those successful-run medians.

Representative recent evidence is [run 37030949457](https://github.com/vpsfreecz/vpsadmin/actions/runs/37030949457),
head `46b3bf6f9549eaf579053bc296ebf19c417bb848`. Its test jobs total about 315.8
runner-minutes: 176.3 full and 139.5 core. RSpec steps total 166.3 and 131.8
minutes respectively. With thirteen simultaneously available slots per mode,
perfect division would average 12.8 full / 10.1 core RSpec minutes per shard,
plus setup. This is an arithmetic bound, not an achieved runtime or proof of
available concurrency. Job bootstrap and repeated suite setup add cost.

Sampled master platform jobs waited as long as 12.73 minutes before starting;
recent feature platform jobs started in about 0.05 minutes. Queueing must be
reported separately from execution. A new partition cannot guarantee runner
availability and increasing job count may worsen scheduling delay.

### Existing partition

The workflow contains thirteen topics, expanded once with
`VPSADMIN_PLUGINS=all` and once with `none`, plus the topic-coverage job. It has
`fail-fast: false`, 45-minute test-job timeouts, and same-ref supersession
concurrency. There is no explicit `max-parallel`. Each test job installs
MariaDB dependencies, restores Bundler dependencies, boots its own API/test DB,
and runs one RSpec invocation over its sorted, deduplicated file list.

The source snapshot has 415 non-migration spec files, all assigned to exactly
one topic by the current patterns. File counts and fourteen-run medians are:

| Topic | Files at source snapshot | Full RSpec min | Core RSpec min |
| --- | ---: | ---: | ---: |
| smoke | 6 | 0.50 | 0.45 |
| coverage | 3 | 0.22 | 0.13 |
| routes | 4 | 0.85 | 0.82 |
| engine | 247 | 3.45 | 3.19 |
| plugins | 17 | 16.39 | 0.13 |
| supervisor | 18 | 0.35 | 0.32 |
| dns | 10 | 18.50 | 18.00 |
| storage | 12 | 14.03 | 14.07 |
| network | 10 | 15.06 | 13.19 |
| mail | 6 | 9.82 | 8.76 |
| users-auth | 18 | 21.91 | 19.57 |
| vps | 10 | 12.92 | 14.00 |
| platform | 54 | 41.08 | 36.53 |

Source file counts and historical timing revisions differ. In particular,
recent feature network RSpec takes approximately 24 minutes. Median full/core
platform *job* times are 41.58/37.14 minutes, so optimizations to apt or Bundler
alone cannot remove the long critical path. File-count sharding is especially
unsuitable: 247 engine files run much faster than ten DNS files.

The coverage job currently waits for `api-specs-full`, downloads its file-list
artifacts, and rejects missing, duplicate-across-topics, or untracked files.
Core uses the same YAML anchor but has no independently checked file manifests.
This is **file assignment coverage**, distinct from the `coverage` topic's API
endpoint/route manifest specs. No SimpleCov result-merging setup was found in
the inspected workflow and helper paths.

### What the timestamped logs establish

The existing documentation formatter emits timestamped top-level group names.
For an approximate group duration, take the interval from a group's heading to
the next top-level heading; stop at the pending/final summary. Match source
group names, including `API lifecycle bypass regressions` and plugin metrics,
and exclude warning/exception backtraces. Aggregate repeated headings. This
accounts for almost the complete RSpec runtime but does not measure each
example, precisely attribute suite hooks, or disambiguate files sharing a
heading. Treat these numbers as estimates, not formatter-derived file timings.

Relevant logs are [September 15 platform](job-104352128433.log),
[September 17 platform](job-105281554947.log),
[October 2 platform](job-110917326737.log),
[October 2 network](job-110917326822.log), and
[October 2 users/auth](job-110917326900.log).

The October 2 platform log has 968 examples, zero failures and five pending;
the September platform logs have 925 examples. The feature-only `StorageFreeze`
group contributes about 0.71 minutes and is separated from the source-snapshot
proposal below. It must be included if that feature is in the implementation
baseline; discovery must always use the actual checked-out revision.

Largest sampled platform groups map individually to
`node_kernel_evidence_spec.rb` (~3.38 min), `security_advisory_spec.rb` (~3.27),
`oom_report_spec.rb` (~2.84), `lifecycle_bypass_spec.rb` (~2.36), and
`migration_plan_spec.rb` (~2.33). Network's largest is
`ip_release_campaign_spec.rb` (~5.91), then `ip_address_spec.rb` (~3.47) and
`host_ip_address_spec.rb` (~2.98). Users/auth's largest is
`user_write_spec.rb` (~2.99), then `user_namespace_map_spec.rb` (~2.45).
`User` headings combine several files and cannot yet give separate weights.
Nothing in these sampled groups requires splitting an individual file for a
15-minute target. DNS, plugin and other unsampled individual-file maxima remain
unknown; collecting those weights is an explicit prerequisite to the stronger
target.

## Concrete static alternatives

### Minimal first change: platform into three topics

Keep every other topic unchanged. Replace the platform topic with the following
disjoint partition of its current files. Resource patterns below are relative
to `spec/api/resources/`; library patterns are relative to `api/`.

| Proposed topic | Membership | Sep 15 estimate | Sep 17 estimate | Oct 2 estimate |
| --- | --- | ---: | ---: | ---: |
| platform-infrastructure | `node_*_spec.rb`, `os_*_spec.rb`, `migration_plan_spec.rb` | 13.55 | 14.23 | 14.23 |
| platform-operations | `security_advisory*_spec.rb`, `oom_report*_spec.rb`, `incident_report_spec.rb`, `lifecycle_bypass_spec.rb`, `object_history_spec.rb`, `transaction*_spec.rb` | 13.52 | 14.25 | 14.05 |
| platform-config | `spec/lib/**/*_spec.rb`; resources `action_state`, `api_server`, `cluster*`, `component`, `debug`, `default_object_cluster_resource`, `environment_read`, `environment_write`, `language`, `location_read`, `location_write`, `metrics_access_token`, `system_config` (all ending `_spec.rb`) | 13.30 | 13.68 | 13.61 |

All times are estimated full-mode RSpec minutes; add setup and queueing.
The source membership is exhaustive for the 54 platform files. The future
implementation should retain explicit patterns and the coverage validator,
rather than silently assigning an unknown new resource to a catch-all domain.

This is fifteen topics/mode, thirty test jobs total. Retaining `platform` as
the config group's display name is possible, but does not preserve the old
check's assurance that all platform files passed; see the check-name migration
requirements below. Four extra job bootstraps are cheap in runner time in this
sample, yet queueing is not controlled. Expected next bottleneck: recent network
and users/auth, approximately 23–25 minutes. Existing DNS is another ~19-minute
floor even after those two topics are divided.

### Static rebalance while keeping thirteen topics per mode

Combine smoke, coverage, routes, engine and supervisor into one topic using
the union of their existing patterns: estimated full RSpec ~5.4 minutes and
core ~4.9 from sums of topic medians, before possible shared-boot savings or
order effects. Five old topics become one, freeing four slots. Spend two on
the three-way platform split, one on users/auth, one on network. This returns
to thirteen jobs/mode without changing any test content.

Concrete users/auth split:

- Authentication: `oauth2_client`, `password_change_log`, `webauthn`,
  `user_known_device`, `user_public_key`, `user_session`, `user_totp_device`,
  `user_webauthn_credential`, all with `_spec.rb`. October 2 group estimates
  sum to about 10.0 minutes.
- Accounts/resources: the remaining existing users-auth membership, about
  12.2 minutes. Expand to explicit patterns in implementation and validate the
  union instead of using an unchecked remainder.

Concrete network split:

- IP ownership: `ip_address*_spec.rb`, `ip_release*_spec.rb`; approximately
  11.0 minutes on October 2.
- Network topology: `network_*_spec.rb`, `network_interface*_spec.rb`,
  `host_ip_address_spec.rb`, `location_network_spec.rb`; approximately
  12.9 minutes. The intentional overlap within this topic must deduplicate
  before RSpec, as it does today.

This variant has a plausible ~19–21 minute execution floor from DNS (and
occasionally another topic). For a ~15-minute target, also divide DNS using
actual file durations; dividing plugins may be needed. Spending additional
slots or merging more topics should follow measured weights. Blindly assigning
half the DNS filenames to each side would not establish balance. The growing
special-case pattern maintenance is why timing-balanced shards are preferable
as the durable design.

Combining formerly separate topic processes can expose Ruby-global or
order-dependent interactions. This variant needs the same full-suite and
multi-seed checks as general sharding; exact-once file coverage alone is not
enough to validate it.

## Preferred durable design: thirteen duration-balanced file shards

### Selection and timing interfaces

Keep one fresh RSpec process and one isolated runner per shard/mode. Preserve
human-readable source topic labels as diagnostic metadata if useful, but
schedule whole files by observed duration. A generic `01`–`13` shard name
is preferable to calling a mixed-domain shard `smoke`.

Proposed interfaces and owning files, not edits made in this investigation:

| File/interface | Responsibility |
| --- | --- |
| `.github/workflows/api-specs.yml` | Existing triggers/concurrency; mode × shard matrix; per-shard selected/executed artifacts; coverage/failure gate. |
| `tools/api_spec_shards.rb` (proposed) | Enumerate eligible tracked files, validate timing data, deterministically allocate thirteen shards, print selection and estimated load. No API boot or database connection for allocation. |
| `api/spec/ci/file-durations.json` (proposed) | Versioned timing schema, per-mode file weights, source run/revision provenance, units and sampling rule. Data only; no paths to executable code. |
| `api/spec/support/ci_timing_formatter.rb` (if needed) | Opt-in formatter loaded explicitly by CI; emit file/example identity, result, seed and elapsed data without changing examples. Avoid unconditional side effects through the support-directory require loop. |
| `tests/api-spec-shards-test.rb` (proposed) | Allocation/coverage regression checks independent of booting the API. |
| `docs/agent-instructions/testing.md`, `AGENTS.md` | Replace manual topic-pattern instructions with exact-once shard requirements and local reproduction. |

If a new selector lives under `tools/`, add its exact path and timing/test paths
to the API workflow's push/PR filters. Otherwise a selector-only change may
never trigger the workflow it changes. Check interaction with the separate
integration selector; do not silently remove existing fallback coverage.

Collection should run within already-needed full tests; use RSpec's structured
results if they expose sufficient identity and timing, or a small explicit
formatter. No need for an extra full run just to time the suite. Keep the
existing human-readable failure output and exit status. Upload results even
on failure, but only complete valid runs should refresh timing weights.
Avoid a serial RSpec process per file: that would repeat schema loading and
plugin migrations hundreds of times.

The selection universe is the same tracked `spec/**/*_spec.rb` set used today,
with the same migration exclusion. Do not derive the universe from historical
timing entries. New files without a timing entry must always be selected.
Whole-file allocation keeps `before(:context)` and file-local definitions
together and avoids changing example inclusion by a new example-ID filter.

For each mode independently:

1. Sort files by descending estimated duration; break ties by normalized path.
2. Assign each to the currently least-loaded shard; break ties by shard ID.
3. Sort each resulting manifest by path before invoking RSpec.
4. Record the complete plan, source commit, mode, weight-data version and
   estimated load. Reject duplicate/missing files, path escapes, malformed
   timings, unexpected empty shards and incompatible schema versions.

This longest-first greedy allocation is simple and reproducible; no online
queue service or test execution distributor is required. Use a committed
snapshot of weights so a rerun of the same commit produces the same allocation.
Timing artifacts should inform a reviewed refresh, not silently change a
running branch's selection. Failed, fork-supplied, or partially uploaded
artifacts are not authoritative allocation data.

Estimate a file from several recent successful runs on comparable runners,
using a recorded median rule. Keep full and core weights separate: core plugin
examples are normally skipped while full plugin work takes ~16 minutes. Missing
weights get a documented nonzero conservative fallback (for example the median
of the same historical topic/mode, otherwise a global median); unknown files
must not be dropped or assigned zero cost. Stale records can be ignored for
allocation with a clear summary and removed on the next reviewed refresh.
Weights affect placement only, never membership or pass/fail behavior.

File example-time sums do not include all suite/context costs. Record both
actual shard elapsed time and the predicted sum; use the discrepancy and slowest
shard to judge the allocator. File-preserving shards cannot beat the largest
single file, so inspect the full distribution before claiming the target.

### Coverage and result gate

Keep `API specs - topic coverage` as a stable public check name if possible,
but deliberately define and document its stronger result contract. It should
wait for both mode matrices, run even when a dependency fails, require every
expected shard artifact, and validate exact-once file membership separately
for `full` and `core`. A successful manifest upload before RSpec is not evidence
that tests ran. A missing, cancelled, timed-out or failed shard must prevent a
successful aggregate result. Include revision/mode/shard identity in artifacts;
use unique names such as `rspec-files-full-01` and `rspec-results-core-01`.

Retain endpoint/custom-route coverage specs and their data files. The generator
spec file stays selected, with the existing `:generator` exclusion unless
`RUN_GENERATOR_SPECS=1`. Plugin-required and plugin-excluded examples keep their
existing skip semantics; do not prune the entire core plugins shard based on
its historical speed. Full/core allocations may differ while both cover the
same file universe.

For validation, compare baseline versus proposed *executed example identities
and outcomes per mode*, not just totals: equal totals can conceal one missing
and one duplicated example. Capture the same filters, environment, revision and
seed. Definitions can be influenced by loaded files, which is another reason
the file gate is necessary but not sufficient. Preserve the baseline's pending
set and demonstrate that no new skip was introduced to obtain a speedup.

## Isolation and implementation boundaries

- `SpecDbSetup.ensure_database_exists!` drops/recreates the configured database
  in test mode, then loads the core schema. Sharing one database between workers
  is unsafe even with transaction-wrapped examples. Some examples deliberately
  use `:no_transaction`.
- Without an explicit URL/config, `tools/test_db.rb` already creates a fresh
  temporary data directory and chooses a free TCP port for each independently
  started process, then stops/prunes that auto instance at process exit. The
  manually managed default database/port is not a parallel-worker namespace.
  The API helper does not automatically apply a worker-number DB suffix.
- `before(:suite)` initializes core seed data, boots the cached API app,
  migrates enabled plugins, bootstraps fixtures, and installs a transaction key.
  Every shard must retain that startup sequence for its mode. Do not cache a
  live DB or copy a partially migrated plugin state to save a few seconds.
- `SpecPlugins` selects one process-level plugin registry and installs skip
  hooks. Full and core must remain different process environments. Sharing an
  API application object cannot represent both modes safely.
- The suite mutates/caches application state: `User.current`,
  `UserSession.current`, PaperTrail context, transaction signer internals,
  `SpecSeed` cache and the cached Rack app. `GlobalReset` runs after examples.
  These are reasons to avoid thread-parallel examples and to test reshuffled
  file combinations under multiple random seeds.
- Preserve both file-manifest coverage and endpoint-manifest coverage. If
  line/branch coverage is later introduced, give each worker/mode unique result
  names and define merging separately; it is not part of this proposal.

Process-level parallelism on each existing runner is a later option, not a
necessary first step. Fresh exec workers can use the current per-process auto
DB behavior, provided no shared `DATABASE_URL` or database configuration is
inherited. Forking after boot would inherit connection/global state and the
auto-instance ownership; do not do that. A same-runner experiment also needs
worker-specific result/temp paths, resource limits, explicit exit aggregation,
owned-child cancellation and DB cleanup on failure. Free-port selection has a
bind/release/start window; simultaneous workers need that behavior evaluated.
More local workers compete for CPU, memory and MariaDB I/O; available cores and
memory were not established by this investigation. Measure a bounded two-worker
experiment before any larger setting. Job-level sharding already gives clean
OS/filesystem isolation and is the lower-complexity optimization here.

Authentication may contribute materially: the lead observed repeated real
Basic authentication and real bcrypt creation/matching. No profile establishes
what fraction of time it costs. Lowering test bcrypt cost, fixture caching,
mocking authentication, or altering authorization flows would change the
test environment and deserves a separate measured proposal with explicit
production-cost and authentication-coverage constraints. It is not assumed in
any estimate above.

## Compatibility, rollout and recovery

Production API contracts, generated clients, CLI/Terraform behavior, service
protocols, persisted formats, migrations, seeds and NixOS/vpsAdminOS deployment
configuration do not change. No production rollout ordering or coordinated node
update is needed. There are no new migrations and no rollback state-conversion
problem. Test databases remain disposable and isolated.

The changed compatibility surface is CI: topic/shard selection, logs, artifacts,
workflow path filters, reproduction commands and required status-check names.
Current test check names are `API specs (full) - <topic>` and
`API specs (core) - <topic>`, plus `API specs - topic coverage`. Required-check
settings and external consumers were not inspected by the architect. Before
implementation rollout, inventory rulesets/protection and any tools matching
these names. Do not rename/remove a required check or leave it covering only
part of its former tests. Preserve old aggregate names through explicit
compatibility gates if necessary, or coordinate migration to a stable aggregate
check that fails unless both complete matrices succeed. Never satisfy an old
check with a no-op success job.

Later rollout sequence: collect timings on the old partition; implement and
review selector/workflow changes; compare old/new partitions on the same code
revision and plugin environments; record correctness and timings; coordinate
check-name settings; only then adopt the new workflow through the normal
explicit integration process. This document does not authorize those actions.

Rollback is to restore the previous workflow/selector/timing configuration and
matching required-check settings. No application or database rollback is
needed. Keep the old reference manifests/results for diagnosis. If a changed
partition reveals a state-ordering failure, investigate and fix the isolation
problem; do not omit the test or accept a green rerun as the explanation.

## Acceptance criteria and verification plan

Completed investigation checks: session identity and required guidance;
read-only workflow/helper inspection; source-file inventory with no missing or
multiply assigned topics; timestamped group estimates; independent summation
of historical job/RSpec durations. No suite was executed and no speedup has
been measured on a proposed partition.

Quick checks for a later implementation:

- Use the repository Nix environment; syntax/style checks for touched Ruby,
  YAML/workflow validation and the declared hooks. Verify current upstream
  action refs before choosing or changing them.
- Assert deterministic allocation, exact-once membership in each mode, all
  thirteen expected manifests, no untracked/extra paths, migration exclusion,
  nonzero new-file fallback, and stable tie breaking.
- Exercise missing/duplicate files, stale/bad timing data, corrupt or absent
  artifacts, failed/cancelled shards and a selector-only workflow change.
  The aggregate check must fail in all incomplete execution cases.
- Check command construction preserves the full selected list in one RSpec
  invocation per shard; empty selection must fail rather than invoke RSpec's
  default discovery. Keep exit codes and readable failure output.
- Inventory complete branch history/final diff and state explicitly that no
  migrations or application runtime changes were introduced. Complete the
  mandatory independent change review after committed changes and quick checks,
  before long integration verification.

Longer checks, only in a later authorized implementation phase and launched/
monitored using the required fresh verification watcher:

- Run baseline and candidate partitions on the same revision and comparable
  runner class; compare complete file/example identities, failures and pending
  reasons in both plugin modes. Repeat representative reshuffled combinations
  with additional seeds to expose global/order dependencies.
- Compare at least several complete runs: queue delay, setup, suite boot,
  RSpec time, slowest shard, total job minutes, workflow critical path, and
  failure rate. Validate a cold dependency cache case as well as warm runs.
- For the thirteen-shard design, seek <=20 minutes per test job with ordinary
  runner availability, closer to15 if the measured heaviest file and runner
  capacity permit. Treat the target as unmet if it requires omitted examples,
  new pending tests, weaker assertions or lost plugin modes. Explain any
  material runner-minute increase rather than hiding it behind lower wall time.
- Preserve and verify the separate migration workflow. Production deployment
  and VM integration tests are not needed to demonstrate a pure API CI partition
  change unless its actual diff expands into runtime/integration selection.

The first implementation decision is between the minimal three-way platform
split (~23–25-minute execution target) and collection followed by balanced
thirteen-shard scheduling (~15–20-minute target). The latter has the better
capacity profile; the former is a smaller change with directly supported group
estimates. Neither target includes a guarantee against GitHub runner queueing.

Session: [API specs optimization](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-03-api-specs-optimization/).
