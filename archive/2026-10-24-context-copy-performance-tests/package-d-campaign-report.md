# Documentation performance campaign

Accepted local evidence for candidate `b85ec364057f536940d689b09e612512ffffaf82` against baseline
`39909094649b1d14a23f00615775ca7136acf4fd`. The one authorized campaign exited 0 in about 90 seconds; no retries or source changes occurred. The utility slot is relinquished.

The lead and architect accepted the root-resource insertion-order exception described below before timing interpretation. All remaining identity and output gates passed.

## Workload and method

Four processes ran dynamic baseline/candidate and Rust baseline/candidate with the same exact harness and shared fixture. Each used both shapes: eight ordinary resources with one action each, and one resource with eight ordinary actions. Both have one public sample per ordinary action, two additional string parameters, the fixed nested/zero/false/empty/null fields, one privileged sample per ordinary action and one extra admin action in resource0. Requests use the synthetic admin user.

Each lane has two warmup batches and five measured trials. HTML measures one Rack request per trial. Context and adapter rows measure 100 operations per trial; their values are batch totals. Mount/profile setup, root ownership construction, description selection, warmups, output validation, hashing and JSON serialization are excluded from lane timings. GC runs before each trial outside the timer; in-workload GC remains included. Wall time uses a monotonic clock; CPU is process CPU; allocations are Ruby object counts.

Every reported median was independently recomputed from raw trials. The tables use baseline → candidate; wall ranges show minimum–maximum of the five trials, and CV is population standard deviation divided by mean. Full variance, standard deviation, mean and range for wall, CPU and allocations are in [structured analysis](package-d-campaign-analysis.json).

## Full HTML requests

| Mode / shape / lane | Wall median ms | CPU median ms | Objects median | Wall range ms (baseline; candidate) | Wall CV % |
| --- | ---: | ---: | ---: | --- | ---: |
| dynamic / resources / html | 898.440 → 239.911 | 897.502 → 239.749 | 1,169,425 → 170,835 | 881.965–963.679; 217.581–261.383 | 3.4 → 6.0 |
| dynamic / actions / html | 1,098.080 → 489.404 | 1,097.468 → 488.809 | 1,465,519 → 496,865 | 1063.618–1140.421; 448.780–508.080 | 2.3 → 4.7 |
| rust / resources / html | 1,176.814 → 302.470 | 1,176.218 → 302.344 | 1,585,661 → 216,552 | 1139.207–1313.651; 281.671–314.399 | 5.8 → 4.1 |
| rust / actions / html | 1,526.721 → 562.464 | 1,526.212 → 562.207 | 1,991,202 → 602,041 | 1379.156–1602.126; 520.250–630.288 | 5.4 → 6.5 |

HTML median wall ratios are 3.74× for dynamic resources, 2.24× for dynamic actions, 3.89× for Rust resources and 2.71× for Rust actions. CPU tracks wall closely. Candidate HTML uses 170,835–602,041 objects per request in these shapes, compared with 1,169,425–1,991,202 at baseline.

## Context derivation batches

| Mode / shape / lane | Wall median ms | CPU median ms | Objects median | Wall range ms (baseline; candidate) | Wall CV % |
| --- | ---: | ---: | ---: | --- | ---: |
| dynamic / resources / context_profile | 130.241 → 0.347 | 130.166 → 0.343 | 211,500 → 500 | 126.485–150.438; 0.314–0.443 | 6.3 → 13.0 |
| dynamic / resources / context_sample | 132.770 → 0.794 | 132.751 → 0.790 | 212,400 → 1,400 | 123.945–142.658; 0.766–1.106 | 4.8 → 15.2 |
| dynamic / actions / context_profile | 133.399 → 0.341 | 133.258 → 0.338 | 205,900 → 500 | 122.252–140.239; 0.319–0.501 | 5.4 → 18.0 |
| dynamic / actions / context_sample | 120.995 → 0.797 | 120.989 → 0.792 | 206,800 → 1,400 | 117.816–124.967; 0.788–0.811 | 2.3 → 1.0 |
| rust / resources / context_profile | 123.199 → 0.356 | 123.192 → 0.353 | 211,500 → 500 | 120.669–134.332; 0.334–0.414 | 3.8 → 8.4 |
| rust / resources / context_sample | 121.581 → 1.077 | 121.574 → 1.072 | 212,400 → 1,400 | 119.558–126.839; 0.810–1.270 | 2.2 → 14.2 |
| rust / actions / context_profile | 126.785 → 0.325 | 126.414 → 0.322 | 205,900 → 500 | 117.124–137.479; 0.323–0.527 | 5.6 → 21.9 |
| rust / actions / context_sample | 123.908 → 0.798 | 123.774 → 0.793 | 206,800 → 1,400 | 116.868–136.398; 0.779–0.803 | 5.2 → 1.2 |

Candidate profile and constant-sample derivation allocations are exactly 500 and 1,400 per 100-operation batch in every case. Baseline counts are 205,900–212,400. The unchanged description is shared only on candidate, as required. Tiny candidate batches have noticeably higher relative variation; their exact ratios should not become latency budgets.

## Rust adapter batches

| Mode / shape / lane | Wall median ms | CPU median ms | Objects median | Wall range ms (baseline; candidate) | Wall CV % |
| --- | ---: | ---: | ---: | --- | ---: |
| rust / resources / rust_async_example | 388.504 → 46.390 | 388.422 → 46.309 | 655,000 → 80,800 | 336.732–400.214; 42.571–59.981 | 6.0 → 12.6 |
| rust / resources / rust_async_auth | 183.175 → 4.657 | 183.053 → 4.653 | 314,900 → 9,000 | 173.673–198.239; 4.437–9.350 | 4.7 → 34.5 |
| rust / resources / rust_blocking_example | 391.623 → 46.636 | 391.093 → 46.550 | 654,900 → 80,700 | 363.327–424.047; 43.297–49.259 | 5.9 → 4.4 |
| rust / resources / rust_blocking_auth | 175.378 → 4.921 | 175.115 → 4.917 | 314,800 → 8,900 | 168.966–192.121; 4.534–5.739 | 4.4 → 8.1 |
| rust / actions / rust_async_example | 364.120 → 45.666 | 363.689 → 45.510 | 639,600 → 80,800 | 355.220–407.891; 44.055–46.624 | 5.0 → 2.1 |
| rust / actions / rust_async_auth | 175.365 → 4.971 | 175.261 → 4.907 | 307,200 → 9,000 | 163.046–181.883; 4.177–5.276 | 3.7 → 9.6 |
| rust / actions / rust_blocking_example | 403.024 → 44.059 | 402.554 → 43.914 | 639,500 → 80,700 | 380.166–441.225; 42.379–48.362 | 5.3 → 4.5 |
| rust / actions / rust_blocking_auth | 187.862 → 4.376 | 187.595 → 4.370 | 307,100 → 8,900 | 170.510–198.215; 4.209–5.059 | 4.9 → 7.2 |

The fixed selected-action adapter batches have about 8–9× lower wall medians; authentication batches about 35–43×. The highest wall CV is 34.5% for the resources async-auth candidate batch, whose five trials range from 4.437 to 9.350 ms. Allocations are stable within each lane.

## Exact output and data parity

All 100 baseline/candidate trial pairs have identical status and byte counts. HTML and Rust generated programs have byte-identical SHA-256 in every trial; no rendered field or byte was normalized. Context action-shape digests also match exactly.

| Mode / shape | HTML status | Bytes | SHA-256 |
| --- | ---: | ---: | --- |
| dynamic / resources | 200 | 266,421 | `86290072889b686937480e1da9eb802d1ba3411810122228c713a2f803838cce` |
| dynamic / actions | 200 | 264,447 | `d3c35a65ec109a75a7083f80bd83fca6152c05152020561180dfca0bd7b20c8f` |
| rust / resources | 200 | 314,004 | `0243b436ff940bd6b6afac76bf695eddab1a856cd7ce6cf3f8950ebd28b6254a` |
| rust / actions | 200 | 312,030 | `51d1b8f1225aa5048651779274f3da8836728647ba71caa1e2588cebb540dd85` |

| Rust program (same digest for both shapes) | Bytes | SHA-256 |
| --- | ---: | --- |
| rust_async_example | 1,082 | `cfa3a457734590401fe668233baf98980b9e5e618d2fb4e1b829d86389e462ea` |
| rust_async_auth | 642 | `e05500211b64c271098a7ab01e61949a4659b9113318a62c3a172ab39589d38b` |
| rust_blocking_example | 1,111 | `01b751e212adefe9b9dc82f72138087d953ae342bb5a2516649c6a9211734600` |
| rust_blocking_auth | 677 | `36bd5938606a97d9125c6ec30fa29beffa71a90dca6bdc2ca815c4abd8ec5fd2` |

The many-resources description and context raw-JSON fingerprints differed because `HaveAPI.resources` enumerates `Module.constants` without sorting; `Server#describe_version` retains that resource insertion order. HTML sorts the resource/action maps. This pre-existing order variation occurs between Ruby processes.

[Retained order proof](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/parity-diagnostic/order-proof.json) and [diagnosis](package-d-campaign-parity-notes.md) preserve actual no-timing authorized descriptions and reconstructed original bodies. Baseline/candidate live data match for every key/value. Permuting only the root `/resources` keys reconstructs each original campaign description SHA-256/byte count exactly, then all 80 original context-trial digest/byte identities using the unchanged sample bytes. No nested key order, array, type, scalar or sample ordering changed. Canonical structural description digests are `e2a4c9a1400c095898788a61456eaee134bb03add6096f1fac591724da7568a4` for resources and `cab224b0a87a3b4584bf9858377bd1c838c4ef122944f8fff28b35f5b415e61f` for actions.

Lead and architect explicitly accepted only that analysis-only root-map order exception. Original reports and their raw fingerprints remain intact. Production code and the benchmark harness were not normalized or changed, and no campaign rerun was needed.

## Runtime, source and input proof

Runtime: `ruby 3.4.11 (2026-09-23 revision 592f1ffdb3) +PRISM [x86_64-linux]`, executable `/nix/store/7b77drpxxyywsxq9hf4y0fc8c56pfivl-ruby-3.4.11/bin/ruby`. Host: `aitherdev`, `linux`. Runtime and hostname match all four processes. Activated gem versions and gem paths match each baseline/candidate mode pair. Rust intentionally adds fiddle, racc and tomlrb.

Every loaded source file digest was checked against disk. Dynamic pairs have 704 matching feature paths and differ only in Context source; Rust pairs have 732 and differ only in Context and the Rust adapter. Baseline export matches all 772 receipt file digests. Candidate exact HEAD and tracked/untracked status are unchanged and clean. All per-process input manifests match before and after each run.

| Input | SHA-256 |
| --- | --- |
| `flake.lock` | `a52bdf3a3b9a069175d3af298234c3cf7adeba54540833eed6ad902e9ccc0a64` |
| `servers/ruby/Gemfile.lock` | `fdc5129f60f9ed2f6a56fbf7f9483af5d6a003fedb13a93e895e9cab87193b52` |
| `clients/rust/Gemfile.lock` | `53b94ab0ef92f5dccfd413eb1e313ed65868f1e2ba41af8b95ce6e62ae8d447f` |
| `servers/ruby/benchmarks/documentation.rb` | `a2cae676b0b6d647e31978893775c94b0fe9a0cec9025fd478c9f62e38f584fb` |
| `servers/ruby/test_support/documentation_performance_fixture.rb` | `85a5f387f69556c91a615efe29ac3a9536bd5a3d4dcb29785f994f00a67cbeb4` |

[Campaign directory](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/launch.log) retains the exact copied launch script and SHA, all four command lines, stdout JSON, stderr, per-run exits/timestamps, overall exit, complete Git trees, export receipt, resolved flake metadata, shell derivation/input graph, hostname and runtime receipts. [Evidence hashes](package-d-campaign-evidence-sha256.json) preserve the campaign and diagnostic artifact identities. Raw reports:

- [dynamic-baseline](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/dynamic-baseline.json), SHA-256 `11aad022e3879fcd51f1e8b862879e1b984987881c5a9e813f96a1d797ab7015`
- [dynamic-candidate](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/dynamic-candidate.json), SHA-256 `3781d85572addc5f494f6064efd835998208448d37d3b8c023e9b9736f25de73`
- [rust-baseline](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/rust-baseline.json), SHA-256 `b0bb8f692619df09ba2d37cfd37f25f5efd4981f52da908d1992be40b58ea91f`
- [rust-candidate](documentation-campaign-b85ec364057f536940d689b09e612512ffffaf82/rust-candidate.json), SHA-256 `4c325cb9248f9c6ad65c2e5ebe4d9afae045ed59875aab27f29b327b8b21b3bf`

The baseline archive receipt retains exact source revision `39909094649b1d14a23f00615775ca7136acf4fd` and tar SHA-256 `c61f0e459fc14db61194ed6134a0e3da89f5d53c3b59c0aad11a5685785107d2`; the exact source remains reconstructible from retained Git objects. [Test-temp cleanup receipt](package-d-baseline-cleanup.json) records that the exact export was retained: ownership/content and archive reconstruction passed, but ten processes could not be fully inspected for open references. No deletion occurred.

## Interpretation and limits

This local synthetic campaign supports lower derivation, HTML request and Rust adapter costs on the recorded host. It does not reproduce or measure production latency. Fixed batch overhead and five trials limit precision, especially for submillisecond context batches. The runs are sequential, so host variation and order effects remain possible. No CI wall-clock gate or latency budget follows from these results.

Concentrated actions remain about 2.04× slower than distributed resources for dynamic candidate HTML and 1.86× with Rust, with substantially more allocations. HTML still explicitly supplies and copies resource/action/sample subtrees; a large resource can therefore remain costly. Saved Rust action resolution and ancestor lookup retain their own scaling costs. These results and deterministic regression checks cover this defect class, without guaranteeing all page shapes or future performance.

The utility slot is released. No source, Git, deployment or lifecycle change was made during the campaign or analysis.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
