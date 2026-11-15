# Package I: disposable native preparation verification

Finalized by implementer2 on 2026-11-15. **Attempt 2 passed idle and working native
scoped preparation in 2.53 seconds; the original working turn was preserved.**
Attempt 1's harness failure and the intervening artifact-retention problem remain
recorded below. Independent product review, builds/site checks, deployment and
integration are reported by the lead, who owns rollout/state and acceptance.
Package I contains verification evidence and disposable harness work only, with
no product edits, commits or migrations.

Session binding was verified with `dev-session current` from this tracking
directory. Both DEV_SESSION identity variables were absent; the trusted developer
binding matched the exact slug/workspace. Live same-session roster confirmed
implementer2, thread `01a1de4d-2a6b-7740-a0fd-f7a682a761a9`, implementation purpose,
workspace_write, GPT-6.1 Sol/xhigh and full_access execution. No prior package.

## Inputs and ownership

- Runtime source: `git@github.com:aither64/dev-workspace.git`, exact head
  `9241a342a6ef4ca69148594e98cce7ddcfb459a6`, base
  `458c7857b942fb592607c83af7b5287a6c93ea96`.
- Own disposable boundary:
  `/tmp/2026-11-13-archive-confirmation-regression-native-verify-i`.
  `source/` is a refreshed complete `git archive` export of that head, with only the new
  `portal/cmd/workspace-portal/provider_native_verify_i_test.go` added.
  G/E/H worktrees, application source and their Git indexes are untouched.
- Fixed native executable:
  `/nix/store/2rqwqchjlv6l2nw5l491pkhvrsijn50c-codex-package-0.165.0/libexec/codex/bin/codex`.
- Exact candidate package:
  `/nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0`.
  Its `libexec/workspace-host` is a Bash wrapper. The corrected launcher loads
  the exact Ruby implementation `libexec/.workspace-host-wrapped` and invokes
  that package's `bin/workspace-portal` Go helper. There is no path fallback.
- Unchanged source lock: codex-web `91a17d00a737d59a91b5e7bb420aa89e7ec52d93`,
  llm-agents `91ff550fe42d4dd51dcf8b6bad87a0134fe7f314`. Complete graph, hashes
  and follows edges remain in the exported `flake.lock`; no lock edits.
  The deployed/composed package graph remains lead/H rollout evidence.

## Acceptance and fixture behavior

This copies E's established synthetic backend/native startup conventions and
stops at preparation. It does not enable or run `TestNativeScopedProviderSwitch`.
The dedicated build tag is `provider_native_verify_i`.

For each private fixture scope, `idle` and `working`, it creates a native lead
and one retained monitor utility. The monitor has a real native project named
for its synthetic operation, exact CWD, source `vscode`, non-ephemeral paginated
history and the exact synthetic initialization marker. The original SDK
bootstrap/verification methods materialize and verify the marker. The private
monitor operation record retains its exact owner, project, thread and marker;
it is unsubmitted and terminated, with no actual verification assignment.

The candidate's actual Ruby `provider_scoped_helper` runs against a synthetic
registered workspace, using the real `codex_environment(entry)` and subprocess
boundary. No method overrides substitute for this launch. Idle preparation starts
without Codex-home variables; working preparation starts with conflicting private
incidental homes. Both must derive canonical storage from the fixture registration:
`run-2/state/codex-homes/f` for CODEX_HOME, CODEX_SQLITE_HOME and
DEV_WORKSPACE_CODEX_HOME. The Go helper then exercises production inventory,
client composition, bootstrap and native archive-state proof.

Each returned snapshot must contain exactly the selected lead and its monitor,
no blockers, the correct monitor operation identity and the expected lead active
intent. The working fixture must actually reach a blocked local Responses request,
have a nonempty native turn ID before preparation, and retain that same exact turn
ID afterwards. Idle must remain idle. Direct settings capture must also succeed.

All HOME, Codex home, SQLite, state, authority, registry, histories, logs and socket
paths are beneath the private run root. The only model backend is local mocked
Responses with fake credentials. No real session/incident data, socket, provider
catalog or credentials are inputs. Native writes, including synthetic bootstrap
and preparation's settings reads/resume, address only newly created fixture IDs.
There is no scoped-switch/continue, provider selection, archive/unarchive, real
session lifecycle action or nonfixture target. Cleanup kills and joins only the
fixture's own newly started daemon process group. Helper cancellation similarly
targets only its newly started subprocess group.

## Released command plan

The parent executed this released command for attempt 2:

```sh
/run/current-system/sw/bin/bash \
  /tmp/2026-11-13-archive-confirmation-regression-native-verify-i/launch-and-wait.sh \
  --review-complete /nix/store/qxclq96999l3ccs39mj5vw0m5k8hwllx-dev-workspace-0.2.0
```

This command selected corrected attempt 2. The lead launched it once under parent
supervision and observed its existing status/logs. An observer must never invoke
the launch command again to obtain observation. The launcher registered the
entire fixture command with `dev-session service run` before any server starts:
label `provider-native-verify-i-2`, exact service ID
`5a85ec36-54df-49f7-bcdc-cff25b7f8a19`, cwd the own exported `source/`.
It sets both already-verified session identity variables only for the launcher.
The service uses `run.sh`; the native daemon is its descendant.

Inside that registered service, the exact test is:

```sh
nix develop path:/tmp/2026-11-13-archive-confirmation-regression-native-verify-i/source \
  --no-write-lock-file --command bash -c '
    export PROVIDER_DIAG_RUBY
    PROVIDER_DIAG_RUBY=$(command -v ruby)
    cd portal
    go test -mod=readonly -tags provider_native_verify_i \
      -run "^TestProviderPrepareWithRetainedMonitor$" -v \
      ./cmd/workspace-portal -count=1 -timeout=60s
  '
```

`run.sh` supplies the fixed native/helper/launcher paths and private run root.
Expected duration: about 5–30 seconds with the already available Nix shell and
Go cache; E's smaller native fixture took 1.15 seconds. Fixture RPC/process context
is 45 seconds; Go's final test bound is 60 seconds. Escalate at 90 seconds if the
command has not ended, identifying source/service/tool identities and known
effects; do not infer failure from quiet output or launch another attempt.

Stop the batch on its first failure. Interpret existing artifacts before any
rerun. Refuse a reused run directory. Do not duplicate the lead's separately
coordinated package, session-creation or archive checks. No service/session stop
or retirement is requested by this command plan.

## Status, artifacts and preparation checks

For attempt 2, under the own disposable boundary:

- `service-launch-2.json`: registration acknowledgement.
- `run-2/exit-status`: atomic authoritative wrapper exit status.
- `run-2/check.log`, `run-2/native.log`: complete local logs.
- `run-2/candidate-package`, `run-2/source-head`, `run-2/input-sha256`: exact run inputs.
- `run-2/idle.stdout`, `run-2/working.stdout`: returned JSON snapshots;
  per-scope `.stderr` and `.snapshot.json.progress`: helper evidence. Preparation
  returns its snapshot on stdout; standalone `.snapshot.json` files are not produced.
- `run-2/result.json`: assertion-backed idle/working observations.
- `run-2/daemon-joined.json`: exact owned daemon PID and completed wait evidence.

A successful wrapper status must be accompanied by passing assertions, result and
daemon-join evidence and an authoritative exited observation of the exact registered
service. Missing status/cleanup or unknown descendants mean incomplete effects,
even if a launcher command returned. The lead's selected observer owns status observation;
implementer2 owns diagnosis, fixture fixes and result interpretation afterwards.

Preparation-only checks passed in the pinned Nix environment: `bash -n` for both
launch scripts, `ruby -c` for the Ruby launcher, gofmt, and Go compilation with
the dedicated tag and `-run '^$'` (0.043 s, **no tests run**). Tool session 79637
exited 0; the earlier compile-only session 13820 also exited 0. No operation-owned
command remains running. The disposable `run/` directory was still absent at
the original preparation handoff. No service or native daemon had launched then.

The first shell entry used plain `nix develop` from a non-Git export and Nix
incorrectly tried the parent `/tmp` Git context. Explicit `path:` source selection
resolved this without source/dependency changes; the released launcher retains it.

Current attempt-2 SHA256 identities:

| Artifact | SHA256 |
| --- | --- |
| Exact refreshed G source archive | `7e410b223b5d18b86c498917837b3a4c78af143fedff448508380d41f63fd6f0` |
| Native fixture | `3264fe8bc52f967c82c476420264d14fbebda125af6b567a2bd17d8abc2e68dd` |
| Ruby launch | `1ce0db81476902b73ce60087ab7bfb4d5457a33a9338afeeed12ff5d00bfb177` |
| Service run wrapper | `9643326bf8f957ee6c7ee872b97141d069a8b73e93cae92cbe569f6bc401a742` |
| Launch/wait wrapper | `003f0e43980e995bbacbf43a0290bd5a0ec805ea9f332c9e852e6992f56b7877` |
| Source flake.lock | `6ef03d811399a0e7256db2aebd114188433a92d02e4f953e7068647164b816c2` |

The source archive identifies all product inputs; the added fixture and wrappers
are disposable verification artifacts, outside the product branch. This evidence
does not replace final independent review or claim full provider-switch coverage.

## Source refresh provenance

The original provider head `e96284d1a0484a01888a6d7166fcbd5f68855659` is unchanged
within successor `9241a342a6ef4ca69148594e98cce7ddcfb459a6`. The only intervening
product-repository delta is `maintenance_continuation_timeout_test.go`: its fake
continuation timeout changes from 300 ms to 3 seconds, with an explanatory comment.
Application code, AGENTS.md, flake inputs and lock, Go module declarations and
native selection are unchanged. The refreshed source includes that exact test
child. Own native fixture and scripts were preserved, with only their embedded
source-revision literals updated. The original source archive hash was
`ce51cab78f2efdc63eafe2a507c7e613cda3cffe6737fd4da5f05f0d4f005a68`.

Refreshed quick checks passed: both Bash syntax checks, Ruby syntax, gofmt
verification and Go compilation with the dedicated tag and `-run '^$'` (0.061 s,
no tests run). Tool session 56550 exited 0. Every exported product file was
compared with the exact new archive; files and symlink identities matched.
The private run root remained absent, with no registered launch or native effects.

The prior build monitor was canceled and reconciled by the lead; the lead reports
that its original build never ran. Package I does not poll that operation or
duplicate its command. Attempt 1 subsequently ran under parent supervision.

## Attempt 1 fixture failure and bounded repair

The parent launched the candidate above; tool 70259 joined with exit 1. Go failed
at idle preparation in 1.373 seconds. `ruby-launch.rb` used `Kernel#load` on the
Nix Bash wrapper `libexec/workspace-host`, producing a Ruby SyntaxError at its
`PATH=${...}` line before the actual helper ran. This is a harness entrypoint
defect and establishes no product failure.

All first-run status/logs remain untouched under `run/`, including `exit-status`
1, `check.log`, `native.log`, idle output/error and `daemon-joined.json`. Original
fixture and scripts were additionally copied to `attempt-1-harness/` before repair.
The daemon receipt reports PID 258615, joined true, killError nil and waitError
`signal: killed`. A fresh authoritative service read at 10:53:19 UTC reported exact
service `58f7745c-5594-48e3-bb02-a98ccbdb0059` state failed, error null. Exact unit
inspection confirmed Result exit-code, ExecMainStatus 1, MainPID 0 and empty
ControlGroup. The first run ended with its native subprocess joined.

The only functional fixture repair loads the exact packaged Ruby body
`libexec/.workspace-host-wrapped`; the inspected Bash wrapper explicitly execs
that file. No speculative alternate path or product change was added. Attempt 2
uses new `run-2/`, new service/acknowledgement identities above, and the same
9241a342 source, candidate, 45-second context and 60-second Go bound.

Bash/Ruby syntax passed. A private `env -i` preflight with the candidate's pinned
Ruby loaded the exact body/class, checked package_root, checked that
provider_scoped_helper comes from the candidate's workspace-provider-sessions.rb,
and verified all three canonical private home values. It started no native process
and called no provider helper. Evidence: `ruby-load-preflight-2.rb` and
`ruby-load-preflight-2.log`; preflight source SHA256
`1e5e585b19e8a25cc51e938861794d225ffc9d58570314bc542502d3351e257d`.
No second native attempt was launched by implementer2. The lead received the exact
second command and fresh identities in report `10e206fd-bb5f-4eb0-bb4e-bc1a7f6804d7`.

The parent's next invocation returned exit 1 before service registration. Static
inspection identifies launch-and-wait.sh line 9, the first candidate executable
check: the exact candidate directory, portal binary and wrapped Ruby body returned
ENOENT. The native executable was available; `run-2/` and `service-launch-2.json`
were absent. No service or native attempt occurred in that invocation, so the
second ID remained unused. This was reported as
`56f86859-ebd1-4daa-ab00-201519b344ec`.

The lead then confirmed from the system journal that
`nix-store-gc-on-pressure.service` deleted this exact unrooted candidate between
attempts. The initial `--no-link` build had no GC root. The lead restored the same
reviewed output using `nix build --out-link` and retained it at
`/tmp/2026-11-13-archive-confirmation-regression-builds/candidate-package` through
deployment. That link resolves to the exact qxcl candidate above. No source,
schema, harness or product-review change was required for artifact restoration.

## Attempt 2 result and interpretation

Parent tool 90158 joined with exit 0. The retained `run-2/exit-status` is 0 and
`check.log` records `TestProviderPrepareWithRetainedMonitor` PASS in 2.53 seconds,
package time 2.588 seconds. Run input receipts bind the exact 9241a342 source,
qxcl candidate, unchanged native executable and current fixture/launcher hashes.

| Observation | Idle | Working |
| --- | --- | --- |
| Packaged helper / stderr | success / empty | success / empty |
| Scoped threads / blockers | 2 / none | 2 / none |
| Monitor source / history | vscode / paginated | vscode / paginated |
| Monitor ephemeral / exact bootstrap proof | false / pass | false / pass |
| Settings read | success, gpt-5.5 / low | success, gpt-5.5 / low |
| Lead active intent / active afterwards | false / false | true / true |
| Original native turn preserved | yes | yes, same exact active turn |
| Close intent / closed / continued | all false | all false |

The fixture also asserts native project and exact CWD identity and waits for the
working lead's mocked Responses request before preparation. Both scopes reached
capturing-settings. The absent-home idle launch and conflicting-home working
launch passed through the packaged Ruby helper and production Go inventory,
validating the two repaired provider-helper inputs against the selected native
runtime. Working execution remains eligible and preparation preserves its turn.

`run-2/daemon-joined.json` directly proves fixture daemon PID 782784 joined, with
killError nil and waitError `signal: killed`. The parent reports the exact second
registered service exited and its source command joined; the startup receipt
itself records registration/running state only. No further native calls, tests,
services, full provider switch, live-target retry or session lifecycle action
were performed for this interpretation. The check establishes scoped preparation
with synthetic retained monitors; it does not establish later switch/continuation
stages or real incident-target behavior. Package I has no remaining verification
work; acceptance and rollout bookkeeping belong to the lead.

Final retained artifact SHA256:

| Artifact | SHA256 |
| --- | --- |
| run-2/result.json | `366b14bad8866273c79a501cd046964e441f2bae343e3c88b12693a620e2d617` |
| run-2/check.log | `65d9b9b4efa5abf4438b195725621bccc345e18c46d8e6177c9bcd75b19b6c07` |
| run-2/daemon-joined.json | `9ad7dbcefe25f03e80d6cf0b8cce5900969799a99f1f8a0999b1760a7cac7f62` |
| Preserved run/check.log | `4ef58a25b3c4658ad6b8a5def10b273f5068f8ad649defdbef9e0d099ef52fe1` |

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-13-archive-confirmation-regression/>.
