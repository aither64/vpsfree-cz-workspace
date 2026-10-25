# Go wire correction: feature push and CI handoff

Feature branch `2026-10-22-haveapi-release` now points remotely to exact reviewed
`ee67d27419c48d27a01c83a29114adf9a82062ba`, tree `2e0d29769aff48b484c1ac331b11255d22abd0ae`. Fresh SSH fetch/ls-remote before push proved
feature `3fb91caf783eaeacf49bf3647b8409d536339d71` and master `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. The explicit
lease and `--no-follow-tags` succeeded, exit0; after proof shows the exact final
feature head and unchanged master. Exact argv/remote proof are in
`go-wire-push-ci.json`; complete push output is retained in `go-wire-push-ci.log`
and `go-wire-push.log`. No default, release branch, tag or registry mutation.

Top-level tools-only Nix and executable declared Overcommit hooks stayed enabled
without bypass. Final source/index checks passed; known untracked caches remain.
No source/history/hook/artifact edit, dependency install, build, test, compile or
long retry was performed. Git/source/hooks and all commands are yielded to lead.

The first redundant inside-Nix session check failed before fetch/push because
the workspace CLI inherited HaveAPI GEM_HOME native extensions. Only that CLI
subprocess's GEM_HOME/GEM_PATH/BUNDLE_GEMFILE were isolated, after the ordinary
outside-shell binding check passed. The actual Git/Overcommit environment stayed
unchanged. Exact explanation and initial driver are preserved separately.

## Automatic build-only release

All ten exact-head workflows started automatically. Release run
`39841084945` has event `push`, branch ref `refs/heads/2026-10-22-haveapi-release`
and head `ee67d27419c48d27a01c83a29114adf9a82062ba`. No workflow_dispatch was issued because an automatic exact-head
release run already existed. Reviewed workflow `.github/workflows/release.yml`
blob `35e55e56e592e646879bbfa30dbdabc0efaf1a06` is retained in
`go-wire-push-release-workflow.yml`. Publication condition:

```text
github.repository == 'vpsfreecz/haveapi' && github.event_name == 'push' && startsWith(github.ref, 'refs/tags/')
```

This feature branch fails the tag condition. The run is build-only; no protected
publication environment or registry action was requested. JSON records the exact
automatic event/head/ref and conditional dispatch decision. No CI wait or rerun.

## Exact-head CI discovery snapshot

| Workflow | Run | Status | Conclusion |
| --- | --- | --- | --- |
| clients/python | [39841085266](https://github.com/vpsfreecz/haveapi/actions/runs/39841085266) | in_progress | pending |
| RuboCop | [39841085304](https://github.com/vpsfreecz/haveapi/actions/runs/39841085304) | in_progress | pending |
| clients/rust | [39841085155](https://github.com/vpsfreecz/haveapi/actions/runs/39841085155) | queued | pending |
| clients/go RSpec | [39841085152](https://github.com/vpsfreecz/haveapi/actions/runs/39841085152) | in_progress | pending |
| clients/js tests | [39841084962](https://github.com/vpsfreecz/haveapi/actions/runs/39841084962) | in_progress | pending |
| clients/php PHPUnit | [39841085033](https://github.com/vpsfreecz/haveapi/actions/runs/39841085033) | in_progress | pending |
| clients/ruby RSpec | [39841085117](https://github.com/vpsfreecz/haveapi/actions/runs/39841085117) | in_progress | pending |
| release | [39841084945](https://github.com/vpsfreecz/haveapi/actions/runs/39841084945) | in_progress | pending |
| servers/ruby RSpec | [39841084950](https://github.com/vpsfreecz/haveapi/actions/runs/39841084950) | in_progress | pending |
| i18n health | [39841084982](https://github.com/vpsfreecz/haveapi/actions/runs/39841084982) | completed | success |

No superseded active same-branch run existed, so no cancellation was requested.
The raw branch discovery snapshot is `go-wire-push-ci-discovery.json`; successes
are only those returned by that snapshot. Later monitoring belongs to lead.

Final artifact build/verification and actual16-program Go compile/run acceptance
remain separate required evidence. Dynamic installed wheel/sdist/npm results
retain actual3fb91 identity; Rust dev/MSRV retains actual48543 identity. Reviewed
748 unchanged entries/nine live locks/310 original Rust inputs support reuse;
none is relabeled as literal final-head execution.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
