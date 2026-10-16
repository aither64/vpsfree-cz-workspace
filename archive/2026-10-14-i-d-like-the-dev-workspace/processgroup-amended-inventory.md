# Process-group accepted Advisory remedy

Implementer0 applied only the lead-accepted reviewer Advisory, under direct
mandatory-review steps 9/10 verification. Exact current session and both absent
environment markers were reverified; the saved ready workspace-write identity
matched. Applicable guidance was reused unchanged. No reviewer confirmation
rerun, broader implementation or user-facing copy change was introduced.

## Exact preserved and final history

Reviewed third commit `b4b90aca3198b6d0ab5171044c6731708af8776e` is retained at
`refs/session/2026-10-14-i-d-like-the-dev-workspace/processgroup-reviewed-b4b90aca`.
`processgroup-amended-original.json` records that ref and the old evidence
manifest digest before amendment. Every b4 packet/log remains unchanged and
`processgroup-artifacts.sha256` still verifies all fourteen original artifacts.

New frozen clean unpublished head:
`6e1d9a191724d376cad2a71f234f0e4d1c01f36f`.
Parent remains `bb9e6291bec10227c961c36559fba406938f1eaa`.
Complete branch over `832d9f1a6a21337dd44063ddf39f7a88cfc95450`:

1. `96717cdeb5f733391846a95d78c117068ce77de8` — original attention/Web Push.
2. `bb9e6291bec10227c961c36559fba406938f1eaa` — original provider diagnostics.
3. `6e1d9a191724d376cad2a71f234f0e4d1c01f36f` — amended test-only observer.

The first two commits are untouched. No merge or fourth follow-up commit was
introduced. Whole branch remains 41 files, +4126/-104. The test-only owning
commit remains one file, +233/-22. Commit amendment reused the exact existing
message file `/tmp/processgroup-test-commit.txt`, verified against the old
message, all lines within 80 columns. Normal Git hooks were not bypassed; the
repository still declares no hook framework/active nonsample hooks.

## Narrow source delta

Only this line in `portal/internal/processgroup/processgroup_test.go` changed:

```diff
- wrongPID, wrongGroup := sample("S"), sample("S")
+ wrongPID, wrongGroup := sample("Z"), sample("X")
```

Both retain the expected start time. The wrong-PID sample has matching PGID and
terminal Z, so removing the PID guard would incorrectly report exit. The
wrong-group sample has matching PID and terminal X, so removing the PGID guard
would incorrectly report exit. Each existing negative case therefore exercises
its guard. No helper, production, boundary, deadline, parser, diagnostic or docs
code changed in this remedy.

Production `processgroup.go` remains exact blob
`9e7d02c4e8c234d2d4f12fb446e7e082bf74b45a`. New test blob is
`5861bd05cd3a8d81c8aee7133e3739632a7e4598`.

## Evidence at each head

At **b4b90aca**, the prior complete focused uncached check passed the timeout
and graceful cancellation tests, deterministic parser/read/wait contracts and
real owned live-child control: package 3.089s, command 3.735s. That original
evidence remains `processgroup-focused.log/status.json` and is not relabeled as
a new complete run on the amended head. Unchanged live checks were not repeated.

At the **amended source tree**, only the changed deterministic wait contract
ran uncached using declared Go 1.26.6 with readonly/offline cached modules:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
export GOFLAGS=-mod=readonly GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-attention-go-build GOPROXY=off GOSUMDB=off
go -C portal test -mod=readonly ./internal/processgroup -run '^TestWaitForProcessExitIsBoundedAndDoesNotReprobeTerminal$' -count=1 -v
```

PASS: one top-level test and all fifteen named subcases; package 0.011s,
command 0.872s. Evidence: `processgroup-amended-wait.log` and
`processgroup-amended-wait.status.json`. This command compiled the package but
did not execute either cancellation fixture or the owned live-child check.
Declared gofmt, scope, staged/final/whole-branch diff checks and clean-tree and
production-blob checks passed. No broader test or investigation ran.

## Exact packet hashes and provenance

| New artifact | SHA256 |
| --- | --- |
| `processgroup-advisory-remedy.patch` — b4..6e1, one line replaced | `ca313371e71e2913170bc799c2eae1d9322ea78378413fd2b354c139fc37b5f5` |
| `processgroup-amended-final.patch` — bb9..6e1 | `4c99a87aedb53daa34b4c0c436018179f697e3941e73d4a7c94171260eca44d6` |
| `processgroup-amended-wholebranch.patch` — 832d..6e1 | `12bdf7e11866052f6c7b5a443372574cb94874a5ecb0da216847ac9896c96216` |
| `processgroup-amended-series.txt` | `e77068c53ce330b6aa459f3d3a0388dd59bb085c6c6e355af7cd5711a1fd6497` |
| `processgroup-amended-stat.txt` | `5ee31862d6baa117a6525cdf7d4d03aefb466958ea08b9a2da28acc1b5988731` |

`processgroup-amended-freeze.json` binds the exact ranges, blobs, unchanged
first two commits, amended deterministic result and historical live-evidence
head. The original source investigation remains in `processgroup-inventory.md`;
all its old artifacts remain immutable.

No dependencies, vendor hash, migrations, schemas, formats, production behavior
or supported compatibility paths changed. Retained feature private formats and
protected upstream integration journals/capability fencing remain as recorded
in `frontier-runtime-inventory.md`. No new deployed or externally consumed state
exists for this remedy. The original causes remain unproved; corrected tests
do not provide causal proof.

Hold push, pins, long checks, daemon/network/host/provider/queue/reservation and
lifecycle actions. Lead owns direct narrow-fix inspection/checks, publication
and downstream refresh. Existing live harnesses retain their original heads.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
