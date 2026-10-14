# K review remediation focused packet: retained artifact authority

Prepared and unlaunched. This replaces the preparation-only quick1 selection;
all quick1 controls/receipts remain untouched and honestly unused. The ongoing
review inspected original committed K93a16d6cecb6bc847ec9335a3f170eb8b301ab56,
D51aba080b264c28f5584867b6cf006bf423ae2f3 and Ed2079f605ae87871037ae73c5e5daf20a3e0d03d.
No current-source passing or review-certification claim is made.

Thirteen owned K paths are frozen, including root-approved doc2
2ba15e77f6423ebb1e6528f4bd77406eafc5bb62670f7e75c4422f7f61d65e61.
The index remains empty, one new test file remains untracked, and full status,
tracked/new-file diffs, path/mode/size/hashes and an empty protected-source diff
are retained. No intent-to-add is needed: the exact committed K93 shell evaluates
its unchanged declaration/lock while tests read the owned draft from explicit CWD.

## Implementation boundary

Node safely opens persistent outputRoot/tmp/capture.lock without truncation or
symlink following. Only the fixed Ruby artifact helper inherits that same open
file description as fd3. Ruby validates its path/dev/ino/uid/mode before flock
and readiness. Node retains its descriptor through snapshot/publication and
browser/SSH/cluster/helper cleanup, closes it last on every exit, and never
LOCK_UNs either duplicate. Validator --exec retains its existing writing-child
inheritance and close-only exclusion. There is no new native dependency,
workspace dependency, state schema or metadata/ownership protocol.

Both artifact and cluster cancellation/liveness gate browser/SSH/fixture work,
staging and publication. Artifact loss cancels pending cluster readiness; after
acquisition capture cancels work while keeping the cluster controller until its
normal cleanup boundary. Physical descriptor authority excludes other writers
while Node cannot dispatch death events during synchronous writes. A dead
controller is still a failure once observed. No rollback or undo of an already
issued remote request/synchronous write is claimed.

Update preflight compares actual resolved SSH host/port maps before candidate
creation, journaling, phase changes, build/import or stop. Changed endpoints
refuse; retained host-key trust is not rewritten. Other compatible source/config
updates continue through the original path.

## Focused source verification selected

The packet uses K93's exact immutable declared Nix devShell and proves effective
Ruby/Minitest/timeout/Node paths in Nix despite conflicting ambient Ruby settings.
It captures native toolchain JSON, scoped Ruby/Node/shell syntax/ShellCheck and
whitespace, focused Node TAP plus existing proxy teardown, then full owning
runtime Minitest output. Every stage and aggregate records logs/status, stops
on first failure and refuses existing receipts. Prepared source inventory is
29 Node examples (14 connection, 9 artifact, 6 actual capture orchestration),
the separate existing proxy teardown, and 24 runtime examples. These are not
execution counts or passing evidence.

Actual capture orchestration keeps main, Connection, browser supervision,
CaptureSession, Artifacts and real Ruby flock controllers. Guest SSH subprocesses,
Chromium implementation and fixture/scenario contents are synthetic. The
synchronous case blocks the real writer at a PNG rename after its live check,
validates the still-unreaped owned helper's parent, and kills that helper from
an independent test process while writer event processing remains paused. An
independent actual capture must stay excluded both during publication and
controlled browser cleanup, then acquire after the final writer close and keep
its successful row/PNG. The old writer reports controller failure.

Additional actual-main examples exercise known-loss cancellation with a queued
competing writer, pending cluster acquisition, artifact readiness loss before
and in its readiness window, and sequential CS/EN plus genuine stderr-only EOF.
The normal language case checks descriptor absence in actual cluster-controller
and SSH child processes. Physical-lock tests cover normal/abnormal helper exit,
unrelated-child leak, writer death/helper EOF, validator-wrapper death, separate
output-root independence, unsafe paths/modes, inherited-FD/path mismatch and
nontruncation. Existing provenance/hash/merge/interruption tests remain.

Three runtime examples change local SSH host, forwarded port or local-to-bridge
endpoint resolution and preserve all retained file bytes/inodes, credentials,
live run and claims. The fourth exercises the real trust implementation with
only keyscan transport mocked: same endpoint/key succeeds; stable key with
changed endpoint prefix or changed key refuses without replacing trust.

No VM/guest, rendered PNG, full validation/build/package/activation or deployment
proof is supplied by these synthetic tests. Inputs, inventory, fixtures,
state/closure/disks, VM scenarios and protected screenshots remain unchanged.
No suite, commit/ref/publication/pin/build/VM/lifecycle/GitHub action was launched.

Root/fresh watcher may execute only after inspection:

```sh
bash /home/aither/workspace/ai/vpsfree.cz/work/2026-10-05-network-ipv4-left-counter/kb-runtime-review-fix-quick2.sh
```

Main owns result interpretation, normal final consolidation/publication,
downstream mechanical K pin refresh and the affected-lane committed reviewer
rerun. New same-description plumbing warrants that rerun; original review
snapshots and receipts remain preserved.
