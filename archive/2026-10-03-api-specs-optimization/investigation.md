# API specs timing investigation

Request: preserve every existing vpsAdmin API spec while reducing the 40+
minute feedback cycle. This report is investigation only; no workflow or test
changes have been implemented, no new CI runs launched, and nothing deployed.

## Evidence and sampling

Inspected canonical vpsAdmin origin/master at
`148ef0eaed0459c825f1ba94b8dad2b9f3311b2f` (fetched 2026-10-03).
Read `.github/workflows/api-specs.yml`, `api/.rspec`, spec setup/support,
`AGENTS.md`, and `docs/agent-instructions/testing.md`.

Queried GitHub's Actions API for the latest 50 workflow runs and separately
20 master runs. Downloaded job/step metadata for 14 successful runs: the latest
8 successful master runs (September 13–17), and 6 recent successful
storage-redesign branch runs (September 25–October 2). This is a representative
sample across revisions, not a controlled benchmark or a random sample of all
branches. One October 3 failed run was inspected separately and excluded from
success medians. Canceled runs and the currently running/rerun workflow were
excluded. No Actions state was modified.

Compute wall time from workflow creation to the last job's completed_at,
including queueing and the coverage gate. Job time is started_at to completed_at;
RSpec time uses the Run RSpec (topic) step. Avoid workflow updated_at as an
end-time proxy, especially on reruns. Local reproducible metadata lives in
workflow-runs*.json, jobs-*.json and timing-summary.json.

| Successful cohort | Runs | Wall median | Wall range | Full platform job median | Full platform RSpec median | Full platform start delay median |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| master, September 13–17 | 8 | 49.59 min | 42.52–55.77 min | 41.35 min | 40.85 min | 8.42 min |
| storage branch, September 25–October 2 | 6 | 43.19 min | 40.67–47.40 min | 42.71 min | 42.21 min | 0.05 min |

Representative runs:

- [Latest sampled master run](https://github.com/vpsfreecz/vpsadmin/actions/runs/35244637812): wall 55.77 min; full platform started 12.73 min after creation, ran 42.85 min (RSpec 42.30 min).
- [October 2 successful feature run](https://github.com/vpsfreecz/vpsadmin/actions/runs/37030949457): wall 43.48 min; full platform ran 43.25 min (RSpec 42.77 min).
- [October 1 successful feature run](https://github.com/vpsfreecz/vpsadmin/actions/runs/36925295017): wall 47.40 min; full platform ran 44.40 min.

## What determines the finish time

Already parallel: 13 topics run under both VPSADMIN_PLUGINS=all and none,
for 26 independent Ubuntu runners, plus a final topic-coverage job.
Both modes use the same anchored topic patterns. RSpec is sequential within a
job; order is randomized. Fail-fast is disabled. Each topic has a 45-minute
job timeout.

Across the 14 successful runs, median durations are:

| Topic job | Median |
| --- | ---: |
| full platform | 41.58 min |
| core platform | 37.14 min |
| full users-auth | 22.38 min |
| core users-auth | 20.03 min |
| full DNS | 19.07 min |
| core DNS | 18.56 min |
| full plugins | 17.07 min |
| full network | 15.80 min (recent branch runs reach 24.50 min) |
| full storage | 14.61 min |
| full VPS | 14.27 min |
| full engine | 3.97 min |
| full routes | 1.43 min |
| full smoke | 1.07 min |
| full supervisor | 0.88 min |
| full coverage | 0.74 min |

The platform topic wins the critical path in every successful sampled run.
Typical platform setup and teardown combined cost about half a minute; reducing
apt or Bundler setup alone cannot produce the desired improvement. The
separate coverage gate usually costs seconds after the slowest full topic.

Platform includes all spec/lib files plus many unrelated request resources:
nodes, clusters, environments, locations, transactions, alerts, histories,
OS families/templates, configuration and more. Logs show many moderate groups,
rather than a single group consuming the entire 42 minutes. Timestamp-derived
group durations are approximate and may include neighboring hook/log overhead;
use per-file RSpec timing output for accurate balancing in implementation.

The October 2 run spent 166.33 RSpec minutes in full mode and 131.78 in core
mode. Perfectly spreading those across the existing 13 jobs per mode yields
12.79 and 10.14 minutes before setup, boot repetition, imbalance and queueing.
This is a mathematical lower bound under unconstrained scheduling, not a
predicted achieved time. Total observed runner time was about 316 minutes
(median across the six feature runs); a split changes wall time primarily,
with some added boot/setup work.

## Parallelization constraints

Independent runner jobs are the simplest isolation boundary. The spec helper
resets the test database and loads schema at process start, boots the singleton
Rack app, migrates enabled plugins, seeds data, and generates a transaction key.
An around hook rolls ordinary examples back; some examples opt out. There is
mutable global user/session/signer/seed state. Concurrent Ruby threads sharing
this environment are unsuitable. Separate processes on one runner need
verified independent DB/socket/data/tmp state rather than simply starting two
RSpec commands against the existing connection.

The existing coverage gate validates selected file manifests from full mode
only, with identical patterns reused for core. Preserve the exact-once invariant
per mode, the generator exclusion, intentional core plugin skips, and the
separate migration workflow. Do not implement speed through dropped tests or
changed path filters. Renamed check contexts need a branch-protection audit.

Master job starts were materially delayed; recent feature runs generally
started promptly. Organization concurrency, other workloads, or runner supply
are possible causes; metadata alone does not identify the exact cause or the
organization's plan. GitHub documents plan-dependent shared concurrency limits:
[Actions limits](https://docs.github.com/en/actions/reference/limits).
Adding more topics indefinitely will not remove queueing.

## Candidate solutions

1. **Minimal first change:** split platform into three approximately balanced
   file groups in both modes. Keep all other topics. This raises topic runners
   from 26 to 30 and plausibly shifts the critical path to users-auth/network,
   around 23–25 minutes plus queueing. The exact split belongs in design.md;
   estimates need a complete run before acceptance.
2. **Further improvement:** split or rebalance users-auth, network and DNS too,
   targeting 12–15 minutes of work in the largest partition. A roughly 15–20
   minute total target is plausible with adequate runner capacity; it is not
   measured yet.
3. **Rebalance without increasing runner count:** combine smoke, coverage,
   routes, engine and supervisor into one small topic (about 6 minutes in full
   mode), freeing four slots. Use two for splitting platform three ways, one
   for users-auth two ways, and one for network two ways. Keep 13 jobs/mode;
   DNS/plugins then impose an approximately 18–22 minute execution floor.
   This is a simple static alternative to generic shards and preserves domain
   labels. Keep coverage validation independent of test success.
4. **Duration-balanced file shards:** collect per-file durations and rebalance
   the existing roughly 13 slots per mode, mixing small meta/lib groups with
   larger resource groups or using a checked-in deterministic weighted file
   allocation. This better uses existing idle slots but changes naming and
   selection more substantially. New files must be included automatically or
   fail closed, and missing/stale timing weights must never omit files.

Start with job partitioning, keep real authentication/test semantics, retain
full/core modes, and expose timings for subsequent balancing. Existing real
bcrypt password verification on basic-auth requests is a possible aggregate
CPU cost, but it was not profiled here. Lower test-only crypto cost is a
separate optional investigation, not part of the coverage-preserving first
recommendation.

## Validation before calling an implementation ready

- Statically compare tracked non-migration spec files with partition manifests:
  each file exactly once in each mode; reject duplicate, extra, missing and
  unexpectedly empty partitions.
- Preserve existing effective filters and the generator/migration contracts.
- Run full and core on the same revision; compare example IDs or counts per
  file and mode (including expected pending examples), not just file lists.
- Capture RSpec timings, setup cost, queue delay and total wall time. Compare
  repeated complete runs to a baseline; account for randomized order and runner
  variability. Keep failures from every shard visible with fail-fast disabled.
- Review changed CI logic under the mandatory change review workflow before
  long verification. Use a fresh session-policy watcher for long runs.
- Check required status contexts before rollout; rollback is restoring the
  previous workflow partition. No API/schema/production rollout is involved.

## Collection notes

`gh api .../actions/jobs/ID/logs` initially refused ANSI escape sequences.
Read-only retry with `--allow-escape-sequences` succeeded; downloaded logs were
kept in files and only selected sanitized lines inspected. No suite rerun was
used as a substitute for investigating historical runs.
