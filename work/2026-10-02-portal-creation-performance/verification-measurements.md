# Isolated session creation measurements

Five sequential Full-team creations passed with 3,379 genuine synthetic
history threads, 16 KiB of developer context per seed and no archived history.
The warm-up is excluded from these five values. Services and all evidence remain.

Candidate: `/nix/store/0klh7dhca2dwyfwsz0m67pbjj2nml70d-dev-workspace-0.2.0`.
Runtime revision: `8ae46f9de6ea54b4dab7a4dbeb694593210cc7a1`.
Selected Codex: `0.160.0`; installed Full-team catalog/settings unchanged.

| Sample | Ready after acceptance (s) | First assistant after acceptance (s) | First assistant after ready (s) |
| --- | ---: | ---: | ---: |
| 1 | 6.121215 | 11.762439 | 5.641224 |
| 2 | 6.401349 | 11.316560 | 4.915211 |
| 3 | 6.332730 | 10.620890 | 4.288160 |
| 4 | 6.500734 | 11.322786 | 4.822052 |
| 5 | 6.428341 | 10.863319 | 4.434978 |

Median readiness: **6.401349 seconds**. Maximum:
**6.500734 seconds**. Both strict targets passed: median
under 10 seconds and maximum under 15 seconds, using every value. Each sample
has its exact ready receipt and retained root/three member identities, a
completed model turn, one canonical initial request and no tool activity.
Required stage completion and visible detailed phases passed for every sample.

Root conversation stage: median 0.356 seconds; maximum 0.384
seconds. The earlier observed portal baseline was 103.546 seconds, including
a 98.212-second filesystem history scan. These measurements verify the fresh
request path; recovery deliberately retains complete history discovery.

## Recovery result at this checkpoint

The combined run remains **incomplete**. The lost-root-helper-response fault
reached its intended boundary. Its first attempt failed after successful root
creation, then retry2 completed history discovery and refused with the selected
Codex missing-rollout error. Selected-source diagnosis traced that error to resume of a still-loaded root
without a persisted rollout; disappearance recognition must remain strict.
The partial-member fault was not reached. Parent diagnosis and the correction
brief are tracked in state.md; no additional retry or activation has run.

The isolated histories are synthetic. The actual-history live canary remains a
separate post-activation gate. These timings precede the loaded-root recovery correction and retain that
precise source/package provenance.

[Session portal](https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-02-portal-creation-performance/)
