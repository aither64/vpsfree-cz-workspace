# Benchmark CI watcher result

- Run: [39276852536](https://github.com/vpsfreecz/vpsadminos/actions/runs/39276852536), job 118143302393, `Matched warm native suite timing`.
- Workflow head: `06915925a7a63a2fac7135a752101228b5b699e0` (`2026-10-17-impermanence-test-failures-benchmark`). Tested product SHA: `a2ccd72d08dc67f678d7f115a92ed5eeca50c1a1`.
- Result: failed. The measurement step failed at 2026-10-19 15:51:29 UTC; all exposed job steps, including uploads and runner completion, reported complete by 15:51:32 UTC. `gh run watch` then completed with failure. GitHub's final run record reports `completed` / `failure` at 16:16:18 UTC, while the per-job API still reports `in_progress` with no conclusion or completion timestamp.
- Queue time: 3m58s (run created 15:18:40, job started 15:22:38 UTC). Run wall time: 57m38s (15:18:40–16:16:18 UTC). Exposed job steps completed in 28m54s (15:22:38–15:51:32 UTC). The recorded preparation/warm-closure phase was 1681.965 seconds. No A/B test leg ran.
- Runner: `gh-runner3.int.vpsadminos.org` / `gh-runner3`, Linux x86_64, Intel Xeon Gold 6230R, 48 CPUs; job 118143302393. The captured identity reports zero OOM and OOM-kill events.
- Raw `timings.json` reports `legs: []`, `comparison.complete: false`, and qualification “The comparison does not contain two completed CLI runs.” Its error is `NoMethodError: undefined method 'fetch' for an instance of Integer`. Thus A/B total time, preparation time, runtime, and results are absent; no performance conclusion can be drawn.
- The full Actions log shows successful setup/checkouts and preparation, then this error and exit code 1 in “Prepare environment, warm closures and measure both legs.” Upload and diagnostics-retention steps succeeded. The retained text does not show an actual Linux kernel derivation compilation. GitHub did not expose in-progress logs; they became available after the job steps completed. No warmup `build.log` files were included in the uploaded artifact.
- No cancellation or rerun was performed. No acceptance or causal decision is made here.

Evidence files:

- Full Actions log: `benchmark-ci-39276852536/github-actions.log`.
- Downloaded artifact archive: `benchmark-ci-39276852536/artifact.zip`.
- Extracted uploaded files: `benchmark-ci-39276852536/artifact/` and the `benchmark-ci-39276852536/prebuild-benchmark-39276852536-1/` directory.
- Raw timings: `benchmark-ci-39276852536/prebuild-benchmark-39276852536-1/timings.json`.
- Other retained evidence: `benchmark.log`, `identity.json`, `selection.json`, `nix-dry-run.log`, and `environment.log` in the same artifact directory.
