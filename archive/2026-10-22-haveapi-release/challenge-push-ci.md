# Python login candidate: feature push and CI handoff

Only feature branch `2026-10-22-haveapi-release` pushed over SSH, exact final head
`48543f8cd254eb0fc087931a5dc98ea730fd94af`, tree `d240b01bc06f9a240e08f74452fc2700a795a0f1`. Fresh fetch/ls-remote proved expected prior
feature `ee150c8515aae399dc14e0fe9daefeb95a8bb17e` and target master `a32b15e379f44fc6dae4b15ef4ec17a142e5f465` before mutation.
Explicit force-with-lease and --no-follow-tags succeeded (exit0). Remote after
proof equals final SHA and master is unchanged. Exact argv/proof in JSON, output
in challenge-push.log. No default, release branch/tag or registry mutation.

Top-level tools-only Nix with installed Overcommit pre-push entrypoint enabled;
no disable variables or bypass. No extra PrePush checks declared; final commit
hooks already passed. Tracked source clean/index empty after push, known generated
caches preserved. No source/history/build/install/artifact mutation, no long run.
All source/Git/hooks yielded to lead for fresh immutable verification; no command
pending. Earlier records/artifacts and exact reviewed source refs preserved.

Read-only discovery snapshots follow; no CI wait or retry. Verified superseded
queued/running same-branch runs alone received cancellation requests. Each entry
records before/after actual status; a request is not claimed as final completion.
Older server Ruby run39826642565 is in_progress,
conclusion pending, based on direct
workflow status rather than successful listed jobs. See JSON for exact proof.

| Final-head workflow | Run | Status snapshot | Conclusion |
| --- | --- | --- | --- |
| release | [39831117185](https://github.com/vpsfreecz/haveapi/actions/runs/39831117185) | in_progress | pending |
| clients/rust | [39831116821](https://github.com/vpsfreecz/haveapi/actions/runs/39831116821) | queued | pending |
| servers/ruby RSpec | [39831116724](https://github.com/vpsfreecz/haveapi/actions/runs/39831116724) | in_progress | pending |
| clients/python | [39831116805](https://github.com/vpsfreecz/haveapi/actions/runs/39831116805) | completed | success |
| i18n health | [39831116580](https://github.com/vpsfreecz/haveapi/actions/runs/39831116580) | completed | success |
| clients/go RSpec | [39831116767](https://github.com/vpsfreecz/haveapi/actions/runs/39831116767) | in_progress | pending |
| RuboCop | [39831116723](https://github.com/vpsfreecz/haveapi/actions/runs/39831116723) | completed | success |
| clients/ruby RSpec | [39831116722](https://github.com/vpsfreecz/haveapi/actions/runs/39831116722) | completed | success |
| clients/php PHPUnit | [39831116644](https://github.com/vpsfreecz/haveapi/actions/runs/39831116644) | completed | success |
| clients/js tests | [39831116599](https://github.com/vpsfreecz/haveapi/actions/runs/39831116599) | completed | success |

Superseded cancellation requests: 0.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/

Cancellation anomaly: normal `gh run cancel 39826642565` exited1 with "Cannot cancel a workflow run that is completed", but direct before/after and final workflow reads still show in_progress with no conclusion. This is retained as inconsistent remote status, not prior success or confirmed cancellation. No force-cancel, repeated attempt or CI wait. Lead/watcher owns follow-up.
