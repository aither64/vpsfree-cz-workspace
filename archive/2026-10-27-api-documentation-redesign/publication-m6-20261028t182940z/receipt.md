# M6 development branch publication

Published exact reviewed HaveAPI `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9` (tree
`ed2764be21718b64e8f9f1bf9e2480798beaa18d`) to `refs/heads/2026-10-27-api-documentation-redesign` over canonical
SSH `git@github.com:vpsfreecz/haveapi.git`. Fresh post-push SSH readback verifies that full SHA.
Master stayed `f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0` before and after publication.

The fresh fetch and SSH ref inspection found feature at exact expected
`35c1fb964735639c0873aacf078e18569f05f9bc` and the intended recovery branch absent.
One atomic push created `refs/heads/recovery/2026-10-27-api-documentation-redesign-published35c-20261028t180031z` at that exact old published head
and updated only the session feature to M6. It used explicit full-SHA refspecs,
--no-follow-tags, the exact expected-old feature lease and an empty expected-old
recovery lease. No foreign ref was replaced. Local35c recovery remains exact.
Old publication reports and all previous refs/receipts remain retained.

Exact commands, exits and elapsed time are in fetch.execution.json and
push.execution.json; logs and before/after remote ref maps are adjacent. Push
exited0; all network mutation effects are reconciled. No repository merge claim
was acquired for this independent feature publication. No default branch, tag,
version metadata, registry, release, consumer or peer source was changed.

The existing executable Overcommit pre-push hook remained active and unchanged,
without bypass or reconfiguration. The tools-only declared root Nix shell and
frozen prepared tools graph passed bundle check; Nix realized its declared
store closure as recorded in push.log, without gem/component installation,
lock refresh or source-input changes. No new test batch was launched.

Final independent review milestone6-final-review.md binds the exact f6..a06b
five-commit range/tree, retained reviewer0 Sol/xhigh, all4 lanes, no new findings.
Publication provides an immutable development source, not full gate readiness.

## Single CI observation

Observed at `2026-10-28T18:31:02.696617+00:00` exactly once. Every row is a push event on
this session feature branch with full head `a06b0cfa2abd7560f10cb58ebe99d8eb3f10b8f9`.
Statuses below are that observation only; no CI wait or watcher was started.

| Run ID | Workflow | Observed status | Conclusion |
| --- | --- | --- | --- |
| [40745814300](https://github.com/vpsfreecz/haveapi/actions/runs/40745814300) | clients/js tests | in_progress | pending |
| [40745814365](https://github.com/vpsfreecz/haveapi/actions/runs/40745814365) | RuboCop | queued | pending |
| [40745814328](https://github.com/vpsfreecz/haveapi/actions/runs/40745814328) | servers/ruby RSpec | queued | pending |
| [40745814572](https://github.com/vpsfreecz/haveapi/actions/runs/40745814572) | clients/go RSpec | queued | pending |
| [40745814325](https://github.com/vpsfreecz/haveapi/actions/runs/40745814325) | i18n health | completed | success |
| [40745814060](https://github.com/vpsfreecz/haveapi/actions/runs/40745814060) | servers/ruby performance | in_progress | pending |
| [40745814069](https://github.com/vpsfreecz/haveapi/actions/runs/40745814069) | clients/rust | in_progress | pending |
| [40745814145](https://github.com/vpsfreecz/haveapi/actions/runs/40745814145) | release | in_progress | pending |
| [40745814262](https://github.com/vpsfreecz/haveapi/actions/runs/40745814262) | clients/python | in_progress | pending |
| [40745814376](https://github.com/vpsfreecz/haveapi/actions/runs/40745814376) | clients/ruby RSpec | in_progress | pending |
| [40745814315](https://github.com/vpsfreecz/haveapi/actions/runs/40745814315) | clients/php PHPUnit | in_progress | pending |

No superseded queued/in-progress run for this exact branch was found, so no
cancellation was needed. Current-head and other-branch runs were untouched.
The automatic release workflow is its ordinary branch build-only path; no tag,
dispatch, protected-environment approval or package publication occurred.
Performance run metadata does not expose its resolved baseline selection;
owner0 must reconcile the actual runner selection later. Static architect
expectation is the nonancestor35c-to-a06b quick pair, not f6; that is not claimed
as an observed execution result here. The required later f6 campaign remains
separate.

## Preservation and release

Source/head/tree/history, logical index/flags and executable pre-push hook bytes
are unchanged. All2148 protected hashes match before/after, including retained
prepared generators/MSRV/published runtime/JS/Python/frozen/preview graphs.
Local source/index are clean. No source, checkout, commit, rebase, dependency,
preview/service/provider/TLS/private-fixture/consumer/lifecycle action occurred.
No pending command or uncertain network effect remains. No watcher owns utility
capacity. Exclusive Git/remote slot RELEASED with the report. Lead owns later
peer handoff and separately granted verification; no merge or release approval
is inferred.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
