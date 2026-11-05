# CI corrections

## Native Job rendering correction

The completed local correction is consolidated at
`ee3f1fdd0d3585a8f4fa9b952169d692e9fa3d5f`, tree
`e52d2aa3da60fcf2e5d563b7606c98e7ef844180`. It remains unpublished, with a clean
runtime worktree/index. Its complete three-commit series retains the original UI
commit, folds the two-file fix into core `f7add7ce`, and preserves the dependent
portal patch unchanged. The old published `7302f4dc` and direct fixup `bb87e2e9`
are retained under session refs. No migrations, schema, API or command-flag change
was introduced. The runtime Git lane is returned for lead inspection and the
applicable review; no native check, push, pin update or deployment was performed.

CI run 41526190428 passed fast/package and native creation at exact `7302f4dc`.
Archive reached its first registered service launch after the prior browser revive
case passed. Its retained [archive log](tracking/runtime-ci-7302f4dc/failed-archive-job.log)
records the service Starting/Started, then `service manager job state unavailable`
at lines 5586–5593. Earlier PermissionDenied was the expected interrupted-recovery
fixture. The failure log SHA256 is
`2c8c8bcdda778d6edbf3ee0746297ef50173af04599cb1c1d6bf8b64cf9b5d9c`.

The VM runs systemd 260.2. The architect's
[source-backed clarification](design.md#native-job-formatting-clarification-2602-fixture-failure)
establishes that the exact explicit-property command renders the native no-job
tuple as `Job=`. The fixture instead supplied `Job=0`, and the parser rejected
the native rendering. The VM did not capture raw `show` output, so the precise
failed value is source-derived rather than directly observed. Changing only the
fixture rendering reproduced the identical first-launch error locally.

The parser now normalizes only a present empty Job value to its internal `'0'`.
Missing, bare, null-text, whitespace and malformed values still refuse; canonical
positive IDs remain pending. Strict InvocationID equality, uncertain/unobserved
launch handling, native-job settlement and expected-cgroup proof are unchanged.
No reusable documentation change was useful beyond the nearby parser comment:
the existing recovery guide already requires these proofs.

| Quick check | Result |
| --- | --- |
| Native-empty fixture against original parser | Expected red: exact launch error, 1 test/4 assertions |
| Focused raw-value, pending/unloaded, InvocationID and uncertain-launch checks | 7 tests/118 assertions passed |
| All service tests, standalone | 32 tests/466 assertions passed in 21.91 s |
| Aggregate loading, all service tests plus both original bad-root tests | 34 tests/478 assertions passed in 22.38 s |
| Both changed Ruby syntax checks and diff whitespace | Passed |
| Same focused smoke at final consolidated commit | 7 tests/118 assertions passed in 1.49 s |

The [final receipt](tracking/runtime-ci-7302f4dc/job-parser-consolidated-receipt.json)
binds exact commands, source metadata/full lock graph, checksums and preserved
refs. The [range diff](tracking/runtime-ci-7302f4dc/job-parser-range-diff.txt)
shows only core changed; the [final delta](tracking/runtime-ci-7302f4dc/job-parser-final-delta.patch)
is two files, 71 insertions/3 deletions. Fixup and consolidated trees are identical.
Normal commit used a temporary message file, with no declared hook framework,
active hooks or bypass. No owned command remains running.

Final source is `/nix/store/8ygzal9j12xj6x600ws7yrhgn1ijngx2-source`, NAR
`sha256-5mDdLgLQl/XPjIs9Ey5l2UDxWwVKR/VWpNCQwEvqsiw=`. The lock and complete input
graph are unchanged. These quick proofs do not claim native execution or reuse
of the earlier packaged Ruby result for changed inputs. After source acceptance
and applicable review, the existing exported `session-archive-lifecycle` check is
the shortest affected native proof. Old 7302 pins and prepared system/site artifacts
remain held at their actual scope.

## Earlier Ruby shard failure correction

The narrow correction is committed at
`d13751ffb615ef2af930ea8a22979d04394bd4a5`, tree
`9b93683362e149ba6f2599232bc1fbbbe4694a17`, directly above published runtime
`312d2e2a8994c136f96938d2f2a71ae8e2f16f33`. It is an unpushed core fixup:
three owned files, 71 insertions and five deletions. No rebase, pin refresh,
deployment or live service/lifecycle action was performed.

## Diagnosis and correction

CI run [41503878011](https://github.com/aither64/dev-workspace/actions/runs/41503878011)
failed before any native VM ran. The complete logs/result remain in
[runtime-ci-312d2e2a/](runtime-ci-312d2e2a/result.json).

The two existing bad-recovery-root tests failed because the new lifecycle-access
reader asked the strict service Store for a prelude even when no prelude existed.
That probed a registry below an invalid state-root ancestor and raised `ENOTDIR`
before ordinary deletion could report its existing recovery-location refusal.
The access reader now checks the exact workspace prelude path first. Present
preludes still receive the complete strict registry/identity validation.

Only `ENOENT` means absence in the service file-owner reader. Other filesystem
errors become `WorkspaceSessionServices::Error`, retaining their typed cause.
The existing Runner lifecycle-access boundary maps service-owner errors to
`DevSession::Error`, as the service CLI boundary already does. Unknown state
still refuses; no ownership/schema changes or error inheritance tricks were used.

The partial-transfer test's first expected stop failure was not its CI failure.
The second invocation failed before reaching the intended evidence-unlink fault.
Its fixture gave real filesystem writes and scheduling a 150 ms wall deadline.
A controlled 200 ms delay after the successful retry stop reproduced the exact
failure in both standalone and aggregate loading, with the underlying cause
`service observation deadline exceeded`. CI's printed wrapper stack alone did
not expose this inner cause. The controlled reproducer and source establish the
timing defect; no aggregate load-order dependence was found.

The component fixture now advances monotonic time only during simulated polling.
It retains explicit deadline-expiry assertions, including a new timed-out stop
followed by successful deletion recovery. A delayed successful retry now reaches
the intended partial-transfer fault and completes its existing retry proof.
Production's 20-second bound and native systemd stop/cgroup proof are unchanged.

## Focused evidence

| Check | Result |
| --- | --- |
| Original bad-root tests, standalone with their existing NullTmux support loaded | 2 tests, 12 assertions, passed |
| Standalone transfer/expiry/invalid-prelude/inventory proofs | 4 tests, 71 assertions, passed |
| Aggregate loading: all 29 service tests plus both original bad-root tests | 31 tests, 395 assertions, passed in 20.69 s |
| Delayed successful retry, standalone | 1 test, 23 assertions, passed |
| Delayed successful retry, aggregate loading | 1 test, 23 assertions, passed |
| Changed Ruby syntax and complete diff whitespace | Passed |

Logs preserve baseline failures and final proof:

- [ci-remediation-baseline.log](ci-remediation-baseline.log).
- [ci-remediation-cause.log](ci-remediation-cause.log).
- [ci-remediation-quick.log](ci-remediation-quick.log).
- [ci-remediation-delayed-retry.log](ci-remediation-delayed-retry.log).
- [ci-remediation-diff.patch](ci-remediation-diff.patch).
- [ci-remediation-commit.json](ci-remediation-commit.json).

The standalone deletion file depends on `NullTmux` from the existing lifecycle
component. Its first direct run exposed that missing preload; the corrected
focused command preloads that support. No fixture-support refactor was added.

Normal Git commit used a temporary message file. This repository declares no
hook framework and had no active hooks. The resulting index/worktree was clean.
No reusable documentation change was needed: this restores the documented strict
error and recovery contract. The lead accepted the diagnostic wording and narrow
source correction and directly inspected the exact committed diff, confirming
no schema, API or ownership expansion.

## Actual packaged shard verification

One fresh Luna/low utility owns the exported Ruby shards 0, 2 and 3. The command,
source/input graph, exact filtered Ruby input, recursive derivations, outputs and
watcher launch policy are recorded under
[ci-remediation-shards/manifest.json](ci-remediation-shards/manifest.json) and
[ci-remediation-shards/launch.json](ci-remediation-shards/launch.json).
The exact command passed in 224.761 seconds (exit zero). Parent verification
confirmed complete per-shard timing manifests, unique selected test execution,
all three original failing tests included, and each output's exact expected
deriver. The committed source and lock remained unchanged and the checkout clean.

| Exported check | Tests | Assertions | Skips |
| --- | --- | --- | --- |
| `ruby-dev_session-0` | 126 | 1,380 | 4 |
| `ruby-dev_session-2` | 128 | 1,958 | 4 |
| `ruby-dev_session-3` | 136 | 1,943 | 3 |
| Total affected shards | 390 | 5,281 | 11 |

There were zero failures or errors. This proves the three affected shards;
shard 1 and full four-shard coverage are not claimed. The configured skips and
native VM checks remain separate from this component verification.

The final source is `/nix/store/snbsx4bqra8nkr8qsy6h13mydriq79sj-source`, NAR
`sha256-f3UjSBS9+zyEULhOdBjiBG04aDiqTKNsjzuwokIYzJ4=`. Its filtered Ruby
input is `/nix/store/032kq2fwxbidrsaavf38vwskkrckd3v6-dev-workspace-ruby-source`,
NAR `sha256-YofCVP7YhwSMX2ynV8e/hD0vh4y1dPARm0uXvr2cxgQ=`. The complete
flake graph and unchanged lock, recursive derivations and output metadata are
retained in the operation directory. The verified receipt is
[ci-remediation-shards/verified-result.json](ci-remediation-shards/verified-result.json).

Build log SHA256:
`586b8b6fcdb084ebc70eb484dc934972a22b7a0ac925e474934dfcd2db0561ca`.
Watcher result SHA256:
`a8dbbb5ce901ac45263510825297b3e67bd348a5d4b97ce52163f072ae308e8d`.
Recursive derivation receipt SHA256:
`d5ff3b20d01f39941cbbc7301d7fb43b27297dade73e7fa87a3048af03028898`.

The fresh watcher `/root/ci_ruby_shards_correction` reported its owned build
exited; no cancellation or running operation remains. The utility slot and
runtime Git lane are returned to the lead. Source/Git remain idle pending the
lead's coordinated consolidation/publication package. No VM, browser,
full-package or CI rerun was part of this component operation.

The earlier configuration pin `7b6d1a12` and workspace pin `25282ddfc` are held
as stale evidence, including their successful old cross-lock check. They must
be replaced and consolidated into each stream's single final pin after a
corrected runtime is published under the lead's later grant.

Stable session:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-02-session-temporary-service-cleanup/
