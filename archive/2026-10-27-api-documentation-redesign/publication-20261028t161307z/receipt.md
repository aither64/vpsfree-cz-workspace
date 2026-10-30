# Development branch publication

Published only `refs/heads/2026-10-27-api-documentation-redesign` over canonical SSH
`git@github.com:vpsfreecz/haveapi.git` at exact reviewed head
`35c1fb964735639c0873aacf078e18569f05f9bc`, tree
`756b61de87833d8ded478b5d7785618671b4ddcb`. Fresh remote SSH readback confirms that SHA.

Fresh upstream before publication and the post-push remote master both equal
`f6e5c3750c747b33ec869c54ca220bf6f1d9d2d0`. The feature branch was absent before push;
no old remote feature existed to preserve or replace. The push used an explicit
empty expected-old lease (branch must remain absent), explicit full source SHA,
and disabled following tags. No blind force, default-branch write, tag, registry
publication, PR or release was performed. All existing local recovery refs and
receipts remain unchanged.

Actual command/exit/timing are in `push.execution.json`, stdout/stderr in
`push.log`; SSH before/after refs are in `remote-before.txt` and
`remote-after.txt`. Push exited0 and its effects are reconciled. No repository
merge claim was needed or acquired for this independent feature publication.

The declared Nix environment used its existing tools-only switch and frozen root
bundle; availability passed. The installed executable ordinary pre-push hook
remained active, with no bypass option or hook configuration change. It reported
no applicable pre-push check output. Prior mandatory commit hooks/review/quicks
remain their own evidence; no broad test was repeated for publication.

Review: `../milestone5-final-review.md`, retained reviewer0 Sol/xhigh, all4lanes,
exact f6..35c range, no remaining source findings; R1/R2 source findings closed.
Publication supplies the requested immutable development-source pin and does
not claim completed browser/compiler/wire/performance/provider acceptance.

## One CI metadata observation

All runs below are `push` events on this exact feature branch and full head
`35c1fb964735639c0873aacf078e18569f05f9bc`. Their statuses are the single observation, not current-result
claims after a wait. Full IDs/head/URL/timestamps are in `ci-runs-once.json`.

| Run ID | Workflow | Observed status | Conclusion |
| --- | --- | --- | --- |
| [40723979827](https://github.com/vpsfreecz/haveapi/actions/runs/40723979827) | clients/js tests | in_progress | pending |
| [40723979663](https://github.com/vpsfreecz/haveapi/actions/runs/40723979663) | clients/rust | in_progress | pending |
| [40723979876](https://github.com/vpsfreecz/haveapi/actions/runs/40723979876) | release | in_progress | pending |
| [40723979715](https://github.com/vpsfreecz/haveapi/actions/runs/40723979715) | servers/ruby performance | in_progress | pending |
| [40723980008](https://github.com/vpsfreecz/haveapi/actions/runs/40723980008) | clients/go RSpec | in_progress | pending |
| [40723980063](https://github.com/vpsfreecz/haveapi/actions/runs/40723980063) | servers/ruby RSpec | in_progress | pending |
| [40723979700](https://github.com/vpsfreecz/haveapi/actions/runs/40723979700) | clients/php PHPUnit | completed | success |
| [40723979668](https://github.com/vpsfreecz/haveapi/actions/runs/40723979668) | RuboCop | completed | success |
| [40723980034](https://github.com/vpsfreecz/haveapi/actions/runs/40723980034) | i18n health | completed | success |
| [40723979835](https://github.com/vpsfreecz/haveapi/actions/runs/40723979835) | clients/python | completed | success |
| [40723979792](https://github.com/vpsfreecz/haveapi/actions/runs/40723979792) | clients/ruby RSpec | completed | success |

No superseded queued/in-progress run for this branch was found, so no
cancellation was needed. No current-head run was cancelled. The automatically
triggered workflow named `release` is its ordinary branch build-only CI path;
publication jobs require a version-tag push under the retained workflow guard.
No tag or workflow dispatch was issued. CI was not awaited and no watcher was
started; single utility capacity remains with the lead's startup/browser owners.

## Preservation and handoff

The feature head/tree/branch and clean source/index remain unchanged. All2,148
current protected input/evidence hashes match before/after. No checkout,
rebase, commit, head move, application/index/dependency mutation or preview
service action occurred. Only the fetched remote refs/new remote branch and
session publication evidence were written. No pending command, uncertain
network mutation or watcher remains. See `final-state.json`.

Long compiler/wire/runtime/documentation/browser/performance and real-provider
acceptance remain separate grants; this publication is not full branch
readiness. Main owns the peer source-pin handoff. No peer contact, default
integration, release/registry action, private fixture/TLS, session lifecycle,
cleanup or deletion occurred. Exclusive Git/remote slot released with report.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-27-api-documentation-redesign/
