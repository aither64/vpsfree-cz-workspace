# Frozen-head hosted verification checkpoint

This head has a diagnosed direct-comparator source-proof normalization defect.
The lead authorized C's narrow fix and composition regression. **No numeric
results are accepted.** The watcher plan below is historical and must not be
launched for acceptance. Old ae60 runs/evidence remain preserved; capture
available weekly evidence before any authorized post-successor cancellation.
[Successor publication/cancellation preparation](../../api-performance-hosted-successor-plan.md)
governs the next phase; no new publication, status query or dispatch was run in
this preparation continuation.

Latest authorized checkpoint, 2026-10-25T10:50:17Z: one manual-quick status
read established completed **failure** for 40186001987 attempt1. Complete
[run JSON](manual-quick/bounded-status/run.json),
[status receipt](manual-quick/bounded-status/receipt.json),
[attempt logs](manual-quick/bounded-status/logs.zip),
[jobs/steps](manual-quick/bounded-status/jobs.json) and
[original artifact](manual-quick/bounded-status/artifact.zip) retained.
Artifact API SHA256 `524b1bbbc274acf7146460f40851b4212c23aeff9d1efa14331f3bf24dad006d`
was verified; artifact 12596023231 retains 30-day expiry. Exact head/event/branch
are authoritative; the actual retained `event.json` inputs and `selection.json`
match candidate ae60, fixed b85 and quick profile. See
[artifact/input receipt](manual-quick/bounded-status/artifact-receipt.json).

The runner finished writing samples and worker receipts, then returned exit3:
`HaveAPI::Performance::ContractError: Invalid comparison input: key not found: "sha"`.
[Original error report](manual-quick/bounded-status/artifact/results/report.json)
and stderr preserve source SHAs/profile. The paired-run step and aggregate
failed; source resolution, setup and artifact upload succeeded. No classifications
or measurements are accepted. D reported the blocking failure and routed exact
samples/worker evidence to C for comparator diagnosis; no source change/retry.

Because quick was terminal, the separately authorized weekly attempt was sent
once and accepted exit0 as run **40186402016**:
https://github.com/vpsfreecz/haveapi/actions/runs/40186402016 .
[Exact command/output/exit receipt](manual-weekly/dispatch-receipt.json) binds
candidate `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`, reference
`b85ec364057f536940d689b09e612512ffffaf82`, profile `weekly`, and feature ref.
Neither manual dispatch was refused. Weekly authoritative run/event/head/input
validation and final conclusion await its fresh watcher window; no weekly
status read was made. No further push snapshot or CI polling loop was launched.
The original publication/snapshot below is preserved as historical evidence.

Publication completed at 2026-10-25T10:43:17Z. Full head `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`,
tree `e83aff21574490a79282f58fc5cbe28bb2d8170b`, branch
`2026-10-24-context-copy-performance-tests`; remote SSH feature ref matches.
Fetch and merge-base both bind unchanged origin/master
`39909094649b1d14a23f00615775ca7136acf4fd`. Fixed reference
`b85ec364057f536940d689b09e612512ffffaf82` is an ancestor.
Feature-only non-force push, normal Nix environment and active Overcommit hook;
all commands exit0, no overrides or installation. Worktree/index clean and
reviewed source/tree unchanged after publication. Git window relinquished
immediately and reported to lead. Complete logs/commands/exits:
[publication receipt](publication/receipt.json). Published workflow/budgets/
flake inputs retained with [hash manifest](published-inputs/manifest.json).
Final independent review/range: [review packet](../../api-performance-review-packet.md),
[review report](../../api-performance-review-report.md); lead additionally
accepted both narrow fixes at this exact head.

## One bounded push snapshot

Captured once at 2026-10-25T10:44:06Z; all eleven entries have exact frozen head,
branch and push event. This is a snapshot, not final CI acceptance.

| Workflow | Run ID | Snapshot status | Snapshot conclusion |
| --- | --- | --- | --- |
| clients/rust | 40185931122 | in_progress | pending |
| servers/ruby RSpec | 40185931163 | in_progress | pending |
| release | 40185931077 | in_progress | pending |
| servers/ruby performance | 40185931208 | in_progress | pending |
| clients/go RSpec | 40185931182 | in_progress | pending |
| i18n health | 40185931090 | completed | success |
| clients/php PHPUnit | 40185931094 | completed | success |
| RuboCop | 40185931105 | completed | success |
| clients/ruby RSpec | 40185931164 | completed | success |
| clients/js tests | 40185931083 | completed | success |
| clients/python | 40185931108 | completed | success |

[Original run JSON](push/runs-initial.json) and
[snapshot command/time/exit receipt](push/snapshot-receipt.json) are retained.
No polling loop or CI watcher has been started.

## Manual dispatch

Explicit quick accepted exit0 at 2026-10-25T10:44:22Z:
https://github.com/vpsfreecz/haveapi/actions/runs/40186001987 . Exact inputs:
`candidate_sha=ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`,
`baseline_sha=b85ec364057f536940d689b09e612512ffffaf82`, `profile=quick`.
[Full command/output/exit receipt](manual-quick/dispatch-receipt.json).
This was accepted; no absent-default refusal occurred for quick. The actual
run's event/head/branch and resulting selection/report still require validation.

Weekly was initially deferred because workflow_dispatch runs on this branch
share a cancellation concurrency group. After the one authorized read established
quick completion, weekly was submitted once as recorded above. No rerun,
cancellation, workaround or default integration was performed.

PR/default/Sunday scheduled executions remain unexecuted; local resolver tests
cover their selection semantics and do not establish hosted execution.

## Fresh watcher plan, not launched

Wait for the lead to grant the single utility slot after A/C. Resolve retained
verification utility/native configuration and installed execution policy afresh
as required by the dev-session-monitor skill; fresh context, Luna/low, no old
utility reuse. Use [frozen run list](watch-runs.json), never a moving branch query.
Candidate checkout/worktree is read-only for the watcher; no Git mutation,
installation, dispatch, rerun, cancellation, diagnosis or source edit.

For each of the eleven push IDs and manual weekly ID 40186402016:

Manual quick 40186001987 is already terminal failure with complete retained
attempt1 evidence; do not launch another wait or rerun for it.

1. Capture `gh run view ID --repo vpsfreecz/haveapi --json databaseId,workflowName,event,headSha,headBranch,status,conclusion,url,jobs`
   under `watch/run-ID-before.json`. Require exact head `ae60e0fdbc892d248c1cd4bff9a52ee74a0cfc43`,
   branch `2026-10-24-context-copy-performance-tests`, expected workflow and event
   (`push` for eleven; `workflow_dispatch` for weekly). Stop on mismatch.
2. Observe only this existing run with `gh run watch ID --repo vpsfreecz/haveapi --exit-status`.
   Retain exact stdout/stderr/exit under `watch/run-ID-watch.*`; do not replace
   this status with subsequent log-command exits or invent a wait timeout.
3. Capture final metadata/jobs to `watch/run-ID-final.json`, full log to
   `watch/run-ID.log`, and command exits independently. On failure return
   promptly with raw evidence, identifying any batch runs not yet observed.
4. For performance IDs 40185931208 and 40186402016, retain authoritative run
   details/attempt and available artifact metadata for D's independent download
   and provenance/response/counter/classification analysis. Successful workflow
   conclusion alone does not establish report acceptance.

D owns diagnosis after watcher returns; no parent polling alongside watcher.
All timing/error/inconclusive gates stay unchanged. Weekly dispatch is accepted; do not send it again. D requests a fresh
watcher window after A/C and preserves the known quick failure for diagnosis.
No final hosted pass is accepted for the five initially pending push runs or
weekly; quick is a known blocking failure.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-24-context-copy-performance-tests/
