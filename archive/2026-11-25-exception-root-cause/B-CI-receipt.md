# API CI evidence — package B

[API run 45641819759](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819759), workflow 234996228, attempt 1: **completed / success**. One final attempt read and one job/artifact snapshot were obtained; no polling, rerun or new test was started.

Tested runtime source: `da7724abdc080e59820cc4f0812ce1a41b3fc5df`, branch `2026-11-25-exception-root-cause`, event `push`. This CI did **not** run at the later documentation-only head. E's source-input equivalence and final-range review remain separate evidence. The declaration-neutral client exemption is accepted by lead; no client generation was run for this receipt.

All 27 jobs succeeded (13 topics per mode plus aggregate). Platform-operations jobs [full 139302209506](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819759/job/139302209506) and [core 139302209297](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819759/job/139302209297) both started `2026-11-25T15:08:45Z`. [Topic coverage 139318712561](https://github.com/vpsfreecz/vpsadmin/actions/runs/45641819759/job/139318712561) succeeded.

## File and example coverage

Both platform-operations manifests contain 8 files and include `spec/api/resources/incident_report_spec.rb` exactly once. Each mode reports **244 examples, 0 failures, 0 pending, 0 outside-example errors**. All **27 incident-report examples passed** per mode; their complete ID/status/pending-reason sets match. Tested source declares 27 examples and has spec SHA-256 `8a99a06fc82f8b0c6223cf1347fce31696d9aa411d3147ae18d4fcf419abc37e`, matching the reviewed/focused-check input.

| Exact example ID (only leading `./` normalized) | Case | Full | Core |
| --- | --- | --- | --- |
| `spec/api/resources/incident_report_spec.rb[1:2:8]` | filters by ip_addr without leaking other users | passed | passed |
| `spec/api/resources/incident_report_spec.rb[1:2:9]` | orders IP-filtered reports with includes by their own detection time | passed | passed |

## Artifact and environment identity

All four downloaded zip SHA-256 values match GitHub artifact digests. Metadata identifies the exact runtime head/run. Expected manifest and native result/environment member names were validated. Raw archives, extracted files and API snapshots are in `B-ci-raw/`, verified Git-ignored and untracked before writes; none was staged or committed.

| Artifact | ID | Verified zip SHA-256 |
| --- | --- | --- |
| `rspec-files-core-platform-operations` | 15035840958 | `61d0c6e2541237ffdbbee641a8677c7653dd0bfd27e972924492ffeb271b73e8` |
| `rspec-files-full-platform-operations` | 15036215480 | `d4bdb3fb4f4779ea8e53c8f80626b00a8eac2466211b1b7be0883862910ab790` |
| `rspec-results-core-platform-operations` | 15036964582 | `0988b5df6b04eb9d150dcbf9575b9da461615cf988502ad14a34c31c06687602` |
| `rspec-results-full-platform-operations` | 15036519046 | `c590c245e52afef5e3e4975b122844df1a3f0483978cbd9c122109b7de590535` |

Both environment records identify topic `platform-operations`, Ruby `ruby 3.4.13 (2026-11-19 revision 48857d6f2e) +PRISM [x86_64-linux]`, Bundler `2.6.9`, RSpec `3.13.7`, and their correct mode. Effective lock digests are mode-specific; no full/core lock equality is claimed.

| Mode | Effective API Gemfile.lock SHA-256 | Native duration |
| --- | --- | --- |
| full | `5774c8a65867910c21eaa3db6ce2aabf73d8cb95fbe3b4fe9306a0c0b38ec9f1` | 1190.37s |
| core | `f2eafe983b7851209dd7ec0584ddeb8419eec9e01e634e8618f1788597dde70a` | 1386.94s |

No API coverage gap remains for B. Lead reported RuboCop/i18n success at the same runtime head. Main CI 45641819704 remains separately lead-observed and was not queried by B. No source, index, branch, export, client or lifecycle mutation was performed.
