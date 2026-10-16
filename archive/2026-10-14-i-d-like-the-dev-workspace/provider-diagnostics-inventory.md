# Provider failure diagnostics amendment

Implementation owner: implementer0. Accepted design: the
"Provider failure diagnostics addendum, 2026-10-15" at the end of `design.md`.
The original b8a6 failure remains unresolved; this amendment repairs the proven
loss of exception context. The one exact-package diagnostic did not reproduce
the original failure.

## Scope and behavior

Only four product paths are changed:

- `libexec/workspace-codex-providers.rb`: local step/readiness context and one
  safe stderr record before each existing forward/recovery exception replacement.
- `test/workspace_host/codex_provider_test.rb`: focused fault, safety, call-order
  and static/extracted VM-driver contracts.
- `nix/tests/session-recovery-boot.nix`: expected-phase-first polling and bounded
  failure collection, retaining all five subtests and both reboots.
- `docs/codex-providers.md`: worker journal location and diagnostic limits.

`PROVIDER_FAILURE` records are at most 2 KiB, with UUID/direction/stage/fixed
step/elapsed time, finite exception category/numeric errno, at most four fixed
source labels/lines and optional safe readiness values. No exception messages,
argv, helper output, credentials, arbitrary filesystem paths or snapshot/RPC
contents are emitted. Unknown exceptions use `OtherError`. Unavailable values
are explicit. The readiness summary uses only existing probes, remembers last
observations if a later property read fails, and starts fresh for each recovery.
There is no per-poll output, TracePoint, new probe or logging framework.

Working, failing sink and failing formatter runs have the same service/helper
calls, state-write sequence, final state and generic recovery error. The source
retains existing service order, readiness deadline/retries, ownership checks,
locks, restart policy, terminal restoration and recovery fencing. VM unexpected
terminal results return to Python and fail immediately; expected failed/canceled
results and recovery-required continue to work. Failure collection cannot replace
the original assertion.

## Quick verification

All commands use the registered runtime worktree and source:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
ruby -c libexec/workspace-codex-providers.rb
ruby -c test/workspace_host/codex_provider_test.rb
nix-instantiate --parse nix/tests/session-recovery-boot.nix >/dev/null
ruby test/workspace_host/codex_provider_test.rb --exclude '/test_shared_readiness_waits_for_native_protocol_and_refuses_early_exit/'
git diff --check
```

Member results: syntax/static parse/diff PASS; 19 cases, 183 assertions PASS in
1.119 seconds. The Ruby interpreter is exactly
`/nix/store/nin40kn7prvsn7pmbl7k576hhwcpp9x1-ruby-3.4.9/bin/ruby`.
The unchanged existing Unix-socket readiness test is excluded only from member
verification because its real `UNIXServer` bind is refused with EPERM. No source
workaround was introduced. The full known-quick lead command is:

```sh
cd /home/aither/workspace/ai/vpsfree.cz/worktrees/2026-10-14-i-d-like-the-dev-workspace/dev-workspace
source /home/aither/workspace/ai/vpsfree.cz/work/2026-10-14-i-d-like-the-dev-workspace/runtime-dev-env.sh
ruby test/workspace_host/codex_provider_test.rb
```

New contracts include separate nested forward/recovery failures, exact
state/service/helper call order under broken diagnostics, silent success,
compatible state keys, missing initial observations, immediate identity error,
timeout after last health category, last-observation retention, fresh recovery
context, unknown exception fallback, large secret canaries, record/frame bounds,
and formatter/sink failure isolation. Python functions extracted from the real
VM driver are compiled and exercised with a fake machine; no VM/product/native
operation is launched. These contracts prove expected/terminal/intermediate
phase handling, collection isolation and preservation of later scenarios.

The initial development checks found and corrected test-only setup/expectation
issues (mock support not present in the declared Ruby, a missing `blockers` key
in the expected persisted key list, and an identity fault that fired at the
earlier safety check). The final tests use scoped restored method doubles and
fault only the intended readiness invocation. No dependency change resulted.

## History, compatibility and provenance

Recorded base: `ba8669b14536f72b559abc912bba8eac430111e4`.
Existing owning feature commit remains intact:
`b8a6be26a75347dcc9ec0fd1330dff886e47c93f`.
One separate logical diagnostics commit follows after main-agent docs copy and
quick approval. No published feature amend, push, merge, pin update or deployment
is part of this assignment. Affected independent committed review remains with
the lead before long VM verification.

No migrations, dependencies, package closure/hash declarations, persistent
schema/state fields, receipts, operation stages, API/wire formats, successful
CLI stdout or notification behavior change. Old/new helpers retain the same
state contract; stderr is additive. No new private format was applied, deployed,
released or externally consumed. Existing feature private-format provenance is
unchanged from its retained inventory/review; this amendment introduces none.

No repository hook framework is declared, `core.hooksPath` is unset, and the
canonical hooks directory has sample hooks only. No hook was bypassed.
The original recovery-diagnostic input and six preserved-evidence hash manifests
still verify unchanged. No long test, provider/host/network action, lifecycle
mutation or queue/reservation action was performed by the member.

## Frozen committed deliverable

Final head: `0b403305e085aa01884cf56acea7c717f78f7e86`; registered runtime
worktree is clean. This head is committed locally and held from publication.
The lead directly applied the writing/Humanizer pass to the 11-line provider
guide addition; both requested wording edits are in the commit. Commit message
was read from `/tmp/provider-diagnostics-commit.txt`, all lines within 80 columns.
No hooks were bypassed.

Complete base-to-head series, with no merge or intermediate diagnostics commit:

| Commit | Parent | Logical scope |
| --- | --- | --- |
| `b8a6be26a75347dcc9ec0fd1330dff886e47c93f` | `ba8669b14536f72b559abc912bba8eac430111e4` | Existing complete attention/Web Push feature and inseparable webpush import/module/vendor closure; 36 files, +3349/-64; preserved byte-for-byte |
| `0b403305e085aa01884cf56acea7c717f78f7e86` | `b8a6be26a75347dcc9ec0fd1330dff886e47c93f` | Independent provider failure diagnostics and owning tests/docs; exact four assigned paths, +544/-18 |

Whole branch final diff: 40 files, +3893/-82. Detailed file inventory and both
complete commit messages/parents are in
`runtime-final-with-diagnostics-stat.txt` and
`runtime-final-with-diagnostics-series.txt`. No superseded pin or dependency
stream is introduced. The existing feature commit retains its original reviewed
history/packaging boundary. The separate diagnostics change repairs a later
demonstrated evidence gap and preserves that complete feature commit as directed.

Exact review artifacts and SHA256:

| Artifact | SHA256 |
| --- | --- |
| `provider-diagnostics-final.patch` — b8a6..0b403 | `b6a49b5a57f84d08932dae0572cbca861173ebae65a3133051ed3419db962f16` |
| `runtime-final-with-diagnostics.patch` — ba866..0b403 | `cb439bae3f28ad258a7d4572a8104278d495efcd4214a487ccb4d723d2e6801d` |
| `runtime-final-with-diagnostics-series.txt` | `db084f27236fb02ad8dc566f8a40627aad4eaff0ce7e6832210c4d826b0f94d0` |
| `runtime-final-with-diagnostics-stat.txt` | `b97317ec933b8cfc70481861dfcd3c34c28e7c0546d95b850a6352136356471b` |

`provider-diagnostics-freeze.json` records exact base/feature/head, four changed
paths and these hashes. Committed final and full-branch `git diff --check` pass.
Member post-copy Ruby syntax and Nix parse checks pass; no test rerun was needed
for the two approved wording changes.

The lead ran the complete focused Ruby file with no exclusion on the final code:
20 cases, 185 assertions, 0 failures/errors/skips, 1.118786 seconds, seed 38199.
Evidence: `provider-diagnostics-lead-ruby-final.log` and
`provider-diagnostics-lead-ruby-final.status` (exit 0). This resolves the member
socket-check gap without a product change. No long integration has run for this
new committed diagnostics deliverable; retained affected independent review is
the next lead-owned step before a fresh full recovery-VM watcher.

The original feature has no migration files. Its initial private notification
schema 1 and optional strict creation-receipt flag remain unchanged: omitted
old flags remain valid; new flagged receipts require the capable paired helper
and forward recovery. See `amended-final-inventory.md` and
`provider-disable-replacement-inventory.md` for retained feature lineage and
review. This diagnostics commit creates no private format or schema version,
no conversion and no externally consumed migration path. The earlier disposable
probes remain evidence, not supported product-state predecessors. No amendment
deployment, pin or live operation has occurred.

Lead owns session state/artifact registration, publication and the retained
affected committed review. Hold push and long tests. The original root cause
remains unproved after this amendment.

Session: <https://vpsfree-cz.workspace.aitherdev.int.vpsfree.cz/2026-10-14-i-d-like-the-dev-workspace/>

## Accepted review advisory: collection time bound

Retained final review of `bd60e37064ec4811a4686392bc9e83f0729ebcc1` found no
Blocking/Important findings. The lead accepted its one Advisory and directly
assigned the narrow timeout remedy under review steps 9/10; no reviewer rerun
or long test is requested. The amended owning diagnostics commit is now
`0b403305e085aa01884cf56acea7c717f78f7e86`, still directly parented by b8a6.
No other source or docs changes accompanied the remedy.

The three failure-collection commands now each call `machine.execute` with
`timeout=10`, bounding diagnostic command wait to at most 30 seconds excluding
driver overhead. The extracted fake machine requires/checks the timeout and
simulates a `TimeoutError`; both unexpected terminal assertions survive all
three collection timeouts unchanged. The canary never reaches output.

Exact reviewed-head-to-amended-head delta: two files, +8/-3, preserved in
`provider-diagnostics-timeout-remedy.patch`, SHA256
`8794f1e17786a3f60be9a62089c50b4280ea6279b29f3e79370f789546784b5a`.
Final member quick check: 19 cases, 183 assertions, 0 failures/errors/skips,
1.102004 seconds, seed 15830. Source/test Ruby syntax, Nix fixture parse and
committed narrow/full diff whitespace checks pass. Lead full Ruby check for
the amended head is pending; the previous 20/185 PASS above belongs to bd60.
Push and long checks remain held. No migration/provenance or original root-cause
conclusion changed. Frozen diagnostic/probe evidence remains unchanged.
