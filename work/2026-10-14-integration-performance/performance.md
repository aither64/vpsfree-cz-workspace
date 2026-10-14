# Integration performance measurements

Targets: <=5 minutes administration and <=30 minutes standard aitherdev workflow
with fresh verification and populated dependency caches, excluding external waits.
Implementation/review elapsed time and benchmark repetitions are separate.

The three disposable real-worker driver runs completed with active administration
of 0.696, 0.690 and 0.675 seconds. Each merged/pushed a fixture repository, recovered
its retained operation and exported completion. Queue time was zero. These measure
the driver, not a full four-repository production integration. Real feature merges
remain separately gated by user direction.

All main verification/preparation checks passed in25m17s: runtime evaluation34s,
packaged checks3m7s, extension suite19m30s, workspace checks17s, already-prepared
workspace build7s and aitherdev build1m40s. The workspace/aitherdev artifacts were
also independently prepared in parallel in2m18s and2m43s. Runtime CI38647942844
passed at832d9f1a. Detailed commands/heads: verification-results.json.

Comparable workspace cache-hit samples:1.273,1.354,1.288seconds. A second sample
rebuilt35 missing store outputs and took309.7seconds, so it is recorded as a cache
miss and excluded from that comparison. The package now has a retained GC root.
The earlier generic Ruby outputs were absent; no automatic-GC cause is assumed.
Exact Ruby aggregate derivation was unchanged across the Go-only metadata fix,
proving input identity reuse. Earlier run passed689Ruby tests across11shards.

Comparable aitherdev repeat preparations:104.2,96.1,99.2seconds. Repeated confctl
input/plan evaluation remains visible even when the generation is already built.
The extension's serial command fixtures remain the longest full-verification step.

Previous banner final verification observed a workspace build874.65s (14m35s),
aitherdev128.94s (2m9s) and browser24.48s. Source:
../2026-10-14-dismiss-recovery-banner/merge-final-verification-results.json.
That prior workload is not a controlled before/after benchmark.

The administration target is met by the disposable driver measurements. The full
live integration/rollout target is not certified: real merges are not authorized,
and deployment timing is recorded separately in rollout.md. Do not treat warm
builds or the25m17s verification phase as proof of the whole workflow target.

Raw results: performance-results.json, driver-benchmark-{1,2,3}.json,
parallel-builds.json and verification-results.json. Retain original uncertain
claims, source/artifact roots and feature refs through review/integration.
