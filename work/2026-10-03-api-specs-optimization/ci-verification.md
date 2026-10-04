# Controlled API-spec workflow benchmark

2026-10-04. Instrumented original topics versus approved static 13 domains;
source/test/plugin/dependency inputs identical. Every run completed on its
explicit attempt1 before the next began. No retry or superseded cancellation.

| Run | Head | Wall minutes | Max test-job minutes | Maximum job start delay | Runner minutes |
| --- | --- | ---: | ---: | ---: | ---: |
| [Baseline](https://github.com/vpsfreecz/vpsadmin/actions/runs/37182100859) | 0412a349 | 41.03 | 40.85 (full platform) | 1.33 | 296.97 |
| [Candidate1](https://github.com/vpsfreecz/vpsadmin/actions/runs/37184185919) | 13b0e78f | 23.85 | 21.13 (full DNS) | 9.97 | 303.93 |
| [Candidate2](https://github.com/vpsfreecz/vpsadmin/actions/runs/37185470628) | 13b0e78f | 29.77 | 19.73 (core DNS) | 9.88 | 303.70 |

Wall includes queueing and controller/aggregate time (run created_at to
updated_at). Job time is started_at to completed_at, including setup/uploads.
Start delay is created_at to test-job started_at; it includes scheduling and
queueing, not only runner assignment. Aggregate's late start is excluded from
maximum test-job start delay. Runner minutes sum all27 jobs including aggregate.
Native RSpec/setup/step durations and per-topic records are in
[benchmark-summary.json](benchmark-summary.json).

Both candidates meet <=25-minute max test-job target. Observed wall reduction
was41.9% and27.5%. Candidate1's critical path was full platform-operations:
9.50-minute start delay +14.20-minute job. Candidate2's critical path was core
DNS:9.88-minute start delay +19.73-minute job. Queueing explains why its wall
time exceeds25 minutes despite every job executing faster than20 minutes.
Total runner use increased about2.3%; faster completion comes from balancing
the same test work, not reducing tests. These are two observed candidates,
not a controlled hardware or repository-wide timing distribution; future queue
and runner variation still matter.

## Coverage, outcomes and dependencies

All 81 jobs passed:26 test jobs plus stable aggregate in each of3runs. Each mode
has13 nonempty topic manifests and exact-once coverage of the same415 eligible
nonmigration spec files. Migration workflow and generator filters unchanged.
All 52 artifacts per run retained separately under local ci-evidence/ directories,
with explicit run/head/attempt provenance; raw bulk evidence is not committed.

[Native three-way comparison](example-parity.json) passed. Each mode executes
4,646 examples in each run; full has8pending, core 404 pending, with exactly equal
scoped IDs, definition paths, passed/pending statuses and pending reasons.
No failures, outside-example errors, missing/extra examples or duplicate IDs.
No new skips. Random seeds/order remain normal and are retained in the evidence.

Every job within each mode matches the effective dependency fingerprint:
Ruby 3.4.11 (592f1ffdb3), Bundler 2.6.9, RSpec 3.13.6. Full lock SHA256:
5463f1eb084cee89c16fca27d27e47d155da7375c27a4b82bfaacbda41644db2;
core:10486e712b9a25cfd5f9418e79af422a750702ec54bef3e53b08980b4cc0e4f4.
Mode locks intentionally differ. Source-input equality alone was not used as
proof; generated API locks are ignored/untracked, unlike the package lock.
The comparator checks example/dependency parity, while lead acceptance also
checked successful gates, source equality and measured job target.

## Review, history and adoption

[Independent full-branch review](implementation-review.md) passed all four lanes
with no findings before CI. Exact two functional commits remain at final
13b0e78f0932f280d77bef409fc6dc90237a5ca6, source base/origin master
f9beb46e5206864bca9d37672e1419cf03661467. Final fetch confirmed base unchanged;
source/index clean. No source edits after review and no migrations/obsolete
unmerged approaches. Saved portal comparison captures that exact base/head.

Ready, awaiting explicit vpsadmin/master merge approval. CI check-name mapping
is in design.md; aggregate name stays stable. Classic protection REST403 and
GraphQL FORBIDDEN prevent complete required-context inventory; empty rulesets
do not prove no protection. Resolve required checks before adoption; no settings
change or master integration was performed. No production deployment needed.
Session and branches remain open/retained.

## Execution notes

Parent monitored exact run IDs with bounded status checks, using the monitoring
skill's visible fallback because required native utility selection was absent.
All temporary commands completed, no unowned operation remains. First ambient
Git push failed Overcommit configuration signature validation; unchanged hook
source was rechecked, standard signing and push succeeded in declared Nix shell.
No bypass or source mutation from that failure. Setup/socket workarounds and
normal hook results are recorded in state.md and the linked setup lesson.
