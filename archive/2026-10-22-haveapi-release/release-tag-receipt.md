# Official HaveAPI 0.30.0 refs and publication handoff

Exact reviewed/integrated source `b64fb25bea8d8222fb3263b99956c0b61438a859`, tree `05384a632290653cb4560c7451b3897acd5956c8`.
Authorized user direction and publisher confirmations: `release-authorization.md`.
Integration succeeded through the short single HaveAPI repository claim, with
normal ff-only merge and SSH master push. Exact claim
`a30d80f5-7287-4586-9bdd-67afc2b84d32` was explicitly released and
verified before CI/records and independently rechecked before release-ref work.
Master integration proof is `release-integration-execution.json` and receipt.

## Official branch and tag

Only after reconciled remote master==reviewedb64 and releasedclaim, rechecked
clean exact source/index, version0.30.0, source ancestry, absent local/remote
haveapi-0.30/v0.30.0 and newest release line0.29. Existing refs were not overwritten.
Created `haveapi-0.30` at `b64fb25bea8d8222fb3263b99956c0b61438a859` and annotated `v0.30.0` at the same commit.
Annotation `Version 0.30.0` came from a temporary message file. No new sourcecommit
or version change. Declared hooks/signatures enabled in root tools-onlyNix.

Atomic explicit SSH push of only new releasebranch+tag succeeded, exit0:

```sh
git push --atomic --no-follow-tags origin \
  refs/heads/haveapi-0.30:refs/heads/haveapi-0.30 \
  refs/tags/v0.30.0:refs/tags/v0.30.0
```

No force, movement of existing tag, registry action or protected approval.
Remote branch points to `b64fb25bea8d8222fb3263b99956c0b61438a859`. Remote tag object is
`81a896f97b75781f62c5850a6e8df7932c92782b`, type tag, peeled exactly to `b64fb25bea8d8222fb3263b99956c0b61438a859`.
Master and retained feature both remain the sameb64. Exact before/after refs,
argv, source and releasedclaim proof in `release-tag-execution.json`; push output
in `release-tag-push.log`. No uncertain mutation remains. Existing other-session
mastercheckout untouched. Disposabletarget/feature/dist/evidence retained.

## Exact tag-triggered release

**[Release run39849807897](https://github.com/vpsfreecz/haveapi/actions/runs/39849807897)**,
event `push`, ref `v0.30.0`, head `b64fb25bea8d8222fb3263b99956c0b61438a859`, workflow
`.github/workflows/release.yml`. Official API identity is retained in
`release-tag-release-run.json`. Snapshot status `in_progress` /
`pending` is not completion or publication proof.
No workflow_dispatch, rerun or cancellation was issued. Lead and fresh policy
watcher own subsequent observation and protected publication approval.

| Tag workflow | Run | Event | Status | Conclusion |
| --- | --- | --- | --- | --- |
| RuboCop | [39849807971](https://github.com/vpsfreecz/haveapi/actions/runs/39849807971) | push | completed | success |
| i18n health | [39849808330](https://github.com/vpsfreecz/haveapi/actions/runs/39849808330) | push | completed | success |
| clients/rust | [39849808244](https://github.com/vpsfreecz/haveapi/actions/runs/39849808244) | push | in_progress | pending |
| clients/go RSpec | [39849808688](https://github.com/vpsfreecz/haveapi/actions/runs/39849808688) | push | in_progress | pending |
| servers/ruby RSpec | [39849808638](https://github.com/vpsfreecz/haveapi/actions/runs/39849808638) | push | in_progress | pending |
| clients/php PHPUnit | [39849808278](https://github.com/vpsfreecz/haveapi/actions/runs/39849808278) | push | completed | success |
| clients/python | [39849808059](https://github.com/vpsfreecz/haveapi/actions/runs/39849808059) | push | completed | success |
| clients/ruby RSpec | [39849808547](https://github.com/vpsfreecz/haveapi/actions/runs/39849808547) | push | completed | success |
| release | [39849807897](https://github.com/vpsfreecz/haveapi/actions/runs/39849807897) | push | in_progress | pending |
| clients/js tests | [39849807922](https://github.com/vpsfreecz/haveapi/actions/runs/39849807922) | push | completed | success |

## Master/releasebranch discovery

| Master workflow | Run | Event | Status | Conclusion |
| --- | --- | --- | --- | --- |
| Dependabot Updates | 39849766175 | dynamic | completed | failure |
| Dependabot Updates | 39849766962 | dynamic | completed | failure |
| Dependabot Updates | 39849767818 | dynamic | completed | failure |
| Dependency Graph | 39849476163 | dynamic | completed | success |
| servers/ruby RSpec | 39849448544 | push | completed | success |
| clients/go RSpec | 39849448508 | push | completed | success |
| clients/rust | 39849448313 | push | in_progress | pending |
| RuboCop | 39849448451 | push | completed | success |
| release | 39849448372 | push | in_progress | pending |
| i18n health | 39849448358 | push | completed | success |
| clients/php PHPUnit | 39849448321 | push | completed | success |
| clients/ruby RSpec | 39849448388 | push | completed | success |
| clients/js tests | 39849448316 | push | completed | success |
| clients/python | 39849448330 | push | completed | success |

No separate `haveapi-0.30` branch run was observed in this snapshot. Tag and master
pushes are distinct execution records even with identical source. Automatic
DependencyGraph result and three dynamic Dependabot Updates failures are retained
as observed; those are separate metadata jobs, not the ten maintained push checks.
No diagnosis/retry requested. Lead accepted this distinction and owns escalation
only if a concrete release effect appears.

Raw exacthead discovery: `release-tag-ci-discovery.json`; grouped immutable
snapshot: `release-tag-ci.json`. No CI wait or duplicate polling after watcher
handoff. All Git/source/hooks/record commands have exited. No local build/tests,
dependency install, artifact modification, deployment, cleanup or session lifecycle
action. Existing final12 artifact hashes and original review/execution/inputgraphs
remain retained. The tag-triggered workflow's own retained candidate and protected
approval are required before claiming packages published; no such claim here.

Session: https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-22-haveapi-release/
