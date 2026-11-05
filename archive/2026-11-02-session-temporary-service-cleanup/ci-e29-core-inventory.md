# Core inventory of settled e29 CI failure

Read-only inventory of complete downloaded logs for runtime
`e29d4d83fc62e0dc929aca332f324336c9c8b034`, run `41509697499`.
All jobs are settled. B owns the browser correction and runtime Git lane.
No A source, Git, pin, build, service or session operation was performed.

The full log contains one distinct test failure in each of creation, fast and
archive: `details starts a resumed read before old success/error/finally settles`
at `internal/web/read_cycle_browser_test.cjs:78`. All report
`ReferenceError: applyCount is not defined` from extracted
`refreshSessionDetails` at `evalmachine.<anonymous>:134:7`, reached from test
line 85. Each package browser batch reports 17 tests, 16 passed and one failed.

| Job | Browser error line in full.log | Subsequent failure chain |
| --- | --- | --- |
| creation | 3050 | Package builder fails; creation test driver and VM run refuse because a dependency failed. |
| fast | 5053 | Package builder fails; agent-team-catalog check refuses because a dependency failed. |
| archive | 8149 | Package builder fails; archive test driver and VM run refuse because a dependency failed. |

No separate Ruby/core failure appears. In each job all four `dev_session` shards
report zero failures/errors: 126/1,380, 128/1,958, 136/1,943 and 140/2,571
tests/assertions (530 tests, 7,852 assertions, 13 skips total). The host Ruby
suite also reports 245 tests, 2,804 assertions, zero failures/errors and three
skips in each job. Every other printed Ruby summary has zero failures/errors.
The separate repository-review browser assets report 13 passed, zero failed.

No native VM run started. The package failure prevents reaching that proof;
there is no observed native failure and no native success claim.

The shortest next step is B's scoped browser-fixture correction and its focused
browser checks, followed by the lead's separately authorized exact-source
packaging/native verification. No additional A test or edit is warranted by
this failure inventory. Existing configuration `abee6aec` and workspace
`00381d14` pins stay held until later corrected runtime publication.

Evidence: [full.log](runtime-ci-e29d4d83/full.log),
[failed-job log](runtime-ci-e29d4d83/log-failed.txt),
[settled status](runtime-ci-e29d4d83/final.json), and
[line-indexed inventory](ci-e29-core-inventory.json). A read the downloaded
evidence; no CI API polling, cancellation or retry was performed.
