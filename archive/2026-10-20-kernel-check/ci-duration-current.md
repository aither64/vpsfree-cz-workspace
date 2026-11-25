# Current CI duration receipt

Same sole native watcher `01a1634c-0553-7530-ba30-b19cfc2307d0` captured exact
[run39767770407](https://github.com/vpsfreecz/vpsadminos/actions/runs/39767770407)
and its jobs at2026-10-22T20:32:55–57Z. Head is exact846bb, attempt1. This is
a bounded requested status refresh, not a second observer or test run.

Workflow creation/run-start is11:03:56Z, wall age9h29m01s at capture. API overall
status is `queued` with null conclusion; individual jobs establish partial
execution. The OS/cache job completed11:18:07Z. Six jobs passed, two failed,
and three remain unfinished:

| Remaining job | Exact status at capture | Timing | Runner/active step |
| --- | --- | --- | --- |
| amd-fresh119793311399 | queued | Created11:18:07Z; queue age9h14m50s | Runner ID0, empty name, no steps |
| amd-scale-aged-v5 119793311416 | in_progress | Created11:18:07Z; started15:54:58Z; elapsed4h37m59s | gh-runner4.int.vpsadminos.org, ID11199, group vpsadminos runners; Run livepatch lifecycle tests started15:55:02Z, elapsed4h37m55s |
| amd119793311543 | queued | Created11:18:07Z; queue age9h14m50s | Runner ID0, empty name, no steps |

All three use label `amd-livepatch`. Queued job `started_at` equals creation,
but their explicit queued state, no steps and unassigned runner mean this is
not evidence of executed runtime. The aged-v5 creation-to-start gap is4h36m51s.
Earlier aged-v6 occupied the same named runner from11:18:09Z to15:42:18Z;
this supports shared-runner serialization but does not identify every cause of
the remaining allocation gap. Source and historical lanes own its interpretation.

Completed durations: OS/cache13m16s; product suite3h6m41s failed;
AMD-scale-aged-v6 4h24m09s failed; AMD-low-memory-v6 6m17s and v5 6m18s passed;
Intel1h34m45s, Intel representative-v6 1h43m44s and representative-v5 7m7s passed.

Raw evidence: `generic-sysctl-ci-39767770407-duration-run.json`,
`generic-sysctl-ci-39767770407-duration-jobs.json`, and capture start/end/exit
receipts. Both API reads exited0. No rerun/cancellation occurred. Current step
metadata supplies no live inner-test progress or confirmed stall. No configured
deadline breach or hang is established by this receipt alone; the assigned
source/history lanes assess actual budgets and comparable timing.

To deliver this request through the same owner, only its superseded local600s
watch was interrupted and accounted (local130 is control, not CI result).
Same native identity now continues one600s watch using
`generic-sysctl-ci-39767770407-600s-detail.*` receipts. Prior captures remain
unchanged. No source/Git/test/workflow/deployment/lifecycle action was selected.


## Later same-owner snapshot

At 2026-10-23T00:38:17Z, the same native watcher captured another exact-run
snapshot and retained the existing watch process. Head remains846bb, attempt1,
status `in_progress` with null conclusion. `amd-fresh` has passed and aged-v5
has failed. Only `amd` job119793311543 remains unfinished, executing on
`gh-runner4.int.vpsadminos.org`/11199, label `amd-livepatch`, group
`vpsadminos runners`. It started23:40:37Z; its lifecycle-test step started
23:40:41Z, about57m36s before the snapshot. API step state does not expose live
guest progress or establish a stall. Workflow wall age is13h34m21s, including
queue time; `amd` creation-to-start alone is12h22m30s.

This later watcher capture reused the two raw `-duration-{run,jobs}.json`
filenames. Those files now contain the00:38 snapshot; the original20:32
capture start/end receipts and historical summary above remain, but the
original raw JSON at those names was overwritten. The later raw data is also
preserved explicitly as `generic-sysctl-ci-39767770407-duration-20261023T003817Z-run.json`
and `generic-sysctl-ci-39767770407-duration-20261023T003817Z-jobs.json`.
`generic-sysctl-ci-39767770407-duration.captured` identifies the later capture.
No second watch process, rerun, cancellation or test was launched.
