# Process-group test observer correction

Prepared by implementer0 under the lead's accepted bounded test-only brief in
the design section "Process-group verification failure investigation,
2026-10-15". Exact session/current, both absent environment markers and the saved
ready workspace-write member identity were verified before edits. Applicable
Git/commit/verification/documentation procedures, runtime AGENTS and the
documentation skill were read or reused unchanged.

The original failing builder PID was never inspected or signaled. The original
failure, same-head CI success and earlier diagnostic/verification artifacts are
unchanged. This correction does not prove that the original failure was a
zombie-to-dead transition or that production cancellation was correct.

## Frozen source and history

New clean unpublished head:
`b4b90aca3198b6d0ab5171044c6731708af8776e`.
Parent: `bb9e6291bec10227c961c36559fba406938f1eaa`.
Branch base: `832d9f1a6a21337dd44063ddf39f7a88cfc95450`.

Only `portal/internal/processgroup/processgroup_test.go` changed, +233/-22.
Production `processgroup.go` remains byte-identical at blob
`9e7d02c4e8c234d2d4f12fb446e7e082bf74b45a`; new test blob is
`0f98ca5383f4ead6c08aa5f719946a6d3b03a158`.
The original parent is retained under session-owned ref
`refs/session/2026-10-14-i-d-like-the-dev-workspace/processgroup-original-bb9e6291`
and new `processgroup-original.json` / `processgroup-original-test.go` artifacts.

The complete final branch is exactly three logical commits with no merge:

| Commit | Owning change |
| --- | --- |
| `96717cdeb5f733391846a95d78c117068ce77de8` | Existing accepted attention/Web Push feature and inseparable vendor closure |
| `bb9e6291bec10227c961c36559fba406938f1eaa` | Existing bounded provider failure diagnostics and collection timeout |
| `b4b90aca3198b6d0ab5171044c6731708af8776e` | New test-only identity-aware descendant exit observer and contracts |

Prior two commits were preserved without amendment. Whole branch: 41 paths,
+4126/-104. Complete exact messages/parents, final file inventory and patches
are preserved in new `processgroup-series.txt`, `processgroup-stat.txt`,
`processgroup-final.patch` and `processgroup-wholebranch.patch`.
`processgroup-freeze.json` binds source blobs, exact ranges and quick result.

## Local test behavior

Both existing cancellation tests now consume one bounded wait result. They
cannot reverse an established terminal observation with a separate final probe.
The same two-second bound and 10-millisecond polling interval remain. Real
`time.Now`/`Sub` observations retain Go's monotonic clock behavior; deterministic
tests inject only a local test clock and observer.

Only required stat fields are parsed after the final parenthesized command
delimiter, supporting spaces and parentheses in `comm`. A valid matching PID
must have parseable positive start time and PGID. Validated absence, a reused
start-time identity, or matching identity/group in terminal `Z`/`X` state proves
exit. Malformed/read/permission/unknown or wrong PID/group observations never
prove death and fail closed if unresolved at the bound. The identity-free
kill-zero fallback is removed. The graceful fixture now explicitly checks its
recorded PGID against the leader, as the timeout fixture already did.

A failed wait emits one context capped at 1 KiB: expected PID/start time/PGID,
leader PID, elapsed time, last parsed identity/state and fixed category/errno.
No raw stat, comm, arbitrary read error/path, argv, environment or per-poll output
is emitted. Only the last sample is retained. The read/parser/wait helpers are
local to this one test file; no generic observer or product framework is added.

The real negative control starts one owned `sleep` process, proves its live
identity and requires the observer to reject exit throughout the bound. Cleanup
uses only that exact spawned child handle and waits for it. The existing product
group cancellation in the two retained tests is unchanged. No new group signal,
process scan or foreign/global cleanup was added.

## Quick checks and evidence

Declared tools were sourced from the existing `runtime-dev-env.sh`. Go is exactly
1.26.6; `GOFLAGS=-mod=readonly`, `GOPROXY=off`, `GOSUMDB=off`, existing cached
module/build paths. No dependency fetch, Nix daemon, package build, flake check,
integration suite or repeated-until-green run occurred.

Deterministic parser/read/wait checks passed uncached, 0.920-second command.
They cover live S/R/D/stopped states at the bound; Z/X, absent/reused identity;
wrong PID/group; malformed/short/nonnumeric fields; read/permission errors;
unknown state; command parentheses/spaces; fixed polling/bound; Z-then-X without
another probe; and safe bounded diagnostics/canary omission. An earlier compile-
only attempt found a local variable name collision with the existing graceful
result channel. It was corrected before any real child was executed; both logs
remain preserved as `processgroup-deterministic*` artifacts.

The single real focused uncached package run was:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
export GOFLAGS=-mod=readonly GOMODCACHE=/tmp/session-webpush-mod GOCACHE=/tmp/session-attention-go-build GOPROXY=off GOSUMDB=off
go -C portal test -mod=readonly ./internal/processgroup -count=1 -failfast -v
```

PASS: both original cancellation tests, deterministic parser/wait tests and the
real owned live-child negative control; five top-level tests, including fifteen
named deterministic wait subcases. Package time 3.089 seconds, command time
3.735 seconds. The real live-child control remained live for 2.01 seconds and
was correctly rejected as exited. New evidence is `processgroup-focused.log`
and `processgroup-focused.status.json` (exit 0). No real assertion failed and
no live check was retried. The result proves the corrected observer/control,
not the original failure's cause.

Declared gofmt formatting, Go compilation via the uncached checks, staged/final
affected and whole-branch `git diff --check`, exact one-file scope and unchanged
production blob checks passed. Commit used `/tmp/processgroup-test-commit.txt`
via `git commit -F`, all lines within 80 columns. The repository has no declared
hook framework, no core.hooksPath and only sample hooks; none was bypassed.

## Patch integrity, compatibility and remaining work

| Artifact | SHA256 |
| --- | --- |
| `processgroup-final.patch` (bb9e6291..new head) | `97cfc8af86b0f623d16c7f8327a08917c8867d4a8e1e480ac2e1752222bd4f30` |
| `processgroup-wholebranch.patch` (832d9f1..new head) | `022c2cafdcf17832f2245c1d270afaa3d668523b000a5973a131c19f69d06ed4` |
| `processgroup-series.txt` | `cf3d47991ce4800cfb85d7f2abe0dfedfe9ffe7d0fb401d08bc96f5cf7397cfe` |
| `processgroup-stat.txt` | `5ee31862d6baa117a6525cdf7d4d03aefb466958ea08b9a2da28acc1b5988731` |

No dependencies, vendor hash, migrations, schemas, state/receipt formats,
service/API/CLI behavior or production cancellation rules changed. This new
third commit has no deployment or externally consumed state. Existing feature
private-format lineage and protected upstream integration journals/capability
fencing remain as recorded in `frontier-runtime-inventory.md`; they are not
obsolete migrations to remove. The first two commits retain their exact review
and source history. For prior Node contracts, cite the corrected named lead
evidence `frontier-node-evidence.md` and `frontier-node-lead-named.*`, not a
speculative explanation of the earlier file-level reporter output.

No new user-facing prose or copy gate is introduced by this test-only change.
No provider/host, reservation/queue, default integration, session lifecycle,
source publication or downstream pin action was performed. Existing live
harnesses still bind their original revisions; none was silently retargeted.
Lead owns affected independent review, later finite watcher verification and
new exact downstream artifacts. Hold push/pins/long checks. Original root cause
remains unproved.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>
