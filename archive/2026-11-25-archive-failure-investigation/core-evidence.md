# Package C: archive readiness proof reuse

Owner: implementer0. Status: committed, published and final affected quick
checks passed and C accepted by lead. Independent final review passed without
findings at the frozen final heads; see [review.md](review.md). Package E later
passed the required runtime/package and isolated lifecycle checks plus composed
application/composition targets; see [verification evidence](verification-evidence.md).
No live lifecycle action, default integration or deployment was performed by C/E.

## Requested outcome and implementation

Follow the lead-released [design](design.md): avoid the duplicate native monitor
proof after the CLI has returned a validated `monitorLocal.state=quiescent`
result under the same admission. The helper checks `ctx.Err()` first and consumes
that result immediately. The optional-field fallback and every blocked or
quiesceable observer assessment/owner/join/full-readiness path remain intact.
The ordinary executor still freshly validates readiness before shutdown/removal.
No cache, timeout increase, backend interface, durable format or authority changed.

Core files, incremental installed-base-to-head diff:

- `portal/internal/web/archive_preparation.go`: nine added lines, context guard
  and typed quiescent shortcut with proof-lifetime comment.
- `portal/internal/web/archive_preparation_test.go`: synthetic completed native
  utility, one successful proof, then an expensive duplicate proof that would
  exhaust a one-second parent deadline. The typed case makes zero duplicate
  project reads and hands off with one history entry; the absent-field case
  makes one read, reaches its deadline and refuses without repair/handoff.
  A canceled context refuses even with the typed quiescent result. Existing
  coordination/truncated-blocker refusal fixtures now explicitly carry typed
  quiesceable data. Original lost-owner refusal and detach/recheck coverage stay.
- `docs/session-archive-recovery.md`: eight lines explaining the local proof's
  admission lifetime, optional-field fallback, cancellation and executor checks.

No source outside those three paths differs from the installed parent.
Incremental diff: three files, 126 insertions and one deletion. The synthetic
fixture represents cumulative expensive native history with one deliberately
blocking proof; it does not create 59 records or wait for a real 30-second timeout.
All runtime/session fixture state is disposable, unrelated to live sessions.

## Exact source, publication and full branch history

Repository: `git@github.com:aither64/dev-workspace.git`, target `master`.
Own branch: `2026-11-25-archive-failure-investigation`.
Own worktree:
`/home/aither/workspace/ai/vpsfree.cz/worktrees/2026-11-25-archive-failure-investigation/dev-workspace`.

- Freshly fetched default/base: `65544340f94ebb112872743738f84c1a7022b06a`.
- Installed parent selected by lead:
  `91cafd4c0c50ffb7208498a605707c4c3b1b1174`.
- Final published candidate head:
  `f6d60bf87002fb1896599f35f0284743c16d7e6f`.
- Final tree: `0ab8c211365bedcd18ddc8fd5074db72b54df562`.

The complete default-to-candidate series is:

1. `9bf34aa1963e3ba226ec678237cee3dacb2e7a25`
   `portal: refuse conflicting team initial IDs before materialization`.
2. `91cafd4c0c50ffb7208498a605707c4c3b1b1174`
   `pi-runtime: recover proven held team-message conflicts`.
3. `f6d60bf87002fb1896599f35f0284743c16d7e6f`
   `portal: reuse quiescent archive readiness within admission`.

The first two are unchanged installed parent originals, retained to preserve
actually deployed content, not new C implementation. Their full reviewed range
is `65544340..91cafd4`; the original accepted final affected review by retained
reviewer0/Sol/xhigh is in
`work/2026-11-23-pi-message-delivery/review.md:1992` (preceding affected review at
`:1972`). [Design's candidate follow-up](design.md#candidate-composition-follow-up)
records source sensitivity verification and original report/proof references.
The parent report concludes unchanged P plus one consolidated R, no obsolete
final update stream and no migrations. Reuse that baseline evidence and assess
C's affected lanes without repeating unchanged Pi implementation diagnosis.
The complete final branch still requires an explicit independent whole-history,
repeated-update and migration conclusion.

Full final diff is `git diff 65544340f94ebb112872743738f84c1a7022b06a..f6d60bf87002fb1896599f35f0284743c16d7e6f`
(37 files, 4343 insertions, 233 deletions, including unchanged installed parents).
C alone is `git diff 91cafd4c0c50ffb7208498a605707c4c3b1b1174..f6d60bf87002fb1896599f35f0284743c16d7e6f`.

C has one logical final commit, no migrations, generated artifacts, input/pin
updates, repeated update streams, superseded approaches or unused compatibility
paths. No C migration was merged, released, deployed or externally consumed.
The preserved parent migrations/history have the original explicit no-migrations
conclusion above; no parent commit/ref/worktree was modified by this session.

## Rebase equivalence and parent preservation

The independently prepared old C range was
`65544340f94ebb112872743738f84c1a7022b06a..e50f54dc8ae1a5dcf1dbc485991aba49b3c8a61b`.
Lead then selected installed-preserving composition. After a fresh fetch confirmed
master still did not contain installed `91cafd4`, only this session's own branch
was rebased onto that exact immutable parent.

- `git range-diff OLD_BASE..OLD_HEAD 91cafd4..f6d60bf` reports one `=` commit.
- Binary patch files from those two ranges compare byte-identically with `cmp`.
- Both stable patch IDs: `ea289e0482d2c0a6289b45abc29526862c1fbbe5`.
- Independently loaded `91cafd4` into a disposable Git index and applied the
  original binary patch. `git write-tree` produced the final tree
  `0ab8c211365bedcd18ddc8fd5074db72b54df562`. This proves the candidate preserves
  every parent byte/mode/symlink plus exactly C.
- The temporary index fixture is `/tmp/archive-core-tree-expectation-ham8moge`;
  original/rebased patches are `/tmp/archive-core-{original,rebased}.patch`.
- SSH publication used a lease explicitly expecting old `e50f54dc`.
  `git ls-remote` verified exact final-head equality. The worktree is clean.
- Superseded own CI run `45636431540` at `e50f54dc` was canceled and verified
  `status=completed, conclusion=cancelled`. Current-head run `45636961676`
  remains active; no current run or other branch's workflow was canceled.

## Checks and input identities

The repository declares no hook framework and has no active custom Git hooks or
`core.hooksPath`. Only sample hook files exist; no hook was bypassed. Commit
message came from a temporary file and has `area: action` subject/body rationale.
`gofmt` was applied to the two changed Go files in `nix develop`.
`git diff --check` and staged checks passed. No module/lockfile changed.

Pre-rebase new-case check passed:

```sh
nix develop --command sh -c 'cd portal && go test -mod=readonly ./internal/web -run "^TestArchivePreparation(ReusesQuiescentCheckWithinAdmission|QuiescentProofRespectsCancellation)$" -count=1'
```

Result: pass, web 1.325 seconds. The initial attempt caught a test assertion
mismatch: existing blocked-safety conversion returns its reason without retaining
the deadline error's wrapping. The corrected fixture checks `ctx.Err()` and
refusal independently; production fallback behavior was left unchanged.

Pre-rebase focused archive/monitor batch passed with fresh Luna/low watcher:
web 20.149 seconds, monitoroperation 11.774 seconds, exit zero. Disposable log
`/tmp/archive-core-quick-20261125.log`. Watcher accounted for completed tool
session 25120 with no outstanding effects.

After the parent change, the final affected quick batch runs against committed
`f6d60bf`, with this exact command from the owned runtime root:

```sh
nix develop --command sh -c 'cd portal && go test -mod=readonly ./internal/web -run "^TestArchivePreparation" -count=1 && go test -mod=readonly ./internal/monitoroperation -run "^TestMonitor(Lifecycle|LocalSafety|CI|Observer)" -count=1'
```

This repeats only affected archive admission/cancellation/receipt/target and
monitor safety/refusal/owner/join coverage on the changed candidate baseline.
Final result: passed, exit zero; web 22.039 seconds and monitoroperation
1.290 seconds, total command elapsed 73 seconds including Nix evaluation.
Watcher joined operation-owned session 54312 and reported no remaining work. Launcher `/tmp/archive-core-final-quick.sh`, SHA-256
`24808e9fdf8c0db68568fac1d55dd00fe700abf9315b86bc756e39b1fd22e8d5`.
Fresh standalone native watcher (not a team member):
`01a2132b-e28d-7c22-83aa-59596c42c314`, installed utility
`dw_c699c3bf36ffc569cca1d7f83580bf68e6fffbb536cfad0d`, catalog
`1184a2cf511b6e77ff7afe12433027abe06e8bb0b897f39cffc26efd443d1a7c` from
`/nix/store/1zn1a51qrsin83fszrprdjp45208vsj4-dev-workspace-0.2.0`.
Native launch header verifies gpt-6-luna/low, approval never and
sandbox danger-full-access. Parent stays active for its result. Logs/results:
`/tmp/archive-core-final-quick.log`,
`/tmp/archive-core-final-watcher2-{native.log,result.txt}`.
The previous fresh watcher `01a2132a-2f71-7061-b342-6f6f78861981` stopped
before tests because its `/usr/bin/time` timing wrapper was unavailable (exit
127). It left no command running. The final fresh watcher executes the identical
script directly with shell timestamps; this is an environment correction, not
a rerun of any started test.

Final clean source evaluation (no builds/tests launched):

- source `/nix/store/hh81k6nk1r1x0jhi0v8a1l9d53jr0h4n-source`;
- source NAR `sha256-JZJQaci1y3dGVSQwHbdHS8X0IDFpyrz+dk3rqntZJOE=`;
- package check `/nix/store/rn1872lrbs1g0jzszr3jg756f6f5gfss-dev-workspace-0.2.0.drv`;
- archive lifecycle check
  `/nix/store/gnkq2g5ljyf6abi1mfip5i5nns42ysy2-vm-test-run-dev-workspace-session-archive-lifecycle.drv`.

Complete immutable runtime inputs are in that source's `flake.lock` (all nodes,
original/locked identities and follows graph), also at the committed candidate.
Its SHA-256 is `ca7f6a807e2a32d76deb463a44677023e3fac2236ce93c82426c54307aefa51f`.
Go module manifest SHA-256:
`ac2196b0a12a3135a8482c6194e19e29f166f9712843abc1bf90909e2b9f7e6a`;
module sum SHA-256:
`4ed83b1de0a9aa6f327df553888dd85ed22a58f4d63c0e774bbb932e51735d51`.
No graph node changed in C or from installed `91cafd4`.
[Deployment preflight](deployment-preflight.md) owns the complete composed site
source/input lineage, extension/catalog/profile and activation recovery evidence.
Old master-based C derivations are superseded, not evidence for final builds.

## Documentation and review routing

| Topic | Reader/class | Authoritative home | Evidence |
| --- | --- | --- | --- |
| Monitor proof lifetime, fallback, cancellation and executor safety | Runtime maintainers/operators; reference/operations | `docs/session-archive-recovery.md#local-ci-observation-before-archive` | Typed guard and new regressions; existing executor unchanged |
| Local control-flow invariant | Runtime maintainers; implementation reference | Comment beside `quiescePreparationMonitors` | Immediate callback after validation under admission |
| Concrete candidate lineage, checks, review and next actions | This initiative; individual execution | This file, design.md, state.md | Exact IDs/results here; shared lead tracking |
| Installed graph, candidate composition and activation/recovery | Deployment owners; individual execution | deployment-preflight.md and D/lead rollout receipt | Package B/D owners; no C deployment claim |

README already links the archive recovery guide, so no new entry point is needed.
No recovery instruction, warning or supported path was removed. The lead directly
applied user-facing-writing + humanizer-en to the added paragraph and accepted
its plain wording before commit; technical content was preserved.

Suggested independent review: high risk because this optimizes pre-destructive
readiness; general, architecture/repetition, scope/proportionality and
risk/compatibility lanes. Reviewer choice/settings and invocation remain with
lead. The local operator is trusted; ordinary identity, ownership, races,
cancellation, interrupted recovery, remote validation and secrets remain in scope.
Owning component is generic dev-workspace's archive preparation. Consumers are
the CLI readiness result and existing browser preparation/executor; no public
wire contract changed. Optional typed data was already supported. Older packages
can read unchanged state, retaining the old timeout risk.

Rejected alternatives/non-goals: timeout increase, native inventory parallelism,
durable proof cache, schema/interface redesign, parent Pi refactoring, production
archive retry and session cleanup. No C default-branch integration approval was
received. Integration/deployment/lifecycle authority remains with lead/user.

## Remaining acceptance and longer checks

After final independent committed review and resolution/acceptance of findings,
run a fresh monitored related batch from this runtime worktree:

```sh
nix build --no-link --print-build-logs .#checks.x86_64-linux.package
nix build --no-link --print-build-logs .#checks.x86_64-linux.session-archive-lifecycle
```

Use the final exact derivations above; a changed head/input requires refreshing
those identities. VM lifecycle operations run only against isolated fixture state.
These checks were prepared but not launched before review. After the accepted
no-findings final review, package E launched the exact runtime checks together
with the composed app/composition targets; see [verification evidence](verification-evidence.md)
for the passed one-shot batch, input/output receipts and terminal effect accounting.
All four targets passed in1845s (30m45s), with exact prepared derivations and
outputs. No live failed-target retry, archive/revive/stop/delete or smoke was
performed or authorized. Source freshness, accepted mechanical reuse, integration,
activation and actual usability remain with D/F/lead.

Stable session portal:
https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-11-25-archive-failure-investigation/
