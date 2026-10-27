# Automatic Check at runtime352a: passed, observation settled

After owner1's successful copy command settled and released the slot, one short
`gh run view` final observation of existing
[Check40493270858](https://github.com/aither64/dev-workspace/actions/runs/40493270858)
confirmed exact head `352aa4c60457d682207b900fa5835dec82e5d064`, push event,
created `2026-10-27T11:03:40Z`. The run completed **success**, updated
`2026-10-27T11:26:00Z`. The complete actual API response is
[final-run.json](final-run.json). The [earlier in-progress snapshot](status.json)
is retained separately.

| Job | ID | Observed result |
| --- | --- | --- |
| creation | 122152238082 | Success, `11:03:42Z`–`11:26:00Z` (22m18s) |
| fast | 122152238516 | Success, `11:03:42Z`–`11:19:03Z` (15m21s) |
| archive | 122152238544 | Success, `11:03:42Z`–`11:17:13Z` (13m31s) |
| host | 122152240777 | Skipped, as expected for ordinary feature push |

No current failure was present, so no failure-log retrieval was needed. No
dispatch, rerun, cancellation or CI watcher was launched. The original final
capture command (handle11254) exited0. No observation process, uncertain command
or utility is running; the slot is free. The final result was reported to lead.
The separate [corrected local host batch](../host-vm-352a/result.md) passed both
requested outputs and is not relabeled as this skipped CI job.

## Earlier35d6 scope

Owner0's retained [initial352a branch list](../runtime-quick/final-352a-auto-runs.json)
records old [Check40490727734](https://github.com/aither64/dev-workspace/actions/runs/40490727734)
as completed **failure** at `35d6073e42c2110ee4a99fa902815d26495c6078`, created
`2026-10-27T10:43:51Z`. That capture contains overall run metadata, not job-level
failure logs or conclusions. No old run was polled again for this report.
The [original local35d6 host failure](../host-vm-35d6/result.md) and its full log
remain separate local evidence; they are not presented as automatic CI logs.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-26-codex-upgrade-naming/
