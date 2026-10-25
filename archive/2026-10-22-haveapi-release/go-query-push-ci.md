# Go query correction: feature push and CI handoff

Feature branch `2026-10-22-haveapi-release` now points remotely to reviewed
`b64fb25bea8d8222fb3263b99956c0b61438a859`, tree `05384a632290653cb4560c7451b3897acd5956c8`. Fresh SSH fetch/ls-remote proved prior feature
`ee67d27419c48d27a01c83a29114adf9a82062ba` and master `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. Explicit expected-ee67 lease
and `--no-follow-tags` succeeded, exit0; after proof shows the exact final
feature head and unchanged master. Exact argv/before/after proof are in
`go-query-push-ci.json`; push output is retained in `go-query-push-ci.log` and
`go-query-push.log`. No default, release branch, tag or registry mutation.

Identity verified outside Nix and through the already-proven workspace-CLI-only
gem environment isolation. Actual Git/project hooks use normal top-level
tools-only Nix, executable Overcommit enabled without bypass. Source/index clean;
known unrelated untracked caches preserved. No source/history/hook/artifact edit,
dependency install, test/build/compile or long retry. All commands exited and
Git/source/hooks/records are yielded to lead.

## Automatic build-only release and CI snapshot

All ten exact-head workflows started automatically. Release run
`39843638181` is event `push`, branch `refs/heads/2026-10-22-haveapi-release` and exact
head `b64fb25bea8d8222fb3263b99956c0b61438a859`. No workflow_dispatch was issued because the automatic exact-head
release already exists. Workflow `.github/workflows/release.yml` blob
`35e55e56e592e646879bbfa30dbdabc0efaf1a06` is retained in `go-query-push-release-workflow.yml`.
Publication condition:

```text
github.repository == 'vpsfreecz/haveapi' && github.event_name == 'push' && startsWith(github.ref, 'refs/tags/')
```

The feature branch fails the tag requirement, so release is build-only. No
protected publish environment or registry action requested. JSON binds actual
release event/head/ref and conditional-dispatch decision. No CI wait or rerun.

| Workflow | Run | Status | Conclusion |
| --- | --- | --- | --- |
| clients/js tests | [39843638087](https://github.com/vpsfreecz/haveapi/actions/runs/39843638087) | in_progress | pending |
| clients/rust | [39843638091](https://github.com/vpsfreecz/haveapi/actions/runs/39843638091) | in_progress | pending |
| RuboCop | [39843638107](https://github.com/vpsfreecz/haveapi/actions/runs/39843638107) | completed | success |
| release | [39843638181](https://github.com/vpsfreecz/haveapi/actions/runs/39843638181) | in_progress | pending |
| clients/php PHPUnit | [39843638228](https://github.com/vpsfreecz/haveapi/actions/runs/39843638228) | in_progress | pending |
| clients/python | [39843638186](https://github.com/vpsfreecz/haveapi/actions/runs/39843638186) | in_progress | pending |
| i18n health | [39843638223](https://github.com/vpsfreecz/haveapi/actions/runs/39843638223) | completed | success |
| clients/ruby RSpec | [39843638278](https://github.com/vpsfreecz/haveapi/actions/runs/39843638278) | in_progress | pending |
| clients/go RSpec | [39843638156](https://github.com/vpsfreecz/haveapi/actions/runs/39843638156) | in_progress | pending |
| servers/ruby RSpec | [39843638240](https://github.com/vpsfreecz/haveapi/actions/runs/39843638240) | in_progress | pending |

The complete branch snapshot found no superseded active same-branch runs.
Separate fresh API view of prior ee67 JS run39841084962 reports
**completed / success**, updated `2026-10-22T19:48:25Z`; raw proof is
`go-query-push-superseded-js-fresh.json`. No cancellation requested. This is the
actual observed state, not an inference from the earlier in-progress record.
All new conclusions are only the API snapshot shown; lead owns later monitoring.

Final exact-head artifact rebuild/verification, actual full Go16-program execution
and final CI completion remain separate required evidence. Unchanged dynamic
success retains actual3fb91 and Rust dev/MSRV retains actual48543; reviewed748
unchanged inputs/nine locks/310 Rust inputs support reuse without relabeling those
executions. No new Go acceptance success is claimed by this push receipt.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
