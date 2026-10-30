# Performance commands for the upstream 0.31 pair

Prepared command selection only. No all-client, scaling, paired pilot or
measurement is authorized by this preparation task. Final committed independent
review and a separate run grant are required before executing these commands.

- Manual quick baseline: `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`.
- Candidate and neutral harness: `a0c78d1c0e5ef84b5e746d9bba4bc51830c77139`.
- Source exports and frozen-input availability: see `source-preparation.json`
  and the linked source quick/package receipt once the current operation ends.
- Retain the fixed reference `b85ec364057f536940d689b09e612512ffffaf82`,
  existing budgets, calibrated runtime and single neutral candidate harness.
- Benchmark gems stay in the checkout's dedicated benchmark store. Do not use
  root/server/Go or Rust gem homes for the unbundled benchmark workers.

## All-client and both scaling dimensions

Run from the neutral checkout after review/run approval:

```sh
export HAVEAPI_BENCHMARK_GEM_HOME="$PWD/servers/ruby/benchmarks/.gems"
nix-shell servers/ruby/benchmarks/shell.nix --run 'make -C /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-a0c78d1c/candidate test-performance-clients'
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
nix-shell servers/ruby/benchmarks/shell.nix --run 'make performance PERFORMANCE_ARGS="--baseline-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-a0c78d1c/baseline --baseline-sha f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0 --candidate-root /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-a0c78d1c/candidate --candidate-sha a0c78d1c0e5ef84b5e746d9bba4bc51830c77139 --profile quick --budgets servers/ruby/benchmarks/performance_budgets.json --output /home/aither/workspace/ai/vpsfree.cz/work/2026-10-27-api-documentation-redesign/performance-a0c78d1c/paired-quick"'
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
