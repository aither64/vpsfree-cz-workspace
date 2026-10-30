# Prepared performance verification inputs

Prepared only; no test, benchmark pilot or measurement has run for this pair.
Independent review and a separate run grant are required before executing below.

- Baseline: `2f5156262baaf137800c17a9321e617c2b5df1d5`, tree
  `ec4f90ba282e4e73b981163ea3fc07a3de4ec763`.
- Candidate: `82a7f2abcc1ecfc361097d30de39e93aca026d64`, tree
  `88c140470b161a66237ae891cae7e1be197677e1`.
- Neutral harness: exact candidate checkout at
  `/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-27-api-documentation-redesign/haveapi`.
  It contains both exact Git objects. `neutral-harness.sha256` identifies the
  runner, comparator and unchanged timing fixtures.
- Frozen bundle: the checkout's `servers/ruby/benchmarks/.gems`, with
  Bundler 4.0.23 and JSON 2.21.2. The shell clears inherited Bundler/Ruby settings.
- Calibrated Ruby:
  `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`.
- Both exports have run `make doc`; all 860/892 tracked source blobs still match
  their Git trees afterward. Archive, native ls-tree, complete source hashes and
  generated-document hashes remain beside this file.
- `input-preparation.log` retains Ruby identity, locked dependency availability
  and exact gem store paths. Exit status is `0`. This proves preparation, not a
  fully activated worker graph or any performance result.

Benchmark Gemfile, lock, shell and budgets are identical in baseline, candidate
and neutral checkout. No budget/reference/runtime/fixture policy was changed.
Before launch, recheck that the reviewed candidate and neutral harness still
identify these exact inputs. A review fix requires a fresh candidate export.

## All-client and both scaling dimensions

Run from the neutral checkout after review/run approval:

```sh
export HAVEAPI_BENCHMARK_GEM_HOME="$PWD/servers/ruby/benchmarks/.gems"
nix-shell servers/ruby/benchmarks/shell.nix --run 'make -C /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-82a7f2ab/candidate test-performance-clients'
```

Retain stdout/stderr in this directory as `all-client.log` and the actual exit
status as `all-client.exit`. The existing suite covers all 15 clients and both
levels, every supported provider/action/failure lane, exact HTML panels and
admin/member/admin isolation, unrelated-resource growth and action-panel growth.
Its `ALL_CLIENT_PERFORMANCE` output retains measurements. Existing +32 object/
call and 2.5 increment bounds remain unchanged.

Plan approximately 1–3 minutes; this is an estimate, not a timeout or a result.
Run once through a fresh pinned watcher; stop on failure and retain diagnostics.
Do not proceed to paired measurement if this required contract fails. No
retry-until-green, narrowed client matrix or budget relaxation.

## Paired quick comparison

Use the same neutral checkout and frozen shell, outside Bundler:

```sh
export HAVEAPI_BENCHMARK_GEM_HOME="$PWD/servers/ruby/benchmarks/.gems"
nix-shell servers/ruby/benchmarks/shell.nix --run 'make performance PERFORMANCE_ARGS="--baseline-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-82a7f2ab/baseline --baseline-sha 2f5156262baaf137800c17a9321e617c2b5df1d5 --candidate-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-82a7f2ab/candidate --candidate-sha 82a7f2abcc1ecfc361097d30de39e93aca026d64 --profile quick --budgets servers/ruby/benchmarks/performance_budgets.json --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-82a7f2ab/paired-quick"'
```

Retain command output as `paired-quick.log` and actual exit as
`paired-quick.exit`. The native output directory contains `samples.json`,
`report.json`, source/runtime/input receipts and per-worker logs/progress. It
has not been created by preparation.

Plan approximately 5–10 minutes; reassess overruns without inventing a quiet-run
kill timeout. The existing runner bounds setup to 120 seconds and each batch to
30 seconds, retains failures, and supervises/reaps its workers. Run one campaign
through a fresh pinned watcher after the all-client contract passes. Escalate
unexpected local kernel compilation; do not launch an unrelated runtime build.
Exit 1 means regression, exit 3 means error. Exit 0 may mean pass or explicitly
inconclusive timing: inspect `report.json` and preserve that distinction. No
automatic rerun, baseline substitution or reference/budget update is authorized.
The quick profile compares one unchanged endpoint request; a smaller overview
response is not evidence that resource-page rendering is faster.
