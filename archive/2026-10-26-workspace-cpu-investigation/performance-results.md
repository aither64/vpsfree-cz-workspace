# Controlled performance results

One-off opt-in experiment; ordinary tests and CI skip it. All 24 runs passed.
Baseline `d2099c62656bc2a36c306918a92832ba1e1a0cc0`, candidate
`0fd31c1fa8858ef15d516e58c883f8dea9aa727e`, identical reviewed fixture files.
20 roots with five members each (120 conversations), validated 3,145,879-byte
ledger, complete scheduler settlement before counters, three alternating warmed
pairs per cell, 30-second measurement windows. Timed campaign approximately
26 minutes (21:25–21:51 UTC); preparation is separate.

| Cell | Baseline cores (range) | Candidate cores (range) | CPU reduction | Coordinator reduction |
| --- | ---: | ---: | ---: | ---: |
| idle0 | 0.945 (0.943–0.946) | 0.113 (0.110–0.116) | 88.0% | 97.5% |
| idle1 | 1.013 (1.007–1.029) | 0.190 (0.187–0.196) | 81.3% | 97.5% |
| idle5 | 1.343 (1.339–1.347) | 0.194 (0.192–0.197) | 85.6% | 97.4% |
| active5 | 1.540 (1.521–1.558) | 0.247 (0.243–0.247) | 84.0% | 91.6% |

Whole-service cgroup CPU includes actual subprocess helpers. The fixture uses
synthetic native Client/Backend and admission seams; native Codex daemon,
activity connection, model work and browser rendering CPU are excluded. Remaining
tmux work includes healthy recovery, outside the optimization scope.

| Active workload metric | Baseline | Candidate |
| --- | ---: | ---: |
| Updates observed / notifications delivered | 3 / 3 | 3 / 3 |
| Pending notifications | 0 | 0 |
| Native reaction p50 / p95 | 28.819 / 28.837 s | 28.682 / 28.695 s |
| Notification delivery p50 / p95 | 6.358 / 6.408 s | 1.394 / 1.401 s |
| Status request p50 / p95 | 392 / 431 ms | 400 / 443 ms |

No repeatable >20% active latency regression appears. Active CPU is 84% lower.
The workload intentionally allows one outstanding update, so each active run has
one event, not six coalesced events. Three samples provide bounded evidence,
not broad tail-latency assurance.

Median idle0 Go self CPU fell 5.661→1.624 CPU-seconds; Go allocated bytes
172.8→55.7 MB and allocations739,282→285,458. Ruby coordinator allocations
1,278,392→81,026. At five consumers status helpers30→6; idle native notification
verification60→0 and tmux600→120, with120 fresh passive observations retained.
Active notification verification81→2 while prepare/send stay1 each.

Acceptance: provisional ≥50% total idle and ≥80% coordinator savings met in
every idle cell. Active CPU/latency checks met for this controlled fixture.
Raw samples, self CPU, allocations, helper counts and latency arrays are in
`cpu-benchmark/summary.json` and24 logs; exact hashes in source-identities.txt.
All120 conversations warmed in every run, all updates observed and all
notifications delivered with zero pending work, independently checked by lead.

Final rollout sourcef23e717c is a patch-equivalent successor on the already-live
disjoint archive repairdeed45f0, independently reviewed. This experiment measures
d209..0fd31 and the unchanged CPU patches; it is not a direct measurement of
the complete refreshed package or a promise about uncontrolled production CPU.
Final-head build/check/deployment and live-service measurements remain separate.
