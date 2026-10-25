# Follow-up final CI handoff

Development branch `2026-10-22-haveapi-release-followups` is published at
`090a188cb4ef3477324718627f4ae3415d1c0975`, tree `e9473d5453e014ff2b0da36d4bb21f0eab2eb7e2`.
The reviewed six-commit series, all eight actual local verification phases and
all seven automatic exact-head CI runs passed.

| Workflow | Run | Attempt | Conclusion |
| --- | --- | ---: | --- |
| RuboCop | [39992191274](https://github.com/vpsfreecz/haveapi/actions/runs/39992191274) | 1 | success |
| i18n health | [39992191325](https://github.com/vpsfreecz/haveapi/actions/runs/39992191325) | 1 | success |
| release | [39992191335](https://github.com/vpsfreecz/haveapi/actions/runs/39992191335) | 1 | success |
| servers/ruby RSpec | [39992191336](https://github.com/vpsfreecz/haveapi/actions/runs/39992191336) | 1 | success |
| clients/rust | [39992191340](https://github.com/vpsfreecz/haveapi/actions/runs/39992191340) | 1 | success |
| clients/js tests | [39992191465](https://github.com/vpsfreecz/haveapi/actions/runs/39992191465) | 1 | success |
| clients/python | [39992192454](https://github.com/vpsfreecz/haveapi/actions/runs/39992192454) | 1 | success |

Each run is bound to this exact source, development branch and `push` event.
The successful release workflow was build-only: publication job
`120549359142` was **skipped** and the tag-only predicate was false.
CI artifact `12518641624`, `release-39992191335`, is bound by metadata to this
head, with digest `sha256:9b55894fa8e31e670650a4579ac78dc35fcd779cb0195b00c69ff4f8476acbeb`.
Its package archive was not downloaded or substituted for retained local files;
its internal manifest was not separately inspected.

[Complete warning comparison](followups-ci-whole-job-warning-comparison.md)
uses the original 3,201-line release job and exact new 3,053-line CI build job.
All five targeted warning categories are absent. The new full job retains eight
Nix-runner UID warnings and four empty-Git-fixture warnings, plus the recorded
Git hint and Composer dependency-name mentions. Raw logs are unmodified.

[Push proof](followups-feature-push-ci.md),
[local verification handoff](followups-verification-handoff.md) and
[independent final review](followups-final-review.md) retain the full source,
history, tool/input, artifact and acceptance evidence, including stated limits.
The [final read-only proof](followups-ci-observation-resume-090a188c-20261023T171600Z/final-source-output-remote-proof.json)
at 2026-10-23T17:20:03.951483+00:00 confirms exact head/tree and clean tracked source/index,
302 cache paths, 69 generated docs, one PHPUnit cache and twelve development
artifacts preserved. Remote master, original feature and `haveapi-0.30` remain
at `b64fb25b`; the official tag object/peeled commit, source and all twelve
official artifact hashes are unchanged.

The initial observer stopped on GH's raw-ANSI terminal-output guard after
saving the complete release log archive. The diagnosed recovery reused three
terminal results and the exact archived job; it observed only four remaining
runs and release artifact metadata. No direct-log retry or escape override was
used. The recovery utility's final prose said “incomplete” despite the fixed
command exiting zero and producing all seven terminal results. The
[reconciliation](followups-ci-observation-resume-090a188c-20261023T171600Z/native-final-report-reconciliation.json) records the
parent's independent validation of every raw identity and conclusion. Both
original reports remain intact; no extra CI query or operation was needed.

[Machine receipt](followups-final-ci-receipt.json) links raw snapshots, jobs and
step results, logs, artifact metadata and copy/hash proofs. No CI mutation,
local test/build/install repetition, publication, default integration, cleanup
or lifecycle action occurred. All owned commands have exited. Git, index,
hooks, source and execution ownership are yielded to the lead. Fixes remain on
the development branch; no additional release is approved.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
