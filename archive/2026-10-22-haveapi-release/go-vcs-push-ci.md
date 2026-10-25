# Final Go harness candidate: feature push and CI handoff

Only feature branch `2026-10-22-haveapi-release` pushed over SSH at exact reviewed
`3fb91caf783eaeacf49bf3647b8409d536339d71`, tree `8698b4a7b707b2c165877931071d31505f346370`. Fresh fetch/ls-remote before push proved prior
feature `48543f8cd254eb0fc087931a5dc98ea730fd94af` and master `a32b15e379f44fc6dae4b15ef4ec17a142e5f465`. Explicit lease and
--no-follow-tags succeeded, exit0. Remote after proof matches final SHA and
unchanged master. Exact argv/remote proof are in go-vcs-push-ci.json; complete
push output is go-vcs-push.log. No default/release branch/tag/registry mutation.

Top-level tools-only Nix, executable Overcommit entrypoint enabled with no disable
or bypass. No extra PrePush checks declared; final commit hooks already passed.
Tracked source clean/index empty, no source/history/artifact edits or local
build/install/tests. No pending command; Git/source/hooks yielded to lead for the
fresh final verification batch. All previous receipts/refs/artifacts preserved.

## Automatic release run and conditional dispatch decision

Actual exact-head automatic release run is 39836913496, event push,
ref refs/heads/2026-10-22-haveapi-release. All ten workflows actually started automatically.
No workflow_dispatch command was issued because the authorized dispatch was
conditional on automatic release being absent. This avoids a duplicate build.
The reviewed workflow source is .github/workflows/release.yml at source head
3fb91caf783eaeacf49bf3647b8409d536339d71, blob 35e55e56e592e646879bbfa30dbdabc0efaf1a06. Its publication condition is:

```text
github.repository == 'vpsfreecz/haveapi' && github.event_name == 'push' && startsWith(github.ref, 'refs/tags/')
```

The branch ref fails the tag requirement, so this run is build-only; no protected
publication environment or registry action was requested. JSON records the exact
automatic event/head/ref and dispatch-skipped decision, not invented dispatch
arguments or a second run. No CI wait, retry or job rerun.

## Exact-head CI discovery snapshot

| Workflow | Run | Status | Conclusion |
| --- | --- | --- | --- |
| clients/go RSpec | [39836913912](https://github.com/vpsfreecz/haveapi/actions/runs/39836913912) | in_progress | pending |
| release | [39836913496](https://github.com/vpsfreecz/haveapi/actions/runs/39836913496) | in_progress | pending |
| clients/rust | [39836913470](https://github.com/vpsfreecz/haveapi/actions/runs/39836913470) | in_progress | pending |
| RuboCop | [39836913532](https://github.com/vpsfreecz/haveapi/actions/runs/39836913532) | completed | success |
| i18n health | [39836913580](https://github.com/vpsfreecz/haveapi/actions/runs/39836913580) | completed | success |
| clients/php PHPUnit | [39836913551](https://github.com/vpsfreecz/haveapi/actions/runs/39836913551) | completed | success |
| clients/ruby RSpec | [39836913585](https://github.com/vpsfreecz/haveapi/actions/runs/39836913585) | completed | success |
| clients/js tests | [39836913477](https://github.com/vpsfreecz/haveapi/actions/runs/39836913477) | completed | success |
| clients/python | [39836913457](https://github.com/vpsfreecz/haveapi/actions/runs/39836913457) | completed | success |
| servers/ruby RSpec | [39836913590](https://github.com/vpsfreecz/haveapi/actions/runs/39836913590) | completed | success |

No superseded queued/running same-branch candidates existed; no cancellation.
Raw initial/final discovery snapshots are retained. Snapshot successes are only
those API conclusions shown; remaining runs belong to the lead's monitor.
Final local artifact/Go acceptance and CI completion remain separate evidence.
Earlier dynamic/Rust successes retain actual tested48543 identity and separate
310-blob/tool-graph proof; no false final-head execution claim.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
