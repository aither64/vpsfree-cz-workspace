# Verified Linux review bases

Target session is ordinary (manifest has no sensitive flag and is tracked).
All selected bases are exact ancestors of the observed heads. All 13 were applied
through the supported CLI on 2026-11-27. No source refs changed. Live core history
and comparison passed with 13 commits and 9 changed files. Local
review-base-application.json retains previous and applied values.

| Registration | Observed head | Base | Commits | Files | Evidence |
| --- | --- | --- | ---: | ---: | --- |
| linux | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 0 | 0 | d4-network-base-evidence.md:11-14 |
| linux-99283-followup | `39af8ab261a29203849dc5e3931a902d91b55c6e` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 2 | 1 | portal.yml initial_base_sha |
| linux-bpf | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 0 | 0 | d2-bpf-evidence.md:12-17 |
| linux-core | `2904ad84b510af32ee889812560861507059ce2c` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 13 | 9 | portal.yml initial_base_sha |
| linux-k1-amd | `a872c1e2813b1f70065bf76cfdf07498689cb847` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 4 | 3 | portal.yml initial_base_sha |
| linux-k2-common | `952185886feb4cf8996a3ef11e9c6a553a86a367` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 5 | 6 | portal.yml initial_base_sha |
| linux-k3-intel | `f548c27598fbe0493d1da336c8d4ecd3478e5207` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 2 | 1 | portal.yml initial_base_sha |
| linux-kvm-adaptation | `f3dedb0850c8b2b862b94e2aa4b0eb87c34f51eb` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 12 | 12 | portal.yml initial_base_sha |
| linux-metrics-lifetime | `f62db2f88d7bd211a7eb95aae4ad55d89ff0d206` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 1 | 1 | portal.yml initial_base_sha |
| linux-network-closure | `5c8e1987e80cff7ca6187c59d538a03802819334` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 2 | 2 | portal.yml initial_base_sha |
| linux-pidns | `7d8430b9bc0d47578d0146d0d924c1d6ef355ba7` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 3 | 2 | portal.yml initial_base_sha |
| linux-pivot-root | `6d5a58005bd774f93600580925517da48d4842be` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 1 | 1 | portal.yml initial_base_sha |
| linux-reqsk | `564f9982a87625e006b8465bdb4a7deb51cf55e0` | `1dfea587406b7dd79973831d1677fb2418e5e9aa` | 3 | 5 | portal.yml initial_base_sha |
