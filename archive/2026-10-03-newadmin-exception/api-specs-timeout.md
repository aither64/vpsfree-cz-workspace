# API Specs timeout and bounded recovery

API Specs run `37146401912`, exact API head `af8a9767`, attempt 1 completed
cancelled. Full-platform job `111271142722` reached its workflow-defined
45-minute job limit; RSpec ran 44m32s. Every other topic and topic coverage passed.
No watcher cancelled or reran any job. Integration CI is excluded from waiting
by user direction and is not part of this investigation or merge gate.

Lead inspected the complete available platform job log. The new persisted
cleanup/refresh/access-authentication regression passed at 19:03:42 UTC. No
RSpec failure marker appears in the log. It continued reporting completed
examples every few seconds through SecurityAdvisory resources until cancellation
at 19:47:49; this evidence does not indicate a stuck SSO regression. Cancellation
prevented the suite's final summary, so this is not a passing run.

Compared actual successful master-run metadata:

| API source | Run | Full-platform RSpec |
| --- | --- | --- |
| incident pin `a65a4dfe` | [35244637812](https://github.com/vpsfreecz/vpsadmin/actions/runs/35244637812) | 42m18s, success |
| `941451cf` | [35209242605](https://github.com/vpsfreecz/vpsadmin/actions/runs/35209242605) | 40m38s, success |

The job has little runtime margin. Slower runner throughput is a plausible
explanation; the exact contributor (runner variability versus inherited
dependency performance) is not established. Source/spec inventory remains the
reviewed guard and two existing specs; only one added example belongs to the
platform topic, and it completed early.

Decision: one targeted rerun of the cancelled full-platform job on the unchanged
API commit, after inspecting first-attempt logs and baseline duration. Preserve
this first-attempt evidence. If it hits the cap again, investigate topic capacity
or performance rather than blindly rerunning. A passing retry must be the actual
API Specs workflow conclusion at the exact head before either default-branch
integration; partial job success alone does not satisfy the user's condition.

Raw log is retained locally at
`api-ci-completion-37146401912/platform.log`; no raw credentials or report email
are copied into tracking. Compact result: [first attempt](api-ci-completion-result.json).
Retry evidence will be recorded in the final verification record.

## Superseding user direction

User requested 60 minutes instead of another unchanged-head rerun. Attempt 2
(run 37146401912, job111280576895, started19:55:22 UTC) was still in progress
when its observer returned incomplete. No watcher cancelled it. The bounded
implementation changes only full/core topic timeouts45 ->60, preserves coverage
10 and all topic selection. The new published head must pass API Specs; older
head success cannot meet that condition. Existing action major refs match
official current release lines (checkout7.0.1/upload7.0.1/download8.0.1; Ruby
setup1.327.0 through rolling v1).

## Final result

Requested workflow change published as f9; fresh exact-head run 37151153953
passed all 27 jobs in 34m17s, including topic coverage. Full-platform RSpec took
32m56s. The 60-minute setting adds headroom; this success does not identify the
exact contributor to the earlier cancellation. No unchanged-head retry was
accepted as final validation. Both default branches then fast-forwarded to
reviewed/tested heads. [Verification](verification.md),
[integration proof](integration-result.json).
