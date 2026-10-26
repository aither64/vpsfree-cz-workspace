# Controlled benchmark launch handoff

Executed once under the lead's verification utility after independent review.
All 24 runs passed for the exact d209..0fd31 pair below; final results are in
performance-results.md. This retained launch recipe is historical, not a routine
test/CI gate. Owned temporary exports/binaries were removed after hash and idle
checks; committed fixtures and raw result logs remain. Final deployed runtime is
fffbd0d5, a reviewed successor; no matrix rerun was performed for later refreshes.

Method: `dev-workspace/docs/cpu-benchmark.md`. Fixture source files are
`portal/internal/web/cpu_benchmark_test.go` and `test/support/cpu_fixture.rb`.
The native Codex daemon, model service and activity observer connection are
excluded; actual helper subprocesses are included in whole-cgroup CPU.

## Quick evidence

Inside the runtime Nix shell, Ruby syntax and opt-in fixture validation passed
with one root/member and a valid 3,145,879-byte ledger. Validation includes a
full retry admission, status read, real candidate coordinator pass, and one due
notification delivered through its synthetic native subprocess.
The validation took 4.73 seconds; its active coordinator path recorded 15 ledger
reads, two claim/journal inventories, two verify helpers, one prepare and one send.
These are feasibility observations, not a warmed performance result.

## Source preparation (utility, after review)

Use exact source exports of baseline
`d2099c62656bc2a36c306918a92832ba1e1a0cc0` and published final candidate
`0fd31c1fa8858ef15d516e58c883f8dea9aa727e` (independent history/equivalence accepted;
see history.md). The baseline includes the separately merged background-tab title
correction, outside this CPU patch. `7e6d7c9c` remains the original deployed-source
baseline for historical live measurements, not this controlled comparison.
This is a one-off opt-in campaign, never a routine test/CI gate.
Do not benchmark the shared changing worktree. Prepare these owned temporary
paths and record them in the lead's verification receipt:

- `/tmp/workspace-cpu-investigation-baseline/`
- `/tmp/workspace-cpu-investigation-candidate/`
- `/tmp/workspace-cpu-investigation-baseline.test`
- `/tmp/workspace-cpu-investigation-candidate.test`
- Logs: this session's `cpu-benchmark/` directory (disposable raw evidence).

Export each tree with `git archive EXACT_HEAD` from the canonical runtime repo;
copy only the two identical reviewed fixture files into the baseline source.
Record Git heads, flake.lock hashes, fixture SHA-256s, Go/Ruby versions and host.
Do not fetch/rebase/change refs or invoke a live workspace command.

From each export, compile in its Nix environment:

```sh
nix develop --command go -C portal test -mod=readonly -c \
  -o /tmp/workspace-cpu-investigation-baseline.test ./internal/web
```

Use the matching `candidate.test` destination for candidate. Allow two minutes
per cached compilation; escalate a failure or unexpected source/dependency build
instead of retrying or diagnosing in the utility. Validate the baseline once in
quick mode before accepting a comparison; failure returns to implementer3.

## Timed launches

For each source, enter its Nix shell and run this concrete form, changing only
the revision label, cell, run number and corresponding source/binary path:

```sh
systemd-run --user --wait --pipe --collect \
  --unit=workspace-cpu-bench-baseline-idle0-1 \
  --property=CPUAccounting=yes \
  --working-directory=/tmp/workspace-cpu-investigation-baseline/portal/internal/web \
  --setenv=PATH="$PATH" --setenv=DEV_WORKSPACE_CPU_BENCH=measure \
  --setenv=CPU_BENCH_ROOTS=20 --setenv=CPU_BENCH_MEMBERS=5 \
  --setenv=CPU_BENCH_CONSUMERS=0 --setenv=CPU_BENCH_ACTIVE=0 \
  /tmp/workspace-cpu-investigation-baseline.test \
  -test.run '^TestCPUFixture$' -test.v -test.timeout=6m
```

Run four cells: `idle0` (0 consumers), `idle1` (1), `idle5` (5), and `active5`
(5 consumers, `CPU_BENCH_ACTIVE=1`). Per cell, run three baseline/candidate pairs,
reversing pair order for run 2. Warm-up proves passive coverage and completed
controller transactions for all 120 identities, with a ten-second minimum and
135-second sweep bound (120 one-second candidate slots plus the fifteen-second
worker bound). Expect 30–60 seconds in this fixture. Each then measures thirty
seconds at a quiescent Ruby boundary. Active keeps one native version outstanding
and drains it within the same 135-second bound after the thirty-second window;
status polls and CPU remain counted during drain. Save each
stdout/stderr as `cpu-benchmark/{baseline,candidate}-{cell}-{1,2,3}.log` here.
Expect 24–36 minutes plus active drains/setup, with reassessment at 45 minutes.
An individual fixture timeout/failure escalates immediately without automatic
retry or an extra matrix. Record actual warm-up intervals, covered conversation
counts and active update/reaction counts; six reactions per run are not required.
Do not launch package tests or deployment from this utility.

The accepted batch contains no optional cells, small-state control or profiling.
Return the first result or failure for lead assessment before further work.

The lead accepts raw samples only if active observations and notification
deliveries are complete, all commands exit zero, source/fixture identities match,
and CPU uses each reported actual interval. Report all three samples, median,
range, ratios, request/reaction p50/p95 and sample counts. Keep the experimental
80% coordinator / 50% combined idle targets and the repeatable >20% active-regression
criterion separate from unchanged correctness. Live rollout samples are distinct
corroboration with workload caveats.
